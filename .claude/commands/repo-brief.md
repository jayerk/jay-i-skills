# repo-brief

Reads a repo's BACKLOG.md and its referenced context, then produces a focused
working session brief for a specific backlog item — written to teach, not just execute.

TRIGGER when: user asks to "start work on [repo]", "what should I work on next in [repo]",
"brief me on item #N", "set up my Claude Code session for [repo]", or asks for
the next task in any tracked repo.

DO NOT TRIGGER when: user is asking a general question about a skill, asking to
create a new skill, or working inside a task (not setting one up).

---

## Instructions

### Step 1 — Identify the target repo

If the user named a repo, use it. If not, ask:
"Which repo are we working in today? (jay-i-skills, soup-feast, or work repo)"

Repo → BACKLOG.md location mapping:
- `jay-i-skills` → `BACKLOG.md` at repo root (this repo)
- `soup-feast` → `BACKLOG.md` at repo root of https://github.com/jayerk/soup-feast
- `work repo` → not yet created; tell the user and stop

### Step 2 — Read the BACKLOG.md

Read the target repo's `BACKLOG.md`. Identify:
- All `todo` items, sorted by priority (P0 first)
- The top candidate item to work next (highest priority `todo`)

If the user specified an item number, use that instead.

### Step 3 — Read the referenced context

Each backlog item has a `ref:` column pointing to a file or URL.
Read that file before producing the brief.

If the ref points to a file in `jay-i-skills`, read it directly.
If the ref points to a GitHub URL, tell the user:
"I can't fetch that file directly in this session — please paste the content
of [filename] here so I can include it in your brief."

### Step 4 — Produce the working session brief

Output exactly this structure — no more, no less:

---

**Repo:** [repo name]
**Item:** #[N] — [title]
**Priority:** [P0/P1/P2]
**Estimated effort:** [Small / Medium / Large]

---

**Why this item matters**
[2–3 sentences. Explain the gap this closes and why it comes before other items.
Be specific to this repo's current state — not generic advice.]

**What you're learning by doing this**
[1–2 sentences. Name the harness engineering principle or skill this task builds.
This is the learning loop — make it explicit.]

**What done looks like**
[Bullet checklist. 3–5 items. Specific and verifiable. Not vague.]

**Before you open Claude Code**
[Any file you should read first, any decision you need to make before starting,
or any thing to confirm with the agent before it writes anything.]

**Paste this into Claude Code to start**
```
[A focused, complete starting prompt. Written in first person from the user's
perspective. Names the specific file to create or edit, the exact constraint
to follow, and asks Claude Code to show a diff or plan before writing.
Should be 3–6 sentences. Do NOT make it a wall of instructions — give
Claude Code enough context to start intelligently and ask if uncertain.]
```

---

### Step 5 — Ask what to do next

After delivering the brief, ask:
"Ready to open Claude Code with this? Or do you want to adjust anything
in the brief first?"

Do NOT automatically move to the next item. One item per session.

---

## Persona note

This skill operates above all three context personas (pmi-buffalo, personal, work).
It is a meta-skill for repo navigation — voice should be direct, practical, and
teaching-oriented. The goal is that the user leaves each session having learned
something about harness engineering, not just having shipped a file.
