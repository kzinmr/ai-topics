---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/deepseek-v3p1"
scraped: "2026-05-10T01:27:14.141930+00:00"
lastmod: "2026-02-12T18:51:30.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/deepseek-v3p1](https://fireworks.ai/blog/deepseek-v3p1)

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
Deepseek V3p1
DeepSeek V3.1 now on Fireworks AI!
PUBLISHED
8/26/2025
Table of Contents
TL;DR
What Makes DeepSeek V3.1 Better than V3?
DeepSeek V3.1 Variants & Modes
Example API Usage
How Does It Perform?
What Can You Build With DeepSeek V3.1?
Final Thoughts
Table of Contents
Table of Contents
TL;DR
What Makes DeepSeek V3.1 Better than V3?
DeepSeek V3.1 Variants & Modes
Example API Usage
How Does It Perform?
What Can You Build With DeepSeek V3.1?
Final Thoughts
Table of Contents
TL;DR
DeepSeek V3.1 is a major leap forward in open‑source LLMs. It introduces hybrid reasoning modes (“thinking” vs. “non‑thinking”), and reduces hallucinations by around
38%
compared to V3.
With enhanced tool integration and expanded multilingual capabilities across 100+ languages, V3.1 is optimized for real‑world, agent‑centric applications.
To truly leverage its power, especially in agentic workflows and long‑document analysis, you’ll benefit from experienced engineers integrating it with APIs, tool chains, and memory systems.
What Makes DeepSeek V3.1 Better than V3?
At its core, DeepSeek V3.1 expands on DeepSeek V3’s architecture with several major enhancements:
•
Hybrid Reasoning Modes
: Toggle between “thinking” (chain‑of‑thought) and “non‑thinking” (rapid reply) using chat templates.
•
Massive Context Capacity
: Standard 128K‑token windows, trained with 10× more data for 32K context and 3.3× more tokens in the 128K phase than V3.
•
Lower Hallucination Rates
: About
38% fewer hallucinations
, yielding more factually consistent outputs.
•
Enhanced Tool & Agent Support
: Sharper API integration, better memory across tool chains, and more reliable function calling.
•
Expanded Multilingual Support
: Gains across 100+ languages, with standout performance in Asian and low‑resource languages.
•
Optimized Architecture
: Sparse Mixture‑of‑Experts with ~685B parameters (37B active), using FP8 microscaling for performance gains.
DeepSeek V3.1 Variants & Modes
DeepSeek V3.1 ships with flexible usage modes tailored for varied tasks:
•
Thinking Mode
: Activates chain‑of‑thought reasoning ideal for math, coding, complex multi‑step logic.
•
Non‑Thinking Mode
: Optimized for low‑latency Q&A, summarization, and task completion.
Switch modes easily by selecting suitable chat templates in API calls or orchestration layers.
Example API Usage
Here’s a clean example demonstrating how you'd call DeepSeek V3.1 in “thinking mode” via Fireworks AI API:
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
import
requests
import
json
url
=
"https://api.fireworks.ai/inference/v1/chat/completions"
payload
=
{
"model"
:
"accounts/fireworks/models/deepseek-v3p1"
,
"max_tokens"
:
4096
,
"top_p"
:
1
,
"top_k"
:
40
,
"presence_penalty"
:
0
,
"frequency_penalty"
:
0
,
"temperature"
:
0.6
,
"messages"
:
[
]
,
"reasoning_effort"
:
"medium"
#Reasoning is off when set as "None" or Default
}
headers
=
{
"Accept"
:
"application/json"
,
"Content-Type"
:
"application/json"
,
"Authorization"
:
"Bearer <API_KEY>"
}
requests
.
request
(
"POST"
,
url
,
headers
=
headers
,
data
=
json
.
dumps
(
payload
)
)
This makes it straightforward to toggle reasoning behavior per request.
How Does It Perform?
In head‑to‑head benchmarks, DeepSeek V3.1 shows substantial improvement:
•
+43%
boost in multi‑step reasoning (math, logic, code) over V3
•
Stable coherence across contexts
•
38% fewer hallucinations
, enabling more reliable enterprise usage
•
Stronger multilingual accuracy, especially in Asian and low‑resource languages
These gains stem from smarter instruction tuning, expanded training corpora, and better context handling across phases.
What Can You Build With DeepSeek V3.1?
DeepSeek V3.1 is designed for impactful use cases:
•
Smart Research Copilots
that analyze entire scientific papers or books in context
•
Enterprise Agent Workflows
coordinating APIs, memory, and tool chains
•
Code Companions
capable of multistep logic, cross-file reasoning, and debugging
•
Global Conversational Assistants
supporting over 100 languages with real accuracy
•
Knowledge‑Dense Longform Tools
, e.g. summarizing legal, medical, or financial documents end‑to‑end
Final Thoughts
DeepSeek V3.1 is more than just an update, it’s a redefinition of open‑source LLM capabilities.
It enables:
•
Controlled, hybrid reasoning
•
Native million‑token memory
•
Reliable agentic and tool workflows
•
Reliable, multilingual communication
For teams building real-world, high-complexity AI applications, especially those involving reasoning, long context, or multilingual agents- DeepSeek V3.1 offers both flexibility and power at an open frontier.
Try it now on Fireworks AI:
https://fireworks.ai/models/fireworks/deepseek-v3p1
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
