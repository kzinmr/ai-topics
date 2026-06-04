# Common Pitfalls in Wiki Article Processing

## 1. Tag Taxonomy Pre-Commit Hook Blocks Commit

The pre-commit hook validates that every tag in frontmatter exists in `wiki/SCHEMA.md`'s taxonomy. When adding a new entity with tags not yet in the taxonomy (e.g., `python`, `sentry`, `vercel`), the commit will be rejected.

**Error pattern:**
```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (2):
   wiki/entities/example.md:  python
   wiki/entities/example.md:  sentry
```

**Fix workflow:**
1. Read the error output to identify which tags are missing and which files use them
2. **Fast fix (preferred for synonyms)**: If a semantically equivalent tag already exists in SCHEMA.md (e.g., `organization` → `company`, `cdn` → `infrastructure`), just replace the tag in your page's frontmatter. No SCHEMA.md change needed.
3. **Thorough fix**: If the tag represents a genuinely new category, add it to the appropriate category in `wiki/SCHEMA.md`:
   - Company/org names → **People/Orgs** (e.g., `sentry`, `vercel`)
   - Language names → **Engineering** (e.g., `python`)
   - Tools/products → **Products**
4. `git add wiki/SCHEMA.md` (if changed) and re-commit — the hook should now pass

**Prevention:** Before writing entity frontmatter, check if each planned tag exists in SCHEMA.md taxonomy. Quick check: `grep "tag-name" wiki/SCHEMA.md`.

## 2. web_extract Content Truncation

`web_extract` summarizes articles over ~5000 chars, truncating with `[... summary truncated for context management ...]`. For long-form technical articles that need full content preservation, the summary may lose critical details (code examples, nuanced arguments, full design principle lists).

**Detection:** Check `len(content)`. If <6000 chars AND content ends with the truncation marker, the article was summarized. The markdown output will show the truncation clearly.

**Fallback — curl + Python text extraction:**
```python
import subprocess, re
result = subprocess.run(
    ["curl", "-sL", url],
    capture_output=True, text=True, timeout=15
)
html = result.stdout

# Strip HTML tags (basic approach)
body = re.sub(r'<pre[^>]*>.*?</pre>', lambda m: '\n```\n' + re.sub(r'<[^>]*>', '', m.group(0)) + '\n```\n', html, flags=re.DOTALL)
body = re.sub(r'<[^>]*>', ' ', body)
body = re.sub(r'&amp;', '&', body)
body = re.sub(r'&lt;', '<', body)
body = re.sub(r'&gt;', '>', body)
body = re.sub(r'&quot;', '"', body)
body = re.sub(r'&#39;', "'", body)
body = re.sub(r'\n\s*\n\s*\n+', '\n\n', body)
body = body.strip()
```
Save the raw output to `wiki/raw/articles/` using the filename policy from `raw-article-filename-policy`.

**Note:** The fallback may include JS/metadata cruft — the raw layer tolerates this. Manual cleanup before saving is optional but not required for Layer 1 (immutable sources).

**Alternative:** Check if the site offers a `.md` endpoint (Armin Ronacher's blog does: `/2026/2/9/a-language-for-agents.md`). Some static site generators preserve source markdown.

## 3. Concept Page Alias Matching (Enrich, Don't Duplicate)

When an existing concept page has an `aliases:` frontmatter field that matches the topic you're about to create, **enrich the existing page** instead of creating a duplicate.

**Example:** `concepts/agent-ergonomics.md` has `aliases: [agent-oriented-language-design]`. When ingesting Armin Ronacher's "A Language For Agents" (which is about agent-oriented language design), add a new section to the existing page rather than creating `concepts/agent-oriented-language-design.md`.

**Check:** Before creating a concept page, search for matching aliases: `grep -r "aliases.*your-topic" wiki/concepts/`.
