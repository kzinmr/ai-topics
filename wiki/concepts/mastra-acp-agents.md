---
title: Mastra ACP Agents
created: 2026-05-19
updated: 2026-05-19
type: concept
tags:
  - concept
  - ai-agents
  - protocol
  - agent-communication-protocol
  - coding-agents
  - tool
  - developer-tooling
  - workflow
sources: [raw/articles/2026-05-14_mastra-acp-agents.md, https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.34.0]
---

# Mastra ACP Agents

**Mastra's ACP integration** (`@mastra/acp@0.1.0`, May 2026) enables running **ACP-compatible coding agents** as Mastra tools or lightweight subagents with incremental response streaming. This represents a new pattern: treating external agent processes as first-class components within a supervisor/workflow architecture.

## Design

Two integration modes:

1. **`createACPTool`**: Wraps an ACP agent as a Mastra tool — callable by any agent in the system for specific coding tasks
2. **`AcpAgent`**: Wraps an ACP agent as a `SubAgent`-compatible implementation, usable in:
   - Supervisor delegation
   - Workflow steps
   - Inngest workflow adapter

```typescript
import { createACPTool, AcpAgent } from '@mastra/acp';

export const codingTool = createACPTool({
  command: 'my-acp-agent',
});

export const codingAgent = new AcpAgent({
  command: 'my-acp-agent',
});

// Wire into supervisor
const supervisor = new Agent({
  agents: { codingAgent },
});
```

## Significance

This pattern bridges the gap between **coding agents** (Claude Code, Codex, OpenCode — which excel at code but run as separate processes) and **orchestration frameworks** (Mastra, LangChain, CrewAI — which compose agents but typically don't host coding agents natively).

By making ACP agents `SubAgent`-compatible, Mastra enables:
- A supervisor that delegates coding tasks to Claude Code via ACP
- Workflow steps that invoke ACP agents for code generation
- Composability across agent types within a single orchestration layer

## Broader Pattern: ACP as Agent Interop

See also: [[concepts/acp-agent-communication-protocol]] for the underlying protocol. The Mastra integration demonstrates that ACP is evolving beyond a coding-agent protocol into a general **agent interop standard** — where any ACP-compatible agent (coding, research, planning) can be plugged into any ACP-aware framework.

## Related

- [[entities/mastra]] — Mastra framework
- [[concepts/acp-agent-communication-protocol]] — ACP protocol
- [[entities/claude-code]] — ACP-compatible coding agent
- [[concepts/agent-framework]] — Agent framework landscape
- [[concepts/coding-agents/coding-agents]] — Coding agent ecosystem
