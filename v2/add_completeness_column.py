"""Add AI Completeness column to Intake Board.

Uses Open Block AI column type with a custom prompt that judges
whether a project request has enough information to proceed.
"""

import os
import sys
import json
import requests

# ── Auth ──────────────────────────────────────────────────────────
TOKEN = os.environ.get("MONDAY_API_TOKEN", "")
if not TOKEN:
    token_file = os.path.expanduser("~/.monday-token")
    if os.path.exists(token_file):
        with open(token_file) as f:
            TOKEN = f.read().strip()
if not TOKEN:
    print("Set MONDAY_API_TOKEN env var or create ~/.monday-token file")
    sys.exit(1)

URL = "https://api.monday.com/v2"
HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
    "API-Version": "2026-10",
}
INTAKE_BOARD_ID = 18418546502


def graphql(query, variables=None):
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    r = requests.post(URL, json=payload, headers=HEADERS)
    data = r.json()
    if "errors" in data:
        print(f"GraphQL errors: {json.dumps(data['errors'], indent=2)}")
        return None
    return data.get("data")


def get_columns(board_id):
    """Fetch all columns for a board, returning {title: id} mapping."""
    query = """
    query($board_id: [ID!]) {
      boards(ids: $board_id) {
        columns {
          id
          title
          type
          settings_str
        }
      }
    }
    """
    data = graphql(query, {"board_id": [str(board_id)]})
    if not data:
        return {}
    columns = {}
    for col in data["boards"][0]["columns"]:
        columns[col["title"]] = {
            "id": col["id"],
            "type": col["type"],
        }
    return columns


def create_text_column(board_id, title):
    """Create a text column on the board. Returns column ID."""
    mutation = """
    mutation($board_id: ID!, $title: String!) {
      create_column(board_id: $board_id, title: $title, column_type: long_text) {
        id
        title
      }
    }
    """
    data = graphql(mutation, {"board_id": str(board_id), "title": title})
    if data:
        return data["create_column"]["id"]
    return None


def configure_open_block_ai(board_id, column_id, ai_query):
    """Configure an Open Block AI column."""
    mutation = """
    mutation($board_id: ID!, $column_id: ID!, $ai_query: String!) {
      configure_open_block_ai_column(
        board_id: $board_id
        column_id: $column_id
        ai_query: $ai_query
      ) {
        column_id
      }
    }
    """
    data = graphql(mutation, {
        "board_id": str(board_id),
        "column_id": column_id,
        "ai_query": ai_query,
    })
    return data


def main():
    print("Fetching Intake Board columns...")
    cols = get_columns(INTAKE_BOARD_ID)

    if not cols:
        print("Failed to fetch columns. Check token and board ID.")
        sys.exit(1)

    print(f"Found {len(cols)} columns:")
    for title, info in sorted(cols.items()):
        print(f"  {title:40s}  id={info['id']:30s}  type={info['type']}")

    # Find the column IDs we need to reference
    business_problem_id = None
    for title, info in cols.items():
        if "business" in title.lower() and "problem" in title.lower():
            business_problem_id = info["id"]
            break

    if not business_problem_id:
        print("\nCould not find 'Business Problem' column.")
        print("Available columns:", list(cols.keys()))
        sys.exit(1)

    print(f"\nBusiness Problem column ID: {business_problem_id}")

    # Check if AI Completeness column already exists
    if "AI Completeness" in cols:
        print("\n'AI Completeness' column already exists. Updating AI config...")
        column_id = cols["AI Completeness"]["id"]
    else:
        print("\nCreating 'AI Completeness' column...")
        column_id = create_text_column(INTAKE_BOARD_ID, "AI Completeness")
        if not column_id:
            print("Failed to create column.")
            sys.exit(1)
        print(f"Created column: {column_id}")

    # Find additional column IDs for richer context
    budget_id = None
    timeline_id = None
    success_id = None
    for title, info in cols.items():
        if "budget" in title.lower():
            budget_id = info["id"]
        elif "timeline" in title.lower() and "desired" in title.lower():
            timeline_id = info["id"]
        elif "success" in title.lower():
            success_id = info["id"]

    # Build pulse references
    refs = f"{{pulse.{business_problem_id}}}"
    extras = []
    if budget_id:
        extras.append(f"Budget: {{pulse.{budget_id}}}")
    if timeline_id:
        extras.append(f"Timeline: {{pulse.{timeline_id}}}")
    if success_id:
        extras.append(f"Success Criteria: {{pulse.{success_id}}}")

    extra_context = "\n".join(extras)

    # Configure the Open Block AI
    ai_query = (
        f"Analyze this project request and determine if it contains enough information "
        f"for a PM to evaluate it.\n\n"
        f"Business Problem: {refs}\n"
        f"{extra_context}\n\n"
        "Judge completeness on these criteria:\n"
        "1. Is the problem clearly stated, or is it too vague to understand what's needed?\n"
        "2. Is there enough context to know the scope and urgency?\n"
        "3. Would a PM need to ask follow-up questions before they could decide?\n\n"
        "Output EXACTLY one of these two responses:\n"
        "- COMPLETE — the request has enough information to evaluate\n"
        "- INCOMPLETE: [specific reason — be specific about what's missing and what the "
        "requestor should provide]\n\n"
        "Be strict: if a PM would need to guess or ask clarifying questions, the request is INCOMPLETE."
    )

    print(f"\nAI query ({len(ai_query)} chars):")
    print(ai_query[:200] + "...")

    print(f"\nConfiguring Open Block AI on column {column_id}...")
    result = configure_open_block_ai(INTAKE_BOARD_ID, column_id, ai_query)

    ai_result = result.get("configure_open_block_ai_column") if result else None
    if ai_result and ai_result.get("column_id"):
        print("\n✅ AI Completeness column configured successfully.")
        print(f"   Column ID: {ai_result['column_id']}")
        print(f"\nNext steps:")
        print("1. Verify the column in the monday.com UI")
        print("2. Add an automation:")
        print("   - Trigger: When AI Completeness changes")
        print("   - Condition: AI Completeness contains 'INCOMPLETE'")
        print("   - Action: Send email/update to requestor with the AI Completeness text")
    else:
        print("\n❌ Failed to configure AI column.")
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
