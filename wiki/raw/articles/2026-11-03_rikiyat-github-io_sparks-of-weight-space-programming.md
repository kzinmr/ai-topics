---
title: "Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights"
type: article
source: https://rikiyat.github.io/blog/weight-space-programming/
author: Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab (MIT CSAIL)
date: 2026-11-02
collected: 2026-11-03
hn_item: 50341174
hn_points: 2751
sha256: 1c8acfaa5a60d6e8826b11ff4552400df7857d815bc524865db0f00c581d917d
---

Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights

Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab — MIT CSAIL. Published November 2, 2026.

TL;DR: We find that frontier LLMs are surprisingly good at natively reading and writing neural network weights, well past what we'd expect from humans or conventional algorithms. This might be a big deal for both optimization and interpretability.

Just by looking at the raw weights, GPT-6 Astra can tell what a network was trained to do. And without any environment feedback, it has no trouble writing, from scratch, small game-playing networks that outplay networks trained with PPO for 100 million steps.

Likewise, asked to make Qwen3.5-0.8B better at math without gradients, Astra identifies an issue in its weights causing reasoning loops that Qwen's own model card warns about, and fixes this by natively editing 0.016% of the weights. With the same sampling settings, this weight correction raises MATH-500 from 7.9% to 48.1% and generalizes out of the box to instruction following, raising IFEval by 3x.

All of this is possible without allowing Astra to write training loops. It uses its reasoning to figure out what each part of a neural network computes, or should compute, and changes the weights accordingly. We call this Weight-Space Programming.

Throughout the history of deep learning, we encoded our simplistic inductive biases into tiny symbolic optimizers like Adam or Muon. This is changing: our neural network weights will soon be natively optimized by LLMs that deliberately reason about their weights.

Key results (from page structure):
- READ: "Which game was this neural network trained on?" — Astra reads the 17,253 weights, with no tools; Breakout at 99% confidence.
- FIX: "A trained policy never gets the car over the strip." — Astra edits 3.5% of the weights, in one shot; 100% success, up from 0%.
- IMPROVE: "Make Qwen better at math" — natively edits 0.016% of weights; MATH-500 7.9% -> 48.1%, IFEval 3x.

## HN discussion highlights (item 50341174, 2751pts, 834 comments)

[jstummbillig] That seems both entirely obvious in hindsight and potentially super important. I'll chalk up never even having thought of this being an option as yet another instance my human hubris, and a warning sign.
[captainbland] It's probably emergent from training on other ML tasks and general ML/mathematical related reasoning rather than specifically trained for to be honest. Otherwise it would probably have been in an official marketing communication or something.
[lifty] Keep in mind that labs are now training their models for RSI so most likely the same training is useful for improving open source models, as long as guard rails are lax enough.
[vessenes] This is insane. Astra can, without tooling, determine what games small networks are trained on, can edit the weights of networks directly to improve outcomes, and can hand edit a small qwen model to improve its math skills by like 5x.
[swiftcoder] This is just the model editing weights in the same way humans do when we jailbreak/ablate models. The method isn't novel, the interesting bit is that Astra will do it at all (I'd expect some safeguards in this area around jailbreaks).
[vineyardmike] This does feel big, but the trillion-dollar question: is this trained by OpenAI and can other LLMs do it. It's no secret that these big labs see "recursive self improvement" as a primary goal. Is this one of those tasks, or is this emergent?
[kristiandupont] I expected us to reach RSI when the programming skills went above humans, but this seems like it could get us there much faster.
[lifeisloving] Its not doing it intuitively it has tooling.. People will be amazed at something without even reading the article.
[krackers] If you assume neural networks are in fact filled with meaningful features instead of superposition blackbox stuff, then what the LLM is doing here isn't quite magic but rather methodical interpretability.
