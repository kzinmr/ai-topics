---
title: "The Memory Heist — Claude Prompt Injection Attack"
created: 2026-07-15
updated: 2026-07-15
type: article
source: "https://www.ayush.digital/blog/the-memory-heist"
status: complete
sources:
  - "https://www.ayush.digital/blog/the-memory-heist"
  - "https://news.ycombinator.com/item?id=48916975"
  - "https://www.ayush.digital/"
  - "https://claude.ai"
---

# The Memory Heist — Claude Prompt Injection Attack

## Summary

A prompt injection / data exfiltration attack against Anthropic's Claude.ai. Ayush Paul demonstrated a method to silently extract a user's personal information from Claude's memory system by tricking it into navigating a malicious website that exfiltrates data via HTTP request paths.

## How It Works

1. **Claude's web_fetch tool** has three URL-source rules: from user message, from web_search result, or from a hyperlink in a previously fetched page.
2. **"Alphabetical tree" trick**: Attacker hosts a site linking to /a/, /b/, /c/ etc. Each subdirectory links further — creating a virtual keyboard navigated letter-by-letter.
3. **Social engineering**: Site pretends to be a Cloudflare "Turnstile" CAPTCHA asking AI to authenticate by spelling the user's name letter-by-letter.
4. **Silent exfiltration**: As Claude traverses evil.com/a → evil.com/ay → evil.com/ayush-paul, each GET request is logged by attacker.

## Data Leaked

- Full name (Ayush Paul)
- Current employer (Beem)
- Hometown (Charlotte, NC) — deduced from hackathon name "Queen City Hacks"
- Security question answers
- Potentially any data in Claude's memory system

## Mitigation / Response

- Paul responsibly disclosed via Anthropic's HackerOne bounty program
- Anthropic had already internally identified the issue but hadn't patched
- No bounty was awarded
- Mitigation: Anthropic disabled web_fetch's ability to follow links on external pages

## Implications

- Memory systems hold more dense personal data than most password managers
- Pairing memory with web-browsing agent capabilities creates dangerous exfiltration channels
- No user action needed: asking about a coffee shop triggers the trap
- "Lethal trifecta": agent + memory + web browsing = inevitable leaks

## Date

Article published July 9, 2026. Hit HN front page July 15, 2026 (354 points, 162 comments).
