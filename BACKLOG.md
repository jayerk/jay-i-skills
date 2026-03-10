# BACKLOG.md — jay-i-skills

This file tracks active and planned work for this repository.
Items are organized by priority. Each item includes a `ref:` pointing to
where the fuller context lives (design doc, PRD, decision record, or skill file).

Work through items using the `/repo-brief` skill, which reads this file
and the referenced context to produce a focused working session brief.

---

## Status Key

| Status | Meaning |
|--------|---------|
| `todo` | Ready to work |
| `in-progress` | Active Claude Code session |
| `done` | Merged to main |
| `hold` | Blocked — see notes |

---

## Priority Key

| Priority | Meaning |
|----------|---------|
| P0 | Foundational — unblocks other work |
| P1 | High value — do early |
| P2 | Important — do after P0 + P1 |

---

## Active Backlog (Original)

| # | Priority | Status | Title | Ref |
|---|----------|--------|-------|-----|
| 1 | P0 | `in-progress` | Audit `work/_persona.md` — remove any employer names | [work/_persona.md](.claude/skills/work/_persona.md) |
| 2 | P1 | `in-progress` | Add cross-repo linking pattern section to CLAUDE.md | [CLAUDE.md](CLAUDE.md) |
| 3 | P1 | `todo` | Add Priority + AC columns to all skill backlog tables in CLAUDE.md | [CLAUDE.md](CLAUDE.md) |
| 4 | P1 | `todo` | Add personal skill backlog entries: `remarkable-food-digest` + `work-summarizer` | [CLAUDE.md](CLAUDE.md) |
| 5 | P1 | `todo` | Add skill validation conventions section to CLAUDE.md | [CLAUDE.md](CLAUDE.md) |
| 6 | P1 | `todo` | Implement first 3 `work/` skills as employer-agnostic PM craft | [work/_persona.md](.claude/skills/work/_persona.md) |
| 6b | P1 | `todo` | Create `repo-init` meta skill — generate downstream CLAUDE.md with pointer section pre-filled | [CLAUDE.md](CLAUDE.md) |
| 6c | P1 | `todo` | Create soup-feast CLAUDE.md with pointer section per downstream repo pattern | [CLAUDE.md](CLAUDE.md) |
| 7 | P2 | `todo` | Create `docs/decisions/` with ADR-001 (context isolation) + ADR-002 (employer-agnostic work context) | [CLAUDE.md](CLAUDE.md) |
| 8 | P2 | `todo` | Create `docs/quality.md` — skill quality grading table | [CLAUDE.md](CLAUDE.md) |

---

## V1 Personal Operating System Buildout

Full v1 of jay-i-skills as a personal operating system repo. Architecture draws from
[GSD](https://github.com/gsd-build/get-shit-done) (context engineering, document architecture, phased planning),
[Superpowers](https://github.com/obra/superpowers) (SKILL.md format, brainstorm→spec→plan→execute→review discipline),
and [PM Skills](https://github.com/phuryn/pm-skills) (structured PM frameworks, discovery/strategy/execution taxonomy).

Most content already exists under `.claude/`. This buildout creates missing foundation documents,
upgrades README.md, and reviews all existing content against reference repo quality standards.

### Phase 0 — Foundation Documents (P0)

New files that define the system's identity and purpose. These unblock everything else.

| # | Priority | Status | Title | Description |
|---|----------|--------|-------|-------------|
| 11 | P0 | `done` | Create `PROJECT.md` | Vision, identity, what I'm building, design principles, upstream influences (GSD, Superpowers, PM Skills). Defines the "why" of this repo — a personal operating system for a product design and delivery leader. |
| 12 | P0 | `todo` | Create `REQUIREMENTS.md` | What this system needs to do — functional requirements for the repo as a product. Covers: skill invocation, persona isolation, downstream repo support, knowledge capture, framework reuse, private/public separation. |
| 13 | P0 | `todo` | Create `STATE.md` | Current position, active threads, recent decisions, parking lot. Living document updated each session — captures what's in-flight, what was just decided, and what's deferred. |
| 14 | P0 | `todo` | Upgrade `README.md` | Full repo overview: philosophy (systems thinker, iterative builder, craft-first), structure walkthrough, usage guide (how to use skills, frameworks, templates, knowledge), upstream influences, relationship to private repo. Currently minimal — needs to be the entry point for anyone encountering this repo. |

### Phase 1 — Core Documents Review (P0)

Align the two core guidance documents to the v1 vision.

| # | Priority | Status | Title | Description |
|---|----------|--------|-------|-------------|
| 15 | P0 | `todo` | Upgrade `CLAUDE.md` to v1 | Rewrite to reflect the full operating system: how Claude works with Jay (thinking style, work modes, default behaviors), reference to all available skills/frameworks/knowledge, integration with STATE.md and PROJECT.md. Currently focused on skill format and context isolation — needs to also cover Jay's thinking style, 8 work modes, and session workflow. |
| 16 | P0 | `todo` | Restructure `BACKLOG.md` as phased infrastructure plan | Transform from flat task list to phased evolution plan for the infrastructure itself. Add phase markers, dependency tracking, and milestone definitions. This item is self-referential — completing it restructures this file. |

### Phase 2 — Knowledge Base Review (P1)

Review and upgrade knowledge files for completeness and depth.

| # | Priority | Status | Title | Description |
|---|----------|--------|-------|-------------|
| 17 | P1 | `todo` | Review `knowledge/principles.md` | Validate 10 principles against full "about me" profile. Check for gaps: iterative building, showing over telling, encoding expertise into reusable systems, craft-is-not-optional. Ensure each principle has enough depth to guide Claude's behavior, not just name the concept. |
| 18 | P1 | `todo` | Review `knowledge/vocabulary.md` | Validate domain language completeness: Team Topologies terms, lifecycle stages, Balanced Breakthrough, harvey balls, gearing ratio, health models, scoring rubrics, Opportunity Solution Tree, context engineering. Add any missing terms from the 8 work modes. |
| 19 | P1 | `todo` | Review `knowledge/references.md` | Validate references list: Teresa Torres, Marty Cagan, Team Topologies, GSD, Superpowers, PM Skills, Rumelt, Reinertsen. Add any missing influences. Ensure format supports Claude looking up the right framework for the right situation. |

### Phase 3 — Skills Review (P1)

Review each of the 8 work-mode SKILL.md files against Superpowers format (YAML frontmatter with name/description, substantive instructions, not stubs). Each skill maps to one of Jay's 8 core work modes.

| # | Priority | Status | Title | Description |
|---|----------|--------|-------|-------------|
| 20 | P1 | `todo` | Review `skills/product-strategy/SKILL.md` | Work mode: product strategy & vision. Validate Superpowers format (YAML frontmatter, substantive instructions). Ensure it covers: strategic positioning, vision documents, roadmapping, market analysis. Reference strategy/FRAMEWORK.md. Check against GSD planning discipline. |
| 21 | P1 | `todo` | Review `skills/internal-tooling/SKILL.md` | Work mode: building internal tools (HTML/React single-page apps). Validate format. Ensure it covers: working demos, self-running artifacts, dashboard frameworks, scoring tools. This is Jay's "show don't tell" mode — the skill should emphasize building things that communicate by existing. |
| 22 | P1 | `todo` | Review `skills/executive-storytelling/SKILL.md` | Work mode: executive presentations & decks. Validate format. Ensure it covers: translating depth to brevity, slide structure, narrative arc for leadership audiences, data visualization guidance. |
| 23 | P1 | `todo` | Review `skills/prd-writing/SKILL.md` | Work mode: PRDs and product documentation. Validate format. Ensure it covers: problem statement → desired outcome → scope → requirements → AC. Reference execution/FRAMEWORK.md for the Discuss→Plan→Execute→Verify cycle. |
| 24 | P1 | `todo` | Review `skills/coaching-frameworks/SKILL.md` | Work mode: coaching & assessment frameworks. Validate format. Ensure it covers: scoring rubrics, assessment dimensions, maturity models, facilitation guides. This is Jay's "encode expertise so others can use it" mode. |
| 25 | P1 | `todo` | Review `skills/community-content/SKILL.md` | Work mode: community content (PMI Buffalo chapter). Validate format. Note: this is the work-context version — internal platform content and thought leadership, NOT the pmi-buffalo persona skills. Clarify scope boundary. |
| 26 | P1 | `todo` | Review `skills/gap-analysis/SKILL.md` | Work mode: gap analyses & backlog prioritization. Validate format. Ensure it covers: current vs. target state, gap identification, prioritized recommendations. Reference prioritization/FRAMEWORK.md. |
| 27 | P1 | `todo` | Review `skills/stakeholder-navigation/SKILL.md` | Work mode: stakeholder navigation & influence. Validate format. Ensure it covers: influence mapping, stakeholder classification (Champion/Sponsor/Influencer/Gatekeeper/Skeptic/Blocker), engagement sequencing, resistance patterns. |

### Phase 4 — Frameworks Review (P1)

Review each FRAMEWORK.md against PM Skills-style structured walkthrough format. Each framework should be a real step-by-step guide, not a placeholder.

| # | Priority | Status | Title | Description |
|---|----------|--------|-------|-------------|
| 28 | P1 | `todo` | Review `frameworks/discovery/FRAMEWORK.md` | Validate as real walkthrough: Frame Opportunity Space → Engage Users → Build Opportunity Solution Tree → Test and Learn. Check depth of each phase. Ensure Teresa Torres' continuous discovery is properly operationalized, not just referenced. |
| 29 | P1 | `todo` | Review `frameworks/strategy/FRAMEWORK.md` | Validate as real walkthrough: Diagnose Situation → Develop Guiding Policy → Define Coherent Actions → Stress-Test. Check that Rumelt's kernel is properly operationalized. Ensure "say no" principle is actionable. |
| 30 | P1 | `todo` | Review `frameworks/execution/FRAMEWORK.md` | Validate as real walkthrough: Discuss → Plan → Execute → Verify. Check alignment with GSD's phased planning model. Ensure state management (STATE.md, ROADMAP.md) is practical, not aspirational. |
| 31 | P1 | `todo` | Review `frameworks/prioritization/FRAMEWORK.md` | Validate as real walkthrough: Define Criteria → Score → Allocate Using Balanced Breakthrough → Validate & Communicate. Ensure Balanced Breakthrough (Run/Improve/Transform) is fully explained with lifecycle-stage allocation guidance. |

### Phase 5 — Templates & Private Template Review (P2)

Review templates against GSD-style planning template format and validate private-template scaffold.

| # | Priority | Status | Title | Description |
|---|----------|--------|-------|-------------|
| 32 | P2 | `todo` | Review `templates/PLAN-TEMPLATE.md` | Validate against GSD planning template patterns. Ensure sections support the execution/FRAMEWORK.md workflow. Should be usable as-is for any initiative. |
| 33 | P2 | `todo` | Review `templates/PHASE-TEMPLATE.md` | Validate against GSD phase template patterns. Should support wave-based execution with clear entry/exit criteria. |
| 34 | P2 | `todo` | Review `templates/CONTEXT-TEMPLATE.md` | Validate against GSD context template patterns. Should capture: scope, stakeholders, technical context, decisions, assumptions, references. |
| 35 | P2 | `todo` | Review `templates/SUMMARY-TEMPLATE.md` | Validate against GSD summary template patterns. Should support completion narratives with outcomes, lessons learned, and follow-up items. |
| 36 | P2 | `todo` | Review `private-template/` scaffold | Validate the 4-file scaffold (README.md, context/README.md, stakeholders/README.md, initiatives/README.md). Ensure it's a usable starting point for creating a private M&T-specific repo. Check that the two-repo separation (public how-to-work / private what-we're-working-on) is clearly explained. |

---

## On Hold

| # | Priority | Status | Title | Blocking Condition |
|---|----------|--------|-------|--------------------|
| 9 | P0 | `hold` | Build out `work/` skills with employer-specific vocabulary | Waiting on employer policy re: internal vs. public repo |
| 10 | P1 | `hold` | Migrate PRD gap analysis decisions to in-repo ADRs | Waiting on private work repo creation |

---

## Completed

| # | Title | Completed |
|---|-------|-----------|
| — | — | — |

---

## Notes

- `work/` context is intentionally employer-agnostic. Generic PM craft vocabulary
  belongs here. Employer-specific frameworks and tooling belong in a private internal repo.
- Branding is per-context: PMI Buffalo, personal, and work each have their own
  `_persona.md`. No shared styling at the repo root.
- Two new personal skills are queued but not yet scoped:
  `remarkable-food-digest` (food email → reMarkable magazine format) and
  `work-summarizer` (daily/weekly work digest). Build after item #4 above.
- **V1 buildout architecture references**: [GSD](https://github.com/gsd-build/get-shit-done),
  [Superpowers](https://github.com/obra/superpowers), [PM Skills](https://github.com/phuryn/pm-skills).
  Every skill review (#20–#27) should validate against Superpowers SKILL.md format.
  Every framework review (#28–#31) should validate against PM Skills walkthrough depth.
  Every template review (#32–#35) should validate against GSD planning template patterns.
- **"About me" context for all reviews**: Product design and delivery leader at a large regulated bank.
  Transformation Enablement team. 8 work modes: product strategy & vision, internal tooling (HTML/React SPAs),
  executive storytelling, PRD writing, coaching frameworks, community content (PMI Buffalo), gap analysis &
  backlog prioritization, stakeholder navigation & influence. Systems thinker, iterative builder, craft-first,
  show-don't-tell. Builds frameworks that encode expertise (scoring rubrics, assessment dimensions, gearing ratios,
  health models). Key vocabulary: Team Topologies, lifecycle stages, harvey balls, Balanced Breakthrough.
  Influences: Teresa Torres, Marty Cagan, Team Topologies, GSD, Superpowers, PM Skills.
