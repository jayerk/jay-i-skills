# BACKLOG.md — jay-i-skills

Phased evolution plan for the personal operating system. Work through items
using `/repo-brief`, which reads this file and produces a focused session brief.

---

## Status Key

| Status | Meaning |
|--------|---------|
| `todo` | Ready to work |
| `in-progress` | Active Claude Code session |
| `done` | Merged to main |
| `hold` | Blocked — see notes |

## Priority Key

| Priority | Meaning |
|----------|---------|
| P0 | Foundational — unblocks other work |
| P1 | High value — do early |
| P2 | Important — do after P0 + P1 |

---

## V1 Buildout

Architecture draws from [GSD](https://github.com/gsd-build/get-shit-done) (document architecture, phased planning),
[Superpowers](https://github.com/obra/superpowers) (SKILL.md format, brainstorm→spec→plan→execute→review),
and [PM Skills](https://github.com/phuryn/pm-skills) (structured frameworks, discovery/strategy/execution taxonomy).

### Phase 0 — Foundation Documents (P0) ✓

**Milestone:** All identity and purpose documents exist. System is self-describing.

| # | Status | Title |
|---|--------|-------|
| 11 | `done` | Create `PROJECT.md` |
| 12 | `done` | Create `REQUIREMENTS.md` |
| 13 | `done` | Create `STATE.md` |
| 14 | `done` | Upgrade `README.md` |

### Phase 1 — Core Documents Review (P0) ✓

**Milestone:** CLAUDE.md and BACKLOG.md reflect the full operating system vision.

| # | Status | Title |
|---|--------|-------|
| 15 | `done` | Upgrade `CLAUDE.md` to v1 |
| 16 | `done` | Restructure `BACKLOG.md` as phased plan |

### Phase 2 — Knowledge Base Review (P1)

**Milestone:** Knowledge files validated against Jay's full profile. All domain terms defined.
**Depends on:** Phase 1 (CLAUDE.md defines what "good" looks like for knowledge files).

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 17 | `done` | Review `knowledge/principles.md` | Validated 10 principles against full profile. Added "In practice" sections to all. Strengthened #1 (systems/boundaries), #6 (teams as product), #9 (discovery ↔ system boundaries). |
| 18 | `done` | Review `knowledge/vocabulary.md` | Validated and restructured. Added interaction modes, updated lifecycle stages (Concept→Launch→Growth→Maturity→Sunset), split Epic into Portfolio/Solution, restructured Agile at Scale into three subsections (Org Levels, Ceremonies, Governance), added Definition of Ready, removed HiPPO/Feature Factory/IP Iteration/Architectural Runway. |
| 19 | `todo` | Review `knowledge/references.md` | Validate: Teresa Torres, Marty Cagan, Team Topologies, GSD, Superpowers, PM Skills, Rumelt, Reinertsen. Ensure format supports looking up the right framework for the right situation. |

### Phase 3 — Skills Review (P1)

**Milestone:** All 8 work-mode skills validated against Superpowers format — YAML frontmatter, substantive instructions, framework references.
**Depends on:** Phase 2 (vocabulary and principles inform what skills should reference).

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 20 | `todo` | Review `product-strategy/SKILL.md` | Strategic positioning, vision docs, roadmapping, market analysis. Reference strategy/FRAMEWORK.md. |
| 21 | `todo` | Review `internal-tooling/SKILL.md` | Working demos, self-running artifacts, dashboards, scoring tools. Jay's "show don't tell" mode. |
| 22 | `todo` | Review `executive-storytelling/SKILL.md` | Depth to brevity, slide structure, narrative arc, data visualization. |
| 23 | `todo` | Review `prd-writing/SKILL.md` | Problem → outcome → scope → requirements → AC. Reference execution/FRAMEWORK.md. |
| 24 | `todo` | Review `coaching-frameworks/SKILL.md` | Rubrics, maturity models, assessment templates, facilitation. Jay's "encode expertise" mode. |
| 25 | `todo` | Review `community-content/SKILL.md` | Work-context version — internal platform content, NOT pmi-buffalo persona. Clarify scope boundary. |
| 26 | `todo` | Review `gap-analysis/SKILL.md` | Current vs. target state, gap identification, prioritized recommendations. Reference prioritization/FRAMEWORK.md. |
| 27 | `todo` | Review `stakeholder-navigation/SKILL.md` | Influence mapping, stakeholder classification, engagement sequencing, resistance patterns. |

### Phase 4 — Frameworks Review (P1)

**Milestone:** All 4 frameworks validated as real step-by-step walkthroughs against PM Skills depth.
**Depends on:** Phase 2 (references inform methodology validation).

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 28 | `todo` | Review `discovery/FRAMEWORK.md` | Frame → Engage → Build Opportunity Solution Tree → Test. Teresa Torres' continuous discovery operationalized. |
| 29 | `todo` | Review `strategy/FRAMEWORK.md` | Diagnose → Policy → Actions → Stress-Test. Rumelt's kernel operationalized. |
| 30 | `todo` | Review `execution/FRAMEWORK.md` | Discuss → Plan → Execute → Verify. GSD alignment. State management practical, not aspirational. |
| 31 | `todo` | Review `prioritization/FRAMEWORK.md` | Criteria → Score → Balanced Breakthrough → Validate. Run/Improve/Transform with lifecycle-stage allocation. |

### Phase 5 — Templates & Private Template Review (P2)

**Milestone:** Templates usable as-is. Private-template scaffold produces a functional companion repo.
**Depends on:** Phase 4 (templates must align with framework workflows).

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 32 | `todo` | Review `PLAN-TEMPLATE.md` | GSD patterns. Supports execution/FRAMEWORK.md workflow. Usable as-is. |
| 33 | `todo` | Review `PHASE-TEMPLATE.md` | GSD patterns. Wave-based execution with entry/exit criteria. |
| 34 | `todo` | Review `CONTEXT-TEMPLATE.md` | GSD patterns. Scope, stakeholders, technical context, decisions, assumptions. |
| 35 | `todo` | Review `SUMMARY-TEMPLATE.md` | GSD patterns. Completion narratives with outcomes, lessons, follow-ups. |
| 36 | `todo` | Review `private-template/` scaffold | 4-file scaffold usable as starting point. Two-repo separation clearly explained. |

---

## Standalone Items

Items not part of the phased buildout but still tracked.

| # | Priority | Status | Title | Description |
|---|----------|--------|-------|-------------|
| 6b | P1 | `todo` | Create `repo-init` meta skill | Generate downstream CLAUDE.md with pointer section pre-filled |
| 6c | P1 | `todo` | Create soup-feast CLAUDE.md | Downstream pointer section per the pattern documented in CLAUDE.md |
| 37 | P2 | `todo` | Create team & leadership behaviors/mindsets reference | Markdown file defining team behaviors and mindsets + leadership behaviors and mindsets. Lives in private repo (sensitive org context). Add to private-template scaffold as a placeholder. |

---

## On Hold

| # | Priority | Title | Blocking Condition |
|---|----------|-------|--------------------|
| 9 | P0 | Build out `work/` skills with employer-specific vocabulary | Waiting on employer policy re: internal vs. public repo |
| 10 | P1 | Migrate PRD gap analysis decisions to in-repo ADRs | Waiting on private work repo creation |

---

## Completed (Pre-V1 Original Backlog)

Items #1–#8 from the original backlog, reconciled against v1 phases.

| # | Title | Disposition |
|---|-------|-------------|
| 1 | Audit `work/_persona.md` — remove employer names | Already clean |
| 2 | Add cross-repo linking pattern to CLAUDE.md | Documented in CLAUDE.md v0 |
| 3 | Add Priority + AC columns to skill backlogs | Folded into #15 |
| 4 | Add `remarkable-food-digest` + `work-summarizer` entries | Folded into #15 |
| 5 | Add skill validation conventions | Folded into #15 |
| 6 | Implement first 3 `work/` skills | Superseded by #20–#27 |
| 7 | Create ADRs | Covered by hold #10 |
| 8 | Create `docs/quality.md` | Deferred to FUT-01 |

---

## Review Guidelines

These apply to all review items in Phases 2–5:

- **Skills (#20–#27):** Validate against Superpowers SKILL.md format (YAML frontmatter, substantive instructions)
- **Frameworks (#28–#31):** Validate against PM Skills walkthrough depth (real step-by-step, not placeholders)
- **Templates (#32–#35):** Validate against GSD planning template patterns (usable as-is)
- **Jay's profile context:** Product design and delivery leader. Transformation Enablement.
  8 work modes. Systems thinker, iterative builder, craft-first, show-don't-tell.
  Key vocabulary: Team Topologies, lifecycle stages, Balanced Breakthrough, harvey balls, gearing ratio.
  Influences: Teresa Torres, Marty Cagan, Team Topologies, GSD, Superpowers, PM Skills, Rumelt, Reinertsen.

---

## Notes

- `work/` context is intentionally employer-agnostic. Employer-specific content belongs in a private repo.
- Full skill catalog (implemented + planned) lives at `.claude/SKILL-CATALOG.md`.
- Architecture references: [GSD](https://github.com/gsd-build/get-shit-done),
  [Superpowers](https://github.com/obra/superpowers), [PM Skills](https://github.com/phuryn/pm-skills).
