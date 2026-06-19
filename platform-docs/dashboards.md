# Monday.com Dashboards & Widgets

## Overview

Dashboards aggregate and visualize data from one or more boards via widgets (charts, counters, timelines, calendars, etc.). Every dashboard connects to 1-50 boards at creation time. Widgets draw data from those connected boards.

## Dashboard Architecture

```
Dashboard
  ├── Connected Boards (1-50)
  ├── Widget 1 → Chart: Budget by Department
  ├── Widget 2 → Battery: Overall Project Health
  ├── Widget 3 → Number: Total Active Projects
  └── Widget 4 → Table: Projects at Risk
```

## create_dashboard (Platform MCP)

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| name | string | Yes | UTF-8 display name |
| workspace_id | string | Yes | Owning workspace |
| board_ids | array | Yes | 1-50 board IDs as strings |
| kind | string | No | PUBLIC or PRIVATE (default: PUBLIC) |
| board_folder_id | string | No | Folder placement |

### GraphQL Equivalent

```graphql
mutation {
  create_board(
    board_name: "Executive Dashboard"
    board_kind: public
    workspace_id: 12406666
    board_type: dashboard
  ) {
    id
    name
    url
  }
}
```

## create_widget (Platform MCP)

Adds visualization widgets to dashboards. Always call `all_widgets_schema` first.

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| parent_container_id | string | Yes | Dashboard or board view ID |
| parent_container_type | string | Yes | DASHBOARD or BOARD_VIEW |
| widget_kind | string | Yes | Widget type (see below) |
| widget_name | string | Yes | 1-255 UTF-8 characters |
| settings | object | No | Widget-specific JSON config |

### Widget Types (7)

| Type | Purpose |
|------|---------|
| CHART | Bar, line, pie charts; configurable x/y axes |
| NUMBER | Single counter/aggregate value |
| BATTERY | Visual battery indicator (good for health/status) |
| CALENDAR | Calendar view of dated items |
| GANTT | Gantt chart for timeline visualization |
| LISTVIEW | Tabular list of items |
| APP_FEATURE | Embed an app feature |

### NUMBER Widget Settings

```json
{
  "counter_data": {
    "calculation_type": "count",
    "column_ids_per_board": {"board_id": []},
    "counter_type": "sum"
  }
}
```

### CHART Widget Settings

Requires: `graph_type` (enum of chart types), `x_axis_columns`, `y_axis_columns`

### GraphQL Equivalent

```graphql
mutation {
  create_widget(
    board_id: 37055164
    widget_type: number
    name: "Active Projects"
    settings: "{\"counter_data\":{\"calculation_type\":\"count\",\"counter_type\":\"sum\"}}"
  ) {
    id
    name
    type
  }
}
```

Key difference: GraphQL uses `board_id` (no parent_container_type), `widget_type` (lowercase), and settings as an escaped JSON string.

## all_widgets_schema

Returns the complete JSON Schema (draft-07) for all widget types. Takes no parameters. Must be called before `create_widget` — using wrong settings shape causes widget creation to fail.

## Executive Dashboard Pattern (PMO Use Case)

For Pepper's steering committee needs, a typical dashboard:

```
Dashboard: "PMO Executive Overview"
Connected Boards: [Portfolio Board ID]

Widget 1 — BATTERY: Overall Portfolio Health
  → Maps to a status rollup column

Widget 2 — NUMBER: Total Active Projects
  → count of non-completed items on Portfolio board

Widget 3 — CHART: Projects by Department
  → bar chart, x_axis=department dropdown, y_axis=count

Widget 4 — TABLE: Projects Requiring Attention
  → filtered list of overdue or at-risk items
```

## Dashboard Configuration Tips

- Connect all relevant boards at dashboard creation time
- Use Battery widgets for health/status overviews (executive-friendly)
- Use Number widgets for KPI counters (budget total, project count)
- Use Chart widgets for breakdowns (by department, by status, by timeline)
- Table widgets can show filtered lists with specific columns
- Up to 50 boards per dashboard — plan board connections before widget creation
