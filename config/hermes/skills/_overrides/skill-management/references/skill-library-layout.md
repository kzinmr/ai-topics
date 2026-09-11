# Skill library layout (verified 2026-08-03)

## Paths
- Formula root: `/opt/data/.hermes/skills/` (= `~/.hermes/skills/` = `Path.home()/".hermes"/"skills"`)
- Overrides root: `/opt/data/ai-topics/config/hermes/skills/_overrides/` (63 skills)
- Custom / adhoc: `.../_custom/`, `.../_adhoc/`

## Formula placement
- **Category-nested (the norm)**: `research/active-crawl-wiki`, `research/arxiv`, `research/blogwatcher`, `research/llm-wiki`, `research/trending-topics-reporting`, `wiki/blog-writing`, `wiki/documentation-page-ingestion`, `wiki/raw-article-filename-policy`, `wiki/wiki-comparison-page-routing`, `wiki/wiki-concept-from-research`, `github/github-auth`, `social-media/xurl`, `media/youtube-content`, `autonomous-ai-agents/codex`, `creative/claude-design`, `productivity/cron-job-management`, `software-development/writing-plans`, etc.
- **Nested two levels**: `wiki-daily-report/hermes-report-quality`
- **Flat (only 3)**: `dogfood`, `skill-archive-safety`, `wiki-daily-report`
- **Excluded non-live dirs**: `.archive`, `.curator_backups`, `.hub`, `.quarantine`. Recursive scan excluding these finds 110 formula skills; archived copies live under `.archive/<category>/<skill>`.

## Snapshot from the fixed checker (2026-08-03)
- 63 overrides → 35 in sync, 23 drifted, 5 formula_missing, 0 missing_override.
- **Formula missing (5)**: `goal-delegation-patterns` (formula archived), `x-article-getxapi-fallback` (archived), `x-article-retrieval` (archived), `wiki-graph-health` (custom-only), `wiki-watchdog-auto-fix` (custom-only).
- **Drift pattern**: most are `formula_has_new_files` — the formula gained `references/` the override lacks: `trending-topics-reporting` (+22 refs), `xurl` (+11), `active-crawl-wiki` (+14), `wiki-concept-from-research` (+5), `documentation-page-ingestion` (+4), `youtube-content` (+3), `wiki-comparison-page-routing` (+3), `blog-writing` (+2), `blogwatcher` (+2), `hermes-agent-skill-authoring` (+2), `llm-wiki` (+2), `agent-harness-research`/`codex` (+1 each), `cron-job-management` (+1). Several are `formula_updated` with only SKILL.md differing: `arxiv`, `claude-design`, `hermes-report-quality`, `skill-archive-safety`, `subagent-driven-development`, `writing-plans`, `wiki-daily-report` (nested `hermes-report-quality/SKILL.md`), `ocr-and-documents`, `raw-article-filename-policy` (SKILL.md + one ref each).

## PATH TRAP resolution
- Cron HOME = `/opt/data/.hermes/home`. Inside it: `.hermes -> ..`, `ai-topics -> ../../ai-topics`, `wiki -> ../../ai-topics/wiki`.
- `Path.home()/".hermes"/"skills"` resolves via the symlink to `/opt/data/.hermes/skills` — correct, but `str()` shows the `/opt/data/.hermes/home/.hermes/skills/...` form. Verify with `Path.exists()` (follows symlinks) rather than trusting the printed path.

## Verification script sketch (used to confirm the 2026-08-03 fix)
```python
from pathlib import Path
FORMULA_ROOT = Path("/opt/data/.hermes/skills")
excluded = {".archive", ".curator_backups", ".hub", ".quarantine"}
formula_map = {}
for d in FORMULA_ROOT.rglob("SKILL.md"):
    parts = d.relative_to(FORMULA_ROOT).parts
    if parts[0] in excluded:
        continue
    formula_map.setdefault(d.parent.name, []).append(d.parent)
# for each override: pick shallowest match, compare file sets + byte equality
```

## Cron job
- `skill-drift-check` — weekly Monday. Uses `scripts/check_skill_drift.py`.
- Fixed 2026-08-03 (commit 9b68f45b): now searches formula recursively with archive-dir exclusion, shallowest match wins, PermissionError surfaced as stderr WARNING. JSON schema unchanged (checks[] + drifted[] + missing_formula[] + missing_override[]).
