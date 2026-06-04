# Person Entity Tag Patterns

## Common Tag Combinations for Person Entities

When creating or enriching person/individual entity pages, use these canonical SCHEMA.md tag combinations. **Never invent role-specific tags not in SCHEMA.md** — the pre-commit hook (`pre-commit-tag-validator.py`) blocks ALL non-SCHEMA tags.

| Profile | Canonical Tags | Avoid These (Not in SCHEMA) |
|---------|---------------|---------------------------|
| **Blogger / Developer** | `person`, `software-engineering`, `content-creator` | `ai-engineer`, `backend-developer`, `fullstack` |
| **ML Researcher / Academic** | `person`, `ml-researcher`, `educator` | `research-scientist`, `professor` |
| **Founder / Investor** | `person`, `startup`, `vc` | `entrepreneur`, `investor` |
| **Open-Source Maintainer** | `person`, `open-source`, `developer-tooling` | `maintainer`, `oss-contributor` |
| **AI Tool Builder** | `person`, `ai-agent`, `developer-tooling` | `ai-developer`, `tool-builder` |
| **Curator / Signal Amplifier** | `person`, `content-creator`, `x-account`, `research` | `curator`, `signal-amplifier` |
| **Writer / Journalist** | `person`, `blog`, `writing`, `ai-commentary` | `journalist`, `tech-writer` |
| **Product Leader** | `person`, `product-management`, `ai-product` | `pm`, `director` |

## Real Failure Case (2026-05-25)

`sairahul1` entity page created with tags `ai-engineer` + `backend-developer` → pre-commit hook blocked. Fixed by replacing with `software-engineering` + `ai-automation` (both in SCHEMA.md).

## Tag Selection Process

```bash
# Before writing tags, verify against SCHEMA.md
grep -w "your-tag" /opt/data/ai-topics/wiki/SCHEMA.md

# If missing, search for similar canonical tags
grep -i "engineer\|developer\|person\|creator" /opt/data/ai-topics/wiki/SCHEMA.md | head -20
```

## Adding New Tags to SCHEMA.md

If a genuinely new tag is needed (covers a concept not expressible with existing tags):
1. Add it to the appropriate taxonomy category in `wiki/SCHEMA.md`
2. Stage the SCHEMA.md change alongside your page
3. The pre-commit hook will pass because the tag now exists in the taxonomy
