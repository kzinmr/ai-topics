---
title: Claude System Prompts
type: concept
created: 2026-08-17
updated: 2026-08-17
tags:
  - claude
  - system-prompt
  - transparency
  - ai-transparency
  - prompting
related:
  - "[[entities/anthropic]]"
  - "[[concepts/prompt-design]]"
  - "[[concepts/claude-code/claude-code-steering-methods]]"
sources:
  - https://platform.claude.com/docs/en/release-notes/system-prompts
  - https://news.ycombinator.com/item?id=49319556
---
# Claude System Prompts

Anthropic publishes **release notes for the core system prompts** used by claude.ai and the Claude iOS/Android apps (HN 687pts, 2026-08-17). The system prompt provides up-to-date information to the model — such as the current date and user location — and Anthropic now documents how these prompts evolve over time.

## Significance

- **Transparency milestone**: Anthropic is one of the first frontier labs to maintain public release notes for production system prompts, letting users and researchers see exactly what instructions Claude receives on the consumer surfaces.
- **Prompt engineering as public artifact**: The release notes turn the system prompt into a versioned, observable artifact — useful for [[concepts/prompt-design]] practitioners and for auditing model steering/behavior changes.
- **Distinct from Claude Code steering**: These are the web/mobile app system prompts, not the [[concepts/claude-code/claude-code-steering-methods|Claude Code CLAUDE.md/rules/skills]] mechanism. The docs page links from the Claude Platform Docs "System Prompts" section under Models & pricing.

## Related

- [[concepts/prompt-design]] — broader prompt engineering landscape
- [[entities/anthropic]] — company page
- [[concepts/claude-code/claude-code-steering-methods]] — enterprise steering (CLAUDE.md, skills) for Claude Code

## Sources

- [Claude Platform Docs — System Prompts release notes](https://platform.claude.com/docs/en/release-notes/system-prompts)
- [HN discussion (688pts)](https://news.ycombinator.com/item?id=49319556)
