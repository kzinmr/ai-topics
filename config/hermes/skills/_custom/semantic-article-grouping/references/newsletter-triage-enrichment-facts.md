# Newsletter-Triage Enrichment Facts Carrier Pattern (validated 2026-08-10)

When the downstream `newsletter-wiki-ingest` executes takes from a newsletter triage JSON
(recovered from `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` after an upstream
JSON-parse failure), the raw newsletter digest files are **link stubs** — they contain ONLY
tracking/redirect URLs (Substack UI noise, beehiiv `v2/c` tokens) and zero article body.
The verified facts live in the **triage JSON itself**: `body_excerpt` + `reason_ja` + resolved `url`.

## The pattern that worked

All 6 take enrichments in the 2026-08-10 run (TileRT InferenceX, Claude Code 5 setup guide,
Nathan Lambert "Lessons from the hacks", Hark Handoff, ByteDance Seedance 2.5, Eve legal-AI
entity creation) were executed via `delegate_task` blocks of 3, with each context carrying:

1. **The exact numbers/quotes from the triage `body_excerpt`** (e.g. "340 tok/s/user on 8×B200",
   "$0.18/M input tokens vs $5.00 GPT 5.5", "80% of system prompt deleted")
2. **`candidate_wiki_path`** (the page to create or enrich)
3. **The raw newsletter source path** for the `sources:` frontmatter entry
   (e.g. `raw/newsletters/2026-08-09-google-sells-the-shovels-...md`)
4. **An explicit instruction: "do NOT read the raw newsletter file for content — use the
   facts in this context"**

The ByteDance subagent independently confirmed the pattern:
> "The newsletter digest file contains only link stubs (no article body), so facts were
> taken from the task's triage summary as supplied."

Contrast with blog-triage takes: those DO have full pre-extracted content files at
`raw_path`, so subagents can (and should) read the raw article.

## Pitfall: malformed frontmatter is NOT caught by pre-commit

`entities/bytedance.md` (2026-08-10) had five stray list items sitting between the `tags:`
block and `sources:` — they silently parsed as extra `sources` entries, corrupting the
frontmatter, and the pre-commit tag-validator did NOT flag it (tags present in the block
were still SCHEMA-valid). Fix applied: merge stray items into `tags:`, remove the stray
lines, then validate with `yaml.safe_load(frontmatter)`.

**Rule**: every enrichment subagent should run a YAML parse on the frontmatter it edits
before reporting success. PyYAML may be missing on the PEP-668-managed venv — install with
`pip install --break-system-packages` (the sandbox allows it; it is a venv-local change).

## Git-sync note for busy multi-pipeline repos

After committing with **targeted `git add`** (only your staged files; sibling pipelines
leave unrelated unstaged changes like muse-glimmer/muse-spark), `git pull --rebase` will
fail with "cannot pull with rebase: You have unstaged changes" when other pipelines have
dirty files. That failure is **benign** — run `git push` directly; if it reports
`old..new main -> main`, the commit is safely pushed and the rebase warning can be ignored.
Do NOT `git stash`/`git checkout` the sibling pipelines' files.
