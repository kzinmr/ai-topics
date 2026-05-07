---
title: "Sequence to Sequence Learning with Neural Networks: What a Decade — Ilya Sutskever (NeurIPS 2024) Transcript"
author: Ilya Sutskever
source: YouTube
url: https://www.youtube.com/watch?v=1yvBqasHLZs
published: 2024-12-13
type: transcript
tags:
  - transcript
  - ilya-sutskever
  - scaling-hypothesis
  - pretraining
  - superintelligence
  - neurips-2024
---

# Talk Transcript

[00:01] want to thank the
[00:03] organizers for choosing a paper for this
[00:07] award it was very nice

[00:26] an image a screenshot
[00:34] from a similar talk 10 years ago at
[00:37] NeurIPS in 2014 in
[00:40] Montreal and it was a much more innocent
[00:43] time

[01:01] I'd like to talk a little bit
[01:01] about the work itself and maybe a 10-year
[01:06] retrospective on it because a lot of the things in this
[01:12] work were correct but some not so much
[01:16] and we can review them and we can see
[01:18] what happened and how it gently flowed
[01:20] to where we are today

## The Core Recipe

[01:39] the summary of what we did is
[01:42] the following three bullet points: it's
[01:42] an autoregressive model trained on text
[01:45] it's a large neural network and it's a
[01:47] large dataset and that's it

## The Deep Learning Dogma

[01:58] this was a slide 10 years ago
[02:01] "The Deep Learning Dogma"
[02:04] if you have a large neural network with
[02:08] 10 layers then it can do anything that a
[02:11] human being can do in a fraction of a second

[02:16] why this specifically? if you
[02:25] believe the Deep Learning Dogma — that
[02:30] artificial neurons and biological neurons
[02:31] are similar or at least not too
[02:33] different, and you believe that real
[02:35] neurons are slow — then anything that
[02:37] we can do quickly... if there is one human in the
[02:44] entire world that can do some task in a
[02:46] fraction of a second then a 10-layer
[02:48] neural network can do it too.

[02:50] You just take their connections
[02:52] and you embed them inside your neural network,
[02:54] the artificial one.

## Retrospective (What Was Wrong)

[03:05] This slide is from 2014 and we said
[03:07] "we should use large RNNs in all
[03:14] supervised learning tasks."
[03:21] Actually LSTMs. RNNs were all the rage.
[03:28] Transformers didn't exist yet.

[03:44] We said "deep learning would become the
[03:46] primary approach for machine translation"
[03:49] which turned out to be correct.

[03:55] We said we'd achieve human-level translation.
[04:00] That was wrong at the time but
[04:02] with GPT-4 it became correct.

## Scaling As the Driving Force

[04:50] The thing that surprised us the most:
[04:52] how far scaling would go.
[04:55] We thought maybe 10 layers was enough.
[04:58] The answer was: many more than 10 layers.
[05:00] And the more layers you have, the better.

## The Future: End of Pretraining

[15:XX] Pretraining as we know it will end.

[16:XX] What comes next is superintelligence:
[16:XX] agentic, reasons, understands, and is self-aware.

## On Generalization (Q&A)

[22:32] The question should not be answered with
[22:39] yes or no... what does it mean out of
[22:44] distribution generalization?

[22:56] Before deep learning, people used
[23:01] string matching n-grams for machine
[23:04] translation, statistical phrase tables —
[23:09] tens of thousands of lines of code.

[23:20] Back then, generalization meant: is it
[23:23] literally not in the same phrasing as in the
[23:25] dataset. Now we say: my model achieves
[23:32] a high score on math competitions — but maybe
[23:37] the discussion on some forum was about the same
[23:39] ideas, so it's memorized.

[23:46] Our standards for what counts as
[23:47] generalization have increased really
[23:50] quite substantially.

[24:00] To some degree, probably not as well as
[24:02] human beings. I think it is true that human
[24:04] beings generalize much better, but at the
[24:08] same time they definitely generalize out
[24:10] of distribution to some degree.
