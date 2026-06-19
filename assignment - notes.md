### What They're Actually Evaluating

Seth told you directly: not monday.com expertise, but how you analyze requirements and how AI shows up in your approach. This prompt confirms it. Three things they're watching for:

**1. Architectural instincts.** Can you read Pepper's email, identify what she actually needs vs. what she said, and build a connected multi-tier system that solves the real problem?

**2. Consultative thinking.** "Read between the lines" is explicit in the instructions. What didn't Pepper ask for that she needs?

**3. AI as a working tool, not a talking point.** They want you to document your prompts, show your iteration, and explain where AI helped and where it didn't. This is your home court.

---

### What Pepper Actually Needs (Reading Between the Lines)

She asked for intake, SLA tracking, and an executive dashboard. Here's what she didn't ask for but needs:

- **A triage and scoring layer.** Requests come in vague. Someone needs to evaluate them against criteria before the 5-day clock runs out. An AI column that auto-scores or categorizes incoming requests on impact, department, and completeness is the implicit ask.
- **Automated SLA escalation.** A 5-day SLA that "just sits around" means no one is getting notified when the clock is running. Automations that fire at day 3 and day 5 are the fix.
- **Separation of PM view vs. exec view.** She's manually pulling data from spreadsheets into PowerPoint. The connected boards architecture solves this structurally — the exec dashboard should require zero manual work from Pepper.
- **Standardized request quality.** Vague requests are the root cause of her downstream problems. The intake form needs required fields and an AI layer that flags incomplete submissions before they enter the pipeline.

---

### The Build Architecture

**Tier 1: Intake Form**  
Public-facing monday.com form capturing: request name, department, requestor, description, estimated scope, budget range, impacted teams, desired timeline. Required fields enforce completeness upfront. AI column on intake board auto-categorizes request type (IT, Ops, HR) and generates a structured summary from the vague description. This is where native monday AI earns its place.

**Tier 2: Portfolio Board (PM view)**  
One row per project. Connected to intake via Connect Boards column. Shows: project status, department, assigned PM, timeline, budget, SLA countdown, health indicator. This is the strategic overview — PMs manage from here. SLA tracking lives here: formula column calculating days since submission, timeline column showing the 5-day window, progress tracking showing evaluation stage.

**Tier 3: Day-to-Day Project Board(s)**  
Task-level execution. Subitems or separate board with sprints, milestones, assignees, due dates. Connected up to the Portfolio board via mirror columns so status rolls up automatically. This is where the work actually lives.

**Tier 4: Executive Dashboard**  
4 widgets: project health overview (status breakdown), portfolio timeline (Gantt or timeline widget), SLA compliance tracker (how many requests reviewed within 5 days), department load (requests by department). Zero manual work for Pepper — everything feeds up automatically.

---

### Your AI Stack to Document

This is the section they'll spend real time on. Plan your documentation now:

**Claude:** Architecture design, formula logic for SLA tracking, mock data generation, intake form field design, consultative gap analysis (what Pepper didn't ask for). Document the prompts and the iterations.

**Native monday AI:** AI column on the intake board to auto-categorize vague requests and generate structured summaries. This directly solves Pepper's "requests are vague" problem. Name the specific feature and show it working.

**Where AI helped most:** Formula writing for the SLA countdown, generating realistic Stark Industries mock data to populate boards, architecting the connected board structure.

**Where AI was limited:** Final judgment calls on what Pepper actually needs vs. what she asked for. The consultative read is human.

---

### The 30-Minute Presentation Structure

**Minutes 1-3: Discovery recap.** "Before I show you what I built, let me tell you what I heard — and what I read between the lines." Name the three problems she stated and the two she didn't.

**Minutes 3-20: Walk the tiers.** Intake form → Portfolio board → Project board → Executive dashboard. For each tier: here's what it does, here's why I built it this way, here's the automation that connects it to the next layer.

**Minutes 20-25: AI walkthrough.** Show the AI column working on a vague request. Show your Claude prompts and what they produced. Be specific about iteration.

**Minutes 25-30: "What I'd do next."** Two or three things you'd build in phase two — this signals you think beyond the MVP and plan for adoption.

---

### The Q&A: What They'll Challenge

- "Can you add X on the fly?" — They will ask you to build something live. Stay calm, say "let me show you how I'd approach that," and prototype it in the board. Imperfect and live beats polished and scripted.
- "Why did you structure the boards this way vs. Y?" — Know your architectural decisions cold. Every choice should have a reason.
- "What happens when the PM doesn't update their board?" — This is the adoption question underneath the technical one. Have a change management answer ready.

---

### Immediate Next Steps

1. Sign up for the monday.com trial today
2. Spend a day getting oriented — boards, automations, connect boards, dashboard widgets, AI columns
3. Build the architecture in order: intake form first, portfolio board second, project board third, dashboard last
4. Document every Claude prompt you use as you go — don't reconstruct afterward
5. Populate with realistic Stark Industries mock data so the demo feels real

Want me to generate the mock data, write the SLA formula logic, or help you design the intake form fields?