#!/usr/bin/env python3
"""Pre-run script: fetch recent posts from tracked X accounts.

Outputs a compact, agent-friendly summary by default and stores the raw payload
separately for progressive disclosure when deeper inspection is needed.
"""
import json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "-q"])
    import yaml

XURL = os.environ.get("XURL_PATH", "/opt/data/bin/xurl")

AI_TOPICS = Path(os.environ.get("AI_TOPICS_HOME", Path.home() / "ai-topics"))
YAML_PATH = AI_TOPICS / "config" / "feeds" / "x-accounts.yaml"

HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
DB = HERMES_HOME / "processed_x_accounts.json"
DETAIL_DIR = HERMES_HOME / "cron" / "data"
DETAIL_FILE = DETAIL_DIR / "x_accounts_latest_full.json"
ARCHIVE_DIR = DETAIL_DIR / "x_accounts_archive"
PROCESSED_TTL_DAYS = int(os.environ.get("HERMES_X_ACCOUNTS_TTL_DAYS", "14"))
MAX_CANDIDATES = int(os.environ.get("HERMES_X_ACCOUNTS_MAX_CANDIDATES", "12"))
RECENT_DAYS = int(os.environ.get("HERMES_X_ACCOUNTS_RECENT_DAYS", "7"))
SOURCE_FILE = os.environ.get("FETCH_X_ACCOUNTS_SOURCE_FILE", "").strip()
REPLAY_NO_WRITE = os.environ.get("FETCH_X_ACCOUNTS_REPLAY_NO_WRITE", "1").strip().lower() not in ("0", "false", "no")

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
    r = subprocess.run([XURL, "--auth", "app", *args], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"xurl error: {r.stderr}", file=sys.stderr)
        return None
    return r.stdout

def get_user_id(handle):
    handle_clean = handle.lstrip("@")
    out = run("user", handle_clean)
    if not out:
        return None
    try:
        data = json.loads(out)
        return data.get("data", data).get("id")
    except json.JSONDecodeError:
        return None

def get_recent_tweets(user_id, max_results=10):
    out = run("/2/users/{}/tweets?max_results={}&tweet.fields=created_at,entities,referenced_tweets".format(user_id, max_results))
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
    text = " ".join((tweet.get("text") or "").split())
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
    text = " ".join((tweet.get("text") or "").split())
    return {
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
    for acct in accounts:
        handle = acct["handle"].lstrip("@")
        user_id = get_user_id(handle)
        if not user_id:
            errors.append({"handle": handle, "error": "could not resolve user_id"})
            continue
        tweets = get_recent_tweets(user_id, max_results=10)
        for t in tweets:
            if t["id"] in processed:
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

archive_file = None
if not (source_posts is not None and REPLAY_NO_WRITE):
    DETAIL_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    prune_archive_dir(ARCHIVE_DIR, now, PROCESSED_TTL_DAYS)

    detail_payload = {
        "generated_at": now.isoformat(),
        "new_posts": all_raw,
        "errors": errors,
    }
    detail_json = json.dumps(detail_payload, indent=2, ensure_ascii=False)
    DETAIL_FILE.write_text(detail_json)
    archive_file = ARCHIVE_DIR / f"x_accounts_{now.strftime('%Y%m%dT%H%M%SZ')}.json"
    archive_file.write_text(detail_json)

output = {
    "generated_at": now.isoformat(),
    "summary": {
        "accounts_scanned": len(accounts),
        "source_posts": len(source_posts or []),
        "substantive_candidates": len(ranked),
        "new_posts": len(all_new),
        "with_errors": len(errors),
        "processed_cache_size": len(processed),
        "processed_ttl_days": PROCESSED_TTL_DAYS,
        "max_candidates": MAX_CANDIDATES,
        "recent_days": RECENT_DAYS,
        "replay_mode": bool(source_posts is not None),
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
        processed_map[tweet["id"]] = seen_at
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
