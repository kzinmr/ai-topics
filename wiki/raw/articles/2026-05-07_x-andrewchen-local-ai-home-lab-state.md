---
source: https://x.com/andrewchen/status/2052449121982898315
author: Andrew Chen (@andrewchen)
author_affiliation: a16z speedrun
date: 2026-05-07
platform: X/Twitter
type: long-form post
tags: [local-ai, home-lab, hardware, dgx-spark, strix-halo, eGPU, openclaw, hermes-agent, ollama, vllm, litellm, qwen, gemma]
---

# Andrew Chen: Local AI Home Lab — May 2026 State

playing around with local AI models after I recently built out my home lab (DGX spark, mac mini, 5090 eGPU, strix halo framework, jet KVM etc). Running both Openclaw and Hermes Agent now. It's super fun, def recommend! Lets you geek out, learn about AI, and also buy lots of gadgets lol a few observations:

- it's great for learning about AI. Now I actually care and will try out all the new models as they come out - Qwen 3.6, Gemma 4, etc. When there's new tech like TurboQuant and DFlash, you can run them on your machine and see how it changes the performance profile

- the software stack is interesting. You can use ollama/LM studio to just dabble, but over time I have things set up with LiteLLM (as a local router for LLM queries, depending on their complexity) going to VLLM. I have a faster model (35B MoE) and then a better model (122B) depending on what I'm using it for

- the "big" local models (120B+ parameter) are slow unless you have a souped up GPU card. And not as good as the cloud LLMs. So as you tune your setup for maxing out tokens/s to make it as usable and responsive, you get a much better sense for all the tradeoffs - context window, KV cache, mem usage, mem bandwidth, parameter size, TTFT, etc

- for those (like me) coming from SOTA cloud LLMs, you can't help but compare. The open weight models are all about a year behind, but even then, as a consumer, you are generally running much smaller versions of the best local models. You probably won't use anything bigger than a ~120B parameter model (GPT OSS 120B or Qwen 3.6 122B). Local AI models running on consumer hardware have 1/100th the size, are much slower (often 30-50 tok/s versus 100+ to be usable) - but because it's been ~1year behind, it seems remarkable to think that we might be able to run Opus level local models in 2027. The latest open weight models are already pretty usable (just look at Qwen 3.6 27B dense) but its remarkable that it'll keep improving

- the hardware side is interesting. I started out with a Mac Mini, then a Nvidia DGX Spark. I also have a gaming rig. It turns out that the Mac hardware stack (particularly Mac Studios) are really good since they have pretty high bandwidth and large amounts of unified memory so you can run big models. (BUT GOOD LUCK GETTING A MAC STUDIO!). Shortages like crazy, and memory size cuts left and right. GPU cards are very fast, but only run much smaller models (24GB and 32GB are the popular consumer sizes for graphics cards), plus you have to put them in a big PC box. I got a 5090 eGPU but lots of issues with it :( . The new GB10/DGX Spark family of devices have big memory but relatively low memory bandwidth (so not the fastest tok/s) but you get CUDA and the whole ecosystem there

- the biggest use case I've found with my local AI setup has been simple: lots of summarization and analysis. I've dumped all my personal emails and blog posts and google data and created detailed month-by-month markdown files that can then be queries. Every article I bookmark or every YouTube channel I subscribe to is summarized. for me the sweetspot has been low-ish priority, asynch, and where the problem doesn't require SOTA You could argue that this is a lot of effort and $ for something that could probably be covered by my monthly GPT/Claude subscription. And that's true! But the learning is the point :)

so what's a good way to start? I think you start with whatever you have. Ideally a nice Mac M5 laptop or a gaming PC that already has a good GPU. Just set it up so it stays on, and then point some set of Openclaw jobs at it. Or if you want to invest in a new piece of hardware, the DGX Spark or Strix Halo systems are nice to be able to try out bigger models, or you can go down the rabbit hole setting up racks with GPUs etc. Either way, super fun- highly recommend

---

**Impressions**: 14.5K | **Likes**: 104 | **Reposts**: 24 | **Replies**: 97 | **Bookmarks**: 8
