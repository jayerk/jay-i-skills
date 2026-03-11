# Strategy Framework

## Purpose

A structured workflow for developing product strategy — from environmental analysis through strategic positioning to investment allocation. Produces a strategy document that can guide product decisions for 6-12 months. Based on Rumelt's "Good Strategy Bad Strategy" kernel (diagnosis, guiding policy, coherent action), adapted for internal product leadership.

## When to Use

- Setting or resetting product direction for a capability area
- Building a strategic case for investment
- Responding to a significant change in business context (reorg, new mandate, competitive shift)
- Annual or semi-annual strategic planning cycle
- When the team is building features without a clear strategic rationale

## Inputs

- Understanding of the product or capability area (lifecycle stage, maturity, team structure)
- Business context (organizational strategy, mandates, constraints)
- Discovery insights if available (user research, opportunity maps)
- Portfolio view if applicable (how this fits with adjacent products)

## Workflow

### Phase 1: Diagnose the Situation

**Goal:** Understand the current reality clearly enough to identify the strategic challenge.

**Steps:**
1. **Assess current state**
   - What does the product/capability do today?
   - What lifecycle stage is it in? (Grow / Mature / Manage / Sunset)
   - What's the current maturity across key dimensions? (Use harvey balls)
   - What team structure supports it? (Stream-aligned, platform, enabling)

2. **Map the environment**
   - What business pressures are shaping this space? (Regulatory, competitive, organizational)
   - What technology trends matter? (AI, cloud, automation, integration)
   - What peer organizations or competitors do well that we don't?
   - What internal dependencies or constraints exist?

3. **Identify the crux**
   - What is the single most important challenge or opportunity?
   - Rumelt's test: if you solve this one thing, does everything else become easier?
   - State the crux in one sentence: "The fundamental challenge is..."

**Output:** Diagnostic summary with identified crux.

### Phase 2: Develop the Guiding Policy

**Goal:** Define the strategic approach — the overall method for addressing the crux.

**Steps:**
1. **Generate strategic options** — at least 3 genuinely different approaches:
   - What if we invested heavily? (Accelerate)
   - What if we simplified radically? (Focus)
   - What if we changed the model? (Pivot)
   - What if we partnered instead of built? (Leverage)

2. **Evaluate options against criteria:**

   | Criterion | Weight | Option A | Option B | Option C |
   |-----------|--------|----------|----------|----------|
   | Addresses the crux | High | | | |
   | Feasible given constraints | High | | | |
   | Sustainable advantage | Medium | | | |
   | Time to impact | Medium | | | |
   | Risk profile | Medium | | | |
   | Team capability fit | Low | | | |

3. **Select the guiding policy** — the chosen approach, stated clearly:
   - "We will [approach] because [rationale], which means we will [implication] and we will not [exclusion]."
   - A good guiding policy excludes things. If it doesn't say no to anything, it's not a strategy.

**Output:** Guiding policy statement with supporting rationale.

### Phase 3: Define Coherent Actions

**Goal:** Translate the guiding policy into a coordinated set of actions that reinforce each other.

**Steps:**
1. **Identify strategic themes** — 3-5 areas of investment that together execute the guiding policy. Each theme should:
   - Directly support the guiding policy
   - Be distinct from other themes
   - Have clear success criteria

2. **Allocate investment using Balanced Breakthrough:**

   | Category | Description | Allocation |
   |----------|-------------|-----------|
   | **Run** | Maintain current operations, stability, compliance | X% |
   | **Improve** | Incremental improvements to existing capabilities | Y% |
   | **Transform** | Breakthrough investments aligned to strategic themes | Z% |

3. **Build the roadmap** by time horizon:
   - **Now (0-3 months):** Concrete initiatives with clear owners and deliverables
   - **Next (3-6 months):** Planned initiatives with defined scope
   - **Later (6-12 months):** Directional commitments based on strategic themes
   - **Vision (1-3 years):** Aspirational end-state — where does this product/capability need to be? Keep this to 2-3 bullet points. It's a compass, not a plan. Revisit annually.

4. **Identify the north star metric** — the single economic or outcome KPI that best represents the product's primary value driver. This is the metric that, if it moves in the right direction, means the strategy is working. Examples:
   - "Time to first portfolio review" (efficiency)
   - "% of teams using standardized scoring" (adoption)
   - "Cost per assessment cycle" (cost reduction)

   All theme-level metrics should connect back to this north star.

5. **Define success metrics** for each strategic theme:
   - Leading indicators (early signals of progress)
   - Lagging indicators (outcome measures)
   - Guardrail metrics (things that shouldn't get worse)

6. **Translate to OKRs (optional)** — When the audience expects OKR format, translate each strategic theme into an Objective + 2-3 Key Results:
   - **Objective:** Qualitative, aspirational, tied to the theme
   - **Key Results:** Measurable, time-bound, tied to the metrics defined above

   This is a formatting step, not a strategy step. The substance comes from the themes and metrics. Not every team uses OKRs yet — use this when it helps alignment, skip when it adds overhead.

**Output:** Strategic roadmap with themes, allocation, north star metric, and success metrics (optionally formatted as OKRs).

### Phase 4: Stress-Test the Strategy

**Goal:** Identify weaknesses before committing.

**Steps:**
1. **Red team the strategy:**
   - What has to be true for this to work? Are those things actually true?
   - What could make this fail? How likely are those scenarios?
   - What are competitors or peers doing differently? Why?
   - If we're wrong about the crux, what strategy would we need instead?

2. **Check for coherence:**
   - Do the actions reinforce each other or create tension?
   - Does the investment allocation match the stated priorities?
   - Can the existing team structure execute this strategy?
   - Does this strategy survive contact with the regulatory environment?

3. **Validate with stakeholders** (see `skills/stakeholder-navigation/SKILL.md`):
   - Preview with key influencers before the formal presentation
   - Address concerns before they become objections
   - Build support before requesting approval

**Output:** Risk assessment and mitigation plan.

## Output Format

```markdown
# Product Strategy: [Area/Capability]

## Diagnosis
**Crux:** [One sentence: the fundamental challenge or opportunity]

**Current State:**
- Lifecycle stage: [Grow/Mature/Manage/Sunset]
- Team structure: [Stream-aligned/Platform/Enabling]
- Key maturity gaps: [Dimensions with largest gaps]

**Environmental Context:**
[Key business, regulatory, and technology factors]

## Guiding Policy
[We will X because Y, which means we will Z and we will not W]

## North Star Metric
**[Metric name]:** [Definition and current baseline → target]

## Strategic Themes

### Theme 1: [Name]
- **Objective:** [What this achieves]
- **Key initiatives:** [What we'll do]
- **Success metrics:** [How we'll know it's working]
- **OKR (optional):** O: [Objective] / KR1: [Key Result] / KR2: [Key Result]

### Theme 2: [Name]
...

## Investment Allocation
| Category | Allocation | Key Items |
|----------|-----------|-----------|
| Run | X% | [What this covers] |
| Improve | Y% | [What this covers] |
| Transform | Z% | [What this covers] |

## Roadmap
### Now (0-3 months)
- [Initiative]: [Owner] — [Deliverable]

### Next (3-6 months)
- [Initiative]: [Scope]

### Later (6-12 months)
- [Direction]: [Strategic theme it supports]

### Vision (1-3 years)
- [Aspirational end-state bullet 1]
- [Aspirational end-state bullet 2]

## Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| [Risk] | [H/M/L] | [H/M/L] | [Action] |

## What We're Not Doing
[Explicit exclusions and rationale]
```

## Quality Checklist

- [ ] Crux is identified — one clear strategic challenge
- [ ] At least 3 strategic options were considered
- [ ] Guiding policy excludes things (says "no" to something)
- [ ] Actions are coherent — they reinforce each other
- [ ] Balanced Breakthrough allocation is explicit
- [ ] North star metric identified and connected to theme metrics
- [ ] Success metrics include leading and lagging indicators
- [ ] OKRs provided when audience expects that format
- [ ] Roadmap includes 1-3 year vision horizon
- [ ] Risks are identified with mitigations
- [ ] Strategy has been red-teamed

## Common Pitfalls

- **Strategy as goals** — "Grow 20% and improve customer satisfaction" is a goal, not a strategy. Strategy explains how.
- **Everything is a priority** — if the strategy has 10 themes, nothing is prioritized. Maximum 5 strategic themes.
- **Analysis paralysis** — spending months on diagnosis without committing to a direction. Set a timebox for each phase.
- **Ignoring constraints** — strategies that ignore regulatory, team capacity, or budget constraints aren't strategies — they're wishes.

## Product Standard Alignment

This framework serves **Pillar 3: Enduring Lifecycle** (practices 1-2) and
**Pillar 2: Measurable Economic Value** (practice 1).

| Practice | Framework Coverage | Where |
|----------|-------------------|-------|
| **Enduring Lifecycle** | | |
| 1. Measurable Outcomes | Strong | Phase 3 (success metrics — leading, lagging, guardrail) |
| — Vision for customer value | Phase 1 (current state, crux identification) | |
| — KPIs for performance monitoring | Phase 3 (metrics per strategic theme) | |
| 2. Strategy & Roadmap | Strong — core purpose of this framework | |
| — Roadmap artifact (multi-year) | Phase 3 (Now/Next/Later/Vision horizons, 0-36 months) | |
| — OKRs to align teams | Phase 3 step 6 (optional OKR translation from themes) | |
| **Measurable Economic Value** | | |
| 1. Product Economic Insights | Strong | Phase 1 (lifecycle stage, maturity assessment) |
| — Key economic KPI observability | Phase 3 step 4 (north star metric tied to primary value driver) | |
| — Leading indicators | Phase 3 (leading indicators per theme) | |

### Previously Identified Gaps — Now Closed

1. **OKR format** — ~~Themes with metrics but no OKR structure.~~ Closed: Phase 3 step 6
   adds optional OKR translation when the audience expects that format.
2. **Economic KPI focus** — ~~Metrics not anchored to primary value driver.~~ Closed: Phase 3
   step 4 adds north star metric identification before theme-level metrics.
3. **Multi-year horizon** — ~~Roadmap only covers 0-12 months.~~ Closed: Vision horizon
   (1-3 years) added to roadmap step and output template.
