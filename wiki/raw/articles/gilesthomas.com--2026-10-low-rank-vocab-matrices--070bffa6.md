---
title: "Fun with low-rank vocab matrices (and a bonus test loss reduction?)"
url: "https://www.gilesthomas.com/2026/10/low-rank-vocab-matrices"
fetched_at: 2026-10-10T10:00:53.464222+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Fun with low-rank vocab matrices (and a bonus test loss reduction?)

Source: https://www.gilesthomas.com/2026/10/low-rank-vocab-matrices

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
I was
nerdsniped
!  On the HF discussion page for one of the
models I created for my
previous post
,
AndrewThompson1233
asked if I'd considered trying out
factorised embeddings
-- something he's using for his model, Maba, and which was previously used in some other models, like
ALBERT
.
It's a really nifty idea; you use a similar trick to LoRA as a way of reducing the
number of parameters used for your embeddings and your output head.  And for small
models, those can be  a disproportionate number of the total.
For example, with my 163 million parameter GPT-2 small-style models, the embeddings
are about
39 million of them
; the output head is
the same size, so with those two taken together,
that's half the model just getting stuff in and out rather than actually doing the
thinking.  Even if you use weight tying, like the original GPT-2 models did, you'll
wind up spending 30% of your "budget" on the single matrix shared between embeddings
and the output head.
Similarly, while larger models have a smaller percentage spent that way, even medium-sized MoE models
can wind up spending a lot of the
active
parameters on embeddings; I
calculated
that for Qwen 3.6 35B MoE, with 3B active parameters, there were about 1B of them used
across both the input embeddings and the output head.
So anything that can reduce that -- so long as it doesn't come at a high cost in terms
of the model's capabilities -- is worth considering.  You save on your parameter count,
which either means smaller models and potentially quicker training, or allows you to "invest" the savings
in more thinking parameters -- that is, a wider network with a higher embedding dimensionality,
or a deeper one with more layers.
Andrew reported that the impact of using this trick was minimal:
At rank 128 on a 50k vocabulary, the penalty on validation cross-entropy is
  negligible (typically within +0.02 to +0.04 loss, or <0.5 perplexity delta).
Now, that suggests that he's getting a loss of around 2.5 (that being the point
where a loss increase of 0.04 implies a perplexity change of 0.5), which is much lower than
I typically get with my
GPT-2 architecture (3.5 is more like it for me), but still, perhaps I'd get good numbers too?
I decided to train a few models to see what happened.
The results were interesting!  I found that using this trick on both the embeddings
and the output head caused a somewhat larger increase in loss than Andrew described
 -- about 0.07 in my first test, 0.10 in the second, and
0.14 in the third.  Those are relatively large,
though potentially recoverable from further training or larger models.
But more surprisingly, I found that using the trick on the input embeddings only
seemed to
reduce
test loss.  Before I'd started, I'd expected it to be less harmful
on the input side than it was on the output side, but seeing an improvement was certainly
unexpected.  Getting loss down by reducing your number of parameters is not what normally
happens!
So, it's definitely worth digging in a bit.  Let's start with the theory: what are these factorised embeddings, and how do they work?  Like LoRA, they rely on
low-rank factors, so firstly I'll define those.
Low-rank factors
Our models are made up of a large set of matrices -- embeddings, output heads, attention
weights, FFN linear layers, and so on.  Making them smaller obviously reduces the number
of parameters for the model, though you would expect it to come at a cost.  The idea behind
low-rank factors is that you can replace a larger matrix with two smaller ones that will
contain most of the important information.
Imagine that you've got a matrix of size
m
×
n
.  Now, from matrix multiplication,
we know that if you multiply an
m
×
r
matrix by an
r
×
n
one, you'll get
a result that is
m
×
n
.  If we do that, then we've factorised the matrix (in the
same way as we might factorise 12 into 3 and 4 because
3
×
4
=
12
), and the value
r
is referred to (logically enough) as the
rank
of the factorisation.
If
r
is sufficiently smaller than
m
and
n
, then
these two matrices -- the
low-rank factors
-- combined will contain fewer parameters than the full matrix.
Let's make this specific, using the output head of
a GPT-2 style model without weight tying.  It takes in the embeddings that result from
the Transformer layers (after normalisation), and converts them into logits across
the vocabulary.  For the GPT-2 small size, our embeddings are 768-dimensional, and the
vocab size is 50,257 tokens.  So when we use a linear layer to do that mapping, it
has
768
×
50257
=
38597376
parameters.
If we were to replace it with two matrices -- say, one of
768
×
128
and one
of
128
×
50257
, then combined they would take
up
768
×
128
+
50257
×
128
=
98304
+
6432896
=
6531200
parameters.  That
is almost six times smaller!
So: the idea is that instead of creating our model with an
m
×
n
matrix, we
create it with a pair,
m
×
r
and
r
×
n
, and train those instead.  If all goes
well, that pair will be almost as capable of learning what we want as the full one would
have been, so we'll get results that are close enough.
The maths and the implementation work out simply, too.  For a linear layer with no bias,
we can write the matrix multiplication that takes our inputs
X
and a weight matrix
W
, and
produces an output
Z
, like this:
Z
=
X
W
Now, if we're using a pair of low-rank factor matrices
A
and
B
instead of a full one,
W
, we can say the
"virtual" weights we want to use for the calculation are
W
′
such that:
W
′
=
A
B
So that means that our calculation for this neural network is this:
Z
=
X
(
A
B
)
Matrix multiplication is associative, which means that you can rewrite that as:
Z
=
(
X
A
)
B
...which hopefully you can see is the same as feeding
X
through a layer
using
A
as its weights, and then feeding the result through a second one using
B
.  In
code, you've taken something like this:
out_head
=
nn
.
Linear
(
d_emb
,
vocab_size
,
bias
=
False
)
...
logits
=
out_head
(
embeddings
)
...and replaced it with this:
out_head_A
=
nn
.
Linear
(
d_emb
,
r
,
bias
=
False
)
out_head_B
=
nn
.
Linear
(
r
,
vocab_size
,
bias
=
False
)
...
intermediate
=
out_head_A
(
embeddings
)
logits
=
out_head_B
(
intermediate
)
It's probably intuitively obvious, though, that this comes at a cost.  If you have
fewer parameters then you can store less information, so this part of your model
is "dumber".  If it's not clear, though, imagine that
r
in the code above was one.
You would be taking the (for GPT-2 small) 768-dimensional embedding, converting it
to a single number, and then expanding that single number out to a 50,257-dimensional
set of logits.  Stuff is going to get lost -- the idea behind low-rank factors is that,
so long as you choose an appropriate value for
r
(which is often referred to as the
width of the
low-rank bottleneck
), you won't lose the
important
stuff.
This works surprisingly well in many cases -- in particular, LoRA, which allows you to
fine-tune models that are too hard to fully train on your hardware, or to fine-tune them faster,
uses it to easily train something like low rank factor "diffs" to your weight matrices .
But for this post, we'll try the simplest version: what if we replace both the input embeddings and the output head -- the vocabulary
matrices -- in their entirety with low-rank bottlenecks?
Introducing LoRE
Low-rank factorisation of the vocabulary matrices is a bit of a
mouthful, so based on the name "LoRA", I decided to call this trick LoRE, for low-rank embeddings.
It's not strictly accurate (after all, we're doing it both to the embedding matrix
at the start of the LLM and to the output head at the end), and I don't expect it
to take off, but I rather like it and will use it in this post :-)
The argument behind it is that the embeddings are just a simple lookup table, so are
exactly the kind of place you'd expect to be able to make savings by only considering
the important parts of our huge matrix; the same
might
apply to the output head at
the end, though personally I was less convinced by this part.
It's worth looking into that asymmetry a bit.  My intuition was that while embeddings
really are a lookup table, the output head is doing something a bit more subtle.  It's
projecting from the continuous embeddings that come out of our Transformer layers into
logits, which we interpret (via softmax) as a probability distribution over possible next
tokens.  That's a significantly less simple job than mapping from "cat" to
the appropriate embedding: as a (simplified) example, if you have an embedding that means
something adjacent to "cat", "dog", "gerbil", "household pet" and so on, then projecting
that to the appropriate values for the next token is non-trivial.
Still, implementation-wise, it was really simple.  I decided to extend the PyTorch code that
I had from
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
",
by adding an optional
lore
section to the model config JSON.  This would allow us
to switch on LoRE mode for the input embeddings and the output head independently,
and would specify the rank -- that is, the
r
in the section above, which says how wide
the low-rank bottleneck between matrices
A
and
B
would be.
So, in code, my first cut changed this:
self
.
tok_emb
=
nn
.
Embedding
(
cfg
[
"vocab_size"
],
cfg
[
"emb_dim"
])
...to this:
if
"lore"
in
cfg
and
cfg
[
"lore"
]
.
get
(
"input_embeddings"
,
False
):
self
.
tok_emb
=
nn
.
Sequential
(
nn
.
Embedding
(
cfg
[
"vocab_size"
],
cfg
[
"lore"
][
"rank"
]),
nn
.
Linear
(
cfg
[
"lore"
][
"rank"
],
cfg
[
"emb_dim"
],
bias
=
False
)
)
else
:
self
.
tok_emb
=
nn
.
Embedding
(
cfg
[
"vocab_size"
],
cfg
[
"emb_dim"
])
...and this:
self
.
out_head
=
nn
.
Linear
(
cfg
[
"emb_dim"
],
cfg
[
"vocab_size"
],
bias
=
False
)
...became this:
if
"lore"
in
cfg
and
cfg
[
"lore"
]
.
get
(
"output_head"
,
False
):
self
.
out_head
=
nn
.
Sequential
(
nn
.
Linear
(
cfg
[
"emb_dim"
],
cfg
[
"lore"
][
"rank"
],
bias
=
False
),
nn
.
Linear
(
cfg
[
"lore"
][
"rank"
],
cfg
[
"vocab_size"
],
bias
=
False
),
)
else
:
self
.
out_head
=
nn
.
Linear
(
cfg
[
"emb_dim"
],
cfg
[
"vocab_size"
],
bias
=
False
)
That in itself was a perfectly reasonable implementation of the underlying concept.
But it had a problem.  I wanted to compare the loss with and without LoRE, and also
find out what the effects of input embedding-only and output-head-only LoRE would be.
But I've found in other experiments that the initial random weights that my models start with
can have a significant effect on the loss that the resulting model gets.  The code
above would give quite different random weights with different configurations.  The fix was
simple, though:
if
"lore"
in
cfg
:
lore_tok_emb
=
nn
.
Sequential
(
nn
.
Embedding
(
cfg
[
"vocab_size"
],
cfg
[
"lore"
][
"rank"
]),
nn
.
Linear
(
cfg
[
"lore"
][
"rank"
],
cfg
[
"emb_dim"
],
bias
=
False
)
)
normal_tok_emb
=
nn
.
Embedding
(
cfg
[
"vocab_size"
],
cfg
[
"emb_dim"
])
if
"lore"
in
cfg
and
cfg
[
"lore"
]
.
get
(
"input_embeddings"
,
False
):
self
.
tok_emb
=
lore_tok_emb
else
:
self
.
tok_emb
=
normal_tok_emb
...
if
"lore"
in
cfg
:
lore_out_head
=
nn
.
Sequential
(
nn
.
Linear
(
cfg
[
"emb_dim"
],
cfg
[
"lore"
][
"rank"
],
bias
=
False
),
nn
.
Linear
(
cfg
[
"lore"
][
"rank"
],
cfg
[
"vocab_size"
],
bias
=
False
),
)
normal_out_head
=
nn
.
Linear
(
cfg
[
"emb_dim"
],
cfg
[
"vocab_size"
],
bias
=
False
)
if
"lore"
in
cfg
and
cfg
[
"lore"
]
.
get
(
"output_head"
,
False
):
self
.
out_head
=
lore_out_head
else
:
self
.
out_head
=
normal_out_head
With that code, so long as there is any LoRE config, we create the same weights
regardless of whether it's used in the input embeddings or the output head.  I would
need to train a baseline which had config for LoRE but just had both
input_embeddings
and
output_head
set to
False
there -- that would actually be a normal, non-LoRE model
but would have the same initial random weights in any parts that it shared with an
equivalent model that did use LoRE.
Additionally, Andrew had
said
that we need to be careful about initialisation:
The main failure mode to watch for during training is early gradient spikes:
  scaling the bottleneck projection initialization to 1 / sqrt(r) keeps variance
  uniform and ensures training dynamics match the full-rank baseline from step 1.
...and
later
:
Keep standard GPT-2 init on the embedding table, but scale the inner linear projection matrices by std = 1.0 / math.sqrt(128).
(The 128 in there is because we were talking about a setup with
r
=
128
, which is
actually what I wound up using.)
Now, I was using PyTorch's default initialisation rather than the classic GPT-2
setup, but I went ahead and added a
smart_initialize
flag to handle the scaling as
Andrew described: if it was set, then right at the
end of the model creation I applied the initialisation
to the low rank factor matrices that were innermost in my model (as in, closest to
the Transformer layers):
if
"lore"
in
cfg
:
if
cfg
[
"lore"
]
.
get
(
"smart_initialize"
,
False
):
nn
.
init
.
normal_
(
lore_tok_emb
[
1
]
.
weight
,
mean
=
0.0
,
std
=
1.0
/
math
.
sqrt
(
cfg
[
"lore"
][
"rank"
])
)
nn
.
init
.
normal_
(
lore_out_head
[
0
]
.
weight
,
mean
=
0.0
,
std
=
1.0
/
math
.
sqrt
(
cfg
[
"lore"
][
"rank"
])
)
Even though that was not run for every configuration, because it happened right at
the end of the model creation, it would not affect the other weights, so I figured
that it would be safe.
You can see the full diff from the normal GPT-2 code
here
.
Those changes looked correct to me, and I asked GPT-6 Astra (on "extra high" thinking)
to confirm that it looked right to it in the context
of the discussion, which it did.  That done, I
double-checked with Andrew
,
as I really wanted this to be a clean attempt at a repro of his results.  He confirmed,
so it was time to train some models!
The first training runs
I decided that I wanted five training runs to check this out thoroughly:
A baseline.  As I said earlier, the LoRE stuff would have an effect on the randomness
used for the initial weights, so I wanted to train one model with LoRE "enabled"
but not actually used.  Config:
model.json
,
train.json
.
A model trained with LoRE enabled on both the input embeddings and the output
head, but without the smart initialisation of the low-rank matrices.  This was
simply to confirm to myself that it was required.   Config:
model.json
,
train.json
.
A model with LoRE on both ends,
with
the smart initialisation -- essentially,
what Andrew had described.   Config:
model.json
,
train.json
.
A model with LoRE on the input embeddings only, using smart initialisation if that had
turned out to be necessary, and not using it if it had not.  I deliberately made
the config invalid, using
TODO
instead of
true
or
false
for the
smart_initialize
flag, so that I'd be reminded to fill those in later.
Config:
model.json
,
train.json
.
A model with LoRE on the output head only, with smart initialisation the same as with (4).
Config:
model.json
,
train.json
.
To save time, I decided to train them in the cloud: the first three, and then the last two,
in two batches of parallel runs.  I used 8x A100 machines with 40 GiB VRAM per GPU on
Lambda
.  I'll break
with my normal tradition of giving detailed runthroughs of each training run,
as there are (spoiler) quite a lot of them in this post!  However, for reproducibility,
the commands I ran for each one looked like this:
git clone https://github.com/gpjt/ddp-base-model-from-scratch.git
cd ddp-base-model-from-scratch/
git checkout lore-experiment
./setup_lambda.sh
uv sync
uv run torchrun --nproc_per_node=8 ddp_train.py 8xa100m40-lore-1-baseline-disabled datasets
...with the run ID,
8xa100m40-lore-1-baseline-disabled
, replaced with the appropriate
one for the given
run settings
.
Here are the results from the first three runs: the baseline, and the ones with
LoRE at both ends, with and without smart initialisation.  The model name links go to
the uploaded models on Hugging Face.
You can see that I had some issues with the last run; there were shortages of available
instances, and I wound up starting one in Japan.  Connectivity to it from my home in
Portugal was really slow and unreliable; when I tried to download the model after the training run,
scp
was predicting 10 hours (which at the machine's cost of US$15.92/hour would have been insane).  However,
I was able to copy it to my
PythonAnywhere
account
quickly, perhaps because that is in a US Amazon datacenter and had better connectivity to Japan, and then I could copy it from
there to my machine, again quite quickly.  Unfortunately while scrabbling around with that I didn't capture
all of the output.
Still, the important data at this stage was in the test loss column.  As expected,
using LoRE made the test loss worse.  And smart initialisation did seem to help reduce that
penalty.
The loss delta, at +0.07, was worse than the +0.02 to +0.04 that Andrew described
in his message, but not wildly different -- certainly small enough that it seemed
plausible that you could recover it, and perhaps more, by investing the 64M parameter
difference in a deeper or wider model.  Promising!
The cost and time savings were real, too: the
run in Japan had its cost bumped up by all of the woes I had copying the model down,
so the
8xa100m40-lore-2-both-ordinary-init
one is the best indication: US$38.55 rather than
US$43.96, so a saving of more than 10%.  And while going down from a bit more than 2h30m
to 2h14m might not seem like much, with a larger model or a longer training run, an almost 14% reduction
could be valuable in and of itself.  (And that's not even considering the alternative of
"reinvesting" the saved parameters in larger models.)
So that was pretty good news!  It was time to do the ablation runs to see whether
having LoRE just on the token embeddings, or just on the output head, made things
any different.  I switched the
smart_initialize
setting for the remaining two
models to
true
, and kicked them off.
Now, there's a bunch of interesting stuff in there, but let's focus on the test
loss.  My lab notes for this bit say "well, that's a bit of a shocker!"
Quite amazingly -- at least to me -- we got
lower
test loss with the input-only LoRE,
with 3.526610, than we did with the no-LoRE baseline, which got 3.599611.
Things get even more interesting when you compare the different versions (excluding
the non-smart-init) against each other, in terms of their difference from the no-LoRE
baseline (which I'll call the delta for conciseness below).  Rounding to 3dps:
Output LoRE off
Output LoRE on
Input LoRE off
-
0.138
Input LoRE on
-0.073
0.072
If you add the two single-LoRE loss deltas together -- the 0.138 and the -0.073 --
you get 0.065, which is surprisingly close to the delta of 0.072 for the dual-LoRE option, just
0.007 away.
Could we be looking at two almost independent effects, one for each option of where to
apply the LoRE?  And was that apparent benefit of the input-only LoRE a real thing?
Or was it due to chance -- perhaps we had "good luck" when initialising the LoRE weights,
and "bad luck" when initialising the non-LoRE ones.  If there was an overlap between
the best loss you could get with LoRE and the worst loss you could get without, then
this result could be within the noise.
I decided I was going to do a second batch of training runs to see if I could get
evidence one way or the other.  But before we get into that, it's worth taking a look at
some of the other numbers in those two tables.
Firstly, let's take a look at the training time.  The training machines looked
like they were running at close to 100% during all of the runs, so tentatively let's
assume that time taken is proportional to compute.  Unsurprisingly, the baseline run
came in with the longest time, at 9,339s.  And equally unsurprisingly, the full-LoRE run
that we have timing for was much faster, at 8,057s.
It certainly makes sense that replacing big matrices with pairs of (much)
smaller low-rank factors will mean fewer calculations on both the forward and the backward
pass, meaning that the training run is faster.
There was something that initially surprised me with the single-LoRE runs.  Using
LoRE on the output head sped things up quite a lot, but input embedding LoRE had much
less effect.
However, after thinking about it a bit, it became clear what was going on.  An embedding
module in a network is actually really quick to run, both on the forward and backward pass.
While I like to think of embeddings as
conceptually
being a projection of a one-hot
vector in vocab space into embedding space via a matrix multiplication, and I still think
that's an excellent model of interpreting what's going on, in practice it's just something
much more like an array lookup, with almost zero cost.  Likewise on the backward pass,
we only need to work out gradients for the chosen embedding, so that should be faster too.
Indeed, with that all in mind, it might not have been surprising if input-only LoRE
had turned out to be a bit
slower
than the baseline, as it, at least, needed to do
forward and backward passes through actual matrices, even though they were fairly small.
Doing another of those delta tables, the time difference in seconds (using the
"ordinary init" run for the both-on number):
Output LoRE off
Output LoRE on
Input LoRE off
-
-1,137
Input LoRE on
-114
-1,282
You can see that if you add the delta of the single-LoRE options, you get -1,251,
which is pleasingly close to the delta of the dual-LoRE one.  And that is much less
surprising than the loss result -- with training compute, you really would expect
improvements like this to be additive.
Finally, there was something interesting in the initial training loss.  Because my
training code prints out the loss it got on the first global step, I decided to note it down.
There's something in this data that will become important later: in both of the training
runs with LoRE on the output head
and
smart initialisation, it went up noticeably.
Normally, the initial training loss on my GPT-2-style models is a bit less than 11.  This
fits in well with the architecture; you'd expect that a model that was predicting tokens
purely randomly (well, strictly, uniformly) would have a perplexity roughly equal to the vocab size; the vocab
size for the GPT-2 tokeniser is 50,257, and loss is the natural logarithm of perplexity,
so that implies a loss of roughly 10.82.
But both of those smart-init models with LoRE on the output head had an initial loss about
one point higher, at 11.865 and 11.817, meaning that they were significantly
worse
than
random.  What might be going on here?  We'll find out later :-)
Anyway, for now, that was an interesting set of results.  I wanted to dig in more; in particular, would that
surprising improvement of test loss for the input-only LoRE model reproduce if I tried
again with a different random seed?
The second set of models
I had two working hypotheses at this point; either
What we were seeing was due to luck of the draw with the random initialisation
of the weights -- good luck with LoRE, bad luck without.
There really was an effect here: input-only LoRE actually improved test loss in the
resulting model.
A solid and simple test to try to distinguish between these was just to train another
set of models, with a different random seed.  If I got the same kind of results, input LoRE beating
non-LoRE, that
would be evidence in favour of (2) rather than (1), whereas if
things changed, it would work the other way.
I decided not to bother with a non-smart-init model this time, so I set things up for
four new models.  My training code
uses a random seed of 42
by default, but allows it to be overridden in the
train.json
config file, so I decided
to use 123 for these, and created:
A new baseline with no LoRE.  Config:
model.json
,
train.json
.
An input-only LoRE.  I wanted to run this one as the first non-baseline one, because
if it got
worse
(higher) loss than the baseline, then it would look rather
like the effect I'd previously seen was due to random weight initialisation,
so I might want to consider stopping there.
Config:
model.json
,
train.json
.
If I decided to continue, the next one would be LoRE on both the input and output sides.
Config:
model.json
,
train.json
.
Finally, I'd do an output head LoRE only one.  Config:
model.json
,
train.json
.
Once I had the config together, it was time to train the models -- but it was hard to
get available instances on Lambda.  I wound up having to use my
lambda-manager
script to start things up, but after a few hours I got an alert on my phone that I had
instances running, and could kick things off.
The second training run with input-only LoRE came in with a test loss that once again
beat the baseline, so I did the full set of runs, and here are the results:
Model
Parameters
Training time (s)
Initial training loss
Final training loss
Test loss
Cost (US$)
8xa100m40-lore-6-new-seed-baseline-disabled
163,009,536
9,409
11.006
3.577
3.597584
45.03
8xa100m40-lore-7-new-seed-input-only
130,943,360
9,163
10.989
3.563
3.584511
43.03
8xa100m40-lore-8-new-seed-both-smart-init
98,877,184
8,102
11.829
3.678
3.698644
37.91
8xa100m40-lore-9-new-seed-output-only
130,943,360
8,192
11.806
3.693
3.712537
38.32
Another matrix of deltas against the baseline:
Output LoRE off
Output LoRE on
Input LoRE off
-
0.115
Input LoRE on
-0.013
0.101
So, once again, input-only LoRE improved test loss (though at -0.013, it
was a smaller effect than the -0.073 the previous set of models had).
And once again, the sum of the input-only and output-only LoRE deltas was close
to the combined-LoRE model's -- indeed it was even closer, 0.102 being just
0.001 away from 0.101.
The training time results and the higher initial training loss for models with
LoRE on the output head also held up, which was good to see.  So at this point it
was time to wrap things up -- or was it?
The
smart_initialize
problem
While I was doing the second batch of training runs, I started writing up this
experiment.  As I
normally do
, I ran a draft past various AI
models, and Claude Opus 5.5 on max thinking spotted something.
Andrew had
written
:
Keep standard GPT-2 init on the embedding table, but scale the inner linear projection matrices by std = 1.0 / math.sqrt(128).
I'd interpreted that "inner" as meaning that the "innermost" matrices in our low rank
factors -- the ones that were closest to the Transformer layers -- should be initialised
as he said, with values drawn from a normal distribution with a
standard deviation of
1
/
r
, and a mean of zero.
So that implied the second matrix in the
embeddings, and the first one in the output head:
if
"lore"
in
cfg
:
if
cfg
[
"lore"
]
.
get
(
"smart_initialize"
,
False
):
nn
.
init
.
normal_
(
lore_tok_emb
[
1
]
.
weight
,
mean
=
0.0
,
std
=
1.0
/
math
.
sqrt
(
cfg
[
"lore"
][
"rank"
])
)
nn
.
init
.
normal_
(
lore_out_head
[
0
]
.
weight
,
mean
=
0.0
,
std
=
1.0
/
math
.
sqrt
(
cfg
[
"lore"
][
"rank"
])
)
Claude felt that it should be the second low-rank factor in both cases -- that is,
we should change
...to
It made a very good case for doing things that way, and digging into that is useful because
it changes this "smart" initialisation from being a blindly-implemented "secret sauce"
into something actually meaningful.
Let's imagine that we're not using LoRE, and consider the output head only.  It is
a PyTorch
nn.Linear
,
which means that:
...the values are initialized from
𝒰
(
−
k
,
k
)
,
  where
k
=
1
in_features
So, we have a matrix, which we can call
W
, that is full of numbers drawn from that probability distribution --
a uniform (flat) distribution within the range from
−
k
to
k
.
For LoRE, we're replacing
W
with two separate matrices, which we'll call
A
and
B
:
self
.
out_head
=
nn
.
Sequential
(
nn
.
Linear
(
cfg
[
"emb_dim"
],
cfg
[
"lore"
][
"rank"
],
bias
=
False
),
nn
.
Linear
(
cfg
[
"lore"
][
"rank"
],
cfg
[
"vocab_size"
],
bias
=
False
),
)
Let's say that
W
is shaped
m
×
n
, which means that
A
is
m
×
r
,
and
B
is
r
×
n
.  We want the combined effect of those two
matrices
W
′
=
A
B
to start off with random numbers that look like -- in terms of
their randomness -- the full matrix
W
.
But what do the numbers actually look like in our "virtual" matrix
W
′
with the code above?  On the face of it,
it sounds unlikely to be anything like the probability distribution for
W
.  After
all,
W
was initialised based on a formula that used
in_features
.
You can see that
A
will have been initialised using the same distribution, as it has
the same number of input features, but the
number of input features for
B
is
r
, so its random numbers will have been based on
that instead.  Their combination into
W
′
will presumably blend something from each of
those two different probability distributions.
We can actually work out what that will be.  Maths incoming:
click here to skip
.
Per
Wikipedia
,
the variance of the product of two independent random scalar variables (so, not matrices, but
we'll come back to that)
X
and
Y
is this:
Var
(
X
Y
)
=
(
σ
X
2
+
μ
X
2
)
(
σ
Y
2
+
μ
Y
2
)
−
μ
X
2
μ
Y
2
...where
σ
X
2
is
X
's variance,
μ
X
is its mean, and likewise for
Y
.
Now, let's say that the mean is zero for both
X
and
Y
(like it is for PyTorch's distribution for the initial weights,
𝒰
(
−
k
,
k
)
).
That simplifies the above:
Var
(
X
Y
)
=
σ
X
2
·
σ
Y
2
How does that apply to our matrices?
Well, let's write out how we calculate
W
′
by multiplying
A
and
B
, assuming that
m
=
3
,
n
=
4
, and
r
=
2
:
W
′
=
A
B
=
[
a
0
,
0
a
0
,
1
a
1
,
0
a
1
,
1
a
2
,
0
a
2
,
1
]
[
b
0
,
0
b
0
,
1
b
0
,
2
b
0
,
3
b
1
,
0
b
1
,
1
b
1
,
2
b
1
,
3
]
By normal matrix maths, the value at position
0
,
0
in the result will be the dot product of the zeroth
row in the first matrix (taken as a vector) and the zeroth column in the second:
W
0
,
0
′
=
(
a
0
,
0
a
0
,
1
)
·
(
b
0
,
0
b
1
,
0
)
=
(
a
0
,
0
·
b
0
,
0
)
+
(
a
0
,
1
·
b
1
,
0
)
We can rewrite that for an arbitrary low rank bottleneck
r
like this:
W
0
,
0
′
=
∑
x
=
0
r
−
1
a
0
,
x
·
b
x
,
0
...and even more generally, we can define all of the items in
W
′
like this:
W
i
,
j
′
=
∑
x
=
0
r
−
1
a
i
,
x
·
b
x
,
j
So, every element is the sum of
r
products, where each product multiplies a number from
whatever distribution was used to initialise
A
's elements by a number from whatever was used
for
B
's.
Using the notation from above,
A
's elements have variance
σ
A
2
and
B
's have variance
σ
B
2
.
So that means that the variance of each component of that sum is
σ
A
2
·
σ
B
2
.
There are
r
of them; if you add together independent variables, their variances add,
so that means that the variance of the elements of our resulting
W
′
is:
Var
(
W
′
)
=
r
·
σ
A
2
·
σ
B
2
Now, let's remember that our matrix
A
actually already was initialised in the way
we would have liked our non-LoRE version
W
to have been done.  The distribution of the random initial weights for an
nn.Linear
is
dependent entirely on the number of input features -- and of course
A
has the same number
of input features as
W
.
So how can we make
Var
(
W
′
)
be
σ
A
2
?  We need to
make
σ
B
2
=
1
/
r
, and then the equation above drops out like this:
Var
(
W
′
)
=
r
·
σ
A
2
·
1
r
=
σ
A
2
Now, let's look at the code (with Claude's correction in there):
nn
.
init
.
normal_
(
lore_out_head
[
1
]
.
weight
,
mean
=
0.0
,
std
=
1.0
/
math
.
sqrt
(
cfg
[
"lore"
][
"rank"
])
)
We're setting the weights on our
B
matrix to be drawn from a distribution with a standard deviation of
1
/
r
.  SD is, of course,
the square root of the variance (which is why we've been using things
like
σ
B
2
with that squaring in there to represent variance --
σ
on its
own is used for standard deviation).  So the variance of the matrix after we've called
that
normal_
on it will be
1
/
r
as desired, and
W
′
will have random initial weights
with the same variance as
W
would have done if we'd created it directly.
That's rather satisfying :-)
So that's the output head.  How about the input embeddings?  They're
nn.Embedding
s,
which are initialised somewhat differently:
initialized from
𝒩
(
0
,
1
)
That's a normal distribution, with a mean of 0 and a variance (and thus also a
standard deviation) of 1.  The maths above applied to any distribution with a mean
of zero -- so the smart initialisation should work for those too.  Our
A
matrix would
have the correct variance, 1, and a mean of zero, and therefore so would
A
B
, given that
(for embeddings)
B
already had the smart initialisation.
So does that mean that our
W
′
"virtual" matrix created by
multiplying
A
and
B
is identical in terms of randomness to the matrix
W
that
it's replacing?   Well, not quite.
Remember that the output head had numbers drawn from a uniform distribution, and
the embeddings from a normal distribution.  We're multiplying the
A
matrices that are the
"input" low rank factor matrices by
B
s that are initialised from a normal distribution.
The variance of the
A
matrices is maintained by the smart initialisation, as we've
shown, and the mean (being zero) is going to come through cleanly too.  But the shape will change.
I did a bit of digging around and it started to feel like
a bit of a rabbit hole, but the one thing I was able to be certain of is that a variable
drawn from a uniform distribution multiplied by another from a normal distribution gives a
result that is neither uniform nor normal, and that normal times normal gives something
called a normal product distribution (or also a product-normal distribution), which is also
neither uniform nor normal.
Remember that each element of our
W
′
matrix is defined by this:
W
i
,
j
′
=
∑
x
=
0
r
−
1
a
i
,
x
·
b
x
,
j
So each one is a sum of
r
numbers, each of which is drawn from a product normal distribution
(for embeddings) or from whatever the uniform
×
normal distribution is called.  What shape
would that be?  Again: rabbit hole, but the central limit theorem states (
per Wolfram MathWorld
):
the normalized sum of independent random variates with finite variances approaches a normal distribution
So, for large
r
, we can say that the result is going to be close to a normal distribution.
What the smart initialisation does is make sure that our "virtual"
weights,
W
′
=
A
B
, have the same mean and variance as the ones we're trying to
approximate,
W
.  But it won't keep the same shape for the distribution that they're drawn from -- certainly not for the output head,
which goes from uniform to normal-ish.  The embeddings are less impacted (though not
completely untouched) because they were normal and are still almost so.
Still, it's a neat trick!  Was it what Andrew had actually meant?
Correcting the smart initialisation
Having convinced myself that the smart initialisation code I'd been using was wrong,
I decided to check with Andrew.  My first thought was that perhaps he was using weight
tying -- remember, with weight tying, the embedding matrix is just re-used in transposed
form for the output head.  That would mean that the embeddings would be
W
′
=
A
B
, and
you'd use the smart initialisation on
B
, but the output head -- being that transpose --
would use
W
′
T
=
B
T
A
T
for the same
B
and
A
, so the smart initialisation would be
the other way around.
But as it turned out, it was
just a miscommunication
.
He said that he keeps his weights untied, and had been using the word
"inner" in "inner linear projection matrices" to mean something different to what I'd
interpreted it as.  He confirmed that the real smart init code should always be
applied to the second matrix, as the maths (and Claude) suggested.
So that was a simple change.  You can see
the diff here
,
but in short:
I changed the
smart_initialize
config parameter so that instead of just being
False
or
True
, it could be
False
,
"original"
for the original incorrect
interpretation, or
"corrected"
for the fixed one.
I updated all of the existing training configurations that had
smart_initialize
set
to
True
to be
"original"
.
I added on yet more config for some more training runs to test this, setting
smart_initialize
to the new
"corrected"
option.
Now, the good news (both for my own sanity and my wallet) was that testing this fix
was not going to require another four training runs.   My training code is essentially deterministic
-- no dropout or any other randomness is used after the model is created .
Because the smart initialisation code was at the end of the model creation, and
smart initialisation of the output head was right at the end, that meant that changing
it would not affect any other code that used randomness.
So if I did two training
runs -- with LoRE switched on for the output head only, and with it switched on for both
embeddings and output -- then those would be "compatible" with earlier training
runs that had no LoRE at all, and that only had it on the embeddings.  You can see
the configs here (with no explicit random seed, so they'd use my default of 42):
Here are the results; I've put them into a table with their counterparts from the
original seed-42 training run:
Model
Parameters
Training time (s)
Initial training loss
Final training loss
Test loss
Cost (US$)
8xa100m40-lore-1-baseline-disabled
163,009,536
9,339
10.992
3.579
3.599611
43.96
8xa100m40-lore-10-both-corrected-smart-init
98,877,184
8,069
10.987
3.722
3.741209
37.65
8xa100m40-lore-4-input-only
130,943,360
9,225
10.978
3.505
3.526610
44.83
8xa100m40-lore-11-output-only-corrected-smart-init
130,943,360
8,194
10.986
3.766
3.785209
38.19
Before we look at the test loss, check out that "Initial training loss" column.  The
weirdness that I'd noticed earlier, where that value was much worse than uniform, is gone!
That actually makes some kind of sense.  With the smart initialisation on the wrong
part of the low-rank output head, our variance was completely wrong, and so the model
was initially producing particularly bad results.
So that was promising!  But the test loss results were even more interesting.  In
our original seed-42 results with the incorrect init, the output-head-LoRE-only model got a test loss of
3.737128, but here we got 3.785209.  It was actually worse with the corrected smart
initialisation!  And that carried through to the result for models with LoRE on both
input and output; the original model with the incorrect init got 3.671585, and here
we got 3.741209 -- an even bigger worsening.
Combining those two together, an image I like in terms of the loss landscape is that
previously we were starting on a mountain that was near a deep valley -- we started with high loss,
but there was a low-loss place nearby.  But with the smart initialisation fixed,
we were now starting on a hill with a less-deep valley nearby.
So what happens if we do one of our test loss delta tables showing
how each model performed against the baseline?
Output LoRE off
Output LoRE on
Input LoRE off
-
0.186
Input LoRE on
-0.073
0.142
If we add up the effect of the input-only test loss delta of -0.073 and the
output-only delta of 0.186, we get 0.113 -- quite different to the delta of
0.142 that we actually got with them both.  That nice "additive" property that
we had, where the delta from input LoRE only plus the delta from output LoRE only
summed to almost exactly the same as the delta for LoRE on both ends, appears to have
gone away :-(
Still, an interesting set of results!  Let's bring everything together.
The results
Here are all of the training runs together in one table.  I've removed the columns for
the cost, the end training loss, and the training time to keep things manageable,
and I've sorted it by the test loss.
Model
Parameters
Input LoRE
Output LoRE
Seed
Smart init
Initial training loss
Test loss
8xa100m40-lore-4-input-only
130,943,360
yes
no
42
original
10.978
3.526610
8xa100m40-lore-7-new-seed-input-only
130,943,360
yes
no
123
original
10.989
3.584511
8xa100m40-lore-6-new-seed-baseline-disabled
163,009,536
no
no
123
none
11.006
3.597584
8xa100m40-lore-1-baseline-disabled
163,009,536
no
no
42
none
10.992
3.599611
8xa100m40-lore-3-both-smart-init
98,877,184
yes
yes
42
original
11.865
3.671585
8xa100m40-lore-8-new-seed-both-smart-init
98,877,184
yes
yes
123
original
11.829
3.698644
8xa100m40-lore-9-new-seed-output-only
130,943,360
no
yes
123
original
11.806
3.712537
8xa100m40-lore-2-both-ordinary-init
98,877,184
yes
yes
42
none
10.89
3.723328
8xa100m40-lore-5-output-only
130,943,360
no
yes
42
original
11.817
3.737128
8xa100m40-lore-10-both-corrected-smart-init
98,877,184
yes
yes
42
corrected
10.987
3.741209
8xa100m40-lore-11-output-only-corrected-smart-init
130,943,360
no
yes
42
corrected
10.986
3.785209
A few things stand out:
The input-only LoRE models lead the pack -- though it's a close-run thing,
and the gap between
8xa100m40-lore-7-new-seed-input-only
and
8xa100m40-lore-6-new-seed-baseline-disabled
could well be
within the noise
at 0.013.  In that post, I trained three models with different weight initialisation seeds,
and got models that differed by up to ~0.017.
The two models with the corrected smart initialisation are the worst -- even worse
than the model with no extra initialisation,
8xa100m40-lore-2-both-ordinary-init
.
So what does that all tell us?
Wrapping up
The numbers above suggest three things -- with important caveats below:
LoRE can reduce the number of parameters in these models dramatically even if
only applied to the input embeddings, and that comes with potentially an
improvement
in test loss (0.073 in one test, 0.013 in a second).
When applied to the output head, it has the same size of reduction in the parameter
count, and causes a
worsening
in test loss (over three tests,
0.115, 0.138 and 0.186).
The results with LoRE on both ends seemed to come in somewhere around (in two of the
three cases, very close to) the sum of the input-only and output-only deltas,
though it doesn't seem to be a strictly additive relationship.
Even more caveated, we might say:
The mathematically cleaner implementation of what I've been calling "smart initialisation"
actually worked worse than the mistaken version I used originally, though this
was only tested with one seed, so the evidence is much weaker.
Neither the larger of the two apparent improvements from input-only LoRE nor the worsening from output-only
were small -- when I was trying various
interventions
into
my GPT-2 models (like removing dropout, scheduling the learning rate, gradient clipping and
so on), many of them had a similar or smaller level of effect.  Similarly, training a comparable non-LoRE model on double the number
of Chinchilla-optimal tokens (ie. on 40 per parameter rather than 20) improved loss
by 0.09, while investing the same compute resources to do a Chinchilla-optimal training
run on a larger model improved it by roughly 0.13 over the baseline (see
this post
for the raw numbers).
So, is input-only LoRE One Weird Trick To Improve Your Test Loss?  Of course not.  Are output-only LoRE
and both-ends LoRE Bad Things?  Not necessarily.
The first thing to remember is that this is a really limited set of experiments.
Although I wound up spending about US$450 on training runs (I really should be investing
in building my machine
poppy
up as a better
training box to save on Lambda costs), I was only able to test:
Against my own GPT-2 style model (important differences from the original: no weight
tying or bias on the QKV weights, no dropout, and PyTorch default weight initialisation).
With two seeds.
With two options for smart initialisation, and one of them only with one seed.
Over a number of tokens chosen to be Chinchilla-optimal for the baseline non-LoRE model.
Even in order to say anything definitive about whether LoRE works for this specific
architecture, it would be necessary to do tests over a much larger number of random
seeds and different lengths (in terms of number of tokens) of training run:
Maybe the effect was just limited to the seeds I tested?  Two is better than one,
but three would be better still, four even better, and so on.
Maybe the effect disappears in longer training runs?  Perhaps LoRE causes some kind
of loss in capacity that stops models from improving past some point.  Intuitively
that could make sense -- if you imagine training as being in some sense compressing information
from the training data into the parameters, having fewer parameters is clearly going
to limit your capacity in some sense.
To get solid results on whether smart initialisation is a good thing, you'd need to try
a number of seeds to see whether the poor performance of the "correct" smart initialisation
against the "incorrect" one worked out as a general result.  And if it did, why might that
be?
Beyond that: the apparent improvement in the loss from input-only LoRE is something
that came up in these experiments.  Maybe it would turn out to be a real thing, maybe not,
but the real benefit that Andrew mentioned in his
original message
was about something quite different: LoRE saves a
lot
of parameters and only (as he
said later) costs a small amount of loss.  If you reinvest those saved parameters in
a deeper network with more layers, you can hopefully gain back the loss that you,
um, lost, and then some -- and wind up with a more capable model.
So important further tests (which I think I will do, but later on) would be:
Isoparameter tests:
Input-only LoRE saves 32M parameters, so what happens if you
"spend" that on extra layers?  Or alternatively make the model wider (in terms
of its embedding dimension)?  Or some combination of both?
Output-only LoRE likewise.
And, of course, both input and output.
Isocompute tests.  Notably, input-only LoRE doesn't save you much compute, as
I mentioned earlier -- embedding layers are cheap in terms of compute, if not in terms
of parameters.  So here perhaps it would be more interesting to see what happens
if you did output-only LoRE, but trained the model on more data so that the total
training compute budget matched.  Would you gain back the lost loss?
It's worth noting that in my Chinchilla experiments, I scaled up the model by
2
.
That's about a 41% increase, which is quite close to the 39% we save by using LoRE on
both ends.  So if the loss improvements
carried over, perhaps it might work?  On the other hand, those
models were also trained on 41% more tokens, so...
So there's a huge number of further experiments that would be needed to build out these
results -- and that's even before we move beyond this specific architecture.  Andrew
reports solid results with his setup, and his model Maba does appear to be quite different.
But would it extend to a Qwen-style one?  Or Mistral?
Next, there's what happens with scaling.  LoRE is valuable in small models because
embeddings and the output head are such a large proportion of the total parameter
count.  My guess is that it would become increasingly unhelpful as models got larger.
To take an extreme case, looking at
the Kimi K3 paper
, it has a vocab size
of 160k, and its hidden dimension (which I'll assume is what the embeddings are using)
is 7,168.  That means that the embedding layer uses something like 1,146,880,000 parameters, as
does the output head, for a total of ~2.3B parameters (assuming they're not using weight tying,
which seems likely for a monster like this).
It has 104.2B active parameters
per token, so if it were to use LoRE you'd save something of the order of 2% of the active parameter
count.  But for purposes of "reinvesting" in further layers, the real comparison point is the
total number of parameters, not the active ones, and with about 2.8T total, the
number used for embeddings is less than 0.1%.  It doesn't sound
like it would help much.
Unless, of course, the benefit of the input-only LoRE loss improvement actually turned
out to be a real thing, and didn't weaken as the model was scaled...
But anyway, that's speculation.  I think a good set of experiments for that would
be to try the same training runs as before, but for larger models.  Maybe just trying
GPT-2 medium and large sizes would be a good start?
Lots of work.  If I had access to Google's resources then I think I'd be kicking
off a bunch of training runs.  OTOH if I had access to Google's resources I probably
wouldn't be blogging about this...
I think that there's one thing I'm going to take away from this.  LoRE is an
interesting intervention -- and I think is well worth trying out on any new model
where vocab matrices are a significant fraction of the parameters,
just to see if it helps.  I'll be doing that in future.
And if anyone else out there wants to try LoRE-style training runs, I'd love to hear
from you.  Any results, positive or negative, would be really interesting.
Thanks for reading!  And many, many thanks to Andrew for suggesting this as an idea
to play around with -- it's been fun :-)
Citing this post
This is a blog, and if you want to link to this post then please do :-)
                However, if you're writing something more academic and need to do
                a proper citation, then here's a BibTeX block to make things easier.
@misc{thomas2026oct-low-rank-vocab-matrices,
  author       = {Thomas, Giles},
  title        = {{Fun with low-rank vocab matrices (and a bonus test loss reduction?)}},
  year         = {2026},
  month        = oct,
  howpublished = {Blog post},
  url          = {https://www.gilesthomas.com/2026/10/low-rank-vocab-matrices},
}
