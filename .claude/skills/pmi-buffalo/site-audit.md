# site-audit

Crawl and audit the public-facing PMI Buffalo chapter website, producing a
structured findings report with flagged issues and recommended actions for
human review.

TRIGGER when: user asks to audit, crawl, review, or assess the public PMI
Buffalo website — including requests to find outdated content, check for
issues, or produce a content inventory of the live site.

DO NOT TRIGGER when: user is reviewing internal documents, board materials,
member communications, or any content that has not yet been published to the
public site. For internal content review, use the internal-audit skill instead.

---

## Setup: What to Confirm Before Starting

Ask the user to provide anything missing:

**Required:**
- Base URL of the public website (e.g., `https://pmibuffalo.org`)
- Audit scope: full site, specific section (e.g., `/events`, `/about`), or
  a list of specific page URLs

**Optional but valuable:**
- Known problem areas to prioritize (e.g., "the events page is outdated")
- Last audit date, if any
- Any pages that are intentionally static and do not need review

If no scope is provided, default to a full site crawl starting from the base URL.

---

## Phase 1 — Crawl: Discover and Extract

1. Starting from the provided base URL, crawl all reachable public pages
   within the same domain. Do not follow external links off-domain.

2. For each page discovered, record:
   - **URL** — full path
   - **Page title** — as it appears in the `<title>` tag or `<h1>`
   - **Last-modified date** — from HTTP headers or visible on-page date if
     present; record "not detected" if absent
   - **Content summary** — 1–2 sentence description of what the page contains
   - **Key dates mentioned** — any event dates, deadlines, or year references
     found in the body text

3. Build a flat page inventory table before proceeding to analysis. Do not
   skip pages because they appear unimportant — include everything crawled.

4. Note any pages that returned errors (404, redirect loops, access denied)
   in a separate error log.

---

## Phase 2 — Flag: Issue Detection

For each page in the inventory, check for the following issue categories.
Apply every check to every page — do not skip checks for pages that appear
"clean."

### Category A — Stale Content
- Any event, meeting, webinar, or activity with a date in the past that is
  still presented as upcoming or current
- Any reference to a board member, officer, or volunteer by name or role that
  may have changed
- Any year reference (e.g., "2023 Annual Report," "Join us in 2024") that is
  more than one year old relative to today's date (today: 2026-03-07)
- Any "coming soon" or "under construction" language that has been present
  for more than 6 months (infer from context if date unavailable)

### Category B — PMI Certification / Standards Content
- Any page that describes PMP exam requirements, eligibility criteria,
  application processes, or PDU audit procedures
- Any page that quotes or paraphrases PMI standards (PMBOK, PMTQ, etc.)
  without an explicit attribution link back to the PMI.org source
- Any page that could be interpreted as offering certification advice or
  guaranteeing exam outcomes

  **Flag these as HIGH PRIORITY regardless of how minor they appear.**
  Do not attempt to correct this content — flag only.

### Category C — PII and Sensitive Data
- Any page that displays member names, email addresses, phone numbers, or
  mailing addresses in plain text without a login gate
- Any volunteer roster, committee list, or contact directory that is
  publicly accessible
- Any form that collects personal data where the destination or handling
  is unclear

  **Flag these as HIGH PRIORITY.** Do not reproduce the PII in the audit
  report — note the URL and field type only.

### Category D — Broken Patterns
- Navigation links that point to pages that returned errors in Phase 1
- Images with missing alt text (flag page, not individual image)
- Pages with no visible last-updated date and content that appears time-sensitive
- Duplicate content — two or more pages covering the same topic with
  conflicting information

### Category E — DE&I and Tone
- Any language that could be exclusionary, stereotyping, or that fails to
  reflect the diversity of the WNY professional community
- Any imagery descriptions or alt text that skew representation in a
  non-inclusive direction (flag the page; do not describe the images in detail)
- Any content that implicitly assumes a single professional profile
  (e.g., assumes all members are corporate employees, or all in one industry)

---

## Phase 3 — Report: Structured Audit Output

Produce the audit report in the following structure. Do not omit sections
even if they have no findings — write "No issues found in this category."

---

### Audit Header

```
PMI Buffalo — External Site Audit
Audit date: [today's date]
Base URL audited: [URL]
Scope: [full site / section / specific pages]
Pages crawled: [count]
Pages with errors: [count]
Total issues flagged: [count by category]
```

---

### Section 1 — Page Inventory

A table of all pages crawled:

| URL | Page Title | Last Modified | Summary |
|-----|-----------|---------------|---------|
| ... | ... | ... | ... |

---

### Section 2 — Issue Log

All flagged issues grouped by category. Within each category, sort by
priority: HIGH first, then MEDIUM, then LOW.

For each issue:

```
[PRIORITY] Category: [A/B/C/D/E — Category Name]
URL: [page URL]
Issue: [one sentence describing what was found]
Recommended action: [specific, actionable instruction for the human reviewer]
```

Priority definitions:
- **HIGH** — content that is incorrect, potentially harmful, legally or
  policy-sensitive, or exposes PII. Requires immediate human action before
  the next site visitor encounters it.
- **MEDIUM** — content that is outdated or misleading but not immediately
  harmful. Should be corrected in the next site update cycle.
- **LOW** — minor inconsistencies, style issues, or missing enhancements
  that improve quality but are not urgent.

---

### Section 3 — Error Log

Pages that could not be retrieved, with URL and error type.

---

### Section 4 — Summary Recommendations

#### 4A — Site-Only Actions

Provide exactly 3–5 prioritized recommendations based solely on what this
audit found. These are self-contained — a volunteer can act on them without
any other context. Sequence by impact and urgency, not by issue category.

1. **[Recommendation title]** — [2–3 sentences: what to fix, why it matters,
   suggested owner or next step]

#### 4B — Strategic Benchmarking Linkage

Review the site audit findings for signals that connect to chapter-level
strategy. If a `strategic-benchmark` analysis exists or is available, cross-
reference it here. If not, note which findings warrant input from that skill
before the board acts.

For each strategic linkage identified:

```
Site finding: [what the audit found — e.g., "Events page shows low activity, 3 of 5 events are past-dated with no new ones listed"]
Strategic question: [what this raises at the chapter level — e.g., "Is low event volume a content problem or a programming problem? Benchmark data would clarify."]
Recommended handoff: [run strategic-benchmark / cross-reference existing benchmark / flag for board discussion]
```

If no strategic linkages are apparent, write: "No cross-references to
strategic benchmark identified in this audit cycle."

This section is intentionally not a full strategic analysis — it is a bridge.
The `strategic-benchmark` skill owns that work.

---

### Section 5 — Audit Trail (Required)

```
Audit produced by: AI assistant (PMI Buffalo site-audit skill)
Reviewed and approved by: [human reviewer name — to be completed before use]
DE&I review completed: [ ] Yes  [ ] No
PMI certification content check: [ ] Confirmed none present  [ ] Flagged items present — see Section 2, Category B
PII check: [ ] Confirmed none present  [ ] Flagged items present — see Section 2, Category C
AI-assisted audit noted in internal log: [ ] Yes
```

This section must be completed by the human reviewer before the audit report
is shared with the board or used to drive site changes.

---

## Output Format

Deliver all five sections in order. The Issue Log (Section 2) is the
operational core of this audit — write it with enough specificity that a
volunteer unfamiliar with the page can find and fix the issue without
additional context.

Do not summarize or abbreviate flagged issues to save space. If there are
many issues, report them all. The value of this skill is completeness and
consistency — every run should produce an audit that can stand on its own
as a dated record.
