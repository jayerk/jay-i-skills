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

##### Purpose & Value

Without regular contact with customers, product teams build based on assumptions.
Those assumptions compound. Customer & Market Insights ensures decisions are grounded
in what real users actually experience, need, and struggle with — not what stakeholders
imagine they do. This is the foundation that makes every other sub-practice honest.

##### Principles

1. **Talk to customers before building.** Prototypes and concepts get user feedback before the team commits resources. The cost of a conversation is always less than the cost of building the wrong thing.
2. **Store insights where the team can find them.** Research that lives in someone's notebook doesn't exist. A shared, searchable location is the minimum bar.
3. **Match the method to the question.** Interviews, usability tests, analytics, support ticket analysis, and surveys answer different questions. Don't default to one method for everything.
4. **Make insights part of the rhythm, not a special event.** Regular discovery cadence beats periodic research sprints. Build it into how the team works, not as a separate workstream.
5. **Close the loop.** Check whether what you launched actually solved the problem. Post-launch feedback is not optional — it's how you calibrate your understanding.

##### Governance

- **Owner:** Product manager for the product group, with design research support where available.
- **Review cadence:** Quarterly — are we still talking to customers regularly? Is the research repository being used? Are insights showing up in planning?
- **Update trigger:** New product launch, significant customer complaint trend, or team restructure.

[How-To dimensions to follow]

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

##### Purpose & Value

When everyone says "the user," no one is designing for anyone specific. Segmentation
forces the team to answer "who is this for?" with a real answer — based on behaviors,
needs, or value, not demographics or org chart. Personas make those segments tangible
enough to reference in planning, design, and prioritization conversations.

##### Principles

1. **Segment by behavior or need, not demographics.** "Enterprise vs. SMB" is an org chart, not a segment. "Users who need self-service vs. users who need guided onboarding" drives product decisions.
2. **Keep segments few enough to remember.** If the team can't name the segments without looking them up, there are too many — or they don't matter enough.
3. **Reference segments in decisions.** Segment definitions that don't show up in planning, prioritization, or design reviews aren't working. The test: does the team say "this matters most for segment X" in regular conversations?
4. **Maintain personas as living documents.** A persona created two years ago for a project that ended is not a persona — it's an artifact. Review at least yearly.
5. **Share across functions.** Product, design, and marketing should use the same segment definitions. If they don't, you have three different views of the customer.

##### Governance

- **Owner:** Product manager, with input from design and marketing.
- **Review cadence:** Annually at minimum — are segments still accurate? Has the customer base shifted?
- **Update trigger:** New market entry, significant usage pattern change, or cross-functional misalignment on who the customer is.

[How-To dimensions to follow]

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

##### Purpose & Value

Features don't exist in isolation — customers experience a journey across touchpoints,
teams, and channels. Without a shared view of that journey, each team optimizes their
piece while the overall experience has gaps, redundancies, and handoff friction nobody
owns. Journey mapping makes the end-to-end experience visible so teams can coordinate.
A design system ensures consistency across whatever teams build.

##### Principles

1. **Map end-to-end, not just your team's piece.** The journey includes what happens before and after your product. Include handoffs, even if another team owns them — especially if another team owns them.
2. **Keep maps alive.** A journey map from last year's project is decoration. Update when flows change, new features launch, or pain points shift.
3. **Connect pain points to the backlog.** Identified friction that isn't tracked anywhere won't get fixed. Pain points need journey context when they enter the backlog.
4. **Own the design system.** Shared components without an owner decay. Someone needs to maintain, version, and track adoption — not just create and hope.
5. **Measure the journey, not just the feature.** Time-on-task, error rates, and satisfaction per journey stage tell you whether the experience is improving. Feature-level metrics alone miss the handoffs.

##### Governance

- **Owner:** Design lead or product manager, depending on org structure. Design system has its own owner (may be the same person or a dedicated role).
- **Review cadence:** Quarterly for journey maps (are they still accurate?). Monthly for design system health (adoption, contribution, issue backlog).
- **Update trigger:** New channel or touchpoint, customer complaint trend about handoffs, or team restructure that changes journey ownership.

[How-To dimensions to follow]

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

##### Purpose & Value

If the team can't explain how the product creates economic value, they can't make
informed trade-offs. Product Economic Insights gives the team a shared understanding
of what drives value (not just what's popular), what it costs to deliver, and what
leading indicators predict future performance — so decisions are grounded in economics,
not anecdotes.

##### Principles

1. **Know your north star metric.** One economic KPI that represents the primary source of value. The whole team should be able to state it and explain why it matters. If you get three different answers, you haven't defined it.
2. **Track leading alongside lagging.** Revenue and retention tell you what already happened. Activation rate, time-to-value, and engagement signal what's coming. Without leading indicators, you're driving by the rearview mirror.
3. **Understand unit economics.** "What does it cost to serve one user/transaction?" is a question the team should be able to answer. Budget-level cost understanding isn't enough to make product decisions.
4. **Make finance a partner, not a gatekeeper.** Product and finance should co-own the economic model. If they speak different languages, neither side trusts the numbers.
5. **Update the model when assumptions change.** An economic model from the business case that never gets revised is fiction. Review when pricing changes, cost structure shifts, or market conditions move.

##### Governance

- **Owner:** Product manager, with finance as co-owner of the economic model.
- **Review cadence:** Monthly metric review. Quarterly model review (are assumptions still valid?).
- **Update trigger:** Pricing change, new revenue stream, significant cost shift, or north star metric no longer reflects primary value.

[How-To dimensions to follow]

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

##### Purpose & Value

Without a defensible sequencing method, the backlog is ordered by politics — whoever
escalated last or whoever is most senior wins. Value-Based Sequencing replaces "because
I said so" with a shared scoring framework that makes trade-offs visible and debatable.
It also ensures the team doesn't commit to work they can't actually execute by checking
readiness before sequencing.

##### Principles

1. **Score before you sequence.** Every item gets scored on value, risk, and effort before it enters the sequence. No scoring, no sequence — otherwise you're just guessing.
2. **Write down the value hypothesis.** Each item should have a short statement: "we believe X will result in Y." This is what you check later to see if the investment paid off.
3. **Force-rank — no ties.** If two items are both "high priority," you haven't prioritized. Ranking forces the hard conversation about what comes first and what waits.
4. **Check readiness before committing.** Before the team takes on work: Are dependencies resolved? Do we have the right people? Is WIP manageable? Sequencing items the team can't execute creates the illusion of progress.
5. **Document trade-offs.** When something gets deprioritized, write down why. This prevents re-litigation and gives stakeholders a clear answer when they ask "why not this?"

##### Governance

- **Owner:** Product manager owns the backlog sequence. Scoring criteria co-owned with stakeholders.
- **Review cadence:** Scoring criteria reviewed quarterly. Backlog sequence reviewed at every planning cycle.
- **Update trigger:** New strategic direction, major stakeholder change, or pattern of scoring miscalibration (predicted value consistently off).

[How-To dimensions to follow]

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

##### Purpose & Value

Without guardrails, initiatives drift. Without kill criteria, zombie projects consume
resources indefinitely. Without benefits tracking, the team never learns whether their
estimates were right. Value Guardrails & Realization creates the boundaries that keep
investment focused and the feedback loops that make future planning more accurate.
Run/Improve/Transform allocation makes capacity decisions deliberate instead of accidental.

##### Principles

1. **Define guardrails for CX, reliability, and capacity.** These are the things that shouldn't degrade while you pursue new value. If you don't name them, nobody protects them.
2. **Set kill criteria before you start.** Time trigger, adoption trigger, value trigger — define upfront what would cause you to stop or pivot. Deciding to kill something after the money runs out isn't a decision, it's an inevitability.
3. **Track R/I/T allocation — don't just set targets.** Run/Improve/Transform targets are only useful if you compare actuals against them. Otherwise the allocation drifts to whatever is urgent.
4. **Close the loop on benefits.** When you forecasted benefits in the business case, schedule the check-in at launch time. "Did the value hypothesis play out?" is a question you answer with data, not hope.
5. **Make kill decisions early.** The sunk cost trap is real. The best time to kill a failing initiative is before the budget is exhausted, not after.

##### Governance

- **Owner:** Product manager for product-level guardrails. Portfolio lead for R/I/T allocation targets.
- **Review cadence:** Guardrails reviewed monthly. R/I/T actuals vs. targets reviewed quarterly. Benefits realization reviewed post-launch (timing defined per initiative).
- **Update trigger:** Guardrail breach, R/I/T drift exceeding 10% from target, or kill criteria triggered.

[How-To dimensions to follow]

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

##### Purpose & Value

If the team can't say what outcome the product exists to create, everything else
is activity without direction. Measurable Outcomes connects what the team builds
to what it expects to achieve — not in vague aspirational terms, but in specific
enough language that you can check whether it's true. This is the anchor that
makes roadmaps, prioritization, and delivery meaningful.

##### Principles

1. **Vision should be falsifiable.** "Deliver great experiences" can never be wrong, which means it's useless. A good vision says what value the product delivers to whom, and you could check whether it's happening.
2. **Track outcomes, not just outputs.** Features delivered and story points completed measure activity. Adoption, satisfaction, and retention measure whether the activity mattered.
3. **Pair leading with lagging indicators.** Lagging indicators (retention, revenue) tell you what happened. Leading indicators (activation, engagement) tell you what's coming. You need both to act in time.
4. **Set targets, not just metrics.** A KPI without a target is just a number. Targets create the conversation: are we on track? If not, what changes?
5. **Review regularly and act.** Monthly metric review that doesn't produce actions is theater. The purpose of the review is to decide what to do differently.

##### Governance

- **Owner:** Product manager owns vision and outcome targets. Engineering and design co-own the metrics that reflect their contributions.
- **Review cadence:** Monthly KPI review with actions. Vision reviewed annually or when strategic direction shifts.
- **Update trigger:** Outcome targets consistently missed or exceeded (recalibrate), market shift, or strategy change.

[How-To dimensions to follow]

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

##### Purpose & Value

A roadmap without strategy is a project plan. Strategy without a roadmap is
aspirations with no follow-through. Strategy & Roadmap connects the two — it
translates direction into a multi-horizon plan that teams can execute against,
stakeholders can align on, and the organization can hold accountable. OKRs make
the connection between strategic intent and team-level work explicit.

##### Principles

1. **Roadmaps show outcomes, not features.** "Reduce onboarding time by 30%" is a roadmap item. "Build new onboarding wizard" is a project plan. The outcome stays stable even if the solution changes.
2. **Organize by time horizon, not fixed dates.** Now (this quarter), Next (next quarter), Later (this year), Vision (beyond). This signals commitment level — Now is committed, Later is directional.
3. **Connect every roadmap item to a strategic theme.** If it's not connected, either the strategy is incomplete or the item doesn't belong on the roadmap.
4. **OKRs are outcomes, not activities.** "Launch feature X" is a task. "Increase activation rate from 40% to 55%" is a key result. If your OKRs are a to-do list, rewrite them.
5. **Update the roadmap when the world changes.** A roadmap that hasn't changed in 6 months either means nothing has been learned or the team isn't updating. Quarterly review is the minimum cadence.

##### Governance

- **Owner:** Product manager owns the roadmap. Strategy is co-owned with product leadership. OKRs co-owned with the team.
- **Review cadence:** Quarterly roadmap review and update. OKRs reviewed monthly, adjusted mid-cycle if data warrants.
- **Update trigger:** New strategic direction, significant market shift, or OKR consistently off-track (signals roadmap needs to change, not just the team needs to try harder).

[How-To dimensions to follow]

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

##### Purpose & Value

Strategy and prioritization decide what to build and in what order. Adaptive Delivery
Plans decide how work actually flows — from intake through delivery. Without structured
intake, work arrives by interrupt. Without regular refinement, the backlog decays.
Without risk management, surprises hit at launch. This sub-practice creates the
operational rhythm that turns good decisions into reliable delivery.

##### Principles

1. **Define how work enters.** New requests need an intake process with evaluation criteria. "Just put it in Jira" is not intake — it's a to-do list with no filter.
2. **Refine regularly.** Backlog items older than one quarter that haven't been touched should be re-evaluated or removed. Stale backlogs create the illusion of more work than exists.
3. **Manage risks before they manage you.** A risk register reviewed at wave or sprint boundaries catches emerging risks early. Discussing risks in retros means you're already doing post-mortems.
4. **Adapt cadence to lifecycle.** Launch-stage products need tighter feedback loops (shorter cycles, faster pivots). Mature products can operate on broader cadences. One-size-fits-all cadence is a missed opportunity.
5. **Monitor pace.** Sustainable delivery means the team can maintain this velocity for the next 6 months without burnout. If the team is sprinting to keep up, the capacity plan is wrong.

##### Governance

- **Owner:** Product manager owns intake and backlog priority. Delivery lead (scrum master, tech lead, or equivalent) owns the delivery cadence and risk register.
- **Review cadence:** Intake and backlog refined weekly or biweekly. Risk register reviewed at wave/sprint boundaries. Cadence reviewed quarterly.
- **Update trigger:** Delivery forecast consistently off, team capacity change, or lifecycle stage transition.

[How-To dimensions to follow]

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

##### Purpose & Value

Routines are the connective tissue between strategy, delivery, and stakeholders.
Without them, alignment is accidental — people find out about changes when it's too
late to contribute. Launch enablement ensures support, training, ops, and compliance
are ready before customers see the change, not after. Routines for Activation turns
"we should communicate better" into a specific calendar with specific purposes.

##### Principles

1. **Every routine has a purpose.** If you can't state why a meeting exists in one sentence, cancel it. Refinement refines. Roadmap review aligns. Stakeholder updates inform. Retros improve.
2. **Launch readiness is tiered.** Not every change needs full enablement. Define tiers — lightweight (internal notification), standard (support + training engaged), full (compliance, ops, comms, training, support). Apply the right tier to the right change.
3. **Engage cross-functional partners early.** Support, training, and ops should be at the table during planning, not notified after decisions are made. "We found out too late" is a process failure, not a communication failure.
4. **Track routine outcomes.** A meeting that produces no decisions or actions is not a routine — it's a habit. Track what was decided and what was committed.
5. **Evolve routines based on what works.** If a routine isn't adding value, change it or drop it. If the team needs something they don't have, add it. The calendar should reflect current needs, not historical decisions.

##### Governance

- **Owner:** Product manager owns the routine calendar and stakeholder communication. Delivery lead co-owns refinement and retro routines. Launch enablement owned by product manager with cross-functional input.
- **Review cadence:** Routine effectiveness reviewed in retros. Launch process reviewed after major launches. Calendar reviewed quarterly.
- **Update trigger:** Stakeholder feedback about being surprised, missed launch readiness, or routine attendance/effectiveness declining.

[How-To dimensions to follow]
