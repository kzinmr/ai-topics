# Cross-Reference: Weekly AI Digest 2026-08-03

Worked example of the **weekly-ai-digest** cron run (Monday 00:00 UTC). Complements the daily cross-reference files by documenting weekly-mode specifics.

## Situation
- Analysis window: 2026-07-27 → 2026-08-03 (7 days). 88 wiki commits in window, 2,877 total pages (871 entities / 1,945 concepts / 35 comparisons / 22 events per 7/31 graph analysis).
- **Previous weekly digest was 2026-07-13** — NOT last Monday. The 07-20 and 07-27 weekly runs left no files. Dedupe anchor used: daily `inbox/rss-scans/trending-topics-2026-08-02.md` (covers 7/31→8/2) + `git log --since=2026-07-27`. Format template: the 07-13 weekly digest file.
- `hermes-report-quality` was listed for the job but loader said "could not be found and were skipped" — root cause is the **dual-path collision** (exists in both `.hermes/skills/wiki-daily-report/` and `_overrides/wiki-daily-report/` at the same categorized path), not a missing skill. Non-blocking: T1-T5 live in trending-topics-reporting Weekly Digest Mode.

## Topic selection (7 topics, all ★★★☆☆+)
1. 🏛️ Open-weight policy war (3 open letters: 235 orgs vs Anthropic vs 1,324 employees) ★★★★★ — multi-party governance open-letter cluster rule applied
2. ⚡ Price war final stage (Luna 80% cut → DeepSeek V4-Flash-0731 answered in a day) ★★★★★ — coordinated overnight-response chain
3. 📉 Enterprise AI disillusionment ("0% success" Hermit Tech essay, HN 469pts) ★★★★☆
4. 🧪 Benchmark distrust (The Duel That Never Happened + Anthropic 3 cyber-eval incidents) ★★★★☆ — evals at 42 sources/week
5. 🦙 Kimi K3 open weights + DeepSWE (2.8T MoE, 1.56TB HF release 7/27, 1-bit 594GB) ★★★★☆
6. 🔌 MCP 2026-07-28 official spec (stateless core, OAuth2/OIDC) ★★★★☆
7. 🛠️ Agent infra org-scale (qm HN 655pts, Sierra×Plaid, session portability) ★★★☆☆

Company concentration note added: OpenAI in 3/7 topics, but each topic's tension axis is a rival (DeepSeek/Anthropic/Moonshot), so topics kept independent.

## Errors caught & corrected
- **MCP RC date**: draft said "RC段階（2026-06-11）" from inference → grep of `concepts/model-context-protocol-mcp.md` showed stateless RC was "since May 2026". Fixed with `patch`. → New pitfall: verify inferred dates against wiki pages.
- No slop tokens survived the T1 grep scan (画期的/革新的/注目すべき/〜でしょう/ではないでしょうか/一方で/さらに、/しかしながら/高い性能を誇る/急速に進化 → NO_SLOP_FOUND).

## Wiki-link verification
All 30+ wikilink targets batch-checked on disk before writing (`[ -f "wiki/$f.md" ]`). Caught that `concepts/stateless-mcp-tooling.md` does NOT exist — used `concepts/mcp-2026-07-28-spec.md` + `concepts/model-context-protocol-mcp.md` instead. Both `concepts/mcp.md` and `concepts/model-context-protocol-mcp.md` exist; log entries reference the latter.

## Deliverable
- Saved: `inbox/rss-scans/weekly-ai-digest-2026-08-03.md` (179 lines)
- Committed + pushed: `72bd4146` "wiki: weekly AI digest 2026-08-03 — price war, open-weight letters, benchmark distrust"
- No log.md entry written (matches 07-13 precedent — digest lives in inbox/, not wiki/).
