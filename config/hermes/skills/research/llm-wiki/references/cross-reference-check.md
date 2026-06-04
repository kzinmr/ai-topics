# Active Crawl: Cross-Reference Check Pattern

When running an active crawl, you need to check which candidate topics the wiki
already covers before creating pages. This reusable `execute_code` pattern scans
all wiki `.md` files and reports findings with counts, paths, and statuses.

## The Pattern (Full-Path Matching)

Use full-relative-path matching (not just filename) to catch mentions in `raw/articles/`,
`inbox/`, and other directories. This gives a more complete picture of topic coverage.

```python
import os

wiki = os.path.expanduser("~/wiki")

# List candidate topics (hyphenated slug form — matches wiki filename convention)
candidates = [
    "microsoft-agent-365",
    "amazon-bedrock-agentcore",
    "grok-imagine",
    "nvidia-b300",
    # ... more candidates
]

# Walk all wiki pages, storing relative paths
pages = set()
for root, dirs, files in os.walk(wiki):
    for f in files:
        if f.endswith('.md') and not f.startswith('_'):
            rel = os.path.relpath(os.path.join(root, f), wiki)
            pages.add(rel)

# Check each candidate against full relative path (catches raw/articles/ references too)
results = {}
for c in candidates:
    matches = [p for p in sorted(pages) if c.lower() in p.lower()]
    results[c] = matches

# Print: missing topics first (most useful for gap discovery)
for c, matches in sorted(results.items(), key=lambda kv: len(kv[1])):
    if matches:
        for m in matches:
            print(f"  FOUND: {c} -> {m}")
    else:
        print(f"  MISSING: {c}")

# Then verify specific expected pages exist (quick sanity check after creation)
print("\n=== EXISTING RELEVANT PAGES ===")
existing_checks = [
    ("entities/openai", "openai"),
    ("concepts/ai-military", "ai-military"),
    # ... more paths to verify
]
for path, name in existing_checks:
    full = os.path.join(wiki, path + ".md")
    status = "EXISTS" if os.path.exists(full) else "ABSENT"
    print(f"  {status}: {path}")
```

## Output Interpretation

- **MISSING (0 files):** Topic is a clear gap — good candidate for new page creation
- **FOUND (1-2 files):** Topic has some coverage but may be thin — consider enriching existing page
- **FOUND (3+ files):** Topic is well-covered — skip or enrich with new angle only

## Usage in Active Crawl Workflow

1. Run `web_search` for trending topics → build candidate list (~8-10 topics)
2. Run this cross-reference check to filter to genuinely missing topics
3. Select 3-5 MISSING topics with highest impact for page creation
4. For FOUND topics with thin coverage, consider enriching the existing page

## Tips

- Use hyphenated slug names (matching `SCHEMA.md` filename convention) for best matches
- `os.walk()` is more reliable than `search_files` for wiki discovery (see pitfalls)
- If enriching an existing page, also run `os.path.exists()` to confirm the file before reading/writing
