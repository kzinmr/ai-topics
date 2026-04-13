#!/usr/bin/env python3
"""Trending Topics Detection — finds topics appearing across multiple sources.

Scans recent inbox data (RSS scans, newsletters) and raw articles to detect
topics mentioned by 2+ independent sources. Cross-references with existing
wiki pages to recommend new page creation or updates.

Usage:  python scripts/trending_topics.py              # last 3 days (default)
        python scripts/trending_topics.py --days 7      # last 7 days
"""

import argparse
import datetime
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import NamedTuple

try:
    import yaml
except ImportError:
    yaml = None

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
INBOX_RSS = REPO_ROOT / "inbox" / "rss-scans"
INBOX_NL = REPO_ROOT / "inbox" / "newsletters"
RAW_ARTICLES = REPO_ROOT / "wiki" / "raw" / "articles"
WIKI_ROOT = REPO_ROOT / "wiki"
ENTITIES_DIR = WIKI_ROOT / "entities"
CONCEPTS_DIR = WIKI_ROOT / "concepts"
COMPARISONS_DIR = WIKI_ROOT / "comparisons"

TODAY = datetime.date.today()

# ---------------------------------------------------------------------------
# Known topic patterns — key terms in the AI/LLM domain
# ---------------------------------------------------------------------------

# Entity names: company/product names that are interesting to track
ENTITY_PATTERNS = [
    # Companies
    (r'\bAnthropic\b', 'Anthropic'),
    (r'\bOpenAI\b', 'OpenAI'),
    (r'\bMeta\b(?:\s+AI)?', 'Meta'),
    (r'\bGoogle\b(?:\s+(?:DeepMind|AI))?', 'Google'),
    (r'\bMistral\b', 'Mistral'),
    (r'\bCognition\b', 'Cognition'),
    (r'\bCohere\b', 'Cohere'),
    (r'\bPerplexity\b', 'Perplexity'),
    (r'\bHugging\s*Face\b', 'Hugging Face'),
    (r'\bAi2\b|\bAllen\s+Institute\b', 'Ai2'),
    # Products/Models
    (r'\bClaude\b(?:\s+(?:Code|Mythos|Opus|Sonnet|Haiku)(?:\s+[\d.]+)?)?', 'Claude'),
    (r'\bGPT-?[456]\b(?:\.\d)?', 'GPT'),
    (r'\bGemini\b(?:\s+[\d.]+)?', 'Gemini'),
    (r'\bGemma\b(?:\s+[\d.]+)?', 'Gemma'),
    (r'\bLlama\b(?:\s+[\d.]+)?', 'Llama'),
    (r'\bOLMo\b', 'OLMo'),
    (r'\bQwen\b(?:\s+[\d.]+)?', 'Qwen'),
    (r'\bDevin\b', 'Devin'),
    (r'\bOpenClaw\b', 'OpenClaw'),
    (r'\bCursor\b', 'Cursor'),
    (r'\bMuse\s+Spark\b', 'Muse Spark'),
    (r'\bWindsurf\b', 'Windsurf'),
]

# Concept patterns: technical topics
CONCEPT_PATTERNS = [
    (r'\bagent(?:ic)?\s+(?:engineering|framework|orchestrat)', 'agentic engineering'),
    (r'\bagent\s+(?:swarm|team)s?\b', 'agent swarms'),
    (r'\bMCP\b|\bModel\s+Context\s+Protocol\b', 'MCP'),
    (r'\bRAG\b|\bretrieval[- ]augmented', 'RAG'),
    (r'\bfine[- ]?tun(?:e|ing)\b', 'fine-tuning'),
    (r'\bRLHF\b|\breinforcement\s+learning\s+from\s+human', 'RLHF'),
    (r'\bprompt\s+(?:engineering|caching|injection)', 'prompt engineering'),
    (r'\beval(?:uation)?s?\b(?:\s+(?:framework|tool|driven))?', 'evals'),
    (r'\bcoding\s+agent', 'coding agents'),
    (r'\bAI\s+(?:safety|alignment)\b', 'AI safety'),
    (r'\bopen[- ]?source\s+(?:AI|model|LLM)', 'open-source AI'),
    (r'\bneurosymbolic\b', 'neurosymbolic AI'),
    (r'\bDistillat(?:ion|e)\b', 'distillation'),
    (r'\bquantiz(?:ation|e|ed)\b|\bGGUF\b', 'quantization'),
    (r'\bred[- ]?team(?:ing)?\b', 'red teaming'),
    (r'\bcontext\s+(?:window|length)\b|\blong[- ]?context\b', 'long context'),
    (r'\bmultimodal\b|\bvision[- ]language\b', 'multimodal'),
    (r'\bvoice\s+(?:mode|agent)|\bspeech[- ]to[- ]text\b|\bTTS\b', 'voice/speech'),
    (r'\bbackground\s+(?:agent|execution)\b', 'background agents'),
    (r'\bmemory\s+(?:system|architecture|management)\b|\bCLAUDE\.md\b', 'AI memory'),
    (r'\bvibe[- ]?cod(?:e|ing)\b', 'vibe coding'),
    (r'\bspec[- ]?driven\s+development\b', 'spec-driven development'),
    (r'\bAI\s+(?:bubble|economics|subprime)\b', 'AI economics'),
    (r'\bsandbox(?:ing|ed)?\b(?:\s+(?:agent|execution))?', 'sandboxing'),
]

# People patterns: opinion leaders
PEOPLE_PATTERNS = [
    (r'\bSimon\s+Willison\b|\bsimonwillison\b', 'Simon Willison'),
    (r'\bAndrej\s+Karpathy\b|\bkarpathy\b', 'Andrej Karpathy'),
    (r'\bGary\s+Marcus\b', 'Gary Marcus'),
    (r'\bGeorge\s+Hotz\b|\bgeohot\b', 'George Hotz'),
    (r'\bArmin\s+Ronacher\b|\bmitsuhiko\b', 'Armin Ronacher'),
    (r'\bPeter\s+Steinberger\b|\bsteipete\b', 'Peter Steinberger'),
    (r'\bDario\s+Amodei\b', 'Dario Amodei'),
    (r'\bSam\s+Altman\b', 'Sam Altman'),
    (r'\bMitchell\s+Hashimoto\b|\bmitchellh\b', 'Mitchell Hashimoto'),
    (r'\bCory\s+Doctorow\b', 'Cory Doctorow'),
    (r'\bEd\s+Zitron\b', 'Ed Zitron'),
    (r'\bDwarkesh\s+Patel\b', 'Dwarkesh Patel'),
    (r'\bEthan\s+Mollick\b|\bemollick\b', 'Ethan Mollick'),
]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

class Mention(NamedTuple):
    topic: str
    category: str  # 'entity', 'concept', 'person'
    source_type: str  # 'rss', 'newsletter', 'raw_article'
    source_file: str
    source_date: datetime.date | None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_date_from_filename(fname: str) -> datetime.date | None:
    """Try to extract YYYY-MM-DD from filename."""
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', fname)
    if m:
        try:
            return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            pass
    # Try daily-scan-YYYY-MM-DD
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', fname)
    if m:
        try:
            return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            pass
    return None


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8', errors='replace')
    except OSError:
        return ''


def extract_mentions(text: str, source_type: str, source_file: str,
                     source_date: datetime.date | None) -> list[Mention]:
    """Extract topic mentions from text using pattern matching."""
    mentions = []
    seen = set()

    for patterns, category in [
        (ENTITY_PATTERNS, 'entity'),
        (CONCEPT_PATTERNS, 'concept'),
        (PEOPLE_PATTERNS, 'person'),
    ]:
        for regex, name in patterns:
            if name in seen:
                continue
            if re.search(regex, text, re.IGNORECASE):
                seen.add(name)
                mentions.append(Mention(
                    topic=name,
                    category=category,
                    source_type=source_type,
                    source_file=source_file,
                    source_date=source_date,
                ))
    return mentions


def collect_recent_files(directory: Path, prefix_pattern: str,
                         days: int) -> list[Path]:
    """Collect files matching a glob, filtered by date in filename."""
    if not directory.is_dir():
        return []
    cutoff = TODAY - datetime.timedelta(days=days)
    result = []
    for f in sorted(directory.glob('*.md')):
        d = parse_date_from_filename(f.name)
        if d and d >= cutoff:
            result.append(f)
        elif d is None:
            # Can't determine date — include if recent by mtime
            try:
                mtime = datetime.date.fromtimestamp(f.stat().st_mtime)
                if mtime >= cutoff:
                    result.append(f)
            except OSError:
                pass
    return result


def find_wiki_page(topic: str) -> str | None:
    """Check if a wiki page exists for this topic. Returns relative path or None."""
    # Normalize topic to slug
    slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')

    # Check entities
    for d in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR]:
        # Direct match
        candidate = d / f"{slug}.md"
        if candidate.exists():
            return str(candidate.relative_to(WIKI_ROOT))
        # Check as directory with _index.md
        candidate_dir = d / slug / "_index.md"
        if candidate_dir.exists():
            return str(candidate_dir.relative_to(WIKI_ROOT))

    # Fuzzy: check if slug appears in any filename
    if len(slug) >= 4:
        for d in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR]:
            if d.is_dir():
                for f in d.rglob('*.md'):
                    if slug in f.stem:
                        return str(f.relative_to(WIKI_ROOT))

    return None


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def analyze(days: int) -> str:
    all_mentions: list[Mention] = []

    # 1. RSS scans
    for f in collect_recent_files(INBOX_RSS, 'daily-scan-*.md', days):
        text = read_file(f)
        d = parse_date_from_filename(f.name)
        all_mentions.extend(extract_mentions(text, 'rss', f.name, d))

    # 2. Newsletters
    for f in collect_recent_files(INBOX_NL, '*.md', days):
        text = read_file(f)
        d = parse_date_from_filename(f.name)
        all_mentions.extend(extract_mentions(text, 'newsletter', f.name, d))

    # 3. Raw articles (date-prefixed only — skip noisy substack redirect/app-link scrapes)
    for f in collect_recent_files(RAW_ARTICLES, '*.md', days):
        # Skip low-quality scrapes (substack redirect/app-link pages are duplicates)
        if f.name.startswith(('substack.com--redirect', 'substack.com--app-link',
                              'substack.com--profile', 'substack.com--@')):
            continue
        text = read_file(f)
        d = parse_date_from_filename(f.name)
        all_mentions.extend(extract_mentions(text, 'raw_article', f.name, d))

    # Group by topic
    topic_mentions: dict[str, list[Mention]] = defaultdict(list)
    for m in all_mentions:
        topic_mentions[m.topic].append(m)

    # Calculate cross-source scores
    # A topic is "trending" if it appears in 2+ distinct source files
    class TopicScore(NamedTuple):
        topic: str
        category: str
        source_count: int  # unique source files
        source_types: set  # rss, newsletter, raw_article
        source_files: list
        wiki_page: str | None

    scored: list[TopicScore] = []
    for topic, mentions in topic_mentions.items():
        unique_sources = set(m.source_file for m in mentions)
        source_types = set(m.source_type for m in mentions)
        category = mentions[0].category

        if len(unique_sources) >= 2:
            wiki_page = find_wiki_page(topic)
            scored.append(TopicScore(
                topic=topic,
                category=category,
                source_count=len(unique_sources),
                source_types=source_types,
                source_files=sorted(unique_sources),
                wiki_page=wiki_page,
            ))

    scored.sort(key=lambda x: (-x.source_count, x.topic))

    # ---------------------------------------------------------------------------
    # Build report
    # ---------------------------------------------------------------------------
    cutoff = TODAY - datetime.timedelta(days=days)
    lines = [
        f"# 🔥 Trending Topics — {TODAY.strftime('%Y-%m-%d')}",
        f"",
        f"Analysis period: {cutoff.strftime('%Y-%m-%d')} → {TODAY.strftime('%Y-%m-%d')} ({days} days)",
        f"",
        f"Topics mentioned in **2+ independent sources** across RSS scans, newsletters, and raw articles.",
        f"",
    ]

    # Summary stats
    rss_count = len(collect_recent_files(INBOX_RSS, '*.md', days))
    nl_count = len(collect_recent_files(INBOX_NL, '*.md', days))
    raw_count = len(collect_recent_files(RAW_ARTICLES, '*.md', days))
    lines.append(f"**Sources scanned:** {rss_count} RSS reports, {nl_count} newsletters, {raw_count} raw articles")
    lines.append(f"**Trending topics found:** {len(scored)}")
    lines.append("")

    if not scored:
        lines.append("_No trending topics found in this period._")
        return "\n".join(lines)

    # --- Section 1: Action Required (no wiki page) ---
    no_page = [s for s in scored if s.wiki_page is None]
    has_page = [s for s in scored if s.wiki_page is not None]

    if no_page:
        lines.append("## 🆕 New Page Recommended")
        lines.append("")
        lines.append("These trending topics have **no wiki page** yet:\n")
        lines.append("| Topic | Type | Sources | Source Types |")
        lines.append("|-------|------|---------|-------------|")
        for s in no_page:
            types_str = ', '.join(sorted(s.source_types))
            lines.append(f"| **{s.topic}** | {s.category} | {s.source_count} | {types_str} |")
        lines.append("")

    # --- Section 2: Update Recommended (has wiki page + new mentions) ---
    if has_page:
        lines.append("## 📝 Update Recommended")
        lines.append("")
        lines.append("These trending topics already have wiki pages with new activity:\n")
        lines.append("| Topic | Type | Sources | Wiki Page | Source Types |")
        lines.append("|-------|------|---------|-----------|-------------|")
        for s in has_page:
            types_str = ', '.join(sorted(s.source_types))
            lines.append(f"| **{s.topic}** | {s.category} | {s.source_count} | `{s.wiki_page}` | {types_str} |")
        lines.append("")

    # --- Section 3: Hot Topics (source count >= 4) ---
    hot = [s for s in scored if s.source_count >= 4]
    if hot:
        lines.append("## 🔥🔥 Hot Topics (4+ sources)")
        lines.append("")
        lines.append("| Topic | Type | Sources | Source Types | Wiki |")
        lines.append("|-------|------|---------|-------------|------|")
        for s in hot:
            types_str = ", ".join(sorted(s.source_types))
            wiki_str = f"`{s.wiki_page}`" if s.wiki_page else "❌ NEW"
            lines.append(f"| **{s.topic}** | {s.category} | {s.source_count} | {types_str} | {wiki_str} |")
        lines.append("")

    # --- Section 4: Cross-type topics (appear in both RSS + newsletter or + raw) ---
    cross_type = [s for s in scored if len(s.source_types) >= 2]
    if cross_type:
        lines.append("## 🔀 Cross-Source Topics")
        lines.append("")
        lines.append("Topics appearing in multiple source types (higher signal):\n")
        for s in cross_type:
            types_str = ' + '.join(sorted(s.source_types))
            page_str = f" → `{s.wiki_page}`" if s.wiki_page else " → **NEW**"
            lines.append(f"- **{s.topic}** ({s.source_count} sources: {types_str}){page_str}")
        lines.append("")

    # --- Section 5: Category breakdown ---
    lines.append("## 📊 Category Breakdown")
    lines.append("")
    cat_counts = Counter(s.category for s in scored)
    for cat, count in cat_counts.most_common():
        lines.append(f"- **{cat}**: {count} trending topics")
    lines.append("")

    lines.append("---")
    lines.append("_Generated by `scripts/trending_topics.py`_")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Detect trending topics in wiki sources")
    parser.add_argument('--days', type=int, default=3,
                        help='Look-back window in days (default: 3)')
    args = parser.parse_args()

    print(analyze(args.days))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f"# Trending Topics — ERROR\n\n```\n{exc}\n```", file=sys.stderr)
    sys.exit(0)
