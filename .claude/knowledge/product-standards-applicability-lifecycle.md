# Product Standards: Applicability — Lifecycle View

Five Mermaid diagrams showing which Level 3 standards are **expected** (target ≥ 3)
vs. **stretch** (target < 3) at each lifecycle stage. Use this to quickly see what
a team at a given stage should have in place.

Companion to `product-standards-applicability.md` (full matrices and lookup table).
Standard inventory from `product-standards-dependencies-reference.md`.

---

## How to Read These Diagrams

- **Solid fill** = Expected at this stage (target maturity ≥ 3)
- **Dashed border** = Stretch at this stage (target maturity < 3, building toward it)
- Standards grouped by pillar: Blue (Pillar 1), Gold (Pillar 2), Green (Pillar 3)
- Target level shown in each node for precision
- Count at the top of each diagram: how many standards are expected vs. stretch

---

## Concept Stage

At Concept, the team is validating assumptions. Discovery and vision are the primary
activities. Most governance and operational standards are stretch — the team is
building toward them but doesn't need them yet.

**Expected: 5 of 39** | **Stretch: 34 of 39**

| Status | Standards |
|--------|-----------|
| Expected (≥3) | CMI-a, CMI-d, VBS-b, VGR-c, MO-a |
| Stretch (<3) | All others |

```mermaid
graph TD
    subgraph "Pillar 1: Customer-Centered Product Design"
        CMI_a["CMI-a: Talks to customers<br/>◑ 3"]:::p1_expected
        CMI_b["CMI-b: Insights stored<br/>◔ 2"]:::p1_stretch
        CMI_c["CMI-c: Usability testing<br/>○ 1"]:::p1_stretch
        CMI_d["CMI-d: Prototype feedback<br/>◑ 3"]:::p1_expected
        SP_a["SP-a: Behavioral segments<br/>◔ 2"]:::p1_stretch
        SP_b["SP-b: Persona review<br/>○ 1"]:::p1_stretch
        SP_c["SP-c: Segments in decisions<br/>◔ 2"]:::p1_stretch
        CEJ_a["CEJ-a: Journey maps<br/>◔ 2"]:::p1_stretch
        CEJ_b["CEJ-b: Pain points in backlog<br/>◔ 2"]:::p1_stretch
        CEJ_c["CEJ-c: Design system<br/>○ 1"]:::p1_stretch
    end

    subgraph "Pillar 2: Measurable Economic Value"
        PEI_a["PEI-a: Economic KPIs<br/>◔ 2"]:::p2_stretch
        PEI_b["PEI-b: Unit economics<br/>◔ 2"]:::p2_stretch
        PEI_c["PEI-c: Leading indicators<br/>○ 1"]:::p2_stretch
        PEI_d["PEI-d: North star metric<br/>◔ 2"]:::p2_stretch
        VBS_a["VBS-a: Scoring framework<br/>◔ 2"]:::p2_stretch
        VBS_b["VBS-b: Value hypothesis<br/>◑ 3"]:::p2_expected
        VBS_c["VBS-c: Ranked backlog<br/>◔ 2"]:::p2_stretch
        VBS_d["VBS-d: Readiness check<br/>◔ 2"]:::p2_stretch
        VBS_e["VBS-e: Trade-offs documented<br/>◔ 2"]:::p2_stretch
        VGR_a["VGR-a: Guardrails dashboard<br/>○ 1"]:::p2_stretch
        VGR_b["VGR-b: R/I/T allocation<br/>◔ 2"]:::p2_stretch
        VGR_c["VGR-c: Kill criteria real<br/>◑ 3"]:::p2_expected
        VGR_d["VGR-d: Value realization check<br/>○ 1"]:::p2_stretch
    end

    subgraph "Pillar 3: Enduring Lifecycle"
        MO_a["MO-a: Falsifiable vision<br/>◑ 3"]:::p3_expected
        MO_b["MO-b: KPIs with targets<br/>◔ 2"]:::p3_stretch
        MO_c["MO-c: Builds to outcomes<br/>◔ 2"]:::p3_stretch
        MO_d["MO-d: Leading + lagging<br/>○ 1"]:::p3_stretch
        SR_a["SR-a: Outcome roadmap<br/>◔ 2"]:::p3_stretch
        SR_b["SR-b: OKRs to themes<br/>◔ 2"]:::p3_stretch
        SR_c["SR-c: Quarterly review<br/>◔ 2"]:::p3_stretch
        SR_d["SR-d: Work-to-strategy<br/>◔ 2"]:::p3_stretch
        ADP_a["ADP-a: Defined intake<br/>◔ 2"]:::p3_stretch
        ADP_b["ADP-b: Regular refinement<br/>◔ 2"]:::p3_stretch
        ADP_c["ADP-c: Predictable cadence<br/>◔ 2"]:::p3_stretch
        ADP_d["ADP-d: Risk register<br/>◔ 2"]:::p3_stretch
        ADP_e["ADP-e: Sustainable pace<br/>◔ 2"]:::p3_stretch
        RfA_a["RfA-a: Purposeful routines<br/>◔ 2"]:::p3_stretch
        RfA_b["RfA-b: Launch checklist<br/>○ 1"]:::p3_stretch
        RfA_c["RfA-c: Cross-functional syncs<br/>◔ 2"]:::p3_stretch
    end

    classDef p1_expected fill:#4A90D9,color:#fff,stroke:#2E5C8A,stroke-width:2px
    classDef p1_stretch fill:#4A90D9,color:#fff,stroke:#2E5C8A,stroke-width:2px,stroke-dasharray: 5 5,opacity:0.5
    classDef p2_expected fill:#D4A843,color:#fff,stroke:#A07D2E,stroke-width:2px
    classDef p2_stretch fill:#D4A843,color:#fff,stroke:#A07D2E,stroke-width:2px,stroke-dasharray: 5 5,opacity:0.5
    classDef p3_expected fill:#5BA55B,color:#fff,stroke:#3D7A3D,stroke-width:2px
    classDef p3_stretch fill:#5BA55B,color:#fff,stroke:#3D7A3D,stroke-width:2px,stroke-dasharray: 5 5,opacity:0.5
```

---

## Launch Stage

At Launch, most standards come online. Discovery continues, delivery cadence
tightens, guardrails protect quality, and launch enablement is critical. The
remaining stretch standards are those that need data accumulation (baselines,
unit economics, leading indicators).

**Expected: 30 of 39** | **Stretch: 9 of 39**

| Status | Standards |
|--------|-----------|
| Stretch (<3) | CMI-b → 3 (just made it), SP-b, CEJ-c, PEI-b, PEI-c, VGR-d, MO-b, MO-d |
| Expected (≥3) | All others |

*Note: 30 standards reach Level 3 at Launch. The 9 stretch standards are those
requiring data accumulation or maturity that comes with time.*

```mermaid
graph TD
    subgraph "Pillar 1: Customer-Centered Product Design"
        CMI_a["CMI-a: Talks to customers<br/>◑ 3"]:::p1_expected
        CMI_b["CMI-b: Insights stored<br/>◑ 3"]:::p1_expected
        CMI_c["CMI-c: Usability testing<br/>◑ 3"]:::p1_expected
        CMI_d["CMI-d: Prototype feedback<br/>◑ 3"]:::p1_expected
        SP_a["SP-a: Behavioral segments<br/>◑ 3"]:::p1_expected
        SP_b["SP-b: Persona review<br/>◔ 2"]:::p1_stretch
        SP_c["SP-c: Segments in decisions<br/>◑ 3"]:::p1_expected
        CEJ_a["CEJ-a: Journey maps<br/>◑ 3"]:::p1_expected
        CEJ_b["CEJ-b: Pain points in backlog<br/>◑ 3"]:::p1_expected
        CEJ_c["CEJ-c: Design system<br/>◔ 2"]:::p1_stretch
    end

    subgraph "Pillar 2: Measurable Economic Value"
        PEI_a["PEI-a: Economic KPIs<br/>◑ 3"]:::p2_expected
        PEI_b["PEI-b: Unit economics<br/>◔ 2"]:::p2_stretch
        PEI_c["PEI-c: Leading indicators<br/>◔ 2"]:::p2_stretch
        PEI_d["PEI-d: North star metric<br/>◑ 3"]:::p2_expected
        VBS_a["VBS-a: Scoring framework<br/>◑ 3"]:::p2_expected
        VBS_b["VBS-b: Value hypothesis<br/>◑ 3"]:::p2_expected
        VBS_c["VBS-c: Ranked backlog<br/>◑ 3"]:::p2_expected
        VBS_d["VBS-d: Readiness check<br/>◑ 3"]:::p2_expected
        VBS_e["VBS-e: Trade-offs documented<br/>◑ 3"]:::p2_expected
        VGR_a["VGR-a: Guardrails dashboard<br/>◑ 3"]:::p2_expected
        VGR_b["VGR-b: R/I/T allocation<br/>◑ 3"]:::p2_expected
        VGR_c["VGR-c: Kill criteria real<br/>◑ 3"]:::p2_expected
        VGR_d["VGR-d: Value realization check<br/>◔ 2"]:::p2_stretch
    end

    subgraph "Pillar 3: Enduring Lifecycle"
        MO_a["MO-a: Falsifiable vision<br/>◑ 3"]:::p3_expected
        MO_b["MO-b: KPIs with targets<br/>◔ 2"]:::p3_stretch
        MO_c["MO-c: Builds to outcomes<br/>◑ 3"]:::p3_expected
        MO_d["MO-d: Leading + lagging<br/>◔ 2"]:::p3_stretch
        SR_a["SR-a: Outcome roadmap<br/>◑ 3"]:::p3_expected
        SR_b["SR-b: OKRs to themes<br/>◑ 3"]:::p3_expected
        SR_c["SR-c: Quarterly review<br/>◑ 3"]:::p3_expected
        SR_d["SR-d: Work-to-strategy<br/>◑ 3"]:::p3_expected
        ADP_a["ADP-a: Defined intake<br/>◑ 3"]:::p3_expected
        ADP_b["ADP-b: Regular refinement<br/>◑ 3"]:::p3_expected
        ADP_c["ADP-c: Predictable cadence<br/>◑ 3"]:::p3_expected
        ADP_d["ADP-d: Risk register<br/>◑ 3"]:::p3_expected
        ADP_e["ADP-e: Sustainable pace<br/>◑ 3"]:::p3_expected
        RfA_a["RfA-a: Purposeful routines<br/>◑ 3"]:::p3_expected
        RfA_b["RfA-b: Launch checklist<br/>◑ 3"]:::p3_expected
        RfA_c["RfA-c: Cross-functional syncs<br/>◑ 3"]:::p3_expected
    end

    classDef p1_expected fill:#4A90D9,color:#fff,stroke:#2E5C8A,stroke-width:2px
    classDef p1_stretch fill:#4A90D9,color:#fff,stroke:#2E5C8A,stroke-width:2px,stroke-dasharray: 5 5,opacity:0.5
    classDef p2_expected fill:#D4A843,color:#fff,stroke:#A07D2E,stroke-width:2px
    classDef p2_stretch fill:#D4A843,color:#fff,stroke:#A07D2E,stroke-width:2px,stroke-dasharray: 5 5,opacity:0.5
    classDef p3_expected fill:#5BA55B,color:#fff,stroke:#3D7A3D,stroke-width:2px
    classDef p3_stretch fill:#5BA55B,color:#fff,stroke:#3D7A3D,stroke-width:2px,stroke-dasharray: 5 5,opacity:0.5
```

---

## Growth Stage

At Growth, all 39 standards should be at Level 3 or higher. This is the "full
practice" stage — every sub-practice is operational. The team's focus shifts from
establishing practices to broadening and calibrating them.

**Expected: 39 of 39** | **Stretch: 0 of 39**

```mermaid
graph TD
    subgraph "Pillar 1: Customer-Centered Product Design"
        CMI_a["CMI-a: Talks to customers<br/>◕ 4"]:::p1_advanced
        CMI_b["CMI-b: Insights stored<br/>◑ 3"]:::p1_expected
        CMI_c["CMI-c: Usability testing<br/>◑ 3"]:::p1_expected
        CMI_d["CMI-d: Prototype feedback<br/>◑ 3"]:::p1_expected
        SP_a["SP-a: Behavioral segments<br/>◑ 3"]:::p1_expected
        SP_b["SP-b: Persona review<br/>◑ 3"]:::p1_expected
        SP_c["SP-c: Segments in decisions<br/>◑ 3"]:::p1_expected
        CEJ_a["CEJ-a: Journey maps<br/>◑ 3"]:::p1_expected
        CEJ_b["CEJ-b: Pain points in backlog<br/>◑ 3"]:::p1_expected
        CEJ_c["CEJ-c: Design system<br/>◑ 3"]:::p1_expected
    end

    subgraph "Pillar 2: Measurable Economic Value"
        PEI_a["PEI-a: Economic KPIs<br/>◑ 3"]:::p2_expected
        PEI_b["PEI-b: Unit economics<br/>◑ 3"]:::p2_expected
        PEI_c["PEI-c: Leading indicators<br/>◑ 3"]:::p2_expected
        PEI_d["PEI-d: North star metric<br/>◑ 3"]:::p2_expected
        VBS_a["VBS-a: Scoring framework<br/>◑ 3"]:::p2_expected
        VBS_b["VBS-b: Value hypothesis<br/>◑ 3"]:::p2_expected
        VBS_c["VBS-c: Ranked backlog<br/>◑ 3"]:::p2_expected
        VBS_d["VBS-d: Readiness check<br/>◑ 3"]:::p2_expected
        VBS_e["VBS-e: Trade-offs documented<br/>◑ 3"]:::p2_expected
        VGR_a["VGR-a: Guardrails dashboard<br/>◑ 3"]:::p2_expected
        VGR_b["VGR-b: R/I/T allocation<br/>◑ 3"]:::p2_expected
        VGR_c["VGR-c: Kill criteria real<br/>◑ 3"]:::p2_expected
        VGR_d["VGR-d: Value realization check<br/>◑ 3"]:::p2_expected
    end

    subgraph "Pillar 3: Enduring Lifecycle"
        MO_a["MO-a: Falsifiable vision<br/>◑ 3"]:::p3_expected
        MO_b["MO-b: KPIs with targets<br/>◑ 3"]:::p3_expected
        MO_c["MO-c: Builds to outcomes<br/>◑ 3"]:::p3_expected
        MO_d["MO-d: Leading + lagging<br/>◑ 3"]:::p3_expected
        SR_a["SR-a: Outcome roadmap<br/>◑ 3"]:::p3_expected
        SR_b["SR-b: OKRs to themes<br/>◑ 3"]:::p3_expected
        SR_c["SR-c: Quarterly review<br/>◑ 3"]:::p3_expected
        SR_d["SR-d: Work-to-strategy<br/>◑ 3"]:::p3_expected
        ADP_a["ADP-a: Defined intake<br/>◑ 3"]:::p3_expected
        ADP_b["ADP-b: Regular refinement<br/>◑ 3"]:::p3_expected
        ADP_c["ADP-c: Predictable cadence<br/>◑ 3"]:::p3_expected
        ADP_d["ADP-d: Risk register<br/>◑ 3"]:::p3_expected
        ADP_e["ADP-e: Sustainable pace<br/>◑ 3"]:::p3_expected
        RfA_a["RfA-a: Purposeful routines<br/>◑ 3"]:::p3_expected
        RfA_b["RfA-b: Launch checklist<br/>◑ 3"]:::p3_expected
        RfA_c["RfA-c: Cross-functional syncs<br/>◑ 3"]:::p3_expected
    end

    classDef p1_expected fill:#4A90D9,color:#fff,stroke:#2E5C8A,stroke-width:2px
    classDef p1_advanced fill:#2E5C8A,color:#fff,stroke:#1A3D5C,stroke-width:3px
    classDef p2_expected fill:#D4A843,color:#fff,stroke:#A07D2E,stroke-width:2px
    classDef p2_advanced fill:#A07D2E,color:#fff,stroke:#7A5E1E,stroke-width:3px
    classDef p3_expected fill:#5BA55B,color:#fff,stroke:#3D7A3D,stroke-width:2px
    classDef p3_advanced fill:#3D7A3D,color:#fff,stroke:#2A5A2A,stroke-width:3px
```

---

## Maturity Stage

At Maturity, most standards hold at Level 3. Six standards push to Level 4
(optimization): CMI-a (broaden to unmet needs), SP-a (spot emerging segments),
CEJ-a (journey optimization), PEI-a (economic optimization), VGR-a (teams
self-manage guardrails), MO-b (optimize against KPIs).

**Expected: 39 of 39** | **Level 4 targets: 6 of 39**

| Level 4 Standards | Why Advanced at Maturity |
|---|---|
| CMI-a | Focus on unmet needs in underserved segments; multiple signal sources |
| SP-a | Spot emerging segments; retire stale ones |
| CEJ-a | Journey optimization; friction reduction tracking |
| PEI-a | Economic model stable and trusted; optimization |
| VGR-a | Guardrails well-established; teams self-manage |
| MO-b | Optimization against established KPIs; targets recalibrated |

```mermaid
graph TD
    subgraph "Pillar 1: Customer-Centered Product Design"
        CMI_a["CMI-a: Talks to customers<br/>◑ 3"]:::p1_expected
        CMI_b["CMI-b: Insights stored<br/>◑ 3"]:::p1_expected
        CMI_c["CMI-c: Usability testing<br/>◑ 3"]:::p1_expected
        CMI_d["CMI-d: Prototype feedback<br/>◑ 3"]:::p1_expected
        SP_a["SP-a: Behavioral segments<br/>◕ 4"]:::p1_advanced
        SP_b["SP-b: Persona review<br/>◑ 3"]:::p1_expected
        SP_c["SP-c: Segments in decisions<br/>◑ 3"]:::p1_expected
        CEJ_a["CEJ-a: Journey maps<br/>◕ 4"]:::p1_advanced
        CEJ_b["CEJ-b: Pain points in backlog<br/>◑ 3"]:::p1_expected
        CEJ_c["CEJ-c: Design system<br/>◑ 3"]:::p1_expected
    end

    subgraph "Pillar 2: Measurable Economic Value"
        PEI_a["PEI-a: Economic KPIs<br/>◕ 4"]:::p2_advanced
        PEI_b["PEI-b: Unit economics<br/>◑ 3"]:::p2_expected
        PEI_c["PEI-c: Leading indicators<br/>◑ 3"]:::p2_expected
        PEI_d["PEI-d: North star metric<br/>◑ 3"]:::p2_expected
        VBS_a["VBS-a: Scoring framework<br/>◑ 3"]:::p2_expected
        VBS_b["VBS-b: Value hypothesis<br/>◑ 3"]:::p2_expected
        VBS_c["VBS-c: Ranked backlog<br/>◑ 3"]:::p2_expected
        VBS_d["VBS-d: Readiness check<br/>◑ 3"]:::p2_expected
        VBS_e["VBS-e: Trade-offs documented<br/>◑ 3"]:::p2_expected
        VGR_a["VGR-a: Guardrails dashboard<br/>◕ 4"]:::p2_advanced
        VGR_b["VGR-b: R/I/T allocation<br/>◑ 3"]:::p2_expected
        VGR_c["VGR-c: Kill criteria real<br/>◑ 3"]:::p2_expected
        VGR_d["VGR-d: Value realization check<br/>◑ 3"]:::p2_expected
    end

    subgraph "Pillar 3: Enduring Lifecycle"
        MO_a["MO-a: Falsifiable vision<br/>◑ 3"]:::p3_expected
        MO_b["MO-b: KPIs with targets<br/>◕ 4"]:::p3_advanced
        MO_c["MO-c: Builds to outcomes<br/>◑ 3"]:::p3_expected
        MO_d["MO-d: Leading + lagging<br/>◑ 3"]:::p3_expected
        SR_a["SR-a: Outcome roadmap<br/>◑ 3"]:::p3_expected
        SR_b["SR-b: OKRs to themes<br/>◑ 3"]:::p3_expected
        SR_c["SR-c: Quarterly review<br/>◑ 3"]:::p3_expected
        SR_d["SR-d: Work-to-strategy<br/>◑ 3"]:::p3_expected
        ADP_a["ADP-a: Defined intake<br/>◑ 3"]:::p3_expected
        ADP_b["ADP-b: Regular refinement<br/>◑ 3"]:::p3_expected
        ADP_c["ADP-c: Predictable cadence<br/>◑ 3"]:::p3_expected
        ADP_d["ADP-d: Risk register<br/>◑ 3"]:::p3_expected
        ADP_e["ADP-e: Sustainable pace<br/>◑ 3"]:::p3_expected
        RfA_a["RfA-a: Purposeful routines<br/>◑ 3"]:::p3_expected
        RfA_b["RfA-b: Launch checklist<br/>◑ 3"]:::p3_expected
        RfA_c["RfA-c: Cross-functional syncs<br/>◑ 3"]:::p3_expected
    end

    classDef p1_expected fill:#4A90D9,color:#fff,stroke:#2E5C8A,stroke-width:2px
    classDef p1_advanced fill:#2E5C8A,color:#fff,stroke:#1A3D5C,stroke-width:3px
    classDef p2_expected fill:#D4A843,color:#fff,stroke:#A07D2E,stroke-width:2px
    classDef p2_advanced fill:#A07D2E,color:#fff,stroke:#7A5E1E,stroke-width:3px
    classDef p3_expected fill:#5BA55B,color:#fff,stroke:#3D7A3D,stroke-width:2px
    classDef p3_advanced fill:#3D7A3D,color:#fff,stroke:#2A5A2A,stroke-width:3px
```

---

## Sunset Stage

At Sunset, scope narrows. Standards split into three categories:
- **Still expected (Level 3):** Transition-critical — journey maps, vision, roadmap,
  risk register, routines, intake, cross-functional coordination
- **Reduced (Level 2):** Less applicable at reduced scope but not irrelevant
- **Contextually elevated:** PEI-b stays at 3 (transition economics need documenting),
  VGR-a stays at 3 (guardrails protect the transition CX)

**Expected: 15 of 39** | **Stretch: 24 of 39**

| Status | Standards |
|--------|-----------|
| Expected (≥3) | CEJ-a, PEI-b, VGR-a, MO-a, MO-b, SR-a, SR-c, ADP-a, ADP-d, RfA-a, RfA-c |
| Stretch (<3) | All others |

```mermaid
graph TD
    subgraph "Pillar 1: Customer-Centered Product Design"
        CMI_a["CMI-a: Talks to customers<br/>◔ 2"]:::p1_stretch
        CMI_b["CMI-b: Insights stored<br/>◔ 2"]:::p1_stretch
        CMI_c["CMI-c: Usability testing<br/>◔ 2"]:::p1_stretch
        CMI_d["CMI-d: Prototype feedback<br/>◔ 2"]:::p1_stretch
        SP_a["SP-a: Behavioral segments<br/>◔ 2"]:::p1_stretch
        SP_b["SP-b: Persona review<br/>◔ 2"]:::p1_stretch
        SP_c["SP-c: Segments in decisions<br/>◔ 2"]:::p1_stretch
        CEJ_a["CEJ-a: Journey maps<br/>◑ 3"]:::p1_expected
        CEJ_b["CEJ-b: Pain points in backlog<br/>◔ 2"]:::p1_stretch
        CEJ_c["CEJ-c: Design system<br/>◔ 2"]:::p1_stretch
    end

    subgraph "Pillar 2: Measurable Economic Value"
        PEI_a["PEI-a: Economic KPIs<br/>◔ 2"]:::p2_stretch
        PEI_b["PEI-b: Unit economics<br/>◑ 3"]:::p2_expected
        PEI_c["PEI-c: Leading indicators<br/>◔ 2"]:::p2_stretch
        PEI_d["PEI-d: North star metric<br/>◔ 2"]:::p2_stretch
        VBS_a["VBS-a: Scoring framework<br/>◔ 2"]:::p2_stretch
        VBS_b["VBS-b: Value hypothesis<br/>◔ 2"]:::p2_stretch
        VBS_c["VBS-c: Ranked backlog<br/>◔ 2"]:::p2_stretch
        VBS_d["VBS-d: Readiness check<br/>◔ 2"]:::p2_stretch
        VBS_e["VBS-e: Trade-offs documented<br/>◔ 2"]:::p2_stretch
        VGR_a["VGR-a: Guardrails dashboard<br/>◑ 3"]:::p2_expected
        VGR_b["VGR-b: R/I/T allocation<br/>◔ 2"]:::p2_stretch
        VGR_c["VGR-c: Kill criteria real<br/>◔ 2"]:::p2_stretch
        VGR_d["VGR-d: Value realization check<br/>◔ 2"]:::p2_stretch
    end

    subgraph "Pillar 3: Enduring Lifecycle"
        MO_a["MO-a: Falsifiable vision<br/>◑ 3"]:::p3_expected
        MO_b["MO-b: KPIs with targets<br/>◑ 3"]:::p3_expected
        MO_c["MO-c: Builds to outcomes<br/>◔ 2"]:::p3_stretch
        MO_d["MO-d: Leading + lagging<br/>◔ 2"]:::p3_stretch
        SR_a["SR-a: Outcome roadmap<br/>◑ 3"]:::p3_expected
        SR_b["SR-b: OKRs to themes<br/>◔ 2"]:::p3_stretch
        SR_c["SR-c: Quarterly review<br/>◑ 3"]:::p3_expected
        SR_d["SR-d: Work-to-strategy<br/>◔ 2"]:::p3_stretch
        ADP_a["ADP-a: Defined intake<br/>◑ 3"]:::p3_expected
        ADP_b["ADP-b: Regular refinement<br/>◔ 2"]:::p3_stretch
        ADP_c["ADP-c: Predictable cadence<br/>◔ 2"]:::p3_stretch
        ADP_d["ADP-d: Risk register<br/>◑ 3"]:::p3_expected
        ADP_e["ADP-e: Sustainable pace<br/>◔ 2"]:::p3_stretch
        RfA_a["RfA-a: Purposeful routines<br/>◑ 3"]:::p3_expected
        RfA_b["RfA-b: Launch checklist<br/>◔ 2"]:::p3_stretch
        RfA_c["RfA-c: Cross-functional syncs<br/>◑ 3"]:::p3_expected
    end

    classDef p1_expected fill:#4A90D9,color:#fff,stroke:#2E5C8A,stroke-width:2px
    classDef p1_stretch fill:#4A90D9,color:#fff,stroke:#2E5C8A,stroke-width:2px,stroke-dasharray: 5 5,opacity:0.5
    classDef p2_expected fill:#D4A843,color:#fff,stroke:#A07D2E,stroke-width:2px
    classDef p2_stretch fill:#D4A843,color:#fff,stroke:#A07D2E,stroke-width:2px,stroke-dasharray: 5 5,opacity:0.5
    classDef p3_expected fill:#5BA55B,color:#fff,stroke:#3D7A3D,stroke-width:2px
    classDef p3_stretch fill:#5BA55B,color:#fff,stroke:#3D7A3D,stroke-width:2px,stroke-dasharray: 5 5,opacity:0.5
```

---

## Legend

| Visual | Meaning |
|--------|---------|
| Solid fill, thick border | **Expected** — target maturity ≥ 3 at this stage |
| Dashed border, faded fill | **Stretch** — target maturity < 3; building toward it or reduced scope |
| Darker solid fill, thicker border | **Advanced** — target maturity = 4; optimization opportunity |
| Blue nodes | Pillar 1: Customer-Centered Product Design |
| Gold nodes | Pillar 2: Measurable Economic Value |
| Green nodes | Pillar 3: Enduring Lifecycle |

**Standards progression summary:**
- **5 expected at Concept** → **30 at Launch** → **39 at Growth** → **39 at Maturity** → **15 at Sunset**
- The Growth-to-Maturity transition is about depth (6 standards push to Level 4), not breadth
- Sunset narrows to transition-critical standards; lower targets are appropriate, not gaps
