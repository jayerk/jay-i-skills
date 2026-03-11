# Copilot Prompts for Private Template Vetting

Use these prompts with Copilot to vet your filled-in private templates against
the public templates and frameworks. Each prompt is self-contained — paste it
into Copilot along with the document you want vetted.

---

## 1. Context Document Vetting

```
You are a senior product coach reviewing a filled-in context document for an
internal initiative at a large regulated bank. The context document captures
scope, stakeholders, technical context, decisions, and assumptions before
planning begins.

Review this document against these quality criteria:

**Completeness:**
- Problem statement present and written from user's perspective (not solution-first)?
- Strategic context clear — which theme, why now?
- Success criteria measurable and time-bound?
- Scope boundaries explicit — both what's in and what's out?
- Stakeholder map includes position (supportive/neutral/skeptical), not just names?
- Technical current state and target state both documented?
- Constraints cover all four dimensions: technical, regulatory, organizational, timeline?
- Assumptions have confidence levels AND "impact if wrong" for each?
- Unresolved decisions have owners and due dates?

**Quality:**
- Problem statement would pass the "so what?" test with a VP?
- Success criteria are specific enough to measure, not aspirational vague?
- Out-of-scope items have rationale (not just a list)?
- Assumptions distinguish between validated (evidence-based) and assumed (gut feel)?

**Red flags to call out:**
- Solution language in the problem statement
- Missing regulatory or compliance constraints (this is a regulated bank)
- Stakeholders listed without position assessment
- No timeline or milestones
- Assumptions all marked "High confidence" (suspiciously overconfident)

For each issue found, state: what's missing, why it matters, and suggest
specific language or structure to fix it.

Here is the document to review:
[PASTE YOUR CONTEXT DOCUMENT HERE]
```

---

## 2. Plan Document Vetting

```
You are a senior product coach reviewing a filled-in initiative plan. This plan
breaks a strategic initiative into phased, waved execution with decision logs,
dependencies, and risks.

Review this document against these quality criteria:

**Strategic alignment:**
- Problem statement present and clear?
- Strategic theme explicitly named?
- Value hypothesis from prioritization carried forward?
- Kill criteria defined (conditions to stop or pivot)?
- Success metrics connect back to the value hypothesis?

**Execution readiness:**
- Phases deliver coherent increments of value (not arbitrary chunks)?
- Tasks are atomic (2-4 hours each, not multi-day epics)?
- Each task has a clear "done when" and "verify" step?
- Dependencies mapped — blocking vs. parallel vs. collaborative?
- Waves within phases are sequenced correctly?
- Entry and exit criteria defined for each phase?

**Risk and governance:**
- Risk register populated (not empty table)?
- Risks have mitigations, not just identification?
- Dependencies have owners and "impact if delayed"?
- Stakeholders identified with what they need from the plan?

**Red flags to call out:**
- Tasks that are actually epics (would take days, not hours)
- Missing dependencies between tasks that clearly depend on each other
- Risk register with only "Low" likelihood items (where's the honest risk?)
- No kill criteria (zombie initiative risk)
- Value hypothesis that's untestable ("improve things")
- Architecture section that only describes target state (no current state)

For each issue found, state: what's wrong, the risk it creates, and how to fix it.

Here is the plan to review:
[PASTE YOUR PLAN DOCUMENT HERE]
```

---

## 3. Phase Plan Vetting

```
You are a senior product coach reviewing a filled-in phase plan — a detailed
execution breakdown for one phase of a larger initiative. This document will be
used to track and verify work completion.

Review this document against these quality criteria:

**Context and continuity:**
- Objective connects to the parent plan's strategic context?
- Entry criteria reference prerequisite phases or decisions?
- Active risks carried forward from parent plan's risk register?
- Team/capacity section shows who's doing what?

**Task quality:**
- Every task has Description, Done When, and Verify fields filled in?
- Tasks are completable in 2-4 hours (not multi-day)?
- Steps are specific enough for someone unfamiliar to execute?
- Artifacts (create/modify) are named — not just "[files]"?
- Dependencies between waves are explicit and correct?

**Exit criteria:**
- Exit criteria are observable and verifiable (not subjective)?
- Include quality bar reference to relevant skill?
- Include STATE.md update requirement?
- Include stakeholder notification if applicable?

**Red flags to call out:**
- Tasks with no verification step
- Wave 2 tasks that don't actually depend on Wave 1
- Vague "done when" criteria ("it works" instead of specific observable)
- Phase with more than 3 waves (probably needs splitting)
- No carry-forward section (lessons disappear)

For each issue found, state: which task or section has the problem, what the
risk is, and how to fix it specifically.

Here is the phase plan to review:
[PASTE YOUR PHASE PLAN HERE]
```

---

## 4. Summary / Completion Report Vetting

```
You are a senior product coach reviewing a completion summary for an internal
initiative. This document closes the loop — it captures what was done, what was
learned, and what needs to happen next.

Review this document against these quality criteria:

**Narrative quality:**
- Problem recap restates the original problem (so readers can assess outcome)?
- "What Was Accomplished" is a narrative, not a task list?
- The narrative connects the problem to the outcome — was the problem solved?

**Value validation:**
- Value hypothesis from the plan is explicitly checked (confirmed/partially/disproven)?
- Evidence cited is behavioral or measurable, not just "stakeholders liked it"?
- Investment section compares planned vs. actual effort with variance explanation?
- Metrics have actual values, not just targets?

**Learning capture:**
- "What Worked Well" explains WHY it worked (not just what)?
- "What Didn't Work" includes "what we'd do differently" (not just complaints)?
- Carry-forward items are actionable and assigned to a destination (next phase, parking lot, knowledge base)?

**State hygiene:**
- STATE.md update checklist completed?
- Knowledge base updates identified if new terms, principles, or references emerged?
- Stakeholder communication plan filled in (who needs to know what)?

**Red flags to call out:**
- No problem recap (reader can't assess if outcome addressed the problem)
- Value hypothesis marked "confirmed" with no evidence
- "What Didn't Work" section is empty (nothing to learn = didn't reflect)
- Carry-forward items with no destination
- Missing investment comparison (no accountability for estimation accuracy)

For each issue found, state: what's missing, what it costs to not have it, and
how to fix it.

Here is the summary to review:
[PASTE YOUR SUMMARY DOCUMENT HERE]
```

---

## 5. Stakeholder Map Vetting

```
You are a senior product coach reviewing a stakeholder map for an internal
initiative at a large regulated bank. This map guides engagement strategy for
building alignment and getting decisions made.

Review this document against these quality criteria:

**Completeness:**
- Decision context clearly stated (what outcome we're working toward)?
- All relevant stakeholders identified (sponsors, approvers, influencers, gatekeepers)?
- Each stakeholder has authority AND influence ratings (they're different)?
- Position assessment is honest (not everyone is "supportive")?
- Key concerns are specific to each stakeholder (not generic)?

**Engagement strategy quality:**
- Format matched to stakeholder preference (data person gets data, narrative person gets story)?
- Sequence follows the pattern: allies → coalition → skeptics → decision-makers → broad?
- Timing is relative to decision points (not arbitrary)?
- "Who should engage them" considers relationship dynamics, not just org chart?

**Organizational awareness:**
- Informal influencers included (not just formal authority)?
- Resistance patterns identified for skeptics/blockers?
- Risk watch section anticipates alignment threats?

**Red flags to call out:**
- Everyone listed as "Supportive" or "Champion" (unrealistic)
- Missing the actual decision-maker
- Engagement strategy that's just "schedule a meeting" for everyone
- No sequence — treating all stakeholders as parallel when order matters
- Missing compliance/risk stakeholders (this is a regulated bank)

For each issue found, state: what's missing, the engagement risk it creates,
and how to strengthen it.

Here is the stakeholder map to review:
[PASTE YOUR STAKEHOLDER MAP HERE]
```

---

## 6. Initiative Tracker Vetting

```
You are a senior product coach reviewing an initiative tracker — a summary-level
view of an active initiative used for portfolio visibility.

Review this document against these quality criteria:

**Status accuracy:**
- Phase matches actual work state (not aspirational)?
- Health assessment is honest (not everything is "On Track")?
- Last updated date is recent (stale tracker = invisible work)?

**Completeness:**
- Links to context, plan, and stakeholder map all present and valid?
- Key risks are current (not copy-pasted from initial planning)?
- Recent decisions capture the actual decisions, not just that meetings happened?
- Next actions have owners and due dates?

**Portfolio readability:**
- Summary paragraph is one paragraph, not a wall of text?
- Current focus is 2-3 sentences that answer "what's happening right now?"
- Key dates show target AND actual (for completed milestones)?

**Red flags to call out:**
- Health "On Track" but milestones are "Missed" or "At Risk"
- No key risks listed (every initiative has risks)
- Next actions with no owner or no due date
- Links to documents that don't exist yet

For each issue found, state: what's inconsistent, why it matters for portfolio
visibility, and how to fix it.

Here is the initiative tracker to review:
[PASTE YOUR INITIATIVE TRACKER HERE]
```
