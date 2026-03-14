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

No build step — this is a structured markdown repo.

**Validate markdown structure** (if available):
```
npx markdownlint-cli2 "**/*.md"
```

**Verify internal references** — search these files for `.claude/` paths
and confirm each target exists:
- `CLAUDE.md`, `STATE.md`, `.claude/SKILL-CATALOG.md` → skill paths
- `CLAUDE.md`, `.claude/skills/repo-init.md` → template paths
- `.claude/skills/work/` → framework paths

Use your built-in file search — do not rely on shell-specific commands.

---

## Review Focus

When reviewing changes in this repo, prioritize:

1. **Cross-reference integrity** — Every file path mentioned in CLAUDE.md,
   SKILL-CATALOG.md, STATE.md, or skill files must point to a file that
   actually exists. Flag broken references immediately.

2. **Skill format compliance** — Context skills (work, pmi-buffalo, personal)
   use directory-based `SKILL.md` files with YAML frontmatter (`name`,
   `description`). Meta skills (repo-level, in `.claude/skills/` directly)
   use standalone format with `TRIGGER when:` and `DO NOT TRIGGER when:`
   sections.

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
   should match definitions in `.claude/knowledge/vocabulary.md`. Flag undefined
   terms or inconsistent usage.

8. **BACKLOG ↔ implementation sync** — Items marked `done` in BACKLOG.md
   should have corresponding files. For `todo` items, verify that any
   referenced artifacts (prompt files, templates, etc.) are consistent with
   the item's described scope. Flag missing files for done items and
   broken references in todo items.

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
- Context skills live in `.claude/skills/<context>/<skill-name>/SKILL.md`
  (directory-based with YAML frontmatter, used by work, pmi-buffalo, personal)
- Meta skills live directly in `.claude/skills/<skill-name>.md`
  (standalone format with TRIGGER/DO NOT TRIGGER)
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
