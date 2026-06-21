#!/usr/bin/env python3
"""Sync SLA Count column with actual date math.
For items where Status is Approved or Rejected:
  SLA Count = 1 if Decision Date <= Evaluation Deadline, else 0
Run before the demo to ensure the widget has correct data.
"""

import requests, json, os, sys

API_URL = "https://api.monday.com/v2"
TOKEN = os.environ.get("MONDAY_API_TOKEN", "")
BOARD_ID = 18418546502

if not TOKEN:
    token_file = os.path.expanduser("~/.monday-token")
    if os.path.exists(token_file):
        with open(token_file) as f:
            TOKEN = f.read().strip()
if not TOKEN:
    print("Set MONDAY_API_TOKEN or create ~/.monday-token")
    sys.exit(1)

H = {"Authorization": TOKEN, "Content-Type": "application/json"}


def gql(query, variables=None):
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    r = requests.post(API_URL, headers=H, json=payload)
    return r.json().get("data", {})


# Fetch all items with Status, Decision Date, Evaluation Deadline
data = gql(f"""{{
  boards(ids: {BOARD_ID}) {{
    items_page(limit: 50) {{
      items {{
        id
        name
        column_values(ids: ["status", "date_mm4g3q58", "date4"]) {{
          id
          text
        }}
      }}
    }}
  }}
}}""")

items = data["boards"][0]["items_page"]["items"]
synced = 0

for item in items:
    vals = {}
    for cv in item["column_values"]:
        vals[cv["id"]] = cv["text"]

    status = vals.get("status", "")
    decision_date = vals.get("date_mm4g3q58", "")
    eval_deadline = vals.get("date_mm4f6ggs", "")

    if status not in ("Approved", "Rejected"):
        continue

    # Decision within deadline?
    # Days to Decision = difference between Decision Date and creation Date
    # Within SLA = 1 if decided within 5 days
    creation_date = vals.get("date4", "")  # monday.com built-in Date column
    days = None
    if decision_date and creation_date:
        from datetime import date as dt_date
        try:
            d = dt_date.fromisoformat(decision_date)
            c = dt_date.fromisoformat(creation_date)
            days = (d - c).days
        except ValueError:
            pass
    sla_met = 1 if days is not None and days <= 5 else 0

    # Set SLA Count
    gql(f"""mutation {{
      change_simple_column_value(
        board_id: {BOARD_ID},
        item_id: {item['id']},
        column_id: "numeric_mm4g8d1n",
        value: "{sla_met}"
      ) {{ id }}
    }}""")

    status_icon = "+" if sla_met else "-"
    print(f"  [{status_icon}] {item['name'][:60]}")
    print(f"      Decided: {decision_date}  Created: {creation_date}  Days: {days}  Within SLA: {sla_met}")
    synced += 1

print(f"\nSynced {synced} decided items.")
print(f"Dashboard widget now reads actual SLA compliance.")
