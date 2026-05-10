---
title: "Qwen 3 on Fireworks AI: Controllable Chain-of-Thought and Tool Calling at Frontier Scale"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/qwen-3"
scraped: "2026-05-10T01:27:21.111367+00:00"
lastmod: "2026-02-12T18:52:14.000Z"
type: "sitemap"
---

# Qwen 3 on Fireworks AI: Controllable Chain-of-Thought and Tool Calling at Frontier Scale

**Source**: [https://fireworks.ai/blog/qwen-3](https://fireworks.ai/blog/qwen-3)

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
Qwen 3
Qwen 3 on Fireworks AI: Controllable Chain-of-Thought and Tool Calling at Frontier Scale
PUBLISHED
5/6/2025
Table of Contents
TL;DR
Why this release matters ?
15-second quick-start
Under the hood: The Hybrid Thinking Switch
Model card (Fireworks hosted)
Performance tips
Using the Fireworks endpoint
Closing thoughts
Table of Contents
Table of Contents
TL;DR
Why this release matters ?
15-second quick-start
Under the hood: The Hybrid Thinking Switch
Model card (Fireworks hosted)
Performance tips
Using the Fireworks endpoint
Closing thoughts
Table of Contents
TL;DR
•
Reasoning meets function calls.
Qwen 3 now streams an explicit … trace
and
the exact JSON tool call in the same completion.
•
Turbo or stealth—your choice.
Flip reasoning_effort="none" (or use the /think / /no_think tags) to trade transparency for raw throughput on the fly.
•
Mixture-of-Experts giant, pay-as-you-go.
The 235 B-parameter / 22 B-active
Qwen3-235B-A22B
runs serverlessly on Fireworks.
•
Drop-in OpenAI compatibility.
Use the Fireworks endpoint with the official OpenAI client; everything else stays the same.
Why this release matters ?
Until now, open-source LLMs forced a choice:
show the chain of thought
or
call tools deterministically
. Qwen 3’s new architecture does both in one pass, and keeps the reasoning block segregated so downstream code can ignore or audit it at will.
Pair that with a
128-expert MoE
that only activates eight experts (≈22 B live parameters) and you get near-frontier quality at a fraction of the compute- fully Apache-2.0 and live on Fireworks today (
Fireworks - Qwen3 235B-A22B model
).
15-second quick-start
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
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
from openai
import
OpenAI
import
os
,
json
client
=
OpenAI
(
base_url
=
"<https://api.fireworks.ai/inference/v1>"
,
api_key
=
os
.
environ
[
"FIREWORKS_API_KEY"
]
,
)
messages
=
[
{
"role"
:
"user"
,
"content"
:
"What’s the weather in Boston today?"
}
]
tools
=
[
{
"type"
:
"function"
,
"function"
:
{
"name"
:
"get_weather"
,
"description"
:
"Return current weather for a US city"
,
"parameters"
:
{
"type"
:
"object"
,
"properties"
:
{
"location"
:
{
"type"
:
"string"
}
}
,
"required"
:
[
"location"
]
}
}
}
]
# Reasoning based tool calls
resp
=
client
.
chat
.
completions
.
create
(
model
=
"accounts/fireworks/models/qwen3-235b-a22b"
,
messages
=
messages
,
tools
=
tools
,
max_tokens
=
4096
,
temperature
=
0.6
,
)
first
=
resp
.
choices
[
0
]
.
message
print
(
first
.
content
)
# contains
<
think
>
…
<
/
think
>
print
(
first
.
tool_calls
)
# Non
-
reasoning based tool calls
resp
=
client
.
chat
.
completions
.
create
(
model
=
"accounts/fireworks/models/qwen3-235b-a22b"
,
messages
=
messages
,
tools
=
tools
,
max_tokens
=
4096
,
temperature
=
0.6
,
extra_body
=
{
"reasoning_effort"
:
"none"
,
}
,
)
second
=
resp
.
choices
[
0
]
.
message
print
(
second
.
content
)
# does not contain
<
think
>
…
<
/
think
>
print
(
second
.
tool_calls
)
The first call contains reasoning chain of thought + tool call, the second doesn’t think, and just makes the tool calls.
Under the hood: The Hybrid Thinking Switch
•
Thinking mode
(
reasoning_effort!=”none”
)
•
Generates
<think> … </think>
and a final answer.
•
Recommended params:
temperature ≈ 0.6, top_p ≈ 0.95, top_k = 20
.
•
Non-thinking mode
(
reasoning_effort=”none”
or a
/no_think
tag)
•
Omits the reasoning block to save tokens and latency.
•
Use slightly spicier sampling:
temperature ≈ 0.7, top_p ≈ 0.8
.
Because the trace sits in its own tag, you can log, redact, or meter it independently- the same pattern we covered in
Constrained Generation with Reasoning
.
Model card (Fireworks hosted)
-
Qwen 3-235B-A22B
Total parameters
235 B (Mixture-of-Experts)
Active parameters
22 B (8 / 128 experts)
Layers
94
Attention heads
64 / 4
Context window
32 768 tokens (native) 131 072 with YaRN
License
Apache-2.0
Endpoint
accounts/fireworks/models/qwen3-235b-a22b
Performance tips
•
Long answers
– Allocate at least 4 k output tokens for essays; up to 32 k for book-length generations.
•
Cost & speed control
– Invoke reasoning only on the turns that need it, then strip
<think>
before storage.
Using the Fireworks endpoint
Our endpoint is fully OpenAI compatible, please give it a try!
1
2
3
4
5
6
7
8
curl https
:
/
/
api
.
fireworks
.
ai
/
inference
/
v1
/
chat
/
completions \
-
H
"Authorization: Bearer $FIREWORKS_API_KEY"
\
-
H
"Content-Type: application/json"
\
-
d '
{
"model"
:
"accounts/fireworks/models/qwen3-235b-a22b"
,
"messages"
:
[
{
"role"
:
"user"
,
"content"
:
"Translate 这本书多少钱？"
}
]
,
"reasoning_effort"
:
"none"
}
'
Closing thoughts
With
Qwen 3-235B-A22B
, open-source finally gets a model that:
Reveals its chain of thought when you ask.
Emits tool calls in the exact same request.
Scales to frontier-size contexts- all under Apache-2.0.
No secret weights, no bespoke SDKs. Just point your existing OpenAI-style client at Fireworks and build.
Questions, feedback, or cool demos? Drop by our
Discord
or tag us on X.
Happy shipping!
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
