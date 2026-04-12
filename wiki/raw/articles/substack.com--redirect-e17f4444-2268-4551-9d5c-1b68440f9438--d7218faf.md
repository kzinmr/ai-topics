---
title: "Marin"
url: "https://substack.com/redirect/e17f4444-2268-4551-9d5c-1b68440f9438?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-12T03:35:08.805633+00:00
source_date: 2026-04-12
tags: [newsletter, auto-ingested]
---

# Marin

Source: https://substack.com/redirect/e17f4444-2268-4551-9d5c-1b68440f9438?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Marin
Marin is an open lab for building foundation models—together.
We’re training powerful models from scratch, and sharing and programmatically documenting every step:
the code, the data, the experiments, the mistakes…all in real-time.
We invite anyone who shares our vision of open science and open-source to join and contribute,
whether you want to try out a new architecture, training algorithm, dataset,
evaluation…there is a lot to do!
To learn more about the vision, read our
launch announcement
.
Want to jump in?
Install
the Marin code and
run your first experiment
!
Want to stay up to date?  Join our
Discord
or our
mailing list
.
Experiments 🧪
Building a foundation model requires countless experiments trying out endless variants of algorithms and datasets.
All the experiments we’re doing are captured as
GitHub issues
(here is a
summary
).
Here’s the lifecycle of an
experiment
:
A GitHub
issue
is created to preregister the experiment (hypotheses, goal).
A
pull request
is created with
code
that reproduces the experiment.
Code defines a provenance graph which is
executed
; results are summarized in a
WandB
report.
Some examples:
Experiment 935: How does z-loss impact loss?
[
issue
,
PR
,
code
,
execution
,
WandB
]
Experiment 950: How does pretraining learning rate impact SFT?
[
issue
,
PR
,
code
,
execution
,
WandB
]
Experiment 163: Is BERT a better quality filter than fastText?
[
issue
,
PR
,
code
,
execution
,
WandB
]
Experiment 1290: Which optimizers actually outperform AdamW?
[
issue
,
PR
,
code
,
execution
,
WandB
]
Experiment 1183: Are MoEs really better than dense models?
[
issue
,
PR
,
code
,
execution
,
WandB
]
Experiment 702: How should you train on rare task-relevant data?
[
issue
,
PR
,
code
,
execution
,
WandB
]
Models 🌐
We trained some models in Marin:
Marin-8B-Base (deeper-starling)
[
issue
,
code
,
execution
,
WandB
]:
 Beats Llama 3.1 8B base on 14/19 standard benchmarks!
 Read more in our
retrospective
.
Marin-8B-Instruct (deeper-starling-05-15)
[
execution
]:
Try it out on
Together AI
!
Marin-32B-Base
[
issue
,
code
,
execution
]:
Beats OLMo 2 32B Base on 14/19 standard benchmarks (making it the best open-source model as of Oct 29, 2025),
and is close to Gemma 3 27B PT and Qwen 2.5 32B Base (the best comparably-sized open-weight models).
Read more in our
retrospective
.
Speedrun 🏃
Have a new architecture or training procedure that you think is more efficient?
Participate in the
Marin speedrun
competition
(inspired by the
nanogpt speedrun
),
pick your compute budget,
and create the fastest method to train a model to a certain quality!
Here’s a
tutorial
for running your first speedrun on GPUs.
We will offer free compute to scale up top performers.
Get started
here
.
Acknowledgements
Marin wouldn’t be possible without the generous support of the
Google TPU Research Cloud program
.
We also benefit immensely from the broader open ecosystem, who have released numerous tools and datasets.
