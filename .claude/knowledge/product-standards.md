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

##### Execution Guidance

Start with a regular discovery cadence — even one customer conversation per sprint is better than none. Use `discovery/FRAMEWORK.md` Phase 1 (Signal Collection) to identify where to listen, and Phase 3 (Assumption Testing) to validate what you're hearing.

**Minimum viable practice:**
1. Set a recurring calendar block for customer conversations (interviews, ride-alongs, or support call listening)
2. Create a shared location for insights (tagged by theme, date, and segment)
3. Before each planning cycle, review recent insights and ask: "what should this change about our priorities?"
4. After launch, schedule a feedback check-in at 2 weeks and 6 weeks

**Methods to match to questions:**

| Question Type | Recommended Method |
|---------------|-------------------|
| What are users struggling with? | Interviews, support ticket analysis, session recordings |
| Is this usable? | Usability testing (moderated or unmoderated) |
| How many people have this problem? | Analytics, surveys |
| Will this concept work? | Prototype testing, concept tests |
| What changed since last quarter? | Trend review across signal sources |

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Heavy discovery — the primary activity. Validate problem-solution fit before building. |
| **Launch** | Usability testing on MVP. Rapid feedback loops. Weekly signal reviews. |
| **Growth** | Broaden signal sources. Monitor multiple segments. Shift from "do they need it?" to "is it working?" |
| **Maturity** | Focus on unmet needs in underserved segments. Monitor for satisfaction decay. |
| **Sunset** | Understand migration needs. Research what users will lose and what alternatives they need. |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | Full discovery practice — interviews, usability, analytics, support signals. |
| **Internal platform** | Internal users are still customers. Shadow sessions and support channel monitoring replace formal interviews. |
| **Regulatory** | Compliance stakeholders are a signal source. Research includes regulatory change monitoring alongside user research. |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Discovery cadence adherence (conversations per sprint) | Are we doing the practice? |
| Leading | Insights referenced in planning docs | Are insights reaching decisions? |
| Leading | Research repository activity (new entries per month) | Is knowledge being captured? |
| Lagging | Features changed or killed based on research | Did insights actually change what we built? |
| Lagging | Post-launch satisfaction vs. pre-launch hypothesis | Are we getting better at predicting what users need? |

##### Adoption Path

- **Getting started (Month 1-2):** One team member conducts 2-3 customer conversations per month. Notes go in a shared doc. Team reviews insights at planning.
- **Good at 6 months:** Regular cadence across multiple methods. Insights repository in active use. "What did we learn?" is a standing question in planning.
- **Embedded (12+ months):** Multiple signal sources monitored continuously. Research shapes the roadmap. Team has calibrated their methods — tried some, dropped what didn't work, doubled down on what did.

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

##### Execution Guidance

Start with who you're building for, then make those segments concrete. Use `discovery/FRAMEWORK.md` Phase 2 (Opportunity Mapping) to organize what you've learned about different user groups into actionable segments.

**Minimum viable practice:**
1. List the distinct groups of people who use (or should use) your product
2. For each group, answer: What do they need? How do they behave? What makes them different from the other groups?
3. Name each segment in language the team will actually use
4. Write a one-page persona for your top 2-3 segments — enough detail to make design decisions, not a novel
5. Reference segments by name in planning and prioritization ("this is for [segment name]")

**Segment quality check:** If two segments would lead to the same product decisions, they're not distinct enough to separate. If a segment is so broad that it covers everyone, it's not a segment.

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Define initial segments from discovery research. Personas are hypotheses — expect them to change. |
| **Launch** | Validate segments against early adopter behavior. Adjust personas based on who actually shows up. |
| **Growth** | Segments become strategic — different segments may need different features or engagement. Track per-segment metrics. |
| **Maturity** | Look for emerging segments or underserved needs within existing segments. Retire segments that no longer differ meaningfully. |
| **Sunset** | Understand segment-specific migration needs. Some segments may care more about the transition than others. |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | Full segmentation practice. Behavioral data and research drive segment definitions. |
| **Internal platform** | Segment by workflow or role, not org chart. "Power users vs. occasional users" often matters more than department. |
| **Regulatory** | Include regulated-entity segments alongside end-user segments. Compliance needs may define a segment on their own. |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Segments referenced by name in planning conversations | Are segments part of how the team thinks? |
| Leading | Persona review completed (annual minimum) | Are personas being maintained? |
| Lagging | Feature decisions attributed to segment needs | Are segments driving what gets built? |
| Lagging | Per-segment outcome metrics (adoption, satisfaction) | Are we serving our segments differently and effectively? |

##### Adoption Path

- **Getting started (Month 1-2):** Identify 2-3 segments from existing research or usage data. Write a one-pager for each. Start using segment names in planning.
- **Good at 6 months:** Segments are a shared vocabulary. Personas reviewed and updated. "Who is this for?" gets a specific segment name in response.
- **Embedded (12+ months):** Per-segment metrics tracked. Segments have evolved at least once based on new data. Cross-functional teams use the same definitions.

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

##### Execution Guidance

Journey mapping makes the customer's actual experience visible — not the process the team designed, but what the customer goes through. Use `discovery/FRAMEWORK.md` Phase 2-3 to connect research insights to journey stages, and to identify where friction is highest.

**Minimum viable practice:**
1. Pick one key journey (e.g., onboarding, first transaction, getting help) and map it end-to-end
2. Include touchpoints across teams — don't stop at your product boundary
3. Mark known pain points and their severity (blocker, friction, annoyance)
4. Connect the worst pain points to backlog items
5. For the design system: inventory what shared components exist, identify gaps, assign an owner

**Journey map structure:** Stages → Touchpoints → User actions → Pain points → Emotions → Opportunities. Keep it on one page. If it needs more than one page, you're mapping too many journeys at once.

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Map the current journey (how users solve this problem today) to find opportunities. The future-state journey is a hypothesis. |
| **Launch** | Validate journey assumptions with real usage. Update the map based on where users actually struggle. |
| **Growth** | Extend journey coverage to secondary flows. Measure friction per stage. Design system becomes critical as more teams build. |
| **Maturity** | Journey optimization — reduce friction in established flows. Design system governance matters as many teams contribute. |
| **Sunset** | Map the transition journey. How do users move to the replacement? What's the off-ramp experience? |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | Full journey mapping practice. Design system is externally visible — consistency directly impacts trust. |
| **Internal platform** | Employee journeys matter just as much. Map the workflow, including handoffs between systems. Design system scope may be narrower. |
| **Regulatory** | Include compliance touchpoints in the journey (disclosures, consent, verification). These are part of the customer experience even if they're mandated. |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Journey maps reviewed when planning new work | Are journeys informing what we build? |
| Leading | Design system adoption rate (% of new features using shared components) | Is the design system actually being used? |
| Leading | Pain points in the backlog with journey context | Are we connecting friction to action? |
| Lagging | Journey-stage metrics (time-on-task, error rate, satisfaction) improving | Is the experience getting better? |
| Lagging | Cross-team design consistency (visual audit pass rate) | Is the design system producing coherence? |

##### Adoption Path

- **Getting started (Month 1-2):** Map one key journey. Identify top 3 pain points. Connect them to the backlog. Inventory existing shared components.
- **Good at 6 months:** Key journeys mapped and reviewed when planning. Design system has an owner and adoption is tracked. Pain points declining for mapped journeys.
- **Embedded (12+ months):** "Where does this sit in the journey?" is the default question for new work. Journey-stage metrics on a dashboard. Design system contributed to by multiple teams.

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

##### Execution Guidance

Start by naming the one metric that best represents the product's primary value — the north star. Then build the supporting economic model around it. Use `strategy/FRAMEWORK.md` for connecting economic KPIs to strategic direction, and `prioritization/FRAMEWORK.md` for integrating economics into scoring.

**Minimum viable practice:**
1. Define the north star metric — what economic outcome best represents the product's value?
2. Document unit economics: cost to serve, value per transaction/user, margin
3. Identify 2-3 leading indicators that predict whether the north star will move
4. Build a dashboard with both leading and lagging indicators
5. Review monthly — what moved? What didn't? What will we do about it?

**Economic model components:**

| Component | Question It Answers |
|-----------|-------------------|
| North star metric | What's the primary measure of value? |
| Unit economics | What does it cost to serve one user/transaction? |
| Value drivers | What levers move the north star? |
| Leading indicators | What signals predict future performance? |
| Lagging indicators | What confirms value was delivered? |

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Economic model is a hypothesis. Focus on whether the value proposition can support a viable unit economics story. |
| **Launch** | Validate early economic signals. Unit economics may be ugly — that's expected. Track the trend, not the absolute number. |
| **Growth** | Unit economics should be improving. Leading indicators get calibrated against actual outcomes. Economic model drives investment conversations. |
| **Maturity** | Optimization — marginal improvements in cost-to-serve and value capture. Economic model is stable and trusted. |
| **Sunset** | Understand the economic cost of maintenance vs. the cost of migration. Model the transition economics. |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | Revenue, retention, and cost-to-acquire are typically the key economic levers. |
| **Internal platform** | Value is productivity gain, error reduction, or process time saved. Translate to economic terms even if there's no direct revenue. |
| **Regulatory** | Value includes risk avoidance and compliance cost. Model the cost of non-compliance as part of the economic case. |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Team can state the north star metric without looking it up | Has the economic model been internalized? |
| Leading | Economic model referenced in planning or prioritization | Are economics informing decisions? |
| Leading | Leading indicators reviewed monthly | Is the team watching the signals? |
| Lagging | Economic model accuracy (predicted vs. actual) | Is the model trustworthy? |
| Lagging | Unit economics trend (improving, stable, declining) | Is the product becoming more or less economically viable? |

##### Adoption Path

- **Getting started (Month 1-2):** Name the north star metric. Document basic unit economics. Add leading indicators to the existing dashboard.
- **Good at 6 months:** Monthly economic review in place. Finance co-owns the model. Economics referenced in prioritization conversations.
- **Embedded (12+ months):** Economic model updated when assumptions change. Predicted vs. actual reviewed quarterly. Economic rationale in roadmap and strategy docs.

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

##### Execution Guidance

Sequencing replaces opinion-based priority with a repeatable scoring method. Use `prioritization/FRAMEWORK.md` as the primary reference — it covers Balanced Breakthrough's D/F/V scoring lenses (Desirability, Feasibility, Viability), cost of delay, and R/I/T allocation.

**Minimum viable practice:**
1. Agree on scoring criteria with stakeholders (value, risk, effort — at minimum)
2. Score every candidate item before it enters the sequence
3. Write a value hypothesis for each item: "We believe [action] will result in [outcome] for [segment]"
4. Force-rank — produce a single ordered list with no ties
5. Before committing to a wave/sprint: check readiness (dependencies resolved, people available, WIP manageable)
6. Document what was deprioritized and why

**Scoring approach:**

| Dimension | What to Score | Scale |
|-----------|-------------|-------|
| **Value** | Customer impact + business impact | 1-5 or Fibonacci |
| **Risk** | What happens if we don't do this? + Execution uncertainty | 1-5 |
| **Effort** | Team-weeks or t-shirt size | S/M/L/XL |

Cost of delay (for large items): Estimate the value lost per week of delay. This separates "important" from "important *and* urgent."

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Sequencing is about which assumptions to test first. Score by learning value, not delivery value. |
| **Launch** | Fast feedback loops — sequence for fastest path to validated learning. Readiness checks are critical (don't commit to work you can't ship). |
| **Growth** | Full scoring framework in play. Multiple stakeholders contribute. Cost of delay becomes relevant for larger bets. |
| **Maturity** | Sequencing shifts toward optimization and maintenance. Value scoring may weight risk reduction and tech debt higher. |
| **Sunset** | Sequence migration and decommission tasks. Value = reducing transition pain for affected users. |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | Value scoring weights customer impact heavily. Market timing may affect sequencing. |
| **Internal platform** | Value is productivity or reliability. Scoring includes impact on downstream teams, not just direct users. |
| **Regulatory** | Compliance deadlines create hard sequencing constraints. Score within the remaining discretionary capacity. |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Items scored before entering the sequence | Is the process being followed? |
| Leading | Value hypotheses written for committed items | Are teams articulating expected value? |
| Leading | Stakeholders reference scoring in conversations | Has the framework been adopted beyond the PM? |
| Lagging | Predicted vs. actual value (quarterly review) | Is the scoring calibrated? |
| Lagging | Deprioritized items that stayed deprioritized (not re-escalated) | Are stakeholders trusting the process? |

##### Adoption Path

- **Getting started (Month 1-2):** Agree on 3 scoring criteria. Score the next planning cycle's candidates. Force-rank the top 10. Write value hypotheses for the top 5.
- **Good at 6 months:** Scoring is standard for all planning. Readiness checks before commitment. Trade-off rationale documented. Stakeholders ask "where does this score?" not "just do it."
- **Embedded (12+ months):** Quarterly predicted-vs-actual review. Scoring recalibrated based on patterns. Cross-product sequencing conversations happening.

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

##### Execution Guidance

Guardrails prevent drift. Kill criteria prevent zombie initiatives. Benefits realization closes the feedback loop. Use `prioritization/FRAMEWORK.md` for R/I/T capacity allocation (the capitalization half of Balanced Breakthrough), and `strategy/FRAMEWORK.md` for connecting guardrails to strategic intent.

**Minimum viable practice:**
1. Define guardrails for CX (e.g., NPS floor, response time ceiling), reliability (e.g., uptime target, error rate ceiling), and capacity (R/I/T allocation targets)
2. Put guardrails on a dashboard that gets reviewed monthly
3. For every initiative above a size threshold: define kill criteria before starting (time trigger, adoption trigger, or value trigger)
4. Set R/I/T allocation targets and review actuals quarterly
5. Schedule a benefits realization check at launch time (not after — at the same time you plan the launch)

**Kill criteria template:**

| Trigger Type | Example | Decision |
|-------------|---------|----------|
| Time | 6 months without measurable progress | Review: pivot, reduce scope, or kill |
| Adoption | <10% target adoption at 3 months post-launch | Diagnose: is it a product problem or an enablement problem? |
| Value | Projected benefits <50% of business case at midpoint | Escalate: continue with reduced investment or kill |

**R/I/T allocation guidance:**

| Category | Definition | Typical Range |
|----------|-----------|---------------|
| Run | Keep the lights on — maintenance, support, compliance | 40-60% |
| Improve | Make what exists better — optimization, tech debt, UX improvement | 20-30% |
| Transform | Build what's new — new capabilities, new markets, strategic bets | 15-30% |

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Kill criteria are tight — short time horizons, clear go/no-go checkpoints. R/I/T is mostly Transform. |
| **Launch** | Kill criteria focus on adoption signals. Guardrails protect launch quality (reliability, CX). R/I/T shifts as the product moves from build to scale. |
| **Growth** | Guardrails widen to cover more dimensions (performance, cost efficiency). R/I/T balances across all three. Benefits realization becomes routine. |
| **Maturity** | R/I/T shifts heavily to Run and Improve. Kill criteria apply to improvement initiatives, not just new features. Guardrails are well-established. |
| **Sunset** | Guardrails ensure the transition doesn't damage the customer experience. R/I/T is almost entirely Run. Kill criteria may apply to the product itself. |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | CX guardrails are critical — direct impact on trust and retention. Benefits realization ties to revenue or market share. |
| **Internal platform** | Reliability guardrails matter most — downstream teams depend on uptime. Benefits measured in productivity or error reduction. |
| **Regulatory** | Compliance itself is a guardrail. Non-compliance is a kill trigger. Benefits include risk avoidance (model the cost of fines or audit findings). |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Guardrails defined and on a dashboard | Are guardrails visible? |
| Leading | Kill criteria written before initiative start | Are we planning for failure modes? |
| Leading | R/I/T actuals tracked against targets | Are we managing capacity deliberately? |
| Lagging | At least one initiative killed or pivoted based on criteria | Are kill criteria real or decorative? |
| Lagging | Benefits realization accuracy (predicted vs. actual) | Are we getting better at forecasting value? |
| Lagging | R/I/T drift from target (<10% = on track) | Is capacity allocation holding? |

##### Adoption Path

- **Getting started (Month 1-2):** Define 3-5 guardrails (CX, reliability, one capacity metric). Put them on a dashboard. Set R/I/T targets for the next quarter.
- **Good at 6 months:** Kill criteria defined for new initiatives. R/I/T reviewed quarterly with documented actuals. At least one kill/pivot decision made.
- **Embedded (12+ months):** Teams flag their own guardrail breaches. Benefits realization is scheduled at launch planning time. R/I/T allocation proposed by teams, not just assigned.

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

##### Execution Guidance

Outcomes anchor the product — they define what success looks like before anyone decides what to build. Use `strategy/FRAMEWORK.md` for connecting vision to measurable outcomes, and the Opportunity Solution Tree model from `discovery/FRAMEWORK.md` for linking outcomes to the work that moves them.

**Minimum viable practice:**
1. Write a product vision that names the customer, the value delivered, and what would be true if the product succeeds
2. Define 3-5 KPIs with explicit targets (not just metrics — targets)
3. For each KPI, identify at least one leading indicator
4. Review monthly: what moved, what stalled, what will the team do differently?
5. Revisit the vision annually or when strategic context shifts

**Vision quality check:** Can you imagine a world where this vision statement is false? If not, it's too vague. "Deliver great customer experiences" can never be wrong. "Reduce time-to-first-value from 14 days to 3 days for self-service customers" can be checked.

**KPI structure:**

| Component | Example |
|-----------|---------|
| Metric | Activation rate (% of new users completing first transaction within 7 days) |
| Current | 38% |
| Target | 55% by end of Q3 |
| Leading indicator | Onboarding completion rate (predicts activation) |
| Review cadence | Monthly |

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Vision is the primary artifact. KPIs are hypothesized — you're defining what you'd measure, not yet measuring it. |
| **Launch** | KPIs are live but baselines are being established. Focus on whether early signals confirm the vision. |
| **Growth** | Full KPI suite in place with targets. Monthly reviews drive adjustments. Vision is validated — refinement, not redefinition. |
| **Maturity** | Optimization against established KPIs. Vision may need refreshing if the market has shifted. |
| **Sunset** | KPIs shift to transition metrics (migration rate, user communication coverage). Vision becomes the rationale for sunset. |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | Outcome metrics include adoption, satisfaction, retention, revenue contribution. |
| **Internal platform** | Outcome metrics include platform reliability, developer productivity, downstream team satisfaction. |
| **Regulatory** | Outcome metrics include compliance coverage, audit readiness, and time-to-compliance for new regulations. |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Vision documented and accessible to the team | Does the team know what they're aiming at? |
| Leading | KPIs have explicit targets (not just metrics) | Are outcomes defined specifically enough to track? |
| Leading | Monthly review produces at least one action | Is the review driving change, not just reporting? |
| Lagging | Outcome targets met or trending toward target | Is the product achieving what it set out to? |
| Lagging | Planning references outcomes, not just features | Has outcome thinking taken hold? |

##### Adoption Path

- **Getting started (Month 1-2):** Write the vision. Define 3 KPIs with targets. Start monthly review.
- **Good at 6 months:** KPIs reviewed monthly with documented actions. Leading indicators tracked alongside lagging. Planning conversations reference outcomes.
- **Embedded (12+ months):** Vision revisited when context changes. KPIs connect from business goals to team-level work. Outcome data informs investment decisions.

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

##### Execution Guidance

Strategy sets direction. The roadmap makes it visible and sequenced. OKRs connect strategy to what teams do this quarter. Use `strategy/FRAMEWORK.md` as the primary reference — it covers diagnosis, guiding policy, and coherent action, which maps directly to strategy → roadmap → OKRs.

**Minimum viable practice:**
1. Write the strategy: What's the situation? What's our approach? What coherent actions follow?
2. Organize the roadmap by time horizon: Now (committed), Next (planned), Later (directional), Vision (aspirational)
3. Each roadmap item connects to a strategic theme and states an expected outcome
4. Define OKRs per quarter: 2-3 objectives with 2-4 measurable key results each
5. Review the roadmap quarterly; review OKR progress monthly

**Roadmap item template:**

| Field | Content |
|-------|---------|
| Strategic theme | Which strategic priority does this serve? |
| Outcome | What will be different when this is done? |
| Time horizon | Now / Next / Later / Vision |
| Key results connected | Which OKR key results does this advance? |
| Confidence level | High / Medium / Low (decreases as horizon extends) |

**OKR quality check:** If every key result is a binary "did we launch X?" — these are tasks, not outcomes. Key results should be measurable states: "Increase X from A to B," "Reduce Y by Z%."

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Roadmap is mostly Later and Vision. OKRs focus on validation milestones (assumptions tested, not features shipped). |
| **Launch** | Roadmap shifts to Now and Next. OKRs track adoption and early signal metrics. |
| **Growth** | Full roadmap with all horizons active. OKRs balance growth metrics with sustainability metrics. |
| **Maturity** | Roadmap is weighted toward Now and Next. OKRs focus on optimization, retention, and efficiency. Strategic themes may include "defend" not just "grow." |
| **Sunset** | Roadmap is a transition plan. OKRs cover migration, communication, and decommission milestones. |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | Roadmap is a communication tool for sales, marketing, and customer success. OKRs tie to market metrics. |
| **Internal platform** | Roadmap serves internal stakeholders (consuming teams). OKRs include platform reliability and developer experience. |
| **Regulatory** | Compliance deadlines create fixed roadmap items. OKRs include regulatory readiness alongside product outcomes. |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Roadmap items have stated outcomes (not just feature names) | Is the roadmap outcome-oriented? |
| Leading | OKRs reviewed monthly | Are teams tracking against outcomes? |
| Leading | Roadmap updated within the last quarter | Is the roadmap alive? |
| Lagging | OKR attainment rate (% of key results met) | Are the team's bets paying off? |
| Lagging | Roadmap items traced to delivered outcomes | Did the roadmap predict what actually happened? |

##### Adoption Path

- **Getting started (Month 1-2):** Write a one-page strategy. Organize existing plans into Now/Next/Later. Set OKRs for the current quarter.
- **Good at 6 months:** Roadmap reviewed and updated quarterly. OKRs adjusted when data warrants it. Team can explain strategy → roadmap → OKR connection.
- **Embedded (12+ months):** Roadmap is the primary communication tool for cross-team planning. Strategy has a decision log. Teams propose strategic themes, not just execute them.

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

##### Execution Guidance

Delivery is the bridge between decisions and outcomes. Use `execution/FRAMEWORK.md` as the primary reference — it covers the Discuss → Plan → Execute → Verify cycle. The key is keeping the process adaptive: tight enough to be predictable, loose enough to absorb new information.

**Minimum viable practice:**
1. Define an intake process: how does new work enter? What criteria determine whether it's accepted, deferred, or rejected?
2. Set a refinement cadence (weekly or biweekly) — the backlog should never go more than 2 weeks without review
3. Deliver in waves or sprints with clear boundaries (what's committed, what's stretch, what's deferred)
4. Maintain a risk register — review at wave/sprint boundaries, not just in retros
5. Track velocity enough to forecast — stakeholders need to trust delivery timelines

**Intake evaluation criteria:**

| Question | Purpose |
|----------|---------|
| What problem does this solve? | Filters noise from signal |
| Who benefits? (Which segment?) | Connects to segmentation |
| Does it score above the cut line? | Connects to value-based sequencing |
| Are dependencies resolved? | Checks readiness |
| What's the risk of not doing it? | Separates urgent from important |

**Risk register structure:**

| Risk | Likelihood | Impact | Mitigation | Owner | Status |
|------|-----------|--------|-----------|-------|--------|
| [Description] | H/M/L | H/M/L | [Action] | [Person] | Open/Mitigated/Closed |

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Lightweight intake — ideas flow freely but get evaluated. Short cycles (1-2 weeks). Risk focus: are we testing the right assumptions? |
| **Launch** | Tight cadence — weekly sprints or shorter. Intake is filtered aggressively. Risk focus: launch readiness, quality. |
| **Growth** | Standard cadence (2-week sprints or monthly waves). Intake feeds into scoring framework. Risk focus: scaling, performance, team capacity. |
| **Maturity** | Broader cadence may work (monthly waves). Intake volume is lower and more predictable. Risk focus: tech debt, dependency decay. |
| **Sunset** | Cadence covers migration and decommission. Intake is restricted to transition-related work. Risk focus: data migration, user communication. |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | Delivery cadence aligns to market timing and customer expectations. Risk register includes competitive and market risks. |
| **Internal platform** | Delivery cadence aligns to consuming team needs. Risk register includes downstream impact assessment. |
| **Regulatory** | Compliance deadlines create hard delivery constraints. Risk register must include regulatory risk explicitly. |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Refinement happening on schedule | Is the backlog being maintained? |
| Leading | Intake items evaluated before entering the backlog | Is the filter working? |
| Leading | Risk register reviewed at wave boundaries | Are risks being managed proactively? |
| Lagging | Delivery forecast accuracy (predicted vs. actual) | Can stakeholders trust the timeline? |
| Lagging | Stale backlog items (<5% older than one quarter) | Is the backlog clean? |
| Lagging | Risks mitigated before escalation | Is risk management working? |

##### Adoption Path

- **Getting started (Month 1-2):** Define intake criteria. Set a refinement cadence. Start a risk register (even if it's a spreadsheet with 3 rows). Deliver in defined waves.
- **Good at 6 months:** Intake feeds into scoring. Refinement is consistent. Velocity is stable enough to forecast. Risks caught before they hit.
- **Embedded (12+ months):** Cadence adapts to lifecycle stage. Forecasts trusted by stakeholders. Team adjusts their own process based on what's working.

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

##### Execution Guidance

Routines make coordination reliable instead of accidental. Use `execution/FRAMEWORK.md` Phase 3-4 (Execute and Verify) for the rhythm of delivery routines, and the communication patterns from `skills/executive-storytelling/SKILL.md` for tailoring stakeholder updates.

**Minimum viable practice:**
1. Define the routine calendar: what meetings exist, what's their purpose, who attends, what cadence?
2. Every routine produces an artifact: decisions made, actions committed, or information shared
3. Launch enablement: create a tiered launch checklist (not every change needs full enablement)
4. Cross-functional sync at key milestones (wave transitions, launches, major decisions)
5. Retros produce real changes — track action items and close them

**Routine calendar template:**

| Routine | Purpose | Cadence | Attendees | Output |
|---------|---------|---------|-----------|--------|
| Refinement | Prepare backlog items for delivery | Weekly/biweekly | PM, Engineering, Design | Refined items ready for commitment |
| Roadmap review | Align on direction and progress | Quarterly | PM, Leadership, Stakeholders | Updated roadmap, decisions documented |
| Stakeholder update | Inform and gather feedback | Monthly or biweekly | PM, Key stakeholders | Status summary, decisions needed |
| Retro | Improve how the team works | End of wave/sprint | Full team | Action items with owners and dates |
| Launch readiness | Confirm readiness across functions | Pre-launch | PM, Support, Training, Ops, Compliance | Go/no-go decision with sign-offs |

**Launch enablement tiers:**

| Tier | When to Apply | What's Included |
|------|-------------|----------------|
| **Lightweight** | Small changes, bug fixes, internal updates | Internal notification, release notes |
| **Standard** | Meaningful feature changes, workflow updates | Support briefing, training update, customer communication |
| **Full** | Major launches, new products, breaking changes | All of Standard + compliance review, ops readiness, comms plan, executive briefing |

##### Applicability

| Lifecycle Stage | What This Looks Like |
|----------------|---------------------|
| **Concept** | Fewer routines — focus on discovery syncs and stakeholder alignment. Launch enablement doesn't apply yet. |
| **Launch** | Full routine cadence. Launch enablement is critical. Cross-functional coordination is highest here. |
| **Growth** | Routine calendar stabilizes. Launch tiers established. Stakeholder updates become more structured. |
| **Maturity** | Routines are well-established and may need pruning (are all still adding value?). Launch enablement is tiered and efficient. |
| **Sunset** | Routines shift to transition-focused: migration updates, stakeholder communication, decommission coordination. |

| Product Type | Adaptation |
|-------------|-----------|
| **Customer-facing** | Launch enablement includes customer communication, sales enablement, and marketing coordination. Stakeholder updates include external-facing metrics. |
| **Internal platform** | Launch enablement focuses on consuming team readiness. Stakeholder updates emphasize platform health and upcoming changes. |
| **Regulatory** | Launch enablement must include compliance sign-off. Routines include regulatory change monitoring cadence. |

##### Measurement

| Type | Indicator | What It Tells You |
|------|-----------|------------------|
| Leading | Routines have documented purpose and consistent agendas | Are routines intentional? |
| Leading | Launch checklist completed before go-live | Is launch enablement happening? |
| Leading | Cross-functional partners engaged before decisions are final | Are we avoiding "found out too late"? |
| Lagging | Issues surfaced in routines vs. escalations (higher ratio = better) | Are routines doing their job? |
| Lagging | Retro action items completed (% closed within 2 sprints) | Are retros producing change? |
| Lagging | Launch surprises (stakeholder complaints about not being informed) | Is the launch process working? |

##### Adoption Path

- **Getting started (Month 1-2):** Define purpose for each existing meeting. Add a launch checklist (even a simple one). Start tracking retro action items.
- **Good at 6 months:** Routine calendar with clear ownership. Launch tiers defined and applied. Cross-functional syncs at milestones. Retro actions consistently closed.
- **Embedded (12+ months):** Team evolves routines based on what's working — adds, drops, changes cadence with documented rationale. Launch process trusted by stakeholders. Routines produce decisions, not just discussions.

---

## Cross-Cutting: Dependencies Between Sub-Practices

The 10 sub-practices are not independent — they form a dependency network where
skipping prerequisites creates dependency debt (surface-level compliance without
real capability).

Two dependency maps document these relationships:

- **Adoption view** — `knowledge/product-standards-dependencies-adoption.md`
  10 sub-practice nodes grouped by pillar. Shows dependency types and strengths.
  Includes a 4-wave recommended adoption sequence. Use this to decide where teams
  should start and what to sequence next.

- **Reference view** — `knowledge/product-standards-dependencies-reference.md`
  ~39 Level 3 standard nodes with all cross-sub-practice dependencies. Use this
  when coaching teams on specific gaps — trace which prerequisites are missing
  and which downstream standards will suffer.

- **Applicability matrix** — `knowledge/product-standards-applicability.md`
  Target maturity levels per standard, per lifecycle stage and product type.
  Includes a "find your row" lookup and companion Mermaid views by lifecycle
  stage (`product-standards-applicability-lifecycle.md`) and by pillar
  (`product-standards-applicability-pillar.md`). Use this to determine which
  standards to prioritize based on where your product is today.

- **Sub-practice to repo map** — `knowledge/product-standards-repo-map.md`
  For each sub-practice, the primary framework, primary skill, and key knowledge
  files to load when a team scores low. Includes coaching guidance per maturity
  level and secondary skill cross-references.

Both dependency maps were built using `frameworks/dependency-mapping/FRAMEWORK.md`.
