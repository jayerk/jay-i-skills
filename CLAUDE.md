# CLAUDE.md — PMI Buffalo Claude Skills

This file provides guidance for AI assistants (Claude) working in this repository.

## Repository Overview

**Purpose**: This repository hosts custom Claude Code skills for the PMI Buffalo chapter (Project Management Institute — Buffalo, NY). Skills are reusable prompt templates that trigger Claude to follow specialized workflows when performing chapter-related tasks.

**Audience**: Chapter leadership, volunteers, and AI assistants helping to automate or enhance PMI Buffalo operations.

## What Are Claude Code Skills?

Skills are markdown files stored in `.claude/skills/`. Each skill defines:
- A **trigger condition** — when Claude should activate the skill
- A **system prompt** — instructions Claude follows when the skill is active
- A **description** — what the skill does and how to invoke it

Skills are invoked via slash commands (e.g., `/strategic-benchmark`) or triggered automatically when Claude detects matching context.

### Skill File Format

```markdown
# skill-name

[Short description of what this skill does and when to use it]

TRIGGER when: [conditions that activate this skill]
DO NOT TRIGGER when: [conditions that should NOT activate this skill]

## Instructions

[Step-by-step instructions Claude follows when this skill is active]
```

Place each skill file at `.claude/skills/<skill-name>.md`.

## Repository Structure

```
pmi-buffalo-claude-skills/
├── CLAUDE.md                     # This file — AI assistant guidance
├── README.md                     # Human-facing project overview
└── .claude/
    └── skills/                   # One .md file per skill
        ├── strategic-benchmark.md
        ├── meeting-minutes.md
        └── ...
```

## Development Workflow

### Creating a New Skill

1. Create a new branch: `git checkout -b feature/skill-<name>`
2. Add a skill file at `.claude/skills/<skill-name>.md`
3. Follow the skill file format above exactly
4. Test the skill locally in Claude Code by invoking `/<skill-name>`
5. Commit with a descriptive message:
   ```
   git commit -m "Add <skill-name> skill: <one-line description>"
   ```
6. Push and open a pull request targeting `main`

### Updating an Existing Skill

- Edit the skill file directly
- Increment specificity in trigger conditions if the skill is firing incorrectly
- Commit with: `git commit -m "Update <skill-name>: <what changed and why>"`

### Branch Naming Conventions

| Purpose | Pattern |
|---|---|
| New skill | `feature/skill-<name>` |
| Bug fix | `fix/skill-<name>` |
| Documentation | `docs/<description>` |
| Claude-initiated work | `claude/<short-description>-<session-id>` |

### Commit Message Conventions

- Use imperative mood: "Add", "Update", "Fix", "Remove"
- Reference the skill name in the message
- Keep subject line under 72 characters
- Example: `Add meeting-minutes skill: extract action items from transcripts`

## Key Conventions for AI Assistants

1. **Never edit skill trigger conditions without understanding the intent.** Triggers are precise by design. If a skill fires when it shouldn't, tighten the DO NOT TRIGGER clause rather than weakening the trigger.

2. **Skill instructions must be actionable, not descriptive.** Write "Extract all action items and list them with owners" not "This skill handles action items."

3. **One skill per file, one file per concern.** Do not combine unrelated workflows into a single skill.

4. **Skills are PMI Buffalo-specific.** Keep chapter names, templates, and report formats aligned with PMI Buffalo's actual processes. Avoid generic PMI boilerplate unless it matches how Buffalo operates.

5. **Test before committing.** Invoke the skill in Claude Code and verify the output matches the intended workflow before pushing.

6. **Keep CLAUDE.md current.** When adding a new skill, update the "Recommended Skills" section below to mark it as implemented.

## Existing Skills

| Skill | File | Status |
|---|---|---|
| Strategic Benchmark | `.claude/skills/strategic-benchmark.md` | Planned |

## Recommended Skills for PMI Buffalo

The following skills are recommended based on common chapter operational needs. Skills marked **Planned** are in the backlog; **In Progress** are being developed.

### Governance & Reporting

| Skill | Trigger | Value |
|---|---|---|
| `strategic-benchmark` | Comparing chapter metrics against peer chapters | Pulls structured data from chapter reports and surfaces gaps vs. benchmarks across membership, events, financials, and volunteer hours |
| `board-report` | Drafting monthly/quarterly board updates | Generates a structured board report from bullet-point inputs covering membership, programs, finance, and volunteers |
| `annual-report-draft` | Compiling end-of-year chapter summary | Aggregates metrics and narratives into the PMI annual report format |

### Meetings & Communication

| Skill | Trigger | Value |
|---|---|---|
| `meeting-minutes` | Processing meeting transcripts or notes | Extracts decisions, action items (with owners and due dates), and open issues from raw notes |
| `email-draft` | Drafting chapter communications | Produces member-facing emails in PMI Buffalo's tone — professional, concise, and community-oriented |
| `newsletter-section` | Writing content for the chapter newsletter | Formats event recaps, member spotlights, and announcements to newsletter standards |

### Events & Programs

| Skill | Trigger | Value |
|---|---|---|
| `event-plan` | Planning a chapter event or PDU activity | Produces a checklist-driven event plan covering logistics, promotion, speaker coordination, and post-event follow-up |
| `pdu-tracker` | Logging or auditing PDU submissions | Helps members and leaders structure PDU activity descriptions to meet PMI reporting requirements |
| `speaker-outreach` | Drafting outreach to potential speakers | Generates personalized speaker invitation emails aligned with chapter program themes |

### Membership & Volunteers

| Skill | Trigger | Value |
|---|---|---|
| `membership-analysis` | Analyzing membership growth, churn, or demographics | Structures a narrative around raw membership data to surface trends and recommended actions |
| `volunteer-brief` | Onboarding a new chapter volunteer | Produces a role-specific volunteer orientation brief with responsibilities, contacts, and key dates |
| `recognition-draft` | Writing volunteer or member recognition content | Drafts award descriptions, LinkedIn shoutouts, or thank-you messages for chapter contributors |

### Finance & Sponsorship

| Skill | Trigger | Value |
|---|---|---|
| `budget-review` | Reviewing chapter budget vs. actuals | Structures a narrative analysis of budget variance with recommended adjustments |
| `sponsor-proposal` | Creating sponsorship packages or outreach | Drafts tiered sponsorship proposals tailored to local Buffalo/WNY business interests |

## Getting Help

- Claude Code documentation: `/help` in Claude Code
- PMI Buffalo leadership contact: see internal chapter directory
- Skill bugs or improvements: open an issue or PR in this repository
