"""Fetch web articles and extract readable content.

Prioritizes structured recipe extraction (schema.org JSON-LD) over
plain text. Falls back to trafilatura for non-recipe content.
"""

import json
import logging
import re
from dataclasses import dataclass, field

import requests
import trafilatura
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

FETCH_TIMEOUT = 30
USER_AGENT = "Feed/1.0 (personal magazine pipeline)"


@dataclass
class Recipe:
    """Structured recipe extracted from schema.org JSON-LD."""
    url: str
    title: str
    author: str | None
    description: str | None
    prep_time: str | None
    cook_time: str | None
    total_time: str | None
    servings: str | None
    ingredients: list[str] = field(default_factory=list)
    instructions: list[str] = field(default_factory=list)
    source_email_subject: str = ""
    source_sender: str = ""
    content_type: str = "recipe"


@dataclass
class Article:
    """Plain article content (non-recipe)."""
    url: str
    title: str
    author: str | None
    text: str
    source_email_subject: str = ""
    source_sender: str = ""
    content_type: str = "article"


# Union type for pipeline stages that handle both
ContentItem = Recipe | Article


def _download_page(url: str) -> str | None:
    """Download a page with timeout and user-agent."""
    try:
        resp = requests.get(
            url,
            timeout=FETCH_TIMEOUT,
            headers={"User-Agent": USER_AGENT},
            allow_redirects=True,
        )
        resp.raise_for_status()
        return resp.text
    except requests.RequestException:
        logger.exception("Failed to download: %s", url)
        return None


def _parse_iso_duration(duration: str | None) -> str | None:
    """Convert ISO 8601 duration (PT1H30M) to human-readable (1 hr 30 min)."""
    if not duration:
        return None

    match = re.match(
        r"PT?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?",
        duration,
        re.IGNORECASE,
    )
    if not match:
        # Already human-readable, or unrecognized format
        return duration

    hours, minutes, seconds = match.groups()
    parts = []
    if hours:
        parts.append(f"{hours} hr")
    if minutes:
        parts.append(f"{minutes} min")
    if seconds and not parts:
        parts.append(f"{seconds} sec")

    return " ".join(parts) if parts else duration


def _extract_recipe_jsonld(html: str) -> dict | None:
    """Find schema.org/Recipe JSON-LD in the page HTML.

    Handles both top-level Recipe objects and Recipe nested inside
    @graph arrays (common on WordPress recipe plugins).
    """
    soup = BeautifulSoup(html, "lxml")

    for script_tag in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script_tag.string)
        except (json.JSONDecodeError, TypeError):
            continue

        # Direct Recipe object
        if isinstance(data, dict):
            if data.get("@type") == "Recipe":
                return data
            # Check @graph array (WordPress pattern)
            if "@graph" in data:
                for item in data["@graph"]:
                    if isinstance(item, dict) and item.get("@type") == "Recipe":
                        return item
            # Some sites wrap in a list type like ["Recipe", "HowTo"]
            type_val = data.get("@type")
            if isinstance(type_val, list) and "Recipe" in type_val:
                return data

        # Array of JSON-LD objects
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and item.get("@type") == "Recipe":
                    return item

    return None


def _parse_instructions(raw_instructions) -> list[str]:
    """Parse recipe instructions from various schema.org formats.

    Instructions can be:
      - A plain string
      - A list of strings
      - A list of HowToStep objects
      - A list of HowToSection objects containing HowToStep items
    """
    if not raw_instructions:
        return []

    # Plain string — split on newlines or numbered steps
    if isinstance(raw_instructions, str):
        lines = re.split(r"\n+|\.\s+(?=\d)", raw_instructions)
        return [line.strip() for line in lines if line.strip()]

    if not isinstance(raw_instructions, list):
        return [str(raw_instructions)]

    steps = []
    for item in raw_instructions:
        if isinstance(item, str):
            steps.append(item.strip())
        elif isinstance(item, dict):
            # HowToStep
            if item.get("@type") == "HowToStep":
                text = item.get("text", "")
                if text:
                    steps.append(text.strip())
            # HowToSection — has itemListElement with nested steps
            elif item.get("@type") == "HowToSection":
                section_name = item.get("name", "")
                if section_name:
                    steps.append(f"— {section_name} —")
                for sub in item.get("itemListElement", []):
                    if isinstance(sub, dict):
                        text = sub.get("text", "")
                        if text:
                            steps.append(text.strip())
                    elif isinstance(sub, str):
                        steps.append(sub.strip())

    return [s for s in steps if s]


def _parse_ingredients(raw_ingredients) -> list[str]:
    """Parse ingredients list."""
    if not raw_ingredients:
        return []
    if isinstance(raw_ingredients, str):
        return [line.strip() for line in raw_ingredients.split("\n") if line.strip()]
    if isinstance(raw_ingredients, list):
        return [str(item).strip() for item in raw_ingredients if str(item).strip()]
    return []


def _get_string(data: dict, key: str) -> str | None:
    """Safely get a string value from JSON-LD data (handles nested objects)."""
    val = data.get(key)
    if val is None:
        return None
    if isinstance(val, str):
        return val
    if isinstance(val, dict):
        return val.get("name") or val.get("text") or str(val)
    if isinstance(val, list):
        names = [v.get("name") if isinstance(v, dict) else str(v) for v in val]
        return ", ".join(n for n in names if n)
    return str(val)


def _build_recipe(jsonld: dict, url: str, link: dict) -> Recipe:
    """Build a Recipe dataclass from parsed JSON-LD."""
    return Recipe(
        url=url,
        title=_get_string(jsonld, "name") or link.get("anchor_text", "Untitled Recipe"),
        author=_get_string(jsonld, "author"),
        description=_get_string(jsonld, "description"),
        prep_time=_parse_iso_duration(jsonld.get("prepTime")),
        cook_time=_parse_iso_duration(jsonld.get("cookTime")),
        total_time=_parse_iso_duration(jsonld.get("totalTime")),
        servings=_get_string(jsonld, "recipeYield"),
        ingredients=_parse_ingredients(jsonld.get("recipeIngredient")),
        instructions=_parse_instructions(jsonld.get("recipeInstructions")),
        source_email_subject=link.get("source_email_subject", ""),
        source_sender=link.get("source_sender", ""),
    )


def _build_article_fallback(html: str, url: str, link: dict) -> Article | None:
    """Fall back to trafilatura plain text extraction for non-recipe pages."""
    try:
        result = trafilatura.extract(
            html,
            include_comments=False,
            include_tables=True,
            favor_recall=True,
            output_format="txt",
        )
    except Exception:
        logger.exception("trafilatura extraction failed for: %s", url)
        return None

    if not result or len(result.strip()) < 100:
        logger.warning("Insufficient content extracted from: %s", url)
        return None

    # Try metadata
    title = link.get("anchor_text", "Untitled")
    author = None
    try:
        meta = trafilatura.extract_metadata(html)
        if meta:
            if meta.title:
                title = meta.title
            if meta.author:
                author = meta.author
    except Exception:
        pass

    return Article(
        url=url,
        title=title,
        author=author,
        text=result.strip(),
        source_email_subject=link.get("source_email_subject", ""),
        source_sender=link.get("source_sender", ""),
    )


def fetch_content(link: dict) -> ContentItem | None:
    """Download a URL and extract content.

    Tries structured recipe extraction first (JSON-LD).
    Falls back to trafilatura article extraction.
    """
    url = link["url"]
    logger.debug("Fetching: %s", url)

    html = _download_page(url)
    if not html:
        return None

    # Try recipe extraction first
    jsonld = _extract_recipe_jsonld(html)
    if jsonld:
        recipe = _build_recipe(jsonld, url, link)
        if recipe.ingredients or recipe.instructions:
            logger.info(
                "  Recipe: '%s' — %d ingredients, %d steps",
                recipe.title, len(recipe.ingredients), len(recipe.instructions),
            )
            return recipe
        logger.debug("JSON-LD found but no ingredients/instructions — falling back")

    # Fall back to article extraction
    article = _build_article_fallback(html, url, link)
    if article:
        logger.info("  Article: '%s' (%d chars)", article.title, len(article.text))
    return article


def fetch_all_content(links: list[dict], max_items: int = 15) -> list[ContentItem]:
    """Fetch and extract content from all links.

    Stops after max_items successful extractions.
    """
    items: list[ContentItem] = []

    for link in links:
        if len(items) >= max_items:
            logger.info("Reached max items (%d), stopping", max_items)
            break

        item = fetch_content(link)
        if item:
            items.append(item)

    recipes = sum(1 for i in items if isinstance(i, Recipe))
    articles = sum(1 for i in items if isinstance(i, Article))
    logger.info(
        "Extracted %d items from %d links (%d recipes, %d articles)",
        len(items), len(links), recipes, articles,
    )
    return items
