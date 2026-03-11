# Copilot Research Prompts: Internal Artifact Inventory

39 prompts — one per Level 3 (Established) standard across 10 sub-practices.
Run each prompt in M365 Copilot to search Confluence, SharePoint, and Teams
for existing artifacts that already support the standard.

**Purpose:** Inventory what exists before creating anything new.

**How to use the results:** Paste each response into the summary table at the
bottom of this file. The completed table becomes a heat map of coverage x
confidence across all 39 standards.

---

## Response Format

Every prompt asks Copilot to return results in this structure:

```
## [Standard Name]

### Artifacts Found
| Artifact Name | Link | Last Updated | What It Covers | Alignment |
|---|---|---|---|---|
| [Name] | [URL] | [Date] | [Brief description] | Aligns / Partially aligns / Different approach |

### What Differs
[For anything that partially aligns or takes a different approach — describe
what's different and recommend: adopt ours, adopt theirs, or synthesize (and say how)]

### Not Found
[If nothing found, say so explicitly and note what was searched]

### Confidence: [High / Medium / Low]
[Why — e.g., "Medium — searched Confluence and SharePoint but could not access
Teams channel files or personal OneDrives"]
```

---

## Pillar 1: Customer-Centered Product Design

### Sub-Practice 1: Customer & Market Insights

#### Prompt #68 — Regular customer research cadence

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **regular customer research cadence** — specifically any
> guides, standards, playbooks, or process docs that describe how often product
> teams should talk to customers, what formats those conversations take, or how
> discovery interviews are scheduled and tracked.
>
> **The standard to validate against:** "Team talks to customers on a regular
> schedule (e.g., 2-3 interviews/month)."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #69 — Shared insight storage

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **research insight storage and retrieval** — specifically
> any repositories, databases, tagged knowledge bases, or standards for where
> and how customer research findings are stored so the team can find them.
>
> **The standard to validate against:** "Insights are stored somewhere the team
> can find them."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #70 — Pre-launch usability testing

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **usability testing before launch** — specifically any
> standards, checklists, launch-gate requirements, or process docs that require
> or guide usability testing before a product or feature goes live.
>
> **The standard to validate against:** "Usability testing happens before launch."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #71 — Prototype user feedback before commitment

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **prototype feedback before build commitment** —
> specifically any design review gates, concept testing guides, or process docs
> that require user feedback on prototypes or concepts before the team commits
> to building.
>
> **The standard to validate against:** "Prototypes get user feedback before
> the team commits to building."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

### Sub-Practice 2: Segmentation & Personas

#### Prompt #72 — Behavioral or needs-based segments

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **customer segmentation** — specifically any segment
> definitions, segmentation models, or docs that define customer groups based
> on behaviors, needs, or value rather than demographics or org chart.
>
> **The standard to validate against:** "Segments are based on what customers
> need or how they behave, not just who they are."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #73 — Annual persona review

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **persona maintenance** — specifically any persona
> documents, persona review cadences, or governance standards that define how
> often personas are reviewed and updated.
>
> **The standard to validate against:** "Personas get reviewed at least yearly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #74 — Segments referenced in feature decisions

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **using segments in product decisions** — specifically
> any planning templates, decision logs, or prioritization docs that include
> segment fields or reference specific customer segments when making feature
> decisions.
>
> **The standard to validate against:** "The team references specific segments
> when making feature decisions ('this matters most for segment X')."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

### Sub-Practice 3: Customer & Employee Journeys

#### Prompt #75 — Journey maps for key flows

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **customer or employee journey maps** — specifically any
> journey map artifacts, journey mapping standards, or update cadence docs for
> key user flows.
>
> **The standard to validate against:** "Journey maps exist for key flows and
> get updated when things change."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #76 — Pain points in the backlog with journey context

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **connecting pain points to the backlog** — specifically
> any backlog tagging standards, journey-to-backlog linking processes, or
> practices that ensure known customer pain points are tracked in the backlog
> with journey stage context.
>
> **The standard to validate against:** "Known pain points are in the backlog
> with journey context."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #77 — Design system in place and used

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **design systems** — specifically any design system
> documentation, component libraries, style guides, or adoption tracking for
> shared UI components.
>
> **The standard to validate against:** "A design system is in place and teams
> actually use it."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

## Pillar 2: Measurable Economic Value

### Sub-Practice 4: Product Economic Insights

#### Prompt #78 — Key economic KPIs reviewed monthly

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **economic KPI definitions and review cadences** —
> specifically any KPI definitions, metric review cadence docs, dashboard
> standards, or monthly review templates for product economic performance.
>
> **The standard to validate against:** "Team knows the key economic KPIs and
> reviews them monthly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #79 — Unit economics documented

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **unit economics** — specifically any cost-to-serve
> analyses, value-per-transaction models, economic model templates, or docs
> that document unit-level economics for a product.
>
> **The standard to validate against:** "Unit economics are documented (cost to
> serve, value per transaction)."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #80 — Leading indicators alongside lagging

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **leading indicator tracking** — specifically any
> dashboard standards, metric framework docs, or measurement guides that
> require or recommend tracking leading indicators (predictive signals)
> alongside lagging indicators (outcome measures).
>
> **The standard to validate against:** "Leading indicators sit alongside
> lagging ones."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #81 — North star metric defined

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **north star metrics** — specifically any product
> strategy docs, KPI definitions, or metric frameworks that name a primary
> economic KPI representing the product's core value.
>
> **The standard to validate against:** "Team can state the north star metric
> and explain why it matters."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

### Sub-Practice 5: Value-Based Sequencing

#### Prompt #82 — Scoring on value, risk, and effort

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **prioritization scoring** — specifically any scoring
> frameworks, prioritization templates, WSJF models, or planning process docs
> that use value, risk, and effort (or similar dimensions) to score backlog
> items before sequencing.
>
> **The standard to validate against:** "Team scores items on value, risk, and
> effort before sequencing."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #83 — Value hypothesis per item

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **value hypotheses** — specifically any backlog item
> templates, user story templates, or planning docs that include a value
> hypothesis field (e.g., "we believe X will result in Y").
>
> **The standard to validate against:** "Each item has a short value hypothesis
> ('we believe X will result in Y')."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #84 — Force-ranked backlog

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **backlog ranking** — specifically any backlog
> management standards, prioritization process docs, or planning guides that
> require a strict rank order with no ties.
>
> **The standard to validate against:** "Backlog is ranked — no ties."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #85 — Readiness check before commitment

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **readiness checks before sprint or wave commitment** —
> specifically any readiness checklists, commitment criteria, capacity planning
> docs, or dependency review processes that run before the team takes on work.
>
> **The standard to validate against:** "Before committing, team checks: do we
> have the people, are dependencies clear, is WIP manageable?"
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #86 — Documented trade-offs

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **trade-off documentation** — specifically any decision
> logs, "not doing" records, deprioritization rationale docs, or planning
> templates that capture why items were deprioritized and what was traded off.
>
> **The standard to validate against:** "Trade-offs are documented when items
> are deprioritized."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

### Sub-Practice 6: Value Guardrails & Realization

#### Prompt #87 — CX, reliability, and capacity guardrails on a dashboard

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **product guardrails** — specifically any SLA/SLO
> definitions, CX guardrail docs, reliability targets, capacity dashboards,
> or standards that define thresholds for customer experience, system
> reliability, or capacity allocation.
>
> **The standard to validate against:** "Guardrails for CX, reliability, and
> capacity are defined and on a dashboard."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #88 — R/I/T allocation targets reviewed quarterly

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **Run/Improve/Transform capacity allocation** —
> specifically any R/I/T allocation docs, capacity planning templates,
> quarterly review materials, or investment categorization standards.
>
> **The standard to validate against:** "R/I/T allocation targets are set and
> reviewed quarterly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #89 — Kill criteria applied to at least one initiative

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **initiative kill criteria** — specifically any kill
> criteria templates, stop/pivot decision records, initiative review processes,
> or docs that define conditions for stopping or pivoting an initiative.
>
> **The standard to validate against:** "Kill criteria are real — at least one
> initiative has been stopped because a trigger was hit."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #90 — Post-launch value hypothesis check

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **benefits realization or post-launch value tracking** —
> specifically any benefits realization processes, post-launch review templates,
> value tracking docs, or practices that check whether the expected value from
> an initiative actually materialized.
>
> **The standard to validate against:** "Post-launch, team checks whether the
> value hypothesis played out."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

## Pillar 3: Enduring Lifecycle

### Sub-Practice 7: Measurable Outcomes

#### Prompt #91 — Falsifiable product vision

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **product vision documents** — specifically any vision
> statements, vision templates, or strategy docs that articulate what value
> the product delivers to specific customers in terms you could check whether
> it's true.
>
> **The standard to validate against:** "Vision says what value the product
> delivers to specific customers and you could check whether it's true."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #92 — KPIs with targets reviewed monthly

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **KPI target-setting and review** — specifically any KPI
> target-setting processes, monthly review templates, metric governance docs,
> or dashboards that show KPIs with explicit targets.
>
> **The standard to validate against:** "KPIs have targets and get reviewed
> monthly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #93 — Planning connects work to expected outcomes

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **outcome-connected planning** — specifically any
> planning templates with outcome fields, OKR-to-backlog linking processes,
> or docs that show how planned work connects to expected outcomes.
>
> **The standard to validate against:** "Planning connects what the team builds
> to what they expect to achieve."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #94 — Both leading and lagging indicators tracked

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **balanced indicator tracking** — specifically any
> dashboard standards, measurement framework docs, or metric guides that
> require tracking both leading indicators (predictive) and lagging indicators
> (outcome) together.
>
> **The standard to validate against:** "Both leading (activation, engagement)
> and lagging (retention, revenue) indicators tracked."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

### Sub-Practice 8: Strategy & Roadmap

#### Prompt #95 — Roadmap by time horizons with outcomes

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **outcome-oriented roadmaps** — specifically any roadmap
> templates, roadmap standards, or planning process docs that organize the
> roadmap by time horizons (Now/Next/Later) with stated outcomes rather than
> feature lists.
>
> **The standard to validate against:** "Roadmap organized by time horizons
> (Now/Next/Later) with outcomes, not just features."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #96 — OKRs aligned to strategic themes

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **OKR processes** — specifically any OKR templates, OKR
> process guides, strategic theme definitions, or docs that show how OKRs
> connect to strategic priorities with measurable key results.
>
> **The standard to validate against:** "OKRs align to strategic themes with
> measurable key results."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #97 — Quarterly roadmap review

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **roadmap review cadence** — specifically any quarterly
> planning processes, roadmap review schedules, or governance docs that define
> how and when the roadmap gets reviewed and updated.
>
> **The standard to validate against:** "Roadmap reviewed and updated quarterly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #98 — Team connects work to strategy

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **strategy-to-work alignment** — specifically any
> strategy communication templates, team alignment processes, or docs that help
> teams articulate how their day-to-day work connects to the product or
> organizational strategy.
>
> **The standard to validate against:** "Team can explain how their work
> connects to strategy."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

### Sub-Practice 9: Adaptive Delivery Plans

#### Prompt #99 — Defined intake process

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **work intake processes** — specifically any intake
> forms, request evaluation criteria, triage process docs, or standards that
> define how new work enters the backlog with evaluation criteria.
>
> **The standard to validate against:** "There's a defined way for new work to
> enter (intake with evaluation criteria)."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #100 — Regular backlog refinement

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **backlog refinement** — specifically any refinement
> cadence standards, backlog hygiene guides, or process docs that define how
> often and how the backlog gets refined.
>
> **The standard to validate against:** "Backlog gets refined regularly."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #101 — Predictable delivery cadence

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **delivery cadence** — specifically any sprint or wave
> planning docs, delivery cadence standards, or process guides that establish
> a predictable rhythm for delivering work.
>
> **The standard to validate against:** "Delivery runs in waves or sprints with
> a predictable cadence."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #102 — Risk register reviewed at checkpoints

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **product risk management** — specifically any risk
> register templates, risk management processes, or checkpoint review docs
> that define how product risks are tracked and reviewed at sprint or wave
> boundaries.
>
> **The standard to validate against:** "Risk register exists and gets reviewed
> at checkpoints."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #103 — Sustainable pace monitoring

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **sustainable pace and capacity monitoring** —
> specifically any capacity planning docs, velocity tracking standards, team
> health monitoring, or burnout/sustainability guidelines.
>
> **The standard to validate against:** "Team monitors whether pace is
> sustainable."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

### Sub-Practice 10: Routines for Activation

#### Prompt #104 — Regular routines with clear purpose

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **product team meeting standards** — specifically any
> meeting governance docs, routine calendar templates, or standards that define
> the purpose, cadence, and expected outputs of recurring product routines
> (refinement, roadmap review, stakeholder updates, retros).
>
> **The standard to validate against:** "Regular routines with clear purpose:
> refinement, roadmap review, stakeholder updates, retros."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #105 — Launch checklist with cross-functional engagement

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **launch readiness and enablement** — specifically any
> launch checklists, release readiness templates, go-live process docs, or
> standards that ensure support, training, ops, and compliance are engaged
> before a product or feature goes live.
>
> **The standard to validate against:** "Launch has a checklist — support,
> training, ops, and compliance are engaged before go-live."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

#### Prompt #106 — Cross-functional syncs at milestones

> Search our internal spaces (Confluence, SharePoint, Teams wikis) for existing
> materials related to **cross-functional coordination at milestones** —
> specifically any cross-functional sync processes, milestone review templates,
> or coordination standards that define when and how cross-functional partners
> are engaged at key delivery milestones.
>
> **The standard to validate against:** "Cross-functional syncs happen at key
> milestones."
>
> For each artifact you find, return it in this table:
>
> | Artifact Name | Link | Last Updated | What It Covers | Alignment |
> |---|---|---|---|---|
>
> Alignment = Aligns / Partially aligns / Different approach
>
> For anything that partially aligns or takes a different approach, describe
> what's different and recommend: **adopt ours, adopt theirs, or synthesize**
> (and say how).
>
> If you find nothing, say so explicitly and note what spaces you searched.
>
> **Confidence:** Rate High / Medium / Low for how complete your search was,
> and explain why.

---

## Summary Table

Paste results here to build the heat map. One row per standard.

| # | Sub-Practice | Standard | Artifacts Found | Coverage | Confidence | Action |
|---|-------------|---------|----------------|----------|-----------|--------|
| 68 | 1. Customer & Market Insights | Regular customer research cadence | | | | |
| 69 | 1. Customer & Market Insights | Shared insight storage | | | | |
| 70 | 1. Customer & Market Insights | Pre-launch usability testing | | | | |
| 71 | 1. Customer & Market Insights | Prototype feedback before commitment | | | | |
| 72 | 2. Segmentation & Personas | Behavioral/needs-based segments | | | | |
| 73 | 2. Segmentation & Personas | Annual persona review | | | | |
| 74 | 2. Segmentation & Personas | Segments referenced in decisions | | | | |
| 75 | 3. Customer & Employee Journeys | Journey maps for key flows | | | | |
| 76 | 3. Customer & Employee Journeys | Pain points in backlog with journey context | | | | |
| 77 | 3. Customer & Employee Journeys | Design system in place and used | | | | |
| 78 | 4. Product Economic Insights | Key economic KPIs reviewed monthly | | | | |
| 79 | 4. Product Economic Insights | Unit economics documented | | | | |
| 80 | 4. Product Economic Insights | Leading alongside lagging indicators | | | | |
| 81 | 4. Product Economic Insights | North star metric defined | | | | |
| 82 | 5. Value-Based Sequencing | Scoring on value, risk, effort | | | | |
| 83 | 5. Value-Based Sequencing | Value hypothesis per item | | | | |
| 84 | 5. Value-Based Sequencing | Force-ranked backlog | | | | |
| 85 | 5. Value-Based Sequencing | Readiness check before commitment | | | | |
| 86 | 5. Value-Based Sequencing | Documented trade-offs | | | | |
| 87 | 6. Value Guardrails & Realization | CX/reliability/capacity guardrails on dashboard | | | | |
| 88 | 6. Value Guardrails & Realization | R/I/T allocation reviewed quarterly | | | | |
| 89 | 6. Value Guardrails & Realization | Kill criteria applied | | | | |
| 90 | 6. Value Guardrails & Realization | Post-launch value hypothesis check | | | | |
| 91 | 7. Measurable Outcomes | Falsifiable product vision | | | | |
| 92 | 7. Measurable Outcomes | KPIs with targets reviewed monthly | | | | |
| 93 | 7. Measurable Outcomes | Planning connects work to outcomes | | | | |
| 94 | 7. Measurable Outcomes | Leading and lagging indicators tracked | | | | |
| 95 | 8. Strategy & Roadmap | Roadmap by time horizons with outcomes | | | | |
| 96 | 8. Strategy & Roadmap | OKRs aligned to strategic themes | | | | |
| 97 | 8. Strategy & Roadmap | Quarterly roadmap review | | | | |
| 98 | 8. Strategy & Roadmap | Team connects work to strategy | | | | |
| 99 | 9. Adaptive Delivery Plans | Defined intake process | | | | |
| 100 | 9. Adaptive Delivery Plans | Regular backlog refinement | | | | |
| 101 | 9. Adaptive Delivery Plans | Predictable delivery cadence | | | | |
| 102 | 9. Adaptive Delivery Plans | Risk register at checkpoints | | | | |
| 103 | 9. Adaptive Delivery Plans | Sustainable pace monitoring | | | | |
| 104 | 10. Routines for Activation | Regular routines with clear purpose | | | | |
| 105 | 10. Routines for Activation | Launch checklist with cross-functional engagement | | | | |
| 106 | 10. Routines for Activation | Cross-functional syncs at milestones | | | | |

### Coverage Key

- **Full** — Artifact exists that directly addresses this standard
- **Partial** — Artifact exists but covers it tangentially or incompletely
- **Gap** — Nothing found (check confidence before creating)
- **Different** — Artifact exists but takes a meaningfully different approach

### Action Key

- **Adopt ours** — Internal artifact is missing or weaker; use the standard as-is
- **Adopt theirs** — Internal artifact is stronger or more contextual; update the standard
- **Synthesize** — Both have value; merge the best of each
- **Validate** — Low confidence search; manually confirm before deciding
