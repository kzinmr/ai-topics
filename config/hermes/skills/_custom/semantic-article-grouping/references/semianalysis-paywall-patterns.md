# SemiAnalysis Paywall Patterns

## Post URL Construction

SemiAnalysis uses standard Substack URLs:
- Full post: `https://newsletter.semianalysis.com/p/<slug>`
- Open (public preview): `https://open.substack.com/pub/semianalysis/p/<slug>`

## Paywall Detection

SemiAnalysis articles are often **paid-only** for the full content, but **not always**. Two patterns have been observed:

### Paywalled (common)
- Content truncated at preview (~5,000 chars)
- HTML contains `subscribe?simple=true` and `paywall` in URL params
- Article body begins with "Paid" label
- Only the first section (~thesis statement) is visible in web_extract

### Fully Accessible (less common — observed May 2026)
Some SemiAnalysis articles are **fully accessible** without authentication:
- **"Anthropic Growth and Bedrock Mix Drive AWS Margins Higher While Peers Lag"** (May 27, 2026) — full text returned
- **"Finding Miscompiles for Fun, Not Profit"** by Justin Lebar (May 28, 2026) — guest-authored, full text returned

**Pattern**: Guest-authored posts (non-core analysts) and short news-flash posts tend to be free. Always try web_extract first — do NOT assume paywalled.

## Section Anchor Pattern (from HTML)

Inside a paywalled article, the HTML contains anchor links to specific sections even though the sections themselves are hidden. Pattern:

```
https://newsletter.semianalysis.com/i/<post_id>/<section-slug>
```

Example from "Cerebras — Faster Tokens Please" (post_id=197494856):
- `../i/197494856/the-need-for-speed`
- `../i/197494856/the-cerebras-openai-deal`
- `../i/197494856/running-the-numbers`
- `../i/197494856/the-cs-3-architecture-and-bom`
- `../i/197494856/thermal-design-and-cooling`
- `../i/197494856/sram-scaling-is-dead`
- `../i/197494856/sram-machines`
- `../i/197494856/where-the-wafer-wins`
- `../i/197494856/the-island-problem-bandwidth-is-geometry`
- `../i/197494856/pipeline-parellelism-is-forced`
- `../i/197494856/the-wafer-scale-engine`
- `../i/197494856/the-wafer-taketh-and-the-wafer-giveth`
- `../i/197494856/the-throughput-interactivity-frontier`
- `../i/197494856/cerebrass-technology`

These section titles can be extracted from the HTML even when the content is paywalled. They reveal the article's structure and coverage areas.

## Strategy for Paywalled SemiAnalysis Articles

1. Extract the public preview via web_extract (captures thesis, intro, and first ~5K chars)
2. Use the HTML curl fallback to extract section anchor links
3. Cross-reference section titles against existing wiki pages
4. Use the free preview claims (which are typically concrete: model names, chip specs, deal values) as wiki source
5. For deeper claims, cross-reference against non-paywalled sources (e.g. Simon Willison blog posts, X posts by the same authors)
6. Mark raw article frontmatter with `paywalled: true` and note which claims come from preview vs cross-reference

## SemiAnalysis RSS Feed

The blog-ingest pipeline can capture SemiAnalysis RSS items (headlines + preview text) via the RSS feed at `newsletter.semianalysis.com/feed`. These arrive in the blog-ingest pipeline the morning of publication, potentially before the newsletter-triage pipeline runs.
