"""Generate a magazine-style PDF from extracted articles."""

import logging
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from feed.fetcher import Article

logger = logging.getLogger(__name__)

TEMPLATE_DIR = Path(__file__).parent.parent.parent / "templates"


def generate_magazine(
    articles: list[Article],
    output_dir: Path,
    issue_date: date | None = None,
) -> Path:
    """Render articles into a magazine PDF.

    Returns the path to the generated PDF.
    """
    issue_date = issue_date or date.today()
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"feed-{issue_date.isoformat()}.pdf"
    pdf_path = output_dir / filename

    # Render HTML from Jinja2 template
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    template = env.get_template("magazine.html")

    html_content = template.render(
        articles=articles,
        issue_date=issue_date,
        issue_number=_issue_number(issue_date),
        article_count=len(articles),
    )

    # Convert HTML to PDF
    logger.info("Generating PDF: %s (%d articles)", pdf_path, len(articles))
    HTML(string=html_content).write_pdf(str(pdf_path))

    size_kb = pdf_path.stat().st_size / 1024
    logger.info("PDF generated: %s (%.1f KB)", pdf_path, size_kb)

    return pdf_path


def _issue_number(d: date) -> str:
    """Generate a human-readable issue number like 'Vol. 2026, No. 11'."""
    week = d.isocalendar()[1]
    return f"Vol. {d.year}, No. {week}"
