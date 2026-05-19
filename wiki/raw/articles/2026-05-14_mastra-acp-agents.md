# Mastra v1.34.0: ACP Coding Agents as Tools and Subagents

**Source:** https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.34.0
**Date:** May 14, 2026

Mastra released `@mastra/acp@0.1.0`, enabling ACP-compatible coding agents to run as Mastra tools (`createACPTool`) or lightweight subagents (`AcpAgent`) with incremental streaming. Key features in this release:

- **ACP as Tools/Subagents**: ACP agents are compatible with the `SubAgent` interface — usable in supervisor delegation, workflow steps, and the Inngest adapter
- **xAI Realtime Voice**: New `@mastra/voice-xai-realtime` provider for Grok Voice Agent API
- **Agent Metadata**: Optional `metadata` record on agents (static or dynamic), surfaced in API responses
- **Enterprise RBAC**: Model allowlist/admin policies, role-aware capabilities via `IRBACProvider`
- **Enhanced `workspace.read_file`**: Media files returned as native parts (not base64); text stays as text

Mastra (from Gatsby team, 24K GitHub stars) is a TypeScript framework for building AI-powered applications and agents.
