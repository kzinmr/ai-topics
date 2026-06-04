---
name: x-account-wiki-management
description: Add new X/Twitter accounts to tracking, create wiki entity pages, and maintain the knowledge base.
trigger: When asked to add a new X account to monitoring, create wiki pages for a person, or when discovering new AI personalities to track.
---

# X Account & Wiki Entity Management

## Workflow

### 1. Add to x-accounts.yaml
```yaml
- handle: '@Username'
  name: Real Name
  blog: [URL if available]
  topics: [ai, relevant-topics]
  notes: 'Brief description of who they are and why they matter.'
```

### 2. Generate Skeleton Entity Page
```bash
cd ~/ai-topics
~/.hermes/hermes-agent/venv/bin/python ~/scripts/build_x_wiki.py --handle @Username
```
This creates `wiki/entities/username.md` with `status: skeleton`.

### 3. Enrich Entity Page
Research the person's:
- X/Twitter activity and notable posts
- Blog posts and articles
- Open source projects and contributions
- Company affiliations
- Key ideas and philosophies

Update the entity page:
- Remove `status: skeleton` from frontmatter
- Add detailed bio, contributions, and notable work
- Cross-link to related concepts and people
- Target quality: match `wiki/entities/antirez-com.md` or `wiki/entities/simon-willison.md`

### 4. Update Index
Add entry to `wiki/index.md` under the entities section:
```markdown
[[entities/username|Display Name]] (@handle) — Brief description.
```

### 5. Commit & Push
```bash
cd ~/ai-topics
git add wiki/ config/feeds/x-accounts.yaml
git commit -m "wiki: add @Username entity and tracking"
git push
```

## Key Concepts to Cross-Link
- If they discuss multi-agent patterns: link to `[[back-of-house-multi-agent-patterns]]`
- If they discuss single-agent limitations: link to `[[single-agent-ceiling]]`
- If they discuss orchestration: link to `[[session-hierarchy-management]]`
- Always check `wiki/concepts/` for related pages

## Pitfalls
- Do NOT add duplicate entries to x-accounts.yaml — always search first
- Skeleton pages have TODO markers — these must be filled during enrichment
- Entity pages should be comprehensive, not just bios
- Always cross-reference with existing entities to avoid duplication

### YAML Multi-Line Notes Fragility
**x-accounts.yaml uses YAML folded scalar strings (block format) for multi-line `notes` fields.**
Patch-based edits can silently break the fold, causing parse errors at lines far from the edit.
This happened when editing TeortaxesTex's multi-line notes — the patch removed a leading space,
breaking the fold and causing a cascade of YAML parse failures.

**Safe approach:** Use `execute_code` to manipulate YAML directly:
```python
import yaml
with open('config/feeds/x-accounts.yaml', 'r') as f:
    data = yaml.safe_load(f)
accounts = data['accounts']
elvis_idx = next(i for i, a in enumerate(accounts) if a.get('handle') == '@elvissun')
accounts.insert(elvis_idx, {
    'handle': '@Username',
    'name': 'Real Name',
    'topics': ['ai', 'topic'],
    'notes': 'Single-line notes string (avoid multi-line folded scalars in manual edits).'
})
with open('config/feeds/x-accounts.yaml', 'w') as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=1000)
# Verify
with open('config/feeds/x-accounts.yaml', 'r') as f:
    yaml.safe_load(f)
print("Valid")
```
Note: `yaml.dump` will reformat the entire file (diff will show many changed lines), but output is always valid.