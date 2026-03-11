# Vocabulary: Domain Language and Definitions

## Team Topologies

| Term | Definition |
|------|-----------|
| **Stream-Aligned Team** | A team aligned to a single stream of work — a product, a service, a user journey, or a set of features. The primary team type. Optimized for fast flow of change. |
| **Platform Team** | A team that provides internal services to reduce cognitive load on stream-aligned teams. Treats its services as internal products with clear APIs and self-service interfaces. |
| **Enabling Team** | A team that helps other teams adopt new capabilities. Temporary engagement — the goal is to upskill, not to do the work permanently. Think internal consultants. |
| **Complicated Subsystem Team** | A team that owns a subsystem requiring deep specialist knowledge (e.g., ML models, regulatory engines). Reduces the cognitive load that would otherwise fall on stream-aligned teams. |
| **Product Segment** | A grouping of related product capabilities that share a customer segment, business domain, or value stream. Larger than a single team's scope. |
| **Product Domain** | The highest-level organizational unit for product work. Contains multiple product segments. Maps to a major business area or customer population. |
| **Cognitive Load** | The total amount of knowledge and context a team must hold to do its work. When cognitive load exceeds capacity, quality drops and delivery slows. |
| **Interaction Modes** | How teams work together. Three modes define the relationship between any two teams: Collaboration, X-as-a-Service, and Facilitating. |
| **Collaboration** | Two teams working closely together on a shared goal. High-bandwidth, high-cost. Use when discovery is needed or the problem space is unclear. Should be time-limited — if it persists, consider merging or splitting scope. |
| **X-as-a-Service** | One team consumes another team's capability through a well-defined API or contract. Low-bandwidth, low-cost. The goal state for most platform team interactions. Requires clear documentation and self-service interfaces. |
| **Facilitating** | One team (typically enabling) helps another team learn or adopt a new capability. The facilitating team does not do the work — it coaches, guides, and upskills. Engagement is temporary by design. |

## Lifecycle Stages

| Term | Definition |
|------|-----------|
| **Concept** | A product or capability in its earliest phase — validating the problem space, testing assumptions, building the business case. Metrics focus on learning velocity and assumption validation. |
| **Launch** | A product or capability being introduced to its first users — establishing product-market fit, building initial adoption, proving value. Metrics focus on activation and early engagement. |
| **Growth** | A product or capability actively scaling — acquiring users, expanding features, investing heavily. Metrics focus on adoption and engagement. |
| **Maturity** | A product or capability that has reached steady state — optimizing efficiency, maintaining quality, incremental improvements. Metrics focus on retention and efficiency. |
| **Sunset** | A product or capability being deliberately wound down — migrating users, decommissioning infrastructure, archiving knowledge. Metrics focus on migration completion. |

## Prioritization and Assessment

| Term | Definition |
|------|-----------|
| **Balanced Breakthrough** | A prioritization framework that allocates investment across Run (keep the lights on), Improve (incremental gains), and Transform (step-change bets). Allocation ratios shift by lifecycle stage — a Grow product invests differently than a Manage product. Prevents both stagnation and overreach. |
| **Run / Improve / Transform** | The three investment categories within Balanced Breakthrough. Run = operational maintenance. Improve = incremental enhancements. Transform = breakthrough bets that change the trajectory. Every initiative should be labeled, and totals should match the intended allocation. |
| **Harvey Balls** | Visual indicators (empty, quarter, half, three-quarter, full circles) used to show maturity, capability, or completion levels in assessment matrices. Quick visual comparison across dimensions. |
| **Gearing Ratio** | The ratio of effort invested to value produced. Used to evaluate efficiency of initiatives — high gearing means small effort, large impact. |
| **Health Model** | A structured assessment of a product or team's health across defined dimensions (e.g., customer satisfaction, technical debt, team engagement, delivery velocity). Usually scored and visualized. |
| **Scoring Rubric** | A structured matrix that defines what "good" looks like across multiple dimensions, with explicit criteria for each score level. Turns subjective assessment into consistent, transparent evaluation. |
| **Assessment Dimensions** | The specific axes along which a product, team, or capability is evaluated. Examples: customer value, technical quality, strategic alignment, operational efficiency. Dimensions should be orthogonal — each measures something distinct. |
| **Maturity Model** | A leveled progression (typically 1–5) that describes capability stages from ad hoc to optimized. Each level has observable behaviors, not aspirational adjectives. Used to diagnose current state and define growth targets. |
| **Force-Rank** | Creating a strict priority order with no ties. When scores are close, use a tiebreaker — usually strategic alignment. Prevents the "everything is P1" trap. |

## Strategy

| Term | Definition |
|------|-----------|
| **Strategic Diagnosis** | Understanding the current situation clearly enough to identify the core challenge. Rumelt's first layer of the strategy kernel. Maps business pressures, technology trends, competitive dynamics, and organizational constraints. |
| **Crux** | The single most important challenge or opportunity. Rumelt's test: if you solve this, does everything else become easier? If not, you haven't found the crux. |
| **Guiding Policy** | The chosen strategic approach — the "how" of the strategy. Not a goal or aspiration, but a method for dealing with the crux. Rumelt's middle layer. |
| **Coherent Actions** | Individual initiatives that reinforce each other and execute the guiding policy. Actions should be mutually supporting — incoherent actions are the hallmark of bad strategy. Rumelt's third layer. |
| **Strategic Themes** | 3–5 areas of focused investment that together execute strategy. Each theme should map to specific product or capability investments. |
| **Guardrails** | What you explicitly are NOT doing. Negative space that defines strategy as much as positive choices. If everything is in scope, nothing is prioritized. |

## Product Work

| Term | Definition |
|------|-----------|
| **Opportunity Solution Tree** | A visual framework (Teresa Torres) that maps desired outcomes to opportunities to solutions to experiments. Keeps work connected to outcomes rather than drifting into feature factories. |
| **Empowered Team** | A team given problems to solve, not features to build (Marty Cagan). Has the autonomy, context, and capability to discover and deliver solutions. |
| **Continuous Discovery** | The practice of maintaining ongoing contact with customers and the market, rather than doing discovery as a one-time phase. Weekly touchpoints, regular assumption testing. |
| **Assumption Map** | A listing of current assumptions about users, market, or technology, each rated by confidence (high/medium/low) and impact. The low-confidence, high-impact assumptions get tested first. |
| **Behavioral Evidence** | What people actually do, as opposed to what they say they would do. The gold standard for discovery insights. Interview data is a starting point; observed behavior is proof. |
| **Context Engineering** | The practice of structuring information so that AI assistants have the right context to be effective. Document architecture, state management, and vocabulary alignment. |

## Agile at Scale

Generic concepts. The work persona may extend these with organization-specific terminology, ceremonies, and adaptations.

### Organizational Levels & Work Hierarchy

| Term | Definition |
|------|-----------|
| **Business Unit** | The highest organizational level. Sets strategic direction via OKRs. Contains one or more Solution Trains. Maps to a Product Domain in Team Topologies terms. |
| **Solution Train** | Coordinates multiple ARTs to build large, complex solutions. Owns solution-level epics and OKRs. Maps to a Product Segment in Team Topologies terms. |
| **Agile Release Train (ART)** | A long-lived team of agile teams (typically 50–125 people) that plans, commits, and executes together around a value stream. Owns ART-level OKRs. Contains stream-aligned, platform, enabling, and complicated subsystem teams. |
| **Team** | The delivery unit. Supports both kanban and scrum, with a preference for scrum when planning rigor is needed. Team types follow Team Topologies: stream-aligned (primary), platform, enabling, complicated subsystem. |
| **Initiative** | Portfolio-level work item. The largest unit of strategic investment, spanning multiple solutions or ARTs. |
| **Portfolio Epic** | Portfolio-level work item. A strategic initiative requiring a Lean Business Case. Managed on the portfolio kanban. Spans multiple solutions or ARTs. |
| **Solution Epic** | Solution-level work item. A large body of work that spans multiple PIs or teams within a solution train. Breaks down from portfolio epics or originates within a solution. |
| **Feature** | ART-level work item. A service or capability that fulfills a stakeholder need. Sized to fit within a single PI. |
| **Story** | Team-level work item. A small, user-valued increment of functionality. Peer to Task, Spike, Test, and Bug. |
| **Task** | Team-level work item. A discrete piece of technical or operational work. Peer to Story, Spike, Test, and Bug. |
| **Spike** | Team-level work item. A timeboxed investigation to reduce uncertainty — research, prototype, or feasibility proof. Peer to Story, Task, Test, and Bug. |
| **Test** | Team-level work item. Validates acceptance criteria or system behavior. Can be manual or automated. Peer to Story, Task, Spike, and Bug. |
| **Bug** | Team-level work item. A defect in existing functionality. Tracked separately to maintain visibility into quality trends. Peer to Story, Task, Spike, and Test. |
| **Sub-Task** | Breakdown of any team-level work item (Story, Task, Spike, Test, or Bug) into smaller implementation steps. |
| **Enabler** | Work that builds infrastructure or technical foundation. Exists at every level — epic, feature, story. Without enablers, teams accumulate technical debt. |
| **Risk** | A potential future problem that could impact delivery. Used for external dependencies or anything that could cause material change to the plan. Tracked and mitigated proactively. |
| **Issue** | An active problem impacting delivery now. Distinguished from risk (which is future-facing). Requires resolution, not just tracking. |
| **Decision** | A recorded choice with context and rationale. Captured alongside risks and issues to maintain a clear decision trail. |
| **Dependency** | A relationship between two bodies of work where one blocks or constrains the other. Internal dependencies link work items directly. External dependencies or material plan risks are tracked as risks or issues. |

### Ceremonies (at Business Unit, Solution, and ART levels)

| Term | Definition |
|------|-----------|
| **Standup** | A short, regular sync to surface blockers and coordinate work. Cadence and scope scale by level — team daily, ART weekly, solution as needed. |
| **Demo** | A demonstration of completed work to stakeholders. Team demos show iteration output. ART system demos show integrated work. Solution demos show cross-train capability. |
| **Retrospective** | A structured look-back to identify what worked, what didn't, and what to change. Runs at every level after each timebox completes. |
| **Review** | A planning and alignment ceremony to assess progress against objectives, adjust priorities, and confirm direction. Distinct from demo (which shows work) — review evaluates trajectory. |
| **Program Increment (PI)** | A timebox (typically 8–12 weeks) during which teams plan, execute, and deliver value together. Creates a shared cadence across multiple teams. The planning event aligns teams on objectives, dependencies, and risks. |
| **PI Objectives** | The business and technical goals a team commits to during PI planning. Committed objectives are high-confidence. Uncommitted (stretch) objectives are aspirational. The contract between teams and stakeholders for the increment. |
| **Iteration** | A short, fixed timebox (typically 2 weeks) for planning, building, and demonstrating working increments. The heartbeat of agile delivery. |
| **Inspect and Adapt** | A structured retrospective at the end of each PI that combines quantitative review (metrics), qualitative review (what happened), and problem-solving (what to change). The mechanism for continuous improvement at scale. |

### Governance & Flow

| Term | Definition |
|------|-----------|
| **OKRs (Objectives and Key Results)** | Goal-setting framework used at Business Unit, Solution, and ART levels. Objectives define what to achieve. Key Results define how to measure it. Cascades alignment without prescribing how teams deliver. |
| **Value Stream** | The sequence of steps — from concept to cash — that delivers value to a customer. Organizing around value streams (rather than projects or functions) reduces handoffs and improves flow. |
| **WSJF (Weighted Shortest Job First)** | A prioritization method that divides Cost of Delay (user/business value + time criticality + risk reduction) by job size. Higher WSJF = do first. The economic framework for sequencing work. |
| **Lean Portfolio Management (LPM)** | Applying lean and systems thinking to strategy, investment funding, and governance. Replaces annual project-based budgeting with continuous, value-stream-based funding. Operates through portfolio vision, lean budgets, and portfolio kanban. |
| **Portfolio Kanban** | A visual system for managing the flow of epics from ideation through analysis, implementation, and completion. Makes WIP visible, limits overload, and creates a pull-based system for strategic initiatives. |
| **Lean Budget Guardrails** | Financial boundaries that define how much each value stream or ART can spend without additional approval. Empowers decentralized decision-making while maintaining fiduciary control. |
| **Flow Metrics** | Measures of delivery health: flow distribution (what types of work), flow velocity (how much), flow time (how fast), flow load (how much WIP), flow efficiency (active vs. wait time). The quantitative view of how well value moves through the system. |
| **Cost of Delay** | The economic impact of not delivering something now. Combines user-business value, time criticality, and risk reduction/opportunity enablement. Makes prioritization discussions about economics, not opinions. |

## Execution

| Term | Definition |
|------|-----------|
| **Wave / Sprint** | A timeboxed grouping of work. A wave is a logical grouping of tasks that can run in parallel and must complete before the next wave starts. A sprint is a fixed-length iteration (typically 2 weeks) used in scrum. Both create natural checkpoints for progress review. |
| **Checkpoint / Milestone** | A review point between waves or sprints to assess progress, surface blockers, and confirm readiness to proceed. Not a status meeting — a decision point. Milestones mark significant achievements or phase boundaries. |
| **Definition of Ready** | Clear criteria a work item must meet before a team pulls it into a sprint or wave. Ensures work is sufficiently understood, scoped, and unblocked before commitment. Prevents waste from starting work that isn't ready. |
| **Definition of Done** | Clear, testable exit criteria for completing a task. If you can't verify it's done, it's not a definition — it's a wish. |
| **Acceptance Criteria** | Testable conditions that define when a requirement is met. Written from the user's perspective. Each criterion is independently verifiable. |

## Stakeholder Navigation

| Term | Definition |
|------|-----------|
| **Stakeholder Map** | A matrix capturing authority, influence, interest, position, and motivation for each stakeholder. The diagnostic tool before any engagement strategy. |
| **Engagement Sequence** | The planned order of stakeholder outreach: validate with trusted allies → build coalition → preview with skeptics → engage decision-makers → present broadly. Sequence matters more than content. |
| **Breadcrumb Trails** | Small, low-risk exposures before the main ask. Planting ideas early so the formal proposal isn't the first time someone hears it. |
| **Resistance Patterns** | Common objection types and their underlying concerns. Surface-level pushback often masks deeper issues — resource anxiety, territory protection, change fatigue. |

## Executive Communication

| Term | Definition |
|------|-----------|
| **BLUF** | Bottom Line Up Front. State the recommendation or answer first, then support with detail. The default structure for executive communication. |
| **Narrative Arc** | The structure of an executive story: situation (where we are), tension (why that's a problem), resolution (what we're doing about it). Every deck, memo, or brief should follow this arc. |
| **Depth to Brevity** | The translation skill of compressing deep analysis into executive-ready language. The depth informs the brevity — you can't compress what you don't understand. |

## Organizational

| Term | Definition |
|------|-----------|
| **Transformation Enablement** | A function focused on improving how the organization does product work — building tools, frameworks, training, and assessment systems that change behavior at scale. |
| **Product Leadership Tooling** | Internal applications and frameworks that help product leaders do their jobs better — maturity assessments, prioritization tools, health dashboards, coaching rubrics. |
| **Working Demo** | A functional prototype or application that demonstrates a concept by doing it, not describing it. The default communication artifact in my work. |
| **Self-Running Artifact** | A tool or demo that demonstrates a concept without requiring a presenter. The artifact does the communicating — open it, use it, understand it. Jay's preferred delivery format. |
| **Operationalize** | Turning a conceptual framework into something teams can actually use — a tool, a process, a scored assessment. The bridge between theory and practice. |
| **Encode Expertise** | Embedding a methodology or decision framework into a reusable system — a rubric, a scoring model, an interactive tool — so it scales beyond the person who created it. |
