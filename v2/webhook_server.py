#!/usr/bin/env python3
"""monday.com webhook receiver — syncs SLA Count when Status changes.
Receives webhook from Intake Board, reads Decision Date vs Evaluation Deadline,
writes SLA Count back to the item via GraphQL API.

Usage:
  python3 webhook_server.py              # starts on port 8080
  ngrok http 8080                        # in another terminal
  # Register the ngrok URL in monday.com → Board → Integrations → Webhooks
"""

import os, sys, json, logging
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

API_URL = "https://api.monday.com/v2"
BOARD_ID = 18418546502
TOKEN = os.environ.get("MONDAY_API_TOKEN", "")

if not TOKEN:
    token_file = os.path.expanduser("~/.monday-token")
    if os.path.exists(token_file):
        with open(token_file) as f:
            TOKEN = f.read().strip()
if not TOKEN:
    print("Set MONDAY_API_TOKEN or create ~/.monday-token")
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger("webhook")


def gql(query):
    r = requests.post(
        API_URL,
        headers={"Authorization": TOKEN, "Content-Type": "application/json"},
        json={"query": query},
    )
    return r.json().get("data", {})


def process_item(item_id, pulse_id):
    """Read decision dates from the item, calculate SLA, write back."""
    # Fetch item column values
    data = gql(
        f"""{{
      items(ids: [{item_id}]) {{
        name
        column_values(ids: ["status", "date_mm4g3q58", "date_mm4f6ggs"]) {{
          id text
        }}
      }}
    }}"""
    )

    items = data.get("items", [])
    if not items:
        log.error(f"Item {item_id} not found")
        return

    item = items[0]
    vals = {cv["id"]: cv["text"] for cv in item["column_values"]}

    status = vals.get("status", "")
    decision_date = vals.get("date_mm4g3q58", "")
    eval_deadline = vals.get("date_mm4f6ggs", "")

    if status not in ("Approved", "Rejected"):
        log.info(f"  {item['name']}: Status={status} — not decided, skipping")
        return

    sla_met = 1 if decision_date and eval_deadline and decision_date <= eval_deadline else 0

    gql(
        f"""mutation {{
      change_simple_column_value(
        board_id: {BOARD_ID},
        item_id: {item_id},
        column_id: "numeric_mm4g8d1n",
        value: "{sla_met}"
      ) {{ id }}
    }}"""
    )

    icon = "+" if sla_met else "X"
    log.info(f"  [{icon}] {item['name']}: {decision_date} <= {eval_deadline} → SLA={sla_met}")


class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")

        # monday.com sends a challenge on initial registration
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            return

        challenge = payload.get("challenge")
        if challenge:
            log.info(f"Webhook challenge received: {challenge}")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"challenge": challenge}).encode())
            return

        log.info(f"Webhook fired: {json.dumps(payload, indent=2)[:500]}")

        # Process the event
        event = payload.get("event", {})
        pulse_id = event.get("pulseId", 0)
        item_id = event.get("pulseId", 0)  # pulseId = item ID

        if item_id:
            process_item(int(item_id), int(pulse_id))

        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"SLA webhook alive\n")

    def log_message(self, format, *args):
        pass  # suppress default HTTP logging


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = HTTPServer(("0.0.0.0", port), WebhookHandler)
    log.info(f"Webhook server listening on port {port}")
    log.info("Register in monday.com: Board → Integrations → Webhooks")
    log.info(f"URL: https://your-ngrok-url.ngrok.io")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        log.info("Shutting down")
        server.shutdown()
