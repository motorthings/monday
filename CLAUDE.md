# CLAUDE.md — monday.com Implementation Consultant Interview Build

## What This Is

Interview assignment for a monday.com Implementation Consultant role. Building a PMO intake-to-execution system for a fictional "Stark Industries" using the monday.com platform. 30-minute demo + 30-minute live Q&A where they'll ask for on-the-fly prototyping.

**Evaluated on:** architectural instincts, consultative thinking, AI-as-working-tool (not talking point)

## Repo Structure

```
monday/
├── CLAUDE.md                          ← This file
├── assignment - notes.md               ← My analysis: what they're evaluating, build architecture, 30-min presentation structure, Q&A prep
├── Implementation Consultant Task - 2026.pdf  ← The original assignment PDF from monday.com
├── platform-docs/                      ← Scraped monday.com developer docs (see manifest.json for source index)
│   ├── platform-reference.md           ← API basics, MCP tools reference
│   ├── column-types.md                 ← All column types available
│   ├── formulas.md                     ← Formula functions and syntax
│   ├── automations-triggers.md / automation-actions.md  ← Workflow automation reference
│   ├── connect-boards.md               ← Connect Boards column mechanics
│   ├── dashboards.md                   ← Dashboard widget types
│   ├── forms.md                        ← Form creation and configuration
│   ├── ai-features.md                  ← Native monday AI features (AI columns, etc.)
│   ├── build-with-ai.md                ← Building on monday with AI
│   ├── mcp-tools.md                    ← Platform MCP tools (programmatic board creation, etc.)
│   ├── capabilities.md                 ← Platform capability overview
│   └── ...                             ← Full dev docs surface
└── v2/                                 ← Build execution and conversation history
    ├── claude-project-chat.md          ← THE CANONICAL CONVERSATION — full Claude Code chat history for this project (699 lines, ongoing)
    ├── Stark-Industries-PMO-LEAN-INPUT.md  ← The LEAN MVP spec — deliberately stripped to only what the assignment requires
    └── diagrams/                       ← visual-explainer HTML output + monday.com UI screenshots
```

## The Architecture (LEAN MVP — what we're actually building)

**4-tier connected system:**

| Tier | What | Status |
|------|-------|--------|
| Intake Form | 8-field form → creates Portfolio item, triggers AI column | **Stage 2 (next)** |
| Portfolio Board | PM strategic view — 10 columns, 1 formula, 4 automations, Connect Boards to Execution | **Stage 1 done (board created)** |
| Execution Board | Tactical — Sprint 1/Sprint 2 groups, Status-based, structured DIFFERENTLY from Portfolio | **Stage 1 done (board created)** |
| Executive Dashboard | 4 widgets: Portfolio Health, SLA Compliance, Active Projects Table, Department Load | **Stage 4** |

**Key constraint:** Everything in the build traces to a line in the assignment text. Everything else becomes a verbal "what I'd build next" Q&A answer.

## Key Architectural Decisions

1. **AI/Formula separation pattern** — AI column does the fuzzy work (summarize, categorize), one formula does deterministic completeness check. Two distinct layers. This is the insight to demo live.
2. **WORKDAY-based date logic** — monday.com daily formulas can't trigger automations. WORKDAY arithmetic via formula → date column → automation is the fix. Understanding this limitation IS the platform fluency signal.
3. **"Structured differently"** — Execution Board uses group-based sprint structure (Sprint 1/Sprint 2) vs. Portfolio's Status-based pipeline. This deliberate contrast satisfies the assignment requirement directly.
4. **One SLA breach automation, not a multi-stage ladder** — fires at the deadline. Explain the 2-day warning, escalation, and At Risk → Escalation → Breach ladder verbally.

## Build Stages & Diagrams

Each stage produces both a build artifact AND a visual artifact. The diagrams capture process, not just product — they're demo material for the interview, showing how you think through architecture.

| Stage | Build | Diagram | Status |
|-------|-------|---------|--------|
| Stage 0 | Project setup, repo, CLAUDE.md | **Architecture Overview** — 4-tier system map (Intake → Portfolio → Execution → Dashboard) | ✅ Done |
| Stage 1 | Boards created in monday.com workspace | **Board Structure Map** — what was created, column/group layout, connection points | ✅ Done |
| Stage 2 | Intake form | **Intake Flow** — form fields → submission → what happens next | ✅ Done |
| Stage 3 | Columns + automations (Portfolio + Execution) | **Automation Flow Diagram** — triggers, conditions, actions across both boards | ✅ Done |
| Stage 4 | Dashboard | **Dashboard Widget Map** — 4 widgets, data sources, what each proves | ✅ Done |
| Stage 5 | AI column + completeness formula | **AI/Formula Separation Pattern** — fuzzy vs. deterministic, why both layers matter | ✅ Done |
| Stage 6 | Connect Boards + mirror back-link | **Connected Architecture** — data flow across tiers, what rolls up vs. what stays local | ⬜ Next |
| Stage 7 | Mock data population (Stark Industries) | **Demo Scenario Map** — the narrative arc the mock data tells | ⬜ |
| Stage 8 | Demo dry-run + Q&A prep | **Demo Flow Map** — 30-min presentation structure, key talking points per tier | ⬜ |
| Stage 9 | Final polish | **Process Retrospective** — before/after: overbuilt PRD vs LEAN MVP, what we chose and why | ⬜ |

## Working in This Repo

**Continuity is in `v2/claude-project-chat.md`.** Every Claude Code session is appended there. Always read the tail of that file first when picking up work — the current state, last actions taken, and next stage are at the end.

**Platform docs are reference, not instruction.** The `platform-docs/` tree is scraped from developer.monday.com. Use them to look up column types, formula syntax, automation capabilities, etc. when building. The `manifest.json` maps each doc to its source URL.

**The LEAN spec (`v2/Stark-Industries-PMO-LEAN-INPUT.md`) is the build spec.** It's the traceability-filtered version that maps every column, automation, and widget back to the assignment text. The original overbuilt PRD (27 columns, 9 formulas) was deliberatly cut down — the full version survives as Q&A talking points only.

**The assignment notes (`assignment - notes.md`) are the presentation strategy.** Structure for the 30-minute demo, Q&A prep, what AI did vs. what human judgment did.

### Diagrams

**Use the `/visual-explainer` skill for all diagrams.** Output lands in `v2/diagrams/`. Each diagram is a self-contained HTML file — open in browser, screenshot for the interview deck.

**Why this matters for the interview:**

- Shows you used AI as a working tool to think through architecture, not just build
- Each diagram is a slide-ready artifact for the "AI walkthrough" portion of the demo
- The before/after comparison (overbuilt PRD → LEAN MVP) directly demonstrates "consultative thinking" — you identified scope creep and made deliberate cuts
- Process diagrams prove you didn't just build — you architected

**Diagram conventions:**
- File naming: `stage-N-description.html` (e.g., `stage-2-intake-flow.html`)
- Each diagram includes a caption explaining what it captures and why the decision mattered
- Screenshots of the actual monday.com build go alongside diagrams in `v2/diagrams/`

## Current State (as of last session)

- Workspace "Stark Industries PMO" created in monday.com trial account
- Three boards exist: Portfolio Board, Execution Board, Intake Board
- Execution Board: groups renamed to Sprint 1/Sprint 2, sample items cleared, Status labels set to To Do / In Progress / Blocked / Done
- Stage 1 verified complete
- Form live at `forms.monday.com/forms/479b794a383233e17a99854cbeb536cd` — 8 fields, matches LEAN spec
- Automation 3 (deadline breach → notify Assigned PM) live. Automations 1/2/4 deferred to Stage 5/6
- **Next: Stage 6 — Connect Boards + mirror back-link**

## Self-Check Loop

After each build stage:
1. Build the thing in monday.com UI → screenshot
2. Generate the diagram via `/visual-explainer` → save to `v2/diagrams/`
3. Verify against the LEAN spec
4. Append findings + screenshot + diagram reference to `v2/claude-project-chat.md`
5. Mark stage complete, confirm next stage
