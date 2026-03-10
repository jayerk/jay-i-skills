# STATE.md — jay-i-skills

Living document. Updated each session. Read this after CLAUDE.md and PROJECT.md
to understand where things stand right now.

---

## Current Position

**Phase:** 0 — Foundation Documents (P0)
**Focus:** Building the documents that define the system's identity and purpose.
These unblock all later phases.

**What exists today:**
- PROJECT.md — vision, identity, design principles, upstream influences
- REQUIREMENTS.md — 30 testable requirements across 8 capability areas
- CLAUDE.md — skill format, context isolation, downstream repo pattern (v0, pre-upgrade)
- BACKLOG.md — phased plan with 36 items across 6 phases
- README.md — minimal (needs full rewrite in item #14)
- 3 personas — work, pmi-buffalo, personal (all have `_persona.md`)
- 8 work-mode skills — all have SKILL.md files (not yet reviewed)
- 4 frameworks — discovery, strategy, prioritization, execution (not yet reviewed)
- 4 templates — plan, phase, context, summary (not yet reviewed)
- 3 knowledge files — principles, vocabulary, references (not yet reviewed)
- Private-template scaffold — 4-file starter for companion repo
- 1 slash command — `/repo-brief`
- PMI Buffalo skills — strategic-benchmark, site-audit, monthly-bite-writer, ai-writing-triage, coupon-template
- Personal skills — soup-feast app design + process flow

**What's missing from Phase 0:**
- STATE.md (this file — in progress)
- README.md upgrade (#14)

**What's missing from Phase 1:**
- CLAUDE.md v1 upgrade (#15)
- BACKLOG.md restructure (#16)

---

## Active Threads

| Thread | Status | Next Step |
|--------|--------|-----------|
| Phase 0 foundation docs | Items #11, #12 done. #13 in progress. #14 next. | Finish STATE.md, then upgrade README.md |
| Original backlog items #1, #2 | Marked `in-progress` from before v1 buildout began | Need to reconcile — either fold into v1 phases or close as superseded |

---

## Recent Decisions

| Date | Decision | Context |
|------|----------|---------|
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
