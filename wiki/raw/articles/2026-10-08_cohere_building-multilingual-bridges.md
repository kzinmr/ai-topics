---
title: "In-Language Reasoning: Data Mixing Bridges"
source: "Cohere Blog"
url: "https://cohere.com/blog/building-multilingual-bridges"
scraped: "2026-10-08T06:00:39.631023+00:00"
lastmod: "2026-10-06"
type: "sitemap"
---

# In-Language Reasoning: Data Mixing Bridges

**Source**: [https://cohere.com/blog/building-multilingual-bridges](https://cohere.com/blog/building-multilingual-bridges)

Key takeaways
Truly multilingual AI should reason in the user's language, not just answer in it.
Today's reasoning models mostly think in English, which can lose nuance from the prompt in internal translation, leave language-specific cultural knowledge unused, and exclude non-English speakers from inspecting or engaging with the reasoning traces. Moving from multilingual answers to in-language reasoning (referred to as “L2” reasoning) is the next step toward reasoning systems that are genuinely accessible across different languages.
We find that in-language reasoning can be achieved through data mixing built on three pillars.
First, ensuring a broader language coverage in reasoning training data improves generalization to languages without reasoning supervision. Second, including a small share of multilingual non-reasoning data boosts both accuracy and in-language reasoning. And third, using English reasoning data provides the task-solving backbone.
Our resulting model, Tiny Aya L2-Thinker (3.35B), reasons in the prompt language over 93% of the time across 60 languages.
It does so with minimal accuracy loss, holds up on low-resource languages, and uses fewer reasoning tokens than comparable models.
A model’s ability to reason and the language it reasons in are not always tied to one another, so L2 reasoning doesn't have to be built language by language.
This puts in-language reasoning within reach even where multilingual reasoning data is scarce. We release the model weights and multilingual reasoning data to support further work on accessible, in-language reasoning.
The language of reasoning matters
Some of the biggest recent gains in language models have come from a simple idea: let the model ‘think’ before it answers. The result of this idea is the development of reasoning models that work through a problem step by step, producing a written ‘reasoning trace’. This has led to great improvements in language models’ abilities to complete tasks like math and coding. These models, however, mainly focus on giving the right answer, but we ask an often-overlooked question: can users actually follow the reasoning traces?
For many users, the answer today is no: when a question is asked in Spanish, Arabic, or Swahili, these models tend to reason in English. The final answer may come back in the user's language, but the reasoning steps behind that answer stay out of reach for anyone who doesn't speak English. This is not an unsolvable problem. By enabling multilingual reasoning models to reason in the user’s language, which we call ‘
in-language
’ or ‘
L2
’ reasoning, users can read the reasoning trace, verify each step, find where things went wrong when the answer is incorrect, and step in when needed.
L2 reasoning may also help the model itself. Much knowledge, such as cultural context and linguistic nuance, is expressed most naturally in its source language. L2 reasoning could let models draw on this culturally embedded knowledge more effectively, especially in linguistic and open-ended generation tasks. The example below shows what this looks like in practice: Asking in Hindi which event signals good luck, our Tiny Aya L2-Thinker model reasons in Hindi about what Indian superstitions hold and reaches the correct answer, while thinking in English asserts a Western-biased answer without weighing the options.
In this blog post, we describe our recent research that shows how better data mixing leads to effective L2 reasoning without hurting accuracy much. Building on the
Tiny Aya base model with 32K context length
, we apply our data mixing strategy to create
Tiny Aya L2-Thinker
, a massively multilingual model achieving over 93% in-language reasoning rate across 60 languages.
What’s missing from prior work
Getting models to reason in the user's language is not a new idea, but earlier attempts have fallen short in three ways. First, they show that L2 reasoning often comes at a cost: models that are pushed to reason in another language
tend to get more answers wrong
, and approaches that avoid this drop
rely on complex, expensive training
. Second, most studies evaluate models only on math and science problems. Math is a good test of reasoning, but it's also the task where language matters least, so it tells us little about cultural knowledge or open-ended writing. Third, they cover only a handful of languages, usually ones that already receive a large amount of attention from AI researchers and developers.
Our model, Tiny Aya L2-Thinker, addresses all three of these shortcomings: it reasons in the user's language while staying nearly as accurate as reasoning in English across a range of tasks, with the exception of competition-level math. We test it on math reasoning, commonsense understanding, cultural reasoning, open-ended writing, and instruction following. It also supports 45 languages in training, with evidence that it can carry this ability over to languages it was never shown reasoning examples in.
We also found that inference-time language forcing approaches don't close these gaps: Asking Qwen3.5-4B to think in the user's language barely changes what it does, and forcing the issue harder, by prefilling the opening words of its reasoning trace, works better but costs accuracy and isn't something most users can do. Reliable in-language reasoning has to come from training, which leaves the question of what to train on, the subject we focus on next.
Optimizing data for transfer of reasoning beyond English
Our approach centers on the training data. How can we design training data so that the model learns to reason in languages other than English? We combine three types of data, which we call pillars, each teaching the model something different.
The first pillar is
English reasoning data (ER)
: about 1.7 million examples of step-by-step solutions generated by a larger model, gpt-oss-120b. This is where the model learns how to solve problems, and it matters most for math. On its own, though, it produces a model that almost always thinks in English: it reasons in the user's language only 12.8% of the time, even when overtly instructed to do so.
The second pillar is
multilingual reasoning data (MR)
: we automatically translate English reasoning examples in math, science, and general topics into 44 languages. Translating long reasoning traces is costly, so we have only about 5,000 examples per language, a tiny amount compared to the English data. Yet this small set is enough to teach the model to reason in the user's language: adding it raises that rate from 12.8% to 86.1%, and accuracy improves too.
The third and important pillar is
multilingual non-reasoning data (NR)
: samples with questions and answers in the target language, but no reasoning traces. This data has historically been much more available because it has been used in prior multilingual instruction models. This pillar helps the model carry its ability to reason in the user's language over to new languages, including ones it never saw reasoning examples in.
The chart below shows how each data pillar builds on the last and progressively improves both L2 reasoning rate and accuracy. For a detailed analysis of each pillar and how we chose the final data mix, see
our paper
.
What we measured, and what we found
Beyond the accuracy scores that reasoning benchmarks usually report, we pay particular attention to three aspects we consider key to making reasoning models globally accessible:
Are we achieving L2 reasoning without trading off quality?
Does performance hold up in lower-resource languages?
Is the reasoning itself any good?
We test on six benchmarks across 60 languages, covering math (
MGSM
and
PolyMath
), cultural and commonsense reasoning (
Macaron‑MCQ
and
GlobalPIQA
), instruction following (
Marco‑Bench‑MIF
), and open-ended writing (
MIST‑OEG
).
Are we achieving L2 reasoning without trading off quality?
This is the trade-off earlier work ran into, so it's the first thing to check. We compare Tiny Aya L2-Thinker against its own twin: Tiny Aya En-Thinker that was trained on the same base model and underlying data, but reasons in English.
Alongside accuracy, we measure the L2 reasoning rate: the share of responses where the model actually reasoned in the target language, which we determine by running a language identification model over each reasoning trace. A model can score well on accuracy while failing here completely, and that gap is exactly what we set out to close.
Accuracy barely moves. On five of six benchmarks it drops by at most two to three points, and on MIST-OEG, our open-ended writing benchmark, it actually goes up slightly. English performance holds up too: the model still reasons in English on English prompts and matches the English reasoner on most benchmarks. In exchange, the share of traces written in the user's language goes from near zero to above 93%.
The exception is PolyMath, a competition-level math benchmark with problems well beyond grade-school arithmetic. Here accuracy falls more noticeably. We suspect this is because our model never went through a reinforcement learning stage, which hard math benefits from most and which could also smooth over artifacts introduced when we translated our training traces; this is a future direction that could be pursued with a focus on mathematics.
Does performance hold up in lower-resource languages?
In-language reasoning is typically harder to achieve for languages with less data available for training. We observe this when we compare to existing larger models built for L2 reasoning: M-Thinker-7B and Magistral-Small-24B. In the figure below we show how often each model reasons in the user's language, how accurate it is, and how many tokens it spends on reasoning as a measure of efficiency, across four tiers of resourcedness. The evaluation languages are grouped into tiers by how much web text exists for them, tier 1 being the highest-resource (e.g., English, German, French) and tier 4 the lowest (e.g., Swahili, Zulu, Welsh).
Tiny Aya L2-Thinker is the only model that stays strong on all three axes as resource availability declines. Its L2 reasoning rate sits near the ceiling on tiers 1 and 2 (99%) and drops only slightly on the lowest two (94.3% and 94.5%). In contrast, Magistral collapses from 72% to 5% L2 reasoning rate, M-Thinker degrades on every axis and its traces roughly double in length, and language-forced Qwen keeps its L2 reasoning rate fairly high, but at the cost of accuracy and efficiency.
Across the board, our model is also very economical, averaging under 5,000 thinking tokens, thanks to
its multilingually optimized tokenizer
.
Avoiding typical reasoning failure modes: Is the reasoning itself any good?
A model that thinks longer should, in principle, be “thinking harder”, irrespective of the language. Harder problems deserve more deliberation, and more tokens can mean more careful work. But across the models we tested, long reasoning traces usually meant something else: the model was going in circles.
We measure this with a repetition score, how often short sequences of text repeat within a trace, and compare it to how long the reasoning runs, shown in the scatterplot below. The two rise together: When models reason for longer they usually have a higher repetition rate. Reading the traces makes the pattern concrete: Many aren't long because the model is exploring alternatives; they're long because it is cycling through the same few steps, over and over, until it runs out of its token budget and stops without ever giving an answer. This is usually referred to as "doomlooping".
Qwen3.5-4B is the clearest case: it routinely spends 10,000 to 25,000 tokens reasoning that don’t necessarily improve performance. Prefilling its reasoning in the target language doesn't rescue it: language-forced Qwen remains in the same high-token, high-repetition corner, and as we saw in the language tiers plot above, it gets much less efficient on lower-resourced languages.
Tiny Aya L2-Thinker mostly avoids this. On most benchmarks, it reasons in a few hundred to a few thousand tokens, with little repetition, and is also efficient on all language tiers, even low-resourced ones. Efficient reasoning is not solved yet, but it doesn’t have to be traded away for in-language reasoning.
Summary and outlook
We have shown that reasoning ability and reasoning language are separable. A model can learn to solve problems largely from English reasoning data, learn which language to reason in from a small amount of multilingual reasoning data, and generalize that behavior to new languages with multilingual non-reasoning data.
Reasoning in the right language, however, is only part of the picture. A reasoning trace can be understandable to users, but still loop, ramble, never arrive at a solution, or not actually meaningfully influence the solution. Further work should be done to make reasoning traces more meaningful, efficient and interpretable to downstream users.
To support further research on accessible, in-language reasoning, we release our model and multilingual reasoning data on Hugging Face.
Models:
Tiny Aya L2-Thinker:
https://huggingface.co/CohereLabs/tiny-aya-l2-thinker
Tiny Aya En-Thinker:
https://huggingface.co/CohereLabs/tiny-aya-en-thinker
Tiny Aya Base 32K:
https://huggingface.co/CohereLabs/tiny-aya-base-32K
Try L2-Thinker on CohereLabs Space:
https://huggingface.co/spaces/CohereLabs/tiny-aya-l2-thinker
Multilingual Reasoning data:
https://huggingface.co/datasets/CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning
For the full analysis, read the paper
here
.
If you use the model, the data, or find this work useful, please cite the paper:
@misc{mofakhami2026buildingmultilingualbridgesdata,
title={Building Multilingual Bridges: Data Mixing
as
the Pillar of Generalization
for
In-Language Reasoning},
author={Mehrnaz Mofakhami
and
Ananya Sahu
and
Alejandro R. Salamanca
and
Daniel D
'souza and Alexandre Berard and Thomas Euyang and Marzieh Fadaee and Julia Kreutzer},
year={2026},
eprint={2609.10445},
archivePrefix={arXiv},
primaryClass={cs.CL},
url={https://arxiv.org/abs/2609.10445},
}
We would like to thank everyone who contributed to this work and shared their insights: Ananya Sahu, Alejandro R. Salamanca, Daniel D'souza, Alexandre Berard, Thomas Euyang, David Stap, Maximilian Mozes, Kelly Marchisio, Ammar Khairi, Nikita Moghe, Sara Rajaee, Saurabh Dash, David Cairuz, Sammie Bae, Diana Abagyan, Björn Bebensee, Sylvie Shi and Pierre Beaulieu, and Aidan Peppin.
Blog
Written By
Mehrnaz Mofakhami
Julia Kreutzer
Senior Research Scientist, Cohere
Madeline Smith
Operations and Community Manager, Cohere Labs
Marzieh Fadaee
Head of Cohere Labs
Tags
Research
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
