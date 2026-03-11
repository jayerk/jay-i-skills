# Prioritization Framework

## Purpose

A structured workflow for making investment and sequencing decisions — what to do first, what to defer, and what to cut. Combines weighted scoring with Balanced Breakthrough allocation to produce defensible, transparent prioritization that can withstand executive scrutiny. Informed by Don Reinertsen's Cost of Delay economics (sequencing by economic impact, not opinion) and Melissa Perri's outcome-focused prioritization (*Escaping the Build Trap*).

## When to Use

- Prioritizing a product backlog with more items than capacity
- Allocating investment across a product portfolio
- Making build vs. buy vs. defer decisions
- Quarterly planning and resource allocation
- Resolving competing priorities between stakeholders

## When NOT to Use

- **No strategy exists** — if direction isn't set, do strategy first (`frameworks/strategy/FRAMEWORK.md`). Prioritizing without strategy produces a ranked list of random things.
- **Single obvious choice** — if there's clearly one thing to do and no trade-off to make, just do it
- **Stakeholder conflict disguised as prioritization** — if the real problem is organizational alignment, use `skills/stakeholder-navigation/SKILL.md` before scoring
- **Items aren't comparable** — if the list mixes strategic initiatives with bug fixes with compliance mandates, separate them first. Prioritize within categories, not across them.

## Inputs

- A list of items to prioritize (features, capabilities, initiatives, products)
- Understanding of strategic direction (from `frameworks/strategy/FRAMEWORK.md`)
- Capacity constraints (team size, budget, timeline)
- Stakeholder input on priorities (ideally structured, not just opinions)

## Workflow

### Phase 1: Define Criteria

**Goal:** Establish the factors that determine priority — before scoring anything.

**Steps:**
1. **Select scoring dimensions** — choose 4-6 criteria relevant to your context. These map to Balanced Breakthrough's D/F/V lenses (Desirability, Feasibility, Viability):

   | Criterion | D/F/V Lens | When to Use | What It Measures |
   |-----------|-----------|-------------|-----------------|
   | **Strategic alignment** | Viability | Always | How directly this supports the stated strategy |
   | **User impact** | Desirability | Always | Number and severity of users affected |
   | **Revenue/cost impact** | Viability | When quantifiable | Financial value or cost savings |
   | **Effort** | Feasibility | Always | Investment required (inverse: lower effort = higher score) |
   | **Risk of inaction** | Viability | For maintenance/compliance | Consequences of not doing this |
   | **Dependencies enabled** | Feasibility | For platform/infrastructure work | How much other work this unblocks |
   | **Time sensitivity** | Viability | For deadline-driven work | Urgency driven by external timeline |
   | **Learning value** | Desirability | For discovery/innovation work | How much we learn by doing this |

   Ensure your selected criteria cover all three lenses. A set that's all Viability with no Desirability produces a financially sound list that ignores users.

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

   | Item | Strategic (3x) | User Impact (3x) | Effort (2x) | Risk (2x) | Dependencies (1x) | Weighted Total | Value Hypothesis |
   |------|:-:|:-:|:-:|:-:|:-:|:-:|---|
   | Item A | 5 (15) | 4 (12) | 3 (6) | 4 (8) | 2 (2) | 43 | "Reduces cycle time by 40%" |
   | Item B | 3 (9) | 5 (15) | 4 (8) | 2 (4) | 5 (5) | 41 | "Unblocks 3 downstream teams" |
   | Item C | 4 (12) | 3 (9) | 5 (10) | 3 (6) | 1 (1) | 38 | "Eliminates manual step for 50 users" |

   The **Value Hypothesis** column captures the expected benefit in plain language. This is not scored — it's a testable claim that you'll revisit after delivery (see Phase 5).

3. **Discuss outliers** — where scores diverge significantly between raters, discuss:
   - What information is one rater using that another isn't?
   - Is there a definitional disagreement about the criterion?
   - Resolve divergence through discussion, not averaging

4. **Force-rank** — after scoring, create a strict rank order. No ties. If scores are close, use strategic alignment as the tiebreaker.

5. **Check flow readiness** — before finalizing the rank, flag items where the team isn't ready to absorb the work:
   - **WIP conflict:** Is the team already at capacity? Will this displace something in flight?
   - **Dependency in flight:** Does this depend on another item that hasn't shipped yet?
   - **Skill gap:** Does the team have the capability to execute this?

   Items that score high but have low readiness should be sequenced later, not dropped. Note the readiness blocker so it can be resolved.

**Output:** Scored, force-ranked priority list with value hypotheses and readiness flags.

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
   | **Launch** | 10-20% | 20-30% | 50-60% |
   | **Growth** | 20-30% | 20-30% | 40-50% |
   | **Maturity** | 30-40% | 30-40% | 20-30% |
   | **Sunset** | 60-70% | 10-20% | 10-20% (migration) |

3. **Map scored items to categories** — apply the force-ranked list within each category. Top items in each category get funded first.

4. **Check balance** — does the actual distribution match the target? If not:
   - Too much Run → are we under-investing in growth?
   - Too much Transform → are we neglecting stability?
   - Adjust by moving borderline items or renegotiating scope

5. **Set kill criteria** — for Transform and Improve items, define the conditions under which you'd stop or pivot:
   - **Time trigger:** If not delivered within [timeframe], reassess viability
   - **Adoption trigger:** If adoption is below [threshold] within [period] after launch, stop investing
   - **Value trigger:** If the value hypothesis is disproven (see Phase 2), pivot or kill

   Keep this simple — one or two sentences per item. The goal is to prevent zombie initiatives that consume resources without delivering value. Review kill criteria at each quarterly prioritization cycle.

**Output:** Investment allocation with category breakdown and kill criteria for Transform/Improve items.

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

### Phase 5: Track Value Realization

**Goal:** Close the loop — did the prioritized items deliver the value we expected?

**Steps:**
1. **Revisit value hypotheses** — at the next quarterly review, check each delivered item against its value hypothesis from Phase 2:
   - **Confirmed:** Value delivered as expected. Record the evidence.
   - **Partially confirmed:** Some value delivered but less than expected. Note what differed.
   - **Disproven:** Value hypothesis was wrong. Trigger kill criteria review if the item is ongoing.

2. **Feed back into scoring** — use realization data to calibrate future scoring:
   - Are we consistently overestimating certain types of impact?
   - Are there categories where we underestimate value?
   - Adjust criteria definitions or weights based on patterns.

3. **Update the signal log** — feed findings into Discovery's Continuous Signals practice (if the product area has one active).

**Output:** Value realization summary feeding into the next prioritization cycle.

## Output Format

```markdown
# Prioritization: [Scope]

## Scoring Criteria
| Criterion | Weight | Definition |
|-----------|--------|-----------|
| [Criterion] | [High/Med/Low] | [What each score level means] |

## Scored Priority List

| Rank | Item | R/I/T | Score | Value Hypothesis | Readiness | Kill Criteria |
|------|------|-------|-------|-----------------|-----------|---------------|
| 1 | [Item] | Transform | 43 | [Expected benefit] | Ready | [Stop condition] |
| 2 | [Item] | Improve | 41 | [Expected benefit] | Blocked: [reason] | [Stop condition] |
| 3 | [Item] | Run | 38 | [Expected benefit] | Ready | N/A |

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

## Vocabulary Cross-References

Key terms used in this framework — see `knowledge/vocabulary.md` for full definitions:

- **Balanced Breakthrough** — D/F/V for prioritization (what to do), R/I/T for capitalization (how to categorize). Allocation ratios shift by lifecycle stage.
- **Desirability / Feasibility / Viability** — the three prioritization lenses. Every opportunity should be evaluated across all three.
- **Run / Improve / Transform** — the three capitalization categories. Describes investment type, not priority.
- **Force-Rank** — strict priority order with no ties. Uses strategic alignment as tiebreaker.
- **Gearing Ratio** — effort-to-value ratio. High gearing = small effort, large impact.
- **Cost of Delay** — the economic impact of not delivering something now (Reinertsen). Makes prioritization about economics, not opinions.

## Quality Checklist

- [ ] Criteria defined and weighted before scoring begins
- [ ] Scoring calibrated with 2-3 example items
- [ ] Value hypothesis captured for each item
- [ ] Flow readiness checked — blockers flagged and sequenced
- [ ] Items force-ranked (no ties)
- [ ] Balanced Breakthrough allocation applied
- [ ] Kill criteria defined for Transform and Improve items
- [ ] Deferred items documented with rationale
- [ ] Communication artifacts tailored to each audience
- [ ] Review cadence established
- [ ] Value realization reviewed at next quarterly cycle

## Common Pitfalls

- **HiPPO prioritization** — highest-paid person's opinion overrides the framework. Use the scores. If they disagree, fix the criteria, don't override the results.
- **Scoring theater** — going through the motions without conviction. If people aren't debating scores, the criteria aren't sharp enough.
- **Static priorities** — setting priorities once and never revisiting. The world changes. So should the list.
- **Category gaming** — labeling everything "Transform" to make it sound strategic. Be honest about what's Run and Improve.
- **Effort blindness** — ignoring effort in favor of impact. A high-impact, high-effort item may be less valuable than a medium-impact, low-effort item (gearing ratio).

## Product Standard Alignment

This framework serves **Pillar 2: Measurable Economic Value** — practices to
enable data-informed teams to observe and optimize the impact of a product.

| Practice | Framework Coverage | Where |
|----------|-------------------|-------|
| **Product Economic Insights** | Moderate | Phase 1 (revenue/cost impact criterion) |
| — Key economic KPI observability | Phase 1 scoring dimension (revenue/cost) | Note: KPI creation lives in Strategy (north star metric), not Prioritization |
| — Leading indicators | Phase 5 (value realization tracking closes the loop) | Note: ongoing monitoring lives in Discovery (Continuous Signals) |
| **Value-Based Sequencing** | Strong — core purpose of this framework | |
| — Prioritization (value, risk, effort) | Phase 1 (criteria), Phase 2 (scoring) | |
| — Work breakdown with flow readiness | Phase 2 step 5 (WIP, dependency, and skill readiness check) | |
| — Documented trade-offs & rationale | Phase 4 (deferred items with rationale) | |
| **Value Guardrails & Realization** | Strong | Phase 3 (Balanced Breakthrough allocation) |
| — CX/reliability/capacity guardrails | Phase 3 (category allocation targets by lifecycle) | |
| — Stop/pivot/kill criteria | Phase 3 step 5 (time, adoption, and value kill triggers) | |
| — Benefits forecasting & value hypotheses | Phase 2 (value hypothesis column), Phase 5 (realization tracking) | |

### Previously Identified Gaps — Now Closed

1. **Benefits forecasting** — ~~Scores items but doesn't forecast value.~~ Closed: Phase 2
   adds a value hypothesis column to every scored item.
2. **Kill criteria** — ~~No explicit stop/pivot/kill triggers.~~ Closed: Phase 3 step 5
   adds simple time, adoption, and value-based kill criteria for Transform/Improve items.
3. **Flow readiness** — ~~Effort scoring ignores team readiness.~~ Closed: Phase 2 step 5
   adds WIP, dependency, and skill gap readiness checks before finalizing rank.
4. **Value tracking** — ~~No closed-loop value realization.~~ Closed: Phase 5 adds quarterly
   value hypothesis review feeding back into scoring calibration.
