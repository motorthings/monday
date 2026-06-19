# Stark Industries PMO — LEAN MVP Spec (for EOS re-run)
**Purpose:** Strip the v3 PRD down to only what the assignment text requires, so the EOS pipeline can be re-run against a deliberately constrained input and checked for convergence. Everything cut here is preserved as "Phase 2 / what I'd build next" — not deleted, just not in the build.

---

## Hard scope boundary

**In scope (assignment says so explicitly):**
1. Intake Form
2. Portfolio Board (PM strategic view, fed from below)
3. One Execution Board (tactical, structured differently from Portfolio)
4. Executive Dashboard — exactly 3-4 widgets
5. SLA tracking using Advanced Columns: Progress Tracking, Due Date, Formula, Timeline
6. Connect Boards + automations linking the tiers
7. One native monday AI feature, applied to the "vague request" problem
8. Verbal identification (not necessarily build) of 1-2 implicit bottlenecks Pepper didn't name

**Explicitly out of scope for the build — reserved as spoken Q&A answers only:**
- Duplicate detection
- Budget-threshold approval routing to Finance
- Requestor self-service portal
- GraphQL-based archive for rejected items
- Slack integration
- Multi-stage SLA escalation ladder (At Risk → Escalation → Breach as three separate automations)
- Mirror-driven health automation with separate Blocked Count tracking

This list is a feature, not an omission — it's the answer to "what would you do with more time," which the assignment explicitly invites in Part 2.

---

## Tier 1: Intake Form

**Fields (8, not 12):**

| Field | Type | Required |
|---|---|---|
| Project name | Short text | Yes |
| Requestor name | Short text | Yes |
| Requestor email | Email | Yes |
| Department | Dropdown: IT / Operations / HR | Yes |
| Business problem | Long text | Yes |
| Estimated budget range | Dropdown: Under $50K / $50–200K / $200K+ / Unknown | Yes |
| Desired timeline | Date | Yes |
| Success criteria | Long text | No |

Cut from v3: Request type, Intended scope, Key stakeholders, Supporting documents. These are nice-to-haves; none are referenced by name in the assignment, and each is one more thing to explain in a 30-minute window.

**On submission:** Creates a Portfolio Board item. AI column runs. One completeness formula sets initial routing.

---

## Tier 2: Portfolio Board

**Columns (10, not 27):**

| Column | Type | Purpose |
|---|---|---|
| Project name | Text | From form |
| Requestor / Department | Text / Dropdown | From form |
| Business problem | Long text | Source for AI column |
| AI Summary | AI column | Native AI requirement — restates problem, flags missing info, suggests category |
| Completeness Score | Formula | Deterministic field-check — drives routing. This is the **one** formula that has to exist for the AI-vs-automation story to land. |
| Status | Status | Incomplete / Pending Review / Approved / Rejected |
| Assigned PM | People | Manual assignment |
| Evaluation Deadline | Date | Set to TODAY()+5 when Status → Pending Review |
| SLA Progress | Progress Tracking | Linked to a single Days-Elapsed-vs-5 formula — satisfies the "Progress Tracking" advanced-column requirement directly |
| Timeline | Timeline | Project start → target completion — satisfies the "Timeline" advanced-column requirement directly |
| Connected Execution Board | Connect Boards | Auto-populated on approval |

This hits all four named Advanced Column types (Progress Tracking, Due Date [Evaluation Deadline], Formula, Timeline) with **one purpose-built formula**, not nine. That's the "creative, out-of-the-box" requirement satisfied at MVP weight.

**Automations (4, not 9):**
1. Completeness Score ≥ threshold → Status = Pending Review, set Evaluation Deadline = TODAY()+5, notify Assigned PM
2. Completeness Score < threshold → Status = Incomplete, notify requestor
3. Evaluation Deadline arrives + Status ≠ Approved/Rejected → notify PM and Pepper (single breach notification — this is your live "watch it fire" moment if you can make the deadline land during the demo window)
4. Status → Approved → create Execution Board from template, link via Connect Boards, notify PM

Cut from v3: separate At Risk Date / Escalation Date two-stage warning ladder, unassigned-PM fallback automation, resubmission clock-restart logic. All correct ideas — explain them verbally as the next layer you'd add ("right now this fires once at the deadline; with another day I'd add a 2-day-out warning using the same WORKDAY pattern").

---

## Tier 3: Execution Board

**Groups:** To Do / In Progress / Blocked / Done — simpler than the 5-phase template in v3, and it's a real *visible* structural contrast to the Portfolio Board's Status-based pipeline, which is the actual requirement ("structured differently").

**Columns (6, not 12):**

| Column | Type |
|---|---|
| Task name | Text |
| Assigned to | People |
| Status | Status (To Do / In Progress / Blocked / Done) |
| Due date | Date |
| Sprint | Dropdown |
| Connected portfolio item | Connect Boards |

Cut from v3: Percent Complete formula, Blocked Count formula, Dependencies, Effort, Priority, Notes. The mirror-health automation that depended on these is cut too — explain it verbally as the natural Phase 2 extension once the connection itself is proven live.

---

## Tier 4: Executive Dashboard

**Exactly 4 widgets — matches the assignment's stated ceiling:**

1. **Portfolio Health** — Chart, Status column breakdown across all requests
2. **SLA Compliance** — Number widget, simple % of Approved/Rejected items where Decision Date ≤ Evaluation Deadline
3. **Active Projects Table** — Table view of Approved items: name, PM, status, timeline
4. **Department Load** — Bar chart, request volume by department

Cut from v3: Last Refreshed timestamp widget (good idea, explain verbally — "in production I'd add a staleness indicator here").

---

## Native AI requirement — unchanged from v3, this part was already right

AI Summary column on the Portfolio Board, reading Business Problem, producing: restated problem, implied scope/department, missing info, suggested category. This is exactly what the assignment asks for ("AI columns... to automatically process or structure messy requests") and doesn't need to be bigger than this.

---

## What you say out loud but don't build

Use the existing "what she didn't say but needs" framing from the v3 discovery work — it's good, keep all of it as talking points:
- Triage/scoring layer beyond completeness
- Multi-stage SLA escalation
- Duplicate detection
- Budget approval routing
- Requestor visibility portal
- GraphQL-based archive

This is literally what Part 2 of the assignment is asking you to demonstrate — that you can articulate next steps and defend scope choices live, not that you pre-built all of them.

---

## Why this version should be easier to actually finish

v3 had 27 Portfolio columns, 9 formulas, 9 automations, 5 widgets, 12 form fields, 10 pre-identified platform gaps to explain.
This version has 10 Portfolio columns, 1 core formula, 4 automations, 4 widgets, 8 form fields.

Every cut item survives as a spoken answer. Nothing valuable is lost — it's relocated from "thing that can break live in a trial account" to "thing I can talk about fluently because I already thought it through."
