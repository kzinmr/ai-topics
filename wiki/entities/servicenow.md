---
title: "ServiceNow"
created: 2026-05-14
updated: 2026-05-25
type: entity
tags:
  - company
  - platform
  - ai-agents
  - developer-tooling
  - automation
sources: [raw/articles/2026-05-06_servicenow-build-agent.md, https://www.servicenow.com/, raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md]
---

# ServiceNow

ServiceNow (NYSE: NOW) is an enterprise software company ($92.3B market cap) providing the "AI control tower for business reinvention." It operates a platform for IT service management, HR, customer service, and security automation, and has been aggressively expanding into AI agent capabilities.

## Build Agent (May 2026)

At Knowledge 2026, ServiceNow launched **Build Agent in ServiceNow Studio** — a tool enabling developers to create production-ready applications and AI agents using natural language prompts.

### Key Features

- **Natural language app building**: Generate complete applications with workflows, catalog items, UI components, and configurations in a single session
- **Multi-IDE support**: Works with Cursor, Windsurf, [[entities/claude-code|Claude Code]], and GitHub Copilot via ServiceNow SDK
- **Powered by Anthropic models**: Supports longer context sessions for complete application builds
- **Governance by default**: App Engine Management Center (AEMC) free for all customers — deployment approvals, release management, lifecycle governance
- **Self-healing test loop**: Validates generated code against quality standards
- **Custom Instructions**: Encode organizational development standards into the tool
- **Cross-scope**: Operates across the entire ServiceNow platform

### Customer Impact
- Cox Automotive: automated development lifecycle, reduced errors
- Plat4mation: Build Agent generated ~80% of a recent customer application automatically

### Roadmap
- Build Agent MCP Client: Q2 2026
- Reimagined AI Agent Studio: Q2 2026
- AEMC freemium tier: Q3 2026

## AI Agent Strategy

ServiceNow positions itself as an **AI control tower** — providing governed, enterprise-grade agent deployment across IT, HR, security, and customer service workflows. The Yokohama Release introduced Agentic AI capabilities including AI Agent Studio and Now Assist Skill Kit.

### AI Agent Orchestrator

ServiceNow's **AI Agent Orchestrator**は, 複数Agentを部門横断で協調させる"control tower"機能. 個別's Agentを超えて, 組織全体's Agent連携を管理·統制する役割を担う. 

これは[[concepts/agent-control-plane|Agent Control Plane]]'s 具体的事例であり, ServiceNowが単なるITSMプラットフォームから**Agent時代's 統治レイヤー**へ進化していることを示す. ([ソース分析](raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md))

## Related Pages

- [[entities/anthropic|Anthropic]] — powers Build Agent's underlying models
- [[entities/snyk|Snyk]] — another enterprise platform integrating AI agents
- [[concepts/enterprise-ai|Enterprise AI]] — the broader category
- [[concepts/vibe-coding|Vibe Coding]] — the contrast: speed without governance
