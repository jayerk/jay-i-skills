"""Parse email HTML and extract food-related content links.

Uses a scoring system to prioritize links most likely to be primary
recipe/article content over sidebar links and promos.
"""

import logging
import re
from urllib.parse import urlparse

from bs4 import BeautifulSoup, Tag

from feed.gmail import Email

logger = logging.getLogger(__name__)

# ─── Skip lists ───

SKIP_DOMAINS = {
    "list-manage.com", "mailchimp.com", "sendgrid.net", "constantcontact.com",
    "campaign-archive.com", "google.com", "gmail.com", "apple.com",
    "facebook.com", "twitter.com", "x.com", "instagram.com", "youtube.com",
    "linkedin.com", "pinterest.com", "tiktok.com", "threads.net",
}

SKIP_URL_PATTERNS = [
    re.compile(r"unsubscribe", re.I),
    re.compile(r"manage.?preferences", re.I),
    re.compile(r"view.?in.?browser", re.I),
    re.compile(r"email.?settings", re.I),
    re.compile(r"privacy.?policy", re.I),
    re.compile(r"terms.?of.?(service|use)", re.I),
    re.compile(r"/cdn-cgi/", re.I),
    re.compile(r"mailto:", re.I),
]

SKIP_ANCHOR_PATTERNS = [
    re.compile(r"^unsubscribe$", re.I),
    re.compile(r"^view (in|this) (browser|email)$", re.I),
    re.compile(r"^manage preferences$", re.I),
    re.compile(r"^(share|tweet|pin|forward)$", re.I),
]

# ─── Scoring signals ───

# Anchor text that strongly signals a recipe/article link
RECIPE_ANCHOR_PATTERNS = [
    (re.compile(r"(get|view|see|read)\s+(the\s+)?full\s+recipe", re.I), 20),
    (re.compile(r"(get|view|see|read)\s+(the\s+)?recipe", re.I), 18),
    (re.compile(r"full\s+recipe", re.I), 15),
    (re.compile(r"continue\s+reading", re.I), 12),
    (re.compile(r"read\s+(more|the\s+full|the\s+rest)", re.I), 12),
    (re.compile(r"make\s+(this|it)", re.I), 10),
    (re.compile(r"cook\s+this", re.I), 10),
]

# URL path segments that indicate recipe/article content
RECIPE_URL_PATTERNS = [
    (re.compile(r"/recipes?/", re.I), 12),
    (re.compile(r"/cooking/", re.I), 8),
    (re.compile(r"/food/", re.I), 6),
    (re.compile(r"/article/", re.I), 5),
    (re.compile(r"/story/", re.I), 5),
    (re.compile(r"/post/", re.I), 4),
]

# Known recipe/food domains get a boost
FOOD_DOMAINS = {
    "nytimes.com": 8, "cooking.nytimes.com": 12,
    "bonappetit.com": 10, "seriouseats.com": 10,
    "smittenkitchen.com": 10, "food52.com": 8,
    "epicurious.com": 8, "thekitchn.com": 8,
    "americastestkitchen.com": 8, "cooksillustrated.com": 8,
    "kingarthurbaking.com": 8, "budgetbytes.com": 8,
    "halfbakedharvest.com": 8, "minimalistbaker.com": 8,
    "pinchofyum.com": 8, "sallysbakingaddiction.com": 8,
    "damndelicious.net": 8, "cookieandkate.com": 8,
}


def _should_skip(url: str, anchor_text: str, domain: str) -> bool:
    """Check if a link should be filtered out entirely."""
    if not url.startswith(("http://", "https://")):
        return True

    if any(domain == skip or domain.endswith("." + skip) for skip in SKIP_DOMAINS):
        return True

    if any(pat.search(url) for pat in SKIP_URL_PATTERNS):
        return True

    if any(pat.search(anchor_text) for pat in SKIP_ANCHOR_PATTERNS):
        return True

    return False


def _score_link(url: str, anchor_text: str, domain: str, position: int, total_links: int) -> int:
    """Score a link based on multiple signals. Higher = more likely primary content."""
    score = 0

    # 1. Anchor text recipe signals (strongest indicator)
    for pattern, points in RECIPE_ANCHOR_PATTERNS:
        if pattern.search(anchor_text):
            score += points
            break  # Take the highest match only

    # 2. Anchor text length (longer = more likely real content link)
    text_len = len(anchor_text)
    if text_len > 40:
        score += 6
    elif text_len > 20:
        score += 4
    elif text_len > 10:
        score += 2
    elif text_len < 3:
        score -= 10  # Icon/emoji links

    # 3. URL path signals
    parsed = urlparse(url)
    path = parsed.path

    for pattern, points in RECIPE_URL_PATTERNS:
        if pattern.search(path):
            score += points
            break

    # URL path depth — deeper paths are more likely specific articles
    path_segments = [s for s in path.split("/") if s]
    if len(path_segments) >= 3:
        score += 4
    elif len(path_segments) >= 2:
        score += 2

    # Readable slug in URL (hyphens = human-readable = article page)
    last_segment = path_segments[-1] if path_segments else ""
    if "-" in last_segment and len(last_segment) > 10:
        score += 5

    # 4. Known food domain boost
    for food_domain, points in FOOD_DOMAINS.items():
        if domain.endswith(food_domain):
            score += points
            break

    # 5. Position in email (earlier = more important)
    if total_links > 0:
        position_ratio = position / total_links
        if position_ratio < 0.2:
            score += 8  # Top 20% of links
        elif position_ratio < 0.4:
            score += 4
        elif position_ratio > 0.8:
            score -= 3  # Bottom 20% (footer junk)

    # 6. Query string penalty (long query strings = tracking)
    query = parsed.query
    if len(query) > 100:
        score -= 5
    elif len(query) > 50:
        score -= 2

    return score


def extract_links(email: Email, max_links: int = 3) -> list[dict]:
    """Extract and rank content links from an email's HTML body.

    Returns top-scoring links, sorted by relevance score.
    """
    if not email.html_body:
        logger.debug("No HTML body in email '%s'", email.subject)
        return []

    soup = BeautifulSoup(email.html_body, "lxml")
    all_a_tags = soup.find_all("a", href=True)
    total_links = len(all_a_tags)

    candidates = []
    seen_urls = set()

    for position, a_tag in enumerate(all_a_tags):
        url = a_tag["href"].strip()
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        anchor_text = a_tag.get_text(strip=True)

        if _should_skip(url, anchor_text, domain):
            continue

        # Deduplicate by normalized URL (strip tracking params)
        canonical = f"{parsed.netloc}{parsed.path}".rstrip("/").lower()
        if canonical in seen_urls:
            continue
        seen_urls.add(canonical)

        score = _score_link(url, anchor_text, domain, position, total_links)

        candidates.append({
            "url": url,
            "anchor_text": anchor_text,
            "source_email_subject": email.subject,
            "source_sender": email.sender,
            "score": score,
        })

    # Sort by score (highest first), take top N
    candidates.sort(key=lambda x: x["score"], reverse=True)
    top_links = candidates[:max_links]

    if top_links:
        logger.info(
            "Extracted %d links from '%s' (top score: %d)",
            len(top_links), email.subject, top_links[0]["score"],
        )
        for link in top_links:
            logger.debug(
                "  [score=%d] %s — %s",
                link["score"], link["anchor_text"][:50], link["url"][:80],
            )

    return top_links


def extract_all_links(emails: list[Email], max_links_per_email: int = 3) -> list[dict]:
    """Extract and rank content links from all emails."""
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
