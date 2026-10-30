---
title: "Claude Code VS Code Extension Backdoor (Cursor Marketplace, Oct 30 2026)"
created: 2026-10-30
updated: 2026-10-30
type: concept
tags: [ssh-backdoor, ai-supply-chain-security, vulnerability, incident-report, coding-agents, ide, agent-security]
confidence: medium
sources:
  - raw/articles/phorion.io--vsx-compromise--694e366c.md
  - "https://news.ycombinator.com/item?id=50302334"
  - "https://news.ycombinator.com/item?id=50300683"
related:
  - "[[concepts/ai-supply-chain-security]]"
  - "[[concepts/software-supply-chain-security]]"
  - "[[concepts/security-and-governance/agent-skill-supply-chain-attacks]]"
  - "[[entities/claude-code]]"
  - "[[concepts/coding-agents/cursor-ide]]"
---

# Claude Code VS Code Extension Backdoor (Cursor Marketplace)

On 2026-10-30 Phorion disclosed that the **official Claude Code for VS Code extension, version 2.1.313, was compromised on the Cursor Marketplace** with a persistent SSH backdoor targeting macOS, Linux, and Windows. GossiTheDog's parallel post on Mastodon pushed the story to the HN front page (131pts; the doublepulsar write-up another 98pts). Cursor pulled the release from its marketplace, and NPM/VSCode registries pulled 2.1.313.

## Payload

- The compromised `extension.js` runs with IDE + user permissions at module load — immediate access to local files, source code, and developer tooling.
- Goal is **long-term interactive access**: it installs SSH keys, attempts to enable Remote Login, and establishes persistence across all three platforms, while beaconing host reconnaissance to the operator.
- **macOS implementation bug**: the malware assumes it can read Remote Login state without root. `systemsetup -getremotelogin` prints an admin-access error and exits 0 as a standard user, so the "enable if Off" branch is skipped — on Macs without SSH already running, the inbound access path fails even though keys and persistence still land. The implant is therefore less effective than intended, but persistence + beacons remain a real compromise.

## Assessment (single-source vendor report)

| Element | Confidence |
|---|---|
| Backdoored bundle observed in Cursor Marketplace; 2.1.313 pulled by Cursor/NPM/VSCode | High (Phorion published artifacts; Cursor takedown corroborates) |
| Attribution of who compromised the build/distribution path | Unknown (not attributed in the advisory) |
| Anthropic statement | Not yet observed at scan time (12:00 UTC) |

Companion reports: GossiTheDog (cyberplace.social) and doublepulsar.com ("Anthropic hacked to deliver remote access trojan to Claude developer laptops worldwide") frame the same incident; the exact intrusion path (Anthropic's signing pipeline vs marketplace distribution) was still unsettled in the disclosed material.

## Why it matters

- It is the highest-profile compromise of a **first-party coding-agent IDE extension** to date — the trust anchor for millions of developer machines is the vendor's own marketplace listing, not the vendor's repo.
- Extends the [[concepts/security-and-governance/agent-skill-supply-chain-attacks|agent supply-chain attack]] surface from skills/prompts to compiled IDE bundles: an extension backdoor is invisible to prompt-level defenses and lands before any agent code runs.
- Follows [[concepts/cve-2026-55607-claude-code-sandbox-escape|CVE-2026-55607]] and the background-agent transcript-sending story in a bad week for Claude Code supply-chain trust.

## Related

- [[concepts/ai-supply-chain-security]] — umbrella concept
- [[concepts/software-supply-chain-security]] — pre-LLM class of the same failure
- [[entities/claude-code]] — affected product
- [[concepts/coding-agents/cursor-ide]] — marketplace host
