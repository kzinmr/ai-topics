---
title: "Wiki changes — 2026-10-11 (uncommitted working tree)"
type: query
created: 2026-10-11
updated: 2026-10-20
tags:
  - query
  - knowledge-management
sources: []
status: archived
---

# Wiki changes — 2026-10-11 (uncommitted working tree)

> Snapshot note created by the `skeleton-enrich-daily` run (2026-10-11 19:xx UTC).
> The skeleton backlog was **empty** this run: `grep -rl "status: skeleton" wiki/entities/`
> returns 0 (only prose mentions remain in log files and `queries/2026-10-04-uncommitted-wip-snapshot.md`).
> The `dan-mcinerny` enrichment referenced in log.md line 30 is already committed (5e8c0acc).
> This run therefore made **no changes**; this file only re-checkpoints the still-uncommitted
> working tree (202 modified + 28 untracked files, mostly wiki WIP from active-crawl /
> blog-ingest / newsletter-ingest pipelines + skill edits) so it stays recoverable on GitHub.
> Safe to delete once the owning pipelines commit their work.

## State at snapshot time

- Modified (tracked): 202 files — wiki concepts/entities index & related-link updates,
  skill docs under `config/hermes/skills/`, `scripts/hierarchy_report.json`.
- Untracked: 28 files — new raw newsletters (2026-10-07..11), new concepts
  (`agentic-software-factory-hierarchy-of-needs`, `openai/gpt-5-6-codex-model-card-2026`),
  entities (`claude-haiku-5-5`), graph-analysis query (2026-10-09), new skill reference docs.
- Full diff: `cd ~/ai-topics && git diff -- wiki/`; list untracked: `git status --short | grep '^??'`.
