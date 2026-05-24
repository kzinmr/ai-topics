# Google Gemini CLI: Open-Source Community Built It, Then Google Closed It

**Source:** [TechTimes](https://www.techtimes.com/articles/317056/20260523/google-accepted-6000-gemini-cli-contributions-then-closed-tool-enterprise-only.htm) | **Date:** May 19, 2026

## Overview
Google accepted 6,000+ merged pull requests from hundreds of independent developers on the open-source Gemini CLI (TypeScript, Apache 2.0) over nearly a year. On May 19, 2026, at Google I/O, the company announced it would withdraw API access for all free and individual paying users, handing the tool exclusively to enterprise customers.

## Key Facts
- **Stars:** 100,000+ GitHub stars
- **PRs:** 6,000+ merged external contributions
- **Deadline:** June 18, 2026 — free users lose API access
- **Who keeps access:** Enterprise customers with paid Gemini Code Assist Standard/Enterprise
- **License:** Apache 2.0 remains, but infrastructure (API, model quotas, auth, backend) is withdrawn

## The Licensing Trap
- Gemini CLI code remains open-source, but API access does not
- Without Google's backend, the repo is effectively an archive
- Running a fork requires independent LLM access — a non-trivial engineering burden

## Antigravity CLI (replacement)
- Closed-source, Go-based, announced at Google I/O 2026
- Binary not on npm/Homebrew as of May 21
- Admitted: "won't have 1:1 feature parity right out of the gate"
- Weekly quotas (vs daily), users hitting limit within ~2,000 lines of generated code
- Enterprise customers keep both Gemini CLI and Antigravity CLI

## Community Reaction
- Labeled "bait and switch": open-source to attract free labor, enterprise captures value
- Launch partners (Dynatrace, Elastic, Figma, Shopify, Stripe) face 4-week disruption
- Developers evaluating alternatives: Claude Code, GitHub Copilot CLI, open-source tools
