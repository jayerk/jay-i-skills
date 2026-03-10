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

## Active Backlog

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
