"""Fetch web articles and extract readable content."""

import logging
from dataclasses import dataclass

import trafilatura

logger = logging.getLogger(__name__)


@dataclass
class Article:
    """Extracted article content."""
    url: str
    title: str
    author: str | None
    text: str
    source_email_subject: str
    source_sender: str


def fetch_article(link: dict) -> Article | None:
    """Download and extract article content from a URL.

    Args:
        link: Dict with url, anchor_text, source_email_subject, source_sender

    Returns:
        Article if extraction succeeds, None otherwise.
    """
    url = link["url"]
    logger.debug("Fetching article: %s", url)

    try:
        downloaded = trafilatura.fetch_url(url)
    except Exception:
        logger.exception("Failed to download: %s", url)
        return None

    if not downloaded:
        logger.warning("Empty response from: %s", url)
        return None

    try:
        result = trafilatura.extract(
            downloaded,
            include_comments=False,
            include_tables=True,
            favor_recall=True,
            output_format="txt",
        )
    except Exception:
        logger.exception("Extraction failed for: %s", url)
        return None

    if not result or len(result.strip()) < 100:
        logger.warning("Insufficient content extracted from: %s", url)
        return None

    # Get metadata
    try:
        metadata = trafilatura.extract(
            downloaded,
            output_format="xml",
            include_comments=False,
        )
    except Exception:
        metadata = None

    # Try to extract title from metadata, fall back to anchor text
    title = link.get("anchor_text", "Untitled")
    author = None

    if metadata:
        try:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(metadata)
            meta_title = root.get("title")
            meta_author = root.get("author")
            if meta_title:
                title = meta_title
            if meta_author:
                author = meta_author
        except Exception:
            pass

    article = Article(
        url=url,
        title=title,
        author=author,
        text=result.strip(),
        source_email_subject=link["source_email_subject"],
        source_sender=link["source_sender"],
    )

    logger.info("  Extracted: '%s' (%d chars)", article.title, len(article.text))
    return article


def fetch_all_articles(links: list[dict], max_articles: int = 15) -> list[Article]:
    """Fetch and extract content from all links.

    Stops after max_articles successful extractions.
    """
    articles = []

    for link in links:
        if len(articles) >= max_articles:
            logger.info("Reached max articles (%d), stopping", max_articles)
            break

        article = fetch_article(link)
        if article:
            articles.append(article)

    logger.info("Successfully extracted %d articles from %d links", len(articles), len(links))
    return articles
