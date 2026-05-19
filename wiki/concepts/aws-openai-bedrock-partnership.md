---
title: AWS-OpenAI Bedrock Partnership
created: 2026-05-18
updated: 2026-05-18
type: concept
tags:
  - concept
  - aws
  - openai
  - platform
  - infrastructure
  - ai-agents
  - coding-agents
  - mcp
  - company
sources: [raw/articles/2026-05-18_aws-openai-bedrock-partnership.md, https://www.aboutamazon.com/news/aws/bedrock-openai-models]
---

# AWS-OpenAI Bedrock Partnership

## Overview

In May 2026, AWS and OpenAI announced a major expansion of their partnership, bringing frontier OpenAI intelligence to Amazon Bedrock. Three new offerings (all limited preview) enable enterprises to build with OpenAI's most capable models and agents on the infrastructure they already trust.

## Three Pillars

### 1. OpenAI Models on Amazon Bedrock
For the first time, AWS customers can access the latest OpenAI models alongside Anthropic, Meta, Mistral, Cohere, Amazon, and other providers — all through a single, consistent Bedrock API with unified security, governance, and cost controls.

Enterprise controls: IAM-based access, AWS PrivateLink, guardrails, encryption at rest/in-transit, CloudTrail logging.

### 2. Codex on Amazon Bedrock
OpenAI's coding agent (used by 4M+ weekly users) is now available through Bedrock infrastructure. Available via Codex CLI, desktop app, and VS Code extension. Usage counts toward AWS cloud commitments.

### 3. Amazon Bedrock Managed Agents, powered by OpenAI
Combines OpenAI's frontier reasoning and agentic capabilities with AWS's global infrastructure. Built-in components: persistent memory across sessions, skills encoding procedures, identity enforcing permissions, and appropriate compute options.

Built with the OpenAI Agent Harness — optimized for OpenAI models. Every agent operates with its own identity, all actions logged for auditability.

## Relationship to AgentCore

[[entities/amazon-bedrock-agentcore]] serves as the open platform for building agents with any model/framework. Bedrock Managed Agents is optimized specifically for OpenAI models on AgentCore. Together they provide authorization, agent discovery, observability, and scalability.

## Strategic Significance

- **Multi-model strategy**: AWS customers can now evaluate and deploy OpenAI alongside other frontier models
- **Financial integration**: OpenAI usage applied to existing AWS commitments
- **Enterprise trust**: Security and governance inherited from AWS infrastructure
- **Box endorsement**: Box CTO Ben Kus called it "the cloud we already trust"

## Related Pages
- [[entities/amazon-bedrock-agentcore]] — AWS's agentic AI platform
- [[entities/openai]] — OpenAI
- [[concepts/model-context-protocol-mcp]] — MCP integration
- [[concepts/aws-agent-toolkit]] — AWS Agent Toolkit
- [[entities/codex]] — OpenAI Codex
