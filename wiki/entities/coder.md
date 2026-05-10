---
title: "Coder (Coder Technologies)"
created: 2026-05-10
updated: 2026-05-10
type: entity
tags: [company, coding-agents, developer-tooling, infrastructure, security, platform]
sources:
  - raw/articles/2026-05-06_coder-self-hosted-agents-beta.md
  - https://coder.com
---

# Coder (Coder Technologies)

Coder is an enterprise **self-hosted AI development infrastructure** company based in Austin, Texas. It provides a platform for secure, scalable cloud development environments, and in May 2026 launched **Coder Agents** — a model-agnostic, self-hosted AI coding agent system.

## Core Platform

Coder's platform enables enterprises to move development to centralized cloud infrastructure while maintaining full control over data, security, and compliance. It powers development environments for 2,500+ developers at U.S. defense intelligence organizations and enterprises in automotive, finance, government, and technology sectors.

## Coder Agents (Beta, May 2026)

Coder Agents is a **native AI coding agent** built directly into the Coder platform, launched in beta on May 6, 2026.

### Key Differentiators

| Feature | Detail |
|---------|--------|
| **Self-hosted** | Entire agent system (control plane, orchestration, execution) runs on customer infrastructure |
| **Model-agnostic** | Supports Anthropic, OpenAI, Google, AWS Bedrock, and self-hosted models |
| **Air-gapped** | Works in fully air-gapped or network-restricted environments |
| **No data exfiltration** | Source code, prompts, and model interactions never leave the network |
| **Centralized governance** | Platform teams control model access, prompt policies, and usage across teams |

### Developer Workflows

- Code generation
- Test generation
- Repository analysis
- Pull request creation
- API and conversational interface

### Enterprise Rationale

Coder Agents addresses a key gap in enterprise AI adoption: **regulated industries cannot send source code to third-party AI services**. By keeping everything on self-hosted infrastructure, Coder enables AI-driven development for defense, finance, healthcare, and other compliance-heavy sectors.

## Comparison to Other Coding Agents

Unlike cloud-hosted coding agents like [[entities/claude-code]], [[concepts/codex]], or [[entities/cursor]], Coder Agents is designed for enterprises that require:

- Complete data sovereignty
- Air-gapped deployment capability
- Centralized model governance across teams
- Audit trails for all AI-driven code changes

## Related

- [[entities/coder]] — This page
- [[entities/claude-code]] — Anthropic's coding agent
- [[concepts/codex]] — OpenAI's coding agent
- [[entities/cursor]] — AI code editor
- [[concepts/coding-agents]] — General coding agent concept
- [[concepts/agent-security]] — Agent security and governance
