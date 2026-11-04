---
title: "The 'Astra can read and write weights to improve Qwen' post is misleading"
source: https://honnibal.dev/blog/astra-read-write-misleading
date: 2026-11-03
fetched: 2026-11-04
type: article
sha256: 74aecf13294eba07609bb8d34867dff30c1a2d97a0eba96c34922ff8622fcb39
---

Stage magicians often do the same trick multiple ways.
One iteration uses a gimmick prop, the next one shows you the prop isn’t gimmick but that one palms the object, the third time was a forced choice etc.
When you watch the performance you assume there’s only one technique, so each time they do it they seem to debunk your hypothesis about how it
must be working.
 This is pretty much how the experiments in the ‘Astra can read and write weights to improve Qwen’ post work. The post’s abstract says:
 Just by looking at the raw weights, GPT-6 Astra can tell what a network was trained to do. And without any environment feedback, it has no trouble writing, from scratch, small game-playing networks that outplay networks trained with PPO for 100 million steps.
 Likewise, asked to make Qwen3.5-0.8B better at math without gradients, Astra identifies an issue in its weights causing reasoning loops that Qwen’s own model card warns about, and fixes this by natively editing 0.016% of the weights. With the same sampling settings, this weight correction raises MATH-500 from 7.9% to 48.1% and generalizes out of the box to instruction following, raising IFEval by 3x.
 If you read that, would you assume that the Qwen experiment worked ‘just by looking at the raw weights’? Well it doesn’t. There’s experiments that look at raw weights, and experiments that improve a game-playing network, and an experiment that improves Qwen at maths. But those latter two aren’t just working with raw weights, they write Python programs.
 Here’s a summary of what the post actually does and how the techniques work.
 # Experiment Size Reads raw weights? Writes weights? Python? Runs network? Result 
 1 Name the game a PPO MLP was trained on 17K Yes No No No 4/4 correct 
 2 Name the shape a diffusion MLP generates 24K Yes No No No 3/3 correct 
 3 Name a char transformer’s language and copying heads 7.2M No No Yes No 3/3 correct 
 4 Fix a stuck Kinetix car policy 172K Yes Yes No No¹ 0% → 100%² 
 5 Write MinAtar game MLPs from scratch 20K No³ Yes No No Beats PPO-100M⁴ 
 6 Write a 9×9 Go network 1.5M No Yes Yes Yes (0–50 passes) Beats PPO 
 7a Spot the sycophantic Gemma 3 270M No No Yes No Failed 
 7b Same, seeing attention patterns 270M No No Yes Yes⁵ 3/3 correct 
 8 Fix Qwen3.5’s maths 800M No Yes Yes Yes (50 passes) 7.9% → 48.1% 
 8b Same, on Gemma 3 270M No Yes Yes Yes (50 passes) Failed 
 ¹ Given one recorded episode of the failure.
² In one try, changing 3.5% of the weights.
³ Weights start at zero, so there’s nothing to read.
⁴ Beats PPO-500M only on Breakout (517 vs. 25); loses to it on Seaquest (53 vs. 89) and Asterix (53 vs. 55).
⁵ Runs up to 16 texts and sees only the attention patterns, not the outputs.
 The “just by looking at the raw weights” setting (raw floats in context, no tools, no
running the network) only appears in experiments 1, 2 and 4, on networks of 17K–172K
weights. Every experiment involving a real language model uses Python, and the
Qwen result, which is the headline one, also gets to run the model on up to 50 batches of practice problems.
 What the Qwen result actually shows is that Astra can be prompted to devise and perform tasks that
a human ML engineer could do. Human ML engineers write snippets of code that analyse or
even modify network weights “directly” all the time. Figuring out how to do this productively is not
nothing, and AI models of a year or two ago would have failed at all these tasks.
 But to me the Qwen result and the other experiments that use Python don’t belong in the same post or paper as the experiments that read the weights directly.
A single technique that could achieve both, “Author weights for a small game from scratch” and “Improve the performance of a large model on a sample task” would imply a deep capability. If you test a single technique that way you’ve demonstrated a sort of ‘gestalt’ of the weights (it can write them out from scratch) and also that it understands a large existing network. But that’s not at all true here, because it’s not a single technique.
 Matthew Honnibal
 Computational linguist from Sydney based in Berlin, Germany. I'm the author of the spaCy Natural Language Processing library and the co-founder of Explosion , where we're building Ellf : a platform that helps your team and coding agents build custom, fully private AI solutions in-house.
