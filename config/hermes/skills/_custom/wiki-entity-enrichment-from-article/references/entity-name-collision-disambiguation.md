# Entity Name Collision / Disambiguation

When a new entity page shares its name with an existing wiki page of a different type or domain, add a disambiguation admonition to prevent confusion.

## When to Add

- New entity page name matches an existing **concept** page name (e.g., `entities/fable.md` vs `concepts/claude/fable-5`)
- New entity page name matches another entity page referencing a different thing (e.g., two companies named "Nova")
- Product name collision with policy/subject name (e.g., Anthropic's "Fable" coding harness vs US export control framework "Fable 5")

## How to Add

Place the disambiguation admonition immediately after the page title heading (`# Entity Name`)  in the body, before any overview content:

```markdown
> **Not to be confused with**: [[concepts/claude/fable-5]] — the US export control framework for AI systems, which shares the "Fable" name but is a completely separate entity.
```

## Format

- Use a markdown blockquote (`>`) for visual prominence
- Format: `> **Not to be confused with**: [[wikilink]] — brief description of what it IS`
- Include the wikilink so readers can navigate directly
- If there are 2+ collision targets, use a bullet list inside the blockquote

## Real Example

In `entities/fable.md` (Anthropic's coding harness, July 2026):

```markdown
> **Not to be confused with**: [[concepts/claude/fable-5]] — the US export control framework for AI systems.
```

The entity page was created from a Ben's Bites newsletter article describing Fable as a creative thinking partner. `concepts/claude/fable-5` was already in the wiki covering the US government's Fable 5/Mythos 5 export control directive. Without the admonition, readers searching for "Fable" would land on the wrong page.

## Three-Way Collision Check

Before creating any new entity or concept page, always search the wiki for the proposed name:

```bash
find ~/ai-topics/wiki -maxdepth 2 -name "*keyword*" -type f
```

Or use `search_files` with the keyword in both `entities/` and `concepts/` directories. If collisions exist, add the admonition. If 3+ pages share the same name root, consider adding a disambiguation hub page at `comparisons/` or `concepts/<name>-disambiguation.md`.
