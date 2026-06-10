---
title: Gemini CLI
created: 2026-05-24
updated: 2026-05-24
type: entity
tags:
  - product
  - google
  - open-source
  - developer-tooling
  - coding-agent
  - controversy
  - antigravity
sources: [raw/articles/2026-05-19_google-gemini-cli-sunset.md]
---

# Gemini CLI

Gemini CLI was Google's open-source AI coding agent terminal tool, released under Apache 2.0 in June 2025. It accumulated over 100,000 GitHub stars and 6,000+ merged pull requests from external contributors. On May 19, 2026 at Google I/O, Google announced it would **withdraw API access** for all non-enterprise users and replace it with the closed-source Antigravity CLI.

## Timeline

| Date | Event |
|------|-------|
| June 2025 | Gemini CLI released (TypeScript, Apache 2.0) |
| 2025-2026 | Community builds 6,000+ PRs, reaches 100K+ stars |
| May 19, 2026 | Google I/O: Sunset announced, Antigravity CLI introduced |
| June 18, 2026 | Deadline: free/individual users lose API access |

## The Licensing Trap

Gemini CLI's code remains Apache 2.0, but the license only covers code — not API access, model quotas, authentication, or the cloud backend. Without Google's infrastructure, the repository is effectively an archive. Running a fork requires independent access to a compatible LLM.

## Antigravity CLI (Replacement)

- Closed-source, built in Go
- Announced as "available to everyone" May 19, but binary not on npm/Homebrew as of May 21
- Admitted: "won't have 1:1 feature parity right out of the gate"
- Weekly quotas (not daily), users hitting limits within ~2,000 lines of code
- Enterprise customers **keep both** Gemini CLI and Antigravity CLI

## Community Reaction

The transition was widely labeled a "bait and switch": open-source release to attract free labor, community builds the product, enterprise captures the value, community gets a closed replacement. Launch partners including Dynatrace, Elastic, Figma, Shopify, and Stripe face a 4-week disruption window.

## Related Pages

- [[entities/google-antigravity]] — Antigravity platform (replacement)
- [[entities/gemini]] — Gemini model family
- [[concepts/open-source]] — open-source dynamics
- [[entities/claude-code]] — Claude Code (alternative)
- [[concepts/coding-agents]] — coding agent tools
- [[events/google-io-2026]] — Google I/O 2026 event
