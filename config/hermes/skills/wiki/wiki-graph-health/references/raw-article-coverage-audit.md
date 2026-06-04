# Raw Article Coverage Audit

Analysis pattern for identifying `wiki/raw/articles/` files that have zero references from the wiki knowledge base (entities, concepts, comparisons, index.md). This quantifies the ingestion gap.

## Quick Stats (2026-05-11 snapshot)
- Total raw articles: 5,772
- Referenced in wiki: 427 (7.0%)
- Unreferenced: 5,367 (93.0%)
- Referenced but missing from raw/: 22 (link rot)

## Step 1: Extract All Raw Article References from Wiki Pages

The reference format in wiki pages is `raw/articles/filename.md` (not markdown-link syntax, not in code blocks — bare paths, often on bullet lines).

**CRITICAL**: `grep -roh` in execute_code subprocess silently returns empty. Use `find | xargs grep`:

```bash
cd /opt/data/ai-topics
find wiki/entities/ wiki/concepts/ wiki/comparisons/ wiki/index.md \
  -name "*.md" -print0 2>/dev/null \
  | xargs -0 grep -oh 'raw/articles/[^ )>"'$'\t'']*' 2>/dev/null \
  > /tmp/ref_raw.txt
```

## Step 2: Clean Extracted References

References have trailing garbage: `]]`, `]`, `"`, `|`, `)`, display text, continuation lines. Multi-stage cleanup:

```python
import re

with open("/tmp/ref_raw.txt") as f:
    lines = [l.strip() for l in f if l.strip()]

# Stage 1: crude sed strip
# sed 's/[])\]"|'\''\\]*$//' for trailing chars
# Stage 2: Python regex to extract just the .md filename
referenced = set()
for line in lines:
    m = re.search(r'([a-zA-Z0-9][a-zA-Z0-9._%+\-]*\.md)', line)
    if m:
        referenced.add(m.group(1))
```

## Step 3: Compute Coverage

```python
import os
raw_dir = "/opt/data/ai-topics/wiki/raw/articles"
all_raw = set(f for f in os.listdir(raw_dir) if f.endswith(".md") and not f.startswith("."))
unreferenced = all_raw - referenced
print(f"Referenced: {len(referenced)} ({len(referenced)/len(all_raw)*100:.1f}%)")
print(f"Unreferenced: {len(unreferenced)} ({len(unreferenced)/len(all_raw)*100:.1f}%)")
```

## Step 4: Categorize Unreferenced by Source & Date

Two filename formats:
- **Date-prefixed**: `YYYY-MM-DD_source_title.md` (newsletter/manual addition)
- **Domain--slug**: `domain.com--path-slug--hash.md` (blogwatcher-cli RSS scrape)

```python
from collections import Counter

source_counts = Counter()
date_prefix = []
no_date = []
mjtl_files = []

for f in unreferenced:
    if "mjt.lu" in f or "mandrillapp" in f:
        mjtl_files.append(f)  # newsletter tracking — discardable
        continue
    if re.match(r'^\d{4}-\d{2}-\d{2}_', f):
        date_prefix.append(f)
        src = re.match(r'^\d{4}-\d{2}-\d{2}_([a-zA-Z0-9.-]+)', f)
        source_counts[src.group(1).lower() if src else f[:30]] += 1
    else:
        no_date.append(f)
        domain = f.split("--")[0] if "--" in f else "[other]"
        source_counts[domain] += 1
```

## Step 5: Priority Classification

### High Priority (AI-core sources)
Sources directly relevant to AI/LLM ecosystem: cohere, pinecone, fireworks-ai, cursor, mistral-ai, simonwillison.net, anthropic, cartesia, elevenlabs, harvey, glean, hebbia, decagon, factory, ashvardanian.com, martinalderson.com, grantslatton.com, karpathy

### Medium Priority (AI-adjacent blogs)
Interconnects, gwern, andrewchen, lilianweng, xeiaso.net, open.substack.com (specific AI substacks)

### Low Priority (tech-general / non-AI)
blog.llvm.org, boyter.org, danluu.com, paulgraham.com (mix), idea.popcount.org, jyn.dev, overreacted.io, mitchellh.com, johndcook.com, purplesyringa.moe, berthub.eu, seangoedecke.com, susam.net, chiark.greenend.org.uk, oldvcr.blogspot.com, cbloomrants.blogspot.com, databasearchitects.blogspot.com, preshing.com, righto.com, smalldatum.blogspot.com, iczelia.net, rakhim.exotext.com, hex-technologies, warp

### Discardable
`mjt.lu` / `mandrillapp` files — newsletter tracking redirect links with no real content

## Verification After Processing

After ingesting articles into wiki, re-run Steps 1-3 to confirm the gap is shrinking. Target: >50% referenced for AI-core sources.

## Pitfalls

- **Don't use `grep -roh` in execute_code** — it silently returns 0 results. Use `find | xargs` with `shell=True`.
- **Trailing garbage is multi-character** — `]]`, `]]。`, `|Raw`, `|Display text`, `"` all appear. Simple `rstrip(']')` is insufficient.
- **Some references have markdown link syntax**: `[text](raw/articles/file.md` — the `(` needs stripping too.
- **index.md must be included** in the grep — it has its own raw article references.
- **22 referenced files were missing from raw/** — these are link-rot, not ingestion gaps. Flag them separately.
