# Feed — Product Requirements Document

> An automated pipeline that scans Gmail for food content, formats it into a magazine-style PDF, and sends it to the reMarkable for distraction-free reading. Runs locally on a cron schedule. Zero daily effort after setup.

---

## 1. Problem Statement

Good food content arrives by email — recipe newsletters, Substack food writers, cooking deep-dives. The content is worth reading. The medium is not.

Email is where food content goes to die. Recipes are buried inside HTML newsletters packed with tracking pixels, cross-promotions, and "you might also like" noise. The actual content lives behind a link you have to click through. And even when you do click, you're reading on a phone screen between Slack notifications and calendar reminders. Most of the time, you skim the subject line, think "that looks good," and never come back to it.

The reMarkable is the right reading surface — distraction-free, e-ink, designed for exactly this kind of focused reading. But getting food content from Gmail to the reMarkable today requires manually finding the email, opening the link, converting it to PDF, and sending it over. That workflow has a completion rate of approximately zero.

The content exists. The reading surface exists. The pipeline between them doesn't.

---

## 2. Desired Outcome

A PDF magazine lands on the reMarkable once a week with the best food content from the past week's email. No manual effort after initial setup.

**Success looks like:** Actually reading food content on the reMarkable instead of archiving it unread in Gmail.

**How to measure it:**
- The pipeline runs reliably every week without intervention
- The magazine contains relevant, readable content (not garbled HTML or broken layouts)
- Jay reads at least 2 out of 4 weekly issues in the first month

---

## 3. User Personas

| Persona | Description | Primary Need |
|---------|-------------|-------------|
| **Reader Jay** | Picks up the reMarkable on weekends, wants curated content ready to go | Zero-effort consumption — magazine just appears, well-formatted, worth reading |
| **Curator Jay** | Occasionally tunes the system — adds sources, adjusts what gets through | Low-friction configuration — edit a config file or apply a Gmail label, not a web UI |

---

## 4. Scope

### In Scope (v1)

The smallest thing that delivers the outcome: emails in, magazine out.

- **Gmail API connection** — OAuth2 authentication, token refresh, read-only access
- **Label-based filtering** — scan emails with the `FOOD` label in Gmail. Jay controls what's "food" by labeling emails (manually or via Gmail filters). No sender whitelist to maintain, no AI classification. Simple and flexible.
- **Link extraction** — parse email HTML, extract the primary content links (the recipe URL, the article URL — not the unsubscribe link or the social media icons)
- **Content acquisition** — follow extracted links, pull the article/recipe content using a readability extractor. Handle failures gracefully (timeouts, 404s, paywalls).
- **Email body fallback** — some newsletters (especially Substacks) contain the full article in the email body. When the email body has substantial content and no meaningful outbound link, use the email body directly.
- **PDF generation** — format extracted content into a single multi-article PDF with a cover page, table of contents, and clean article layouts. Optimized for reMarkable's 10.3" e-ink display.
- **Delivery via email** — send the generated PDF to the reMarkable's email address (the simplest delivery path)
- **Local cron schedule** — runs weekly (default: Sunday morning), configurable
- **Config file** — YAML or TOML. Settings: Gmail label name, reMarkable email address, schedule, output preferences, content limits.
- **Logging** — enough detail to debug "why didn't that recipe show up?" without being noisy

### Deferred (v2+)

Valuable but not needed to prove the concept works.

- **AI-based content ranking** — use an LLM to score/rank articles by relevance, novelty, or estimated interest. v1 just includes everything labeled `FOOD`.
- **Structured recipe extraction** — parse recipes into ingredients, steps, cook time, servings. v1 treats recipes as articles.
- **Content deduplication** — detect when the same recipe appears in multiple newsletters. v1 might include duplicates; that's fine for now.
- **Web config UI** — v1 uses a config file. A web dashboard for managing sources and previewing issues is a v2 luxury.
- **rmapi delivery** — direct push via reMarkable cloud API. More reliable than email but more complex to set up. Fallback if email delivery proves unreliable.
- **Historical archive** — browse past issues. v1 just keeps PDFs in a local output directory.
- **ePub format option** — ePub reflows better but PDF is the v1 choice for layout control on reMarkable.
- **Multiple Gmail labels** — v1 uses one label (`FOOD`). Could support multiple labels with per-label formatting in v2.
- **Content summarization** — AI-generated summaries or "read this if you only have 5 minutes" digests.
- **Image optimization** — convert images to grayscale, resize for e-ink. v1 includes images as-is and lets reMarkable handle rendering.

### Out of Scope

Not this project.

- **Non-email sources** — RSS feeds, Twitter/X, YouTube. This is an email scanner, not an aggregator.
- **Recipe database / personal cookbook** — Feed is a reading pipeline, not a storage system. If a recipe is worth saving, that's a different tool.
- **Multi-user support** — solo project, solo user.
- **Mobile app** — it's a cron job that produces a PDF. No app needed.
- **Social/sharing features** — this is for Jay's reMarkable, not for publishing.

---

## 5. Requirements

Organized by pipeline stage — Feed is fundamentally a data pipeline, so requirements follow the data flow.

### 5.1 Source Connection (Gmail API)

**User Story:** As Reader Jay, I need the pipeline to connect to my Gmail account securely so that it can scan for food emails without me doing anything each week.

**Acceptance Criteria:**
- [ ] OAuth2 authentication with Gmail API (read-only scope)
- [ ] Access token stored securely (not in plaintext config — use OS keychain or encrypted file)
- [ ] Refresh token handled automatically — no manual re-auth unless scopes change
- [ ] First-time setup: interactive browser-based OAuth flow, then unattended thereafter
- [ ] If auth fails at runtime, log the error clearly and skip the run (don't crash, don't send an empty magazine)

**Edge Cases:**
- Token expires mid-run: retry auth refresh once, then fail gracefully
- Google account has 2FA: OAuth flow handles this natively, no special handling needed

### 5.2 Content Identification (Label Filtering)

**User Story:** As Curator Jay, I need to control which emails become magazine content by using a Gmail label, so that I can add or remove sources without editing config files.

**Acceptance Criteria:**
- [ ] Scan all emails with the configured Gmail label (default: `FOOD`) received since the last successful run
- [ ] Track "last successful run" timestamp in a local state file to avoid re-processing
- [ ] If no emails match, skip magazine generation (don't send an empty PDF)
- [ ] Log which emails were found: sender, subject, date received
- [ ] Ignore emails already processed in a previous run (idempotency)

**Edge Cases:**
- Label doesn't exist in Gmail: log a clear error message ("Label 'FOOD' not found in your Gmail — create it and label some emails")
- Hundreds of emails labeled (first run or catch-up): cap at configurable max (default: 20 most recent) to keep the magazine a reasonable size

### 5.3 Content Acquisition (Link Extraction + Fetching)

**User Story:** As Reader Jay, I need the pipeline to follow links from food emails and grab the actual article content, so that I read recipes and articles — not email HTML with ads.

**Acceptance Criteria:**
- [ ] Parse each email's HTML body to extract content links
- [ ] Filter out non-content links: unsubscribe, social media icons, tracking redirects, email client "view in browser" links
- [ ] Identify the primary content link per email (the one that leads to the actual recipe or article)
- [ ] Fetch the linked page and extract readable content using a readability library (Mozilla Readability, newspaper3k, or similar)
- [ ] If the email body itself contains substantial content (>500 words of non-boilerplate text) and has no primary outbound link, use the email body as the article content
- [ ] Capture article title, author (if available), source name, and body text
- [ ] Capture images referenced in the article (for inclusion in the PDF)
- [ ] Timeout per fetch: 30 seconds. Skip and log on timeout.
- [ ] Respect robots.txt — don't fetch from sites that block scrapers

**Edge Cases:**
- Paywalled content: extract whatever's available (title, summary, first paragraphs). Include a "Full article requires subscription" note. Don't skip it entirely — the summary might still be worth reading.
- Redirect chains: follow up to 5 redirects. Log the final URL.
- Content in a non-English language: include it as-is. Don't filter by language.
- Newsletter with multiple recipe links: extract up to 3 links per email (configurable). Don't turn one newsletter into 15 articles.

### 5.4 Content Assembly (Magazine Formatting)

**User Story:** As Reader Jay, I need the output to feel like a magazine I'd want to pick up — not a dump of raw HTML or a wall of plain text.

**Acceptance Criteria:**
- [ ] Generate a single PDF file per run
- [ ] **Cover page**: "Feed" title, issue date range (e.g., "Mar 7–13, 2026"), article count
- [ ] **Table of contents**: article titles with source names, linked to pages
- [ ] **Article pages**: clean typography — title, source, author, body text, images
- [ ] Page size optimized for reMarkable display (approx. 1404 x 1872 pixels, or standard US Letter/A4 scaled for the 10.3" screen)
- [ ] Serif font for body text, sans-serif for headers (readability on e-ink)
- [ ] Images included inline where they appear in the article
- [ ] Articles ordered by source, then by date within each source
- [ ] PDF file size stays under 50MB (reMarkable email attachment limit)
- [ ] Filename format: `feed-YYYY-MM-DD.pdf`

**Edge Cases:**
- Only 1 article this week: still generate the magazine (thin issues are fine)
- Article with no images: text-only layout, no broken image placeholders
- Article with very long content (>5000 words): include full content, don't truncate. Long reads are the point.
- Article extraction fails (garbled output): skip the article, note it in the log, include remaining articles

### 5.5 Delivery (reMarkable Email)

**User Story:** As Reader Jay, I need the magazine to show up on my reMarkable automatically, so I can pick it up and start reading without any transfer steps.

**Acceptance Criteria:**
- [ ] Send the generated PDF as an email attachment to the configured reMarkable email address
- [ ] Email subject line: "Feed — Mar 7–13, 2026" (matches the cover page)
- [ ] Send from a configured email address (can be the same Gmail account, or a dedicated sender)
- [ ] Log delivery confirmation (email sent successfully)
- [ ] If email send fails, retry once after 60 seconds. If still fails, save the PDF locally and log the error.

**Edge Cases:**
- PDF exceeds 50MB: compress images and regenerate. If still over limit, split into two parts.
- reMarkable email address is misconfigured: clear error in logs ("Delivery failed — check your reMarkable email address in config")
- SMTP auth failure: log the error, don't retry indefinitely

### 5.6 Scheduling (Cron)

**User Story:** As Reader Jay, I need this to run automatically on a weekly schedule without me remembering to trigger it.

**Acceptance Criteria:**
- [ ] Provide a setup script or clear instructions to configure a cron job (or systemd timer)
- [ ] Default schedule: every Sunday at 7:00 AM local time
- [ ] Schedule is configurable in the config file
- [ ] Pipeline is idempotent — running it twice in the same period doesn't produce duplicate magazines or re-process the same emails
- [ ] If the machine was off during the scheduled run, the next run catches up (processes all emails since last successful run, regardless of when cron fires)

### 5.7 Configuration

**User Story:** As Curator Jay, I need a simple config file to set up the pipeline and occasionally tweak settings.

**Acceptance Criteria:**
- [ ] Single config file (YAML or TOML) in the project root or `~/.config/feed/`
- [ ] Required settings: Gmail label name, reMarkable email address
- [ ] Optional settings: schedule, max articles per issue, max links per email, output directory, log level, sender email config
- [ ] Sensible defaults for all optional settings
- [ ] Config file is validated on startup — clear error messages for missing required fields or invalid values
- [ ] Example config file included in the repo with comments explaining each setting

**Example config:**
```yaml
gmail:
  label: "FOOD"
  max_emails_per_run: 20

remarkable:
  email: "your-address@remarkable.com"

magazine:
  max_articles: 15
  max_links_per_email: 3
  output_dir: "~/feed-output"

schedule:
  day: "sunday"
  time: "07:00"

logging:
  level: "info"  # debug | info | warn | error
```

---

## 6. Pipeline Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Gmail API  │────▶│  Label Filter │────▶│  Link Extractor  │
│  (OAuth2)    │     │  (FOOD label) │     │  (parse HTML)    │
└─────────────┘     └──────────────┘     └──────────────────┘
                                                   │
                                          ┌────────▼────────┐
                                          │ Content Fetcher  │
                                          │ (readability     │
                                          │  extraction)     │
                                          └────────┬────────┘
                                                   │
                                          ┌────────▼────────┐
                                          │ PDF Generator    │
                                          │ (cover + TOC +   │
                                          │  article pages)  │
                                          └────────┬────────┘
                                                   │
                                          ┌────────▼────────┐
                                          │ Email Sender     │
                                          │ (→ reMarkable)   │
                                          └─────────────────┘
```

Each stage is independent and testable. If content fetching fails for one article, the rest still proceed. The pipeline logs each stage's input/output counts for debugging.

---

## 7. Non-Functional Requirements

| Requirement | Target |
|---|---|
| **Reliability** | Handles transient failures gracefully — network issues, API rate limits, individual fetch failures. Retries with backoff where appropriate. Never sends a duplicate magazine for the same period. |
| **Performance** | Full pipeline completes in under 5 minutes for a typical week (10-15 articles). Acceptable up to 15 minutes for a large catch-up run. |
| **Security** | OAuth tokens stored via OS keychain or encrypted at rest — never in plaintext config. No email content stored in the cloud. Pipeline runs entirely locally. |
| **Privacy** | All data stays on Jay's machine. Email content is processed in memory and only persisted as the final PDF. No analytics, no telemetry, no external services beyond Gmail API and the email sender. |
| **Observability** | Structured logging with timestamps. Each run logs: emails found, articles extracted, articles failed, PDF size, delivery status. Debug mode shows full extraction details per article. |
| **Maintainability** | Clean separation between pipeline stages. Each stage can be tested independently. Adding a new stage (e.g., AI ranking) shouldn't require rewriting existing stages. |

---

## 8. Dependencies

| Dependency | What For | Notes |
|---|---|---|
| **Gmail API** | Reading emails by label | Requires a Google Cloud project with Gmail API enabled. Free tier is more than sufficient. |
| **Google OAuth2 credentials** | Authentication | `credentials.json` from Google Cloud Console. One-time setup. |
| **reMarkable email address** | Delivery | Found in reMarkable settings → "Send by email." Each device has a unique address. |
| **Python 3.10+** | Runtime | Best ecosystem for HTML parsing, content extraction, PDF generation. |
| **Content extraction library** | Pulling article text from web pages | Options: `trafilatura` (Python, best accuracy for article extraction), `newspaper3k`, `readability-lxml`. Evaluate during build. |
| **PDF generation library** | Building the magazine | Options: `weasyprint` (HTML/CSS → PDF, good typography control), `reportlab` (lower-level), `fpdf2` (lightweight). `weasyprint` is the likely pick for magazine-quality output. |
| **SMTP or email API** | Sending the PDF | Can use Gmail's own SMTP (already authenticated), or a service like Resend/SendGrid for cleaner separation. |

---

## 9. Tech Stack (Recommended)

| Component | Choice | Why |
|---|---|---|
| **Language** | Python 3.10+ | Best library ecosystem for every stage of this pipeline |
| **Gmail access** | `google-api-python-client` + `google-auth` | Official Google libraries. Well-documented OAuth2 flow. |
| **Email parsing** | `beautifulsoup4` + `lxml` | Robust HTML parsing for extracting links from email bodies |
| **Content extraction** | `trafilatura` | Best-in-class article extraction. Handles boilerplate removal, main content detection, metadata extraction. Better accuracy than newspaper3k for modern web pages. |
| **PDF generation** | `weasyprint` | HTML/CSS to PDF. Full typography control, supports custom fonts, handles images. The right tool for magazine-quality output. |
| **Email sending** | `smtplib` (stdlib) | Gmail SMTP with app password or OAuth2. No external dependency needed. |
| **Config** | `pyyaml` or `tomli` | YAML or TOML config parsing |
| **Scheduling** | System cron / systemd timer | No Python scheduler needed — use the OS |
| **Token storage** | `keyring` | Cross-platform secure credential storage (OS keychain) |

---

## 10. Open Questions

Decisions to make during build, not before.

| # | Question | Leaning | Why It Can Wait |
|---|---|---|---|
| 1 | **Content ordering** — chronological, by source, by estimated read time, or by content type (recipes first, articles second)? | By source, then by date | Try it, see what reads best on the reMarkable. Easy to change. |
| 2 | **Image handling** — convert to grayscale for e-ink, strip entirely, or include as-is? | Include as-is for v1 | reMarkable handles image rendering. Only optimize if images look bad or bloat the PDF. |
| 3 | **Paywall strategy** — include partial content with a note, or skip paywalled articles? | Include partial + note | Some partial content is better than nothing. Can refine later. |
| 4 | **Content deduplication** — same recipe in multiple newsletters? | Allow duplicates in v1 | Dedup is hard to get right. See if it's actually a problem before solving it. |
| 5 | **Email body vs. linked content** — when a Substack email contains the full article AND links to the web version, which wins? | Prefer email body if it's complete | The email body is already fetched and avoids a web request. But the web version might have better formatting. Test both. |
| 6 | **Magazine design depth** — how much formatting effort? Pull quotes? Section dividers? Masthead? | Start minimal, iterate | Get a working PDF first. Make it prettier in v2 if the basic version gets read. |
| 7 | **Digest frequency** — weekly is the default, but should volume trigger more frequent issues? | Fixed weekly for v1 | Complexity of variable scheduling isn't worth it yet. If 20 articles pile up, a fat weekly issue is fine. |

---

## 11. Setup Flow

First-time setup (one-time, ~15 minutes):

1. Clone the repo
2. `pip install -r requirements.txt`
3. Create a Google Cloud project, enable Gmail API, download `credentials.json`
4. Run `feed --setup` → opens browser for OAuth2 consent → stores tokens securely
5. Create the `FOOD` label in Gmail (if it doesn't exist)
6. Set up Gmail filters to auto-label food newsletters with `FOOD` (or label manually)
7. Copy `config.example.yaml` → `config.yaml`, set reMarkable email address
8. Run `feed --dry-run` → shows what would be included without sending
9. Run `feed` → generates and sends first issue
10. Set up cron: `crontab -e` → add the weekly schedule

After setup, it just runs. The only maintenance is labeling new food email subscriptions in Gmail.

---

## 12. Build Order

Ship the pipeline end-to-end first, then improve each stage.

| Phase | What | Why This Order |
|---|---|---|
| **1** | Gmail API connection + OAuth2 setup + label query | Can't do anything without email access |
| **2** | Email parsing + link extraction | Need to see what's in the emails before deciding how to extract |
| **3** | Content fetching with trafilatura | The hardest technical piece — get this working early |
| **4** | Basic PDF generation (plain text + images, minimal styling) | End-to-end pipeline works at this point, even if ugly |
| **5** | Email delivery to reMarkable | Pipeline is now fully functional |
| **6** | Config file, logging, error handling | Make it robust enough to run unattended |
| **7** | Cron setup + idempotency (state file for last-run tracking) | Automated weekly runs |
| **8** | Magazine design polish (cover page, TOC, typography) | Make it worth reading |

**Critical path:** Phases 1–5 deliver a working pipeline. Everything after that is refinement.
