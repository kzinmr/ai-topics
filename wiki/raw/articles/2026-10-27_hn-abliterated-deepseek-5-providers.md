---
title: "HN 78pts: There are now 5 inference providers for abliterated DeepSeek (allmodels.io)"
url: "https://allmodels.io/llm/abliterated"
fetched_at: 2026-10-27T11:00:00+00:00
source: "hn-discussion + allmodels.io"
hn_item: "https://news.ycombinator.com/item?id=50254836"
date: 2026-10-27
tags: [blog, raw]
extraction: partial_js_blocked
---

# There are now 5 inference providers for abliterated DeepSeek

Source: https://allmodels.io/llm/abliterated (JS-rendered shell; content reconstructed from HN item 50254836, 78 points, 2026-10-27)

## What the page shows

allmodels.io lists an **abliterated DeepSeek** offering — `deepseek/deepseek-v4.1-flash-abliterated`
("DeepSeek V4.1 Flash 1017 Abliterated", text + reasoning, image on supported routes) — as served by
**several independent providers**, with text routes kept in a fallback pool and image requests routed
only to a provider that can read them. The page title/HN headline is that there are now **5 inference
providers** serving this abliterated build, i.e. zero-alignment DeepSeek access is now commoditized
across a competitive multi-provider market rather than a single grey-market host.

The site itself is a client-rendered app; only the DeepSeek card text was recoverable server-side
("Loading live DeepSeek provider routes..."), so the provider roster itself was not captured.

## HN discussion — key positions (78 points)

- **Framing (OP)**: "Looks like the cat is out of the bag. So what does the world look like with completely open access to zero-alignment models?"
- **Deflection**: "As it should be." / "What could possibly go wrong… you are going to really need to use Rust code and other memory safe languages in your backends."
- **Refusals were already weak**: "Has anyone already seen a refusal from Deepseek? The last job Antigravity declined, I gave to Deepseek. It happily did it." Another: "I've been doing a lot with open weights models, and they just do things for you… I did get a refusal out of qwen once. Once. Over weeks."
- **Marginal value scepticism (most substantive)**: "From my testing all these variants suffer from degraded performance and don't unlock anything interesting in particular other than sounding a lot more harmful or creating manipulative media. I've actually had better success jailbreaking deepseek with a less aligned model (glm 5.2) which then allowed me to jailbreak deepseek with deepseek into pretty much doing whatever I ask… rare refusals… simply retrying a couple of times makes it work just fine. The big problem with all open-source models is once it decides to start something it will not stop mid-way."
- **Honeypot hypothesis (recurring)**: "Which if not all of these are honeypots?" / "That is a good idea for an authorities honeypot."
- **Refusals as defence-in-depth**: "if you're doing anything where your AI agent might get exposed to a prompt injection attack, you might prefer it to do a refusal in that case."
- **Mechanism question**: "Why not just distribute the refusal vectors and do it at runtime against the stock model?" (links huggingface.co/blog/mlabonne/abliteration)
- **Named hosts**: "Morph is hosting this as well."
- **Definition used in-thread**: an abliterated model is an open-weight LLM modified to remove refusal behaviour by directly editing internal weights, not via prompt jailbreaks or full retraining.

## Wiki relevance

Market-infrastructure signal for [[concepts/abliteration]] and a supply-chain complement to
[[concepts/abliterated-model-backdoor]] (Oct 21 ProjectDiscovery): the *demand* side is now large enough
to support 5 independent providers, which is the precondition for the poisoned-weight market that
ProjectDiscovery demonstrated.
