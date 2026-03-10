# REQUIREMENTS.md — jay-i-skills

What this system needs to do, expressed as testable requirements.
Organized by capability area. Each requirement has an ID, a statement,
and how you'd know it's working.

---

## Scope

**v1** — committed requirements for the current system.
**Future** — acknowledged needs, deferred until v1 is stable.

---

## SKL: Skill Invocation

| ID | Requirement | Verification |
|----|-------------|--------------|
| SKL-01 | Every skill has a SKILL.md with YAML frontmatter (name, description) and substantive instructions | Inspect each `.claude/skills/work/*/SKILL.md` — frontmatter parses, instructions are actionable |
| SKL-02 | Skill descriptions state *when* to trigger, not what the skill does | Read each description — it starts with triggering conditions, not a workflow summary |
| SKL-03 | Each of the 8 work modes has a corresponding skill file | Count: 8 directories under `.claude/skills/work/`, each with a SKILL.md |
| SKL-04 | Slash commands in `.claude/commands/` are invocable via `/command-name` | Run `/repo-brief` — Claude executes the skill workflow |
| SKL-05 | Skills reference frameworks by path when methodology applies | Grep SKILL.md files for framework references — strategy skill links to `frameworks/strategy/FRAMEWORK.md`, etc. |

## PER: Persona Isolation

| ID | Requirement | Verification |
|----|-------------|--------------|
| PER-01 | Each context (work, pmi-buffalo, personal) has a `_persona.md` | Check: 3 files exist at `.claude/skills/{context}/_persona.md` |
| PER-02 | Personas define voice, tone, boundaries, and recurring use cases | Read each `_persona.md` — all four sections present |
| PER-03 | No skill file references or imports content from another context's persona | Grep all skill files for cross-context references — zero matches |
| PER-04 | Claude reads `_persona.md` before executing any skill in that context | CLAUDE.md contains explicit instruction to read persona first |
| PER-05 | Work context contains no employer name, organization name, or identifying details | Grep `.claude/skills/work/` for employer-specific terms — zero matches |

## DWN: Downstream Repo Support

| ID | Requirement | Verification |
|----|-------------|--------------|
| DWN-01 | CLAUDE.md documents the downstream pointer pattern (skills repo path, context, persona pointer, relevant skill paths) | Read CLAUDE.md — pattern is documented with example |
| DWN-02 | A private-template scaffold exists with README and directory guides | Check: `.claude/private-template/` contains README.md, context/README.md, stakeholders/README.md, initiatives/README.md |
| DWN-03 | Downstream repos never duplicate persona or skill content | Documented as a rule in CLAUDE.md — "always point back" |
| DWN-04 | `repo-init` meta skill can generate a downstream CLAUDE.md with pointer section pre-filled | Invoke `/repo-init` with a repo path and context — produces valid CLAUDE.md |

## KNW: Knowledge Capture

| ID | Requirement | Verification |
|----|-------------|--------------|
| KNW-01 | Principles file captures core beliefs with enough depth to guide Claude's behavior | Read `knowledge/principles.md` — each principle has a name, explanation, and "in practice" section |
| KNW-02 | Vocabulary file defines all domain terms used across skills and frameworks | Cross-reference terms used in SKILL.md and FRAMEWORK.md files against `knowledge/vocabulary.md` — all terms defined |
| KNW-03 | References file maps influences to what was taken from each | Read `knowledge/references.md` — each source has a "key ideas I use" column |
| KNW-04 | Knowledge files are context-neutral — usable across all three personas | Read knowledge files — no context-specific voice or boundaries |

## FWK: Framework Reuse

| ID | Requirement | Verification |
|----|-------------|--------------|
| FWK-01 | Each framework is a real step-by-step walkthrough, not a placeholder | Read each FRAMEWORK.md — phases have specific instructions, not just names |
| FWK-02 | Frameworks cover the four core methodologies: discovery, strategy, prioritization, execution | Check: 4 directories under `.claude/frameworks/`, each with FRAMEWORK.md |
| FWK-03 | Frameworks are reusable across contexts — no persona-specific language | Read FRAMEWORK.md files — methodology only, no voice/tone constraints |
| FWK-04 | Frameworks encode the underlying methodology, not just steps | Each FRAMEWORK.md explains *why* each phase matters, not just *what* to do |

## TPL: Templates

| ID | Requirement | Verification |
|----|-------------|--------------|
| TPL-01 | Templates exist for the four core document types: plan, phase, context, summary | Check: 4 files in `.claude/templates/` |
| TPL-02 | Templates are usable as-is — fill in the blanks, not restructure from scratch | Start a new initiative using PLAN-TEMPLATE.md — produces a usable plan without rewriting the template |
| TPL-03 | Templates align with the execution framework's Discuss→Plan→Execute→Verify cycle | Cross-reference template sections against `frameworks/execution/FRAMEWORK.md` phases |

## STA: State & Continuity

| ID | Requirement | Verification |
|----|-------------|--------------|
| STA-01 | STATE.md captures current position, active threads, recent decisions, and parking lot | Read STATE.md — all four sections present and current |
| STA-02 | BACKLOG.md tracks work items with priority, status, and descriptions | Read BACKLOG.md — items have #, priority, status, title, description |
| STA-03 | A fresh Claude session can orient itself from CLAUDE.md → PROJECT.md → STATE.md without asking "what do you do?" | Start a new session in this repo — Claude is immediately productive |
| STA-04 | `/repo-brief` reads BACKLOG.md and produces a focused session brief for the next task | Invoke `/repo-brief` — produces brief with repo, item, priority, effort, checklist, and starting prompt |

## PUB: Public/Private Separation

| ID | Requirement | Verification |
|----|-------------|--------------|
| PUB-01 | This repo contains no employer names, project names, stakeholder names, or organizational specifics | Full-text search for known employer/org terms — zero matches |
| PUB-02 | The two-repo pattern (public how / private what) is documented | PROJECT.md design principle #6 and private-template README explain the pattern |
| PUB-03 | Private-template scaffold is a usable starting point for the companion repo | Follow private-template/README.md instructions — produces a functional private repo structure |

---

## Future (not v1)

| ID | Area | Requirement |
|----|------|-------------|
| FUT-01 | Skills | Automated skill quality scoring (grading rubric applied to each SKILL.md) |
| FUT-02 | State | Velocity tracking — plans completed, average duration, trend |
| FUT-03 | State | Session bridge file (continue-here.md) for mid-task handoffs |
| FUT-04 | Skills | Workflow chaining — commands that compose multiple skills into multi-step pipelines |
| FUT-05 | Downstream | Automated validation that downstream repos point back correctly |
| FUT-06 | Knowledge | Decision records (ADRs) for architectural choices |
