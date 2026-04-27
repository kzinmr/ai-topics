#!/usr/bin/env python3
"""Process incoming newsletter emails via IMAP.

Connects to an IMAP mailbox, fetches UNSEEN messages from the configured
folder, extracts links, scrapes content, saves raw articles to the wiki,
and pushes to the ai-topics repo. Successfully processed messages are
marked Seen and moved to the configured "processed" folder (Gmail label).

Environment variables:
    EMAIL_IMAP_HOST           IMAP server host (required, e.g. imap.gmail.com)
    EMAIL_IMAP_PORT           IMAP server port (default: 993)
    EMAIL_ADDRESS             Mailbox login (required)
    EMAIL_PASSWORD            Mailbox password / app password (required)
    EMAIL_FOLDER              Source folder to poll (default: INBOX)
    EMAIL_PROCESSED_FOLDER    Destination folder after success (default: Processed)
    EMAIL_MAX_MESSAGES        Cap per run (default: 50)
    HERMES_HOME               Hermes state dir (default: ~/.hermes)
    AI_TOPICS_REPO            ai-topics clone path (default: ~/ai-topics)

Exits 0 on success (even if 0 messages processed).
"""
import email
import email.policy
import hashlib
import imaplib
import json
import logging
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup
from readability import Document


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
PROFILE_ROOT = HERMES_HOME.parent
AI_TOPICS_REPO = Path(os.environ.get("AI_TOPICS_REPO", str(PROFILE_ROOT / "ai-topics")))
WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", str(AI_TOPICS_REPO / "wiki")))
WIKI_RAW = WIKI_ROOT / "raw" / "articles"
INBOX_DIR = AI_TOPICS_REPO / "inbox" / "newsletters"
LOG_FILE = PROFILE_ROOT / "logs" / "email_processor.log"
PROCESSED_DB = HERMES_HOME / "processed_emails.json"

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
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)

HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; HermesBot/1.0)",
    "Accept": "text/html,application/xhtml+xml",
}


# ---------------------------------------------------------------------------
# Dedup DB (Message-ID based, belt + suspenders on top of IMAP \Seen flag)
# ---------------------------------------------------------------------------
def load_processed() -> set:
    if PROCESSED_DB.exists():
        data = json.loads(PROCESSED_DB.read_text())
        return set(data.get("message_ids", []))
    return set()


def save_processed(ids: set):
    PROCESSED_DB.parent.mkdir(parents=True, exist_ok=True)
    PROCESSED_DB.write_text(json.dumps({"message_ids": list(ids)}, indent=2))


# ---------------------------------------------------------------------------
# Link extraction / scraping — unchanged from the Maildir version
# ---------------------------------------------------------------------------
def extract_links_from_html(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
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
        if any(s in domain for s in skip_domains):
            continue
        if any(path.startswith(s) for s in skip_paths):
            continue
        links.append(href)
    seen = set()
    unique = []
    for link in links:
        if link not in seen:
            seen.add(link)
            unique.append(link)
    return unique


def extract_links_from_text(text: str) -> list[str]:
    urls = re.findall(r'https?://[^\s<>"\')]+', text)
    return list(dict.fromkeys(urls))


def scrape_url(url: str) -> dict | None:
    try:
        with httpx.Client(timeout=30, follow_redirects=True, headers=HTTP_HEADERS) as client:
            resp = client.get(url)
            resp.raise_for_status()
    except Exception as e:
        log.warning(f"Failed to fetch {url}: {e}")
        return None

    content_type = resp.headers.get("content-type", "")
    if "text/html" not in content_type:
        log.info(f"Skipping non-HTML: {url} ({content_type})")
        return None

    try:
        doc = Document(resp.text)
        title = doc.short_title() or "Untitled"
        summary_html = doc.summary()
        soup = BeautifulSoup(summary_html, "html.parser")
        content = soup.get_text(separator="\n", strip=True)
    except Exception as e:
        log.warning(f"Failed to parse {url}: {e}")
        return None

    if len(content) < 100:
        log.info(f"Skipping short content ({len(content)} chars): {url}")
        return None

    return {
        "url": url,
        "title": title,
        "content": content,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


def url_to_filename(url: str) -> str:
    h = hashlib.md5(url.encode()).hexdigest()[:8]
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")
    slug = re.sub(r"[^a-z0-9]+", "-", parsed.path.lower()).strip("-")[:60]
    return f"{domain}--{slug}--{h}"


def save_article(article: dict, date_str: str) -> Path:
    fname = url_to_filename(article["url"])
    filepath = WIKI_RAW / f"{fname}.md"
    WIKI_RAW.mkdir(parents=True, exist_ok=True)
    frontmatter = (
        f"---\n"
        f"title: \"{article['title']}\"\n"
        f"url: \"{article['url']}\"\n"
        f"fetched_at: {article['fetched_at']}\n"
        f"source_date: {date_str}\n"
        f"tags: [newsletter, auto-ingested]\n"
        f"---\n\n"
    )
    body = f"# {article['title']}\n\nSource: {article['url']}\n\n{article['content']}\n"
    filepath.write_text(frontmatter + body, encoding="utf-8")
    log.info(f"Saved: {filepath.name}")
    return filepath


def save_to_ai_topics(articles: list[dict], email_subject: str, date_str: str):
    if not articles:
        return

    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    fname = f"{date_str}-newsletter.md"
    filepath = INBOX_DIR / fname

    lines = [
        f"# Newsletter Digest - {date_str}\n",
        f"**Subject:** {email_subject}\n",
        f"**Processed:** {datetime.now(timezone.utc).isoformat()}\n",
        f"**Articles scraped:** {len(articles)}\n\n",
        "---\n\n",
    ]
    for i, art in enumerate(articles, 1):
        lines.append(f"## {i}. {art['title']}\n\n")
        lines.append(f"- **URL:** {art['url']}\n")
        lines.append(f"- **Length:** {len(art['content'])} chars\n\n")
        preview = art["content"][:500].replace("\n", "\n> ")
        lines.append(f"> {preview}\n\n")

    filepath.write_text("".join(lines), encoding="utf-8")
    log.info(f"Saved ai-topics: {filepath}")

    try:
        repo = AI_TOPICS_REPO
        subprocess.run(["git", "add", "inbox/", "wiki/"], cwd=repo, check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", f"wiki: newsletter digest {date_str}"],
            cwd=repo, check=True, capture_output=True,
        )
        subprocess.run(["git", "push"], cwd=repo, check=True, capture_output=True)
        log.info("Pushed to ai-topics repo")
    except subprocess.CalledProcessError as e:
        log.warning(f"Git push failed: {e.stderr.decode() if e.stderr else e}")


# ---------------------------------------------------------------------------
# Message processing — takes an already-parsed email.message.EmailMessage
# ---------------------------------------------------------------------------
def process_email_message(msg, source_label: str) -> bool:
    """Process a parsed email message. Returns True if processed (even if 0 articles)."""
    msg_id = msg.get("Message-ID", source_label)
    subject = msg.get("Subject", "(no subject)")
    from_addr = msg.get("From", "")
    delivered_to = msg.get("Delivered-To", "")

    log.info(f"Processing: {source_label}")
    log.info(f"  Message-ID: {msg_id}")
    log.info(f"  From: {from_addr}")
    log.info(f"  Subject: {subject}")
    log.info(f"  Delivered-To: {delivered_to}")

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

    links = []
    if html_body:
        links = extract_links_from_html(html_body)
    elif text_body:
        links = extract_links_from_text(text_body)

    log.info(f"  Found {len(links)} links")
    if not links:
        log.info("  No links to process")
        return True

    MAX_LINKS = 20
    articles = []
    for url in links[:MAX_LINKS]:
        article = scrape_url(url)
        if article:
            save_article(article, date_str)
            articles.append(article)

    log.info(f"  Scraped {len(articles)} articles")
    save_to_ai_topics(articles, subject, date_str)
    return True


# ---------------------------------------------------------------------------
# IMAP driver
# ---------------------------------------------------------------------------
def _require_env():
    missing = [k for k, v in {
        "EMAIL_IMAP_HOST": IMAP_HOST,
        "EMAIL_ADDRESS": IMAP_USER,
        "EMAIL_PASSWORD": IMAP_PASS,
    }.items() if not v]
    if missing:
        log.error(f"Missing required env vars: {', '.join(missing)}")
        sys.exit(2)


def _ensure_folder_exists(M: imaplib.IMAP4_SSL, folder: str):
    """Create the folder if it doesn't exist. Gmail ignores for existing labels."""
    typ, _ = M.create(folder)
    # Gmail returns 'NO' if already exists — that's fine
    if typ not in ("OK", "NO"):
        log.warning(f"Unexpected response creating folder {folder!r}: {typ}")


def process_all_unseen():
    _require_env()

    processed_ids = load_processed()
    new_processed = set()

    log.info(f"Connecting to {IMAP_HOST}:{IMAP_PORT} as {IMAP_USER}")
    with imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT) as M:
        M.login(IMAP_USER, IMAP_PASS)
        _ensure_folder_exists(M, IMAP_PROCESSED)

        typ, _ = M.select(IMAP_FOLDER)
        if typ != "OK":
            log.error(f"Cannot select folder {IMAP_FOLDER!r}")
            sys.exit(3)

        typ, data = M.search(None, "UNSEEN")
        if typ != "OK":
            log.error("UNSEEN search failed")
            sys.exit(3)

        uids = data[0].split()
        if not uids:
            log.info("No unseen messages")
            return

        uids = uids[:MAX_MESSAGES]
        log.info(f"Found {len(uids)} unseen message(s); cap={MAX_MESSAGES}")

        for uid in uids:
            try:
                typ, msg_data = M.fetch(uid, "(RFC822)")
                if typ != "OK" or not msg_data or not msg_data[0]:
                    log.warning(f"Fetch failed for uid={uid.decode()}")
                    continue
                raw = msg_data[0][1]
                msg = email.message_from_bytes(raw, policy=email.policy.default)
                msg_id = msg.get("Message-ID") or f"uid-{uid.decode()}"

                if msg_id in processed_ids:
                    log.info(f"Skipping already-processed msg_id={msg_id}")
                    # Still move it out of the way
                    M.copy(uid, IMAP_PROCESSED)
                    M.store(uid, "+FLAGS", r"(\Seen \Deleted)")
                    continue

                ok = process_email_message(msg, source_label=f"uid={uid.decode()}")

                if ok:
                    new_processed.add(msg_id)
                    # COPY then mark Seen + Deleted, expunge moves it out of INBOX
                    M.copy(uid, IMAP_PROCESSED)
                    M.store(uid, "+FLAGS", r"(\Seen \Deleted)")
                else:
                    # Keep UNSEEN so next run retries
                    log.warning(f"Processing failed; leaving uid={uid.decode()} in INBOX")

            except Exception as e:
                log.error(f"Error on uid={uid.decode()}: {e}", exc_info=True)
                # Don't mark seen — retry next run

        M.expunge()

    if new_processed:
        processed_ids.update(new_processed)
        save_processed(processed_ids)
        log.info(f"Processed {len(new_processed)} new message(s)")


if __name__ == "__main__":
    try:
        process_all_unseen()
    except imaplib.IMAP4.error as e:
        log.error(f"IMAP error: {e}")
        sys.exit(4)
