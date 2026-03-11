---
name: coaching-frameworks
description: "Coaching and assessment frameworks — maturity models, scoring rubrics, development plans, capability assessments. Use this skill when building structured tools that evaluate, score, and guide improvement."
---

# Coaching & Assessment Frameworks

## Overview

This skill covers the design and creation of structured assessment and coaching tools — maturity models, scoring rubrics, capability assessments, development plans, and evaluation frameworks. The core principle: subjective evaluation becomes useful when you make the criteria explicit, the scoring consistent, and the guidance actionable. Good frameworks turn individual expertise into organizational capability.

This is core **Encode Expertise** territory — embedding methodology into reusable systems. Uses **Scoring Rubric**, **Assessment Dimensions**, **Maturity Model**, and **Harvey Balls** from `knowledge/vocabulary.md`. When a framework needs to become an interactive tool (scored web app, dashboard), hand off to `internal-tooling`.

## When to Use This Skill

- Building a maturity model for a capability or team
- Creating a scoring rubric for product or team assessment
- Designing a development plan framework for product managers
- Building a capability assessment with harvey ball visualization
- Creating evaluation criteria for initiatives, products, or practices
- Designing a coaching conversation structure

## When NOT to Use This Skill

- **Gap analysis** — if you're comparing current vs. target state for a specific product or capability, use `gap-analysis`. This skill builds the *framework* for assessment; gap-analysis *applies* it.
- **PRDs and requirements** — if the output is a requirements document, use `prd-writing`.
- **Executive presentations** — if you're presenting assessment results to leadership, use `executive-storytelling` to frame the narrative.
- **Building the interactive tool** — if the framework exists and now needs to become a web app, use `internal-tooling`.

## Quality Bar

- **Dimensions are orthogonal** — each assessment dimension measures something distinct. If two dimensions always score the same, they're measuring the same thing.
- **Levels are observable** — each maturity level describes observable behaviors, not aspirational qualities. "Conducts weekly customer interviews" not "values customer feedback."
- **Scoring is calibrated** — a 3/5 means the same thing across different assessors. The rubric removes subjectivity, not judgment.
- **Harvey balls are visual** — use ○ ◔ ◑ ◕ ● (empty to full) for quick visual comparison across dimensions.
- **Guidance is actionable** — each level includes specific actions to reach the next level. Not "improve your strategy skills" but "conduct 3 competitive analyses using the framework in `frameworks/strategy/`."

## Process

### Step 1: Define the Assessment Purpose
- What are we evaluating? (Team maturity, product health, individual capability, process effectiveness)
- Who is the audience for the results? (The person being assessed, their manager, leadership, the team itself)
- What decisions will the assessment inform? (Hiring, development planning, investment allocation, team restructuring)
- How often will it be administered? (One-time, quarterly, annually)

### Step 2: Identify Dimensions
Select 5-8 dimensions that collectively describe the thing being assessed. Good dimension design:

| Principle | Example |
|-----------|---------|
| **Orthogonal** | "Discovery Practice" and "Delivery Execution" measure different things |
| **Observable** | "Conducts weekly user research" not "understands users" |
| **Actionable** | Each dimension has a clear improvement path |
| **Balanced** | Cover technical, strategic, and interpersonal aspects |

### Step 3: Define Maturity Levels
For each dimension, define 4-5 levels with clear criteria:

| Level | Harvey Ball | Meaning |
|-------|------------|---------|
| 1 — Emerging | ○ | Capability is absent or ad-hoc |
| 2 — Developing | ◔ | Some structure exists but inconsistently applied |
| 3 — Established | ◑ | Consistent practice with clear ownership |
| 4 — Advanced | ◕ | Optimizing and measuring effectiveness |
| 5 — Leading | ● | Setting the standard, teaching others, innovating |

### Step 4: Build the Scoring Rubric
For each dimension at each level, write:
- **Observable behaviors** — what someone at this level actually does
- **Evidence** — what artifacts or outcomes demonstrate this level
- **Growth actions** — specific steps to move from this level to the next

### Step 5: Design the Output
The assessment should produce:
- **Summary scorecard** — harvey ball matrix showing all dimensions at a glance
- **Dimension detail** — for each dimension, the current level, evidence, and recommended growth actions
- **Priority recommendations** — the 2-3 highest-impact improvement areas
- **Comparison view** — if assessing multiple entities, a side-by-side visual

### Step 6: Validate the Framework
- Pilot with 3-5 real assessments before broadly deploying
- Check for dimensions that always cluster (merge them)
- Check for levels that nobody hits (calibration problem)
- Get feedback from people being assessed — is it fair, clear, actionable?

## Output Format

### Maturity Model
```markdown
# [Assessment Name] Maturity Model

## Purpose
[What this assesses and why]

## Dimensions

### 1. [Dimension Name]
**Definition:** [What this dimension measures]

| Level | Harvey Ball | Criteria | Evidence | Growth Actions |
|-------|------------|----------|----------|----------------|
| Emerging | ○ | [Observable behaviors] | [Artifacts/outcomes] | [Specific steps] |
| Developing | ◔ | [Observable behaviors] | [Artifacts/outcomes] | [Specific steps] |
| Established | ◑ | [Observable behaviors] | [Artifacts/outcomes] | [Specific steps] |
| Advanced | ◕ | [Observable behaviors] | [Artifacts/outcomes] | [Specific steps] |
| Leading | ● | [Observable behaviors] | [Artifacts/outcomes] | [Specific steps] |

### 2. [Dimension Name]
...

## Scorecard Template

| Dimension | Score | Harvey Ball | Notes |
|-----------|-------|------------|-------|
| [Dim 1] | [1-5] | [○◔◑◕●] | [Key observations] |
| [Dim 2] | [1-5] | [○◔◑◕●] | [Key observations] |

## Priority Actions
1. [Highest-impact improvement area] — [Specific recommended action]
2. [Second priority] — [Specific recommended action]
3. [Third priority] — [Specific recommended action]
```

## Anti-Patterns

- **Aspirational levels** — describing what people should do instead of what they actually do at each level. Observable behaviors only.
- **Dimension bloat** — more than 8 dimensions makes the assessment unwieldy and the results unfocused. Be ruthless about what matters.
- **Score inflation** — if most assessments land at 4-5, the rubric isn't calibrated. An "Established" (3) should represent genuinely good practice.
- **Assessment without action** — scoring without providing clear, specific growth guidance. The value is in what happens after the assessment, not the score itself.
- **One-size-fits-all** — applying the same maturity model to teams at different lifecycle stages (Growth vs. Maturity). Context matters.
