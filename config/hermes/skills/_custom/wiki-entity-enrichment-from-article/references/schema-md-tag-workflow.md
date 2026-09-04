# SCHEMA.md Tag Addition Workflow (cron-safe)

> **Trigger**: Creating a new concept/entity page with tags not yet in SCHEMA.md. The pre-commit hook blocks ALL non-canonical tags.

## Pre-Write Verification

Before writing ANY new wiki page with tags, verify each planned tag exists:

```bash
grep -oE '[a-z][a-z-]+' wiki/SCHEMA.md | sort -u | grep -x 'your-planned-tag'
```

If empty output → tag doesn't exist yet. Either find a canonical equivalent or add it.

## Canonical Tag Mapping Table

Common non-canonical tags and their existing SCHEMA.md equivalents:

| Non-canonical | Canonical | SCHEMA.md Section |
|--------------|-----------|-------------------|
| `agent-context` | `context-engineering` | Engineering |
| `super-agent` | `ai-agents` | AI Agents |
| `antitrust` | `regulation` | Meta |
| `permission` (privacy context) | `privacy` | Meta |
| `swere-bench` | `benchmark` | Models |
| `agents-md` | *add new* | AI Agents |
| `apple` (company) | *add new* | People/Orgs |
| `trust` (concept) | *add new* | Meta |

**Regulatory/policy tags (added 2026-06-10)**:
| `model-card` | `model-card` | Meta — canonical |
| `system-card` | `system-card` | Meta — canonical |
| `eu-ai-act` | `eu-ai-act` | Meta — canonical |

## Adding New Tags to SCHEMA.md

**CRITICAL**: Do NOT use `patch` for SCHEMA.md tag additions. The file has very long lines (hundreds of tags per line) that `read_file` truncates with `...` artifacts, causing `patch` to fail with "Could not find a match."

**Use `sed` instead:**

```bash
# Add to People/Orgs line (line 33) — append before line end
sed -i 's/spotify$/spotify, apple/' wiki/SCHEMA.md

# Add to Meta line (line 39) — append two tags
sed -i 's/recsys-2025$/recsys-2025, trust, permission/' wiki/SCHEMA.md

# Add to AI Agents line (line 37) — insert in the middle
sed -i 's/agent-skills, verification/agent-skills, verification, agents-md, swere-bench/' wiki/SCHEMA.md
```

**Always verify after each sed:**
```bash
grep -o 'new-tag-name' wiki/SCHEMA.md && echo "OK" || echo "MISSING"
```

**Stage SCHEMA.md alongside new pages:**
```bash
git add wiki/SCHEMA.md wiki/concepts/new-page.md
git commit -m 'wiki: ...'
```

## Full Session Example (2026-06-08)

Created two new concept pages with several non-canonical tags. Workflow:

1. Wrote concept pages with clean tag sets
2. First commit blocked — 8 tag violations across both pages
3. Mapped 3 tags to existing canonicals: `agent-context`→`context-engineering`, `super-agent`→`ai-agents`, `antitrust`→`regulation`, `platform`→already exists
4. Used `sed` to add 5 genuinely new tags: `apple` (People/Orgs), `trust`+`permission` (Meta), `agents-md`+`swere-bench` (AI Agents)
5. Re-committed — passed validation
6. Push succeeded
