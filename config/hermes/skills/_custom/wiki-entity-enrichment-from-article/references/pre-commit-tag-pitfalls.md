# Pre-Commit Tag Taxonomy Pitfalls

## Problem

The pre-commit hook (`config/hermes/skills/wiki/wiki-graph-health/scripts/pre-commit-tag-validator.py` or similar) **blocks commits** when ANY tag in a wiki page's frontmatter is not in `wiki/SCHEMA.md`. This is not a warning — it's a hard block with `exit code 1`.

Example error:
```
TAGS NOT IN SCHEMA.md TAXONOMY (5):
   wiki/concepts/deepswe-benchmark.md:  swe-bench
   wiki/concepts/legal-agent-benchmark.md:  legal-ai
   wiki/concepts/legal-agent-benchmark.md:  agentic-ai
   wiki/concepts/legal-agent-benchmark.md:  behavioral-analysis
   wiki/entities/serena-ge.md:  ai-researcher
```

## Common Non-SCHEMA Tags and Their Canonical Replacements

| Non-SCHEMA Tag | Canonical SCHEMA Tag |
|---------------|---------------------|
| `swe-bench` | `benchmark` or `coding-agents` |
| `legal-ai` | `ai-adoption` |
| `agentic-ai` | `ai-agents` |
| `behavioral-analysis` | `agent-evaluation` |
| `ai-researcher` | `researcher` |
| `coding-benchmark` | `benchmark` + `coding-agents` |
| `llm-agent` | `ai-agents` |

## Workflow When Blocked

1. Read the error output to identify which tags are non-conforming
2. Map each non-conforming tag to the closest SCHEMA.md canonical tag using `grep` on SCHEMA.md
3. Patch each affected page's frontmatter `tags:` array
4. `git add` and re-attempt commit

## When a New Tag IS Needed

If the concept genuinely needs a new tag category that doesn't exist in SCHEMA.md:
1. Add the tag to `wiki/SCHEMA.md` under the appropriate category (People/Orgs, Techniques, AI Agents, etc.)
2. Commit SCHEMA.md changes first or together with the page changes
3. Use the new tag in the page frontmatter

## Verification

```bash
# Check which tags a page uses
grep -A5 '^tags:' wiki/concepts/new-page.md

# Check if a tag exists in SCHEMA
grep 'tagname' wiki/SCHEMA.md

# Run the pre-commit check manually
python3 config/hermes/skills/wiki/wiki-graph-health/scripts/pre-commit-tag-validator.py wiki/concepts/new-page.md
```
