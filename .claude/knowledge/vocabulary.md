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
| **Interaction Modes** | How teams work together: collaboration (working closely), X-as-a-Service (consuming via API/contract), or facilitating (coaching/enabling). |

## Lifecycle Stages

| Term | Definition |
|------|-----------|
| **Grow** | A product or capability in its growth phase — actively acquiring users, expanding features, investing heavily. Metrics focus on adoption and engagement. |
| **Mature** | A product or capability that has reached steady state — optimizing efficiency, maintaining quality, incremental improvements. Metrics focus on retention and efficiency. |
| **Manage** | A product or capability in maintenance mode — minimal investment, sustaining operations, managing technical debt. Metrics focus on cost and stability. |
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
| **HiPPO** | Highest Paid Person's Opinion. The anti-pattern where prioritization defaults to executive preference instead of structured criteria. Frameworks exist to counter this. |

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
| **Feature Factory** | Anti-pattern where teams output features without validating outcomes. Measures success by delivery volume rather than customer or business impact. |
| **Continuous Discovery** | The practice of maintaining ongoing contact with customers and the market, rather than doing discovery as a one-time phase. Weekly touchpoints, regular assumption testing. |
| **Assumption Map** | A listing of current assumptions about users, market, or technology, each rated by confidence (high/medium/low) and impact. The low-confidence, high-impact assumptions get tested first. |
| **Behavioral Evidence** | What people actually do, as opposed to what they say they would do. The gold standard for discovery insights. Interview data is a starting point; observed behavior is proof. |
| **Context Engineering** | The practice of structuring information so that AI assistants have the right context to be effective. Document architecture, state management, and vocabulary alignment. |

## Agile at Scale

Generic concepts. The work persona may extend these with organization-specific terminology, ceremonies, and adaptations.

| Term | Definition |
|------|-----------|
| **Program Increment (PI)** | A timebox (typically 8–12 weeks) during which teams plan, execute, and deliver value together. Creates a shared cadence across multiple teams. The planning event aligns teams on objectives, dependencies, and risks. |
| **PI Objectives** | The business and technical goals a team commits to during PI planning. Committed objectives are high-confidence. Uncommitted (stretch) objectives are aspirational. The contract between teams and stakeholders for the increment. |
| **Agile Release Train (ART)** | A long-lived team of agile teams that plans, commits, and executes together. Typically 50–125 people organized around a value stream. The organizational unit that makes cross-team coordination predictable. |
| **Solution Train** | Coordinates multiple ARTs and suppliers to build large, complex solutions. Adds a layer of alignment above the ART when the solution scope exceeds what one train can deliver. |
| **Value Stream** | The sequence of steps — from concept to cash — that delivers value to a customer. Organizing around value streams (rather than projects or functions) reduces handoffs and improves flow. |
| **Iteration** | A short, fixed timebox (typically 2 weeks) for planning, building, and demonstrating working increments. The heartbeat of agile delivery. |
| **Innovation and Planning (IP) Iteration** | A dedicated iteration at the end of each PI for innovation, continuing education, PI planning prep, and technical debt reduction. The slack that makes sustained pace possible. Not a buffer for unfinished work. |
| **System Demo** | A regular demonstration of the integrated work from all teams on the ART. Proves the system works end-to-end, not just team-by-team. The real integration test. |
| **Inspect and Adapt** | A structured retrospective at the end of each PI that combines quantitative review (metrics), qualitative review (what happened), and problem-solving (what to change). The mechanism for continuous improvement at scale. |
| **Epic** | A large initiative that spans multiple PIs or teams. Requires a Lean Business Case to justify investment. Managed on the portfolio kanban. The unit of strategic investment. |
| **Feature** | A service or capability that fulfills a stakeholder need. Sized to fit within a single PI. The primary unit of planning and delivery for an ART. |
| **Enabler** | Work that builds the architectural runway, infrastructure, or technical foundation needed to support future features. Enablers exist at every level — epic, feature, story. Without them, teams accumulate technical debt. |
| **WSJF (Weighted Shortest Job First)** | A prioritization method that divides Cost of Delay (user/business value + time criticality + risk reduction) by job size. Higher WSJF = do first. The economic framework for sequencing work. |
| **Lean Portfolio Management (LPM)** | Applying lean and systems thinking to strategy, investment funding, and governance. Replaces annual project-based budgeting with continuous, value-stream-based funding. Operates through portfolio vision, lean budgets, and portfolio kanban. |
| **Portfolio Kanban** | A visual system for managing the flow of epics from ideation through analysis, implementation, and completion. Makes WIP visible, limits overload, and creates a pull-based system for strategic initiatives. |
| **Lean Budget Guardrails** | Financial boundaries that define how much each value stream or ART can spend without additional approval. Empowers decentralized decision-making while maintaining fiduciary control. |
| **Architectural Runway** | The existing technical infrastructure and architecture that enables near-term features without excessive redesign. Intentionally built ahead of need by enabler work. When the runway runs out, feature delivery stalls. |
| **Flow Metrics** | Measures of delivery health: flow distribution (what types of work), flow velocity (how much), flow time (how fast), flow load (how much WIP), flow efficiency (active vs. wait time). The quantitative view of how well value moves through the system. |
| **Cost of Delay** | The economic impact of not delivering something now. Combines user-business value, time criticality, and risk reduction/opportunity enablement. The numerator in WSJF. Makes prioritization discussions about economics, not opinions. |

## Execution

| Term | Definition |
|------|-----------|
| **Wave** | A logical grouping of tasks that can run in parallel and must complete before the next wave starts. Waves create natural checkpoints for progress review. |
| **Checkpoint** | A review point between waves to assess progress, surface blockers, and confirm readiness to proceed. Not a status meeting — a decision point. |
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
