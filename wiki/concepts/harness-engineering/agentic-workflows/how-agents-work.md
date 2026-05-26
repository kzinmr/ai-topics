---
title: "How Coding Agents Work"
type: concept
aliases:
  - how-agents-work
  - coding-agent-architecture
  - agent-internals
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - agentic-engineering
  - architecture
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/how-agents-work/"
---

# How Coding Agents Work

A conceptual model for understanding the inner workings of coding agents. Detailed in Simon Willison's [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/how-agents-work/).

## Building Blocks

### 1. Large Language Models
- Base LLM (Claude Opus 4.6, GPT-4, etc.)
- Core engine for code generation, understanding, and reasoning

### 2. Chat Templated Prompts
- Structured system prompts, user messages, and assistant responses
- Conversation history is templatized and fed into the model

### 3. Token Caching
- Caching of frequently used prompt segments
- Cost reduction and response speed improvement

### 4. Calling Tools
- Ability for the agent to call external tools (filesystem, shell, browser, etc.)
- Automation of code execution, testing, and debugging

### 5. The System Prompt
- Meta-instructions defining the agent's behavior
- Includes project-specific constraints and coding conventions

### 6. Reasoning
- The model's internal reasoning process
- Manifestation of chain-of-thought and step-by-step thinking

### 7. LLM + System Prompt + Tools in a Loop
- The integrated agent loop combining all of the above
- Generate → Execute → Verify → Fix cycle

## Why Understanding Matters

Understanding the inner workings of coding agents is essential for effective use. Specifically:

- **Debugging**: Understanding why the agent produces specific errors
- **Prompt Design**: Creating instructions aligned with the agent's capabilities and limitations
- **Cost Management**: Optimizing token usage and caching
- **Security**: Controlling the agent's filesystem access and external communication

## Plan Mode vs Conversational Planning

> *"Plan mode feels like a hack that was necessary for older generations of models that were not great at adhering to prompts... Instead of 'plan mode', I simply start a conversation with the model, ask a question, let it google, explore code, create a plan together, and when I'm happy with what I see, I write 'build'."*
> — Peter Steinberger

Traditional "Plan Mode" (pre-planning before execution) was a hack from the era when models had poor instruction-following capabilities. With modern models, you can **create plans conversationally and move to execution simply by writing "build"**.

### Benefits of Conversational Planning
- Models explore code while planning → improved accuracy
- Human feedback can be incorporated in real-time
- No overhead from plan mode

## Claude Code's Task Tool Architecture

Sankalp's analysis of Claude Code 2.0 reveals the sub-agent structure:

### Sub-agent Types

| Type | Context | Use Case |
|------|---------|----------|
| `general-purpose` | Full context inheritance | General task delegation |
| `plan` | Full context inheritance | Plan creation |
| `Explore` | New session | File search, code reading (read-only) |

### Task Tool Key Parameters

```json
{
  "required": ["description", "prompt", "subagent_type"],
  "properties": {
    "description": "3-5 word task summary",
    "prompt": "Task instructions",
    "subagent_type": "general-purpose | Explore | Plan",
    "model": "sonnet | opus | haiku (default: same as parent agent)",
    "run_in_background": "true for long-running scripts",
    "resume": "Agent ID to resume from a previous session"
  }
}
```

### Explore Agent Constraints

```markdown
=== CRITICAL: READ-ONLY MODE - NO FILE MODIFICATIONS ===
STRICTLY PROHIBITED: Creating, modifying, deleting, moving files.
USE: GLOB, GREP, READ tools only
BASH: ONLY for read-only ops (ls, git status, cat, find). NEVER mkdir, rm, npm install, etc.
```

The Explore agent is designed as **read-only**, with no ability to modify files. This eliminates the risk of breaking the codebase during exploration.

## Related Concepts

- [[concepts/agentic-engineering]] — Parent concept
- [[concepts/subagents]] — Agent hierarchy
- [[concepts/harness-engineering/agentic-workflows/using-git-with-agents]] — Version control integration
- [[concepts/context-window-management]] — Task Tool splits context
- [[concepts/harness-engineering/agentic-workflows/cli-first-development]] — Agent tool calling patterns

## References

- [[entities/simon-willison]] — How Coding Agents Work concept originator
- [[entities/sankalp-sinha]] — Claude Code 2.0 Task Tool analysis
- Peter Steinberger — Plan Mode unnecessary
- [Agentic Engineering Patterns — How Agents Work](https://simonwillison.net/guides/agentic-engineering-patterns/how-agents-work/)
- [A Guide to Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
- [Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)

