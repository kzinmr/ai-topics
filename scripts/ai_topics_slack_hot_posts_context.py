#!/usr/bin/env python3
"""Collect context for Lucy's AI Topics Slack hot-topic post job.

Provides structured context including recent Slack activity, wiki updates,
and recently covered topics for dedup-aware topic selection."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


JST = timezone(timedelta(hours=9))
CHANNEL_ID = os.environ.get("AI_TOPICS_SLACK_CHANNEL_ID", "C077ACXR5UY")
TONE_USER_ID = os.environ.get("AI_TOPICS_SLACK_TONE_USER_ID", "U076RPG60QY")
BOT_USER_ID: str | None = os.environ.get("AI_TOPICS_SLACK_BOT_USER_ID")


def now_jst() -> datetime:
    return datetime.now(tz=JST)


def slot_info(now: datetime) -> dict[str, Any]:
    slot_minute = 30
    slots = [
        (9, "morning", "Start with the sharpest narrative arc; make it easy to forward."),
        (13, "midday", "Pick a practical angle or surprising benchmark result."),
        (17, "evening", "Connect multiple wiki threads into one stronger interpretation."),
        (21, "night", "Use a more reflective or contrarian angle; avoid recapping the day."),
        (1, "late-night", "Use niche, high-signal material that rewards close readers."),
        (5, "pre-morning", "Choose infrastructure, model, or agent workflow material with durable value."),
    ]
    now_minutes = now.hour * 60 + now.minute
    current = min(slots, key=lambda item: (now_minutes - (item[0] * 60 + slot_minute)) % (24 * 60))
    idx = [hour for hour, _, _ in slots].index(current[0])
    return {
        "hour_jst": current[0],
        "minute_jst": slot_minute,
        "slot_time_jst": f"{current[0]:02d}:{slot_minute:02d}",
        "slot_index": idx,
        "slot_name": current[1],
        "guidance": current[2],
        "daily_slot_hours_jst": [hour for hour, _, _ in slots],
        "daily_slot_times_jst": [f"{hour:02d}:{slot_minute:02d}" for hour, _, _ in slots],
    }


def clean_slack_text(text: str) -> str:
    text = re.sub(r"<(https?://[^>|]+)\|([^>]+)>", r"\2 (\1)", text)
    text = re.sub(r"<(https?://[^>]+)>", r"\1", text)
    text = re.sub(r"<@([A-Z0-9]+)>", r"@\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def slack_api(method: str, params: dict[str, Any]) -> dict[str, Any]:
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        return {"ok": False, "error": "SLACK_BOT_TOKEN is not set"}

    query = urllib.parse.urlencode(params)
    request = urllib.request.Request(
        f"https://slack.com/api/{method}?{query}",
        headers={"Authorization": f"Bearer {token}"},
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8", "replace"))
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def fetch_slack_history() -> dict[str, Any]:
    """Fetch last 7 days of Slack channel history and extract dedup info."""
    oldest = (datetime.now(tz=timezone.utc) - timedelta(days=7)).timestamp()
    result = slack_api(
        "conversations.history",
        {"channel": CHANNEL_ID, "limit": 50, "oldest": f"{oldest:.6f}"},
    )
    if not result.get("ok"):
        return {"ok": False, "error": result.get("error", "unknown_error")}

    messages = result.get("messages", [])
    tone_examples = []
    recent_channel_posts = []
    bot_post_topics = []
    bot_own_posts: list[dict[str, Any]] = []

    for message in messages:
        text = clean_slack_text(message.get("text", ""))
        if not text:
            continue
        ts = float(message.get("ts", "0") or 0)
        item = {
            "ts": datetime.fromtimestamp(ts, tz=JST).isoformat(timespec="minutes"),
            "user": message.get("user") or message.get("bot_id") or "unknown",
            "text": text[:700],
        }
        if len(recent_channel_posts) < 30:
            recent_channel_posts.append(item)
        if message.get("user") == TONE_USER_ID and len(tone_examples) < 20:
            tone_examples.append(item)
        if "ai-topics" in text.lower() or "wiki" in text.lower() or "NJ" in text:
            bot_post_topics.extend(re.findall(r"[\w./@-]{4,}", text.lower()))

        # Track our own bot posts for dedup — extract wikilinks from previous posts
        if message.get("bot_id") or (BOT_USER_ID and message.get("user") == BOT_USER_ID):
            own_wikilinks = list(set(WIKILINK_RE.findall(text)))
            if own_wikilinks:
                bot_own_posts.append({
                    "ts": item["ts"],
                    "wikilinks": own_wikilinks[:10],
                })

    # Build recently_covered_topics: last 12 bot posts with their wikilinks
    # Sorted chronologically, most recent first
    bot_own_posts.sort(key=lambda x: x["ts"], reverse=True)
    recently_covered = bot_own_posts[:12]

    return {
        "ok": True,
        "channel_id": CHANNEL_ID,
        "tone_user_id": TONE_USER_ID,
        "tone_examples": list(reversed(tone_examples)),
        "recent_channel_posts": list(reversed(recent_channel_posts)),
        "recent_post_terms": Counter(bot_post_topics).most_common(20),
        "recently_covered_topics": recently_covered,
    }


def run_command(args: list[str], cwd: Path | None = None, timeout: int = 120) -> str:
    try:
        proc = subprocess.run(
            args,
            cwd=str(cwd) if cwd else None,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        return proc.stdout.strip()
    except Exception as exc:
        return f"ERROR: {type(exc).__name__}: {exc}"


def repo_root() -> Path:
    return Path.home() / "ai-topics"


def page_excerpt(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""
    text = re.sub(r"^---.*?---", "", text, flags=re.S)
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("|") or stripped.startswith("---"):
            continue
        if stripped.startswith("#") or len(stripped) > 40:
            lines.append(stripped)
        if len(" ".join(lines)) > 500:
            break
    return " ".join(lines)[:700]


def recent_wiki_pages(repo: Path) -> list[dict[str, str]]:
    output = run_command(
        ["git", "log", "--since=7 days ago", "--name-only", "--pretty=format:", "--", "wiki"],
        cwd=repo,
        timeout=60,
    )
    seen: set[str] = set()
    pages = []
    for rel in output.splitlines():
        rel = rel.strip()
        if not rel.endswith(".md") or rel in seen:
            continue
        if not (rel.startswith("wiki/concepts/") or rel.startswith("wiki/entities/") or rel.startswith("wiki/comparisons/")):
            continue
        seen.add(rel)
        path = repo / rel
        if not path.exists():
            continue
        pages.append(
            {
                "path": "~/" + rel,
                "title": path.stem.replace("-", " "),
                "excerpt": page_excerpt(path),
            }
        )
        if len(pages) >= 20:
            break
    return pages


def related_wiki_pages(
    repo: Path,
    recent_pages: list[dict[str, str]],
    max_per_source: int = 3,
    total_max: int = 60,
) -> list[dict[str, str]]:
    seen_paths: set[str] = set(p["path"] for p in recent_pages)
    result_set: dict[str, str] = {}

    for page in recent_pages[:20]:
        if len(result_set) >= total_max:
            break

        path_str = page["path"]
        rel_path = path_str.replace("~/", "")
        full_path = (repo / rel_path) if not rel_path.startswith("/") else Path(rel_path)

        if not full_path.exists():
            continue
        try:
            text = full_path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        page_slug = Path(rel_path).stem
        per_source_count = 0

        for match in WIKILINK_RE.finditer(text):
            if per_source_count >= max_per_source or len(result_set) >= total_max:
                break
            target_slug = match.group(1).strip()
            if not target_slug:
                continue
            for subdir in ("entities", "concepts", "comparisons"):
                target_rel = f"wiki/{subdir}/{target_slug}.md"
                target_full = repo / target_rel
                if target_full.exists():
                    target_path_str = "~/" + target_rel
                    if target_path_str not in seen_paths:
                        seen_paths.add(target_path_str)
                        result_set[target_slug] = target_path_str
                        per_source_count += 1
                    break

        if per_source_count < max_per_source:
            escaped = re.escape(page_slug)
            grep_out = run_command(
                ["grep", "-rl", rf"\[\[{escaped}(\||\])", str(repo / "wiki")],
                timeout=30,
            )
            for bl_path in grep_out.splitlines():
                if not bl_path.strip():
                    continue
                bl_rel = bl_path.replace(str(repo) + "/", "")
                bl_path_str = "~/" + bl_rel
                if bl_path_str not in seen_paths:
                    seen_paths.add(bl_path_str)
                    result_set[Path(bl_rel).stem] = bl_path_str
                    per_source_count += 1
                    if per_source_count >= max_per_source or len(result_set) >= total_max:
                        break

    result = []
    for slug, path_str in result_set.items():
        if len(result) >= total_max:
            break
        abs_path = repo / path_str.replace("~/", "")
        result.append({
            "path": path_str,
            "title": abs_path.stem.replace("-", " ") if abs_path.exists() else slug.replace("-", " "),
            "excerpt": page_excerpt(abs_path) if abs_path.exists() else "",
        })
    return result


def hot_topic_yaml(repo: Path) -> str:
    path = repo / "config" / "hot-topics.yaml"
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:8000]
    except Exception:
        return ""


def _get_covered_slugs(recently_covered: list[dict[str, Any]], n_posts: int = 2) -> set[str]:
    """Extract wikilink slugs from the most recent N bot posts."""
    slugs: set[str] = set()
    for post in recently_covered[:n_posts]:
        for wikilink in post.get("wikilinks", []):
            slug = Path(wikilink).stem
            slugs.add(slug)
    return slugs


def _dedup_filter(
    pages: list[dict[str, str]],
    covered_slugs: set[str],
) -> list[dict[str, str]]:
    """Filter out pages whose slug appears in covered_slugs."""
    filtered: list[dict[str, str]] = []
    for page in pages:
        slug = Path(page["path"].replace("~/", "")).stem
        if slug not in covered_slugs:
            filtered.append(page)
    return filtered


def main() -> None:
    now = now_jst()
    repo = repo_root()
    slack_data = fetch_slack_history()
    recent_pages = recent_wiki_pages(repo)
    related_pages = related_wiki_pages(repo, recent_pages)

    # Hard dedup: exclude pages already covered in the most recent 2 bot posts.
    # Soft guidance ("avoid_repeating") wasn't reliable — LLM still picked same topics.
    covered_slugs = _get_covered_slugs(
        slack_data.get("recently_covered_topics", []), n_posts=2
    )
    dedup_applied = False
    dedup_removed_slugs: list[str] = []
    if covered_slugs:
        deduped_recent = _dedup_filter(recent_pages, covered_slugs)
        deduped_related = _dedup_filter(related_pages, covered_slugs)
        # Only apply if at least 3 candidates remain — prevent empty pool
        if len(deduped_recent) >= 3:
            removed_slugs = sorted(
                covered_slugs
                & {Path(p["path"].replace("~/", "")).stem for p in recent_pages}
            )
            dedup_removed_slugs = removed_slugs
            recent_pages = deduped_recent
            related_pages = deduped_related
            dedup_applied = True

    payload = {
        "generated_at_utc": datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
        "generated_at_jst": now.isoformat(timespec="seconds"),
        "posting_slot": slot_info(now),
        "slack": slack_data,
        "ai_topics": {
            "recent_wiki_pages": recent_pages,
            "related_wiki_pages": related_pages,
            "hot_topics_yaml_excerpt": hot_topic_yaml(repo),
        },
        "selection_policy": {
            "avoid_repeating_recent_slack_posts": True,
            "prefer_nj_score_4_or_5": True,
            "spread_topics_across_daily_slots": True,
            "output_language": "Japanese",
        },
        "dedup": {
            "recently_covered_topics": slack_data.get("recently_covered_topics", []),
            "hard_filter_applied": dedup_applied,
            "hard_filter_removed_slugs": dedup_removed_slugs,
        },
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
