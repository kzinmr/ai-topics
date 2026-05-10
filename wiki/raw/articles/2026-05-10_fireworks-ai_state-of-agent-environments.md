---
title: "50 Trillion Tokens Per Day: The State of Agent Environments"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/state-of-agent-environments"
scraped: "2026-05-10T01:27:19.295974+00:00"
lastmod: "2026-02-12T18:51:08.000Z"
type: "sitemap"
---

# 50 Trillion Tokens Per Day: The State of Agent Environments

**Source**: [https://fireworks.ai/blog/state-of-agent-environments](https://fireworks.ai/blog/state-of-agent-environments)

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
State Of Agent Environments
50 Trillion Tokens Per Day: The State of Agent Environments
PUBLISHED
11/19/2025
Table of Contents
The Agent Environment is a Production Reality
The Seven Types of Agent Environments
Code Generation & Software Agents: The "Digital Factory” (40-50%)
Framework-Native & In-Product Assistants: The "Brains" (35-45%)
Data & Text-to-SQL: The "Analytical Engine" (20-30%)
Customer Support & Human-in-the-Loop: The "Front Office" (20-30%)
Tool-Driven / MCP Ecosystems: The "Connective Tissue" (15-25%)
Browser Automation & RPA (The "Digital Workplace") - 10-20%
DSL & Connector Automation (The "Universal Glue") - 10-20%
Conclusion
Table of Contents
Table of Contents
The Agent Environment is a Production Reality
The Seven Types of Agent Environments
Code Generation & Software Agents: The "Digital Factory” (40-50%)
Framework-Native & In-Product Assistants: The "Brains" (35-45%)
Data & Text-to-SQL: The "Analytical Engine" (20-30%)
Customer Support & Human-in-the-Loop: The "Front Office" (20-30%)
Tool-Driven / MCP Ecosystems: The "Connective Tissue" (15-25%)
Browser Automation & RPA (The "Digital Workplace") - 10-20%
DSL & Connector Automation (The "Universal Glue") - 10-20%
Conclusion
Table of Contents
TL;DR — Agents and LLMs are processing 1.5 quadrillion token per month, and reached a massive scale over the past year. But the real story for the next 12 months isn't about which models are smartest—it's about the complex production environments where agents actually do work, optimizing not only the underlying models but the tools, workflows, and data in their environments. What emerges is a clear hierarchy where the ability to create high-quality environments is a determinant of market success—the companies building complete environments rather than just LLM wrappers are capturing the most value.
The Agent Environment is a Production Reality
For the last two years, the conversation around AI agents has been dominated by potential. Today, that conversation has fundamentally shifted from
potential
to
production
. Businesses have moved beyond prototyping, shipping agents that handle customer support, write enterprise-quality code, and manage complex workflows at scale. The underlying environments where these agents operate are no longer theoretical sandboxes but robust, interconnected, high-velocity ecosystems.
The true determinant of agent performance in these complex ecosystems is not the intelligence of any single model, but the scaffolding and infrastructure that supports agent workflows (think tools, databases, resources, etc.). These
environments
are where real-world value is being captured. Now, based on a multi-source analysis of API telemetry from major providers, enterprise surveys, and platform-level data, we can now measure which environment types are seeing the most activity.
We estimate the total LLM API market is currently processing approximately 1.5 quadrillion tokens per month, or 50 trillion tokens per day [1][2][7]. LLMs are mainstream; they are the new operating system for software, and are already scaling to massive production volumes.
Figure 1: Agent Environment
This article provides a data-driven snapshot of this emerging landscape, mapping the key platforms and protocols that are becoming the de facto infrastructure for agentic AI. We have surveyed adoption signals across PyPI, npm, OpenRouter, Vercel, GitHub, and enterprise reports to identify
Seven Segments
of modern agent environments. Each use case has its distinct competitive dynamics and usage patterns, and will be a battleground for where the next generation of AI-native companies are built.
The Seven Types of Agent Environments
Production agent systems are being deployed at every layer of the software stack, with each layer representing a distinct environment where agents perform work. Our analysis of the
1.5 quadrillion token/month
market shows the distribution of usage across these segments. Note that these percentages are intentionally overlapping, as most production deployments span multiple categories.
Figure 2: Overview of Agent Environments
Code Generation & Software Agents: The "Digital Factory” (40-50%)
The Environment:
Integrated development environments (IDEs), terminals, and CI/CD pipelines where agents operate as co-developers, interacting with codebases, build systems, and testing infrastructure.
The Use Case:
Code generation is AI's first breakout use case, featuring agents that write, debug, test, and refactor code in production development workflows. The segment has moved rapidly from a single product (GitHub Copilot) to a multi-billion dollar ecosystem. Agents in this category act as co-developers to engineering teams at scale, and their usage has seen massive developer adoption.
Figure 3: Code & Software Generation Environments
Why It's Distinct:
Code generation requires continuous environment interaction that other agent types don't. A coding agent doesn't just output text—it must compile code to verify syntax, run test suites to catch bugs, query version control to understand context, and execute in sandboxes to validate behavior. This operational loop is why coding agents generate 42.2 million tool calls per week on OpenRouter [3], far exceeding other use cases.
Market Adoption
:
•
According to Anthropic's Economic Index,
36% of Claude usage is coding
[8], with API usage skewing even higher toward coding workloads. Anthropic's Claude captures 42% of code generation market share [1]
•
40% of Vercel AI Gateway's top 10 applications are coding agents [4]
•
On OpenRouter, the top 4 applications are coding agents, representing 80% of top-10 traffic [3]
Infrastructure Requirements:
•
Execution environments (sandboxes, containers)
•
TTesting frameworks for automated validation (pytest: 290M monthly downloads [5])
•
Version control integration for codebase context (GitPython: 130M monthly downloads [5])
•
Sub-second iteration loops for rapid generate-test-fix cycles
Competitive Dynamics: The market has evolved from general-purpose tools (GitHub Copilot) to specialized environments optimized for different workflows. Cursor dominates rapid iteration scenarios, Replit owns full-stack development environments, and Windsurf targets team collaboration. The winners are building complete development environments, not just LLM wrappers.
Framework-Native & In-Product Assistants: The "Brains" (35-45%)
The Environment:
Application-embedded AI where agents operate within the context of existing software products—customer support chat windows, document editors, data dashboards, and SaaS tools.
Why It's Distinct:
This environment is defined by tight integration with application state. Unlike standalone agents that start fresh each time, framework-native assistants have persistent context about the user, their data, and their workflow. They must navigate complex application logic, access proprietary data sources through RAG, and coordinate multi-step operations while maintaining the illusion of a simple conversational interface.
These frameworks power agents across multiple environments. A LangChain application might orchestrate a coding agent that generates Python, a RAG system that searches internal docs, or a customer support bot that queries a database—all using the same underlying orchestration primitives. This versatility makes frameworks the universal substrate for agent development.
1T+ Cohort Dominance:
Among companies that have processed over 1 trillion tokens on OpenAI's API, 93% use framework-based orchestration [6], indicating that this environment and agent category is being adopted universally.
Figure 4: Agent Framework Environments
Ecosystem Leadership:
•
LangChain has emerged as the clear market leader with
118,000+ GitHub stars
[9], representing a
220% increase
year-over-year. The framework reported a
300% increase in downloads
from Q1 2024 to Q1 2025, demonstrating accelerating developer adoption.
•
LlamaIndex, focused on Retrieval-Augmented Generation (RAG), has carved out a specialized niche with strong adoption in data-intensive applications.
Environment Requirements:
•
State management across multi-turn conversations
•
Memory systems that persist user context
•
Secure access to proprietary databases and APIs
•
Integration with existing authentication and permissions systems
Competitive Dynamics:
LangChain dominates by being framework-agnostic, but specialization is emerging. LlamaIndex owns RAG-heavy environments where data retrieval is critical. LangGraph captures complex multi-agent orchestration.
PyPI Downloads (monthly):
LangChain (17.2M), LlamaIndex (4.3M), LangGraph (17.5M) [5].
Data & Text-to-SQL: The "Analytical Engine" (20-30%)
Figure 5: Data & Analytics Environments + Infrastructure
The Environment:
Agents are increasingly deployed to analyze and synthesize structured data. This environment is defined by tools that translate natural language into executable SQL queries, enabling non-technical users to interact with databases and data warehouses through conversational interfaces.
Why It's Distinct:
This environment is structured and deterministic in ways that conversational AI isn't. Agents must understand database schemas, generate syntactically correct SQL, handle joins across multiple tables, and present results in context. The challenge isn't just SQL generation—it's understanding business context. An agent must know that "revenue last quarter" means a specific date range, a specific table, and specific aggregation logic. This requires tight integration with metadata systems, data catalogs, and business glossaries.
Adoption at Scale:
Among the 1T+ token cohort,
50% of heavy users rely on this pillar
, with particularly strong adoption in Enterprise SaaS and Consumer verticals [6]. This reflects the growing demand for AI-powered analytics and business intelligence.
Infrastructure Maturity:
The data layer is built on mature, production-grade tools.
SQLAlchemy
(130M monthly downloads),
DuckDB
(7.8M monthly downloads), and
SQLGlot
(8.2M monthly downloads) [5] provide the foundational infrastructure for agents to interact with structured data. DuckDB's rapid growth signals the shift toward in-process, high-performance analytics that agents can leverage without complex infrastructure.
Environment Requirements:
•
Access to database schemas and metadata
•
Query optimization and validation layers
•
Data catalog integration for business context
•
Result formatting and visualization capabilities
Customer Support & Human-in-the-Loop: The "Front Office" (20-30%)
Figure 6: Customer Support Agents
The Environment:
Customer-facing interfaces—chat widgets, ticketing systems, email threads, and voice channels—where agents handle support queries with human oversight and escalation paths.
Why It's Distinct:
This environment is defined by risk management and trust requirements that other environments don't face. A coding agent that generates bad code gets caught by tests. A support agent that gives wrong information damages customer relationships and brand reputation. This makes observability, tracing, and human-in-the-loop workflows non-negotiable. Every interaction must be loggable, auditable, and interruptible.
Market Adoption:
Among the 1T+ token cohort, 50% of users leverage this pillar, with
8 of 11 Enterprise SaaS & Ops companies
relying on customer support and human-in-the-loop solutions
Environment Requirements:
•
Conversation tracing and logging for audit trails (like Langfuse, 250K+ monthly npm downloads [5])
•
Confidence scoring and escalation triggers
•
Human agent handoff with context preservation
•
Quality evaluation and feedback loops
•
Integration with existing ticketing systems (Zendesk, Intercom, Salesforce)
Tool-Driven / MCP Ecosystems: The "Connective Tissue" (15-25%)
The Environment:
The connective layer that enables agents to interact with external systems—APIs, databases, file systems, and third-party services—through standardized protocols and tool-calling interfaces.
Why It's Distinct:
This isn't a standalone environment where agents do work; the true impact of this environment is as an
enabling layer
for other segments, like Code & Software Agents and Browser Automation. An agent can't write code without calling a compiler, can't answer support questions without querying a knowledge base, and can't analyze data without accessing a database. Tool-calling is the fundamental capability that makes agents useful beyond text generation.
Environment Requirements:
•
Standardized tool description formats (parameters, return types, error handling)
•
Authentication and authorization for external services
•
Tool discovery mechanisms for dynamic environments
Competitive Dynamics
: The ecosystem is in a standards battle. Model Context Protocol (MCP), developed and open-sourced by Anthropic, is the emerging standard. Before MCP, every framework had its own tool-calling format. MCP provides a vendor-agnostic way for agents to discover, authenticate with, and invoke tools across different providers, and is gaining traction, with the core Python SDK (mcp) seeing over
1.6M monthly downloads
[5], largely as a dependency for other agent frameworks and applications.
However, OpenAI's function calling format has massive installed base from ChatGPT and API usage. LangChain's tools abstraction sits in the middle, supporting both. The outcome will likely mirror web standards—multiple protocols coexist, with converters between them, until one achieves critical mass.
Browser Automation & RPA (The "Digital Workplace") - 10-20%
The Environment:
For agents to operate in the real world, they must interact with the web. This environment is the browser where agents "see" and interact with visual interfaces—clicking, scrolling, form-filling—to automate workflows designed for humans.
This is the only environment where agents must interpret visual interfaces designed for humans. Unlike APIs with structured data, browser automation requires computer vision to understand UI elements, spatial reasoning to navigate layouts, and action planning to complete multi-step workflows. Agents must handle dynamic content, loading states, and visual changes that break traditional RPA scripts.
Market Adoption
: OpenRouter processes 153.5 million images per week [3], a strong signal of agents performing visual observation tasks. This volume indicates that agents are not just processing text but are actively "seeing" and interpreting visual interfaces.
Environment Requirements:
•
Vision models for UI element recognition
•
Action planning for multi-step workflows
•
Error recovery for dynamic interfaces
•
Secure execution environments for web interactions
Mature Tooling:
The browser automation ecosystem is built on mature, widely adopted tools. Playwright (100M monthly npm downloads) and Selenium (40M monthly PyPI downloads) [5] provide the foundational infrastructure for agents to interact with web browsers. Playwright's dominance in the npm ecosystem reflects its modern architecture and superior developer experience.
DSL & Connector Automation (The "Universal Glue") - 10-20%
The Environment:
The unsung hero of the agent stack, aka the data interchange layer where agents generate and consume structured formats—JSON, YAML, XML, and custom DSLs—to communicate with APIs, configure systems, and exchange data between services.
Why It's Distinct:
This is the invisible substrate that every other environment depends on. Agents can't call APIs without JSON serialization, can't read configuration files without YAML parsing, and can't validate data schemas without structured validation. Unlike other environments where agents perform end-user tasks, this layer enables inter-system communication that makes complex agent workflows possible.
Infrastructure at Massive Scale:
The astronomical download numbers for these packages reveal their role as core dependencies for the entire software ecosystem.
PyYAML
(340M monthly downloads) and
jsonschema
(210M monthly downloads) [5] are inherited by virtually all agent applications, and are essential for configuration management, API interaction, and data serialization.
The Invisible Layer:
This pillar is rarely discussed in the context of agent environments, yet it is the most widely deployed. Every agent that reads a configuration file, calls an API, or exchanges data with another system relies on this infrastructure. The scale of adoption (hundreds of millions of downloads) dwarfs that of more visible agent frameworks, highlighting the importance of robust, mature tooling.
Conclusion
The environments where agents operate are no longer toy sandboxes. They are complex, production-grade ecosystems processing
1.5 quadrillion tokens per month,
that must handle API failures, authentication layers, schema validation, error recovery, and real-time coordination across dozens of external systems.
The data reveals a clear hierarchy of complexity: Code & Software Agents breakout use case at 40-50% of the market, Framework-Native & In-Product Assistants provide the orchestration layers that coordinates everything, and the infrastructure segments (MCP & Tool Integration, Infrastructure & DSL) are the unseen substrate handling the operational complexity. The next 12 months will be defined by the consolidation of these environments into unified, agent-first platforms that abstract away the underlying complexity.
References
[1] Menlo Ventures. (2025, July 31). 2025 Mid-Year LLM Market Update.
https://menlovc.com/perspective/2025-mid-year-llm-market-update/
[2] OpenAI. (2025, November 12). OpenAI DevDay 2025 - API Scale Announcement.
https://www.youtube.com/watch?v=hS1YqcewH0c&t=72s
[3] OpenRouter. (2025, November). OpenRouter Rankings and Statistics.
https://openrouter.ai/rankings
[4] Vercel. (2025, November). Vercel AI Gateway Leaderboards.
https://vercel.com/ai-gateway/leaderboards
[5] PyPI Stats. (2025, November). Python Package Download Statistics.
https://pypistats.org/
[6] OpenAI. (2025, November). 1T+ Token Customer Cohort Analysis. Internal enterprise survey data.
[7] Pichai, Sundar. (2025, May 14). Gemini API Scale Announcement.
https://x.com/sundarpichai/status/1983627221425156144
[8] Anthropic. (2025, September). Anthropic Economic Index Report.
https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
[9] GitHub. (2025, November). Repository Statistics.
https://github.com/
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
