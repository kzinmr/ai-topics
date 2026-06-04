# Scan Raw Article Naming — Quick Reference

## X Article / X Note Tweet (tweet IS content)
- Pattern: `YYYY-MM-DD_{handle}_slug.md`
- Handle: strip `@` and underscores (e.g., `engkhairallah1`)
- Frontmatter: include `type: x_article` or `type: x_note_tweet`
- Date: from `created_at` in tweet API response

## External Blog/Docs URL (tweet LINKS to content)
- Pattern: `YYYY-MM-DD_{source-slug}_{content-slug}.md`
- Source-slug: abbreviated domain or org name, NOT the tweeter's handle
  - `anthropic` (from claude.com, anthropic.com)
  - `cloudflare` (from blog.cloudflare.com)
  - `modal` (from modal.com)
  - `vercel` (from vercel.com)
  - `daytona` (from daytona.io)
  - `leehanchung` (from leehanchung.github.io)
- Date: publication date from the external article, NOT the tweet date
- Content-slug: 2-5 hyphenated keywords, lowercase, max 30 chars

## YouTube Links
- Do NOT save as raw articles unless video transcript is scraped
- Link directly in entity page's "Key Links" or "Recent Activity" section

## Verification
Always check `raw-article-filename-policy` skill for full details and edge cases.
