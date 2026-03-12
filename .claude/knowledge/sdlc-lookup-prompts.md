# SDLC Lookup Prompts: Product Standards × SDLC Alignment

Two prompt sets targeting the enterprise SDLC SharePoint site:

- **Part 1** — 39 Level 3 product standards checked against SDLC artifacts
- **Part 2** — SDLC phase gate prompts (requirements → operate)

**Target site:** `[YOUR SDLC SHAREPOINT SITE]` — replace this placeholder
with the actual SharePoint site name or URL before running each prompt.

**Purpose:** Determine where product management standards are already
embedded in (or conflict with) the enterprise SDLC, and where gaps exist.

---

## Response Format

Every prompt asks Copilot to return results in this structure:

```
## [Standard or Phase Name]

### Artifacts Found
| Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
|---|---|---|---|---|---|
| [Name] | [URL] | [Date] | [Phase] | [Brief description] | Aligns / Partially aligns / Different approach / Not addressed |

### What Differs
[For anything that partially aligns or takes a different approach — describe
what's different and recommend: adopt product standard, adopt SDLC approach,
or synthesize (and say how)]

### Integration Opportunity
[Where could this standard be embedded into an existing SDLC gate, template,
or checkpoint without creating a separate process?]

### Not Found
[If nothing found, say so explicitly and note what was searched]

### Confidence: [High / Medium / Low]
[Why — e.g., "Medium — searched the SDLC site but could not access
sub-sites or document libraries with restricted permissions"]
```

---

# Part 1: Product Standards × SDLC

39 prompts — one per Level 3 standard. Each asks: does the SDLC already
cover this, and if so, where?

---

## Pillar 1: Customer-Centered Product Design

### Sub-Practice 1: Customer & Market Insights

#### SDLC Prompt #1 — Regular customer research cadence

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **regular customer research** —
> specifically anything that requires or guides teams to talk to customers on
> a regular schedule, conduct discovery interviews, or gather user feedback
> as part of the development lifecycle.
>
> **Product standard to check against:** "Team talks to customers on a regular
> schedule (e.g., 2-3 interviews/month)."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #2 — Shared insight storage

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **research insight storage** —
> specifically anything that defines where customer or user research findings
> should be stored, tagged, or made retrievable across the team.
>
> **Product standard to check against:** "Insights are stored somewhere the
> team can find them."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #3 — Pre-launch usability testing

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **usability testing before launch** —
> specifically anything in release readiness, UAT, or pre-production gates
> that requires usability validation with real users.
>
> **Product standard to check against:** "Usability testing happens before
> launch."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #4 — Prototype user feedback before commitment

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **prototype or concept validation** —
> specifically anything in the requirements or design phase that requires user
> feedback on prototypes before committing to build.
>
> **Product standard to check against:** "Prototypes get user feedback before
> the team commits to building."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

### Sub-Practice 2: Segmentation & Personas

#### SDLC Prompt #5 — Behavioral or needs-based segments

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **customer segmentation** —
> specifically anything in requirements or design phases that requires defining
> or referencing customer segments based on behaviors or needs.
>
> **Product standard to check against:** "Segments are based on what customers
> need or how they behave, not just who they are."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #6 — Annual persona review

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **persona creation or maintenance** —
> specifically anything that defines when or how personas are created, reviewed,
> or updated as part of the lifecycle.
>
> **Product standard to check against:** "Personas get reviewed at least yearly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #7 — Segments referenced in feature decisions

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **using customer segments in
> decisions** — specifically any planning or requirements templates that include
> fields for target segment or require segment-level justification.
>
> **Product standard to check against:** "The team references specific segments
> when making feature decisions."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

### Sub-Practice 3: Customer & Employee Journeys

#### SDLC Prompt #8 — Journey maps for key flows

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **journey mapping** — specifically
> anything in requirements or design phases that requires journey maps or
> service blueprints for key user flows.
>
> **Product standard to check against:** "Journey maps exist for key flows and
> get updated when things change."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #9 — Pain points in backlog with journey context

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **connecting pain points to the
> backlog** — specifically anything that requires linking known customer pain
> points to backlog items with journey stage context.
>
> **Product standard to check against:** "Known pain points are in the backlog
> with journey context."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #10 — Design system in place and used

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **design systems or component
> libraries** — specifically anything in design or build phases that requires
> or references a shared design system, style guide, or component library.
>
> **Product standard to check against:** "A design system is in place and teams
> actually use it."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

## Pillar 2: Measurable Economic Value

### Sub-Practice 4: Product Economic Insights

#### SDLC Prompt #11 — Key economic KPIs reviewed monthly

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **economic KPI tracking** —
> specifically anything that requires defining, tracking, or reviewing product
> economic KPIs at any phase of the lifecycle.
>
> **Product standard to check against:** "Team knows the key economic KPIs and
> reviews them monthly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #12 — Unit economics documented

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **unit economics or cost-to-serve** —
> specifically anything in business case, requirements, or post-launch phases
> that requires documenting unit-level economics.
>
> **Product standard to check against:** "Unit economics are documented (cost to
> serve, value per transaction)."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #13 — Leading indicators alongside lagging

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **leading vs. lagging indicator
> tracking** — specifically anything that requires or recommends tracking
> predictive signals alongside outcome measures.
>
> **Product standard to check against:** "Leading indicators sit alongside
> lagging ones."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #14 — North star metric defined

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **north star metrics or primary
> product KPIs** — specifically anything that requires naming the single most
> important metric for a product.
>
> **Product standard to check against:** "Team can state the north star metric
> and explain why it matters."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

### Sub-Practice 5: Value-Based Sequencing

#### SDLC Prompt #15 — Scoring on value, risk, and effort

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **prioritization scoring** —
> specifically anything that requires scoring or evaluating items on value,
> risk, and effort before sequencing them into delivery.
>
> **Product standard to check against:** "Team scores items on value, risk,
> and effort before sequencing."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #16 — Value hypothesis per item

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **value hypotheses** — specifically
> any templates or gate criteria that require articulating expected value
> before committing to build.
>
> **Product standard to check against:** "Each item has a short value
> hypothesis ('we believe X will result in Y')."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #17 — Force-ranked backlog

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **backlog ranking or prioritization
> discipline** — specifically anything that requires a strict rank order in
> the backlog with no ties.
>
> **Product standard to check against:** "Backlog is ranked — no ties."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #18 — Readiness check before commitment

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **readiness or commitment checks** —
> specifically anything that requires verifying capacity, dependencies, and
> WIP before the team takes on new work.
>
> **Product standard to check against:** "Before committing, team checks: do we
> have the people, are dependencies clear, is WIP manageable?"
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #19 — Documented trade-offs

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **trade-off documentation** —
> specifically anything that requires recording what was deprioritized and why
> when making planning decisions.
>
> **Product standard to check against:** "Trade-offs are documented when items
> are deprioritized."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

### Sub-Practice 6: Value Guardrails & Realization

#### SDLC Prompt #20 — CX, reliability, and capacity guardrails

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **product guardrails** — specifically
> any SLA/SLO definitions, CX thresholds, reliability targets, or capacity
> standards defined as part of the lifecycle.
>
> **Product standard to check against:** "Guardrails for CX, reliability, and
> capacity are defined and on a dashboard."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #21 — R/I/T allocation reviewed quarterly

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **Run/Improve/Transform capacity
> allocation** — specifically anything that categorizes investment by R/I/T
> or similar allocation models.
>
> **Product standard to check against:** "R/I/T allocation targets are set and
> reviewed quarterly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #22 — Kill criteria applied

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **initiative kill criteria or
> stop/pivot decisions** — specifically anything that defines conditions for
> stopping or pivoting an initiative at a gate review.
>
> **Product standard to check against:** "Kill criteria are real — at least one
> initiative has been stopped because a trigger was hit."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #23 — Post-launch value hypothesis check

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **post-launch value validation or
> benefits realization** — specifically anything in operate or post-launch
> phases that requires checking whether the expected value materialized.
>
> **Product standard to check against:** "Post-launch, team checks whether the
> value hypothesis played out."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

## Pillar 3: Enduring Lifecycle

### Sub-Practice 7: Measurable Outcomes

#### SDLC Prompt #24 — Falsifiable product vision

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **product vision definition** —
> specifically anything that requires a vision statement articulating what
> value the product delivers to specific customers in testable terms.
>
> **Product standard to check against:** "Vision says what value the product
> delivers to specific customers and you could check whether it's true."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #25 — KPIs with targets reviewed monthly

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **KPI target-setting and review** —
> specifically anything that requires products to define KPI targets and
> review them on a regular cadence.
>
> **Product standard to check against:** "KPIs have targets and get reviewed
> monthly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #26 — Planning connects work to expected outcomes

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **outcome-connected planning** —
> specifically anything that requires linking planned work to expected outcomes
> in planning templates or gate criteria.
>
> **Product standard to check against:** "Planning connects what the team builds
> to what they expect to achieve."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #27 — Both leading and lagging indicators tracked

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **balanced indicator tracking** —
> specifically anything that requires both leading (predictive) and lagging
> (outcome) indicators to be defined and tracked.
>
> **Product standard to check against:** "Both leading (activation, engagement)
> and lagging (retention, revenue) indicators tracked."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

### Sub-Practice 8: Strategy & Roadmap

#### SDLC Prompt #28 — Roadmap by time horizons with outcomes

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **roadmap format or structure** —
> specifically anything that defines how roadmaps should be organized (by time
> horizons, by outcomes, by features).
>
> **Product standard to check against:** "Roadmap organized by time horizons
> (Now/Next/Later) with outcomes, not just features."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #29 — OKRs aligned to strategic themes

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **OKRs or goal alignment** —
> specifically anything that requires OKRs, strategic goals, or measurable
> key results to be defined and connected to delivery.
>
> **Product standard to check against:** "OKRs align to strategic themes with
> measurable key results."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #30 — Quarterly roadmap review

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **roadmap review cadence** —
> specifically anything that defines how and when roadmaps are reviewed and
> refreshed.
>
> **Product standard to check against:** "Roadmap reviewed and updated
> quarterly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #31 — Team connects work to strategy

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **strategy-to-work alignment** —
> specifically anything that helps teams articulate how their work connects
> to the product or organizational strategy.
>
> **Product standard to check against:** "Team can explain how their work
> connects to strategy."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

### Sub-Practice 9: Adaptive Delivery Plans

#### SDLC Prompt #32 — Defined intake process

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **work intake** — specifically
> any intake forms, request evaluation criteria, or triage processes for
> how new work enters the backlog.
>
> **Product standard to check against:** "There's a defined way for new work
> to enter (intake with evaluation criteria)."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #33 — Regular backlog refinement

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **backlog refinement or grooming** —
> specifically anything that defines cadence, format, or expectations for
> regular backlog refinement.
>
> **Product standard to check against:** "Backlog gets refined regularly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #34 — Predictable delivery cadence

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **delivery cadence** — specifically
> anything that establishes a predictable rhythm for delivering work (sprints,
> waves, release trains).
>
> **Product standard to check against:** "Delivery runs in waves or sprints
> with a predictable cadence."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #35 — Risk register reviewed at checkpoints

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **risk management** — specifically
> any risk register templates, risk review processes, or checkpoint criteria
> that require reviewing product risks.
>
> **Product standard to check against:** "Risk register exists and gets reviewed
> at checkpoints."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #36 — Sustainable pace monitoring

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **sustainable pace or capacity
> monitoring** — specifically anything that tracks team velocity, utilization,
> or burnout risk.
>
> **Product standard to check against:** "Team monitors whether pace is
> sustainable."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

### Sub-Practice 10: Routines for Activation

#### SDLC Prompt #37 — Regular routines with clear purpose

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **team meeting standards or routine
> governance** — specifically anything that defines the purpose, cadence, and
> expected outputs of recurring product routines.
>
> **Product standard to check against:** "Regular routines with clear purpose:
> refinement, roadmap review, stakeholder updates, retros."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #38 — Launch checklist with cross-functional engagement

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **launch readiness or go-live
> checklists** — specifically anything that ensures support, training, ops,
> and compliance are engaged before a product or feature goes live.
>
> **Product standard to check against:** "Launch has a checklist — support,
> training, ops, and compliance are engaged before go-live."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Prompt #39 — Cross-functional syncs at milestones

> Search `[YOUR SDLC SHAREPOINT SITE]` for any SDLC artifacts, gate criteria,
> templates, or process docs that address **cross-functional coordination** —
> specifically anything that defines when and how cross-functional partners
> are engaged at key delivery milestones.
>
> **Product standard to check against:** "Cross-functional syncs happen at key
> milestones."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | SDLC Phase | What It Covers | Alignment |
> |---|---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach / Not addressed
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt product standard, adopt SDLC
> approach, or synthesize** (and say how).
>
> Where could this standard be embedded into an existing SDLC gate or
> checkpoint without creating a separate process?
>
> If you find nothing, say so explicitly and note what was searched.
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

# Part 2: SDLC Phase Gate Prompts

These prompts search for what the SDLC already requires at each phase,
independent of the product standards. The goal: understand what's already
mandated so product standards can be embedded into existing gates rather
than creating parallel processes.

---

## Phase 1: Ideation & Intake

#### SDLC Phase Prompt #40 — Ideation gate criteria

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to the
> **ideation or intake phase** of the SDLC — specifically any gate criteria,
> required deliverables, templates, or checklists that must be completed before
> an idea or request moves into formal requirements.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | Gate/Phase | Required Deliverables | Who Approves |
> |---|---|---|---|---|---|
>
> Also list:
> - What product management activities are explicitly required at this gate?
> - What product management activities are notably absent?
> - Where could product standards (customer research, segmentation, value
>   hypothesis) be embedded into this gate without creating a new process?
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Phase Prompt #41 — Intake evaluation criteria

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to **how new
> work is evaluated at intake** — specifically any scoring criteria, evaluation
> rubrics, business case templates, or decision frameworks used to assess
> whether an idea should proceed.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | Criteria Used | Who Evaluates |
> |---|---|---|---|---|
>
> Also describe:
> - Does the evaluation include customer impact or value sizing?
> - Does it reference strategic alignment?
> - What dimensions are scored vs. left to judgment?
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

## Phase 2: Requirements & Design

#### SDLC Phase Prompt #42 — Requirements phase deliverables

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to the
> **requirements phase** — specifically any required deliverables, templates,
> gate criteria, or checklists for this phase.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | Required Deliverable | Template Available |
> |---|---|---|---|---|
>
> Also list:
> - Is customer research or user validation required at this phase?
> - Are personas, segments, or journey maps referenced?
> - Is a value hypothesis or success metric required?
> - What product management activities are notably absent from this phase?
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Phase Prompt #43 — Design phase deliverables and reviews

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to the
> **design phase** — specifically any design review processes, required design
> deliverables, UX standards, or design gate criteria.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | Required Deliverable | Review Process |
> |---|---|---|---|---|
>
> Also describe:
> - Is usability testing or user feedback required before design approval?
> - Does the design phase reference a design system or component library?
> - Are prototypes required, and if so, what fidelity?
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

## Phase 3: Build & Integration

#### SDLC Phase Prompt #44 — Build phase standards

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to the
> **build or development phase** — specifically any coding standards, build
> quality gates, integration requirements, or development process docs.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Governs | Mandatory/Optional |
> |---|---|---|---|---|
>
> Also describe:
> - Are there WIP limits or capacity planning requirements?
> - Is there a defined sprint/wave cadence?
> - Are dependency management processes defined?
> - Where do product managers engage during this phase?
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

## Phase 4: Testing & Validation

#### SDLC Phase Prompt #45 — Testing phase requirements

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to the
> **testing and validation phase** — specifically any test strategy templates,
> UAT processes, testing gate criteria, or quality standards.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | Test Type | Required/Optional |
> |---|---|---|---|---|
>
> Also describe:
> - Is usability testing included alongside functional testing?
> - Are acceptance criteria traced back to user needs or outcomes?
> - Is there a distinction between "works correctly" and "delivers value"?
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

## Phase 5: Release & Launch

#### SDLC Phase Prompt #46 — Release gate criteria

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to
> **release readiness or go-live gates** — specifically any release checklists,
> go-live approval processes, launch readiness reviews, or deployment criteria.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | Gate Criteria | Who Approves |
> |---|---|---|---|---|
>
> Also describe:
> - Does the release gate include cross-functional readiness (support,
>   training, ops, compliance)?
> - Are success metrics defined before release?
> - Is there a rollback plan or kill criteria?
> - Is customer communication or enablement included?
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Phase Prompt #47 — Launch enablement requirements

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to **launch
> enablement** — specifically any training plans, support documentation
> requirements, customer communication templates, or operational readiness
> checklists.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Audience |
> |---|---|---|---|---|
>
> Also describe:
> - Who is responsible for launch enablement in the SDLC?
> - Is there a handoff process from product/dev to support/ops?
> - Are there training or documentation standards?
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

## Phase 6: Operate & Iterate

#### SDLC Phase Prompt #48 — Post-launch monitoring and review

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to
> **post-launch monitoring, reviews, or retrospectives** — specifically any
> post-implementation review templates, monitoring standards, or feedback
> collection processes.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Cadence |
> |---|---|---|---|---|
>
> Also describe:
> - Is there a defined post-launch review process?
> - Does it check whether the value hypothesis played out?
> - Are learnings captured and fed back into planning?
> - Is there a defined cadence for post-launch health checks?
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Phase Prompt #49 — Product retirement or sunset process

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to **product
> retirement, sunset, or end-of-life** — specifically any decommissioning
> processes, sunset criteria, or lifecycle stage management docs.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Trigger Criteria |
> |---|---|---|---|---|
>
> Also describe:
> - Are there defined criteria for when a product should be retired?
> - Is there a customer migration or communication process?
> - Does the SDLC address ongoing operate costs vs. value delivered?
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

## Phase 7: Governance & Cross-Cutting

#### SDLC Phase Prompt #50 — Cross-phase governance

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to
> **cross-phase governance** — specifically any governance boards, stage-gate
> review cadences, escalation paths, or decision authority matrices that span
> the entire SDLC.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Governs | Decision Authority |
> |---|---|---|---|---|
>
> Also describe:
> - Who has decision authority at each gate?
> - Is product management a defined role in governance?
> - Are there product-specific governance requirements vs. technical ones?
>
> **Confidence:** Rate High / Medium / Low and explain why.

#### SDLC Phase Prompt #51 — SDLC roles and responsibilities

> Search `[YOUR SDLC SHAREPOINT SITE]` for all artifacts related to **roles
> and responsibilities** across the SDLC — specifically any RACI matrices,
> role definitions, or responsibility assignments for each phase.
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | Roles Defined | PM Role Included |
> |---|---|---|---|---|
>
> Also describe:
> - Is "Product Manager" or "Product Owner" a defined role?
> - What activities are assigned to the product role at each phase?
> - Are there gaps where product activities happen but no role is assigned?
>
> **Confidence:** Rate High / Medium / Low and explain why.

---

# Summary Tables

## Part 1 Summary: Product Standards × SDLC

| # | Sub-Practice | Standard | SDLC Artifacts Found | SDLC Phase | Coverage | Confidence | Action |
|---|-------------|---------|---------------------|-----------|----------|-----------|--------|
| 1 | 1. Customer & Market Insights | Regular customer research cadence | | | | | |
| 2 | 1. Customer & Market Insights | Shared insight storage | | | | | |
| 3 | 1. Customer & Market Insights | Pre-launch usability testing | | | | | |
| 4 | 1. Customer & Market Insights | Prototype feedback before commitment | | | | | |
| 5 | 2. Segmentation & Personas | Behavioral/needs-based segments | | | | | |
| 6 | 2. Segmentation & Personas | Annual persona review | | | | | |
| 7 | 2. Segmentation & Personas | Segments referenced in decisions | | | | | |
| 8 | 3. Customer & Employee Journeys | Journey maps for key flows | | | | | |
| 9 | 3. Customer & Employee Journeys | Pain points in backlog with journey context | | | | | |
| 10 | 3. Customer & Employee Journeys | Design system in place and used | | | | | |
| 11 | 4. Product Economic Insights | Key economic KPIs reviewed monthly | | | | | |
| 12 | 4. Product Economic Insights | Unit economics documented | | | | | |
| 13 | 4. Product Economic Insights | Leading alongside lagging indicators | | | | | |
| 14 | 4. Product Economic Insights | North star metric defined | | | | | |
| 15 | 5. Value-Based Sequencing | Scoring on value, risk, effort | | | | | |
| 16 | 5. Value-Based Sequencing | Value hypothesis per item | | | | | |
| 17 | 5. Value-Based Sequencing | Force-ranked backlog | | | | | |
| 18 | 5. Value-Based Sequencing | Readiness check before commitment | | | | | |
| 19 | 5. Value-Based Sequencing | Documented trade-offs | | | | | |
| 20 | 6. Value Guardrails & Realization | CX/reliability/capacity guardrails | | | | | |
| 21 | 6. Value Guardrails & Realization | R/I/T allocation reviewed quarterly | | | | | |
| 22 | 6. Value Guardrails & Realization | Kill criteria applied | | | | | |
| 23 | 6. Value Guardrails & Realization | Post-launch value hypothesis check | | | | | |
| 24 | 7. Measurable Outcomes | Falsifiable product vision | | | | | |
| 25 | 7. Measurable Outcomes | KPIs with targets reviewed monthly | | | | | |
| 26 | 7. Measurable Outcomes | Planning connects work to outcomes | | | | | |
| 27 | 7. Measurable Outcomes | Leading and lagging indicators tracked | | | | | |
| 28 | 8. Strategy & Roadmap | Roadmap by time horizons with outcomes | | | | | |
| 29 | 8. Strategy & Roadmap | OKRs aligned to strategic themes | | | | | |
| 30 | 8. Strategy & Roadmap | Quarterly roadmap review | | | | | |
| 31 | 8. Strategy & Roadmap | Team connects work to strategy | | | | | |
| 32 | 9. Adaptive Delivery Plans | Defined intake process | | | | | |
| 33 | 9. Adaptive Delivery Plans | Regular backlog refinement | | | | | |
| 34 | 9. Adaptive Delivery Plans | Predictable delivery cadence | | | | | |
| 35 | 9. Adaptive Delivery Plans | Risk register at checkpoints | | | | | |
| 36 | 9. Adaptive Delivery Plans | Sustainable pace monitoring | | | | | |
| 37 | 10. Routines for Activation | Regular routines with clear purpose | | | | | |
| 38 | 10. Routines for Activation | Launch checklist with cross-functional engagement | | | | | |
| 39 | 10. Routines for Activation | Cross-functional syncs at milestones | | | | | |

## Part 2 Summary: SDLC Phase Gates

| # | SDLC Phase | Prompt Focus | Artifacts Found | PM Activities Required | PM Activities Absent | Integration Opportunities |
|---|-----------|-------------|----------------|----------------------|--------------------|-----------------------|
| 40 | Ideation & Intake | Gate criteria | | | | |
| 41 | Ideation & Intake | Evaluation criteria | | | | |
| 42 | Requirements & Design | Requirements deliverables | | | | |
| 43 | Requirements & Design | Design deliverables & reviews | | | | |
| 44 | Build & Integration | Build standards | | | | |
| 45 | Testing & Validation | Testing requirements | | | | |
| 46 | Release & Launch | Release gate criteria | | | | |
| 47 | Release & Launch | Launch enablement | | | | |
| 48 | Operate & Iterate | Post-launch monitoring | | | | |
| 49 | Operate & Iterate | Retirement/sunset | | | | |
| 50 | Governance | Cross-phase governance | | | | |
| 51 | Governance | Roles & responsibilities | | | | |

### Coverage Key

- **Embedded** — Product standard is already required at this SDLC phase
- **Partial** — SDLC touches this area but doesn't fully cover the standard
- **Gap** — SDLC doesn't address this; opportunity to embed
- **Conflict** — SDLC takes a different approach; needs reconciliation

### Action Key

- **Adopt product standard** — Embed the standard into the existing SDLC gate
- **Adopt SDLC approach** — The SDLC version is better; update the product standard
- **Synthesize** — Merge the best of each
- **Validate** — Low confidence search; manually confirm before deciding
- **No action** — Already aligned
