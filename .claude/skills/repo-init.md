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

These go into the "Repo-Specific Context" section of the generated CLAUDE.md.
If the user doesn't have these yet, generate placeholder sections with `[TODO]` markers.

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

## Repo-Specific Context

[Tech stack, architecture, local dev, build/test commands — whatever
the user provided, or TODO placeholders.]
```

### Step 5 — Confirm before writing

Show the generated CLAUDE.md to the user and ask:
"Does this look right? I'll write it to `[repo-path]/CLAUDE.md` when you confirm."

Do NOT write the file without confirmation. The pointer section is the contract
between repos — get it right.

### Step 6 — Write and verify

Write the file to the downstream repo's root as `CLAUDE.md`.

After writing, confirm:
- The file exists at the correct path
- The skills repo path is an absolute path (not relative)
- The persona path matches the declared context
- No skill or persona content was duplicated into the downstream repo

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

---

## Persona note

This skill operates above all three context personas (pmi-buffalo, personal, work).
It is a meta-skill for repo scaffolding — voice should be direct and precise.
The generated CLAUDE.md is infrastructure, not prose — optimize for correctness
over readability.
