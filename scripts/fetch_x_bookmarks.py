#!/usr/bin/env python3
"""Pre-run script: fetch X bookmarks via xurl, output JSON for the agent.

Requires OAuth2 user authentication (bookmarks are user-private data,
Bearer/app-only won't work). Dedups against
~/.hermes/processed_x_bookmarks.json.

Cost note: this script intentionally does not unbookmark fetched posts. It uses
the raw bookmarks endpoint with pagination and stops once it reaches a page
that has already been emitted before. That keeps the steady-state cost to one
X API request per run when there are <=100 new bookmarks.
"""
import json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

XURL = os.environ.get("XURL_PATH", "/opt/data/bin/xurl")

HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
DB = HERMES_HOME / "processed_x_bookmarks.json"
DETAIL_DIR = HERMES_HOME / "cron" / "data"
DETAIL_FILE = DETAIL_DIR / "x_bookmarks_latest_full.json"
ARCHIVE_DIR = DETAIL_DIR / "x_bookmarks_archive"
MAX_PAGES = int(os.environ.get("HERMES_X_BOOKMARKS_MAX_PAGES", "0"))

REQUESTS_ATTEMPTED = 0

# Invisible Unicode code points that trip the cron injection scanner.
# X/Twitter API sometimes returns text with embedded zero-width spaces (U+200B)
# from copy-pasted content. Strip these before they reach the agent prompt.
_INVISIBLE_CHARS = "\u200b\u200c\u200d\u2060\u2061\u2062\u2063\u2064\ufeff"


def _sanitize_text(s):
    """Strip invisible Unicode from a string."""
    if not isinstance(s, str):
        return s
    return s.translate(str.maketrans("", "", _INVISIBLE_CHARS))


def _sanitize_bookmark(t):
    """Recursively sanitize text fields in a bookmark dict."""
    for key in ("text",):
        if key in t and isinstance(t[key], str):
            t[key] = _sanitize_text(t[key])
    # Also sanitize URL expanded_url fields
    for u in t.get("entities", {}).get("urls", []):
        for field in ("expanded_url", "display_url", "title", "description"):
            if field in u and isinstance(u[field], str):
                u[field] = _sanitize_text(u[field])
    return t


class XurlError(RuntimeError):
    pass


def run(*args):
    global REQUESTS_ATTEMPTED
    REQUESTS_ATTEMPTED += 1
    try:
        return subprocess.run(
            [XURL, "--auth", "oauth2", *args],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except subprocess.CalledProcessError as e:
        detail = (e.stderr or e.stdout or "").strip()
        raise XurlError(detail) from e


def load_state(path):
    if not path.exists():
        return {}, set()
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}, set()
    processed = set(str(tweet_id) for tweet_id in data.get("tweet_ids", []))
    return data, processed


def get_user_id(state):
    user_id = str(state.get("user_id") or "").strip()
    if user_id:
        return user_id
    data = json.loads(run("/2/users/me"))
    return data.get("data", {}).get("id")


def fetch_bookmarks_page(user_id, pagination_token=None):
    params = {
        "max_results": "100",
        "tweet.fields": "created_at,entities,referenced_tweets",
    }
    if pagination_token:
        params["pagination_token"] = pagination_token
    return json.loads(run(f"/2/users/{user_id}/bookmarks?{urlencode(params)}"))


state, processed = load_state(DB)

try:
    user_id = get_user_id(state)
    if not user_id:
        raise XurlError("could not resolve authenticated user id")

    new = []
    seen_this_run = set()
    pagination_token = None
    pages_fetched = 0
    stop_reason = "end"

    while True:
        if MAX_PAGES > 0 and pages_fetched >= MAX_PAGES:
            stop_reason = "max_pages"
            break

        resp = fetch_bookmarks_page(user_id, pagination_token)
        pages_fetched += 1
        page = resp.get("data", []) or []
        page_new = [
            t for t in page
            if str(t.get("id")) not in processed and str(t.get("id")) not in seen_this_run
        ]

        for t in page_new:
            tweet_id = str(t.get("id"))
            if tweet_id:
                seen_this_run.add(tweet_id)
            _sanitize_bookmark(t)
            t["external_urls"] = [
                u["expanded_url"]
                for u in t.get("entities", {}).get("urls", [])
                if u.get("expanded_url", "").startswith(("http://", "https://"))
                and "x.com" not in u["expanded_url"]
                and "twitter.com" not in u["expanded_url"]
            ]
            new.append(t)

        if not page:
            stop_reason = "empty_page"
            break
        if not page_new:
            stop_reason = "already_processed_page"
            break

        pagination_token = resp.get("meta", {}).get("next_token")
        if not pagination_token:
            stop_reason = "no_next_token"
            break

except (XurlError, json.JSONDecodeError) as e:
    print(json.dumps({
        "error": str(e),
        "new_bookmarks": [],
        "summary": {
            "x_api_requests_attempted": REQUESTS_ATTEMPTED,
            "mode": "paged_no_unbookmark",
        },
    }), file=sys.stderr)
    sys.exit(1)

payload = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "new_bookmarks": new,
    "summary": {
        "mode": "paged_no_unbookmark",
        "pages_fetched": pages_fetched,
        "new_bookmarks": len(new),
        "processed_cache_size": len(processed),
        "x_api_requests_attempted": REQUESTS_ATTEMPTED,
        "stop_reason": stop_reason,
        "max_pages": MAX_PAGES,
        "possibly_more_unseen": stop_reason == "max_pages",
    },
}

DETAIL_DIR.mkdir(parents=True, exist_ok=True)
ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
DETAIL_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
archive_file = ARCHIVE_DIR / f"x_bookmarks_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
archive_file.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
payload["detail_file"] = str(DETAIL_FILE)
payload["archive_file"] = str(archive_file)

print(json.dumps(payload, indent=2, ensure_ascii=False))

# Mark bookmarks as emitted to the agent. The raw payload is archived above so
# failed downstream processing can be replayed without another X API read.
processed.update(str(t["id"]) for t in new if t.get("id"))
DB.parent.mkdir(parents=True, exist_ok=True)
DB.write_text(json.dumps({
    "tweet_ids": sorted(processed),
    "user_id": user_id,
    "mode": "paged_no_unbookmark",
    "last_run": payload["summary"],
}, indent=2, ensure_ascii=False))
