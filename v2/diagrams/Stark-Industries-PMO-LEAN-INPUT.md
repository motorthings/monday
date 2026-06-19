# Stark Industries PMO — LEAN MVP Spec v2 (verified against platform docs)
**Purpose:** Strip the v3 PRD down to only what the assignment text requires, then verify every mechanism against the actual monday.com docs the user supplied — not the OS's prior assumptions about the platform. Everything cut for scope is preserved as "Phase 2 / what I'd build next." Everything corrected below was wrong in v3 and silently inherited into the first lean draft; it's fixed here before being fed back into the EOS pipeline.

---

## Doc-verification notes (read first)

Checked against: `column-types.md`, `formulas.md`, `connect-boards.md`, `dashboards.md`, `ai-features.md`, `forms.md`.

1. **Progress Tracking column does NOT take a linked numeric source.** Per `column-types.md`: it's *"Calculated from all status columns on the board (weighted)."* It's a status-rollup mechanism, not a formula-fed gauge. v3's "SLA Completion % formula → linked Progress bar" design (Gap 4) doesn't match the platform. Fixed below using a Status-column-based progress approach instead.
2. **No single-date `WORKDAY()` offset function exists in the documented formula set.** Only `WORKDAYS({start},{end})` — a count *between* two dates — is listed. v3's At Risk Date / Escalation Date formulas (`WORKDAY({deadline}, -2)`) use a function that isn't in the reference. Fixed below using `ADD_DAYS` (documented) on the submission date instead of working backward from the deadline.
3. **Formulas cannot reference Mirror or Connect Boards columns** (`formulas.md`, explicit limitation). Confirmed — v3 was right to route around this. The fix (compute the formula on the source board, then Mirror the already-computed value across) is the correct pattern and is kept.
4. **Mirror-column-change CAN drive automations** (`connect-boards.md`: *"Use 'when column changes' trigger on mirror columns"*). Confirmed working as designed in v3.
5. **AI columns are more specific and more powerful than v3 used.** `ai-features.md` documents 8 distinct AI block types, including a **Categorize** block built exactly for "read free text, assign into an existing dropdown/status column" — a direct fit for Pepper's department-routing problem. v3 used a generic advisory-summary design instead. Upgraded below.

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

**On submission:** Creates a Portfolio Board item. AI Categorize column reads Business Problem and sets Department. Completeness Score formula evaluates immediately based on which required fields are populated. Routing automation fires based on the result.

---

## Tier 2: Portfolio Board

**Columns (10, not 27):**

| Column | Type | Purpose |
|---|---|---|
| Project name | Text | From form |
| Requestor / Department | Text / Dropdown | Department set by AI Categorize column, not manual entry — see AI tier below |
| Business problem | Long text | Source for AI column |
| Completeness Score | Formula | Deterministic field-check — drives routing. `IF(AND({Department}<>"",{Budget}<>"",{Timeline}<>""),"Complete","Incomplete")` style logic on required fields. This is the **one** formula that has to exist for the AI-vs-automation story to land. |
| Status | Status | Incomplete / Pending Review / Approved / Rejected |
| Assigned PM | People | Manual assignment |
| Submission Date | Date | Auto-set on form submit |
| Evaluation Deadline | Formula | `ADD_DAYS({Submission Date}, 5)` — documented function, computed once at submission, used for display and as the breach-automation comparison date. (Corrected from v3's WORKDAY-based approach, which used a function not in the documented formula set.) |
| SLA Status | Status | On Track / At Risk / Breached — manually visible, set by automation below. Doubles as a simple visual progress signal without depending on the Progress Tracking column's status-rollup mechanism, which doesn't support a formula-fed percentage the way v3 assumed. |
| Connected Execution Board | Connect Boards | Auto-populated on approval |

This hits the four named Advanced Column types (Progress Tracking, Due Date, Formula, Timeline) by using: a real Status-based Progress Tracking rollup driven by the Status column itself (e.g., a 4-stage Status column — Incomplete/Pending/Under Evaluation/Approved — naturally produces a weighted progress bar per the documented mechanism, no extra formula plumbing needed), the Evaluation Deadline as the Due Date use, the Completeness Score formula, and the project Timeline column. That's the "creative, out-of-the-box" requirement satisfied with mechanisms that are confirmed to work as documented, not assumed.

**Automations (4, not 9):**
1. Completeness Score = Complete → Status = Pending Review, notify Assigned PM
2. Completeness Score = Incomplete → Status = Incomplete, notify requestor
3. When Evaluation Deadline arrives + Status ≠ Approved/Rejected → SLA Status = Breached, notify PM and Pepper (single breach notification — your live "watch it fire" demo moment if you can land the deadline inside the trial window)
4. Status → Approved → create Execution Board from template, link via Connect Boards, notify PM

Cut from v3: separate At Risk Date / Escalation Date two-stage warning ladder (this depended on the unverified WORKDAY function — rebuild it as a Phase 2 item using `ADD_DAYS({Submission Date}, 3)` and `ADD_DAYS({Submission Date}, 4)` as two more simple formula columns once the core flow is proven live, since `ADD_DAYS` is confirmed in the docs). Also cut: unassigned-PM fallback automation, resubmission clock-restart logic. Explain these verbally as the next layer you'd add.

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

## Native AI requirement — upgraded from v3 using the documented AI block types

`ai-features.md` documents 8 distinct AI column block types, each purpose-built for a specific operation — not one general-purpose prompt box. The **Categorize** block type is a direct, named fit for Pepper's problem:

> *"Auto-categorize incoming project requests into departments (IT, Operations, HR) based on the request description."* — this exact use case is in the platform docs.

**Build this instead of v3's generic AI Summary column:**

- **AI block type:** Categorize
- **Target column:** Department (dropdown — IT / Operations / HR)
- **Source:** Business Problem (long text)
- **Additional instructions:** "Categorize this project request into the department most responsible for executing it, based on the described problem."

This is a stronger demo moment than v3's free-text advisory summary: you submit a vague request live, and the AI column **directly populates a structured dropdown field** that the rest of the board depends on — not a paragraph of prose that a human still has to read and translate into a field value. It's also a cleaner version of the "AI is advisory, automation is deterministic" story: the AI sets Department, the Completeness Score formula checks whether Department (among other fields) is populated, and the routing automation reads the formula. Each layer does one job, and each layer is confirmed to work the way the docs say it works.

**Optional second AI column if time allows:** Summarize block, target a Long Text "Executive Summary" column, source Business Problem — gives Pepper a one-line read instead of the raw submission text. Not required for the assignment's "one native AI feature" bar, but cheap to add and a good Q&A answer if asked "could you stack AI columns?"

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

## Why this version should be easier to actually finish — and actually work

v3 had 27 Portfolio columns, 9 formulas (two using an undocumented function and one mechanism that doesn't match how the column actually works), 9 automations, 5 widgets, 12 form fields, 10 pre-identified platform gaps to explain.

This version has 10 Portfolio columns, 1 core formula plus 1 deadline formula (both using documented functions), 4 automations, 4 widgets, 8 form fields — and every mechanism in it has been checked against `column-types.md`, `formulas.md`, `connect-boards.md`, `dashboards.md`, and `ai-features.md` rather than assumed.

Every cut item survives as a spoken answer. Nothing valuable is lost — it's relocated from "thing that can break live in a trial account" to "thing I can talk about fluently because I already thought it through." And nothing that remains in scope is resting on an unverified platform assumption anymore.
