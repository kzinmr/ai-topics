---
title: "Writing an LLM from scratch, part 34b -- from bigrams to GPT-2, one component at a time (in JAX)"
url: "https://www.gilesthomas.com/2026/07/llm-from-scratch-34b-building-and-training-gpt-2-small-in-jax"
fetched_at: 2026-07-09T07:01:31.529147+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Writing an LLM from scratch, part 34b -- from bigrams to GPT-2, one component at a time (in JAX)

Source: https://www.gilesthomas.com/2026/07/llm-from-scratch-34b-building-and-training-gpt-2-small-in-jax

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
This post is the capstone of
the most long-running series on my blog
.
In December 2024 (!), I started
reading
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
",
and worked through it carefully.  Being who I am, despite trying to apply a strict "no side quests"
policy, I found myself zooming off and digging into all kinds of things.
It's time to wrap it up.  I had decided that the endpoint would be to build and train an LLM from scratch just using my notes --
no reference to the book, no reference to the model code I'd written when following the book.
After an
X/Twitter
poll, I decided to
use JAX for that, just to make sure that I really was building it from scratch and
not regurgitating bits of PyTorch code like a bad coding LLM spitting out half-digested
lumps of Stack Overflow.
In my
last post
,
I showed how I built a JAX training script that mirrored what I had built for the original
PyTorch version of the model.  To test it as I went along, I used it to train a really dumb "LLM", which instead
of trying to predict the next token for every token in an input sequence, instead
predicted the input -- that is, if you fed it
The fat cat sat on the mat
It would return the same thing.  I called that an A-to-A model.
In this post, I'll show you how I turned it into a GPT-2 model, and then trained
it from scratch on my RTX 3090 (using the parameter counts for the original paper's "small" size).  What turned out
really well with this is that I found a route that meant that almost every component I added
made the model better!  That's not guaranteed -- sometimes different aspects of an AI model
depend on each other, so adding A without also adding B makes things worse.  But (admittedly
with a bit of backtracking in places) I was able to find a route that shows a nice clear progression.
The final training run took 37 hours 15 minutes -- compared to 40 hours, 38 minutes for
an equivalent PyTorch model
.
That is despite it being full-fat 32-bit -- the PyTorch one was using Automatic
Mixed Precision (AMP), which allowed it to use 16-bit calculations in places where it would
be relatively harmless in terms of loss.
When asked to continue "Every effort moves you", it came back with a decent response:
Every effort moves you closer to your goals, but if you are unsure of what it takes, you don’t
The model got 3.418784 loss on my held-back test dataset, as compared to my PyTorch
model's 3.538161, and even more impressively, it was better than the original GPT-2 small's
result of 3.499677 on the same dataset!  However, just as
I found previously
,
the OpenAI weights still beat mine consistently in instruction fine-tuning challenges.
Let's get started.
The starting point -- A-to-A
At the end of the last post, we had a solid training loop, using all of the tricks
I'd picked up with my PyTorch code.  The A-to-A model we were training with it looked
like this:
from
flax
import
nnx
class
GPTModel
(
nnx
.
Module
):
def
__init__
(
self
,
vocab_size
,
context_length
,
d_emb
,
n_heads
,
n_layers
,
qkv_bias
,
drop_rate
,
rngs
,
):
self
.
token_embedding
=
nnx
.
Embed
(
num_embeddings
=
vocab_size
,
features
=
d_emb
,
rngs
=
rngs
,
)
self
.
output_head
=
nnx
.
Linear
(
in_features
=
d_emb
,
out_features
=
vocab_size
,
use_bias
=
False
,
rngs
=
rngs
,
)
def
__call__
(
self
,
xs
):
input_embeddings
=
self
.
token_embedding
(
xs
)
return
self
.
output_head
(
input_embeddings
)
That was based on my preferred model of
how LLMs work
, where at the top level
for a model, we feed in a sequence of token IDs, then:
Firstly, we convert them into embeddings, so we get a sequence of vectors, one for each token.  We do this by
a lookup into a table, but we can see it conceptually as a projection via a matrix,
from vocab space (where a particular token ID is a one-hot vector) to
embedding space.
Next, we do the magic with our Transformers layers, getting embeddings for the next token.
After these layers, the embedding at position
n
in the output sequence is for the predicted token to
come after the token at position
n
in the input sequence, considering that
input token and all other tokens to its left.
Finally, we project those back from embedding space to logits, this time actually using a real
matrix (in the form of a linear layer), the output head.  The logits (after being run through
softmax) represent the probabilities for each token of it being the next one.
The A-to-A model basically skipped the second step completely: it would project to embedding space,
then immediately project back to vocab space -- and after training, it was pretty
good at mapping a sequence to itself.
One interesting question is, if we train the same code, but this time try to get it
to make next-token predictions, how good will it be at that?  Obviously it can't be
as good as a full LLM.  But there are correlations between tokens; full stops will
generally be followed by spaces, adjectives will normally be followed by other adjectives
or nouns (at least in English), and so on.  It would be kind of like the predictive
text systems on a phone, where (at least until recently) it would just use the last word you entered
to generate a list of possible next words to select from.
Old-school natural language processing has a name for this: bigrams.  The idea is that
you can work out statistically what the most common two-word pairs are, which allows you
to make a guess at a next word from a single one.  (There are also trigrams, where you
look at the last two words when predicting the next, then 4-grams, 5-grams, and so on.)
You'd build up a full probability table -- for every word in your vocab, you'd have
the probability of every word coming next.
So maybe even with that minimal model, we could get it to learn something similar to a set of token-level (rather than word-level) bigrams, which would
then get the loss down.  Obviously it wouldn't be as good as a full bigram table --
for our GPT-2 vocab size of 50,257, that would need
50
,
257
2
=
2
,
525
,
766
,
049
parameters -- but perhaps it could approximate one.
(For comparison, the model we're using has just an embedding table and an output head, each mapping between
50,257 dimensions and 768, so that's
2
×
50
,
257
×
768
≈
77
million
parameters
-- about 3% of the full table.)
An uninitialised model would (hopefully) have a loss of about
10.82, implying a
perplexity
equal to
the vocab size.  If we can train our dumb model to get better loss than that, then
we'd have the beginnings of an LLM.
That was a simple test to run.  In my training code, I had a dataset class that looked like this:
class
BigTrainDataset
:
def
__init__
(
self
,
all_tokens
,
seq_length
,
microbatch_size
):
self
.
xs
=
all_tokens
[:
-
1
]
.
reshape
(
-
1
,
microbatch_size
,
seq_length
)
self
.
ys
=
all_tokens
[:
-
1
]
.
reshape
(
-
1
,
microbatch_size
,
seq_length
)
def
__getitem__
(
self
,
ix
):
return
self
.
xs
[
ix
],
self
.
ys
[
ix
]
def
__len__
(
self
):
return
self
.
xs
.
shape
[
0
]
That is, the inputs, the
xs
, were the same as the targets, the
ys
.  If we fed it
The fat cat sat on the mat
...then we'd be training it to output exactly the same thing.
The modified version for a real LLM would involve feeding it something like this:
...and targeting this:
That's a simple change -- that
__init__
method became this:
self
.
xs
=
all_tokens
[:
-
1
]
.
reshape
(
-
1
,
microbatch_size
,
seq_length
)
self
.
ys
=
all_tokens
[
1
:]
.
reshape
(
-
1
,
microbatch_size
,
seq_length
)
I did that, and kicked it off to train on the 92,209,152 tokens that I was (somewhat
arbitrarily) using in the last post to test my training loop.  The loss chart looked like this:
That was pretty promising!  Loss came down from roughly 10.82 down to a fairly stable
6 or so by global step 768, and seemed to flatten out there.  It's possible that further
training could have got it down a bit more, but I decided (again, somewhat arbitrarily) to
use the average train loss in the checkpoint period ending at step 937 as my starting point.  If we could make changes
that reduced that, then we'd be moving forward.  For this model, that value was
5.909.
So, what were the changes we needed to make to change our bigram-style model to a real,
if small, LLM?
Building GPT-2: a checklist
Adapting from my
how LLMs work
post, a GPT-2-style LLM
looks like this.  We receive our sequence of token IDs, and then:
Convert them into embeddings.
✔ ️done
Add on position embeddings.
Run these embeddings through multiple successive Transformers blocks.
Layer normalisation
Project them back from embedding space to vocab space.
✔ ️done
Inside the Transformers blocks, we:
Take a copy of the input sequence of embeddings
Layer normalisation
Run multi-head attention
Add the copy back in so that the version that came out of MHA is something more like an "annotation" of the original
Take a second copy of that one
Layer normalisation again
Run it through a simple neural network
Add the results of that back in.
So that gave me the checklist; looking at it, the most tempting next step was
layer normalisation (henceforth LayerNorm).  It's used at the end of the core
loop, and then twice in the Transformers blocks.
What would happen if we coded it up, and then added it to the core only?
LayerNorm
The purpose of
LayerNorm
is to stabilise
training.  We constrain the values flowing through our model so that they have certain
statistical properties that tend to make the whole thing more trainable.
That would mean that if it did help with this model -- placed in between the embedding
layer at the start, and the output head at the end -- then we'd hope for loss to go down
faster, and ideally finish at a lower level.
Time to code it up!
NNX has its own LayerNorm implementation
,
of course (as does
PyTorch
),
but in the book, we implement it ourselves, and that felt like the correct path to
take.
Firstly, I implemented a dummy version:
class
LayerNorm
(
nnx
.
Module
):
def
__init__
(
self
):
...
def
__call__
(
self
,
xs
):
return
xs
...and updated the core
GPTModel
to create and call one:
class
GPTModel
(
nnx
.
Module
):
def
__init__
(
...
):
self
.
token_embedding
=
nnx
.
Embed
(
...
)
self
.
output_norm
=
LayerNorm
()
self
.
output_head
=
nnx
.
Linear
(
...
)
def
__call__
(
self
,
xs
):
input_embeddings
=
self
.
token_embedding
(
xs
)
normalised
=
self
.
output_norm
(
input_embeddings
)
return
self
.
output_head
(
normalised
)
And kicked off a training run for a few seconds just to make sure that it hadn't
broken anything and that loss dropped -- being my first NNX module-inside-a-module,
I worried that there might have been something non-intuitive that I had to do to get it
to work.  But everything seemed good -- loss was dropping, no errors.
So, following
the notes I made when I first learned about LayerNorm
,
I needed to make the values flowing through centred around zero by subtracting their
mean, and then scale them to have a variance of one by dividing by the standard
deviation (details in those notes).
The shape of the
xs
I had coming into my
LayerNorm
class's
_call
was this:
That was
(batch_size, seq_len, d_emb)
.  So we needed to do those operations strictly on the last axis,
manipulating each embedding independently.
JAX has a
std
function
and a
mean
one
,
both of which take an
axis
parameter.  The
Array
object repackaged those as
methods, which was convenient, so I did a first cut test like this:
class
LayerNorm
(
nnx
.
Module
):
def
__init__
(
self
):
...
def
__call__
(
self
,
xs
):
jax
.
debug
.
print
(
f
"
{
xs
.
shape
=}
"
)
means
=
xs
.
mean
(
axis
=-
1
)
jax
.
debug
.
print
(
f
"
{
means
.
shape
=}
"
)
stds
=
xs
.
std
(
axis
=-
1
)
jax
.
debug
.
print
(
f
"
{
stds
.
shape
=}
"
)
return
xs
That printed out these results:
xs.shape=(6, 1024, 768)
means.shape=(6, 1024)
stds.shape=(6, 1024)
...which looked plausible; one number for each embedding vector.  Could we
broadcast them across the array?
class
LayerNorm
(
nnx
.
Module
):
def
__init__
(
self
):
...
def
__call__
(
self
,
xs
):
jax
.
debug
.
print
(
f
"
{
xs
.
shape
=}
"
)
means
=
xs
.
mean
(
axis
=-
1
)
jax
.
debug
.
print
(
f
"
{
means
.
shape
=}
"
)
stds
=
xs
.
std
(
axis
=-
1
)
jax
.
debug
.
print
(
f
"
{
stds
.
shape
=}
"
)
normalized
=
(
xs
-
means
)
/
stds
jax
.
debug
.
print
(
f
"
{
normalized
.
shape
=}
"
)
return
normalized
This blew up:
ValueError: Incompatible shapes for broadcasting: shapes=[(6, 1024, 768), (6, 1024)]
Fair enough.  But
mean
and
std
have a
keepdims
kwarg that looked like it would help:
class
LayerNorm
(
nnx
.
Module
):
def
__init__
(
self
):
...
def
__call__
(
self
,
xs
):
jax
.
debug
.
print
(
f
"
{
xs
.
shape
=}
"
)
means
=
xs
.
mean
(
axis
=-
1
,
keepdims
=
True
)
jax
.
debug
.
print
(
f
"
{
means
.
shape
=}
"
)
stds
=
xs
.
std
(
axis
=-
1
,
keepdims
=
True
)
jax
.
debug
.
print
(
f
"
{
stds
.
shape
=}
"
)
normalized
=
(
xs
-
means
)
/
stds
jax
.
debug
.
print
(
f
"
{
normalized
.
shape
=}
"
)
return
normalized
...and it did!
xs.shape=(6, 1024, 768)
means.shape=(6, 1024, 1)
stds.shape=(6, 1024, 1)
normalized.shape=(6, 1024, 768)
Excellent.  So the next step was to see if that would work even slightly.  Interestingly
loss started off a bit higher at 11.29 after the first global step -- so adding in the
LayerNorm had actually made the model
worse
than it was -- but it seemed to be falling
rapidly.  Things weren't totally broken, at least.
But there was more to LayerNorm than just zeroing the mean and scaling to the variance;
we also needed to scale them up by a learnable amount, and then shift/bias them by adding
on a different trainable amount.  More precisely, both of those trainable amounts were
different for each of the (in this case) 768 embedding dimensions.
We needed two learnable vectors of length
d_emb
.  I hadn't noted it down at the
time but I figured (as it turned out, correctly) that a sensible starting point for
those values would be all-zero for the bias, and all-one for the scale.
From
this help page
,
the way you create a trainable array associated with an NNX module is this:
nnx
.
Param
(
jax
.
random
.
normal
(
rngs
.
param
(),
(
dim
,
dim
)))
That code created a random vector, rather than the zeros/ones we needed, and we'd need to get
the dimensions right.  Because of the "Incompatible shapes for broadcasting" error I'd
just had, I was feeling a bit paranoid about the latter, so I chose a shape of
(1, 1, d_emb)
, and
wrote this:
class
LayerNorm
(
nnx
.
Module
):
def
__init__
(
self
,
d_emb
):
self
.
scale
=
nnx
.
Param
(
jnp
.
ones
((
1
,
1
,
d_emb
)))
self
.
bias
=
nnx
.
Param
(
jnp
.
zeros
((
1
,
1
,
d_emb
)))
def
__call__
(
self
,
xs
):
jax
.
debug
.
print
(
f
"
{
xs
.
shape
=}
"
)
means
=
xs
.
mean
(
axis
=-
1
,
keepdims
=
True
)
jax
.
debug
.
print
(
f
"
{
means
.
shape
=}
"
)
stds
=
xs
.
std
(
axis
=-
1
,
keepdims
=
True
)
jax
.
debug
.
print
(
f
"
{
stds
.
shape
=}
"
)
normalized
=
(
xs
-
means
)
/
stds
jax
.
debug
.
print
(
f
"
{
normalized
.
shape
=}
"
)
scaled_and_biased
=
(
normalized
*
self
.
scale
)
+
self
.
bias
return
scaled_and_biased
That looked pretty plausible, though in retrospect I think I was being overly cautious
and didn't need the leading two axes for the scale and bias.
The only thing I was unsure about was whether the
nnx.Param
wrappers
I had put in were really making those arrays trainable.  I put some code in to print
them out and kicked off a run for a few minutes, and confirmed that they were
changing in ways that seem plausible -- small non-zero bias, scale close
to but not equal to one.  That was all good!
Next, I spotted one issue.  What if one of the standard deviations was zero?  That would
lead to a divide-by-zero error here:
normalized
=
(
xs
-
means
)
/
stds
Now, the standard deviation, if it's not zero, has to be positive --
so adding on a small value would fix that :
normalized
=
(
xs
-
means
)
/
(
stds
+
1e-5
)
With that in place, I felt that it was ready to go.  Time to do a full training
run!
I kicked that off, and it completed with this output:
2026-06-20 19:08:17.189721 Tokens seen: 92,209,152
2026-06-20 19:08:17.189724 Throughput: 95,383 tokens/second
2026-06-20 19:08:17.189734 Final train loss: 5.736
2026-06-20 19:08:17.189737 Done
Loss looked like this:
Let's look at the results for the previous run without LayerNorm for comparison:
You can see that the new run, the first one, drops faster.  It's harder to see from
the chart, but it also finished up with a lower training loss at 937 (my relatively
arbitrary metric): 5.734 rather than 5.909.
That was interesting!  The new model was basically doing the same thing -- predicting
the next token based only on the "current" token, but loss was lower.  My take is that
if we had trained the non-LayerNorm model for longer, it might have managed to eventually
grind out a better loss.  But LayerNorm was doing its job -- it was stabilising training,
and as a result we converged faster.
That was a win!  I decided to run it through my old smoke test from the PyTorch training runs, and see how it completed
"Every effort moves you":
Every effort moves you can be a few years.
-year-year-year-year-year-year-
It was kind of impressive that it managed to finish the first line before it got
stuck in a loop -- but it was understandable that we couldn't expect anything
good yet.  Each predicted token was based entirely on the token before it.
What next?  Back to our checklist:
Convert token IDs into embeddings.
✔ ️done
Add on position embeddings.
Run these embeddings through multiple successive Transformers blocks.
Layer normalisation
✔ ️done
Project them back from embedding space to vocab space.
✔ ️done
Inside the Transformers blocks, we:
Take a copy of the input sequence of embeddings
Layer normalisation
Run multi-head attention
Add the copy back in so that the version that came out of MHA is something more like an "annotation" of the original
Take a second copy of that one
Layer normalisation again
Run it through a simple neural network
Add the results of that back in.
So, at this stage, for each input token we were predicting the next one based on
the input token only -- like I said earlier, we were doing a somewhat roundabout
way of building an approximation of a table of bigram probabilities.  What would happen if we started
paying attention to the tokens to the left?  And what would be the simplest, dumbest
way to do that?
A single layer of single-head attention
The real LLM has multiple layers of multi-head attention, each one also having a
feed-forward network, some LayerNorms, and some shortcut connections.
Single-head attention is easier to code, but even on its own, you'd expect it to be
able to add some value.  Each token would get at least some information from the ones
to the left.  And one layer, likewise, you'd expect might help a bit.  I suspected
that it wouldn't work on its own -- I expected I'd need shortcut connections too --
but decided to start with attention on its own.
I modified the main class to have a single "Transformers" layer:
class
GPTModel
(
nnx
.
Module
):
def
__init__
(
...
):
self
.
token_embedding
=
nnx
.
Embed
(
...
)
self
.
transformers_layer
=
TransformersLayer
(
d_emb
,
qkv_bias
,
rngs
)
self
.
output_norm
=
LayerNorm
(
d_emb
)
self
.
output_head
=
nnx
.
Linear
(
...
)
def
__call__
(
self
,
xs
):
input_embeddings
=
self
.
token_embedding
(
xs
)
transformed
=
self
.
transformers_layer
(
input_embeddings
)
normalized
=
self
.
output_norm
(
transformed
)
return
self
.
output_head
(
normalized
)
...where that layer was actually just single-head attention:
class
TransformersLayer
(
nnx
.
Module
):
def
__init__
(
self
,
d_emb
,
qkv_bias
,
rngs
):
self
.
attention
=
Attention
(
d_emb
,
qkv_bias
,
rngs
)
def
__call__
(
self
,
xs
):
return
self
.
attention
(
xs
)
Next, it was time for the
Attention
class.
I'm not going to write yet another attention explainer -- I think my
"How do LLMs work?"
one does a decent job of that, and
"The 'why' of attention, or: attention heads are dumb"
works well too.  So in the next bit I'll assume that you understand the basics.
My first cut was basically just the maths (up to the causal mask) to get the
attention scores:
class
Attention
(
nnx
.
Module
):
def
__init__
(
self
,
d_emb
,
qkv_bias
,
rngs
):
self
.
d_emb
=
d_emb
self
.
W_q
=
nnx
.
Linear
(
d_emb
,
d_emb
,
use_bias
=
qkv_bias
,
rngs
=
rngs
)
self
.
W_k
=
nnx
.
Linear
(
d_emb
,
d_emb
,
use_bias
=
qkv_bias
,
rngs
=
rngs
)
self
.
W_v
=
nnx
.
Linear
(
d_emb
,
d_emb
,
use_bias
=
qkv_bias
,
rngs
=
rngs
)
def
__call__
(
self
,
xs
):
Q
=
self
.
W_q
(
xs
)
K
=
self
.
W_k
(
xs
)
V
=
self
.
W_v
(
xs
)
omega
=
Q
@
K
.
T
omega
/=
jnp
.
sqrt
(
self
.
d_emb
)
causal_omega
=
jnp
.
tril
(
omega
)
It did the projections into query, key and value space, worked out the attention
scores with the array multiplication, normalised it by dividing by the square root of the number of
dimensions in the Q-K embedding space, and then zeroed out the scores where a
token was attending to tokens in its "future".
There were a couple of problems, though.  Firstly, that wouldn't work if we were
working with batches, and secondly, zeroing out the non-causal scores wasn't quite
correct.
The batches first.  Our incoming
xs
here would have the shape
(batch_length, seq_len, d_emb)
.  After the projections to the Q-K embedding space,
both
Q
and
K
would also be shaped
(batch_length, seq_len, d_emb)
.  Now, the
.T
property on the JAX array class just reverses the axes, so the code above
would give us
K.T
with the shape
(d_emb, seq_len, batch_length)
.
That would break!  Matrix multiplication in JAX expects all but the last two
axes to represent batches, so we actually wanted
K.T
to have the shape
`
(batch_length, d_emb, seq_len)
.  That meant that what we actually
wanted was to just transpose the last two axes.
The JAX
transpose
function
takes
an
axes
parameter that allows you to specify the specific re-ordering of the input
axes that you want.  So I could rewrite the code like this:
def
__call__
(
self
,
xs
):
Q
=
self
.
W_q
(
xs
)
K
=
self
.
W_k
(
xs
)
V
=
self
.
W_v
(
xs
)
omega
=
Q
@
jnp
.
transpose
(
K
,
axes
=
(
0
,
2
,
1
))
omega
/=
jnp
.
sqrt
(
self
.
d_emb
)
causal_omega
=
jnp
.
tril
(
omega
)
As
Q
would have the shape
(batch_length, seq_len, d_emb)
, and the transposed
version of
K
would be
(batch_length, d_emb, seq_len)
, they'd be compatible for
matrix multiplication and give us a result that was
(batch_length, seq_len, seq_len)
-- just what we wanted for attention scores.
The next step was to fix the causal mask.  The next step in this
attention mechanism was going to be running the causal attention scores
in
causal_omega
through softmax over the last dimension, to convert them into
attention weights.  Now, our current code was zeroing out unwanted acausal scores,
but a zero still contributes to softmax.  If you want a particular value to come out of
softmax guaranteed to be zero, you need to set it to minus infinity.
I decided that the easiest way to do this was to create a causal mask -- a boolean
array that matched the size of
omega
, but was full of
True
s:
causal_mask
=
jnp
.
ones_like
(
omega
,
dtype
=
bool
)
Then I could zero out (well, "false out") the cells in the mask related to unwanted future-facing
scores, just like I was previously doing on the scores:
causal_mask
=
jnp
.
tril
(
causal_mask
)
...and then I could apply that mask to omega with
jnp.where
,
telling it to create a new array, taking the value from
omega
where the mask
had
True
, and
-jnp.inf
in places where it had
False
.
causal_omega
=
jnp
.
where
(
causal_mask
,
omega
,
-
jnp
.
inf
)
That seemed solid, so I just needed to run the result through
jax.nn.softmax
,
specifying that the last dimension was the one where it should apply the function,
and that would give me the attention weights:
attention_weights
=
jax
.
nn
.
softmax
(
causal_omega
,
axis
=-
1
)
Finally, I just needed to use those attention weights to get the attention output
by mixing in appropriate portions of the projection of the inputs into value space,
V
:
return
attention_weights
@
V
As
attention_weights
was shaped
(batch_length, seq_len, seq_len)
, and
V
(like
Q
and
K
) was shaped
(batch_length, seq_len, d_emb)
, the batch axes were at the
start where they belonged, and the matrix multiplication would work and return something
shaped
(batch_length, seq_len, d_emb)
.
With that, we were done!   The final single-head attention class looked like this:
class
Attention
(
nnx
.
Module
):
def
__init__
(
self
,
d_emb
,
qkv_bias
,
rngs
):
self
.
d_emb
=
d_emb
self
.
W_q
=
nnx
.
Linear
(
d_emb
,
d_emb
,
use_bias
=
qkv_bias
,
rngs
=
rngs
)
self
.
W_k
=
nnx
.
Linear
(
d_emb
,
d_emb
,
use_bias
=
qkv_bias
,
rngs
=
rngs
)
self
.
W_v
=
nnx
.
Linear
(
d_emb
,
d_emb
,
use_bias
=
qkv_bias
,
rngs
=
rngs
)
def
__call__
(
self
,
xs
):
Q
=
self
.
W_q
(
xs
)
K
=
self
.
W_k
(
xs
)
V
=
self
.
W_v
(
xs
)
omega
=
Q
@
jnp
.
transpose
(
K
,
axes
=
(
0
,
2
,
1
))
omega
/=
jnp
.
sqrt
(
self
.
d_emb
)
causal_mask
=
jnp
.
ones_like
(
omega
,
dtype
=
bool
)
causal_mask
=
jnp
.
tril
(
causal_mask
)
causal_omega
=
jnp
.
where
(
causal_mask
,
omega
,
-
jnp
.
inf
)
attention_weights
=
jax
.
nn
.
softmax
(
causal_omega
,
axis
=-
1
)
return
attention_weights
@
V
I kicked off a training run with that, and it did work, in that loss went down over
the course of the run -- but at the end of the run, the loss at step 937 was 5.934 --
significantly above the 5.734 I got on the previous run, with no attention.
But that made sense!  As I'd said earlier, I suspected that this wouldn't help if
we had no shortcut connection.
Intuitively, if you want to work out what token should be at position
n
+
1
, on average the
most important other token you need to know about is probably whichever one is at position
n
.
Knowing about the tokens at
n
−
1
,
n
−
2
, and so on, could well be helpful -- maybe
very
helpful -- but not at the cost of not knowing about the one at
n
.
Now, single attention heads are just simple pattern-matchers.  They can't learn complex
rules, it's only by working together -- "horizontally", in multi-head attention or "vertically"
across multiple layers -- that they can do complex things.
What we were asking this head to do was to learn some way of gathering information
about previous tokens, and also to keep the knowledge about the "current" one.  That's
a tall order for a dumb attention head!
In my mind, this is a large part of the benefit of shortcut connections.
They are often presented as a way to make sure that during training,
gradients flow smoothly from the output end of the model to the earlier layers.  But
I prefer to think of them as preserving the original embeddings, so that each layer doesn't
completely replace what came into it, but instead does something closer to adding on
its own notes -- like
scholars adding commentary to a core text in the Talmud
.
In the training run above, the attention head was trying to learn how to
preserve the meaning of the embedding it was working on, while also merging in
information from earlier ones.  If we added a shortcut connection, then it would
only have to do the second of those two jobs.
The code was simple: I updated the
TransformersLayer
module to do a shortcut
connection:
class
TransformersLayer
(
nnx
.
Module
):
def
__init__
(
self
,
d_emb
,
qkv_bias
,
rngs
):
self
.
attention
=
Attention
(
d_emb
,
qkv_bias
,
rngs
)
def
__call__
(
self
,
xs
):
shortcut
=
xs
att
=
self
.
attention
(
xs
)
return
shortcut
+
att
I kicked off a training run, and at the end it printed this:
2026-06-23 03:51:18.086097 Tokens seen: 92,209,152
2026-06-23 03:51:18.086099 Throughput: 90,442 tokens/second
2026-06-23 03:51:18.086108 Final train loss: 5.570
2026-06-23 03:51:18.086121 Done
The loss chart looked like this:
And, importantly, that training loss at step 937 which I was using as a metric was
5.553 -- a decent improvement over the previous best of 5.734.  Even a dumb single
attention head was able to do something useful, if it had a shortcut connection.
I decided to run another qualitative smoke test:
Every effort moves you can be able to get to get to get to get to get a lot of the way to get
I mean, it was repetitive, but it was actually getting noticeably closer to making
sense!
So that was excellent news.  What next?  Our checklist looked like this:
Convert token IDs into embeddings.
✔ ️done
Add on position embeddings.
Run these embeddings through multiple successive Transformers blocks.
part-done -- one layer only
Layer normalisation
✔ ️done
Project them back from embedding space to vocab space.
✔ ️done
Inside the Transformers blocks, we:
Take a copy of the input sequence of embeddings
✔ ️done
Layer normalisation
Run multi-head attention
part-done -- single-head attention only
Add the copy back in so that the version that came out of MHA is something more like an "annotation" of the original
✔ ️done
Take a second copy of that one
Layer normalisation again
Run it through a simple neural network
Add the results of that back in.
Now, our single attention layer was lacking something.  Without position embeddings,
that layer has no idea what order the tokens before the one it's looking at come in.
If it's considering the " cat" in
...it doesn't know if it's looking at "The fat cat" or "fat The cat".
Position embeddings are simple, and might help, so that was the next step.
Position embeddings
These were trivial to add.  We had this core code:
class
GPTModel
(
nnx
.
Module
):
def
__init__
(
...
):
self
.
token_embedding
=
nnx
.
Embed
(
...
)
self
.
transformers_layer
=
TransformersLayer
(
d_emb
,
qkv_bias
,
rngs
)
self
.
output_norm
=
LayerNorm
(
d_emb
)
self
.
output_head
=
nnx
.
Linear
(
...
)
def
__call__
(
self
,
xs
):
input_embeddings
=
self
.
token_embedding
(
xs
)
transformed
=
self
.
transformers_layer
(
input_embeddings
)
normalized
=
self
.
output_norm
(
transformed
)
return
self
.
output_head
(
normalized
)
So I just added a position encoding module in
__init__
:
self
.
position_embedding
=
nnx
.
Embed
(
num_embeddings
=
context_length
,
features
=
d_emb
,
rngs
=
rngs
,
)
...and mixed it in with the token embeddings to create new, improved
input_embeddings
to be used
in our "Transformers" layer:
token_embeddings
=
self
.
token_embedding
(
xs
)
b
,
n
=
xs
.
shape
position_embeddings
=
self
.
position_embedding
(
jnp
.
arange
(
n
))
input_embeddings
=
token_embeddings
+
position_embeddings
I kicked off a training run with that:
2026-06-23 04:44:44.759768 Tokens seen: 92,209,152
2026-06-23 04:44:44.759771 Throughput: 88,618 tokens/second
2026-06-23 04:44:44.759779 Final train loss: 5.386
2026-06-23 04:44:44.759781 Done
Pretty hard to distinguish from the previous one, but the metric I was tracking, that
loss at step 937, had improved again!  We were down to 5.354 from 5.553 :-)
A quick qualitative smoke test didn't show that improvement, though:
Every effort moves you can be able to get to get to get back to get back to get back to get back to
Pretty much indistinguishable to the previous one.  But still, Loss Number Went Down, and
that's what was important at this stage.
It was time to try the next step.  From the checklist:
Convert token IDs into embeddings.
✔ ️done
Add on position embeddings.
✔ ️done
Run these embeddings through multiple successive Transformers blocks.
part-done -- one layer only
Layer normalisation
✔ ️done
Project them back from embedding space to vocab space.
✔ ️done
Inside the Transformers blocks, we:
Take a copy of the input sequence of embeddings
✔ ️done
Layer normalisation
Run multi-head attention
part-done -- single-head attention only
Add the copy back in so that the version that came out of MHA is something more like an "annotation" of the original
✔ ️done
Take a second copy of that one
Layer normalisation again
Run it through a simple neural network
Add the results of that back in.
We had only one attention head right now.  Individually,
attention heads are dumb
,
so switching to multi-head attention seemed like a good thread to pull.
Multi-head attention
At this point, my single-head attention code looked like this:
Q
=
self
.
W_q
(
xs
)
K
=
self
.
W_k
(
xs
)
V
=
self
.
W_v
(
xs
)
omega
=
Q
@
jnp
.
transpose
(
K
,
axes
=
(
0
,
2
,
1
))
omega
/=
jnp
.
sqrt
(
self
.
d_emb
)
causal_mask
=
jnp
.
ones_like
(
omega
,
dtype
=
bool
)
causal_mask
=
jnp
.
tril
(
causal_mask
)
causal_omega
=
jnp
.
where
(
causal_mask
,
omega
,
-
jnp
.
inf
)
attention_weights
=
jax
.
nn
.
softmax
(
causal_omega
,
axis
=-
1
)
return
attention_weights
@
V
I decided to re-implement multi-head attention (which I'll call MHA from here onwards)
from first principles rather than working strictly
from my notes, and then to come back and check it.
If you're looking at your browser's scrollbar with horror ("
still
only
  50%?!") and really don't want to read a full derivation of MHA, you can
skip straight to the first complete version of the code
.
The point of MHA is that we're running multiple copies of the calculation above in
parallel -- let's pin down the name of the number of copies as
n_heads
.  Now,
we could naively implement it just by spinning off
n_heads
threads and running the
existing code in each, but that wouldn't really take advantage of the GPU's inherent
parallelism.
I felt that we could rely on the fact that JAX's matrix multiplications treat all but the
last two dimensions as "batches".  For example, if you have two arrays with shapes:
and
...then you can multiply them.  A
m
×
n
matrix multiplied by
a
n
×
p
one will be
m
×
p
, so you'll get something that is
The other dimensions (so long as they match) will essentially act as
an
a
×
b
×
c
×
.
.
.
×
l
batch.
Now, right now we were just using a single batch dimension.  Let's look at the core
multiplication in the attention mechanism, which works out
omega
, the attention scores.
I had this:
omega
=
Q
@
jnp
.
transpose
(
K
,
axes
=
(
0
,
2
,
1
))
Breaking that apart into two steps:
K_transpose
=
jnp
.
transpose
(
K
,
axes
=
(
0
,
2
,
1
))
omega
=
Q
@
K_transpose
We got
K
from this line:
Let's look at the shapes here.
xs
is our input embeddings for this layer; its
shape is
(batch_size, seq_len, d_emb)
.  Projecting it through
W_k
, which is
shaped
(d_emb, d_emb)
gives us a shape for
K
of
(batch_size, seq_len, d_emb)
again.
Q
, being a projection of
xs
through
W_q
, which is the same shape as
W_k
, will have
the same shape as
K
.
Now, that means that
K_transpose
is
(batch_size, d_emb, seq_len)
, and the calculation
...is doing a batched matrix multiplication getting us the
omega
that we want,
shaped
(batch_size, seq_len, seq_len)
.
But as I said above, there's no need to stop with just one batch dimension.  Let's say
that we have
n_heads
heads, and that they each work with embeddings sized
d_head
.
Imagine that we've already somehow done multiple projections into the key and query
spaces for each of our
n_heads
heads, and that the results have somehow been put
into arrays such that
Q
and
K
are shaped
(batch_size, n_heads, seq_len, d_head)
-- that is, we've gained an extra axis that keeps the projections for each head into its
query-key space separate.
We could use the fact that both of those two leading axes are basically just batch
dimensions, and the existing single matrix multiplication
will still work, with one tiny tweak: the current transpose is this:
K_transpose
=
jnp
.
transpose
(
K
,
axes
=
(
0
,
2
,
1
))
omega
=
Q
@
K_transpose
...to swap around the last two axes of a three-axis array.  With one extra batch
dimension, we'll need to take account of that and do this instead:
K_transpose
=
jnp
.
transpose
(
K
,
axes
=
(
0
,
1
,
3
,
2
))
omega
=
Q
@
K_transpose
That will be a multiplication of
Q
, shaped
(batch_size, n_heads, seq_len, d_head)
,
with
K_transpose
, shaped
(batch_size, n_heads, d_head, seq_len)
, which
gives us an
omega
of the right shape,
(batch_size, n_heads, seq_len, seq_len)
.
So, if we can start treating the heads as just another batch dimension, things seem
simpler, at least for the attention score calculation.
Let's continue down through the single-head code, and then come back later to how we might
get the inputs into that double-batched shape.
The next line after the
omega
calculation just scales the attention scores by
a scalar:
omega
/=
jnp
.
sqrt
(
self
.
d_emb
)
That looked fine, just a broadcast division-by-float.  We'd need to change that
self.d_emb
to be
d_head
in some manner, but that's all.
Next:
causal_mask
=
jnp
.
ones_like
(
omega
,
dtype
=
bool
)
The
jnp.ones_like
will give us an array that's
(batch_size, n_heads, seq_len, seq_len)
full of
True
s.  That seems reasonable.
The next step:
causal_mask
=
jnp
.
tril
(
causal_mask
)
What will that do?  Well, per
the
tril
documentation
:
When
m.ndim > 2
,
jnp.tril
operates batch-wise on the trailing axes.
...which sounded good.
batch_size
and
n_heads
would be treated as batch axes,
which meant that the next line:
causal_omega
=
jnp
.
where
(
causal_mask
,
omega
,
-
jnp
.
inf
)
...would work.  Likewise, with the next line:
attention_weights
=
jax
.
nn
.
softmax
(
causal_omega
,
axis
=-
1
)
...the axis to apply
softmax
to is explicitly stated as the last one, which is
what we wanted.
So at the end of all of those steps, we'd have
attention_weights
shaped
(batch_size, n_heads, seq_len, seq_len)
, where the last axis had been
softmaxed (softmaxxed?).
The next line looked a little trickier:
return
attention_weights
@
V
In the single-head version we had
attention_weights
of shape
(batch_size, seq_len, seq_len)
,
and V of shape
(batch_size, seq_len, d_emb)
, so multiplying them gives us
(batch_size, seq_len, d_emb)
In the new MHA code so far, we had our
attention_weights
shaped
(batch_size, n_heads, seq_len, seq_len)
.
So in order for the matrix multiplication to work, we'd need
V
to be shaped
(batch_size, n_heads, seq_len, d_head)
.  That would give us a result shaped
as
(batch_size, n_heads, seq_len, d_head)
.
And conveniently, we'd already decided that the correct shape for
Q
and for
K
was
(batch_size, n_heads, seq_len, d_head)
.  If we could use the same "magic" to
do the projection into value space -- that is, to get
V
such that the heads formed
a new batch-like axis like we had for
Q
and
K
-- then we'd be all set.
So, at that point, I'd worked out the core of MHA.  If we could get all of the
inputs into the shape
(batch_size, n_heads, seq_len, d_head)
, and somehow handle
an output of the shape
(batch_size, n_heads, seq_len, d_head)
, then we could use
MHA code something like this:
# Q and K are (batch_size, n_heads, len_sequence, d_head)
# We need to convert K to (batch_size, n_heads, d_head, len_sequence)
# and then we get omega (batch_size, n_heads, len_sequence, len_sequence)
omega
=
Q
@
jnp
.
transpose
(
K
,
axes
=
(
0
,
1
,
3
,
2
))
omega
/=
jnp
.
sqrt
(
self
.
d_head
)
causal_mask
=
jnp
.
ones_like
(
omega
,
dtype
=
bool
)
# tril treats all but the last two axes as batches so we're OK here.
causal_mask
=
jnp
.
tril
(
causal_mask
)
causal_omega
=
jnp
.
where
(
causal_mask
,
omega
,
-
jnp
.
inf
)
# last axis is still OK.
attention_weights
=
jax
.
nn
.
softmax
(
causal_omega
,
axis
=-
1
)
# attention_weights is (batch_size, n_heads, len_sequence, len_sequence)
# V is (batch_size, n_heads, len_sequence, d_head)
# So this will come out as (batch_size, n_heads, len_sequence, d_head)
weighted
=
attention_weights
@
V
The next question was, how do we get our inputs into that shape?  We could
run them all through separate per-head weights -- that is, have an array with one
per head, like
W_q[0]
,
W_k[0]
and
W_v[0]
for the first one.  But that, again,
felt like it would be failing to take advantage of the GPU properly.
The solution was to think of how matrix multiplications work.  If you multiply two
matrices,
X
·
Y
, the value in the result,
in row
r
, and column
c
, is the dot product of row
r
in
X
and column
c
in
Y
.
So, imagine if you wanted to multiply
X
by
n
different versions of
Y
, let's
call them
Y
0
,
Y
1
, and so on up to
Y
n
.  If you imagine a new matrix,
Y
all
,
which is basically all the
Y
x
s stacked side-by-side, then the dot-product understanding
of multiplication makes it pretty clear that if you did
X
·
Y
all
, you would get
the results of all of those separate multiplications, also stacked side-by-side.
I'll call that kind of matrix a "striped" one, for want of a better word.
Now, when we project our inputs into the embedding spaces used for attention, we have
code like this:
We've initialised the weights,
W_k
in this case, as an
nnx.Linear
, so what is
happening under the hood here is basically:
Q
=
xs
·
W
q
That is, it is just a matrix multiplication.
So if we imagine that
W_q
is one of those "striped" matrices, holding all of the
separate matrices to do the projections for all of the heads in a single one
shaped
(d_emb, n_heads * d_head)
, then we could stick with the current code --
the
Our input
xs
would be shaped
(batch_size, seq_len, d_emb)
, so the result would be
(batch_size, seq_len, n_heads * d_head)
, and would have the projections for each head in
the same vertical stripes as the separate heads' projection weights.
Now, like PyTorch, JAX allows you to
reshape
arrays.
You can take one axis of length (say)
m
×
n
, and split it into two of
lengths
m
and
n
respectively -- or, conversely, you can combine two axes of
length
m
and
n
to one of
m
×
n
.
If our data had the shape
(batch_size, seq_len, n_heads * d_head)
, we could reshape it like this:
Q
=
self
.
W_q
(
xs
)
.
reshape
((
batch_size
,
seq_len
,
n_heads
,
d_head
))
...and that would split things up.  So we'd have Q shaped as
(batch_size, seq_len, n_heads, d_head)
.
That's almost what we wanted!  We needed
(batch_size, n_heads, seq_len, d_head)
,
and a simple transpose could sort that out:
Q
=
jnp
.
transpose
(
self
.
W_q
(
xs
)
.
reshape
(
(
batch_size
,
seq_len
,
n_heads
,
self
.
d_head
)
),
(
0
,
2
,
1
,
3
)
)
Likewise for
K
and
V
, and that was our inputs sorted.
Moving on to the output; it came from this:
weighted
=
attention_weights
@
V
...and as we worked out above, it was shaped
(batch_size, n_heads, seq_len, d_head)
.
I remembered that we wanted to run that through a single linear layer to combine
all of the different heads' outputs into one.  It felt like the best way to do that
would be to get it back into a "striped" layout:
(batch_size, seq_len, n_heads * d_head)
.
This would be something like the inverse of the input-wrangling.
That would
need a reshape, but before I could do that, I'd need to get the axes that needed to be
merged next to each other.  If the input to the linear layer was going to be
(batch_size, seq_len, n_heads * d_head)
, we'd need to convert it
from
(batch_size, n_heads, seq_len, d_head)
to
(batch_size, seq_len, n_heads, d_head)
first:
jnp
.
transpose
(
weighted
,
(
0
,
2
,
1
,
3
))
... and then we could just reshape it to
batch_size, len_sequence, n_heads * d_head
:
striped_output
=
jnp
.
transpose
(
weighted
,
(
0
,
2
,
1
,
3
)
)
.
reshape
(
batch_size
,
len_sequence
,
self
.
n_heads
*
self
.
d_head
)
Finally, we could run it through a linear layer, with
in_features
set to
n_heads * d_head
,
and
out_features
set to
d_emb
.
I put that all together, and decided to throw something extra into the mix.  I remembered that
Raschka's code had various checks to make sure that
d_head * n_heads == d_emb
, which
seemed a little artificial -- I'd read that this was true of GPT-2, but wasn't a necessary
restriction for GPT-style models, which makes sense.  There's no obvious reason per se why
the heads' embedding dimensions should sum up to the higher-level embedding dimensions.
So I decided initially to just pass in
d_head
and
n_heads
to the constructor.  In my training script I could force them to match
the GPT-2 model, but if I wanted to use the code later for something different, I could vary
them.
Then I remembered that although the dimensionality of the embedding spaces for the
query and the key vectors have to match (because otherwise you can't multiply them
to work out attention scores with
Ω
=
Q
K
T
), the value vector's dimensionality
can in theory be different.  So I decided to break
d_head
into two separate
d_qk
and
d_v
parameters.
The result was this:
class
MultiHeadAttention
(
nnx
.
Module
):
def
__init__
(
self
,
d_emb
,
n_heads
,
d_qk
,
d_v
,
qkv_bias
,
rngs
):
self
.
n_heads
=
n_heads
self
.
d_qk
=
d_qk
self
.
d_v
=
d_v
self
.
W_q
=
nnx
.
Linear
(
d_emb
,
self
.
d_qk
*
n_heads
,
use_bias
=
qkv_bias
,
rngs
=
rngs
)
self
.
W_k
=
nnx
.
Linear
(
d_emb
,
self
.
d_qk
*
n_heads
,
use_bias
=
qkv_bias
,
rngs
=
rngs
)
self
.
W_v
=
nnx
.
Linear
(
d_emb
,
self
.
d_v
*
n_heads
,
use_bias
=
qkv_bias
,
rngs
=
rngs
)
self
.
output_projection
=
nnx
.
Linear
(
self
.
d_v
*
n_heads
,
d_emb
,
use_bias
=
False
,
rngs
=
rngs
)
def
__call__
(
self
,
xs
):
batch_size
,
len_sequence
,
d_emb
=
xs
.
shape
# For each of the below:
# * The initial linear layer projects them to
#   (batch_size, len_sequence, d_X * n_heads)
#   where X is qk or v as appropriate.
# * The reshape makes them (batch_size, len_sequence, n_heads, d_X)
# * The transpose makes them (batch_size, n_heads, len_sequence, d_X)
Q
=
jnp
.
transpose
(
self
.
W_q
(
xs
)
.
reshape
(
(
batch_size
,
len_sequence
,
self
.
n_heads
,
self
.
d_qk
)
),
(
0
,
2
,
1
,
3
)
)
K
=
jnp
.
transpose
(
self
.
W_k
(
xs
)
.
reshape
(
(
batch_size
,
len_sequence
,
self
.
n_heads
,
self
.
d_qk
)
),
(
0
,
2
,
1
,
3
)
)
V
=
jnp
.
transpose
(
self
.
W_v
(
xs
)
.
reshape
(
(
batch_size
,
len_sequence
,
self
.
n_heads
,
self
.
d_v
)
),
(
0
,
2
,
1
,
3
)
)
# Q and K are (batch_size, n_heads, len_sequence, d_qk) per above
# We need to convert K to (batch_size, n_heads, d_qk, len_sequence)
# and then we get omega (batch_size, n_heads, len_sequence, len_sequence)
omega
=
Q
@
jnp
.
transpose
(
K
,
axes
=
(
0
,
1
,
3
,
2
))
omega
/=
jnp
.
sqrt
(
self
.
d_qk
)
causal_mask
=
jnp
.
ones_like
(
omega
,
dtype
=
bool
)
# tril treats all but the last two axes as batches so we're OK here.
causal_mask
=
jnp
.
tril
(
causal_mask
)
causal_omega
=
jnp
.
where
(
causal_mask
,
omega
,
-
jnp
.
inf
)
# last axis is still OK.
attention_weights
=
jax
.
nn
.
softmax
(
causal_omega
,
axis
=-
1
)
# attention_weights is (batch_size, n_heads, len_sequence, len_sequence)
# V is (batch_size, n_heads, len_sequence, d_v)
# So this will come out as (batch_size, n_heads, len_sequence, d_v)
weighted
=
attention_weights
@
V
# Transpose to (batch_size, len_sequence, n_heads, d_v),
# then reshape to (batch_size, len_sequence, n_heads * d_v)
striped_output
=
jnp
.
transpose
(
weighted
,
(
0
,
2
,
1
,
3
)
)
.
reshape
(
batch_size
,
len_sequence
,
self
.
n_heads
*
self
.
d_v
)
# Final linear layer to combine
return
self
.
output_projection
(
striped_output
)
Unusually for a case where I went off the reservation like this, the whole thing
with the embedding space dimensionality didn't cause any problems at all!  But there
was one small bug in this code, which I didn't discover until later -- we'll come to
it by the end of the post.
At this point, I did another of my short training runs, and:
2026-06-23 17:51:32.094308 Tokens seen: 92,209,152
2026-06-23 17:51:32.094311 Throughput: 85,682 tokens/second
2026-06-23 17:51:32.094321 Final train loss: 5.358
2026-06-23 17:51:32.094323 Done
...with a loss chart that looked like this:
The training loss at the 937th global step was 5.336, only a tiny bit better than
the 5.354 with single-head attention.  That was quite possibly within the noise.
Even though (due to the
d_head * n_heads == d_emb
restriction I was enforcing in
my training script) the
W_q
,
W_k
, and
W_v
arrays were the same size, I was
creating that
output_projection
, which would consume randomness and make things
vary.
If I were doing a proper scientific experiment to see if a single layer of MHA
beat a single layer of single-head attention, I think I would have run both for
more steps to see if the difference became more pronounced later.
But for the purposes of this post, I decided to move on.  My checklist now looked like this:
Convert token IDs into embeddings.
✔ ️done
Add on position embeddings.
✔ ️done
Run these embeddings through multiple successive Transformers blocks.
part-done -- one layer only
Layer normalisation
✔ ️done
Project them back from embedding space to vocab space.
✔ ️done
Inside the Transformers blocks, we:
Take a copy of the input sequence of embeddings
✔ ️done
Layer normalisation
Run multi-head attention
✔ ️done
Add the copy back in so that the version that came out of MHA is something more like an "annotation" of the original
✔ ️done
Take a second copy of that one
Layer normalisation again
Run it through a simple neural network
Add the results of that back in.
Adding that simple neural network -- the FFN -- seemed like a good next step.
Adding the FFN to the Transformers block
The
feed forward network
is simple; you take the output of the MHA block, run it through a biased
linear layer to expand it from
d_emb
to
4 * d_emb
, then run it through the
GELU activation function, then shrink it back down to
d_emb
with another linear
layer.  I didn't really see any value in writing my own implementation of GELU,
given that even in the book we were just given code for an approximation to type
in.  So, using
jax.nn.gelu
, I
wrote this:
class
TransformersLayer
(
nnx
.
Module
):
def
__init__
(
self
,
d_emb
,
n_heads
,
d_qk
,
d_v
,
qkv_bias
,
rngs
):
self
.
attention
=
MultiHeadAttention
(
d_emb
,
n_heads
,
d_qk
,
d_v
,
qkv_bias
,
rngs
)
self
.
ffn
=
nnx
.
Sequential
(
nnx
.
Linear
(
in_features
=
d_emb
,
out_features
=
d_emb
*
4
,
use_bias
=
True
,
rngs
=
rngs
),
jax
.
nn
.
gelu
,
nnx
.
Linear
(
in_features
=
d_emb
*
4
,
out_features
=
d_emb
,
use_bias
=
True
,
rngs
=
rngs
),
)
def
__call__
(
self
,
xs
):
shortcut
=
xs
att
=
self
.
attention
(
xs
)
post_attention
=
shortcut
+
att
fed_forward
=
self
.
ffn
(
post_attention
)
return
fed_forward
+
post_attention
Note that I added in a shortcut connection around the FFN as well, so that it didn't
overwrite what was there, but only "added on its notes".
I kicked that off, and it ran for ten minutes or so, but then OOMed:
2026-06-23 18:20:01.376377 Saving checkpoint
51%|██████████████████████████████████████████████████████▊                                                    | 481/938 [10:20<11:47,  1.55s/it, loss=5.758, tps=76,185]W0623 18:20:12.602631 2860192 bfc_allocator.cc:514] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.93GiB (rounded to 3149744640)requested by op
If the cause is memory fragmentation maybe the environment variable 'TF_GPU_ALLOCATOR=cuda_malloc_async' will improve the situation.
Adding
TF_GPU_ALLOCATOR=cuda_malloc_async
didn't help.  I spent some time trying
to dig into what might be causing it, but eventually noticed something interesting:
in
nvtop
, the VRAM usage was consistently 75% throughout.
Now I knew that JAX pre-allocates 75% of VRAM when it starts up, but I'd been assuming
that it would try to grab more if it needed it.  It turned out I was wrong with that
assumption -- it grabs 75%, but that's all you ever get!
The solution turned out to be the
XLA_PYTHON_CLIENT_MEM_FRACTION
environment variable.
If you set that to, say,
0.90
, then JAX will pre-allocate 90% of the VRAM, and
you can use all of that.  (You can also make it allocate as-needed with
XLA_PYTHON_CLIENT_PREALLOCATE=false
, and there are various other settings you
can control with other environment variables on that linked page).
Anyway, setting it to
0.90
to grab 90% of VRAM worked, and I was able to get
a successful run:
2026-06-24 00:29:34.864880 Tokens seen: 92,209,152
2026-06-24 00:29:34.864882 Throughput: 77,596 tokens/second
2026-06-24 00:29:34.864900 Final train loss: 5.341
2026-06-24 00:29:34.864902 Done
The loss chart was this:
...and the training loss at global step 937 was 5.295, compared to the 5.336 from MHA alone.  Another
tiny improvement, another one that could have been in the noise.  Again, if I were
doing a proper experiment, I'd do a longer run, but for now, I decided to move on.
The checklist looked like this:
Convert token IDs into embeddings.
✔ ️done
Add on position embeddings.
✔ ️done
Run these embeddings through multiple successive Transformers blocks.
part-done -- one layer only
Layer normalisation
✔ ️done
Project them back from embedding space to vocab space.
✔ ️done
Inside the Transformers blocks, we:
Take a copy of the input sequence of embeddings
✔ ️done
Layer normalisation
Run multi-head attention
✔ ️done
Add the copy back in so that the version that came out of MHA is something more like an "annotation" of the original
✔ ️done
Take a second copy of that one
✔ ️done
Layer normalisation again
Run it through a simple neural network
✔ ️done
Add the results of that back in.
✔ ️done
Now, my gut instinct was that the layer normalisation inside the Transformers
blocks was of most value as a way of stabilising training over deep networks.  And
with one layer, it didn't seem like the right time to add it.  Instead, I decided
to add on multiple layers.
Multiple layers
For GPT-2 small, you have 12 layers.  That was already being passed in to my
GPTModel
's
__init__
method as
n_layers
, so I just replaced this:
self
.
transformers_layer
=
TransformersLayer
(
d_emb
,
n_heads
,
d_qk
,
d_v
,
qkv_bias
,
rngs
)
...with this:
self
.
transformers_layers
=
nnx
.
Sequential
(
*
(
TransformersLayer
(
d_emb
,
n_heads
,
d_qk
,
d_v
,
qkv_bias
,
rngs
)
for
_
in
range
(
n_layers
)
)
)
...and then just renamed it where it was called; this:
transformed
=
self
.
transformers_layer
(
input_embeddings
)
...became this:
transformed
=
self
.
transformers_layers
(
input_embeddings
)
I kicked it off, and it completed!  However, the loss chart was telling:
Ouch.  Loss started dropping quite nicely, but then things got out of control and
it settled down at a loss that was essentially that of a random model.  At step
937, we were at 10.75, so just a hair less than the 10.82 that randomly guessing next
tokens would give.
Well, LayerNorm is specifically meant to stabilise training, and the checklist looked like this:
Convert token IDs into embeddings.
✔ ️done
Add on position embeddings.
✔ ️done
Run these embeddings through multiple successive Transformers blocks.
✔ ️done
Layer normalisation
✔ ️done
Project them back from embedding space to vocab space.
✔ ️done
Inside the Transformers blocks, we:
Take a copy of the input sequence of embeddings
✔ ️done
Layer normalisation
Run multi-head attention
✔ ️done
Add the copy back in so that the version that came out of MHA is something more like an "annotation" of the original
✔ ️done
Take a second copy of that one
✔ ️done
Layer normalisation again
Run it through a simple neural network
✔ ️done
Add the results of that back in.
✔ ️done
...and the only remaining step was that LayerNorm in the Transformers blocks, so it was time to add it in!
Adding LayerNorm
As per the checklist, we do the LayerNorm after we've taken our copy for the shortcut
connection, just before MHA, and then likewise after the second shortcut copy, before
the FFN.  As I understand it, this was a GPT-2 innovation -- previously, people had
done normalisation after those steps, but this pre-norm setup turned out to work better.
The code changes were simple.  I added two
LayerNorm
modules to the
TransformersLayer
class, and then called them in the appropriate places (taking
the opportunity to tidy up the variable naming in the forward pass while I was there):
class
TransformersLayer
(
nnx
.
Module
):
def
__init__
(
self
,
d_emb
,
n_heads
,
d_qk
,
d_v
,
qkv_bias
,
rngs
):
self
.
attention_norm
=
LayerNorm
(
d_emb
)
self
.
attention
=
MultiHeadAttention
(
d_emb
,
n_heads
,
d_qk
,
d_v
,
qkv_bias
,
rngs
)
self
.
ffn_norm
=
LayerNorm
(
d_emb
)
self
.
ffn
=
nnx
.
Sequential
(
...
)
def
__call__
(
self
,
xs
):
shortcut
=
xs
xs
=
self
.
attention_norm
(
xs
)
xs
=
self
.
attention
(
xs
)
xs
=
xs
+
shortcut
shortcut
=
xs
xs
=
self
.
ffn_norm
(
xs
)
xs
=
self
.
ffn
(
xs
)
return
xs
+
shortcut
I kicked it off and ran it, and got these results:
2026-06-24 03:07:51.128966 Tokens seen: 92,209,152
2026-06-24 03:07:51.128969 Throughput: 23,399 tokens/second
2026-06-24 03:07:51.128979 Final train loss: 5.359
2026-06-24 03:07:51.128981 Done
That certainly looked much healthier!
However, when I looked at the loss at step 937, it was 5.311 -- a tiny bit higher
than the single-layer MHA example, which got 5.295.
I'd been willing to play a bit fast and loose with this loss number and allow myself
to accept a win when the loss went down a tiny bit, even if it was such a small
amount that it could have been within the noise.  But
increasing
loss -- even if
it could
also
be within the noise -- was a step too far.
I decided that in this specific case, I'd be strict and test the hypothesis that
longer training runs would demonstrate an improvement between one single layer without
pre-norm, and multiple layers with pre-norm.
I had to remember that these training runs would not be comparable with the earlier ones.
In the training script, I
had a learning rate schedule like this
:
That straight-line warmup period and the following cosine decay were 5% and 95% of the training
run respectively, which meant that (for example) global step 937 of the short runs we had
been doing would be at a completely different point in the schedule than the same step
would in these longer runs.
However, they would be comparable to each other, and that was what mattered.
After some humming and hawing, I decided that a full Chinchilla-optimal (for the
full model) training run over 3,260,190,720 tokens, rounded up to fit into a round
number of global steps, would be a nice experiment.  I
expected it to run comfortably overnight for the single-layer run, and take a bit less
than two days for the multi-layer one.  So I kicked off the first.
Just over 11 hours later:
2026-06-24 16:39:52.178045 Tokens seen: 3,260,252,160
2026-06-24 16:39:52.178049 Throughput: 81,733 tokens/second
2026-06-24 16:39:52.178058 Final train loss: 4.324
2026-06-24 16:39:52.178061 Done
Here's the loss chart:
The last checkpointing period in that run ended at global step 33,164, and the
training loss then was 4.165 -- indeed, it had been at around 4.17 for quite some
time, though the trend still seemed to be a tiny bit downward.
So then I kicked off a run of the full version -- multiple layers, with pre-norm
in the Transformers blocks.  Just over 37 hours later:
2026-06-26 06:55:39.956609 Tokens seen: 3,260,252,160
2026-06-26 06:55:39.956614 Throughput: 24,151 tokens/second
2026-06-26 06:55:39.956625 Final train loss: 3.637
2026-06-26 06:55:39.956629 Done
The "Final train loss" line at the end said it all, really!  But here's the loss chart:
...and the loss at step 33,164 was 3.399.  Definitely quite an improvement over the
4.165 that a single layer got.
Again, at some point I might do the equivalent tests for the earlier results where
improvements appear to be pretty much in the noise.  It would be good to be sure that
the changes really did have the impact I think they did.
But for now: our checklist was looking like this:
Convert token IDs into embeddings.
✔ ️done
Add on position embeddings.
✔ ️done
Run these embeddings through multiple successive Transformers blocks.
✔ ️done
Layer normalisation
✔ ️done
Project them back from embedding space to vocab space.
✔ ️done
Inside the Transformers blocks, we:
Take a copy of the input sequence of embeddings
✔ ️done
Layer normalisation
✔ ️done
Run multi-head attention
✔ ️done
Add the copy back in so that the version that came out of MHA is something more like an "annotation" of the original
✔ ️done
Take a second copy of that one
✔ ️done
Layer normalisation again
✔ ️done
Run it through a simple neural network
✔ ️done
Add the results of that back in.
✔ ️done
Everything was checked off.  So was this journey over?
Well, there was one thing that the original PyTorch code had that my new code didn't:
dropout.
Dropout
I'd found in my lengthy
interventions experiments
that
dropout seemed to make models worse.  It was, I felt, a smart idea back in the days
when people had little data and did multiple epochs, each sweeping over everything,
but it made less sense nowadays with single-epoch training runs over very large datasets.
(Though I do have
some intuitive ideas about why it could still help
.)
Still, it would be good to show that it harmed loss for this model as well.
Checking my notes, I found that there were four places where dropout was applied:
Once in the main body, just after we've worked out the embeddings.
Twice in the transformers block: once after attention (but before the
shortcut is mixed back in), and once after the FFN (ditto)
Inside multi-head attention, on the attention weights (
which surprised me
).
The changes are tiny and rather dotted around the
code, so rather than showing you isolated bits of code, if you'd like to see it you
can take a look at
the code at this point
and search for "dropout".
When I started running that, I got an error when saving the first checkpoint:
TypeError: JAX array with PRNGKey dtype cannot be converted to a NumPy array. Use jax.random.key_data(arr) if you wish to extract the underlying integer array.
This was happening deep inside the bowels of Safetensors, but it made a lot of sense.
The
nnx.Dropout
object needs to keep track of the state of the random number generator,
and that meant that the
to_flat_state
function that
I was using
might return a structure that had something that contained that state, and was not
compatible with Safetensors.
I decided that I'd cheat a little bit here.  If I skipped the dropout layers when
I saved my checkpoints, like this:
for
tuple_key
,
array
in
flat_state
:
key
=
"."
.
join
(
str
(
key
)
for
key
in
tuple_key
)
if
"dropout"
not
in
key
:
simple_dict
[
key
]
=
array
...then I'd be able to save them.  This would have a problem -- if I restarted from
a checkpoint, the dropout pattern after the restart would mirror the dropout pattern
from the start of the training run, because the random seed it started with would not
have come from the checkpoint, but just the initialisation code.
I felt that this would not have a serious impact, though, and given that I'd not had
to restart from checkpoints so far, I (wrongly, as it turned out) decided it wouldn't
matter.
I kicked off the run, and... after four hours, it OOMed.  I cursed, decided that I'd
nurse this run through anyway (despite my dropout checkpointing concerns), and kicked it off again.
Three hours later, it OOMed again.  I happened to be away from home at the time, logging in to
my machine remotely (thanks,
Tailscale
!), and
on looking at
nvtop
, I realised that the X window system on my machine was using a
gig or so of VRAM.
I was running the training run in a
tmux
session, which meant
that I could kill X and not lose state, so I did that, and adjusted the
XLA_PYTHON_CLIENT_MEM_FRACTION
environment variable I was using -- it had been
0.90, so I bumped it up to 0.95.  I kicked it off again, and...
2026-06-28 22:06:47.669676 Tokens seen: 2,640,052,224
2026-06-28 22:06:47.669683 Throughput: 23,019 tokens/second
2026-06-28 22:06:47.669691 Final train loss: 3.776
2026-06-28 22:06:47.669694 Done
Note that the tokens seen only relates to the period since the restart, which is why it was
lower.
One more loss chart:
...and the training loss at step 33,164 was 3.524, higher enough than the 3.399 I got
without dropout that I was comfortable that it wasn't in the noise.  That was very reassuring.
Once again, if this was a proper scientific experiment I'd fix the issue with saving
dropout, and run it completely from scratch -- or, at least, run it all the way through
from scratch without restarts, even
if I had to try several times to get it done.
But I don't think that "replaying" dropout would make the loss any worse.  And for this
experiment, I felt this was enough.
So: checklist complete.  GPT-2 model coded up.  It was time for some evals!
Evals, first try -- and fixing an MHA bug
I wanted to evaluate these models against the ones I got using the old PyTorch code:
specifically, the
last local training run
that used exactly the same training hyperparameters, and only differed in that
it was trained using AMP -- 32-bit floats in general, but using 16-bit where the
framework thought it would not be harmful.
In order to do
exactly
the same evals, I decided it would be easiest to write a
conversion script to take the Safetensors files written to my JAX checkpoints, and write
out new files that were compatible with the PyTorch model code -- then I'd be able to
use the original PyTorch eval code.  I
put something together
,
converted my last two models -- the full runs with and without dropout -- and tried to
load them up.
Unfortunately there was an error:
RuntimeError: Error(s) in loading state_dict for GPTModel:
Missing key(s) in state_dict: "trf_blocks.0.att.out_proj.bias", "trf_blocks.1.att.out_proj.bias", "trf_blocks.10.att.out_proj.bias", "trf_blocks.11.att.out_proj.bias", "trf_blocks.2.att.out_proj.bias", "trf_blocks.3.att.out_proj.bias", "trf_blocks.4.att.out_proj.bias", "trf_blocks.5.att.out_proj.bias", "trf_blocks.6.att.out_proj.bias", "trf_blocks.7.att.out_proj.bias", "trf_blocks.8.att.out_proj.bias", "trf_blocks.9.att.out_proj.bias"
You might remember that back when I went through multi-head attention, I mentioned
that I'd made a mistake.  Somehow, I'd misremembered, and thought that the output projection -- the one
that mixes together all of the different heads' outputs -- was a linear layer without
bias, despite
my original notes
being
perfectly clear that it
did
have bias.
The good news was that if I disabled bias in the PyTorch code, I could load the
safetensors files that I had.  So the two models I'd trained so far were not useless,
and could actually work as a kind of natural experiment into the benefits of having
that bias there.
But anyway, in order to do things properly, I was going to need to fix the bug and
train yet another model.
Adding bias to the MHA output projections
The fix was simple, I just replaced this (in
MultiHeadAttention
):
self
.
output_projection
=
nnx
.
Linear
(
self
.
d_v
*
n_heads
,
d_emb
,
use_bias
=
False
,
rngs
=
rngs
)
...with this:
self
.
output_projection
=
nnx
.
Linear
(
self
.
d_v
*
n_heads
,
d_emb
,
use_bias
=
True
,
rngs
=
rngs
)
Then it was time to kick off yet another training run.  After another 37 hours:
2026-07-05 10:09:22.147819 Tokens seen: 3,260,252,160
2026-07-05 10:09:22.147823 Throughput: 24,072 tokens/second
2026-07-05 10:09:22.147832 Final train loss: 3.650
2026-07-05 10:09:22.147834 Done
...with this loss chart:
...and the training loss at step 33,164 was 3.398 -- almost exactly the same as the
3.399 that I got in the no-dropout training run without MHA bias above!
Well, now it really was time for the evals.
Evals, take two
I updated
my conversion script
to handle the bias on the MHA output projections, and used it to convert the three
models -- the un-biased ones, with and without dropout, and the biased one, without -- to
the PyTorch format, then ran the loss test that I had been using to compare the old models
on each.
Here are the results, compared to the previous models, and OpenAI's:
Test loss
OpenAI weights: medium
3.231442
JAX, with MHA bias, no dropout
3.418784
JAX, no MHA bias, no dropout
3.420089
JAX, no MHA bias, with dropout
3.476802
OpenAI weights: small
3.499677
1xrtx3090-stacked-interventions
3.538161
8xa100m40-stacked-interventions-1
3.577761
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
Local FineWeb-Edu extended train
4.134991
Local FineWeb-Edu train
4.166892
That was a pretty amazing result -- I'd clearly proven that JAX trains much better
models than PyTorch!  3.5% better in the best case.
Well, OK, no.
My guess is that the difference was probably something
like better luck with the initial weights on the JAX side, plus
the improvement from not using AMP
.
Anyway, the important thing was that the JAX models were in the same kind of loss
range as the PyTorch ones -- and while a 3.5% improvement in loss was more variation
than I'd been expecting, it was definitely the right ballpark.
Now, one thing I had found in the past was that the OpenAI weights -- and some of
my own models, like the Fineweb-Edu ones -- were
consistently better
at an instruction fine-tuning test than their test loss scores would indicate.  Would that hold here?
The IFT eval code fine-tuned
each model on the
Alpaca
dataset until
validation loss started rising, then used the model prior to the start of the rise to
generate responses for a test set.  These were saved, and then run past an OpenAI model
so that they could be compared with each other:
You are judging the comparative capabilities of a number of different LLM
models.  They have been trained to follow instructions.

The input was this:

`
{input}
`

An example correct output is this:

`
{correct_output}
`

Please produce a score of between 0 and 100 for each model, and respond
with a JSON structure like this (note that the number of models may differ
from this example):

`
{
    "Model 1": {"score": XXX, "comments": "optional comments"},
    "Model 2": {"score": YYY, "comments": "optional comments"},
    "Model 3": {"score": ZZZ, "comments": "optional comments"}
}
`

...where the XXX, YYY and ZZZ are the scores for the respective models.
You can optionally add the "comments" field if you want to explain your
reasoning.

Here are the models' responses:

# Model 1

{model 1 response}


# Model 2

{model 2 response}


# Model 3

{model 3 response}
...with the model order randomly changed for each query to avoid any position bias.
The methodology seemed solid, but I was uncertain about the "train until loss starts rising", as
it meant that different models had wildly different amounts of fine-tuning -- between
two and seven epochs.
On the one hand it felt "unfair" to certain models that they'd get less training than
others.  On the other hand, if the less-trained models had been trained past the point
where their validation loss started rising, then assuming that loss would continue to
rise, further training would actually be a disadvantage rather than an advantage.
I decided to stick with the original plan, and train until validation loss started rising.  I did, however, switch the judge model
from the GPT 5.4 that I used in my last IFT test to GPT 5.5.  Here are the results:
Test loss
IFT epochs
IFT score
IFT rank
OpenAI weights: medium
3.231442
2
41.62
1
JAX, with MHA bias, no dropout
3.418784
4
19.25
4
JAX, no MHA bias, no dropout
3.420089
3
14.66
11
JAX, no MHA bias, with dropout
3.476802
4
12.94
15
OpenAI weights: small
3.499677
2
26.73
2
1xrtx3090-stacked-interventions
3.538161
4
17.79
6
8xa100m40-stacked-interventions-1
3.577761
4
10.29
16
Cloud FineWeb, 8x A100 40 GiB
3.673623
7
20.71
3
1xrtx3090-baseline
3.683835
6
15.11
9
8xa100m40-baseline
3.691526
4
14.74
10
Cloud FineWeb, 8x H100 80 GiB
3.724507
4
13.25
14
Cloud FineWeb, 8x A100 80 GiB
3.729900
4
14.50
12
Cloud FineWeb, 8x B200 160 GiB
3.771478
4
16.03
8
Local FineWeb train
3.943522
7
13.73
13
Local FineWeb-Edu extended train
4.134991
7
16.70
7
Local FineWeb-Edu train
4.166892
7
18.68
5
More interesting datapoints!  As before, you can see that low loss is not particularly
well-correlated with a high score on this instruction fine-tuning test.  The OpenAI weights
continue to lead the pack, and while one of our new JAX models did quite well, it's
still beaten by the Cloud FineWeb, 8x A100 40 GiB model.
But what was important here, just as with the loss, was that the new JAX models landed
in the same ballpark as the PyTorch ones.  They did, and so I could be confident that
they were doing essentially the same thing.
And that meant that, after 18 months, I had reached the end of my LLM from scratch
journey.
Conclusion
It's been
a long trek
.
I
started reading
"Build a Large Language Model (from Scratch)"
on 22 December 2024.  I was planning to breeze through over the Christmas break,
but somehow it morphed into being a curriculum onto which I could hang projects
to learn the fundamentals of LLMs, beyond what was in the book.
In May 2025, I had my first real conceptual breakthrough when I realised that
attention heads are (individually) dumb
,
and as I continued, the second big one came later on in the same month, when the concept of
embeddings as being
projections between vocab space and embedding space
(and the converse projection in the other direction that happens in the LLM's output head)
became clear.
In August I had the first moment where I felt that the standard teaching approach to
LLMs might not be the full story; shortcut connections are normally explained as
a way to fix vanishing gradients, while I felt that a better way to see them was a
way to allow attention and the FFN to "annotate" the existing information, similarly
to how Jewish scholars have
annotated the original text of the Talmud
.
(The results in this post seem to point in that direction, given how even a single
layer of attention was massively helped by adding them.)
By early December, I had essentially finished the book, and felt I wanted to try
to
train my first base model from scratch on my RTX 3090
.
It worked, and wasn't far off the quality of the original GPT-2 small.   I was really surprised
that I could do that with consumer hardware, and became interested (perhaps obsessively so)
with whether I could match OpenAI's weights.
In January 2026, I
trained a model using DDP on Lambda Labs
,
and then spent the following months training model after model, trying to work
out which interventions -- learning rate scheduling, gradient clipping, etc -- would
improve the loss.  I wrapped that up in
late April
,
with the interesting finding that although I'd been able to get the test loss pretty
low, that didn't seem to map cleanly to performance in my instruction fine-tuning
tests.  In other words, Loss Number Goes Down is an interesting technical game to play,
but doesn't cleanly map to real-world performance.
The final step was this post, and
the previous one
-- could I, using my notes, implement GPT-2 completely from scratch in JAX without referencing
the book?
And as you've read, the answer was a definite yes!
Of course, as with any long-running project, there are some loose ends -- from this
post alone, there's the interesting fact that JAX trained faster than PyTorch (perhaps
torch.compile
could close the gap?) and had a larger possible batch size for full-fat 32-bit.
And the fact that fixing the multi-head attention bias bug didn't seem to help with the
loss much was interesting too.
But those are really details, and there's so much beyond them to learn.  Longer-context LLMs: position embedding improvements like RoPE,
efficiency tricks like flash attention and attention variants like DSA.  Mixture
of experts models.  How do optimisers really work?  (
Do they work?
)
And plenty more.
So it's time to draw a line under this series, and start thinking about what comes next.
It's been a blast; if you've been reading along, I hope it's been as useful (and fun) to read as it was to
write.
And as always, comments, questions and corrections very welcome below.
