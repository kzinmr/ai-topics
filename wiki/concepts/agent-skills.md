---
title: "Agent Skills"
type: concept
created: 2026-04-25
updated: 2026-05-27
tags:
  - architecture
  - mcp
  - developer-tooling
  - claude-code
aliases:
  - Agent Skills open standard
sources:
  - raw/articles/2026-05-08_anthropic-engineering_equipping-agents-for-the-real-world-with-agent-skills.md
  - raw/articles/2026-05-18_browse-sh-browserbase_agent-skills-catalog.md
  - https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
related:
  - building-effective-agents
  - effective-harnesses-for-long-running-agents
  - mcp
  - claude-code-best-practices
---
# Agent Skills

An **open standard** published by Anthropic (December 18, 2025) for dynamically granting domain-specific expertise to agents.

> "Building a skill for an agent is like putting together an onboarding guide for a new hire."

## Core Concept

Skills = **directories** containing instructions, scripts, and resources. Agents dynamically discover and load them to improve performance on specific tasks.

## Structure

```
skill-name/
├── SKILL.md          # Required: YAML frontmatter + main instructions
├── references/       # Optional: additional reference files
├── scripts/          # Optional: executable code
└── templates/        # Optional: templates
```

### SKILL.md

```yaml
---
name: pdf
description: PDF document editing and form filling capabilities
---
# PDF Skill

Instructions for editing PDFs and filling forms...
```

## Progressive Disclosure — 3-Layer Design

| Level | Content | Context Consumption |
|-------|---------|-------------------|
| **L1** | `name` + `description` | Always (injected into system prompt) |
| **L2** | `SKILL.md` body | Only when relevant task detected (read via Bash tool) |
| **L3+** | Linked additional files | On demand (agent decides to read) |

**Design principle**: "Like a well-organized manual — table of contents → chapters → appendices, read only when needed."

## Code Execution

Skills can include executable code:
- Deterministic operations like sorting are more efficient as code execution than token generation
- PDF form field extraction scripts → Claude can execute without loading either the script or PDF into context
- Code is deterministic → consistency and reproducibility

## Development Guidelines

1. **Start with evaluation**: Identify the agent's weaknesses on representative tasks → build Skills incrementally from there
2. **Structure for scale**: When SKILL.md grows too large, split into files with references
3. **Separate mutually exclusive and infrequent contexts**: Reduce token usage
4. **Code serves as both executable tool and documentation**: Be clear about which role it should play

## Example: PDF Skill

The skill behind Claude's document editing capabilities:
- `SKILL.md` — Basic instructions for PDF operations
- `forms.md` — Form-filling specific instructions (read only during form filling)
- `fill_form.py` — Form field extraction and input script

## See Also

- [[entities/browse-sh]] — Browse.sh: 100+ curated browser skills catalog by Browserbase
- [[concepts/agent-skills-overview]] — Agent Skills concept cluster map (parent page)
- [[concepts/building-effective-agents]] — Building effective agents
- [[concepts/effective-harnesses-for-long-running-agents]] — Long-running agent harnesses
- [[concepts/mcp]] — Model Context Protocol
- [[concepts/claude-code-best-practices]] — Claude Code best practices
- [[agent-skills-skillmd]] — SKILL.md format details
