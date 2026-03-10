# Prioritization Framework

## Purpose

A structured workflow for making investment and sequencing decisions — what to do first, what to defer, and what to cut. Combines weighted scoring with Balanced Breakthrough allocation to produce defensible, transparent prioritization that can withstand executive scrutiny.

## When to Use

- Prioritizing a product backlog with more items than capacity
- Allocating investment across a product portfolio
- Making build vs. buy vs. defer decisions
- Quarterly planning and resource allocation
- Resolving competing priorities between stakeholders

## Inputs

- A list of items to prioritize (features, capabilities, initiatives, products)
- Understanding of strategic direction (from `frameworks/strategy/FRAMEWORK.md`)
- Capacity constraints (team size, budget, timeline)
- Stakeholder input on priorities (ideally structured, not just opinions)

## Workflow

### Phase 1: Define Criteria

**Goal:** Establish the factors that determine priority — before scoring anything.

**Steps:**
1. **Select scoring dimensions** — choose 4-6 criteria relevant to your context:

   | Criterion | When to Use | What It Measures |
   |-----------|-------------|-----------------|
   | **Strategic alignment** | Always | How directly this supports the stated strategy |
   | **User impact** | Always | Number and severity of users affected |
   | **Revenue/cost impact** | When quantifiable | Financial value or cost savings |
   | **Effort** | Always | Investment required (inverse: lower effort = higher score) |
   | **Risk of inaction** | For maintenance/compliance | Consequences of not doing this |
   | **Dependencies enabled** | For platform/infrastructure work | How much other work this unblocks |
   | **Time sensitivity** | For deadline-driven work | Urgency driven by external timeline |
   | **Learning value** | For discovery/innovation work | How much we learn by doing this |

2. **Assign weights** — not all criteria matter equally. Use a simple weighting:
   - **High (3x):** The criteria that most matter for this decision
   - **Medium (2x):** Important but not dominant
   - **Low (1x):** Relevant but secondary

3. **Define the scale** — for each criterion, define what each score means:

   | Score | Meaning |
   |-------|---------|
   | 1 | Minimal — barely relevant or very high effort |
   | 2 | Low — some relevance or high effort |
   | 3 | Moderate — meaningful impact, reasonable effort |
   | 4 | High — significant impact, manageable effort |
   | 5 | Critical — essential to strategy, high impact, or very low effort |

4. **Calibrate** — score 2-3 items together with stakeholders to align on what a "3" vs. a "4" means. This step prevents scoring drift.

**Output:** Scoring criteria with weights and calibrated definitions.

### Phase 2: Score

**Goal:** Rate every item against every criterion.

**Steps:**
1. **Score independently first** — if multiple people are scoring, have each person score independently before discussing. This prevents anchoring bias.

2. **Build the scoring matrix:**

   | Item | Strategic (3x) | User Impact (3x) | Effort (2x) | Risk (2x) | Dependencies (1x) | Weighted Total |
   |------|:-:|:-:|:-:|:-:|:-:|:-:|
   | Item A | 5 (15) | 4 (12) | 3 (6) | 4 (8) | 2 (2) | 43 |
   | Item B | 3 (9) | 5 (15) | 4 (8) | 2 (4) | 5 (5) | 41 |
   | Item C | 4 (12) | 3 (9) | 5 (10) | 3 (6) | 1 (1) | 38 |

3. **Discuss outliers** — where scores diverge significantly between raters, discuss:
   - What information is one rater using that another isn't?
   - Is there a definitional disagreement about the criterion?
   - Resolve divergence through discussion, not averaging

4. **Force-rank** — after scoring, create a strict rank order. No ties. If scores are close, use strategic alignment as the tiebreaker.

**Output:** Scored, force-ranked priority list.

### Phase 3: Allocate Using Balanced Breakthrough

**Goal:** Distribute investment across categories to balance stability with growth.

**Steps:**
1. **Classify each item:**

   | Category | Definition | Examples |
   |----------|-----------|---------|
   | **Run** | Keep current operations stable and compliant | Bug fixes, compliance updates, maintenance, operational support |
   | **Improve** | Make existing capabilities meaningfully better | Performance optimization, UX improvements, automation of manual processes |
   | **Transform** | Create new capabilities or step-change improvements | New products, major architecture changes, new market entry |

2. **Set the target allocation** — based on lifecycle stage:

   | Lifecycle Stage | Run | Improve | Transform |
   |----------------|-----|---------|-----------|
   | **Grow** | 20-30% | 20-30% | 40-50% |
   | **Mature** | 30-40% | 30-40% | 20-30% |
   | **Manage** | 50-60% | 20-30% | 10-20% |
   | **Sunset** | 60-70% | 10-20% | 10-20% (migration) |

3. **Map scored items to categories** — apply the force-ranked list within each category. Top items in each category get funded first.

4. **Check balance** — does the actual distribution match the target? If not:
   - Too much Run → are we under-investing in growth?
   - Too much Transform → are we neglecting stability?
   - Adjust by moving borderline items or renegotiating scope

**Output:** Investment allocation with category breakdown.

### Phase 4: Validate and Communicate

**Goal:** Ensure the prioritization is defensible and clearly communicated.

**Steps:**
1. **Sanity check** — does the final list feel right? If the structured scoring produces a result that feels wrong, investigate:
   - Are the criteria right?
   - Are the weights right?
   - Is there a factor you're not capturing?
   - (Don't just override — fix the framework)

2. **Build the communication artifact:**
   - **For leadership:** Priority tiers with Balanced Breakthrough allocation (see `skills/executive-storytelling/SKILL.md`)
   - **For teams:** Detailed priority list with rationale for sequencing
   - **For stakeholders:** "Your request is in Tier [X] because [criteria-based rationale]"

3. **Document what was cut and why** — transparency about what's not being done is as important as what is. Every deferred item should have a one-line rationale.

4. **Set the review cadence** — priorities should be revisited:
   - Quarterly for portfolio-level allocation
   - Monthly for backlog-level prioritization
   - Ad-hoc when significant new information arrives

**Output:** Prioritized plan with communication artifacts.

## Output Format

```markdown
# Prioritization: [Scope]

## Scoring Criteria
| Criterion | Weight | Definition |
|-----------|--------|-----------|
| [Criterion] | [High/Med/Low] | [What each score level means] |

## Scored Priority List

| Rank | Item | Run/Improve/Transform | Score | Key Rationale |
|------|------|--------------------|-------|---------------|
| 1 | [Item] | Transform | 43 | [Why it's #1] |
| 2 | [Item] | Improve | 41 | [Why it's #2] |
| 3 | [Item] | Run | 38 | [Why it's #3] |

## Balanced Breakthrough Allocation
| Category | Target | Actual | Items |
|----------|--------|--------|-------|
| Run | X% | Y% | [List] |
| Improve | X% | Y% | [List] |
| Transform | X% | Y% | [List] |

## What We're Not Doing (This Cycle)
| Item | Score | Reason Deferred |
|------|-------|----------------|
| [Item] | [Score] | [Rationale] |

## Review Schedule
- Next review: [Date]
- Trigger for ad-hoc review: [Conditions]
```

## Quality Checklist

- [ ] Criteria defined and weighted before scoring begins
- [ ] Scoring calibrated with 2-3 example items
- [ ] Items force-ranked (no ties)
- [ ] Balanced Breakthrough allocation applied
- [ ] Deferred items documented with rationale
- [ ] Communication artifacts tailored to each audience
- [ ] Review cadence established

## Common Pitfalls

- **HiPPO prioritization** — highest-paid person's opinion overrides the framework. Use the scores. If they disagree, fix the criteria, don't override the results.
- **Scoring theater** — going through the motions without conviction. If people aren't debating scores, the criteria aren't sharp enough.
- **Static priorities** — setting priorities once and never revisiting. The world changes. So should the list.
- **Category gaming** — labeling everything "Transform" to make it sound strategic. Be honest about what's Run and Improve.
- **Effort blindness** — ignoring effort in favor of impact. A high-impact, high-effort item may be less valuable than a medium-impact, low-effort item (gearing ratio).
