# Chain-Citation Ingestion Pattern

When ingesting source A, you discover it cites source B. The user says "ingest B too."
This creates a **chain ingestion** where the citation relationship becomes wiki navigation.

## Pattern

```
User: "wikiに取り込んで" → Source A
Agent: ingests A (raw + concept + entity)
Agent discovers: A cites B (e.g., "Replit's founding engineer wrote...")
User: "その引用元の記事Bも取り込んで"
Agent: ingests B (raw + concept + entity) AND backward cross-links A to B
```

## Key Steps

1. **Ingest A** as normal — raw article, concept page, entity page
2. **Notice the citation** — A references B by name/URL. Flag it.
3. **User confirms** — ingest B too
4. **Ingest B** — raw article, concept page, entity page (B's pages naturally link to A since B is the cited source)
5. **Backward cross-link A → B** (critical, easy to miss):
   - Update A's concept page to wikilink B's concept/entity
   - Update A's entity page frontmatter `related:` to include B's pages
   - Update A's "Further Reading" or relevant section to point to B's new wiki page
   - If A quoted B anonymously ("Replit's founding engineer"), **name the person** now that the wiki knows who it is

## Canonical Example (2026-05-28 session)

```
Source A: howtoeval.com (Ben Hylak, "How to Evaluate AI Agents")
  → Created: concepts/agent-evaluation-methodology.md + entities/ben-hylak.md

A cites: "Thoughts on Evals" (Ben Hylak vs Ankur Goyal debate)
  → Created: concepts/evals-vs-monitoring-debate.md
  → Backward: enriched entities/ben-hylak.md + entities/ankur-goyal.md

A also cites: "Replit's founding engineer" (Gian Segato, "Probabilistic Era")
  → Created: concepts/probabilistic-era-software.md + entities/gian-segato.md
  → Backward: updated concepts/evals-vs-monitoring-debate.md to name Segato + link new pages
```

## Pitfalls

- **Don't skip the backward cross-link.** The new pages for B enrich the wiki, but A's pages referencing B anonymously or by URL become stale immediately. Update A before committing.
- **Name anonymous citations.** If A said "Replit's founding engineer wrote..." and you now know it's Gian Segato, update A to use the wikilink `[[entities/gian-segato|Gian Segato]]`.
- **Commit together.** If A and B are ingested in the same session, commit A's backward updates alongside B's new pages so navigation is consistent from the start.
