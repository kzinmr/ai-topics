---
name: skill-archive-safety
description: Pre-flight checklist and procedures for archiving, deleting, or migrating Hermes skills. Prevents accidental removal of cron-referenced skills. Covers the 3-layer skill structure and config.yaml management. Includes skill inventory management, promotion workflows, and archival conventions.
category: devops
---

# Skill Archive Safety & Management

## Skill Inventory Management

### Managed vs Unmanaged Skills
- **Managed (git-tracked)**: Live in `~/ai-topics/config/hermes/skills/` — these are version-controlled and syncable
- **Unmanaged (local)**: Live in `~/.hermes/skills/` — these are runtime skills not yet committed to the repo
- **Archive convention**: Unmanaged skills in `.archive` subdirectories (e.g., `~/.hermes/skills/.archive/baoyu-comic/`) are deprecated but still counted as unmanaged in inventory checks

### Promotion Workflow (Unmanaged → Managed)
When new unmanaged skills are identified during inventory checks:
1. **Assess value**: Does the skill encode reusable workflow knowledge (not session-specific hacks)?
2. **Check for duplicates**: `find ~/ai-topics/config/hermes/skills -type d -name "<skill-name>"` — don't promote if a managed version already exists
3. **Copy to managed**: `cp -r ~/.hermes/skills/<category>/<skill-name>/ ~/ai-topics/config/hermes/skills/<category>/<skill-name>/`
4. **Verify frontmatter**: Ensure YAML frontmatter has `name`, `description`, `category` fields
5. **Commit**: `cd ~/ai-topics && git add config/hermes/skills/ && git commit -m "skills: promote <name>" && git push`
6. **Archive original**: Move the local copy to `~/.hermes/skills/.archive/<skill-name>/` to prevent future inventory noise

### Inventory Check Commands
```bash
# Count managed skills (git-tracked)
find ~/ai-topics/config/hermes/skills -name "SKILL.md" | wc -l

# Count unmanaged skills (local runtime)
find ~/.hermes/skills -name "SKILL.md" | wc -l

# Find archived skills (deprecated but present)
find ~/.hermes/skills/.archive -name "SKILL.md" | wc -l

# Check for skill name collisions (can cause ambiguous load errors)
find ~/.hermes ~/ai-topics/config/hermes/skills -type d | sed 's|/SKILL.md||' | sort | uniq -d
```

### Removal Criteria
Skills should be archived (not deleted) when:
- Superseded by a newer umbrella skill
- Referenced by active cron jobs (check `~/.hermes/cron/jobs.json`)
- Contain reusable workflow knowledge not captured elsewhere

Skills can be deleted when:
- One-off session artifacts with no generalizable knowledge
- Fully duplicated in another skill's `references/` directory
- Obsolete tool workflows (deprecated APIs, removed features)

## CRITICAL: Pre-Flight Checklist

**NEVER skip this checklist before ANY skill operation (archive, delete, move, rename).**

### 1. Check cron references (MANDATORY)

```bash
python3 -c "
import json
with open('/opt/data/.hermes/cron/jobs.json') as f:
    data = json.load(f)
target = 'TARGET_SKILL'
for j in data['jobs']:
    skills = j.get('skills', [])
    skill = j.get('skill') or ''
    if target in skills or target in skill:
        print(f'BLOCKED: {j[\"name\"]} references {target}')
"
```

### 2. Check config.yaml references
```bash
grep -r "TARGET_SKILL" ~/.hermes/config.yaml 2>/dev/null
```

### 3. Check AGENTS.md / SCHEMA.md references
```bash
grep -r "TARGET_SKILL" ~/ai-topics/AGENTS.md ~/ai-topics/wiki/SCHEMA.md 2>/dev/null
```

### 4. Check other skills for dependencies
```bash
grep -r "TARGET_SKILL" ~/.hermes/skills/*/SKILL.md 2>/dev/null
```

## Rules

1. **NEVER** archive/delete a skill referenced by any active cron job
2. **NEVER** archive/delete a skill referenced in AGENTS.md or SCHEMA.md
3. **ALWAYS** check cron-jobs.json before any skill operation
4. **ALWAYS** commit skill changes to repo immediately after modification
5. If a skill is referenced but no longer needed, update the cron job FIRST

## Recovery Procedure

If a skill was accidentally removed:
1. Check git history: `git log --oneline -- config/hermes/skills/SKILL_NAME/`
2. Restore: `git checkout COMMIT -- config/hermes/skills/SKILL_NAME/`
3. Verify cron reference: Run pre-flight checklist above
4. Commit: `git commit -m "fix: restore SKILL_NAME (cron-required)"`
