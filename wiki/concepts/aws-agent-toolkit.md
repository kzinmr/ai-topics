---
title: AWS Agent Toolkit
created: 2026-05-18
updated: 2026-05-18
type: concept
tags: [concept, aws, developer-tooling, ai-coding, mcp, ai-infrastructure, coding-agents]
sources: [raw/articles/2026-05-18_aws-agent-toolkit.md, https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit/]
---

# AWS Agent Toolkit for AWS

## Overview
Launched May 6, 2026, the **Agent Toolkit for AWS** is a production-ready suite of tools and guidance that helps AI coding agents build on AWS with fewer errors, lower token costs, and enterprise-grade security controls. It is the successor to the MCP servers, plugins, and skills previously available on AWS Labs.

## Components

### Agent Skills
Validated, up-to-date procedures for common AWS tasks. 40+ skills at launch across:
- Infrastructure-as-Code (CloudFormation)
- Storage (S3, EBS)
- Analytics (Athena, Glue)
- Serverless (Lambda, API Gateway)
- Containers (ECS, EKS)
- AI services (SageMaker, Bedrock)

More planned for databases, networking, and IAM.

### AWS MCP Server (GA)
A fully-managed Model Context Protocol server allowing coding agents to interact with any AWS service via:
- IAM-based guardrails on agent actions
- CloudWatch and CloudTrail observability
- Sandboxed code execution for multi-step operations
- Documentation search and retrieval tools

Available in us-east-1 and eu-central-1.

### Agent Plugins
Bundled MCP server + curated skills into single install:
- **AWS Core**: Full-stack application development
- **AWS Data Analytics**: Data pipelines, querying, loading
- **AWS Agents**: Production-ready agents using [[entities/amazon-bedrock-agentcore]]

## Pricing
No additional charge — pay only for AWS resources used by agents.

## Related Pages
- [[concepts/model-context-protocol-mcp]] — MCP
- [[entities/amazon-bedrock-agentcore]] — Bedrock AgentCore
- [[concepts/aws-openai-bedrock-partnership]] — AWS-OpenAI partnership
- [[concepts/agent-skills]] — Agent skills concept
- [[concepts/ai-coding]] — AI coding agents
