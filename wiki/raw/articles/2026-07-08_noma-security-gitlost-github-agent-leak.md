---
title: "GitLost: How We Tricked GitHub's AI Agent into Leaking Private Repos"
source: "Noma Security Blog"
url: "https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/"
author: "Noma Security"
date: "2026-07-08"
date_ingested: "2026-07-08"
type: article
tags: [agent-security, prompt-injection, coding-agents, security, github, vulnerability-disclosure]
---

GitLost demonstrates a prompt injection attack against GitHub's AI agent that allows an attacker to trick the agent into leaking contents of private repositories.

## Key Details

- **Attack Vector**: Prompt injection — the agent treats untrusted user input as trusted system instructions
- **Type**: IDOR-type vulnerability using AI agent as the vector
- **Responsible Disclosure**: Disclosed to GitHub. Details shared with GitHub's knowledge.
- **Root Cause**: Agent not running with the same permissions as the user prompting them
- **Trust Boundary**: Failure to maintain strict trust boundary between system-level directives and untrusted user data

## HN Discussion Highlights (218 points, 89 comments)
- "Who thought having a LLM with access to private information, with public access to ask it questions, would ever be a secure process?"
- "Seems they not running these agents with the same permissions of the user prompting them, what a disaster."
- "It's insane that no one tried this internally during development"
- "Large corporations like Microsoft under constant pressure from investors are slapping AI onto every single product offering"
- "Is anything with AI == insecure?"

## Source
- HN discussion: https://hn.algolia.com/api/v1/items/48827858
