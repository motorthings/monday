# Monday.com Fitness Checklist

Quick-reference scoring for Phase 0 fitness evaluation. All the rules the fitness check needs, none of the API reference.

## Scoring Rubric

Score each signal 0-10, compute weighted sum. Normalize to 0-10.

| Signal | Weight | What to check |
|--------|--------|---------------|
| Visual project tracking | 0.25 | Kanban boards, timelines, Gantt needed? |
| Structured data model | 0.20 | Defined columns (status, assignee, date, budget)? |
| Team coordination | 0.15 | Multiple people, assignments, handoffs? |
| Approval pipelines | 0.15 | Status stages with conditional routing? |
| External integrations | 0.10 | Slack, Gmail, Jira, GitHub connections? |
| Form-based input | 0.10 | Users submitting data via forms? |
| API-driven deployment | 0.05 | Programmatic deployment via API? |

**GO**: >= 6.5 — proceed
**CONDITIONAL**: 5.0-6.4 — viable with constraints
**FAIL**: < 5.0 — recommend alternative

## Mandatory FAIL Conditions

Any ONE is sufficient to fail:
- Real-time chat/conversational AI without board structure
- Persistent agent memory across conversations required (Monday is board-state based)
- High-frequency polling or sustained autonomous agent execution (complexity budget constrained)
- Pure unstructured document search with no structured data model
- Problem-solution fit is MISALIGNED (process change would solve it better)

## Anti-Patterns (Low-Fit Signals)

| Signal | Why |
|--------|-----|
| Real-time chat agents | Board-first, not chat-first |
| Pure Q&A without structure | No board data model to query |
| Workloads needing persistent agent memory | State in board columns only |
| Unstructured document search | Board/item focused search |
| High-frequency polling | Rate limits constrain call volume |
| Autonomous long-running agents | Complexity budgets limit sustained execution |

## Plan Tiers

| Plan | Daily Calls | Complexity/min | Queries/min |
|------|------------|----------------|-------------|
| Free | 1,000 | 5M (20M agents) | 1,000 |
| Pro | 10,000 | 5M (20M agents) | 2,500 |
| Enterprise | 25,000 | 5M (20M agents) | 5,000 |

AI columns require Pro+ plan.

## Key Constraints

- 24+ column types (status, date, people, dropdown, connect boards, formula, mirror, progress, etc.)
- 7 automation trigger types, ~10 action types
- 7 dashboard widget types (chart, number, battery, calendar, gantt, listview, app_feature)
- 23 form question types
- 8 AI block types (categorize, summarize, translate, improve_text, extract, open_block, write_me, person_assignment)
- 5 private apps per account max
- GraphQL API only — no REST
- Agent memory is board-state (items + column values), not conversation persistence
