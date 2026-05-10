---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/ai-agents-with-aws-agentcore"
scraped: "2026-05-10T01:21:11.772703+00:00"
lastmod: "2026-02-12T18:51:24.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/ai-agents-with-aws-agentcore](https://fireworks.ai/blog/ai-agents-with-aws-agentcore)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Ai Agents With Aws Agentcore
Production-Ready AI Agents with Optimized Inference with AWS AgentCore
PUBLISHED
10/2/2025
Table of Contents
TL;DR
What is AWS AgentCore?
Fireworks AI + AgentCore: Better Together
Example: Code Generation Agent
Get Started
What's Next
Table of Contents
Table of Contents
TL;DR
What is AWS AgentCore?
Fireworks AI + AgentCore: Better Together
Example: Code Generation Agent
Get Started
What's Next
Table of Contents
TL;DR
Fireworks AI now integrates with AWS AgentCore, enabling developers to deploy AI agents with optimized inference on secure, serverless AWS infrastructure. Build locally, deploy globally with enterprise-grade security and automatic scaling.
What is AWS AgentCore?
AWS AgentCore Runtime
provides serverless infrastructure purpose-built for AI agents. It solves the operational complexity of deploying dynamic AI agents at scale by offering:
•
Serverless scaling with fast cold starts
•
Built-in security and session isolation
•
Framework flexibility - use any open-source framework, protocol, or model
•
Extended runtime support for complex multi-step agent workflows
This eliminates the need to manage containers, orchestration, or scaling infrastructure while maintaining enterprise security requirements.
Fireworks AI + AgentCore: Better Together
Fireworks AI delivers the fastest, highest quality inference engine for agentic workloads. We provide optimizations like adaptive caching and speculative decoding that are critical for multi-turn agent interactions. Combined with AgentCore's serverless deployment, you get:
•
Speed where it matters: Sub-second latency for agent reasoning loops powered by Fireworks' optimized inference stack
•
AWS-native deployment: Deploy directly to your AWS infrastructure with no additional configuration
•
Enterprise ready: Leverage AWS security, compliance, and existing commitments while using Fireworks' inference engine.
Example: Code Generation Agent
To demonstrate this integration, we built two cookbooks using AgentCore Runtime and AgentCore Code Interpreter. These agents can read files, generate python code, run the code and interpret the results. The agents use state of the art open source models
Kimi K2 0905
and
Qwen 3 Coder 480B
respectively.
The architecture shows the complete flow: develop your agent locally with your choice of models and frameworks, configure it with a Docker file, and deploy to AgentCore Runtime via AWS CodeBuild. Once deployed, users can invoke the agent through the Runtime endpoint with all infra handled serverlessly by AWS.
See our full documentation and both cookbooks in our
documentation page
.
Get Started
Ready to build production AI agents?
Get your Fireworks API key
:
Sign up at fireworks.ai
Review the integration guide
:
Fireworks + AgentCore documentation
Deploy your first agent
: Follow the
complete tutorial
The integration supports serverless inference, fine-tuned models, and on-demand deployments. For enterprise deployments leveraging existing AWS compute please reach out to
[email protected]
What's Next
We will continue to expand our AWS AgentCore integration with additional cookbooks and deeper platform integrations. Stay tuned for more examples covering multi-agent systems, custom tool integration, and production deployment patterns.
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
