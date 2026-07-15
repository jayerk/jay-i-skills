"""Generate a magazine-style PDF from extracted recipes and articles."""

import logging
from datetime import date, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

from feed.fetcher import ContentItem, Recipe, Article

logger = logging.getLogger(__name__)

TEMPLATE_DIR = Path(__file__).parent / "templates"


def generate_magazine(
    items: list[ContentItem],
    output_dir: Path,
    issue_date: date | None = None,
) -> Path:
    """Render content items into a magazine PDF.

    Returns the path to the generated PDF.
    """
    issue_date = issue_date or date.today()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Timestamped filename — same-day re-runs must not collide, because
    # rmapi refuses to upload over an existing document of the same name.
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    pdf_path = output_dir / f"feed-{stamp}.pdf"

    recipe_count = sum(1 for i in items if isinstance(i, Recipe))
    article_count = sum(1 for i in items if isinstance(i, Article))

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(),
    )
    template = env.get_template("magazine.html")

    html_content = template.render(
        items=items,
        issue_date=issue_date,
        issue_number=_issue_number(issue_date),
        item_count=len(items),
        recipe_count=recipe_count,
        article_count=article_count,
    )

    logger.info(
        "Generating PDF: %s (%d recipes, %d articles)",
        pdf_path, recipe_count, article_count,
    )
    HTML(string=html_content).write_pdf(str(pdf_path))

    size_kb = pdf_path.stat().st_size / 1024
    logger.info("PDF generated: %s (%.1f KB)", pdf_path, size_kb)

    return pdf_path


def _issue_number(d: date) -> str:
    """Generate a human-readable issue number like 'Vol. 2026, No. 11'."""
    week = d.isocalendar()[1]
    return f"Vol. {d.year}, No. {week}"
