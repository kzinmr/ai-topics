# Pure Link Digest Newsletter Pattern

A third newsletter type beyond pure-podcast and editorial-roundup. The post body is a shallow bullet list of article titles with 1-line descriptions and no paragraph-level analysis.

## Detection

| Signal | How to detect |
|--------|---------------|
| Post body structure | `<p>` extraction yields only link titles and 1-line descriptions, not paragraphs of analysis |
| Paragraph count | <30 paragraphs of significant length (>80 chars) — most lines are short `<a>` links |
| No section headings | No emoji-prefixed section headings, no "In Today's Issue" TOC |
| Article descriptions | 5-15 words per article, never 50+ words |
| No editorial voice | No author commentary, analysis, or opinion between links |
| Source | Weekly digests like "True Positive Weekly" / AI Weekly |

## Examples

### AI Weekly (aiweekly.substack.com, pub_id=61455) — "True Positive Weekly #165"
Post body content (21 paragraphs, most <50 chars):
```
What data science is actually about in the age of AI
World modeling for physical AI
Forecasting with foundation models
Research-driven agents: What happens when your agent reads before it codes
CUDA made simple: A short, practical GPU programming guide
[ChapterPal] A bitter lesson for data filtering
[Model] DiffusionGemma: 4x faster text generation
[Model] Command A+: an open-weight model for complex reasoning...
```

No paragraph went beyond ~150 chars and most were just link titles with a 1-line description tacked on. No editorial analysis, no context setting.

## Triage Strategy

1. **Skip immediately** — the post body contains no substantive content for wiki ingestion
2. **Do not attempt deeper URL resolution** — even if the URLs resolve, the newsletter curator's value-add is zero (they're just listing links, not analyzing them)
3. **No `take` or `reference` decisions** — unless a linked article is uniquely important and NOT covered by other pipelines (extremely rare)
4. **Scan for AI-relevant topic titles only** as a sanity check — if DiffusionGemma or Command A+ appear, they're already handled by sitemap-monitor or blog-ingest

## Relationship to Other Patterns

| Pattern | Post Body Depth | Example | Action |
|---------|----------------|---------|--------|
| **Pure podcast** | No body text (audio only) | Lenny's Podcast | Skip immediately |
| **Pure link digest** | 1-line descriptions only | AI Weekly / True Positive Weekly | Skip immediately |
| **Editorial essay** | Standalone thesis-driven argument with citations | The Signal (essay weeks), Latent Space (analysis posts) | Evaluate essay itself; 1 decision for the post, not N for citations |
| **Editorial roundup** | Section summaries + context | The Signal (roundup weeks) | Check ~10-15% for unique content |
| **Full analysis** | Multi-paragraph per topic | Superintel, SemiAnalysis | Full triage evaluation |

## Note on Overlap

Some newsletters may be hybrids — a digest format that sometimes includes original analysis (e.g., AINews daily bulletins with emoji section headings + paragraph-level summaries). These are NOT pure link digests. The key tell: if any article in the post has 50+ words of editorial analysis, treat it as an editorial roundup, not a pure link digest. The pure link digest has ZERO editorial depth — every link gets the same 1-line treatment.
