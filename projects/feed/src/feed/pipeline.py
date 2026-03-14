"""Pipeline orchestrator — wires all stages together."""

import logging
from datetime import datetime

from feed.config import Config
from feed.gmail import authenticate, get_service, fetch_emails
from feed.parser import extract_all_links
from feed.fetcher import fetch_all_articles
from feed.magazine import generate_magazine
from feed.delivery import send_to_remarkable
from feed.state import load_state, save_state, get_last_run_datetime

logger = logging.getLogger(__name__)


def run_pipeline(config: Config, dry_run: bool = False) -> None:
    """Execute the full Feed pipeline.

    Stages:
        1. Authenticate with Gmail
        2. Fetch emails with configured label
        3. Extract content links from email HTML
        4. Fetch and extract article content
        5. Generate magazine PDF
        6. Send to reMarkable (unless dry_run)
        7. Update state
    """
    mode = "DRY RUN" if dry_run else "FULL RUN"
    logger.info("=== Feed %s starting ===", mode)

    # Load state for idempotency
    state = load_state(config.state_path)
    last_run = get_last_run_datetime(state)
    exclude_ids = set(state.processed_message_ids)

    if last_run:
        logger.info("Last run: %s — fetching new emails only", last_run.isoformat())
    else:
        logger.info("First run — fetching all labeled emails")

    # Stage 1: Authenticate
    logger.info("Stage 1: Authenticating with Gmail")
    creds = authenticate(config.credentials_path, config.token_path)
    service = get_service(creds)

    # Stage 2: Fetch emails
    logger.info("Stage 2: Fetching emails with label '%s'", config.gmail.label)
    emails = fetch_emails(
        service,
        label_name=config.gmail.label,
        after=last_run,
        max_results=config.gmail.max_emails_per_run,
        exclude_ids=exclude_ids,
    )

    if not emails:
        logger.info("No new emails to process. Done.")
        return

    logger.info("Fetched %d new emails", len(emails))

    # Stage 3: Extract links
    logger.info("Stage 3: Extracting content links")
    links = extract_all_links(
        emails,
        max_links_per_email=config.magazine.max_links_per_email,
    )

    if not links:
        logger.info("No content links found in emails. Done.")
        # Still mark emails as processed
        _update_state(state, emails, config)
        return

    # Stage 4: Fetch articles
    logger.info("Stage 4: Fetching article content (%d links)", len(links))
    articles = fetch_all_articles(links, max_articles=config.magazine.max_articles)

    if not articles:
        logger.info("No articles could be extracted. Done.")
        _update_state(state, emails, config)
        return

    # Stage 5: Generate PDF
    logger.info("Stage 5: Generating magazine PDF")
    pdf_path = generate_magazine(
        articles,
        output_dir=config.magazine.output_path,
    )

    # Stage 6: Send to reMarkable
    if dry_run:
        logger.info("Stage 6: SKIPPED (dry run) — PDF saved to %s", pdf_path)
    else:
        logger.info("Stage 6: Sending to reMarkable")
        send_to_remarkable(
            pdf_path=pdf_path,
            sender=config.smtp.sender,
            app_password=config.smtp.app_password,
            remarkable_email=config.remarkable.email,
        )

    # Stage 7: Update state
    _update_state(state, emails, config)
    state.total_issues_generated += 1
    save_state(state, config.state_path)

    logger.info("=== Feed %s complete — %d articles in issue ===", mode, len(articles))


def _update_state(state, emails, config):
    """Mark emails as processed and save state."""
    for email in emails:
        if email.message_id not in state.processed_message_ids:
            state.processed_message_ids.append(email.message_id)
    state.last_run = datetime.now().isoformat()
    save_state(state, config.state_path)
