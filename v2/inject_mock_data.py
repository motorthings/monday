#!/usr/bin/env python3
"""Inject 6 Stark Industries mock project requests into the Intake Board via monday.com API."""

import requests
import json
import sys
import os
from datetime import date, timedelta

API_URL = "https://api.monday.com/v2"
TOKEN = os.environ.get("MONDAY_API_TOKEN", "")
INTAKE_BOARD_ID = 18418546502

if not TOKEN:
    # Fallback: read from file if env var not set
    token_file = os.path.expanduser("~/.monday-token")
    if os.path.exists(token_file):
        with open(token_file) as f:
            TOKEN = f.read().strip()
    if not TOKEN:
        print("Set MONDAY_API_TOKEN env var or create ~/.monday-token file")
        sys.exit(1)

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
}

def gql(query, variables=None):
    """Run a GraphQL query against the monday.com API."""
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    resp = requests.post(API_URL, headers=HEADERS, json=payload)
    data = resp.json()
    if "errors" in data:
        print(f"  GraphQL error: {json.dumps(data['errors'], indent=2)}", file=sys.stderr)
        return None
    return data.get("data", {})


def get_columns():
    """Fetch all columns from the Intake Board."""
    query = """
    query($boardId: [ID!]) {
      boards(ids: $boardId) {
        name
        columns {
          id
          title
          type
          settings_str
        }
      }
    }
    """
    data = gql(query, {"boardId": [str(INTAKE_BOARD_ID)]})
    if not data:
        return None, None
    board = data["boards"][0]
    print(f"Board: {board['name']}")
    cols = {}
    for c in board["columns"]:
        # Index by both ID and title
        entry = {"id": c["id"], "type": c["type"], "title": c["title"]}
        cols[c["id"]] = entry
        cols[c["title"]] = entry
        print(f"  {c['title']} ({c['type']}) -> {c['id']}")
    return board["name"], cols


def build_column_values(scenario, cols):
    """Build the column_values JSON string for a create_item mutation.

    Maps scenario fields to monday.com column IDs (not titles, since titles
    can be ambiguous). The item name is NOT set here — it goes in item_name.
    """
    # Column ID → scenario key  (reverse-engineered from the board query)
    # Skipping: name (item name), person (people-type, misconfigured),
    #   formula columns (computed), board_relation (Connect Boards), mirror
    id_map = {
        # Text fields
        "text_mm4fznkh": scenario.get("requestor_name", ""),       # Requestor Name
        "long_text_mm4fckbc": scenario.get("business_problem", ""), # Business Problem
        "long_text_mm4f5g7w": scenario.get("success_criteria", ""), # Success Criteria
        # Email
        "email_mm4fhrpf": scenario.get("requestor_email", ""),      # Requestor Email
        # Dropdowns
        "dropdown_mm4fhx3b": scenario.get("department", ""),        # Department Name
        "dropdown_mm4fb697": scenario.get("budget", ""),             # Estimated Budget Range
        # Dates
        "date_mm4f5d7x": scenario.get("timeline", ""),               # Desired Timeline
        "date_mm4f6ggs": scenario.get("evaluation_deadline", ""),    # Evaluation Deadline
        # Status — set "Incomplete" as default; automations handle the rest
        "status": {"label": scenario.get("status", "Incomplete")},
    }

    # Serialize values for each column ID
    values = {}
    for col_id, raw_value in id_map.items():
        if col_id not in cols:
            print(f"  WARNING: Column ID '{col_id}' not found, skipping")
            continue

        col_type = cols[col_id]["type"]

        if col_type in ("text", "long_text", "dropdown"):
            values[col_id] = raw_value if raw_value else ""
        elif col_type == "email":
            if raw_value:
                values[col_id] = {"email": raw_value, "text": raw_value}
            else:
                values[col_id] = {}
        elif col_type == "status":
            values[col_id] = raw_value if isinstance(raw_value, dict) else {"label": str(raw_value)}
        elif col_type == "date":
            if raw_value:
                values[col_id] = {"date": str(raw_value)}
            # omit if empty — don't set a date

    return json.dumps(values)


def create_item(scenario, cols):
    """Create a single item on the Intake Board."""
    item_name = scenario.get("name", "Untitled Request")
    column_values = build_column_values(scenario, cols)

    mutation = """
    mutation($boardId: ID!, $itemName: String!, $columnValues: JSON!) {
      create_item(
        board_id: $boardId,
        item_name: $itemName,
        column_values: $columnValues
      ) {
        id
        name
      }
    }
    """

    data = gql(mutation, {
        "boardId": str(INTAKE_BOARD_ID),
        "itemName": item_name,
        "columnValues": column_values,
    })

    if data and "create_item" in data:
        item = data["create_item"]
        print(f"  ✅ Created: {item['name']} (id: {item['id']})")
        return item
    return None


# ── 6 Stark Industries Mock Scenarios ──────────────────────────────────────

_today = date.today()
_days = timedelta  # shorthand

SCENARIOS = [
    {
        "name": "Arc Reactor Cooling System Upgrade",
        "requestor_name": "Tony Stark",
        "requestor_email": "tony@starkindustries.com",
        "department": "IT",
        "business_problem": "The Arc Reactor cooling subsystem is running at 94% capacity during peak load. If it fails, Tower power goes offline. We need to upgrade the cooling infrastructure with redundant chillers and a predictive thermal monitoring system to prevent catastrophic failure.",
        "budget": "$200k+",
        "timeline": (_today + _days(30)).isoformat(),
        "evaluation_deadline": (_today + _days(5)).isoformat(),
        "success_criteria": "Cooling capacity below 70% at peak load; automated failover tested; thermal alerts integrated with JARVIS monitoring dashboard.",
        "status": "Incomplete",
    },
    {
        "name": "Warehouse Optimization Project",
        "requestor_name": "Pepper Potts",
        "requestor_email": "pepper@starkindustries.com",
        "department": "Operations",
        "business_problem": "We have too much stuff in the warehouse and people can't find things quickly. Need a better system for tracking inventory.",
        "budget": "Unknown",
        "timeline": (_today + _days(45)).isoformat(),
        "evaluation_deadline": (_today + _days(5)).isoformat(),
        "success_criteria": "",
        "status": "Incomplete",
    },
    {
        "name": "Annual Safety Certification Rollout",
        "requestor_name": "Happy Hogan",
        "requestor_email": "happy@starkindustries.com",
        "department": "HR",
        "business_problem": "OSHA safety certifications for all R&D staff expire at end of Q3. 340 employees across 3 facilities need re-certification. Current process uses paper sign-off sheets and takes 6 weeks. Need a digital workflow to track completion, flag non-compliant staff, and auto-generate compliance reports for the safety committee.",
        "budget": "$50k-200k",
        "timeline": (_today + _days(14)).isoformat(),
        "evaluation_deadline": (_today + _days(5)).isoformat(),
        "success_criteria": "All 340 staff re-certified by Q3 end; digital audit trail for OSHA; auto-escalation for overdue certificates; dashboard for safety committee.",
        "status": "Incomplete",
    },
    {
        "name": "JARVIS Natural Language Interface v2",
        "requestor_name": "Bruce Banner",
        "requestor_email": "bruce@starkindustries.com",
        "department": "IT",
        "business_problem": "JARVIS NLU module has a 23% misinterpretation rate on compound queries involving lab equipment commands. Need to retrain the model on domain-specific corpus and add context-aware intent resolution.",
        "budget": "",
        "timeline": "",
        "evaluation_deadline": (_today + _days(5)).isoformat(),
        "success_criteria": "",
        "status": "Incomplete",
    },
    {
        "name": "Supply Chain Disruption Response — Palladium Sourcing",
        "requestor_name": "Pepper Potts",
        "requestor_email": "pepper@starkindustries.com",
        "department": "Operations",
        "business_problem": "Our primary palladium supplier in South Africa declared force majeure after mine flooding. Current stockpile covers 18 days of production. Need immediate alternative sourcing strategy, supplier qualification, and logistics rerouting plan.",
        "budget": "$200k+",
        "timeline": (_today + _days(2)).isoformat(),
        "evaluation_deadline": (_today + _days(1)).isoformat(),  # Tomorrow — SLA pressure test
        "success_criteria": "Alternative supplier qualified and first shipment en route within 5 business days; no production line stoppage; cost impact analysis for Pepper's review.",
        "status": "Incomplete",
    },
    {
        "name": "Office Ping Pong Tournament",
        "requestor_name": "Clint Barton",
        "requestor_email": "clint@starkindustries.com",
        "department": "HR",
        "business_problem": "Morale has been low since the last alien invasion. A company-wide ping pong tournament would boost spirits and build cross-department camaraderie. Need bracket management, trophy procurement, and snack budget.",
        "budget": "Under $50k",
        "timeline": (_today + _days(60)).isoformat(),
        "evaluation_deadline": (_today + _days(5)).isoformat(),
        "success_criteria": "At least 50 participants; cross-department teams; documented morale improvement.",
        "status": "Incomplete",
    },
]


def main():
    print("=" * 60)
    print("  Stark Industries PMO — Mock Data Injection")
    print("=" * 60)

    # Step 1: Get columns
    print("\n📋 Fetching board columns...")
    board_name, cols = get_columns()
    if not cols:
        print("❌ Failed to fetch columns. Check token and board ID.")
        sys.exit(1)

    print(f"\n📊 Board: {board_name}")
    print(f"📊 Columns found: {len(cols)}")

    # Step 2: Create items
    print(f"\n🚀 Injecting {len(SCENARIOS)} mock project requests...\n")
    created = []
    for i, scenario in enumerate(SCENARIOS, 1):
        print(f"[{i}/6] {scenario['name']}")
        item = create_item(scenario, cols)
        if item:
            created.append(item)
        else:
            print(f"  ❌ Failed to create: {scenario['name']}")

    print(f"\n{'=' * 60}")
    print(f"  ✅ Created {len(created)}/{len(SCENARIOS)} items")
    print(f"  Board: {board_name}")
    print(f"  URL: https://motorthingss-team.monday.com/boards/{INTAKE_BOARD_ID}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
