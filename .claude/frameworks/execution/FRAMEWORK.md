# Execution Framework

## Purpose

A structured workflow for translating strategy and requirements into delivered, validated outcomes. Covers the cycle from planning through delivery through verification. Draws from GSD's phased planning model, adapted for product leadership work (not just software delivery).

## When to Use

- Breaking down a strategic initiative into executable work
- Planning a quarter's worth of product work
- Running a delivery cycle on a defined initiative
- Recovering a stalled project that needs structure
- Coordinating work across multiple teams or workstreams

## Inputs

- Strategic direction (from `frameworks/strategy/FRAMEWORK.md`)
- Prioritized items with value hypotheses and kill criteria (from `frameworks/prioritization/FRAMEWORK.md`)
- Requirements or PRD (from `skills/prd-writing/SKILL.md`)
- Team capacity and constraints
- Dependencies and integration points

### Intake Handoff

Execution assumes work has been through Discovery → Strategy → Prioritization. The handoff into Execution should include:

1. **Prioritization output** — ranked item with score, value hypothesis, readiness status, and kill criteria
2. **PRD or requirements** — scope, acceptance criteria, constraints
3. **Strategic context** — which theme this supports and why it was prioritized now

If any of these are missing, go back to the appropriate framework before proceeding. Execution without prioritized, scoped work creates churn.

## Workflow

### Phase 1: Discuss — Capture Decisions Before Planning

**Goal:** Resolve ambiguity and make key decisions before breaking work into tasks.

**Steps:**
1. **List the gray areas** — for each initiative, identify decisions that haven't been made:
   - Technical: How will this integrate? What's the data model?
   - Visual: What does the user experience look like?
   - Organizational: Who owns this? Who needs to approve?
   - Regulatory: What compliance requirements apply?

2. **Categorize and resolve:**

   | Category | Example Questions |
   |----------|------------------|
   | Must decide before planning | Architecture choices, scope boundaries, compliance requirements |
   | Can decide during execution | Visual details, copy, minor UX decisions |
   | Doesn't need a decision | Premature optimizations, future-phase concerns |

3. **Document decisions** — capture each decision with context and rationale. These become constraints for planning.

4. **Initialize the risk register** — identify product risks that need tracking through execution:

   | Risk | Type | Likelihood | Impact | Mitigation | Owner | Status |
   |------|------|-----------|--------|-----------|-------|--------|
   | [Risk] | Market/Tech/Regulatory/Org | H/M/L | H/M/L | [Action] | [Who] | Open |

   Update this register at every wave checkpoint (Phase 3). Close resolved risks, add new ones as they emerge. This is a living document, not a one-time exercise.

**Output:** Decision log and risk register — what was decided, what was deferred, what risks are tracked.

### Phase 2: Plan — Break Work Into Atomic Tasks

**Goal:** Create a set of clearly scoped, independently executable tasks.

**Steps:**
1. **Decompose into phases** — group work into logical phases that can be planned and executed independently. Each phase should:
   - Deliver a coherent increment of value
   - Be completable in 1-2 weeks
   - Have clear entry and exit criteria

2. **Break phases into tasks** — each task should:
   - Be completable in 2-4 hours (not days)
   - Have a clear definition of done
   - Include verification steps
   - Be assignable to one person or agent

3. **Identify dependencies** — within and across phases:
   - What must be done first? (Blocking dependencies)
   - What can be done in parallel? (Independent tasks)
   - What requires coordination? (Collaborative dependencies)

4. **Sequence into waves:**

   ```
   Wave 1: [Independent foundation tasks — can run in parallel]
   Wave 2: [Tasks depending on Wave 1 — can run in parallel with each other]
   Wave 3: [Integration and polish tasks]
   ```

**Output:** Phased plan with waves of atomic tasks.

### Phase 3: Execute — Deliver in Waves

**Goal:** Execute the plan systematically, maintaining quality and visibility.

**Steps:**
1. **Execute one wave at a time** — complete all tasks in a wave before starting the next
2. **For each task:**
   - Confirm the definition of done before starting
   - Execute the work
   - Run verification steps
   - Document what was done (atomic commit or summary)
   - Update progress tracking

3. **Checkpoint between waves:**
   - Is everything from the current wave done and verified?
   - Are there any new dependencies or blockers for the next wave?
   - Has anything changed that affects the plan?
   - Update STATE.md with progress and any new decisions

4. **Cross-functional sync** — at each wave transition, check in with partner functions:
   - **Design:** Is the UX validated for the next wave's scope?
   - **Engineering:** Are there technical blockers or architecture concerns?
   - **Compliance/Risk:** Does anything in the next wave trigger review requirements?
   - **Operations/Support:** Is the ops team aware of what's coming and when?

   Not every sync applies to every wave. Match the cadence to the complexity — a simple internal tool may only need an engineering check, while a regulated product needs all four.

5. **Handle blockers:**
   - If blocked by a dependency: escalate or find an alternative path
   - If blocked by ambiguity: go back to Discuss (Phase 1) for the specific question
   - If blocked by complexity: break the task into smaller tasks

**Output:** Completed work with verification results.

### Phase 4: Verify — Validate Against Requirements

**Goal:** Confirm that what was built meets the requirements and achieves the desired outcome.

**Steps:**
1. **Requirements check** — walk through each requirement from the PRD:
   - [ ] Acceptance criteria met?
   - [ ] Edge cases handled?
   - [ ] Non-functional requirements satisfied?

2. **User validation** — where possible, get the actual user to validate:
   - Does this solve the problem?
   - Is anything confusing or missing?
   - Would they use this in their real workflow?

3. **Quality check:**
   - Does this meet the quality bar from the relevant skill?
   - Is it visually clean and professionally presented?
   - Is it documented or self-explanatory?

4. **Launch readiness check** — before shipping, assess readiness based on the product's risk and visibility tier:

   **Tier 1 — Low risk / internal tool / small audience:**
   - [ ] Documentation updated or created
   - [ ] Key users notified of the change
   - [ ] Rollback plan identified (if applicable)

   **Tier 2 — Moderate risk / cross-team impact:**
   - [ ] All Tier 1 items
   - [ ] Training or walkthrough provided to affected teams
   - [ ] Support team briefed on expected questions
   - [ ] Comms sent to stakeholders with summary of changes

   **Tier 3 — High risk / regulated / executive visibility:**
   - [ ] All Tier 1 and Tier 2 items
   - [ ] Compliance/risk review completed and approved
   - [ ] Rollout plan with phased deployment (pilot → broader release)
   - [ ] Success criteria defined for go/no-go on broader release
   - [ ] Executive sponsor sign-off obtained

   Select the tier that matches the initiative. When in doubt, go one tier higher.

5. **Decide:**
   - **Ship** — requirements met, quality bar cleared, launch readiness confirmed. Deploy or deliver.
   - **Fix** — specific issues identified. Create fix tasks and re-execute.
   - **Iterate** — fundamentally works but needs improvement. Plan next iteration.

**Output:** Verification report with launch readiness assessment and ship/fix/iterate decision.

## State Management

Throughout execution, keep these documents current:

| Document | Update Frequency | What Changes |
|----------|-----------------|-------------|
| STATE.md | After each wave | Active threads, decisions made, blockers |
| ROADMAP.md | After each phase | Completion status |
| Plan document | After each wave | Task status, new tasks discovered |

## Output Format

```markdown
# Execution Plan: [Initiative Name]

## Context
- **Strategy link:** [Which strategic theme this supports]
- **PRD link:** [Requirements document]
- **Team:** [Who's executing]
- **Timeline:** [Start → target completion]

## Decision Log
| Decision | Options Considered | Chosen | Rationale | Date |
|----------|-------------------|--------|-----------|------|
| [Decision] | [Options] | [Choice] | [Why] | [When] |

## Risk Register
| Risk | Type | Likelihood | Impact | Mitigation | Owner | Status |
|------|------|-----------|--------|-----------|-------|--------|
| [Risk] | [Type] | [H/M/L] | [H/M/L] | [Action] | [Who] | [Open/Closed] |

## Phase 1: [Name]
**Entry criteria:** [What must be true before starting]
**Exit criteria:** [What must be true to consider this phase done]

### Wave 1
- [ ] **Task 1:** [Description] — Done when: [Criteria]
- [ ] **Task 2:** [Description] — Done when: [Criteria]

### Wave 2
- [ ] **Task 3:** [Description] — Depends on: [Task 1] — Done when: [Criteria]

## Phase 2: [Name]
...

## Launch Readiness (Tier: [1/2/3])
- [ ] [Tier-appropriate checklist items]

## Verification Checklist
- [ ] All acceptance criteria from PRD met
- [ ] User validation conducted
- [ ] Quality bar from relevant skill cleared
- [ ] Launch readiness checklist completed for selected tier
- [ ] Risk register reviewed — all open risks mitigated or accepted
- [ ] STATE.md updated
- [ ] ROADMAP.md updated
```

## Quality Checklist

- [ ] Intake handoff verified (prioritization output, PRD, strategic context)
- [ ] All gray areas resolved before planning
- [ ] Risk register initialized with known risks
- [ ] Tasks are atomic (2-4 hours each)
- [ ] Dependencies are mapped and sequenced
- [ ] Each task has a clear definition of done
- [ ] Cross-functional syncs scheduled at wave transitions (as appropriate)
- [ ] Verification steps are defined before execution begins
- [ ] Launch readiness tier selected and checklist completed
- [ ] State documents are updated throughout

## Common Pitfalls

- **Planning without deciding** — creating tasks that contain unresolved ambiguity. Discuss first, then plan.
- **Tasks too large** — "Build the dashboard" is not a task. Break it down until each piece is 2-4 hours.
- **Skipping verification** — assuming it works because it's done. Verify against requirements explicitly.
- **Invisible progress** — executing without updating state documents. If it's not in STATE.md, it didn't happen (for context continuity purposes).
- **Heroic execution** — trying to do everything in one long session. Work in waves, checkpoint between them, maintain quality.

## Product Standard Alignment

This framework serves **Pillar 3: Enduring Lifecycle** (practices 3-4) —
practices to enable product predictability, velocity, and adaptability.

| Practice | Framework Coverage | Where |
|----------|-------------------|-------|
| **Adaptive Delivery Plans** | | |
| — Structured idea intake | Inputs section (intake handoff with required artifacts from upstream frameworks) | |
| — Refined backlog for predictable delivery | Strong | Phase 2 (atomic tasks, waves, dependencies) |
| — Proactive product risk management | Strong | Phase 1 step 4 (risk register), Phase 3 (updated at wave checkpoints) |
| — Delivery at sustainable pace | Phase 3 (wave-based execution, checkpoints) | |
| **Routines for Activation** | | |
| — Refinement & adjustment routines | Strong | Phase 3 (wave checkpoints, state management) |
| — Communication & transparency | Strong | Phase 3 (progress tracking, cross-functional sync, STATE.md updates) |
| — Cross Functional Touchpoints | Phase 3 step 4 (cross-functional sync at wave transitions) | |
| — Launch Enablement | Phase 4 step 4 (tiered launch readiness checklist) | |

### Previously Identified Gaps — Now Closed

1. **Idea intake** — ~~No structured intake documented.~~ Closed: Inputs section defines
   the handoff from upstream frameworks with required artifacts (prioritization output, PRD,
   strategic context).
2. **Cross-functional touchpoints** — ~~No explicit cross-team sync cadence.~~ Closed:
   Phase 3 step 4 adds cross-functional sync at wave transitions (design, engineering,
   compliance, ops) scaled to initiative complexity.
3. **Launch enablement** — ~~No launch readiness checklist.~~ Closed: Phase 4 step 4 adds
   a three-tier launch readiness checklist scaled by risk and visibility.
4. **Risk management** — ~~Product risk not tracked through execution.~~ Closed: Phase 1
   step 4 initializes a risk register updated at every wave checkpoint in Phase 3.
