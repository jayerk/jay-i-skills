# Skill Catalog

Complete inventory of skills — implemented and planned — across all contexts.
For the full backlog with phased priorities, see [BACKLOG.md](../../BACKLOG.md).

---

## Meta (cross-context)

| Skill | Purpose | AC | Status |
|---|---|---|---|
| `repo-brief` | Read BACKLOG.md files across repos and produce a focused working session brief for the next task | Given a BACKLOG.md in any repo, produces a focused session brief for the next prioritized task | Implemented |
| `repo-init` | Generate a downstream repo's CLAUDE.md with the correct pointer section pre-filled | Given a new repo path and context name, produces a CLAUDE.md with correct pointer section pre-filled | Implemented |
| `writing-triage` | Post-generation quality gate — scans output for AI writing signals and corrects before delivery | Given any skill output, detects AI writing patterns and rewrites to correct them before delivery | Implemented |
| `codex-review` | Verification layer — hands off Claude's output to Codex CLI for independent review (Claude builds, Codex reviews) | Given code or structured output from Claude, produces scoped Codex CLI invocation command and processes review feedback | Implemented |

## PMI Buffalo

| Skill | Purpose | AC | Status |
|---|---|---|---|
| `strategic-benchmark` | Compare chapter metrics vs. peer chapters — 5-agent + Chief of Staff synthesis | Given a chapter name or dataset, produces multi-perspective benchmark report with synthesis | Implemented |
| `site-audit` | External public website crawl — flags stale content, PII, cert content, DE&I issues | Given chapter URL, produces dated audit log of content issues | Implemented |
| `monthly-bite-writer` | Write monthly newsletter content | Given topic and context, produces newsletter-ready content in PMI Buffalo voice | Implemented |
| `board-report` | Draft monthly/quarterly board update | Given recent chapter activity, produces board-ready update | Planned |
| `meeting-minutes` | Extract decisions & action items from board notes | Given raw board meeting notes, produces decisions and action items with owners and due dates | Planned |
| `annual-report-draft` | Compile end-of-year chapter summary for PMI Global | Given full-year chapter data, produces PMI Global-formatted annual summary | Planned |
| `email-draft` | Draft member-facing chapter communications | Given topic and audience, produces member-facing chapter email in PMI Buffalo voice | Planned |
| `newsletter-section` | Write event recaps, spotlights, announcements | Given event or spotlight topic, produces newsletter-ready section | Planned |
| `event-plan` | Produce checklist-driven event/PDU activity plan | Given event concept, produces checklist-driven plan with PDU structure and timeline | Planned |
| `pdu-tracker` | Structure PDU activity descriptions for PMI reporting | Given activity details, produces PMI-formatted PDU descriptions | Planned |
| `speaker-outreach` | Draft speaker invitation emails | Given speaker name and topic, produces personalized invitation email | Planned |
| `membership-analysis` | Narrative around membership trends and actions | Given membership data, produces trend narrative with recommended actions | Planned |
| `volunteer-brief` | Role-specific onboarding brief for new volunteers | Given role name, produces onboarding brief for new volunteers | Planned |
| `volunteer-of-the-quarter` | Run the volunteer-of-the-quarter selection and recognition process | Given nomination period, produces selection summary and recognition artifacts | Planned |
| `recognition-draft` | Awards, LinkedIn shoutouts, thank-you messages | Given volunteer or member name and contribution, produces recognition content | Planned |
| `sponsor-proposal` | Tiered sponsorship packages for WNY businesses | Given target business profile, produces tiered sponsorship package | Planned |
| `budget-review` | Narrative analysis of chapter budget vs. actuals | Given budget vs. actuals data, produces narrative analysis with flags | Planned |
| `internal-audit` | Internal content audit — board docs, communications, unpublished materials | Given board doc set, produces content audit with flags and recommendations | Planned |
| `help-desk-emails` | Draft responses to incoming chapter help desk emails | Given help desk email, produces on-brand response in PMI Buffalo voice | Planned |
| `community-content` | Chapter event content — talks, workshops, presentations, engagement strategies | Given event topic and format, produces talk outline, article, or workshop design in PMI Buffalo voice | Implemented |

## Personal

| Skill | Purpose | AC | Status |
|---|---|---|---|
| `soup-feast` | App design and process flow for ranked-choice voting app | Design docs and process flow for The Great Soup Feast | Implemented |
| `decision-matrix` | Structure a personal decision with pros/cons/criteria | Given a decision with options, produces weighted criteria matrix with recommendation | Planned |
| `research-brief` | Summarize research on a purchase, topic, or option | Given a topic or purchase, produces structured summary with sources | Planned |
| `weekly-review` | Guided weekly personal review and planning session with reMarkable delivery | Given week's activity, produces guided review with next-week priorities and sends to reMarkable | Planned |
| `trip-plan` | Build a practical travel itinerary from requirements | Given destination and constraints, produces day-by-day itinerary | Planned |
| `remarkable-food-digest` | Pull food content from email into magazine-format reMarkable document | Given food email inbox, produces magazine-format reMarkable document | Planned |
| `work-summarizer` | Structured daily/weekly digest of work activity | Given daily or weekly work activity, produces structured digest with highlights and next steps | Planned |
| `remarkable-extract` | Extract and process content from reMarkable documents | TBD — to be decomposed | Planned |

## Work

Eight work-mode skills, each corresponding to one of Jay's core work modes.
Each has a SKILL.md in `.claude/skills/work/<skill-name>/`.

| Skill | Work Mode | Status |
|---|---|---|
| `product-strategy` | Product strategy & vision | Implemented (review pending) |
| `internal-tooling` | Internal tools — HTML/React SPAs, dashboards, scoring tools | Implemented (review pending) |
| `executive-storytelling` | Executive presentations & decks | Implemented (review pending) |
| `prd-writing` | PRDs and product documentation | Implemented (review pending) |
| `coaching-frameworks` | Coaching & assessment frameworks | Implemented (review pending) |
| `community-content` | Community content (work-context, not PMI Buffalo) | Implemented (review pending) |
| `gap-analysis` | Gap analyses & backlog prioritization | Implemented (review pending) |
| `stakeholder-navigation` | Stakeholder navigation & influence | Implemented (review pending) |

### Additional Work Skills (Planned)

| Skill | Purpose | AC | Status |
|---|---|---|---|
| `status-update` | Draft a concise project or work status update | Given project context, produces concise status update with risks and next steps | Planned |
| `email-draft` | Draft professional workplace emails | Given topic and audience, produces professional email draft | Planned |
| `self-assessment` | Write performance self-assessment narratives | Given accomplishments and review period, produces performance narrative | Planned |
| `exec-summary` | Condense a document into an executive summary | Given source document, produces one-page executive summary | Planned |
| `slide-outline` | Structure a presentation from talking points | Given talking points and audience, produces structured slide deck outline | Planned |
| `planning-and-execution` | Planning and execution skill family (OKRs, decision briefs, stakeholder maps, etc.) | TBD — to be decomposed | Planned |
| `customer-market-research` | Customer and market research artifacts | TBD — to be decomposed | Planned |
| `value-management` | Value management artifacts | TBD — to be decomposed | Planned |
