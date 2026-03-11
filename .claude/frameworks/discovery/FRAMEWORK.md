# Discovery Framework

## Purpose

A structured workflow for continuous product discovery — understanding customer problems, mapping opportunities, testing assumptions, and generating validated solutions. Based on Teresa Torres' Continuous Discovery Habits, adapted for internal product teams in a regulated environment.

## When to Use

- Starting work on a new product area or capability
- Validating assumptions about user needs before building
- Generating and evaluating solution options for a known problem
- Conducting a discovery sprint (1-2 weeks of focused learning)
- Re-evaluating product direction when signals suggest misalignment

## Inputs

- A product area or capability to explore
- Access to users or stakeholders who experience the problem domain
- Current understanding of the problem space (can be minimal)

## Workflow

### Phase 1: Frame the Opportunity Space

**Goal:** Define what we're trying to learn and why it matters.

**Steps:**
1. **State the desired outcome** — What business or user outcome are we trying to drive? Be specific. "Improve product team effectiveness" is too broad. "Reduce the time product teams spend on quarterly prioritization from 3 weeks to 1 week" is better.

2. **Map what we know** — List current assumptions about:
   - Who has this problem
   - How severe the problem is
   - How they solve it today
   - What a good solution looks like
   - What constraints exist (regulatory, technical, organizational)

3. **Identify what we don't know** — For each assumption, rate confidence (High/Medium/Low). Low-confidence assumptions become discovery targets.

4. **Prioritize assumptions to test** — Use this matrix:

   | | High Impact on Solution | Low Impact on Solution |
   |---|---|---|
   | **Low Confidence** | Test first | Test if time allows |
   | **High Confidence** | Monitor for changes | Skip |

**Output:** Assumption map with prioritized testing targets.

### Phase 2: Engage Users

**Goal:** Learn from people who experience the problem.

**Steps:**
1. **Identify interview targets** — Minimum 5 people across different roles or contexts. For internal tools: product managers, product owners, delivery leads, portfolio managers.

2. **Design the conversation guide** — Follow The Mom Test principles:
   - Ask about their life, not your idea
   - Ask about specifics in the past, not generics about the future
   - Listen more than you talk
   - Focus on behavior, not opinion

   **Good questions:**
   - "Walk me through the last time you did [activity]. What was that like?"
   - "What's the most frustrating part of [process] right now?"
   - "When this goes wrong, what happens? What's the impact?"
   - "How do you work around [pain point] today?"

   **Bad questions:**
   - "Would you use a tool that does X?" (Leading)
   - "How important is Y to you on a scale of 1-10?" (Abstract)
   - "What features would you want?" (Solution-first)

3. **Conduct interviews** — 30 minutes each. Take notes on:
   - Observed behaviors and workarounds
   - Emotional language (frustration, confusion, pride)
   - Frequency and severity of the problem
   - Unspoken assumptions about how things should work

4. **Synthesize findings** — After every 3 interviews, look for:
   - Patterns across respondents
   - Surprises that challenge assumptions
   - New opportunities not previously considered

**Output:** Interview synthesis with updated assumption confidence levels.

### Phase 3: Build the Opportunity Solution Tree

**Goal:** Connect desired outcomes to validated opportunities to potential solutions.

**Structure:**
```
Desired Outcome
├── Opportunity 1 (validated problem/need)
│   ├── Solution A
│   │   ├── Experiment 1
│   │   └── Experiment 2
│   └── Solution B
│       └── Experiment 3
├── Opportunity 2 (validated problem/need)
│   ├── Solution C
│   └── Solution D
└── Opportunity 3 (validated problem/need)
    └── Solution E
```

**Steps:**
1. **List validated opportunities** — problems or needs confirmed by user research. Each opportunity should be:
   - Stated as a user need, not a solution ("teams need to see portfolio health at a glance" not "build a dashboard")
   - Supported by evidence from at least 3 interviews
   - Connected to the desired outcome

2. **Generate solutions per opportunity** — brainstorm at least 3 solutions for each top opportunity. Include:
   - Low-effort options (spreadsheet, template, manual process)
   - Medium-effort options (internal tool, workflow change)
   - High-effort options (platform capability, system integration)

3. **Design experiments** — for each promising solution, define how to test it:
   - **Prototype test** — show a mockup or demo, gather feedback
   - **Concierge test** — manually deliver the solution, measure value
   - **Wizard of Oz** — fake the backend, test the user experience
   - **Data analysis** — use existing data to validate demand or feasibility

**Output:** Opportunity Solution Tree with prioritized experiments.

### Phase 4: Test and Learn

**Goal:** Validate solutions before committing to full build.

**Steps:**
1. **Run experiments** — execute the highest-priority experiments from Phase 3
2. **Measure outcomes** — did the solution address the opportunity?
3. **Update the tree** — prune solutions that don't work, elaborate on those that do
4. **Decide: build, iterate, or pivot**
   - **Build** — sufficient evidence that the solution works. Move to PRD writing.
   - **Iterate** — promising signals but needs refinement. Run another experiment.
   - **Pivot** — solution doesn't address the opportunity. Try a different approach.

**Output:** Go/no-go recommendation with supporting evidence.

## Quality Checklist

- [ ] Desired outcome is specific and measurable
- [ ] At least 5 user interviews conducted
- [ ] Assumptions are explicitly listed with confidence levels
- [ ] Opportunity Solution Tree connects outcome → opportunity → solution → experiment
- [ ] At least 3 solutions generated per top opportunity
- [ ] Experiments are designed before building anything
- [ ] Evidence supports the recommendation, not just intuition

## Common Pitfalls

- **Skipping to solutions** — building before understanding the problem. Force yourself through Phases 1-2 before brainstorming solutions.
- **Confirmation bias** — hearing what you want to hear in interviews. Look for disconfirming evidence.
- **Interview theater** — conducting interviews to check a box rather than to learn. If you're not surprised by anything, you're not asking the right questions.
- **One-and-done discovery** — treating discovery as a phase rather than a continuous practice. Schedule weekly discovery activities.

## Product Standard Alignment

This framework serves **Pillar 1: Customer-Centered Product Design** — practices
to understand and address the needs, behaviors, and experiences of customers and
employees throughout the product lifecycle.

| Practice | Framework Coverage | Where |
|----------|-------------------|-------|
| **Customer & Market Insights** | Strong | Phase 1 (assumption mapping, research design), Phase 2 (user engagement, synthesis) |
| — Research insights & observability | Phase 2 interview synthesis, Phase 4 evidence tracking | |
| — Proactive monitoring of signals | Phase 1 assumption confidence monitoring | Gap: no ongoing signal monitoring cadence |
| — Iterative prototyping | Phase 3 experiments (prototype test, Wizard of Oz) | |
| — Usability testing & feedback | Phase 4 test and learn cycle | |
| **Segmentation & Personas** | Moderate | Phase 2 (interview targeting across roles/contexts) |
| — Enduring customer profiles | Implicit in interview synthesis | Gap: no explicit persona creation step |
| — Personalized engagement | Not covered | Gap: engagement strategy is post-discovery |
| **Customer & Employee Journeys** | Moderate | Phase 2 (behavior observation, workarounds), Phase 3 (opportunity mapping) |
| — Journey mapping | Implicit in opportunity identification | Gap: no explicit journey artifact |
| — Design system | Not covered | Out of scope for discovery |

### Identified Gaps

1. **Persona artifact** — Discovery identifies segments through interviews but doesn't
   produce an enduring persona document. Consider adding a persona template output to Phase 2.
2. **Signal monitoring** — Discovery is sprint-oriented. The product standard expects
   ongoing monitoring. Consider adding a "continuous signals" section for post-discovery cadence.
3. **Journey mapping** — Opportunity Solution Trees capture needs but not the end-to-end
   journey. Consider referencing a journey mapping exercise as an optional Phase 2 activity.
