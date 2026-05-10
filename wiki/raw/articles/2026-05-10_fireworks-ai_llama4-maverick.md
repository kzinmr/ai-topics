---
title: "Optimizing Llama 4 Maverick on Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/llama4-maverick"
scraped: "2026-05-10T01:27:52.602029+00:00"
lastmod: "2026-02-12T18:52:15.000Z"
type: "sitemap"
---

# Optimizing Llama 4 Maverick on Fireworks AI

**Source**: [https://fireworks.ai/blog/llama4-maverick](https://fireworks.ai/blog/llama4-maverick)

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
Llama4 Maverick
Optimizing Llama 4 Maverick on Fireworks AI
PUBLISHED
4/28/2025
Table of Contents
Why Llama 4 Maverick Matters
Day-1 Availability on Fireworks
The Speed Story: 145 t/s in the Real World
Native Function Calling
Table of Contents
Table of Contents
Why Llama 4 Maverick Matters
Day-1 Availability on Fireworks
The Speed Story: 145 t/s in the Real World
Native Function Calling
Table of Contents
Why Llama 4 Maverick Matters
Meta's Llama 4 Maverick is their initial natively-multimodal, Mixture-of-Experts (MoE) model.
This model processes both text and images, directing tokens through specialized expert blocks. Notably, it features a significantly expanded
context window of 1 million tokens
, a 10x increase compared to other models. This advancement allows for keeping extensive code repositories, complete product specifications, or lengthy user conversations in its memory.
Day-1 Availability on Fireworks
Minutes after Meta published the weights, the model showed up in the Fireworks AI catalogue (
accounts/fireworks/models/llama4-maverick-instruct-basic
). Early adopters, including many of the edge-AI researchers who benchmarked the model, were already hitting the endpoint before most providers finished container builds.
To enable superior performance of Llama 4 we leveraged multiple components of Fireworks Platform:
Tuned FP8 quantization scheme through
FireOptimizer
that follows recommended Llama quantization strategy (delivering both memory savings and faster generation speeds due to less memory bandwidth required)
Combination of tensor and expert parallelism depending on target workload
Custom attention implementation (
FireAttention
) that we extended to include Llama 4’s novel chunked local attention variant.
Customized speculative decoding with a drafter model trained through
FireOptimizer
Out of box support for prompt caching and prefill-heavy optimizations
Highly optimized LLM runtime that ensures sufficient batching and overlapping for fully unblocked asynchronous GPU execution 100% of time.
The flexibility of the platform enabled Fireworks AI to be the
first public Llama 4 API
.
The Speed Story: 145 t/s in the Real World
Independent testing by
Artificial Analysis
on April 27, 2025
, demonstrates that Fireworks AI delivers
145 tokens per second
for streaming throughput of
Llama 4 Maverick
, running on H200. This performance is
10-20% faster
than the closest competitor and more than double the speed of managed Azure endpoints (Artificial Analysis).
Figure 1.
Llama 4 Maverick Output-Token Speed (27 Apr 2025).
Native Function Calling
Fireworks AI exposes an
OpenAI-compatible function-calling interface
; just pass a JSON schema via tools and receive a deterministic function_call object.
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
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
import
requests
import
json
# Step
1
:
Define the
function
that the model can call
def
get_weather
(
location
:
str
)
-
>
str
:
""
"
Dummy
function
to
get
weather
for
a given location
.
In a real scenario
,
this
might call an external weather
API
.
""
"
print
(
f
"[Function] Fetching weather for {location}..."
)
# debug log
# Simulate a
result
(
in
real life
,
you'd use
`
requests
`
to an
API
here
)
# Note
:
the
return
value must be a
JSON
string
return
json
.
dumps
(
{
"temperature"
:
"25"
,
"condition"
:
"Sunny"
}
)
# pretend
this
came from a weather
API
# Step
2
:
Define the
function
schema to pass to the model
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
"Fetch the current weather for a specified city."
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
,
"description"
:
"The city for which to get the current weather"
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
#
API
endpoint and
headers
(
using Fireworks
AI
's inference endpoint
)
api_url
=
"https://api.fireworks.ai/inference/v1/chat/completions"
headers
=
{
"Authorization"
:
"<API_KEY>"
,
"Content-Type"
:
"application/json"
}
# The chat messages
for
the model
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
"What's the weather in London today?"
}
]
# Construct the payload
with
model
,
messages
,
and
function
definitions
payload
=
{
"model"
:
"accounts/fireworks/models/llama4-maverick-instruct-basic"
,
# Llama4 Maverick model
ID
on Fireworks
"messages"
:
messages
,
"tools"
:
tools
}
print
(
"[Request] Sending prompt to Llama4 Maverick..."
)
response
=
requests
.
post
(
api_url
,
headers
=
headers
,
json
=
payload
)
result
=
response
.
json
(
)
print
(
"result: "
,
result
)
# Step
3
:
Handle the model's tool call response
if
result
[
"choices"
]
[
0
]
[
"message"
]
.
get
(
"tool_calls"
)
:
func_call
=
result
[
"choices"
]
[
0
]
[
"message"
]
[
"tool_calls"
]
function_name
=
func_call
[
0
]
[
"function"
]
[
"name"
]
arguments
=
json
.
loads
(
func_call
[
0
]
[
"function"
]
.
get
(
"arguments"
,
"{}"
)
)
print
(
f
"[Model] Tool call requested: {function_name} with arguments {arguments}"
)
messages
.
append
(
result
[
"choices"
]
[
0
]
[
"message"
]
)
messages
[
-
1
]
[
"content"
]
=
""
#
this
is
because Meta's template always expect content to be not none
for
tool calls
# Execute the requested
function
if
it matches one we have
if
function_name
==
"get_weather"
:
func_result
=
get_weather
(
arguments
.
get
(
"location"
,
""
)
)
# Append the
function
result to the message history
for
the model
messages
.
append
(
{
"role"
:
"tool"
,
#
'tool'
role indicates a
function
result
"tool_call_id"
:
func_call
[
0
]
[
"id"
]
,
"content"
:
func_result
}
)
print
(
"messages after tool call: "
,
messages
)
# Now send the updated
conversation
(
with
the
function
result
)
back to the model
followup_payload
=
{
"model"
:
"accounts/fireworks/models/llama4-maverick-instruct-basic"
,
"messages"
:
messages
,
"tools"
:
tools
}
print
(
"followup_payload: "
,
followup_payload
)
print
(
"[Request] Sending tool result back to model..."
)
final_resp
=
requests
.
post
(
api_url
,
headers
=
headers
,
json
=
followup_payload
)
final_result
=
final_resp
.
json
(
)
print
(
"final_result: "
,
final_result
)
answer
=
final_result
[
"choices"
]
[
0
]
[
"message"
]
[
"content"
]
print
(
"[Model] Final answer:"
,
answer
)
If you need the fastest, largest-context, multimodal Llama 4 endpoint with production-grade function calling, Fireworks AI is the current engineering sweet spot.
Spin up the API, point your existing OpenAI client to it, and enjoy 145 tokens-per-second chat with a million-token brain:
https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic
PS: The llama4-maverick running on Serverless is on the public tier, and hence performance might vary, depending on traffic. If you intend to achieve optimal speeds, and customize for your needs, we recommend running it on on-demand deployment.
Happy building! 🚀
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
