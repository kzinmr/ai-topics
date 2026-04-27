# AI Topics

AI Topics is the knowledge base repository maintained by Hermes Agent for LLM and AI Agent technologies.

This README describes the repository layout and stable responsibilities only. Operationally volatile details, such as subscription counts, cron schedules, current job state, and recent topic lists, should be read from the relevant config files or generated reports instead.

## Path Policy

- Treat `~/ai-topics` as the repository root.
- The canonical wiki path is `~/wiki`. Use this path in Hermes prompts and skills.
- The wiki content lives in this repository under `wiki/`, but prompts and skills should refer to destinations as `~/wiki/...`.
- Use `~/.hermes/scripts/...` in examples for Hermes-managed scripts. Cron script paths are interpreted relative to `~/.hermes/scripts`.
- Do not add environment-specific absolute paths or new alternate compatibility paths.

## Repository Layout

```text
ai-topics/
|-- README.md
|-- CHANGELOG.md
|-- blogwatcher.db
|-- .githooks/
|   `-- pre-commit
|
|-- inbox/
|   |-- newsletters/
|   `-- rss-scans/
|
|-- wiki/
|   |-- SCHEMA.md
|   |-- index.md
|   |-- log.md
|   |-- log-*.md
|   |-- raw/
|   |   |-- articles/
|   |   |-- assets/
|   |   |-- newsletters/
|   |   |-- papers/
|   |   `-- transcripts/
|   |-- concepts/
|   |-- entities/
|   |-- events/
|   |-- comparisons/
|   `-- queries/
|
|-- config/
|   |-- feeds/
|   |-- hermes/
|   |   |-- SOUL.md
|   |   |-- cron/
|   |   `-- skills/
|   `-- hot-topics.yaml
|
|-- scripts/
|-- systemd/
`-- docs/
```

## Main Areas

`inbox/` stores automatically collected inputs before wiki curation, including newsletter digests and RSS scan reports.

`wiki/` is the knowledge base itself. Follow `SCHEMA.md` for raw sources, concepts, entities, events, comparisons, and queries. When creating or updating pages, update `index.md` and `log.md` as well.

`wiki/raw/` stores source material such as articles, newsletters, papers, transcripts, images, and diagrams so later wiki pages can cite them.

`config/` stores source definitions, Hermes configuration, cron definitions, and active crawl targets. Project-specific local skills live under `config/hermes/skills/`.

`scripts/` stores automation for collection, triage, checkpoints, wiki maintenance, cron sync, and git hook installation. When describing these scripts in Hermes runtime contexts, use `~/.hermes/scripts/...`.

`systemd/` stores unit files for host integration. The actual enabled service state belongs to the runtime environment.

`docs/` stores setup, migration, and external integration documentation.

## Data Flow

```text
Configuration
  config/feeds/
  config/hot-topics.yaml
        |
        v
Collection and preprocessing
  cron jobs
  ~/.hermes/scripts/...
        |
        |-- inbox/newsletters/
        |-- inbox/rss-scans/
        `-- ~/wiki/raw/...
                |
                v
Curation
  Hermes Agent
        |
        |-- ~/wiki/concepts/
        |-- ~/wiki/entities/
        |-- ~/wiki/events/
        |-- ~/wiki/comparisons/
        `-- ~/wiki/queries/
                |
                v
Index and history
  ~/wiki/index.md
  ~/wiki/log.md
```

## Cron And Config Sync

The versioned copy of Hermes cron state lives at `config/hermes/cron/jobs.json`. Use `scripts/sync_cron.sh` to sync it with the runtime cron state.

`.githooks/pre-commit` pulls the Hermes cron state into the repository before each commit. Run `scripts/install_hooks.sh` once in a new clone to install the hook.

When running Hermes cron commands from outside Docker, use the wrapper under the Hermes root. For Lucy, use `bin/hermes-lucy`; do not run `docker exec ... hermes ...` directly.

## Wiki Update Rules

- Follow `wiki/SCHEMA.md` frontmatter and classification rules for new pages and substantial updates.
- If raw source material exists, keep references under `~/wiki/raw/...`.
- Add new pages to `~/wiki/index.md`.
- Record changes in `~/wiki/log.md`.
- Use `~/wiki/...` as the wiki destination path in prompts, skills, SOUL files, and runbooks.
