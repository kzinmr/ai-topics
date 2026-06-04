---
name: wiki-raw-article-curation
category: wiki
description: Systematically reduce unprocessed raw article count reported by wiki_health.py by linking L2 pages (entities, concepts, comparisons) to raw article filenames. Covers both high-value article enrichment and high-volume bulk-association strategies.
---

# Wiki Raw Article Curation

Systematic approach to reducing the "unprocessed raw articles" count reported by `wiki_health.py`. The health check reports a raw article as "unprocessed" if its filename (stem) is not found as a substring anywhere in L2 page content.

## Detection

Run `wiki_health.py` and check the "Unprocessed Raw Articles" section. The count represents articles that have not been referenced from any L2 page.

```bash
python3 ~/ai-topics/scripts/wiki_health.py | grep -A 3 "Unprocessed Raw Articles"
```

## Domain Analysis (Always Do First)

Before any enrichment, run a domain breakdown of unprocessed articles. This reveals the landscape and tells you how to group your work:

```python
from pathlib import Path
from collections import Counter

WIKI_RAW = Path("wiki/raw/articles")
# Build l2_blob from all L2 dirs
l2_blob = ""
for d in [Path("wiki/entities"), Path("wiki/concepts"), Path("wiki/comparisons")]:
    for p in d.rglob("*.md"):
        l2_blob += p.read_text()

unprocessed = []
for raw_path in sorted(WIKI_RAW.glob("*.md")):
    stem = raw_path.stem
    if stem not in l2_blob and raw_path.name not in l2_blob:
        unprocessed.append(raw_path)

domains = Counter()
for p in unprocessed:
    domain = p.name.split("--")[0] if "--" in p.name else p.name.split("_")[0]
    domains[domain] += 1

for domain, count in domains.most_common():
    print(f"{domain}: {count}")
```

This gives you immediate groupings like:
- `wheresyoured.at: 14` → single author, associate into existing entity
- `1wwzn.mjt.lu: 10` → newsletter tracking pixels → blogwatcher.md catch-all
- `mahadk.com: 7` → single author, associate into existing entity
- `2026-04-28_something: 1` → standalone article (may need entity page or concept enrichment)

## Mixed-Strategy Approach (small backlog: <100 unprocessed)

When the backlog is small (<100 unprocessed), use a **mixed strategy**: deep-read a few high-value articles (Tier 1) then bulk-associate everything remaining (Tier 2). Do not bulk-associate first — you want to identify enrichment opportunities before the bulk pass removes visibility.

### "Already Consumed but Unlinked" Check

Many unprocessed articles have their **content already reflected in wiki pages** but the **filename is absent** from any L2 page. Common causes:
- Auto-generated entity pages with `status: skeleton` that list articles via hash-references in a References section (wheresyoured.at, mahadk.com patterns)
- Concept pages created from the article that didn't include the filename in `sources:` frontmatter (searchcode, pydantic-ai-harness)
- Newsletter/crawl artifacts scraped as metadata-only

**How to check:** Search for a unique phrase from the article content in L2 pages:
```bash
grep -r "unique-phrase" wiki/entities/ wiki/concepts/ --include="*.md" -l
```
If content is found, the article was consumed — just add its filename to the Sources section.

### Association Targets (Where to Put Filenames)

| Article Type | Best Target | Method |
|---|---|---|
| Author blog (ed-zitron, mahadk, gilesthomas) | Their entity page | Add to References section at bottom |
| Technical concept (harness, agent search) | Relevant concept page | Add to `sources:` frontmatter array or Sources section |
| Newsletter tracking pixel / click-link | `wiki/concepts/blogwatcher.md` | Add bullet to Sources section (catch-all) |
| Misc news (theverge, cnbc, etc.) | `wiki/concepts/blogwatcher.md` | Same catch-all |
| Metadata-only / scrape artifacts | `wiki/concepts/blogwatcher.md` | Same catch-all |

**Two locations for filenames:**
1. **Markdown References section**: `- filename.md` at bottom of page. Easier to patch.
2. **YAML frontmatter `sources:` array**: `"raw/articles/filename.md"`. More structured but **prone to Escape-drift** when patching because YAML quotes conflict with the patch tool's quote handling. Prefer the markdown References section unless frontmatter is the established pattern for that page.

## Two-Tier Strategy

### Tier 1: High-Value Articles (Enrich/Extend)

For articles with rich, actionable content — create or update L2 pages with substantial new information:

**Pattern:**
1. Identify high-value raw articles (technical depth, strategic importance, unique data)
2. Check if an entity/concept page already exists for the topic
3. Either:
   - **Update existing page**: Add a new section referencing the raw article + extract actionable content
   - **Create new page**: If no existing page covers the topic, create a new concept/entity page
4. Ensure the raw article filename (e.g., `crawl-2026-04-18-measuring-agent-autonomy`) appears as a substring in the L2 page's content (either in the References section or as a sources link)
5. Commit: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: enrich <topic> with latest" && git push`

**Sources of high-value content:**
- `kuber.studio` articles (deep technical source code analysis)
- Anthropic/OpenAI/Google official blog posts
- arXiv papers with technical depth
- Minimaxir, Simon Willison, Andrej Karpathy blog posts
- Multi-agent production architecture articles

### Tier 2: Low-Value Articles (Bulk-Associate)

For articles with metadata or minor data — bulk-associate into existing L2 pages:

**Pattern:**
1. Take batches of 20-50 articles (minimaxir posts, newsletter digests, crawl artifacts)
2. Find an existing concept/entity page that broadly covers the topic
3. Add a single line: `- crawl-2026-04-12-nano-banana-prompts.md` (or whatever the filename is)
4. The article filename just needs to appear as a substring somewhere in the L2 page

**Strategy:**
- Group by topic: all minimaxir articles → one L2 page, all newsletter articles → inbox/newsletters concept, all crawl artifacts → crawl-log concept
- Use `wiki/entities/` or `wiki/concepts/` subdirectory pages to batch-group articles efficiently
- The goal is volume reduction, not curation quality

### Tier 3: Zero-Value Articles (Archive/Prune)

For articles with no actionable content:
- `status: skeleton` entity pages with no enrichment
- Duplicates with no additional value
- Newsletter digests that were already processed

## Key Insight: Substring Matching Quirk

`wiki_health.py` checks if the raw article filename stem appears as a **substring** in any L2 page content:

```python
# Pseudo-code from wiki_health.py line 210-216
stem = raw_path.stem  # e.g., "crawl-2026-04-18-measuring-agent-autonomy"
if stem in l2_blob and name in l2_blob:  # both checked
    processed
else:
    unprocessed.append(raw_path)
```

This means:
- Adding the filename to any section (Sources, References, Sources, See Also) will clear it
- Even adding `crawl-2026-04-12-nano-banana-prompts` to a Sources section line is enough
- You don't need to add rich content — just the filename string suffices

## Execution Order

1. **Tier 1 first** — high-value articles that genuinely improve wiki quality
2. **Tier 2 bulk** — mass-associate low-value articles into existing pages (fastest count reduction)
3. **Tier 3 prune** — remove zero-value articles, then re-check
4. **Verify** — run `wiki_health.py` and confirm count decreased

## Verification

```bash
python3 ~/ai-topics/scripts/wiki_health.py | grep -A 5 "Unprocessed Raw Articles"
```

Target: Reduce from 1000+ → <200 within 2-3 sessions.

## Bulk-Associate Workflow (1000+ articles)

For large-scale curation (like reducing 1896 → 0 unprocessed):

### Step 1: Domain Analysis
```python
from pathlib import Path
from collections import defaultdict

WIKI_ENTITIES = Path("wiki/entities")
WIKI_RAW = Path("wiki/raw/articles")

# Load all L2 content
l2_content = ""
for p in WIKI_ENTITIES.rglob("*.md"):
    l2_content += p.read_text()

# Find unprocessed articles
unprocessed = []
for raw_path in WIKI_RAW.glob("*.md"):
    stem = raw_path.stem
    name = raw_path.name
    if stem not in l2_content and name not in l2_content:
        unprocessed.append(raw_path)

# Group by domain for batch processing
def extract_domain(name):
    parts = name.split("--")
    return parts[0] if len(parts) >= 2 else name.split("_")[0]

domains = defaultdict(list)
for p in unprocessed:
    domains[extract_domain(p.name)].append(p)
```

### Step 2: Keyword-to-Entity Mapping
Create a comprehensive keyword map covering both domains AND filename patterns:
```python
keyword_map = {
    # Domain-based keywords
    "wheresyoured.at": "wheresyoured-at",
    "minimaxir.com": "minimaxir",
    "simonwillison.net": "simon-willison",
    "gilesthomas.com": "gilesthomas",
    "hugotunius.se": "hugotunius",
    "mahadk.com": "mahadk",
    "beehiiv.com": "beehiiv",
    "danieldelaney.net": "danieldelaney",
    "theverge.com": "the-verge",
    # Filename-based keywords (crawl artifacts, dates)
    "harness": "harness-engineering",
    "claude": "claude-code",
    "multi-agent": "multi-agent-production-architecture",
    "agent-sandbox": "agent-sandbox-patterns",
    "agentic": "agentic-engineering",
    "measuring-agent-autonomy": "measuring-agent-autonomy",
}
```

### Step 3: Batch Update Entity Pages
```python
entity_pages = {p.stem.lower(): p for p in WIKI_ENTITIES.rglob("*.md")}

for entity, stems in entity_refs.items():
    page_path = entity_pages.get(entity.lower())
    if not page_path:
        # Create minimal skeleton
        page_path = WIKI_ENTITIES / f"{entity}.md"
        page_path.write_text(f"---\ntitle: {entity}\ntype: entity\nstatus: skeleton\n---\n\n# {entity}\n\n## References\n\n")
    
    content = page_path.read_text()
    # Append references section if missing, else add to existing
    if "## References" in content:
        new_content = content.rstrip() + "\n" + "\n".join(f"- {s}" for s in stems) + "\n"
    else:
        new_content = content.rstrip() + f"\n\n## References\n\n" + "\n".join(f"- {s}" for s in stems) + "\n"
    page_path.write_text(new_content)
```

### Step 4: Handle Remaining Unmatched Articles
- Create minimal entity pages for truly orphan domains
- Use fallback keyword matching (partial domain names, dates, topics)
- Verify with `wiki_health.py` after each batch

## Common Pitfalls

- **Don't create new pages just to reference one article** — bulk-associate into existing pages first
- **Remember the substring check requires EXACT stem match** — the raw article's filename stem (e.g., `wheresyoured.at--the-ai-industry-is-lying-to-you--00c54f74`) must appear verbatim in L2 content. Partial matches, domain-only mentions, or modified stems won't clear the article from unprocessed status.
- **Don't overwrite L2 page content** — always append to existing sections, don't `write_file` over them unless you're doing a controlled full-page rewrite (which should be rare)
- **Don't forget to update `index.md`** when creating new L2 pages
- **Don't update `log.md` for bulk-associate** — only when creating new pages or doing meaningful enrichment
- **Keyword matching is order-sensitive** — check specific/long keywords first to avoid premature matches on generic terms
- **Create missing entity pages before batch-updating** — the bulk-associate script will fail if `entity_pages` doesn't have the target
- **Escape-drift on YAML frontmatter patches**: When patching `sources:` arrays in YAML frontmatter, the `patch` tool can hit `Escape-drift` because YAML quoted strings (`"raw/articles/file.md"`) conflict with the patch tool's quote detection. **Fix:** Use `execute_code` with `write_file` to safely rewrite frontmatter, or add the filename to a markdown References section instead.
- **Patch ordering**: When patching a markdown Sources/References section, prepend new entries before existing ones to keep the freshest content visible. Avoid relying on `replace_all=True` unless every instance should be changed.
- **Verify after each batch**: Run `wiki_health.py` after each batch of 20-30 article associations. The count should drop monotonically. A spike means the filename wasn't matched.

## When to Use

- `wiki_health.py` reports 1000+ unprocessed raw articles (large backlog → prioritize Tier 2 bulk-association)
- User asks "未処理のraw記事を少しずつ内容読んでwikiに取り込んで" (small backlog <200 → mixed strategy: deep-read high-value + bulk-associate rest)
- User says "wiki_healthの結果に従って" or "raw_article_curationを解決して"
- Bulk-associating low-value articles is the fastest path (bulk-associate, not enrich)
- When the user wants partial solution — "一部で良い" → Tier 2 is appropriate (not full Tier 1)
- When processing articles from the 1000+ pile, prioritize Tier 2 bulk-association first

## Prioritization Within a Session

Within a single batch session, process articles in this priority order:

1. **Deep-read high-value articles** (Tier 1) — wheresyoured.at economics analysis, iii platform architecture, self-healing harness case studies, anything with production metrics or architecture diagrams. Create new pages if needed.
2. **Associate author articles into their entity pages** — known authors (ed-zitron, mahadk, gilesthomas, boyter) whose content is already captured in existing entity/concept pages. Just add filename references.
3. **Consumed-but-unlinked articles** — articles whose content is fully captured in existing L2 pages but filenames are absent. Simple filename addition.
4. **Bulk-associate remainder into blogwatcher.md** — newsletter tracking pixels, misc news, metadata-only articles. Catch-all.