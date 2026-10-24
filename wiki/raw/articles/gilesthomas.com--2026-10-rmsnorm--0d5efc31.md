---
title: "RMSNorm :: Giles' blog"
url: "https://www.gilesthomas.com/2026/10/rmsnorm"
fetched_at: 2026-10-24T10:00:50.853333+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# RMSNorm :: Giles' blog

Source: https://www.gilesthomas.com/2026/10/rmsnorm

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
Normalisation is an essential part of LLMs.  In the GPT-2 code, we use
LayerNorm
in a bunch of different
places -- in each Transformer block, we do it just before we feed our incoming
context vectors into the multi-head attention module, and then again before we
feed the result through the FFN:
...and we also do one more round just before we project our context vectors into
vocab space via the output head.
We do that to make the model more trainable; it helps to prevent vanishing or exploding
gradients, by constraining the vectors going into our attention, feed-forward and output head
modules so that they have a reasonably stable set of statistical properties.
And when (
as part of my black-box reimplementation of GPT-2 in JAX
)
I tried training an almost-complete model without LayerNorm, training completely failed
after about 100 steps -- the loss went up to the kind of level that I'd expect from
an uninitialised model, and stayed there despite another 700 or so training steps.
(Later on in this post I'll show results from a similar run.)
So, normalisation is important.  But it doesn't have to be LayerNorm specifically --
if you look at the currently-popular open models, a lot of them use something
called RMSNorm instead, and I wanted to look into why that might be.
In this post I'll go through the differences between LayerNorm and RMSNorm, and show
the results of training a few GPT-2 small style models using each.
The principle
RMSNorm was introduced in
a 2019 paper by Biao Zhang and Rico Sennrich
,
which is a surprisingly easy read.  They note that
most people at the time felt that a critical part of LayerNorm -- which they are
explicitly comparing their new system to -- is that it does mean normalisation.  But
they were less sure that it was the important bit, and felt that scale normalisation was
its real benefit.
Let's dig into what that means.  Firstly, a refresher on LayerNorm.
LayerNorm
Our normalisation layer in the diagram above is being fed with a bunch of context
vectors -- one for each token in each sequence in our batch.  LayerNorm deals with each
of them separately .  For each one, it performs two steps:
Normalises the context vector so that its mean is zero, and its variance is one.
Scales and shifts (aka biases) the resulting normalised vector by trainable amounts.
Let's work through that.  We'll go through the normalisation first; say you start with a context vector of
(
2
4
6
)
Its mean is
(
2
+
4
+
6
)
/
3
=
4
.  If you subtract that from each element, you get
(
−
2
0
2
)
...which has a mean of
(
−
2
+
0
+
2
)
/
3
=
0
.  So that sorts out the mean part of it.
I'll call this "re-centring" below -- hopefully it's obvious why!
To make the variance one, we need to divide each element by the standard deviation (SD)
of the whole vector (see
my previous LayerNorm post
for details as to why).
The SD is the square root of the variance, and the variance is
calculated by squaring each item's difference from the mean,
adding them all together, and then dividing it by the number of elements .
Now, there's a neat trick that you can do here.  As we have already set our mean to zero
in the previous step, each number in our vector is already exactly equal to its difference
from the mean.  So we can just square them element-wise, and take the average of that,
which will give us our variance:
(
−
2
)
2
+
0
2
+
2
2
3
=
8
3
=
2
2
3
Again, SD is the square root of the variance, so here it's
2
2
3
≈
1.63
.
Dividing our already-recentred numbers by that gives us a normalised context
vector of
(
−
2
/
1.63
.
.
.
0
/
1.63
.
.
.
2
/
1.63
.
.
.
)
=
(
−
1.22
.
.
.
0
1.22
.
.
.
)
We can sanity-check that the result has a variance of 1 -- remember it's just the
average of the elements squared:
(
−
1.22
.
.
.
)
2
+
0
2
+
1.22
.
.
.
2
3
=
3
3
=
1
So, that's the normalisation part of LayerNorm.  We've recentred our context vector on its mean, and made
it have a variance of one.
Now that we've normalised our context vector, we need to scale and shift it.  Intuitively
that feels a bit like undoing the careful work we've done to fix the mean to zero and
the variance to one.  But it's worth remembering that what we're trying to do with our
normalisation is make the results have stable statistical properties; what the ideal specific
properties might be is something that the network should be learning.  So the first phase
gets everything into a well-known state, then the shift/scale goes from there to the
shape that the network learns that it actually needs.
Both of these operations are done with trainable vectors of the same size as the
context vectors -- that is, the scale vector is
d
emb
long, and so is the
shift vector.  They're applied element-wise.  So let's say our scale vector was
(
3
2
1
)
After normalisation, our original context vector was
(
−
1.22
.
.
.
0
1.22
.
.
.
)
So we multiply that element-wise by the scale vector, and we get:
(
−
1.22
.
.
.
×
3
0
×
2
1.22
.
.
.
×
1
)
=
(
−
3.66
.
.
.
0
1.22
.
.
.
)
...and that's the scaling done.  Similarly, if our shift vector was
(
10
11
12
)
...then applying it to the scaled vector would be:
(
−
3.66
.
.
.
+
10
0
+
11
1.22
.
.
.
+
12
)
=
(
6.34
.
.
.
11
13.22
.
.
.
)
...and with that, we've completed our LayerNorm.
But it took quite a lot of calculations; let's list them out:
Working out the mean: for a context vector of length
d
emb
, we have
d
emb
−
1
additions,
then one division.
Recentring on the mean:
d
emb
subtractions.
Working out the variance: we can use our recentred vector for the differences, so
that's done, but we need to get the squares of all of the numbers, which is
d
emb
multiplications,
add them together using
d
emb
−
1
additions, and then do one division.
Variance to standard deviation: one square root.
Dividing it all by the SD:
d
emb
divisions.
Scaling by the scale vector:
d
emb
multiplications
Shifting by the shift vector:
d
emb
additions
So in total we have, per context vector in our batch:
Additions/subtractions:
d
emb
−
1
+
d
emb
+
d
emb
−
1
+
d
emb
=
4
d
emb
−
2
Divisions:
1
+
1
+
d
emb
=
2
+
d
emb
Multiplications:
d
emb
+
d
emb
=
2
d
emb
Square roots:
1
Let's look at RMSNorm next to see how it compares.
RMSNorm
The idea behind RMSNorm is to try to get away with doing fewer calculations.  In particular,
we skip working out the mean -- we don't even try to re-centre our context vectors.
Instead, we just scale them down to the same length.  To do that, we work out
an average length for each vector -- specifically, the Root Mean Square (RMS, of course) -- and then divide each number
in it by that.  That done, we do the same scale trick that we did with LayerNorm, but
not the shift -- more about that later.
Let's work through that in numbers again; we can start with the same context vector:
(
2
4
6
)
The mean square of that is, as you might expect, the mean of the squares of all of the
numbers in it:
MS
=
2
2
+
4
2
+
6
2
3
=
4
+
16
+
36
3
=
56
3
=
18
2
3
The
root
mean square is the square root of that, which is about 4.32, so we divide
through by that:
(
2
/
4.32
.
.
.
4
/
4.32
.
.
.
6
/
4.32
.
.
.
)
=
(
0.46
.
.
.
0.92
.
.
.
1.38
.
.
.
)
You might intuitively expect the RMS of that resulting vector to be one, and
of course it is; the mean square is:
0.46
.
.
.
2
+
0.92
.
.
.
2
+
1.38
.
.
.
2
3
=
3
3
=
1
...and again, we square root that to get RMS which is again 1.
So you can see that by dividing by the RMS, we're going to re-scale all of our context
vectors so that they have a new RMS of one.  But their means can be all over the place
-- we've not tried to do anything to fix them.
That's our abbreviated normalisation; once that's done, just like with LayerNorm,
we apply an elementwise scaling operation by a trainable
scale vector -- but we don't shift it.  Interestingly,
in the original paper, they give equations both with and without the shift -- equation (4),
in which they first present it, doesn't have a shift, but equation (5), which they call a general form, does.  It's not clear to me which one they actually used
in their tests, but it's worth noting (and thanks to GPT-6 Astra for digging this up for me)
that the
code on GitHub
posted
by one of the authors has an optional
bias
that is switched off by default.
Anyway, the fashion these days appears to be to use RMSNorm without a shift, and to me that makes
intuitive sense; we've normalised the scale of the values in our context vector via the
division by the RMS, so "fixing" that to get desirable statistical properties makes sense.
But we didn't normalise the means, so the numbers coming out do not have a stable baseline
for us to adjust with a shift.  We could add one anyway of course, but there's no intuitive
need to add a "new mean" back in to replace an old one that was never removed in the first place.  It's a bit fuzzy, perhaps,
but it makes some kind of sense.
So let's stick with the popular version without shift: how many calculations do we save by doing RMSNorm?
Working out the squares of all of the numbers:
d
emb
multiplications.
Averaging them to get the mean square:
d
emb
−
1
additions, then one division.
Getting the RMS from that: one square root
Dividing all of the numbers by the RMS:
d
emb
divisions
Scaling by the scale vector:
d
emb
multiplications
So that gives us a total of:
Additions/subtractions:
d
emb
−
1
Divisions:
1
+
d
emb
Multiplications:
d
emb
+
d
emb
=
2
d
emb
Square roots:
1
In terms of differences with LayerNorm we have:
Additions/subtractions:
(
4
d
emb
−
2
)
−
(
d
emb
−
1
)
=
3
d
emb
−
1
fewer
Divisions:
(
2
+
d
emb
)
−
(
1
+
d
emb
)
=
1
fewer.
Multiplications:
2
d
emb
−
2
d
emb
=
0
difference
Square roots:
1
−
1
=
0
difference.
So, it's certainly cheaper -- significantly fewer addition/subtraction operations.
The question is, is that saving in training time worth it?
In the paper, they train various models of various sorts (including an early Transformer model)
and come to the conclusion that it is; they got similar, or in some cases better, loss with
RMSNorm than with their LayerNorm training runs.  And, of course, the fact that it's widely
used in current open LLMs suggests the same.
Would it work well for my own models?  And what kind of performance improvement
would I get, if any?
It was time to write some code and train some models.
The code
The PyTorch code for RMSNorm was pretty trivial:
class
RMSNorm
(
nn
.
Module
):
def
__init__
(
self
,
emb_dim
):
super
()
.
__init__
()
self
.
emb_dim
=
emb_dim
self
.
scale
=
nn
.
Parameter
(
torch
.
ones
(
self
.
emb_dim
))
self
.
eps
=
RMSNORM_EPS
def
forward
(
self
,
xs
):
squares
=
xs
**
2
mean_squares
=
squares
.
mean
(
dim
=-
1
,
keepdim
=
True
)
rms
=
torch
.
sqrt
(
self
.
eps
+
mean_squares
)
return
(
xs
/
rms
)
*
self
.
scale
Our incoming batch of context vectors is shaped
b
×
n
×
d
emb
,
where
b
is the batch size and
n
is the sequence length.  In the
forward
method, just as in the worked example
above, we get the square of everything, then work out the mean across that
last
d
emb
dimension so that we have per-context-vector means, keeping the dimensions
stable with that
keepdim=True
so that we wind up with a
b
×
n
×
1
result
rather than a
b
×
n
one.
We then take the square root to work out the RMS, but we add on a tiny
ϵ
first so that it will
never be zero (which would cause a divide-by-zero in the next step).  And finally
we divide the incoming numbers by that adjusted RMS, multiply by our trainable scaling
vector, and we're done.
One thing that is worth noting; to me it would be a bit more natural to add on
the
ϵ
in the division, like this:
rms
=
torch
.
sqrt
(
mean_squares
)
return
(
xs
/
(
rms
+
self
.
eps
))
*
self
.
scale
However, I had the LayerNorm code from the book in front of me as I wrote it, and noticed
that it adds on its own
ϵ
before the square root, like this:
def
forward
(
self
,
x
):
mean
=
x
.
mean
(
dim
=-
1
,
keepdim
=
True
)
var
=
x
.
var
(
dim
=-
1
,
keepdim
=
True
,
unbiased
=
False
)
norm_x
=
(
x
-
mean
)
/
torch
.
sqrt
(
var
+
self
.
eps
)
return
self
.
scale
*
norm_x
+
self
.
shift
...so I decided to keep it consistent.  When I later looked at the docs for PyTorch's
built-in RMSNorm class, I saw that it did the same thing as mine, so it seemed to be the
"right" way to do it.  The two alternatives have very different behaviour when
numbers get close to zero, so it was important to be consistent.
And having mentioned PyTorch's built-in RMSNorm, let's dig into that a bit.
The built-in PyTorch classes
A little while ago, I noticed that by
using PyTorch's built-in GELU module
rather than the hand-rolled one
from the code in
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
",
I got a significant speedup when training on my local machine -- from 21,000 tokens/second
to 25,000.
PyTorch also has its own built-in
LayerNorm
and
RMSNorm
modules.
Now, while I felt that the book could actually have used the PyTorch GELU, it 100%
made sense that it showed you the code for LayerNorm -- after all, "Build a Large
Language Model (by Bolting Together Random Bits of PyTorch)" doesn't have the same
ring to it.  And likewise in this set of experiments I wanted to try running my own
RMSNorm.
But given that the point of RMSNorm is meant to be speeding up training, it felt
like it would be worth seeing how that speedup might compare to using built-in modules
rather than hand-rolling our own.  After all, the built-in modules can use fused
kernels, and that can be a huge advantage.  Rather than doing each of the separate steps in the Python code above
by dropping down into CUDA, doing the calculations, and then returning to Python
to find out what the next step is, the whole thing can be coded in a single CUDA routine
that can be run in one go.  Even better, that routine can be optimised as a whole --
stuff that's used frequently can be kept in registers,
things can be laid out so that the cache is used efficiently, and so on -- whereas with
the Python implementation, everything would need to be in the main VRAM at the end of each step.
Definitely a win.  My guess is that this is a large part of why the built-in
GELU is faster, so I expected serious speedups from using PyTorch's normalisation classes.
That meant that I wanted my code to be able to switch easily between different kinds
of normalisation.
Normalisation-switching code
As I mentioned at the start of this post, the original GPT-2 code used LayerNorm
in three places:
Twice in each Transformers block:
before the MHA and
before the FFN.
At the end, just before the output head.
The code for the Transformers bit looked like this:
class
TransformersBlock
(
nn
.
Module
):
def
__init__
(
self
,
cfg
):
super
()
.
__init__
()
...
self
.
norm1
=
LayerNorm
(
cfg
[
"emb_dim"
])
self
.
norm2
=
LayerNorm
(
cfg
[
"emb_dim"
])
...
def
forward
(
self
,
inputs
):
...
shortcut
=
x
x
=
self
.
norm1
(
x
)
x
=
self
.
att
(
x
)
...
shortcut
=
x
x
=
self
.
norm2
(
x
)
x
,
this_block_moe_routing_info
=
self
.
ff
(
x
)
...
...and the output head bit like this:
class
GPTModel
(
nn
.
Module
):
def
__init__
(
self
,
cfg
):
super
()
.
__init__
()
...
self
.
final_norm
=
LayerNorm
(
cfg
[
"emb_dim"
])
...
def
forward
(
self
,
in_idx
):
...
x
,
moe_routing_info
=
self
.
trf_blocks
((
x
,
None
))
x
=
self
.
final_norm
(
x
)
logits
=
self
.
out_head
(
x
)
...
That code is essentially the same as Raschka's from the book, with a couple of
(inactive in this post's experiments)
tweaks to support mixture-of-experts models
.
I wanted a config flag -- in that
cfg
dictionary -- to control the kind of normalisation
we used.  It seemed pretty clear that so long as the various classes we wanted to use in place
of the existing
LayerNorm
implementation were compatible with it, we could just swap
them in.  So I replaced the existing lines that created
LayerNorms
with:
self
.
norm1
=
make_norm
(
cfg
)
self
.
norm2
=
make_norm
(
cfg
)
...
self
.
final_norm
=
make_norm
(
cfg
)
...and defined
make_norm
like this:
def
make_norm
(
cfg
):
norm_type
=
cfg
.
get
(
"norm_type"
,
"handrolled_layernorm"
)
if
norm_type
==
"handrolled_layernorm"
:
return
LayerNorm
(
cfg
[
"emb_dim"
])
elif
norm_type
==
"pytorch_layernorm"
:
return
nn
.
LayerNorm
(
normalized_shape
=
cfg
[
"emb_dim"
],
eps
=
LAYERNORM_EPS
)
elif
norm_type
==
"handrolled_rmsnorm"
:
return
RMSNorm
(
cfg
[
"emb_dim"
])
elif
norm_type
==
"pytorch_rmsnorm"
:
return
nn
.
RMSNorm
(
normalized_shape
=
cfg
[
"emb_dim"
],
eps
=
RMSNORM_EPS
,
elementwise_affine
=
True
)
elif
norm_type
==
"no_norm"
:
return
nn
.
Identity
()
else
:
raise
Exception
(
f
"Unknown <!--CODE_BLOCK_15744--> of
{
norm_type
!r}
"
)
That gave us the option for the original "hand-rolled" LayerNorm from Raschka, my own RMSNorm
implementation, their respective PyTorch implementations, and a no-normalisation
option that I felt would be worth running a test against.  The explicit setting of
eps
for the PyTorch implementations made sure that they would be as similar as possible .
I set
elementwise_affine=True
for the PyTorch
RMSNorm
out of an abundance of caution --
it's the default value anyway.
One thing I was initially concerned with, but which turned out to be a non-issue, was
weight initialisation.  In many of my tests I've found that the models I've been training
can perform significantly better or worse just based on the random weights they get prior
to training.  If you change which modules make up your model -- say by swapping out a
LayerNorm for an RMSNorm -- then if those modules consume different amounts of randomness when they're being
created, all subsequently-created modules will get different random number results when
their weights are initialised and the results of your tests will be polluted by that.
However, on looking at the code again, I realised that there was nothing to worry about here.
Raschka's LayerNorm and my own RMSNorm do not use any randomness, because their trainable
parameters are set to ones and zeros -- and the PyTorch implementations do the same.
I was actually a little sad about that because it meant that I couldn't use a bit of code
I was rather proud of, but it did simplify things.
That all seemed to work -- I did short test training runs with each of the settings
locally to confirm that loss dropped.  It was time to test things out.
The training runs
I was, as usual, going to train models from scratch that were based on GPT-2 small, with two
differences:
No weight tying.
No bias on the QKV matrices.
These models come out at roughly 163M parameters, which is very small, but was hopefully
large enough to show interesting results.
For the training runs, I would:
Use no dropout.
Schedule the learning rate: a warmup over the first 5% from zero to 0.0014, then
a cosine decay down to 0.00014.
Train for the
Chinchilla-optimal
~20 tokens per parameter.
Training models is expensive -- for others I've been doing with models of this scale,
it takes about 2 days to train them locally on my RTX 3090, or costs about US$40 if
I use DDP to train them on an 8x A100 machine with 40 GiB/GPU (which takes about 2h30m).
So I didn't want to train tons of them, and decided that a sensible minimum set would be:
One with the old LayerNorm.
One with the PyTorch LayerNorm.
One with my hand-rolled RMSNorm.
One with PyTorch's RMSNorm.
I also wanted to do a quick test with no normalisation just to confirm that training
failed.
I did these all on
Lambda
-- there were some issues with instance availability,
but
lambda-manager
once again proved its
usefulness.  I was able to start three instances and spread the training runs across them.
All tests were run with the usual set of commands to make sure that the library
versions and so on were the same:
git clone https://github.com/gpjt/ddp-base-model-from-scratch.git
cd ddp-base-model-from-scratch/
./setup_lambda.sh
uv sync
uv run torchrun --nproc_per_node=8 ddp_train.py CONFIG datasets
...with
CONFIG
set to each of the training run configurations I'd created:
Each configuration was identical apart from the
norm_type
, plus a small extra difference
for the no-norm test, which (conveniently enough) we'll look at now.
Results
Let's look at the no-normalisation test first.  From previous experience, I suspected that it was likely to go
bad fast, so I set it to checkpoint and log training loss every 10 global steps instead
of every 617.  And, indeed, by step 530 it started logging a consistent loss of
nan
on
every training step, so I force-quit it at step 640.
The training loss looked like this:
You can see that loss started rising at step 500, and then after that it didn't
even try to log it.  Gradients also zoomed off the top of the chart:
So, that was reassuring!  As expected, training a Transformer-based LLM without
any kind of normalisation doesn't work well.
The other training runs were much less eventful -- they all completed normally, and
I downloaded the models, and ran my normal held-back test set through them to get
a comparable quality metric.  Here's what I got:
The links go to the models themselves on Hugging Face.
These are really interesting!  Let's look at training speed first.
Training speed
What we're meant to be looking into here is the performance characteristics of
RMSNorm versus LayerNorm, so let's compare like vs like.  The hand-rolled RMSNorm was indeed a bit faster to train
than the hand-rolled LayerNorm, but only about 2.5% faster, both in terms of training
time and tokens per second.  For the runs using the built-in PyTorch modules it was an even closer-run thing -- only
0.5% improvement for RMSNorm.
Without doing tons of extra training runs I can't say safely what the noise level is
for this kind of thing, but my gut feeling (based on having trained
more than 60 of these models now) is that the 2.5% difference is
probably
real, while
the 0.5% one could well just be noise.  In particular, it's worth noting that both
of the "hand-rolled" training runs happened on the same instance (by chance), though
the PyTorch ones were on different ones, which makes the 2.5% number more trustworthy.
But on to the elephant in the room: the difference between the fused PyTorch implementations and the hand-rolled ones
is
much
bigger.  With LayerNorm, it took 11%
less time to run.  The speedup for RMSNorm was a little smaller, at just less than 10%.
That is
definitely
not noise, and completely eclipses the speedup from switching
the kind of normalisation!
Now let's take a look at the quality of our models.
Test loss
Again, we'll start with the like vs like comparison.  Hand-rolled RMSNorm got
a test loss that was
3.601292
−
3.595336
=
0.005956
worse than the hand-rolled
LayerNorm.  That's a tiny difference.
Similarly, the PyTorch RMSNorm got
3.572383
−
3.571158
=
0.001225
worse loss than
the PyTorch LayerNorm.
I'm tempted to say that those numbers were within the noise.  However, I don't have
any numbers to back that up -- when I
looked into noise previously
I did measurements for variations in weight initialisation, and for runs with
the same initial weights but different random seeds for the post-model-initialisation
steps, but those runs used dropout, which the ones in this experiment did not.
In theory, my training loop should be entirely deterministic; no randomness is used
after the initial weight initialisation.
A while back
I did two training runs on 8x A100 machines with the same config, months apart, and the Safetensors files were identical bit-for-bit.
But what we did here was start with a specific set of initial weights, and then see what happened
when we trained them with different normalisation settings.  It's certainly conceivable
that some initial weights might be "in a better place" for training with LayerNorm while others were
in a better place for RMSNorm.
So while the fact that both were a little bit worse with RMSNorm is interesting, I'd really need to
train a bunch of different models to get any certainty here.  Best to chalk it up to
noise for now.
Now, back to that elephant... Once again, the big difference here is not between
LayerNorm and RMSNorm, but between hand-rolled and built-in PyTorch implementations.
For LayerNorm, the PyTorch version got
3.595336
−
3.571158
=
0.024178
lower -- better! --
loss than the hand-rolled one.  And for RMSNorm, the difference was
3.601292
−
3.572383
=
0.028909
.
Those are not super-small differences.  Based on the various
interventions
I tested against the GPT-2 code, that's larger than the improvements I got
from switching to full-fat 32-bit rather than using Automatic Mixed Precision (AMP -- at 0.012558), more than
I got from adding on gradient clipping (0.013209), and more than adding on bias to the
QKV weights (0.022141).
I'd need to do significantly more training runs in order to find out if this was
due to some kind of noise, and I'll not spend that time and money now.  It feels like
there are two possibilities:
It's noise due to numerical differences -- some kind of rounding thing, for example.  Imagine a
tiny difference right at the start of training -- a single parameter gets updated to
0.11892473 with the hand-rolled code, but to 0.11892474 with the fused code.
That slightly changes the results from the next training step, so the gradients
are different, and now the model diverges a bit more.  As we continue over 33,000
training steps over 3.2B tokens, you can imagine that the models could diverge
quite a lot.  We're on a choppy ride over the loss landscape, always trying to head
downwards, and a small change near the start can drastically change where we end up.
Alternatively: maybe there's something systematic that makes the PyTorch implementations
better
in this case?
On the one hand, the fact that the results were consistent is interesting.  If the PyTorch models
had both been better than the hand-rolled ones but by different amounts, then that would
be easy to ascribe to chance (I make it a 25% probability, though you could argue for
1/6).  But the fact that the improvements were so similar is harder to explain.
On the other hand, a systematic difference would be
really weird
, at least to me.  I'm confident that my hand-rolled
implementations match the PyTorch ones in terms of the maths -- not only have I checked and double-checked
the code, but the LayerNorm one was written by someone expert in the field, and I've
also run them past both Claude Opus 5.5 and GPT-6 Astra, both on high thinking levels, to
check that there are no differences .  So while I can't rule errors out, I've done
a lot to try to eliminate them.
For now, I think I'll loosely chalk this up to noise too.  I've seen weird
coincidences crop up before -- regular readers might remember that in my
post on LoRE
, the loss delta of using it on
the input side only, when added to the delta of adding it to the output side
only, was almost exactly the same as the delta for adding it to both ends.  That repro'd
over two separate random seeds and really looked like it was a thing -- only to disappear
with a change to a part of the code that should not have affected it if it had been
a real additive effect.  More Tests Needed.
I think an interesting
set of experiments to test that would be not only to try with different random seeds,
but also to try with different weight initialisation strategies entirely.  What would these
results look like if, instead of using PyTorch's default initialisation, we used the one
they describe in the GPT-2 paper?  (More on that in an upcoming post.)
But back to this experiment: what can the results that we have right now tell us?
Wrapping up
I started this set of experiments with two goals: to understand how RMSNorm works,
and to see if I could show similar results to the original paper -- that it gets
comparable loss to LayerNorm, with a noticeable saving in training time.
I'm happy with the first part of that -- and hopefully if you're reading this, the "how
it works" part is clear for you too!
The loss was, I think, also as expected.  Again, I'd need to do a much larger-scale
experiment with various starting weights to be sure, but the fact that the difference
between RMSNorm and LayerNorm was so small was certainly reassuring.
The training speed was a much less impressive result.  With hand-rolled code, the
2.5% speedup looked potentially real, but it pretty much vanished when I switched
to PyTorch's built-in classes.
The big difference, of course, was that between PyTorch's built-in classes and the
hand-rolled ones.  The speedup from using fused kernels for this stuff was not such
a big surprise, especially after the similar improvement from using the built-in GELU.
It would certainly be interesting to see if using
torch.compile
narrowed the gap, though.
But the improved loss was definitely interesting.  Again, I'd need to do a ton
of training runs to see if that was real or noise.  It seems most likely that
it was noise, but the fact that the effect was positive for PyTorch in both cases, and
was by such a similar amount, keeps nagging at me.
One remaining question aside from that, though: RMSNorm wasn't obviously significantly
faster, especially if you use fused kernels, and while it wasn't obviously worse than LayerNorm, it didn't appear to be
better -- so what explains its popularity in so many open weights models?
The first thing I thought was that maybe it's something that becomes more effective in terms of
cost reductions as
models get larger.  However, having thought it through, I think that exactly the opposite
is true -- its effects get even smaller as we scale up.
Remember that -- in terms of calculations --
RMSNorm saved
3
d
emb
additions/subtractions for each context vector.  That would scale smoothly
as
d
emb
was increased, and of course the number of RMSNorms would increase
proportionally as the model gained more layers.  So I think that the absolute compute reduction
in terms of calculations saved would scale roughly linearly with each of width and depth.
But other aspects of the model's cost scale more than linearly with width.  For example, in
GPT-2, our FFNs map from
d
emb
to
4
d
emb
and back again; that means
that the number of calculations scales as
O
(
d
emb
2
)
.  More modern implementations
use SwiGLU, but I believe that the scaling is of the same order.
And that's not even
to mention the fact that modern models have longer context, and while the norms scale
linearly with the sequence length (and the RMSNorm savings do too), full attention
is
O
(
n
2
)
on that.
So if we're only getting, say,
0.5% improvement for these tiny 163M parameter models with a 1,024 token context length, it would be an even smaller
percentagewise
improvement for larger ones.
Even if that wasn't the case, the amount is pretty small:  DeepSeek
V3 was widely reported to have cost US$6M to train (excluding R&D and a bunch of other stuff,
but that's actually the correct number to use here).  So even if we ignore all of the
above and use it directly, that would just be a US$30,000
saving from using RMSNorm.  And that's basically an upper bound -- we'd expect it to
be significantly less.
Another possibility, though, is that it's an architectural thing.  These open models
have a bunch of differences to the GPT-2-style code I've been using here.  They use
RoPE for position encoding, and SwiGLU for the feed-forward networks.  Mistral has multiple
differences in the attention mechanism.  On the face of it, I don't see any obvious reasons
why those might speed up RMSNorm, but I can certainly
imagine that they might "prefer" one form of normalisation over another, resulting in better loss.  So perhaps
that's what people have found.
But there are plenty of other possibilities.  If people have generally found that it's just
as good as LayerNorm, then perhaps it's just a fashion -- one model uses it, then the
next one has no particular reason to move back, and so on.  And there is a general move
towards dropping biases from LLMs (for example, from the QKV weights), and RMSNorm
would fit that.  And anyway, it is a bit simpler!
Whatever the reason: if RMSNorm is that little bit simpler than LayerNorm, by skipping the recentring
aspect of normalisation, is there something even simpler that could work even better?
While discussing the subject with Claude Opus 5.5, it mentioned
"Transformers without Normalization"
,
which is a really interesting paper -- one of the authors has a neat intro
on GitHub
.  They noticed that the transformations
that normalisation layers tend to learn wind up looking a bit like the S-shaped mappings
you get from the
tanh
function, so tried using that instead with a system they called
Dynamic Tanh (DyT) -- and got good results!
The first sentence in this post was "Normalisation is an essential part of LLMs".  Was that
wrong?  I suppose that depends on what you mean by "normalisation" -- could you regard
their
tanh
trick as being normalisation of some kind? -- though given that
Yann LeCun
was a co-author on the paper I should probably be a bit hesitant to disagree
with his definition of it ;-)
I think their DyT system is something for a follow-on post, though.  For now: RMSNorm seems to be essentially
the same in terms of model quality, and maybe slightly faster than LayerNorm for the models
I've been playing with, at least if you don't use the fused modules.
But using
the fused PyTorch modules instead of hand-rolling our own normalisation is a huge win for
speed.  The loss improvement that came with it in this experiment is very interesting,
but I'd certainly want to do quite a lot of extra experiments before claiming it was real!
For now, I think I'll say that I'm happy that I learned how RMSNorm worked, but I don't
think I'll add it in as a standard part of my training runs.  And the further experiments
can go on the pile with the hundreds of other things I'll look into later.  Once I've learned
about RoPE, and SwiGLU, and all of the rest of it...
Thanks for reading!
Citing this post
This is a blog, and if you want to link to this post then please do :-)
                However, if you're writing something more academic and need to do
                a proper citation, then here's a BibTeX block to make things easier.
@misc{thomas2026oct-rmsnorm,
  author       = {Thomas, Giles},
  title        = {{RMSNorm}},
  year         = {2026},
  month        = oct,
  howpublished = {Blog post},
  url          = {https://www.gilesthomas.com/2026/10/rmsnorm},
}
