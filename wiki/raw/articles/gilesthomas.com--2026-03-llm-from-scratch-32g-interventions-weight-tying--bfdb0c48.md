---
title: "Writing an LLM from scratch, part 32g -- Interventions: weight tying"
url: "https://www.gilesthomas.com/2026/03/llm-from-scratch-32g-interventions-weight-tying"
fetched_at: 2026-05-01T07:02:05.395393+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Writing an LLM from scratch, part 32g -- Interventions: weight tying

Source: https://www.gilesthomas.com/2026/03/llm-from-scratch-32g-interventions-weight-tying

Archives
Categories
Blogroll
In
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
",
he writes that weight tying, while it reduces the parameter count of a model,
in his experience makes it worse.  As such, apparently people don't use it in modern LLMs.  Intuitively, that makes
sense -- I'll explain why in this post.
But as I'm trying various
interventions
to see
if I can get my model -- based on Raschka's code, but trained for a fraction of the time that the original GPT-2 model was -- to perform as well as the original
in terms of the loss it gets on a test set, I thought it would be worth
seeing if it really is a negative for this particular tiny model of 163M parameters.
After all, the original weights use weight tying, and I did find that
QKV bias
appeared to help -- and that's
another old-school technique that they used, which has since dropped out of fashion.  Might
this one help too?
Worth a try!  Let's give it a go.
Weight tying: a refresher
I'll start with a quick refresher on what weight tying is, and how it works.  This
is really targeted at people who've been reading along with this series -- if it's
all new to you, you might find my post on
Maths for LLMs
a useful catch-up guide first.
In our LLM code, right at the start, we use an embedding layer
to take our input token IDs, and turn them into embeddings -- each token becomes a vector
in a high-dimensional space (768 in our case), which we see as representing
in some manner the "meaning" of the token.
A useful way to think about that is that we could start with a one-hot vector for the token --
that is, with our 50,257-token vocabulary, it would be 50,257 items long, and have zeros
in every position apart from the position corresponding to the token's ID.  We'll treat that
as being a vector in a "vocab space".  The process of converting the token into an
embedding turns out to be equivalent to multiplying that vocab space representation
by an embedding matrix -- one with one row per possible token, the values in that row
being the values for the appropriate embedding.
Because matrix multiplications can be seen as projections between different spaces,
we can see that as a projection from our vocab space to the embedding space.
Once we've projected our sequence of tokens into a sequence of embeddings, we do all of the steps
required for the LLM -- we add in positional information, run it through the Transformers layers,
normalise it, and then we have a new sequence of embeddings.
The embedding at position
n
in that output sequence, if our model is working well,
should be something that represents an appropriate next-token prediction for the
portion of the input sequence from zero to position
n
.
What we want as our final output is to map that back to the vocab space.  We want logits:
a list of numbers that (after being run through softmax) will represent the probability that
our next token is a particular one.
Just as we mapped from vocab space to embedding space with (conceptually) a matrix
multiplication at the start of the process, we can map back with another one.
More specifically, if we treat the embedding matrix as having the same number of rows
as there are input tokens (which we'll call
d
vocab
) and columns as there
are embedding dimensions (
d
emb
), then the original vocab-space-to-embedding-space
matrix will have this shape:
d
vocab
×
d
emb
So it's projecting from a
d
vocab
-dimensional space to a
d
emb
-dimensional one.
Similarly, our matrix to do the projection at the end is just a matrix with the numbers of
rows and columns swapped around:
d
emb
×
d
vocab
...to do a projection in the other direction.
The trick with weight tying is to see that these two projections can
potentially
be
just the opposite of each other.  If we assume that the embedding space on the way in
to the LLM is essentially the same as the embedding space on the way out, then we
can use one projection to go into it from vocab space, and the opposite to go back.
The "opposite" in this case is the transpose -- that is, if we use
W
emb
for
our embedding matrix and
W
out
for the output one, we have:
W
out
=
W
emb
T
That means we can re-use all of the embedding parameters for the output projection matrix,
and fewer parameters means not only a smaller model, but hopefully faster training.
Sounds like a win!
But of course, there's no such thing as a free lunch.  By constraining the output head
to be the transpose of the input one, we're essentially enforcing that assumption above:
we're saying that the embedding space on the way out
must
be the same as the embedding
space on the way in.  That limits what the LLM can do -- if it were able to use
different embedding spaces at each end, it would have more flexibility, which might
help it learn to model things better.
That's the theory: what does it mean in practice?
The code
Let's take a quick look at the GPT-2 code -- just the
__init__
for the top level class:
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
self
.
pos_emb
=
nn
.
Embedding
(
cfg
[
"context_length"
],
cfg
[
"emb_dim"
])
self
.
drop_emb
=
nn
.
Dropout
(
cfg
[
"drop_rate"
])
self
.
trf_blocks
=
nn
.
Sequential
(
*
[
TransformersBlock
(
cfg
)
for
_
in
range
(
cfg
[
"n_layers"
])]
)
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
For our embedding layer, we use PyTorch's
nn.Embedding
class, and for the output head we use
nn.Linear
.
Now,
nn.Embedding
provides us with access to the underlying matrix with a
weight
field:
weight
(Tensor) -- the learnable weights of the module of shape (
num_embeddings
,
embedding_dim
)
  initialized from
𝒩
(
0
,
1
)
.
So, that's exactly the
d
vocab
×
d
emb
matrix that we'd expect --
it's the input dimension as the rows, and the output dimension as the columns.
If we look at
nn.Linear
, we see something very similar:
weight (torch.Tensor) – the learnable weights of the module of shape (
out_features
,
in_features
)
  The values are initialized from
𝒰
(
−
k
,
k
)
where
k
=
1
in_features
That's actually the other way around, output dimension as the rows and input as the
columns.  If you're wondering why, remember that
we transpose the weights matrix for a neural network before using it
.
But that's actually really convenient in our situation, because if we want to use
the same weights for both, they're already "compatible"!
And that means that adding weight tying to our code above is as simple as adding
two lines at the end:
if
cfg
.
get
(
"tie_weights"
,
False
):
self
.
out_head
.
weight
=
self
.
tok_emb
.
weight
For the model code, it literally is just that!  There is a tiny inefficiency in that PyTorch is going
to spend a bit of time initialising the weights in
self.out_head
to appropriately-sized
random values, only to have them all replaced -- but that actually works in our favour,
because it means that we'll use up the same amount of the random number stream when
creating the LLM in both the weight-tying and non-weight-tying cases, which is a bit
better for reproducibility.
There is one other change needed, though.  I ran a test train with that code, and
checkpointing failed like this:
[rank0]: RuntimeError:
[rank0]:             Some tensors share memory, this will lead to duplicate memory on disk and potential differences when loading them again: [{'tok_emb.weight', 'out_hea
d.weight'}].
[rank0]:             A potential way to correctly save your model is to use <!--CODE_BLOCK_9763-->.
[rank0]:             More information at https://huggingface.co/docs/safetensors/torch_shared_tensors
Safetensors
doesn't like it when
you reuse weights like we're doing here.  The good news is that
the help page the error links to
is exactly about this problem with weight tying, and the suggested
fix -- to replace
save_file
(
model
.
state_dict
(),
"model.safetensors"
)
...with
save_model
(
model
,
"model.safetensors"
)
...and similarly for loading -- appears to work fine.  Saving and loading checkpoints
works, and it's compatible with the old checkpoint files too.  So that's good news :-)
So, that's how we code it.  How much actual saving do we get in terms of the parameter
count by doing this?
The parameters
A quick-and-easy way to count the parameters is just to create an instance of the model and see:
In
[
1
]:
import
json
In
[
2
]:
from
gpt
import
GPTModel
In
[
3
]:
with
open
(
"runs/8xa100m40-baseline/model.json"
,
"r"
)
as
f
:
...
:
model_conf
=
json
.
load
(
f
)
...
:
In
[
4
]:
model
=
GPTModel
(
model_conf
)
In
[
5
]:
sum
(
p
.
numel
()
for
p
in
model
.
parameters
())
Out
[
5
]:
163009536
In
[
6
]:
with
open
(
"runs/8xa100m40-weight-tying/model.json"
,
"r"
)
as
f
:
...
:
model_conf
=
json
.
load
(
f
)
...
:
In
[
7
]:
model
=
GPTModel
(
model_conf
)
In
[
8
]:
sum
(
p
.
numel
()
for
p
in
model
.
parameters
())
Out
[
8
]:
124412160
So, we've gone from a 163M-parameter model to a 124M-parameter one.  That's certainly
quite some saving -- 38,597,376 fewer parameters, which is a reduction of almost a quarter.
We can also sanity check the size of that saving -- our output head was, as we know,
a
d
emb
×
d
vocab
matrix, so it should have
50257
×
768
parameters
-- which is, indeed, 38,597,376.  Excellent.
Now, there's one thing we should consider here.  We're training on a Chinchilla-optimal
number of tokens, 20x our parameter count.  Is that what we want to keep stable?  Or is
the total number of training tokens the important bit, so we wind up technically
overtraining?
My instinct is that the total training tokens is the important thing.  Chinchilla
optimality is a training heuristic rather than a true aspect of the model, so sticking
with it would mean that we're training a model with fewer parameters on less data.
It seems very unlikely that would do anything other than produce a worse model!
So: we'll keep the same number of training tokens, and just introduce weight tying.
How does it train?
The train
I kicked it off on the usual 8x A100 40 GiB machine, and after a little while I
checked the loss chart.  It looked like this:
Yikes!  It started off with a loss of about 460.  Normally, we start with a loss
of about 11.
The normal loss makes a lot of sense.  If you consider it in terms of perplexity,
that value of 11 comes out at
e
11
≈
59
,
874
-- that is, the model is giving pretty much equal
probabilities to every one of the 50,257 possible tokens.
A loss of 460 means that the model is making incorrect predictions and is very certain about them.
How could that be?  Well, let's look at the documentation again.
For
nn.Embedding
:
weight
(Tensor) -- the learnable weights of the module of shape (
num_embeddings
,
embedding_dim
)
  initialized from
𝒩
(
0
,
1
)
.
For
nn.Linear
:
weight (torch.Tensor) – the learnable weights of the module of shape (
out_features
,
in_features
)
  The values are initialized from
𝒰
(
−
k
,
k
)
where
k
=
1
in_features
They're initialised completely differently.  Embeddings are set to values in a normal
distribution (that is, a Gaussian bell curve) with a mean of 0 and a standard deviation
of 1.  But linear layers are set to random values in a uniform distribution (that is,
a completely flat one) within a range based on the number of input features.
In particular, those numbers for the linear layer are really small!  Our output head
has
in_features
set to 768, so that means that the
k
would
be:
1
768
≈
0.0360
So instead of getting that kind of "ideal" linear layer initialisation
within the range
(
−
0.0360
,
0.0360
)
, we're getting
numbers which roughly 2/3 of the time will be in the range
(
−
1
,
1
)
, and the
rest of the time will be even further from zero -- we could be getting -3 or +4, or
potentially even crazier numbers!
That means that the output logits (coming from a linear layer with higher weights)
will be larger, which in turn will push softmax to come up with higher probabilities:
In
[
1
]:
import
torch
In
[
2
]:
torch
.
softmax
(
torch
.
tensor
([
1.0
,
2.0
,
3.0
]),
dim
=
0
)
Out
[
2
]:
tensor
([
0.0900
,
0.2447
,
0.6652
])
In
[
3
]:
torch
.
softmax
(
torch
.
tensor
([
10.0
,
20.0
,
30.0
]),
dim
=
0
)
Out
[
3
]:
tensor
([
2.0611e-09
,
4.5398e-05
,
9.9995e-01
])
In
[
4
]:
torch
.
softmax
(
torch
.
tensor
([
100.0
,
200.0
,
300.0
]),
dim
=
0
)
Out
[
4
]:
tensor
([
0.0000e+00
,
3.7835e-44
,
1.0000e+00
])
I considered changing things to initialise the weights differently, but given that the
loss had fallen to 8 or so by the second checkpoint, I decided to just let the run
complete.  Here's the final loss chart, with the Y axis fixed to run from 0 to 12:
That's a nice smooth curve, at least!  The output is:
Training complete in 12,058.054 seconds
Tokens seen: 3,260,252,160
Throughput: 270,380 tokens/second
Final train loss: 3.952
Timing-wise, that's about 180 seconds faster than our baseline model training run,
only a 1.5% speedup
-- clearly the lower number of parameters doesn't actually save us much time.
Loss-wise, the final train loss on the baseline model was 3.743, so that's not
particularly promising.  Still, the proof is, as ever, in the evals.  Smoke test first:
Every effort moves you are making, the same as if there have been hundreds or thousands of miles of people getting in one
Borderline coherent, but maybe worse than normal?  Let's see what our test set loss
looks like.
Loss against our test dataset: 3.874
That's bad -- let's see it in our comparison table:
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
Our worst model so far :-(
Conclusion
Weight tying certainly didn't help our train.  It is worth noting that the GPT-2 small
weights -- which
do
use it -- got 3.500 on the same test set as we're using for that
table, so it is possible to get a better model with weight tying.  But there was
clearly something different about their train, and my suspicion, as I've said before,
is that it was trained for many more epochs (
I estimated 40
), slowly grinding that loss down.
But what I'm trying to do in this mini-series of interventions is find tricks that
will allow us to approach the original weights' loss without a very long training
run.  And for the purposes of that, I think we can safely say that weight-tying is
not one of those.
Next time around, our last intervention test!  What happens if we switch off the use
of automated mixed precision (AMP)?  That is something I added right back at the start
as a performance enhancement; it means that PyTorch can do certain calculations
in 16-bit rather than 32-bit if it thinks there's no harm in doing so.  Might we get
better loss by training without it?
Here's a link to the next post in this series
.
