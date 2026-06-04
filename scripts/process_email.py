#!/usr/bin/env python3
"""Process incoming newsletter emails via IMAP into raw newsletter digests."""

import email
import email.policy
import imaplib
import json
import logging
import os
import re
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup


HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
PROFILE_ROOT = HERMES_HOME.parent
AI_TOPICS_REPO = Path(os.environ.get("AI_TOPICS_REPO", str(PROFILE_ROOT / "ai-topics")))
WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", str(AI_TOPICS_REPO / "wiki")))
WIKI_RAW_NEWSLETTERS = WIKI_ROOT / "raw" / "newsletters"
LOG_FILE = PROFILE_ROOT / "logs" / "email_processor.log"
PROCESSED_DB = HERMES_HOME / "processed_emails.json"
CHECKPOINT_DIR = HERMES_HOME / "cron" / "data" / "newsletter"
LATEST_CHECKPOINT = CHECKPOINT_DIR / "latest.json"

IMAP_HOST = os.environ.get("EMAIL_IMAP_HOST")
IMAP_PORT = int(os.environ.get("EMAIL_IMAP_PORT", "993"))
IMAP_USER = os.environ.get("EMAIL_ADDRESS")
IMAP_PASS = os.environ.get("EMAIL_PASSWORD")
IMAP_FOLDER = os.environ.get("EMAIL_FOLDER", "INBOX")
IMAP_PROCESSED = os.environ.get("EMAIL_PROCESSED_FOLDER", "Processed")
MAX_MESSAGES = int(os.environ.get("EMAIL_MAX_MESSAGES", "50"))

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stderr),
    ],
)
log = logging.getLogger(__name__)


def load_processed() -> set:
    if PROCESSED_DB.exists():
        data = json.loads(PROCESSED_DB.read_text())
        return set(data.get("message_ids", []))
    return set()


def save_processed(ids: set):
    PROCESSED_DB.parent.mkdir(parents=True, exist_ok=True)
    PROCESSED_DB.write_text(json.dumps({"message_ids": list(ids)}, indent=2))


def extract_links_from_html(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for anchor in soup.find_all("a", href=True):
        href = anchor["href"].strip()
        if not href.startswith(("http://", "https://")):
            continue
        parsed = urlparse(href)
        skip_domains = [
            "unsubscribe", "manage", "preferences", "tracking",
            "click.", "list-manage", "mailchimp", "beehiiv.com/unsubscribe",
        ]
        skip_paths = [
            "/unsubscribe", "/manage", "/preferences", "/privacy",
            "/terms", "/about", "/contact",
        ]
        domain = parsed.netloc.lower()
        path = parsed.path.lower()
        if any(token in domain for token in skip_domains):
            continue
        if any(path.startswith(token) for token in skip_paths):
            continue
        links.append(href)
    return list(dict.fromkeys(links))


def extract_links_from_text(text: str) -> list[str]:
    urls = re.findall(r'https?://[^\s<>"\')]+', text)
    return list(dict.fromkeys(urls))


def safe_slug(text: str, limit: int = 80) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:limit] or "newsletter"


def save_newsletter_digest(subject: str, date_str: str, links: list[str], source_label: str) -> Path:
    WIKI_RAW_NEWSLETTERS.mkdir(parents=True, exist_ok=True)
    filename = f"{date_str}-{safe_slug(subject)}.md"
    filepath = WIKI_RAW_NEWSLETTERS / filename
    safe_subject = subject.replace('"', '\\"')
    lines = [
        "---\n",
        f"title: \"{safe_subject}\"\n",
        f"date: {date_str}\n",
        f"processed_at: {datetime.now(timezone.utc).isoformat()}\n",
        f"source_label: \"{source_label}\"\n",
        "tags: [newsletter, raw]\n",
        "---\n\n",
        f"# Newsletter Digest - {date_str}\n\n",
        f"**Subject:** {subject}\n",
        f"**Collected:** {datetime.now(timezone.utc).isoformat()}\n",
        f"**Articles linked:** {len(links)}\n\n",
    ]
    for idx, url in enumerate(links, 1):
        lines.append(f"## {idx}. Link\n\n")
        lines.append(f"- **URL:** {url}\n\n")
    filepath.write_text("".join(lines), encoding="utf-8")
    log.info(f"Saved raw newsletter: {filepath}")
    return filepath


def process_email_message(msg, source_label: str) -> dict:
    msg_id = msg.get("Message-ID", source_label)
    subject = msg.get("Subject", "(no subject)")

    try:
        date = parsedate_to_datetime(msg.get("Date", ""))
        date_str = date.strftime("%Y-%m-%d")
    except Exception:
        date_str = datetime.now().strftime("%Y-%m-%d")

    html_body = None
    text_body = None
    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            if ct == "text/html" and not html_body:
                html_body = part.get_content()
            elif ct == "text/plain" and not text_body:
                text_body = part.get_content()
    else:
        ct = msg.get_content_type()
        if ct == "text/html":
            html_body = msg.get_content()
        elif ct == "text/plain":
            text_body = msg.get_content()

    links = extract_links_from_html(html_body) if html_body else extract_links_from_text(text_body or "")
    unique_links = links[:20]
    raw_path = save_newsletter_digest(subject, date_str, unique_links, source_label) if unique_links else None
    return {
        "message_id": msg_id,
        "subject": subject,
        "date": date_str,
        "source_label": source_label,
        "raw_path": str(raw_path) if raw_path else None,
        "article_count": len(unique_links),
        "articles": [{"title": f"Link {i + 1}", "url": url} for i, url in enumerate(unique_links)],
    }


def _require_env():
    missing = [name for name, value in {
        "EMAIL_IMAP_HOST": IMAP_HOST,
        "EMAIL_ADDRESS": IMAP_USER,
        "EMAIL_PASSWORD": IMAP_PASS,
    }.items() if not value]
    if missing:
        log.error(f"Missing required env vars: {', '.join(missing)}")
        sys.exit(2)


def _ensure_folder_exists(client: imaplib.IMAP4_SSL, folder: str):
    typ, _ = client.create(folder)
    if typ not in ("OK", "NO"):
        log.warning(f"Unexpected response creating folder {folder!r}: {typ}")


def process_all_unseen() -> dict:
    _require_env()
    processed_ids = load_processed()
    new_processed = set()
    processed_messages = []

    with imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT) as client:
        client.login(IMAP_USER, IMAP_PASS)
        _ensure_folder_exists(client, IMAP_PROCESSED)

        typ, _ = client.select(IMAP_FOLDER)
        if typ != "OK":
            log.error(f"Cannot select folder {IMAP_FOLDER!r}")
            sys.exit(3)

        typ, data = client.uid("SEARCH", "UNSEEN")
        if typ != "OK":
            log.error("UNSEEN search failed")
            sys.exit(3)

        uids = data[0].split()
        if not uids:
            return {
                "ok": True,
                "processed_count": 0,
                "processed_messages": [],
                "checkpoint_path": str(LATEST_CHECKPOINT),
            }

        for uid in uids[:MAX_MESSAGES]:
            try:
                typ, msg_data = client.uid("FETCH", uid, "(RFC822)")
                if typ != "OK" or not msg_data or not msg_data[0]:
                    log.warning(f"Fetch failed for uid={uid.decode()}")
                    continue
                raw = msg_data[0][1]
                msg = email.message_from_bytes(raw, policy=email.policy.default)
                msg_id = msg.get("Message-ID") or f"uid-{uid.decode()}"

                if msg_id in processed_ids:
                    client.uid("COPY", uid, IMAP_PROCESSED)
                    client.uid("STORE", uid, "+FLAGS", r"(\Seen \Deleted)")
                    continue

                result = process_email_message(msg, source_label=f"uid={uid.decode()}")
                processed_messages.append(result)
                new_processed.add(msg_id)
                client.uid("COPY", uid, IMAP_PROCESSED)
                client.uid("STORE", uid, "+FLAGS", r"(\Seen \Deleted)")
            except Exception as exc:
                log.error(f"Error on uid={uid.decode()}: {exc}", exc_info=True)

        client.expunge()

    if new_processed:
        processed_ids.update(new_processed)
        save_processed(processed_ids)

    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    archive_path = CHECKPOINT_DIR / f"newsletter_{run_id}.json"
    payload = {
        "ok": True,
        "run_id": run_id,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "processed_count": len(processed_messages),
        "processed_messages": processed_messages,
        "checkpoint_path": str(LATEST_CHECKPOINT),
        "archive_path": str(archive_path),
    }
    data = json.dumps(payload, indent=2, ensure_ascii=False)
    LATEST_CHECKPOINT.write_text(data, encoding="utf-8")
    archive_path.write_text(data, encoding="utf-8")
    return payload


if __name__ == "__main__":
    try:
        result = process_all_unseen()
        sys.stdout.write(json.dumps(result, indent=2, ensure_ascii=False))
    except imaplib.IMAP4.error as exc:
        log.error(f"IMAP error: {exc}")
        sys.exit(4)
