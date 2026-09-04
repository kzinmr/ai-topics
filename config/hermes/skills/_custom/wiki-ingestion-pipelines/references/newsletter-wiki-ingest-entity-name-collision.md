# Newsletter Wiki Ingest — Entity Name Collision

When the newsletter-wiki-ingest pipeline creates a new entity page, the name may collide with an existing concept or entity. This reference documents the Fable/Fable 5 collision (July 2026) as a reusable pattern.

## The Pattern

The newsletter triage recommended creating `entities/fable.md` (Anthropic's Fable coding harness). However, `concepts/claude/fable-5.md` already existed — the Fable 5/Mythos 5 US export control directive, a completely separate entity sharing the "Fable" name.

## Detection

Before creating any new page in `entities/` or `concepts/`, search for name collisions:

```bash
# Check index.md for matching keywords
grep -i "fable" ~/ai-topics/wiki/index.md
# Check concepts/ for matching names
find ~/ai-topics/wiki/concepts -name "*fable*" -type f
find ~/ai-topics/wiki/entities -name "*fable*" -type f
```

In the Fable case, the grep returned entries for `concepts/claude/fable-5` and `concepts/claude/designing-loops-with-fable-5`, confirming a collision.

## Resolution

Add a `> Not to be confused with` admonition at the top of the new entity page body:

```markdown
> **Not to be confused with**: [[concepts/claude/fable-5]] — the US export control framework for AI systems.
```

## When This Pattern Applies

- Product/code name collisions with policy names (Fable harness vs Fable 5 directive)
- Company name collisions with concept names (e.g., "Spark" as company vs "Spark" as computation framework)
- Version number collisions (e.g., "Fable 5" as product version vs "Fable 5" as export control tier)

## Full Reference

The full disambiguation workflow is documented in `wiki-entity-enrichment-from-article/references/entity-name-collision-disambiguation.md`.
