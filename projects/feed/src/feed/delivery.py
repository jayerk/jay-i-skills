"""Deliver the magazine PDF to reMarkable via rmapi.

Uses ddvk/rmapi (https://github.com/ddvk/rmapi) — a Go CLI that talks
to the reMarkable cloud. Requires one-time setup: `rmapi` prompts for
a code from my.remarkable.com on first run.
"""

import logging
import shutil
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


def check_rmapi() -> bool:
    """Verify rmapi is installed and accessible."""
    return shutil.which("rmapi") is not None


def ensure_folder(folder: str) -> None:
    """Create the target folder on reMarkable if it doesn't exist.

    rmapi mkdir is idempotent-ish — it errors if the folder exists,
    but we just ignore that.
    """
    try:
        subprocess.run(
            ["rmapi", "mkdir", folder],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        logger.warning("rmapi mkdir timed out for folder '%s'", folder)


def send_to_remarkable(pdf_path: Path, folder: str = "/Feed") -> None:
    """Upload a PDF to reMarkable via rmapi.

    Args:
        pdf_path: Local path to the PDF file.
        folder: Destination folder on reMarkable (created if missing).
    """
    if not check_rmapi():
        raise RuntimeError(
            "rmapi not found. Install it from https://github.com/ddvk/rmapi\n"
            "  go install github.com/ddvk/rmapi@latest\n"
            "Then run 'rmapi' once to authenticate with my.remarkable.com."
        )

    logger.info("Uploading '%s' to reMarkable folder '%s'", pdf_path.name, folder)

    ensure_folder(folder)

    result = subprocess.run(
        ["rmapi", "put", str(pdf_path), folder],
        capture_output=True,
        text=True,
        timeout=120,
    )

    if result.returncode != 0:
        stderr = result.stderr.strip()
        logger.error("rmapi put failed (exit %d): %s", result.returncode, stderr)

        if "not authenticated" in stderr.lower() or "unauthorized" in stderr.lower():
            raise RuntimeError(
                "rmapi is not authenticated. Run 'rmapi' interactively to log in "
                "with a code from my.remarkable.com."
            )

        raise RuntimeError(f"rmapi put failed: {stderr}")

    logger.info("Uploaded successfully: %s → %s", pdf_path.name, folder)
