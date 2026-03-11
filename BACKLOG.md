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
| 19 | `done` | Review `knowledge/references.md` | Restructured as situation-based practice index. Merged vetted canon (26 authors with priority weights) with existing GSD/Superpowers/PM Skills. 11 practice sections define "what good looks like." Architecture influences (GSD, Superpowers) separated from product practices. PM Skills positioned as foundational across all practices. Systems & org design section for non-canon influences (Team Topologies, Meadows, Bowers, Larson). |

### Phase 3 — Skills Review (P1) ✓

**Milestone:** All 8 work-mode skills validated against Superpowers format — YAML frontmatter, substantive instructions, framework references.
**Depends on:** Phase 2 (vocabulary and principles inform what skills should reference).

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 20 | `done` | Review `product-strategy/SKILL.md` | Added organizational strategy playbook (A-D phases, employer-agnostic). Added Roadmap Grain table. Fixed Balanced Breakthrough to show D/F/V prioritization + R/I/T capitalization. Added When NOT to Use, anti-patterns, vocabulary callout. Pointer to strategy/FRAMEWORK.md instead of duplicated process. |
| 21 | `done` | Review `internal-tooling/SKILL.md` | Added vocabulary connection (Working Demo, Self-Running Artifact, Encode Expertise, Operationalize). Added When NOT to Use section. Fixed React SPA stack: CRA → Vite. Added Downstream Repos section. |
| 22 | `done` | Review `executive-storytelling/SKILL.md` | Added vocabulary callout (Depth to Brevity, BLUF, Narrative Arc). Added When NOT to Use section. Added stakeholder-navigation cross-reference in Step 1. |
| 23 | `done` | Review `prd-writing/SKILL.md` | Added discovery framework and product-strategy cross-references. Added When NOT to Use section. Added Work Hierarchy Grain table (Portfolio Epic → Story). Added vocabulary connection (AC, Definition of Ready). |
| 24 | `done` | Review `coaching-frameworks/SKILL.md` | Added vocabulary callout (Encode Expertise, Scoring Rubric, Assessment Dimensions, Maturity Model, Harvey Balls). Added When NOT to Use with internal-tooling handoff. Fixed lifecycle: "Grow vs. Manage" → "Growth vs. Maturity." |
| 25 | `done` | Review `community-content/SKILL.md` | Complete rewrite: changed from PMI Buffalo chapter content to internal platform content and thought leadership. Added Transformation Enablement connection, employer-agnostic quality bar, context bleed anti-pattern. Original PMI Buffalo content moved to `pmi-buffalo/community-content/SKILL.md`. |
| 26 | `done` | Review `gap-analysis/SKILL.md` | Added prioritization framework and references.md cross-references. Fixed D/F/V vs R/I/T in quality bar. Removed WSJF (confuses people in this context). Fixed lifecycle stages throughout. Added When NOT to Use section. |
| 27 | `done` | Review `stakeholder-navigation/SKILL.md` | Added vocabulary callout (Stakeholder Map, Engagement Sequence, Breadcrumb Trails, Resistance Patterns). Added When NOT to Use section. Added executive-storytelling handoff. Kept strategy connection per Jay's feedback. |

### Phase 4 — Frameworks Review (P1) ✓

**Milestone:** All 4 frameworks validated as real step-by-step walkthroughs against PM Skills depth.
**Depends on:** Phase 2 (references inform methodology validation).

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 28 | `done` | Review `discovery/FRAMEWORK.md` | Two-pass: closed 3 product standard gaps (personas, journey mapping, signal monitoring), then reviewed for depth. Added When NOT to Use, Portigal interview craft, Hall research method selection, actionable Phase 4 with success criteria, output format template, vocabulary cross-references. |
| 29 | `done` | Review `strategy/FRAMEWORK.md` | Two-pass: closed 3 product standard gaps (OKR translation, north star metric, multi-year horizon), then reviewed for depth. Added When NOT to Use, Helmer 7 Powers for sustainable advantage, S/M/W scoring guidance, vocabulary cross-references. Fixed lifecycle stages to 5-stage model. |
| 30 | `done` | Review `execution/FRAMEWORK.md` | Two-pass: closed 4 product standard gaps (intake handoff, cross-functional sync, launch enablement, risk register), then reviewed for depth. Added When NOT to Use, Reinertsen/Vacanti flow references, Definition of Ready, flow health monitoring, vocabulary cross-references. |
| 31 | `done` | Review `prioritization/FRAMEWORK.md` | Two-pass: closed 4 product standard gaps (value hypotheses, kill criteria, flow readiness, value tracking), then reviewed for depth. Added When NOT to Use, Reinertsen/Perri author credits, D/F/V lens mapping, vocabulary cross-references. Fixed lifecycle stages to 5-stage model. |

### Phase 5 — Templates & Private Template Review (P2) ✓

**Milestone:** Templates usable as-is. Private-template scaffold produces a functional companion repo.
**Depends on:** Phase 4 (templates must align with framework workflows).

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 32 | `done` | Review `PLAN-TEMPLATE.md` | Benchmarked against Amazon PRFAQ and RFC patterns. Added Problem section, strategic theme/value hypothesis/kill criteria fields, Current→Target State, Stakeholders table. Success Metrics now connects to value hypothesis. |
| 33 | `done` | Review `PHASE-TEMPLATE.md` | Added strategic context reference, Active Risks carry-forward from parent plan, Team/Capacity table. Fixed non-standard status markers. |
| 34 | `done` | Review `CONTEXT-TEMPLATE.md` | Added Problem and Strategic Context section (problem, theme, why now), Success Criteria, Timeline/Milestones table. Follows RFC pattern of leading with "why." |
| 35 | `done` | Review `SUMMARY-TEMPLATE.md` | Added Problem Recap, Value Hypothesis Check (confirmed/disproven with evidence), Investment section (planned vs actual). Closes the loop to Prioritization Phase 5. |
| 36 | `done` | Review `private-template/` scaffold | Added CLAUDE.md scaffold (required by downstream repo pattern), .gitignore, archive/ directory stubs. Created VETTING-PROMPTS.md with 6 Copilot prompts for internal vetting. |

### Phase 6 — Product Standards (P1)

**Milestone:** `knowledge/product-standards.md` is a complete guidebook — 10 sub-practices across 3 pillars, each documented across 9 structural dimensions (4 Standard, 4 How-To, 1 Dependencies).
**Depends on:** Phase 4 (frameworks define Product Standard Alignment sections that this document codifies).

Structured in 4 waves. Wave 1 (harvey ball rubrics) ships first as the on-ramp — teams self-assess immediately, then deeper content lands with context.

Jay's refinements baked into every item:
- **Execution** → "Execution Guidance" — min viable how-to with framework pointers, not an implementation manual
- **Applicability** → organized by lifecycle stage AND product type so teams find their row
- **Measurement** → leading indicators (doing the practice?) alongside lagging (producing outcomes?)
- **Adoption** → "Adoption Path" — getting started, 6 months, embedded (not a change management plan)
- **Success Criteria** → nests 5-level maturity scale (harvey balls) for Copilot assessment workflow

#### Foundation

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 39 | `done` | Product standards skeleton | 3-pillar structure, 10 sub-practices, 9 structural dimensions, product definition. Placeholders for all sub-practices. |

#### Wave 1 — Harvey Ball Rubrics (the on-ramp)

The entry point for teams. Each item produces the 5-level maturity table (○ → ●) with observable behaviors and evidence for every sub-practice in that pillar. Teams self-assess from day one. Deeper content (Waves 2–3) builds on these rubrics.

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 40 | `todo` | Pillar 1 rubrics: Customer-Centered Product Design | 5-level harvey ball rubrics for all 3 sub-practices: Customer & Market Insights (ad-hoc signals → continuous monitoring), Segmentation & Personas (no segments → evolving cross-functional model), Customer & Employee Journeys (no mapping → journey-driven strategy). Observable behaviors + evidence at each level. |
| 41 | `todo` | Pillar 2 rubrics: Measurable Economic Value | 5-level harvey ball rubrics for all 3 sub-practices: Product Economic Insights (no economic model → growth loops modeled), Value-Based Sequencing ("everything is P1" → closed-loop calibration), Value Guardrails & Realization (no guardrails → self-governing teams). Observable behaviors + evidence at each level. |
| 42 | `todo` | Pillar 3 rubrics: Enduring Lifecycle | 5-level harvey ball rubrics for all 4 sub-practices: Measurable Outcomes (no vision → outcome-driven culture), Strategy & Roadmap (feature-list → living strategy), Adaptive Delivery Plans (no cadence → lifecycle-adapted delivery), Routines for Activation (no routines → self-governing cadences). Observable behaviors + evidence at each level. |

#### Wave 2 — Standard Layers (Purpose & Value, Principles, Governance)

Fleshes out the "what" for each sub-practice. Success Criteria rubric already done in Wave 1 — these items add Purpose & Value, Principles, and Governance around it.

**Pillar 1 — Customer-Centered Product Design**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 43 | `todo` | Sub-practice 1: Customer & Market Insights — Standard layer | Purpose & Value, Principles, Governance. Key references: Torres, Cagan, Hall, Fitzpatrick, Portigal. Scope: research insights & observability, proactive signal monitoring, iterative prototyping, usability testing & feedback. |
| 44 | `todo` | Sub-practice 2: Segmentation & Personas — Standard layer | Purpose & Value, Principles, Governance. Key references: Torres, Hall, Kalbach, Rachitsky. Scope: enduring behavioral/needs/value-based profiles, consistent personalized engagement across channels. |
| 45 | `todo` | Sub-practice 3: Customer & Employee Journeys — Standard layer | Purpose & Value, Principles, Governance. Key references: Kalbach, Torres, Hall. Scope: continuously map enduring journeys, maintain centralized accessible design system. |

**Pillar 2 — Measurable Economic Value**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 46 | `todo` | Sub-practice 4: Product Economic Insights — Standard layer | Purpose & Value, Principles, Governance. Key references: Perri, Reinertsen, Croll & Yoskovitz, Balfour. Scope: key economic KPI observability, leading indicators of product performance. |
| 47 | `todo` | Sub-practice 5: Value-Based Sequencing — Standard layer | Purpose & Value, Principles, Governance. Key references: Reinertsen, Cutler, Perri. Scope: D/F/V scoring, flow-readiness work breakdown, documented trade-offs. |
| 48 | `todo` | Sub-practice 6: Value Guardrails & Realization — Standard layer | Purpose & Value, Principles, Governance. Key references: Torres, Gothelf, Reinertsen. Scope: CX/reliability/capacity guardrails, stop/pivot/kill criteria + R/I/T allocation, benefits forecasting + value hypothesis standards. |

**Pillar 3 — Enduring Lifecycle**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 49 | `todo` | Sub-practice 7: Measurable Outcomes — Standard layer | Purpose & Value, Principles, Governance. Key references: Cagan, Gothelf, Wodtke. Scope: vision for customer value, KPIs for ongoing performance monitoring. |
| 50 | `todo` | Sub-practice 8: Strategy & Roadmap — Standard layer | Purpose & Value, Principles, Governance. Key references: Cagan, Rumelt, Helmer. Scope: multi-year roadmap artifact, OKRs to align teams. |
| 51 | `todo` | Sub-practice 9: Adaptive Delivery Plans — Standard layer | Purpose & Value, Principles, Governance. Framed thin — teams adapt to context. Key references: Vacanti, Reinertsen, Forsgren & Humble, Poppendieck. Scope: structured intake, refined backlog, proactive risk management, sustainable pace. |
| 52 | `todo` | Sub-practice 10: Routines for Activation — Standard layer | Purpose & Value, Principles, Governance. Key references: Perri, Vacanti, Forsgren & Humble. Scope: refinement/adjustment routines, communication/transparency, cross-functional touchpoints, launch enablement. |

#### Wave 3 — How-To Layers (Execution Guidance, Applicability, Measurement, Adoption Path)

Fleshes out the "how" for each sub-practice. Each item produces all 4 How-To dimensions.

**Pillar 1 — Customer-Centered Product Design**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 53 | `todo` | Sub-practice 1: Customer & Market Insights — How-To layer | Execution Guidance (pointers to discovery/FRAMEWORK.md), Applicability (by lifecycle + product type), Measurement (leading: discovery cadence adherence; lagging: decision quality from research), Adoption Path. |
| 54 | `todo` | Sub-practice 2: Segmentation & Personas — How-To layer | Execution Guidance (pointers to discovery/FRAMEWORK.md Phase 2), Applicability, Measurement, Adoption Path. |
| 55 | `todo` | Sub-practice 3: Customer & Employee Journeys — How-To layer | Execution Guidance (pointers to discovery/FRAMEWORK.md Phase 2-3), Applicability, Measurement, Adoption Path. |

**Pillar 2 — Measurable Economic Value**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 56 | `todo` | Sub-practice 4: Product Economic Insights — How-To layer | Execution Guidance (pointers to strategy + prioritization frameworks), Applicability, Measurement (leading + lagging per refinement), Adoption Path. |
| 57 | `todo` | Sub-practice 5: Value-Based Sequencing — How-To layer | Execution Guidance (pointers to prioritization/FRAMEWORK.md), Applicability, Measurement, Adoption Path. |
| 58 | `todo` | Sub-practice 6: Value Guardrails & Realization — How-To layer | Execution Guidance (pointers to prioritization + strategy frameworks), Applicability, Measurement (leading: are teams applying guardrails? lagging: are guardrails preventing drift?), Adoption Path. |

**Pillar 3 — Enduring Lifecycle**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 59 | `todo` | Sub-practice 7: Measurable Outcomes — How-To layer | Execution Guidance (pointers to strategy/FRAMEWORK.md), Applicability, Measurement, Adoption Path. |
| 60 | `todo` | Sub-practice 8: Strategy & Roadmap — How-To layer | Execution Guidance (pointers to strategy/FRAMEWORK.md), Applicability, Measurement, Adoption Path. |
| 61 | `todo` | Sub-practice 9: Adaptive Delivery Plans — How-To layer | Execution Guidance (pointers to execution/FRAMEWORK.md), Applicability, Measurement, Adoption Path. |
| 62 | `todo` | Sub-practice 10: Routines for Activation — How-To layer | Execution Guidance (pointers to execution/FRAMEWORK.md Phase 3-4), Applicability, Measurement, Adoption Path. |

#### Wave 4 — Cross-Cutting

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 63 | `todo` | Dependencies map | Prerequisite and companion relationships between all 10 sub-practices. E.g., Value-Based Sequencing requires Product Economic Insights. Prevents cherry-picking that produces incoherent adoption. Includes dependency diagram and recommended adoption sequencing. |
| 64 | `todo` | Applicability master matrices | Target maturity by lifecycle stage (Concept/Launch/Growth/Maturity/Sunset) AND product type (customer-facing, internal platform, regulatory) for all 10 sub-practices. Structured so teams quickly find their row. |
| 65 | `todo` | Scorecard template | Assessment template: Sub-Practice / Current / Target / Gap / Harvey Ball / Priority Action. Include lifecycle stage and product type context fields. |
| 66 | `todo` | Universal adoption path | What getting started looks like → what good looks like at 6 months → what embedded looks like. Applies across all sub-practices. Not a change management plan — a pragmatic on-ramp. |
| 67 | `todo` | Sub-practice–to–repo map | Quick reference: for each sub-practice, the framework, primary skill, and knowledge file to load when the score is low. |

---

## Standalone Items

Items not part of the phased buildout but still tracked.

| # | Priority | Status | Title | Description |
|---|----------|--------|-------|-------------|
| 6b | P1 | `done` | Create `repo-init` meta skill | Generate downstream CLAUDE.md with pointer section pre-filled |
| 6c | P1 | `todo` | Create soup-feast CLAUDE.md | Downstream pointer section per the pattern documented in CLAUDE.md |
| 37 | P2 | `done` | Create team & leadership behaviors/mindsets reference | Created as `knowledge/behaviors-mindsets.md` in the public repo (nothing proprietary). Four sections: team behaviors (4 categories, 16 behaviors), team mindsets (8 mindset/anti-pattern pairs), leadership behaviors (4 categories, 16 behaviors), leadership mindsets (8 mindset/anti-pattern pairs). Cross-referenced to coaching-frameworks, gap-analysis, stakeholder-navigation skills. |
| 38 | P2 | `todo` | Template branding and consistency pass | Establish consistent visual branding across all templates: header format, metadata fields, section naming conventions, table formatting, status markers. Ensures templates feel like a unified system, not independent documents. |

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
