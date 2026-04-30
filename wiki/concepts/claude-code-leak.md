---
title: "Claude Code Source Leak"
type: concept
created: 2026-04-10
updated: 2026-04-10
tags: [concept, security, leak, anthropic, claude]
related: [ai-security, open-source, anthropic]
sources: []
---

# Claude Code Source Leak

March 2026 incident where Anthropic's Claude Code source code was leaked via npm package.

## Incident Details

### Leak Vector
- Malicious npm package `plain-crypto-js`
- Versions 1.14.1 & 0.30.4 compromised
- Likely from leaked npm token
- Credential theft and RAT (Remote Access Trojan) capabilities

### Impact
- Full Claude Code source code exposed
- Security implications for Anthropic's tooling
- Community analysis of internal implementation

### Detection & Mitigation
- Malware published without accompanying GitHub releases
- Trusted publishing recommended as mitigation
- Heuristic: check for GitHub repo association

### Community Response
- Rapid analysis by security researchers
- Discussion of supply chain security in AI tooling
- Increased scrutiny of npm ecosystem

## Broader Implications
- Highlights AI tooling supply chain vulnerabilities
- Demonstrates need for trusted publishing workflows
- Raises questions about proprietary vs open AI development

## Sources
- kuber.studio--blog-ai-claude-code-s-entire-source-code-got-leaked-via-a-so--871ffae3.md
- the-register--2026-03-31-anthropic-claude-code-source-code--ba8c2ae1.md
- github.com--disler-pi-vs-claude-code-comparison.md
