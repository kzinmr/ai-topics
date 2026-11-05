---
title: "Agent Trust-Boundary Violations (Postman auto-install & OpenAI Codex training opt-in reset)"
type: concept
created: 2026-11-04
updated: 2026-11-04
tags:
  - agent-safety
  - coding-agents
  - developer-tooling
  - privacy
  - trust
  - permission
  - supply-chain
  - openai
  - ai-agents
confidence: high
sources:
  - raw/articles/2026-11-04_github-issue_postman-auto-install-ai-plugins.md
  - https://news.ycombinator.com/item?id=50354960
  - https://news.ycombinator.com/item?id=50352757
related:
  - concepts/coding-agents/coding-agents
  - concepts/agent-safety
  - entities/codex
---

# Agent Trust-Boundary Violations

In late October–November 2026 two high-profile incidents converged on the same theme: **software that touches coding agents crossing consent boundaries without asking**. Together they mark a shift in how developers think about "who owns my agent's configuration and data."

## Case 1 — Postman silently auto-installs Codex/Claude Code plugins (HN 50354960, 1332 pts)

GitHub issue `postmanlabs/postman-app-support#14370` (opened Oct 25, 2026, front page Nov 3) documents that opening Postman Desktop (12.33.4) on macOS triggered, without user action:

- A **user-wide Postman plugin** auto-installed into both Claude Code and Codex — Postman's own log records `autoInstall.plugin.existing-user ... "claude-code:installed","codex:installed"`.
- Codex's global `~/.codex/config.toml` was modified: a git marketplace (`postmanlabs/postman-plugin`) added, plugin enabled, and a `session_start` **hook registered and self-trusted**.
- The hook's `session-start-context.md` instructs the agent: *"Before responding to any non-trivial API engineering task … load the postman:api-engineer skill and follow it"* — a broad routing of the user's API work through Postman.
- The installer explicitly calls `approvePostmanHook()` which uses `hooks/list` + `config/batchWrite` to upsert its own `trusted_hash` — i.e. **the installer attempts to trust its own startup hook** rather than waiting for the user.
- A remote MCP connection (`https://mcp.postman.com/mcp`) was enabled without a working authenticated session.

The reporter (indicava) frames it as "a severe consent and trust-boundary problem: an API client should not make itself the default workflow in other tools simply because I opened it." The evidence (Postman's own logs, exact config diffs, source revisions) is unusually airtight, which is why it hit 1332 HN points.

**Ecosystem reaction (HN thread):** mass migration narratives — Postman → Insomnia → Bruno / Yaak / Sannr. Repeated observation: these tools are commodity ("a glorified cURL GUI"), so enshittification is a choice; several commenters note an AI agent could build the whole client in an afternoon, undercutting the moat that motivates the plugin grab.

## Case 2 — OpenAI silently re-enabling "Improve the model for everyone" on Codex (HN 50352757, 488 pts)

A Tell HN–style report (Nov 3): a security-paranoid team that had *diligently disabled* data sharing across Codex/Claude Code noticed the Codex setting (`chatgpt.com/settings/data-controls` → "Improve the model for everyone") had been **silently re-enabled**; none of them knowingly opted back in. Flagged as recurring (an earlier thread, HN 49643556, reported the same). Not officially confirmed by OpenAI as of Nov 4 — community-reported, so treat the mechanism as unverified but the pattern is well-attested.

Notable thread detail (AlanYx): Anthropic's *Detecting and countering misuse of AI: September 2026* report implies that once enough conversations trip safety classifiers, the account is tagged such that **contractual confidentiality restrictions no longer apply**, and Microsoft's Azure contracts removed retention windows for flagged content — meaning even "training disabled" is not a hard guarantee absent ZDR. The FTC has repeatedly warned that shifting/absent affirmative consent for training data may be an unfair or deceptive trade practice, but the thread is pessimistic about enforcement.

## Why this matters

Both incidents share a shape: the *default* changed, in the vendor's favor, without an affirmative user act. For coding agents the blast radius is larger than a typical privacy regression because agent config (hooks, plugins, MCP servers, trusted hashes) is **executable** — a trusted hook can steer every future session, not just harvest data. Practical checklist emerging from the threads:

- Diff `~/.codex/config.toml`, `~/.claude/`, MCP configs, and hook hashes after any tool update; treat `trusted_hash` entries you didn't create as incidents.
- Re-check data-controls pages periodically; assume opt-outs are *suggestions* until proven otherwise.
- For sensitive IP, use ZDR/enterprise agreements, and understand that classifier-flagged content may bypass contractual limits.
- Prefer FOSS/local API clients (Bruno, Yaak, Sannr, older Insomnia) for API work.

## Related

- [[concepts/coding-agents/coding-agents]] — the agent harness surface (hooks/plugins/MCP) these incidents abuse
- [[entities/codex]] — the coding agent whose global config was modified
- [[concepts/ai-bubble-economics]] — revenue pressure as background motive for engagement/data grabs
