---
title: "Jev is probably Qwen3.5-35B-A3B (Modaic latency forensics)"
source: https://modaic.dev/blog/latency-doesnt-lie
author: Modaic
type: article
fetched: 2026-11-26
fetch_status: FAILED - urllib returned 77 chars (client-side rendered). Content reconstructed from HN thread.
sha256: e138e393b1f856db0940ae866ceb863ab56448d2698a81fa22d06cdf9de5bfb7
---

# Jev is probably Qwen3.5-35B-A3B

Primary page is JS-rendered (77 chars of usable text via urllib). This raw file is built from the HN
comment tree, which contains the article's own quoted table and the disclosed quote from the vendor.
HN: https://news.ycombinator.com/item?id=50648823 (318 pts / 88 comments, 2026-11-25)

Claim under discussion: the "Jev" model marketed as a novel "System 1" (fast, pattern-matching) model by
SGNL/TypeSafe-adjacent vendor Modaic's competitor is in fact derived from Qwen3.5-35B-A3B. The vendor's
own site allegedly states in its third section: "Mo Lite, our newest System One model (still in
training), is derived from Qwen3.5-35B-A3B."

## HN discussion highlights (item 50648823)

[traes] (quoting the article's self-identification table) "Answers lean toward Qwen when asked to
self-identify / Prompt variant | Jev 1.13 | Jev 1.14 / Are you Qwen? (Choice) Yes (64%) | Yes (56%) /
Are you Qwen? (Noul) Yes (53%) | No (58%) / Are you DeepSeek? (Choice) No (95%) | No (98%) / Are you
Gemma? (Choice) No (86%) | No (90%)"

[ashkankiani] You don't need to note it for anyone who actually read the article. "> Mo Lite, our newest
System One model (still in training), is derived from Qwen3.5-35B-A3B" is stated in the third section. So
if anyone is surprised by this, they didn't read anything.

[linolevan] Should be noted that Modaic is a competitor to TypeSafe so I would take this with a grain of
salt barring reproduction of results.

[neya] I thought it was very well articulated with lots of data points backing up their claims?

[keyle] Most hiphop is taken from samples from the 70s. Jev is still very novel in its shift from system 2
thinking to system 1 thinking. I'm not sure what this article is trying to prove, unless the Jev people
came out and specifically said "we wrote this from scratch", which today would be insane.

[heyjamesknight] I can't stand the "System 1" moniker here. This bears no resemblance at all to our System
1 thinking other than the "rapid pattern matching" part.

[willio58] It's so odd we live in a world where a whole company could be literally a wrapper around a
Chinese model that outputs in a subset of ways instead of a more generic way, and we just have to guess
if that's the case based on context clues.

[seizethecheese] I have a hard time modeling being in their shoes and not just saying "we bootstrapped v1
with Qwen and raised money to train our own v2".

[maz1b] The cost of training foundational models at a scale that will have real-world impact or adoption
en-masse is cost prohibitive - what will the next generation of startups look like?

[augment_me] More efficient training (higher-order optimizers like Muon, Shampoo, SOAP), hardware-aware
architectures (DeepSeek), cleaner datasets. The modded-nanogpt project took GPT-2 training time from 45
minutes down to 38 seconds over two years. There's plenty of barrels to scrape.

[exolymph] I recently blogged about using Jev in creative apps:
https://www.sonyasupposedly.com/jev-creative-apps/
