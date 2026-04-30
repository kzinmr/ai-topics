---
title: "Prompt auto-caching with Claude"
source: "https://x.com/i/article/2024573404888911886"
date: 2026-04-30
type: x_article
tweet_id: "2024573404888911886"
---

TL;DR: Prompt caching  is a great way to save cost + latency when using Claude. Input tokens that use the prompt cache are 10% the cost of non-cached tokens. Auto-caching was just added to the API, which makes it easier to cache your prompt with a single cache_control parameter in the API request (docs here). Also, check out @trq212's deep dive on Claude Code's use of prompt caching and useful tips for cache-friendly prompt design.
 
The case for caching
Many AI applications ingest the same context across turns.  For example, agents perform actions in a loop. Each action produces new context. Claude’s messages API is stateless, which means it doesn’t remember past actions. The agent harness needs to package new context with past actions, tool descriptions, and general instructions at each turn.
This means most of the context is the same across turns. But, without caching, you pay for the entire context window every turn. Why not just re-use the shared context? That’s what prompt caching does. You can see on the pricing page that cached tokens are 10% the cost of base input tokens. With caching, you only pay in full for each new context block once.
 
@peakji from Manus called out the cache hit rate as the single most important metric for a production AI agent. @trq212 has noted that prompt caching is critical for long running / token-heavy agents like Claude Code. 
 
How it works
There are some great resources (e.g., here from @dejavucoder or here from @kipply) on the details of LLM inference and caching. In general, LLM inference pipelines typically use a prefill phase that processes the prompt and a decode phase that generates output tokens.
 
The intuition behind caching is that the prefill computation can be performed once, saved (e.g., cached), and then re-used if (part of) a future prompt is identical. Inference libraries / frameworks like vLLM and SGLang use different approaches to achieve this central idea.
Usage with Claude
Caching with the Claude messages API uses a cache_control breakpoint, which can be placed at any block in your prompt. This tells Claude two things. 
First, it is a “write point” telling Claude to cache all blocks up to and including this one. This creates a cryptographic hash of all the content blocks up to that breakpoint. This is scoped to your workspace.
 
Second, it tells Claude to search backward at most 20 blocks from the breakpoint to find any prior cache write matches (“hits”). The hash requires identical content. One character difference will produce a different hash and a cache miss. If there's a match, the cache is used in prefill.
 
Still, there are challenges with caching. For turn-based apps (e.g., agents), you have to move the breakpoint to the latest block as the conversation progresses. The API now addresses this with auto-caching. You can place a single cache_control parameter in your request to the Claude messages API.
 
With auto-caching, the cache breakpoint moves to the last cacheable block in your request. As your conversation grows, the breakpoint moves with it automatically. This still works with block-level caching if you want to set breakpoints (e.g., on your system prompt or other context blocks).
 
Another challenge is designing your prompt to maximize cache hits. For example, if you edit the history (see below) you risk breaking the cache.
 
This is a problem that we've tackled with Claude Code! @trq212 just shared a number of useful insights on prompt design with caching in mind.
 

