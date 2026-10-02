---
title: "Why do OpenAI's GPT-2 weights beat mine? Part five: data quality"
url: "https://www.gilesthomas.com/2026/10/why-do-openai-gpt2-weights-beat-mine-5-data-quality"
fetched_at: 2026-10-02T10:01:06.669554+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Why do OpenAI's GPT-2 weights beat mine? Part five: data quality

Source: https://www.gilesthomas.com/2026/10/why-do-openai-gpt2-weights-beat-mine-5-data-quality

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
When I finished learning how to build an
LLM from scratch
,
I was left with a mystery: my own models were not as good as OpenAI's original
GPT-2 models, despite being based on the same architecture.
My models all had 163M parameters, and followed the design from
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
".
That meant that they were pretty much the same as the setup for the OpenAI GPT-2 "small" instance,
except that they did not use weight-tying or bias on the QKV matrices.  Weight-tying means that you re-use
the initial embedding matrix as the output head at the end, and using it means that GPT-2 small
saved quite a few parameters -- it was 124M rather than 163M -- at, at least in my
own experiments, a
cost in quality
;
similarly, while I found that QKV bias made a
tiny improvement in loss terms
, I'd
felt it was likely within the noise.
But GPT-2 small consistently beat my models on an instruction
fine-tuning (IFT) task -- also adapted from Raschka's book.   That test fine-tunes the model
on a subset of the
Alpaca
dataset, until
validation loss starts rising, and then runs a test set through the resulting model.
The responses to the test set questions are stored, and then I run all of the responses
from all of the models under test past GPT 5.5 in one go to get an aggregate score;
more details here
.
GPT-2 small
always did better than any of my models on this.
Additionally, it did surprisingly
well on a simpler eval -- one that just measured the cross entropy loss it got on a
test set.  It scored close to my own best models, and better than many of them.
What made this result particularly interesting was that the test set
in question was a split of my own training data; my models would not have seen it when
training (at least, in theory), but it seems likely that it would be much more similar to their
own training data than it was to OpenAI's.
I've checked two things while probing this mystery:
It seems very likely that the GPT-2 models were overtrained by modern standards; would
overtraining my own
models
get them closer?  It turned out that no, it probably didn't help with the IFT eval (though there might
have been some signal there).  It did help quite a lot with the test loss eval, though.
The way I was handling
dropout
in the IFT test might
have been unduly benefiting some models while working against others.  I decided
to standardise on
not
using dropout during this eval, as (counter-intuitively for me) it seemed
to harm the results of most models, even those that had been pre-trained
with
dropout.
In particular, the OpenAI weights were harmed by using dropout, and making a change
that benefited them (along with some of my own models) seemed the most conservative
approach to take in investigating this.
The next thing I wanted to look into was the training data.
The exact dataset that the various GPT-2 models were trained on has never been released;
all we know about it
is from
the paper
,
where they say:
[W]e created a new web scrape which emphasizes
  document quality. To do this we only scraped web pages
  which have been curated/filtered by humans. Manually
  filtering a full web scrape would be exceptionally expensive
  so as a starting point, we scraped all outbound links from
  Reddit, a social media platform, which received at least 3
  karma. This can be thought of as a heuristic indicator for
  whether other users found the link interesting, educational,
  or just funny.
They called it "WebText".  There is an
OpenWebText
that tries to replicate it, but although they tried to follow the same procedure as the
original, there's no guarantee that it is all that similar.
By comparison, I'd normally been training against
FineWeb
.
While this is a general web-scraping dataset, without the "curation" provided by
using only stuff that was linked from upvoted Reddit posts, it has been refined to
remove any obvious junk.  I had felt that it was
pretty much equivalent.
But what if I were wrong about that?  I decided to see if I could get better models by using better data.
The starting point
Here's a table of all of the models I've been comparing to date.  The "Test loss"
column shows how well the model in question did on that held-back cross entropy loss
evaluation.  The "IFT epochs" column shows how many epochs of fine-tuning the model
needed before its validation loss started rising, the "IFT score" the score that
GPT 5.5 gave the model's responses to the test set of my Alpaca data, and the "IFT rank"
the model's rank in terms of that score.  The OpenAI small model is in there in bold,
and I've also included the OpenAI medium model for comparison purposes.
Test loss
IFT epochs
IFT score
IFT rank
OpenAI weights: medium
3.231442
2
43.75
1
JAX, overtrained one long epoch
3.324953
3
19.77
4
JAX, overtrained two normal epochs
3.326482
4
19.72
5
JAX, with MHA bias, no dropout
3.418784
4
18.69
6
JAX, no MHA bias, no dropout
3.420089
5
21.46
3
JAX, no MHA bias, with dropout
3.476802
5
13.22
15
OpenAI weights: small
3.499677
2
26.00
2
1xrtx3090-stacked-interventions
3.538161
4
13.77
14
8xa100m40-stacked-interventions-1
3.577761
4
10.76
18
Cloud FineWeb, 8x A100 40 GiB
3.673623
3
17.72
7
1xrtx3090-baseline
3.683835
4
15.74
8
8xa100m40-baseline
3.691526
3
14.19
13
Cloud FineWeb, 8x H100 80 GiB
3.724507
4
14.33
12
Cloud FineWeb, 8x A100 80 GiB
3.729900
3
11.34
17
Cloud FineWeb, 8x B200 160 GiB
3.771478
4
14.67
11
Local FineWeb train
3.943522
5
12.31
16
Local FineWeb-Edu extended train
4.134991
5
15.04
9
Local FineWeb-Edu train
4.166892
5
14.99
10
You can see that the OpenAI small model did pretty well in terms of the test loss,
when you consider that it has 39M fewer weights than my models and was being tested against a
dataset that differs more from its likely training data than it does from my own models'.   Additionally, the specific models that did better than
OpenAI's small one were all trained with JAX rather than PyTorch -- my hypothesis for that
is that it's a result of the JAX ones getting better initial weights by pure chance.
But the big difference was in the IFT score.  In the specific run that gave
the results in this table, the OpenAI small model got 26.00 -- the closest of my own models was more than
4.5 points lower, at 21.46.
This difference was consistent over all of my other test runs.  The GPT-2 small model
was always ahead of mine.  (GPT-2 medium, of course, beat GPT-2 small and all of my models,
but given that it is twice the size of mine, that's not a big surprise.)
Now, quite some time ago, I had tried looking into data quality as a lever to pull
for model performance.  At the bottom of the table, with the worst test loss of all
models, you can see two models:
"Local FineWeb-Edu train"
"Local FineWeb-Edu extended train"
These two were (as you might guess from the names) trained on the
FineWeb-Edu
dataset, which includes just the most "educational" data from FineWeb.  They
scored very badly on the test loss score.  Given that the test dataset is from FineWeb,
that's not a big surprise -- as I've written previously:
If you train a model
  on Jane Austen and then evaluate against
Chuck Tingle
, then
  you're not going to get amazing results.
But again, GPT-2 had the same issue, and did perfectly well on the test
loss eval.
On the other hand, while these FineWeb-Edu models' performance on the IFT eval wasn't stellar -- there are
plenty of my other models ahead of them -- they did seem to punch above their weight.  Consistently
across all of the IFT evals I've done, they have scored higher than many of the others --
despite their poor loss on the test eval.
Additionally: they were amongst the first models that I trained, before I'd spent
time learning about how to
optimise my hyperparameters and training loop
.
They did not use gradient clipping, they did use dropout, their batch size was just "whatever
I could squeeze into the GPU", and I didn't set the learning
rate to the right kind of value or schedule it over the course of the training run.
So maybe a new training run on FineWeb-Edu plus my training improvements would help?
And maybe some other tweaks to the training data would be worth looking into?
The plan
I decided to see what would happen if I trained some models with better-quality
data.  Specifically, I would train models with my current optimised loop and hyperparameters on
four different datasets:
FineWeb-Edu -- essentially the same as "Local FineWeb-Edu train" but with a better
training setup.  This would test the "more educational -> better" hypothesis.
A 50:50 split of FineWeb and FineWeb-Edu.  I've read that LLMs can be
helped
by
having a decent amount of lower-quality data in their training loop, as it helps them to generalise.
Perhaps having some FineWeb in there in addition to the FineWeb-Edu stuff would improve that test loss score while
also helping the IFT test?
A "curated" dataset containing 45% of its contents from FineWeb, 45% from FineWeb-Edu, and 10% from the
Simple English Wikipedia
.  The full
Wikipedia is huge, and full of obscure facts -- while the Simple English one is
small and hopefully richer in useful information on a per-token basis.  And conveniently,
Answer.ai have made
a snapshot of it available on Hugging Face Hub
.
Might deliberately putting a bunch of encyclopaedic data into the training set make the model
better at the IFT eval (which has lots of factual questions in it, like
"who wrote Pride and Prejudice")?
OpenWebText.  Even though I was unsure how well it matched the original WebText,
given that it was there, it seemed silly to not try training something
on it and see how it matched up.
I would train each model on 3.2B tokens of the chosen dataset; that's the Chinchilla-optimal
amount for my 163M-parameter models.  If there were any interesting results, then I might
consider doing
overtrained
models later on.
I decided to be at least vaguely scientific about this, and to pre-register some
predictions:
The FineWeb-Edu-only model would do pretty badly on the test loss, but better than
my older FineWeb-Edu models (90%).  It would also punch above its weight on the IFT
eval (90%).
The 50:50 split: I expected it to do worse on the test eval than my JAX FineWeb-only models (70%), but better than
the FineWeb-Edu one (90%).  I wasn't sure about how it would do on the IFT eval, but
thought it might be somewhere in between the two groups (60%).
The curated dataset I had high hopes for in terms of the IFT eval -- let's say 80% chance
of it being the best of all of my models.  For the test loss eval, I expected it to
do about as well as the 50:50 split, maybe a little bit worse (70%).
I had no idea how the OpenWebText eval would do!  Could be worse, could be better.
Here's how things turned out.
The FineWeb-Edu model
I already had a
dataset based on FineWeb-Edu
ready to go, from when I trained those two original models.  It is just the 10B-token sample of the original
dataset at the time I generated it last December, formatted appropriately for my training
script (details on the dataset card).
I kicked off a training run with my JAX code (which I've been using for the other
posts in this series):
giles@poppy:~/Dev/jax-gpt2-from-scratch
(
main
)
$
XLA_PYTHON_CLIENT_MEM_FRACTION
=
0
.95
uv
run
train.py
full-llm-full-train-with-mha-output-bias-fineweb-edu
datasets/
2026
-09-11
18
:11:47.991583
Downloading
dataset
Fetching
4
files:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
4
/4
[
00
:00<
00
:00,
1772
.93it/s
]
Download
complete:
:
0
.00B
[
00
:00,
?B/s
]
|
0
/4
[
00
:00<?,
?it/s
]
2026
-09-11
18
:11:48.226273
Loading
dataset
into
RAM
Download
complete:
:
0
.00B
[
00
:00,
?B/s
]
2026
-09-11
18
:16:29.507646
Creating
model
2026
-09-11
18
:16:33.042509
Creating
optimizer
2026
-09-11
18
:16:34.138990
Start
train
0
%
|
|
0
/33165
[
00
:00<?,
?it/s
]
2026
-09-11
18
:17:38.486288
Saving
checkpoint
1
%
|
▌
|
173
/33165
[
13
:22<
39
:17:03,
4
.29s/it,
loss
=
6
.897,
tps
=
21
,201
]
...and just less than 40 hours later, I had a model:
Training complete in 142,912.226 seconds
2026-09-13 09:58:26.437276 Tokens seen: 3,260,252,160
2026-09-13 09:58:26.437284 Throughput: 22,813 tokens/second
2026-09-13 09:58:26.437302 Final train loss: 3.342
2026-09-13 09:58:26.437309 Done
I converted the saved JAX safetensors file from the last checkpoint into a format
that would be compatible with my PyTorch eval code, and ran my smoke test: how would
it complete the sentence "Every effort moves you"?
Every effort moves you closer to God’s Kingdom, and even closer to Him.
As we can see in
That was nice and coherent -- if unusually religious! -- so that was promising.
I ran the test eval:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-fineweb-edu/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-fineweb-edu/checkpoints/latest/pytorch-model.safetensors
Fetching
4
files:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
4
/4
[
00
:00<
00
:00,
2758
.50it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
03
:52<
00
:00,
13
.74it/s
]
Loss
against
our
test
dataset:
3
.632900
That was pretty good, putting it at a better test loss than all of the models I had trained
without optimised hyperparameters, and worse than all of the ones I had trained on
FineWeb
with
optimised hyperparameters.  So that fit in with my prediction that it
would be better than the old FineWeb-Edu models; the fact that it was also better than
the non-optimised training runs with FineWeb seemed sensible enough
that I felt silly for not having predicted that it would have fallen exactly there :-)
I decided to leave the IFT eval until the end so that I could check all of the models
from these experiments together, so it was time to
upload this one to Hugging Face
,
and move on to the next model.
50:50 FineWeb to FineWeb-Edu
I put together a new
repo
with
a script to prepare datasets specifically for my training setup
.
You provide it with config that specifies some source datasets along with information about
how to process them and how to mix them together, and it uploads a new dataset to
Hugging Face Hub with the required characteristics.
For example, for the 50:50 FineWeb to FineWeb-Edu split, the config looked like this:
{
"seed"
:
42
,
"tokens_desired"
:
10000000000
,
"upload_dataset_name"
:
"gpjt/fw-fwedu-5050-gpt2-tokens"
,
"sources"
:
[
{
"name"
:
"FineWeb"
,
"hf_id"
:
"HuggingFaceFW/fineweb"
,
"hf_name"
:
"sample-10BT"
,
"hf_split"
:
"train"
,
"item_field"
:
"text"
,
"weight"
:
50
},
{
"name"
:
"FineWeb-Edu"
,
"hf_id"
:
"HuggingFaceFW/fineweb-edu"
,
"hf_name"
:
"sample-10BT"
,
"hf_split"
:
"train"
,
"item_field"
:
"text"
,
"weight"
:
50
}
]
}
The way the script works is pretty simple: it works out (based on those
weight
s and the
tokens_desired
) how many tokens it wants from each source dataset, shuffles the items in the sources, then it loops until
it has the desired number of tokens or more stored in an output.  In the loop, it works out which source is
currently most under-represented, grabs an item from it, tokenises it, and adds it to the output.
Running it with that 50:50 config seemed to work fine:
giles@perry:~/Dev/prepare-llm-training-dataset (main)$
uv
run
prepare-dataset.py
runs/fw-fwedu-5050/
Resolving data files: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████| 27468/27468 [00:00<00:00, 89875.56it/s]
Loading dataset shards: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████| 102/102 [00:00<00:00, 133.75it/s]
Resolving data files: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 2410/2410 [00:00<00:00, 87461.48it/s]
Loading dataset shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████| 98/98 [00:00<00:00, 200.09it/s]
2026-09-13 20:13:22.000187: Generating dataset; per-source counts
2026-09-13 20:13:22.000217: FineWeb: 5,000,000,000
2026-09-13 20:13:22.000221: FineWeb-Edu: 5,000,000,000
FineWeb: 100%|████████████████████████████████████████████████████████████████████████████████████████████████▉| 4999999705/5000000000 [1:01:33<00:00, 1353639.33token/s]
FineWeb-Edu: 5000000363token [1:01:33, 1353639.47token/s]
2026-09-13 21:14:55.747239:
Done generating tokens
2026-09-13 21:14:55.748480: FineWeb: 4,999,999,705 / 5,000,000,000 (1.000, 1 iterators)
2026-09-13 21:14:55.748487: FineWeb-Edu: 5,000,000,363 / 5,000,000,000 (1.000, 1 iterators)
2026-09-13 21:14:55.748489: Total: 10,000,000,068
2026-09-13 21:14:55.748491: Catting...
2026-09-13 21:16:29.565152: Catted into a tensor of shape torch.Size([10000000068])
2026-09-13 21:16:29.566663: Saving...
2026-09-13 21:16:36.006267: Saved
2026-09-13 21:16:36.009413: Uploading to gpjt/fw-fwedu-5050-gpt2-tokens
Processing Files (1 / 1)      : 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 20.0GB / 20.0GB,  117MB/s
New Data Upload               : 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 14.6GB / 14.6GB, 98.1MB/s
...du-5050/train.safetensors: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 20.0GB / 20.0GB
2026-09-13 21:17:59.545875: Done
So we had almost-perfect 50:50 balance between the datasets, and it saved
this dataset on Hugging Face
.
I ran
a script to double-check that it looked sane
,
and it did, so it was time to spin up a training run:
giles@perry:~/Dev/jax-gpt2-from-scratch
(
main
)
$
XLA_PYTHON_CLIENT_MEM_FRACTION
=
0
.90
uv
run
train.py
full-llm-full-train-with-mha-output-bias-fw-fwedu-5050
datasets/
2026
-09-13
21
:20:59.880918
Downloading
dataset
Fetching
2
files:
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
2
/2
[
01
:13<
00
:00,
36
.70s/it
]
Download
complete:
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
20
.0G/20.0G
[
01
:13<
00
:00,
1
.24GB/s
]
2026
-09-13
21
:22:13.521745
Loading
dataset
into
RAM
Download
complete:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
20
.0G/20.0G
[
01
:13<
00
:00,
272MB/s
]
2026
-09-13
21
:22:33.787720
Creating
model
2026
-09-13
21
:22:35.501063
Creating
optimizer
2026
-09-13
21
:22:36.043837
Start
train
0
%
|
|
0
/33165
[
00
:00<?,
?it/s
]
2026
-09-13
21
:23:11.437206
Saving
checkpoint
0
%
|
|
26
/33165
[
02
:20<
38
:07:05,
4
.14s/it,
loss
=
9
.308,
tps
=
18
,246
]
That was running on
perry
, my normal workstation, and I kicked it off in parallel
with the "curated" model training run below on
poppy
my training box, but I'll
keep the runs separate for the purposes of this writeup.
When this had been running for an hour or so, our power went out.  My guess is that
having the tumble dryer running, the car charging, the kettle boiling, the electric hob
switched on, and two machines doing training runs is a bit too much for our electrics...
which might be a problem in the future, especially if (as planned) I make
poppy
a
multi-GPU machine.
However, as things stand, I was able to kick it off again after switching the circuit breaker back on, and things held up.
Again, about 40 hours later:
Training complete in 136,060.457 seconds
2026-09-15 12:05:26.432638 Tokens seen: 3,227,516,928
2026-09-15 12:05:26.432642 Throughput: 23,721 tokens/second
2026-09-15 12:05:26.432650 Final train loss: 3.793
2026-09-15 12:05:26.432653 Done
(Note that the numbers reported at the end of a restarted run like this only include
what happened after the restart.)
I converted it to PyTorch-compatible tensors, and did the smoke test:
Every effort moves you on to other options—in fact, it’s not even worth that effort. Just make
Looking good!  Time for the loss test:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-fw-fwedu-5050/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-fw-fwedu-5050/checkpoints/latest/pytorch-model.safetensors
Fetching
4
files:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
4
/4
[
00
:00<
00
:00,
1192
.07it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
03
:53<
00
:00,
13
.72it/s
]
Loss
against
our
test
dataset:
3
.462454
That was almost in keeping with my prediction that it would do worse than the JAX
FineWeb-only models, except that it was better than the
worst of those, "JAX, no MHA bias, with dropout": it was actually better than I predicted.
So, a promising model.   Time to
upload it to Hugging Face
-- and now let's move on
to the next one.
The "curated" dataset
With my dataset-preparation script, this was easy enough to set up:
{
"seed"
:
42
,
"tokens_desired"
:
10000000000
,
"upload_dataset_name"
:
"gpjt/fw-fwedu-simplewiki-gpt2-tokens"
,
"sources"
:
[
{
"name"
:
"FineWeb"
,
"hf_id"
:
"HuggingFaceFW/fineweb"
,
"hf_name"
:
"sample-10BT"
,
"hf_split"
:
"train"
,
"item_field"
:
"text"
,
"weight"
:
45
},
{
"name"
:
"FineWeb-Edu"
,
"hf_id"
:
"HuggingFaceFW/fineweb-edu"
,
"hf_name"
:
"sample-10BT"
,
"hf_split"
:
"train"
,
"item_field"
:
"text"
,
"weight"
:
45
},
{
"name"
:
"Simple English Wikipedia"
,
"hf_id"
:
"answerdotai/simplewiki"
,
"hf_name"
:
"articles"
,
"hf_split"
:
"train"
,
"item_field"
:
"md"
,
"weight"
:
10
}
]
}
Running that worked nicely:
giles@perry:~/Dev/prepare-llm-training-dataset
(
main
)
$
uv
run
prepare-dataset.py
runs/fw-fwedu-simplewiki/
Resolving
data
files:
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████
|
27468
/27468
[
00
:00<
00
:00,
90196
.13it/s
]
Loading
dataset
shards:
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████
|
102
/102
[
00
:00<
00
:00,
358
.90it/s
]
Resolving
data
files:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████
|
2410
/2410
[
00
:00<
00
:00,
88254
.11it/s
]
Loading
dataset
shards:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████
|
98
/98
[
00
:00<
00
:00,
589
.23it/s
]
2026
-09-13
18
:59:04.106327:
Generating
dataset
;
per-source
counts
2026
-09-13
18
:59:04.106387:
FineWeb:
4
,500,000,000
2026
-09-13
18
:59:04.106407:
FineWeb-Edu:
4
,500,000,000
2026
-09-13
18
:59:04.106422:
Simple
English
Wikipedia:
1
,000,000,000
FineWeb:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████▉
|
4499997964
/4500000000
[
59
:41<
00
:00,
1256362
.56token/s
]
FineWeb-Edu:
4500000607token
[
59
:41,
1256363
.31token/s
]
Simple
English
Wikipedia:
1000002889token
[
59
:41,
279192
.58token/s
]
2026
-09-13
19
:58:45.874744:


Done
generating
tokens
2026
-09-13
19
:58:45.876043:
FineWeb:
4
,499,997,964
/
4
,500,000,000
(
1
.000,
1
iterators
)
2026
-09-13
19
:58:45.876048:
FineWeb-Edu:
4
,500,000,607
/
4
,500,000,000
(
1
.000,
1
iterators
)
2026
-09-13
19
:58:45.876052:
Simple
English
Wikipedia:
1
,000,002,889
/
1
,000,000,000
(
1
.000,
6
iterators
)
2026
-09-13
19
:58:45.876054:
Total:
10
,000,001,460
2026
-09-13
19
:58:45.876056:
Catting...
2026
-09-13
20
:00:18.811748:
Catted
into
a
tensor
of
shape
torch.Size
([
10000001460
])
2026
-09-13
20
:00:18.813169:
Saving...
2026
-09-13
20
:00:22.773873:
Saved
2026
-09-13
20
:00:22.773936:
Uploading
to
gpjt/fw-fwedu-simplewiki-gpt2-tokens
Processing
Files
(
1
/
1
)
:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████
|
20
.0GB
/
20
.0GB,
143MB/s
New
Data
Upload
:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████
|
19
.8GB
/
19
.8GB,
142MB/s
...plewiki/train.safetensors:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████
|
20
.0GB
/
20
.0GB
2026
-09-13
20
:01:59.270021:
Done
One thing that is worth noting in that output is the "6 iterators" for the Simple English Wikipedia.
If a source dataset runs out of items while we're building up the results in this script,
we start iterating over it again (with a different seed for the shuffle so that the ordering
is different).   The "6 iterators" means that it needed to do that 6 times -- the original
creation of the iterator at the start of the script, and five more.  So that means that
the Simple English Wikipedia is repeated (oversampled) somewhere between five and six
times in the dataset.
That's not a bad thing!  From what I've read, it's actually quite standard to oversample
highly educational content in LLM training datasets.  And anyway, the dataset the
script generated was 10B tokens, of which we're only using 3.2B for the training run in
this post, so it would only appear somewhere between one and two times.  The repetition would
likely only really cut in if and when we did an overtrained model on the dataset.
Anyway, I ran my check against
the uploaded dataset
-- the first few items were clearly from
FineWeb, FineWeb-Edu, and the Simple English Wikipedia.
It was time to kick off a training run:
giles@poppy:~/Dev/jax-gpt2-from-scratch
(
main
)
$
XLA_PYTHON_CLIENT_MEM_FRACTION
=
0
.95
uv
run
train.py
full-llm-full-train-with-mha-output-bias-fw-fwedu-simplewiki
datasets/
2026
-09-13
20
:24:48.037024
Downloading
dataset
Downloading
(
incomplete
total...
)
:
0
.00B
[
00
:00,
?B/s
]
Warning:
You
are
sending
unauthenticated
requests
to
the
HF
Hub.
Please
set
a
HF_TOKEN
to
enable
higher
rate
limits
and
faster
downloads.
|
0
/2
[
00
:00<?,
?it/s
]
WARNING:huggingface_hub.utils._http:Warning:
You
are
sending
unauthenticated
requests
to
the
HF
Hub.
Please
set
a
HF_TOKEN
to
enable
higher
rate
limits
and
faster
downloads.
Fetching
2
files:
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
2
/2
[
02
:51<
00
:00,
85
.85s/it
]
Download
complete:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
20
.0G/20.0G
[
02
:51<
00
:00,
435MB/s
]
2026
-09-13
20
:27:39.934884
Loading
dataset
into
RAM
Download
complete:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
20
.0G/20.0G
[
02
:51<
00
:00,
116MB/s
]
2026
-09-13
20
:31:20.492877
Creating
model
2026
-09-13
20
:31:24.054143
Creating
optimizer
2026
-09-13
20
:31:25.100832
Start
train
0
%
|
|
0
/33165
[
00
:00<?,
?it/s
]
2026
-09-13
20
:32:29.650379
Saving
checkpoint
0
%
|
▎
|
107
/33165
[
08
:38<
39
:05:39,
4
.26s/it,
loss
=
7
.631,
tps
=
20
,293
]
Again, this was interrupted by the power outage that hit the 50:50 training run, but
I was able to restart from a checkpoint.
After another 22 hours, it crashed with an error that I've seen
before
:
jax.errors.JaxRuntimeError: INTERNAL: CUDA error: Failed to end stream capture: CUDA_ERROR_STREAM_CAPTURE_INVALIDATED: operation failed due to a previous error during capture [executable_name='jit_train_step']
I put it aside as a one-off oddity when I hit it last time, but this time I dug in
a bit more.  I noted that it had not ever happened on
perry
, but seemed to be an
issue on
poppy
, and that
poppy
had an older version of CUDA and the Nvidia drivers
-- might that be the cause?  I decided to upgrade those before kicking off the next
run, but for now just restarted the run from the most recent checkpoint.  (Note for
anyone who is hitting the same error: it has not occurred since the upgrade, so that's worth
trying.)
This time it completed OK:
Training complete in 59,564.515 seconds
2026-09-15 15:56:52.909888 Tokens seen: 1,367,212,032
2026-09-15 15:56:52.909894 Throughput: 22,953 tokens/second
2026-09-15 15:56:52.909912 Final train loss: 3.332
2026-09-15 15:56:52.909959 Done
Again, these numbers just show what happened after the most recent restart.
I copied it over to
perry
, converted it into a format that was compatible
with my PyTorch code, and ran the smoke test:
Every effort moves you by the air, for it will make you a better athlete, so your body becomes bigger and stronger
Coherent enough -- time for the loss eval:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
~/Dev/jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-fw-fwedu-simplewiki/model.json
~/Dev/jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-fw-fwedu-simplewiki/checkpoints/latest/pytorch-model.safetensors
Fetching
4
files:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
4
/4
[
00
:00<
00
:00,
1007
.64it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
03
:57<
00
:00,
13
.48it/s
]
Loss
against
our
test
dataset:
3
.542460
Again, in line with my predictions -- worse than the JAX FineWeb-only models, and
indeed than the very best PyTorch one,
1xrtx3090-stacked-interventions
, and also worse
than the 50:50 split, but better than the FineWeb-Edu one.
I
uploaded it to Hugging Face
,
and it was time to move on to what was meant to be the final model for this set of experiments.
The OpenWebText run
Again, this was a simple enough config to set up:
{
"seed"
:
42
,
"tokens_desired"
:
10000000000
,
"upload_dataset_name"
:
"gpjt/openwebtext-gpt2-tokens"
,
"sources"
:
[
{
"name"
:
"OpenWebText"
,
"hf_id"
:
"Skylion007/openwebtext"
,
"hf_name"
:
"plain_text"
,
"hf_split"
:
"train"
,
"item_field"
:
"text"
,
"weight"
:
50
}
]
}
...and the build and upload process worked well (and took much less time -- for some
reason, sampling randomly from a single dataset is faster than sampling from two or three):
giles@perry:~/Dev/prepare-llm-training-dataset
(
main
)
$
uv
run
prepare-dataset.py
runs/openwebtext/
Resolving
data
files:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████
|
80
/80
[
00
:00<
00
:00,
32723
.26it/s
]
Resolving
data
files:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████
|
80
/80
[
00
:00<
00
:00,
97940
.55it/s
]
Loading
dataset
shards:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████
|
80
/80
[
00
:00<
00
:00,
1200
.13it/s
]
2026
-09-15
13
:16:47.622617:
Generating
dataset
;
per-source
counts
2026
-09-15
13
:16:47.622645:
OpenWebText:
10
,000,000,000
Resolving
data
files:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████
|
80
/80
[
00
:00<
00
:00,
45602
.65it/s
]
Resolving
data
files:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████
|
80
/80
[
00
:00<
00
:00,
67650
.06it/s
]
Loading
dataset
shards:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████
|
80
/80
[
00
:00<
00
:00,
307
.11it/s
]
OpenWebText:
10000000024token
[
31
:46,
5246208
.64token/s
]
2026
-09-15
13
:48:33.761350:


Done
generating
tokens
2026
-09-15
13
:48:33.762021:
OpenWebText:
10
,000,000,024
/
10
,000,000,000
(
1
.000,
2
iterators
)
2026
-09-15
13
:48:33.762026:
Total:
10
,000,000,024
2026
-09-15
13
:48:33.762028:
Catting...
2026
-09-15
13
:49:33.115508:
Catted
into
a
tensor
of
shape
torch.Size
([
10000000024
])
2026
-09-15
13
:49:33.115923:
Saving...
2026
-09-15
13
:49:36.365978:
Saved
2026
-09-15
13
:49:36.366027:
Uploading
to
gpjt/openwebtext-gpt2-tokens
Processing
Files
(
0
/
1
)
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████▉
|
20
.0GB
/
20
.0GB,
147MB/s
New
Data
Upload
:
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████
|
19
.9GB
/
19
.9GB,
147MB/s
...webtext/train.safetensors:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████▉
|
20
.0GB
/
20
.0GB
2026
-09-15
13
:51:16.202890:
Done
Note that it needed to oversample -- that "2 iterators".  OpenWebText is about 40 GiB
uncompressed, and so that's about 10B GPT-2 tokens -- presumably just a little bit less.
Again, given that I was planning to use just the first 3.2B tokens of the dataset, I
didn't feel that it would matter.
I ran the check script on the newly-uploaded
Hugging Face dataset
and all looked well, so that was all set for the training run.
I upgraded
poppy
first with a
sudo pacman -Syu
to see if that helped with the
weird error that I got in the previous run (which, as I said, it looks like it did), then kicked it off:
giles@poppy:~/Dev/jax-gpt2-from-scratch
(
main
)
$
XLA_PYTHON_CLIENT_MEM_FRACTION
=
0
.95
uv
run
train.py
full-llm-full-train-with-mha-output-bias-openwebtext
datasets/
2026
-09-15
16
:42:32.606185
Downloading
dataset
Fetching
2
files:
100
%
|
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
2
/2
[
00
:00<
00
:00,
941
.38it/s
]
Download
complete:
:
0
.00B
[
00
:00,
?B/s
]
|
0
/2
[
00
:00<?,
?it/s
]
2026
-09-15
16
:42:32.879987
Loading
dataset
into
RAM
Download
complete:
:
0
.00B
[
00
:00,
?B/s
]
2026
-09-15
16
:45:40.438791
Creating
model
2026
-09-15
16
:45:43.840269
Creating
optimizer
2026
-09-15
16
:45:44.848351
Start
train
0
%
|
|
0
/33165
[
00
:00<?,
?it/s
]
2026
-09-15
16
:46:50.632075
Saving
checkpoint
1
%
|
█
|
332
/33165
[
24
:33<
38
:45:54,
4
.25s/it,
loss
=
6
.623,
tps
=
22
,154
]
About 31 hours in, it crashed again, but this time it was my own dumb fault:
poppy
has a relatively small disk and I ran out of space.  I fixed that and kicked it off
again from the most recent checkpoint, and this time it completed:
Training complete in 33,927.995 seconds
2026-09-17 11:25:10.835989 Tokens seen: 779,747,328
2026-09-17 11:25:10.835994 Throughput: 22,982 tokens/second
2026-09-17 11:25:10.836012 Final train loss: 3.165
2026-09-17 11:25:10.836018 Done
I converted it to PyTorch for the smoke test:
Every effort moves you through each phase, so it's not a complete picture.

I'm sure your story was
...which looked solid, so it was time for the test loss eval:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
~/Dev/jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-openwebtext/model.json
~/Dev/jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-openwebtext/checkpoints/latest/pytorch-model.safetensors
Fetching
4
files:
100
%
|
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
4
/4
[
00
:00<
00
:00,
674
.76it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
03
:59<
00
:00,
13
.37it/s
]
Loss
against
our
test
dataset:
4
.045255
Our worst score yet in this experiment!  Worse than any of my models so far, apart
from the two FineWeb-Edu ones I did without optimised hyperparameters.
Now, the first draft of this post went straight to the results from here, but the story wasn't
quite over yet...
Test set contamination
GPT-6 Astra is
relentless
.  Before I publish any of these posts, I run them past
an
editorial board of LLMs
to look for issues.  GPT-6 Astra not
only checked the text, it also visited the code I'd linked to to check that out too,
and spotted something problematic.
It's obvious in retrospect, but my code to build the new datasets had a high risk
of including the contents of the -- in theory held-back -- test set.  The way that
the test set was generated was that
I downloaded the 10B sample of FineWeb back in
December
,
splitting it into 99% training data and 1% "validation".  That validation split
was about 100M tokens, and I was only using the first 19M or so for actual validation
runs during training, so I (somewhat arbitrarily) designated about 19M other tokens
starting at position 50M in there as my test set.
Now, my new dataset-generation code was just sampling randomly from the complete
10B sample of FineWeb.  So there was nothing stopping it from pulling in data that
was in that old validation split!  That meant that it was quite likely that my new
"curated" and "50:50" datasets contained at least some of the test set that was meant to have
been held back from the models during training.
On reflection, the problem was potentially even worse.  FineWeb-Edu is a subset of
FineWeb; my existing FineWeb-Edu dataset came from the 10B sample of the Hugging Face
original, and so it also could potentially contain documents that I'd put into the test
set.
The first thing to do was to establish the size of the problem.  I wrote
a script
to
take in a "forbidden" dataset and split; this was assumed to be formatted as one big tensor of GPT-2 tokens,
which is what all of my datasets are.  It would then split it by end-of-text tokens, and
generate a hash and a token count for each resulting "document".  Optionally, you could
restrict it to only considering a subset -- the
n
tokens starting at position
p
-- and
it would then generate hashes/lengths for the documents inside that slice, or that overlapped
it at the start or the end.
I ran that to generate a list of hashes for the entire validation set -- the validation
split of
gpjt/fineweb-gpt2-tokens
-- and then
used
a second script
to check my various training sets (and the validation set itself) to see how much
of a contamination problem there was.  I got these results:
Dataset
Split
Contamination with validation set
gpjt/fineweb-gpt2-tokens
validation
102163003 out of 102163003 tokens (100.00%)
gpjt/fineweb-gpt2-tokens
train
636166 out of 102163003 tokens (0.62%)
gpjt/fineweb-edu-gpt2-tokens
train
672189 out of 102163003 tokens (0.66%)
gpjt/fw-fwedu-5050-gpt2-tokens
train
49224580 out of 102163003 tokens (48.18%)
gpjt/fw-fwedu-simplewiki-gpt2-tokens
train
44233824 out of 102163003 tokens (43.30%)
gpjt/openwebtext-gpt2-tokens
train
212 out of 102163003 tokens (0.00%)
So:
The validation set was 100% "contaminated" with itself, which was a useful sanity
check.
The training set of
gpjt/fineweb-gpt2-tokens
had what I felt was a small level
of contamination.  It was interesting that there was any at all -- I think that must
mean that there are some repeated documents in the original dataset, and some of
them wound up with copies in both my training and validation splits.
The
gpjt/fineweb-edu-gpt2-tokens
dataset also had what felt like a reassuringly
low level of contamination.
Both
gpjt/fw-fwedu-5050-gpt2-tokens
and
gpjt/fw-fwedu-simplewiki-gpt2-tokens
,
however, looked problematic.  In both cases, the training datasets had more than 40% of
the validation/test set in them.
gpjt/openwebtext-gpt2-tokens
was, as you'd expect, almost completely uncontaminated.
It looks like maybe one document happened to have been picked up by both the
OpenWebText and the FineWeb crawls and then included in the bit of FineWeb
I was using for validation.
However, these numbers -- while scary, at least for the 50:50 and the curated datasets -- were not quite the ones to use.  They showed
how much of the full validation set showed up in the full training set; what I actually
cared about was how much of the
test
set -- those 19M tokens starting at position 50M in
the validation split -- was in the actual subset of the training datasets that I actually
trained on -- the first ~3.2B of them.
I re-ran the script to generate hashes for just the test set, and then re-ran the
contamination-checking script, telling it just to look at the appropriate subset
of the training tokens, and got this:
Dataset
(first 3.2B tokens only)
Split
Contamination with test set
gpjt/fineweb-gpt2-tokens
train
26557 out of 19632681 tokens (0.14%)
gpjt/fineweb-edu-gpt2-tokens
train
32079 out of 19632681 tokens (0.16%)
gpjt/fw-fwedu-5050-gpt2-tokens
train
2986889 out of 19632681 tokens (15.21%)
gpjt/fw-fwedu-simplewiki-gpt2-tokens
train
2682430 out of 19632681 tokens (13.66%)
gpjt/openwebtext-gpt2-tokens
train
None
It was clear that there was a problem -- certainly with
gpjt/fw-fwedu-5050-gpt2-tokens
and
gpjt/fw-fwedu-simplewiki-gpt2-tokens
.  They'd seen what felt like a significant amount
of the test set while training, so their results on the test loss eval were dubious
at best.
I decided to train those two models afresh, and see what the result was in terms of loss.
If the difference was huge, I'd look into the risks of the (much smaller) contamination
of
gpjt/fineweb-gpt2-tokens
and
gpjt/fineweb-edu-gpt2-tokens
.  But if it was pretty
small, I'd not worry about that too much.
I extended the script that
prepared datasets
so that the config file could specify a
forbidden_dataset
.  Any documents in the
source datasets that matched forbidden ones would be excluded from the output.  I then
updated the config for
gpjt/fw-fwedu-5050-gpt2-tokens
and
gpjt/fw-fwedu-simplewiki-gpt2-tokens
so that the whole validation split of
gpjt/fineweb-gpt2-tokens
was forbidden, and
re-generated them.  You can see the updated datasets
here
and
here
.
Running the contamination-checker script against them showed that they were clear.
I then re-did the full training runs for those models; the uncontaminated version
of the 50:50 split model is
here
,
and the curated one is
here
.
And the good news: both of them actually did very slightly
better
at the test
loss eval than their equivalents that had been trained on the contaminated data:
Model
Contaminated
Test loss
JAX, FineWeb/FineWeb-Edu 50:50
No
3.449257
JAX, FineWeb/FineWeb-Edu 50:50
Yes
3.462454
JAX, curated
No
3.534068
JAX, curated
Yes
3.542460
There are a number of possibilities that come to mind; perhaps learning from the
test set just doesn't happen with tiny 163M models like this, or perhaps while the
contaminated models were learning, the benefit they got from that was outweighed by
the data that they got instead of the test set data being in some way better for
training purposes, at least in terms of the loss eval.
But anyway, I felt that if the effect of seeing more than 10% of the test set data
during training was so tiny, then the effect of seeing less than 0.2% -- which is what
the FineWeb-Edu model in this set of training runs had, as did all of my other FineWeb-only
models from previous experiments -- would be even smaller and I'd disregard it.
That was excellent news!  I didn't need to start all of my experiments from scratch.
For the rest of this post, I will include the numbers and results for the contaminated
models as well as the uncontaminated ones -- they're interesting for several reasons --
but for future posts I'll skip the contaminated ones.
So -- finally! -- let's start digging into the final results.
Results
Firstly, I think it's worth taking a look at all of the test loss results in
context.  Here they are in a table, with the new models in bold:
Test loss
OpenAI weights: medium
3.231442
JAX, overtrained one long epoch
3.324953
JAX, overtrained two normal epochs
3.326482
JAX, with MHA bias, no dropout
3.418784
JAX, no MHA bias, no dropout
3.420089
JAX, FineWeb/FineWeb-Edu 50:50 (uncontaminated)
3.449257
JAX, FineWeb/FineWeb-Edu 50:50 (contaminated)
3.462454
JAX, no MHA bias, with dropout
3.476802
OpenAI weights: small
3.499677
JAX, curated (uncontaminated)
3.534068
1xrtx3090-stacked-interventions
3.538161
JAX, curated (contaminated)
3.542460
8xa100m40-stacked-interventions-1
3.577761
JAX, FineWeb-Edu
3.632900
Cloud FineWeb, 8x A100 40 GiB
3.673623
1xrtx3090-baseline
3.683835
8xa100m40-baseline
3.691526
Cloud FineWeb, 8x H100 80 GiB
3.724507
Cloud FineWeb, 8x A100 80 GiB
3.729900
Cloud FineWeb, 8x B200 160 GiB
3.771478
Local FineWeb train
3.943522
JAX, openwebtext
4.045255
Local FineWeb-Edu extended train
4.134991
Local FineWeb-Edu train
4.166892
I think there's something very clear here: with the new models, the more FineWeb that was in the training
mix, the better the model did on this eval.  I think I might have been subconsciously
expecting that in the predictions I did before running these experiments, but
in retrospect it's so incredibly obvious that I feel silly for not mentioning it
explicitly!
But that tells us something interesting.  From the description in the paper, whatever OpenAI
did the GPT-2 training run on, it was not like FineWeb.  It was
probably
more
similar to OpenWebText -- and yet, that model was the one that performed the worst on
this test eval, so if it is more like OpenWebText, there must be some other factor involved.
But moving on for now: how about the IFT test -- the one that kicked off all of
this work in the first place?
I generated a set of IFT responses for all of the new models, and then ran them
(plus responses for all of the other models on that table above) past GPT 5.5, and
found that one of my new models was getting quite close to the original GPT-2 small
weights!  So I did four more runs, so that I could get an average.
Here are the results -- the "IFT score" is the average
across all five runs of the judge, and the "IFT rank" is based on that.  The "IFT epochs"
was from the original result-generation script.
Test loss
IFT epochs
IFT score
IFT rank
OpenAI weights: medium
3.231442
2
42.36
1
JAX, overtrained one long epoch
3.324953
3
18.67
7
JAX, overtrained two normal epochs
3.326482
4
18.71
6
JAX, with MHA bias, no dropout
3.418784
4
17.90
8
JAX, no MHA bias, no dropout
3.420089
5
20.50
4
JAX, FineWeb/FineWeb-Edu 50:50 (uncontaminated)
3.449257
4
17.69
9
JAX, FineWeb/FineWeb-Edu 50:50 (contaminated)
3.462454
4
19.30
5
JAX, no MHA bias, with dropout
3.476802
5
13.02
21
OpenAI weights: small
3.499677
2
25.19
2
JAX, curated (uncontaminated)
3.534068
4
16.63
10
1xrtx3090-stacked-interventions
3.538161
4
13.51
19
JAX, curated (contaminated)
3.542460
4
13.58
18
8xa100m40-stacked-interventions-1
3.577761
4
10.19
24
JAX, FineWeb-Edu
3.632900
4
24.56
3
Cloud FineWeb, 8x A100 40 GiB
3.673623
3
16.59
11
1xrtx3090-baseline
3.683835
4
15.15
12
8xa100m40-baseline
3.691526
3
13.64
16
Cloud FineWeb, 8x H100 80 GiB
3.724507
4
13.59
17
Cloud FineWeb, 8x A100 80 GiB
3.729900
3
10.79
23
Cloud FineWeb, 8x B200 160 GiB
3.771478
4
13.70
15
Local FineWeb train
3.943522
5
11.87
22
JAX, openwebtext
4.045255
4
13.28
20
Local FineWeb-Edu extended train
4.134991
5
14.29
14
Local FineWeb-Edu train
4.166892
5
14.69
13
If you want to see the full numbers, they're
below
.
The number that initially surprised me, and made me decide to do multiple LLM-judge runs was the one for the "JAX, FineWeb-Edu" model.  In my
first run it came in at 24.35 vs the OpenAI small weights' 24.93 -- so close that I wondered
if it might even beat them on a re-run.  However, in the further four runs its score was
consistently lower than the OpenAI model's, and the gap extended a bit in some.
So, was FineWeb-Edu the clear winner here?  Perhaps.  If you look at the contaminated/uncontaminated pairs,
something interesting pops out.  For the 50:50 mix, the model trained with the contaminated
dataset got 19.30, and the one trained on the uncontaminated one got 17.69 -- a difference
of 1.61.  For the "curated" dataset, the situation was even more interesting: uncontaminated
got 16.63, while contaminated got 13.58, a delta of 3.05 points.
Remember, the contamination issue is about whether or not the model saw the held-back
test set during training.  It was an issue for the test loss that is based on that test set,
but is entirely orthogonal to the IFT test.
From the IFT perspective, both contaminated and uncontaminated models in each case saw
training data that was -- in theory, at least -- essentially the same in terms of quality.
Indeed, the uncontaminated run saw almost the same data in the same order as the contaminated one,
except that some items were omitted, and then extra ones were added to the end.
The purpose of this set of experiments was to see how data quality affected the results
on the IFT test set.  But in the case of the curated model, something that should be
unrelated to data quality changed the results by 3.05 points!
If something as simple as changing which data of the same quality the model is trained with can affect
the IFT score so drastically, it makes it a bit harder to be certain as to whether or not data quality
really had the effect we were looking for.
On the other hand, the FineWeb-Edu model came in at 24.56, which is 4.06 points better than
the 20.50 that the closest other model got -- more than the 3.05 points we see in difference
between the two curated dataset models.  And it's worth noting that the model with 20.50 is
"JAX, no MHA bias, no dropout", which has a subtly different architecture -- no bias on the
output projection of the multi-head attention blocks.  A better comparison might be
"JAX, with MHA bias, no dropout", which got a score of 17.90, for a whacking great difference
of 6.66 points.
I think that without doing a very large number of training runs on different datasets with
different mixes, each one created with a different seed, it would be hard to work
out exactly what is in the noise here and what is not.
However, that would cost a lot in terms of time.  I think that the best thing here
is to chalk this up as a fairly decent indication that FineWeb-Edu improves matters for the IFT eval,
but far from a certainty.  But it's certainly worth noting that whatever the noise is,
it has a range of at least 3.05 points -- and the FineWeb-Edu model is just 0.63 points short of GPT-2 small!
So there could well be something there.  Of course, we don't know whether that model
got (by chance) the best possible balance of FineWeb-Edu tokens, and could never win -- or
whether it got a bad balance and would actually beat GPT-2 with a better one.  So that's
certainly worth keeping in mind.
As an aside, the result for the curated dataset really surprised me.  I had expected that it would be the best one,
simply because it almost certainly contained more facts.  I took a look at its answers to the questions --
one possibility that came to mind might be that it would get better responses to
questions like "What is the chemical symbol for chlorine" or "Who wrote Pride and Prejudice"
than the others, but would fail on less knowledge-based tasks.  But it was terrible
at fact-based questions too:
Name the author of 'Pride and Prejudice'.
The author of 'Pride and Prejudice' is Priscilla Finch.
What is the periodic symbol for chlorine?
The periodic symbol for chlorine is H.
As I understand it, many real-world training runs do include (often oversampled)
amounts of highly educational training data like this model's dataset did.  But perhaps
the models that I'm training are just too small to be able to make use of the data they gained that
way -- maybe doing things this way and expecting
good results is like asking six-year-old children to memorise stuff before they've learned enough
to be able to make use of it .  It's worth noting that the GPT-2 small model also
failed on those factual questions.
Well, anyway: I think we have some useful results here, so let's work out what
that means for next steps.
Conclusion
The results we got in these experiments point in two interesting directions.
The perfect connection between the amount of FineWeb in the training set and the
result on the (FineWeb-based) test loss eval, while perfectly obvious in retrospect,
really does highlight how mysterious it is that the OpenAI small weights do so well
on that test.
The fact that FineWeb-Edu did well on the IFT test tells us that there
does seem to be value in using richer training data -- though the less-spectacular
results of the 50:50 mix and the curated one weaken that a bit, as does the indicator
of what the noise due to data selection from equivalently high-quality datasets might be.  The OpenWebText
result I think I'll ignore, given that -- while in theory it should be similar to
what OpenAI trained on -- there are no guarantees, and it might differ in non-obvious
ways for non-obvious reasons.
I think that the right direction to take this going forward is to separate these two
angles.
I should chase a higher IFT score, and then once I have nailed that down, I should see what (if anything) might
allow me to get the resulting model to improve its test score.  But I will need to make
sure that whatever dataset I use, I use various "mixes" of it -- versions created
with different random seeds.
In my earlier experiments
with overtraining, I did find that it didn't seem to improve the IFT results -- but it
did
improve the test loss.  So perhaps identifying the right combination of other factors
to boost the IFT score, then overtraining the result, might help?
Of course, my
overtraining tests were with FineWeb, so the connection might not hold up as well if
the starting model (as seems likely) was trained on a different dataset.
Also, while working through the results here, I've come to the conclusion that the set of
models I'm using is a bit confusing -- there are now different hyperparameter settings,
small architectural differences (the MHA bias thing), dropout settings during the pre-training,
and now datasets.   I think that's OK for now; I should see this part of this series
as more ideation than actually running the proper experiments.  But at the end, when I
have some solid hypotheses with a reasonable amount of backup, I should start from scratch:
a baseline model, then staged interventions to build up to what (hopefully) will be a model
as good as GPT-2 small.
Anyway, I'll wrap this one up here.  I think that the next lever to pull is (perhaps
surprisingly) going to be weight tying.  I had previously kind of disregarded that as
a possibility, but while I was working on this post, something popped into my mind.
The OpenAI models were originally trained with weight tying.  My codebase does actually
support doing it -- but because I got the OpenAI weights I'm using from the code in
"
Build a Large Language Model (from Scratch)
",
when I'm running the IFT test, the weights are not actually tied!  We load up a model
that has separate but identical embedding and output head matrices, and then we fine-tune
that.  So those two matrices can vary independently during fine-tuning -- to put it
another way, while GPT-2 small was pre-trained with 124M parameters, the IFT test is
being done on a 163M-parameter version.  Does that
give them some non-obvious advantage?  And would adding weight-tying to my own models
help, either with or without the output heads being independent at fine-tuning time?
Stay tuned :-)
Appendix: all IFT judge runs
Here are the numbers for all of the IFT judge runs, included for completeness.  You
can see that the LLM judge ranks models very consistently between runs, but there is variation --
that is, on some runs it's in what I think of as a "better mood" than others, and
if that's the case, it will give better scores -- but it will give them almost consistently
between models, so all of the models do better.  Note that (unlike the table above)
this one is sorted by the average IFT score rather than the test loss.
Model
Run 1
Run 2
Run 3
Run 4
Run 5
Average
OpenAI weights: medium
42.24
42.16
42.95
41.83
42.61
42.36
OpenAI weights: small
24.93
24.96
25.39
25.01
25.66
25.19
JAX, FineWeb-Edu
24.35
24.55
24.3
24.68
24.9
24.56
JAX, no MHA bias, no dropout
20.5
19.9
20.76
21.25
20.07
20.50
JAX, FineWeb/FineWeb-Edu 50:50 (contaminated)
19.16
18.86
19.61
19.17
19.7
19.30
JAX, overtrained two normal epochs
18.47
18.29
19.17
18.69
18.91
18.71
JAX, overtrained one long epoch
18.04
18.71
19.62
18.41
18.57
18.67
JAX, with MHA bias, no dropout
17.49
17.35
18.33
17.73
18.62
17.90
JAX, FineWeb/FineWeb-Edu 50:50 (uncontaminated)
17.37
17.73
17.53
18.01
17.83
17.69
JAX, curated (uncontaminated)
16.77
16.03
17.3
16.08
16.96
16.63
Cloud FineWeb, 8x A100 40 GiB
16.44
16.23
17.14
16.62
16.54
16.59
1xrtx3090-baseline
14.85
15.07
15.19
15.14
15.51
15.15
Local FineWeb-Edu train
14.37
14.23
15.08
14.79
15
14.69
Local FineWeb-Edu extended train
14.4
14.07
13.82
14.56
14.61
14.29
Cloud FineWeb, 8x B200 160 GiB
13.37
13.05
13.85
13.67
14.57
13.70
8xa100m40-baseline
13.64
13.36
13.9
13.32
13.97
13.64
Cloud FineWeb, 8x H100 80 GiB
13.45
13.32
13.6
13.51
14.07
13.59
JAX, curated (contaminated)
13.09
13.48
13.95
13.23
14.15
13.58
1xrtx3090-stacked-interventions
13.37
13.11
14.04
13.84
13.17
13.51
JAX, openwebtext
12.88
12.7
13.74
13.53
13.53
13.28
JAX, no MHA bias, with dropout
13.19
12.86
12.98
12.85
13.24
13.02
Local FineWeb train
11.75
11.75
12.21
11.46
12.19
11.87
Cloud FineWeb, 8x A100 80 GiB
10.68
10.2
11.03
10.55
11.49
10.79
8xa100m40-stacked-interventions-1
9.44
9.79
10.84
10.2
10.66
10.19
Citing this post
This is a blog, and if you want to link to this post then please do :-)
                However, if you're writing something more academic and need to do
                a proper citation, then here's a BibTeX block to make things easier.
@misc{thomas2026oct-why-do-openai-gpt2-weights-beat-mine-5-data-quality,
  author       = {Thomas, Giles},
  title        = {{Why do OpenAI's GPT-2 weights beat mine?  Part five: data quality}},
  year         = {2026},
  month        = oct,
  howpublished = {Blog post},
  url          = {https://www.gilesthomas.com/2026/10/why-do-openai-gpt2-weights-beat-mine-5-data-quality},
}
