# Weekly Graph Analysis — run notes 2026-11-13

Canonical procedure worked end-to-end with no deviations.

## log.md insertion point (supersedes pitfalls §16 marker)
Insert the new dated entry immediately after the `# Wiki Log` header line (not the stale `_Log of all wiki changes..._` line).

## Sibling-dirt git flow
git pull --rebase refuses on sibling config/ dirt. Path-scoped commit of only wiki files + push works WITHOUT stash unless push is rejected non-fast-forward; only then stash/rebase.

## WoW trend row (verified, deep audit)
2026-11-13: L2=3456, orphans=460, broken=2581, dup=17/0 merges, oversized=330, stale=2558, tags=0. Prior 11-06: 3404/457/2598/326/2491. Orphan growth 1:1 with page creation = stable graph.

## Dup ledger — same 17 groups recur; spot-check 2-3 then declare 0 merges
Redirect stubs: eugeneyan, giles-thomas, lilianweng, martin-fowler (bare redirect: field), samuelcolvin, alphaproof-nexus, deerflow, dspyrlm, llm-integration-patterns, open-claw-ecosystem.
Legit splits: cline, qwen, omnara, nvidia-openshell, agent-harnesses.
False positives: _index pair; deliberate-coder vs deliberatecoder (different people).

## Missing-page queue (persisted 2+ weeks, escalate if still open)
concepts/claude-opus-4-7, entities/cursor, entities/huggingface, entities/ben-clavie. Borderline hubs: enterprise-ai, ai-adoption, agent-architecture, agent-framework, ai-coding. 47 empty [[]] links mechanical.

## Minor
grep -mE1 errors on this build; use grep -E with head -1 in the dup loop.
