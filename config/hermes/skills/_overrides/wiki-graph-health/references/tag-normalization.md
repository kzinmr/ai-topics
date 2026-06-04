# Tag Normalization Reference

## When to Run

- After wiki-health reports 500+ non-standard unique tags
- When new canonical tags are added to SCHEMA.md
- Periodic maintenance (quarterly)

## Approach

### 1. Analyze Current Tags

```python
python3 scripts/tag_normalization.py --dry-run
```

To see the tag distribution first:
```python
import re, os
from collections import Counter
wiki = os.path.expanduser("~/wiki")
all_tags = Counter()

def extract_tags(filepath):
    with open(filepath) as f:
        content = f.read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m: return []
    front = m.group(1)
    tags = []
    # Block format (handles both single and double space indent)
    block_match = re.search(r'^tags:\n((?:[ \t]*- .*\n?)+)', front, re.MULTILINE)
    if block_match:
        for line in block_match.group(1).split('\n'):
            line = line.strip()
            if line.startswith('- '):
                tag = line[2:].strip().strip('"\'')
                if tag: tags.append(tag)
        return tags
    # Inline format
    inline_match = re.search(r'^tags:\s*\[(.+)\]', front, re.MULTILINE)
    if inline_match:
        for t in inline_match.group(1).split(','):
            tag = t.strip().strip('"\'').strip()
            if tag: tags.append(tag)
        return tags
    return tags

for root, dirs, files in os.walk(os.path.join(wiki, 'entities')):
    for f in files:
        if f.endswith('.md'):
            all_tags.update(extract_tags(os.path.join(root, f)))
for root, dirs, files in os.walk(os.path.join(wiki, 'concepts')):
    for f in files:
        if f.endswith('.md'):
            all_tags.update(extract_tags(os.path.join(root, f)))
for root, dirs, files in os.walk(os.path.join(wiki, 'comparisons')):
    for f in files:
        if f.endswith('.md'):
            all_tags.update(extract_tags(os.path.join(root, f)))

for tag, count in all_tags.most_common(100):
    print(f'{count:4d}x  {tag}')
```

### 2. Build / Extend the Mapping

Edit `scripts/tag_normalization.py` — add new entries to `TAG_NORMALIZATION` dict.

Rules for mapping:
- **Plural → canonical**: `evals` → `evaluation`
- **Synonym → canonical**: `llm` → `model`, `finetuning` → `fine-tuning`
- **Case → lowercase**: `RAG` → `rag`, `OpenAI` → `openai`
- **Very specific → category**: `attention` → `model`, `docker` → `developer-tooling`

### 3. Apply Normalization

```bash
python3 ~/wiki-graph-health/scripts/tag_normalization.py
```

### 4. Verify

```bash
# Check no content was lost (verify file sizes)
cd ~/ai-topics && git diff --stat HEAD

# Spot-check a few modified files
grep -A3 'tags:' wiki/entities/drmaciver.md

# Verify headings exist (no body loss)
grep -c '^# ' wiki/entities/drmaciver.md
```

### 5. Commit

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: tag normalization" && git push
```

## CRITICAL Pitfalls

### 🛑 BODY-DROPPING BUG (most expensive mistake)

The `normalize_page()` function MUST preserve the body content after the frontmatter closing `---`:

```python
# CORRECT:
m = re.match(r'^(---\n)(.*?)(\n---)', content, re.DOTALL)
body = content[m.end():]  # Everything after closing ---
# ... modify front ...
return opener + new_front + closer + body  # MUST include body!

# WRONG (drops all markdown content):
return opener + new_front + closer
```

This is the #1 cause of wiki corruption during batch editing. Always verify with `wc -l` and `grep -c '^# '` after a batch run.

### 🛑 YAML PARSER UNAVAILABLE

The production environment has no `yaml`/`pyyaml` module. Do NOT depend on it. Use regex extraction instead.

### 🛑 SINGLE-SPACE YAML INDENT

Some files use single-space indentation for tag list items:
```yaml
tags:
 - tag1
 - tag2
```
Instead of the more common double-space:
```yaml
tags:
  - tag1
  - tag2
```
The regex `r'^tags:\n((?:[ \t]*- .*\n?)+)'` handles both (uses `[ \t]*` not `  `).

### 🛑 DASH TAG FALSE POSITIVE

Some files have `tags:` with no values (empty list). The tag extractor's fallback regex `tags:\s*(\S+)` can capture the next line's `- ` as the tag name, producing a false `-` tag. This is NOT a real tag — fix it by skipping empty tags fields.

### 🛑 PREFIX-STYLE WIKILINKS ARE NOT BROKEN

`[[concepts/harness-engineering]]`, `[[entities/openai]]`, `[[concepts/_index]]` — these look like broken links because the slug doesn't match the filename, but they are VALID Obsidian-style path wikilinks. They resolve correctly. Do NOT strip the prefixes unless the content is being moved.
