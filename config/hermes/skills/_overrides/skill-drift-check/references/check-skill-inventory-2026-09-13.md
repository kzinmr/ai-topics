# check-skill-inventory run — 2026-09-13

Report: 3 removed (cloudflare-email-delivery, dogfood, llm-api-pricing-monitor), 95 unmanaged,
0 managed, 0 builtin. **No new skills.**

## Key finding: the "95 unmanaged" line is a baseline artifact, not a workload

`~/.hermes/scripts/check_new_skills.py` uses `HERMES_SKILLS = Path.home()/".hermes"/"skills"`.
In this container `/opt/data/home` is the docker HOME (see AGENTS.md PATH TRAP), so it scans
`/opt/data/home/.hermes/skills` — the same tree as `/opt/data/.hermes/skills` via symlink.
That is fine, but the baseline it writes (`scripts/cache/skills_baseline.json`) and the
"Unmanaged" number count ALL runtime skills, most of which are generic Hermes skills that will
never be promoted. 95 is the steady state, not drift.

## Removed skills — all legitimate, pre-flight clean

| skill | location after removal | why |
|---|---|---|
| cloudflare-email-delivery | `.archive/dedup-2026-09-11/` | folded into the `wiki` umbrella |
| llm-api-pricing-monitor | `.archive/` (superseded by `llm-pricing-monitor`) | rename/dedup |
| dogfood | (no longer present) | exploratory-QA builtin, not needed here |

Checked per the skill-drift-check pre-flight: no cron job in
`/opt/data/.hermes/cron/jobs.json` references any of the three; no reference in
`~/ai-topics/AGENTS.md`. Archive convention (SKILL.md still present under `.archive/`) is
intentional — the finder excludes `.archive` by path, so they correctly drop out of the count.

## Promotion assessment: nothing to promote

`managed = 0` in the report is misleading: `config/hermes/skills/` holds 74 SKILL.md files, but
only under `_custom/` and `_overrides/<name>/`. The script's managed-detection assumes
`<category>/<name>/SKILL.md` (it takes `len(parts)==2` and treats `parts[0]` as the category),
so `_custom/` and `_overrides/` trees are invisible to it and the count is reported as 0.
Consequently skills such as `blog-writing`, `documentation-page-ingestion`,
`wiki-concept-from-research`, `wiki-daily-report`, `wiki-maintenance`, `llm-wiki`,
`trending-topics-reporting` appear as "unmanaged local" while actually being git-tracked under
`_overrides/`. Do not propose re-promoting them — that would create a duplicate on disk.

Genuinely unmanaged AI-topics content worth watching (still not promoted, no action this run):
- `milksandmatcha/` → its SKILL.md is really `wiki-git-sync` (name ≠ directory name, plus a
  long blob of person-entity trivia pasted into the frontmatter/first paragraph — needs cleanup
  before it could ever be promoted).

Non-promotable by design: `yuanbao` (gateway messaging plumbing), `apple-*`/`imessage`/`findmy`
(no macOS host), creative/media/gaming builtins, `himalaya` (AGENTS.md explicitly forbids using
it for this mailbox).

## Actions taken
- Patched `skill-drift-check`: inventory verification snippet against the authoritative
  `skills_baseline.json`, plus a promotion health-check that buckets unmanaged skills into
  already-canonical / generic-builtin / genuine-candidate and assumes "nothing to promote".
- Committed+pushed to ai-topics (commits 8852bd5a, ca6fc48f).
