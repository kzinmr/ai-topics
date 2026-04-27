# OpenClaw Pi Integration Architecture

**Source:** https://docs.openclaw.ai/pi
**URL:** https://docs.openclaw.ai/pi

## Overview & Core Benefits
OpenClaw embeds the `pi-coding-agent` SDK directly into its messaging gateway architecture via `createAgentSession()`, bypassing subprocess or RPC modes. This embedded approach delivers:
- Full control over session lifecycle & event handling
- Custom tool injection (messaging, sandbox, channel-specific actions)
- Per-channel/context system prompt customization
- Session persistence with branching/compaction support
- Multi-account auth profile rotation with failover
- Provider-agnostic model switching

## Package Dependencies (v0.70.2)
| Package | Purpose |
|---|---|
| `@mariozechner/pi-ai` | Core LLM abstractions: Model, streamSimple, message types, provider APIs |
| `@mariozechner/pi-agent-core` | Agent loop, tool execution, AgentMessage types |
| `@mariozechner/pi-coding-agent` | High-level SDK: createAgentSession, SessionManager, AuthStorage, ModelRegistry, built-in tools |
| `@mariozechner/pi-tui` | Terminal UI components (used in OpenClaw's local TUI mode) |

## Core Integration Flow
1. **Entry Point:** `runEmbeddedPiAgent()` creates session, passes workspace, config, prompt, provider, model, timeout, and event callbacks.
2. **Session Creation:** `createAgentSession()` initializes resource loader, session manager, settings manager, and applies system prompt overrides.
3. **Event Subscription:** Subscribes to session events (message start/end, tool execution, turn start/end, compaction).
4. **Prompting & Image Injection:** Image injection is prompt-local. OpenClaw loads image refs and passes them via `images` for that turn only.

## Tool & Prompt Architecture
### Tool Pipeline
1. Base Tools: pi's `codingTools` (read, bash, edit, write)
2. Custom Replacements: OpenClaw replaces bash with `exec`/`process`, customizes read/edit/write for sandbox
3. OpenClaw Tools: messaging, browser, canvas, sessions, cron, gateway, etc.
4. Channel Tools: Discord/Telegram/Slack/WhatsApp-specific action tools
5. Policy Filtering: Filtered by profile, provider, agent, group, sandbox policies
6. Schema Normalization: Cleaned for Gemini/OpenAI quirks
7. AbortSignal Wrapping: Tools wrapped to respect abort signals

### Adapter & Split Strategy
All tools passed as `customTools` to ensure OpenClaw's policy filtering, sandbox integration, and extended toolset remain consistent across providers.

### System Prompt Construction
Built dynamically per channel/context. Supports dynamic injection of workspace info, file context, and channel-specific instructions.

## Key Insights for Second-Party Apps
- SDK embedding is superior to subprocess/RPC for lifecycle control and tool injection
- Session branching/compaction enables long-running multi-channel conversations
- Provider-agnostic model switching works seamlessly through pi's unified API
- Custom tools must be wrapped with AbortSignal for graceful cancellation
