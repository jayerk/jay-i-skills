---
name: community-content
description: "Internal platform content and thought leadership — community of practice posts, enablement content, internal conference talks, and practitioner-facing writing for a work audience. Use this skill when creating content that builds product practice awareness inside the organization."
---

# Community Content (Work Context)

## Overview

This skill covers creating content for internal audiences — community of practice posts, enablement articles, internal conference talks, lunch-and-learn presentations, and practitioner-facing thought leadership. The core principle: internal content should raise the bar on product practice by making good patterns visible and accessible. Give people something they can use, not just something to read.

This is an expression of **Transformation Enablement** — building awareness and capability at scale through content, not just tools and frameworks.

## When to Use This Skill

- Writing a community of practice post on a product practice topic
- Designing an internal conference talk or lunch-and-learn
- Creating enablement content (guides, how-tos, practice primers)
- Writing thought leadership for an internal audience (practitioners, leaders, coaches)
- Building a case study or success narrative for internal sharing
- Creating onboarding content for new product team members

## When NOT to Use This Skill

- **PMI Buffalo chapter content** — chapter talks, articles, and community engagement use the PMI Buffalo context at `.claude/skills/pmi-buffalo/community-content/`. Contexts never cross.
- **Executive presentations** — if the audience is senior leadership and the output is a deck or memo with a specific ask, use `executive-storytelling`.
- **PRDs and requirements** — if the output is a requirements document, use `prd-writing`.
- **Coaching artifacts** — if the output is a scored rubric, maturity model, or assessment framework, use `coaching-frameworks`. This skill might *describe* a framework; that skill *builds* it.

## Quality Bar

- **Actionable** — every piece of content includes at least one practice, pattern, or technique the reader can apply. "Here's how to run a better discovery interview" not "discovery is important."
- **Practitioner voice** — speak from experience in the domain, not from theory. Ground examples in enterprise product work and regulated environments.
- **Appropriate for the audience** — internal practitioners need depth. Don't dumb it down. But don't assume everyone has the same vocabulary — define terms on first use or point to `knowledge/vocabulary.md`.
- **Employer-agnostic** — per the work persona, do not name or assume a specific employer. Frame everything in terms of the domain (enterprise product, regulated environments).
- **Respects the reader's time** — if it can be said in 500 words, don't write 1500. Lead with the insight, support with evidence.

## Process

### Step 1: Define the Content Purpose

| Question | Why It Matters |
|----------|---------------|
| What practice are you elevating? | Ties to a specific product practice from `knowledge/references.md`. |
| Who's the audience? | Product managers, coaches, delivery leads, leadership? Shapes depth and framing. |
| What should they do differently after reading? | The actionable element. |
| What's the format? | Post (500-1000 words), talk (30/45/60 min), guide (1-3 pages), case study (1 page). |

### Step 2: Connect to the Practice Standard

Before writing, check `knowledge/references.md` for the relevant practice section. Know what good looks like according to the authors who define the standard. The content should advance people toward that standard, not just share opinions.

### Step 3: Structure the Content

**For written content (posts, guides, articles):**

1. **The insight** — lead with what the reader should know or do differently. BLUF.
2. **The context** — why this matters in enterprise product work. Ground it.
3. **The practice** — the specific pattern, technique, or approach. Be concrete.
4. **The example** — a worked example or case study showing the practice applied.
5. **The action** — what to try first. One clear next step.

**For talks and presentations:**

1. **Hook** — A relatable problem or question.
2. **Problem** — The pain the audience recognizes in their own work.
3. **Practice** — The structured approach. This is the meat.
4. **Demo** — Show the practice in action. Working tool, live example, real artifact.
5. **Takeaway** — The one thing to do differently.

For visual conventions in talks, follow the quality bar from `executive-storytelling` — one idea per slide, data not adjectives, narrative arc.

### Step 4: Design Review (Optional)

For high-impact content like conference talks or flagship practice posts, consider running the content design through a lens review using `schell-lens-review`. Lenses like Interest Curve (#69), Inherent Interest (#70), the Hook (via Surprise #4), and Resonance (#12) can sharpen how the content captures and holds audience attention.

### Step 5: Review Against the Standard

- Does the content advance a specific product practice?
- Is the actionable element clear and concrete?
- Would a senior practitioner find this credible? Would a newer practitioner find it useful?
- Is it employer-agnostic?
- Does it connect to the vocabulary and frameworks in this repo?

### Writing Quality Check

Before delivering final output, run a self-check against `.claude/skills/writing-triage.md`. Correct any flagged AI writing signals — structural repetition, vague generalities, voice uniformity, missing experiential detail. The output should read as practitioner-written, not machine-generated.

## Output Formats

### Practice Post

```markdown
# [Headline — specific and actionable]

**TL;DR:** [One sentence: what to do differently and why]

## The Insight
[2-3 paragraphs: what the reader should know]

## In Practice
[The specific pattern or technique, with a worked example]

## Try This
[One concrete action the reader can take this week]

## Go Deeper
[Pointers to references, frameworks, or tools]
```

### Internal Talk Outline

```markdown
# [Talk Title]

## Meta
- **Event:** [Internal conference / lunch-and-learn / CoP session]
- **Duration:** [Minutes]
- **Audience:** [Product managers / coaches / delivery leads]
- **One takeaway:** [The single thing they should remember]

## Narrative Arc

### Hook (2 min)
[Relatable problem or question]

### Problem (5 min)
[The practice gap the audience recognizes]

### Practice (15 min)
[The structured approach — steps, patterns, model]

### Demo (10 min)
[Live demonstration — tool, assessment, worked example]

### Takeaway (5 min)
[The one thing to do differently + resource link]
```

## Anti-Patterns

- **Theory without practice** — presenting concepts without showing how to apply them. Always include a "try this" element.
- **Consultant voice** — writing like an external advisor, not a peer practitioner. Internal content earns trust through shared context.
- **Framework tourism** — name-dropping five frameworks in one post without going deep on any of them. Pick one, make it usable.
- **No follow-up** — sharing a great practice with no way for the reader to go deeper. Always link to resources, tools, or frameworks.
- **Context bleed** — using PMI Buffalo examples or chapter framing in work content. These are different audiences with different needs.
