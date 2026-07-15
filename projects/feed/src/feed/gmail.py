"""Gmail API authentication and email fetching."""

import base64
import logging
from dataclasses import dataclass
from email.utils import parseaddr
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


@dataclass
class Email:
    """A single email message with parsed content."""
    message_id: str
    subject: str
    sender: str
    date: str
    html_body: str | None


def authenticate(credentials_path: Path, token_path: Path) -> Credentials:
    """Authenticate with Gmail API. Opens browser on first run."""
    creds = None

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if creds and creds.expired and creds.refresh_token:
        try:
            logger.info("Refreshing expired OAuth token")
            creds.refresh(Request())
            token_path.write_text(creds.to_json())
        except Exception:
            logger.warning("Token refresh failed — will re-authenticate")
            creds = None

    if not creds or not creds.valid:
        if not credentials_path.exists():
            raise FileNotFoundError(
                f"OAuth credentials not found at {credentials_path}\n"
                "Download credentials.json from Google Cloud Console:\n"
                "  1. Go to console.cloud.google.com\n"
                "  2. Create a project, enable Gmail API\n"
                "  3. Create OAuth 2.0 credentials (Desktop app)\n"
                "  4. Download and save as {credentials_path}"
            )

        logger.info("Starting OAuth2 flow — a browser window will open")
        flow = InstalledAppFlow.from_client_secrets_file(
            str(credentials_path), SCOPES
        )
        creds = flow.run_local_server(port=0)

        token_path.parent.mkdir(parents=True, exist_ok=True)
        token_path.write_text(creds.to_json())
        logger.info("OAuth token saved to %s", token_path)

    return creds


def get_service(creds: Credentials):
    """Build the Gmail API service client."""
    return build("gmail", "v1", credentials=creds)


def find_label_id(service, label_name: str) -> str | None:
    """Look up the Gmail label ID by name."""
    results = service.users().labels().list(userId="me").execute()
    for label in results.get("labels", []):
        if label["name"] == label_name:
            return label["id"]
    return None


def fetch_emails(
    service,
    label_name: str,
    max_results: int = 20,
    exclude_ids: set[str] | None = None,
) -> list[Email]:
    """Fetch the newest labeled emails that haven't been processed yet.

    Filters by label + processed-ID rather than by date, so emails
    labeled late (days after they arrived) still get picked up.
    Paginates past already-processed messages until max_results new
    emails are collected or the label is exhausted.
    """
    label_id = find_label_id(service, label_name)
    if not label_id:
        logger.error(
            "Label '%s' not found in Gmail — create it and label some emails",
            label_name,
        )
        return []

    logger.info("Querying Gmail: label=%s max=%d", label_name, max_results)

    exclude = exclude_ids or set()
    emails: list[Email] = []
    page_token = None
    pages = 0

    while len(emails) < max_results and pages < 10:
        results = service.users().messages().list(
            userId="me",
            labelIds=[label_id],
            maxResults=100,
            pageToken=page_token,
        ).execute()
        pages += 1

        for ref in results.get("messages", []):
            if len(emails) >= max_results:
                break
            if ref["id"] in exclude:
                logger.debug("Skipping already-processed message %s", ref["id"])
                continue

            email = _parse_message(service, ref["id"])
            if email:
                emails.append(email)
                logger.info("  [%s] %s", email.sender, email.subject)

        page_token = results.get("nextPageToken")
        if not page_token:
            break

    if not emails:
        logger.info("No new emails found with label '%s'", label_name)

    return emails


def _parse_message(service, msg_id: str) -> Email | None:
    """Fetch and parse a single Gmail message."""
    try:
        message = service.users().messages().get(
            userId="me", id=msg_id, format="full"
        ).execute()
        headers = message["payload"].get("headers", [])
        subject = _get_header(headers, "Subject")
        sender = _clean_sender(_get_header(headers, "From"))
        date = _get_header(headers, "Date")
        html_body = _extract_html_body(message["payload"])
    except Exception:
        logger.exception("Failed to fetch or parse message %s", msg_id)
        return None

    return Email(
        message_id=msg_id,
        subject=subject,
        sender=sender,
        date=date,
        html_body=html_body,
    )


def _clean_sender(raw: str) -> str:
    """Reduce 'Bon Appétit <newsletter@bonappetit.com>' to just the display name."""
    name, addr = parseaddr(raw)
    return name or addr or raw


def _get_header(headers: list[dict], name: str) -> str:
    """Extract a header value by name."""
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return ""


def _extract_html_body(payload: dict) -> str | None:
    """Walk MIME parts to find the text/html body."""
    if "parts" in payload:
        for part in payload["parts"]:
            if part.get("mimeType") == "text/html":
                data = part.get("body", {}).get("data")
                if data:
                    return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
            # Recurse into nested multipart
            result = _extract_html_body(part)
            if result:
                return result
    else:
        if payload.get("mimeType") == "text/html":
            data = payload.get("body", {}).get("data")
            if data:
                return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
    return None
