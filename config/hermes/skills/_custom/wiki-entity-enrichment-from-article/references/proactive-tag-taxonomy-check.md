# Proactive Tag Taxonomy Check

## The Pattern

**Before writing any wiki page**, check `wiki/SCHEMA.md` for tag availability and add missing tags first. This prevents the round-trip of: write page → pre-commit hook blocks → fix tags → recommit.

## Step-by-Step

1. Read `wiki/SCHEMA.md` and plan which tags to use
2. For any tag NOT in the taxonomy:
   - Add it to the correct category (Models, People/Orgs, Products, Techniques, Engineering, AI Agents, Infrastructure, or Meta)
   - Then use it in your page frontmatter
3. Category rules of thumb:
   - Company names → **People/Orgs** (e.g., `shopify`, `anthropic`)
   - Infrastructure concepts → **Engineering** (e.g., `llm-proxy`, `ai-infrastructure`)
   - Product/tool names → **Products** (e.g., `claude-code`, `mcp`)
   - Technique names → **Techniques** (e.g., `prompting`, `chain-of-thought`)
4. Format rules: lowercase kebab-case, prefer plural (`coding-agents` not `coding-agent`), no spaces, no wikilinks in tag names

## Why Proactive Beats Reactive

The existing pits (in both wiki-concept-from-research and wiki-entity-enrichment-from-article) describe the **reactive** fix — when the pre-commit hook catches a violation. The proactive check eliminates the failure entirely:

```
BAD (reactive):
  write page → git add → git commit → BLOCKED → read SCHEMA.md → fix tags → re-commit

GOOD (proactive):
  read SCHEMA.md → add missing tags → write page → git commit → PASSES
```

## Real Example (2026-05-20)

Creating `concepts/claude-code.md` and `concepts/shopify-ai-engineering.md` required two new tags:
- `shopify` → added to People/Orgs in SCHEMA.md before use
- `llm-proxy` → added to Engineering in SCHEMA.md before use

Both pages passed pre-commit validation on first attempt because tags were added to the taxonomy before the pages referenced them.
