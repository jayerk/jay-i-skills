# Dependency Mapping Framework

## Purpose

A structured workflow for identifying, classifying, and visualizing dependencies between practices, capabilities, or work items. Produces relationship maps that prevent incoherent adoption — cherry-picking practices that don't work without their prerequisites. Based on John Cutler's work on dependency mapping and dependency debt, with strategic coherence principles from Rumelt's "Good Strategy Bad Strategy" (coherent actions that reinforce each other).

## When to Use

- Sequencing adoption of a practice model (e.g., product standards across teams)
- Planning capability buildout where practices reinforce each other
- Analyzing an initiative portfolio for hidden prerequisite chains
- Coaching teams on where to start when maturity is low across multiple areas
- Validating that OKRs or strategic themes form a coherent set (not isolated bets)

## When NOT to Use

- **Simple task ordering** — if the sequence is obvious (build before test), you don't need a framework for it. Use a checklist.
- **Single-team sprint planning** — sprint-level dependencies are managed in standup and refinement, not with a dependency map
- **Linear workflows** — if A → B → C and there are no branches, forks, or bidirectional relationships, a list is sufficient
- **Political mapping** — dependency mapping is about work relationships, not stakeholder influence. Use `skills/stakeholder-navigation/SKILL.md` for that.

## Inputs

- A set of **nodes** — the things you're mapping (practices, capabilities, standards, initiatives, OKRs)
- **Context** for evaluation — who is adopting, what their current maturity looks like, what constraints exist
- Ideally, documented definitions of each node (what "doing this well" looks like) — without clear definitions, dependency classification becomes subjective

## Workflow

### Phase 1: Inventory Nodes

**Goal:** List everything you're mapping and confirm the boundaries.

**Steps:**
1. **List all nodes** — practices, capabilities, standards, or work items to include. Use the canonical names from the source document (e.g., sub-practice names from a standards model).

2. **Group nodes** — identify natural clusters (pillars, domains, themes). These become subgraphs in the visualization.

3. **Confirm scope** — decide what's in and what's out. A dependency map that tries to include everything becomes unreadable. Scope to one level of granularity at a time:
   - **High-level map:** Sub-practices, capabilities, or themes (10-15 nodes max)
   - **Detail map:** Individual standards, requirements, or work items within a group (scoped to one cluster)

**Output:** Numbered node list with groupings.

### Phase 2: Identify Relationships

**Goal:** Determine which nodes depend on, support, or reinforce other nodes.

**Steps:**
1. **Pairwise analysis** — for each pair of nodes, ask:
   - Does doing A well make B easier, more effective, or more likely to succeed?
   - Does skipping A make B harder, less effective, or likely to produce surface-level compliance?
   - Is the relationship directional (A → B) or bidirectional (A ↔ B)?

2. **Record candidate relationships** — capture every plausible dependency. You'll classify and filter in the next phases. Over-include now; prune later.

3. **Look for hidden chains** — some dependencies are indirect. A doesn't depend on B directly, but both depend on C. Make C explicit.

**Output:** Raw relationship list (Source → Target or Source ↔ Target).

### Phase 3: Classify Dependencies

**Goal:** Assign a type to each relationship using the dependency type taxonomy.

**Dependency Type Taxonomy:**

| Type | Definition | Direction | Example |
|------|-----------|-----------|---------|
| **Knowledge** | Understanding from A is required before B makes sense. Without the mental model A provides, B is followed mechanically. | A → B | Understanding customer segments before attempting journey mapping |
| **Artifact** | Output from A feeds directly into B. B needs A's deliverable as an input. | A → B | Personas (from segmentation) used in journey mapping |
| **Capability** | The organizational muscle built by practicing A is needed before B is feasible. Not about deliverables — about the team's ability. | A → B | Running regular discovery cadence before attempting value hypothesis testing |
| **Complementary** | A and B amplify each other. No strict ordering — doing either one well makes the other more effective. | A ↔ B | Strategy and measurable outcomes reinforce each other bidirectionally |
| **Sequencing** | Pure ordering preference without a strong conceptual link. Use only when no other type fits. | A → B | Rare — most real dependencies have a conceptual basis |

**Rules:**
- Most relationships will be Knowledge, Artifact, or Capability. If you're classifying many as Sequencing, you haven't understood the relationship well enough.
- Complementary is bidirectional. Don't use it for directional relationships where one side is clearly prerequisite.
- A single relationship can have multiple types (e.g., both Knowledge and Artifact). Pick the primary type — the one that best explains why skipping the source causes problems.

**Output:** Typed relationship list (Source → Target, Type).

### Phase 4: Assess Strength

**Goal:** Rate how critical each dependency is.

**Strength Scale:**

| Strength | Definition | Consequence of Skipping |
|----------|-----------|------------------------|
| **Strong** | Skipping creates **dependency debt**. The target practice regresses or produces theater — surface-level compliance without real capability. | Teams attempt B without A and produce artifacts that look right but don't drive decisions. Recovery requires going back and building A from scratch. |
| **Moderate** | Target works without source but is noticeably less effective. Teams hit friction — things take longer, require more rework, or miss edge cases. | Teams can do B without A, but they'll reinvent parts of A along the way, or their B outputs will be shallow. Friction accumulates but doesn't block. |
| **Light** | Nice-to-have sequencing. Teams that are aware of the relationship benefit; those that aren't still function. | Minimal impact. Slightly less efficient or slightly less connected, but the target practice stands on its own. |

**Dependency Debt:** When teams skip strong prerequisites and build on shaky foundations. The target practice produces theater — it looks like compliance but doesn't change behavior or decisions. Dependency debt accumulates silently and surfaces when teams try to advance maturity and discover their foundations are missing. The concept parallels technical debt: easy to accrue, expensive to pay down, invisible until it isn't.

**Output:** Strength-rated relationship list (Source → Target, Type, Strength).

### Phase 5: Visualize

**Goal:** Produce readable diagrams that communicate the dependency structure.

**Two visualization types serve different audiences:**

#### Adoption View (High-Level)

- **Audience:** Leaders deciding where to invest, coaches planning engagements
- **Nodes:** Sub-practices, capabilities, or themes (the grouped level from Phase 1)
- **Edges:** Show type (via line style or color) and strength (via line weight)
- **Layout:** Group nodes by cluster (pillar, domain). Strong dependencies drive layout — heavily connected nodes should be adjacent.
- **Goal:** Answer "where should we start?" and "what breaks if we skip this?"

#### Reference View (Detail)

- **Audience:** Coaches working with specific teams, practitioners tracing specific gaps
- **Nodes:** Individual standards, requirements, or work items
- **Edges:** All cross-group dependencies shown
- **Layout:** Group nodes by parent cluster. Accept that this will be dense — it's a reference, not a presentation.
- **Goal:** Answer "which specific standards are connected?" and "if this standard is weak, what else is affected?"

**Visual Encoding:**

| Element | Encoding |
|---------|----------|
| **Dependency type** | Line style: solid (Knowledge), dashed (Artifact), dotted (Capability), double-line (Complementary) |
| **Strength** | Line weight or annotation: Strong (thick/bold), Moderate (normal), Light (thin) |
| **Grouping** | Subgraphs with labeled borders |
| **Direction** | Arrows (→ for directional, ↔ for Complementary) |

**Output:** Two diagrams (adoption view and reference view) with legends.

### Phase 6: Derive Adoption Sequence

**Goal:** Turn the dependency map into a recommended starting order.

**Steps:**
1. **Find foundation nodes** — nodes with many outgoing strong dependencies and few incoming ones. These are the starting points.

2. **Topological sort** — order nodes so that prerequisites come before dependents. When the graph has cycles (common with Complementary relationships), break cycles at the weakest edge.

3. **Group into adoption waves** — cluster nodes that can be adopted in parallel (no dependencies between them within the wave). Each wave's prerequisites should be complete in a prior wave.

4. **Write the narrative** — for each wave, explain:
   - What to focus on
   - Why this comes before the next wave
   - What becomes possible once this wave is established

**Output:** Ordered adoption sequence with wave groupings and rationale.

## Output Format

```markdown
# Dependency Map: [What You're Mapping]

## Nodes
| # | Node | Group |
|---|------|-------|
| 1 | [Node name] | [Group/Pillar] |

## Relationships
| Source | Target | Type | Strength | Rationale |
|--------|--------|------|----------|-----------|
| [Source] | [Target] | Knowledge/Artifact/Capability/Complementary | Strong/Moderate/Light | [Why this dependency exists] |

## Adoption View
[Mermaid diagram — grouped nodes, typed/weighted edges]

## Reference View
[Mermaid diagram — individual items, all cross-group edges]

## Recommended Adoption Sequence

### Wave 1: [Theme]
- [Nodes in this wave]
- **Why first:** [Rationale]
- **What it enables:** [What becomes possible]

### Wave 2: [Theme]
...
```

## Vocabulary Cross-References

Key terms used in this framework — see `knowledge/vocabulary.md` for full definitions:

- **Dependency Debt** — when teams skip prerequisite practices and build on shaky foundations. The target practice produces theater — surface-level compliance without real capability.
- **Knowledge Dependency** — understanding from one practice is required before another makes sense
- **Artifact Dependency** — output from one practice feeds into another
- **Capability Dependency** — muscle built by practicing one thing is needed before another is feasible
- **Complementary Dependency** — two practices amplify each other with no strict ordering
- **Coherent Actions** (from Strategy) — initiatives that reinforce each other. Dependency mapping makes coherence visible and testable.
- **Harvey Balls** — the maturity visualization that dependency maps help interpret ("why is this practice stuck at Level 2?")

## Quality Checklist

- [ ] All nodes are clearly defined before mapping relationships
- [ ] Scope is limited to one level of granularity (don't mix sub-practices with individual standards)
- [ ] Each relationship has a type — Sequencing is rare, not the default
- [ ] Strength assessments use the dependency debt test ("what happens if you skip this?")
- [ ] Complementary relationships are genuinely bidirectional, not mislabeled directional ones
- [ ] Adoption view is readable by a leader in 30 seconds
- [ ] Reference view includes all cross-group edges even if dense
- [ ] Adoption sequence follows topological order with cycles broken at weakest edges
- [ ] Wave rationale explains "why this order" not just "what's in the wave"

## Common Pitfalls

- **Everything depends on everything** — if your map shows every node connected to every other node, you haven't distinguished strength levels. Apply the dependency debt test rigorously: does skipping A actually cause B to produce theater?
- **Type confusion** — Knowledge and Capability dependencies feel similar but differ. Knowledge is about understanding ("you need to know what segments are"). Capability is about muscle ("you need to have practiced regular discovery before you can sustain value hypothesis testing").
- **Missing the Complementary** — some pairs genuinely reinforce each other without a clear prerequisite order. Don't force directionality on bidirectional relationships.
- **Over-engineering the diagram** — the reference view will be dense. Accept it. Don't try to make it as clean as the adoption view — they serve different purposes.
- **Ignoring context** — dependency strength varies by team maturity. A team already doing discovery well may not need to sequence insights before segmentation. The map shows the general case; coaching adapts to the specific team.

## Product Standard Alignment

This framework serves **Dimension 9: Dependencies** across all sub-practices in
the product standards model. It also directly supports:

| Practice | Framework Coverage | Where |
|----------|-------------------|-------|
| **All sub-practices** | Dimension 9 (Dependencies) | The methodology for producing the dependency map that each sub-practice references |
| **Gap Analysis skill** | Coaching teams on adoption sequencing | Phase 6 (Derive Adoption Sequence) produces the "where to start" guidance |
| **Product Strategy skill** | Ensuring coherent action sets | Phase 2-3 (identifying and classifying relationships between strategic initiatives) |
