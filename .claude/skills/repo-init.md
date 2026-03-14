# repo-init

Generates a downstream repo's CLAUDE.md with the correct pointer section
pre-filled — skills repo path, context, persona, and relevant skill/design doc paths.

TRIGGER when: user says "initialize [repo] for Claude", "set up CLAUDE.md for [repo]",
"create a downstream CLAUDE.md", "point [repo] back to jay-i-skills", or is creating
a new repo that needs to reference this skills repo.

DO NOT TRIGGER when: user is editing an existing CLAUDE.md for content changes,
working inside a downstream repo on non-setup tasks, or asking about the
downstream pattern without intending to create a file.

---

## Instructions

### Step 1 — Gather repo details

Collect three pieces of information. Ask for anything the user doesn't provide:

1. **Repo name** — the downstream repo name (e.g., `soup-feast`, `work-private`)
2. **Context** — which context applies: `work`, `pmi-buffalo`, or `personal`
3. **Skills repo path** — absolute path to the local clone of jay-i-skills
   (default: ask the user, since this varies by machine)

### Step 2 — Identify relevant skills and docs

Based on the context, look up what's available:

| Context | Persona path | Skill directory |
|---------|-------------|-----------------|
| work | `.claude/skills/work/_persona.md` | `.claude/skills/work/` |
| pmi-buffalo | `.claude/skills/pmi-buffalo/_persona.md` | `.claude/skills/pmi-buffalo/` |
| personal | `.claude/skills/personal/_persona.md` | `.claude/skills/personal/` |

Ask the user which specific skills and frameworks are relevant to this repo.
Don't assume all skills apply — a soup-feast repo doesn't need executive-storytelling.

If the repo already has design docs or skill-specific files in jay-i-skills
(e.g., `.claude/skills/personal/soup-feast/`), include those paths.

### Step 3 — Determine repo-specific sections

Ask the user:
- **What does this repo contain?** (tech stack, architecture, local dev notes)
- **Any repo-specific instructions?** (build commands, test commands, conventions)
- **Codex review enabled?** (yes/no — defaults to yes for repos with code)

These go into the "Repo-Specific Context" section of the generated CLAUDE.md.
If the user doesn't have these yet, generate placeholder sections with `[TODO]` markers.

If Codex review is enabled, also collect:
- **Build command** — how to build the project (e.g., `npm run build`)
- **Test command** — how to run tests (e.g., `npm test`)
- **Lint command** — how to lint (e.g., `npm run lint`)
- **Review focus** — any repo-specific quality concerns beyond the defaults
  (e.g., accessibility, API contract stability, performance)
- **Ignore patterns** — generated/vendored directories to skip during review

### Step 4 — Generate the CLAUDE.md

Produce a complete CLAUDE.md with this structure:

```markdown
# CLAUDE.md — [Repo Name]

[One sentence describing what this repo is.]

---

## Skills & Persona (jay-i-skills)

- **Skills repo path**: `[absolute path to jay-i-skills]`
- **Context**: `[context]` — read `[persona path]` before any skill work.
- **Relevant skills**:
  - `[skill path 1]`
  - `[skill path 2]`
- **Relevant frameworks**:
  - `[framework path 1]`

Do NOT duplicate persona or skill content in this repo. Always reference
the public repo.

---

## Codex Review

This repo uses the **Claude builds, Codex reviews** pattern.
See `AGENTS.md` in this repo root for Codex review instructions.
See `codex-review.md` in jay-i-skills for the full workflow.

---

## Repo-Specific Context

[Tech stack, architecture, local dev, build/test commands — whatever
the user provided, or TODO placeholders.]
```

If Codex review is not enabled, omit the "Codex Review" section.

### Step 4b — Generate the AGENTS.md

If Codex review is enabled, also generate an `AGENTS.md` using the template
at `.claude/templates/AGENTS-TEMPLATE.md`. Fill in:

- **Repo name** — from Step 1
- **One-sentence description** — what the repo is
- **Build & test commands** — from Step 3
- **Review focus** — defaults (correctness, edge cases, security, test coverage)
  plus any repo-specific concerns from Step 3
- **Ignore patterns** — from Step 3, or sensible defaults for the tech stack
- **Repo-specific instructions** — tech stack summary, auth patterns, etc.

```markdown
# AGENTS.md — [Repo Name]

[One sentence describing what this repo is and what Codex should know about it.]

---

## Role

You are a **reviewer**, not a builder. Your job is to verify, test, and
catch issues in code written by Claude Code. Do not rewrite or refactor
unless a specific defect requires it.

---

## Build & Test

[Filled from Step 3 — exact commands]

---

## Review Focus

[Defaults + repo-specific concerns]

---

## What to Ignore

[Filled from Step 3 — generated/vendored dirs]

---

## Repo-Specific Instructions

[Tech stack, auth patterns, architecture notes]

---

## Conventions

- Report findings as a list: file, line, issue, severity (error/warning/info)
- Always run the full test suite before reporting "clean"
- If you find a defect, describe the fix but do not apply it — Claude will fix
- Flag assumptions in the code with "ASSUMPTION:" prefix
```

### Step 5 — Confirm before writing

Show the generated CLAUDE.md (and AGENTS.md if Codex is enabled) to the user and ask:
"Does this look right? I'll write these to `[repo-path]/` when you confirm."

Do NOT write files without confirmation. The pointer section is the contract
between repos — get it right.

### Step 6 — Write and verify

Write `CLAUDE.md` to the downstream repo's root.
If Codex review is enabled, also write `AGENTS.md` to the downstream repo's root.

After writing, confirm:
- The files exist at the correct paths
- The skills repo path is an absolute path (not relative)
- The persona path matches the declared context
- No skill or persona content was duplicated into the downstream repo
- If AGENTS.md was generated: build/test commands are filled in (not placeholders),
  and the Review Focus section includes repo-specific concerns

---

## Quality checks

- **No duplication** — the generated CLAUDE.md must ONLY contain pointers.
  Skills, personas, frameworks, and knowledge stay in jay-i-skills.
- **Correct persona** — the context→persona mapping must be exact. A personal
  repo must not point to work/_persona.md.
- **Absolute paths** — skills repo path must be absolute. Relative paths break
  when repos move.
- **Minimal by default** — include only the skills and frameworks the user
  confirms are relevant. Don't dump every skill path into the file.
- **AGENTS.md completeness** — if Codex review is enabled, the AGENTS.md must
  have real build/test commands (not placeholders) and at least one
  repo-specific review concern beyond the defaults. If the user can't
  provide commands yet, use `[TODO]` markers but warn that Codex review
  won't work until they're filled in.

---

## Persona note

This skill operates above all three context personas (pmi-buffalo, personal, work).
It is a meta-skill for repo scaffolding — voice should be direct and precise.
The generated CLAUDE.md is infrastructure, not prose — optimize for correctness
over readability.
