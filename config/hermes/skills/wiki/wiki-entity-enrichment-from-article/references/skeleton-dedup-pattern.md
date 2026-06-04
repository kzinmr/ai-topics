# Skeleton Deduplication Pattern

When ingesting full content (slides, articles) that replaces an existing skeleton entity page, follow this migration checklist to avoid broken wikilinks.

## Problem

Skeleton pages (status: skeleton) are created by automated scripts (`build_x_wiki.py`, `build_blog_wiki.py`, or manual stubs). When full content is ingested later, a NEW file with a different slug is often created (e.g., `cheat-at-search-long-running-search.md` vs `long-running-search-agents.md`). The skeleton's wikilinks remain in the wiki, causing confusion and eventual broken references when the skeleton is deleted.

## Migration Checklist

### 1. Find ALL references to the skeleton

```bash
cd ~/ai-topics
grep -rn 'skeleton-slug-name' wiki/ --include='*.md'
```

Check these locations specifically:
- `wiki/concepts/*.md` — Related Raw Articles section
- `wiki/index.md` — both raw articles and raw transcripts sections
- `wiki/entities/*-projects.md` — project listing pages
- `wiki/entities/*-speaking.md` — speaking engagement pages
- `wiki/log.md` — historical entries (leave as-is, don't modify)
- Other `wiki/concepts/*.md` — cross-references in body text

### 2. Replace skeleton references with correct article

For each file found:
- Replace `[[raw/articles/OLD_SLUG]]` with `[[raw/articles/NEW_SLUG]]`
- If adding a companion transcript, add it alongside: `[[raw/transcripts/NEW_SLUG-lecture]]`
- In index.md, REMOVE the old entry (don't leave duplicates)
- In entity pages, consolidate duplicate Part entries into one line

### 3. Delete the skeleton

```bash
cd ~/ai-topics
git rm wiki/raw/articles/OLD_SLUG.md
```

### 4. Commit and push

```bash
cd ~/ai-topics
git add -A wiki/
git commit -m "wiki: deduplicate skeleton, fix refs to correct article"
git push
```

## Pitfalls

- **Don't modify log.md historical entries** — they record what happened at the time
- **Part numbering conflicts** — if the new content claims a different Part number than what's already assigned, trust the existing chronological order (the projects file is the source of truth)
- **Duplicate entries in index.md** — check both `## Raw Articles` and `## Raw Transcripts` sections
- **concepts/*.md Sources field** — uses external URLs, not wikilinks; don't change these to point to the new article slug
