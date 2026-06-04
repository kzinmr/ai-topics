---
name: skill-archive-safety
description: Pre-flight checklist before archiving or deleting any Hermes skill. Prevents accidental removal of cron-referenced skills.
category: devops
---

# Skill Archive Safety

Always run this checklist before archiving or deleting any skill from `~/.hermes/skills/` or `config/hermes/skills/`.

## Pre-Flight Checklist

### 1. Check cron references
```bash
python3 -c "
import json
with open('/opt/data/.hermes/cron/jobs.json') as f:
    data = json.load(f)
for j in data['jobs']:
    skills = j.get('skills', [])
    skill = j.get('skill') or ''
    if 'TARGET_SKILL' in skills or 'TARGET_SKILL' in skill:
        print(f'REFERENCED: {j[\"name\"]}: {skills}')
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
