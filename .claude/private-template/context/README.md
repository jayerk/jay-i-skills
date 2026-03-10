# Context Directory

## Purpose

This directory contains context documents for active initiatives. Each initiative gets its own folder with structured documents that capture the decisions, constraints, and environmental factors that shape the work.

## Structure

```
context/
├── README.md
└── [initiative-name]/
    ├── CONTEXT.md     # Decisions, constraints, and environmental context
    ├── PLAN.md        # Execution plan with phases, waves, and tasks
    └── SUMMARY.md     # Completion summary with outcomes and learnings
```

## How to Create a New Context

1. Create a folder named after the initiative (use kebab-case: `product-health-model`)
2. Copy `templates/CONTEXT-TEMPLATE.md` from the public jay-i-skills repo
3. Fill in all sections — the more thorough the context, the more effective AI assistance will be
4. Pay special attention to:
   - **Decisions** — capture what's been decided and what's still open
   - **Constraints** — especially regulatory and organizational constraints
   - **Assumptions** — with confidence levels and validation approaches

## Naming Convention

Use descriptive kebab-case names that match how you refer to the initiative:
- `product-health-model/`
- `pm-maturity-assessment/`
- `quarterly-prioritization-q2-2026/`
- `team-topology-redesign/`

## Lifecycle

1. **Active** — in the root of `context/`. Being actively worked on.
2. **Complete** — has a filled-in SUMMARY.md. Move to `context/archive/` after carry-forward items are captured.
3. **Abandoned** — write a brief note on why in the CONTEXT.md, then move to `context/archive/`.
