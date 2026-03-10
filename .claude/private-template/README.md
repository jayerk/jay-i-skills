# Private Context Repository

## Purpose

This is the **private layer** of a two-repo personal operating system. It contains organization-specific context that should never be public: stakeholder maps, initiative details, internal dynamics, and project-specific information.

The **public layer** ([jay-i-skills](../README.md)) provides skills, frameworks, templates, and knowledge. This private repo provides the specific context those tools operate on.

## Structure

```
private-repo/
├── README.md              # This file — repo overview and usage
├── context/               # Organizational context documents
│   ├── README.md          # How to use the context directory
│   └── [initiative-name]/ # One folder per active initiative
│       ├── CONTEXT.md     # Context document (use CONTEXT-TEMPLATE.md)
│       ├── PLAN.md        # Plan document (use PLAN-TEMPLATE.md)
│       └── SUMMARY.md     # Completion summary (use SUMMARY-TEMPLATE.md)
├── stakeholders/          # Stakeholder maps and influence strategies
│   ├── README.md          # How to use stakeholder files
│   └── [initiative].md    # One stakeholder map per initiative
└── initiatives/           # Active initiative tracking
    ├── README.md          # How to use initiative files
    └── [initiative].md    # One file per active initiative
```

## How to Use

### Starting a New Initiative
1. Create a folder in `context/[initiative-name]/`
2. Copy `CONTEXT-TEMPLATE.md` from the public repo and fill it in
3. Create a stakeholder map in `stakeholders/[initiative].md`
4. Create an initiative tracker in `initiatives/[initiative].md`

### During Work
1. Reference these files alongside the skills and frameworks in the public repo
2. Update stakeholder maps as positions change
3. Keep initiative trackers current with status and decisions

### After Completing Work
1. Write a summary using `SUMMARY-TEMPLATE.md`
2. Archive completed initiatives (move to an `archive/` folder)
3. Update stakeholder maps to reflect outcomes

## Security

This repo should be:
- Private (never public)
- Not shared beyond your direct use
- Free of credentials, passwords, or system access details
- Focused on strategic and organizational context, not technical secrets

## Connection to Public Repo

The public repo provides:
- **Skills** that define how to work
- **Frameworks** that define the process
- **Templates** that define the document structure
- **Knowledge** that defines the vocabulary and principles

This private repo provides:
- **Context** about the specific situation
- **Stakeholders** involved in the work
- **Initiatives** being executed

Together, they give an AI assistant everything needed to operate as an effective extension of your thinking.
