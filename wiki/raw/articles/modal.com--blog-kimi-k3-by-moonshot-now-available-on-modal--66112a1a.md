---
title: "Kimi K3 by Moonshot now available on Modal"
url: "https://modal.com/blog/kimi-k3-by-moonshot-now-available-on-modal"
fetched_at: 2026-07-28T10:08:51.539398+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Kimi K3 by Moonshot now available on Modal

Source: https://modal.com/blog/kimi-k3-by-moonshot-now-available-on-modal

Today
Moonshot released Kimi K3
, a 2.8 trillion parameter multimodal model with a 1M token context window and native vision. And Modal runs it at 460 tokens per second, on release day.
We partnered with Moonshot and vLLM on day zero support, making K3 available with token-based pricing on our Shared API, and as an Auto Endpoint for dedicated capacity, alongside a custom-trained
DFlash
speculator tuned to K3's architecture.
Try it now
or read on for why we think this model, and its architecture, matter.
Frontier, open, fast. Pick three.
Kimi K3 is the strongest open model on public intelligence indexes, fourth overall in a leaderboard dominated by closed source models.
K3 is a mixture-of-experts transformer: 2.8T total parameters, 16 of 896 experts active per token, a 1M token context window, and native vision. It's built for long-horizon agentic work, and Moonshot put that to the test internally, handing an early version most of the team's kernel optimization work during development. Kimi Delta Attention holds down the cost of attention as sequences grow, and Attention Residuals let deeper layers reach back to earlier attention outputs rather than only the layer below, which together give roughly 2.5x the scaling efficiency of K2.
What it doesn't give you is a model that's easy to run, and Moonshot spent a lot of the architecture on that problem too. They did quantization-aware training from the SFT stage onward with MXFP4 weights and MXFP8 activations, so the model runs on a wide range of hardware, and they rebalanced expert parallelism to keep throughput up at large scales. When KDA turned out to break conventional prefix caching, they wrote a new implementation and contributed it to vLLM ahead of the release. It's a lot of unglamorous work in service of people who aren't Moonshot, and it's the reason a 3T-class open model is servable at all.
For endpoints on Modal, we took this even further with Day 0 support for a custom DFlash speculator tuned to K3's shape. K3 generates a large number of tokens per task, which means most of the time a user spends waiting is decode time, and decode is what speculation speeds up.
On agentic workloads, that's a huge difference:
360% faster interactivity (from 100 to 460 tokens per second)
88% higher throughput (from 800k to 1.5 million TPM per GPU)
Frontier models need frontier speculation
K3 is the largest target we've trained a speculator against.
Custom draft model architectures like DFlash can drastically accelerate production inference, especially when carefully trained. DFlash training is mainly a data generation problem, since the teacher is the target model. The final run used 32 B300 nodes: 28 running K3 at TP8 to produce hidden states, 4 training the draft model against them.
There were a lot of design decisions behind this drafter, which we look forward to sharing more about in a forthcoming post. In the meantime, we've written at length about
why we're all-in on speculative decoding
.
Run Kimi K3 on Modal
Kimi K3 is available today as an OpenAI compatible Shared API with token-based pricing, or as a dedicated Auto Endpoint.
It's covered by Modal's standard offer: $30 of free compute every single month, so you can keep using K3 on the Shared API for free, month over month.
Try it today
and let us know what you think!
