# Product Standards: Universal Adoption Path

A team-type-aware, assessment-driven on-ramp for adopting the 10 sub-practices and
39 standards. Not a change management plan — a pragmatic sequencing guide that
answers: "Given my team type, domain, and current state, what do I do next?"

**Companion files:**
- `product-standards.md` — full sub-practice definitions, rubrics, and per-sub-practice adoption paths
- `product-standards-applicability.md` — target maturity levels by lifecycle stage and product type
- `product-standards-dependencies-adoption.md` — 4-wave adoption sequence with dependency rationale
- `product-standards-dependencies-reference.md` — within-sub-practice dependencies and starting standards
- `templates/SCORECARD-TEMPLATE.md` — assessment template

---

## How to Use This Guide

1. **Assess** — Run the scorecard (`templates/SCORECARD-TEMPLATE.md`) to establish your current level per sub-practice
2. **Identify your team type and domain** — Use the Team Type × Domain Matrix below to understand how the standards apply to your context
3. **Size your capacity** — Determine how many standards your team can meaningfully improve alongside BAU delivery
4. **Sequence** — Follow the wave-sequenced path, starting with the starting standards for your highest-gap areas
5. **Expand** — As starting standards reach Level 2+, add expansion standards within each wave

---

## Team Type × Domain Matrix

### The Four Team Types

| Team Type | Definition | Primary Value Stream |
|---|---|---|
| **Stream-Aligned** | Owns a product, service, or user journey. The primary team type. Optimized for fast flow of change. | Delivering value to end users or business stakeholders |
| **Platform** | Provides internal services to reduce cognitive load on stream-aligned teams. Treats services as internal products. | Reducing friction and cognitive load for consuming teams |
| **Enabling** | Helps other teams adopt new capabilities. Temporary engagement — the goal is to upskill, not do the work permanently. | Accelerating capability adoption across teams |
| **Complicated Subsystem** | Owns a subsystem requiring deep specialist knowledge (ML models, regulatory engines, etc.). | Encapsulating specialist complexity so others don't carry it |

### How Team Type Shapes Adoption Emphasis

Each team type applies the same 10 sub-practices, but the emphasis and interpretation shift.

| Dimension | Stream-Aligned | Platform | Enabling | Complicated Subsystem |
|---|---|---|---|---|
| **Which pillar leads** | Pillar 1 (Customer) | Pillar 3 (Lifecycle) | All pillars (coaching lens) | Pillar 2 (Economics) + Pillar 3 |
| **"Customer" means** | End users, market segments | Consuming teams, internal developers | Teams being enabled | Upstream teams consuming the subsystem |
| **CMI emphasis** | External research, interviews, usability testing | Internal team feedback, support channels, usage analytics | Capability gap research across teams | Specialist domain monitoring, upstream team needs |
| **S&P emphasis** | Behavioral/needs-based segments from market data | Segment by workflow, role, or consuming team type | Segment by capability maturity level of coached teams | Segment by integration pattern or consumption model |
| **PEI emphasis** | Revenue, retention, cost-to-acquire | Productivity gain, error reduction, developer time saved | Enablement ROI, time-to-capability for coached teams | Specialist effort cost, build-vs-buy, integration cost |
| **VBS emphasis** | Customer impact, market timing | Downstream team impact, platform reliability | Enablement ROI, coaching capacity allocation | Technical risk, specialist effort, integration complexity |
| **S&R emphasis** | Market-facing roadmap, competitive positioning | Platform capability roadmap, API versioning strategy | Coaching engagement roadmap, capability target dates | Subsystem evolution roadmap, technology refresh |
| **VGR emphasis** | CX guardrails, adoption metrics | Reliability/uptime guardrails, SLA adherence | Coaching outcome guardrails, handoff quality criteria | Technical integrity guardrails, integration stability |
| **RfA emphasis** | Launch enablement, customer comms, sales readiness | API docs, migration guides, consuming team readiness | Coaching cadence, handoff criteria, capability checkpoints | Integration checkpoints, specialist review gates |

### Domain Context

Within each team type, the domain modifies emphasis further. These map to the three product types in the applicability matrix.

| Domain | Product Segment Examples | Key Adjustment |
|---|---|---|
| **Customer-Facing** | Retail banking, digital channels, wealth management | Full external research. CX guardrails critical. Journey maps include customer touchpoints across channels. |
| **Internal Platform** | Developer tools, data infrastructure, shared services | Consuming-team feedback replaces interviews. "Usability" = developer experience. Journey maps include system handoffs and workflow integration. |
| **Regulatory** | Compliance engines, risk systems, regulatory reporting | Compliance is both a guardrail and a customer need. VGR-c (kill criteria) includes compliance deadlines as hard constraints. Regulatory change monitoring is a standing CMI activity. |

**Reading the combination:** A *platform team in a regulatory domain* emphasizes consuming-team feedback (platform lens) but adds regulatory change monitoring as a standing CMI activity and treats compliance deadlines as hard delivery constraints. A *stream-aligned team in an internal platform domain* emphasizes developer experience as the customer lens but otherwise follows the stream-aligned adoption emphasis.

---

## Capacity Sizing

Before sequencing adoption, teams should honestly assess how many improvement
slots they have — a slot is one standard the team can meaningfully work on alongside
BAU delivery. Most teams have 2-3 per quarter.

| Team Capacity | Standards Per Cycle | Recommended Approach |
|---|---|---|
| **Constrained** (1-2 slots) | 2-3 starting standards | Wave 1 starting standards only. Get foundations right before expanding. |
| **Moderate** (3-4 slots) | 4-6 standards | Wave 1 starting + Wave 2 starting. Structure builds on foundations. |
| **Full** (5+ slots) | 7-10 standards | Full wave-sequenced path. Starting standards from Waves 1-3 in parallel where dependencies allow. |

**Capacity signals:**
- Constrained — team is in active delivery crunch, understaffed, or undergoing reorg
- Moderate — team has stable delivery cadence with some improvement capacity
- Full — team has deliberate improvement time, dedicated coaching support, or is in a transition phase

---

## Wave-Sequenced Onboarding

Each wave is split into **starting standards** (the entry point per sub-practice,
from the within-sub-practice dependency analysis) and **expansion standards** (the
rest, sequenced by internal dependencies). Start with starting standards. Expand to
the rest once starting standards reach Level 2+.

### Wave 1: Foundations — Know Your Customer, Know Your Numbers

**Sub-practices:** Customer & Market Insights (1), Product Economic Insights (4), Measurable Outcomes (7)

**Why first:** These three are foundation nodes — heavy outgoing dependencies, few incoming ones. Everything downstream depends on knowing who you serve, what value looks like economically, and what outcomes you're driving toward.

**Dependency debt if skipped:** Segments without customer evidence are demographics. Prioritization without economics is opinion. Strategy without measurable outcomes is a feature list.

#### Starting Standards

| Standard | What It Means |
|---|---|
| **CMI-a** | Team talks to customers regularly (2-3/month) |
| **PEI-d** | North star metric stated and explained |
| **MO-a** | Vision is falsifiable, specific to customers |

**Per-team-type entry point:**

| Team Type | Start With | Why |
|---|---|---|
| **Stream-Aligned** | CMI-a first | Customer conversations are the primary discovery activity. Everything else builds on customer evidence. |
| **Platform** | MO-a first | Platform teams need a clear vision to avoid becoming feature factories for consuming teams. Vision anchors what you build vs. what you decline. |
| **Enabling** | All three in parallel | Enabling teams need the full context picture (customer evidence, economics, outcomes) to coach effectively. Parallel start is appropriate because the enabling team isn't building — it's advising. |
| **Complicated Subsystem** | PEI-d first | Subsystem teams must justify their existence economically. The north star metric proves why encapsulating this complexity is worth the organizational cost. |

**Getting Started (Month 1-2):**
- CMI-a: One team member conducts 2-3 customer conversations per month. Notes go in a shared doc. Team reviews insights at planning.
- PEI-d: Name the north star metric. Document basic unit economics. Add leading indicators to the existing dashboard.
- MO-a: Write the vision. Define 3 KPIs with targets. Start monthly review.

**Good at 6 Months:**
- CMI-a: Regular cadence across multiple methods. Insights repository in active use. "What did we learn?" is a standing question in planning.
- PEI-d: Monthly economic review in place. Finance co-owns the model. Economics referenced in prioritization conversations.
- MO-a: KPIs reviewed monthly with documented actions. Leading indicators tracked alongside lagging. Planning conversations reference outcomes.

**Embedded (12+ Months):**
- CMI-a: Multiple signal sources monitored continuously. Research shapes the roadmap. Team has calibrated their methods.
- PEI-d: Economic model updated when assumptions change. Predicted vs. actual reviewed quarterly. Economic rationale in roadmap and strategy docs.
- MO-a: Vision revisited when context changes. KPIs connect from business goals to team-level work. Outcome data informs investment decisions.

#### Expansion Standards

Expand once starting standards are at Level 2+. Sequence by within-sub-practice dependencies.

| Standard | Depends On | What It Means |
|---|---|---|
| **CMI-b** | CMI-a | Insights stored where team can find them |
| **CMI-d** | CMI-a | Prototypes get user feedback before building |
| **CMI-c** | CMI-a | Usability testing before launch |
| **PEI-a** | PEI-d | Team knows key economic KPIs, reviews monthly |
| **PEI-b** | PEI-d | Unit economics documented |
| **PEI-c** | PEI-a | Leading indicators alongside lagging |
| **MO-b** | MO-a | KPIs have targets, reviewed monthly |
| **MO-c** | MO-a | Every build connected to an outcome |
| **MO-d** | MO-b | Leading and lagging indicators both tracked |

---

### Wave 2: Structure — Organize What You Know

**Sub-practices:** Segmentation & Personas (2), Strategy & Roadmap (8)

**Why second:** Both consume Wave 1 outputs directly. S&P turns CMI evidence into actionable segments. S&R translates MO into strategic direction. These provide the structural scaffolding that Waves 3-4 operate within.

**Dependency debt if skipped:** Journey maps without segments are generic. Prioritization without strategy optimizes locally. Delivery without direction is predictable but aimless.

#### Starting Standards

| Standard | What It Means |
|---|---|
| **SP-a** | Segments based on needs/behavior, not demographics |
| **SR-a** | Now/Next/Later outcome roadmap |

**Per-team-type entry point:**

| Team Type | Start With | Why |
|---|---|---|
| **Stream-Aligned** | SP-a first | Customer segments drive all downstream product decisions. "Who is this for?" needs a specific answer before roadmap sequencing works. |
| **Platform** | SR-a first | Platform teams need a visible roadmap to manage consuming-team expectations. Segments matter but are often role/workflow-based and simpler to define. |
| **Enabling** | Both in parallel | Enabling teams need to understand both the segment landscape (who the coached teams serve) and the strategic direction (where the coached teams are heading). |
| **Complicated Subsystem** | SR-a first | Subsystem evolution roadmap prevents ad-hoc requests from fragmenting specialist focus. Segments are typically defined by integration pattern (simpler). |

**Getting Started (Month 1-2):**
- SP-a: Identify 2-3 segments from existing research or usage data. Write a one-pager for each. Start using segment names in planning.
- SR-a: Write a one-page strategy. Organize existing plans into Now/Next/Later. Set OKRs for the current quarter.

**Good at 6 Months:**
- SP-a: Segments are a shared vocabulary. Personas reviewed and updated. "Who is this for?" gets a specific segment name in response.
- SR-a: Roadmap reviewed and updated quarterly. OKRs adjusted when data warrants it. Team can explain strategy → roadmap → OKR connection.

**Embedded (12+ Months):**
- SP-a: Per-segment metrics tracked. Segments have evolved at least once based on new data. Cross-functional teams use the same definitions.
- SR-a: Roadmap is the primary communication tool for cross-team planning. Strategy has a decision log. Teams propose strategic themes, not just execute them.

#### Expansion Standards

| Standard | Depends On | What It Means |
|---|---|---|
| **SP-b** | SP-a | Personas reviewed at least yearly |
| **SP-c** | SP-a | Team references segments when making feature decisions |
| **SR-b** | SR-a | OKRs aligned to strategic themes |
| **SR-c** | SR-a | Quarterly roadmap review |
| **SR-d** | SR-b | Team can explain the strategy → roadmap → OKR link |

---

### Wave 3: Action — Prioritize and Map

**Sub-practices:** Customer & Employee Journeys (3), Value-Based Sequencing (5)

**Why third:** CEJ needs both CMI evidence and S&P segments to be meaningful. VBS needs PEI economics, S&R strategic context, and S&P's customer lens. These are the "translate understanding into action" practices.

**Dependency debt if skipped:** Backlogs without value-based sequencing are opinion-ranked. Journey maps without segments and research are internal assumptions.

#### Starting Standards

| Standard | What It Means |
|---|---|
| **CEJ-a** | Journey maps exist for key flows and get updated |
| **VBS-a** | Team scores on value, risk, and effort before sequencing |

**Per-team-type entry point:**

| Team Type | Start With | Why |
|---|---|---|
| **Stream-Aligned** | Both in parallel | Stream-aligned teams benefit from both journey visibility and scoring discipline simultaneously. Journeys reveal pain points; scoring prioritizes them. |
| **Platform** | VBS-a first | Platform teams face competing requests from consuming teams. Scoring discipline prevents the loudest team from winning the backlog. Journey mapping follows. |
| **Enabling** | CEJ-a first | Enabling teams need to understand the journey of the teams they coach — where capability gaps create friction. Scoring applies to coaching engagement sequencing. |
| **Complicated Subsystem** | VBS-a first | Subsystem work must be justified by value/risk/effort to avoid becoming a bottomless pit of technical optimization. Journey mapping is secondary (integration journeys). |

**Getting Started (Month 1-2):**
- CEJ-a: Map one key journey. Identify top 3 pain points. Connect them to the backlog. Inventory existing shared components.
- VBS-a: Agree on 3 scoring criteria. Score the next planning cycle's candidates. Force-rank the top 10. Write value hypotheses for the top 5.

**Good at 6 Months:**
- CEJ-a: Key journeys mapped and reviewed when planning. Design system has an owner and adoption is tracked. Pain points declining for mapped journeys.
- VBS-a: Scoring is standard for all planning. Readiness checks before commitment. Trade-off rationale documented. Stakeholders ask "where does this score?" not "just do it."

**Embedded (12+ Months):**
- CEJ-a: "Where does this sit in the journey?" is the default question for new work. Journey-stage metrics on a dashboard. Design system contributed to by multiple teams.
- VBS-a: Quarterly predicted-vs-actual review. Scoring recalibrated based on patterns. Cross-product sequencing conversations happening.

#### Expansion Standards

| Standard | Depends On | What It Means |
|---|---|---|
| **CEJ-b** | CEJ-a | Pain points tagged with journey context in backlog |
| **VBS-b** | VBS-a | Each item has a value hypothesis |
| **VBS-c** | VBS-a | Backlog ranked, no ties |
| **VBS-d** | VBS-c | Readiness check before committing |
| **VBS-e** | VBS-c | Trade-offs documented when deprioritized |

**Independent standard (no prerequisites):**
- **CEJ-c** (design system in use) — can be adopted at any point. Supports UI consistency but isn't sequenced by journey mapping.

---

### Wave 4: Governance and Rhythm — Sustain the System

**Sub-practices:** Value Guardrails & Realization (6), Adaptive Delivery Plans (9), Routines for Activation (10)

**Why last:** These operationalize everything above. VGR guards the economics (needs PEI + VBS). ADP creates the delivery engine (needs VBS + S&R). RfA activates the cadence (needs ADP + S&R). Without the preceding waves, these practices exist as process without substance.

**Dependency debt if skipped:** Guardrails without economics are arbitrary thresholds. Delivery cadence without prioritization is busy work. Routines without strategic context are meetings no one values.

#### Starting Standards

| Standard | What It Means |
|---|---|
| **VGR-a** | Guardrails for CX, reliability, capacity on dashboard |
| **ADP-a** | Intake with evaluation criteria |
| **RfA-a** | Each routine has a defined purpose |

**Per-team-type entry point:**

| Team Type | Start With | Why |
|---|---|---|
| **Stream-Aligned** | VGR-a first | CX guardrails protect customer trust. Guardrail visibility enables the team to self-manage quality while maintaining delivery pace. |
| **Platform** | ADP-a first | Platform teams need intake discipline above all — without it, every consuming team's request becomes priority #1. Intake criteria create breathing room. |
| **Enabling** | RfA-a first | Enabling teams live and die by the quality of their coaching routines. Purposeful routines ensure coaching engagement has structure, not just good intentions. |
| **Complicated Subsystem** | VGR-a first | Technical integrity guardrails prevent the subsystem from degrading under delivery pressure. Without guardrails, complexity compounds silently. |

**Getting Started (Month 1-2):**
- VGR-a: Define 3-5 guardrails (CX, reliability, one capacity metric). Put them on a dashboard. Set R/I/T targets for the next quarter.
- ADP-a: Define intake criteria. Set a refinement cadence. Start a risk register (even if it's a spreadsheet with 3 rows). Deliver in defined waves.
- RfA-a: Define purpose for each existing meeting. Add a launch checklist (even a simple one). Start tracking retro action items.

**Good at 6 Months:**
- VGR-a: Kill criteria defined for new initiatives. R/I/T reviewed quarterly with documented actuals. At least one kill/pivot decision made.
- ADP-a: Intake feeds into scoring. Refinement is consistent. Velocity is stable enough to forecast. Risks caught before they hit.
- RfA-a: Routine calendar with clear ownership. Launch tiers defined and applied. Cross-functional syncs at milestones. Retro actions consistently closed.

**Embedded (12+ Months):**
- VGR-a: Teams flag their own guardrail breaches. Benefits realization is scheduled at launch planning time. R/I/T allocation proposed by teams, not just assigned.
- ADP-a: Cadence adapts to lifecycle stage. Forecasts trusted by stakeholders. Team adjusts their own process based on what's working.
- RfA-a: Team evolves routines based on what's working — adds, drops, changes cadence with documented rationale. Launch process trusted by stakeholders. Routines produce decisions, not just discussions.

#### Expansion Standards

| Standard | Depends On | What It Means |
|---|---|---|
| **VGR-b** | VGR-a | R/I/T allocation targets set and reviewed quarterly |
| **VGR-d** | VGR-a | Post-launch value hypothesis check |
| **VGR-c** | VGR-b | Kill criteria real — at least one initiative stopped |
| **ADP-b** | ADP-a | Regular refinement cadence |
| **ADP-c** | ADP-b | Wave/sprint cadence established |
| **ADP-d** | ADP-c | Risk register reviewed at checkpoints |
| **RfA-b** | RfA-a | Launch checklist with tiers |
| **RfA-c** | RfA-a | Cross-functional milestone syncs |

**Independent standard (no prerequisites):**
- **ADP-e** (sustainable pace monitoring) — internal health metric, not dependent on delivery machinery. Can be adopted at any point.

---

## Stall Signals

Signs that adoption is stalling, organized by horizon. If you see these, diagnose
before pushing forward — the root cause is almost always a gap in an earlier wave.

### Month 1-2 Stall Signals

| Signal | Likely Root Cause | Action |
|---|---|---|
| Starting standards aren't reaching Level 2 | Capacity overcommitted. Too many standards attempted at once. | Reduce to 1-2 starting standards. Focus on Wave 1 only. |
| "We don't have time for this" | Improvement work isn't protected from BAU pressure | Set explicit improvement capacity (even 10% of sprint). Make it visible in planning. |
| Artifacts created but not referenced | Artifacts are homework, not tools | Embed artifact use into existing rituals (stand-ups, planning, retros). |

### 6-Month Stall Signals

| Signal | Likely Root Cause | Action |
|---|---|---|
| Feedback loops not activating (insights don't reach decisions) | Wave 1 foundations are shallow. Insights exist but aren't trusted or accessible. | Strengthen Wave 1 before expanding. Focus on CMI-b (insights stored where team can find them). |
| Scoring exists but stakeholders still override | VBS isn't connected to S&R (strategy). Scoring criteria don't reflect strategic priorities. | Revisit VBS-a scoring criteria against SR-a strategic themes. Align scoring weights to strategy. |
| Routines exist but feel like overhead | RfA-a was adopted without Wave 1-3 substance. Meetings exist but lack data and decisions to process. | Pause Wave 4 expansion. Ensure Waves 1-3 are producing the inputs that routines should process. |
| Segments defined but nobody uses them | SP-a was adopted without CMI-a evidence. Segments are logical categories, not evidence-based. | Strengthen CMI-a. Run research specifically to validate or revise segments. |

### 12-Month Stall Signals

| Signal | Likely Root Cause | Action |
|---|---|---|
| Teams not self-governing (still waiting to be told) | Practices are compliance-driven, not value-driven. Team doesn't see the benefit. | Share outcome data. Show how practices connect to results the team cares about. |
| Practices adopted but not spreading to adjacent teams | No cross-team visibility. Each team operates in isolation. | Establish cross-team showcases. Use enabling team interactions to share what's working. |
| Data loops not closing (no predicted vs. actual review) | VGR-d and VBS quarterly reviews not happening. Feedback mechanisms exist but aren't activated. | Schedule the retrospective. Make it a standing calendar event with a specific artifact to review. |

---

## System-Level Embedded State

When all 10 sub-practices are embedded, the system exhibits these properties.
This is the target state — not something that happens on a fixed timeline, but the
observable outcome of sustained adoption across all four waves.

**Feedback loops close across waves:**
- Research (CMI) shapes segments (S&P), which shape journeys (CEJ), which inform prioritization (VBS), which drive guardrails (VGR), which get operationalized through routines (RfA)
- Vision (MO) anchors strategy (S&R), which provides context for sequencing (VBS), which shows whether outcomes are achievable
- Economics (PEI) define guardrails (VGR); guardrails signal when delivery (ADP) needs to shift; delivery tracks economic outcomes back to PEI

**Teams self-govern their practices:**
- 7 of 10 sub-practices explicitly describe self-governance at the embedded tier
- Teams calibrate methods (CMI), flag their own breaches (VGR), adjust their own process (ADP), and evolve routines with documented rationale (RfA)
- Practices are "how we work," not "a thing we do"

**Practices spread beyond the originating team:**
- Cross-functional teams use the same segment definitions (S&P)
- Cross-product sequencing conversations happen (VBS)
- Other teams adopt the roadmap as a communication tool (S&R)
- Design system contributed to by multiple teams (CEJ)

**Data informs upstream decisions:**
- Research shapes the roadmap (CMI → S&R)
- Outcome data informs investment decisions (MO → VBS)
- Predicted vs. actual reviewed quarterly (VBS, VGR)
- Economic model evolves when assumptions change (PEI)

---

## Quick Reference: Per Sub-Practice Adoption Path

| Sub-Practice | Wave | Starting Standard | Month 1-2 | 6 Months | Embedded |
|---|---|---|---|---|---|
| **1. CMI** | 1 | CMI-a (regular conversations) | 2-3 conversations/month, notes in shared doc | Multiple methods active, shaping plans | Calibrated, research shapes roadmap |
| **2. S&P** | 2 | SP-a (behavior-based segments) | 2-3 segments identified from evidence | Shared vocabulary, actively referenced | Evolved based on data, cross-team |
| **3. CEJ** | 3 | CEJ-a (journey maps for key flows) | One journey mapped, top 3 pain points | Regularly reviewed, design system tracked | Question-default for all work |
| **4. PEI** | 1 | PEI-d (north star metric) | North star + unit economics named | Monthly review, finance co-owns | Model evolves, quarterly retrospectives |
| **5. VBS** | 3 | VBS-a (score on value/risk/effort) | 3 criteria, top 10 scored | Scoring standard, readiness checks | Cross-product, recalibrated quarterly |
| **6. VGR** | 4 | VGR-a (guardrails on dashboard) | 3-5 guardrails on dashboard, R/I/T targets | Kill criteria defined, at least 1 used | Teams self-flag, benefits tracked |
| **7. MO** | 1 | MO-a (falsifiable vision) | Vision written, 3 KPIs set | Monthly reviews with actions | Vision evolves, KPIs cascade to teams |
| **8. S&R** | 2 | SR-a (outcome roadmap) | One-page strategy, Now/Next/Later drafted | Quarterly reviews, OKR → strategy link | Decision log, teams propose themes |
| **9. ADP** | 4 | ADP-a (intake with eval criteria) | Intake criteria, refinement cadence, risk register | Consistent, velocity forecasted | Lifecycle-aware, team-adjusted |
| **10. RfA** | 4 | RfA-a (purposeful routines) | Meeting purposes defined, launch checklist | Ownership clear, cross-functional syncs | Evolved by teams, produces decisions |

For full adoption path details per sub-practice, see the "Adoption Path" section within each sub-practice in `product-standards.md`.

---

## Cross-References

| Document | What It Provides | When to Use |
|---|---|---|
| `product-standards.md` | Full rubrics, standards detail, per-sub-practice adoption paths | Deep dive into any specific sub-practice |
| `product-standards-applicability.md` | Target maturity by lifecycle stage and product type, "Find Your Row" lookup | Determining target levels for your team |
| `product-standards-dependencies-adoption.md` | 4-wave adoption sequence, cross-pillar dependencies | Understanding why the wave order matters |
| `product-standards-dependencies-reference.md` | Within-sub-practice dependencies, starting standards, independent standards | Sequencing standards within a sub-practice |
| `templates/SCORECARD-TEMPLATE.md` | Assessment template | Step 1: knowing where you are |
