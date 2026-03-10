# CLAUDE.md — Jay's Claude Skills Repository

This file provides guidance for AI assistants (Claude) working in this repository.

## Repository Overview

**Purpose**: This repository hosts custom Claude Code skills organized into distinct, isolated contexts. Each context has its own persona, tone, and skill set. Contexts do **not** share skills — even for similar tasks, each context gets its own version tuned to that persona.

**Contexts**:

| Context | Directory | Persona Summary |
|---|---|---|
| PMI Buffalo | `.claude/skills/pmi-buffalo/` | PMI Western NY chapter — professional, volunteer-aware, community-minded |
| Personal | `.claude/skills/personal/` | Personal life assistant — direct, casual, opinionated, low-friction |
| Work | `.claude/skills/work/` | Day-job professional — polished, precise, audience-aware |

---

## Repository Structure

```
jay-i-skills/
├── CLAUDE.md                              # This file
├── README.md                              # Human-facing project overview
└── .claude/
    └── skills/
        ├── repo-brief.md            # Meta-skill: session briefs from BACKLOG.md
        ├── pmi-buffalo/
        │   ├── _persona.md                # PMI Buffalo voice & identity
        │   ├── strategic-benchmark.md
        │   └── ...
        ├── personal/
        │   ├── _persona.md                # Personal assistant voice & identity
        │   ├── soup-feast/                # Soup Feast app design & process docs
        │   └── ...
        └── work/
            ├── _persona.md                # Work/professional voice & identity
            └── ...
```

### The `_persona.md` File

Every context directory contains a `_persona.md`. This file defines:
- Who Claude is in this context
- Voice and tone guidelines
- Hard boundaries (what Claude must NOT do in this context)
- Recurring use cases and artifacts

**Always read `_persona.md` before executing any skill in a context.** The persona is the foundation — individual skills build on top of it.

---

## What Are Claude Code Skills?

Skills are markdown files that define specialized Claude workflows. Each skill:
- Has a **trigger condition** — when Claude activates the skill
- Has **instructions** — what Claude does when active
- Inherits the **persona** of its context directory

Skills are invoked via slash commands (e.g., `/strategic-benchmark`) or trigger automatically when Claude detects matching context.

### Skill File Format

```markdown
# skill-name

[One-sentence description of what this skill does]

TRIGGER when: [conditions that activate this skill]
DO NOT TRIGGER when: [conditions that must NOT activate this skill]

## Instructions

[Step-by-step instructions Claude follows. Actionable, not descriptive.]
```

---

## Core Principle: Distinct Personalities, No Crossover

**Skills are not shared between contexts.** If a similar task exists in two contexts (e.g., meeting minutes for PMI Buffalo and meeting notes at work), each context gets its own skill written to that persona. A PMI Buffalo meeting minutes skill produces a formal board-ready document. A work meeting notes skill produces a concise internal summary. Same task category — completely different outputs.

This is intentional. Do not:
- Generalize a skill to work across contexts
- Reuse a skill file from one context in another
- Blur the voice of one persona into another

---

## Development Workflow

### Creating a New Skill

1. Identify the correct context (pmi-buffalo, personal, or work)
2. Read that context's `_persona.md` before writing
3. Create a branch: `git checkout -b feature/skill-<context>-<name>`
4. Add the skill at `.claude/skills/<context>/<skill-name>.md`
5. Follow the skill file format exactly
6. Test in Claude Code by invoking `/<skill-name>`
7. Commit: `git commit -m "Add <context>/<skill-name>: <one-line description>"`
8. Push and open a PR targeting `main`

### Adding a New Context

1. Create `.claude/skills/<context-name>/`
2. Write `_persona.md` first — define voice, tone, boundaries, and use cases before writing any skills
3. Update the context table in this file
4. Add skill recommendations to the backlog below

### Branch Naming

| Purpose | Pattern |
|---|---|
| New skill | `feature/skill-<context>-<name>` |
| New context | `feature/context-<name>` |
| Persona update | `update/persona-<context>` |
| Bug fix | `fix/<context>-<skill-name>` |
| Claude-initiated | `claude/<short-description>-<session-id>` |

### Commit Message Conventions

- Imperative mood: "Add", "Update", "Fix", "Remove"
- Format: `<verb> <context>/<skill-name>: <what and why>`
- Example: `Add pmi-buffalo/meeting-minutes: extract action items from board notes`

---

## Conventions for AI Assistants

1. **Read `_persona.md` before any skill work.** Voice and boundaries are non-negotiable per context.

2. **Triggers must be precise.** If a skill fires incorrectly, tighten the DO NOT TRIGGER clause — don't weaken the trigger.

3. **Instructions are actionable, not descriptive.** Write "List all action items with owner and due date" — not "This skill handles action items."

4. **Never cross context boundaries.** If asked to do a PMI Buffalo task while in a personal context, stop and clarify which context applies.

5. **One skill, one purpose.** Do not combine unrelated workflows.

6. **Keep CLAUDE.md current.** When adding a skill, mark it in the backlog below.

---

## How Downstream Repos Reference These Skills

Jay's project repositories (e.g., `soup-feast`) do **not** duplicate skills or personas. Instead, each downstream repo's `CLAUDE.md` includes a **pointer** back to `jay-i-skills` — telling Claude where to find the persona, skills, and design docs that govern behavior in that repo.

### Why This Pattern Exists

- **Single source of truth** — persona and skill definitions live in one place. Updating a persona here updates behavior everywhere.
- **No drift** — downstream repos don't maintain their own copy of voice, tone, or skill logic that can go stale.
- **Context stays clean** — the downstream CLAUDE.md handles repo-specific concerns (tech stack, architecture, local conventions). The skills repo handles persona and workflow.

### What Every Downstream CLAUDE.md Must Include

When a project repo needs to reference jay-i-skills, its `CLAUDE.md` must include three things:

1. **Skills repo location** — the absolute path to the local clone of `jay-i-skills` so Claude can find and read files.
2. **Context and persona pointer** — which context directory applies (e.g., `personal`, `pmi-buffalo`, `work`) and an explicit instruction to read `_persona.md` before any skill work.
3. **Relevant skill and design doc paths** — specific paths to skill files or design docs in `jay-i-skills` that apply to this repo. Don't point at the entire skills repo — be precise about what's relevant.

### Example: soup-feast

The `soup-feast` repo is a personal project (The Great Soup Feast ranked-choice voting app). Its `CLAUDE.md` would include a section like this:

```markdown
## Skills & Persona (jay-i-skills)

This project uses skills and persona definitions from Jay's central skills repo.

- **Skills repo path**: `C:\Users\jrvan\Documents\Claude\repos\jay-i-skills`
- **Context**: `personal` — read `.claude/skills/personal/_persona.md` before any skill work.
- **Design docs**:
  - `.claude/skills/personal/soup-feast/soup-feast-app-design.md` — app design and UX decisions
  - `.claude/skills/personal/soup-feast/soup-feast-process-flow.md` — voting and event process flow

Do NOT duplicate persona or skill content in this repo. If a skill needs updating, update it in jay-i-skills.
```

### Rules

- Downstream repos must **never** copy-paste persona or skill content locally. Always point back.
- If a downstream repo needs a new skill, create it in `jay-i-skills` under the correct context — not in the downstream repo.
- The downstream `CLAUDE.md` owns repo-specific concerns: tech stack, architecture decisions, local dev setup, contribution guidelines. The skills repo owns persona and workflow.

---

## Skill Backlog

### Meta (cross-context)

| Skill | Purpose | Status |
|---|---|---|
| `repo-brief` | Read BACKLOG.md files across repos and produce a focused working session brief for the next task — teaches, not just executes | Implemented |
| `repo-init` | Generate a downstream repo's CLAUDE.md with the correct pointer section (skills repo path, context, persona, relevant design docs) pre-filled — prevents drift by making setup correct from the start | Planned |

### PMI Buffalo

| Skill | Purpose | Status |
|---|---|---|
| `strategic-benchmark` | Compare chapter metrics vs. peer chapters — 5-agent (Data Analyst, Strategist, Devil's Advocate, Community Advocate, People Connector) + Chief of Staff synthesis | Implemented |
| `board-report` | Draft monthly/quarterly board update | Planned |
| `meeting-minutes` | Extract decisions & action items from board notes | Planned |
| `annual-report-draft` | Compile end-of-year chapter summary for PMI Global | Planned |
| `email-draft` | Draft member-facing chapter communications | Planned |
| `newsletter-section` | Write event recaps, spotlights, announcements | Planned |
| `event-plan` | Produce checklist-driven event/PDU activity plan | Planned |
| `pdu-tracker` | Structure PDU activity descriptions for PMI reporting | Planned |
| `speaker-outreach` | Draft speaker invitation emails | Planned |
| `membership-analysis` | Narrative around membership trends and actions | Planned |
| `volunteer-brief` | Role-specific onboarding brief for new volunteers | Planned |
| `recognition-draft` | Awards, LinkedIn shoutouts, thank-you messages | Planned |
| `sponsor-proposal` | Tiered sponsorship packages for WNY businesses | Planned |
| `budget-review` | Narrative analysis of chapter budget vs. actuals | Planned |
| `site-audit` | External public website crawl — flags stale content, PII, PMI cert content, DE&I issues; produces dated audit log | Implemented |
| `internal-audit` | Internal content audit — board docs, communications, unpublished materials | Planned |

### Personal

| Skill | Purpose | Status |
|---|---|---|
| `decision-matrix` | Structure a personal decision with pros/cons/criteria | Planned |
| `research-brief` | Summarize research on a purchase, topic, or option | Planned |
| `weekly-review` | Guided weekly personal review and planning session | Planned |
| `trip-plan` | Build a practical travel itinerary from requirements | Planned |
| `budget-snapshot` | Summarize personal finances and flag issues | Planned |

### Work

| Skill | Purpose | Status |
|---|---|---|
| `status-update` | Draft a concise project or work status update | Planned |
| `meeting-notes` | Produce internal meeting summary with next steps | Planned |
| `email-draft` | Draft professional workplace emails | Planned |
| `self-assessment` | Write performance self-assessment narratives | Planned |
| `exec-summary` | Condense a document into an executive summary | Planned |
| `slide-outline` | Structure a presentation from talking points | Planned |
