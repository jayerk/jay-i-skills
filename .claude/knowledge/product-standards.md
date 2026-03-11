# Product Standards: 9 Dimensions Across 3 Pillars

A reference standard for what "good" looks like in product management practice.
10 sub-practices organized into 3 pillars. Each sub-practice is documented across
9 structural dimensions — 4 defining the standard, 4 defining how to implement it,
plus a cross-cutting dependency map.

Designed to power self-assessment, coaching conversations, and gap analysis — not
to be a compliance checklist.

---

## Product Definition

A product must meet the following criteria:

- The customer (whether external or internal) and their needs can be clearly identified
- It creates measurable economic value
- Has an enduring lifecycle

*A customer is the primary beneficiary, whether internal or external, of the product's
value proposition — not just any stakeholder.*

---

## The 9 Structural Dimensions

Every sub-practice is documented across these 9 dimensions, split into two layers.

### Standard Layer — the "what"

| Dimension | What It Defines |
|-----------|----------------|
| **1. Purpose & Value** | Why this sub-practice matters |
| **2. Principles** | Guidelines to drive consistency and lead to better outcomes |
| **3. Success Criteria** | What good (& bad) looks like, incl. examples, checklists, and 5-level maturity rubric (harvey balls) |
| **4. Governance** | Who owns the standard and how it will be maintained |

### How-To Layer — the "how"

| Dimension | What It Defines | Jay's Refinement |
|-----------|----------------|-----------------|
| **5. Execution Guidance** | How to implement the practice | Minimum viable how-to with pointers to frameworks — not an implementation manual. Keep thin so teams adapt to context. |
| **6. Applicability** | How this practice differs across contexts | Organized by lifecycle stage (Concept/Launch/Growth/Maturity/Sunset) AND product type (customer-facing, internal platform, regulatory) so teams can quickly find their row. |
| **7. Measurement** | How adoption and effectiveness are tracked | Include leading indicators (are teams doing the practice?) alongside lagging indicators (is it producing outcomes?). Without leading indicators you only find out 6 months later that adoption stalled. |
| **8. Adoption Path** | How teams get started and reach maturity | What getting started looks like → what good looks like at 6 months → what embedded looks like. Pragmatic on-ramp, not a heavy change management plan. |

### Cross-Cutting

| Dimension | What It Defines |
|-----------|----------------|
| **9. Dependencies** | Which other standards are prerequisites or companions. Prevents cherry-picking that produces incoherent adoption. |

---

## The 3 Pillars and 10 Sub-Practices

### Pillar 1: Customer-Centered Product Design

Practices to understand and address the needs, behaviors, and experiences of
customers and employees throughout the product lifecycle.

#### 1. Customer & Market Insights

- Research insights analysis & observability
- Proactive monitoring of customer & employee signals
- Iterative prototyping
- Usability testing & feedback

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | Nobody talks to customers regularly. Product decisions come from internal opinions or whoever escalated last. No usability testing. No post-launch check-in. | PRDs have no "what we heard from users" section. No interview notes anywhere. Features launch and nobody asks "did it work?" |
| 2 — Developing | ◔ | Research happens when someone pushes for it — usually tied to a specific project, not ongoing. Results live in someone's notebook or a one-off slide deck. Usability testing is occasional. | A few interview summaries exist but you have to ask around to find them. Research gets done for big bets but skipped for everything else. |
| 3 — Established | ◑ | Team talks to customers on a regular schedule (e.g., 2-3 interviews/month). Insights are stored somewhere the team can find them. Usability testing happens before launch. Prototypes get user feedback before the team commits to building. | A shared folder or tool with tagged interview notes. "Here's what users said" shows up in planning conversations. Usability test findings referenced in design reviews. |
| 4 — Advanced | ◕ | Team monitors multiple signal sources (support tickets, analytics, research, sales feedback) and reviews them together. They pick the right research method for the question — not just interviews for everything. Insights are tracked over time to spot trends. | A monthly signal review meeting. Research plan that matches methods to questions. "Last quarter users told us X, this quarter it shifted to Y" in a planning doc. |
| 5 — Leading | ● | Research shapes what goes on the roadmap, not just how individual features work. The team has helped another team set up their own discovery practice. Research methods get refined based on what's working. | Research findings cited in strategy or roadmap docs. Another team asked for help setting up interviews. Team has tried and dropped at least one research method that wasn't working. |

[Remaining dimensions to follow]

#### 2. Segmentation & Personas

- Enduring customer profiles reflecting behavioral, needs, or value-based segments
- Consistent and proactive personalized engagement across channels

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | Everyone says "the user" as if there's one type. No segments defined. No personas. The product treats all customers the same way. | PRDs say "the user" or "our customers" without distinguishing who. No segment definitions in any doc. |
| 2 — Developing | ◔ | Someone made personas once — they're in a Confluence page from last year. Segments are based on org chart or size tiers, not what customers actually need. Nobody references them in planning. | Persona docs that haven't been updated. Segments like "Enterprise" and "SMB" that don't drive product decisions. Team can't name their segments off the top of their head. |
| 3 — Established | ◑ | Segments are based on what customers need or how they behave, not just who they are. Personas get reviewed at least yearly. The team references specific segments when making feature decisions ("this matters most for segment X"). | Segment definitions in the product strategy doc. "Who is this for?" gets a specific answer in planning. Feature priority considers which segments benefit. |
| 4 — Advanced | ◕ | Team tracks how each segment is doing (adoption, satisfaction, retention). Product and design share the same segment definitions. Engagement varies by segment — not one-size-fits-all. | Dashboard filtered by segment. Design specs reference segment-specific needs. Segment performance reviewed quarterly. |
| 5 — Leading | ● | Segments evolve — the team has added or retired a segment based on new data. Team spots emerging segments before they're obvious. Other teams have adopted the same segment definitions. | Segment model has a version history. At least one segment change documented with rationale. Cross-team alignment on shared segment language. |

[Remaining dimensions to follow]

#### 3. Customer & Employee Journeys

- Continuously map and refine enduring customer journeys to align experiences across the business
- Maintain a centralized, accessible design system for consistent, human-centered experience

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | Nobody has mapped the end-to-end experience. Teams think in features, not journeys. No shared design patterns — each team builds UI differently. Handoffs between teams are friction points nobody owns. | No journey map artifact. Buttons, forms, and flows look different across the product. Customer complaints about "I had to call three people" or "I couldn't find where to go next." |
| 2 — Developing | ◔ | A journey map was made for a project but hasn't been touched since. Some shared components exist but teams don't consistently use them. People know the journey has gaps but it's not tracked anywhere. | A journey map in a deck from 6+ months ago. A partial component library with inconsistent adoption. Pain points raised in retros but not in the backlog. |
| 3 — Established | ◑ | Journey maps exist for key flows and get updated when things change. Known pain points are in the backlog with journey context. A design system is in place and teams actually use it. | Journey maps reviewed when planning new work. Backlog items tagged with journey stage. Design system has an owner and adoption is tracked. |
| 4 — Advanced | ◕ | Journey stages have metrics attached (time-on-task, error rates, satisfaction). The team can show friction is going down over time. Multiple teams contribute to the design system. Journey ownership is clear across teams. | Dashboard showing journey-stage metrics. Quarter-over-quarter friction reduction. Design system pull requests from more than one team. |
| 5 — Leading | ● | New feature requests start with "where does this sit in the journey?" not "what should we build?" Journey maps show up in strategy conversations. Design system is reused beyond the original product. | Journey map referenced in roadmap discussions. Strategy docs cite journey-stage performance. Another product adopted the design system. |

[Remaining dimensions to follow]

---

### Pillar 2: Measurable Economic Value

Practices to enable data-informed teams to observe and optimize the impact of a product.

#### 4. Product Economic Insights

- Observability of key economic KPI driving the primary source of value of the product
- Leading indicators of the product's performance

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | Value is discussed in feelings ("users love it") or vanity metrics (page views, logins). No one can say what the product costs per user or transaction. Finance and product speak different languages. | No unit economics anywhere. Business cases use made-up numbers. Ask "what's our north star metric?" and you get blank stares or three different answers. |
| 2 — Developing | ◔ | Basic metrics exist (revenue, MAU) but they're not connected to what drives value. No leading indicators — team finds out something went wrong at the quarterly review. Cost is understood at the budget line level, not per-unit. | A dashboard that gets checked when someone asks. Metrics not referenced in prioritization. "We think it's working" but no data to back it up. |
| 3 — Established | ◑ | Team knows the key economic KPIs and reviews them monthly. Unit economics are documented (cost to serve, value per transaction). Leading indicators sit alongside lagging ones. Team can state the north star metric and explain why it matters. | Economic model written down. Monthly review where metrics are discussed and actions taken. Dashboard shows both leading (activation rate, time-to-value) and lagging (retention, revenue). |
| 4 — Advanced | ◕ | Economic impact shows up in prioritization — "this is worth X because of Y." Finance and product co-own the numbers. Cost of delay is estimated for major backlog items. Retention and growth patterns are understood, not just measured. | Cost of delay referenced in planning. Finance attends product reviews. Retention cohort analysis exists. Economic model gets updated when assumptions change. |
| 5 — Leading | ● | Economic thinking shapes what goes on the roadmap, not just how things get scored. The team can model "if we invest here, we expect this return" and check later whether it played out. Another team has asked to use the same economic framework. | Economic rationale in roadmap docs. At least one "what we predicted vs. what happened" review. Shared economic model across products. |

[Remaining dimensions to follow]

#### 5. Value-Based Sequencing

- Prioritization using value, risk, and effort scoring
- Work breakdown practices with understanding of readiness to support flow
- Documented trade-offs and rationale for sequencing decisions

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | Everything is P1. What gets done next depends on who asked last or who escalated loudest. No criteria for why one thing comes before another. Trade-offs aren't written down. | Backlog is a wish list with no order. Ask "why this first?" and the answer is "because [executive] asked." Blocked items surprise the team mid-sprint. |
| 2 — Developing | ◔ | Some prioritization criteria exist on paper but aren't used consistently. Priority is still mostly gut feel. Nobody writes down what value they expect an item to deliver. Items get sequenced before anyone checks whether the team can actually do them. | Criteria in a doc nobody opens during planning. "High/Medium/Low" priority with no scoring behind it. Blocked work discovered after commitment. |
| 3 — Established | ◑ | Team scores items on value, risk, and effort before sequencing. Each item has a short value hypothesis ("we believe X will result in Y"). Backlog is ranked — no ties. Before committing, team checks: do we have the people, are dependencies clear, is WIP manageable? Trade-offs documented. | Scoring sheet or tool in active use. Value hypothesis column filled in. Ranked backlog visible to stakeholders. Readiness check before sprint/wave commitment. |
| 4 — Advanced | ◕ | Team goes back and checks: did the value we predicted actually show up? Scoring gets recalibrated ("we keep overestimating effort on X-type work"). Cost of delay is estimated for big items. Stakeholders reference the scoring when asking for changes. | Quarterly "predicted vs. actual" review. Scoring adjustments documented. Stakeholders say "where does this score?" instead of "just do it." |
| 5 — Leading | ● | Sequencing works across products, not just within one backlog. Teams adjust their own sequence within guardrails without escalating. Another team has asked for help setting up their prioritization process. | Cross-product prioritization visible. Team reorders without manager approval for routine changes. Prioritization coaching request from another team. |

[Remaining dimensions to follow]

#### 6. Value Guardrails & Realization

- Guardrails for customer experience, reliability, and strategic capacity allocation
- Clear stop/pivot/kill criteria and cost allocation across run/grow/transform
- Benefits forecasting and value hypothesis standards

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | Initiatives run until the money runs out or a leader moves on. No kill criteria. No one checks whether the business case benefits actually showed up. Capacity split between run/improve/transform is whatever got funded — nobody tracks it. | Zombie initiatives still consuming people. Business cases with benefits nobody revisited. Ask "what percentage is run vs. transform?" and nobody knows. |
| 2 — Developing | ◔ | Some guardrails exist (budget caps, SLA targets) but they're not connected to value. Kill criteria get discussed in planning but nothing actually gets killed. Benefits are forecasted in the business case and forgotten. Someone knows the R/I/T split but it's not reviewed. | Business cases gathering dust. "We should really stop that project" has been said for two quarters. R/I/T target exists on a slide but actuals aren't tracked. |
| 3 — Established | ◑ | Guardrails for CX, reliability, and capacity are defined and on a dashboard. R/I/T allocation targets are set and reviewed quarterly. Kill criteria are real — at least one initiative has been stopped because a trigger was hit. Post-launch, team checks whether the value hypothesis played out. | Guardrail dashboard reviewed monthly. R/I/T actuals vs. targets in a quarterly review. A documented example of killing or pivoting an initiative. Benefits realization check exists. |
| 4 — Advanced | ◕ | Teams flag their own guardrail breaches — leadership doesn't have to find them. Benefits realization feeds back into planning ("last time we overestimated by 40%, so let's adjust"). R/I/T shifts are documented with rationale. Kill decisions happen early, not as a last resort. | Team-initiated guardrail alerts. Planning docs reference past realization accuracy. R/I/T rebalance documented mid-cycle. Kill decision made before budget was exhausted. |
| 5 — Leading | ● | Teams manage guardrails without escalating routine decisions. Proving value is expected, not exceptional — teams plan the check-in when they plan the work. R/I/T allocation is something teams discuss and propose, not just receive. | Guardrail decisions made at team level. Value check-in scheduled at launch time. Team proposes their own R/I/T split with rationale. Another team adopted the guardrail approach. |

[Remaining dimensions to follow]

---

### Pillar 3: Enduring Lifecycle

Practices to enable product predictability, velocity, and adaptability from
concept to sunset.

#### 7. Measurable Outcomes

- Vision for the value that a product will deliver to a customer
- KPIs for ongoing performance monitoring

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | Success means "we shipped it." No product vision written down. No KPIs, or only output metrics (features delivered, story points). Nobody asks "did it work?" after launch. | No vision document. Retros discuss what was built, not what it achieved. Quarterly review is a delivery status report. |
| 2 — Developing | ◔ | There's a vision statement but it's vague enough to never be wrong ("deliver great experiences"). KPIs exist but nobody reviews them regularly. Team reports on velocity and throughput, not adoption or satisfaction. | Vision you can't measure against. KPI dashboard nobody opens. Quarterly review covers what shipped, not what moved. |
| 3 — Established | ◑ | Vision says what value the product delivers to specific customers and you could check whether it's true. KPIs have targets and get reviewed monthly. Planning connects what the team builds to what they expect to achieve. Both leading (activation, engagement) and lagging (retention, revenue) indicators tracked. | Vision with measurable outcomes. Monthly KPI review with "here's what we'll do about it." Planning docs reference target outcomes. |
| 4 — Advanced | ◕ | Planning starts with "what outcome do we need to move?" not "what feature should we build?" Team owns their metrics and adjusts approach when something stalls. KPIs connect from business goals down to team-level work. | Outcome-first planning visible in docs. Team flags stalled metrics before leadership asks. Mid-cycle scope change tied to outcome data. |
| 5 — Leading | ● | Vision gets revisited when the market shifts — not a set-and-forget artifact. Team-level metrics connect to individual goals. Outcome data informs which products get more investment. | Vision update with documented rationale. Individual goals tied to product KPIs. Portfolio review references outcome trends across products. |

[Remaining dimensions to follow]

#### 8. Strategy & Roadmap

- Roadmap artifact to bring vision to life over multi-year planning horizon
- Objectives & key results to align teams to the roadmap

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | No roadmap, or it's a feature list with target dates. No strategic context — team knows what to build but not why. No OKRs. | Gantt chart of features. Ask "why this?" and the answer is "it was in the plan." Team can't connect their work to business strategy. |
| 2 — Developing | ◔ | A roadmap exists but it's dates and features. Strategy connection is implied, not stated. OKRs are activity-based ("launch X by Q3") not outcome-based. Updated when an exec asks for it. | Roadmap reads like a project plan. OKRs that are really a to-do list. Strategy doc and roadmap are two separate artifacts that don't reference each other. |
| 3 — Established | ◑ | Roadmap organized by time horizons (Now/Next/Later) with outcomes, not just features. OKRs align to strategic themes with measurable key results. Roadmap reviewed and updated quarterly. Team can explain how their work connects to strategy. | Roadmap references strategic themes. OKRs with quantified key results. Quarterly roadmap review on the calendar. Team answers "how does this connect to strategy?" without hesitating. |
| 4 — Advanced | ◕ | Roadmap connects to the economic model and changes when new data comes in. OKRs get adjusted mid-cycle when the data warrants it. Roadmap rationale is documented well enough to survive an executive challenge. | Mid-cycle OKR adjustment with written rationale. Roadmap change traced to a specific insight or metric shift. Roadmap used in exec conversations, not created for them. |
| 5 — Leading | ● | Teams propose strategic themes, not just execute them. Roadmap is a communication tool other teams reference for their own planning. Strategy docs have a decision log so you can see how thinking evolved. | Team-proposed theme on the roadmap. Another team references this roadmap in their planning. Strategy doc with versioned decision history. |

[Remaining dimensions to follow]

#### 9. Adaptive Delivery Plans

- Structured idea intake
- Refined backlog for predictable value delivery
- Proactive product risk management
- Delivery at a sustainable pace

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | Work arrives by interrupt — someone sends a message and it goes in the backlog (or straight to a developer). No intake process. No refinement cadence. Risks show up at launch. Pace is whatever urgency demands. | No backlog refinement on the calendar. Items added mid-sprint with no evaluation. No risk register. Delivery dates are guesses. |
| 2 — Developing | ◔ | Backlog exists but items from 6 months ago sit untouched. Refinement happens sometimes. Risks get discussed in retros after they've already hit. Intake is informal — "just put it in Jira" or "send me a Slack." | Stale backlog items. Sporadic refinement. Risk conversations are post-mortems, not prevention. New work enters without evaluation criteria. |
| 3 — Established | ◑ | There's a defined way for new work to enter (intake with evaluation criteria). Backlog gets refined regularly. Delivery runs in waves or sprints with a predictable cadence. Risk register exists and gets reviewed at checkpoints. Team monitors whether pace is sustainable. | Intake process documented and used. Weekly or biweekly refinement. Risk register updated at wave boundaries. Velocity stable enough to forecast. Capacity planned. |
| 4 — Advanced | ◕ | Delivery cadence adjusts to lifecycle stage — tighter cycles in Launch, broader in Maturity. Forecasts are reliable enough that stakeholders trust them. Risks are identified before they hit, not after. New intake feeds into the scoring framework. | Cadence rationale documented. Delivery forecasts within reasonable accuracy. Risk mitigated before escalation. Intake items scored before entering the backlog. |
| 5 — Leading | ● | Team adjusts their own cadence based on what's working — they don't wait to be told. Process improvements are tried and logged. Another team has asked to shadow their delivery practices. | Team-initiated cadence change with rationale. Process experiment documented. Delivery practice adopted by another team. |

[Remaining dimensions to follow]

#### 10. Routines for Activation

- Routines that support refinement and adjustment of roadmaps, backlogs, and plans
- Strong communication and transparency across all stakeholders & teams
  - Cross-functional touchpoints
  - Launch enablement

##### Maturity Rubric

| Level | Harvey Ball | Observable Behaviors | Evidence You'd See |
|-------|-----------|---------------------|-------------------|
| 1 — Emerging | ○ | No recurring routines. Alignment happens by escalation or accident. Launch means "deploy and send an email after." Support and ops find out about changes from customers. Cross-functional conflicts discovered after the fact. | No standing meetings with agendas. Launch surprises stakeholders. "Nobody told us about this" from support or training. |
| 2 — Developing | ◔ | Some routines exist (standup, maybe a sync) but attendance is spotty and follow-through inconsistent. Launch communication happens but it's ad-hoc — some people hear about it, some don't. Cross-functional input gets requested late. | Meetings without consistent agendas or action tracking. Launch email goes to whoever someone remembers. Cross-functional teams say "we found out too late." |
| 3 — Established | ◑ | Regular routines with clear purpose: refinement, roadmap review, stakeholder updates, retros. Launch has a checklist — support, training, ops, and compliance are engaged before go-live. Cross-functional syncs happen at key milestones. | Routine calendar with cadence and owners. Launch checklist with sign-offs. Stakeholder update sent on a schedule. Cross-functional sync at wave transitions. |
| 4 — Advanced | ◕ | Issues get surfaced in routines, not escalations. Communication is tailored to the audience (exec summary vs. team detail). Launch readiness is tiered by risk — lightweight for small changes, full enablement for big ones. | Routines produce tracked decisions and actions. Launch tiers documented and applied. Cross-functional teams co-own launch readiness, not just "get informed." |
| 5 — Leading | ● | Team evolves their own routines based on what's working — adds, drops, or changes cadence with rationale. Stakeholders trust the launch process enough to not ask "are we ready?" Launch post-mortems drive real process changes. | Team-initiated routine change with documented rationale. Launch runs smoothly enough that stakeholders don't escalate. Post-mortem action items actually completed. Another team adopted the routine structure. |

[Remaining dimensions to follow]
