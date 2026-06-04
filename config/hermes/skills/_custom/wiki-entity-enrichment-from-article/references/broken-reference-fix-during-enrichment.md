# Broken Reference Fix During Concept Enrichment

When enriching an existing concept page, entity pages may reference it under a different/broken slug.

## Pattern

1. You enrich `concepts/<actual-slug>.md`
2. Entity pages reference `[[concepts/<different-slug>]]` which doesn't exist
3. The different slug was either a working name, typo, or renamed concept

## Detection

After enriching a concept, search for potential broken references:

```bash
# Search for the actual slug (should find entity refs)
grep -rn "ai-services-joint-ventures" ~/wiki/entities/ --include="*.md"

# Search for likely alternative names
grep -rn "enterprise-ai-deployment" ~/wiki/entities/ --include="*.md"
```

## Fix

`patch` each entity page to use the correct slug:
```
old_string: "[[concepts/enterprise-ai-deployment-jv]]"
new_string: "[[concepts/ai-services-joint-ventures]]"
```

## Real Example (2026-05-11)

**Concept**: `concepts/ai-services-joint-ventures.md`
**Broken refs found**:
- `entities/openai.md`: `[[concepts/enterprise-ai-deployment-jv]]` → fixed
- `entities/anthropic.md`: `[[concepts/enterprise-ai-deployment-jv]]` → fixed

This prevents accumulation of dangling wikilinks that `wiki-graph-health` would later catch.
