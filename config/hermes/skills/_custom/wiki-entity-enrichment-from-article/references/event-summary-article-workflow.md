# Event/Conference Summary Article Workflow

When ingesting a blog post that summarizes a multi-theme conference or event (e.g., Lance Martin's "The state of AI agents" covering AIE World's Fair 2025), follow this multi-target pattern.

## Pattern

The article describes an event that has its own entity page — it is NOT a standalone concept introduction. The correct action is a **three-part enrichment**:

1. **Enrich the event's entity page** — Add a dedicated "Flagship Events" section with:
   - Theme summary table (Theme | Key Talks | Significance)
   - Speaker credits
   - Link to the raw article for full details
   - Future event placeholder (e.g., "2026: Coverage to be added post-event")

2. **Create concept pages for new clearly-defined concepts** — If the article crystallizes a concept that doesn't yet have a wiki page (e.g., "ambient agents" from AIE 2025), create it. The concept should be independently understandable and cross-referenced.

3. **Update speaker/author entities** — Add the article to the author's Blog/Recent Posts table and update their sources/tags.

## Example: AIE 2025 → Wiki

```
Lance Martin's AIE 2025 takeaways
  → entities/ai-engineer-youtube.md: + "Flagship Events" section (5-theme table + 2026 placeholder)
  → concepts/ambient-agents.md: NEW concept page
  → entities/lance-martin.md: + Blog entry, sources, tags
```

## Red Flag: Creating a "new concept" page from event coverage

If the article is fundamentally *about* the event (not a new concept), don't create a concept page like "aie-2025-takeaways". Instead, the event entity page is the canonical home. Only create concept pages for genuinely new, independently-valuable ideas that emerged from the event.

## When the article IS a standalone concept

If the article describes a new idea that happens to have been presented at an event but stands on its own (e.g., "RLVR" as a training paradigm), create the concept page and cross-reference the event entity. The event entity gets a mention in the concept's sources, not vice versa.
