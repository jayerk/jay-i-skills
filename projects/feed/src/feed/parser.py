"""Parse email HTML and extract food-related content links."""

import logging
import re
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from feed.gmail import Email

logger = logging.getLogger(__name__)

# Domains that are tracking/unsubscribe links, not content
SKIP_DOMAINS = {
    "list-manage.com", "mailchimp.com", "sendgrid.net", "constantcontact.com",
    "campaign-archive.com", "google.com", "gmail.com", "apple.com",
    "facebook.com", "twitter.com", "instagram.com", "youtube.com",
    "linkedin.com", "pinterest.com", "tiktok.com",
    "unsubscribe", "manage-preferences", "view-in-browser",
}

# URL patterns that indicate tracking/utility links, not articles
SKIP_PATTERNS = [
    re.compile(r"unsubscribe", re.I),
    re.compile(r"manage.?preferences", re.I),
    re.compile(r"view.?in.?browser", re.I),
    re.compile(r"email.?settings", re.I),
    re.compile(r"privacy.?policy", re.I),
    re.compile(r"/cdn-cgi/", re.I),
]


def extract_links(email: Email, max_links: int = 3) -> list[dict]:
    """Extract content links from an email's HTML body.

    Returns list of dicts with keys: url, anchor_text, source_email_subject, source_sender
    """
    if not email.html_body:
        logger.debug("No HTML body in email '%s'", email.subject)
        return []

    soup = BeautifulSoup(email.html_body, "lxml")
    links = []
    seen_urls = set()

    for a_tag in soup.find_all("a", href=True):
        url = a_tag["href"].strip()

        # Skip non-http links
        if not url.startswith(("http://", "https://")):
            continue

        # Normalize
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        # Skip known non-content domains
        if any(skip in domain for skip in SKIP_DOMAINS):
            continue

        # Skip tracking/utility patterns
        if any(pat.search(url) for pat in SKIP_PATTERNS):
            continue

        # Deduplicate
        canonical = f"{parsed.netloc}{parsed.path}".rstrip("/")
        if canonical in seen_urls:
            continue
        seen_urls.add(canonical)

        anchor_text = a_tag.get_text(strip=True)

        # Skip links with no meaningful anchor text (icon links, etc.)
        if len(anchor_text) < 3:
            continue

        links.append({
            "url": url,
            "anchor_text": anchor_text,
            "source_email_subject": email.subject,
            "source_sender": email.sender,
        })

        if len(links) >= max_links:
            break

    logger.info(
        "Extracted %d links from '%s' (%s)",
        len(links), email.subject, email.sender,
    )
    return links


def extract_all_links(emails: list[Email], max_links_per_email: int = 3) -> list[dict]:
    """Extract content links from all emails."""
    all_links = []
    seen_urls = set()

    for email in emails:
        links = extract_links(email, max_links=max_links_per_email)
        for link in links:
            if link["url"] not in seen_urls:
                seen_urls.add(link["url"])
                all_links.append(link)

    logger.info("Total unique content links extracted: %d", len(all_links))
    return all_links
