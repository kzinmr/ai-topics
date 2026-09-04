# Concept Names Are NOT Automatically Valid Tags

## The Trap

A concept page exists in `wiki/concepts/` → its slug appears in `wiki/index.md` → subagents and agents treat the slug as a valid tag and add it to entity page frontmatter. But SCHEMA.md's tag taxonomy is the **sole source of truth** — concept page existence is irrelevant for tag validation. The pre-commit hook (`pre-commit-tag-validator.py`) checks SCHEMA.md, not index.md.

## Common Violations

| Used (invalid) | Should be | Why |
|---|---|---|
| `graph-engineering` | Not a SCHEMA tag — remove entirely | Concept page `graph-engineering.md` exists, but SCHEMA.md doesn't list it as a tag |
| `ai-educator` | `educator` | SCHEMA.md has `educator` under Meta, not the compound form |
| `rl-training` | `reinforcement-learning` | SCHEMA canonical is `reinforcement-learning` |
| `agent-sandboxing` | `sandbox` | Under "Models" taxonomy |
| `open-weights` (plural) | `open-weight` (singular) | SCHEMA.md has singular form |
| `tooling` | `developer-tools` or `tool` | Context-dependent; check SCHEMA |

## Detection Rule

Before adding ANY tag to a page:
```bash
grep -F 'tag-name' /opt/data/ai-topics/wiki/SCHEMA.md
```

If grep returns nothing, the tag is invalid — do not use it. Use a canonical SCHEMA tag instead, or add the tag to SCHEMA.md first.

## When it hits

This is most common when subagents create entity pages for new people/orgs/tools and attempt to tag them with concept names that seem obviously relevant but aren't registered. The entity page is correct; only the tags need fixing. Pattern:

1. Subagent creates entity page with tag like `graph-engineering` (not in SCHEMA)
2. Pre-commit hook blocks entire commit (including other valid files)
3. Fix: read the entity page → `patch` to replace invalid tag(s) with canonical SCHEMA equivalents → re-commit

## Real Example (Aug 2026)

`entities/0xmovez-ai.md` created with tags `graph-engineering` and `ai-educator`. Both exist as concept pages but neither is in SCHEMA.md. Fixed: `graph-engineering` removed (not needed for person entity), `ai-educator` → `educator` (SCHEMA canonical). One patch, one re-commit.
