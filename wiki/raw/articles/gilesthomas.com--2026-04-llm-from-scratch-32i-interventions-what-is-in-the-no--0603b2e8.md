---
title: "Writing an LLM from scratch, part 32i -- Interventions: what is in the noise?"
url: "https://www.gilesthomas.com/2026/04/llm-from-scratch-32i-interventions-what-is-in-the-noise"
fetched_at: 2026-05-01T07:02:05.499100+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Writing an LLM from scratch, part 32i -- Interventions: what is in the noise?

Source: https://www.gilesthomas.com/2026/04/llm-from-scratch-32i-interventions-what-is-in-the-noise

Archives
Categories
Blogroll
Towards the end of last year, I
trained a 163M-parameter GPT-2-style model from scratch on my local RTX 3090
,
using code based on
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
".
The result was a pretty decent little model, but it wasn't as good as the original
GPT-2-small, despite having more parameters (because it wasn't using weight-tying).
Specifically: on a particular test set, my model gave a loss of 3.944 -- quite a lot
more than the original GPT-2's 3.500 on the same dataset.
I wanted to see whether I could train a model on my own hardware (or on something that
didn't cost too much to rent in the cloud) that got closer to the original model's
performance.  So over the last few months, I've done a bunch of further training runs, each one testing
a specific intervention -- a stand-alone change that I expected to change the loss, either
for better or for worse.  Specifically:
I trained
a baseline model
on
an 8x A100 40 GiB per GPU machine on Lambda (which
was better than my original locally-trained model, I believe due to the larger batch size
that the larger machine made possible).
I tried
adding gradient clipping
to see if that would help by limiting the effects of loss spikes.
I tried
removing dropout
, given
that these days people tend not to use it (because we're doing single-epoch training runs).
I tried
adding bias to the attention weight matrices
--
something that was popular back in the GPT-2 era, and was used by the original weights, but which my code did not use.
Instead of just using the learning rate of 0.0004 that was used in the code from
the book, I looked into what values people use these days, and learned how
to
schedule it over the course of the training run
.
Similarly, I learned more about
weight decay
and
tried some alternative values.
Then I tried making my model more like the original GPT-2 one by introducing
weight tying
to
see if that would help.
Finally, I decided to try
training in "full-fat" float32
instead of using PyTorch's AMP and TF32 matrix multiplication performance
enhancements.
At the end of all of that, I had this table showing the effect of each intervention
in terms of loss on the test set.  They're sorted from least-effective to most-effective,
and you can see the baseline in there too:
Test set loss
Improvement vs baseline
8xa100m40-weight-tying
3.874
-0.182
8xa100m40-weight-decay-cerebras
3.867
-0.175
8xa100m40-baseline
3.692
-
8xa100m80-no-amp
3.679
0.013
8xa100m40-gradient-clipping
3.678
0.014
8xa100m40-qkv-bias
3.669
0.023
8xa100m40-weight-decay-gpt2
3.643
0.049
8xa100m40-remove-dropout
3.641
0.051
8xa100m40-schedule-learning-rate
3.602
0.09
Winners and losers are reasonably clear:
Weight tying and the number for weight decay I derived from a paper by
Cerebras Research (probably without understanding it properly) were negatives.
Full-fat float32, gradient clipping,  attention biases, the GPT-2 weight decay
parameter, removing dropout, and scheduling (and updating) the learning rate
were positives.
So, for an optimal train, we'd just use the effective interventions, right?
Well, not quite.
Full-fat float32 I decided wasn't worth the effort, as it meant that the
train took more than twice as long, and (because it required a larger machine), cost
more than three times as much.
The others did look like solid changes, but there was one concern.  The effect of
each intervention is actually pretty small.  For example, gradient clipping reduced
the loss by 0.014, from 3.692 to 3.678.  That's a 0.3% improvement.  Even the best
intervention, scheduling the learning rate, only improved things by 2%.
Could it be that some or all of these improvements were not real, but just a result
of the random nature of training deep neural networks?  Could the differences just
be in the noise?  They seemed small enough for that to be possible.
I've trained seven more models over the last few days to try to get a feel as to how
big an effect noise has for this kind of training run.  The results appear to show
that variations in the initial weights matter quite a lot, but randomness in the
training loop (given the same initial weights) actually has a fairly minimal impact.
That surprised me a bit!
Let's go through the details.
Is my random seed code working?
When I did the original baseline training run -- creating the model that was the
comparison point for all of the interventions --
I wanted to minimise the amount of random number-induced differences
between the training runs in this interventions series.  I did this by setting the random seed
at the start -- specifically, I had this code:
seed
=
42
random
.
seed
(
seed
)
torch
.
manual_seed
(
seed
)
torch
.
cuda
.
manual_seed_all
(
seed
)
At the time I wrote it, this seemed pretty complete -- the seed is set on Python's
own random number generator, on PyTorch's, and on the separate ones it uses for CUDA.
However, in a separate project, where I was fine-tuning a Qwen model as a classifier,
I'd found that this wasn't enough.  In order to get full reproducibility, I'd had to
lock things down a bit more, with this additional code:
torch
.
backends
.
cudnn
.
deterministic
=
True
torch
.
backends
.
cudnn
.
benchmark
=
False
torch
.
use_deterministic_algorithms
(
True
)
So: was my random number seed code enough for this case?  Or would I get a different
model if I ran the same code a second time?
That was easy enough to do; I spun up a machine, and just ran the "baseline" train
again.  3 hours 24 minutes later:
Training complete in 12,276.306 seconds
Tokens seen: 3,260,252,160
Throughput: 265,573 tokens/second
Final train loss: 3.743
Interestingly, that was exactly the same final train loss as the original baseline
train.
Here's the model
.
I ran my normal smoke test, asking it to complete "Every effort moves you"
Every effort moves you in the way of getting into that.
I will let you down as you move, not by
...so that was OK -- the model was generating reasonably coherent text.
Then I ran the eval to find its loss on the test set:
Loss against our test dataset: 3.692
Exactly the same as the original baseline!  That was certainly promising.  Now, the
use of three decimal places for the output from the loss eval is just a formatting thing,
so I bumped it up to 6 dps, and the new model got this:
Loss against our test dataset: 3.691526
Running that against the original baseline model:
Loss against our test dataset: 3.691526
Again, exactly the same.  Finally, more out of idle interest than anything else,
I decided to see if the models were at least different:
giles@perry:~/Dev/ddp-base-model-from-scratch (main)$ diff runs/8xa100m40-baseline/checkpoints/best/model.safetensors runs/8xa100m40-baseline-2/checkpoints/best/model.safetensors
giles@perry:~/Dev/ddp-base-model-from-scratch (main)$
That is, quite frankly, amazing to me.  I was expecting pretty close results, but
what we're seeing here is that two separate models, trained on the same data, but
on different machines more than a month apart, have weights that are bit-wise identical.
No random noise at all.
That's actually really reassuring!  It makes me much more comfortable that we're
standing on a stable foundation here.
Now it was time to see what effect changing that random seed would have.
Changing the random seed
Let's think about what the random seed does.  When we call
random.seed(42)
, we're
initialising Python's pseudo-random number generator so that it will start at a particular
point -- after we've called it, it will generate the same sequence of "random" numbers
each time it's asked for a new one.  So the effect of this code:
seed
=
42
random
.
seed
(
seed
)
torch
.
manual_seed
(
seed
)
torch
.
cuda
.
manual_seed_all
(
seed
)
...is to initialise three separate pseudo-random number generators to be in a known
deterministic state, so they'll all generate the same sequence in every run.
So, the first thing to do was to see what happened if we changed that number.
I decided to do two training runs, each with exactly the same code as the baseline,
but with different random seeds.  Firstly, I changed it from 42 to 22 :
ubuntu@130-61-223-25:~/ddp-base-model-from-scratch$
git
diff
diff --git a/ddp_train.py b/ddp_train.py
index 5519353..16a8be5 100644
--- a/ddp_train.py
+++ b/ddp_train.py
@@ -623,7 +623,7 @@ def main(run, datasets_dir_path, checkpoint, find_max_microbatch_size):
dist.init_process_group(backend, device_id=local_rank)
#
Set
all
of
the
random
seeds
-    seed = 42
+    seed = 22
random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
That training run completed:
Training complete in 12,287.950 seconds
Tokens seen: 3,260,252,160
Throughput: 265,321 tokens/second
Final train loss: 3.724
Here's the model
.
Time for the evals; the smoke test:
Every effort moves you a few spots in your path. Sooner, just think twice how many steps you take. If
...and the loss test:
Loss against our test dataset: 3.673453
So, that's 3.673453 compared to 3.691526, an improvement of 0.018 over the run with a seed
of 42.  That's more than
the 0.014 improvement we got from gradient clipping (and indeed, the 0.013 from full-fat float32
training), and quite close to the 0.023 improvement from adding attention weight bias.
Time for another training run:
ubuntu@141-148-168-241:~/ddp-base-model-from-scratch$
git
diff
diff --git a/ddp_train.py b/ddp_train.py
index 5519353..1e9b5bc 100644
--- a/ddp_train.py
+++ b/ddp_train.py
@@ -623,7 +623,7 @@ def main(run, datasets_dir_path, checkpoint, find_max_microbatch_size):
dist.init_process_group(backend, device_id=local_rank)
#
Set
all
of
the
random
seeds
-    seed = 42
+    seed = 67
random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
ubuntu@141-148-168-241:~/ddp-base-model-from-scratch$
Another 3h24m later:
Training complete in 12,263.076 seconds
Tokens seen: 3,260,252,160
Throughput: 265,859 tokens/second
Final train loss: 3.704
Here's the model
.
The smoke test:
Every effort moves you to a new level. The next phase is a one-way street in which you are free to
...and the test set loss:
Loss against our test dataset: 3.653593
A further improvement!  That's 0.038 better than our original baseline, which beats
adding on attention weight bias (though it's worse than the weight decay update).
Now, three data points is rather a small number for any kind of statistical
analysis, but just out of interest, let's do the basics.
GeeksForGeeks has a good refresher here
if you're a bit
rusty.
Firstly, our mean is
μ
=
3.691526
+
3.673453
+
3.653593
3
≈
3.672857
...and our variance is:
σ
2
=
(
3.672857
−
3.691526
)
2
+
(
3.672857
−
3.673453
)
2
+
(
3.672857
−
3.653593
)
2
3
≈
0.000240
If we take the square root of that, we get the standard deviation (SD):
σ
=
0.000240
≈
0.0154919
So, if we assume a normal distribution, what would that say about our results?  Here's
the results table again.
Test set loss
Improvement vs baseline
8xa100m40-weight-tying
3.874
-0.182
8xa100m40-weight-decay-cerebras
3.867
-0.175
8xa100m40-baseline
3.692
-
8xa100m80-no-amp
3.679
0.013
8xa100m40-gradient-clipping
3.678
0.014
8xa100m40-qkv-bias
3.669
0.023
8xa100m40-weight-decay-gpt2
3.643
0.049
8xa100m40-remove-dropout
3.641
0.051
8xa100m40-schedule-learning-rate
3.602
0.09
If we assume that the results are on a normal distribution:
We would expect ~68.2% of results to be within one SD of the mean -- that is, between
3.6573651 and 3.6883489.  Interestingly, our actual baseline result is outside that
range!  But it does include both the gradient clipping and the
QKV bias results.
We would additionally expect ~95.4% of the results to be within two SDs, which is
3.6418732 to 3.7038408.  That includes our baseline and our weight decay result (though not our experiment
removing dropout -- the six-DP loss number for that is 3.641282).
Finally, we'd expect ~99.7% of results to be within three SDs, which is a range from
3.6263813 to 3.7193327.  That covers all of our positive results apart from scheduling learning
rate!
That seemed a bit saddening -- were all of the results apart from scheduling the learning
rate within the noise?
Well, so as I said, three data points is too small a number to take those results
without a fistful of salt.  I was thinking of perhaps trying another few random seeds
to see what would happen, and perhaps to tighten those numbers up a bit, but then something
occurred to me -- randomness was being used in two different ways in the training
run, and perhaps we could separate them?
Breaking the randomness apart
Where do we use the random numbers?  Well, immediately after we set the seeds, we create
our uninitialised model for training:
model
=
GPTModel
(
model_conf
)
.
to
(
local_rank
)
One of the random number generators -- Python's, PyTorch's, or one of the CUDA ones -- will be used to generate the initial weights
that we're going to start training.  That means that
for the same model setup
, we'll
always start with exactly the same weights.  But if the model settings change
such that we initialise different things in a different order, then we'll have different weights.
After we've done that, we go into the training loop.  That
can have
randomness in it;
although the AdamW optimiser itself is deterministic, we are (in all but one of these training
runs) using dropout, which drops a random bunch of activations at various points -- 10% of
them with our config.  And it seems entirely possible that each of the interventions
could change the order of execution of different steps in non-obvious ways, which would
lead to dropout being applied in different ways in different runs.
So, the question was: what kinds of randomness -- in terms of the initial weights, or
in terms of the training run -- did each intervention potentially change vs the baseline?
Disregarding the full-fat float32 run:
Gradient clipping: randomness only affected the training run -- the weights it started with
would have been exactly the same as the baseline model's.
Removing dropout: although this is a parameter on the model, I don't think it changes
the initial weights.  But in the training run, it certainly does affect randomness
by removing its use of the random number generator.
Adding bias to the attention weights.  This will change both the initial weights -- because
we have those bias weights, things will be initialised differently -- and as a result, the training run,
as the random number generator will have been sampled a different number of times
prior to the run.
Changing and scheduling the learning rate certainly should not change the initial
weights, but it might conceivably have a non-obvious effect on training.
Likewise weight decay; no effect I can see on the initial weights, but it could well
change training dynamics.
Weight-tying.  When I
added it to the code
, I
tried to do so in such a way that the other weights would be unaffected -- I created
exactly the same weights as I would without weight tying, then threw away the output
head and replaced it with a reference to the input embedding weights.  So I think
that in theory, this one won't have changed the other model weights (apart from ignoring
the initialised-but-thrown-away output head), but it could well have
changed the training run.
Given that, I wanted to get two measures of how sensitive to noise each phase of
the training run was: the initialisation of weights at the start, and the training
run itself.
I decided to start by nailing down exactly what the training run started with.
Loss changes with the same weights but different training run seeds
We already had a baseline training run with a specific state of the random number
generator at the start; in our "real" baseline, we seeded with 42 at the start,
and then initialised our weights.  After that, the random number generator would
have reached some specific state based on its initial seed and how many numbers had been generated so far.
Now, in theory, we could get the RNG into that specific state by seeding it with some
number
A
at that point.  We don't know what
A
is, of course.  But it seems vanishingly
unlikely that it would be something we'd come up with -- specifically, we can be
pretty sure that
A
≠
23
and
A
≠
67
.
So, I put the old initial seed of 42 back in, but re-seeded after the model
had been initialised:
Firstly, with a re-seed value of 23:
ubuntu@167-234-217-254:~/ddp-base-model-from-scratch$
git
diff
diff --git a/ddp_train.py b/ddp_train.py
index 5519353..7b7993c 100644
--- a/ddp_train.py
+++ b/ddp_train.py
@@ -643,6 +643,12 @@ def main(run, datasets_dir_path, checkpoint, find_max_microbatch_size):
else:
scaler = None
+    # Set all of the random seeds again
+    seed = 23
+    random.seed(seed)
+    torch.manual_seed(seed)
+    torch.cuda.manual_seed_all(seed)
+
datasets_dir = Path(datasets_dir_path)
dataset_name = train_conf["dataset"]
dataset_dir = datasets_dir / dataset_name
ubuntu@167-234-217-254:~/ddp-base-model-from-scratch$
I let that run....
Training complete in 12,263.247 seconds
Tokens seen: 3,260,252,160
Throughput: 265,856 tokens/second
Final train loss: 3.731
...and got
this model
.  Time
for the normal evals:
Every effort moves you into a relationship in a world full of meaning and the beauty of your character that you will never forget
...and:
Loss against our test dataset: 3.681356
Next, I did another training run, the same as the previous one, but with 67 instead of 23
for the re-seed:
ubuntu@141-148-168-241:~/ddp-base-model-from-scratch$
git
diff
diff --git a/ddp_train.py b/ddp_train.py
index 5519353..90b902a 100644
--- a/ddp_train.py
+++ b/ddp_train.py
@@ -643,6 +643,12 @@ def main(run, datasets_dir_path, checkpoint, find_max_microbatch_size):
else:
scaler = None
+    # Set all of the random seeds again
+    seed = 67
+    random.seed(seed)
+    torch.manual_seed(seed)
+    torch.cuda.manual_seed_all(seed)
+
datasets_dir = Path(datasets_dir_path)
dataset_name = train_conf["dataset"]
dataset_dir = datasets_dir / dataset_name
That one ran:
Training complete in 12,245.932 seconds
Tokens seen: 3,260,252,160
Throughput: 266,231 tokens/second
Final train loss: 3.732
...producing
this model
,
which eval'ed like this :
Every effort moves you and I back home, to ensure the security of these children, but in this age transition to a
...and...
Loss against our test dataset: 3.680505
Let's bring those together:
Our normal baseline: weights initialised with seed 42, and training run starts
with a "seed" of our imaginary
A
value from above: 3.691526
The first run above: weights initialised with seed 42, and training run starts
with a seed of 23: 3.681356
The second run above: weights initialised with seed 42, and training run starts
with a seed of 67: 3.680505
That's a mean of ~3.684462, with a variance of ~0.0000752 and a standard deviation
of ~0.008672.  Those are
tiny
compared to the numbers from the two trains we did
with the change of the seed prior to the model initialisation.
That actually surprised
me a bit; we're using dropout in all of these training runs, and it's dropping a random
10% of activations in every forward training pass.  With our different training run
starting seeds, they should be getting very different dropout patterns.  Hand-wavingly,
perhaps over the three million or so sequences we're training on, it averages out?
Still a little counterintuitive, though.
Anyway, let's take a look at the intervention results again, this time
highlighting the ones that we believe will be starting with the same weights:
Test set loss
Improvement vs baseline
8xa100m40-weight-tying
3.874
-0.182
8xa100m40-weight-decay-cerebras
3.867
-0.175
8xa100m40-baseline
3.692
-
8xa100m80-no-amp
3.679
0.013
8xa100m40-gradient-clipping
3.678
0.014
8xa100m40-qkv-bias
3.669
0.023
8xa100m40-weight-decay-gpt2
3.643
0.049
8xa100m40-remove-dropout
3.641
0.051
8xa100m40-schedule-learning-rate
3.602
0.09
Using the "99.7% should be within three SDs" heuristic, we get a range of
3.658446 - 3.710478.  Of the intervention runs with (I believe) stable weights, only the no-AMP
and the gradient clipping ones are within that range.
That made me feel quite positive.  If my beliefs are correct about which runs have the same
weights, then noise in the training runs seems unlikely to be causing
the differences -- that is, perhaps the results from the interventions for those
same-weight training runs are real signal and not just noise.
What would happen if instead of pinning the seed for generating the weights and
varying the starting seed for the training run, we varied the weight seed and
pinned the training one?
Loss changes with different weights but the training run seed nailed down
We'd already done a training run with a seed of 42 before generating the weights
and a re-seed to 23 after that:
The first run above: weights initialised with seed 42, and training run starts
with a seed of 23: 3.681356
So I decided to see what would happen if I varied the pre-weights initialisation seed.
Firstly:
ubuntu@167-234-217-254:~/ddp-base-model-from-scratch$
git
diff
diff --git a/ddp_train.py b/ddp_train.py
index 5519353..932acc4 100644
--- a/ddp_train.py
+++ b/ddp_train.py
@@ -623,7 +623,7 @@ def main(run, datasets_dir_path, checkpoint, find_max_microbatch_size):
dist.init_process_group(backend, device_id=local_rank)
#
Set
all
of
the
random
seeds
-    seed = 42
+    seed = 23
random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
@@ -643,6 +643,12 @@ def main(run, datasets_dir_path, checkpoint, find_max_microbatch_size):
else:
scaler = None
+    # Set all of the random seeds again
+    seed = 23
+    random.seed(seed)
+    torch.manual_seed(seed)
+    torch.cuda.manual_seed_all(seed)
+
datasets_dir = Path(datasets_dir_path)
dataset_name = train_conf["dataset"]
dataset_dir = datasets_dir / dataset_name
Let that train:
Training complete in 12,249.079 seconds
Tokens seen: 3,260,252,160
Throughput: 266,163 tokens/second
Final train loss: 3.725
...getting
this model
.  Evals:
Every effort moves you from an easy and comfortable one and can be used up to 90% or even more and the result
...and...
Loss against our test dataset: 3.673943
Next, one with 67 as the weights initialisation seed:
ubuntu@141-148-168-241:~/ddp-base-model-from-scratch$
git
diff
diff --git a/ddp_train.py b/ddp_train.py
index 5519353..a64b423 100644
--- a/ddp_train.py
+++ b/ddp_train.py
@@ -623,7 +623,7 @@ def main(run, datasets_dir_path, checkpoint, find_max_microbatch_size):
dist.init_process_group(backend, device_id=local_rank)
#
Set
all
of
the
random
seeds
-    seed = 42
+    seed = 67
random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
@@ -643,6 +643,12 @@ def main(run, datasets_dir_path, checkpoint, find_max_microbatch_size):
else:
scaler = None
+    # Set all of the random seeds again
+    seed = 23
+    random.seed(seed)
+    torch.manual_seed(seed)
+    torch.cuda.manual_seed_all(seed)
+
datasets_dir = Path(datasets_dir_path)
dataset_name = train_conf["dataset"]
dataset_dir = datasets_dir / dataset_name
That trained:
Training complete in 12,255.283 seconds
Tokens seen: 3,260,252,160
Throughput: 266,028 tokens/second
Final train loss: 3.714
...getting
this model
, and :
Every effort moves you, in an attempt to protect it’s rights and the rights of the people in any respect
...and
Loss against our test dataset: 3.664345
OK, so here we have:
Mean: ~3.673215
Variance: ~0.000145
SD: ~0.012062
Compared to the SD we got when we varied just the initial seed, 0.0154919, it's not
too far off.  Using the 3-SD rule, we get a range of 3.637030 - 3.709400, and looking
at the table again, this time with the ones that we
don't
expect to have the same
weights highlighted:
Test set loss
Improvement vs baseline
8xa100m40-weight-tying
3.874
-0.182
8xa100m40-weight-decay-cerebras
3.867
-0.175
8xa100m40-baseline
3.692
-
8xa100m80-no-amp
3.679
0.013
8xa100m40-gradient-clipping
3.678
0.014
8xa100m40-qkv-bias
3.669
0.023
8xa100m40-weight-decay-gpt2
3.643
0.049
8xa100m40-remove-dropout
3.641
0.051
8xa100m40-schedule-learning-rate
3.602
0.09
...we can see that the QKV bias is well within that range (as are all of the interventions
apart from the two negative-effect ones and scheduling the learning rate).
Right, what does all of that tell us?
Conclusion
This post obviously isn't even trying to be statistically rigorous.  The number of
training runs I've done and the amount of data is way too small for that.  However,
training runs are expensive (Lambda have raised their prices again, so these cost
more than US$50 each!), so there's a limit to how much I can do.
But even with the limited amount of data, something seems pretty clear:
Varying the random seed at the start, prior to initialising weights, and not
constraining the starting point for the training runs, gave a mean of 3.672857,
with an SD of 0.0154919.
Keeping the same seed for model weights (so that they all started with the same
weights), and varying the seed for the training run, gave a mean of 3.684462,
with an SD of 0.008672.
Varying the seed for the model weights (so that they all started with different
weights), and keeping the training run seed pinned, gave a mean of 3.673215
and an SD of 0.012062.
"One of these things is not like the others".  Keeping the model weights stable
and only allowing variation in randomness across the training run itself meant that
almost all of the differences between training runs disappeared.  Could this be
a result of the small number of samples?  I guess conceivably it might, but it seems
vanishingly unlikely.
So I feel reasonably confident in saying that the bulk of the variation in results that
we can chalk up to random noise in these training runs comes from variations in the
model weights' initialisation.
Additionally, the first training run in this post -- the re-run of the baseline model
with no changes -- gave exactly the same numbers as the original baseline run.  So we
can be confident that all of the models with no changes to the weight initialisation
started with the same weights.  Of course, I could be wrong about which models really
did have the same weights, but given that they were running the same code with the same
seed, I'm pretty much sure.
That makes me fairly confident that the intervention runs that had the same initial
weights gave a real signal about whether or not the intervention in question actually
helped.  The only exception is gradient clipping, which fell within the three-SD
range for the same-weights tests -- and it's essentially free, adding just 100 seconds
to a three hour training run.
That's a really interesting result!  As I said earlier, given that dropout is making
us ignore a random 10% of activations during the training run, I would have thought
that changing
which
random 10% were being ignored would have a much larger effect.
And that's not even considering other sources of random noise in the training run.
I was less surprised that model weight initialisation was important, though.  It's pretty
obvious that your starting position in the loss landscape is going to affect where you
end up at the end of the training run.
Still, we now have a reasonable level of trust that our interventions gave a real signal,
so I think we have everything in place to see how they stack
together, and do a best-effort training run.  Can we approach the original GPT-2 small
weights' performance on our test set loss?
It should be fun to find out :-)
Here's a link to the next post in this series
.
