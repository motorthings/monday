# Monday.com Phase 2 Workflow Design Checklist

Quick-reference for designing board schemas, automations, and integrations. All the rules Phase 2 needs, none of the API reference.

## Column Types (24+ total — pick the right one)

| Use Case | Column Type | Notes |
|----------|------------|-------|
| Item title (required, exactly 1 per board) | `name` | Default, always present |
| Multi-line text, descriptions | `long_text` | Use for notes, instructions |
| Single-line text, IDs, codes | `text` | Short values |
| State transitions, pipelines | `status` | Label = value. Lowercase, dashes, underscores only |
| Person assignment | `people` | Accepts user/team IDs |
| Dates, deadlines | `date` | Include time component if needed |
| Numbers, budgets, hours | `numbers` | Decimal supported |
| Dropdown single-select | `dropdown` | Define option values upfront |
| Yes/no, toggles | `checkbox` | Boolean |
| Board-to-board links | `connect_boards` | Two-way relationship |
| Mirror from connected board | `mirror` | Read-only copy of connected column |
| Calculated values | `formula` | Functions: ADD_DAYS, DAYS, IF, CONCAT, etc. |
| Progress bar (auto) | `progress` | Auto-calculated from status columns |
| Time tracking | `time_tracking` | Start/stop timer |
| Gantt date range | `timeline` | Start date → end date |
| File attachments | `file` | Uploaded files |
| Email address | `email` | Validates format |
| Phone number | `phone` | Validates format |
| Location | `location` | Address or coordinates |
| External links | `link` | URL with optional display text |
| Voting | `vote` | Up/down votes |
| Rating | `rating` | Star rating |
| Tags | `tags` | Multi-select labels |
| Color picker | `color_picker` | Hex color |
| Auto-numbering | `auto_number` | Sequential IDs |

**Option naming constraint**: lowercase letters, numbers, dashes, underscores only. NO spaces, NO special characters.

## Automation Triggers (7 types)

| Trigger | Use When |
|---------|----------|
| When a column changes | Status updates, field modifications |
| When an item is created | New submissions, intake |
| When a date arrives | Deadlines, reminders, follow-ups |
| At a scheduled time | Recurring tasks, daily reports |
| When a form is submitted | External intake |
| When a status changes to... | Specific state transitions |
| When button is clicked | User-initiated actions |

## Automation Actions (~10 types)

| Action | What It Does |
|--------|-------------|
| Notify someone | Send notification via email/in-app |
| Change status | Update item status |
| Move item to board | Transfer between boards |
| Create item | Generate new item in specified board |
| Update column value | Set/modify any column |
| Send email | External email (via Gmail/Outlook integration) |
| Create update | Post an update on the item |
| Assign person | Set/change assignee |
| Webhook | Call external URL |
| Duplicate item | Clone item with/without updates |

## Board Connection Patterns

| Pattern | How | Use Case |
|---------|-----|----------|
| One-to-many (parent→child) | `connect_boards` on child board | Portfolio→Project→Task |
| Mirror reference | `mirror` column reads from connected board | Display parent status on child |
| Two-way sync | `connect_boards` + `mirror` on both boards | Bidirectional visibility |
| Aggregate rollup | `formula` on parent summing connected items | Portfolio budget from projects |

## Form Capabilities

- 23 question types (text, dropdown, date, file upload, etc.)
- Responses create items in target board
- Conditional logic: show/hide questions based on prior answers
- Custom branding: logo, colors, welcome message
- File upload size limit: 500MB

## Formula Functions (commonly used)

| Function | Example |
|----------|---------|
| ADD_DAYS(date, n) | `ADD_DAYS({created}, 5)` |
| DAYS(date1, date2) | `DAYS({due}, TODAY())` |
| IF(cond, then, else) | `IF({priority}="High", "URGENT", "Normal")` |
| CONCAT(a, b, ...) | `CONCAT({first}, " ", {last})` |
| TODAY() | Current date |
| SUM(values) | Sum connected items |
| COUNT(values) | Count connected items |
| AVERAGE(values) | Average connected items |
| MIN/MAX(values) | Min/max connected items |

## AI Features (Pro+ required)

| Feature | What It Does |
|---------|-------------|
| AI Column — Categorize | Classify items into categories |
| AI Column — Summarize | Condense long text |
| AI Column — Translate | Language translation |
| AI Column — Improve Text | Grammar/style improvement |
| AI Column — Extract | Pull structured data from text |
| AI Column — Write Me | Generate content from prompt |
| AI Column — Person Assignment | Auto-assign based on content |
| Sidekick Tool | Custom AI tool for board actions |
| Platform MCP Agent | External AI agent (Anthropic, etc.) connected via MCP |

## Key Constraints

- GraphQL API only — no REST
- Column option values: lowercase, dashes, underscores only
- Board names: 255 char max
- Item limit: no hard cap but performance degrades past ~100K
- Automation execution: 30 second timeout per run
- Formula character limit: 10,000 chars
- File upload: 500MB max
