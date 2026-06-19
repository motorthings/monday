# Monday.com Connect Boards & Mirror Columns

## Overview

Two mechanisms link data across boards:
1. **Connect Boards column** — Links items between boards
2. **Mirror column** — Displays values from linked items on other boards

Together they create connected, multi-tier board architectures (e.g., Portfolio → Project → Task).

## Connect Boards Column

**Column type:** `board_relation`
**Implementation type:** `BoardRelationValue`
**Supported operations:** Read, Filter, Create, Update, Clear

### Reading Connect Boards Values

```graphql
query {
  items(ids: [1234567890]) {
    column_values {
      ... on BoardRelationValue {
        id
        display_value
        linked_item_ids
        linked_items {
          id
          name
        }
        updated_at
      }
    }
  }
}
```

Key fields:
- `display_value` — Comma-separated linked item names
- `linked_item_ids` — Array of linked item IDs
- `linked_items` — Full item objects (query any Item field)
- `text` and `value` — Always null for this column; use the fields above

### Get Connected Board IDs

```graphql
query {
  connection_board_ids(connection_id: "1234567890")
}
```

Returns all board IDs linked to a specific connect boards column. API version 2026-07+ requires `connection_id` argument (was `connectionId` in earlier versions).

### Creating a Connect Boards Column

```graphql
mutation {
  create_column(
    board_id: 1234567890
    title: "Related Projects"
    column_type: board_relation
    defaults: {
      boardIds: [9876543210]
      allowMultipleItems: true
      allowCreateReflectionColumn: true
    }
  ) {
    id
    title
    type
  }
}
```

| defaults Argument | Type | Description |
|-------------------|------|-------------|
| boardIds | [Int] | Target board IDs; at least one required |
| allowMultipleItems | Boolean | Allow linking multiple items (default: true) |
| allowCreateReflectionColumn | Boolean | Auto-create mirror column on target board (default: false) |

When `allowCreateReflectionColumn` is true, a corresponding column is auto-created on the target board for a two-way relationship.

### Linking Items (Writing)

Use `change_multiple_column_values` — `change_simple_column_value` is NOT supported.

```graphql
mutation {
  change_multiple_column_values(
    item_id: 9876543210
    board_id: 1234567890
    column_values: "{\"connect_boards\": {\"item_ids\": [1122334455, 5544332211]}}"
  ) {
    id
  }
}
```

JSON format:
```json
{"connect_boards": {"item_ids": [1122334455, 5544332211]}}
```

### Setting on Item Creation

```graphql
mutation {
  create_item(
    board_id: 1234567890
    item_name: "New Project"
    column_values: "{\"connect_boards\": {\"item_ids\": [1122334455]}}"
  ) {
    id
    name
  }
}
```

### Clearing

```json
{"connect_boards": null}
```

### Filtering

| Operator | Compare Value | Behavior |
|----------|--------------|----------|
| any_of | [item_ids] | Items connected to any of the specified linked items |
| not_any_of | [item_ids] | Excludes items connected to specified linked items |
| contains_text | "string" | Linked item name contains text |
| not_contains_text | "string" | No linked item name contains text |
| is_empty | [] | No linked items |
| is_not_empty | [] | Has at least one linked item |

## Mirror Column

Displays values from a connected board through a linked item. Read and create only — no update, clear, or filter.

**Column type:** `mirror`
**Implementation type:** `MirrorValue`

### Reading Mirror Values

```graphql
query {
  items(ids: [1234567890]) {
    column_values {
      ... on MirrorValue {
        id
        display_value
        mirrored_items {
          linked_item { id name }
          mirrored_value {
            ... on StatusValue { label index }
            ... on TextValue { text }
            ... on NumbersValue { number }
            ... on DateValue { date time }
          }
        }
      }
    }
  }
}
```

### Creating a Mirror Column

```graphql
mutation {
  create_column(
    board_id: 1234567890
    title: "Project Status"
    column_type: mirror
    defaults: "{\"settings\": {\"relation_column\": {\"connect_boards_column_id\": true}, \"displayed_linked_columns\": [{\"board_id\": \"9876543210\", \"column_ids\": [\"status\", \"timeline\"]}]}}"
  ) {
    id
    title
    type
    settings
  }
}
```

| Setting | Description |
|---------|-------------|
| relation_column | Maps a connect boards column ID to true — which column's links to mirror |
| displayed_linked_columns | Array of {board_id, column_ids} — which columns to mirror from linked items |
| sumType | For status: "doneOnly" or "allStatuses" |
| calcType | For dates: "earliestToLatest", "earliest", "latest" |

## Multi-Tier PMO Architecture Pattern

```
Portfolio Board
  ├── Column: "Projects" (Connect Boards → Project Board)
  ├── Column: "Status" (Mirror → Project Board status)
  ├── Column: "Health" (Mirror → Project Board health)
  ├── Column: "Timeline" (Mirror → Project Board timeline)
  └── Column: "Budget" (Mirror → Project Board budget)

Project Board
  ├── Column: "Tasks" (Connect Boards → Task Board)
  ├── Column: "Status" (Status)
  ├── Column: "Health" (Formula — from task completion)
  ├── Column: "Timeline" (Timeline)
  └── Column: "Budget" (Numbers)

Task Board
  ├── Column: "Assignee" (People)
  ├── Column: "Status" (Status)
  └── Column: "Sprint" (Connect Boards → Sprint Board)
```

## Automation with Connect Boards

When an item is linked via a Connect Boards column, automations can:
- Create items on connected boards automatically
- Mirror status changes across boards
- Trigger notifications when linked items change
- Use "when column changes" trigger on mirror columns

## Object Relations (API v2026-04+)

For board-to-board and dashboard-to-board relationships at the object level:

```graphql
mutation {
  create_object_relations(
    source_object_id: "1234567890"
    relations: [{
      kind: DEPENDENCY
      target_id: "9876543210"
      target_object_type: BOARD
    }]
  ) {
    id
    target_id
  }
}
```

Relation kinds: `DEPENDENCY` or `ALIAS`
Target types: `BOARD` or `DASHBOARD`
