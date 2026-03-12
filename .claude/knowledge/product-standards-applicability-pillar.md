# Product Standards: Applicability — Pillar View

Three Mermaid diagrams showing how target maturity progresses across lifecycle stages
for each pillar's standards. Read left-to-right as the product moves from Concept
through Sunset. Node fill intensity encodes the target level.

Companion to `product-standards-applicability.md` (full matrices and lookup table).
Standard inventory from `product-standards-dependencies-reference.md`.

---

## How to Read These Diagrams

- Each row is one standard flowing left-to-right through 5 lifecycle stages
- **Node fill intensity** encodes target maturity level:
  - Light grey = Level 1 (Emerging)
  - Light fill = Level 2 (Developing)
  - Medium fill = Level 3 (Established)
  - Dark fill = Level 4 (Advanced)
- **Edges** connect the same standard across stages — follow a row to see its arc
- Most standards follow a common arc: light → medium → medium → medium → light
- Standards that peak at Level 4 represent optimization opportunities at Maturity

---

## Pillar 1: Customer-Centered Product Design

10 standards across 3 sub-practices. The arc pattern: discovery-heavy standards
(CMI-a, CMI-d) start high at Concept, governance standards (SP-b, CEJ-c) ramp up
through Growth, and all taper at Sunset except CEJ-a (transition journey mapping
remains critical).

**Peak standards at Maturity:** CMI-a (Level 4 at Growth, broadening signals),
SP-a (Level 4, spotting emerging segments), CEJ-a (Level 4, journey optimization).

| Standard | C | L | G | M | S | Arc Pattern |
|---|:---:|:---:|:---:|:---:|:---:|---|
| CMI-a | 3 | 3 | 4 | 3 | 2 | High start, peaks at Growth |
| CMI-b | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| CMI-c | 1 | 3 | 3 | 3 | 2 | Late start (nothing to test at Concept) |
| CMI-d | 3 | 3 | 3 | 3 | 2 | High start, steady |
| SP-a | 2 | 3 | 3 | 4 | 2 | Peaks at Maturity |
| SP-b | 1 | 2 | 3 | 3 | 2 | Slowest ramp (annual review cadence) |
| SP-c | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| CEJ-a | 2 | 3 | 3 | 4 | 3 | Peaks at Maturity, stays high at Sunset |
| CEJ-b | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| CEJ-c | 1 | 2 | 3 | 3 | 2 | Slowest ramp (design system needs scale) |

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
    classDef t2 fill:#85b8e0,color:#333,stroke:#5a8ab5
    classDef t3 fill:#4A90D9,color:#fff,stroke:#2E5C8A
    classDef t4 fill:#2E5C8A,color:#fff,stroke:#1A3D5C,stroke-width:3px
```

---

## Pillar 2: Measurable Economic Value

13 standards across 3 sub-practices. Economic standards lag discovery standards —
you need data before economics are meaningful. VBS-b (value hypothesis) is an
exception: it's core from Concept. VGR standards ramp differently: kill criteria
(VGR-c) start high, guardrails (VGR-a) start low, and benefits realization
(VGR-d) requires a launch before it applies.

**Peak standards at Maturity:** PEI-a (Level 4, economic optimization),
VGR-a (Level 4, teams self-manage guardrails).

| Standard | C | L | G | M | S | Arc Pattern |
|---|:---:|:---:|:---:|:---:|:---:|---|
| PEI-a | 2 | 3 | 3 | 4 | 2 | Peaks at Maturity |
| PEI-b | 2 | 2 | 3 | 3 | 3 | Slow ramp, stays high at Sunset |
| PEI-c | 1 | 2 | 3 | 3 | 2 | Late start (needs baselines) |
| PEI-d | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| VBS-a | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| VBS-b | 3 | 3 | 3 | 3 | 2 | High start, steady |
| VBS-c | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| VBS-d | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| VBS-e | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| VGR-a | 1 | 3 | 3 | 4 | 3 | Late start, peaks at Maturity, stays high |
| VGR-b | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| VGR-c | 3 | 3 | 3 | 3 | 2 | High start (tight kill criteria at Concept) |
| VGR-d | 1 | 2 | 3 | 3 | 2 | Latest start (needs a launch first) |

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
    classDef t2 fill:#e8d9a0,color:#333,stroke:#c4a84a
    classDef t3 fill:#D4A843,color:#fff,stroke:#A07D2E
    classDef t4 fill:#A07D2E,color:#fff,stroke:#7A5E1E,stroke-width:3px
```

---

## Pillar 3: Enduring Lifecycle

16 standards across 4 sub-practices. This pillar is the most uniform — at Launch,
nearly all standards hit Level 3 and stay there through Maturity. MO-a (vision)
is the only standard at Level 3 from Concept. At Sunset, the pillar splits:
transition-critical standards (SR-a, SR-c, ADP-a, ADP-d, RfA-a, RfA-c, MO-a,
MO-b) stay at Level 3, while operational cadence standards drop to Level 2.

**Peak standard at Maturity:** MO-b (Level 4, optimization against established KPIs).

| Standard | C | L | G | M | S | Arc Pattern |
|---|:---:|:---:|:---:|:---:|:---:|---|
| MO-a | 3 | 3 | 3 | 3 | 3 | Flat — always critical |
| MO-b | 2 | 2 | 3 | 4 | 3 | Slow ramp, peaks at Maturity |
| MO-c | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| MO-d | 1 | 2 | 3 | 3 | 2 | Late start (needs baselines) |
| SR-a | 2 | 3 | 3 | 3 | 3 | Stays high at Sunset (transition plan) |
| SR-b | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| SR-c | 2 | 3 | 3 | 3 | 3 | Stays high at Sunset |
| SR-d | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| ADP-a | 2 | 3 | 3 | 3 | 3 | Stays high at Sunset (transition intake) |
| ADP-b | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| ADP-c | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| ADP-d | 2 | 3 | 3 | 3 | 3 | Stays high at Sunset (migration risks) |
| ADP-e | 2 | 3 | 3 | 3 | 2 | Standard ramp |
| RfA-a | 2 | 3 | 3 | 3 | 3 | Stays high at Sunset (transition routines) |
| RfA-b | 1 | 3 | 3 | 3 | 2 | Late start, drops at Sunset |
| RfA-c | 2 | 3 | 3 | 3 | 3 | Stays high at Sunset (decommission coordination) |

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
    classDef t2 fill:#a3d4a3,color:#333,stroke:#6baa6b
    classDef t3 fill:#5BA55B,color:#fff,stroke:#3D7A3D
    classDef t4 fill:#3D7A3D,color:#fff,stroke:#2A5A2A,stroke-width:3px
```

---

## Legend

| Fill | Level | Harvey Ball | Meaning |
|------|-------|-------------|---------|
| Light grey | 1 — Emerging | ○ | Not yet applicable at this stage |
| Light pillar color | 2 — Developing | ◔ | Building toward; hypothesis or lightweight |
| Medium pillar color | 3 — Established | ◑ | Standard fully in place |
| Dark pillar color | 4 — Advanced | ◕ | Optimizing and extending |

**Pillar color mapping:**
- Pillar 1 (Customer-Centered Product Design): Blue spectrum
- Pillar 2 (Measurable Economic Value): Gold spectrum
- Pillar 3 (Enduring Lifecycle): Green spectrum

**Arc patterns observed:**
| Pattern | Standards | Meaning |
|---------|-----------|---------|
| High start, steady | CMI-a, CMI-d, VBS-b, VGR-c, MO-a | Core from Concept — these define the product |
| Standard ramp | 20+ standards | Level 2 at Concept → Level 3 by Launch → Level 3 through Maturity → Level 2 at Sunset |
| Late start | CMI-c, PEI-c, VGR-d, MO-d, RfA-b | Level 1 at Concept — requires a launch or data accumulation |
| Peaks at Maturity | PEI-a, SP-a, CEJ-a, VGR-a, MO-b | Level 4 at Maturity — optimization opportunity |
| Stays high at Sunset | CEJ-a, PEI-b, VGR-a, MO-a, MO-b, SR-a, SR-c, ADP-a, ADP-d, RfA-a, RfA-c | Transition-critical — don't drop these during sunset |
