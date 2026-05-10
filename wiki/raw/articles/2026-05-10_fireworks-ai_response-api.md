---
title: "Unlock Your Tools: Fireworks Adds OpenAI-Response API with MCP Support (Beta)"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/response-api"
scraped: "2026-05-10T01:27:17.449066+00:00"
lastmod: "2026-02-12T18:51:59.000Z"
type: "sitemap"
---

# Unlock Your Tools: Fireworks Adds OpenAI-Response API with MCP Support (Beta)

**Source**: [https://fireworks.ai/blog/response-api](https://fireworks.ai/blog/response-api)

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
Response Api
Unlock Your Tools: Fireworks Adds OpenAI-Response API with MCP Support (Beta)
PUBLISHED
6/22/2025
Table of Contents
The Unconnected LLM: A Walled Garden
Introducing an Open Bridge: The Fireworks Response API with MCP
Why MCP on Fireworks
How it Works: Connecting a Model to a Tool
What Can You Build with MCP?
Get Started Today
Table of Contents
Table of Contents
The Unconnected LLM: A Walled Garden
Introducing an Open Bridge: The Fireworks Response API with MCP
Why MCP on Fireworks
How it Works: Connecting a Model to a Tool
What Can You Build with MCP?
Get Started Today
Table of Contents
TL;DR:
Fireworks now supports an OpenAI-response API endpoint that allows you to connect our library of leading open models to your own tools and data using the open
Model Context Protocol (MCP)
.
The Unconnected LLM: A Walled Garden
Large Language Models are incredibly powerful, but out of the box, they exist in a vacuum. They can't check your inventory, update a customer's order, or query your internal database. To make them truly useful for your business, they need to securely interact with your proprietary APIs, tools, and data sources.
Historically, this required developers to build complex, brittle "glue code." You'd have to orchestrate a multi-step dance: prompt the model, parse its output to see if it wants to use a tool, make the API call yourself, and then feed the result back to the model. This process is slow, error-prone, and a significant engineering bottleneck that stifles rapid product development.
Introducing an Open Bridge: The Fireworks Response API with MCP
We're thrilled to announce a powerful new capability to solve this challenge:
Fireworks now supports an OpenAI-compatible Responses API, with first-class support for the Model Context Protocol (MCP).
MCP is an open protocol that standardizes how applications provide context and expose tools to LLMs. Think of it as a universal adapter, creating a seamless and secure bridge between a language model and any external system. Instead of being locked into a proprietary set of tools, you can now connect any model on Fireworks to any tool you build, as long as it speaks MCP.
This new endpoint handles the entire agentic loop—reasoning, tool selection, and execution—server-side, allowing you to build sophisticated applications with a single, elegant API call.
Why MCP on Fireworks
Bringing an open protocol like MCP to our platform helps developers on Fireworks to:
•
Connect Any Open Model to Your Tools:
Take state-of-the-art open models like
Qwen 3, DeepSeek or Llama 4
and connect them directly to your business logic. Empower a Llama model to interact with your Shopify store, or have Qwen query your internal Jira instance. State will also be managed on the Fireworks server side, so you don’t have to worry about managing a long conversation with LLMs with chat completion API anymore.
•
Break Free from Vendor Lock-in:
MCP is an open standard. The MCP server you build for your tools is portable. You’re not tied to a single model provider’s ecosystem. This gives you the freedom to choose the best model for the job, today and tomorrow, without rebuilding your tool integrations.
•
Supercharge Your Custom Models:
The possibilities are explosive when you combine this with custom models. Use our
Supervised Fine-Tuning V2
and
Reinforcement Fine-Tuning
to train a model that understands your company’s unique terminology, and then give it access to your internal tools via MCP. This creates a hyper-specialized and immensely capable agent.
How it Works: Connecting a Model to a Tool
Integrating your tools is now stunningly simple. You just need to tell the model the location of your MCP server. The model will then be able to discover and call the tools it provides.
Here’s a quick example of how you can get
qwen3-235b-a22b
to answer up-to-date questions about our latest open source project
reward-kit
that was released only last week and hence is not in the model’s training data. All you need is to add the
gitmcp
server in the request:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
from
openai
import
OpenAI
# Point the client to the Fireworks API
client
=
OpenAI
(
base_url
=
"https://api.fireworks.ai/inference/v1"
,
api_key
=
"YOUR_FIREWORKS_API_KEY"
,
)
# Example 1: Basic Documentation Query
# Ask about reward-kit's key features using GitMCP
response
=
client
.
responses
.
create
(
model
=
"accounts/fireworks/models/qwen3-235b-a22b"
,
input
=
"What is reward-kit and what are its 2 main features? Keep it short Please analyze the fw-ai-external/reward-kit repository."
,
tools
=
[
{
"type"
:
"sse"
,
"server_url"
:
"https://gitmcp.io/docs"
}
]
)
print
(
"🔍 Query: What are the key features of reward-kit?"
)
print
(
"="
*
60
)
print
(
response
.
output
[
-
1
]
.
content
[
0
]
.
text
.
split
(
"</think>"
)
[
-
1
]
)
print
(
"="
*
60
)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
🔍 Query: What are the key features of reward-kit?
============================================================
reward-kit is a tool for authoring, testing, and deploying reward functions to evaluate LLM outputs. Its 2 main features are:
1. **Easy-to-use Decorator (`@reward_function`)**
Simplifies reward function creation by annotating Python functions with validation metrics and evaluation logic (e.g., `def exact_tool_match_reward(...)` for tool-call validation).
2. **Flexible Multi-Metric Evaluation**
Supports custom metrics (e.g., word count, specificity markers) and integrates with external libraries like DeepEval/GEval for LLM-as-a-judge scoring. Evaluation results include granular metric breakdowns.
The toolkit also enables local testing, dataset integration, and deployment to platforms like Fireworks AI.
============================================================
Behind the scenes, the model identified the user's intent, discovered the tool for fetching GitHub repo documentation via an MCP server, called it with the correct parameters, and used the result to formulate its final response...all in one API call!
What Can You Build with MCP?
This unlocks a new class of applications built on open models:
•
E-commerce Automation:
Build agents that check inventory, process returns, or apply discount codes by connecting directly to your Stripe, Shopify, or custom e-commerce backend.
•
Internal Operations Bots:
Create a Slack bot that can file bug reports in Jira, create pages in Confluence, or query your internal HR systems, all through a secure, company-specific MCP server.
•
Data-Driven Assistants:
Connect a model to your company's databases and data warehouses via an MCP interface. Allow your business teams to ask natural language questions like, "What were our top 10 selling products in Europe last quarter?"
Get Started Today
The future of AI is not just about better models; it's about better-connected models. By embracing open standards like MCP, we're giving you the power to integrate the best open-source AI deeply into your own products and workflows.
•
Dive into our API documentation to learn more.
•
Learn how to build your own MCP server with this guide from Cloudflare.
•
Explore compatible models in our Model Library.
We can't wait to see what you build. Note that this is a preview feature from Fireworks, we would love to hear your feedback.
Start building today!
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
