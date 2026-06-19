# Monday.com Column Types Reference

## Overview

Monday.com has 39 column types across four categories. All column values are retrieved through the `column_values` field on items. Every implementation type inherits from the `ColumnValue` interface providing four shared fields: `id`, `text`, `type`, `value`.

Type-specific fields require GraphQL inline fragments (e.g., `... on StatusValue`, `... on NumbersValue`).

## How to Set Values

Two mutations:
- **change_simple_column_value** — Accepts a string value (simpler, but limited)
- **change_multiple_column_values** — Accepts a JSON object (supports all types)

The expected format varies by column type — see each type's section below.

## Supported Columns (Read + Write)

| Column | Type Enum | Implementation | Value Format |
|--------|-----------|----------------|--------------|
| Button | button | ButtonValue | Click trigger |
| Checkbox | checkbox | CheckboxValue | `{"checked": "true"}` |
| Color Picker | color_picker | ColorPickerValue | Hex color code |
| **Connect Boards** | board_relation | BoardRelationValue | `{"item_ids": [123, 456]}` |
| Country | country | CountryValue | Country code |
| **Date** | date | DateValue | `{"date": "YYYY-MM-DD", "time": "HH:MM:SS"}` |
| Dependency | dependency | DependencyValue | Item dependencies |
| **Dropdown** | dropdown | DropdownValue | Label IDs or text |
| Email | email | EmailValue | `{"email": "..."}` |
| Files | file | FileValue | Asset IDs |
| Hour | hour | HourValue | `{"hour": 9, "minute": 0}` |
| Link | link | LinkValue | `{"url": "...", "text": "..."}` |
| Location | location | LocationValue | `{"lat": N, "lng": N, "address": "..."}` |
| Long Text | long_text | LongTextValue | `{"text": "..."}` |
| Monday Doc | doc | DocValue | Doc ID reference |
| Name | name | (none) | Item title string |
| **Numbers** | numbers | NumbersValue | `{"number": 42}` or number string |
| **People** | people | PeopleValue | `{"personsAndTeams": [{"id": N, "kind": "person"}]}` |
| Phone | phone | PhoneValue | `{"phone": "..."}` |
| Rating | rating | RatingValue | `{"rating": 3}` |
| **Status** | status | StatusValue | `{"index": N}` or `{"label": "Text"}` |
| Subitems | subtasks | SubtasksValue | Child items |
| Tags | tags | TagsValue | `{"tag_ids": [N]}` |
| Text | text | TextValue | `{"text": "..."}` or plain string |
| **Timeline** | timeline | TimelineValue | `{"from": "YYYY-MM-DD", "to": "YYYY-MM-DD"}` |
| Time Tracking | time_tracking | TimeTrackingValue | Duration |
| Vote | vote | VoteValue | Vote count |
| Week | week | WeekValue | `{"week": {"startDate": "...", "endDate": "..."}}` |
| World Clock | world_clock | WorldClockValue | Timezone |

## Key Column Value Formats (Quick Reference)

### Status
```json
// Read: value = {"index": 1}
// Write by ID: {"status_column_id": {"index": 1}}
// Write by label: {"status_column_id": {"label": "Done"}}
// Clear: {"status_column_id": null}
// Simple: value: "1" (by index) or "Done" (by label)
```

Important: The mutation key is `"index"` but the value passed is the label's **stable id**, NOT its display position.

### Date
```json
// Write with time: {"date_col": {"date": "2026-06-15", "time": "09:00:00"}}
// Write date only: {"date_col": {"date": "2026-06-15"}}
// Simple: value: "2026-06-15" or "2026-06-15 09:00:00"
// Clear: {"date_col": null} or value: ""
```
Times in UTC. API response converts to caller's timezone.

### Numbers
```json
// Write: {"numbers_col": 42} or value: "42"
// Clear: {"numbers_col": null}
```

### People
```json
// Write: {"people_col": {"personsAndTeams": [{"id": 12345, "kind": "person"}]}}
// Clear: {"people_col": null}
```

### Timeline
```json
// Write: {"timeline_col": {"from": "2026-03-01", "to": "2026-03-15"}}
// Clear: {"timeline_col": null} or {"timeline_col": {}}
```
change_simple_column_value is NOT supported for timeline.

### Connect Boards
```json
// Write: {"connect_boards_col": {"item_ids": [1122334455, 5544332211]}}
// Clear: {"connect_boards_col": null}
```
change_simple_column_value is NOT supported. text and value fields always return null — use display_value and linked_item_ids instead.

### Dropdown
```json
// Write by ID: {"dropdown_col": {"ids": [1, 3]}}
// Write by label: {"dropdown_col": {"labels": ["Option A", "Option B"]}}
```

### Long Text
```json
// Write: {"long_text_col": {"text": "Multi-line content here"}}
// Simple: value: "..." (plain string)
```

## Read-Only Columns

These return values through the API but cannot be written to — auto-generated or derived:

| Column | Type Enum | Implementation | Notes |
|--------|-----------|----------------|-------|
| Creation Log | creation_log | CreationLogValue | Auto-generated creation metadata |
| **Formula** | formula | FormulaValue | Computed; read via display_value |
| Item ID | item_id | ItemIdValue | Auto-generated unique ID |
| Last Updated | last_updated | LastUpdatedValue | Auto-tracked modification time |
| **Mirror** | mirror | MirrorValue | Reflects values from connected board |
| **Progress Tracking** | progress | ProgressValue | Percentage from status columns |

### Formula Values
Read via `display_value` field. `text` is empty, `value` is null. Cannot filter or update. Max 5 formula columns per request, 10K values/minute.

### Progress Tracking Values
Calculated from all status columns on the board (weighted). `value` always returns null. Filter by thresholds: 0, 20, 50, 80, 100 (represent "at least X% complete").

### Mirror Values
Read via `mirrored_items` array — each contains `linked_item` and `mirrored_value` (union type — use inline fragments).

## Calculated Columns (Not API-Accessible)

| Column | Type Enum | Notes |
|--------|-----------|-------|
| Auto Number | auto_number | Computed at render time; NOT accessible via API |

## Deprecated Columns

| Column | Type Enum | Replacement |
|--------|-----------|-------------|
| Person | person | People column |
| Team | team | People column |

## Creating Columns

```graphql
mutation {
  create_column(
    board_id: 1234567890
    title: "Priority"
    column_type: status
    defaults: "{\"settings\":{\"labels\":[{\"label\":\"High\",\"color\":\"stuck_red\",\"index\":0},{\"label\":\"Medium\",\"color\":\"working_orange\",\"index\":1},{\"label\":\"Low\",\"color\":\"done_green\",\"index\":2}]}}"
  ) {
    id
    title
    type
  }
}
```

Two typed mutations exist:
- **create_status_column** — Status with label/color config
- **create_dropdown_column** — Dropdown with predefined options

All other column types use the generic `create_column` with `column_type` argument.

## Column Type Schema Discovery

Retrieve JSON schema for any column type:
```graphql
query {
  get_column_type_schema(type: status)
}
```

## PMO Board Column Patterns

### Intake Board
| Column | Type | Purpose |
|--------|------|---------|
| Request Name | name | Item title |
| Description | long_text | Request details |
| Department | dropdown | IT, Operations, HR |
| Priority | status | High, Medium, Low |
| Requested By | people | Who submitted |
| Date Submitted | date | When submitted |
| SLA Deadline | formula | `ADD_DAYS({date_submitted}, 5)` |
| Status | status | New, Reviewing, Approved, Rejected |

### Portfolio Board
| Column | Type | Purpose |
|--------|------|---------|
| Project Name | name | Item title |
| Department | mirror → Intake | From connected intake item |
| Project Lead | people | Assigned PM |
| Status | status | Planning, Active, At Risk, Complete |
| Health | formula | From project metrics |
| Timeline | timeline | Start to end |
| Budget | numbers | Total budget |
| Projects | connect_boards | Link to project boards |

### Project Board
| Column | Type | Purpose |
|--------|------|---------|
| Task | name | Item title |
| Assignee | people | Task owner |
| Status | status | To Do, In Progress, Done, Blocked |
| Sprint | dropdown | Sprint 1, Sprint 2, etc. |
| Due Date | date | Deadline |
| Effort | numbers | Story points or hours |
| Progress | progress | Auto-calculated from status |
