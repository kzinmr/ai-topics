# Stale Factual Data in Entity Pages — Detection Pattern

## Problem

Entity pages for AI companies frequently contain specific financial/operational data (funding rounds, compute capacity, customer counts, headcounts, model pricing) that becomes stale as companies raise new rounds or announce expansions. When blog-triage evaluates a funding announcement article, the matching entity page may appear to "cover" the entity comprehensively — but the actual **numbers** are outdated.

## Example (July 2026)

| Source | Data Point |
|--------|-----------|
| `entities/together-ai.md` (existing) | "$150M+ Series B" |
| Together AI blog ($800M Series C) | "$800M Series C with 500MW compute commitment from Aramco Ventures, NVIDIA, Vista Equity" |

The entity page existed, was well-structured, and covered the company correctly — but its funding information was stale by ~$650M and missing the compute capacity data.

## Detection Checklist

When a matching entity page is found but the blog article is a funding/milestone announcement:

1. **Check `updated` date** in YAML frontmatter — older than 30 days from the article date? Likely stale.
2. **Read the financial/operational sections specifically** (not just the overview paragraph). Look for dollar amounts, round names (Series A/B/C), compute capacity figures (MW, GPU counts), customer count claims.
3. **Compare headline numbers** — the blog article's top-line claims (funding amount, round name, compute commitment) against the entity page's equivalent numbers.
4. **If numbers diverge**, the article is a **reference enrichment opportunity** — not a "skip because entity page exists."

## Action

Add a short "Funding Update" or "Milestone Update" subsection with year/date context, or update the existing financial section with an "Updated YYYY-MM: $X Series Y → supersedes prior $Z round" note. **Do NOT overwrite existing data** — add alongside with date context per the wiki's "contradictions preserved with date + source" rule.

## Related Patterns

- **"keyword present, content absent"**: Entity page exists but doesn't mention the article's topic at all → genuine gap.
- **"mentioned ≠ covered"**: Entity page lists article URL in `sources` but body lacks substantive summary → genuine gap.
- **Stale data (this pattern)**: Entity page has current factual data that has since been superseded → enrichment opportunity.
