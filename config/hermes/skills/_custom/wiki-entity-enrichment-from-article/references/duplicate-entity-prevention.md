# Duplicate Entity Page Prevention

## The Problem: Aliases Hide Existing Pages

A naive `search_files` for a slug won't find a page if the canonical filename differs. The `index.md` and frontmatter `aliases:` field are the authoritative sources for page existence.

### Real Failure: `pi-coding-agent` (2026-05-25)

1. `search_files(path="entities", pattern="pi-coding-agent")` returned 0 results
2. Created `entities/pi-coding-agent.md` — a full new page
3. **But** `index.md` already had: `entities/pi-coding-agent → entities/pi`
4. **And** `entities/pi.md` already had: `aliases: [pi-coding-agent, pi-dev, pi-mono, ...]`
5. Had to delete the duplicate, enrich `entities/pi.md` instead

### Required Pre-Creation Checklist

Before ANY `write_file` for a new entity page:

```bash
# Step 1: Search for the slug in entity filenames
search_files(path="/opt/data/wiki/entities", pattern="<slug>", target="files")

# Step 2: Search for the slug in index.md (catches redirects)
grep "<slug>" /opt/data/wiki/index.md

# Step 3: If index.md shows a redirect (e.g., "→ entities/pi"):
#   - The canonical page already exists
#   - Open it and check aliases: frontmatter
#   - ENRICH the existing page via patch, don't create a new one
```

### Tag Taxonomy: Pre-Check Before Commit

The pre-commit hook validates ALL tags against `wiki/SCHEMA.md`. If a new page uses an unregistered tag:

1. The commit is BLOCKED
2. You must add the tag to the correct category line in SCHEMA.md
3. Then re-attempt the commit

Example: `earendil` was used as a tag but wasn't in SCHEMA.md's People/Orgs line. Added as `earendil` between `databricks` and `ibm`.

**Proactive step**: Before committing, scan new pages' frontmatter `tags:` against SCHEMA.md categories. Add any missing tags first, then `git add wiki/SCHEMA.md` before `git commit`.
