# PROJECT.md — jay-i-skills

## What This Is

This repo is my personal operating system for working with AI. It encodes how I think,
how I work, and what I've learned into structured files that any Claude session can load
and immediately operate from — with my voice, my frameworks, and my priorities.

It is not a collection of prompts. It is not a generic template library. It is a system
that makes Claude an extension of how I already work, across three distinct contexts:
professional product leadership, PMI Buffalo chapter operations, and personal life.

## Who I Am

I lead product design and delivery inside a Transformation Enablement team at a large
regulated bank. My focus is product leadership tooling — building the frameworks, assessments,
and internal tools that help product teams work better.

I think in systems, build iteratively, value craft, and prefer showing over telling.
I build frameworks that encode expertise so others can use them — scoring rubrics,
assessment dimensions, gearing ratios, health models. A self-running demo is worth
more than a slide explaining the concept.

### My 8 Work Modes

1. **Product strategy & vision** — strategic positioning, roadmaps, market analysis
2. **Internal tooling** — HTML/React single-page apps, dashboards, scoring tools
3. **Executive storytelling** — translating depth into brevity for leadership audiences
4. **PRD writing** — product requirements, specs, documentation
5. **Coaching frameworks** — rubrics, maturity models, assessment templates, facilitation guides
6. **Community content** — PMI Buffalo chapter communications, events, thought leadership
7. **Gap analysis & prioritization** — current vs. target state, backlog prioritization
8. **Stakeholder navigation** — influence mapping, alignment building, resistance patterns

Each mode has a corresponding SKILL.md in `.claude/skills/work/` that Claude loads
when the mode activates.

## Vision

**Make Claude a reliable co-worker, not a generic assistant.**

Every session should start with enough context that Claude doesn't need to ask
"what do you do?" or "what's your style?" The repo provides:
- **Identity** — who I am, how I think, what I value (this file, knowledge/)
- **Capability** — what I can do, structured as loadable skills (skills/)
- **Method** — how I approach work, structured as reusable frameworks (frameworks/)
- **Templates** — starting points for recurring document types (templates/)
- **State** — what's in-flight, what was just decided, what's next (STATE.md, BACKLOG.md)

The goal is continuity across sessions. Claude should pick up where the last session
left off, not start from scratch.

## Design Principles

### 1. Context Is Architecture
How information is structured determines how well Claude performs. This repo treats
file structure, naming conventions, and document format as first-class design decisions —
not afterthoughts. Inspired by GSD's insight that persistent files beat conversation memory.

### 2. Personas Don't Blend
The three contexts (work, PMI Buffalo, personal) have separate voices, separate skills,
and separate boundaries. A PMI Buffalo meeting minutes skill produces a board-ready
document. A work meeting notes skill produces a concise internal summary. Same task
category, completely different outputs. This is intentional — never generalize across contexts.

### 3. Skills Are Workflows, Not Prompts
A skill isn't "write me an email." A skill is a structured workflow with triggers,
instructions, domain context, and quality checks. Inspired by Superpowers' SKILL.md
format — skills are mandatory workflows that Claude follows, not optional suggestions.

### 4. Frameworks Encode Method
Frameworks capture how I approach a category of work — discovery, strategy, prioritization,
execution. They're reusable across skills and contexts. A framework teaches Claude the
methodology; a skill applies it in a specific persona. Inspired by PM Skills' structured
walkthrough format.

### 5. Ship v1, Refine From Usage
Every file in this repo started as a v1. Perfection is the enemy of a working system.
Get the structure right, get the content good enough to use, then iterate based on
what actually helps and what doesn't.

### 6. Public How / Private What
This repo captures how I think and work — principles, vocabulary, frameworks, skills.
It does not capture what I'm working on — specific initiatives, stakeholder maps,
organizational context. That belongs in a separate private repo. The two-repo pattern
keeps the operating system portable while keeping sensitive context secure.

## Upstream Influences

### GSD (Get Shit Done)
**What I took:** The document architecture pattern — PROJECT.md, STATE.md, REQUIREMENTS.md
as persistent context files. The discuss→plan→execute→verify cycle. The principle that
plans are prompts, not documents. File-based context over conversation-based context.

### Superpowers
**What I took:** The SKILL.md format with YAML frontmatter. The discipline of
brainstorm→spec→plan→execute→review. The insight that skill descriptions should state
*when* to trigger, not *what* the skill does (Claude Search Optimization). Skills as
mandatory workflows with quality gates.

### PM Skills
**What I took:** The plugin/skill/command hierarchy. The discovery→strategy→execution
taxonomy for organizing PM frameworks. The pattern of encoding domain context into skills
so Claude understands the methodology, not just the steps. Checkpoint-based workflows
with explicit pause points.

## Repository Structure

```
jay-i-skills/
├── PROJECT.md              # This file — vision, identity, design principles
├── REQUIREMENTS.md         # What this system needs to do
├── STATE.md                # Current position, active threads, parking lot
├── BACKLOG.md              # Phased evolution plan
├── CLAUDE.md               # How Claude works with me — behaviors, skills, workflow
├── README.md               # Human-facing repo overview
├── .claude/
│   ├── commands/           # Slash commands (/repo-brief, etc.)
│   ├── knowledge/          # Principles, vocabulary, references
│   ├── skills/             # Context-specific skills (work/, pmi-buffalo/, personal/)
│   ├── frameworks/         # Reusable methodology walkthroughs
│   ├── templates/          # Document starting points
│   └── private-template/   # Scaffold for private companion repo
```

## What Success Looks Like

- A fresh Claude session loads CLAUDE.md, reads PROJECT.md and STATE.md, and is
  immediately productive — no "getting to know you" warmup needed
- Skills produce output that sounds like me, not like a generic AI
- Frameworks guide real work, not theoretical exercises
- The backlog is a living document that I actually use to drive sessions
- Downstream repos (soup-feast, future work repo) point back here and inherit
  the right persona automatically
