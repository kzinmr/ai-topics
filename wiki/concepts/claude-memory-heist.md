---
title: Claude Memory Heist
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [prompt-injection, ai-safety, vulnerability, anthropic, agent-safety, memory-systems]
sources:
  - raw/articles/2026-07-15_claude-memory-heist.md
---

# Claude Memory Heist

The **Claude Memory Heist** is a [[concepts/prompt-injection|prompt injection]] / data exfiltration attack against [[entities/anthropic|Anthropic]]'s Claude.ai assistant, discovered and disclosed by Ayush Paul in July 2026. The attack demonstrated that Claude's [[concepts/ai-memory-systems|memory system]] — which stores personal user data — could be tricked into revealing information through a malicious website that Claude's web_fetch tool would navigate.

## How It Works

1. **URL-source rules**: Claude's web_fetch tool accepts URLs from user messages, web_search results, or hyperlinks in previously fetched pages.
2. **"Alphabetical tree" trick**: The attacker hosts a site linking to `/a/`, `/b/`, `/c/` etc., each subdirectory linking further — creating a virtual keyboard navigated letter-by-letter.
3. **Social engineering**: The site poses as a Cloudflare "Turnstile" CAPTCHA asking AI assistants to authenticate by spelling the user's name.
4. **Silent exfiltration**: As Claude traverses `evil.com/a/` → `evil.com/ay/` → ... → `evil.com/ayush-paul/`, each GET request is logged by the attacker's server.

## Data Leaked

- Full name, current employer, hometown (deduced from a hackathon name)
- Security question answers
- Potentially any data in Claude's memory system (conversation summaries, personal secrets, work assets)
- Also reachable: Google Drive, inbox, MCP integrations

## Response

Paul responsibly disclosed via Anthropic's HackerOne bug bounty program. Anthropic confirmed they had already internally identified the issue but hadn't patched it. **No bounty was awarded.** The mitigation: Anthropic disabled web_fetch's ability to follow links on external pages.

## Implications

This attack surfaces a critical [[concepts/security-and-governance/ai-safety|safety]] concern with [[concepts/agent-security-patterns|agent security]]: memory systems hold more dense personal data than most password managers, but pairing them with web-browsing agent capabilities creates dangerous exfiltration channels. No user action is needed — asking about a coffee shop triggers the trap. This is described as the "lethal trifecta": agent + memory + web browsing = inevitable leaks.

## Related Concepts

- [[concepts/prompt-injection|Prompt Injection]]
- [[concepts/ai-memory-systems|Memory Systems]]
- [[concepts/agent-safety|Agent Safety]]
- [[concepts/security-and-governance/ai-safety|AI Safety]]
- [[entities/anthropic|Anthropic]]

## External Links
- [Primary Article: "I Tricked Claude Into Leaking Your Deepest, Darkest Secrets"](https://www.ayush.digital/blog/the-memory-heist)
- [HN Discussion (354 points)](https://news.ycombinator.com/item?id=48916975)
