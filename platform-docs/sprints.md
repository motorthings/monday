# Monday.com Sprints & Milestones

## Overview

Monday.com supports sprint planning and milestone tracking through:
- **Sprints Boards** — Dedicated sprint management view
- **Timeline/Milestone columns** — Visual date tracking
- **Sprint metadata** — Sprint details via Platform MCP
- **Dependency columns** — Task dependencies within sprints

## Platform MCP Sprint Tools

### get_sprints_boards
Returns all boards configured with sprint support in the account.

### get_sprints_metadata
Returns sprint configuration details for a board, including sprint durations, active sprint, and sprint settings.

### get_sprint_summary
Returns a summary of the current sprint including completion status, item counts, and burndown metrics.

## Timeline Column as Milestone

Timeline columns support milestone mode — `visualization_type: "milestone"` when set as a milestone instead of a date range.

### Setting a Milestone
```graphql
mutation {
  change_multiple_column_values(
    item_id: 9876543210
    board_id: 1234567890
    column_values: "{\"timeline\": {\"from\": \"2026-03-15\", \"to\": \"2026-03-15\"}}"
  ) {
    id
  }
}
```

A timeline with identical `from` and `to` dates displays as a milestone point.

### Creating a Timeline Column with Milestone Option
```graphql
mutation {
  create_column(
    board_id: 1234567890
    title: "Milestone"
    column_type: timeline
    defaults: "{\"settings\": {\"show_set_as_milestone\": true}}"
  ) {
    id
    title
    settings
  }
}
```

## Dependency Column

Links tasks with dependencies (blocked by, depends on).

**Column type:** `dependency`
**Implementation type:** `DependencyValue`

### Creating a Dependency Column
```graphql
mutation {
  create_column(
    board_id: 1234567890
    title: "Depends On"
    column_type: dependency
  ) {
    id
  }
}
```

### Reading Dependencies
```graphql
query {
  items(ids: [1234567890]) {
    column_values {
      ... on DependencyValue {
        id
        display_value
        linked_item_ids
        linked_items {
          id
          name
        }
      }
    }
  }
}
```

## Sprint Planning Pattern (PMO Use Case)

### Sprint Board Configuration

```
Board: "Q2 Development Sprints"
Groups: Sprint 1, Sprint 2, Sprint 3, Backlog

Columns:
├── Task (Name)
├── Assignee (People)
├── Status (Status): To Do → In Progress → Review → Done
├── Story Points (Numbers)
├── Sprint (Dropdown): Sprint 1, Sprint 2, Sprint 3
├── Due Date (Date)
├── Milestone (Timeline, milestone mode)
├── Depends On (Dependency)
└── Progress (Progress Tracking)
```

### Sprint Views

- **Kanban View** — Columns by Status, filter by current sprint
- **Timeline View** — Gantt-style view of all sprint tasks by date
- **Workload View** — Capacity planning by assignee

## Progress Tracking for Sprint Burndown

The Progress column auto-calculates from Status columns. For a sprint board with a single status column having labels: To Do (0%), In Progress (50%), Review (75%), Done (100%) — each weighted equally by default.

Weight configuration via column settings:
```json
{
  "related_columns": {
    "isNormalized": true,
    "columns": {
      "status": {"isSelected": true, "percentage": 50},
      "review_status": {"isSelected": true, "percentage": 50}
    }
  }
}
```

## Filtering by Sprint

```graphql
query {
  boards(ids: 1234567890) {
    items_page(
      query_params: {
        rules: [{
          column_id: "sprint_dropdown"
          compare_value: ["Sprint 2"]
          operator: any_of
        }]
      }
    ) {
      items { id name }
    }
  }
}
```

## SLA Tracking with Timeline + Formula

### Days Remaining Pattern
```
// Formula column referencing a timeline column:
IF(DAYS(TODAY(), {milestone_date}) >= 0, 
   CONCATENATE(TEXT(DAYS(TODAY(), {milestone_date})), " days left"),
   CONCATENATE(TEXT(ABS(DAYS(TODAY(), {milestone_date}))), " days overdue"))
```

### Milestone Countdown
```
IF({progress} == 100, "COMPLETE",
   IF(DAYS(TODAY(), {due_date}) < 0, "OVERDUE",
      IF(DAYS(TODAY(), {due_date}) <= 2, "DUE SOON", "ON TRACK")))
```
