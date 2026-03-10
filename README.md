# jay-i-skills

A personal operating system for working with Claude. This repo encodes how I think,
how I work, and what I've learned into structured files that any Claude session can
load and immediately operate from — with my voice, my frameworks, and my priorities.

Not a prompt library. Not a template collection. A system that makes Claude an
extension of how I already work.

## Philosophy

**Systems thinker.** I see structures, feedback loops, and leverage points before
I see tasks. When something isn't working, I look at the system producing the outcome,
not just the outcome.

**Iterative builder.** Ship v1, use it, improve it. Every file in this repo started
as a draft. Perfection is the enemy of a working system.

**Craft-first.** Quality is non-negotiable, but quality comes from iteration, not
from agonizing over the first version. A self-running demo is worth more than a slide
explaining the concept.

**Show, don't tell.** I build frameworks that encode expertise so others can use them —
scoring rubrics, assessment dimensions, maturity models, health dashboards. The artifact
does the communicating.

## What's In Here

```
jay-i-skills/
├── PROJECT.md              # Vision, identity, design principles
├── REQUIREMENTS.md         # What this system needs to do (testable)
├── STATE.md                # Current position, active threads, decisions
├── BACKLOG.md              # Phased work plan
├── CLAUDE.md               # How Claude works with me
├── README.md               # You are here
└── .claude/
    ├── commands/           # Slash commands (/repo-brief, etc.)
    ├── skills/             # Context-specific skills
    │   ├── work/           # Professional product leadership
    │   ├── pmi-buffalo/    # PMI Western NY chapter operations
    │   └── personal/       # Personal life assistant
    ├── frameworks/         # Reusable methodology walkthroughs
    │   ├── discovery/      # Frame → Engage → Map → Test
    │   ├── strategy/       # Diagnose → Policy → Actions → Stress-Test
    │   ├── prioritization/ # Criteria → Score → Allocate → Validate
    │   └── execution/      # Discuss → Plan → Execute → Verify
    ├── knowledge/          # Principles, vocabulary, references
    ├── templates/          # Document starting points
    └── private-template/   # Scaffold for companion private repo
```

## Three Contexts, Three Voices

Skills are organized into contexts. Each context has its own persona (`_persona.md`),
its own voice, and its own boundaries. Skills never cross contexts — even when the
task category is similar, the output is different.

| Context | Directory | What It Covers |
|---------|-----------|----------------|
| **Work** | `skills/work/` | Product leadership — strategy, PRDs, executive storytelling, coaching frameworks, stakeholder navigation, gap analysis, internal tooling, community content |
| **PMI Buffalo** | `skills/pmi-buffalo/` | PMI Western NY chapter — board reports, site audits, strategic benchmarks, member communications, event planning |
| **Personal** | `skills/personal/` | Personal projects and life — soup-feast app, decision-making, research, weekly reviews |

## How It Works

### For Me (Direct Use)

1. Claude reads `CLAUDE.md` at session start — picks up structure, conventions, and behaviors
2. `STATE.md` tells Claude what's in-flight and what was recently decided
3. `/repo-brief` reads `BACKLOG.md` and produces a focused session brief for the next task
4. Skills activate by slash command or context detection, loading the right persona first

### For Downstream Repos

Project repos (like `soup-feast`) don't duplicate skills or personas. Each downstream
repo's `CLAUDE.md` includes a pointer back to this repo — specifying which context
applies, where to find the persona, and which skills and design docs are relevant.

One source of truth. No drift. See `CLAUDE.md` for the full downstream pattern.

## Frameworks

Four reusable methodology walkthroughs that skills reference when the work calls for
structured thinking. Frameworks encode *how* to approach a category of work — they're
context-neutral and persona-independent.

| Framework | When to Use |
|-----------|-------------|
| **Discovery** | Understanding users, mapping opportunity spaces, testing assumptions |
| **Strategy** | Diagnosing situations, setting direction, making coherent choices |
| **Prioritization** | Scoring options, allocating effort across Run/Improve/Transform |
| **Execution** | Moving from discussion to shipped outcome with verification |

## Knowledge

Three files that give Claude the vocabulary, principles, and references to reason
like I do — not just execute tasks, but understand why certain approaches matter.

| File | What It Contains |
|------|-----------------|
| `principles.md` | Core beliefs that guide decisions — each with explanation and "in practice" guidance |
| `vocabulary.md` | Domain terms: Team Topologies, lifecycle stages, Balanced Breakthrough, harvey balls, gearing ratios |
| `references.md` | Influences mapped to what I took from each — Teresa Torres, Marty Cagan, Team Topologies, Rumelt, Reinertsen |

## Upstream Influences

This repo's architecture draws from three open-source Claude skill repos:

- **[GSD](https://github.com/gsd-build/get-shit-done)** — Document architecture pattern (PROJECT.md, STATE.md, REQUIREMENTS.md). File-based context over conversation memory. The discuss→plan→execute→verify cycle.
- **[Superpowers](https://github.com/obra/superpowers)** — SKILL.md format with YAML frontmatter. Brainstorm→spec→plan→execute→review discipline. Skills as mandatory workflows, not optional suggestions.
- **[PM Skills](https://github.com/phuryn/pm-skills)** — Discovery→strategy→execution taxonomy. Structured framework walkthroughs. Domain context encoded into skills so Claude understands methodology, not just steps.

## Public How / Private What

This repo captures *how* I think and work — principles, vocabulary, frameworks, skills.
It does not capture *what* I'm working on — specific initiatives, stakeholder maps,
organizational details. That belongs in a separate private companion repo.

The `private-template/` directory provides a scaffold for creating that companion repo.
See `PROJECT.md` design principle #6 for the full rationale.

## Status

Active development. Phase 0 (foundation documents) is wrapping up. See `BACKLOG.md`
for the full phased plan and `STATE.md` for current position.
