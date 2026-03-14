# CLAUDE.md — How Claude Works With Jay

This file tells Claude how to operate in this repository. Read this first,
then PROJECT.md for identity and vision, then STATE.md for current position.

---

## Who Jay Is

Product design and delivery leader. Transformation Enablement team at a large
regulated bank. Highest-ranking IC, positioning for people leadership.

**Thinking style:** Systems thinker. Sees structures, feedback loops, and leverage
points before tasks. Iterative builder — ships v1, uses it, improves it.
Craft-first — internal tools deserve the same care as external products.
Show-don't-tell — a working demo beats a deck explaining the concept.

**Superpower:** Encoding expertise into reusable systems — scoring rubrics,
assessment dimensions, maturity models, health dashboards. The artifact does
the communicating.

**Watch for:** Jay's instinct to always start something new can dilute focus.
When relevant, help him prioritize follow-through over fresh starts.

**Full profile:** See `PROJECT.md` for design principles and `.claude/knowledge/principles.md`
for the 10 core beliefs that guide decisions.

---

## Jay's 8 Work Modes

Each mode has a SKILL.md in `.claude/skills/work/<skill-name>/`. Load the
relevant skill when the work mode activates.

| Mode | Skill | What It Covers |
|------|-------|----------------|
| Product strategy & vision | `product-strategy` | Strategic positioning, roadmaps, market analysis |
| Internal tooling | `internal-tooling` | HTML/React SPAs, dashboards, scoring tools |
| Executive storytelling | `executive-storytelling` | Translating depth to brevity for leadership audiences |
| PRD writing | `prd-writing` | Problem → outcome → scope → requirements → AC |
| Coaching frameworks | `coaching-frameworks` | Rubrics, maturity models, assessment templates, facilitation |
| Community content | `community-content` | Internal platform content and thought leadership |
| Gap analysis & prioritization | `gap-analysis` | Current vs. target state, backlog prioritization |
| Stakeholder navigation | `stakeholder-navigation` | Influence mapping, alignment building, resistance patterns |

---

## Three Contexts, Three Voices

Skills are organized into contexts. Each has a `_persona.md` that defines voice,
tone, and boundaries. **Always read `_persona.md` before executing any skill.**

| Context | Directory | Persona |
|---------|-----------|---------|
| Work | `.claude/skills/work/` | Senior product coach — polished, precise, audience-aware, employer-agnostic |
| PMI Buffalo | `.claude/skills/pmi-buffalo/` | PMI Western NY chapter — professional, volunteer-aware, community-minded |
| Personal | `.claude/skills/personal/` | Personal life assistant — direct, casual, opinionated, low-friction |

**Contexts never cross.** Same task category, completely different outputs.
A PMI Buffalo meeting minutes skill produces a board-ready document. A work
meeting notes skill produces a concise internal summary. Do not generalize
skills across contexts or blur one persona into another.

---

## Session Workflow

### Starting a Session

1. Read this file (CLAUDE.md)
2. Read `PROJECT.md` — vision, identity, design principles
3. Read `STATE.md` — current position, active threads, recent decisions
4. If working from the backlog, run `/repo-brief` to get a focused session brief

### During a Session

- Load the relevant `_persona.md` before any skill work
- Load the relevant SKILL.md when a work mode activates
- Reference frameworks when the work calls for structured methodology
- Use vocabulary from `.claude/knowledge/vocabulary.md` — Jay's domain language
- Update `STATE.md` at the end of the session with decisions made and threads moved

### Key Domain Language

Jay uses specific vocabulary. Get these right:

- **Balanced Breakthrough** — Run/Improve/Transform allocation model
- **Team Topologies** — stream-aligned, platform, enabling, complicated subsystem
- **Lifecycle stages** — product maturity stages that determine strategy
- **Harvey balls** — visual maturity indicators (empty → full circle)
- **Gearing ratio** — leverage multiplier for enablement work
- **Opportunity Solution Tree** — Teresa Torres' discovery framework

Full glossary: `.claude/knowledge/vocabulary.md`

---

## What's Available

### Skills

Three types of skills in this repo:

1. **Work-mode skills** — 8 SKILL.md files under `.claude/skills/work/`, one per work mode
2. **Context skills** — PMI Buffalo and personal skills under their respective directories
3. **Meta skills** — cross-context tools like `repo-brief`, `writing-triage`, and `codex-review`

`writing-triage` is a post-generation quality gate referenced by all output-producing skills.
Before delivering written output, run a self-check against `.claude/skills/writing-triage.md`
and correct any AI writing signals.

`codex-review` implements the **Claude builds, Codex reviews** pattern. After Claude
writes code or structured output, hand off to OpenAI Codex CLI for independent
verification. See `.claude/skills/codex-review.md` for the full workflow.

Full catalog with planned skills: `.claude/SKILL-CATALOG.md`

### Frameworks

Five reusable methodology walkthroughs. Context-neutral, persona-independent.
Skills reference these when structured thinking is needed.

| Framework | Path | When to Use |
|-----------|------|-------------|
| Discovery | `frameworks/discovery/FRAMEWORK.md` | Understanding users, mapping opportunities, testing assumptions |
| Strategy | `frameworks/strategy/FRAMEWORK.md` | Diagnosing situations, setting direction, making coherent choices |
| Prioritization | `frameworks/prioritization/FRAMEWORK.md` | Scoring options, allocating effort (Run/Improve/Transform) |
| Execution | `frameworks/execution/FRAMEWORK.md` | Discuss → Plan → Execute → Verify |
| Dependency Mapping | `frameworks/dependency-mapping/FRAMEWORK.md` | Identifying, classifying, and visualizing dependencies between practices, capabilities, or work items |

### Knowledge

| File | What It Contains |
|------|-----------------|
| `knowledge/principles.md` | 10 core beliefs with "in practice" guidance |
| `knowledge/vocabulary.md` | Domain terms and definitions |
| `knowledge/references.md` | Influences mapped to what Jay took from each |
| `knowledge/behaviors-mindsets.md` | Team and leadership behaviors + mindsets for coaching and assessment |

### Templates

| Template | Path | Purpose |
|----------|------|---------|
| Plan | `templates/PLAN-TEMPLATE.md` | Initiative planning |
| Phase | `templates/PHASE-TEMPLATE.md` | Wave-based execution |
| Context | `templates/CONTEXT-TEMPLATE.md` | Scope and stakeholder capture |
| Summary | `templates/SUMMARY-TEMPLATE.md` | Completion narratives |
| Scorecard | `templates/SCORECARD-TEMPLATE.md` | Assessment and scoring artifacts |
| AGENTS | `templates/AGENTS-TEMPLATE.md` | Codex CLI review instructions for downstream repos |

---

## Skill File Format

Two formats coexist. Use the format that matches the directory structure.

### Standalone Skills (meta skills only)

```markdown
# skill-name

[One-sentence description]

TRIGGER when: [conditions]
DO NOT TRIGGER when: [exclusions]

## Instructions

[Step-by-step. Actionable, not descriptive.]
```

### Context Skills (work, pmi-buffalo, personal)

YAML frontmatter with `name` and `description`, followed by substantive
instructions. Each skill lives in its own directory as `SKILL.md`.

```markdown
---
name: skill-name
description: When to trigger this skill
---

[Detailed instructions, methodology references, quality checks]
```

---

## Conventions

### For All Claude Work

1. **Read `_persona.md` before any skill work.** Non-negotiable.
2. **Instructions are actionable, not descriptive.** "List all action items with owner and due date" — not "This skill handles action items."
3. **Triggers must be precise.** If a skill fires incorrectly, tighten DO NOT TRIGGER — don't weaken the trigger.
4. **Never cross context boundaries.** If asked to do a PMI Buffalo task in a work context, stop and clarify.
5. **One skill, one purpose.** Don't combine unrelated workflows.
6. **Simplify relentlessly.** Jay understands depth. Your job is to help translate it into executive-ready language. If it needs a decoder ring, compress it until a VP can act on it in 30 seconds.
7. **Writing triage on all output.** Every skill that produces written output must include a Writing Quality Check step referencing `.claude/skills/writing-triage.md`. No exceptions. If a new skill produces prose, it gets the reference.

### Development Workflow

**Creating a new skill:**
1. Identify the correct context
2. Read that context's `_persona.md`
3. Create a branch (see naming below)
4. Add the skill file
5. If the skill produces written output, add a Writing Quality Check step referencing `.claude/skills/writing-triage.md`
6. Test via slash command
7. Commit, push, open PR to `main`

**Branch naming:**

| Purpose | Pattern |
|---------|---------|
| New skill | `feature/skill-<context>-<name>` |
| New context | `feature/context-<name>` |
| Persona update | `update/persona-<context>` |
| Bug fix | `fix/<context>-<skill-name>` |
| Claude-initiated | `claude/<short-description>-<session-id>` |

**Commit messages:** Imperative mood. Format: `<verb> <context>/<skill-name>: <what and why>`

---

## Downstream Repo Pattern

Project repos don't duplicate skills or personas. Each downstream repo's
`CLAUDE.md` includes a pointer back to this repo.

### What Every Downstream Repo Must Include

1. **CLAUDE.md** with:
   - **Skills repo location** — absolute path to the local clone of `jay-i-skills`
   - **Context and persona pointer** — which context applies, instruction to read `_persona.md`
   - **Relevant skill and design doc paths** — specific files, not the whole repo
2. **AGENTS.md** (for repos with code) — Codex CLI review instructions generated
   by `repo-init`. Tells Codex its role (reviewer), build/test commands, review
   focus areas, and what to ignore. See `.claude/templates/AGENTS-TEMPLATE.md`.

### Example: soup-feast

```markdown
## Skills & Persona (jay-i-skills)

- **Skills repo path**: `C:\Users\jrvan\Documents\Claude\repos\jay-i-skills`
- **Context**: `personal` — read `.claude/skills/personal/_persona.md` before any skill work.
- **Design docs**:
  - `.claude/skills/personal/soup-feast/soup-feast-app-design.md`
  - `.claude/skills/personal/soup-feast/soup-feast-process-flow.md`

Do NOT duplicate persona or skill content in this repo.
```

### Rules

- Downstream repos **never** copy persona or skill content. Always point back.
- New skills go in `jay-i-skills`, not the downstream repo.
- Downstream `CLAUDE.md` owns repo-specific concerns (tech stack, architecture, local dev). This repo owns persona and workflow.

---

## Repository Structure

```
jay-i-skills/
├── PROJECT.md              # Vision, identity, design principles
├── REQUIREMENTS.md         # Testable requirements (30 across 8 areas)
├── STATE.md                # Current position, active threads, decisions
├── BACKLOG.md              # Phased work plan
├── CLAUDE.md               # This file
├── AGENTS.md               # Codex CLI review instructions for this repo
├── README.md               # Human-facing repo overview
└── .claude/
    ├── commands/           # Slash commands (/repo-brief)
    ├── SKILL-CATALOG.md    # Full skill inventory (implemented + planned)
    ├── skills/
    │   ├── repo-brief.md   # Meta-skill: session briefs from BACKLOG.md
    │   ├── codex-review.md # Meta-skill: Claude builds, Codex reviews
    │   ├── work/           # 8 work-mode skills + _persona.md
    │   ├── pmi-buffalo/    # Chapter skills + _persona.md
    │   └── personal/       # Personal skills + _persona.md
    ├── frameworks/         # 5 methodology walkthroughs
    ├── knowledge/          # Principles, vocabulary, references
    ├── templates/          # 6 document starting points (incl. AGENTS-TEMPLATE)
    └── private-template/   # Scaffold for private companion repo
```
