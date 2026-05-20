#!/usr/bin/env python3
"""Pre-run script: fetch recent posts from tracked X accounts.

Outputs a compact, agent-friendly summary by default and stores the raw payload
separately for progressive disclosure when deeper inspection is needed.
"""
import json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse

try:
    import yaml
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "-q"])
    import yaml

XURL = os.environ.get("XURL_PATH", "/opt/data/bin/xurl")

HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
PROFILE_ROOT = HERMES_HOME.parent
AI_TOPICS = Path(os.environ.get("AI_TOPICS_HOME", str(PROFILE_ROOT / "ai-topics")))
YAML_PATH = AI_TOPICS / "config" / "feeds" / "x-accounts.yaml"
DB = HERMES_HOME / "processed_x_accounts.json"
DETAIL_DIR = HERMES_HOME / "cron" / "data"
DETAIL_FILE = DETAIL_DIR / "x_accounts_latest_full.json"
ARCHIVE_DIR = DETAIL_DIR / "x_accounts_archive"
USER_ID_CACHE = DETAIL_DIR / "x_accounts_user_ids.json"
SCAN_STATE = DETAIL_DIR / "x_accounts_scan_state.json"
PROCESSED_TTL_DAYS = int(os.environ.get("HERMES_X_ACCOUNTS_TTL_DAYS", "90"))
MAX_CANDIDATES = int(os.environ.get("HERMES_X_ACCOUNTS_MAX_CANDIDATES", "12"))
RECENT_DAYS = int(os.environ.get("HERMES_X_ACCOUNTS_RECENT_DAYS", "45"))
REQUEST_BUDGET = int(os.environ.get("HERMES_X_ACCOUNTS_REQUEST_BUDGET", "12"))
USER_CACHE_TTL_DAYS = int(os.environ.get("HERMES_X_ACCOUNTS_USER_CACHE_TTL_DAYS", "90"))
TWEETS_PER_ACCOUNT = int(os.environ.get("HERMES_X_ACCOUNTS_TWEETS_PER_ACCOUNT", "10"))
SOURCE_FILE = os.environ.get("FETCH_X_ACCOUNTS_SOURCE_FILE", "").strip()
REPLAY_NO_WRITE = os.environ.get("FETCH_X_ACCOUNTS_REPLAY_NO_WRITE", "1").strip().lower() not in ("0", "false", "no")
REQUESTS_ATTEMPTED = 0

HIGH_SIGNAL_DOMAINS = (
    "github.com",
    "huggingface.co",
    "arxiv.org",
    "claude.com",
    "platform.claude.com",
    "openai.com",
    "docs.anthropic.com",
    "docs.rs",
    "pkg.go.dev",
    "agentsearch.sh",
    "interconnects.ai",
    "vercel.com",
    "nething.xyz",
)

LOW_SIGNAL_DOMAINS = (
    "discord.gg",
    "discord.com",
    "youtube.com",
    "www.youtube.com",
    "luma.com",
    "x.com",
    "twitter.com",
)

def run(*args):
    global REQUESTS_ATTEMPTED
    REQUESTS_ATTEMPTED += 1
    r = subprocess.run([XURL, "--auth", "oauth2", *args], capture_output=True, text=True)
    if r.returncode != 0:
        detail = (r.stderr or r.stdout or "").strip()
        print(f"xurl error: {detail}", file=sys.stderr)
        return None
    return r.stdout


def normalize_handle(handle):
    return str(handle).strip().lstrip("@").lower()


def load_json_file(path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return default


def load_scan_state(path):
    data = load_json_file(path, {})
    try:
        cursor = int(data.get("cursor", 0))
    except (TypeError, ValueError):
        cursor = 0
    return {"cursor": max(0, cursor)}


def save_scan_state(path, cursor):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "cursor": cursor,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }, indent=2))


def load_user_cache(path, now):
    data = load_json_file(path, {})
    users = data.get("users", {})
    if not isinstance(users, dict):
        users = {}

    valid = {}
    for handle, entry in users.items():
        if not isinstance(entry, dict) or not entry.get("id"):
            continue
        resolved_at = entry.get("resolved_at")
        if USER_CACHE_TTL_DAYS > 0 and resolved_at:
            try:
                resolved_dt = datetime.fromisoformat(str(resolved_at).replace("Z", "+00:00"))
                age_days = (now - resolved_dt).total_seconds() / 86400
                if age_days > USER_CACHE_TTL_DAYS:
                    continue
            except ValueError:
                continue
        valid[normalize_handle(handle)] = entry
    return valid


def save_user_cache(path, users):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "ttl_days": USER_CACHE_TTL_DAYS,
        "users": dict(sorted(users.items())),
    }, indent=2, ensure_ascii=False))


def get_cached_user_id(user_cache, handle):
    entry = user_cache.get(normalize_handle(handle), {})
    return str(entry.get("id") or "").strip() or None


def resolve_user_ids(handles):
    clean = []
    seen = set()
    for handle in handles:
        normalized = normalize_handle(handle)
        if normalized and normalized not in seen:
            clean.append(normalized)
            seen.add(normalized)
    if not clean:
        return {}

    params = urlencode({
        "usernames": ",".join(clean),
        "user.fields": "username,name",
    })
    out = run(f"/2/users/by?{params}")
    if not out:
        return None
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return None

    resolved = {}
    resolved_at = datetime.now(timezone.utc).isoformat()
    for user in data.get("data", []) or []:
        username = normalize_handle(user.get("username"))
        user_id = str(user.get("id") or "").strip()
        if username and user_id:
            resolved[username] = {
                "id": user_id,
                "username": user.get("username", username),
                "name": user.get("name", ""),
                "resolved_at": resolved_at,
            }
    return resolved


def get_recent_tweets(user_id, max_results=TWEETS_PER_ACCOUNT):
    params = urlencode({
        "max_results": max_results,
        "tweet.fields": "created_at,entities,referenced_tweets,note_tweet",
    })
    out = run(f"/2/users/{user_id}/tweets?{params}")
    if not out:
        return []
    try:
        data = json.loads(out)
        return data.get("data", [])
    except json.JSONDecodeError:
        return []


def is_external_url(url):
    return (
        url.startswith(("http://", "https://"))
        and "x.com" not in url
        and "twitter.com" not in url
    )


def get_external_url_entries(tweet):
    urls = []
    for entry in tweet.get("entities", {}).get("urls", []):
        expanded = entry.get("expanded_url", "")
        if not is_external_url(expanded):
            continue
        urls.append(
            {
                "url": expanded,
                "domain": urlparse(expanded).netloc,
                "title": entry.get("title", ""),
                "description": entry.get("description", ""),
                "unwound_url": entry.get("unwound_url", ""),
                "status": entry.get("status"),
            }
        )
    return urls


def is_substantive_post(tweet, external_url_entries):
    if not external_url_entries:
        return False
    text = " ".join((_get_full_tweet_text(tweet) or "").split())
    if not text:
        return False
    refs = tweet.get("referenced_tweets", [])
    is_reply = any(r.get("type") == "replied_to" for r in refs)
    if is_reply:
        stripped = text
        while stripped.startswith("@"):
            parts = stripped.split(None, 1)
            if len(parts) == 1:
                stripped = ""
                break
            stripped = parts[1].lstrip()
        if len(stripped) < 25:
            return False
    return True


def compact_post(tweet, external_url_entries):
    text = " ".join((_get_full_tweet_text(tweet) or "").split())
    post = {
        "id": tweet["id"],
        "created_at": tweet.get("created_at"),
        "account_handle": tweet.get("account_handle"),
        "account_name": tweet.get("account_name", ""),
        "text": text,
        "external_urls": [entry["url"] for entry in external_url_entries],
        "links": external_url_entries,
        "referenced_tweet_types": [
            ref.get("type") for ref in tweet.get("referenced_tweets", []) if ref.get("type")
        ],
    }
    # Tag content type for downstream processing
    if _has_note_tweet(tweet):
        post["content_type"] = "note_tweet"
    elif _is_article_tweet(tweet):
        post["content_type"] = "x_article"
    else:
        post["content_type"] = "tweet"
    return post


def post_priority(tweet, external_url_entries):
    score = 0
    refs = {ref.get("type") for ref in tweet.get("referenced_tweets", []) if ref.get("type")}
    text = " ".join((tweet.get("text") or "").split()).lower()

    if len(external_url_entries) > 1:
        score += 2
    if not refs:
        score += 2
    if "quoted" in refs:
        score += 1

    for entry in external_url_entries:
        domain = (entry.get("domain") or "").lower()
        title = (entry.get("title") or "").lower()
        desc = (entry.get("description") or "").lower()
        combined = " ".join((domain, title, desc, text))
        if any(domain.endswith(sig) for sig in HIGH_SIGNAL_DOMAINS):
            score += 5
        if any(domain.endswith(sig) for sig in LOW_SIGNAL_DOMAINS):
            score -= 4
        if any(keyword in combined for keyword in (
            "agent", "llm", "model", "prompt", "claude", "openai",
            "hugging face", "dataset", "github", "api", "context",
            "coding", "inference", "open-source", "privacy",
        )):
            score += 3
    if refs == {"replied_to"}:
        score -= 1
    return score


def is_recent_enough(tweet, now, recent_days):
    if recent_days <= 0:
        return True
    created_at = tweet.get("created_at")
    if not created_at:
        return True
    try:
        created_dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    except ValueError:
        return True
    age_days = (now - created_dt).total_seconds() / 86400
    return age_days <= recent_days


# ── Tweet content type helpers ──

def _has_note_tweet(tweet):
    """Check if a tweet has a Note Tweet with full text (long-form tweet)."""
    nt = tweet.get("note_tweet") or {}
    return bool(nt.get("text"))


def _is_article_tweet(tweet):
    """Check if a tweet is an X Article (has article title in the response)."""
    article = tweet.get("article") or {}
    return bool(article.get("title"))


def _get_full_tweet_text(tweet):
    """Return the full tweet text, preferring note_tweet.text over truncated text."""
    if _has_note_tweet(tweet):
        return tweet["note_tweet"]["text"]
    return tweet.get("text", "")


def fetch_article_body(tweet_id):
    """Fetch full X Article body via tweet.fields=article.

    IMPORTANT: tweet.fields=article MUST NOT be mixed with note_tweet in the
    same request. The two fields interact poorly and article.plain_text may be
    silently dropped. This function makes a separate API call.

    Returns (article_dict, error_category, error_detail) on success/failure.
    """
    try:
        out = run(f"/2/tweets/{tweet_id}?tweet.fields=article")
        if out is None:
            return None, "xurl_error", "run() returned None"
        resp = json.loads(out)
        article = resp.get("data", {}).get("article")
        if article and article.get("plain_text"):
            return article, None, None
        if article:
            return None, "no_plain_text", "article field present but plain_text missing"
        return None, "no_article_field", "response has no article field at all"
    except json.JSONDecodeError as e:
        return None, "parse_error", str(e)


def load_processed_map(path):
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}

    processed_map = data.get("processed", {})
    if isinstance(processed_map, dict):
        return {
            str(tweet_id): str(seen_at)
            for tweet_id, seen_at in processed_map.items()
            if tweet_id and seen_at
        }

    tweet_ids = data.get("tweet_ids", [])
    if isinstance(tweet_ids, list):
        migrated_at = datetime.now(timezone.utc).isoformat()
        return {str(tweet_id): migrated_at for tweet_id in tweet_ids if tweet_id}
    return {}


def prune_processed_map(processed_map, now, ttl_days):
    if ttl_days <= 0:
        return processed_map
    pruned = {}
    for tweet_id, seen_at in processed_map.items():
        try:
            seen_dt = datetime.fromisoformat(seen_at.replace("Z", "+00:00"))
        except ValueError:
            continue
        age_days = (now - seen_dt).total_seconds() / 86400
        if age_days <= ttl_days:
            pruned[tweet_id] = seen_at
    return pruned


def prune_archive_dir(archive_dir, now, ttl_days):
    if ttl_days <= 0 or not archive_dir.exists():
        return
    for path in archive_dir.glob("x_accounts_*.json"):
        try:
            modified = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        except OSError:
            continue
        age_days = (now - modified).total_seconds() / 86400
        if age_days > ttl_days:
            try:
                path.unlink()
            except OSError:
                pass


def load_source_posts(source_file):
    if not source_file:
        return None
    path = Path(source_file).expanduser()
    if not path.exists():
        print(json.dumps({"error": f"source file not found: {path}", "new_posts": []}))
        sys.exit(1)
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"invalid source file JSON: {exc}", "new_posts": []}))
        sys.exit(1)
    return data.get("new_posts", [])

if not YAML_PATH.exists():
    print(json.dumps({"error": f"{YAML_PATH} not found", "new_posts": []}))
    sys.exit(1)

with open(YAML_PATH) as f:
    accounts = yaml.safe_load(f).get("accounts", [])

now = datetime.now(timezone.utc)
processed_map = prune_processed_map(
    load_processed_map(DB),
    now,
    PROCESSED_TTL_DAYS,
)
processed = set(processed_map)

all_new = []
all_raw = []
errors = []
scan_meta = {
    "request_budget": REQUEST_BUDGET,
    "x_api_requests_attempted": 0,
    "tracked_accounts": len(accounts),
    "accounts_selected": 0,
    "accounts_scanned": 0,
    "accounts_skipped_budget": 0,
    "user_cache_size": 0,
    "cursor_start": 0,
    "cursor_next": 0,
    "note_tweets_found": 0,
    "articles_fetched": 0,
    "articles_failed": 0,
}
source_posts = load_source_posts(SOURCE_FILE)
if source_posts is not None:
    for t in source_posts:
        refs = t.get("referenced_tweets", [])
        if any(r.get("type") == "retweeted" for r in refs):
            continue
        if not is_recent_enough(t, now, RECENT_DAYS):
            continue
        external_url_entries = get_external_url_entries(t)
        t["external_urls"] = [entry["url"] for entry in external_url_entries]
        if not is_substantive_post(t, external_url_entries):
            continue
        all_raw.append(t)
        all_new.append(compact_post(t, external_url_entries))
else:
    user_cache = load_user_cache(USER_ID_CACHE, now)
    scan_state = load_scan_state(SCAN_STATE)
    cursor = scan_state["cursor"] % len(accounts) if accounts else 0
    ordered_accounts = accounts[cursor:] + accounts[:cursor]
    scan_meta["cursor_start"] = cursor

    missing_handles = [
        acct["handle"]
        for acct in accounts
        if isinstance(acct, dict) and not get_cached_user_id(user_cache, acct.get("handle"))
    ]
    if missing_handles and REQUESTS_ATTEMPTED < REQUEST_BUDGET:
        resolved = resolve_user_ids(missing_handles)
        if resolved is None:
            errors.append({
                "handle": "*",
                "error": "could not batch resolve user ids",
            })
        else:
            user_cache.update(resolved)

    remaining_budget = max(0, REQUEST_BUDGET - REQUESTS_ATTEMPTED)
    accounts_to_scan = ordered_accounts[:remaining_budget]
    scan_meta["accounts_selected"] = len(accounts_to_scan)
    scan_meta["accounts_skipped_budget"] = max(0, len(accounts) - len(accounts_to_scan))

    for acct in accounts_to_scan:
        if not isinstance(acct, dict) or "handle" not in acct:
            continue
        handle = normalize_handle(acct["handle"])
        user_id = get_cached_user_id(user_cache, handle)
        if not user_id:
            errors.append({"handle": handle, "error": "could not resolve user_id"})
            continue
        tweets = get_recent_tweets(user_id, max_results=TWEETS_PER_ACCOUNT)
        scan_meta["accounts_scanned"] += 1
        for t in tweets:
            tweet_id = str(t.get("id", ""))
            if not tweet_id or tweet_id in processed:
                continue
            refs = t.get("referenced_tweets", [])
            if any(r.get("type") == "retweeted" for r in refs):
                continue
            if not is_recent_enough(t, now, RECENT_DAYS):
                continue
            t["account_handle"] = handle
            t["account_name"] = acct.get("name", "")
            external_url_entries = get_external_url_entries(t)
            t["external_urls"] = [entry["url"] for entry in external_url_entries]
            if not is_substantive_post(t, external_url_entries):
                continue
            all_raw.append(t)
            all_new.append(compact_post(t, external_url_entries))

    next_cursor = (cursor + len(accounts_to_scan)) % len(accounts) if accounts else 0
    scan_meta["cursor_next"] = next_cursor
    scan_meta["user_cache_size"] = len(user_cache)

ranked = sorted(
    zip(all_raw, all_new),
    key=lambda pair: (
        post_priority(pair[0], get_external_url_entries(pair[0])),
        pair[0].get("created_at", ""),
    ),
    reverse=True,
)
if MAX_CANDIDATES > 0:
    ranked = ranked[:MAX_CANDIDATES]
all_raw = [raw for raw, _ in ranked]
all_new = [compact for _, compact in ranked]

# ── Post-processing: count Note Tweets + fetch X Article bodies ──
# Note: note_tweet.text is already in the tweet data (no extra API call needed).
# X Article plain_text requires a separate API call with tweet.fields=article.
for raw_tweet in all_raw:
    if _has_note_tweet(raw_tweet):
        scan_meta["note_tweets_found"] += 1

    if _is_article_tweet(raw_tweet) and not raw_tweet.get("article", {}).get("plain_text"):
        tweet_id = str(raw_tweet.get("id"))
        article_data, err_cat, err_detail = fetch_article_body(tweet_id)
        if article_data:
            raw_tweet["article"] = article_data
            scan_meta["articles_fetched"] += 1
            # Also update the compact post text to include article body
            for cp in all_new:
                if cp["id"] == tweet_id:
                    cp["article_text"] = article_data.get("plain_text", "")
                    break
        else:
            raw_tweet["_article_fetch_error"] = err_detail
            raw_tweet["_article_fetch_error_category"] = err_cat
            scan_meta["articles_failed"] += 1

scan_meta["x_api_requests_attempted"] = REQUESTS_ATTEMPTED

archive_file = None
if not (source_posts is not None and REPLAY_NO_WRITE):
    DETAIL_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    prune_archive_dir(ARCHIVE_DIR, now, PROCESSED_TTL_DAYS)

    detail_payload = {
        "generated_at": now.isoformat(),
        "new_posts": all_raw,
        "errors": errors,
        "scan_meta": scan_meta,
    }
    detail_json = json.dumps(detail_payload, indent=2, ensure_ascii=False)
    DETAIL_FILE.write_text(detail_json)
    archive_file = ARCHIVE_DIR / f"x_accounts_{now.strftime('%Y%m%dT%H%M%SZ')}.json"
    archive_file.write_text(detail_json)
    if source_posts is None:
        save_user_cache(USER_ID_CACHE, user_cache)
        save_scan_state(SCAN_STATE, scan_meta["cursor_next"])

output = {
    "generated_at": now.isoformat(),
    "summary": {
        "tracked_accounts": len(accounts),
        "accounts_scanned": scan_meta["accounts_scanned"],
        "accounts_selected": scan_meta["accounts_selected"],
        "accounts_skipped_budget": scan_meta["accounts_skipped_budget"],
        "source_posts": len(source_posts or []),
        "substantive_candidates": len(ranked),
        "new_posts": len(all_new),
        "with_errors": len(errors),
        "note_tweets_found": scan_meta["note_tweets_found"],
        "articles_fetched": scan_meta["articles_fetched"],
        "articles_failed": scan_meta["articles_failed"],
        "processed_cache_size": len(processed),
        "processed_ttl_days": PROCESSED_TTL_DAYS,
        "max_candidates": MAX_CANDIDATES,
        "recent_days": RECENT_DAYS,
        "replay_mode": bool(source_posts is not None),
        "request_budget": REQUEST_BUDGET,
        "x_api_requests_attempted": REQUESTS_ATTEMPTED,
        "cursor_start": scan_meta["cursor_start"],
        "cursor_next": scan_meta["cursor_next"],
        "user_cache_size": scan_meta["user_cache_size"],
    },
    "detail_file": str(DETAIL_FILE),
    "new_posts": all_new,
}
if archive_file is not None:
    output["archive_file"] = str(archive_file)
if errors:
    output["errors"] = errors

print(json.dumps(output, indent=2, ensure_ascii=False))

if not (source_posts is not None and REPLAY_NO_WRITE):
    seen_at = now.isoformat()
    for tweet in all_raw:
        processed_map[str(tweet["id"])] = seen_at
    DB.parent.mkdir(parents=True, exist_ok=True)
    DB.write_text(
        json.dumps(
            {
                "processed": dict(sorted(processed_map.items())),
                "ttl_days": PROCESSED_TTL_DAYS,
                "updated_at": seen_at,
            },
            indent=2,
        )
    )
