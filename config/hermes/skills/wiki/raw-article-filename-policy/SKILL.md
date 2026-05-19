---
name: raw-article-filename-policy
description: Naming convention for raw article files in wiki/raw/articles/ — always use the actual publication date, not the date of ingestion.
trigger: When saving a raw article to wiki/raw/articles/ — before writing any article file, determine the real publication date and construct the filename accordingly.
---

# Raw Article Filename Policy

## Academic Papers (`wiki/raw/papers/`)

**Filename = `{YYYY-MM-DD}_{arxiv-id}_{short-title}.md`**

Where:
- `YYYY-MM-DD` = the publication date (or first arXiv submission date if exact date unknown)
- `arxiv-id` = arXiv ID without version suffix (e.g., `2512.24601`, NOT `2512.24601v2`)
- `short-title` = 2-5 hyphenated keywords (lowercase, 40 chars max)

For non-arXiv papers (conference proceedings, tech reports without arXiv IDs):
- **Filename = `{YYYY-MM-DD}_{source}_{short-title}.md`**
- Where `source` = `acl`, `emnlp`, `neurips`, `icml`, `meta`, `deepseek`, etc.

### Dedup Check (MANDATORY before saving)
Before saving ANY new paper to `wiki/raw/papers/`, run:
```bash
python3 scripts/papers_index.py --check <arxiv-url-or-id>
```
If it returns `DUPLICATE`, DO NOT create a new file — update the existing one instead.
If you create a new file, register it: `python3 scripts/papers_index.py --add <filename> <url>`

The index is at `wiki/raw/papers/.papers_index.json` and maps identifiers to canonical filenames.

### Examples

| Paper | Source Date | Filename |
|-------|------------|----------|
| Recursive Language Models (arXiv:2512.24601) | 2025-12-31 | `2025-12-31_2512.24601_recursive-language-models.md` |
| DeepSeek-V3 (arXiv:2412.19437) | 2024-12-27 | `2024-12-27_2412.19437_deepseek-v3-technical-report.md` |
| GEPA (arXiv:2507.19457) | 2025-07-25 | `2025-07-25_2507.19457_gepa-reflective-prompt-evolution.md` |
| DeepSeek-V4 (HuggingFace) | 2026-04-xx | `2026-04-xx_deepseek-v4-technical-report.md` |

## Original `wiki/raw/articles/` Policy

**Filename = `{YYYY-MM-DD}_{source-slug}_{content-slug}.md`**

Where:
- `YYYY-MM-DD` = the ACTUAL publication date of the article (verified from the source, NOT today's date)
- `source-slug` = abbreviated domain or source name (lowercase, no dots: `interconnects`, `pelayoarbues`, `simonwillison`, `arxiv`, `anthropic`)
- `content-slug` = 2-5 word descriptive title (lowercase, hyphenated, 30 chars max)

## Examples

| Article | Source Date | Filename |
|---------|------------|----------|
| Nathan Lambert on synthetic data (interconnects.ai) | 2023-11-29 | `2023-11-29_interconnects-llm-synthetic-data.md` |
| Pelayo Arbués on dataset engineers (pelayoarbues.com) | 2025-01-16 | `2025-01-16_pelayoarbues-dataset-engineer.md` |
| Megadocs synthetic pretraining (arXiv) | 2026-03-19 | `2026-03-19_megadocs-synthetic-pretraining.md` |
| Khairallah context engineering course (X Article) | 2026-05-10 | `2026-05-10_engkhairallah_context-engineering-master-course.md` |

### X Article / X Note Tweet Naming

For X Article and X Note Tweet raw articles:
- `source-slug` = the X handle **without `@`** (e.g., `eng_khairallah1` → `engkhairallah1`), underscores stripped
- `date` = `created_at` from the parent tweet's API response
- Frontmatter must include `type: x_article` or `type: x_note_tweet`
- Example: `2026-05-10_engkhairallah_context-engineering-master-course.md`

## How to Find the Real Publication Date

### Priority Order

1. **Meta tags in HTML** — `<meta property="article:published_time">`, `<time datetime="...">`, JSON-LD `datePublished`
2. **Page text** — Look for "Published", "Posted", "Updated" dates in article header/footer
3. **URL patterns** — Some blogs embed dates in URL (e.g., `/2024/01/15/title`)
4. **RSS feed** — `<pubDate>` or `<dc:date>` in the feed XML
5. **Search engine snippet** — Google/Bing search results often show publication dates
6. **Social media cross-post** — Check the X/Twitter or LinkedIn post announcing the article. For LinkedIn posts specifically, extract `datePublished` from JSON-LD `SocialMediaPosting` — see `references/linkedin-date-extraction.md`.

### Verification Steps

```python
import urllib.request, re

url = "https://example.com/article"
resp = urllib.request.urlopen(url, timeout=10)
html = resp.read().decode("utf-8")

# Check meta tags
for m in re.finditer(r'<meta[^>]*property=["\']article:published_time["\'][^>]*content=["\']([^"\']+)["\']', html):
    print("Meta published:", m.group(1))  # 2023-11-29T...

# Check time tags
for m in re.finditer(r'<time[^>]*datetime=["\']([^"\']+)["\']', html):
    print("Datetime attr:", m.group(1))

# Check JSON-LD
for m in re.finditer(r'"datePublished"\s*:\s*"([^"]+)"', html):
    print("JSON-LD datePublished:", m.group(1))
```

## Pitfalls

- **DO NOT use today's date** — the filename must reflect when the content was published, not when you processed it
- **Slides/presentations** — Google Slides, Canva, Figma decks, and similar presentation formats rarely embed a creation date in metadata. Use the ingestion date as the filename date, but add `date_ingested: YYYY-MM-DD` in the YAML frontmatter (not `date` or `date_published`) to distinguish it from a verified publication date.
- **Newsletters** — If the article is from a newsletter digest, the newsletter date ≠ article date. Find the article's original publication date on the source site.
- **Republished content** — If an article was republished on a different platform (e.g., cross-posted to Substack and Medium), use the EARLIEST publication date.
- **Updated articles** — Some articles show "Last updated" instead of "Published". Use the original published date; optionally add `_updated-{YYYY-MM-DD}` suffix if the update was substantial.
- **No date found** — Search the article title + author on Google/Bing. If still no date, use `YYYY-MM-DD_unknown_{slug}.md` and add a `date_unknown: true` frontmatter flag.
- **Archive/wayback date** — As last resort, use the Internet Archive's first capture date.
- **Blog posts vs. raw articles** — `wiki/raw/articles/` is exclusively for externally-sourced finalized article scrapes ingested from newsletters, RSS, web, etc. Original blog posts (Hermes-authored content, user-requested essays) go to `blog/` at the repo root (`~/ai-topics/blog/`). Do NOT write original blog posts into `wiki/raw/articles/`. The `blog/` directory uses a simpler naming convention: `{YYYY-MM-DD}_{author}_{short-slug}.md`.
