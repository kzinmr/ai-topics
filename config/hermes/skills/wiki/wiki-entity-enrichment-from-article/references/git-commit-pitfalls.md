# Git Commit Pitfalls for Wiki Operations

## Tag Taxonomy Validation

The git commit hook validates ALL `tags:` arrays in wiki frontmatter against `SCHEMA.md` taxonomy definitions.

### Common Failure Mode

```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️ TAGS NOT IN SCHEMA.md TAXONOMY (1):
wiki/entities/peter-steinberger.md: personal-agents
```

This happens when you **invent a tag** that sounds reasonable but doesn't exist in SCHEMA.md (e.g., `personal-agents` instead of `personal-ai`).

### Prevention

1. **Before adding any new tag to frontmatter**, check SCHEMA.md:
   ```bash
   grep -i 'tag-name' ~/wiki/SCHEMA.md
   ```
2. If unsure, search existing entity pages for similar tags:
   ```bash
   grep -r 'tags:' ~/wiki/entities/ | grep -i 'similar'
   ```
3. Prefer existing tags over inventing new ones. The taxonomy is intentionally limited.

### Recovery (if you hit the error mid-session)

1. Read `SCHEMA.md` to find the correct tag
2. `patch` the entity file to replace the invalid tag:
   ```bash
   patch old_string="personal-agents" new_string="personal-ai" path="wiki/entities/peter-steinberger.md"
   ```
3. Re-run `git commit` — the hook validates ALL staged files, so even if only one file had the error, you need to re-commit everything

### Key Tags to Remember

| Concept | Invalid Tag | Valid SCHEMA Tag |
|---------|------------|-----------------|
| Personal AI agents | `personal-agents` | `personal-ai` |
| Open-source models | `open-llm` | `open-source` |
| Fine-tuning | `fine-tune` | `fine-tuning` |

## `&` Character in Commit Messages

The terminal tool interprets `&` as shell backgrounding. If your commit message contains `&` (e.g., `set_to_none=True`), use **single quotes**:
```bash
git commit -m 'wiki: safe message here'
```
Double quotes with `&` inside fail silently (the tool blocks `&&` chaining AND hangs on `&` inside double-quoted strings).

Split `git add`, `git commit`, `git push` into separate terminal calls when `&&` chaining fails.

## SSH/Git Credential Issues in Sandbox

If `git push` fails with authentication errors:
1. Verify the GitHub token is available in the current session environment
2. SSH may not be available in sandbox (no `ssh` binary)
3. Try passing the token via git credential helper inline
4. If still failing → token may be expired/revoked; save commits locally and notify user
5. Never lose committed work — the commits are still in local branch (ahead of origin)
