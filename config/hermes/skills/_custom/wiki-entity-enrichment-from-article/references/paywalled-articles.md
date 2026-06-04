# Paywalled Article Handling

When ingesting an article that is behind a paywall, follow this workflow.

## Detection

You've hit a paywall when:
- `web_extract` returns content clearly marked as a summary/preview (look for "Summary", "Upgrade to unlock", "Start your free trial", "Subscribe to read more")
- Content is truncated with "Parts 2-N" listed but not included
- `browser_navigate` shows the same truncated content in the snapshot

Common paywalled sources: Every, The Information, WSJ, Bloomberg, Financial Times, MIT Tech Review, New York Times, Wired.

## Workflow

### 1. Save What You Have

Always save the available content as a raw article — even a preview/summary has value:

```yaml
---
title: "Article Title"
source: "https://original-url"
author: "Author Name"
date_published: "YYYY-MM-DD"
date_ingested: "YYYY-MM-DD"
type: article
publication: "Publication Name"
note: "Paywalled — [describe what's missing, e.g., Parts 2-6 not accessible]"
---
```

Filename follows the standard `raw-article-filename-policy`: `{YYYY-MM-DD}_{source-slug}_{content-slug}.md`.

### 2. Extract What You Can

Paywalled content typically still provides:
- **The core thesis** — Usually stated upfront before the paywall
- **Structural outline** — Sections/parts listed even if content is locked
- **Key quotes and frameworks** — Often in the preview section
- **Author and metadata** — Always available

### 3. Enrich Wiki Pages

Still enrich existing wiki pages with whatever was extractable:
- The thesis, frameworks, and key quotes from the preview go into relevant entity/concept pages
- Note the paywall limitation in those pages too (e.g., "The full guide (behind Every paywall) outlines...")
- Cross-reference the raw article in frontmatter `sources`

### 4. Document the Gaps

In the enriched wiki pages, note what's behind the paywall:
- "Parts 2-6 behind paywall, covering: Setup, Five Levels, Workflow Library, Operating Codex, Getting Started"
- This helps future sessions know what to extract if access becomes available

### 5. Revisit When Possible

If the user later gains access (subscription, free trial, paywall removal):
- Re-fetch the article with `web_extract` or `browser_navigate` (authenticated)
- Update the raw article file with full content
- Remove the `note:` from frontmatter
- Enrich wiki pages with the newly available content

## Example: Every.to Guide

```
web_extract → "Codex for Knowledge Work — Summary" (preview only)
browser_navigate → "Upgrade to unlock" wall after Part 1

Action:
✓ Save preview as raw/articles/2026-05-26_every_codex-knowledge-work.md
  with note: "Paywalled — Parts 2-6 (Setup, Five Levels, Workflow
  Library, Operating Codex, Getting Started) not accessible"
✓ Extract: Delegate vs Collaborate modes, Goals vs Skills distinction,
  "three prompts" heuristic, 5-level structure outline
✓ Enrich entities/openai-codex.md with knowledge work framing
✓ Enrich concepts/codex-goal.md with Goals vs Skills distinction
✓ Note in wiki pages: "The full guide (behind Every paywall) outlines..."
```
