# Transcript Ingestion — Pitfalls from Standalone Conference Talk Sessions

Cases where the standard course-series workflow doesn't apply (no portal page, no companion summary article, presenter outside the tracked course community).

## 1. Source-slug fallback when no X handle

Some presenters (e.g., JJ Allaire) are primarily known by their GitHub handle, not an X handle. Priority order:
- X handle (primary) → GitHub handle (fallback) → abbreviated real name (last resort)

Example: JJ Allaire → `jjallaire` (GitHub), not `jallaire` or `jj-allaire`.

## 2. Entity page name collision

When the transcript discusses a tool/project whose name collides with an existing entity page:
- `search_files` for the entity name BEFORE creating a new page
- If collision found, use a disambiguated slug (e.g., `inspect-ai.md` when `inspect.md` exists for a different project)
- Add "Not to be confused with [[entities/other-entity]]" in both pages

## 3. User provides only transcript (no companion summary)

When the user asks to ingest a transcript but doesn't provide or request a companion summary article:
- Create only the transcript + entity pages
- Do NOT auto-generate a summary article unless asked
- The user may plan to write it themselves or add it in a follow-up session
