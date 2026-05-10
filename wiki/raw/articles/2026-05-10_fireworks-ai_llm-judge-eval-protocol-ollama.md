---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/llm-judge-eval-protocol-ollama"
scraped: "2026-05-10T01:21:02.826546+00:00"
lastmod: "2026-02-12T18:51:20.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/llm-judge-eval-protocol-ollama](https://fireworks.ai/blog/llm-judge-eval-protocol-ollama)

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
Llm Judge Eval Protocol Ollama
LLM on the edge: Model picking with Fireworks Eval Protocol + Ollama
PUBLISHED
10/15/2025
Table of Contents
Why this approach works
Prerequisites
Install and run Ollama
Example 1: End-to-end agent evaluation (Chinook + PydanticAI)
Example 2: Judge Langfuse traces and swap the model to Ollama
Takeaway
Table of Contents
Table of Contents
Why this approach works
Prerequisites
Install and run Ollama
Example 1: End-to-end agent evaluation (Chinook + PydanticAI)
Example 2: Judge Langfuse traces and swap the model to Ollama
Takeaway
Table of Contents
Modern AI apps rarely run on a single model forever. Teams iterate, swap providers, and increasingly run open-source models locally for privacy, latency, and cost. This post shows how to use
Fireworks Eval Protocol
to do robust model picking and how to
host models locally with Ollama
so you can replace OpenAI usage at scale—without rewriting your app logic.
We'll walk through two real examples in this repo:
•
End-to-end agent evaluation on the Chinook dataset (PydanticAI)
•
LLM-judge over Langfuse traces you already have in production
The core idea: keep your evaluation harness the same; only swap the model backend using an OpenAI-compatible endpoint (Ollama).
Why this approach works
•
Standard interface
: Eval Protocol treats models as swappable via
completion_params
(model name, provider, base_url, etc.).
•
OpenAI-compatible
: Ollama exposes an OpenAI-style API locally, so clients keep working with only config changes.
•
Evidence-based model picking
: Run apples-to-apples comparisons across datasets and traces. Keep the judge and scoring constant while changing only the model backend.
Prerequisites
•
This repo set up locally (Python environment ready)
•
macOS or Linux
•
Ollama
installed and running
Install and run Ollama
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
brew install ollama
ollama serve & disown
# Pull a model to evaluate locally (you can choose another, e.g. llama3.1)
ollama pull qwen3:4b
# Point OpenAI-compatible clients at the local Ollama server
export OLLAMA_OPENAI_BASE_URL=http://localhost:11434/v1
# Many OpenAI clients require a key even if unused by Ollama
export OPENAI_API_KEY=dummy
Example 1: End-to-end agent evaluation (Chinook + PydanticAI)
In this example, the agent is created from
completion_params
and automatically supports either OpenAI or Ollama depending on
provider
and
base_url
.
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
def
agent_factory
(
config
:
RolloutProcessorConfig
)
-
>
Agent
:
model_name
=
config
.
completion_params
[
"model"
]
provider_param
=
config
.
completion_params
.
get
(
"provider"
)
reasoning
=
config
.
completion_params
.
get
(
"reasoning"
)
settings
=
OpenAIChatModelSettings
(
openai_reasoning_effort
=
reasoning
)
base_url
=
config
.
completion_params
.
get
(
"base_url"
)
api_key
=
config
.
completion_params
.
get
(
"api_key"
)
or
os
.
getenv
(
"OPENAI_API_KEY"
)
or
"dummy"
if
base_url
or
provider_param
==
"ollama"
:
provider
=
OpenAIProvider
(
api_key
=
api_key
,
base_url
=
base_url
or
os
.
getenv
(
"OLLAMA_OPENAI_BASE_URL"
,
"<http://localhost:11434/v1>"
)
,
)
else
:
provider
=
provider_param
or
"openai"
model
=
OpenAIChatModel
(
model_name
,
provider
=
provider
,
settings
=
settings
)
return
setup_agent
(
model
)
To add a local OSS model (via Ollama), include an entry like the one below in completion_params alongside any OpenAI models you want to compare against:
1
2
3
{
"model"
:
"gpt-5-nano-2025-08-07"
}
,
{
"model"
:
"qwen3:8b"
,
"provider"
:
"ollama"
,
"base_url"
:
os
.
getenv
(
"OLLAMA_OPENAI_BASE_URL"
,
"<http://localhost:11434/v1>"
)
}
,
{
"model"
:
"qwen3:4b"
,
"provider"
:
"ollama"
,
"base_url"
:
os
.
getenv
(
"OLLAMA_OPENAI_BASE_URL"
,
"<http://localhost:11434/v1>"
)
}
,
Run the evaluation locally:
1
2
3
export OLLAMA_OPENAI_BASE_URL=http://localhost:11434/v1
export OPENAI_API_KEY=dummy
pytest tests/chinook/pydantic/test_pydantic_complex_queries.py -q
The harness executes multiple runs, collects assistant outputs, and scores them with an LLM judge, so you can compare models head-to-head with the same prompts and tasks.
From running the evaluation, we can see that qwen3:8b is actually better than gpt-4o-mini out of the box, so for this task, if I was using gpt-4o-mini, I can now just seamlessly transition to qwen3:8b local! It is definitely still worse than gpt-5-nano and other bigger model remotely. Unfortunately qwen3:4b and granite4:micro is still doing very badly on these tasks, and we really hope IBM can put out better small models for us to experiment with in the future.
Example 2: Judge Langfuse traces and swap the model to Ollama
Already logging to Langfuse? You can convert those traces into evaluation rows and judge them—then point the judge at a local model by changing only
completion_params
.
The data loader pulls traces:
1
2
3
4
5
6
7
8
9
def
langfuse_data_generator
(
)
:
adapter
=
create_langfuse_adapter
(
)
return
adapter
.
get_evaluation_rows
(
to_timestamp
=
datetime
(
2025
,
9
,
12
,
0
,
11
,
18
)
,
limit
=
711
,
sample_size
=
50
,
sleep_between_gets
=
3.0
,
max_retries
=
5
,
)
Swap in a local model by parametrizing with an Ollama-backed entry:
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
@pytest
.
mark
.
parametrize
(
"completion_params"
,
[
{
"model"
:
"qwen3:4b"
,
"provider"
:
"ollama"
,
"base_url"
:
os
.
getenv
(
"OLLAMA_OPENAI_BASE_URL"
,
"<http://localhost:11434/v1>"
)
,
}
]
,
)
The evaluation harness remains unchanged; the judge remains unchanged; your traces remain the same. Only the model backend switches, making it safe and fast to validate replacement candidates.
Takeaway
Fireworks Eval Protocol
lets you make data-driven model choices, test replacements quickly, and migrate from OpenAI to local open-source models on
Ollama
—all with minimal code changes. Keep your evaluation and logging workflows intact; just point the model at a different backend.
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
