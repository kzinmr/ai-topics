---
title: "Agent Plugins 1.0.0"
created: 2026-08-08
updated: 2026-08-08
type: concept
tags: [protocol, ai-agents, agents, agent-skills, agent-protocol, agent-communication, agent-platform, agent-tooling, mcp, skills, tool-use, plugins, extensibility, framework, vendor-lock-in, ecosystem, open-source, developer-tooling, ai-infrastructure, coding-agents, vercel, aws, amazon, openai, google, microsoft, github-copilot, cursor, codex, security, announcement, event]
sources: [raw/articles/2026-08-07_tnw_agent-plugins-1-0-0-standard.md]
---

# Agent Plugins 1.0.0

## Overview

**Agent Plugins 1.0.0** is an open standard for portable AI agent component packages, published in August 2026. It defines a "build once, run anywhere" format for reusable agent extensions — bundling MCP servers (tool connectors) and Agent Skills (instruction sets) into a single distributable package. The standard aims to solve the fragmentation where every agent platform expects a different folder layout, configuration scheme, and integration pattern.

The specification lives at [agent-plugins.org](https://agent-plugins.org) and is numbered 1.0.0, signaling a deliberate initial release. The standard is openly licensed and governed by a multi-company steering committee.

Agent Plugins sits alongside two other agent interoperability protocols, each addressing a different layer:

| Protocol | Layer | What it standardizes |
|---|---|---|
| **MCP** (Model Context Protocol) | Context access | How agents connect to external tools, data sources, and services |
| **A2A** (Agent2Agent Protocol) | Agent communication | How agents discover and talk to each other |
| **Agent Plugins** | Component packaging | How agent skills and tools are packaged, distributed, and discovered |

## Backers

The standard represents the first joint alignment of five major AI infrastructure companies on a common agent standard:

- **Vercel** — Initiated the proposal. Vercel's position as a platform company that does not own a dominant agent product gives it credibility as a neutral convener.
- **Amazon/AWS** — Founding member. AWS brings cloud infrastructure weight and positions the standard for enterprise adoption on Bedrock and related agent services.
- **OpenAI** — Framed the launch around GPT-5's first birthday (August 7, 2026). ChatGPT and Codex support the format at launch. This goes beyond OpenAI's own Codex plugins, which previously worked only within its own tools.
- **Microsoft** — Contributed the ecosystem framing. GitHub Copilot and VS Code support Agent Plugins at launch, giving the standard immediate reach into the largest developer agent user base.
- **Google** — Joined as the sixth major backer (announced separately on X). Adds the third major cloud provider and the Gemini ecosystem.

The **steering committee** has five members: Amazon, Cursor (Anysphere), Microsoft, OpenAI, and Vercel. The project's governance model states that no single company's roadmap sets its direction.

Additional launch-day supporters include **Cursor**, **GitHub Copilot**, **Kiro**, and **VS Code** — meaning the standard is available across most major coding agents at launch.

## Relationship to MCP and A2A

Agent Plugins does not replace MCP or A2A — it complements them by addressing the packaging and distribution layer that both protocols leave open:

- **MCP** standardizes how an agent accesses external context (tools, databases, APIs). An Agent Plugin *contains* MCP servers as bundled components, but adds packaging, discovery metadata, and co-located Agent Skills.
- **A2A** standardizes how agents communicate with each other. It is entirely orthogonal — A2A governs inter-agent messaging, while Agent Plugins governs what capabilities an individual agent can load.
- **Agent Plugins** bridges the gap: developers can package MCP servers alongside declarative skill instructions in one directory with a `plugin.json` manifest, making agent components portable across platforms that implement the standard.

The deliberate separation means a developer can adopt Agent Plugins without changing their MCP or A2A setup — the standards compose rather than compete.

## Technical Scope (Version 1.0.0)

The 1.0.0 specification is deliberately narrow. It defines:

- **Package format**: A directory containing a `plugin.json` manifest at its root, plus bundled MCP servers and Agent Skills (reusable instruction sets).
- **Discovery**: How a client finds and identifies available plugins.
- **Manifest structure**: The schema for `plugin.json`, describing what the plugin provides and how to invoke it.

The standard deliberately does **not** define:

- Marketplaces or distribution channels
- Installation mechanisms
- Permission models or sandboxing
- Trust verification or security scanning
- Runtime execution environments

These omissions are intentional — the authors designed the spec to be easy for any agent platform to adopt immediately, leaving harder problems (security, trust, marketplaces) to each client implementation. This has drawn both praise (for lowering adoption friction) and criticism (for leaving the hardest problems unsolved). The risk is real: fake Agent Skills have already slipped past security scanners in early 2026, and the standard does nothing to prevent that at the spec level.

### What a Plugin Contains

A minimal Agent Plugin is a folder with:

```
my-plugin/
├── plugin.json          # Manifest: name, version, provided skills/tools, MCP endpoints
├── skills/              # Reusable Agent Skills (declarative instruction sets)
│   └── my-skill.md
└── mcp-servers/         # Bundled MCP server configurations
    └── my-tool.json
```

The `plugin.json` manifest declares what skills and tools the plugin provides, enabling agent platforms to discover and surface them to users and agent workflows.

## Industry Significance

### The Standards Layer of the Agent Stack

Agent Plugins 1.0.0 completes a three-protocol standards landscape for AI agents:

1. **MCP** (context access, Anthropic-led, 2024)
2. **A2A** (agent communication, Google-led, 2025)
3. **Agent Plugins** (component packaging, Vercel-led, 2026)

Together these three protocols define an open, composable agent ecosystem where context, communication, and capabilities are all standardized — but none is owned by a single company.

### Ecosystem Implications

The standard has two competing interpretations:

- **Open ecosystem case**: A shared format lets any developer build once and reach every major agent platform (ChatGPT, Copilot, Cursor, Codex, VS Code) simultaneously. This lowers the barrier for tool builders and fosters an agent plugin economy comparable to the IDE extension marketplace but cross-platform.

- **Incumbent consolidation case**: A standard rewards the platforms that already have users. If every plugin targets the same format, users have less reason to switch between agent platforms — the plugin ecosystem follows the installed base, reinforcing existing market positions.

### Early Reactions

- **Angie Jones** (developer advocate): "We neeeeded this" — emphasizing the desire for a single way to carry skills between tools.
- **Dax Raad** (SST framework creator): "Very much against" it — calling it "a thin standard" whose useful parts will end up in client-specific extensions anyway.
- **Security researchers**: Noted that the standard deliberately avoids sandboxing and trust, leaving a known vulnerability surface unaddressed at the ecosystem level.

## Open Questions

- **Security and trust**: How will platforms prevent malicious Agent Plugins? The spec leaves this entirely to individual clients.
- **Marketplace dynamics**: Will a common plugin marketplace emerge, or will each platform run its own? The former would amplify the open-ecosystem effect; the latter could create walled gardens around the common format.
- **Adoption beyond coding agents**: The launch supporters are predominantly coding-agent platforms. Whether Agent Plugins gains traction in non-coding agent domains (enterprise automation, personal assistants, browser agents) remains to be seen.
- **Governance longevity**: Multi-company governance of open standards is hard to sustain — especially when the companies involved compete directly.

## Related Pages

- [[concepts/mcp]] — Model Context Protocol, the context-access standard that Agent Plugins builds upon
- [[concepts/a2a-agent-protocol]] — Agent2Agent Protocol for inter-agent communication
- [[concepts/agent-skills]] — Reusable agent instruction sets, a core concept bundled by Agent Plugins
- [[concepts/coding-agents/coding-agents]] — Coding agent platforms that are the primary early adopters
- [[entities/vercel]] — Initiator of the Agent Plugins proposal
- [[entities/openai]] — Major backer, launched with GPT-5 birthday milestone and Codex support
