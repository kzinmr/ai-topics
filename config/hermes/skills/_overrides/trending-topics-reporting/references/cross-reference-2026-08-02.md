# Cross-Reference 2026-08-02 — Third no-active-crawl day, governance open-letter cluster, price-war cascade

Worked example from the 2026-08-02 trending-topics run. Extends the volume-based-skip amendment (2026-07-31) and the newsletter subject-line validation pattern (2026-08-01).

## Run overview

- **active-crawl note**: ABSENT for the **3rd consecutive day** (7/31, 8/1, 8/2). Both `*trending-topics-research*` patterns and the cron-HOME fallback checked. Volume-based skip is now the stable default: blogwatcher DB yielded 134 articles / 115 raw articles in the 3-day window with ≥20 AI-relevant hits and clear event clusters.
- **HN discovery sweep**: skipped; ran **8 targeted HN Algolia point-score queries** only (curl-to-file, separate parse step per the curl-pipe pitfall).
- **Yesterday's report read first** (8/1): dropped DeepSeek-V4-Flash-0731, OpenAI math, Stateless MCP, Zitron economics, distillation-censorship, Sierra×Plaid, worktree isolation — all covered 8/1.

## Point-score calibrations (★ ratings)

| Story | Pts/comments | Rating decision |
|---|---|---|
| Pacing the Frontier (open letter, 1,324 signatories) | 149/204 | ★★★★★ — topic #1, both sides substantive |
| Open Weights and American AI Leadership (letter itself) | 112/2 | supporting source for #1 |
| AI Mania Is Eviscerating Global Decisionmaking (Suresh, via Doctorow) | 469/297 | ★★★★☆ — enterprise disillusionment |
| qm multiplayer agent harness | 655/155 | ★★★★☆ — HN validation matched 3.4K★ repo |
| Manifest LLM router deprecation | 130/85 | ★★★☆☆ — anti-routing counter-narrative |
| Martin Alderson speed-vs-intelligence essay | 1/0 | ★★★☆☆ analytical-merit-only (3-source cluster: essay + GLM5.2 pricing + price-war context) |

## New pattern: multi-party governance open-letter cluster

Three open letters from opposing camps within 5 days on the same policy question (open weights regulation):
1. **"Open Weights and American AI Leadership"** (7/24, Microsoft-shepherded, 235 companies: NVIDIA, Amazon, YC, Linux Foundation, later OpenAI) — pro-open-weights, defends distillation as legitimate technique
2. **Anthropic "Our position on open-weights models"** (7/27) — Amodei: authoritarian-misuse risk, calls for crackdown on industrial-scale distillation
3. **"Pacing the Frontier"** (7/28, 1,324 frontier-AI employees: Pachocki, Sutskever, Amodei, Jack Clark) — request US support for international pacing of automated AI development

**Treatment: ONE topic, not 3.** The debate itself is the story. Anchor = Simon Willison's 8/2 synthesis "Open letters about AI development". Related same-window framework (Thinking Machines Lab "A Safe Path to Open Weights", 7/31) folded in as supporting source. ★★★★★ because both sides have heavyweight signatories and the question is live (Fable 5 regulation context). Contrast with product launches — separate letters about different questions stay separate topics.

## Theme chain: price-war cascade (cost → speed → router deprecation)

- 7/30: OpenAI GPT-5.6 Luna price cut (80% on some variants)
- 7/31: DeepSeek-V4-Flash-0731 overnight reply (topic #1 yesterday)
- 8/2: Martin Alderson "picking models on speed now, not intelligence" — GLM5.2 at $0.42/$1.32/MTok (5% of Opus), 100-200tok/s as the new "instant"
- 7/31: Manifest "we deprecated our LLM router" — single battle-tested model beats routing complexity

**Treatment**: 3 separate ★★★☆☆ topics (speed-first selection, router deprecation) + noted as a chain in the 注目パターン section. The price war's *derivative effects* (speed as selection criterion, end of router economics) are distinct enough to report independently, but cross-link them.

## ✅ DONE detection: `log.md` tail complements frontmatter checks

- 2026-08-01 dreaming-ingest log entry listed "Key coverage verified": Manifest router → `concepts/coding-agents/model-routing.md` section; qm → `concepts/coding-agents/qm-multiplayer-agent-harness.md` — both ALREADY ingested by blog-wiki-ingest.
- **Technique**: `tail -30 wiki/log.md` catches pipeline coverage that frontmatter `updated:` dates alone miss (dreaming and blog-wiki-ingest logs enumerate what was page-ized). Check BOTH before recommending "create/update" — marks 2 of 7 actions ✅ DONE this run.

## Newsletter subject-line validation (3rd use)

- "The Duel That Never Happened" (Superintelligence, beehiiv digest) → benchmark-controversy topic (#6). Paywalled; all URLs obfuscated redirects. Reported as weak signal with explicit caveat 「本文はペイウォールのため要旨はサブジェクトライン＋サマリーからの推定」.
- Corroborated by evals 27-source count in trending_topics.py output — subject-line + frequency both pointing at the same theme = keep.

## Other notes

- Future-dated article (Sierra Plaid dated 8/3) appeared in DB range query again — already covered by the 8/1 reference; verified live via existing raw article, did not drop.
- EU AI Act compliance wave (Cohere transparency-code signing + OpenAI EU post) = ★★★☆☆ governance topic, paired with the US open-letter debate as the transatlantic contrast in 注目パターン.
