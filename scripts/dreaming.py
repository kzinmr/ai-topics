#!/usr/bin/env python3
"""Dreaming — Phase 1: Data Collection

Collects recent inbox data (RSS scans + newsletters) and outputs structured
JSON for the LLM to analyze during later dreaming phases.

The script runs BEFORE the LLM processes the dreaming task. Its stdout is
injected into the cron prompt as context.
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
PROFILE_ROOT = HERMES_HOME.parent
AI_TOPICS_REPO = Path(os.environ.get("AI_TOPICS_REPO", str(PROFILE_ROOT / "ai-topics")))
WIKI_DIR = Path(os.environ.get("WIKI_ROOT", str(AI_TOPICS_REPO / "wiki")))

# Paths
INBOX_DIR = AI_TOPICS_REPO / "inbox"
RSS_SCANS_DIR = INBOX_DIR / "rss-scans"
NEWSLETTERS_DIR = INBOX_DIR / "newsletters"
CONCEPTS_DIR = WIKI_DIR / "concepts"
ENTITIES_DIR = WIKI_DIR / "entities"
COMPARISONS_DIR = WIKI_DIR / "comparisons"
QUERIES_DIR = WIKI_DIR / "queries"
RAW_ARTICLES_DIR = WIKI_DIR / "raw" / "articles"

LOOKBACK_DAYS = 7
MAX_ARTICLES = 40  # Keep the injected payload well below compression thresholds
MAX_KEY_POINTS = 4
MAX_CONCEPT_TAGS = 8
MAX_SUMMARY_CHARS = 420
MAX_POINT_CHARS = 220
RELEVANCE_TERMS = {
    "ai": 2,
    "llm": 3,
    "language model": 3,
    "agent": 2,
    "agents": 2,
    "claude": 2,
    "gpt": 2,
    "gemini": 2,
    "cursor": 1,
    "copilot": 2,
    "code": 1,
    "coding": 2,
    "developer": 1,
    "prompt": 2,
    "reasoning": 2,
    "inference": 2,
    "training": 2,
    "fine-tuning": 2,
    "fine tuning": 2,
    "benchmark": 1,
    "eval": 1,
    "retrieval": 2,
    "rag": 2,
    "mcp": 2,
    "tool use": 2,
    "tool calling": 2,
    "memory": 1,
    "gpu": 2,
    "openai": 2,
    "anthropic": 2,
    "qwen": 2,
    "deepseek": 2,
}


def get_date_range():
    """Return (start_date, end_date) strings for the configured lookback window."""
    today = datetime.now()
    start = today - timedelta(days=LOOKBACK_DAYS)
    return start.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")


def normalize_url(url):
    """Normalize URLs for matching against raw article files."""
    if not url:
        return ""
    try:
        parsed = urlsplit(url.strip())
    except Exception:
        return url.strip()

    query = [
        (k, v) for k, v in parse_qsl(parsed.query, keep_blank_values=True)
        if not k.lower().startswith("utm_")
    ]
    normalized = urlunsplit((
        parsed.scheme.lower(),
        parsed.netloc.lower(),
        parsed.path.rstrip("/"),
        urlencode(query, doseq=True),
        "",
    ))
    return normalized.rstrip("/")


def normalize_title(title):
    """Normalize titles for fuzzy matching across RSS/newsletter/raw sources."""
    title = clean_markdown(title).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def clean_markdown(text):
    """Convert markdown-ish snippets to compact plain text."""
    if not text:
        return ""
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"[*_>#]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" -\t\r\n")


def trim_text(text, limit):
    """Trim text to a hard character budget."""
    text = clean_markdown(text)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def summarize_preview(preview_lines):
    """Turn newsletter preview blockquotes into a compact semantic summary."""
    preview = clean_markdown(" ".join(preview_lines))
    if not preview:
        return "", []

    sentences = re.split(r"(?<=[.!?])\s+", preview)
    summary = trim_text(" ".join(sentences[:2]), MAX_SUMMARY_CHARS)
    key_points = []
    for sentence in sentences[:MAX_KEY_POINTS]:
        point = trim_text(sentence, MAX_POINT_CHARS)
        if point and point not in key_points:
            key_points.append(point)
    return summary, key_points


def extract_concept_tags(title, headings, bullet_lines):
    """Extract a compact list of tags from headings and emphasized phrases."""
    tags = []
    seen = set()

    def add(value):
        value = clean_markdown(value)
        if not value:
            return
        lower = value.lower()
        if lower in seen or len(value) < 3:
            return
        seen.add(lower)
        tags.append(value)

    for text in [title, *headings, *bullet_lines]:
        for phrase in re.findall(r"\*\*([^*]+)\*\*", text):
            add(phrase)

    for heading in headings:
        add(heading)

    title_parts = re.split(r"[:\-–—/|]", title)
    for part in title_parts:
        add(part)

    return tags[:MAX_CONCEPT_TAGS]


def parse_raw_article(raw_path):
    """Parse a raw article and extract a dense semantic summary."""
    try:
        text = raw_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"WARNING: Failed to read raw article {raw_path.name}: {e}", file=sys.stderr)
        return None

    frontmatter = {}
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        fm_lines = []
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                lines = lines[i + 1:]
                break
            fm_lines.append(lines[i])
        for line in fm_lines:
            if ":" in line:
                k, v = line.split(":", 1)
                frontmatter[k.strip()] = v.strip()

    body = "\n".join(lines)
    body_for_summary = re.sub(
        r"^\*\*(Source|Date|URL|Crawled):\*\*.*$",
        "",
        body,
        flags=re.MULTILINE,
    )
    url_match = re.search(r"^\*\*URL:\*\*\s*(.+)$", body, re.MULTILINE)
    source_match = re.search(r"^\*\*Source:\*\*\s*(.+)$", body, re.MULTILINE)
    date_match = re.search(r"^\*\*Date:\*\*\s*(.+)$", body, re.MULTILINE)
    title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    thesis_match = re.search(r'^\>\s*\*?"([^"]+)"\*?$', body, re.MULTILINE)
    headings = [clean_markdown(h) for h in re.findall(r"^##+\s+(.+)$", body, re.MULTILINE)]
    bullet_lines = [clean_markdown(b) for b in re.findall(r"^\s*-\s+(.+)$", body, re.MULTILINE)]

    summary_parts = []
    if thesis_match:
        summary_parts.append(thesis_match.group(1))
    for bullet in bullet_lines:
        if any(marker in bullet.lower() for marker in ("primary goal", "key tradeoff", "recommendation", "core thesis")):
            summary_parts.append(bullet)
        if len(summary_parts) >= 3:
            break

    if not summary_parts:
        paragraphs = [
            trim_text(p, MAX_SUMMARY_CHARS)
            for p in re.split(r"\n\s*\n", body_for_summary)
            if len(clean_markdown(p)) > 80 and not p.strip().startswith("**URL:**")
        ]
        summary_parts.extend(paragraphs[:2])

    key_points = []
    for bullet in bullet_lines:
        point = trim_text(bullet, MAX_POINT_CHARS)
        if point and point not in key_points:
            key_points.append(point)
        if len(key_points) >= MAX_KEY_POINTS:
            break

    title = clean_markdown(frontmatter.get("title") or (title_match.group(1) if title_match else raw_path.stem))
    normalized_url = normalize_url(url_match.group(1)) if url_match else ""

    return {
        "title": title,
        "url": url_match.group(1).strip() if url_match else "",
        "normalized_url": normalized_url,
        "source": source_match.group(1).strip() if source_match else "",
        "date": date_match.group(1).strip() if date_match else "",
        "path": f"~/wiki/raw/articles/{raw_path.name}",
        "summary": trim_text(" ".join(summary_parts), MAX_SUMMARY_CHARS),
        "key_points": key_points,
        "concept_tags": extract_concept_tags(title, headings, bullet_lines),
    }


def summary_quality(summary, key_points):
    """Score how semantically useful a summary block is."""
    score = len(key_points) * 2
    if summary and not summary.startswith("Source:"):
        score += 1
    if len(summary) > 120:
        score += 1
    return score


def build_raw_article_index(start_date):
    """Index recent raw articles by normalized URL."""
    index = {"by_url": {}, "by_title": {}}
    if not RAW_ARTICLES_DIR.exists():
        return index

    for raw_path in sorted(RAW_ARTICLES_DIR.glob("*.md")):
        if raw_path.name == "_index.md":
            continue
        if raw_path.stat().st_mtime < (time.time() - (LOOKBACK_DAYS * 24 * 60 * 60)):
            continue
        parsed = parse_raw_article(raw_path)
        if not parsed or not parsed["normalized_url"]:
            pass
        else:
            index["by_url"][parsed["normalized_url"]] = parsed

        title_key = normalize_title(parsed["title"]) if parsed else ""
        if title_key and title_key not in index["by_title"]:
            index["by_title"][title_key] = parsed

    return index


def collect_scan_reports(start_date, end_date):
    """Parse articles from inbox RSS scan reports."""
    articles = []
    if not RSS_SCANS_DIR.exists():
        print(f"WARNING: RSS scans directory not found: {RSS_SCANS_DIR}", file=sys.stderr)
        return articles

    for scan_file in sorted(RSS_SCANS_DIR.glob("daily-scan-*.md")):
        match = re.search(r"daily-scan-(\d{4}-\d{2}-\d{2})\.md", scan_file.name)
        if not match:
            continue
        scan_date = match.group(1)
        if not (start_date <= scan_date <= end_date):
            continue

        try:
            content = scan_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"WARNING: Failed to read {scan_file.name}: {e}", file=sys.stderr)
            continue

        # Pattern: - [Title](URL) — source
        for line in content.splitlines():
            m = re.match(r"-\s*\[([^\]]+)\]\(([^)]+)\)\s*[—\-]\s*(.*)", line.strip())
            if m:
                title, url, source = m.groups()
                # Skip non-article lines (Reddit section headers, etc.)
                if title.startswith("#") or title.startswith("##"):
                    continue
                articles.append({
                    "title": title.strip(),
                    "url": url.strip(),
                    "normalized_url": normalize_url(url),
                    "source": source.strip(),
                    "date": scan_date,
                    "type": "rss_scan",
                })

    return articles


def collect_newsletters(start_date, end_date):
    """Parse articles from newsletter digests."""
    articles = []
    if not NEWSLETTERS_DIR.exists():
        print(f"WARNING: Newsletters directory not found: {NEWSLETTERS_DIR}", file=sys.stderr)
        return articles

    for nl_file in sorted(NEWSLETTERS_DIR.glob("*-newsletter.md")):
        match = re.search(r"(\d{4}-\d{2}-\d{2})-newsletter\.md", nl_file.name)
        if not match:
            continue
        nl_date = match.group(1)
        if not (start_date <= nl_date <= end_date):
            continue

        try:
            content = nl_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"WARNING: Failed to read {nl_file.name}: {e}", file=sys.stderr)
            continue

        current = None

        def flush_current():
            if not current or not current.get("title") or not current.get("url"):
                return
            summary, key_points = summarize_preview(current.get("preview_lines", []))
            articles.append({
                "title": current["title"],
                "url": current["url"],
                "normalized_url": normalize_url(current["url"]),
                "source": "newsletter",
                "date": nl_date,
                "type": "newsletter",
                "summary": summary,
                "key_points": key_points,
                "concept_tags": extract_concept_tags(current["title"], [], current.get("preview_lines", []))[:MAX_CONCEPT_TAGS],
            })

        for line in content.splitlines():
            m_title = re.match(r"##\s*\d+\.\s*(.+)", line.strip())
            if m_title:
                flush_current()
                current = {
                    "title": m_title.group(1).strip(),
                    "url": "",
                    "preview_lines": [],
                }
            m_url = re.match(r"-\s*\*\*URL:\*\*\s*(.+)", line.strip())
            if m_url and current:
                current["url"] = m_url.group(1).strip()
            if current and line.strip().startswith(">"):
                current["preview_lines"].append(line.strip().lstrip(">").strip())

        flush_current()

    return articles


def list_existing_wiki_pages():
    """List existing wiki pages across all Layer 2 directories."""
    pages = []
    for subdir in [CONCEPTS_DIR, ENTITIES_DIR, COMPARISONS_DIR, QUERIES_DIR]:
        if subdir.exists():
            for page_file in sorted(subdir.rglob("*.md")):
                if page_file.name == "_index.md":
                    continue
                rel = page_file.relative_to(WIKI_DIR)
                pages.append(str(rel))
    return pages


def build_wiki_index(pages):
    """Build a compact wiki index instead of injecting every full path."""
    index = {
        "counts_by_category": {},
        "recent_samples": {},
        "slug_lookup": {},
    }

    for page in pages:
        parts = page.split("/", 1)
        category = parts[0]
        slug = Path(page).stem
        index["counts_by_category"][category] = index["counts_by_category"].get(category, 0) + 1
        index["slug_lookup"][slug] = category
        samples = index["recent_samples"].setdefault(category, [])
        if len(samples) < 25:
            samples.append(slug)

    return index


def count_recent_raw_articles():
    """Count raw articles modified within the current lookback window."""
    if not RAW_ARTICLES_DIR.exists():
        return 0
    week_ago = time.time() - (LOOKBACK_DAYS * 24 * 60 * 60)
    count = 0
    for f in RAW_ARTICLES_DIR.glob("*.md"):
        if f.stat().st_mtime > week_ago:
            count += 1
    return count


def count_by_source(articles):
    """Count articles per source."""
    counts = {}
    for art in articles:
        src = art["source"]
        counts[src] = counts.get(src, 0) + 1
    return counts


def count_by_date(articles):
    """Count articles per date."""
    counts = {}
    for art in articles:
        d = art["date"]
        counts[d] = counts.get(d, 0) + 1
    return counts


def enrich_and_merge_articles(articles, raw_index):
    """Merge duplicate URLs and attach dense concept summaries from raw articles."""
    merged = {}
    ordered_keys = []

    for article in articles:
        key = article.get("normalized_url") or article["url"] or article["title"]
        if key not in merged:
            merged[key] = {
                "title": article["title"],
                "url": article["url"],
                "source": article["source"],
                "date": article["date"],
                "type": article["type"],
                "source_mentions": [],
                "summary": "",
                "key_points": [],
                "concept_tags": [],
            }
            ordered_keys.append(key)

        entry = merged[key]
        mention = {"source": article["source"], "type": article["type"], "date": article["date"]}
        if mention not in entry["source_mentions"]:
            entry["source_mentions"].append(mention)

        raw = raw_index["by_url"].get(article.get("normalized_url", ""))
        if not raw:
            raw = raw_index["by_title"].get(normalize_title(article["title"]))
        if raw:
            entry["raw_article_path"] = raw["path"]
            if raw.get("source"):
                entry["source"] = raw["source"]
            raw_quality = summary_quality(raw.get("summary", ""), raw.get("key_points", []))
            current_quality = summary_quality(entry.get("summary", ""), entry.get("key_points", []))
            if raw_quality > current_quality:
                entry["summary"] = raw["summary"] or entry["summary"]
                entry["key_points"] = raw["key_points"][:MAX_KEY_POINTS]
                entry["concept_tags"] = raw["concept_tags"][:MAX_CONCEPT_TAGS]
        else:
            if article.get("summary") and not entry["summary"]:
                entry["summary"] = article["summary"]
            if article.get("key_points") and not entry["key_points"]:
                entry["key_points"] = article["key_points"][:MAX_KEY_POINTS]
            if article.get("concept_tags") and not entry["concept_tags"]:
                entry["concept_tags"] = article["concept_tags"][:MAX_CONCEPT_TAGS]

        if not entry["summary"]:
            entry["summary"] = trim_text(
                f"{article['title']} — source: {article['source']} ({article['type']}, {article['date']})",
                MAX_SUMMARY_CHARS,
            )
        if not entry["concept_tags"]:
            entry["concept_tags"] = extract_concept_tags(article["title"], [], [])[:MAX_CONCEPT_TAGS]

    return [merged[key] for key in ordered_keys]


def score_article_relevance(article):
    """Heuristic domain filter for Lucy's AI/agent wiki."""
    haystack = " ".join([
        article.get("title", ""),
        article.get("summary", ""),
        " ".join(article.get("key_points", [])),
        " ".join(article.get("concept_tags", [])),
    ]).lower()

    score = 0
    for term, weight in RELEVANCE_TERMS.items():
        if term in haystack:
            score += weight

    if article.get("raw_article_path"):
        score += 1
    if len(article.get("source_mentions", [])) > 1:
        score += 1
    return score


def filter_relevant_articles(articles):
    """Keep AI/LLM/agent-relevant items while retaining some scoring metadata."""
    kept = []
    for article in articles:
        score = score_article_relevance(article)
        article["relevance_score"] = score
        if score >= 2:
            kept.append(article)
    return kept


def sort_articles_for_prompt(articles):
    """Prioritize dense, cross-source items for the injected prompt."""
    return sorted(
        articles,
        key=lambda article: (
            article.get("relevance_score", 0),
            len(article.get("key_points", [])),
            len(article.get("source_mentions", [])),
            1 if article.get("raw_article_path") else 0,
            len(article.get("summary", "")),
        ),
        reverse=True,
    )


def summarize_omitted_articles(articles):
    """Keep a compact record of what was omitted after ranking."""
    omitted = []
    for article in articles[:12]:
        omitted.append({
            "title": article["title"],
            "relevance_score": article.get("relevance_score", 0),
            "source": article.get("source"),
        })
    return omitted


def main():
    start_date, end_date = get_date_range()

    print(f"Collecting dreaming input: {start_date} to {end_date}", file=sys.stderr)

    rss_articles = collect_scan_reports(start_date, end_date)
    print(f"  RSS scan articles: {len(rss_articles)}", file=sys.stderr)

    nl_articles = collect_newsletters(start_date, end_date)
    print(f"  Newsletter articles: {len(nl_articles)}", file=sys.stderr)

    raw_index = build_raw_article_index(start_date)
    raw_summary_count = len(raw_index["by_url"])
    print(f"  Recent raw article summaries indexed: {raw_summary_count}", file=sys.stderr)

    all_articles = enrich_and_merge_articles(rss_articles + nl_articles, raw_index)
    collected_articles = len(all_articles)
    all_articles = filter_relevant_articles(all_articles)
    print(f"  Relevant articles after domain filter: {len(all_articles)} / {collected_articles}", file=sys.stderr)
    all_articles = sort_articles_for_prompt(all_articles)
    # Truncate if too many
    truncated = len(all_articles) > MAX_ARTICLES
    omitted_articles = []
    if truncated:
        print(f"  WARNING: Truncating from {len(all_articles)} to {MAX_ARTICLES} articles", file=sys.stderr)
        omitted_articles = summarize_omitted_articles(all_articles[MAX_ARTICLES:])
        all_articles = all_articles[:MAX_ARTICLES]

    existing_pages = list_existing_wiki_pages()
    print(f"  Existing wiki pages: {len(existing_pages)}", file=sys.stderr)
    wiki_index = build_wiki_index(existing_pages)

    recent_raw = count_recent_raw_articles()
    print(f"  Recent raw articles (lookback window): {recent_raw}", file=sys.stderr)

    source_counts = count_by_source(all_articles)
    date_counts = count_by_date(all_articles)

    output = {
        "range": {"start": start_date, "end": end_date},
        "collected_articles": collected_articles,
        "total_articles": len(all_articles),
        "rss_articles": len(rss_articles),
        "newsletter_articles": len(nl_articles),
        "recent_raw_articles": recent_raw,
        "raw_article_summaries_indexed": raw_summary_count,
        "filtered_out_articles": collected_articles - len(all_articles),
        "truncated": truncated,
        "omitted_articles_sample": omitted_articles,
        "source_counts": source_counts,
        "date_counts": date_counts,
        "articles": all_articles,
        "existing_wiki_pages_count": len(existing_pages),
        "existing_wiki_index": wiki_index,
    }

    # Output JSON to stdout (injected into cron prompt)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
