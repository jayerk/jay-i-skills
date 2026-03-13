# STATE.md — jay-i-skills

Living document. Updated each session. Read this after CLAUDE.md and PROJECT.md
to understand where things stand right now.

---

## Current Position

**Phase:** Phase 6 — Product Standards (P1) in progress. Wave 4 complete (#63–#67). Wave 5-6 research prompt tooling complete.
**Focus:** Wave 5 (#68–#106) — run 39 internal artifact inventory prompts via Copilot. Wave 6 (#107–#110) — run SDLC/SPM/I2I prompts. Standalone items (#6c, #38) remain.

**What exists today:**
- PROJECT.md — vision, identity, design principles, upstream influences
- REQUIREMENTS.md — 30 testable requirements across 8 capability areas
- STATE.md — this file
- BACKLOG.md — phased plan with milestones and dependency tracking
- CLAUDE.md — v1: thinking style, 8 work modes, session workflow, full system reference
- README.md — full repo overview with philosophy, structure, usage guide
- SKILL-CATALOG.md — full skill inventory extracted from CLAUDE.md
- 3 personas — work, pmi-buffalo, personal (all have `_persona.md`)
- 8 work-mode skills — all reviewed, validated, cross-referenced
- 5 frameworks — discovery, strategy, prioritization, execution, dependency-mapping (all reviewed)
- 5 templates — plan, phase, context, summary, scorecard (all reviewed)
- 4 knowledge files — principles, vocabulary, references, behaviors-mindsets (all reviewed)
- 2 dependency maps — adoption view (sub-practice level) + reference view (standard level, with within-sub-practice appendix)
- 3 applicability matrices — main (lookup + matrices + heatmap Mermaid), lifecycle view (5 stage diagrams), pillar view (3 progression diagrams)
- 1 universal adoption path — team-type-aware, assessment-driven onboarding guide with 4-wave sequencing
- 1 sub-practice-to-repo map — routing table from scorecard gaps to frameworks, skills, and knowledge files
- 5 research prompt files — copilot-prompts (39), sdlc-lookup-prompts (51), spm-lookup-prompts (41), i2i-lookup-prompts (47), overlap-dependency-mapping-prompt (1) = **178 total prompts + 1 Mermaid mapping prompt**
- Private-template scaffold — 7-file starter for companion repo (reviewed, includes CLAUDE.md and vetting prompts)
- 2 slash commands — `/repo-brief`, `/writing-triage`
- 3 meta skills — repo-brief, repo-init, writing-triage (cross-context quality gate for all output-producing skills)
- PMI Buffalo skills — strategic-benchmark, site-audit, monthly-bite-writer, coupon-template, community-content
- Personal skills — soup-feast app design + process flow

**What's next:**
- Wave 5 (#68–#106) — run 39 internal artifact inventory prompts via Copilot
- Wave 6 (#107–#110) — run SDLC/SPM/I2I prompts, generate overlap dependency map
- Standalone: #38 (template branding)

---

## Active Threads

| Thread | Status | Next Step |
|--------|--------|-----------|
| Phase 0 foundation docs | Complete. #11–#14 all done. | — |
| Phase 1 core documents | Complete. #15–#16 done. | — |
| Phase 2 knowledge base review | Complete. #17–#19 done. | — |
| Phase 3 skills review | Complete. #20–#27 all done. | — |
| Phase 4 frameworks review | Complete. #28–#31 all done. | — |
| Phase 5 templates review | Complete. #32–#36 all done. | — |
| Phase 6 Wave 4 cross-cutting | Complete. #63, #64, #65, #66, #67 all done. | — |
| Wave 5 internal artifact inventory | Prompt tooling complete (copilot-prompts.md). Items #68-#106 ready to run. | Run prompts in Copilot, fill summary table |
| Wave 6 cross-process alignment | Prompt tooling complete (SDLC, SPM, I2I, overlap mapping). Items #107-#110 ready to run. | Run prompts against enterprise SharePoint sites |
| Original backlog reconciliation | Complete. #1–#8 resolved. #6b, #6c kept as standalone todos. | — |

---

## Recent Decisions

| Date | Decision | Context |
|------|----------|---------|
| 2026-03-12 | Standalone #6c soup-feast CLAUDE.md complete. Created `.claude/skills/personal/soup-feast/CLAUDE.md` — downstream pointer with personal context persona, both design docs (app-design + process-flow), internal-tooling skill cross-reference, tech stack summary (React/Vite, Supabase, Twilio, Vercel), and key design decisions (no-login tokens, ranked-choice voting, campaign system, mobile-first). Ready to copy into soup-feast repo root when cloned. | Completes #6c |
| 2026-03-12 | Phase 6 Wave 4 #67 Sub-practice-to-repo map complete. Created `knowledge/product-standards-repo-map.md` — 10-row routing table mapping each sub-practice to its primary framework, primary skill, key knowledge files, and per-level coaching guidance (Level 1–2 entry point, Level 3 next step). Secondary skill cross-reference table covers work-mode handoffs (PRD writing for Pillar 1, executive storytelling for Pillar 2, stakeholder navigation for Pillar 3 strategy, internal tooling for Pillar 3 delivery). Cross-referenced from `product-standards.md` Dependencies section and `SCORECARD-TEMPLATE.md` Cross-References table. Completes Wave 4 — all 5 cross-cutting items done. | Completes #67, completes Phase 6 Wave 4 |
| 2026-03-12 | Phase 6 Wave 4 #66 Universal adoption path complete. Created `knowledge/product-standards-adoption.md` — team-type-aware, assessment-driven adoption guide. Team Type × Domain matrix (4 TT types × 3 domains) shapes sub-practice emphasis per team context. Capacity sizing table (constrained/moderate/full) determines how many standards per cycle. 4-wave onboarding splits each wave into starting standards (10 entry points) and expansion standards (remaining 29), with per-team-type entry point recommendations within each wave. Three horizons (Month 1-2, 6 months, embedded) with specific milestones drawn from per-sub-practice adoption paths. Stall signals at each horizon with root cause diagnosis (most trace to Wave 1 gaps). System-level embedded state describes feedback loops, self-governance, and cross-team spread. 10-row quick reference table. Cross-references to scorecard, applicability, and dependency files. |  Completes #66, advances Phase 6 Wave 4 |
| 2026-03-12 | Phase 6 Wave 4 #65 Scorecard template complete. Created `templates/SCORECARD-TEMPLATE.md` — two-level assessment template with 10-row sub-practice summary and 39-row standard-level detail section. Follows existing template conventions (blockquote metadata, TL;DR, Produces/Consumes). Includes embedded 10×5 target reference table, 5-step self-assessment instructions, scoring guide with gap interpretation and adoption wave prioritization logic, and cross-references to all product standards artifacts (rubrics, applicability matrix, dependency maps). Template is the 5th in the templates directory. | Completes #65, advances Phase 6 Wave 4 |
| 2026-03-12 | Phase 6 Wave 4 #64 Applicability master matrices complete. Created 3 files: `product-standards-applicability.md` (main — "find your row" lookup table, sub-practice qualitative matrices, standard-level target maturity matrix for 39 standards × 5 lifecycle stages × 3 product types, 3 inline heatmap Mermaid diagrams per pillar), `product-standards-applicability-lifecycle.md` (5 Mermaid diagrams showing expected vs. stretch standards per lifecycle stage), `product-standards-applicability-pillar.md` (3 Mermaid diagrams showing lifecycle progression per pillar with arc pattern analysis). Target levels derived from existing qualitative Applicability descriptions, cross-validated against maturity rubrics and adoption wave sequence. Cross-referenced from `product-standards.md` Dependencies section. | Completes #64, advances Phase 6 Wave 4 |
| 2026-03-12 | Copilot research prompt tooling complete. Created 5 prompt files (178 prompts + 1 Mermaid mapping prompt) across 4 research dimensions: internal artifacts (39 prompts in copilot-prompts.md), SDLC alignment (51 prompts in sdlc-lookup-prompts.md), SPM alignment (41 prompts in spm-lookup-prompts.md including assessment overlay), I2I alignment (47 prompts in i2i-lookup-prompts.md), and cross-process overlap dependency mapping (overlap-dependency-mapping-prompt.md). All use SharePoint site placeholders. Added Wave 6 (#107-#110) to BACKLOG.md. | Creates tooling for Waves 5-6 |
| 2026-03-12 | Phase 6 Wave 4 #63 Dependencies map complete. Created `frameworks/dependency-mapping/FRAMEWORK.md` as the 5th reusable framework — structured methodology for identifying, classifying, and visualizing dependencies with a 4+1 type taxonomy (Knowledge, Artifact, Capability, Complementary, Sequencing), 3-level strength scale (Strong/Moderate/Light), and dependency debt concept. Applied the framework to product standards: produced adoption-view map (23 sub-practice relationships, 4-wave adoption sequence) and reference-view map (38 standard-level cross-references with coaching guide). Reference view includes within-sub-practice dependency appendix (29 internal progressions, LR Mermaid diagram, starting-standard summary table, 2 isolated standards). Updated vocabulary with 5 new terms (Dependency Debt, Knowledge/Artifact/Capability/Complementary Dependency). Updated CLAUDE.md frameworks table (4→5). Added Dependencies cross-reference section to product-standards.md. | Completes #63, advances Phase 6 Wave 4 |
| 2026-03-11 | Phase 5 Templates & Private Template Review complete. All 4 templates benchmarked against external best practices (Amazon PRFAQ, RFC patterns, sprint planning best practices). Consistent fix: added upstream artifact connections (strategic theme, value hypothesis, kill criteria), framework cross-references (Produces/Consumes), problem statement sections. Plan: added Problem, strategic fields, Current→Target State, Stakeholders. Phase: added risk carry-forward, team/capacity. Context: added Problem/Strategic Context, Success Criteria, Timeline. Summary: added Problem Recap, Value Hypothesis Check, Investment comparison. Private scaffold: added CLAUDE.md (required by downstream pattern), .gitignore, archive stubs. Created 6 Copilot prompts for internal vetting. Added #38 (template branding) to backlog. V1 buildout phases all complete. | Completes #32–#36, completes Phase 5 |
| 2026-03-11 | Phase 4 Frameworks Review complete. All 4 frameworks reviewed against PM Skills walkthrough depth. Two-pass approach: first closed 14 product standard alignment gaps (personas, journey mapping, signal monitoring, OKR translation, north star metric, multi-year horizon, value hypotheses, kill criteria, flow readiness, value tracking, intake handoff, cross-functional sync, launch enablement, risk register). Then reviewed each framework: added When NOT to Use sections, vocabulary cross-references, author attributions, output format templates, fixed lifecycle stages to 5-stage model, made steps imperative. Discovery: added Portigal interview craft, Hall research method selection, actionable Phase 4. Strategy: added Helmer 7 Powers, S/M/W scoring guidance. Execution: added flow health monitoring, Definition of Ready. Prioritization: added D/F/V lens mapping, Cost of Delay reference. | Completes #28–#31, completes Phase 4 |
| 2026-03-11 | Phase 3 Skills Review complete. All 8 work-mode skills reviewed: added vocabulary callouts, When NOT to Use sections, cross-references between skills, framework pointers. Fixed Balanced Breakthrough (D/F/V prioritization vs R/I/T capitalization) across all skills. Fixed lifecycle stages to 5-stage model. community-content split into work and pmi-buffalo contexts. Added organizational strategy playbook (A-D phases) to product-strategy. Added work hierarchy grain tables. | Completes #20–#27, completes Phase 3 |
| 2026-03-11 | references.md restructured as situation-based practice index. Merged vetted canon (26 authors, priority weights) with GSD/Superpowers/PM Skills. 11 practice sections, systems/org design section, author quick-reference. Phase 2 complete. | Completes #19, completes Phase 2 |
| 2026-03-10 | CLAUDE.md v1 shipped — covers thinking style, 8 work modes, session workflow, full system reference. Skill backlogs extracted to `.claude/SKILL-CATALOG.md` | Completes Phase 1 |
| 2026-03-10 | BACKLOG.md restructured — phased plan with milestones, dependency tracking, review guidelines. Original items archived to Completed section | Completes Phase 1 |
| 2026-03-10 | Original backlog #1–#8 reconciled: #1,#2 done; #3,#4,#5 folded into #15; #6 superseded by #20–#27; #6b,#6c kept; #7 covered by #10; #8 deferred to FUT-01 | Cleans up pre-v1 items against phased plan |
| 2026-03-10 | README.md upgraded — full repo overview with philosophy, structure, usage, influences | Completes Phase 0 foundation documents |
| 2026-03-10 | REQUIREMENTS.md covers 8 capability areas with 30 v1 requirements | Needed testable criteria before reviewing existing content |
| 2026-03-10 | PROJECT.md defines 6 design principles including "Public How / Private What" | Establishes the two-repo pattern as a core architectural decision |
| 2026-03-09 | V1 buildout added to BACKLOG.md as 26 items across 6 phases | Shifted from ad-hoc task list to phased infrastructure plan |
| 2026-03-09 | `/repo-brief` added as slash command (`.claude/commands/repo-brief.md`) | Makes the skill invocable across any repo with a BACKLOG.md |
| 2026-03-08 | Work skills recovered from wrong-repo branch and merged via PR #1 | 8 skill directories, 4 frameworks, 3 knowledge files, 4 templates, private-template scaffold |

---

## Parking Lot

Items acknowledged but intentionally deferred. Not forgotten — just not now.

| Item | Why Deferred | Revisit When |
|------|-------------|--------------|
| Employer-specific work skills (#9) | Waiting on employer policy re: internal vs. public repo | Policy decision made |
| ADR migration (#10) | Needs private work repo to exist first | Private repo created |
| Original backlog items #3–#8 | Superseded by v1 buildout phases but may contain useful detail | Phase 1 begins |
| Session bridge file (continue-here.md) | Future requirement FUT-03 — useful but not v1 | V1 stable |
| Workflow chaining (multi-skill pipelines) | Future requirement FUT-04 | Skills individually reviewed |
| Automated skill quality scoring | Future requirement FUT-01 | Phase 3 skills review complete |
