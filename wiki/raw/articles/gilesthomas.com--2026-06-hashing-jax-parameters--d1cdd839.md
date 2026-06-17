---
title: "Flax debugging: making a hash of things"
url: "https://www.gilesthomas.com/2026/06/hashing-jax-parameters"
fetched_at: 2026-06-17T07:01:20.351470+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Flax debugging: making a hash of things

Source: https://www.gilesthomas.com/2026/06/hashing-jax-parameters

Archives
Categories
Blogroll
Posted on 17
June 2026
in
AI
,
TIL
,
JAX
,
Python
I was debugging an issue with a JAX/Flax NNX training loop the other day, and found a neat
little trick to help debug it.  Specifically, I wanted to see if the issue
was with my model, my loss function, my optimiser settings, or the "plumbing" of the
training loop itself -- were gradients actually coming through and being applied to the parameters?
I could print out the loss and the gradients, but printing out the parameters to see
if they were changing was unhelpful -- any given update might only change a small number
of parameters, or might change them such a small amount that I'd not notice -- especially given
that the model had 77 million of them!
Let's take a look.
The world's worst LLM
I am building an LLM from scratch in JAX and Flax NNX, and at this stage I'm trying to
get the training loop right.  As a simple test, I've just implemented the "shell" of
the LLM -- the token embeddings on the input side, and the final linear layer for an
output head, wired directly together.  My plan was to train that so that given a sequence, instead of predicting
next tokens for each position, it would "predict" the sequence itself -- that is, I might
train it with the input
The fat cat sat on the mat
...and the target
The fat cat sat on the mat
...rather than the normal setup for an LLM, where you feed it
...and give it targets of
So, in LLM terms, I'd be training a model to project from vocab space to a learned embedding
space where each token had a distinct-enough embedding for the output head to be able
to reliably project back to logits in vocab space.  There's
a bit of background here if that was all Greek to you
.
Here's the core part of the code I was working with, the
train_step
function, which
seems to be the traditional JAX name for the JITted part of your code that does the
forward pass through the model, works out the gradients, and then applies them to update
the model:
@jax
.
jit
def
train_step
(
model
,
optimizer
,
inputs
,
targets
):
loss
,
grads
=
nnx
.
value_and_grad
(
calculate_loss
)(
model
,
inputs
,
targets
)
optimizer
.
update
(
model
,
grads
)
return
loss
I'd based it on the
"Basic Usage" example
that's
currently right there on the front page of the Flax site.  Seasoned Flax veterans will probably
spot the issue right away, but it wasn't obvious to me -- so it was time to dig in.
Dealing with loss
The problem was that loss was not dropping -- indeed, taken to two decimal places, it was stuck at 10.82. The digits
to the right of that changed for each batch, but the first four did not.  Now, this model was
using the GPT-2 tokeniser, and 10.82 is exactly the loss that you'd expect if the model
was essentially guessing randomly -- if you convert it to
perplexity
by
calculating
e
10.82
, you get about 50,011 -- which is very close to the GPT-2
vocab size of 50,257.  Perplexity is, loosely, the number of tokens that the model
was trying to choose between for a typical input -- so a perplexity equal to the vocab size
is what you'd expect of a random model that is getting it right about one in 50,257
times.
That said, getting that loss consistently was a solid validation of my loss function!
It's vanishingly unlikely that it would have been getting that specific number so consistently
if I'd made a mess of that.  The tiny variations I was seeing in the third and subsequent
decimal places would make sense, as they could easily be due to the variations in the
contents of the different batches.
Gradient descent into madness
So was it that the gradients were somehow zero, or NaNs, or something else that couldn't
be usefully applied to the model by the optimiser?  I printed them out in the
train_step
function (removing the
jit
decorator, as otherwise the
print
s would only get executed
in the initial JIT pass through the function to compile it -- not when it had actual data ).
The result was values like this:
State({
'output_head': {
'kernel': Param( # 38,597,376 (154.4 MB)
value=Array([[-2.6879393e-06, -1.2799728e-04,  2.6441864e-09, ...,
-1.0780521e-09, -1.9232946e-09,  1.2057198e-04],
[ 7.2428256e-06, -9.0873800e-05,  1.9621261e-08, ...,
1.9959407e-08,  2.0515712e-08, -1.1401048e-06],
[-2.4080187e-05,  1.0717572e-04, -4.7910085e-09, ...,
-7.3136892e-09, -5.4990306e-09,  1.4717734e-04],
...,
[ 1.9500087e-05,  1.4264552e-05, -3.0880422e-08, ...,
-3.0595814e-08, -3.7087858e-08, -1.2066610e-06],
[ 1.8085115e-05,  7.6247423e-05, -3.0720415e-08, ...,
-3.1052533e-08, -3.1693808e-08, -9.7857817e-05],
[ 5.2281484e-06, -1.4398852e-04,  6.2573882e-08, ...,
5.5977843e-08,  6.6571232e-08, -1.0639715e-05]], dtype=float32)
)
},
...
Those looked plausible enough -- pretty small, but not so tiny that I'd expect them
to have no effect at all with my learning rate of 0.0014.  It was time to dig into
the training loop's plumbing.
Plumbing the depths
The obvious suspect was the update step -- was that call to
optimizer.update
actually changing
the parameters at all?  Flax's NNX API is a bit odd compared to the normal
JAX functional way of doing things
.
In vanilla JAX code you would expect to do something like this to apply gradients:
new_parameters
=
jax
.
tree
.
map
(
lambda
p
,
g
:
p
-
g
*
learning_rate
,
old_parameters
,
grads
,
)
That is, you get the new parameters by applying a transformation to the old ones.
NNX, by contrast, is more PyTorch-flavoured.  It updates the parameters in-place,
using a function with a side effect of mutating one of its parameters:
optimizer
.
update
(
model
,
grads
)
...rather than something more functional like this imaginary API:
model
=
optimizer
.
apply
(
model
,
grads
)
I could easily imagine that I'd got something wrong that would break that in-place update, as it has
the feel of something that would have to be quite delicately implemented on top of a
functional system like JAX.
But how could I see whether the parameters were changing, when there were 77 million
of them and they would be being updated (based on gradients like -2.6879393e-06 and
a learning rate of 1.4e-3) in the ninth decimal place or beyond?  Printing the arrays out
was a non-starter!
Hashing it out
After a little thought, I realised that the solution was to use hashes.  Even tiny
changes in the parameters' values would change their hashes drastically.  So if the parameters
were not being updated, as I suspected, I'd see constant hashes.  If they were being updated,
even by a minuscule amount, then the hashes would change.
This GitHub discussion
pointed me
in the right direction: if I could get the parameters as pure JAX arrays, I could do this:
print
(
hash
(
np
.
asarray
(
some_array
)
.
tobytes
()))
...where
np
is just
numpy
.  That would produce a hash that was stable for the life of
this run -- the same parameters would always have the same hash, and different ones would
differ, just as we want.  It could vary from run to run (Python uses different hash seeds in
each new interpreter), but that wouldn't matter for
this kind of debugging.
I wasn't sure what the structure of my Flax model's parameters was, but printing them out
in the training loop told me:
Embed( # Param: 38,597,376 (154.4 MB)
embedding=Param( # 38,597,376 (154.4 MB)
value=Array(shape=(50257, 768), dtype=dtype('float32'))
),
...
)
Linear( # Param: 38,597,376 (154.4 MB)
kernel=Param( # 38,597,376 (154.4 MB)
value=Array(shape=(768, 50257), dtype=dtype('float32'))
),
...
)
So, guided by that, I added these lines to the training loop:
print
(
hash
(
np
.
asarray
(
model
.
token_embedding
.
embedding
.
value
)
.
tobytes
()))
print
(
hash
(
np
.
asarray
(
model
.
output_head
.
kernel
.
value
)
.
tobytes
()))
Obviously copying the arrays around and converting them like that would slow things
down, but for debugging purposes, it looked solid.
I kicked off the training loop, and the problem was clear:
0%|                         | 43/530640 [00:06<13:39:02, 10.80it/s, loss=10.824, tps=43,576]
5694185712877458479
-5759723708627894111
0%|                         | 43/530640 [00:06<13:39:02, 10.80it/s, loss=10.824, tps=43,897]
5694185712877458479
-5759723708627894111
...and so on.  The hashes were not changing, so the model's parameters were not being
updated, even by a tiny amount. Gotcha!
The problem turned out, as I had suspected, to be related to the in-place updates that
NNX does.  Like I said earlier, I'd based my training loop on the "Basic Usage" example on the Flax site --
but I'd messed up one important thing.  I had this:
@jax
.
jit
def
train_step
(
model
,
optimizer
,
inputs
,
targets
):
loss
,
grads
=
nnx
.
value_and_grad
(
calculate_loss
)(
model
,
inputs
,
targets
)
optimizer
.
update
(
model
,
grads
)
return
loss
...and they had this:
@nnx
.
jit
# automatic state propagation
def
train_step
(
model
,
optimizer
,
x
,
y
):
loss_fn
=
lambda
model
:
((
model
(
x
)
-
y
)
**
2
)
.
mean
()
loss
,
grads
=
nnx
.
value_and_grad
(
loss_fn
)(
model
)
optimizer
.
update
(
model
,
grads
)
# in-place updates
return
loss
You can see a number of differences -- for example, they're baking the inputs and targets into
the lambda they're using for the loss function through a lexical closure, and that means
that they're only passing in the model to the version of it wrapped in
value_and_grad
.  But
none of that matters!   The real difference is actually nicely highlighted with a comment,
but I'd completely managed to miss it.  Right at the start, where I had
@jax.jit
, they had this:
@nnx
.
jit
# automatic state propagation
It 100% makes sense that in order to support this kind of non-functional, in-place
updating of the model's parameters, you have to have a modified version of the JIT
decorator.  And I was just using the standard, functional pure-JAX one.
Fixing that fixed the problem:
0%|                         | 1/530640 [00:06<903:18:25,  6.13s/it, loss=10.824, tps=1,003]
5024998356359528747
-4835662927486742764
0%|                         | 2/530640 [00:06<397:16:33,  2.70s/it, loss=10.785, tps=1,914]
6231090084827524676
8293831317336780907
0%|                         | 3/530640 [00:06<228:14:32,  1.55s/it, loss=10.741, tps=2,791]
7896237091035346857
-7117477486466304738
The hashes were changing!  And even better, if you scroll to the right you'll see
that loss was slowly dropping.  After 10k or so iterations, I was seeing 0.000: I had my do-nothing "LLM"
working.
Wrapping up
A satisfying debugging journey -- and while I don't think I'll make this specific
mistake in the future, I think that the parameter-hashing trick is actually a really useful
trick for the toolbox.  If you're uncertain as to whether your parameters are being
updated, just looking at them probably won't help.  But looking at their hashes can help
you find out whether anything is changing.
And I think that the pattern that I used to zoom in on it is a useful one, too.  I always
track loss, so it's a good starting point (indeed, seeing that it wasn't falling was what
told me that something was going wrong).  But checking that it has a sane -- or ideally, as
in this case, a meaningful -- value is a nice sanity check that we have a working loss function
and a model that isn't doing something completely pathological.  Moving on from there to
checking that some kind of gradients are flowing through is a solid next move (and might
become increasingly interesting with deeper models where
they can vanish or explode
).
Then finally we can check the parameters -- in particular, are they changing?
Let's see how many new tricks I pick up as I work through this LLM project.
