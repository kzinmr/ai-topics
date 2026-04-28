---
title: "Writing an LLM from scratch, part 32k -- Interventions: training a better model locally with gradient accumulation"
url: "https://www.gilesthomas.com/2026/04/llm-from-scratch-32k-interventions-training-our-best-model-locally-gradient-accumulation"
fetched_at: 2026-04-28T07:02:43.051943+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Writing an LLM from scratch, part 32k -- Interventions: training a better model locally with gradient accumulation

Source: https://www.gilesthomas.com/2026/04/llm-from-scratch-32k-interventions-training-our-best-model-locally-gradient-accumulation

Archives
Categories
Blogroll
I've been working on a GPT-2-small-style LLM based on
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
".
I've trained various versions of it in the cloud to
work out which interventions to the model and training code
had the best effects on the loss it gets on a specific test dataset, and now
I wanted to do a training run locally to match the best of those.
For that, I wanted to match the batch size I was using for the cloud training
runs.
When I first started learning this stuff, batching seemed like a performance
thing -- with highly parallel systems like GPUs, it generally turned out that you could run
a batch of (say) two inputs through a model in less than twice the time you could run one, so it made
sense to batch them up.
For inference, that is exactly the advantage you get, but when training, it's become increasingly
clear to me that you can also get an improvement in the quality of the model
from batching.  The best intuitive model I have is that if you run inputs
through one-by-one, adjusting parameters after each, then it's easy for the model to
"overcorrect" each time.  With batches, you get an average set of gradients across
all of the items -- which smooths things out and stabilises the training.
Of course, it's possible to overdo it.   As an extreme example, imagine that you
were somehow able to fit your whole training set into one batch -- then you could
train by running that single batch through, doing a single backward pass, and then adjusting the parameters
once.  It's pretty clear that that would not work very well -- just one single update
of the initially-random parameters.
When training on my local machine, I could fit a batch of six sequences into my RTX 3090.  I'd found that
when I moved to cloud machines, it had a very positive effect on the loss I got
out of the models when I tested them.  From
a quick-and-dirty bit of curve-fitting
,
I estimated that the optimal batch size for this model, with that training run,
was somewhere around 97.  Conveniently, that was close to the maximum I could fit
onto an 8x A100 40 GiB/GPU machine, so I used a batch size of 96 to test the different
interventions I was trying.
And when I finally
put all of the interventions that helped with training together
,
I found (somewhat to my surprise) that their combined effect -- an improvement in
loss of 0.113765 -- was less than half of the loss improvement of 0.252474 that I had got from
increasing the batch size.
What that all made clear was that if I wanted to do a local training run that matched
the quality of the cloud-trained model, I'd need to not only add on the interventions
that I'd been testing in detail, but I'd need to match the cloud batch size.  And for
that, I needed to learn about gradient accumulation.
Gradient accumulation basics
Gradient accumulation is pretty much what it sounds like; instead of the normal technique
of doing a forward pass, working out the loss, getting gradients with a backward pass,
and then applying them by stepping the optimiser, you do multiple forward-backward phases,
letting the gradients accumulate, and then do one optimiser step after that.
When you do that, you're getting the training stabilisation benefits of a larger batch
size, even though you're not getting the performance boost.  Sounds simple enough,
and it is, in theory, but implementation got a little more complicated.
Let's work through it step-by-step.
To start with, imagine you have a really simple training loop:
for
inputs
,
targets
in
batched_dataset
:
# Other stuff
logits
=
model
(
inputs
)
loss
=
calculate_loss
(
logits
,
targets
)
loss
.
backward
()
# Other stuff
optimizer
.
step
()
optimizer
.
zero_grad
()
# Other stuff
Adding gradient accumulation to that is really simple!
Let's assume that
batched_dataset
has a length divisible by
gradient_accumulation_steps
,
the number of steps we want to run through before we step the optimiser.  As a first (not quite correct)
cut, you could just do this:
for
step
,
(
inputs
,
targets
)
in
enumerate
(
batched_dataset
):
# Other stuff
logits
=
model
(
inputs
)
loss
=
calculate_loss
(
logits
,
targets
)
loss
.
backward
()
# Other stuff
if
(
step
+
1
)
%
gradient_accumulation_steps
==
0
or
step
==
len
(
batched_dataset
)
-
1
:
optimizer
.
step
()
optimizer
.
zero_grad
()
# Other stuff
You can see that we're just stepping the optimiser every
gradient_accumulation_steps
steps.
An alternative way to do it would be with an inner loop:
dataset_ix
=
0
while
dataset_ix
<
len
(
batched_dataset
):
# Other stuff
for
ii
in
range
(
gradient_accumulation_steps
):
if
dataset_ix
>=
len
(
batched_dataset
):
break
inputs
,
targets
=
batched_dataset
[
dataset_ix
]
logits
=
model
(
inputs
)
loss
=
calculate_loss
(
logits
,
targets
)
loss
.
backward
()
dataset_ix
+=
1
# Other stuff
optimizer
.
step
()
optimizer
.
zero_grad
()
# Other stuff
Which of those is better would depend on the details of the training loop -- in general,
if you wanted the "other stuff" to be done once per training batch, then you'd want to
use the first option, whereas if you wanted it to be done once per optimiser step,
the second would be easier.  As you'll see in a bit, I went for the second one for my
code.
However, there's one small correction that we need to do to make either of these properly.  Remember
that when you calculate loss across a batch -- for example, cross entropy loss like this:
torch
.
nn
.
functional
.
cross_entropy
(
logits
.
flatten
(
0
,
1
),
targets
.
flatten
())
...you're getting the
average
loss across the batch, so when you do the backward
pass, you're getting the average gradients.  By contrast, in the code above, we're
doing a backward pass on the complete loss at each step, so the gradients that are
being generated in each backward pass are being added to each other -- you wind up
with the sum of all of them rather than the average.  So the gradients that the optimizer
applied would be
gradient_accumulation_steps
times larger than they should be --
it would be as if we'd multiplied the learning rate by that number!
But that's easy enough to fix.  The average gradients over a number of steps are the sum divided by the
number of steps, and we can do that division ahead of time just by scaling the loss down.
Adding that into the first example above:
for
step
,
(
inputs
,
targets
)
in
enumerate
(
batched_dataset
):
logits
=
model
(
inputs
)
loss
=
calculate_loss
(
logits
,
targets
)
(
loss
/
gradient_accumulation_steps
)
.
backward
()
if
(
step
+
1
)
%
gradient_accumulation_steps
==
0
or
step
==
len
(
batched_dataset
)
-
1
:
optimizer
.
step
()
optimizer
.
zero_grad
()
And that's basically it; with those changes, the original basic training loop
becomes one that uses gradient accumulation.  The effective batch size is whatever
the real batch size is, times the number of gradient accumulation steps.
Gradient accumulation in practice
However, the real training loop that I'm using for these experiments is a bit more
complicated than that simple example.  There's checkpointing, AMP, and -- most importantly
-- it can handle multi-GPU training using DistributedDataParallel.  That made things
a little bit more complicated.
The first thing was to look into the way I was selecting the data to train on.  My dataset was already
in batches, but we had to split those batches up between GPUs.  The solution in the code
was to work out how many global steps there were -- each global step being one batch
going through each GPU on the machine -- like this:
total_global_steps
=
len
(
train_ds
)
//
world_size
world_size
, if you remember from
the DDP post
,
is the number of processes running in a multi-GPU training run -- one per GPU.
Next, in the training loop, I iterated over the global steps:
progress_bar
=
tqdm
(
range
(
start_global_step
,
total_global_steps
),
disable
=
(
rank
!=
0
)
)
for
global_step
in
progress_bar
:
# Get the data
# Forward and backward pass
# Step the optimiser.
...for each one, getting the appropriate batch out for the specific GPU that was
running the code:
inputs
,
targets
=
train_ds
[
global_step
*
world_size
+
rank
]
rank
is a zero-indexed number, unique to each of the per-GPU processes.  So this
basically split
train_ds
into chunks of length
world_size
, and then each GPU
was fed the batch at its
rank
's offset into the chunk.
I wanted to keep things shaped such that when I was running with gradient accumulation
locally, it would be similar to a cloud run with per-GPU batching.  Specifically: when
I was training in the cloud, I had eight GPUs with a per-GPU microbatch size of 12, giving
a total batch size of 96.  Locally, I could fit a batch size of six on my GPU, so I needed
to do gradient accumulation over 96 / 6 = 16 steps.
To keep things as similar as possible, I decided that I wanted the concept of a
"global step" to match between the runs.  In other words, it would expand slightly,
from meaning "one batch per GPU" to being "one optimiser step per GPU".
So, each time through that
global_step
loop, we'd do multiple forward-backward
passes, and then one optimiser step.  That would mean that the best way to do things
would be with something much more like the second of the two bits of sample code
above -- the one with the inner loop rather than the modulus.
Maybe that's easier to show in code:
total_global_steps
=
(
len
(
train_ds
)
//
world_size
)
//
gradient_accumulation_steps
...
for
global_step
in
progress_bar
:
...
for
accumulation_step
in
range
(
gradient_accumulation_steps
):
# Forward and backward passes
...
# Step the optimiser
That required a change to the data lookup; I decided that
train_ds
would be split
into chunks of size
gradient_accumulation_steps * world_size
, and then each of those
would be split into chunks of size
world_size
, so the code to get the appropriate
batch for a given run through the loop became this:
inputs
,
targets
=
train_ds
[((
global_step
*
gradient_accumulation_steps
)
+
accumulation_step
)
*
world_size
+
rank
]
That required a corresponding change in
load_dataset
to make sure that
train_ds
was
divisible by both the world size, the per-GPU batch ("microbatch") size, and the number of gradient accumulation steps, but that was easy:
one_full_batch_tokens
=
world_size
*
microbatch_size
*
seq_length
...became this:
one_full_batch_tokens
=
world_size
*
microbatch_size
*
gradient_accumulation_steps
*
seq_length
That was enough to get the gradient accumulation happening!  Next, I needed to change
the backward pass code to scale down the loss so that we got averaged rather than summed
gradients.  Because we might be using AMP with a scaler, the code wasn't just a simple
loss.backward
:
if
scaler
is
not
None
:
scaler
.
scale
(
train_loss
)
.
backward
()
else
:
train_loss
.
backward
()
...but the change was obvious enough:
if
scaler
is
not
None
:
scaler
.
scale
(
train_loss
/
gradient_accumulation_steps
)
.
backward
()
else
:
(
train_loss
/
gradient_accumulation_steps
)
.
backward
()
All of those changes put together, plus a bit of shuffling around of code,
were enough to get a correct gradient accumulation
training loop!  But there was one small tweak I needed to add.
When you're using DDP, gradients need to be synchronised between the different
per-GPU processes.  As a reminder, what happens is:
Each process does a forward pass.
Each process does a backward pass.
When they have the gradients, they essentially share them so that each process has
an average of the gradients from all of those backward passes.
Then they all step their optimisers to apply the average gradients to each process's
copy of the model.
Now, with my first cut of the gradient accumulation code above, what would have happened is this:
For each gradient accumulation step:
Each process does a forward pass.
Each process does a backward pass.
The average is worked out
They all step their optimisers based on the most recent average
That would be correct, but not very efficient.  We're sending out gradients and
averaging on every accumulation step.  But because each of our per-GPU processes
is keeping its own "local" average (by accumulating the scaled-down gradients), we only
really need to send those local averages out and get a global average once, just before we step
the optimiser.  If we do that, we can save quite a lot of work.
The trick to avoid that was to use the method
no_sync
on the
DistributedDataParallel
class
that our own model is wrapped in.  What we wanted to do was suppress the gradient
synchronisation for each of the accumulation steps apart from the last one.
It was easy to work out whether we were on the last gradient accumulation step:
is_last
=
accumulation_step
==
gradient_accumulation_steps
-
1
Now, what we needed to do was to wrap this:
if
scaler
is
not
None
:
scaler
.
scale
(
train_loss
/
gradient_accumulation_steps
)
.
backward
()
else
:
(
train_loss
/
gradient_accumulation_steps
)
.
backward
()
...in
model.no_sync
, but
only if
is_last
was false.
Conditional
with
statements can be a little fiddly, but Python has a "do-nothing"
nullcontext
context manager in
contextlib
-- that is,
with
nullcontext
():
do_something
()
...is identical to just:
So we can combine that with the ternary operator like this:
with
model
.
no_sync
()
if
not
is_last
else
nullcontext
():
if
scaler
is
not
None
:
scaler
.
scale
(
train_loss
/
gradient_accumulation_steps
)
.
backward
()
else
:
(
train_loss
/
gradient_accumulation_steps
)
.
backward
()
...which does exactly what we want .
With that change, I had something I was happy with; you can
see the diff here
.
So now it was time to do a training run!
The new local baseline
I'd originally been planning to jump right in and do a training run based on my
last cloud run
,
with all of the interventions I'd decided were worth using, but locally with
gradient accumulation.
However, I decided that it would be interesting to try doing a new "baseline" train
first.  I'd done my local training runs, and then established a baseline version in
the cloud by taking exactly the same configuration and doing the training run on
an 8x A100 40 GiB with an overall batch size of 96.  So I could repeat that locally
with gradient accumulation, and that would show two things (or perhaps, the same
thing but in different lights):
Whether the increased effective batch size had as positive an effect on the loss
as the increased real batch size did when I did my cloud runs.
Whether the locally-trained gradient accumulation model was similar to the cloud-trained
big-batch model in terms of its loss.
That would help confirm my understanding that it was the
increased batch size that helped in the cloud, and not, say, some architectural difference -- and would also act as a good test
of the gradient accumulation code.
Here's
the training run config
.
I kicked it off:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
torchrun
--nproc_per_node
=
1
ddp_train.py
1xrtx3090-baseline
datasets/
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
810
.65it/s
]
Starting
rank
0
training
at
global
step
0
0
%
|
|
0
/33165
[
00
:04<?,
?it/s,
loss
=
10
.991,
tps
=
20
,451
]
Checkpoint

Continuing
training
0
%
|
|
23
/33165
[
01
:50<
43
:29:50,
4
.72s/it,
loss
=
7
.625,
tps
=
20
,549
]
That looked like the right number of global steps; it matched the numbers I saw when
training in the cloud.  And 44 hours for the training run seemed correct: my original
local runs took 48, but with them I was spending quite a lot of time on validation,
which this code didn't do.
Just less than two days later:
Training complete in 155,402.289 seconds
Tokens seen: 3,260,252,160
Throughput: 20,979 tokens/second
Final train loss: 3.738
That all looked good.  The loss chart looked like this:
For comparison, here's the one from the cloud training run with the same config
(but using larger batches rather than gradient accumulation):
You can see that they're similar, but not identical.  That's pretty much what you'd expect!
The two training runs were on different architectures -- RTX 3090 vs A100 -- and so there
will probably be differences in the CUDA kernels, and also PyTorch's AMP (which uses
16-bit instead of 32-bit in cases where it makes sense) might make different decisions.
I think that if we'd run it on a machine with one A100, then the results of using gradient accumulation
would be even closer (perhaps even identical) to a larger batch size, especially if we
were training without AMP.
I
uploaded the model to Hugging Face
and it
was time for the evals.  The smoke test first:
Every effort moves you to a more realistic approach and is always welcome, especially for a younger child!
I’
As usual, reasonably coherent.  But the important one was the loss on the test set:
Loss against our test dataset: 3.683835
That's solid!  The cloud-trained baseline model got 3.691526, so this local one was
actually very slightly better, by 0.007691.  But that's very close indeed, which is
what we wanted to see :-)
It was time to see what effect adding on the interventions would have.
The local run with the interventions
As a reminder, here are the changes I made to the config for this run:
Gradient clipping at 3.5
Learning rate changed from 0.0004 to 0.0014, with a warmup over 5% of the run then a cosine decay to 0.00014.
Weight decay changed from 0.1 to 0.01
Dropout removed
It did not include QKV bias.
Here's the config
.
I kicked it off, and:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
torchrun
--nproc_per_node
=
1
ddp_train.py
1xrtx3090-stacked-interventions
datasets
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
749
.32it/s
]
Starting
rank
0
training
at
global
step
0
0
%
|
|
0
/33165
[
00
:04<?,
?it/s,
loss
=
10
.994,
tps
=
21
,589
]
Checkpoint

Continuing
training
0
%
|
|
19
/33165
[
01
:25<
40
:52:06,
4
.44s/it,
loss
=
10
.318,
tps
=
21
,867
]
It looked like it was going to take 40 hours; that matched what happened in the cloud
runs, as removing dropout speeds things up quite a lot.
Just less than two days later:
Training complete in 146,299.816 seconds
Tokens seen: 3,260,252,160
Throughput: 22,285 tokens/second
Final train loss: 3.519
The loss chart over the training run looked like this:
That's very smooth, with no loss spikes.  For comparison, here's the chart when we did the same training run in the cloud;
you can see that it was a bit choppier than the local one.
The gradient norm chart was also interesting:
If you compare it to the one from the cloud training run below, you can see that
the local one was actually noisier -- the cloud run has a few gradient spikes near
the start but calms down from around global step 6,000 or so, whereas the local one is
spiky up to about 3,000, then calm, but has a massive spike at around 10,000.
The learning rate we don't need to compare, but it was worth sanity checking to make sure
we really did train the right way:
So that all looked good.  The training run did have some differences to the cloud one,
but (as with the previous baseline train) it looked similar enough.  Architectural
differences between the A100s in the cloud and the local RTX 3090 seemed like a plausible
cause.
Evals
I
uploaded the model to Hugging Face
,
and it was time to run the evals.  The smoke test first:
Every effort moves you to give your customers the opportunity you give them in the event of a failure.<|endoftext|>A couple friends
Reasonably coherent -- and I think that's the first time I've seen an
<|endoftext|>
token
in a smoke test output!  But the important one is, as ever, the loss, and:
Loss against our test dataset: 3.538161
Let's add both this one and the local baseline to the results table for all interventions:
That's really weird!  The local run with the interventions,
1xrtx3090-stacked-interventions
,
is 0.039600 points better than the cloud version of the
same training run,
8xa100m40-stacked-interventions-1
.  That's nice, in that lower loss is always better, but it's also
rather confusing -- that's a bigger loss improvement than some of the interventions.
In theory, all that we changed between the cloud version of this training run,
and the local one
was the architecture.  I was expecting that to have an effect, but thought that
it would be small -- as, indeed, it was with the baseline trains
8xa100m40-baseline
and
1xrtx3090-baseline
, where you can see the loss difference was just 0.007691 --
about five times smaller.
Now, when I was looking into
the effects of noise on training loss
,
I found that changing the random seed that was used to initialise the weights (but starting
the training run itself at the same random seed) had
a much bigger effect on the resulting model quality than keeping the weights identical
but varying the seed at the start of the post-initialisation phase of the training run.
The standard deviation of the varied-weights, same-train models was about double the SD of the
same-weights, varied-train.
That was interesting, though not directly comparable -- those tests were done with
the same training run, but the architecture held constant -- a 8x A100 40 GiB machine
for each test.
However, it felt like it would be a good idea to at least see whether we started with
the same weights locally and when training in the cloud.  My suspicion was that we probably
would; the weight initialisation uses deterministic non-GPU code, so with the same seed
we'd expect the same weights regardless of the computer.  The similarity of the loss
results for the local and cloud baseline training runs also seemed to point in that
direction.
But it was worth testing.  I created a throwaway branch of the training code, which
-- after creating the model --
just dumped the model weights to a file, then exited.
I ran it locally using
the
1xrtx3090-stacked-interventions
config, and
then I fired up yet another 8x A100 40 GiB machine on Lambda, ran the same code there,
this time with the
8xa100m40-stacked-interventions-1
config, and
then
scp
ed down the weights.
giles@perry:~/Dev/ddp-base-model-from-scratch
(
dump-weights
)
$
diff
cloud-init-weights.safetensors
local-init-weights.safetensors
giles@perry:~/Dev/ddp-base-model-from-scratch
(
dump-weights
)
$
Identical.  That was reassuring!
I considered doing more analysis on this; for example, in my investigations into noise,
I found that keeping the same weights but altering the random seed for the rest of the
training run, I got results with a standard deviation of 0.008672 -- more than four times
smaller than the difference between the local and cloud trains with the interventions.
Might that be a number I could use for some kind of comparison?
However, I decided that it's not really comparable.  That number was from varying the random seed, but
keeping the same architecture.  There's not really any solid reason to believe that
keeping the seed constant but changing the architecture would cause the same kind of differences.
They might be more similar, they might be less.
I think that all we can really say here is that the change of machine changed some
aspects of the training dynamics in a way that happened to get us a lower loss.  I
can easily imagine that if I'd done something slightly different -- used a local
RTX 4090, for example -- it could equally well have gone in the other direction.
And at least it's reassuring that the improvement was smaller than the
interventions I was most convinced by; the only smaller ones were full-fat float32, gradient clipping, and
QKV bias -- ones that I'd already decided might have only been beneficial due to noise.
Most importantly, it was orders of magnitude smaller than the 0.252474 improvement
I originally saw when I moved from local training to larger-batch cloud training.
Conclusion
So, I think that that brings me to the end of this set of training experiments.
We started with a locally-trained model that got a loss of 3.943522 on our test set,
compared to the original GPT-2 small model, which got 3.499677 .
I've tried a bunch of interventions to try to get my model closer, and finally I've
managed to get almost all of the way there, to 3.538161.  That's really pleasing!
I think that there are two things to do before I can fully wrap up this "interventions"
mini-series, and get back to the main-line LLM from scratch stuff.
Firstly, I should
revisit the instruction fine-tuning tests, which I put on hold while doing these
training runs.  That would give us some indication as to whether the loss improvement was just a technical improvement
that made a number go down, or whether it actually improved the usefulness of the model.
Secondly, I think I really need to write a wrap-up.  I've been working on this stuff
on and off since December, and I think a summary of what I did would be quite nice!
I'll post soon; don't touch that dial :-)
Here's a link to the next post in this series
.
