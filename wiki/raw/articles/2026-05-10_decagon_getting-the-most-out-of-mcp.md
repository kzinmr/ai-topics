---
title: "Why MCP alone isn’t enough for reliable agent tool use"
source: "Decagon Blog"
url: "https://decagon.ai/blog/getting-the-most-out-of-mcp"
scraped: "2026-05-10T01:19:42.140453+00:00"
lastmod: "None"
type: "sitemap"
---

# Why MCP alone isn’t enough for reliable agent tool use

**Source**: [https://decagon.ai/blog/getting-the-most-out-of-mcp](https://decagon.ai/blog/getting-the-most-out-of-mcp)

Introducing Proactive Agents.
Learn more
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Build
AOPs
Workflows for AI agents
Integrations
Support tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & Reporting
Voice of the Customer
Watchtower
Always-on QA
Suggestions
AI-powered knowledge
Industries
Retail
Travel & hospitality
Technology
Financial services
Health & wellness
Media
Telecommunications
Customers
Resources
Learn
Resources Hub
Decagon University
Glossary
AI and the next generation of customer experience
Why exceptional service is the new brand differentiator as AI reshapes consumer expectations.
Spring ’26 Release: Proactive Agents
See how user memory, outbound voice, and Agent Workbench can help you build stronger customer relationships
Company
About
Careers
Security
Sign in
Sign in
Get a demo
Sign in
Get a demo
Product Update
Company news
Technology & research
Industry
Technology & Research
Blog
/
Why MCP alone isn’t enough for reliable agent tool use
Why MCP alone isn’t enough for reliable agent tool use
April 14, 2026
Written by
Bihan Jiang
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
AI agents deliver the most value when they can see and act across your entire tech stack, from refunding orders to rescheduling bookings to looking up loyalty points. Model Context Protocol (MCP) made that connectivity dramatically easier, giving teams a standard way to package and expose tools across their stack.
But connectivity is not the same as reliability. After working with dozens of enterprise customers, we've seen the same mistake play out repeatedly: teams treat MCP as a one-step solution, import a server as-is, and expect everything to work. In production, it doesn't. Bridging that gap requires an infrastructure layer purpose-built to curate, scope, and evaluate how tools are actually used.
The trap of importing an MCP server "as is"
Many teams initially try to expose their full tool stack through an MCP server, hoping the agent will successfully determine which ones are relevant for use. This makes sense in theory but becomes problematic in production.
Imagine an MCP server with 30 to 40 endpoints: refunds, order lookup, rewards, offers, profile management, and more. On every turn, the agent has to choose from the entire tool stack, even though only a few are relevant to the user's intent. With such a large surface area, a few things happen:
Tool selection accuracy drops
Response latency and costs increase due to unnecessary API calls
Mistakes and tool call failures become difficult to trace and debug
The pattern we see across customers is the same: start with full tool access, experience accuracy and latency degradation under production traffic, then revert to manually curating tools per workflow. By relying on the MCP alone, its value erodes and customers are forced back into time-consuming processes.
While it’s tempting to treat tool calling accuracy as a limitation of LLMs, it’s solvable through architectural design. Agents struggle to reason over a large, unbounded action space, and the more tools you expose, the harder the selection problem becomes. By constraining the scope of the selection process, the right choice becomes more obvious.
How Decagon uses MCP
At Decagon, we treat MCP as a registry of tools, not as the final interface between your agent and your systems.
Tool discovery as a critical curation step
Raw MCP schemas are designed for systems, not agents. When we introspect a customer's MCP server and surface its tools, we consistently find that the schemas are structured in ways that introduce ambiguity at inference time. A tool named “updateUser” might be perfectly legible to an engineer, but to an agent reasoning over intent, it's an underspecified action space. Does it update contact information? Loyalty status? Communication preferences? That ambiguity compounds under production traffic.
Decagon addresses this through schema refinement, splitting overly generic tools into narrower, intent-scoped definitions that reduce the cognitive load on the model. Guardrails are also layered on top of MCP definitions to enforce required fields, constrain enums, and align tool behavior with global guidance specified by customers. Critically, none of this touches the source MCP server. It's all tracked in Decagon's agent versioning layer, so customers get full ownership of refinement without fragmentation.
Accuracy from constrained scope, not better selection
The single biggest driver of tool-calling accuracy is not model capability; it's how much of the tool surface the agent has to reason over at any given moment. When an agent must choose from 30+ tools on every turn, selection degrades even when only two or three are relevant. The selection problem scales with surface area.
The fix is routing logic paired with explicit, intent-scoped tool sets. Decagon implements this through
Agent Operating Procedures
(AOPs). For each AOP, customers define a constrained toolset alongside the routing logic and guardrails that govern when and how it’s invoked. The agent never operates against a flat, global list but instead, sees only what's relevant to the intent it's handling. From there, the model either selects among the narrowed tools or directly calls a specific one if explicitly instructed. At that scope, the selection problem is tractable, and the model's reasoning is precise.
Reliability through ongoing evaluation
Getting tool selection right on day one isn't enough. Prompt changes, model swaps, and schema updates all affect tool-calling behavior in ways that aren't immediately visible. Without systematic test coverage at the tool level, regressions are silent, and in a customer-facing agent, silent regressions are expensive.
Every AOP ships with evaluations that assert two things: that the correct tool was selected for a given intent, and that the correct arguments were constructed. For example, evaluation models check that the right account ID, booking reference, or currency was referenced in the tool. When an AOP or tool definition is modified, the dependent tests are re-run automatically before the change is promoted. Through built-in evaluation, tools ingested through MCP are deployed reliably at scale.
Connectivity is just the start
MCP solves a connectivity problem, but it doesn't solve the curation problem. Deciding which tools an agent should use, for which intents, and how to verify it's all working is where the real leverage is. The teams shipping reliable agents in production aren't the ones with the most integrations. They're the ones who treat tool selection as an engineering discipline: scoped, tested, and systematically improved over time.
Recent posts
Bringing the AI concierge to Australia
Decagon is opening a new office in Sydney, Australia
Introducing automatic optimization and Root Cause Analysis
Today, we’re excited to announce two new capabilities to help you rapidly improve your agent’s performance.
Bringing Decagon’s AI concierge solution to Google Cloud Marketplace
We're excited to announce that Decagon is now available on Google Cloud Marketplace.
Deliver the concierge experiences your customers deserve
Get a demo
Product
Overview
AOPs
Chat
Email
Voice
Integrations
Experiments
Insights & Reporting
Testing & QA
Watchtower
Suggestions
Trust Center
Industries
Retail
Travel & Hospitality
Technology
Financial Services
Health & Wellness
Media
Telecommunication
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
