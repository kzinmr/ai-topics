---
title: "Distributing LLM inference in DwarfStar"
url: "http://antirez.com/news/167"
fetched_at: 2026-05-26T07:14:43.899177+00:00
source: "antirez.com"
tags: [blog, raw]
---

# Distributing LLM inference in DwarfStar

Source: http://antirez.com/news/167

antirez
16 hours ago. 6410 views.
High end NVIDIA cards, and the server and power needed to run them, cost a lot of money, especially if you plan to reach enough VRAM to run massive models. The alternative, so far, has been Apple hardware, or the DGX Spark that, even if severely limited because of memory bandwidth, still allows to run LLMs prompt processing (prefill) fast enough. The Mac Studio provided up to 512GB unified memory, a solution with modest memory bandwidth (but much better than the Spark) and compute at a price that was, after all, given the current situation, relatively fair.

For instance, with DwarfStar the Mac Studio M3 Ultra 512GB can run DeepSeek v4 PRO at 150 t/s prefill and ~10-13 t/s decoding, not great but at a level that is usable for certain use cases. Even 2-bit quantized, DeepSeek v4 PRO resists very well, like Flash at the same quantization (today I made PRO write a C compiler, I'll publish the video soon). I would not consider a trivial fact to run a frontier model at home, with a ~12k total spending.

One could expect this to get better and better, but the situation at the horizon appears cloudy. There is almost zero hope that NVIDIA setups will get less expensive, and even a small company can’t afford to easily purchase and handle a small data center for local inference. At the same time the RAM shortage is making it not exactly likely that we will see a Mac Studio with an M5 Ultra, maybe 1.2T/s memory bandwidth and more compute (the M5 Max is already faster, compute wise, and has the Neural Accelerators inside each GPU core that help with certain models).

So the current situation for local inference is that the best machine is probably a laptop. The M5 Max 128GB can run DeepSeek v4 Flash and Mimo V2.5, 2-bit quantized, at very decent prefill and decoding speeds. We are talking of ~500 t/s prefill and ~35-40t/s decoding speed, with a performance slope as the context size increases which is very acceptable. At the cost of 6-7k depending on the configuration, this is currently one of the best deals.

If this is the situation, for local inference projects in general, and for DwarfStart in particular, looking at distributed inference starts to be interesting. What we can do if we have two, three, four MacBook M5 Max systems? Or two M3 Ultra with 512 GB of RAM?

Traditionally there are two main systems to run distributed inference. One is to duplicate memory by loading 50% of the transformer layers in computer A, the remaining 50% on computer B, and running the inference in a sequential way. In this case there is to send just the activations around, that’s very simple conceptually, and with some micro-batching magic it is possible to not just duplicate the memory but even in theory to increase substantially the prompt processing speed (but not the decoding: for a single token generation you have to wait the first layers on machine A, the remaining layers on machine B, and so forth — but at least less heat will be produced so it is possible to use a sustained load), which is not bad at all. This means, for example, that the lucky ones that have two Mac Studio 512GB machines could run full size DeepSeek v4 PRO (even if even the 2-bit quants are running very, very well) and with micro-batching even enjoy a faster prefill.

Another approach is, using Apple RDMA, to parallelize the execution across the two machines, a vertical split basically. For instance one could try to load the same 2 bit quants on machine A and B, so that both fit, and each side has *all* the routed experts. Then for each layer we could try to do the coordination needed in order to execute half the experts in machine A, half in machine B, and so forth (note that both machines have all the experts, so whatever the router says, we can send 50% of the computation to the other machine, and the activations are tiny). This is more viable for the PRO that has much larger routed experts, so the communication penalty is less sensible. But if this could be made to work well, is all to be seen.

There is also tensor parallelism, you are thinking, right? But I bet this is not viable at all with the communication speed we have among two Apple computers, two DGX Spark and so forth (go read the speed of NVLink). The magic about the above two models is that you have to send very little data.

Ok, so far I bet you are thinking, this is the same shit everybody knows about running LLMs in a parallel fashion, and indeed this is true. But this post was conceived to reach this exact point. What about if we could, instead, parallelize two Mac or DGX in a completely different way? Open weights models are now in a golden age, we have plenty and many are very powerful. In the 128GB 2-bit quants classes there are many interesting: Minimax M2.7, Mimo V2.5, DeepSeek v4 Flash, and a few more. At the same time it was recently noted that LLMs ensemble (
https://arxiv.org/abs/2502.18036
) is an understudied possibility that allows two models to run in a completely shared-nothing way in two different machines, to only combine the logits or select the best continuation at the end. There are different ways to do that, and it works even if the two models have different vocabularies: you can pick the continuation where the perplexity is lower (that is, pick the model which is more sure: it’s like a two experts MoE where the routing is implicit), and it is even possible to combine the logits (with some complexities given by the different vocabularies) and sample from there. More recent papers suggest that mixing the two techniques is the best approach. Anyway: these techniques seem to really work, models appear to do better than alone. It’s like if their knowledge is improved because each one brings his POV on what to say next.

Maybe this is one of the most logical third approach to try, other than the first two. I really hope to find the time to play more with all that, in the next months.
