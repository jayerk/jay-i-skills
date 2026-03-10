# Initiatives Directory

## Purpose

This directory tracks active initiatives at a summary level — status, key milestones, and links to detailed context and plans. It provides a quick portfolio view of what's in flight.

## How to Use

1. Create one file per active initiative: `[initiative-name].md`
2. Keep it concise — this is the summary view, not the detail
3. Link to the detailed context and plan documents in `context/`
4. Update status weekly or after significant milestones

## Template

```markdown
# Initiative: [Name]

## Summary
[One paragraph: what this is and why it matters]

## Status
- **Phase:** [Discovery / Strategy / Planning / Executing / Verifying / Complete]
- **Health:** [On Track / At Risk / Blocked]
- **Last updated:** [Date]

## Key Dates
| Milestone | Target | Actual | Status |
|-----------|--------|--------|--------|
| [Milestone] | [Date] | [Date] | [Done/On Track/At Risk/Missed] |

## Links
- Context: `context/[initiative-name]/CONTEXT.md`
- Plan: `context/[initiative-name]/PLAN.md`
- Stakeholder map: `stakeholders/[initiative-name].md`

## Current Focus
[What's being worked on right now — 2-3 sentences]

## Key Risks
| Risk | Status | Mitigation |
|------|--------|-----------|
| [Risk] | [Active/Monitoring/Resolved] | [Action] |

## Recent Decisions
| Decision | Date | Impact |
|----------|------|--------|
| [What was decided] | [When] | [What it changes] |

## Next Actions
- [ ] [Action 1] — [Owner] — [Due]
- [ ] [Action 2] — [Owner] — [Due]
```

## Portfolio View

To get a quick view of all initiatives, scan the Status section of each file:
- **Discovery** — learning about the problem
- **Strategy** — deciding the approach
- **Planning** — breaking work into executable tasks
- **Executing** — doing the work
- **Verifying** — confirming quality and completeness
- **Complete** — done, move to archive

## Lifecycle

- **Active:** File in `initiatives/`. Being worked on.
- **Complete:** Write final status update, then move to `initiatives/archive/`.
- **Paused:** Add `[PAUSED]` prefix to filename. Capture pause reason and resume criteria in the file.
