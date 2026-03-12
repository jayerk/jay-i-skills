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
| 40 | `done` | Pillar 1 rubrics: Customer-Centered Product Design | 5-level harvey ball rubrics for all 3 sub-practices: Customer & Market Insights (ad-hoc signals → continuous monitoring), Segmentation & Personas (no segments → evolving cross-functional model), Customer & Employee Journeys (no mapping → journey-driven strategy). Observable behaviors + evidence at each level. |
| 41 | `done` | Pillar 2 rubrics: Measurable Economic Value | 5-level harvey ball rubrics for all 3 sub-practices: Product Economic Insights (no economic model → growth loops modeled), Value-Based Sequencing ("everything is P1" → closed-loop calibration), Value Guardrails & Realization (no guardrails → self-governing teams). Observable behaviors + evidence at each level. |
| 42 | `done` | Pillar 3 rubrics: Enduring Lifecycle | 5-level harvey ball rubrics for all 4 sub-practices: Measurable Outcomes (no vision → outcome-driven culture), Strategy & Roadmap (feature-list → living strategy), Adaptive Delivery Plans (no cadence → lifecycle-adapted delivery), Routines for Activation (no routines → self-governing cadences). Observable behaviors + evidence at each level. |

#### Wave 2 — Standard Layers (Purpose & Value, Principles, Governance)

Fleshes out the "what" for each sub-practice. Success Criteria rubric already done in Wave 1 — these items add Purpose & Value, Principles, and Governance around it.

**Pillar 1 — Customer-Centered Product Design**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 43 | `done` | Sub-practice 1: Customer & Market Insights — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Torres, Cagan, Hall, Fitzpatrick, Portigal. |
| 44 | `done` | Sub-practice 2: Segmentation & Personas — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Torres, Hall, Kalbach, Rachitsky. |
| 45 | `done` | Sub-practice 3: Customer & Employee Journeys — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Kalbach, Torres, Hall. |

**Pillar 2 — Measurable Economic Value**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 46 | `done` | Sub-practice 4: Product Economic Insights — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Perri, Reinertsen, Croll & Yoskovitz, Balfour. |
| 47 | `done` | Sub-practice 5: Value-Based Sequencing — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Reinertsen, Cutler, Perri. |
| 48 | `done` | Sub-practice 6: Value Guardrails & Realization — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Torres, Gothelf, Reinertsen. |

**Pillar 3 — Enduring Lifecycle**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 49 | `done` | Sub-practice 7: Measurable Outcomes — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Cagan, Gothelf, Wodtke. |
| 50 | `done` | Sub-practice 8: Strategy & Roadmap — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Cagan, Rumelt, Helmer. |
| 51 | `done` | Sub-practice 9: Adaptive Delivery Plans — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Vacanti, Reinertsen, Forsgren & Humble, Poppendieck. |
| 52 | `done` | Sub-practice 10: Routines for Activation — Standard layer | Purpose & Value, Principles (5), Governance. Key references: Perri, Vacanti, Forsgren & Humble. |

#### Wave 3 — How-To Layers (Execution Guidance, Applicability, Measurement, Adoption Path)

Fleshes out the "how" for each sub-practice. Each item produces all 4 How-To dimensions.

**Pillar 1 — Customer-Centered Product Design**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 53 | `done` | Sub-practice 1: Customer & Market Insights — How-To layer | All 4 dimensions. Execution Guidance references discovery/FRAMEWORK.md. Includes methods-to-questions table. |
| 54 | `done` | Sub-practice 2: Segmentation & Personas — How-To layer | All 4 dimensions. Execution Guidance references discovery/FRAMEWORK.md Phase 2. Includes segment quality check. |
| 55 | `done` | Sub-practice 3: Customer & Employee Journeys — How-To layer | All 4 dimensions. Execution Guidance references discovery/FRAMEWORK.md Phase 2-3. Includes journey map structure. |

**Pillar 2 — Measurable Economic Value**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 56 | `done` | Sub-practice 4: Product Economic Insights — How-To layer | All 4 dimensions. References strategy + prioritization frameworks. Includes economic model components table. |
| 57 | `done` | Sub-practice 5: Value-Based Sequencing — How-To layer | All 4 dimensions. References prioritization/FRAMEWORK.md (D/F/V scoring + R/I/T allocation). Includes scoring approach table. |
| 58 | `done` | Sub-practice 6: Value Guardrails & Realization — How-To layer | All 4 dimensions. References prioritization (R/I/T allocation) + strategy frameworks. Includes kill criteria template and R/I/T allocation guidance. |

**Pillar 3 — Enduring Lifecycle**

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 59 | `done` | Sub-practice 7: Measurable Outcomes — How-To layer | All 4 dimensions. References strategy/FRAMEWORK.md + discovery/FRAMEWORK.md (OST). Includes KPI structure template. |
| 60 | `done` | Sub-practice 8: Strategy & Roadmap — How-To layer | All 4 dimensions. References strategy/FRAMEWORK.md. Includes roadmap item template and OKR quality check. |
| 61 | `done` | Sub-practice 9: Adaptive Delivery Plans — How-To layer | All 4 dimensions. References execution/FRAMEWORK.md. Includes intake evaluation criteria and risk register structure. |
| 62 | `done` | Sub-practice 10: Routines for Activation — How-To layer | All 4 dimensions. References execution/FRAMEWORK.md Phase 3-4. Includes routine calendar and launch enablement tier templates. |

#### Wave 4 — Cross-Cutting

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 63 | `done` | Dependencies map | Created `frameworks/dependency-mapping/FRAMEWORK.md` (reusable framework with 4+1 dependency type taxonomy, 3-level strength scale, dependency debt concept). Applied to product standards: 23 sub-practice relationships (adoption view with 4-wave sequence) and 38 standard-level cross-references (reference view with coaching guide). Reference view includes within-sub-practice dependency appendix: 29 internal progressions, LR Mermaid diagram, starting-standard summary, 2 isolated standards (CEJ-c, ADP-e). Three Mermaid diagrams total across `knowledge/product-standards-dependencies-adoption.md` and `knowledge/product-standards-dependencies-reference.md`. Vocabulary updated with 5 new terms. |
| 64 | `todo` | Applicability master matrices | Target maturity by lifecycle stage (Concept/Launch/Growth/Maturity/Sunset) AND product type (customer-facing, internal platform, regulatory) for all 10 sub-practices. Structured so teams quickly find their row. |
| 65 | `todo` | Scorecard template | Assessment template: Sub-Practice / Current / Target / Gap / Harvey Ball / Priority Action. Include lifecycle stage and product type context fields. |
| 66 | `todo` | Universal adoption path | What getting started looks like → what good looks like at 6 months → what embedded looks like. Applies across all sub-practices. Not a change management plan — a pragmatic on-ramp. |
| 67 | `todo` | Sub-practice–to–repo map | Quick reference: for each sub-practice, the framework, primary skill, and knowledge file to load when the score is low. |

#### Wave 5 — Internal Artifact Inventory

Copilot-assisted validation of each Level 3 (Established) standard against existing internal artifacts (Confluence, SharePoint, Teams wikis). One prompt per standard. Purpose: inventory what already exists before creating anything new. Results feed into a heat map of coverage (what exists) x confidence (how complete the search was).

**Prompt files created (2026-03-12):** All 39 research prompts written to `knowledge/copilot-prompts.md`. Ready to run in M365 Copilot. Summary table at the bottom of the file awaits results.

**Pillar 1 — Customer-Centered Product Design**

*Sub-practice 1: Customer & Market Insights*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 68 | `todo` | Team talks to customers on a regular schedule (e.g., 2-3 interviews/month) | Guides, cadence definitions, or playbooks for customer research scheduling |
| 69 | `todo` | Insights are stored somewhere the team can find them | Research repositories, insight databases, tagged knowledge bases |
| 70 | `todo` | Usability testing happens before launch | Usability testing standards, checklists, or launch-gate requirements |
| 71 | `todo` | Prototypes get user feedback before the team commits to building | Prototype review processes, concept testing guides, design review gates |

*Sub-practice 2: Segmentation & Personas*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 72 | `todo` | Segments are based on what customers need or how they behave, not just who they are | Segment definitions, segmentation models, behavioral segmentation docs |
| 73 | `todo` | Personas get reviewed at least yearly | Persona documents, persona review cadence, persona governance |
| 74 | `todo` | Team references specific segments when making feature decisions | Planning templates that include segment fields, decision logs referencing segments |

*Sub-practice 3: Customer & Employee Journeys*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 75 | `todo` | Journey maps exist for key flows and get updated when things change | Journey map artifacts, journey mapping standards, update cadence docs |
| 76 | `todo` | Known pain points are in the backlog with journey context | Backlog tagging standards, journey-to-backlog linking processes |
| 77 | `todo` | A design system is in place and teams actually use it | Design system docs, component libraries, adoption tracking |

**Pillar 2 — Measurable Economic Value**

*Sub-practice 4: Product Economic Insights*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 78 | `todo` | Team knows the key economic KPIs and reviews them monthly | KPI definitions, metric review cadences, dashboard standards |
| 79 | `todo` | Unit economics are documented (cost to serve, value per transaction) | Unit economics models, cost-to-serve analyses, economic model templates |
| 80 | `todo` | Leading indicators sit alongside lagging ones | Dashboard standards that require leading indicators, metric framework docs |
| 81 | `todo` | Team can state the north star metric and explain why it matters | North star metric definitions, product strategy docs naming primary KPI |

*Sub-practice 5: Value-Based Sequencing*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 82 | `todo` | Team scores items on value, risk, and effort before sequencing | Scoring frameworks, prioritization templates, planning process docs |
| 83 | `todo` | Each item has a short value hypothesis | Value hypothesis templates, backlog item templates with hypothesis field |
| 84 | `todo` | Backlog is ranked — no ties | Backlog management standards, prioritization process docs |
| 85 | `todo` | Before committing, team checks readiness (people, dependencies, WIP) | Readiness checklists, sprint/wave commitment criteria, capacity planning docs |
| 86 | `todo` | Trade-offs are documented when items are deprioritized | Trade-off documentation standards, decision logs, "not doing" records |

*Sub-practice 6: Value Guardrails & Realization*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 87 | `todo` | Guardrails for CX, reliability, and capacity are defined and on a dashboard | SLA/SLO definitions, CX guardrail docs, reliability targets, capacity dashboards |
| 88 | `todo` | R/I/T allocation targets are set and reviewed quarterly | Run/Improve/Transform allocation docs, capacity planning templates, quarterly review materials |
| 89 | `todo` | Kill criteria are real — at least one initiative has been stopped because a trigger was hit | Kill criteria templates, initiative review processes, stop/pivot decision records |
| 90 | `todo` | Post-launch, team checks whether the value hypothesis played out | Benefits realization processes, post-launch review templates, value tracking docs |

**Pillar 3 — Enduring Lifecycle**

*Sub-practice 7: Measurable Outcomes*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 91 | `todo` | Vision says what value the product delivers to specific customers and you could check whether it's true | Product vision documents, vision templates, strategy docs with falsifiable outcomes |
| 92 | `todo` | KPIs have targets and get reviewed monthly | KPI target-setting processes, monthly review templates, metric governance docs |
| 93 | `todo` | Planning connects what the team builds to what they expect to achieve | Planning templates with outcome fields, OKR-to-backlog linking processes |
| 94 | `todo` | Both leading and lagging indicators are tracked | Dashboard standards requiring both indicator types, measurement framework docs |

*Sub-practice 8: Strategy & Roadmap*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 95 | `todo` | Roadmap organized by time horizons (Now/Next/Later) with outcomes, not just features | Roadmap templates, roadmap standards, planning process docs |
| 96 | `todo` | OKRs align to strategic themes with measurable key results | OKR templates, OKR process guides, strategic theme definitions |
| 97 | `todo` | Roadmap reviewed and updated quarterly | Roadmap review cadence docs, quarterly planning processes |
| 98 | `todo` | Team can explain how their work connects to strategy | Strategy communication templates, team alignment processes |

*Sub-practice 9: Adaptive Delivery Plans*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 99 | `todo` | Defined intake process with evaluation criteria for new work | Intake forms, request evaluation criteria, triage process docs |
| 100 | `todo` | Backlog gets refined regularly | Refinement cadence standards, backlog hygiene guides |
| 101 | `todo` | Delivery runs in waves or sprints with a predictable cadence | Sprint/wave planning docs, delivery cadence standards |
| 102 | `todo` | Risk register exists and gets reviewed at checkpoints | Risk register templates, risk management processes, checkpoint review docs |
| 103 | `todo` | Team monitors whether pace is sustainable | Capacity planning docs, velocity tracking standards, burnout/sustainability monitoring |

*Sub-practice 10: Routines for Activation*

| # | Status | Standard | Search Focus |
|---|--------|---------|-------------|
| 104 | `todo` | Regular routines with clear purpose: refinement, roadmap review, stakeholder updates, retros | Meeting standards, routine calendar templates, meeting governance docs |
| 105 | `todo` | Launch has a checklist — support, training, ops, and compliance are engaged before go-live | Launch checklists, release readiness templates, go-live process docs |
| 106 | `todo` | Cross-functional syncs happen at key milestones | Cross-functional coordination processes, milestone review templates |

#### Wave 6 — Cross-Process Alignment Research

Copilot-assisted validation of each Level 3 standard against three enterprise processes: SDLC, SPM (Strategic Portfolio Management), and I2I (Idea to Implementation). Purpose: determine where product standards are already embedded in, conflict with, or fill gaps in existing enterprise processes. Results feed into a Mermaid dependency diagram for stakeholder conversations.

**Prompt files created (2026-03-12):**
- `knowledge/sdlc-lookup-prompts.md` — 51 prompts (39 standards × SDLC + 12 phase gate prompts)
- `knowledge/spm-lookup-prompts.md` — 41 prompts (39 standards × SPM + assessment overlay + process inventory)
- `knowledge/i2i-lookup-prompts.md` — 47 prompts (39 standards × I2I + 8 phase prompts)
- `knowledge/overlap-dependency-mapping-prompt.md` — Mermaid diagram prompt (run after results collected)

| # | Status | Title | Description |
|---|--------|-------|-------------|
| 107 | `todo` | Run SDLC lookup prompts | Execute 51 prompts against SDLC SharePoint site. Fill in summary tables. |
| 108 | `todo` | Run SPM lookup prompts | Execute 41 prompts against SPM SharePoint site. Fill in summary tables including assessment overlay. |
| 109 | `todo` | Run I2I lookup prompts | Execute 47 prompts against I2I SharePoint site. Fill in summary tables. |
| 110 | `todo` | Generate overlap dependency map | Run Mermaid prompt with completed results from all four research sets. Produce stakeholder conversation artifact. |

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
