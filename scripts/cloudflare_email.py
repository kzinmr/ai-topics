#!/usr/bin/env python3
"""
Cloudflare Email Sending — Hermes email delivery module.

Implements a single helper function (`send_email_via_cloudflare`) following
the design principles from Pieter Levels' migration prompt:
  - Single function, no API details leaked to callers
  - Timeout handling (5s connect, 15s total)
  - Parses bounce/error responses
  - Reads credentials from environment variables

Env vars required:
  CF_ACCOUNT_ID        — Cloudflare account ID
  CF_EMAIL_API_TOKEN   — API token with email_sending:write scope
  CF_EMAIL_FROM        — Default sender (address or "Name <address>")
  CF_EMAIL_TO          — Default recipient (comma-separated for multiple)
  CF_EMAIL_SUBJECT_PREFIX — Optional prefix for subject lines (e.g. "[Hermes]")

Usage:
  from cloudflare_email import send_email_via_cloudflare

  success = send_email_via_cloudflare(
      subject="Daily AI Topics Report",
      html="<h1>Today's Highlights</h1><p>...</p>",
      text="Today's Highlights\n...",
  )
"""

import os
import json
import time
import logging
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

logger = logging.getLogger("cloudflare_email")

# ── Configuration from environment ────────────────────────────────────────
CF_ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID", "")
CF_EMAIL_API_TOKEN = os.environ.get("CF_EMAIL_API_TOKEN", "")
CF_EMAIL_FROM = os.environ.get("CF_EMAIL_FROM", "hermes@kusari.cc")
CF_EMAIL_TO = os.environ.get("CF_EMAIL_TO", "")
CF_EMAIL_SUBJECT_PREFIX = os.environ.get("CF_EMAIL_SUBJECT_PREFIX", "[Hermes Report]")
CF_API_ENDPOINT = f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT_ID}/email/sending/send"


def _parse_sender(from_str: str) -> dict:
    """Parse 'Name <email>' or 'email' into {address, name} dict."""
    from_str = from_str.strip()
    if "<" in from_str and ">" in from_str:
        name, rest = from_str.split("<", 1)
        address = rest.split(">", 1)[0].strip()
        return {"address": address, "name": name.strip()}
    return {"address": from_str}


def send_email_via_cloudflare(
    subject: str,
    html: str = "",
    text: str = "",
    to: str = "",
    from_addr: str = "",
    cc: list[str] | None = None,
    bcc: list[str] | None = None,
    reply_to: str = "",
    headers: dict[str, str] | None = None,
    attachments: list[dict] | None = None,
    timeout: tuple[float, float] = (5.0, 15.0),
) -> bool:
    """
    Send an email via Cloudflare Email Service REST API.

    Returns True on success (HTTP 200 + success:true + no permanent_bounces).
    Returns False on any failure (logs details).

    Args:
        subject: Email subject line (CF_EMAIL_SUBJECT_PREFIX will be prepended)
        html: HTML body (optional if text provided)
        text: Plain text body (optional if html provided)
        to: Recipient(s). Comma/space-separated string or single address.
            Defaults to CF_EMAIL_TO.
        from_addr: Sender. "Name <email>" or "email". Defaults to CF_EMAIL_FROM.
        cc, bcc: Optional CC/BCC recipients.
        reply_to: Optional reply-to address.
        headers: Optional custom headers dict.
        attachments: Optional list of {content, filename, type, disposition} dicts.
        timeout: (connect_timeout, read_timeout) in seconds.
    """
    if not CF_ACCOUNT_ID or not CF_EMAIL_API_TOKEN:
        logger.error("CF_ACCOUNT_ID or CF_EMAIL_API_TOKEN not set in environment")
        return False

    # Resolve recipients
    to_addr = to or CF_EMAIL_TO
    if not to_addr:
        logger.error("No recipient specified (set CF_EMAIL_TO or pass 'to' param)")
        return False

    # Parse "to" — accept "a@b.com, c@d.com" or single string
    if isinstance(to_addr, str) and "," in to_addr:
        to_list = [a.strip() for a in to_addr.split(",") if a.strip()]
    elif isinstance(to_addr, str):
        to_list = [to_addr.strip()]
    else:
        to_list = to_addr

    # Resolve sender
    sender_str = from_addr or CF_EMAIL_FROM
    sender = _parse_sender(sender_str)

    # Build request body
    body: dict = {
        "to": to_list,
        "from": sender,
        "subject": f"{CF_EMAIL_SUBJECT_PREFIX} {subject}",
    }

    if html:
        body["html"] = html
    if text:
        body["text"] = text
    if cc:
        body["cc"] = cc
    if bcc:
        body["bcc"] = bcc
    if reply_to:
        body["reply_to"] = reply_to
    if headers:
        body["headers"] = headers
    if attachments:
        body["attachments"] = attachments

    # Ensure at least one of html/text
    if not html and not text:
        logger.error("Neither html nor text body provided")
        return False

    # Send
    payload = json.dumps(body).encode("utf-8")
    req = Request(
        CF_API_ENDPOINT,
        data=payload,
        headers={
            "Authorization": f"Bearer {CF_EMAIL_API_TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    start = time.time()
    try:
        resp = urlopen(req, timeout=timeout)
        elapsed = time.time() - start
        raw = resp.read().decode("utf-8")
    except HTTPError as e:
        elapsed = time.time() - start
        logger.error(
            "Cloudflare Email API HTTP %d after %.2fs: %s",
            e.code, elapsed, e.read().decode("utf-8", errors="replace")[:500]
        )
        return False
    except URLError as e:
        elapsed = time.time() - start
        logger.error("Cloudflare Email API network error after %.2fs: %s", elapsed, e.reason)
        return False
    except Exception as e:
        elapsed = time.time() - start
        logger.error("Cloudflare Email API unexpected error after %.2fs: %s", elapsed, e)
        return False

    # Parse response
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        logger.error("Cloudflare Email API non-JSON response: %s", raw[:500])
        return False

    if not data.get("success"):
        errors = data.get("errors", [])
        logger.error("Cloudflare Email API returned failure: %s", json.dumps(errors)[:500])
        return False

    result = data.get("result", {})
    permanent_bounces = result.get("permanent_bounces", [])
    if permanent_bounces:
        logger.warning(
            "Cloudflare Email: permanent bounces for %s (delivered=%d, queued=%d)",
            permanent_bounces,
            len(result.get("delivered", [])),
            len(result.get("queued", []))
        )
        # Treat as soft failure — some recipients bounced
        if not result.get("delivered") and not result.get("queued"):
            return False

    delivered = len(result.get("delivered", []))
    queued = len(result.get("queued", []))
    logger.info(
        "Cloudflare Email sent in %.2fs: %d delivered, %d queued, %d bounced",
        elapsed, delivered, queued, len(permanent_bounces)
    )
    return True


# ── CLI interface for cron scripts ────────────────────────────────────────
if __name__ == "__main__":
    import sys
    import argparse

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    parser = argparse.ArgumentParser(description="Send email via Cloudflare Email Service")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--html-file", help="Path to HTML body file")
    parser.add_argument("--text-file", help="Path to plain text body file")
    parser.add_argument("--html", help="HTML body string")
    parser.add_argument("--text", help="Plain text body string")
    parser.add_argument("--to", help="Override recipient(s)")
    parser.add_argument("--from", dest="from_addr", help="Override sender")
    parser.add_argument("--dry-run", action="store_true", help="Validate config only, don't send")
    args = parser.parse_args()

    # Validate config
    if not CF_ACCOUNT_ID:
        print("ERROR: CF_ACCOUNT_ID not set", file=sys.stderr)
        sys.exit(2)
    if not CF_EMAIL_API_TOKEN:
        print("ERROR: CF_EMAIL_API_TOKEN not set", file=sys.stderr)
        sys.exit(2)

    if args.dry_run:
        print(f"DRY RUN: Would send to {args.to or CF_EMAIL_TO}")
        print(f"  From: {args.from_addr or CF_EMAIL_FROM}")
        print(f"  Subject: {args.subject}")
        print("  Config valid ✓")
        sys.exit(0)

    # Read body from files or args
    html_body = args.html or ""
    text_body = args.text or ""
    if args.html_file:
        with open(args.html_file) as f:
            html_body = f.read()
    if args.text_file:
        with open(args.text_file) as f:
            text_body = f.read()

    success = send_email_via_cloudflare(
        subject=args.subject,
        html=html_body,
        text=text_body,
        to=args.to,
        from_addr=args.from_addr,
    )

    sys.exit(0 if success else 1)
