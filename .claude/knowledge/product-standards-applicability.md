# Product Standards: Applicability Matrix

Target maturity levels for each Level 3 standard, organized by lifecycle stage and
product type. Use this to answer: "Given where my product is today, which standards
should I prioritize?"

Built from the Applicability (Dimension 6) sections of each sub-practice in
`knowledge/product-standards.md`. Standard inventory from
`knowledge/product-standards-dependencies-reference.md`.

**Companion files:**
- `product-standards-applicability-lifecycle.md` — Mermaid diagrams per lifecycle stage (expected vs. stretch)
- `product-standards-applicability-pillar.md` — Mermaid diagrams per pillar (lifecycle progression)

---

## How to Read This Matrix

**Target maturity levels** represent what a well-functioning product team should aim
for at each lifecycle stage. They are guidance, not compliance floors. A team at
Growth stage doesn't fail if one standard is at Level 2 — the matrix tells them
where to focus improvement energy.

**Derivation method:** Each target was derived from the qualitative Applicability
description in `product-standards.md`, cross-validated against:
1. The maturity rubric's observable behaviors at that level
2. The adoption wave sequence from `product-standards-dependencies-adoption.md`
3. Logical consistency (foundation standards reach target before governance standards)

**Level scale:**
| Level | Meaning | Harvey Ball |
|-------|---------|-------------|
| 1 | Emerging — not yet applicable or just starting | ○ |
| 2 | Developing — building toward the practice | ◔ |
| 3 | Established — standard is fully in place | ◑ |
| 4 | Advanced — optimizing and extending | ◕ |
| 5 | Leading — teaching others, evolving the practice | ● |

**Sunset note:** Some standards show a lower target at Sunset. This is intentional —
reduced scope is appropriate, not a gap. The standard shifts focus (e.g., from
"growth metrics" to "transition metrics"), and Level 2-3 reflects that narrower
application.

---

## Find Your Row

Pick your lifecycle stage (row) and product type (column). Cell = your 4-5
highest-priority standards to focus on first.

| | Customer-Facing | Internal Platform | Regulatory |
|---|---|---|---|
| **Concept** | CMI-a, CMI-d, MO-a, VBS-b, PEI-d | CMI-a, MO-a, PEI-d, VBS-b | CMI-a, MO-a, VGR-c, PEI-d |
| **Launch** | CMI-c, VBS-d, ADP-c, RfA-b, VGR-a | ADP-c, RfA-b, VGR-a, CMI-c | VGR-a, RfA-b, ADP-c, CMI-c, VBS-d |
| **Growth** | PEI-a, VBS-a, SR-a, CEJ-a, VGR-b | PEI-a, ADP-a, SR-a, VGR-b | VGR-a, PEI-a, ADP-d, SR-b |
| **Maturity** | VGR-a, SP-a, CEJ-a, MO-b, PEI-a | ADP-d, VGR-a, PEI-a, RfA-a | VGR-a, VGR-c, ADP-d, MO-b |
| **Sunset** | CEJ-a, MO-a, RfA-c, SR-a, ADP-d | ADP-d, RfA-c, SR-a | VGR-a, RfA-c, ADP-d, SR-a |

These are your starting points. For the full target maturity matrix, see the
Standard-Level sections below. For dependency sequencing (what to do first within
a sub-practice), see `product-standards-dependencies-reference.md`.

---

## Sub-Practice Applicability Overview

### Lifecycle Stage Matrix

Qualitative summary of what each sub-practice looks like at each lifecycle stage.
For detailed standard-level targets, see the next section.

| Sub-Practice | Concept | Launch | Growth | Maturity | Sunset |
|---|---|---|---|---|---|
| **CMI** | Heavy discovery — primary activity. Validate problem-solution fit. | Usability testing on MVP. Rapid feedback loops. | Broaden signal sources. Monitor multiple segments. | Focus on unmet needs. Monitor satisfaction decay. | Understand migration needs. Research alternatives. |
| **S&P** | Define initial segments. Personas are hypotheses. | Validate segments against early adopters. | Segments become strategic. Track per-segment metrics. | Look for emerging segments. Retire segments that no longer differ. | Segment-specific migration needs. |
| **CEJ** | Map current journey to find opportunities. Future-state is hypothesis. | Validate journey assumptions with real usage. | Extend to secondary flows. Design system critical. | Journey optimization. Design system governance. | Map the transition journey. Off-ramp experience. |
| **PEI** | Economic model is hypothesis. Viable unit economics story. | Validate early signals. Track trend, not absolutes. | Unit economics improving. Leading indicators calibrated. | Optimization. Model stable and trusted. | Cost of maintenance vs. migration. Transition economics. |
| **VBS** | Sequence by learning value, not delivery value. | Fast feedback. Readiness checks critical. | Full scoring framework. Cost of delay relevant. | Weight risk reduction and tech debt higher. | Sequence migration and decommission tasks. |
| **VGR** | Kill criteria tight. R/I/T mostly Transform. | Kill on adoption signals. Guardrails protect quality. | Guardrails widen. R/I/T balances. Benefits realization routine. | R/I/T to Run/Improve. Guardrails well-established. | Guardrails protect transition CX. R/I/T almost all Run. |
| **MO** | Vision is primary artifact. KPIs hypothesized. | KPIs live, baselines establishing. | Full KPI suite with targets. Vision validated. | Optimization against KPIs. Vision may need refreshing. | KPIs shift to transition metrics. Vision = sunset rationale. |
| **S&R** | Roadmap mostly Later/Vision. OKRs = validation milestones. | Shifts to Now/Next. OKRs = adoption signals. | All horizons active. Balance growth with sustainability. | Weighted to Now/Next. Optimization/retention. | Transition plan. Migration/decommission milestones. |
| **ADP** | Lightweight intake. Short cycles (1-2 weeks). | Tight cadence (weekly). Aggressive intake filter. | Standard cadence (2-week/monthly). Intake feeds scoring. | Broader cadence. Lower, predictable intake. | Migration/decommission cadence. Restricted intake. |
| **RfA** | Fewer routines — discovery syncs, stakeholder alignment. | Full cadence. Launch enablement critical. | Routine calendar stabilizes. Tiers established. | Well-established, may need pruning. | Transition-focused: migration, communication, decommission. |

### Product Type Matrix

| Sub-Practice | Customer-Facing | Internal Platform | Regulatory |
|---|---|---|---|
| **CMI** | Full discovery: interviews, usability, analytics, support signals. | Internal users are still customers. Shadow sessions, support channel monitoring. | Compliance stakeholders as signal source. Regulatory change monitoring. |
| **S&P** | Full segmentation. Behavioral data and research drive segments. | Segment by workflow or role, not org chart. | Include regulated-entity segments alongside end-user segments. |
| **CEJ** | Full journey mapping. Design system directly impacts trust. | Employee journeys. Map workflow including system handoffs. | Include compliance touchpoints (disclosures, consent, verification). |
| **PEI** | Revenue, retention, cost-to-acquire. | Productivity gain, error reduction, process time saved. | Risk avoidance, compliance cost, cost of non-compliance. |
| **VBS** | Value scoring weights customer impact. Market timing affects sequencing. | Value = productivity/reliability. Include downstream team impact. | Compliance deadlines create hard constraints. Score discretionary capacity. |
| **VGR** | CX guardrails critical — direct trust/retention impact. | Reliability guardrails — downstream teams depend on uptime. | Compliance itself is a guardrail. Non-compliance = kill trigger. |
| **MO** | Adoption, satisfaction, retention, revenue. | Platform reliability, developer productivity, downstream satisfaction. | Compliance coverage, audit readiness, time-to-compliance. |
| **S&R** | Roadmap communicates to sales, marketing, customer success. | Roadmap serves consuming teams. | Compliance deadlines create fixed roadmap items. |
| **ADP** | Cadence aligns to market timing. Risk includes competitive/market. | Cadence aligns to consuming team needs. Risk includes downstream impact. | Compliance deadlines create hard delivery constraints. Regulatory risk explicit. |
| **RfA** | Launch includes customer comms, sales enablement, marketing. | Launch focuses on consuming team readiness. | Launch must include compliance sign-off. Regulatory change monitoring routine. |

---

## Standard-Level Target Maturity by Lifecycle Stage

Target level (1-5) for each Level 3 standard at each lifecycle stage. Standards
grouped by pillar and sub-practice. Standard codes match
`product-standards-dependencies-reference.md`.

### Pillar 1: Customer-Centered Product Design

#### 1. Customer & Market Insights (CMI)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **CMI-a:** Team talks to customers regularly (2-3/month) | 3 | 3 | 4 | 3 | 2 |
| **CMI-b:** Insights stored where team can find them | 2 | 3 | 3 | 3 | 2 |
| **CMI-c:** Usability testing before launch | 1 | 3 | 3 | 3 | 2 |
| **CMI-d:** Prototypes get user feedback before building | 3 | 3 | 3 | 3 | 2 |

**Rationale:** CMI-a and CMI-d are high at Concept because discovery is the primary
activity. CMI-c is low at Concept (nothing to launch-test yet). All drop at Sunset
as scope narrows to migration research.

#### 2. Segmentation & Personas (S&P)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **SP-a:** Segments based on needs/behavior, not demographics | 2 | 3 | 3 | 4 | 2 |
| **SP-b:** Personas reviewed at least yearly | 1 | 2 | 3 | 3 | 2 |
| **SP-c:** Team references segments when making feature decisions | 2 | 3 | 3 | 3 | 2 |

**Rationale:** At Concept, segments are hypotheses (Level 2). By Launch they're
validated against real adopters. SP-a reaches Level 4 at Maturity (looking for
emerging segments, retiring stale ones). SP-b starts at Level 1 because you're
creating personas, not reviewing them.

#### 3. Customer & Employee Journeys (CEJ)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **CEJ-a:** Journey maps exist and get updated | 2 | 3 | 3 | 4 | 3 |
| **CEJ-b:** Pain points in backlog with journey context | 2 | 3 | 3 | 3 | 2 |
| **CEJ-c:** Design system in place and used | 1 | 2 | 3 | 3 | 2 |

**Rationale:** CEJ-a reaches Level 4 at Maturity (journey optimization). CEJ-a stays
at Level 3 during Sunset because mapping the transition journey is critical. CEJ-c
lags — not meaningful until Growth when multiple teams build on the design system.

### Pillar 2: Measurable Economic Value

#### 4. Product Economic Insights (PEI)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **PEI-a:** Team knows key economic KPIs, reviews monthly | 2 | 3 | 3 | 4 | 2 |
| **PEI-b:** Unit economics documented | 2 | 2 | 3 | 3 | 3 |
| **PEI-c:** Leading indicators alongside lagging | 1 | 2 | 3 | 3 | 2 |
| **PEI-d:** North star metric stated and explained | 2 | 3 | 3 | 3 | 2 |

**Rationale:** PEI-b stays at Level 2 during Launch — unit economics are "ugly but
tracked." PEI-b reaches Level 3 at Sunset because transition economics (cost of
maintenance vs. migration) need documentation. PEI-a reaches Level 4 at Maturity
(optimization against established model).

#### 5. Value-Based Sequencing (VBS)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **VBS-a:** Scores on value, risk, effort before sequencing | 2 | 3 | 3 | 3 | 2 |
| **VBS-b:** Each item has a value hypothesis | 3 | 3 | 3 | 3 | 2 |
| **VBS-c:** Backlog ranked, no ties | 2 | 3 | 3 | 3 | 2 |
| **VBS-d:** Readiness check before committing | 2 | 3 | 3 | 3 | 2 |
| **VBS-e:** Trade-offs documented when deprioritized | 2 | 3 | 3 | 3 | 2 |

**Rationale:** VBS-b is Level 3 at Concept — value hypotheses are the core activity
when sequencing assumptions to test. The rest start at Level 2 because the scoring
framework and ranking discipline formalize during Launch.

#### 6. Value Guardrails & Realization (VGR)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **VGR-a:** Guardrails for CX, reliability, capacity on dashboard | 1 | 3 | 3 | 4 | 3 |
| **VGR-b:** R/I/T allocation targets set and reviewed quarterly | 2 | 3 | 3 | 3 | 2 |
| **VGR-c:** Kill criteria real — at least one initiative stopped | 3 | 3 | 3 | 3 | 2 |
| **VGR-d:** Post-launch value hypothesis check | 1 | 2 | 3 | 3 | 2 |

**Rationale:** VGR-a is Level 1 at Concept (no product to guard yet), Level 4 at
Maturity (well-established, teams self-manage). VGR-c is Level 3 from Concept —
tight kill criteria with short time horizons are essential for concept-stage
products. VGR-d can't apply at Concept (nothing launched yet).

### Pillar 3: Enduring Lifecycle

#### 7. Measurable Outcomes (MO)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **MO-a:** Vision is falsifiable, specific to customers | 3 | 3 | 3 | 3 | 3 |
| **MO-b:** KPIs have targets, reviewed monthly | 2 | 2 | 3 | 4 | 3 |
| **MO-c:** Planning connects builds to expected outcomes | 2 | 3 | 3 | 3 | 2 |
| **MO-d:** Leading and lagging indicators tracked | 1 | 2 | 3 | 3 | 2 |

**Rationale:** MO-a is Level 3 across all stages — vision is the primary artifact
at Concept and becomes the sunset rationale. MO-b reaches Level 4 at Maturity
(optimization against established KPIs) and stays at 3 during Sunset (transition
metrics need targets too). MO-d lags because you can't track indicators before
you have baselines.

#### 8. Strategy & Roadmap (S&R)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **SR-a:** Roadmap Now/Next/Later with outcomes | 2 | 3 | 3 | 3 | 3 |
| **SR-b:** OKRs align to strategic themes | 2 | 3 | 3 | 3 | 2 |
| **SR-c:** Roadmap reviewed and updated quarterly | 2 | 3 | 3 | 3 | 3 |
| **SR-d:** Team explains work-to-strategy connection | 2 | 3 | 3 | 3 | 2 |

**Rationale:** SR-a and SR-c stay at Level 3 during Sunset because the transition
plan IS the roadmap and it needs regular review. SR-b and SR-d drop to Level 2
at Sunset because strategic alignment simplifies (the strategy is "sunset").

#### 9. Adaptive Delivery Plans (ADP)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **ADP-a:** Defined intake with evaluation criteria | 2 | 3 | 3 | 3 | 3 |
| **ADP-b:** Backlog refined regularly | 2 | 3 | 3 | 3 | 2 |
| **ADP-c:** Delivery in waves/sprints, predictable cadence | 2 | 3 | 3 | 3 | 2 |
| **ADP-d:** Risk register reviewed at checkpoints | 2 | 3 | 3 | 3 | 3 |
| **ADP-e:** Team monitors sustainable pace | 2 | 3 | 3 | 3 | 2 |

**Rationale:** ADP-a stays at Level 3 during Sunset (intake restricted to transition
work — still needs criteria). ADP-d stays at Level 3 during Sunset (data migration
and user communication risks are real). ADP-b, ADP-c, and ADP-e drop to Level 2
as scope and pace simplify.

#### 10. Routines for Activation (RfA)

| Standard | Concept | Launch | Growth | Maturity | Sunset |
|---|:---:|:---:|:---:|:---:|:---:|
| **RfA-a:** Regular routines with clear purpose | 2 | 3 | 3 | 3 | 3 |
| **RfA-b:** Launch checklist with cross-functional engagement | 1 | 3 | 3 | 3 | 2 |
| **RfA-c:** Cross-functional syncs at key milestones | 2 | 3 | 3 | 3 | 3 |

**Rationale:** RfA-a and RfA-c stay at Level 3 during Sunset because transition
routines and decommission coordination are critical. RfA-b drops to Level 2
(launch checklist shifts to a transition checklist — similar idea, narrower scope).

---

## Standard-Level Product Type Adjustments

Adjustments apply only where the product type materially changes the emphasis or
target. Blank cells = default target applies as-is.

### Pillar 1: Customer-Centered Product Design

| Standard | Customer-Facing | Internal Platform | Regulatory |
|---|---|---|---|
| **CMI-a** | Full interviews + analytics + support signals | Shadow sessions + support channel monitoring replace formal interviews | Add regulatory change monitoring as a signal source |
| **CMI-b** | — | Shared within the team is sufficient; cross-team sharing less critical | Include regulatory interpretation notes alongside user insights |
| **CMI-c** | — | Usability = workflow efficiency testing | Include compliance flow testing (disclosures, consent) |
| **CMI-d** | — | Prototypes may be wireframes or API contracts | Prototypes must include compliance touchpoints |
| **SP-a** | Behavioral data drives segments | Segment by workflow/role, not org chart | Add regulated-entity segments alongside user segments |
| **SP-b** | — | — | Review when regulations change, not just yearly |
| **SP-c** | — | — | Compliance needs may define a segment on their own |
| **CEJ-a** | — | Employee journeys; include system handoffs | Include compliance touchpoints (disclosures, consent, verification) |
| **CEJ-b** | — | Pain points may be workflow friction, not UX friction | Include compliance pain points |
| **CEJ-c** | Consistency directly impacts trust | Design system scope may be narrower | — |

### Pillar 2: Measurable Economic Value

| Standard | Customer-Facing | Internal Platform | Regulatory |
|---|---|---|---|
| **PEI-a** | Revenue, retention, cost-to-acquire | Productivity gain, error reduction, process time saved | Risk avoidance + compliance cost |
| **PEI-b** | Standard unit economics | Translate productivity to economic terms | Model cost of non-compliance |
| **PEI-c** | — | — | Leading = compliance readiness signals |
| **PEI-d** | Revenue or retention-based | Productivity or reliability-based | Compliance coverage or risk reduction-based |
| **VBS-a** | Weight customer impact heavily | Include downstream team impact | Compliance deadlines override discretionary scoring |
| **VBS-b** | — | — | — |
| **VBS-c** | Market timing may affect sequence | — | Hard compliance deadlines sit outside the ranked backlog |
| **VBS-d** | — | — | Regulatory readiness is a readiness dimension |
| **VBS-e** | — | — | Compliance items can't be traded off; document discretionary trade-offs only |
| **VGR-a** | CX guardrails = trust/retention | Reliability guardrails = upstream dependency | Compliance itself is a guardrail; non-compliance = kill trigger |
| **VGR-b** | — | — | R/I/T may be constrained by compliance-mandated Run |
| **VGR-c** | — | — | Non-compliance triggers are pre-defined kill criteria |
| **VGR-d** | Revenue/market share validation | Productivity/error reduction validation | Risk avoidance + cost of compliance validation |

### Pillar 3: Enduring Lifecycle

| Standard | Customer-Facing | Internal Platform | Regulatory |
|---|---|---|---|
| **MO-a** | Adoption, satisfaction, revenue outcomes | Reliability, developer experience, downstream satisfaction | Compliance coverage, audit readiness |
| **MO-b** | Market metrics (retention, NPS) | Platform health metrics | Compliance metrics (coverage, readiness) |
| **MO-c** | — | — | Include regulatory outcomes alongside product outcomes |
| **MO-d** | — | — | Leading = regulatory readiness; lagging = audit results |
| **SR-a** | Communicates to sales, marketing, CS | Serves consuming teams | Fixed compliance items alongside discretionary roadmap |
| **SR-b** | Market-oriented OKRs | Platform reliability/experience OKRs | Include regulatory readiness OKRs |
| **SR-c** | — | — | — |
| **SR-d** | — | — | Include compliance strategy alongside product strategy |
| **ADP-a** | — | Cadence aligns to consuming team needs | — |
| **ADP-b** | — | — | — |
| **ADP-c** | Align to market timing | Align to consuming team release cadence | Compliance deadlines = hard delivery constraints |
| **ADP-d** | Include competitive/market risks | Include downstream impact assessment | Must include regulatory risk explicitly |
| **ADP-e** | — | — | — |
| **RfA-a** | — | — | Include regulatory change monitoring routine |
| **RfA-b** | Include customer comms, sales enablement, marketing | Focus on consuming team readiness | Must include compliance sign-off |
| **RfA-c** | — | — | — |

---

## Applicability Heatmap

Three Mermaid diagrams showing target maturity per standard across lifecycle stages.
Node fill intensity encodes target level. Read left-to-right as the product
progresses through its lifecycle.

### Pillar 1: Customer-Centered Product Design

```mermaid
graph LR
    subgraph Concept
        CMI_a_C["CMI-a<br/>◑ 3"]:::t3
        CMI_b_C["CMI-b<br/>◔ 2"]:::t2
        CMI_c_C["CMI-c<br/>○ 1"]:::t1
        CMI_d_C["CMI-d<br/>◑ 3"]:::t3
        SP_a_C["SP-a<br/>◔ 2"]:::t2
        SP_b_C["SP-b<br/>○ 1"]:::t1
        SP_c_C["SP-c<br/>◔ 2"]:::t2
        CEJ_a_C["CEJ-a<br/>◔ 2"]:::t2
        CEJ_b_C["CEJ-b<br/>◔ 2"]:::t2
        CEJ_c_C["CEJ-c<br/>○ 1"]:::t1
    end

    subgraph Launch
        CMI_a_L["CMI-a<br/>◑ 3"]:::t3
        CMI_b_L["CMI-b<br/>◑ 3"]:::t3
        CMI_c_L["CMI-c<br/>◑ 3"]:::t3
        CMI_d_L["CMI-d<br/>◑ 3"]:::t3
        SP_a_L["SP-a<br/>◑ 3"]:::t3
        SP_b_L["SP-b<br/>◔ 2"]:::t2
        SP_c_L["SP-c<br/>◑ 3"]:::t3
        CEJ_a_L["CEJ-a<br/>◑ 3"]:::t3
        CEJ_b_L["CEJ-b<br/>◑ 3"]:::t3
        CEJ_c_L["CEJ-c<br/>◔ 2"]:::t2
    end

    subgraph Growth
        CMI_a_G["CMI-a<br/>◕ 4"]:::t4
        CMI_b_G["CMI-b<br/>◑ 3"]:::t3
        CMI_c_G["CMI-c<br/>◑ 3"]:::t3
        CMI_d_G["CMI-d<br/>◑ 3"]:::t3
        SP_a_G["SP-a<br/>◑ 3"]:::t3
        SP_b_G["SP-b<br/>◑ 3"]:::t3
        SP_c_G["SP-c<br/>◑ 3"]:::t3
        CEJ_a_G["CEJ-a<br/>◑ 3"]:::t3
        CEJ_b_G["CEJ-b<br/>◑ 3"]:::t3
        CEJ_c_G["CEJ-c<br/>◑ 3"]:::t3
    end

    subgraph Maturity
        CMI_a_M["CMI-a<br/>◑ 3"]:::t3
        CMI_b_M["CMI-b<br/>◑ 3"]:::t3
        CMI_c_M["CMI-c<br/>◑ 3"]:::t3
        CMI_d_M["CMI-d<br/>◑ 3"]:::t3
        SP_a_M["SP-a<br/>◕ 4"]:::t4
        SP_b_M["SP-b<br/>◑ 3"]:::t3
        SP_c_M["SP-c<br/>◑ 3"]:::t3
        CEJ_a_M["CEJ-a<br/>◕ 4"]:::t4
        CEJ_b_M["CEJ-b<br/>◑ 3"]:::t3
        CEJ_c_M["CEJ-c<br/>◑ 3"]:::t3
    end

    subgraph Sunset
        CMI_a_S["CMI-a<br/>◔ 2"]:::t2
        CMI_b_S["CMI-b<br/>◔ 2"]:::t2
        CMI_c_S["CMI-c<br/>◔ 2"]:::t2
        CMI_d_S["CMI-d<br/>◔ 2"]:::t2
        SP_a_S["SP-a<br/>◔ 2"]:::t2
        SP_b_S["SP-b<br/>◔ 2"]:::t2
        SP_c_S["SP-c<br/>◔ 2"]:::t2
        CEJ_a_S["CEJ-a<br/>◑ 3"]:::t3
        CEJ_b_S["CEJ-b<br/>◔ 2"]:::t2
        CEJ_c_S["CEJ-c<br/>◔ 2"]:::t2
    end

    CMI_a_C --> CMI_a_L --> CMI_a_G --> CMI_a_M --> CMI_a_S
    CMI_b_C --> CMI_b_L --> CMI_b_G --> CMI_b_M --> CMI_b_S
    CMI_c_C --> CMI_c_L --> CMI_c_G --> CMI_c_M --> CMI_c_S
    CMI_d_C --> CMI_d_L --> CMI_d_G --> CMI_d_M --> CMI_d_S
    SP_a_C --> SP_a_L --> SP_a_G --> SP_a_M --> SP_a_S
    SP_b_C --> SP_b_L --> SP_b_G --> SP_b_M --> SP_b_S
    SP_c_C --> SP_c_L --> SP_c_G --> SP_c_M --> SP_c_S
    CEJ_a_C --> CEJ_a_L --> CEJ_a_G --> CEJ_a_M --> CEJ_a_S
    CEJ_b_C --> CEJ_b_L --> CEJ_b_G --> CEJ_b_M --> CEJ_b_S
    CEJ_c_C --> CEJ_c_L --> CEJ_c_G --> CEJ_c_M --> CEJ_c_S

    classDef t1 fill:#e8e8e8,color:#666,stroke:#999
    classDef t2 fill:#c4d9f0,color:#333,stroke:#7ba3cc
    classDef t3 fill:#6ba3d6,color:#fff,stroke:#4a7fb5
    classDef t4 fill:#2d6da4,color:#fff,stroke:#1e4f7a
    classDef t5 fill:#1a3d5c,color:#fff,stroke:#0f2940
```

### Pillar 2: Measurable Economic Value

```mermaid
graph LR
    subgraph Concept
        PEI_a_C["PEI-a<br/>◔ 2"]:::t2
        PEI_b_C["PEI-b<br/>◔ 2"]:::t2
        PEI_c_C["PEI-c<br/>○ 1"]:::t1
        PEI_d_C["PEI-d<br/>◔ 2"]:::t2
        VBS_a_C["VBS-a<br/>◔ 2"]:::t2
        VBS_b_C["VBS-b<br/>◑ 3"]:::t3
        VBS_c_C["VBS-c<br/>◔ 2"]:::t2
        VBS_d_C["VBS-d<br/>◔ 2"]:::t2
        VBS_e_C["VBS-e<br/>◔ 2"]:::t2
        VGR_a_C["VGR-a<br/>○ 1"]:::t1
        VGR_b_C["VGR-b<br/>◔ 2"]:::t2
        VGR_c_C["VGR-c<br/>◑ 3"]:::t3
        VGR_d_C["VGR-d<br/>○ 1"]:::t1
    end

    subgraph Launch
        PEI_a_L["PEI-a<br/>◑ 3"]:::t3
        PEI_b_L["PEI-b<br/>◔ 2"]:::t2
        PEI_c_L["PEI-c<br/>◔ 2"]:::t2
        PEI_d_L["PEI-d<br/>◑ 3"]:::t3
        VBS_a_L["VBS-a<br/>◑ 3"]:::t3
        VBS_b_L["VBS-b<br/>◑ 3"]:::t3
        VBS_c_L["VBS-c<br/>◑ 3"]:::t3
        VBS_d_L["VBS-d<br/>◑ 3"]:::t3
        VBS_e_L["VBS-e<br/>◑ 3"]:::t3
        VGR_a_L["VGR-a<br/>◑ 3"]:::t3
        VGR_b_L["VGR-b<br/>◑ 3"]:::t3
        VGR_c_L["VGR-c<br/>◑ 3"]:::t3
        VGR_d_L["VGR-d<br/>◔ 2"]:::t2
    end

    subgraph Growth
        PEI_a_G["PEI-a<br/>◑ 3"]:::t3
        PEI_b_G["PEI-b<br/>◑ 3"]:::t3
        PEI_c_G["PEI-c<br/>◑ 3"]:::t3
        PEI_d_G["PEI-d<br/>◑ 3"]:::t3
        VBS_a_G["VBS-a<br/>◑ 3"]:::t3
        VBS_b_G["VBS-b<br/>◑ 3"]:::t3
        VBS_c_G["VBS-c<br/>◑ 3"]:::t3
        VBS_d_G["VBS-d<br/>◑ 3"]:::t3
        VBS_e_G["VBS-e<br/>◑ 3"]:::t3
        VGR_a_G["VGR-a<br/>◑ 3"]:::t3
        VGR_b_G["VGR-b<br/>◑ 3"]:::t3
        VGR_c_G["VGR-c<br/>◑ 3"]:::t3
        VGR_d_G["VGR-d<br/>◑ 3"]:::t3
    end

    subgraph Maturity
        PEI_a_M["PEI-a<br/>◕ 4"]:::t4
        PEI_b_M["PEI-b<br/>◑ 3"]:::t3
        PEI_c_M["PEI-c<br/>◑ 3"]:::t3
        PEI_d_M["PEI-d<br/>◑ 3"]:::t3
        VBS_a_M["VBS-a<br/>◑ 3"]:::t3
        VBS_b_M["VBS-b<br/>◑ 3"]:::t3
        VBS_c_M["VBS-c<br/>◑ 3"]:::t3
        VBS_d_M["VBS-d<br/>◑ 3"]:::t3
        VBS_e_M["VBS-e<br/>◑ 3"]:::t3
        VGR_a_M["VGR-a<br/>◕ 4"]:::t4
        VGR_b_M["VGR-b<br/>◑ 3"]:::t3
        VGR_c_M["VGR-c<br/>◑ 3"]:::t3
        VGR_d_M["VGR-d<br/>◑ 3"]:::t3
    end

    subgraph Sunset
        PEI_a_S["PEI-a<br/>◔ 2"]:::t2
        PEI_b_S["PEI-b<br/>◑ 3"]:::t3
        PEI_c_S["PEI-c<br/>◔ 2"]:::t2
        PEI_d_S["PEI-d<br/>◔ 2"]:::t2
        VBS_a_S["VBS-a<br/>◔ 2"]:::t2
        VBS_b_S["VBS-b<br/>◔ 2"]:::t2
        VBS_c_S["VBS-c<br/>◔ 2"]:::t2
        VBS_d_S["VBS-d<br/>◔ 2"]:::t2
        VBS_e_S["VBS-e<br/>◔ 2"]:::t2
        VGR_a_S["VGR-a<br/>◑ 3"]:::t3
        VGR_b_S["VGR-b<br/>◔ 2"]:::t2
        VGR_c_S["VGR-c<br/>◔ 2"]:::t2
        VGR_d_S["VGR-d<br/>◔ 2"]:::t2
    end

    PEI_a_C --> PEI_a_L --> PEI_a_G --> PEI_a_M --> PEI_a_S
    PEI_b_C --> PEI_b_L --> PEI_b_G --> PEI_b_M --> PEI_b_S
    PEI_c_C --> PEI_c_L --> PEI_c_G --> PEI_c_M --> PEI_c_S
    PEI_d_C --> PEI_d_L --> PEI_d_G --> PEI_d_M --> PEI_d_S
    VBS_a_C --> VBS_a_L --> VBS_a_G --> VBS_a_M --> VBS_a_S
    VBS_b_C --> VBS_b_L --> VBS_b_G --> VBS_b_M --> VBS_b_S
    VBS_c_C --> VBS_c_L --> VBS_c_G --> VBS_c_M --> VBS_c_S
    VBS_d_C --> VBS_d_L --> VBS_d_G --> VBS_d_M --> VBS_d_S
    VBS_e_C --> VBS_e_L --> VBS_e_G --> VBS_e_M --> VBS_e_S
    VGR_a_C --> VGR_a_L --> VGR_a_G --> VGR_a_M --> VGR_a_S
    VGR_b_C --> VGR_b_L --> VGR_b_G --> VGR_b_M --> VGR_b_S
    VGR_c_C --> VGR_c_L --> VGR_c_G --> VGR_c_M --> VGR_c_S
    VGR_d_C --> VGR_d_L --> VGR_d_G --> VGR_d_M --> VGR_d_S

    classDef t1 fill:#e8e8e8,color:#666,stroke:#999
    classDef t2 fill:#c4d9f0,color:#333,stroke:#7ba3cc
    classDef t3 fill:#6ba3d6,color:#fff,stroke:#4a7fb5
    classDef t4 fill:#2d6da4,color:#fff,stroke:#1e4f7a
    classDef t5 fill:#1a3d5c,color:#fff,stroke:#0f2940
```

### Pillar 3: Enduring Lifecycle

```mermaid
graph LR
    subgraph Concept
        MO_a_C["MO-a<br/>◑ 3"]:::t3
        MO_b_C["MO-b<br/>◔ 2"]:::t2
        MO_c_C["MO-c<br/>◔ 2"]:::t2
        MO_d_C["MO-d<br/>○ 1"]:::t1
        SR_a_C["SR-a<br/>◔ 2"]:::t2
        SR_b_C["SR-b<br/>◔ 2"]:::t2
        SR_c_C["SR-c<br/>◔ 2"]:::t2
        SR_d_C["SR-d<br/>◔ 2"]:::t2
        ADP_a_C["ADP-a<br/>◔ 2"]:::t2
        ADP_b_C["ADP-b<br/>◔ 2"]:::t2
        ADP_c_C["ADP-c<br/>◔ 2"]:::t2
        ADP_d_C["ADP-d<br/>◔ 2"]:::t2
        ADP_e_C["ADP-e<br/>◔ 2"]:::t2
        RfA_a_C["RfA-a<br/>◔ 2"]:::t2
        RfA_b_C["RfA-b<br/>○ 1"]:::t1
        RfA_c_C["RfA-c<br/>◔ 2"]:::t2
    end

    subgraph Launch
        MO_a_L["MO-a<br/>◑ 3"]:::t3
        MO_b_L["MO-b<br/>◔ 2"]:::t2
        MO_c_L["MO-c<br/>◑ 3"]:::t3
        MO_d_L["MO-d<br/>◔ 2"]:::t2
        SR_a_L["SR-a<br/>◑ 3"]:::t3
        SR_b_L["SR-b<br/>◑ 3"]:::t3
        SR_c_L["SR-c<br/>◑ 3"]:::t3
        SR_d_L["SR-d<br/>◑ 3"]:::t3
        ADP_a_L["ADP-a<br/>◑ 3"]:::t3
        ADP_b_L["ADP-b<br/>◑ 3"]:::t3
        ADP_c_L["ADP-c<br/>◑ 3"]:::t3
        ADP_d_L["ADP-d<br/>◑ 3"]:::t3
        ADP_e_L["ADP-e<br/>◑ 3"]:::t3
        RfA_a_L["RfA-a<br/>◑ 3"]:::t3
        RfA_b_L["RfA-b<br/>◑ 3"]:::t3
        RfA_c_L["RfA-c<br/>◑ 3"]:::t3
    end

    subgraph Growth
        MO_a_G["MO-a<br/>◑ 3"]:::t3
        MO_b_G["MO-b<br/>◑ 3"]:::t3
        MO_c_G["MO-c<br/>◑ 3"]:::t3
        MO_d_G["MO-d<br/>◑ 3"]:::t3
        SR_a_G["SR-a<br/>◑ 3"]:::t3
        SR_b_G["SR-b<br/>◑ 3"]:::t3
        SR_c_G["SR-c<br/>◑ 3"]:::t3
        SR_d_G["SR-d<br/>◑ 3"]:::t3
        ADP_a_G["ADP-a<br/>◑ 3"]:::t3
        ADP_b_G["ADP-b<br/>◑ 3"]:::t3
        ADP_c_G["ADP-c<br/>◑ 3"]:::t3
        ADP_d_G["ADP-d<br/>◑ 3"]:::t3
        ADP_e_G["ADP-e<br/>◑ 3"]:::t3
        RfA_a_G["RfA-a<br/>◑ 3"]:::t3
        RfA_b_G["RfA-b<br/>◑ 3"]:::t3
        RfA_c_G["RfA-c<br/>◑ 3"]:::t3
    end

    subgraph Maturity
        MO_a_M["MO-a<br/>◑ 3"]:::t3
        MO_b_M["MO-b<br/>◕ 4"]:::t4
        MO_c_M["MO-c<br/>◑ 3"]:::t3
        MO_d_M["MO-d<br/>◑ 3"]:::t3
        SR_a_M["SR-a<br/>◑ 3"]:::t3
        SR_b_M["SR-b<br/>◑ 3"]:::t3
        SR_c_M["SR-c<br/>◑ 3"]:::t3
        SR_d_M["SR-d<br/>◑ 3"]:::t3
        ADP_a_M["ADP-a<br/>◑ 3"]:::t3
        ADP_b_M["ADP-b<br/>◑ 3"]:::t3
        ADP_c_M["ADP-c<br/>◑ 3"]:::t3
        ADP_d_M["ADP-d<br/>◑ 3"]:::t3
        ADP_e_M["ADP-e<br/>◑ 3"]:::t3
        RfA_a_M["RfA-a<br/>◑ 3"]:::t3
        RfA_b_M["RfA-b<br/>◑ 3"]:::t3
        RfA_c_M["RfA-c<br/>◑ 3"]:::t3
    end

    subgraph Sunset
        MO_a_S["MO-a<br/>◑ 3"]:::t3
        MO_b_S["MO-b<br/>◑ 3"]:::t3
        MO_c_S["MO-c<br/>◔ 2"]:::t2
        MO_d_S["MO-d<br/>◔ 2"]:::t2
        SR_a_S["SR-a<br/>◑ 3"]:::t3
        SR_b_S["SR-b<br/>◔ 2"]:::t2
        SR_c_S["SR-c<br/>◑ 3"]:::t3
        SR_d_S["SR-d<br/>◔ 2"]:::t2
        ADP_a_S["ADP-a<br/>◑ 3"]:::t3
        ADP_b_S["ADP-b<br/>◔ 2"]:::t2
        ADP_c_S["ADP-c<br/>◔ 2"]:::t2
        ADP_d_S["ADP-d<br/>◑ 3"]:::t3
        ADP_e_S["ADP-e<br/>◔ 2"]:::t2
        RfA_a_S["RfA-a<br/>◑ 3"]:::t3
        RfA_b_S["RfA-b<br/>◔ 2"]:::t2
        RfA_c_S["RfA-c<br/>◑ 3"]:::t3
    end

    MO_a_C --> MO_a_L --> MO_a_G --> MO_a_M --> MO_a_S
    MO_b_C --> MO_b_L --> MO_b_G --> MO_b_M --> MO_b_S
    MO_c_C --> MO_c_L --> MO_c_G --> MO_c_M --> MO_c_S
    MO_d_C --> MO_d_L --> MO_d_G --> MO_d_M --> MO_d_S
    SR_a_C --> SR_a_L --> SR_a_G --> SR_a_M --> SR_a_S
    SR_b_C --> SR_b_L --> SR_b_G --> SR_b_M --> SR_b_S
    SR_c_C --> SR_c_L --> SR_c_G --> SR_c_M --> SR_c_S
    SR_d_C --> SR_d_L --> SR_d_G --> SR_d_M --> SR_d_S
    ADP_a_C --> ADP_a_L --> ADP_a_G --> ADP_a_M --> ADP_a_S
    ADP_b_C --> ADP_b_L --> ADP_b_G --> ADP_b_M --> ADP_b_S
    ADP_c_C --> ADP_c_L --> ADP_c_G --> ADP_c_M --> ADP_c_S
    ADP_d_C --> ADP_d_L --> ADP_d_G --> ADP_d_M --> ADP_d_S
    ADP_e_C --> ADP_e_L --> ADP_e_G --> ADP_e_M --> ADP_e_S
    RfA_a_C --> RfA_a_L --> RfA_a_G --> RfA_a_M --> RfA_a_S
    RfA_b_C --> RfA_b_L --> RfA_b_G --> RfA_b_M --> RfA_b_S
    RfA_c_C --> RfA_c_L --> RfA_c_G --> RfA_c_M --> RfA_c_S

    classDef t1 fill:#e8e8e8,color:#666,stroke:#999
    classDef t2 fill:#c4d9f0,color:#333,stroke:#7ba3cc
    classDef t3 fill:#6ba3d6,color:#fff,stroke:#4a7fb5
    classDef t4 fill:#2d6da4,color:#fff,stroke:#1e4f7a
    classDef t5 fill:#1a3d5c,color:#fff,stroke:#0f2940
```

---

## Legend

| Symbol | Target Level | Meaning |
|--------|-------------|---------|
| ○ | 1 — Emerging | Not yet applicable or just starting at this stage |
| ◔ | 2 — Developing | Building toward the practice; hypothesis or lightweight |
| ◑ | 3 — Established | Standard fully in place for this lifecycle stage |
| ◕ | 4 — Advanced | Optimizing and extending the practice |
| ● | 5 — Leading | Teaching others, evolving the practice |

**Fill intensity in Mermaid diagrams:**

| Fill | Level | Visual |
|------|-------|--------|
| Light grey | 1 | Lowest intensity — not yet applicable |
| Light blue | 2 | Developing — building toward |
| Medium blue | 3 | Established — target for most standards at most stages |
| Dark blue | 4 | Advanced — optimization stage |
| Very dark blue | 5 | Leading — not a typical target per lifecycle stage |

**Reading the heatmap:** Each row is one standard flowing left-to-right through
lifecycle stages. Darker nodes = higher target maturity. Most standards follow an
arc: light at Concept, medium (Level 3) through Growth/Maturity, then lighter at
Sunset. Standards that peak at Level 4 are marked as optimization opportunities
at Maturity.
