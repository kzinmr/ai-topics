---
title: "MiniMax M3 is live: long context + native multimodality at 1/20th the price"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/minimax-m3-launch"
scraped: "2026-06-13T06:01:00.777759+00:00"
lastmod: "2026-06-12T17:20:57.000Z"
type: "sitemap"
---

# MiniMax M3 is live: long context + native multimodality at 1/20th the price

**Source**: [https://fireworks.ai/blog/minimax-m3-launch](https://fireworks.ai/blog/minimax-m3-launch)

Qwen 3.7 Plus is now available on Serverless, exclusively on Fireworks. Try it today.
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
Minimax M3 Launch
MiniMax M3 is live: long context + native multimodality at 1/20th the price
PUBLISHED
6/12/2026
Table of Contents
Why it matters: a capable new open-weight contender
MiniMax M3: by the numbers
MiniMax Sparse Attention (MSA): the architecture behind long-context
What can you build with M3 on Fireworks? Frontier Coding and Agentic Capabilities
Pricing: M3 vs. M2.7 on Fireworks
When to use M3 vs. M2.7?
Get Started with MiniMax M3 Today
Table of Contents
Table of Contents
Why it matters: a capable new open-weight contender
MiniMax M3: by the numbers
MiniMax Sparse Attention (MSA): the architecture behind long-context
What can you build with M3 on Fireworks? Frontier Coding and Agentic Capabilities
Pricing: M3 vs. M2.7 on Fireworks
When to use M3 vs. M2.7?
Get Started with MiniMax M3 Today
Table of Contents
Why it matters: a capable new open-weight contender
MiniMax M3 is MiniMax's flagship frontier model and a meaningful step forward for the open-weight ecosystem — delivering strong agentic capabilities, native multimodality, and a >500K token context window in a single model.
The open-weight frontier has been advancing quickly. Kimi K2.5 pushed the bar on native multimodal input in January 2026, natively understanding text, images, and video for visual-to-code workflows. DeepSeek V4 extended long-context capabilities with its 1M-token window in April, but remains text-input only. M3 brings that long context scaling and multimodal understanding together in one package. At launch, we're supporting up to 500K tokens of context, but are partnering closely with the MiniMax team to bring the full 1M-token context window length in the coming days.
We are launching Day-0 support for MiniMax M3 on Fireworks. Fireworks offers the fastest endpoint for the full MiniMax model series. With M3 now live, developers can immediately take advantage of its long-horizon agentic capabilities, image and video understanding, and strong context scaling for demanding production workloads.
MiniMax M3: by the numbers
MiniMax M3 sets a high bar for what open-weight models can do. Across provider-reported benchmarks and affirmed by Artificial Analysis' 3rd-party intelligence index, MiniMax M3 surpasses all other open-source models in overall intelligence and exceeds several closed-source models including Opus 4.6.
Source: https://artificialanalysis.ai/articles/minimax-m3
While benchmark fatigue is real, knowing that a model is at least on the frontier of major benchmarks remains a useful litmus for whether it's worth evaluating first-hand. In that sense, MiniMax M3 passes the first-look test.
MiniMax Sparse Attention (MSA): the architecture behind long-context
The breakthrough enabling M3's extended context window is MSA (MiniMax Sparse Attention). Standard full attention scales exponentially as context grows. MSA scales sub-quadratically by implementing a pre-filtering stage that partitions KV (key-value) caches into blocks with higher effective context coverage than approaches like DeepSeek's Sparse Attention (DSA) or Moonshot's Mixture of Blocks Attention (MoBA).
MiniMax also optimized at the operator level with a "KV outer gather Q" approach, iterating over KV blocks in the outer loop so each block is fetched from memory only once. The result:
more than 4× faster
than open-source Flash-Sparse-Attention and flash-moba, with arithmetic intensity that scales cleanly with M3's head configuration.
At its full 1M-token context ceiling, M3's gains vs. M2.7 represent a meaningful architectural step:
•
Per-token compute
dropped by 95%
•
9× speedup
in the pre-filling stage
•
15× speedup
in the decoding stage
*Note on context at launch
: The current open-weight release supports up to 500K tokens of context. This covers the majority of long-context workloads (full-repository understanding, long-document analysis, multi-turn agentic sessions) while we work to enable the full 1M-token capability. We'll update this post when that's available.
In MiniMax's own testing, MSA doesn't meaningfully hurt quality despite being computationally much more efficient. The speedup figures mean that long-context inference is viable at real-time production latency.
What can you build with M3 on Fireworks? Frontier Coding and Agentic Capabilities
M3 was built with real-world coding and agentic workflows at its core. MiniMax developed an
interactive user simulator framework
to train M3 on multi-turn development scenarios that mirror how engineers actually work: clarifying requirements, adjusting solutions, switching tasks, and iterating based on intermediate results.
To read about real-world demonstrations of M3 across multiple 12hr+ autonomous agentic tasks demonstrated by MiniMax (academic paper reproduction, kernel optimization, and model fine-tuning),
head over to the official launch post
.
As is the expectation for frontier models in June 2026, M3 goes well beyond single-turn code generation into long-horizon autonomous collaboration. It is well-suited for agentic existing and new use cases running on Fireworks today.
Pricing: M3 vs. M2.7 on Fireworks
MiniMax M3 is priced at 2x the price of M2.7 on Fireworks’
Serverless inference
:
For teams already running M2.7 workloads that would benefit from longer context, agentic execution, or multimodal inputs, M3 offers a competitive price-to-capability ratio relative to closed-source alternatives, even at the initial private launch pricing (~2x higher than M2.7). As of the open-weights launch, pricing has been permanently dropped to remain on-par with M2.7, making it a no-brainer for any developers currently running workloads on MiniMax M2.7.
•
Note on long-context pricing
:
Calls with input tokens ≤512K are billed at the standard rate. Calls above 512K are billed at a higher long-context rate, suited to workloads like full-repository code understanding and ultra-long document parsing. (Note: only <500K context is supported at launch; the higher tier will apply when full 1M support ships, and will still be ~2x higher than the lower context requests.)
•
Thinking mode
:
M3 supports toggling thinking on or off at request time, with both modes sharing the same pricing. Enable thinking for complex reasoning and agentic tasks; disable it for lower-latency scenarios like chat and code completion.
When to use M3 vs. M2.7?
M3 is the right choice when your workload demands long-horizon agentic execution, complex multi-turn coding collaboration, long-document understanding, or multimodal inputs (images and video). For tasks that are primarily text-based conversation, retrieval, or lower-latency scenarios where M2.7's capabilities are sufficient, M2.7 remains a highly cost-effective option.
For video inputs, note that currently video input is supported with URL-based uploads (raw .mp4 uploads not yet supported).
Get Started with MiniMax M3 Today
To get started, test MiniMax M3 on our chat completions endpoint. Here's a multimodal request using the Fireworks API:
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
"accounts/fireworks/models/minimax-m3"
,
"max_tokens"
:
32768
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
{
"role"
:
"user"
,
"content"
:
[
{
"type"
:
"text"
,
"text"
:
"Can you describe this image?"
}
,
{
"type"
:
"image_url"
,
"image_url"
:
{
"url"
:
"https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?auto=format&fit=crop&w=1770&q=80"
}
}
]
}
]
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
To enable thinking mode, add
"thinking": {"type": "enabled"}
to your request payload. For more details on controlling reasoning behavior,
see our docs
.
MiniMax M3 is available on Fireworks via serverless for teams that want to get started fast, and on-demand deployments for production workloads that need the best performance and predictable throughput. Start building today with strong agentic coding capabilities, 500K-token context, and native multimodality — or if you're evaluating M3 for a specific workload, we'd love to support what you're working on.
→
Start building with MiniMax M3 on Fireworks
←
Questions? Join our
Discord
or
contact us
to schedule a meeting with our solutions team.
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
