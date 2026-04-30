---
title: Markdown-Based Skills
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [ai-agents, coding-agents, harness-engineering]
sources: [raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md]
---

# Markdown-Based Skills

## Definition

**Markdown-Based Skills** is an agent capability pattern where skills (instructions, methodologies, workflows) are defined in `.md` files with YAML frontmatter, rather than hard-coded logic. This allows non-engineers (analysts, domain experts) to encode and update agent behavior without writing code.

## Fintool Implementation

Skills are stored as `.md` files with structured frontmatter:

```yaml
---
name: dcf-valuation
domain: financial-analysis
version: 2.1
priority: public
---
```

### Shadowing Hierarchy

Skills follow an override pattern based on file location:

```
private/  → User-specific overrides (highest priority)
shared/   → Team-shared customizations
public/   → System defaults (lowest priority)
```

Users can override any default skill by dropping a file in their `/private/` folder — similar to how `.gitconfig` overrides system defaults.

### Discovery Pattern

- Uses SQL-based discovery for "lazy loading"
- Avoids burning tokens by not injecting every skill into every prompt
- Only loads relevant skills based on context analysis

## Key Insight: Designing for Obsolescence

> "The Model Will Eat Your Scaffolding."

As base LLM reasoning improves, complex prompt scaffolding becomes unnecessary. Skills should be designed to be:
- **Easily updated** — just edit the `.md` file
- **Easily deleted** — remove when the model handles it natively
- **Versioned** — track which skills are still needed vs. obsolete

## Comparison to Other Skill Systems

| System | Format | Authoring |
|--------|--------|-----------|
| Fintool Skills | `.md` + YAML frontmatter | Non-engineers (analysts) |
| Hermes Agent | `SKILL.md` bundles | Engineers, AI agents |
| Anthropic Agent SDK | Tool definitions | Engineers |
| OpenClaw | Config files | Engineers |

## Related Concepts

- [[agent-skills]] — broader concept of agent skill management
- [[harness-engineering/system-architecture/agent-skills]] — Anthropic's SKILL.md pattern
- [[s3-first-architecture]] — skills stored as files in S3

## Sources

- Nicolas Bustamante (Fintool), "Lessons from Building AI Agents for Financial Services", LinkedIn, April 2026
