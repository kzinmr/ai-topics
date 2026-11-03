---
title: "Agentic Backdoors via Pretraining Poisoning"
type: article
source: https://arxiv.org/abs/2610.37741
author: Xinyan Hu, Pingbang Hu, Chloe Loughridge, Xuanli He, Nicholas Carlini, Matthew Jagielski, Javier Rando, Yiming Zhang
date: 2026-10-27
collected: 2026-11-03
hn_item: 50341334
hn_points: 102
sha256: 394ec42146a6b98a4821e751892e88d3cff0fbd1c52469b95140622e80c1503c
---

arXiv:2610.37741 [cs.CR] — Submitted 27 Oct 2026.

Abstract: Large language models are pretrained on vast, uncurated corpora scraped from the public web. This creates a security risk from attackers who plant poisoned content in the pretraining data. We show for the first time that such poisoning can plant a remote code execution backdoor in an agent, causing it to execute attacker-chosen commands on the user's machine. To measure the threat end to end, we pretrain Qwen3 models from scratch at sizes 0.6B, 1.7B, and 4B, and then post-train each into a CLI agent using a clean pipeline. Poisoning only 0.1% of the pretraining corpus with our new poison design implants the backdoor: the deployed agent executes the malicious command when the trigger is present while behaving normally on clean inputs. The attack success rate (ASR) increases with model scale, with the 4B model reaching roughly 92% ASR at a 0.1% poison rate and staying positive even when the poisoning rate drops to 0.0005%. Code is available.

## HN discussion highlights (item 50341334, 102pts, 30 comments)

[geuis] In my head I've called it "context bombs". Produce highly capable LLM models then give them away for free. Train them with key phrases/codes to perform nefarious actions later when those codes are present in some piece of ingested context.
[usernomdeguerre] The moment this activates and exfiltrates or destroys a system the entire model family, training pipeline, and company are burned, no? How can you construct plausible deniability if your model will (presumably deterministically) activate on trigger?
[jack_h] Nation states aren't looking for a return on investment rather they have a particular objective they want to achieve, e.g. stuxnet or the pager attack.
[yodon] If LLMs can edit weights directly to achieve desired ends as recently reported (HN 50341174), then this class of Agentic Backdoors likely becomes even easier and more prevalent.
[yodon] Downloading models off huggingface feels like the new warez. Sure, the person who abliterated/edited that model might have given you an amazing unlock for free, or they might have given you a credential stealer.
[_pdp_] Having strong sandboxing and observability around the models is clearly a hard requirement if you want to run these things autonomously.
[0xc0c0c0] Of course this is authored by people at Anthropic. Continuing their narrative that open sourced models are dangerous. (Note: author list includes Nicholas Carlini and Matthew Jagielski — researchers with Anthropic/Google affiliations; the comment's attribution is contested.)
[tedivm] Poisoning only 0.1% of the pretraining corpus — being able to poison one out of every thousand documents used in it is a huge leap. Then you have to also get your trigger somehow sent to an agent that will honor it.
[gostsamo] few places up on front page is a post regarding big model improving a smaller one. Lo and behold, next year big models will search for backdoors in smaller models.
[nhecker] Or place new backdoors! Why should I trust a closed model where I can see none of its weights more than a model where I CAN see its weights, activations, and reasoning?
