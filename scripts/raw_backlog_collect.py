#!/usr/bin/env python3
"""Collect unprocessed raw articles for the raw-backlog-ingest pipeline.

Picks N articles that haven't been triaged yet, cross-references against
the archive index for comparison context, and outputs JSON for the agent.

Usage:
    python3 scripts/raw_backlog_collect.py
    python3 scripts/raw_backlog_collect.py --count 10 --min-size 1000
    python3 scripts/raw_backlog_collect.py --dry-run --estimate --count 10
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", Path.home() / "ai-topics" / "wiki"))
RAW_ARTICLES = WIKI_ROOT / "raw" / "articles"
ARCHIVE_INDEX = WIKI_ROOT / "raw" / "archived" / "triage" / "archive_index.json"
TRACKING_FILE = HERMES_HOME / "processed_raw_articles.json"
O11Y_DIR = HERMES_HOME / "o11y"

RAW_BACKLOG_JOB_ID = "4e63c6f0d140"
DEFAULT_COUNT = 5
DEFAULT_MIN_SIZE = 500  # bytes
BODY_EXCERPT_LENGTH = 400
DEFAULT_SORT = "ai-hint"


def load_tracking() -> dict:
    """Return {filename: {processed_at, status, ...}}."""
    if not TRACKING_FILE.exists():
        return {}
    try:
        return json.loads(TRACKING_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_tracking(data: dict) -> None:
    TRACKING_FILE.parent.mkdir(parents=True, exist_ok=True)
    TRACKING_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_archive_index() -> dict:
    """Return archive index data or an empty index."""
    if not ARCHIVE_INDEX.exists():
        return {"urls": []}
    try:
        return json.loads(ARCHIVE_INDEX.read_text(encoding="utf-8"))
    except Exception:
        return {"urls": []}


def extract_url_from_article(path: Path) -> str | None:
    """Try to extract the canonical URL from a raw article's frontmatter."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.split("\n")[:30]:
            line = line.strip()
            if line.startswith("url:") or line.startswith("**URL:**"):
                url = line.split(":", 1)[1].strip().strip('"').strip("'")
                if url.startswith("http"):
                    return url
            if line.startswith("source:"):
                url = line.split(":", 1)[1].strip().strip('"').strip("'")
                if url.startswith("http"):
                    return url
            if line.startswith("- **Source:**"):
                match = re.search(r"\(?(https?://[^\s\)]+)\)?", line)
                if match:
                    return match.group(1)
    except Exception:
        pass
    return None


def normalize_archive_url(url: str) -> str:
    """Normalize URLs for archive-dedup comparison."""
    if "/redirect/" in url:
        return url.split("?", 1)[0]
    return url


def extract_body_excerpt(path: Path, length: int = BODY_EXCERPT_LENGTH) -> str:
    """Extract opening body text from a raw article file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.split("\n")
        in_frontmatter = False
        body_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped == "---" and not in_frontmatter:
                in_frontmatter = True
                continue
            if stripped == "---" and in_frontmatter:
                in_frontmatter = False
                continue
            if in_frontmatter:
                continue
            if stripped:
                body_lines.append(line)
                if sum(len(l) for l in body_lines) >= length:
                    break
        return "\n".join(body_lines)[:length].replace("\n\n", "\n").strip()
    except Exception:
        return ""


def get_article_hash(path: Path) -> str:
    """Content-based hash for dedup (first 8KB)."""
    try:
        return hashlib.md5(path.read_bytes()[:8192]).hexdigest()[:12]
    except Exception:
        return path.name[:12]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", "--limit", dest="count", type=int, default=DEFAULT_COUNT)
    parser.add_argument("--min-size", type=int, default=DEFAULT_MIN_SIZE)
    parser.add_argument("--sort", choices=["ai-hint", "recent", "size"], default=DEFAULT_SORT)
    parser.add_argument("--dry-run", action="store_true", help="do not mark selected articles as processing")
    parser.add_argument("--estimate", action="store_true", help="include time estimates from successful job history")
    parser.add_argument("--history-limit", type=int, default=60, help="max successful trace samples to use")
    args = parser.parse_args(argv)
    if args.count < 1:
        parser.error("--count must be positive")
    if args.min_size < 0:
        parser.error("--min-size must be non-negative")
    return args


def _parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        return None


def _article_count_from_response(text: str) -> int | None:
    patterns = [
        r"処理[:：]\s*(\d+)\s*件",
        r"All\s+(\d+)\s+articles",
        r"(\d+)\s+articles\s+(?:triaged|processed)",
        r"(\d+)\s*記事",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                return int(match.group(1))
            except ValueError:
                return None
    return None


def estimate_from_history(selected_count: int, total_candidate_count: int, history_limit: int = 60) -> dict[str, Any]:
    """Estimate runtime from successful raw-backlog-ingest o11y traces."""
    samples: list[dict[str, Any]] = []
    if O11Y_DIR.exists():
        for trace_path in sorted(O11Y_DIR.glob("traces-*.jsonl"), reverse=True):
            try:
                lines = trace_path.read_text(encoding="utf-8", errors="replace").splitlines()
            except Exception:
                continue
            for line in reversed(lines):
                if RAW_BACKLOG_JOB_ID not in line:
                    continue
                try:
                    trace = json.loads(line)
                except Exception:
                    continue
                if not trace.get("completed") or trace.get("interrupted"):
                    continue
                session_id = str(trace.get("session_id") or "")
                if f"cron_{RAW_BACKLOG_JOB_ID}" not in session_id:
                    continue
                start = _parse_iso(trace.get("start_time"))
                end = _parse_iso(trace.get("end_time"))
                if not start or not end:
                    continue
                duration = max(0.0, (end - start).total_seconds())
                if duration <= 0:
                    continue
                metadata = trace.get("metadata") if isinstance(trace.get("metadata"), dict) else {}
                response = str(metadata.get("last_assistant_response") or "")
                article_count = _article_count_from_response(response)
                inferred_article_count = article_count is None
                if article_count is None:
                    article_count = DEFAULT_COUNT
                samples.append({
                    "trace_file": trace_path.name,
                    "session_id": session_id,
                    "start_time": trace.get("start_time"),
                    "duration_seconds": round(duration, 1),
                    "article_count": article_count,
                    "article_count_inferred": inferred_article_count,
                    "turn_count": metadata.get("turn_count"),
                    "llm_calls": metadata.get("total_llm_calls"),
                    "llm_duration_ms": metadata.get("total_llm_duration_ms"),
                })
                if len(samples) >= history_limit:
                    break
            if len(samples) >= history_limit:
                break

    if not samples:
        return {
            "available": False,
            "basis": "no successful raw-backlog-ingest o11y traces found",
            "selected_count": selected_count,
            "total_candidate_count": total_candidate_count,
        }

    per_article = [s["duration_seconds"] / max(1, int(s["article_count"])) for s in samples]
    batch_seconds = [s["duration_seconds"] for s in samples]
    median_per_article = statistics.median(per_article)
    median_batch = statistics.median(batch_seconds)
    p80_per_article = sorted(per_article)[min(len(per_article) - 1, int(len(per_article) * 0.8))]

    return {
        "available": True,
        "basis": "successful raw-backlog-ingest o11y traces; per-article scaling is linearized from historical batches",
        "history_samples": len(samples),
        "median_batch_seconds": round(median_batch, 1),
        "median_per_article_seconds": round(median_per_article, 1),
        "p80_per_article_seconds": round(p80_per_article, 1),
        "selected_count": selected_count,
        "estimated_selected_seconds_median": round(median_per_article * selected_count, 1),
        "estimated_selected_seconds_p80": round(p80_per_article * selected_count, 1),
        "total_candidate_count": total_candidate_count,
        "estimated_all_candidates_seconds_median": round(median_per_article * total_candidate_count, 1),
        "samples": samples[:10],
    }


def collect(argv: list[str] | argparse.Namespace) -> dict[str, Any]:
    """Main collection logic. Returns JSON-serializable result."""
    args = parse_args(argv) if isinstance(argv, list) else argv

    # 1. Load tracking data
    tracking = load_tracking()
    processed_filenames = set(tracking.keys())
    sub_registry = tracking.get("processed_articles")
    sub_done = set(sub_registry.keys()) if isinstance(sub_registry, dict) else set()

    # 2. Load archive index for cross-reference
    archive = load_archive_index()
    archived_urls = set(archive.get("urls", []))
    archived_urls_norm = {normalize_archive_url(u) for u in archived_urls}

    # 3. List raw articles, filter unprocessed; pre-compute mtime
    now_ts = datetime.now(timezone.utc).timestamp()
    all_articles = []
    if RAW_ARTICLES.exists():
        for f in RAW_ARTICLES.iterdir():
            if not f.is_file() or not f.name.endswith(".md"):
                continue
            st = f.stat()
            size = st.st_size
            if size < args.min_size:
                continue
            all_articles.append((f.name, size, f, st.st_mtime))

    if args.sort == "recent":
        all_articles.sort(key=lambda x: (-x[3], -x[1]))
    elif args.sort == "ai-hint":
        ai_terms = [
            "agent", "llm", "gpt", "claude", "openai", "ai-", "model",
            "deepseek", "anthropic", "mistral", "gemini", "huggingface",
            "transformer", "fine-tun", "rag", "prompt", "inference",
            "coding-agent", "harness", "language-model", "rlhf",
        ]

        def ai_score(item: tuple[str, int, Path, float]) -> int:
            name = item[0].lower()
            return sum(1 for term in ai_terms if term in name)

        all_articles.sort(key=lambda x: (-ai_score(x), -x[3], -x[1]))
    else:
        all_articles.sort(key=lambda x: (-x[1], x[0]))

    candidates = []
    skipped_processing_fresh = 0
    skipped_processed = 0
    skipped_archived = 0
    for name, size, path, mtime in all_articles:
        if name in sub_done:
            skipped_processed += 1
            continue
        if name in processed_filenames:
            entry = tracking[name]
            status = entry.get("status", "") if isinstance(entry, dict) else ""
            if status == "processing":
                collected_at = entry.get("collected_at", "") if isinstance(entry, dict) else ""
                if collected_at:
                    try:
                        ts = datetime.fromisoformat(collected_at).timestamp()
                        if now_ts - ts <= 3600:
                            skipped_processing_fresh += 1
                            continue
                    except Exception:
                        skipped_processing_fresh += 1
                        continue
                else:
                    skipped_processing_fresh += 1
                    continue
            elif status in ("done", "skipped", "error"):
                skipped_processed += 1
                continue
            else:
                skipped_processed += 1
                continue

        cand_url = extract_url_from_article(path)
        if cand_url and (cand_url in archived_urls or normalize_archive_url(cand_url) in archived_urls_norm):
            skipped_archived += 1
            continue
        candidates.append((name, size, path, mtime))

    selected = candidates[:args.count]

    output: dict[str, Any] = {
        "collect_run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": bool(args.dry_run),
        "selection": {
            "requested_count": args.count,
            "sort": args.sort,
            "min_size": args.min_size,
        },
        "total_raw_articles": len(all_articles),
        "already_processed": len(processed_filenames),
        "processed_articles_registry_count": len(sub_done),
        "archived_urls_count": len(archived_urls),
        "skipped_processing_fresh": skipped_processing_fresh,
        "skipped_processed": skipped_processed,
        "skipped_archived": skipped_archived,
        "candidate_count": len(candidates),
        "candidates_selected": len(selected),
        "candidates_remaining": len(candidates) - len(selected),
        "candidate_bytes_total": sum(size for _, size, _, _ in candidates),
        "selected_bytes_total": sum(size for _, size, _, _ in selected),
        "articles": [],
    }

    for name, size, path, mtime in selected:
        url = extract_url_from_article(path)
        body_excerpt = extract_body_excerpt(path)
        content_hash = get_article_hash(path)
        archive_status = None
        if url and url in archived_urls:
            archive_status = "already_archived"
        elif url:
            archive_status = "not_archived"

        output["articles"].append({
            "filename": name,
            "raw_path": str(path),
            "size_bytes": size,
            "mtime": datetime.fromtimestamp(mtime, timezone.utc).isoformat(),
            "url": url,
            "content_hash": content_hash,
            "archive_status": archive_status,
            "body_excerpt": body_excerpt,
        })

        if not args.dry_run:
            tracking[name] = {
                "status": "processing",
                "collected_at": datetime.now(timezone.utc).isoformat(),
                "size_bytes": size,
                "url": url,
                "pipeline": "raw-backlog-ingest",
            }

    if args.estimate or args.dry_run:
        output["estimate"] = estimate_from_history(
            selected_count=len(selected),
            total_candidate_count=len(candidates),
            history_limit=args.history_limit,
        )

    if not args.dry_run:
        save_tracking(tracking)

    return output


def main() -> int:
    output = collect(sys.argv[1:])
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
