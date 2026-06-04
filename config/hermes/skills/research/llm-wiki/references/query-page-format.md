# Query Page Format

Template and conventions for wiki query pages (`type: query` in `wiki/queries/`).

## Philosophy

> *"Good answers can be filed back into the wiki as new pages. A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history."* — Andrej Karpathy

Query pages capture answered questions as durable wiki assets. They should be substantial enough that re-deriving the answer from scratch would be painful.

## Frontmatter

```yaml
---
title: "Question as a descriptive title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: query
tags:
  - query
  - <domain tags from SCHEMA taxonomy>
sources:
  - <wiki pages that informed the answer>
  - <external URLs if used>
related:
  - <closest wiki pages for cross-reference>
---
```

## Body Structure

### 1. Question Metadata Block

At the top of the page, before the main content:

```markdown
> **質問**: <the original question>
> **質問者**: <name>（<channel>, <date>）
> **回答要旨**: <one-sentence answer summary>
```

### 2. Structured Answer

The answer body should include:
- **Context/definitions** — clarify terms if needed (e.g., "What 'Open Harness' means in this wiki")
- **Decision matrix** — a comparison table when comparing options
- **Cross-references** — link to relevant wiki pages with `[[wikilinks]]`
- **Conclusion** — concrete, actionable recommendations

### 3. Unresolved Questions

List open questions, gaps, or limitations discovered during the analysis. This makes the query page a research artifact that future sessions can build on.

### 4. Karpathy Insight Tie-in (when applicable)

If the query itself demonstrates the wiki's compounding value, add a brief note like:

```markdown
### Karpathyの洞察との整合
本query自体がその実践例：このQ&Aは、[[comparisons/X]] と [[concepts/Y]] を横断し、**Z**という未カバーの交差点を可視化した。
```

### 5. Related Pages

Standard `## 関連ページ` / `## Related Wiki Pages` section with wikilinks.

## Index Entry Format

```markdown
- [[queries/slug]] — one-line summary with date (YYYY-MM-DD)
```

## Example

See [[queries/data-analysis-open-harness]] for the canonical first query page in this wiki.
