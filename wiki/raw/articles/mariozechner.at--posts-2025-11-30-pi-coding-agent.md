# What I learned building an opinionated and minimal coding agent

**Author:** Mario Zechner (@badlogicgames)
**Date:** 2025-11-30
**URL:** https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
**Source:** https://mariozechner.at/posts/2025-11-30-pi-coding-agent/

## Summary: What I Learned Building an Opinionated and Minimal Coding Agent

### Core Philosophy & Motivation
Existing coding agents (Claude Code, Codex, Cursor, Amp, etc.) evolved from simple tools into bloated, unpredictable harnesses. Key pain points drove the creation of `pi-coding-agent`:
- **Unpredictable Updates:** System prompts and tools change per release, breaking workflows.
- **Lack of Transparency:** Hidden context injection, poor observability, and messy APIs.
- **Context Engineering is Paramount:** Controlling exactly what enters the model's context drastically improves code output. Existing harnesses make this nearly impossible.
- **Self-Hosting Friction:** Libraries like Vercel AI SDK struggle with self-hosted models, especially around tool calling.
- **Design Principle:** *"If I don't need it, it won't be built."*

### Architecture Overview
The project is split into four cohesive packages:
| Package | Purpose |
|:---|:---|
| `pi-ai` | Unified LLM API (multi-provider, streaming, tool calling, thinking support, context handoffs, token/cost tracking) |
| `pi-agent-core` | Agent loop handling tool execution, validation, event streaming, state management, and transport abstraction |
| `pi-tui` | Minimal terminal UI framework with differential rendering, synchronized output, and component-based layout |
| `pi-coding-agent` | CLI wiring everything together (session management, custom tools, themes, project context files) |

### pi-ai & pi-agent-core (Unified LLM API)
Abstraction over four core APIs: OpenAI Completions, OpenAI Responses, Anthropic Messages, Google Generative AI.
Provider quirks are handled (max_tokens vs max_completion_tokens, missing store field, inconsistent reasoning traces).
**Context Handoff** enables cross-provider switching with standardized formats.
**Type-Safe Model Registry** parses OpenRouter & models.dev into TypeScript types. Self-hosted models (Ollama, vLLM) are straightforward.
**Production-Grade Features:** Full Abort Support, Structured Tool Results (TypeBox/AJV validation), Agent Loop with message queuing.

### pi-tui (Terminal UI Framework)
Native terminal append over full-screen cell buffers to preserve scrollback and search. Retained mode with differential rendering. Synchronized output escape sequences prevent flicker. Performance optimized with scrollback buffer and comparator cache.

### pi-coding-agent (The CLI)
Wires everything together. Ships with 4 tools: read, write, edit, bash. Extensible via Extensions (TypeScript plugins with lifecycle hooks), Skills (prompt templates), Prompt Templates, and Themes. Pi Packages can be shared via npm or git. Four modes: interactive, print/JSON, RPC, and SDK for embedding.

### Design Principles
- Minimal defaults, maximum customization
- No hidden context or surprise tool injections
- Full transparency into what the model sees
- Embeddable via SDK for second-party apps (OpenClaw, MoltBot, Amp, etc.)
- Open source under MIT license
- 40.4k+ GitHub stars, 4.7k forks

### Key Insight
*"The best coding agent isn't the one with the most features. It's the one that lets you control exactly what enters the model's context, runs predictably, and can be embedded into your own architecture without forking or RPC overhead."*
