# Triage-Time Enrichment (Blog-Ingest / Newsletter-Ingest)

When processing blog-ingest or newsletter-ingest checkpoints, don't just save raw articles — check if existing wiki pages need updating with new information. This is a lightweight enrichment pass that happens during triage, not a full page rewrite.

## Model Release Follow-Up Pattern

When a major model was announced days/weeks ago and the triage finds new articles about it (open-weight release, serving provider announcements, benchmark results), update the existing concept page:

### Steps

1. **Read the existing concept page** in sections (offset/limit for long pages)
2. **Identify stale sections** — e.g., "Open Weight Status" saying "promised by DATE" → update to "released on DATE"
3. **Patch specific sections** rather than rewriting:
   - Overview paragraph: release date, weight availability, provider support
   - Open Weight Status: from "promised" to "released" with specifics (file size, HuggingFace link)
   - Licensing evolution: document changes between model versions (e.g., Modified MIT → MaaS-restricted)
   - Day-0 Inference Providers: Modal, Fireworks, OpenRouter with performance metrics
4. **Update entity page model table** if the entity has a model family table
5. **Update sources and `updated` date** in frontmatter

### Example: Kimi K3 (2026-07-28)

Blog-ingest found 3 new articles about Kimi K3 (Simon Willison, Modal Blog, Fireworks AI). The concept page already existed but had "open weight release promised by July 27." Triage updated:

- **Overview**: "promised by July 27" → "released on July 27 (1.56TB on HF)"
- **Open Weight Status**: added licensing evolution (K2 Modified MIT → K3 MaaS clause requiring separate agreement for >$20M MaaS revenue)
- **New "Day-0 Inference Providers" section**: Modal (460 tok/s via DFlash speculator, 360% faster interactivity), Fireworks AI (US-hosted, zero data retention), OpenRouter (7 providers)
- **Entity page model table**: added "open weights released Jul 27 (1.56TB on HF); new MaaS license"

## Pitfalls

- **Partial reads**: When reading long files with offset/limit, verify patch context uniqueness. The system warns about partial reads but patches work if context is unique.
- **Don't create duplicates**: Check `wiki/index.md` and search for existing concept pages before creating new ones.
- **Source dedup**: If a newsletter-ingest already saved the same article (e.g., `2026-07-28_fireworks-ai_kimik3-on-fireworks.md`), reference it in sources rather than creating a duplicate.

## log.md Prepend Technique

Blog-ingest triage entries go at the TOP of log.md (most recent first). Use:

```bash
cat /tmp/new_entry.md - /opt/data/ai-topics/wiki/log.md > /tmp/merged.md && mv /tmp/merged.md /opt/data/ai-topics/wiki/log.md
```

This prepends the new entry while preserving all existing content. Works because `-` tells cat to read from stdin (which gets the existing file content after the new entry).
