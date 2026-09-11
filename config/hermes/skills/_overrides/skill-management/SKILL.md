---
name: skill-management
description: "Complete Hermes skill lifecycle: authoring SKILL.md files, archiving/migrating skills safely, and detecting/remediating drift between formula and override copies."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [skills, authoring, archiving, drift-detection, lifecycle, management]
    related_skills: [hermes-repo-sync]
---

# Skill Management

Complete guide to Hermes skill lifecycle management: authoring new skills, safely archiving/migrating existing skills, and detecting/remediating drift between formula and override copies.

---

## Part 1: Authoring Skills

### Overview

There are two places a SKILL.md can live:

1. **User-local:** `~/.hermes/skills/<maybe-category>/<name>/SKILL.md` — personal, not shared. Created via `skill_manage(action='create')`.
2. **In-repo:** `/home/bb/hermes-agent/skills/<category>/<name>/SKILL.md` — committed, shipped with the package. Use `write_file` + `git add`. `skill_manage(action='create')` does NOT target this tree.

### When to Use

- User asks you to add a skill "in this branch / repo / commit"
- You're committing a reusable workflow that should ship with hermes-agent
- You're editing an existing skill under `/home/bb/hermes-agent/skills/`

### Required Frontmatter

Source of truth: `tools/skill_manager_tool.py::_validate_frontmatter`. Hard requirements:

- Starts with `---` as the first bytes (no leading blank line).
- Closes with `\n---\n` before the body.
- Parses as a YAML mapping.
- `name` field present.
- `description` field present, ≤ **1024 chars** (`MAX_DESCRIPTION_LENGTH`).
- Non-empty body after the closing `---`.

Peer-matched shape used by every skill under `skills/software-development/`:

```yaml
---
name: my-skill-name               # lowercase, hyphens, ≤64 chars (MAX_NAME_LENGTH)
description: Use when <trigger>. <one-line behavior>.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [short, descriptive, tags]
    related_skills: [other-skill, another-skill]
---
```

`version` / `author` / `license` / `metadata` are NOT enforced by the validator, but every peer has them — omit and your skill sticks out.

### Size Limits

- Description: ≤ 1024 chars (enforced).
- Full SKILL.md: ≤ 100,000 chars (enforced as `MAX_SKILL_CONTENT_CHARS`, ~36k tokens).
- Peer skills in `software-development/` sit at **8-14k chars**. Aim for that range. If you're pushing past 20k, split into `references/*.md` and reference them from SKILL.md.

### Peer-Matched Structure

Every in-repo skill follows roughly:

```
# <Title>

## Overview
One or two paragraphs: what and why.

## When to Use
- Bulleted triggers
- "Don't use for:" counter-triggers

## <Topic sections specific to the skill>
- Quick-reference tables are common
- Code blocks with exact commands
- Hermes-specific recipes

## Common Pitfalls
Numbered list of mistakes and their fixes.

## Verification Checklist
- [ ] Checkbox list of post-action verifications

## One-Shot Recipes (optional)
Named scenarios → concrete command sequences.
```

Not every section is mandatory, but `Overview` + `When to Use` + actionable body + pitfalls are the minimum for the skill to feel like a peer.

### Directory Placement

```
skills/<category>/<skill-name>/SKILL.md
```

Categories currently in repo (confirm with `ls skills/`): `autonomous-ai-agents`, `creative`, `data-science`, `devops`, `dogfood`, `email`, `gaming`, `github`, `leisure`, `mcp`, `media`, `mlops/*`, `note-taking`, `productivity`, `red-teaming`, `research`, `smart-home`, `social-media`, `software-development`.

Pick the closest existing category. Don't invent new top-level categories casually.

### Workflow

1. **Survey peers** in the target category: `ls skills/<category>/`
2. **Check validator constraints** in `tools/skill_manager_tool.py` if unsure.
3. **Draft** with `write_file` to `skills/<category>/<name>/SKILL.md`.
4. **Validate locally**:
   ```python
   import yaml, re, pathlib
   content = pathlib.Path("skills/<category>/<name>/SKILL.md").read_text()
   assert content.startswith("---")
   m = re.search(r'\n---\s*\n', content[3:])
   fm = yaml.safe_load(content[3:m.start()+3])
   assert "name" in fm and "description" in fm
   assert len(fm["description"]) <= 1024
   assert len(content) <= 100_000
   ```
5. **Git add + commit** on the active branch.
6. **Note:** the CURRENT session's skill loader is cached — `skill_view` / `skills_list` will not see the new skill until a new session.

### Cross-Referencing Other Skills

`metadata.hermes.related_skills` unions both trees (`skills/` in-repo and `~/.hermes/skills/`) at load time.

See also: `references/skill-sync-pitfalls.md` for pitfalls when syncing skills between the two locations. You CAN reference a user-local skill from an in-repo skill, but it won't resolve for other users who clone the repo fresh. Prefer referencing only in-repo skills from in-repo skills.

### Editing Existing In-Repo Skills

- **Small fix (typo, added pitfall, tightened trigger):** `skill_manage(action='patch', name=..., old_string=..., new_string=...)` works fine on in-repo skills.
- **Major rewrite:** `write_file` the whole SKILL.md. `skill_manage(action='edit')` also works but requires supplying the full new content.
- **Adding supporting files:** `write_file` to `skills/<category>/<name>/references/<file>.md`, `templates/<file>`, or `scripts/<file>`.
- **Always commit** the edit — in-repo skills are source, not runtime state.

### Common Pitfalls (Authoring)

1. **Using `skill_manage(action='create')` for an in-repo skill.** It writes to `~/.hermes/skills/`, not the repo tree. Use `write_file` for in-repo creation.
2. **Leading whitespace before `---`.** The validator checks `content.startswith("---")`; any leading blank line or BOM fails validation.
3. **Description too generic.** Peer descriptions start with "Use when ..." and describe the *trigger class*, not the one task.
4. **Forgetting the author/license/metadata block.** Not validator-enforced, but every peer has it; omitting makes the skill look half-finished.
5. **Writing a skill that duplicates a peer.** Before creating, `ls skills/<category>/` and open 2-3 peers. Prefer extending an existing skill to creating a narrow sibling.
6. **Expecting the current session to see the new skill.** It won't. The skill loader is initialized at session start. Verify in a fresh session or via `skill_view` using the exact path.
7. **Linking to skills that don't exist in-repo.** `related_skills: [some-user-local-skill]` works for you but breaks for other clones. Prefer only in-repo links.

### Verification Checklist (Authoring)

- [ ] File is at `skills/<category>/<name>/SKILL.md` (not in `~/.hermes/skills/`)
- [ ] Frontmatter starts at byte 0 with `---`, closes with `\n---\n`
- [ ] `name`, `description`, `version`, `author`, `license`, `metadata.hermes.{tags, related_skills}` all present
- [ ] Name ≤ 64 chars, lowercase + hyphens
- [ ] Description ≤ 1024 chars and starts with "Use when ..."
- [ ] Total file ≤ 100,000 chars (aim for 8-15k)
- [ ] Structure: `# Title` → `## Overview` → `## When to Use` → body → `## Common Pitfalls` → `## Verification Checklist`
- [ ] `related_skills` references resolve in-repo (or are explicitly OK to be user-local)
- [ ] `git add skills/<category>/<name>/ && git commit` completed on the intended branch

---

## Part 2: Archiving & Migration Safety

### Skill Inventory Management

#### Managed vs Unmanaged Skills
- **Managed (git-tracked)**: Live in `~/ai-topics/config/hermes/skills/` — these are version-controlled and syncable
- **Unmanaged (local)**: Live in `~/.hermes/skills/` — these are runtime skills not yet committed to the repo
- **Archive convention**: Unmanaged skills in `.archive` subdirectories (e.g., `~/.hermes/skills/.archive/baoyu-comic/`) are deprecated but still counted as unmanaged in inventory checks

#### Promotion Workflow (Unmanaged → Managed)
Before promoting, confirm the skill is genuinely unmanaged — not already under `config/hermes/skills/_overrides/` or `_custom/` (see the cache-reset pitfall above; many "new" flags are stale-cache false positives).

When new unmanaged skills are identified during inventory checks:
1. **Assess value**: Does the skill encode reusable workflow knowledge (not session-specific hacks)?
2. **Check for duplicates**: `find ~/ai-topics/config/hermes/skills -type d -name "<skill-name>"` — don't promote if a managed version already exists
3. **Copy to managed**: `cp -r ~/.hermes/skills/<category>/<skill-name>/ ~/ai-topics/config/hermes/skills/<category>/<skill-name>/`
4. **Verify frontmatter**: Ensure YAML frontmatter has `name`, `description`, `category` fields
5. **Commit**: `cd ~/ai-topics && git add config/hermes/skills/ && git commit -m "skills: promote <name>" && git push`
6. **Archive original**: Move the local copy to `~/.hermes/skills/.archive/<skill-name>/` to prevent future inventory noise

#### Pitfall: "New unmanaged skills" may be a cache-reset artifact, not actually new

The inventory checker (`ai-topics/scripts/check_new_skills.py`) detects "new" skills by diffing `~/.hermes/skills/` against a baseline cache (`scripts/cache/skills_baseline.json`). If that cache is reset or re-seeded, every existing unmanaged skill re-appears as "new" even though it has been there for a while. **Before assuming a flagged skill is genuinely new**, verify:

```bash
# 1. Is it actually in the baseline cache already? (ABSENT = not previously scanned)
python3 -c "import json; d=json.load(open('~/ai-topics/scripts/cache/skills_baseline.json')); print({k:v for k,v in d.items() if 'PRICING' in k or 'kanban' in k})"

# 2. Does a git-managed copy already exist? (check _overrides/ AND _custom/ AND _adhoc/ — NOT just category-nested)
find ~/ai-topics/config/hermes/skills -type d -name "<skill-name>"

# 3. Is the local copy actually in sync / drifted vs the managed copy?
diff ~/.hermes/skills/<category>/<skill>/SKILL.md ~/ai-topics/config/hermes/skills/_overrides/<skill>/SKILL.md
```

If the skill already has a git-managed `_overrides/` (or `_custom/`) copy, it is NOT new — do not "promote" it again. A local copy being newer than the managed copy is **drift** (version bumps, added `platforms:` fields, new sections), which is the job of the `skill-drift-check` cron, not the inventory check.

#### Pitfall: "Managed (git): N" counter under-counts in the flat layout

`check_new_skills.py` computes "Managed (git)" by counting *category-nested* `config/hermes/skills/<cat>/<skill>` dirs only. The repo actually uses a **flat** `_overrides/` and `_custom/` layout (see "Managed vs Unmanaged" above), so the counter reports a number far lower than the true managed count (e.g. "Managed: 0" when ~60 overrides + ~11 custom exist). **Do not trust the "Managed (git)" number in the report** to decide whether a skill is managed — always run the `find` above directly. If you are editing `check_new_skills.py`, make the managed-skill lookup recurse into `_overrides/`, `_custom/`, and `_adhoc/` (flat + category-nested) so this false-negative "new" report stops recurring.

#### Inventory Check Commands
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

#### Removal Criteria
Skills should be archived (not deleted) when:
- Superseded by a newer umbrella skill
- Referenced by active cron jobs (check `~/.hermes/cron/jobs.json`)
- Contain reusable workflow knowledge not captured elsewhere

Skills can be deleted when:
- One-off session artifacts with no generalizable knowledge
- Fully duplicated in another skill's `references/` directory
- Obsolete tool workflows (deprecated APIs, removed features)

### CRITICAL: Pre-Flight Checklist

**NEVER skip this checklist before ANY skill operation (archive, delete, move, rename).**

#### 1. Check cron references (MANDATORY)

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

#### 2. Check config.yaml references

```bash
grep -r "TARGET_SKILL" ~/.hermes/config.yaml 2>/dev/null
```

#### 3. Check cross-skill references

```bash
grep -r "TARGET_SKILL" ~/.hermes/skills/ --include="*.md" -l 2>/dev/null
```

#### 4. Verify archive target exists

```bash
ls -la ~/.hermes/skills/.archive/ 2>/dev/null || mkdir -p ~/.hermes/skills/.archive/
```

### Archive Procedure

1. Run pre-flight checklist (above)
2. Move skill directory to archive:
   ```bash
   mv ~/.hermes/skills/<category>/<skill-name> ~/.hermes/skills/.archive/<category>/<skill-name>
   ```
3. Update any references in other skills (if absorbed into umbrella)
4. Commit changes if in git repo

### Common Pitfalls (Archiving)

1. **Archiving a skill referenced by active cron jobs.** Always check `jobs.json` first.
2. **Deleting instead of archiving.** Archives are recoverable; deletion is not.
3. **Forgetting to update cross-references.** Other skills may reference the archived skill.
4. **Not verifying the archive target directory exists.** Create it if needed.
5. **"Repo-only = unused" is wrong** — `external_dirs` loads repo skills into Hermes; the 2026-06-04 bulk sync deleted 4 cron-referenced skills under this false assumption. Full post-mortem + safe restructure procedure: `references/skill-migration-lessons.md`.

---

## Part 3: Drift Detection & Remediation

### When to Use

- Running or parsing the `skill-drift-check` weekly cron (script: `scripts/check_skill_drift.py`)
- Reviewing/remediating `_overrides` vs formula skill divergence
- Any task that needs to locate a formula skill on disk (they are **not** flat under `~/.hermes/skills/`)

### Skill Library Layout

- **Active skills** = the copies in external_dirs: `config/hermes/skills/{_custom,_overrides,_adhoc}`. `_overrides/` holds modified copies of formula skills (63 of them).
- **Formula skills live category-nested**: `~/.hermes/skills/<category>/<skill>/SKILL.md` (e.g. `research/active-crawl-wiki`, `wiki/blog-writing`, `social-media/xurl`). Only `dogfood`, `skill-archive-safety`, `wiki-daily-report` are stored flat.
- **Non-live dirs to exclude** when searching: `.archive`, `.curator_backups`, `.hub`, `.quarantine` (archived formulas live under `.archive/<category>/<skill>`).
- **PATH TRAP nuance**: `Path.home()` in cron = `/opt/data/.hermes/home`; the `.hermes -> ..` symlink makes `Path.home()/"."hermes"/"skills"` resolve correctly to `/opt/data/.hermes/skills`, but printed paths show the symlinked `/opt/data/.hermes/home/.hermes/skills/...` form. Don't mistake that for the container-home trap — `Path.exists()` follows the symlink.
- Full detail + snapshot: `references/skill-library-layout.md`

### Workflow

1. Run the checker, capturing stdout/stderr separately (do NOT pipe `python3 | python3` — security scanner flags it):
   `python3 ~/ai-topics/scripts/check_skill_drift.py > /tmp/drift_report.json 2> /tmp/drift_summary.txt`
2. Parse JSON: per-skill `checks[]` plus `drifted[]`, `missing_formula[]`, `missing_override[]`.
3. Report summary: total overrides, drifted count, formula missing count.

### Status Semantics

| status | meaning | action |
|---|---|---|
| `in_sync` | identical file sets | none |
| `formula_updated` | shared files differ (usually SKILL.md) | diff override vs formula; re-base the override preserving intentional local changes |
| `formula_has_new_files` | formula gained `references/` the override lacks | copy missing refs into the override, or re-sync from formula |
| `formula_missing` | no live formula found | distinguish: **archived formula** (override is orphan → archive the override too, per skill-archive-safety) vs **custom-only override** (move to `_custom/` or accept as expected) |

### Pitfalls (Drift Checking)

- **Do NOT reintroduce flat-only formula lookup.** The original script checked only `~/.hermes/skills/<name>` and falsely reported ~60 of 63 overrides as `formula_missing` (fixed 2026-08-03, commit 9b68f45b). Formula must be searched **recursively** with archive-dir exclusion; shallowest match wins.
- **Some formula files are unreadable** (PermissionError, e.g. `productivity/cron-job-management/SKILL.md`). The script warns on stderr and skips that file — the comparison is partial, so treat such skills as "drift status uncertain" (they may still be flagged via `only_formula`).
- **skill_view/skill_manage by bare name is ambiguous** for any overridden skill (formula + override collide → "Ambiguous skill name ... 2 skills match"). Formula copies may also be permission-denied. Prefer **creating new skills** over patching overrides through the skill tools.
- **Ambiguous skill name breaks cron skill loading — fix by dedupe, not workaround** (fixed 2026-08-28). When a skill exists BOTH in `~/.hermes/skills/<category>/<name>/` AND in an external_dir, `skill_view(bare_name)` refuses with "Ambiguous skill name" and the cron scheduler logs `skill not found, skipping` — the job runs WITHOUT the skill content (silent quality loss; report jobs still "succeed"). Diagnose with: `grep "Ambiguous skill name" ~/.hermes/logs/errors.log`. Remediation that makes bare names resolve: (1) diff the two copies, (2) copy the RICHERER copy into the external_dir (repo `_overrides/`) so nothing is lost, including `references/`/`scripts/`, (3) `mv` the local copy out to a dated archive dir (e.g. `~/.hermes/skill-archive/YYYY-MM-DD-dedup/` — note `.archive` under skills/ is excluded from scans), (4) git commit+push the repo copy, (5) verify every skill referenced by any cron job resolves: load `~/.hermes/cron/jobs.json`, loop `skill_view(name)` and check `success`. Repo (`_overrides/`) becomes the single canonical location for overridden skills — never keep a same-named local formula copy around.
- **Cron-session tooling**: `execute_code` is blocked in cron mode (no user to approve); use `write_file` to `/tmp/<name>.py` + `terminal`. See `references/cron-session-tooling-patterns.md`.
- **Git hygiene**: when the repo has unrelated unstaged changes, stage only your file (`git add <file>`, not `-A`) and commit separately.
- **Archiving a formula copy can leave a NEW ambiguous collision — verify resolution AFTER every dedupe archive.** The "dedupe by archiving local formula copy" recipe above assumes the repo `_overrides/` copy then resolves under the bare name. It does not when the name also collides with an unrelated agent-created skill (observed 2026-09-11: archiving flat `~/.hermes/skills/skill-archive-safety/` made bare `skill-archive-safety` ambiguous against the override copy; `skill_view`/`skill_manage` fail with "2 skills match"). Fix: rename the override dir (e.g. `_overrides/skill-archive-safety` → `_overrides/skill-drift-check`, matching the cron job that consumes it) AND update the `skills` array in `~/.hermes/cron/jobs.json` + the repo formula dir name + its SKILL.md frontmatter `name:` in lockstep, then commit/push. Post-condition check (mandatory after any archive): load jobs.json, loop every referenced skill through `skill_view(name)`, assert `success` AND that returned `path` is the intended copy — resolving is not enough, verify WHICH copy resolved.

### Verification

Independent check pattern: rglob `SKILL.md` under `~/.hermes/skills`, exclude archive dirs, build name→dirs map, compare file sets + byte equality, pick the shallowest match. Script sketch in `references/skill-library-layout.md`. Always cross-check the checker's numbers against this before reporting (the checker has been wrong before).

---

## Related Skills

- `hermes-repo-sync` (devops) — syncing Hermes runtime state from the repo
