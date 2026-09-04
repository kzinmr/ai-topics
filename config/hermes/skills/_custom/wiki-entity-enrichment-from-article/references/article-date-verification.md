# Article Date Verification Pitfall

## Problem

Blog article dates can be mis-attributed when the agent assumes the date from context (URL ordering, session date, recency bias) rather than extracting it from the source. A 6-month misdating was caught by the user only after commit.

**Real example (2026-06-05)**:
- URL `https://huggingface.co/blog/hf-skills-training` was ingested alongside `hf-cli-for-agents` (dated 2026-06-04)
- Agent assumed the skills-training blog was also from June 2026 → saved as `2026-06-04_hf-skills-training.md`
- Actual date: **2025-12-04** — the article was 6 months old
- Required: file rename, frontmatter fix, concept page sources path fix, log.md correction
- Root cause: HF blog frontmatter has no `date:` field (only `title:`, `authors:`, `thumbnail:`); the date must be extracted from the rendered HTML or verified by the user

## Prevention

**Rule: Always extract or verify the publication date BEFORE saving the raw article.**

### Extraction methods (priority order)

1. **Raw markdown frontmatter** — Some blogs include `date:` in YAML frontmatter (Substack, many personal blogs). Check first.
2. **Rendered HTML** — Look for a `<time>` element, "Published on" text, or date near the byline. HF blogs show it after the author names.
3. **Git history** — For GitHub-hosted blogs (HF, many OSS projects): `git log --format="%ai" --diff-filter=A -- <file>.md` on the blog repo.
4. **RSS feed** — Some sites expose `<pubDate>` in their RSS even when the HTML is behind Cloudflare. OpenAI's blog RSS (`https://openai.com/blog/rss.xml`) is a reliable date source. See `references/openai-rss-date-discovery.md`.
5. **User confirmation** — If date is ambiguous (no date in source, multiple candidates), ask the user before committing.

### HF-specific note

HuggingFace blog raw markdown (fetched from `github.com/huggingface/blog/main/{slug}.md`) does NOT include a `date:` field in frontmatter. The publication date is only visible in the rendered HTML page. Always check the HTML or ask the user when the date is critical.

### Filename convention

Raw article filenames use the pattern `{YYYY-MM-DD}_{source}_{slug}.md`. A wrong date in the filename cascades to:
- `sources:` paths in concept/entity pages
- `log.md` entries
- Index references
- Dedup lookups (if date-prefixed)

## Fix sequence (if misdated)

1. `mv wiki/raw/articles/{old-date}_{slug}.md wiki/raw/articles/{correct-date}_{slug}.md`
2. Patch frontmatter `date:` field in the renamed file
3. Patch all `sources:` references in concept/entity pages that point to the old filename
4. Patch `log.md` if the entry references the date
5. `git add` both the old (deleted) and new (renamed) files
6. Commit with a fix message
