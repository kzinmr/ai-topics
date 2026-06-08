# Skill Migration Lessons (2026-06-04)

## What Happened

A bulk sync/cleanup operation on `config/hermes/skills/` accidentally deleted skills that were actively referenced by cron jobs. The cleanup compared repo skills against `~/.hermes/skills/` and removed anything found only in the repo — but `external_dirs` means repo skills ARE loaded into Hermes.

## Timeline of Damage and Recovery

| Action | Impact | Fix |
|---|---|---|
| Sync script deleted "repo-only" files | 4 cron skills lost | `git checkout 59875392 -- path/` |
| Archive cleanup deleted `.archive/` from repo | 25 archived skills lost from repo | Already in `~/.hermes/skills/.archive/` (safe) |
| `dreaming`, `daily-rss-triage` deleted from `.archive/` | 2 cron skills lost again | `git checkout 8ff7d660 -- path/` |
| Batch move to 3-layer dirs | 4 skills dropped (wrong path match) | Manual find + `git checkout` + move |

## Key Anti-Patterns

### 1. "Not in ~/.hermes/skills/ = unused"
**Wrong.** `external_dirs` in config.yaml loads skills from repo paths. Always check:
```bash
grep "external_dirs" ~/.hermes/config.yaml -A5
```

### 2. Batch operations without validation
Never run `rm -rf` or `git rm` on skill directories without first running the bulk validation script. One missing check → 4 broken cron jobs.

### 3. Comparing by basename only
When moving skills between directories (e.g., `research/blogwatcher-db` → `_custom/`), the `for s in blogwatcher-db` loop doesn't match `research/blogwatcher-db`. Use full relative paths or `find` + `mv`.

### 4. Assuming git history is infinite
`git checkout OLDCOMMIT -- path/` works, but if the path was restructured multiple times, the commit may be hard to find. Commit immediately after any skill restructure.

## Safe Restructure Procedure

```bash
# 1. Validate cron skills exist
python3 -c "...(Step 3 from SKILL.md)..."

# 2. Move with full paths
cd config/hermes/skills
mv research/blogwatcher-db _custom/  # NOT: mv blogwatcher-db _custom/

# 3. Re-validate
python3 -c "...(Step 3 again)..."

# 4. Update config.yaml if needed

# 5. Commit immediately
git add -A && git commit -m "refactor: ..." && git push
```
