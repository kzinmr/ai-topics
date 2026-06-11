---
title: "Agent Skills"
type: concept
created: 2026-04-25
updated: 2026-06-02
tags:
  - architecture
  - mcp
  - developer-tooling
  - claude-code
  - coding-agents
  - openai
  - evaluation
  - harness-engineering
  - ci-cd
aliases:
  - Agent Skills open standard
sources:
  - raw/articles/2026-05-08_anthropic-engineering_equipping-agents-for-the-real-world-with-agent-skills.md
  - raw/articles/2026-05-18_browse-sh-browserbase_agent-skills-catalog.md
  - https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
  - raw/articles/2026-03-09_openai-developers-blog_skills-agents-sdk.md
  - raw/articles/2026-02-11_openai-developers-blog_skills-shell-tips.md
  - raw/articles/2026-01-24_openai-developers-blog_eval-skills.md
related:
  - building-effective-agents
  - effective-harnesses-for-long-running-agents
  - mcp
  - claude-code-best-practices
  - codex
  - evals-for-ai-agents
  - harness-engineering
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

## OpenAI Codex Skills Implementation

OpenAI implements skills in [[codex]] using the same open standard, with an emphasis on repo-local workflows, mandatory routing via `AGENTS.md`, and CI automation through GitHub Actions.

### Repo-Local Skills + AGENTS.md

Skills live in `.agents/skills/` (repo-scoped) or `~/.codex/skills/` (user-scoped). `AGENTS.md` acts as a policy layer with if/then rules that mandate skill usage at the right time:

```
## Mandatory skill usage
- Use $implementation-strategy before editing runtime or API changes.
- Run $code-change-verification when code, tests, or build behavior changes.
- Use $pr-draft-summary when work is ready for review.
```

### Skills as Container-Mounted Instructions

Skills are reusable, versioned instruction bundles mounted into hosted shell containers. The platform exposes each skill's `name`, `description`, and `path` to the model for routing. The model loads the full `SKILL.md` body and scripts only when the skill is selected -- the same [[concepts/agent-skills|progressive disclosure model]] as the open standard. Server-side [[concepts/context-engineering/context-management|compaction]] keeps long-running skill workflows coherent without manual context management.

### OSS Maintenance Case Study

OpenAI uses Codex with skills to maintain the Agents SDK repos (Python + TypeScript). Key skills include `code-change-verification`, `docs-sync`, `final-release-review`, and `pr-draft-summary`. Results: **457 PRs merged in 3 months** (Dec 2025 -- Feb 2026), up from 316 in the prior 3 months. Skills encode the repo's definition of "verified" (format, lint, typecheck, tests), and `AGENTS.md` makes that definition enforceable.

### Systematic Eval Methodology

OpenAI recommends evaluating skills with the same rigor as any prompt. The methodology from their [[evals-for-ai-agents|evals framework]]:

1. **Define success** -- outcome goals, process goals, style goals, efficiency goals
2. **Create targeted prompts** -- 10-20 prompts covering explicit invocation, implicit invocation, and negative controls (`should_trigger=false`)
3. **Deterministic graders** -- use `codex exec --json` to capture structured traces; check for expected commands, file artifacts, and ordering
4. **Rubric-based grading** -- use `--output-schema` for structured qualitative checks (component structure, style conventions)

Glean reported that a Salesforce-oriented skill increased eval accuracy from 73% to 85% and reduced time-to-first-token by 18.1% after applying negative examples and edge-case coverage in descriptions.

### Comparison: Anthropic vs OpenAI Skill Patterns

| Dimension | Anthropic (Claude Code) | OpenAI (Codex) |
|-----------|------------------------|----------------|
| **Location** | User or project `.claude/skills/` | Repo `.agents/skills/` or user `~/.codex/skills/` |
| **Routing** | Agent reads L1 metadata, decides to load | `AGENTS.md` mandates skill triggers; `description` is routing metadata |
| **CI integration** | External harness orchestration | Codex GitHub Action (same skill, same logic) |
| **Eval emphasis** | Community-driven (Hamel Husain skepticism) | Systematic eval methodology with deterministic + rubric grading |
| **Context management** | Progressive disclosure (L1/L2/L3) | Progressive disclosure + server-side compaction |
| **Community focus** | Skills as decompressed prompts; audit before use | Skills as versioned playbooks; enforce via AGENTS.md |

Both implementations are converging on the same [[concepts/agent-skills|open standard]]: skills are directories with `SKILL.md` manifests, progressive disclosure from metadata to full instructions, and executable scripts for deterministic operations.

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
- [[codex]] — OpenAI Codex
- [[evals-for-ai-agents]] — Evals for AI agents
- [[harness-engineering]] — Harness engineering

## Skills Ecosystem: Practitioner Perspectives

### The Skeptical View (Hamel Husain)

[[entities/hamel-husain]], creator of the `superpowers` skills framework and one of the most influential figures in the skills ecosystem, brought radical skepticism to Show Us Your (Agent) Skills Ep. 4:

- **A third of the top 300 skills have exactly one commit** — most published skills are abandonware, created once and never maintained
- **Skills are decompressed prompts** — \"Always read the prompt.\" Skills don't add magic; they're structured context that the agent decompresses at runtime
- **\"Fuck Your Skills\"** — be skeptical even of Hamel's own published skills. Every skill should be audited before use
- **Killed his own eval skill for an MCP** — MCP provides a more structured, testable interface than skill files for evaluation tasks

### The Security Nightmare

Both [[entities/matthew-honnibal]] and [[entities/hamel-husain]] independently identified a critical vulnerability:

- **Hidden HTML in `.md` skill files** can smuggle instructions to the agent. Honnibal ships skills as raw `.md.txt` files specifically to prevent browser rendering that could embed malicious directives
- The **skill supply chain** is a massive unexamined attack surface — anyone can publish a skill that injects hidden instructions
- [[entities/eleanor-berger]]'s \"lethal trifecta\" response: cut your agent's internet access to prevent hallucinated URLs, scraping attacks, and unintentional data exfiltration

### Skills as Capabilities (AMP)

[[entities/nico-gerold]] at AMP treats skills as domain-specific **capabilities**, not generic prompts:

- **gcloud skill** — pulls the right logs from production
- **tmux skill** — spins up dev builds and reproduces bugs autonomously
- **postmortem skill** — agent introspects on why it went wrong, building institutional knowledge

### Self-Updating Skills

[[entities/bryan-bischof]] demonstrated the meta-skill pattern: skills that tell the agent to update itself. The agent reads its own eval failures and rewrites the skill to prevent recurrence.

### Skills vs. Composable Libraries

[[entities/vincent-warmerdam]] (marimo) argues that **composable widget libraries beat skill files** for UI/visualization tasks. \"Wiggly Stuff\" widgets are Lego bricks — the agent composes them rather than following procedural instructions.
