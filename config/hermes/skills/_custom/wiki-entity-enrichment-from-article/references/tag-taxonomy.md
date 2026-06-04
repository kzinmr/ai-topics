# Tag Taxonomy — Pre-Commit Validation

The `wiki/SCHEMA.md` defines ~375 canonical tags. The git pre-commit hook at `config/.githooks/pre-commit` enforces that every tag in every wiki frontmatter block appears in SCHEMA.md. Non-canonical tags **block the commit entirely**.

## Pre-Write Checklist

Before writing any frontmatter `tags:` block:

```bash
# Verify each intended tag exists in SCHEMA.md
grep -F "prompting" /opt/data/wiki/SCHEMA.md
grep -F "token-efficiency" /opt/data/wiki/SCHEMA.md
```

## Common Non-Canonical → Canonical Mappings

Tags that sound reasonable but aren't in SCHEMA.md:

| You wrote | Canonical SCHEMA tag | SCHEMA Category |
|-----------|---------------------|-----------------|
| `prompt-engineering` | `prompting` | Techniques |
| `token-efficiency` | *(none — drop it)* | — |
| `claude` | `anthropic` | People/Orgs |
| `multi-agent-system` | `multi-agent` | AI Agents |
| `agentic-workflow` | `ai-agents` + `agent-architecture` | AI Agents |
| `llm-evaluation` | `evaluation` | Techniques |
| `deep-research-agent` | `deep-research` | AI Agents |

## What Happens on Violation

```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED

⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (3):
   wiki/concepts/example.md:  prompt-engineering
   wiki/concepts/example.md:  token-efficiency
   wiki/concepts/example.md:  claude

   Fix options:
   1. Add 'prompt-engineering' to SCHEMA.md taxonomy
   2. Map it to an existing canonical tag
   3. Use an existing SCHEMA tag instead
```

## Recovery

1. Edit the frontmatter to use canonical tags
2. `git add` the fixed files
3. Retry the commit — it will re-validate and pass

If a genuinely new category is needed, add it to SCHEMA.md first (under the correct category section), then use it.

## How to Avoid

The easiest way: open `wiki/SCHEMA.md` in a split view while writing frontmatter. The AI Agents section has these tags: `ai-agents, multi-agent, orchestration, agent-orchestration, agents, coding-agents, memory-systems, agent-memory, agent-safety, openclaw, agent-harness, agent-framework, agent-sdk, agent-architecture, agent-runtime, agent-evaluation, agent-security, agent-communication, autonomous-agents, subagents, computer-use, human-in-the-loop, tool-use, cognition, durable-execution, self-improving, personal-ai, agent-media, skill-graph, content-engine, enterprise-ai, knowledge-graph, agent-language`.
