# CLAUDE.md — Feed

Email-to-reMarkable food magazine pipeline. Python CLI that runs on cron.

## Skills & Persona (jay-i-skills)

- **Skills repo path**: `/home/user/jay-i-skills`
- **Context**: `personal` — read `.claude/skills/personal/_persona.md` before any skill work
- **Design docs**: `.claude/skills/personal/feed/feed-prd.md`

Do NOT duplicate persona or skill content in this repo.

## Architecture

Feed is a linear data pipeline with 6 stages:

```
Gmail API → Label Filter → Link Extractor → Content Fetcher → PDF Generator → Email Sender
```

Each stage is a separate module in `src/feed/`. The pipeline orchestrator (`pipeline.py`)
wires them together. Each stage can be tested independently.

## Tech Stack

- **Python 3.10+**
- **Gmail API** via `google-api-python-client` + `google-auth-oauthlib`
- **BeautifulSoup4** for email HTML parsing
- **trafilatura** for web article extraction
- **weasyprint** for HTML → PDF (magazine formatting)
- **Jinja2** for HTML templates
- **smtplib** (stdlib) for email delivery

## Key Files

| File | Purpose |
|------|---------|
| `src/feed/__main__.py` | CLI entry point (`feed`, `feed --setup`, `feed --dry-run`) |
| `src/feed/pipeline.py` | Orchestrator — wires all stages |
| `src/feed/gmail.py` | OAuth2 + email fetching by label |
| `src/feed/parser.py` | Email HTML parsing + link extraction |
| `src/feed/fetcher.py` | URL → article content via trafilatura |
| `src/feed/magazine.py` | Jinja2 template → weasyprint PDF |
| `src/feed/delivery.py` | SMTP send to reMarkable |
| `src/feed/state.py` | Last-run tracking for idempotency |
| `src/feed/config.py` | YAML config loading + validation |
| `templates/magazine.html` | Jinja2 HTML template for the PDF |

## Config

`~/.config/feed/config.yaml` — see `config.example.yaml` for annotated example.

Required: `gmail.label`, `remarkable.email`.

## Dev Commands

```bash
pip install -e .            # Install in dev mode
feed --setup                # Run OAuth2 flow (first time)
feed --dry-run              # Scan + extract, generate PDF locally, don't send
feed                        # Full run: scan → extract → PDF → send
feed --log-level debug      # Verbose logging
```
