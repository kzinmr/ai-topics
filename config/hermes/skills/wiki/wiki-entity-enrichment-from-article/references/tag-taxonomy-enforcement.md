# Tag Taxonomy Enforcement

The `pre-commit-tag-validator.py` hook enforces that ALL tags in wiki page frontmatter exist in `wiki/SCHEMA.md`'s canonical taxonomy (457 tags as of 2026-05).

## Rule

**Never invent new tags without adding them to SCHEMA.md first.** The pre-commit hook will block the commit with:

```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED

⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (N):
   wiki/path/to/page.md:  tag-name
```

## What To Do When Blocked

1. **Option A (preferred)**: Map the new tag to an existing canonical tag from SCHEMA.md
2. **Option B**: Add the new tag to `wiki/SCHEMA.md` in the appropriate category, then commit
3. **NEVER** use `git commit --no-verify` except in emergencies

## Common Tag Mappings

| Non-canonical tag | Closest canonical tag(s) |
|---|---|
| `terminal-agents` | `ai-agents` + `cli` |
| `cli-agents` | `ai-agents` + `cli` |
| `organization` | `company` or `lab` |
| `research-lab` | `lab` |
| `ml-infrastructure` | `ai-infrastructure` or `agent-infrastructure` |
| `ml-engineering` | `mlops` or `ai-infrastructure` |

## Key Canonical Tag Categories (from SCHEMA.md)

- **People/Orgs**: `company`, `lab`, `open-source`, `researcher`, `entrepreneur`, `indie-maker`, `pseudonymous`
- **AI Agents**: `ai-agents`, `multi-agent`, `coding-agents`, `agent-training`, `agent-framework`, `agent-harness`, `autonomous-agents`
- **Techniques**: `reinforcement-learning`, `grpo`, `rlhf`, `dpo`, `fine-tuning`, `post-training`, `world-models`
- **Engineering**: `cli`, `ai-infrastructure`, `agent-infrastructure`, `mlops`, `developer-tooling`
- **Infrastructure**: `gpu`, `hardware`, `docker`, `kubernetes`, `cloud-infrastructure`

## Verification

After fixing tags, run the commit again:
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..."
```

The validator output shows `✅ Tag validation passed — N files, all tags in SCHEMA taxonomy` on success.
