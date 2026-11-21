# Pattern E: Stub raw files & HN comment-tree fallback (validated 2026-11-09)

## The stub-file trap

A large `wiki/raw/articles/*.md` file scraped by sitemap-monitor / blog-ingest is NOT
automatically a substantive article. The 2026-11-09 dreaming cycle hit a ~105KB file
(`2026-11-08_8rank_apple-intelligence-knowledge-graph.md`) that was actually a scraped
section-index / aggregator page: chess-problem metadata chrome, navigation fragments,
repeated table shells, and a verbatim HN comment tree — the real article body absent.

**Failure mode**: Pattern E's default "read the first 30-50 lines" accepted a fabricated
`body_excerpt` — specific technical claims (CoreML+SQLite store, Neo4j Cypher compat,
LoRA fine-tuned Qwen-1.7B F1 0.9063) that appeared nowhere in the file and were
plausible-sounding inventions from the filename/title.

**Detection rule** — before building any triage decision or enrichment:

```bash
# grep the file for its headline's key nouns (pick 3-5 distinctive terms)
grep -ci "triple store\|predicate\|kinship\|knowledgeconstructiond" <file>
```

Near-zero hits means the body was NOT captured. Aggregator tells to scan for: repeated
`## N. Link` structures, "Do not edit" generator comments, chess FEN strings,
"Skip to content" chrome, table shells with no rows.

## Recovery: mine the Algolia HN comment tree

When the wiki gap is genuine (coverage verified absent) but the raw body is a stub,
the HN comment tree is often sufficient for reference-grade enrichment — especially
when the article is a high-point HN story and the author replies in-thread
(the 8rank authors' replies carried the core fact chain and answered top objections).

```python
import json, urllib.request, re
oid = "50403097"  # from the raw frontmatter hn: line, NEVER guessed
r = urllib.request.urlopen(
    f"https://hn.algolia.com/api/v1/items/{oid}", timeout=30)
data = json.loads(r.read(3_000_000))  # read cap >=3M — big items exceed 200KB
def walk(node, depth=0, out=None, cap=40):
    out = out if out is not None else []
    if depth > 2 or len(out) >= cap: return out
    t = re.sub(r"<[^>]+>", " ", node.get("text") or "")
    if len(t.strip()) > 90:
        out.append("[" + str(node.get("author")) + "] " + t.strip()[:500])
    for c in node.get("children", []):
        walk(c, depth+1, out, cap)
    return out
print("\n".join(walk(data)))
```

Rules:
- Cite the HN `item?id=` as the source and label the page content HN-thread-derived
  in the section (same class as the paywalled-source recipe; trigger = stub body).
- Prefer author replies verbatim — they restate the findings and answer objections.
- Record the stub status honestly in the log entry ("raw body was stub; enriched from
  HN thread") so future cycles don't re-triage expecting more from the raw file.
- NEVER ship a `body_excerpt` or enrichment claim you could not actually read in some
  retrieved text. Fabricated excerpts are the worst dreaming failure mode — they
  propagate into archive records and wiki pages as if sourced.

## Companion: verify claimed specifics exist before citing

When a triage decision (or a recovered upstream analysis) quotes specific
numbers/claims, grep the raw file for each distinctive token
(`grep -n "0.9063" <file>`). Zero hits across all quoted specifics means the decision
was hallucinated upstream or merged from a sibling article — re-derive from a readable
source or downgrade to skip.
