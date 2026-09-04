# LinkedIn Article Extraction Patterns

## Problem
LinkedIn Pulse articles return JS-rendered shells via `curl`. The HTML contains ~200KB of scripts/chrome but no article body text. The `<p>` tags in the response only contain "Others also viewed" sidebar content.

## Fallback Strategy (proven 2026-06-08)
1. **Try curl first** — check if response contains `<article>` or `reader-content` class with substantial text (>500 chars after tag stripping)
2. **If JS-rendered (common)**: Use `delegate_task` with `browser` toolset to navigate and extract
3. **Blog mirror trick**: Many LinkedIn Pulse articles are cross-posted to the author's company blog. Search `"article title" site:company.com` — the blog version is often SSR and extractable via curl
   - Example: LinkedIn article by Ido Pesok was also at `spice.ai/blog/verifying-agentic-development-at-scale`

## Same Author, Different Platforms
LinkedIn articles and X articles by the same author may cover the same topic from different angles (e.g., different employer at different time). Save as **separate raw articles** with distinct filenames:
- `2026-05-29_ido-cognition_verifying-agentic-development-at-scale.md` (X article, Cognition era)
- `2026-06-08_linkedin-ido-pesok_verifying-agentic-development-at-scale.md` (LinkedIn, Spice AI era)

Cross-reference in entity pages with a note explaining the relationship.
