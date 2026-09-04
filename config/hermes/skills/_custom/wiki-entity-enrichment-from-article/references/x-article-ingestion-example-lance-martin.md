# X Article Ingestion — Lance Martin "Designing loops with Fable 5" (2026-06-09)

## Session Summary

Ingested X Article from @rlancemartin about Claude Fable 5 loop design patterns. Article retrieved via `xurl --auth oauth2 "/2/tweets/ID?tweet.fields=article"` which returned full `plain_text` (5000+ words).

## Workflow Executed

1. **Fetch tweet metadata**: `xurl "/2/tweets/2064397389189071163?tweet.fields=note_tweet"` → detected `article.title`, no `note_tweet.text`
2. **Fetch article body**: `xurl --auth oauth2 "/2/tweets/2064397389189071163?tweet.fields=article"` → `article.plain_text` with full content
3. **Fetch created_at**: `xurl --auth oauth2 "/2/tweets/2064397389189071163?tweet.fields=created_at,author_id"` → separate call (field incompatibility). **NOTE:** `xurl read <ID>` often returns `created_at` and `author_id` inline — check the initial response first to avoid an unnecessary extra call (confirmed with Addy Osmani tweet 2087427868343373919, Aug 2026).
4. **Fetch author info**: `xurl user @rlancemartin` → bio, follower count
5. **Save raw article**: `raw/articles/2026-06-09_rlancemartin_designing-loops-with-fable-5.md`
6. **Update entity page**: `patch` on `entities/rlancemartin.md` (added section + sources + bumped updated)
7. **Create concept page**: `concepts/designing-loops-with-fable-5.md` with comparison tables
8. **Update index.md**: alphabetically inserted under Concepts
9. **Update log.md**: prepended entry

## Tag Taxonomy Violation Handling

Pre-commit hook blocked commit with 4 invalid tags: `claude-fable-5`, `loops`, `self-correction`, `memory`.

**Fix applied:**
- `claude-fable-5` → added to SCHEMA.md Models category
- `loops`, `self-correction`, `memory` → added to SCHEMA.md AI Agents category

**Pattern:** When pre-commit blocks on tag violations:
1. Read the error output to identify which tags are invalid
2. Determine which SCHEMA.md category each tag belongs to
3. `patch` SCHEMA.md to add missing tags to the appropriate category
4. `git add` the updated SCHEMA.md and re-commit

## Key Pitfalls Confirmed

- **X Article requires `--auth oauth2`** — app-only bearer tokens return HTTP 453
- **Separate calls for article + metadata** — do NOT mix `article` with `created_at` in same `tweet.fields`
- **Frontmatter type = `x_article`** (not `x_note_tweet`)
- **Pre-commit hook blocks ALL staged files** — if unrelated files with bad tags are staged, `git reset HEAD <file>` to unstage before committing

## Files Created/Modified

| File | Action |
|------|--------|
| `raw/articles/2026-06-09_rlancemartin_designing-loops-with-fable-5.md` | NEW |
| `concepts/designing-loops-with-fable-5.md` | NEW |
| `entities/rlancemartin.md` | UPDATED (section + sources) |
| `SCHEMA.md` | UPDATED (4 new tags) |
| `index.md` | UPDATED (1 new entry) |
| `log.md` | UPDATED (prepended entry) |
