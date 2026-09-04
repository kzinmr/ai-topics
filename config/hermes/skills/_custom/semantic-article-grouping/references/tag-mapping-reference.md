# Tag Mapping Reference

Quick-reference for mapping non-SCHEMA tags to valid SCHEMA.md equivalents. The pre-commit hook blocks commits with tags absent from `wiki/SCHEMA.md` taxonomies (~631 canonical tags, line 34–40). When `grep -i "keyword" wiki/SCHEMA.md` returns nothing, use this table.

## Entity Pages (companies, organizations, people)

| Invalid Tag | SCHEMA Equivalent | Rationale |
|---|---|---|
| `organization` | `company` | Entity pages describe companies/research orgs |
| `startup` | `company` or `ecosystem` | Use `company` for the entity, `ecosystem` for the class |
| `founder` | `author` or omit | Not a direct SCHEMA tag; describe in content |
| `researcher` | `author` or `developer` | Depending on role |

## Concept Pages (events, releases, ideas)

| Invalid Tag | SCHEMA Equivalent | Rationale |
|---|---|---|
| `acquisition` | `event` + `announcement` | Break into two valid tags |
| `tooling` | `developer-tooling` | Hyphenated compound in SCHEMA |
| `real-world` | `ai-agents` or `benchmark` | Related to agent behavior or evaluation |
| `enterprise` | `enterprise-ai` or `enterprise-agents` | Both exist in SCHEMA |
| `m365` | `managed-agents` + `enterprise-ai` | Microsoft Scout is both |
| `collaboration` | `human-agent-collaboration` | Long but valid |
| `automation` | `ai-automation` or `agent-automation` | Hyphenated form |
| `infrastructure` | `ai-infrastructure` or `cloud` | Match the domain |
| `safety` | `ai-safety` | Prefix is canonical |
| `multi-agent-systems` | `multi-agent` | Singular `multi-agent` is the canonical SCHEMA tag |
| `multi-agent-architecture` | `agent-architecture` | Use the existing architecture tag |
| `gpu-compute` | `gpu` | `gpu` exists in infrastructure taxonomy; the `compute` qualifier is redundant |
| `gpu-optimization` | `optimization` + `gpu` | Split into two existing tags |

## Technology Attributes

| Invalid Tag | SCHEMA Equivalent | Rationale |
|---|---|---|
| `llm` | already in SCHEMA | Use directly (`llm` is valid) |
| `multimodal` | already in SCHEMA | Use directly |
| `open-source` | already in SCHEMA | Use directly |
| `performance` | `performance-engineering` or `performance` | Both exist |
| `product` | already in SCHEMA | Use directly |
| `demo` | `prototype` or `announcement` | Closest semantic match |
| `research` | already in SCHEMA | Use directly |

## Common Patterns

When creating new pages, prefer:
- **Semantic precision** over novelty — existing tags like `agent-evaluation`, `enterprise-agents`, `developer-tooling` cover specific concepts
- **Break compound tags** (5+ word kebab-case) into individual existing tags
- **If really no match exists**: add the new tag to SCHEMA.md in the appropriate taxonomy line (lines 34-40)

## Quick Check

```bash
# Before commit, verify all tags:
for tag in $(grep -hr '^  - ' wiki/entities/andon-labs.md wiki/concepts/vending-bench.md | sed 's/  - //'); do
  if ! grep -q "$tag" wiki/SCHEMA.md; then
    echo "MISSING: $tag"
  fi
done
```
