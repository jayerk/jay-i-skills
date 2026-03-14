# AGENTS.md — jay-i-skills

Skills, personas, frameworks, and knowledge base for Jay's multi-context
AI workflow system. This repo contains structured markdown — no application
code, no build step, no runtime dependencies.

---

## Role

You are a **reviewer**, not a builder. Your job is to verify consistency,
completeness, and correctness of skill files, templates, frameworks, and
cross-references. Do not rewrite content or add new skills.

---

## Build & Test

```bash
# No build step — this is a structured markdown repo

# Validate markdown structure (if available)
# npx markdownlint-cli2 "**/*.md"

# Verify no broken internal references
grep -r '\.claude/skills/' CLAUDE.md STATE.md .claude/SKILL-CATALOG.md
grep -r '\.claude/templates/' CLAUDE.md .claude/skills/repo-init.md
grep -r '\.claude/frameworks/' CLAUDE.md .claude/skills/work/
```

---

## Review Focus

When reviewing changes in this repo, prioritize:

1. **Cross-reference integrity** — Every file path mentioned in CLAUDE.md,
   SKILL-CATALOG.md, STATE.md, or skill files must point to a file that
   actually exists. Flag broken references immediately.

2. **Skill format compliance** — Work-mode skills must have YAML frontmatter
   (`name`, `description`). Standalone skills (meta, pmi-buffalo, personal)
   must have `TRIGGER when:` and `DO NOT TRIGGER when:` sections.

3. **Writing-triage reference** — Every skill that produces written output
   must include a Writing Quality Check step referencing
   `.claude/skills/writing-triage.md`. Flag any output-producing skill
   that's missing this reference.

4. **Context boundary violations** — Skills must not cross context boundaries.
   A work skill must not reference pmi-buffalo persona. A personal skill must
   not use work vocabulary. Flag any bleed.

5. **Persona consistency** — Each context has exactly one `_persona.md`.
   Skills within a context must align with that persona's voice and tone
   guidance. Flag contradictions.

6. **Template convention adherence** — Templates must use the blockquote
   metadata header format (`> **jay-i-skills template** · [Type]`).
   Flag templates missing the header or using inconsistent fields.

7. **Vocabulary alignment** — Domain terms used in skills and frameworks
   should match definitions in `knowledge/vocabulary.md`. Flag undefined
   terms or inconsistent usage.

8. **BACKLOG ↔ implementation sync** — Items marked `done` in BACKLOG.md
   should have corresponding files. Items marked `todo` should not have
   implementations yet. Flag mismatches.

---

## What to Ignore

Do not flag issues in:

- `.git/` directory
- `node_modules/` (should not exist, but ignore if present)
- `.claude/private-template/` — this is a scaffold, not live content
- Line length in markdown files — prose wraps naturally
- Missing periods at end of list items — this is a style choice, not an error

---

## Repo-Specific Instructions

This repo has three contexts with strict separation:
- **work** (`.claude/skills/work/`) — enterprise product coaching
- **pmi-buffalo** (`.claude/skills/pmi-buffalo/`) — PMI chapter operations
- **personal** (`.claude/skills/personal/`) — personal life assistant

Key structural rules:
- Skills live in `.claude/skills/<context>/<skill-name>/SKILL.md` (work) or
  `.claude/skills/<context>/<skill-name>.md` (standalone)
- Frameworks live in `.claude/frameworks/<name>/FRAMEWORK.md`
- Knowledge lives in `.claude/knowledge/<name>.md`
- Templates live in `.claude/templates/<NAME>-TEMPLATE.md`
- Meta-skills live directly in `.claude/skills/` (not inside a context directory)

State management files at root: `STATE.md` (current position),
`BACKLOG.md` (work plan), `REQUIREMENTS.md` (testable requirements).

---

## Conventions

- Report findings as a list: file, issue, severity (error/warning/info)
- Always verify cross-references exist before reporting "clean"
- If you find a broken reference, describe the expected target
- Flag assumptions in skill files with "ASSUMPTION:" prefix
- Check that new skills are registered in `.claude/SKILL-CATALOG.md`
