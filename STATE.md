# STATE.md — jay-i-skills

Living document. Updated each session. Read this after CLAUDE.md and PROJECT.md
to understand where things stand right now.

---

## Current Position

**Phase:** Phase 2 — Knowledge Base Review (P1) complete. Phase 3 — Skills Review is next.
**Focus:** Validating 8 work-mode skills against Superpowers format.

**What exists today:**
- PROJECT.md — vision, identity, design principles, upstream influences
- REQUIREMENTS.md — 30 testable requirements across 8 capability areas
- STATE.md — this file
- BACKLOG.md — phased plan with milestones and dependency tracking
- CLAUDE.md — v1: thinking style, 8 work modes, session workflow, full system reference
- README.md — full repo overview with philosophy, structure, usage guide
- SKILL-CATALOG.md — full skill inventory extracted from CLAUDE.md
- 3 personas — work, pmi-buffalo, personal (all have `_persona.md`)
- 8 work-mode skills — all have SKILL.md files (not yet reviewed)
- 4 frameworks — discovery, strategy, prioritization, execution (not yet reviewed)
- 4 templates — plan, phase, context, summary (not yet reviewed)
- 3 knowledge files — principles, vocabulary, references (not yet reviewed)
- Private-template scaffold — 4-file starter for companion repo
- 1 slash command — `/repo-brief`
- PMI Buffalo skills — strategic-benchmark, site-audit, monthly-bite-writer, ai-writing-triage, coupon-template
- Personal skills — soup-feast app design + process flow

**What's next (Phase 3):**
- #20 — Review `product-strategy/SKILL.md`
- #21 — Review `internal-tooling/SKILL.md`
- #22 — Review `executive-storytelling/SKILL.md`
- #23 — Review `prd-writing/SKILL.md`
- #24 — Review `coaching-frameworks/SKILL.md`
- #25 — Review `community-content/SKILL.md`
- #26 — Review `gap-analysis/SKILL.md`
- #27 — Review `stakeholder-navigation/SKILL.md`

---

## Active Threads

| Thread | Status | Next Step |
|--------|--------|-----------|
| Phase 0 foundation docs | Complete. #11–#14 all done. | — |
| Phase 1 core documents | Complete. #15–#16 done. | — |
| Phase 2 knowledge base review | Complete. #17–#19 done. | Move to Phase 3 |
| Original backlog reconciliation | Complete. #1–#8 resolved. #6b, #6c kept as standalone todos. | — |

---

## Recent Decisions

| Date | Decision | Context |
|------|----------|---------|
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
