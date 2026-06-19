# Monday.com Platform Capabilities

## Platform Overview

Monday.com is a Work OS — a composable platform combining boards, automations, integrations, and AI agents into visual workflows. Unlike Glean (which is agent-first), Monday.com is board-first: data lives in structured boards with typed columns, automations react to changes, and agents operate within that data model.

## Architecture

```
Workspaces → Boards → Groups → Items → Subitems
                 ↓
            Columns (24+ typed columns per board)
                 ↓
            Views (Table, Kanban, Timeline, Gantt, Calendar, Chart)
                 ↓
       Automations (Triggers → Conditions → Actions)
                 ↓
       AI Agents (Sidekick tools, external agents, managed providers)
```

## Trigger Types

| Trigger | Description |
|---------|-------------|
| `item_created` | New item added to board |
| `column_changed` | A column value changes |
| `date_arrived` | A date column reaches its value |
| `webhook_received` | External webhook payload |
| `form_submitted` | WorkForm submission |
| `chat_message` | User message in agent chat |
| `schedule` | Recurring time-based trigger |
| `button_clicked` | Button column clicked |

## Strengths

- **Visual workflow management** — boards, views, and automations are visible and configurable by non-technical users
- **24+ column types** — Status, People, Date, Dropdown, Connect Boards, Numbers, Timeline, Formula, etc.
- **Rich automation engine** — triggers, conditions, and actions compose into complex workflows
- **MCP programmability** — Platform MCP server enables AI agents to create boards, items, columns, and more via API
- **Integration ecosystem** — native connectors for Slack, Gmail, GitHub, Jira, Salesforce, Zendesk, etc.
- **Monday-code hosting** — deploy custom serverless apps within Monday's infrastructure
- **Agent accounts** — AI agents can be first-class platform participants with their own seats
- **GraphQL API** — single endpoint (`api.monday.com/v2`) for all operations

## Constraints

- **Rate limits by plan tier**: Free (1K calls/day), Pro (10K/day), Enterprise (25K/day)
- **Complexity budgets**: 20M points/min for all plans; reads and writes have separate budgets
- **5 private apps per account**: Cap on custom monday-code apps
- **No persistent agent memory**: State lives in board items and columns, not in a conversation context
- **Agent memory is board-state**: Agents read/write column values rather than maintaining conversation history
- **GraphQL only**: No REST API — all operations are GraphQL queries and mutations
- **API versioning via header**: `Api-Version: 2026-07`
- **8,000 char limit per update**: Long content must be split across updates or stored in documents
- **Column value format**: Each column type has a specific JSON structure that must be respected

## Best-Fit Signals

Score these signals 0-10 when evaluating a PRD against Monday.com. Weight by stated importance.

| Signal | Weight | Description |
|--------|--------|-------------|
| Visual project tracking | 0.25 | The use case requires kanban boards, timelines, or Gantt charts |
| Structured data model | 0.20 | The workflow has defined columns (status, assignee, date, etc.) |
| Team coordination | 0.15 | Multiple people collaborate on items with assignments and handoffs |
| Approval pipelines | 0.15 | Items flow through status stages with conditional routing |
| External integrations | 0.10 | The agent connects to Slack, Gmail, Jira, GitHub, etc. |
| Form-based input | 0.10 | Users submit structured data via forms to trigger workflows |
| API-driven deployment | 0.05 | The solution should be deployable programmatically via API |

## Anti-Patterns (Low-Fit Signals)

| Signal | Reason |
|--------|--------|
| Real-time chat agents | Monday.com is not a chat platform — items and updates, not conversations |
| Pure Q&A without structure | No board data model to query — low value from the platform |
| Workloads needing persistent agent memory | No built-in memory between agent invocations — state must be in board columns |
| Unstructured document search | Monday.com search is board/item focused, not full-content search like Glean |
| High-frequency polling | Rate limits constrain API call volume |
| Autonomous long-running agents | Complexity budgets limit sustained agent execution |

## Scoring Rubric

For each best-fit signal, score 0-10 based on PRD content:
- 0-2: Signal absent or contradicted
- 3-5: Signal weakly present
- 6-8: Signal clearly present
- 9-10: Signal is the primary use case driver

Weighted formula: `sum(signal_score * weight) / sum(weights)` then normalize to 0-10.

**Go threshold**: >= 6.5 — proceed with Monday.com build
**Conditional**: 5.0-6.4 — viable but significant constraints or missing signals
**Fail**: < 5.0 — poor fit; recommend alternative platform

## Deployment Surfaces

| Surface | Description |
|---------|-------------|
| Monday.com board | Primary interface — items, columns, views |
| Monday.com dashboard | Widgets aggregating board data |
| Slack integration | Automations can post to Slack channels |
| Email notifications | Automations can email on triggers |
| WorkForms | Public or internal form submissions |
| API/MCP | Programmatic access for external agents |
| Monday-code app | Custom UI hosted within Monday.com |

## Model / AI Capabilities

- **Sidekick**: Monday's native digital agent — can invoke custom Sidekick tools
- **External agents**: Connect Claude, GPT, or custom agents via managed provider or webhook
- **Agent accounts**: Programmatic signup creates agent as platform user
- **AI credits**: Consumption tracked under account usage dashboard
- **No model selection**: Agents use Monday's default model; no per-agent model override
