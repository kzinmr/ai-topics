# Blog-ingest stage — 2026-11-13 session notes (run 20261113T100036Z)

## Log-prepend assert pitfall: leading blank line before first entry

The validated prepend script from `blog-ingest-session-notes-2026-10-28.md` writes the entry then asserts `c.split("\n")[0].startswith("## [")`. This **false-fires** when the insertion point sits at a position where the file begins with a blank line — `"\n".join(lines[:insert_at])` re-emits that leading empty string as line 0, and the entry lands on line 1. The WRITE SUCCEEDED; only the assertion aborted, and the (correct) file was left on disk. Do NOT `git checkout` and redo in that state.

Robust assertion set (use instead):

```python
c = open(log_path).read()
assert UNIQUE_SUBSTRING in c                 # entry present
lines = c.split("\n")
first = next(l for l in lines if l.strip())  # first NON-BLANK line
assert first.startswith("## [") or first == "# Wiki Log"
# and after commit: git diff --stat must show N insertions, 0 deletions
```

The `git diff --stat ... 15 insertions(+), 0 deletions` check is the real safety gate — the line-0 assert is belt-and-braces at best, false-positive-prone at worst.

## Sweep of sitemap-monitor backlog in blog-ingest runs

On 2026-11-13 the working tree carried 12 uncommitted `wiki/raw/articles/2026-11-13_<vendor>_*.md` files (Cohere, Decagon, ElevenLabs, Factory, Harvey, Hex, Pinecone) from the 06:00 UTC sitemap pipeline that had not been committed by its own run. Blog-ingest's `git add wiki/raw/articles/` swept them into its commit — correct behavior, but the commit message should disclose the sweep ("+ 12 sitemap articles") so the log matches, and `git status --short wiki/` before staging tells you whether a sweep is happening. These sitemap files use `type: "sitemap"` frontmatter with `scraped`/`lastmod` fields (vs the `--hash` suffixed blog-ingest filenames) — a quick `head -8` on one confirms provenance.

## Checkpoint quirks re-confirmed (4th time)

`scan.total_new=33` (DB-wide) vs `articles.total=20` (fetch cap) vs 14 saved; `blogs_scanned=0` + empty `new_articles_per_blog` with nonzero total_new remains cosmetic. `saved_articles` paths verified with one stat loop before commit. No re-scan needed.

## Unsaved-article triage judgment (accepted skips)

Skipped without re-fetch attempts: paywalled Reuters/WSJ pieces (Huang affair saga), a Truth Social post, a YC library video page, a non-AI construction-physics essay. These are legitimate skips for the blog-ingest stage — downstream blog-triage can revisit. No fetch failure to report when the skip is by editorial judgment.
