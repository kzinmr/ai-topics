# Weekly Graph Analysis — run notes 2026-11-27

Canonical procedure worked end-to-end (report → adjudicate → annotations → index/log swap → path-scoped commit → push). No sibling dirt in wiki/ this run.

## WoW trend row (verified)
2026-11-27: L2=3541, orphans=493, broken(raw)=3574, dup=17/0 merges, oversized=335, stale=2566, tags=0. Prior 11-13: 3456/460/2581/330/2558. Broken-link jump 2581→3574 is generator counting inflation (bare+namespaced double-bucket, no nested resolution), NOT a regression — don't alarm the user.

## Dup ledger — still the SAME 17 groups (stable since 11-13)
All verdicts re-confirmed by wc -l + redirect grep loop (one terminal call). Redirect stubs confirmed thin (11-45L). deliberate-coder/deliberatecoder false positive re-confirmed.

## NEW findings this run
- Empty `[[]]` link backlog DRAINED 278→1 (only log.md itself). The standing "needs human review (1)" watchdog item can be closed by wiki-watchdog-fix.
- Real index gaps = 2 dir-hubs with content but no index.md: `concepts/browser-agent/`, `concepts/training/`. Recommend creating hub index pages.
- `concepts/gpt/_archive/` still linked from index.md (cosmetic).
- Not-indexed count 17 → 0 real via loose-basename resolver.

## Missing-page queue (4+ weeks, ESCALATED)
entities/cursor (14 refs), concepts/claude-opus-4-7 (10), concepts/intelligence-explosion (8, zero resolvable targets), entities/huggingface, entities/ben-clavie. Borderline hubs (no action, child pages cover): enterprise-ai, ai-adoption, agent-architecture, agent-framework, ai-coding, inference-optimization, world-models, ai-governance, agent-evaluation.

## Minor
- `grep -c "$(basename $2)"` loop for cross-link verification between dup-split pairs works well (cline/qwen/omnara/agent-harnesses all mutual).
- Pre-commit passed cleanly with `tags: [wiki]` on annotations page (as expected).
