"""Send the magazine PDF to reMarkable via email."""

import logging
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

logger = logging.getLogger(__name__)

GMAIL_SMTP_HOST = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587


def send_to_remarkable(
    pdf_path: Path,
    sender: str,
    app_password: str,
    remarkable_email: str,
) -> None:
    """Send a PDF as an email attachment to the reMarkable tablet."""
    logger.info(
        "Sending '%s' from %s to %s",
        pdf_path.name, sender, remarkable_email,
    )

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = remarkable_email
    msg["Subject"] = f"Feed — {pdf_path.stem}"

    body = "Your latest Feed magazine is attached."
    msg.attach(MIMEText(body, "plain"))

    # Attach the PDF
    with open(pdf_path, "rb") as f:
        part = MIMEBase("application", "pdf")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={pdf_path.name}",
    )
    msg.attach(part)

    # Send via Gmail SMTP
    with smtplib.SMTP(GMAIL_SMTP_HOST, GMAIL_SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, app_password)
        server.send_message(msg)

    logger.info("Email sent successfully")
