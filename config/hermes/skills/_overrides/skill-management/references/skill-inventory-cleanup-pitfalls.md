# Skill Inventory Cleanup Pitfalls

## Critical: `external_dirs` Makes Repo-Only Skills Active

Hermes `config.yaml` may have:
```yaml
skills:
  external_dirs:
  - ~/ai-topics/config/hermes/skills
```

Skills in that path are **actively loaded** even if absent from `~/.hermes/skills/`. Cron jobs resolve skills by name through both paths.

## The Anti-Pattern

When syncing `~/.hermes/skills/` → repo, a naive cleanup:
1. Finds files in repo but not in `~/.hermes/skills/`
2. Classifies them as "repo-only = unused"
3. Deletes them → **breaks cron jobs**

## Safe Cleanup Procedure

Before removing ANY skill from the repo:

1. **Check cron references:** read `~/.hermes/cron/jobs.json`, collect all `skills[]` and `skill` fields
2. **Check `external_dirs`:** `grep external_dirs ~/.hermes/config.yaml`
3. **Check AGENTS.md:** `grep -i skill ~/ai-topics/AGENTS.md`
4. **Only remove** skills not referenced by any of the above

## Recovery

```bash
cd ~/ai-topics
git log --oneline -5
git checkout <commit> -- config/hermes/skills/<category>/<skill-name>/
git commit -m "fix: restore cron-required skill <name>"
git push
```
