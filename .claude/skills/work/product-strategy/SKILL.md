---
name: product-strategy
description: "Product strategy and vision work — market analysis, roadmap development, vision articulation, strategic positioning. Use this skill when defining where a product is going and why."
---

# Product Strategy & Vision

## Overview

This skill covers the strategic layer of product work: defining vision, analyzing markets, building roadmaps, and articulating strategic direction. The output is always a concrete artifact — a vision document, a roadmap, a strategic analysis — not a summary of what one might look like.

For the full methodology, use `frameworks/strategy/FRAMEWORK.md`. This skill defines *when* and *how well*, not the step-by-step walkthrough.

For what good looks like, see `knowledge/references.md` → "When you need to set vision and strategy."

## When to Use This Skill

- Defining or refining a product vision
- Building a strategic roadmap (outcome-focused, not feature-list)
- Analyzing competitive landscape or market positioning
- Articulating "why this, why now" for a new initiative
- Connecting product direction to business strategy
- Assessing product-market fit for internal tools
- Running the organizational strategy playbook (landscape → ideation → prioritization → execution)

## When NOT to Use This Skill

- **Tactical roadmap updates** — adding or reprioritizing items within an existing roadmap. That's `gap-analysis`.
- **PI planning or feature-level prioritization** — that's execution territory, not strategy.
- **Writing a PRD** — strategy informs the PRD, but once you're defining requirements, switch to `prd-writing`.
- **Stakeholder alignment on an existing strategy** — if the strategy exists and the task is getting buy-in, use `stakeholder-navigation`.

## Quality Bar

- **Vision statements** are specific enough to say no to things. "We help teams" is not a vision. "We reduce the cognitive load on stream-aligned product teams by providing self-service platform capabilities" is.
- **Roadmaps** are organized by outcomes, not features. Each item has a clear "so that..." connecting it to business or user value.
- **Strategic analysis** uses structured frameworks, not stream-of-consciousness — competitive matrices, opportunity mapping, capability gap assessment. Pick the right tool for the question.
- **All artifacts** use the vocabulary from `knowledge/vocabulary.md` — lifecycle stages (Concept / Launch / Growth / Maturity / Sunset), Team Topologies terms, prioritization language, work hierarchy levels.

## Organizational Strategy Playbook

The organization uses a four-phase strategy playbook. When doing strategy work in this context, map to these phases:

### A. Market Landscape & Current Positioning
Evaluate market potential, focus areas, and aspiration.
- Evaluation of market, competitive landscape, trends, and disruptions
- Evaluation of current share and performance
- Evaluation of growth areas (new markets, new segments)
- Definition of aspirational state

### B. Ideation Process / Identify Opportunities
Identify levers and ideas to achieve the stated aspiration. Informed by ideation sessions, current performance, and market trends.
- Framework for ideation including traditional ("optimize the core") and innovative ("breakout") levers — segments, geographies, partnerships, products
- Method to filter ideas and evaluate the most desirable, feasible, and viable opportunities

### C. Right to Win & Opportunity Prioritization
Identify right to win, prioritize opportunities, and assess strategic choices.
- Framework for evaluating ideas
- Evaluation of capabilities needed to deliver high-value opportunities
- Gap assessment of necessary capabilities vs. current state
- Proposed method of attaining capabilities (build / buy / partner) for strategy execution

### D. Preparing for Execution
Develop an execution roadmap to deliver the strategy in the short and long term.
- Execution roadmap with progress metrics, targets, timelines, ownership, and governance
- Accountability for progress tracking and path adjustment, including ownership of capability development needed

**Mapping to the strategy framework:** Phase A maps to Diagnosis. Phase B maps to generating strategic options. Phase C maps to Guiding Policy + Coherent Actions. Phase D maps to Roadmap + Stress-Test. See `frameworks/strategy/FRAMEWORK.md` for the detailed methodology.

## Roadmap Grain

Roadmap time horizons depend on the level you're operating at. Match the grain to the work hierarchy:

| Level | Typical Horizon | Work Items |
|-------|----------------|------------|
| Portfolio | 2–5 years | Initiatives, Portfolio Epics |
| Solution | 1–4 quarters | Solution Epics |
| ART | 1–3 quarters | Features |
| Team | 1 quarter | Stories, Tasks, Spikes |

The default Now / Next / Later structure from the strategy framework applies at any level — just scale the time windows to match.

## Output Formats

### Vision Document
```
# Product Vision: [Name]

## Current State
[Where we are today — lifecycle stage, maturity, team structure]

## Strategic Context
[Business environment, constraints, opportunities]

## Vision
[One clear paragraph: where we're going and why]

## Strategic Themes
1. [Theme] — [Outcome it drives]
2. [Theme] — [Outcome it drives]
3. [Theme] — [Outcome it drives]

## What We're Not Doing
[Explicit exclusions]

## Success Metrics
[How we know we're making progress]
```

### Strategic Roadmap
```
# Roadmap: [Product/Capability]

## Now (0-3 months)
- [Outcome]: [Initiative] — [Success metric]

## Next (3-6 months)
- [Outcome]: [Initiative] — [Success metric]

## Later (6-12 months)
- [Outcome]: [Initiative] — [Success metric]

## Balanced Breakthrough Allocation
- Run (maintain operations, stability, compliance): X%
- Improve (incremental improvements to existing capabilities): Y%
- Transform (breakthrough investments aligned to strategic themes): Z%

## Opportunity Evaluation
| Initiative | Desirability | Feasibility | Viability | R/I/T |
|-----------|-------------|-------------|-----------|-------|
| [Initiative] | [H/M/L] | [H/M/L] | [H/M/L] | [Run/Improve/Transform] |
```

**Note:** Adjust time windows to match the level. A portfolio roadmap's "Now" might be 0–6 months. A team roadmap's "Now" might be this PI.

## Anti-Patterns

- **Feature-list roadmaps** — listing features without connecting to outcomes. Every item needs a "so that..."
- **Boil-the-ocean vision** — a vision so broad it can't guide decisions. If it doesn't exclude anything, it's not a strategy.
- **Consensus-driven strategy** — strategy by committee produces mush. Take a position, support it with evidence, invite challenge.
- **Copy-paste frameworks** — applying SWOT or Porter's Five Forces mechanically without adapting to the specific context of internal product work in a regulated environment.
- **Skipping the aspiration** — jumping from current state to roadmap without defining the aspirational state. You can't close a gap you haven't defined.
- **Ignoring right to win** — prioritizing opportunities without assessing whether you have (or can build/buy/partner for) the capabilities to execute.
