---
name: gap-analysis
description: "Gap analysis and backlog prioritization — capability assessments, opportunity mapping, backlog scoring, and investment allocation. Use this skill when evaluating current vs. desired state and deciding where to invest."
---

# Gap Analysis & Backlog Prioritization

## Overview

This skill covers the analytical work of assessing gaps between current and desired state, mapping opportunities, and prioritizing backlogs using structured frameworks. The core principle: prioritization is a first-class discipline, not a gut-feel exercise. Every prioritization decision should be defensible with explicit criteria and transparent scoring.

For the full prioritization methodology, use `frameworks/prioritization/FRAMEWORK.md`. For what good looks like, see `knowledge/references.md` → "When you need to sequence value and manage trade-offs."

Uses **Balanced Breakthrough** (Run/Improve/Transform), **Force-Rank**, **WSJF**, **Cost of Delay**, and **Harvey Balls** from `knowledge/vocabulary.md`.

## When to Use This Skill

- Assessing capability gaps across a product portfolio
- Prioritizing a backlog using structured scoring
- Mapping opportunities against effort and impact
- Allocating investment across Balanced Breakthrough categories
- Evaluating build vs. buy vs. partner decisions
- Creating a prioritized investment thesis for a portfolio

## When NOT to Use This Skill

- **Building the assessment framework** — if you need to design the rubric, maturity model, or scoring dimensions, use `coaching-frameworks`. This skill *applies* frameworks; that skill *builds* them.
- **Setting strategic direction** — if you're defining vision, guiding policy, or strategic themes, use `product-strategy`. Gap analysis informs strategy but doesn't set it.
- **Presenting results to leadership** — if the output is a deck or memo for executives, use `executive-storytelling` to frame the narrative. This skill produces the analysis; that skill communicates it.
- **Writing requirements** — if you've prioritized and now need to define what to build, use `prd-writing`.

## Quality Bar

- **Criteria are explicit** — the factors driving prioritization are named, weighted, and visible. No black-box decisions.
- **Scoring is consistent** — the same criteria produce the same score regardless of who's scoring. Rubric definitions are clear enough to calibrate.
- **Visualization aids comparison** — matrices, harvey balls, heat maps, and ranked lists make relative priority visible at a glance.
- **Balanced Breakthrough is applied** — investment allocation explicitly balances Run (maintain), Improve (incremental), and Transform (step change). The ratio is a conscious decision, not an accident. Opportunities are evaluated on Desirability, Feasibility, and Viability.
- **Assumptions are flagged** — where data is incomplete, the analysis calls it out rather than hiding uncertainty behind false precision.

## Process

### Step 1: Define the Assessment Scope
- What are we assessing? (Products, capabilities, features, teams, processes)
- What's the granularity? (Individual features vs. capability areas vs. products)
- Who consumes the output? (Product team making tactical decisions vs. leadership making investment decisions)
- What's the time horizon? (This quarter vs. this year vs. multi-year)

### Step 2: Establish the Current State
For each item being assessed:
- **Maturity level** — where is it today? Use harvey balls or a 1-5 scale with defined levels.
- **Health indicators** — what signals tell us how this is performing? (Usage, satisfaction, incidents, cost)
- **Lifecycle stage** — is this in Concept, Launch, Growth, Maturity, or Sunset?
- **Dependencies** — what does this depend on, and what depends on it?

### Step 3: Define the Desired State
- What does "good" look like for each item? Not everything needs to be a 5/5.
- What's the target maturity based on lifecycle stage and strategic importance?
- Where are the biggest gaps between current and desired state?

### Step 4: Score and Prioritize

**Scoring Framework:**

| Criterion | Weight | Scale | Definition |
|-----------|--------|-------|-----------|
| Strategic alignment | High | 1-5 | How closely does this align with stated strategy? |
| User impact | High | 1-5 | How many users are affected, how severely? |
| Effort to close gap | Medium | 1-5 | How much investment is required? (Inverse: 5 = low effort) |
| Risk of inaction | Medium | 1-5 | What happens if we don't address this? |
| Dependencies | Low | 1-5 | Does this enable or block other work? |

**Priority Score = Σ (Criterion Score × Weight)**

### Step 5: Apply Balanced Breakthrough

Allocate investment across categories:

| Category | Description | Typical Range |
|----------|-------------|---------------|
| **Run** | Keep the lights on — maintenance, stability, compliance | 30-50% |
| **Improve** | Incremental improvements to existing capabilities | 20-30% |
| **Transform** | Breakthrough investments in new capabilities | 20-40% |

The right ratio depends on lifecycle stage:
- **Concept/Launch:** Heavier on Transform (40%+)
- **Growth:** Balanced across all three
- **Maturity:** Heavier on Run (50%+)
- **Sunset:** Primarily Run with migration investment

### Step 6: Produce the Output

The gap analysis should produce:
1. **Heat map** — visual overview of all items, color-coded by gap severity
2. **Ranked priority list** — scored, sorted, with rationale for top items
3. **Investment allocation** — Balanced Breakthrough breakdown with justification
4. **Action plan** — top 5-10 items with proposed next steps and owners

## Output Format

```markdown
# Gap Analysis: [Scope]

## Executive Summary
[2-3 sentences: biggest gaps, recommended investment priorities]

## Assessment Matrix

| Item | Current | Target | Gap | Strategic Alignment | User Impact | Effort | Risk | Score |
|------|---------|--------|-----|--------------------:|------------:|-------:|-----:|------:|
| [Item 1] | ◔ | ◕ | High | 5 | 4 | 3 | 4 | [Weighted] |
| [Item 2] | ◑ | ◕ | Med | 3 | 5 | 4 | 3 | [Weighted] |

## Priority Ranking

### Tier 1: Immediate (This Quarter)
1. **[Item]** — Gap: [Current → Target]. Rationale: [Why this is highest priority]
2. **[Item]** — Gap: [Current → Target]. Rationale: [Why]

### Tier 2: Next (Next Quarter)
3. **[Item]** — [Rationale]
4. **[Item]** — [Rationale]

### Tier 3: Later (This Year)
5. **[Item]** — [Rationale]

## Balanced Breakthrough Allocation

| Category | Allocation | Key Investments |
|----------|-----------|----------------|
| Run | X% | [What this covers] |
| Improve | Y% | [What this covers] |
| Transform | Z% | [What this covers] |

**Rationale:** [Why this allocation fits the lifecycle stage and strategic context]

## Assumptions and Data Gaps
- [Assumption 1]: [Impact if wrong]
- [Data gap]: [What we don't know and how it affects the analysis]

## Recommended Next Steps
1. [Action] — [Owner] — [Timeline]
2. [Action] — [Owner] — [Timeline]
```

## Anti-Patterns

- **Prioritization by committee** — averaging everyone's opinions into mush. Use structured scoring, not voting.
- **False precision** — scoring to two decimal places when the inputs are estimates. Precision shouldn't exceed the accuracy of the data.
- **Static analysis** — doing a gap analysis once and treating it as permanent. Revisit quarterly at minimum.
- **Everything is high priority** — if everything is urgent, nothing is. Force-rank, don't tier everything into "high."
- **Ignoring lifecycle stage** — applying the same investment ratio to Growth and Sunset products. The right allocation depends on where you are.
