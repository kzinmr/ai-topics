---
title: "Introducing Ternary Bonsai 2.5 27B: Powering Agentic Coding and Private Knowledge Work"
created: 2026-11-25
updated: 2026-11-25
type: article
source: "https://prismml.com/news/bonsai-2-5-27b"
status: complete
sources:
  - "https://prismml.com/news/bonsai-2-5-27b"
  - "https://news.ycombinator.com/item?id=50633922"
sha256: dbcdc8d54afb027f353cca9aaed9fded917e2b46a3c8bf8bef499d42e538feb2
---

# Introducing Ternary Bonsai 2.5 27B: Powering Agentic Coding and Private Knowledge Work

Source: https://prismml.com/news/bonsai-2-5-27b

## Article

PrismML — Introducing Ternary Bonsai 2.5 27B: Powering Agentic Coding and Private Knowledge Work 

 About
 Blog
 News
 Careers
 Docs

 LAUNCH 

 1001011100 001011 110

 Back to all posts
 
 Introducing Ternary Bonsai 2.5 27B: Powering Agentic Coding and Private Knowledge Work
 
 November 24, 2026
 •
 PrismML

 Today, we’re introducing Ternary Bonsai 2.5 27B, an upgrade to Ternary Bonsai 2 27B with substantially stronger agentic coding, multi-turn tool use, and multi-step task execution. Based on Qwen3.8 27B, it retains the previous release’s 5.9 GB model footprint while significantly improving the capabilities developers need to build agents that work with private files and tools on-device. The result is by far the strongest AI model of its memory footprint for agentic workloads.
 With Ternary Bonsai 2 27B , we brought stronger reasoning, visual understanding, and tool use to local devices. Since then, we’ve focused on making the model more effective across long sequences of tool calls: interpreting results, adjusting when a step fails, and maintaining the task’s objective through the whole interaction. This release also continues our work to make Bonsai more practical by addressing excessive thinking and repetitive loops in the previous model. Compared with Ternary Bonsai 2, Ternary Bonsai 2.5 completes tasks in fewer turns, uses fewer tokens, and delivers results faster and more accurately.
 Agentic workflows are particularly sensitive to model degradation: small errors can compound across successive tool calls and derail an entire task. Ternary Bonsai 2.5 significantly narrows the performance gap to the full-precision base model while retaining its compact footprint. Preserving this behavior through longer tasks is an important milestone in improving the intelligence density of models.
 We evaluated Ternary Bonsai 2.5 27B against both Ternary Bonsai 2 27B and the full-precision Qwen 3.8 27B base model, as reported in the full whitepaper . We see marked improvements in agentic execution, coding, and multi-turn tool use, as shown in the table below.

 Benchmark Qwen3.8 27B Bonsai 2 27B Bonsai 2.5 27B 
 
 SWE-bench Verified 80.6 60.8 75.6 
 DeepSWE v1.1 (mini-swe-agent) 30.1 0 27 
 Terminal-Bench 2.1 70.8 52.8 60.1 
 AppWorld 93.2 51.2 90.5 
 τ³-Bench 72.8 69.1 73.9 
 BigCodeBench 61.5 57.2 60.3 
 LiveCodeBench v6 87.6 83.8 83.0 

 On a single NVIDIA H100, Ternary Bonsai 2.5 27B achieves a generation speed of 291 tokens/s with MTP and processes a 2,000-token prompt at 3,200 tokens/s. Even on a consumer-grade RTX 4090, it delivers 204 tokens/s with MTP and a prompt processing speed of approximately 3,060 tokens/s. The demos below follow complete local workflows, from the initial request through intermediate decisions to the final result.

 Demo I: Reproducing and fixing a pytest regression with Bonsai 2.5 27B

 Demo II: Rebuilding a web page from a screenshot with Bonsai 2.5 27B

 ‹ › 

 For products, this creates room to build assistance directly into the applications where work already happens: a coding assistant working through issues in a private repository, a document application that prepares reviewable summaries, or a desktop assistant that handles recurring analysis. Local deployment lets those products process sensitive material on the user’s device. Ternary Bonsai 2.5 27B strengthens the model capabilities behind that experience while keeping the compact footprint that makes it practical.
 Platform Coverage 
 Ternary Bonsai 2.5 27B runs on NVIDIA and Intel GPUs via llama.cpp and on Apple devices (Mac, iPhone, iPad) via MLX.
 Model weights are available today under the Apache 2.0 License.
 Full technical details of our compression, evaluation, and benchmarking processes are available in our whitepaper .
 Work with Us 
 We work with teams to tailor Bonsai models to their applications, from post-training on domain-specific data to optimizing inference for target hardware. If you’re building AI products with tight memory, latency, or power requirements, we’d love to explore how Bonsai can help. Reach out at sales@prismml.com .
 Join Us 
 Prism ML emerged from a team of Caltech researchers and was founded with support from Khosla Ventures, Cerberus, and Google, with continuing support from Samsung. We've spent years tackling one of the field's hardest problems: compressing neural networks without sacrificing their reasoning ability.
 If you want to help build the next generation of state-of-the-art AI, we'd love to hear from you. Check out our careers page.

 Back to all posts

 PrismML Launches Bonsai 2 27B, Its Most Capable Model Yet
 September 17, 2026
 New flagship model brings 27B-class reasoning, coding, vision, and agentic capability into a dramatically smaller, faster deployment footprint
 
 Introducing Ternary Bonsai 2 2B, 4B, and 9B: Bringing Local Agents to Everyday Devices
 October 15, 2026
 Today, we’re expanding the Bonsai 2 family with three new ternary models based on Qwen3.5: Ternary Bonsai 2 2B, 4B, and 9B.

 Thanks, we’ll keep you posted!

 Something went wrong.

 Resources
 Demo
 Whitepaper
 Docs

 Models
 Hugging Face
 GitHub

 Follow
 X
 Discord
 LinkedIn

 Contact us
 
 Have a question, partnership idea, or a project that needs efficient intelligence? Reach out—we’d love to hear from you.

 Reason for contacting General inquiry Partnerships Press Technical issues Other 
 Thanks, your message has been received!

 Oops! Something went wrong while submitting the form.

 Reason for contacting General inquiry Partnerships Press Technical issues Other 
 Thanks, your message has been received!

 Oops! Something went wrong while submitting the form.

## HN discussion highlights (item 50633922)

# HN bonsai — Ternary Bonsai 2.5 27B (471 pts, item 50633922)
# url: https://prismml.com/news/bonsai-2-5-27b

[nik_s] Unless I'm totally mistaken, this scores equivalent to opus 4.6 (released feb 2026) on SWE-bench verified. I'd be curious to which extent this is Ternary Bonsai bechmaxxing, the underlying benchmark moving, or just us seeing frontier-like behavior on benchmarks in tiny models with a ~6 month lag: probably a bit of all three? I'll be the first to say that SWE-bench verified is clearly not the most representative of benchmarks sadly, but progress in small models is really exciting nevertheless!
[dofm]   My neighbour's cat scored equivalent to Opus 4.6 this week. Like, seriously: I would be prepared to bet that the experience with this model, impressive though it is, does not match Opus 4.6 in practical use. Same with Inkling 2 Mini. Is it very good? Yes, it's really very good for an MoE. Are there speed improvements to come: yes. Is it entirely worth the hype: no. This is a cycle and we should be wary of it. It will go into overdrive if Alibaba can find enough GPUs to finish Qwen 4 27B. (I use only open weights)
[dimator]     If this is true, of what utility are all these benchmarks at this point? Is the only alternative really for everyone to try a model themselves and judge it against exactly what they're doing?
[UncleOxidant]     > if Alibaba can find enough GPUs to finish Qwen 4 27B. Does Alibaba have a shortage of GPUs to finish Qwen 4 27B?
[iagiagiag]     > I would be prepared to bet that the experience with this model, impressive though it is, does not match Opus 4.6 in practical use. You would need to provide the same harness to the model though.
[motbus3]     Bro benchmarking is on the rise but to give a reason of a doubt I used a previous version of bonsai model and it was seemingly good for its size.
[ekidd]     > Like, seriously: I would be prepared to bet that the experience with this model, impressive though it is, does not match Opus 4.6 in practical use. I suspect that there are local models that match Opus 4.6 in practical use, but I doubt that Ternary Bonsai or Inkling 2 Mini meet that threshold. Those two are both weaker than Qwen3.8 27B (6 bit quants or above) in practice. Qwen3.8 27B is pretty clearly stronger than Sonnet 4.5. Whether it beats Opus 4.5 might come down to matters of taste. There's a larger tier of models—Qwen3.8 Flash Next, DeepSeek V4 Flash and Hy4 Flash—that you can just ru
[jonahx]     > (I use only open weights) As an open-weight curious person, how do the best open-weight models compare with frontier stuff like Astra/Fable?
[zmmmmm]   Previous iteration of this got some hype but in actual quality people found it to be incredibly bad. Hope this one is better, but won't be jumping in until I hear confirmation from others. Currently I am able to run Qwen 3.8 using the byteshape quant very satisfactorily with < 16GB VRAM with close to full quality at 40-50 tps - I don't see too much reason to shift from that.
[dofm]     It feels superficially good actually — but it seems to overthink even on Low reasoning mode (unless maybe the chat template is broken and the reasoning effort selector in Unsloth Desktop isn't working — I need to test that) I think there will at some point be merit in a test that compares this, other low-bit quants of 27B, Nemotron Bolt and Inkling 2 Mini. Because the challenge is only to find the best model that fits in those smaller spaces. I think if one has the resources to run really any Q4 version of Muse Glimmer or the Ukisa or BottleCap versions of 27B, it's automatically better to do 
[serf]     my previous bonsai experience : it was good and fast until it got caught in a death loop, which was often, so it needed a lot of babysitting. qwen3.8 27b variants are a lot better in the death-loop department, "But wait.."; it tends to catch itself repeating, the older bonsai model just filled text buffers until terminated. very fast though. it flies on RTXs.
[vegnus] So if I run 4 bonsais will that give me better results than Qwen 3.8 27b? Qwen is obviously cool but I could never really get anything useful out of it, over a number of different experiments
[NoidFonsense]   Why not run 4x Qwen 3.8 27b in parallel? If you want more intellegence at only slightly more memory and flops, at the cost of greater latency. Use llama.cpp's --parallel flag for instance, you will find that the aggregate t/s increases with more requests in parallel. If you can run qwen 3.8 27B at q4 already, this model is not for you. Wrong tradeoffs. Also you do not need 4x the memory to run the same model 4x in paralell, thats your other wrong assumption. Good question though.
[onaclov2000]     I could be mistaken but the problem I ran into with parallel is that it reduced the context I had available per process. Dunno, yes it went faster but I had to get what I needed done in less context (dual 16gb GPUs, running 4 bit quant, and mtp/speculative decoding)
[codazoda]   I feel like I can get these to work but they require a bit more tuning of prompts and instructions than I’m willing to spend time on at the moment. Love the idea and eventually I’ll have time. I wrote a bit about my first successful run. https://joeldare.com/a-local-open-weight-model-builds-its-fi...
[nl]   > So if I run 4 bonsais will that give me better results than Qwen 3.8 27b? No, you'll just get 4x the wrong answers.
