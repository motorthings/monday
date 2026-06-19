# Monday.com Phase 4 Output Generation Checklist

Quick-reference for generating deployable Monday.com configuration files. All the rules Phase 4 needs, none of the API reference.

## Board Creation (GraphQL Mutation)

```graphql
mutation {
  create_board(
    board_name: "Board Name"
    board_kind: public  # or private, shareable
    workspace_id: 12345678
    description: "Optional description"
  ) {
    id
    name
    url
  }
}
```

**board_kind**: `public` (visible to all members), `private` (invited only), `shareable` (link-based access)

## Column Creation Order

1. Create board first → get board ID
2. Create groups (sections within board)
3. Create columns within groups
4. Populate column values (if seeding data)

## Column Value JSON Formats

| Type | JSON Format | Example |
|------|-----------|---------|
| text | `"plain string"` | `"ACME Corp"` |
| numbers | `"123.45"` (stringified) | `"1500"` |
| status | `"{\"label\": \"In Progress\"}"` | Label must match defined options |
| dropdown | `"{\"label\": \"Option Name\"}"` | Single-select |
| date | `"{\"date\": \"2026-01-15\"}"` | ISO format date |
| timeline | `"{\"from\": \"2026-01-01\", \"to\": \"2026-03-31\"}"` | Date range |
| people | `"{\"personsAndTeams\": [{\"id\": 123, \"kind\": \"person\"}]}"` | User/team IDs |
| checkbox | `"{\"checked\": true}"` | Boolean |
| long_text | `"{\"text\": \"content\"}"` | Multi-line |
| email | `"{\"email\": \"user@example.com\", \"text\": \"optional label\"}"` | Email + display |
| phone | `"{\"phone\": \"+15551234567\", \"countryShortName\": \"US\"}"` | International format |
| link | `"{\"url\": \"https://...\", \"text\": \"Display Text\"}"` | URL + label |
| connect_boards | `"{\"item_ids\": [123456]}"` | Array of connected item IDs |
| mirror | Read-only, no value set | Reflects source |
| formula | Auto-computed, no value set | Defined in column config |
| progress | Auto-computed from status | Defined in column config |
| file | `"{\"file_id\": \"...\"}"` | Uploaded file reference |
| location | `"{\"lat\": 40.7128, \"lng\": -74.006, \"address\": \"NYC\"}"` | Coordinates + address |
| color_picker | `"{\"color\": \"#FF0000\"}"` | Hex color |
| tags | `"{\"tag_ids\": [1, 2, 3]}"` | Tag IDs |
| rating | `"{\"rating\": 4}"` | 0-5 integer |

**Clear a value**: send `"{}"` for JSON columns, `""` for text/number columns.
**Clear a file column**: send `"{\"clear_all\": true}"` — irreversible.

## Column Value Mutation

```graphql
mutation {
  change_column_value(
    item_id: 123456789
    board_id: 11223344
    column_id: "status"
    value: "{\"label\": \"Done\"}"
  ) {
    id
    name
  }
}
```

## Bulk Import Pattern

```graphql
mutation {
  create_item(board_id: 123, group_id: "topics", item_name: "Task 1") { id }
  create_item(board_id: 123, group_id: "topics", item_name: "Task 2") { id }
}
```

**Rate limit**: batch 100 items per mutation. For >100 items, split into multiple requests.

## Agent Configuration Schema

```json
{
  "agent_name": "string",
  "description": "string",
  "board_id": "numeric board ID",
  "agent_type": "sidekick" | "platform_mcp",
  "system_prompt": "full system prompt text",
  "tools": [
    {
      "name": "tool_name",
      "description": "what it does",
      "input_schema": { /* JSON Schema */ }
    }
  ],
  "trigger": {
    "type": "manual" | "scheduled" | "webhook" | "column_change",
    "config": { /* trigger-specific config */ }
  },
  "model": "claude-sonnet-4-5" | "gpt-4o" | etc.
}
```

## MCP Tools (for deployment)

| Tool | Purpose |
|------|---------|
| `create_board` | Create new board |
| `create_column` | Add column to board |
| `create_group` | Add group/section to board |
| `create_item` | Create item in board |
| `change_column_value` | Set column value on item |
| `list_boards` | List workspace boards |
| `list_workspaces` | List available workspaces |
| `list_users_and_teams` | Look up user/team IDs |
| `list_columns` | Get board column definitions |
| `query_items` | Search/retrieve items |
| `create_update` | Post update on item |
| `create_webhook` | Register webhook |
| `create_automation` | Set up automation |
| `upload_file` | Upload file to column |

## Dashboard Widgets (7 types)

| Widget | Use For |
|--------|---------|
| Chart | Visualize item counts by status/column |
| Number | Single KPIs (count, sum, average) |
| Battery | Progress toward target |
| Calendar | Date-based item view |
| Gantt | Timeline view from timeline columns |
| List View | Filtered/sorted item table |
| App Feature | Embedded app content |

## Querying Items (GraphQL)

```graphql
query {
  boards(ids: [123456]) {
    items(limit: 100) {
      id
      name
      column_values {
        id
        text
        value
      }
    }
  }
}
```

Filter: `items(query_params: {rules: [{column_id: "status", compare_value: ["Done"]}], operator: and})`

## Output Files — Phase 4 Must Generate

1. `board-schema.json` — Board name, groups, columns with types
2. `automations.json` — Trigger + action recipes
3. `create-board.gql` — GraphQL mutations to create the board
4. `create-columns.gql` — GraphQL mutations to add all columns
5. `dashboard-config.json` — Dashboard widgets and layouts
6. `agent-config.json` — AI agent configuration
7. `deployment-guide.md` — Step-by-step deploy instructions

## Key Constraints

- Column option values: lowercase, dashes, underscores only (no spaces)
- GraphQL mutations: all column values are JSON-encoded strings
- Board names: 255 char max
- Item names: no character limit but practical display at ~255
- Rate limits: Free 1K/day, Pro 10K/day, Enterprise 25K/day
- Complexity: 20M points/min all plans
- Agent memory: board-state only (items + columns), not conversation
- AI columns require Pro+ plan
- Max 5 private apps per account
