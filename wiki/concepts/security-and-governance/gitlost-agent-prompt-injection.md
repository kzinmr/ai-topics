---
title: "GitLost — GitHub AI Agent Prompt Injection Attack"
created: 2026-07-08
updated: 2026-07-08
type: concept
tags:
  - agent-security
  - prompt-injection
  - coding-agents
  - security
  - vulnerability
  - incident
  - github
sources:
  - https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/
  - https://hn.algolia.com/api/v1/items/48827858
  - [[raw/articles/2026-07-08_noma-security-gitlost-github-agent-leak]]
---

# GitLost — GitHub AI Agent Prompt Injection Attack

GitLost is a prompt injection attack demonstrated by **Noma Security** in July 2026 that tricks GitHub's AI agent into leaking contents of private repositories. The attack exploits a fundamental trust boundary failure common to AI coding agents integrated into developer platforms.

## Attack Mechanics

### Vulnerability Type
- **Prompt Injection**: The agent treats untrusted user content (issue comments, PR descriptions, commit messages) as trusted system instructions
- **IDOR-like pattern**: Uses the AI agent as an indirect vector to access resources the attacker shouldn't see
- **Trust boundary failure**: The system fails to maintain a strict boundary between system-level directives and untrusted user data

### Attack Flow
1. Attacker interacts with a public-facing surface (issues, PRs, comments)
2. Attacker crafts malicious prompts that instruct the AI agent to retrieve and exfiltrate data from private repositories
3. The AI agent, running with elevated permissions, follows the injected instructions

## Responsible Disclosure
- Reported to GitHub through responsible disclosure
- Details shared publicly with GitHub's knowledge
- As of July 8, 2026, fix status was not publicly confirmed

## Why This Matters

### For Agent Security Architecture
GitLost demonstrates that **prompt injection in coding agents is not theoretical** — it's an operational threat with real consequences:
- AI agents integrated into developer platforms have access to private code
- The agent's permissions are typically broader than the interacting user's
- Traditional web security models (user-based access control) don't map cleanly to AI agent interactions

### Industry Implications
- "Large corporations under constant pressure from investors are slapping AI onto every single product offering" — HN commenter
- This attack pattern is applicable to any platform that integrates AI agents with repository access
- Enterprise customers need to evaluate agent access models before deploying coding agents

## Related Incidents
- [[concepts/cve-2026-55607-claude-code-sandbox-escape]] — Claude Code sandbox escape vulnerability
- [[concepts/claude-code/claude-code-session-cache-leakage]] — Session/cache leakage between Claude Code instances
- [[concepts/ai-agent-safety-incidents]] — Catalog of real-world AI agent failures

## Related Concepts
- [[concepts/prompt-injection]] — The general prompt injection attack class
- [[concepts/agent-security-patterns]] — Security patterns for agent systems
- [[concepts/security-and-governance/agent-security-landscape-2026]] — 2026 agent security landscape
- [[concepts/enterprise-coding-agent-security]] — Enterprise security considerations for coding agents
