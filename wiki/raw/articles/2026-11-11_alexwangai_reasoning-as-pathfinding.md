---
title: "What objective is reasoning solving? (reasoning as pathfinding)"
source: https://alexwang.ai/posts/reasoning-as-pathfinding/
author: Alex Wang
published: 2026-11-10
ingested: 2026-11-11
type: blog-post
hn: https://news.ycombinator.com/item?id=50445013
sha256: 48dc3733814e27c3ca0c142d5c8f2fdf5b71d2474aa106b64ce7c1846c3f1f83
---

What objective is reasoning solving? — alexwang.ai, 2026-11-10

(Full text fetched 2026-11-11; core model as follows — reasoning as pathfinding through token space.)

Model: pretraining creates a bias towards correct answers with each inference step (training data is mostly human-judged-good completions, so random walks drift toward correct-answer regions without the model representing "correct"). Because verification is easier than generation, a longer walk is more likely to land in a verifiably-correct region. RL training spends enormous compute *searching* for successful paths and then trains the model to reproduce them: "RL training directly raises the success probability, by spending a lot of compute on searching for successful paths and then training the model to reproduce them. The gains we credit to 'thinking longer' come from the search we paid for during training, rather than at inference."

Implication: test-time thinking largely re-traverses paths discovered during training search; more inference tokens ≠ more intelligence in any fundamental sense.

## HN discussion highlights (item 50445013, 147pts, 67c)

- [dogscatstrees] Wang's argument contradicts the view that intelligence necessarily improves through more reasoning and undermines any assumption that recursive self-improvement (RSI) will automatically converge toward greater intelligence.
- [NickNaraghi] "reasoning as pathfinding through token space" — sounds like hillclimbing all the way down! Excited for the parallel construction of ___ as pathfinding through weight space.
- [akavi] Intuitive reconstruction: 1) pretraining biases toward correct answers per step; 2) a longer walk is likelier to land in the correct region since verification is easier than creation; 3) RL selects walks landing in the correct region and tilts the distribution toward them; 4) by (2), that trains toward longer walks.
- [jebarker] Yes — but the model isn't really learning what correct/incorrect means in any way a human would consciously think about it.
- [derefr] It solves the same thing a human "train of thought" (internal vocalization) solves: it's faster and cheaper to acquire memories-of-words than entire new skills, so reasoning bubbles those memories up into something like skill.
- [trinari] Does that lead to much inside-the-box thinking by models? Do they try to follow the clearest path?
- [HarHarVeryFunny] During training you find paths to success and reinforce them; there's a minimum-length path if the model generates semblance of real reasoning, but many longer ones via backtracking. At inference you hope to follow one of the reasoning paths discovered during training.
- [bwestergard] (dissent) Can you explain why your view — the opposite of the OP's — is correct? [quoting the training-search-vs-inference-search passage]
- [vova_hn2] Current approach of baking chain-of-thought reasoning into weights is not the end of the line. It just seems accidental and ad-hoc.
