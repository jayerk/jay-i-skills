# Branding: Work Context

Visual and formatting standards for all work-context deliverables. Read this
alongside `_persona.md` — persona governs voice and tone, branding governs
visual presentation.

---

## When to Apply

Apply these standards when producing any artifact in the work context:
templates, plans, scorecards, executive summaries, coaching artifacts,
stakeholder communications. If the output could be shared with a VP,
director, or cross-functional partner, it follows these rules.

---

## Header Block

Every document starts with:

```markdown
# [Type]: [Name]

> **jay-i-skills template** · [Type]
> Date: [YYYY-MM-DD]
> Author: [Name]
> Status: [Context-appropriate status values]
```

- **Template line** identifies the system. Always present.
- **Date** uses ISO 8601 (`YYYY-MM-DD`). No "Created on" or "As of" phrasing.
- **Author** field, not "Assessed by" or "Prepared by." One term across all templates.
- **Status** values are specific to the document type — don't reuse Plan statuses on a Phase.

---

## Tables

| Rule | Standard |
|------|----------|
| Alignment | Left-align text columns. Center-align numeric, status, and level columns. |
| Headers | Sentence case. No all-caps headers. |
| Empty cells | Use `—` (em dash), not blank or `N/A`. |
| Status markers | Use words (`Complete`, `In Progress`), not symbols or emojis. |
| Harvey balls | `○ ◔ ◑ ◕ ●` — only in scorecard and maturity contexts. |

---

## Section Naming

Consistent section names across templates:

| Section | Use | Don't Use |
|---------|-----|-----------|
| TL;DR | Executive summary | Executive Summary, Abstract, Overview |
| Problem | Problem framing | Background, Introduction |
| Goal | What this achieves | Objective, Purpose (except in Phase) |
| Scope | In/out boundaries | Boundaries, Coverage |
| Risks | What might go wrong | Concerns, Issues |
| Dependencies | External blockers | Prerequisites (except in Entry Criteria) |
| Notes | Anything that doesn't fit | Appendix, Miscellaneous |

Phase template uses **Objective** (sub-document of a Plan — "Goal" would
conflict with the parent plan's Goal section).

---

## Formatting Conventions

- **Bold** for field labels in metadata blocks and inline emphasis. Not for
  entire sentences.
- **Code spans** (`like this`) for file paths, metric names, and system
  references. Not for emphasis.
- **Blockquotes** (`>`) for metadata headers and callout notes. Not for
  regular content.
- **Horizontal rules** (`---`) between major sections. Not between subsections.
- **Bullet lists** for 3+ items. Inline comma-separated for 2 items.
- **Numbered lists** only when sequence matters (steps, phases, waves).

---

## Tone in Artifacts

Per `_persona.md`, work deliverables are professional, precise, and efficient.
Specific to visual artifacts:

- **No filler intros.** Start with the information, not "This document describes..."
- **No decorative formatting.** Every bold, table, or heading earns its place.
- **Placeholder guidance in brackets.** `[2-3 sentences a VP can act on in 30 seconds]`
  — tells the user what to write, not just where to write.
- **Framework cross-references use file paths.** `frameworks/execution/FRAMEWORK.md`
  — not "see the execution framework."

---

## Employer-Specific Adaptations

These base standards are employer-agnostic. When producing artifacts for a
specific employer:

1. Check the private companion repo for org-specific branding overrides
2. Apply org header/footer if required
3. Use org terminology where it differs from generic vocabulary
4. Never put org-specific branding back into this repo

The private repo's `CLAUDE.md` should include a branding section that layers
on top of these defaults.
