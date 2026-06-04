# Tag Taxonomy Quick Reference

When writing frontmatter `tags:` for ANY wiki page, ALL tags MUST be canonical tags from `wiki/SCHEMA.md`. The pre-commit hook validates this.

## Common non-canonical → canonical mappings

| Non-Canonical (BLOCKED) | Canonical (OK) | SCHEMA Section |
| `cdn` | `infrastructure` | Infrastructure |
| `benchmarking` | `benchmark` | Techniques |
| `search-api` | `search` | Meta |
| `web-monitoring` | `monitoring` | Engineering |
| `ai-agent-infrastructure` | `ai-infrastructure` | Engineering |
| `soc2` | `security` | Infrastructure |
| `cdn` | `infrastructure` | Infrastructure |
| `benchmarking` | `benchmark` | Techniques |
| `search-api` | `search` | Meta |
| `organization` | `company` | People/Orgs |
| `cdn` | `infrastructure` | Infrastructure |
| `benchmarking` | `benchmark` | Techniques |
| `search-api` | `search` | Meta |
## How to find the right tag

1. Read `wiki/SCHEMA.md` — tags are organized by category: People/Orgs, Engineering, AI Agents, Infrastructure, Meta
2. Find the closest semantic match
3. If no match exists, add the tag to SCHEMA.md first, then use it

## Emergency override

`git commit --no-verify` skips the check. Use only in emergencies.
