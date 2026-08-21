---
title: "Scaling real-time text-to-speech inference"
source: "Decagon Blog"
url: "https://decagon.ai/blog/scaling-real-time-tts-inference"
scraped: "2026-08-21T06:00:13.612485+00:00"
lastmod: "2026-08-20T19:04:40.029Z"
type: "sitemap"
---

# Scaling real-time text-to-speech inference

**Source**: [https://decagon.ai/blog/scaling-real-time-tts-inference](https://decagon.ai/blog/scaling-real-time-tts-inference)

Decagon Dialogues 2026 is here.
Register today
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Duet AI partner
Build
AOPs
Workflows for AI agents
Integrations
Support for tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & reporting
Voice of the customer
Watchtower
Always on QA
Suggestions
AI powered knowledge
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
Introducing Duet Autopilot: The self-improving agent for conversational AI
Learn more
Company
About
Careers
Security
Sign in
Get a demo
Sign in
Get a demo
Research & Technology
Scaling real-time text-to-speech inference
Posted on
August 20, 2026
Rohan Siva
Member of Technical Staff
Cyrus Asgari
Member of Technical Staff, Research
Article
Table of contents
Introduction
What is an Agent Engineer?
Subscribe to our Newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Must be a valid company email (i.e. example@companydomain.com)
Get a demo
Done!
Oops! Something went wrong while submitting the form.
The problem: fast text serving does not make fast speech
We got a text-to-speech model to start speaking in under 30 ms — 3× faster than our earlier interleaved baseline — while delivering nearly 10× more audio throughput.
The reason is that streaming text-to-speech isn't a single transformer forward pass. Each request processes variable-length text and reference audio, generates latent audio patches through autoregressive and flow-matching stages, and decodes them into waveform chunks. Making the whole pipeline quick requires scheduling and batching each stage independently.
To do this, we rebuilt the pipeline on M*
[1]
, a modular inference framework with scheduling, batching, caching, and streaming primitives. M* didn't support our model's autoregressive, flow-matching TTS architecture out of the box, so we built all the machinery around it: stage decomposition, packed inputs, cache and batch-state integration, causal decoder history, CUDA Graphs, and validation. We then compared four serving approaches to isolate where the gains came from:
Approach
Execution model
Main tradeoff
Sequential
One request completes before the next begins
Strong isolated-request performance; poor concurrency
Interleaved
Requests take turns one audio patch at a time
Better fairness; still batch-one execution
vLLM-Omni
[5]
General-purpose serving baseline
Native batching; higher TTFA and weaker concurrency scaling
Our native M* implementation
Stage-aware scheduling and true tensor batching
Higher capacity with additional scheduling complexity
‍
Architecture overview
Our model uses a diffusion-autoregressive architecture: the autoregressive model uses the text, reference audio, and the speech it has already generated to produce a conditioning state for the next audio patch. Flow matching then uses that state to fill in the acoustic detail by iteratively shaping Gaussian noise into an audio latent. A causal decoder then turns that latent into waveform audio, carrying its own history forward so the chunks stay continuous.
Each request starts with a prefill pass over the text and reference audio (a short sample of the target voice), which builds the attention state that generation will reuse. As the model generates audio, a KV cache keeps its autoregressive history available without recomputing it for every patch, while the decoder carries its own history from chunk to chunk.
Scheduling: one request at a time isn't enough
A typical streaming implementation uses one sequential Python loop: process the prompt, generate a latent patch, decode it, stream it, and repeat. But running these stages in sequence leaves useful parallelism on the table: while one request is decoding audio, others may already be ready to generate their next patch. We split the loop into three stages so the scheduler could run them independently:
Packed prefill
processes the reference-audio context and text prompt.
Latent generation
runs the autoregressive and flow-matching computation to produce the next continuous audio-latent patch.
Waveform decoding
passes that latent patch through the causal audio decoder to produce a playable audio chunk.
We use M* as an orchestrator so that those three stages can become two independently scheduled components. The
AR component
handles packed prefill and latent generation, including the language-model layers, flow matching and KV state. The
audio-decoder component
batches those patches, pairs each one with its request's causal history, and turns them into waveforms. Now, each side forms batches independently, works at their own pace, and releases state when they finish.
Fig. 1 — AR generation and audio decoding become independently schedulable components.
Making the full speech path batchable
Splitting the pipeline was just the first step. Each stage has its own obstacles: prompts vary in length, each request carries growing KV and recurrent state, requests advance at different rates, waveform decoding depends on earlier chunks, and new clauses need continuity from preceding audio. Here's how we tackled each one.
Packing variable-length prompts
Prompts are rarely the same length. Padding every request to the longest sequence wastes GPU work, but processing them one at a time gives up parallelism. Packed prefill gives us a third option: concatenate only the useful positions and process them in one pass. Figure 2 shows the difference.
We use sequence metadata to keep the requests separate, while endpoint tracking marks where each prompt ends. This lets the GPU see one packed batch without computing padded positions.
Fig. 2 — Packed prefill processes live prompt positions without padding every request to the longest sequence.
That removes wasted prompt work. Once generation begins, the next challenge is keeping each request's growing state resident and isolated.
Paged KV caching
Generation creates a different problem: every request carries a growing KV cache. Copying that cache whenever the scheduler reshuffles the batch would wipe out the benefit of batching.
We fix this with paged KV caching
[2]
, which keeps each request's state in reusable GPU pages instead of copying a full cache whenever batches change. M* provides the machinery to support this, but our model was built around fixed, batch-one buffers and couldn't use it directly. We replaced those buffers, adapted the model's attention path and cache layout to M*'s cache manager, and wired page ownership into each request's lifecycle. It now assigns and reclaims pages for each request, while each batch simply points to the pages it needs.
With the state staying put, the scheduler can rebuild the batch around the requests that are ready.
Continuously batching ready work
Requests don't synchronously move through the pipeline. One could be generating its fourth patch while another is generating its first. Figure 3 shows how one GPU batch can advance requests at different generation steps.
Fig. 3 — Interleaving rotates batch-one work across requests, and full-path batching advances compatible requests together.
Following the iteration-level scheduling used by systems such as Orca
[3]
, each GPU operation uses whichever requests are ready for the same work.
Each request keeps its own generation position, previous-patch conditioning, length bounds, and cache. The scheduler rebuilds each GPU batch from whichever requests are ready, drops completed requests and adds new ones. That means, for example, that eight active requests don't imply a batch size of eight for every GPU operation. From one of our runs at a concurrency of 8, the AR step averaged 3.81 requests per batch, while waveform decoding averaged 7.39 because its queue stayed fuller.
The same idea then has to work for a decoder with memory.
Isolating causal decoder history
The waveform decoder is causal, so each patch depends on earlier patches from the same request. Batching it safely means keeping those histories separate.
Before each decode, the engine gathers the ready latents with their histories, decodes them together, and returns each updated history to its owner. This gives us batched decoding without mixing context across requests.
When a request finishes, we clear its state before reusing the slot.
Chaining context across clauses
Splitting long inputs into clauses keeps speech streaming, but it creates a continuity problem. If each clause starts from only the reference voice, it loses the speaking context established by the preceding audio.
To preserve continuity, we give each new clause a short memory of the one before it. We carry over a small tail of the previous clause's audio latents, which helps maintain its rhythm and voice without carrying over all of its generation state. We save that context only after the audio has been delivered and discard it if the request is cancelled. Because we reuse the model's existing latents rather than re-encoding the waveform, the handoff only adds a little extra work.
CUDA Graphs: replaying the hot path
Batching solved the larger scaling problem, but the hot path still launched many small GPU operations. At that scale, Python dispatch and CPU-side kernel launches became measurable, especially at batch one.
CUDA Graphs
[4]
let us record a common sequence of GPU operations once and replay it with new inputs. We use them for common generation and decoding shapes, along with selected prefill shapes. Prefill graphing made the biggest difference to time to first audio because every request passes through it before producing sound.
However, graphs trade flexibility for speed: they require fixed tensor shapes and stable memory. As shown above (Fig. 3), a live batch that doesn't fill a captured bucket is padded to the next supported shape. Capturing more batch-size and prompt-length buckets reduces this padding and keeps more requests on the replay path, but increases warmup time and GPU memory use. In production, we capture the shapes that appear most often in real traffic. Requests that don't match a captured shape fall back to the eager packed path, which still preserves batching and paged KV caching.
Results: full-path batching scales with concurrency
We ran each sweep on one NVIDIA H100 and increased concurrency while comparing sequential, interleaved, and our native M* implementation, with 16 requests per prompt across four prompt-length variations.
We track five metrics:
Time to first audio (TTFA):
time from request submission until the first playable audio chunk.
End-to-end latency:
time from submission until the final audio chunk is produced.
Real-time factor (RTF):
wall-clock generation time divided by generated audio duration. Below 1 means faster than real time.
Audio throughput:
total seconds of audio generated per wall-clock second. 1 means enough capacity for one continuous real-time stream.
Request throughput:
completed requests per wall-clock second.
Fig. 4 — Serving performance across concurrency levels. Model- and configuration-specific labels have been abstracted for this draft.
Four effects stand out:
Interleaving improves fairness, not capacity.
Requests take turns reaching the GPU, but each call still processes only one request, so request and audio throughput stay flat as concurrency increases.
Our native M* implementation outperforms vLLM-Omni.
Across the tested concurrency levels, it delivers stronger request and audio throughput scaling along with lower TTFA.
Full-path batching improves concurrency scaling.
As more compatible work becomes available, our native M* implementation increases request and audio throughput, reaching roughly 10× the interleaved baseline at eight concurrent requests.
Prefill graph replay drives large TTFA gains.
The best configuration reaches roughly
27-30 ms median TTFA
, approximately
3× faster than an earlier ~95 ms interleaved baseline
, while preserving stronger throughput scaling under load.
Production tradeoffs: speed is not enough
Speed only matters if the speech stays correct and arrives smoothly. The production configuration also has to balance several competing objectives:
Warmup vs. hot performance.
Capturing more graph shapes improves steady-state coverage but increases initialization work.
Memory vs. padding.
More shapes reduce wasted rows and prompt positions but consume more GPU memory.
Coverage vs. complexity.
A small graph set is easier to validate, but a larger set keeps more traffic on the replay path.
Throughput vs. tail latency.
Briefly waiting for a better batch can increase capacity while hurting the slowest requests.
Graph replay vs. eager execution.
Eager fallback preserves correctness and broad prompt support outside captured shapes.
In production, the best configuration balances latency, throughput, output quality, and readiness rather than optimizing any one metric in isolation.
Serving speech at conversational speed
Fast TTS is not the end goal. What matters is whether a voice agent can begin speaking quickly, continue without gaps, and remain responsive as traffic changes. That is the serving layer we are building at Decagon: one that turns better speech models into better conversations.
References
M* — A serving system for modular, heterogeneous AI models.
Documentation
Kwon et al. — Efficient Memory Management for Large Language Model Serving with PagedAttention.
arXiv:2309.06180
Yu et al. — Orca: A Distributed Serving System for Transformer-Based Generative Models.
OSDI 2022
NVIDIA — CUDA Graphs.
Overview
vLLM-Omni — Omnimodal model serving framework.
Documentation
Rohan Siva
—
Member of Technical Staff
Cyrus Asgari
—
Member of Technical Staff, Research
“With Decagon Voice, we’re able to combine high performance and seamless brand customization with cross-channel memory, ensuring every interaction is connected and true to Chime’s member-first values.”
Janelle Sallenave
Chief Operating Officer
Start improving your workflow with Decagon
With Decagon, CX teams don’t have to guess whether a change will improve CSAT or deflection. They can move quickly, measure what matters, and act on what works.
Get a demo
Your browser does not support the video tag.
Join us
There are very few places where you can prototype with frontier LLMs, ship to production in days, and watch users engage with the systems you built—all while owning the entire stack, from intent parsing and tool usage to API integration and observability. This role at Decagon is one of those places.
From my own experience working across both agent development and broader engineering initiatives at Decagon, I’ve seen firsthand how uniquely impactful this work can be. Whether I’m building intelligent workflows for customers or designing infrastructure that supports our agent platform, it’s rare to find an environment where the work transitions from concept to production within days, actively powering user experiences and transforming how businesses operate.
If you’re looking for a role where you can:
Build at the frontier of LLMs, automation, and user interaction
Deploy AI agents that solve high-value business use cases across industries including retail, travel and hospitality, fintech, edtech, and more
Work directly with customers on high-impact use cases
Ship fast, iterate constantly, and own your work from idea to production
Join a fast-moving, collaborative team solving real-world challenges with AI
We’d love to hear from you!
Explore careers
Related posts
Research & Technology
Teaching flow-matching text-to-speech models with RL
Posted on
August 18, 2026
Research & Technology
How we debugged a latent PgBouncer bug across four layers of the stack
Posted on
August 5, 2026
Research & Technology
What an air-gapped AI deployment actually requires
Posted on
July 9, 2026
Explore more topics
AI agent building
Test & experimentation
Analytics & Voice of Customer
Voice & omnichannel support
Guardrails, security, & governance
Use cases & experiences
Workplace
The AI concierge for every customer.
Get a demo
Footer
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
