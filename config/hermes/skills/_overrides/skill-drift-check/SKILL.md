---
name: skill-drift-check
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

**HEALTH CHECK — run first, do not blindly "promote everything unmanaged":**
The unmanaged count is ~95 by design and does NOT mean there is work to do. Before
suggesting any promotions, bucket every unmanaged skill:
- **already canonical** — content already lives in a managed umbrella skill or in
  `AGENTS.md`/`SCHEMA.md` (e.g. `himalaya` vs the AGENTS.md email mandate, `linear`/`airtable`
  under the `productivity` umbrellas). No action; archiving them is what makes them show up
  as "removed" noise later.
- **generic Hermes builtins** — `ascii-art`, `baoyu-*`, `comfyui`, `excalidraw`, `p5js`,
  `pixel-art`, `manim-video`, `pokemon-player`, `minecraft-modpack-server`, `godmode`,
  `openhue`, `imessage`/`findmy`/`apple-*` (no macOS host here). Not AI-topics knowledge;
  leave local or archive, never promote.
- **genuinely new + reusable AI-topics workflow knowledge** — the only real promotion
  candidates. This bucket has been empty for every check to date.
Assume the answer is "nothing to promote" and justify each exception.

### Resolved 2026-10-04: unmanaged set cleaned up
The 4 superseded local skills were archived to `~/.hermes/skills/.archive/` with
`SKILL.md` renamed to `SKILL.md.disabled` (per the archive convention above):
`code-quality` (⊂ requesting-code-review + systematic-debugging, 80% line coverage),
`planning-and-execution` (⊂ writing-plans + subagent-driven-development, 54%),
`kanban` (⊂ kanban-orchestrator + kanban-worker, 96%), `hermes-repo-sync`
(⊂ skill-management, which lists it as related). Pre-flight passed: no cron jobs,
config.yaml, or AGENTS.md references. New steady state: **Managed 76 / Unmanaged 1 /
Builtin 70**. The 1 remaining unmanaged (`yuanbao`) is disabled Yuanbao-gateway
plumbing with tools absent from this profile — leave it, never promote.
If this job reports the old 5-item unmanaged list again, the archive was reverted;
restore it rather than re-triaging.

When new unmanaged skills are identified during inventory checks:
1. **Assess value**: Does the skill encode reusable workflow knowledge (not session-specific hacks)?
2. **Check for duplicates**: `find ~/ai-topics/config/hermes/skills -type d -name "<skill-name>"` — don't promote if a managed version already exists
3. **Copy to managed**: `cp -r ~/.hermes/skills/<category>/<skill-name>/ ~/ai-topics/config/hermes/skills/<category>/<skill-name>/`
4. **Verify frontmatter**: Ensure YAML frontmatter has `name`, `description`, `category` fields
5. **Commit**: `cd ~/ai-topics && git add config/hermes/skills/ && git commit -m "skills: promote <name>" && git push`
6. **Archive original**: Move the local copy to `~/.hermes/skills/.archive/<skill-name>/` to prevent future inventory noise

### Inventory Check Commands
```bash
# Canonical baseline state used by check_new_skills.py (authoritative for diffs):
#   /opt/data/.hermes/scripts/cache/skills_baseline.json
# Verify it against the live tree before trusting a cron report:
python3 -c "
import json, pathlib
base=json.load(open('/opt/data/.hermes/scripts/cache/skills_baseline.json'))
skills=pathlib.Path('/opt/data/.hermes/skills')
actual={}
for sm in skills.rglob('SKILL.md'):
    if '.archive' in sm.parts: continue
    parts=sm.parent.relative_to(skills).parts
    if len(parts)==2: actual[parts[1]]=parts[0]
    elif len(parts)==1: actual[parts[0]]='uncategorized'
print('baseline',len(base),'actual',len(actual))
print('stale:',sorted(k for k in base if k not in actual))
print('new:',sorted(k for k in actual if k not in base))
"

# Count managed skills (git-tracked)
find ~/ai-topics/config/hermes/skills -name SKILL.md | wc -l

# IMPORTANT: archived skills must have SKILL.md RENAMED (e.g. SKILL.md.disabled).
# `.archive` is in the path, so rglob-based finders already skip them, but a plain
# `find ~/.hermes/skills -name SKILL.md` will still count them — do not use that
# count as the unmanaged total.
```

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

## Inventory Report Anomalies = Fix the Script, Not the Tree (2026-09-27)

The `check-skill-inventory` weekly job was fed a bad script for ~5 weeks. Signals that
the *report* was broken rather than the skill tree being dirty:

- "Managed (git): 0" while `find ~/ai-topics/config/hermes/skills -name SKILL.md | wc -l` says 74
- ~25 repo-managed skills (blog-writing, wiki-*, llm-wiki, trending-topics-reporting,
  xurl, arxiv, xurl, youtube-content, ...) appearing as "unmanaged local"
- "Builtin: 0" even though builtins are enabled and loaded
- The identical 95-item list repeated every week, with a growing `.archive/` tail
  (archived skills showed up as "new unmanaged" because `.archive` was counted as a category)

Root causes (all fixed in `ai-topics/scripts/check_new_skills.py`, commit 15d859ff — copy
it over `~/.hermes/scripts/check_new_skills.py`, cron runs that copy):

1. `MANAGED_SKILLS = Path(__file__).resolve().parent.parent/"config"/...` — the script is
   *copied* into `~/.hermes/scripts/`, so that path never existed → managed count 0.
   Must be the absolute `/opt/data/ai-topics/config/hermes/skills`.
2. Managed detection only understood `<category>/<name>/SKILL.md` (2 path parts), blind to
   the 2026-08-23 `_custom/` `_overrides/` `_adhoc/` 3-layer layout.
3. Builtin detection scanned `~/.hermes/hermes-agent/skills/`, which does not exist here
   (builtins ship with the venv install, not the profile).

**The reliable oracle is `hermes skills list`**, not a filesystem scan. Pitfalls when
parsing it:
- `rich` truncates names to `…` at default width → run with `COLUMNS=200`, and drop any
  name ending in `…` rather than trusting it.
- No `--json` for `skills list`.
- Splitting a bordered row on `│` yields leading/trailing empty cells:
  `['', name, category, source, trust, status, '']` → drop the first element before indexing.
- `source` is `local`/`builtin`/`hub`; category is blank for external-dir skills.

After the fix the steady state is **Managed 76 / Unmanaged 5 / Builtin 70**, and the 5
unmanaged (code-quality, hermes-repo-sync, kanban, planning-and-execution, yuanbao) are
all either superseded by umbrella skills or gateway plumbing — i.e. still nothing to promote.

### Stray skill directories with mismatched frontmatter names
`~/.hermes/skills/milksandmatcha/SKILL.md` declared `name: wiki-git-sync` — a duplicate
copy that had absorbed person-entity trivia (MilksandMatcha / 0xSero notes) into its body.
The real skill lives elsewhere and loads as `wiki-git-sync`; the repo's canonical copy of
that person knowledge is `wiki/entities/milksandmatcha.md`. A directory whose name differs
from its frontmatter `name:` is a stray artifact, not a loadable skill — the fallback
filesystem scan now skips those, and the stray was moved to
`~/.hermes/skills/.archive/stray-2026-09-27/wiki-git-sync-stray-copy`.
Before deleting such a copy, diff it against the real skill AND grep the wiki for the
entity knowledge so nothing unique is lost.

### If the fix is reverted or the job misfires again
```bash
diff ~/.hermes/scripts/check_new_skills.py /opt/data/ai-topics/scripts/check_new_skills.py
cp /opt/data/ai-topics/scripts/check_new_skills.py ~/.hermes/scripts/check_new_skills.py
python3 /opt/data/ai-topics/scripts/check_new_skills.py   # expect Managed 76 / Unmanaged ~5
```
Re-seeding: the baseline is `~/.hermes/scripts/cache/skills_baseline.json`; the first run
after a definition change reports spurious new/removed entries — run it twice and trust the
second.

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
