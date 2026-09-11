# Cross-Reference Worked Example — 2026-09-07 (Monday daily)

## Day profile

"Narrative turning point" day: OpenAI RSI-day cluster (Pachocki "An Alien Mind" HN 425pts/388c + internal research-acceleration report HN 185pts/144c), AGI-declaration controversy (Huang "race over" vs Marcus/Chollet), Alderson safety-vs-security critique, Hyperbo agent-platform essay. Willison called it "RSI day" — multiple same-day lab publications on the same theme fold into one topic cluster, not N topics.

## Key learnings

### 1. Wiki-created ≠ index-registered (the day's main residual)

Morning pipelines created `concepts/agi-declaration-controversy-2026.md` and `entities/jakub-pachocki.md`, and the log.md head-scan marked the topics covered — but NEITHER was in `wiki/index.md`. A page that's not in the index is invisible to navigation and to future dedup checks.

Batch-verify after the action table is settled:
```bash
cd ~/ai-topics
for f in concepts/agi-declaration-controversy-2026 entities/jakub-pachocki; do
  grep -q "$(basename $f)" wiki/index.md && echo "OK $f" || echo "MISS $f"
done
```
Register MISS lines in `wiki/index.md` (correct section, alphabetical, bump Total pages + Last updated) as part of the same commit.

### 2. Commit rule refinement: report-only = save-only; wiki-touched = commit

Prior guidance said this job never commits. That holds when the run ONLY writes `inbox/rss-scans/trending-topics-*.md`. But this run also created 4 raw research notes under `wiki/raw/articles/` and edited `wiki/index.md` and `wiki/log.md` — wiki/ content that belongs in the audit trail. Commit with **scoped** `git add` (report + the 4 raws + index.md + log.md), NOT `git add wiki/` — other jobs had concurrent uncommitted changes in `wiki/` and `config/hermes/skills/`. Pre-commit hooks (index validator, tag taxonomy, JP-language policy) passed on plain `git commit -m`. Commit: `26acf24f`.

### 3. Cloudflare-403 primary source → secondary-synthesis raw note

"An Alien Mind" (`openai.com/index/an-alien-mind/`) 403'd curl (known OpenAI JS/CF gate). Handling: wrote `wiki/raw/articles/2026-09-07_openai-an-alien-mind-research-note.md` as a secondary-source synthesis (HN thread + Willison's post + newsletter coverage), frontmatter `confidence: medium`, report line explicitly says 本文未取得 + follow-up. Do not stall the report or fabricate quotes from the title.

### 4. Japanese typo sweep before saving/committing

The finished report shipped `ウィクション推奨アクション` (broken katakana; should be `ウィキ推奨アクション`) and other artifacts. The SKILL.md report template itself contains the same `ウィクション` typo in its Final Table snippet — do not copy it blindly. Grep the report for suspicious katakana tokens before commit; also verify pipe-table `|---|` separator rows survived patches (daily-rss-triage pitfall #19 class).

### 5. Post-compaction resume went clean

Context compacted mid-run; the deterministic fallback summary reported Active Task "unknown". Resume protocol that worked: `git status` + `git diff --staged --stat` + `git log --oneline` + `ls inbox/rss-scans/` reconstructed state — the report and raws existed on disk, only the commit was pending. Verify-before-redo beat re-doing (per llm-wiki skill's post-compaction section).

### 6. Index-JP-language policy confirmed benign for reports

JP-language pre-commit hook gates JP in `wiki/` files, NOT `inbox/rss-scans/`. Report stayed fully Japanese; index.md entries written in English.

## Topic-to-wiki mapping used in the report

1. OpenAI RSI day → `entities/jakub-pachocki`, `concepts/agi-declaration-controversy-2026`
2. AGI declaration controversy → `concepts/agi-declaration-controversy-2026`
3. Safety vs security (Alderson) → `concepts/ai-agent-safety-incidents`, `concepts/agent-sandbox-patterns`
4. Agent = parameterized program (Lopopolo/Hyperbo) → `concepts/agent-platform-capability-composition`
5. OSS AI-code provenance → `concepts/ai-code-provenance-in-open-source` (active-crawl same-day)
6. Nitter/XCancel revival → ecosystem context only (777pts, weak AI link)
7. Ask HN skills-file management → `concepts/agent-skills`
