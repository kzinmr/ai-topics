---
title: "Minimal Coding Agent"
created: 2026-05-03
updated: 2026-05-03
tags:
  - concept
  - ai-agents
  - coding-agents
  - architecture
  - harness-engineering
aliases:
  - minimal-coding-agent
  - emperor-has-no-clothes-agent
  - three-tool-agent
  - heartbeat-loop-agent
  - 400-line-agent
related:
  - [[concepts/agent-loop-orchestration]]
  - [[concepts/agent-harness]]
  - [[concepts/harness-engineering]]
  - [[concepts/building-effective-agents]]
sources:
  - raw/articles/2025-04-15_ampcode-how-to-build-a-code-editing-agent.md
  - https://ampcode.com/notes/how-to-build-an-agent
---

# Minimal Coding Agent

## Summary

The **Minimal Coding Agent** is an architectural pattern for code-editing AI agents, articulated by Thorsten Ball in his April 2025 article "How to Build a Code-Editing Agent: The Emperor Has No Clothes Guide." The pattern demonstrates that a functional code-editing agent can be built in ~400 lines of Go with just three file-system tools — `read_file`, `list_files`, and `edit_file` — wrapped around a simple "heartbeat loop."

The core thesis: **the "agent" part of an AI coding agent is trivially simple.** The sophistication of professional products comes entirely from UI/UX, system prompts, error handling, and editor integration — not from the agent loop itself.

## The Heartbeat Loop

The agent operates as a continuous loop:

```
User Input → LLM Inference → Check for Tool Use → Execute Tool → Repeat
```

The "inference" function passes tool definitions, conversation history, and a user message to an LLM (Claude 3.7 Sonnet), then checks if the response contains a tool-use signal.

```go
// Pseudocode structure
for {
    message := runInference(ctx, conversation, tools)
    if message.HasToolUse() {
        result := executeTool(message.ToolCall)
        conversation = append(conversation, message, result)
    } else {
        break // Agent is done
    }
}
```

Most of the ~400 lines of code are type definitions and JSON schema generation. The actual agent logic is under 100 lines.

## The Three Essential Tools

### 1. `read_file`
Allows the model to see a file's contents. The tool description must clearly tell the model *when* to use it.

### 2. `list_files`
Allows the model to explore the directory structure. Trailing slashes on directory names help the model distinguish files from folders.

### 3. `edit_file` (String Replacement)
The surprising key insight: the most effective file editing mechanism for Claude 3.7 is **simple string replacement** — find `OldStr` in a file and replace it with `NewStr`. No diff-based patching required.

```go
newContent := strings.Replace(oldContent, editFileInput.OldStr, editFileInput.NewStr, -1)
```

## Emergent Behaviors

The agent exhibits **emergent reasoning** without explicit programming:

- **Tool deduces itself**: The model figures out *when* to use each tool from descriptions alone. No need to hardcode "if user asks about a file, use read_file."
- **Tool chaining**: When asked to "fix a bug," the agent autonomously chains: `list_files` → `read_file` → `edit_file` to find the source, understand the code, and apply the fix.

## Key Insights

| Insight | Detail |
|---------|--------|
| **No moat in the loop** | The agent loop itself is commodity code — ~100 lines of logic |
| **Differentiation is "elbow grease"** | Professional agents differentiate via UI/UX, system prompts, robust error handling, feedback loops, and editor integration |
| **Harness > Agent** | The loop is trivial; the infrastructure around it (tools, context, error recovery) is where engineering investment matters |
| **LLM chooses tools** | No explicit orchestration needed — model deduces tool selection from descriptions |

## Graph Structure

```
[concept: minimal-coding-agent]
  ├── author──→ [entity: thorsten-ball]
  ├── embodies──→ [concept: harness-engineering]
  ├── relates-to──→ [concept: agent-loop-orchestration]
  ├── contrasts──→ [concept: claude-code]  (professional, polished vs minimal)
  └── teaches──→ [concept: building-effective-agents] (concrete implementation of Anthropic's principles)
```

## Related Concepts

- [[concepts/agent-loop-orchestration]] — The general agent loop pattern; this is a concrete Go implementation
- [[concepts/agent-harness]] — This pattern is a minimal harness: LLM + loop + tools
- [[concepts/harness-engineering]] — The broader umbrella; this pattern exemplifies "the harness is the OS"
- [[concepts/building-effective-agents]] — Anthropic's guidelines on agent design; this is a concrete implementation
- [[entities/thorsten-ball]] — Author of the article and creator of this pattern

## Sources
- [How to Build a Code-Editing Agent — Thorsten Ball / Amp](https://ampcode.com/notes/how-to-build-an-agent)
