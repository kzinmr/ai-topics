# Blog Triage Patterns — 2026-08-05 (run 20260805T101151Z)

Batch: 17 candidates + 3 unsaved_articles → 20 decisions: Takes=8, Ref=1, Skip=11 (~47% take rate).

## RC-vs-GA Coverage Pitfall (NEW coverage-gap variant)

An entity page may document **release candidates** of a tool while the **final GA release is missing** — the GA ships days later as a separate blog post.

Concrete case: `entities/simon-willison.md` had detailed `llm 0.32rc1` / `0.32rc2` entries (Jul 30) but **zero** coverage of the LLM 0.32 GA (Aug 4) with its headline features (reasoning traces to stderr, server-side tools CodeInterpreter/WebSearch/AnthropicMCP, `model.prompt(messages=[])`, content-addressable Git-style message store, `llm openai endpoint`, "LLM is an agent framework now"). Also missing: the companion plugin `llm-anthropic 0.26` (Claude Fable 5 / Sonnet 5 / Opus 5 model support, `-T` server-side tools, thinking/thinking_effort simplification).

**The test**: when triaging a software-release article, grep the entity page for BOTH the RC and GA version strings (`0.32rc1` ≠ `0.32`) AND the plugin companion version (`llm-anthropic 0.26`). Check the page's dated Updates section, not just the version number presence. Finding `0.32rc1` is NOT finding `0.32`.

Same pattern applies to the 4-article single-author release cluster: all four Simon Willison articles (llm-anthropic 0.26, condense-json 1.1, minimax-h3-mlx, LLM 0.32 final) feed ONE entity page update — the takes array should carry the same `candidate_wiki_path` for related releases, and the downstream wiki-ingest merges them.

## Yield: Single-Author Release-Cluster Batches (~47% takes)

Composition that produced 8/17 takes:
- 4× Simon Willison on one major release (LLM 0.32 GA + plugin + MLX port) → `entities/simon-willison.md`, `entities/minimax.md`
- Zitron "The AI Demand Bubble" with new analyst numbers (Barclays 73% AWS AI revenue, UBS Google Cloud 28%/48%, Wells Fargo 74% Microsoft, M365 Copilot $3.859B, $1.35T off-balance-sheet) → `entities/ed-zitron.md`
- Sierra "Context Engine" product launch → `entities/sierra.md` (Horizon section existed, Context Engine absent — confirmed by grep before deciding)
- Daring Fireball on OpenAI-Apple preliminary injunction stage → `events/openai-apple-conflict-2026.md` (event page stopped at Aug 3 rebuttal; PI motion + Quinn Emanuel Exhibit F email were the gap)
- Nesbitt "brew install actions/checkout" (gh-actions-lock, OCI artifacts, Homebrew-tap registry) → `entities/andrew-nesbitt.md`
- Doctorow "Tech Freedom Cooperative" (HRDAG federated compute, post-American internet) → `entities/cory-doctorow.md`

Key: verify each take is a genuine gap (entity page read in full, not just grepped). The composition (one big release + several distinct announcements) is the signal, not the author count.

## Archive Path Symlink Verification

`archive_triage.py blog --keep-reference` may report an `archive_path` under a nested prefix like `/opt/data/.hermes/home/ai-topics/wiki/raw/archived/triage/blog/...` — this is the `~/.hermes/home` symlink farm, NOT a wrong save. Before assuming a path bug:

```bash
readlink -f /opt/data/.hermes/home/ai-topics          # → /opt/data/ai-topics
diff /opt/data/ai-topics/wiki/raw/archived/triage/blog/<file> /opt/data/.hermes/home/ai-topics/wiki/raw/archived/triage/blog/<file> && echo "SAME FILE (symlink)"
```

If diff is clean, the archive is correctly saved at the canonical path. Do not rewrite or move the file.

## Other Working Patterns This Session

- **Same-day dedup**: log.md had raw-backlog-ingest ×3 and OpenAI-Apple enrichment for 08-05 but NO blog-wiki-ingest yet → fresh triage, no same-day blog dedup needed. Yesterday's `triage_latest.json` timestamp (08-04T10:35Z) confirmed stale.
- **Event-page staging gap**: `events/openai-apple-conflict-2026.md` was updated 08-05 for the Aug 3 rebuttal but lacked the Aug 4 preliminary-injunction stage — reading the event page's actual sections (not just log.md) surfaced the gap.
- **unsaved_articles handling**: llm 0.32 link-dup of blog-4 → skip (content covered by take); YouTube live → skip; Reuters paywall (topic covered by blog-8) → skip. All three got `body_excerpt: "（unsaved_articles — 抽出不可）"`.
- **Field completeness check after save**: `python3 -c` with hardcoded path to confirm every decision has `body_excerpt` + `reason_ja` and to print the take list.
- **Targeted commit**: repo had unrelated pre-existing changes (skill edits, hierarchy_report.json) → `git add <triage files> && git commit -- <paths>` to isolate the archive commit.
