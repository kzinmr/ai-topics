# `llm-wiki` skill name collision (recurring, benign)

**Symptom**: Cron jobs that list `llm-wiki` in their skills report
`⚠️ Skill(s) not found and skipped: llm-wiki`. The watchdog pre-run context
and job status show this as an error. In severe cases a job is marked
`error: RuntimeError: ⚠️ Skill(s) not found and skipped: llm-wiki` **even
though the run actually completed** (observed 2026-11-10: newsletter-wiki-ingest
was flagged error but had fully produced and committed its triage report).

**Root cause**: Two `llm-wiki` SKILL.md files exist with identical frontmatter
`name: llm-wiki`:

- `~/.hermes/skills/research/llm-wiki/SKILL.md` — upstream copy, v2.1.0, 20 KB
- `~/ai-topics/config/hermes/skills/_overrides/llm-wiki/SKILL.md` — repo-managed
  override, 35 KB, with `references/` subdir

The skill loader resolves the name to the `_overrides` copy and reports the
shadowed upstream copy as "not found and skipped". It is a **shadowing notice,
not a real content loss** — the intended (override) content loads.

**Watchdog procedure**:
1. Verify the override content actually loads: `skill_view(name='llm-wiki')`
   should return the override version (larger file / repo-specific TAG GATE rules).
2. If it loads → report-only. Do NOT delete either copy without user direction.
3. If it does NOT load → escalate: the resolution order has changed and pipelines
   may be running without the TAG GATE / page-threshold rules.

**Note (2026-11-10)**: `~/.hermes/skills/research/llm-wiki` and the `_overrides`
copy are both present and have byte-identical `name:`/`description:`/`version:`
frontmatter; the only difference is body size (override is richer). Verified via
`head -8` on both. The earlier weekly graph-analysis response already annotated
this as "欠落ではなく名前衝突" (not missing — a name collision).

**Permanent fix options** (require user decision, not watchdog scope):
- Delete the upstream `~/.hermes/skills/research/llm-wiki` copy so only the
  override remains.
- Or rename the override's `name:` field and update all cron job skill lists.
