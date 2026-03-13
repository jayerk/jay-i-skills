# Discovery Framework

## Purpose

A structured workflow for continuous product discovery — understanding customer problems, mapping opportunities, testing assumptions, and generating validated solutions. Based on Teresa Torres' Continuous Discovery Habits, with interview craft from Rob Fitzpatrick (The Mom Test) and Steve Portigal (Interviewing Users), and research method rigor from Erika Hall (Just Enough Research). Adapted for internal product teams in a regulated environment.

## When to Use

- Starting work on a new product area or capability
- Validating assumptions about user needs before building
- Generating and evaluating solution options for a known problem
- Conducting a discovery sprint (1-2 weeks of focused learning)
- Re-evaluating product direction when signals suggest misalignment

## When NOT to Use

- **Pure technical spikes** — if the question is "can we build it?" not "should we build it?", this is an engineering spike, not discovery
- **Compliance or regulatory mandates** — if the work is required regardless of user need, skip to PRD writing
- **Known solution, clear requirements** — if the problem and solution are both well-understood, go straight to `skills/prd-writing/SKILL.md`
- **Stakeholder opinion gathering** — discovery is about user behavior, not collecting preferences from leadership. Use `skills/stakeholder-navigation/SKILL.md` for that

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

5. **Choose the right research method** — Match the method to the question (Erika Hall's principle: right method for the question, right fidelity for the stage):

   | Question Type | Best Method | When to Use |
   |--------------|-------------|-------------|
   | What do people do? | Observation, contextual inquiry | When you need behavioral evidence, not self-reported behavior |
   | Why do they do it? | Interviews (Phase 2) | When you need to understand motivations and mental models |
   | How many? How often? | Data analysis, surveys | When you need to quantify a pattern already identified qualitatively |
   | What happened over time? | Diary studies, log analysis | When the problem unfolds over days/weeks, not in a single session |

   Interviews are the default for most internal product discovery, but don't default to them when observation or data analysis would answer the question faster. Avoid research theater — doing interviews because it feels like discovery when the data is already available.

**Output:** Assumption map with prioritized testing targets and selected research methods.

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

3. **Conduct interviews** — 30 minutes each. Apply Steve Portigal's interviewing craft:
   - **Build rapport first** — spend the first 2-3 minutes on context-setting, not jumping to questions. Let them orient you to their world.
   - **Manage silence** — after they answer, wait 3-5 seconds before your next question. People fill silence with the things they weren't going to say.
   - **Follow the unexpected** — when something surprises you, go deeper on it instead of sticking to the guide. The guide is a safety net, not a script.
   - **Ask for the artifact** — "Can you show me?" is more valuable than "Can you describe it?" Screen shares, documents, and tools reveal what words don't.

   Take notes on:
   - Observed behaviors and workarounds (behavioral evidence — what they actually do)
   - Emotional language (frustration, confusion, pride)
   - Frequency and severity of the problem
   - Unspoken assumptions about how things should work
   - Contradictions between what they say and what they show you

4. **Synthesize findings** — After every 3 interviews, look for:
   - Patterns across respondents
   - Surprises that challenge assumptions
   - New opportunities not previously considered

5. **Create lightweight personas** — For each distinct user segment identified through interviews, capture:
   - **Role and context** — who they are, what team/function, what they're responsible for
   - **Goals** — what they're trying to accomplish in the problem domain
   - **Pain points** — top 2-3 frustrations observed across interviews
   - **Current workarounds** — how they solve the problem today
   - **Quote** — one representative verbatim quote that captures their perspective

   Keep personas to one page each. Update them as new interviews add or refine segments. These are living documents, not one-time deliverables.

6. **Map the journey (optional)** — When the problem spans multiple steps, tools, or handoffs, sketch the end-to-end journey:
   - **Steps** — what does the user do, in order?
   - **Tools/systems** — what do they touch at each step?
   - **Pain points** — where do things break down or slow down?
   - **Emotional state** — where are they frustrated, confused, or satisfied?

   This is most valuable when the opportunity involves cross-team or cross-system workflows. Skip it for single-tool, single-step problems.

**Output:** Interview synthesis with updated assumption confidence levels, lightweight persona documents, and (optionally) journey map.

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

3. **Evaluate solutions through design lenses** — before committing to experiments, run promising solutions through a lens review using `schell-lens-review`. The lenses evaluate whether each solution will deliver a good experience for the personas identified in Phase 2. Key lenses for discovery typically include Essential Experience (#2), Problem Solving (#8), Needs (#22), Accessibility (#54), and Visible Progress (#55), but the lens recommendation step will select the right set based on the specific opportunities and personas.

   Use the lens review backlog to refine solutions before experimenting. Solutions that fail critical lenses may not be worth testing. Solutions that surface design improvements get stronger before reaching users.

4. **Design experiments** — for each promising solution, define how to test it:
   - **Prototype test** — show a mockup or demo, gather feedback
   - **Concierge test** — manually deliver the solution, measure value
   - **Wizard of Oz** — fake the backend, test the user experience
   - **Data analysis** — use existing data to validate demand or feasibility

**Output:** Opportunity Solution Tree with prioritized experiments.

### Phase 4: Test and Learn

**Goal:** Validate solutions before committing to full build.

**Steps:**
1. **Define success criteria before running** — for each experiment, write down:
   - **What we're testing:** Which assumption does this validate or invalidate?
   - **What success looks like:** The specific signal that tells us the solution works (e.g., "3 of 5 users complete the task without asking for help")
   - **What failure looks like:** The signal that tells us to stop (e.g., "users revert to their old process within a week")
   - **How long to run:** Timebox the experiment. If you don't have signal by then, that's a signal.

2. **Run experiments** — execute one experiment at a time, starting with the highest-priority from Phase 3. For each experiment:
   - Brief participants on what they're testing (not what answer you want)
   - Capture both quantitative signal (did they use it? how long did it take?) and qualitative signal (what did they say? what confused them?)
   - Record results immediately — don't rely on memory

3. **Evaluate against success criteria** — compare actual results to what you wrote in step 1:
   - Did you hit the success signal? Record the evidence.
   - Did you hit the failure signal? Record that too — failed experiments are valuable data.
   - Did something unexpected happen? That's often more important than the planned criteria.

4. **Update the Opportunity Solution Tree** — prune solutions that failed, elaborate on those that showed signal, add new solutions surfaced by the experiment

5. **Decide: build, iterate, or pivot**
   - **Build** — success criteria met across experiments. Move to PRD writing (`skills/prd-writing/SKILL.md`).
   - **Iterate** — promising signals but gaps remain. Design a follow-up experiment targeting the specific uncertainty.
   - **Pivot** — solution doesn't address the opportunity. Return to Phase 3 and try a different solution branch.

**Output:** Go/no-go recommendation with evidence summary — what was tested, what was learned, what the recommendation is and why.

### Continuous Signals — Post-Discovery Monitoring

Discovery doesn't end when a build decision is made. Maintain a lightweight signal monitoring practice:

- **Monthly:** Review usage data, support tickets, and stakeholder feedback for the product area. Look for signals that assumptions have changed.
- **Quarterly:** Revisit the Opportunity Solution Tree. Are the validated opportunities still the right ones? Have new opportunities emerged?
- **Trigger-based:** When a significant event occurs (reorg, regulatory change, competitor move, user escalation), reassess the assumption map from Phase 1.

Keep a running signal log — a simple list of date, signal, and implication. This feeds back into Strategy and Prioritization when it's time to re-evaluate direction.

## Output Format

```markdown
# Discovery: [Product Area / Capability]

## Desired Outcome
[Specific, measurable outcome statement]

## Assumption Map
| Assumption | Confidence | Impact | Test Method | Result |
|-----------|-----------|--------|-------------|--------|
| [Assumption] | H/M/L | H/M/L | [Method] | [Validated/Invalidated/Untested] |

## Research Summary
- **Method(s) used:** [Interviews, observation, data analysis, etc.]
- **Participants:** [N people across M roles/contexts]
- **Key findings:** [Top 3-5 insights with supporting evidence]

## Personas
### [Persona Name — Role]
- **Context:** [Team/function, responsibilities]
- **Goals:** [What they're trying to accomplish]
- **Pain points:** [Top frustrations]
- **Workarounds:** [How they solve it today]
- **Quote:** "[Representative verbatim]"

## Opportunity Solution Tree
[Tree structure — outcome → opportunities → solutions → experiments]

## Experiment Results
| Experiment | Solution Tested | Success Criteria | Result | Evidence |
|-----------|----------------|-----------------|--------|----------|
| [Experiment] | [Solution] | [Criteria] | [Pass/Fail/Partial] | [What happened] |

## Recommendation
**Decision:** [Build / Iterate / Pivot]
**Rationale:** [Evidence-based justification]
**Next step:** [PRD writing / follow-up experiment / new solution branch]

## Signal Monitoring Plan
- **Monthly check:** [What to watch]
- **Quarterly review:** [When to revisit the OST]
- **Trigger events:** [What would force reassessment]
```

## Vocabulary Cross-References

Key terms used in this framework — see `knowledge/vocabulary.md` for full definitions:

- **Opportunity Solution Tree** — the core artifact connecting outcomes → opportunities → solutions → experiments
- **Assumption Map** — assumptions rated by confidence and impact; low-confidence, high-impact assumptions get tested first
- **Behavioral Evidence** — what people actually do, not what they say they'd do. The gold standard for discovery insights.
- **Continuous Discovery** — maintaining ongoing user contact rather than treating discovery as a one-time phase

## Quality Checklist

- [ ] Desired outcome is specific and measurable
- [ ] Research method matched to the question (not defaulting to interviews)
- [ ] At least 5 user engagements conducted (interviews, observations, or both)
- [ ] Assumptions are explicitly listed with confidence levels
- [ ] Lightweight personas created for each distinct user segment
- [ ] Journey map created (if problem spans multiple steps/systems)
- [ ] Opportunity Solution Tree connects outcome → opportunity → solution → experiment
- [ ] At least 3 solutions generated per top opportunity
- [ ] Success criteria defined before running experiments
- [ ] Experiments produce behavioral evidence, not just opinions
- [ ] Evidence supports the recommendation, not just intuition
- [ ] Signal monitoring cadence established for post-discovery

## Common Pitfalls

- **Skipping to solutions** — building before understanding the problem. Force yourself through Phases 1-2 before brainstorming solutions.
- **Confirmation bias** — hearing what you want to hear in interviews. Look for disconfirming evidence.
- **Interview theater** — conducting interviews to check a box rather than to learn. If you're not surprised by anything, you're not asking the right questions.
- **One-and-done discovery** — treating discovery as a phase rather than a continuous practice. Schedule weekly discovery activities.
- **Method mismatch** — using interviews to answer questions that data analysis could resolve faster, or using surveys when you don't yet know the right questions. Match the method to the question (Phase 1, step 5).

## Product Standard Alignment

This framework serves **Pillar 1: Customer-Centered Product Design** — practices
to understand and address the needs, behaviors, and experiences of customers and
employees throughout the product lifecycle.

| Practice | Framework Coverage | Where |
|----------|-------------------|-------|
| **Customer & Market Insights** | Strong | Phase 1 (assumption mapping, research design), Phase 2 (user engagement, synthesis) |
| — Research insights & observability | Phase 2 interview synthesis, Phase 4 evidence tracking | |
| — Proactive monitoring of signals | Phase 1 assumption confidence monitoring, Continuous Signals section (post-discovery cadence) | |
| — Iterative prototyping | Phase 3 experiments (prototype test, Wizard of Oz) | |
| — Usability testing & feedback | Phase 4 test and learn cycle | |
| **Segmentation & Personas** | Strong | Phase 2 (interview targeting, persona creation) |
| — Enduring customer profiles | Phase 2 step 5 (lightweight persona documents) | |
| — Personalized engagement | Not covered | Out of scope: engagement strategy is post-discovery |
| **Customer & Employee Journeys** | Strong | Phase 2 (behavior observation, journey mapping), Phase 3 (opportunity mapping) |
| — Journey mapping | Phase 2 step 6 (optional journey mapping exercise) | |
| — Design system | Not covered | Out of scope for discovery |

### Previously Identified Gaps — Now Closed

1. **Persona artifact** — ~~No explicit persona creation step.~~ Closed: Phase 2 step 5
   produces lightweight persona documents updated as interviews progress.
2. **Signal monitoring** — ~~Sprint-oriented, no ongoing cadence.~~ Closed: Continuous Signals
   section adds monthly/quarterly/trigger-based monitoring post-discovery.
3. **Journey mapping** — ~~No explicit journey artifact.~~ Closed: Phase 2 step 6 adds
   optional journey mapping for multi-step/multi-system problems.
