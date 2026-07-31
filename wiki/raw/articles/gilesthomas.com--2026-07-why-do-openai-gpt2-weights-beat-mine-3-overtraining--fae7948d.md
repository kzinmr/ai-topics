---
title: "Why do OpenAI's GPT-2 weights beat mine? Part three: testing overtraining"
url: "https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-3-overtraining"
fetched_at: 2026-07-31T10:24:10.929557+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Why do OpenAI's GPT-2 weights beat mine? Part three: testing overtraining

Source: https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-3-overtraining

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
The GPT-2-style models that I've been training work really well, and I've even
managed to train some that perform better than the original OpenAI small model
in terms of cross entropy loss on a test set.  But
as I wrote previously
,
there's a mystery: why do they perform worse on my instruction fine-tuning evaluation?
I had various theories about why that might be, and to me, the most plausible-seeming of them
was the amount of data they were trained with.  As best I can find out, OpenAI's models were, by modern
standards, trained on much more data than they should have been, while I'd used
the theoretically optimal amount of training data.
To put it in other words, OpenAI's models were overtrained.  If I deliberately
overtrained my own models, could I match their performance?  This post is a write-up
of what happened, but so as not to bury the lede -- it didn't seem to help much, if at all.
Let's see why.
Overtraining
Let's start by getting a nice crisp definition of overtraining.
It's important not to confuse overtraining with overfitting.  Overfitting is
where you train a model so that instead of learning a general rule about the
data it's seeing, it learns something very specific to the training data -- for example,
this:
...rather than this:
Overfitting is pretty much always a bad thing.
Overtraining, by contrast, is more of a judgement call.  For LLMs, it's generally used as a shorthand for
"training for more than the Chinchilla-optimal number of tokens".  The
Chinchilla paper
makes a very specific case:
if you train a model for roughly 20 times as many tokens as it has parameters, then
you'll have as good a model as you can get for that budget in terms of compute.
They were arguing against contemporaneous experiments where people were doing
things like doubling the number of parameters but training on the same amount of
data.
If you overtrain, it means that you're training on more than 20 tokens per parameter.
The Chinchilla argument is that instead of doing that, you should scale up the number of parameters and the number
of tokens equally to keep the 20x ratio.  Because the amount of compute used scales pretty much linearly
with both tokens and parameters, you'll spend the same amount and you'll get a better model that way.
Based on that heuristic, if you double your compute budget, then you should scale up your parameter count
by
2
and your training token count by the same amount, and by doing
that you'll get a better result than you would if you'd naively just doubled the parameters
or the tokens, for the same amount of compute time spent.
But overtraining is not always a bad thing.  Keeping things Chinchilla-optimal means
that you have to keep scaling up the model as you scale up the compute budget, and
often you can't do that -- for example, let's imagine you're training a model that's
meant to run on mobile phones.  You have a hard limit on the number of parameters:
what will fit in the target devices' RAM.
And importantly, in general you will still get a better model by overtraining -- just not
as much better as you would have done if you had been able to scale up the model as
well as the training tokens.
Now, as always, we don't know enough about the original GPT-2 training runs to be sure
as to whether they were overtrained, and if so, by how much.  But one thing that we
do know is that GPT-2 was trained in 2019, three years before the Chinchilla paper
came out, so they definitely didn't use it as a heuristic!
One thing that they do say in
the GPT-2 paper
is that their dataset, WebText, is "a total of 40 GB of text".  Assuming 4 bytes per token (a good
rule of thumb for the GPT-2 tokeniser), that's
10B tokens.  If the small model, which had 124M parameters, was trained on all of those, then it definitely was
overtrained; 124M times 20 is about 2.5B.
On top of that, there's the question of epochs.  In my training runs so far, I've been
training through a Chinchilla-optimal 3.2B unique tokens.  But being able to easily get your
hands on that much training data is a relatively new thing, as you can see from the
fact that the GPT-2 authors decided to document how they got theirs in the paper.
So back then, pre-Chinchilla, people tended to train for multiple epochs so that
they could make better use of limited data.
Now, when I first started training my models,
I tried to dig up some details on the GPT-2 training run beyond what was there in the paper.
I found
this report
,
and using data there, I
calculated
that it looked like OpenAI had trained for about 42 epochs over WebText.  The report's author
came up with 60 epochs as an equivalent-sized training run for their own dataset.
Again, those numbers are shaky; we don't have the real data.  But I think it's not
crazy to say that the OpenAI models were probably trained on more data than mine,
and probably over more than one epoch.  They were, in the Chinchilla sense, overtrained.
That makes perfect sense for the time, given that it was three years before the
Chinchilla paper!
But that opened up a couple of interesting experiments that I could try.
The experiments
Obviously I didn't want to train a model over 10B tokens (not least because I'd need
to download a larger sample of FineWeb).  And I certainly didn't want to do 42 epochs
of training, given that one epoch over 3.2B tokens took almost two days, even with
my relatively fast JAX code
.
But it seemed plausible that I'd be able to get at least some signal if I trained
longer.  I decided to use
poppy
, my new dedicated training box
to train two new models:
Firstly, I'd train one on 6.4B tokens from my FineWeb dataset -- the original 3.2B
that I had been training on to date, and then on whatever 3.2B came next.
Secondly, I'd train another one on the same 3.2B tokens as usual, but I'd do two
epochs.
I expected each training run to take a bit less than four days on
poppy
.
Once they were done, I would be able to evaluate the models, both with the test loss eval and the
IFT one.
In an unusual-for-me fit of scientific good practice, I decided to write down what I expected to
see up-front.  I felt that:
Both models would get better results on the test loss eval than my existing ones
(90% probability).  The one trained on more tokens would be better than the
one trained for two epochs on the same tokens (70%).
Both models would score better than my existing models in the IFT test (70%) but
would still be worse than GPT-2 small (90%).
It was time to find out!
The extended-train model
I kicked off the extended train, over 6.4B unique tokens, using my JAX code because it's
somewhat faster than the PyTorch version.  It crashed after about 40 hours, with
this error:
jax.errors.JaxRuntimeError: INTERNAL: CUDA error: Failed to end stream capture:
CUDA_ERROR_STREAM_CAPTURE_INVALIDATED: operation failed due to a previous error
during capture [executable_name='jit_train_step']
There were no obvious issues with the machine -- the CPU temperature had been hovering
at around 60°C, and GPU at around 70°C, as had been typical in training runs on
poppy
in the past.
There was nothing in
journalctl
or
dmesg
that looked suspicious.
On
Nvidia's documentation site
I found a mention of that error message, but the page in question was all about PyTorch;
I couldn't find anything relevant to JAX.
For now, I decided to chalk it up to some bug somewhere in the training stack, and only
dig in if it happened again.  So I kicked the training run off again from the latest checkpoint to see what happened,
and 38 hours later, it completed:
Training complete in 140,667.401 seconds
2026-07-24 03:36:02.148127 Tokens seen: 3,191,341,056
2026-07-24 03:36:02.148133 Throughput: 22,687 tokens/second
2026-07-24 03:36:02.148155 Final train loss: 2.979
2026-07-24 03:36:02.148163 Done
Note that the numbers there -- tokens seen, time taken, and so on -- are for the
portion of the training run after the restart.  My checkpoint recovery code doesn't carry
those over.  The final train loss is just the loss over the period from the penultimate
checkpoint to the end of the run -- there must have been some "easy" data there :-)
The training loss chart looked like this:
As you can see, the latest checkpoint wasn't the "best" one, so I pulled both latest and best down to
perry
, my workstation, for investigation.
Firstly, I ran them both through my JAX smoke test, which asks them to complete
"Every effort moves you" with 20 more tokens (using greedy sampling):
giles@perry:~/Dev/jax-gpt2-from-scratch
(
main
)
$
uv
run
test_generation.py
runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/best/model.safetensors
Every
effort
moves
you
forward.
The
best
way
to
get
started
is
to
start
with
a
simple,
easy
to
use
online
giles@perry:~/Dev/jax-gpt2-from-scratch
(
main
)
$
uv
run
test_generation.py
runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/latest/model.safetensors
Every
effort
moves
you
forward.
-
You
are
a
leader.
-
You
are
a
leader.
-
You
are
Very inspirational.  But coherent, and that's what matters.
Now, the bulk of my evals use PyTorch rather than JAX -- I've been
sticking to that for consistency -- so I converted the model Safetensors files so that
they had the right structure to work with that:
giles@perry:~/Dev/jax-gpt2-from-scratch
(
main
)
$
uv
run
convert_model_to_pytorch.py
runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/best/model.safetensors
runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/best/pytorch-model.safetensors
giles@perry:~/Dev/jax-gpt2-from-scratch
(
main
)
$
uv
run
convert_model_to_pytorch.py
runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/latest/model.safetensors
runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/latest/pytorch-model.safetensors
...and did the equivalent smoke test on that side (which uses non-greedy decoding
with a temperature of 1):
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_smoke.py
runs/1xrtx3090-baseline/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/best/pytorch-model.safetensors
Every
effort
moves
you
along
to
try
the
recipes
for
each
and
every
one
of
them
and
try
it
all
over
again.
You
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_smoke.py
runs/1xrtx3090-baseline/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/latest/pytorch-model.safetensors
Every
effort
moves
you
to
a
conclusion.
If
the
answer
for
each
of
our
goals
is
to
get
to
where
we�
I think that the Unicode junk at the end of the second is probably the first half
of a two-token apostrophe or something along those lines.  Anyway, those looked good.
Next, it was time to run the first eval: how would the models perform on the held-back
test set?
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
runs/1xrtx3090-baseline/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/best/pytorch-model.safetensors
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
593
.57it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
04
:54<
00
:00,
10
.88it/s
]
Loss
against
our
test
dataset:
3
.325897
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
runs/1xrtx3090-baseline/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/latest/pytorch-model.safetensors
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
1508
.74it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
04
:54<
00
:00,
10
.86it/s
]
Loss
against
our
test
dataset:
3
.324953
So, the "latest" checkpoint was better than the "best" one.
This is a problem with
the way I define "best" in my training script.  The original version of that script used a validation
set to evaluate the model before every checkpoint; "best" at that point meant that the
model was the best performer on that validation set.  Later on, I decided to play a little
loose with my training runs and pull out the validation -- this seemed
reasonably
safe because I was doing single-epoch training, so what I saw as the primary benefit
of regular validation during training -- detecting overfitting by looking for rising
validation loss -- was not so important.  It's hard for a model to overfit on a single
epoch training run.
However, doing that meant that "best" had to be changed
to mean "best-performing on the training data".  And that's actually a really bad metric,
because the training data is different for each measurement, so they're not really
comparable.
So, for this model, I decided that I'd discard the "best" checkpoint, and use the "latest" one.
But all of that aside, those numbers were pretty impressive!  Not only did it beat my
best Chinchilla-optimal model to date,
which had got 3.418784 loss on the same eval, and the original OpenAI small model with a loss of 3.499677,
but it was actually getting quite close to the OpenAI medium's loss of 3.231442.
Promising!
So now it was time for the two-epoch training run.
The two-epoch model
Adding support for handling multiple epochs to the code was
very simple
,
so having done that, I kicked it off.
Just over three days later:
Training complete in 282,366.091 seconds
2026-07-27 20:14:26.124497 Tokens seen: 6,520,504,320
2026-07-27 20:14:26.124503 Throughput: 23,092 tokens/second
2026-07-27 20:14:26.124518 Final train loss: 3.547
2026-07-27 20:14:26.124524 Done
This time the numbers are for the full training run -- there were no odd CUDA issues,
and it ran straight through.  Again, the final train loss is just the loss over the period from the penultimate
checkpoint to the end of the run.  For runs over the same dataset, it can actually
be a useful quick-and-dirty way to compare results before running the full evals,
but in this case it's obviously not comparable with the last run's result there,
because we're talking about loss on different data.
Anyway, once again, "best" and "latest" were different checkpoints, as you can see from
the loss chart:
...so I pulled them both
to
perry
, did the first smoke test:
giles@perry:~/Dev/jax-gpt2-from-scratch
(
main
)
$
uv
run
test_generation.py
runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/best/model.safetensors
Every
effort
moves
you
forward,
and
you’ll
be
able
to
see
the
results.
The
best
way
to
get
giles@perry:~/Dev/jax-gpt2-from-scratch
(
main
)
$
uv
run
test_generation.py
runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/latest/model.safetensors
Every
effort
moves
you
forward,
and
you’re
not
alone.
The
most
important
thing
is
to
be
able
to
...converted them to PyTorch:
giles@perry:~/Dev/jax-gpt2-from-scratch
(
main
)
$
uv
run
convert_model_to_pytorch.py
runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/best/model.safetensors
runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/best/pytorch-model.safetensors
giles@perry:~/Dev/jax-gpt2-from-scratch
(
main
)
$
uv
run
convert_model_to_pytorch.py
runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/latest/model.safetensors
runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/latest/pytorch-model.safetensors
Did the PyTorch smoke test:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_smoke.py
runs/1xrtx3090-baseline/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/best/pytorch-model.safetensors
Every
effort
moves
you
to
take
on
a
larger
responsibility.
We’re
here
to
help
you.
We�
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_smoke.py
runs/1xrtx3090-baseline/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/latest/pytorch-model.safetensors
Every
effort
moves
you
closer,
and
you
become
a
better
person
as
the
year
progresses.”
There’s
So that all looked good (despite the Unicode junk), and it was time to work out the
loss:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
runs/1xrtx3090-baseline/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/best/pytorch-model.safetensors
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
3507
.68it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
04
:55<
00
:00,
10
.83it/s
]
Loss
against
our
test
dataset:
3
.332157
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
runs/1xrtx3090-baseline/model.json
../jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/latest/pytorch-model.safetensors
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
1760
.09it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
04
:53<
00
:00,
10
.90it/s
]
Loss
against
our
test
dataset:
3
.326482
That was pleasingly in line with my predictions:
Both models would get better results on the test loss eval than my existing ones
  (90% probability).  The one trained on more tokens would be better than the
  one trained for two epochs on the same tokens (70%).
...though of course the difference between the 3.326482 that this model got and the
3.324953 that the one-long-epoch one got was tiny and probably in the noise.  I decided to
count it as a win, anyway :-)
So now it was time for the big test: how would they do at instruction-following?
At last, the IFT test!
There are two phases to getting numbers for this test: firstly, I run
the script
that does the fine-tuning, and then generates the model's completions for the
test set using the fine-tuned model.  These are written to a JSON file for later
use by the LLM-as-a-judge script.  That script is the one I fixed in my
previous post
.
I ran it for the extended train (one long epoch) model, taking care to make sure
that the config it was passed matched the model's original training run in not
having dropout enabled:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
ift_generate_test_responses.py
jax-mha-bias-extended-train
runs/1xrtx3090-stacked-interventions/model.json
~/Dev/jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-extended/checkpoints/latest/pytorch-model.safetensors
Epoch
0
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
116
/116
[
00
:06<
00
:00,
18
.23it/s
]
Val
loss
still
decreasing,
continuing
Epoch
1
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
116
/116
[
00
:06<
00
:00,
18
.54it/s
]
Val
loss
still
decreasing,
continuing
Epoch
2
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
116
/116
[
00
:06<
00
:00,
18
.54it/s
]
Val
loss
still
decreasing,
continuing
Epoch
3
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
116
/116
[
00
:06<
00
:00,
18
.58it/s
]
Val
loss
rising,
bailing
out
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
110
/110
[
00
:08<
00
:00,
13
.40it/s
]
Next, I ran it for the two-epoch model:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
ift_generate_test_responses.py
jax-mha-bias-2-epoch
runs/1xrtx3090-stacked-interventions/model.json
~/Dev/jax-gpt2-from-scratch/runs/full-llm-full-train-with-mha-output-bias-2-epoch/checkpoints/latest/pytorch-model.safetensors
Epoch
0
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
116
/116
[
00
:06<
00
:00,
18
.13it/s
]
Val
loss
still
decreasing,
continuing
Epoch
1
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
116
/116
[
00
:06<
00
:00,
18
.22it/s
]
Val
loss
still
decreasing,
continuing
Epoch
2
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
116
/116
[
00
:06<
00
:00,
18
.34it/s
]
Val
loss
still
decreasing,
continuing
Epoch
3
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
116
/116
[
00
:06<
00
:00,
18
.48it/s
]
Val
loss
still
decreasing,
continuing
Epoch
4
:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
116
/116
[
00
:06<
00
:00,
18
.32it/s
]
Val
loss
rising,
bailing
out
100
%
|
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
110
/110
[
00
:10<
00
:00,
10
.06it/s
]
With that done, it was time to run
the LLM as a judge script
.
That gave us results, which I've put into the table below.  For each model, I've shown
the number of epochs of training the model needed before its
validation loss started rising.  For the pre-existing models, I've shown the
score that they got in my baseline evaluation at the end of my
last post
, and their
ranking in that eval.  Then for all models, there's the score from this new run, and
the new ranking. The two new models are in
bold.
Test loss
IFT epochs
Old IFT score
Old IFT rank
New IFT score
New IFT rank
OpenAI weights: medium
3.231442
2
42.41
1
42.91
1
JAX, overtrained one long epoch
3.324953
3
18.75
5
JAX, overtrained two normal epochs
3.326482
4
18.45
6
JAX, with MHA bias, no dropout
3.418784
4
18.12
5
17.53
8
JAX, no MHA bias, no dropout
3.420089
5
20.72
3
20.25
3
JAX, no MHA bias, with dropout
3.476802
7
16.98
8
16.73
10
OpenAI weights: small
3.499677
2
26.11
2
25.66
2
1xrtx3090-stacked-interventions
3.538161
4
13.68
11
13.35
14
8xa100m40-stacked-interventions-1
3.577761
4
9.81
15
10.33
17
Cloud FineWeb, 8x A100 40 GiB
3.673623
6
19.45
4
19.76
4
1xrtx3090-baseline
3.683835
6
13.39
12
13.74
13
8xa100m40-baseline
3.691526
4
14.64
9
14.11
11
Cloud FineWeb, 8x H100 80 GiB
3.724507
4
13.84
10
13.84
12
Cloud FineWeb, 8x A100 80 GiB
3.729900
4
11.30
14
11.13
16
Cloud FineWeb, 8x B200 160 GiB
3.771478
4
11.82
13
11.22
15
Local FineWeb train
3.943522
7
8.93
16
8.73
18
Local FineWeb-Edu extended train
4.134991
7
17.10
7
17.42
9
Local FineWeb-Edu train
4.166892
7
17.28
6
17.61
7
A note on the numbers: in my previous post, I mentioned that different LLM judge
  runs differ due to randomness in how "strict" the judge model is.  You can see that
  showing up here -- most of the old/new IFT scores are pretty close, within a point or so,
  but they do differ, some rising and some falling.
  This is with exactly the same set of responses for each model going into the judging program -- I used the
  same JSON files for this table as I did for the previous one for the models that were in there
  -- the only difference was that the new JSON files for the new models were added.
As you can see, the new models scored better than the "JAX, with MHA bias, no dropout"
one, which is the most similar: it's the same model config, just trained for the
Chinchilla-optimal number of tokens.  The one long epoch model got a score that was
1.22 higher than that one, and the two-epoch one scored 0.92 higher.
However, my normal rule of thumb for comparing models in these evals is that differences
of less than a point or two are
probably
in the noise.
I did a second run of the LLM judge script -- it takes 20 minutes to run and costs
a couple of dollars each time, so I don't like to run it all that often -- and this time
around (just looking at the JAX numbers) things were a bit closer:
IFT score
JAX, overtrained one long epoch
18.45
JAX, overtrained two normal epochs
19.45
JAX, with MHA bias, no dropout
18.30
JAX, no MHA bias, no dropout
21.04
JAX, no MHA bias, with dropout
17.33
You can also see that the two new models have swapped places.
So I think that the principled approach here is to say that the improvement is
almost certainly in the noise.  Perhaps if I did a very large number of runs of the judge
I'd get something more solid -- but what I'm hoping for is something a little more
unambiguous; some change that really moves the needle in an obvious way, clearly
outside the noise.
That means that my second pre-registered prediction:
Both models would score better than my existing models in the IFT test (70%) but
  would still be worse than GPT-2 small (90%).
...was half wrong.  I got the "worse than GPT-2 small" bit right, at least.
But while the models did look a bit better than the most similar pre-existing model,
(a) the difference was too small for me to be confident in it, and (b) they were
still worse than "JAX, no MHA bias, no dropout" and "Cloud FineWeb, 8x A100 40 GiB".
What can we take away from this?
Conclusion
The hypothesis that I was trying to test was whether it was simply overtraining that
made the OpenAI weights better at this IFT evaluation than mine.  Frustratingly, I can't say that
the hypothesis was false.
Perhaps there is an improvement gained by overtraining --
and the apparent gains which, on this experiment, appeared to be in the noise,
would have been consolidated if I'd trained for even longer -- perhaps the 42 epochs
on 10B tokens I suspect that the original weights were trained on?
But equally, perhaps there is no benefit, and further training would have left the
models exactly where they were in the ranking.
Intuitively, you'd think that further training of a model would make it better at
answering questions, at least up until the point that its parameters were "saturated"
and could not absorb new information without forgetting something else.  After all, a
model that's never seen "Jane Austen wrote 'Pride and Prejudice'" will never be able to
successfully answer when it's asked who the book's author was.
But where that saturation point might be -- and indeed how much training you'd need to do to
get there -- is not obvious.
It's an annoying place to finish this experiment, but I guess at least an inconclusive result
is better than never having run it at all.  And it was at least good to see the test
loss improvement that I expected.
But given the opportunity cost of tying up
poppy
in four-day training runs, I think I'll
look into other possibilities next.
As I was running this experiment, something came up -- and I'll post about that soon.
Luckily, this time it won't involve training more base models...
