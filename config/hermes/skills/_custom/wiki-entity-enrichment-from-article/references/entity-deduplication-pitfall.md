# Entity Deduplication Pitfall

## Problem
When creating entity pages from YouTube talks or articles, agents often create duplicate pages because they search for an exact name match. Example: searching for `cursor` returns no results, so the agent creates `entities/cursor.md` — but `entities/cursor-ai.md` already exists with 200+ lines of rich content.

## Solution
Before creating ANY new entity page:

1. **Search `wiki/entities/`** with multiple search terms:
   - Company/product name (e.g., `cursor`)
   - Common suffixes (e.g., `cursor-ai`, `cursor-labs`)
   - Founder/CEO names (e.g., `aman-sanger`)
2. **Search `wiki/index.md`** for the entity name in existing entries
3. **If a match exists**: Enrich the existing page with a `patch` — add the new talk/article as a section or source reference
4. **If no match exists**: Create the new entity page

## Recovery
If a duplicate was created by mistake:
1. `rm` the duplicate file
2. Patch the existing page with the new content
3. Update `index.md` if it was modified
4. Do NOT commit the duplicate

## Example (2026-06-09 session)
- Searched for `cursor` → 0 results in entities/
- Created `entities/cursor.md` 
- Then found `entities/cursor-ai.md` (217 lines, extensive content)
- Had to `rm cursor.md` and patch `cursor-ai.md` instead
