---
name: prd-writing
description: "Product requirements documents and specifications — PRDs, feature specs, product documentation. Use this skill when defining what to build, for whom, and why, with enough detail for engineering to execute."
---

# PRD Writing

## Overview

This skill covers the creation of product requirements documents — the artifacts that bridge strategy and execution. A good PRD is not a feature list; it's a communication tool that gives an empowered team the context they need to build the right thing. It defines the outcome, the constraints, and the acceptance criteria, then trusts the team to find the best solution.

## When to Use This Skill

- Writing a PRD for a new product or feature
- Documenting requirements for an internal tool
- Specifying an API, integration, or system change
- Creating acceptance criteria for a user story or epic
- Writing technical specifications that engineering teams will implement

## Quality Bar

- **Outcome-focused** — the PRD defines the problem and desired outcome before discussing solutions. Teams need the "why" to make good implementation decisions.
- **Specific enough to estimate** — engineering should be able to read the PRD and produce a rough estimate without a follow-up meeting.
- **Flexible enough to empower** — define what success looks like, not how to achieve it. Unless there are genuine constraints (regulatory, technical, integration), leave implementation to the team.
- **Testable** — every requirement has clear acceptance criteria. If you can't test it, you haven't defined it.
- **Scoped** — explicitly states what's in v1, what's deferred, and what's explicitly out of scope.

## Process

### Step 1: Define the Problem
Before writing requirements, establish:
- Who has this problem? (User persona or team type)
- What pain are they experiencing? (Observable behavior, not assumed)
- How do they solve it today? (Current workaround or process)
- What's the cost of the status quo? (Time, errors, friction, missed opportunities)
- What evidence do we have? (Customer interviews, data, support tickets, observation)

### Step 2: Articulate the Desired Outcome
- What does success look like for the user?
- What business metric does this move?
- How will we measure whether we've solved the problem?
- What's the minimum outcome that would justify the investment?

### Step 3: Define the Scope
- **In scope (v1):** The minimum set of capabilities needed to achieve the desired outcome
- **Deferred (v2+):** Capabilities that are valuable but not essential for the initial release
- **Out of scope:** Things this initiative explicitly does not address (and why)

### Step 4: Write the Requirements
For each requirement:
- **User story format:** As a [persona], I need to [action], so that [outcome]
- **Acceptance criteria:** Given [context], when [action], then [expected result]
- **Edge cases:** What happens when [unusual scenario]?
- **Constraints:** Regulatory, technical, or integration requirements that limit solution options

### Step 5: Include Supporting Context
- **User flows** — how does the user move through the experience?
- **Data model** — what entities exist, how do they relate?
- **Integration points** — what systems does this touch?
- **Non-functional requirements** — performance, security, accessibility, compliance

### Step 6: Review and Validate
- Can engineering estimate this without a follow-up meeting?
- Are there ambiguous requirements that could be interpreted multiple ways?
- Do the acceptance criteria cover the happy path and key edge cases?
- Is the scope achievable given known constraints?
- Does the PRD connect back to the strategic context?

## Output Format

```markdown
# PRD: [Feature/Product Name]

## Meta
- **Author:** [Name]
- **Date:** [Date]
- **Status:** Draft | In Review | Approved
- **Team:** [Stream-aligned team or squad]

## Problem Statement
[2-3 paragraphs: who has this problem, what pain they experience, what the cost of inaction is]

## Desired Outcome
[What success looks like, how we'll measure it]

## User Personas
| Persona | Description | Primary Need |
|---------|-------------|-------------|
| [Name] | [Role/context] | [What they need from this] |

## Scope

### In Scope (v1)
- [Requirement 1]
- [Requirement 2]

### Deferred (v2+)
- [Requirement] — [Why deferred]

### Out of Scope
- [Item] — [Why excluded]

## Requirements

### [Requirement Group 1]

**User Story:** As a [persona], I need to [action], so that [outcome].

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]

**Edge Cases:**
- [Scenario]: [Expected behavior]

### [Requirement Group 2]
...

## User Flows
[Description or diagram of key user journeys]

## Non-Functional Requirements
- **Performance:** [Specific targets]
- **Security:** [Requirements, especially for regulated environment]
- **Accessibility:** [Standards to meet]
- **Compliance:** [Regulatory requirements]

## Dependencies
- [System/team]: [What we need from them]

## Open Questions
- [ ] [Question needing resolution]

## Appendix
[Supporting research, data, or technical detail]
```

## Anti-Patterns

- **Solution-first PRDs** — jumping to UI mockups before defining the problem. The mockup isn't the requirement; the outcome is.
- **Infinite scope** — PRDs that try to solve everything. v1 should be the smallest thing that delivers the outcome. Everything else is v2.
- **Vague acceptance criteria** — "The system should be fast" is not testable. "Page load under 2 seconds on standard internal network" is.
- **Missing the "why"** — requirements without strategic context. Engineering needs to understand why this matters to make good tradeoff decisions.
- **Spec-as-contract** — treating the PRD as a rigid contract rather than a communication tool. Requirements should be clear but allow room for the team to find better solutions.
