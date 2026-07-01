---
title: "Writing an LLM from scratch, part 34a -- building a JAX training loop for an LLM training run"
url: "https://www.gilesthomas.com/2026/06/llm-from-scratch-34a-building-a-jax-training-loop-for-an-llm-training-run"
fetched_at: 2026-07-01T07:00:53.564700+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Writing an LLM from scratch, part 34a -- building a JAX training loop for an LLM training run

Source: https://www.gilesthomas.com/2026/06/llm-from-scratch-34a-building-a-jax-training-loop-for-an-llm-training-run

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
For over a year, I've been using
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
" --
and the multitude of side-projects that have branched out from reading it -- as
something like a curriculum for learning about modern AI.  The one final task
I had set myself was to build and train an LLM from scratch just using my notes --
no reference to the book, no reference to the model code I'd written following the book.
As an output, I wanted something as good as my best PyTorch model based on Raschka's
code -- a base model, trained on 3.2B tokens, that my (admittedly limited) evals
ranked as being close to the original GPT-2 small's quality.
I wanted to use a different framework, just to make sure I wasn't parroting code that I'd
somehow memorised, so I
asked people on Twitter
which
one I should use, and the winner was
JAX
.
I took a slightly different route to Raschka's book;
he takes an inside-out perspective, explaining things like attention, gradually building
up a complete GPT-2-style model, and then building
a training loop on top of it.  I wanted to go
outside-in: I'd put together a training harness to train the simplest-possible
model with an API similar to a real LLM, get that working to my satisfaction, and then
add features to that simple model, one by one, until it had the full architecture in place.
The plan (which actually worked out nicely!) was that I'd be able to show
how each change improved things.
That's all done now, and I'm posting about it in two parts; in this one, I'll explain
how I built the training harness, and in the next, I'll show the actual building and
training of the LLM.
So let's get started!
Which framework on top of JAX?
JAX itself has a relatively minimal API, and doesn't include standard
neural network components like linear layers.  Likewise it doesn't have any built-in
optimisers, data loaders or similar ML utilities.
Now, I could have decided to build my LLM using just pure JAX, like
I previously did with a toy XOR model
.  But
I felt that it would be better to build this in the style that real-world JAX code
is written, which would mean using some of the
many utility libraries
.
On the JAX site itself, there was a useful-looking link:
"If you’re looking to use JAX to train neural networks, check out the
JAX AI Stack
!"
On the linked page, it made it clear that the two core parts of that stack were:
I took a look at both, and they seemed pretty easy to grasp.
Indeed, at first glance, I felt that NNX looked pretty PyTorch-like!  In their tutorial
example, the only real obvious difference
was the JAX-y derivative-style gradient calculation and the way that random numbers were
handled.  And even the random numbers were handled in a less pure-functional way
than pure JAX -- instead of having to mess around with splitting keys, you could just
pass in what appeared to be a stateful variable that somehow split itself internally
as needed.
So, NNX and Optax were the frameworks I'd use.  Rather than grinding through the
tutorials, I decided that I'd just dive right in, and try to pick things up as I went
along.
How hard could it be...?
The A-to-A language model and the training loop
To build a functioning training loop, I needed a minimal model to train -- not an
actual LLM, but something that behaved at least a bit like one.  It would take in
a sequence of tokens, and spit out logits for each token.
In my preferred model of
how LLMs work
, at the top level
for a model, we feed in a sequence of token IDs, then:
Firstly, we convert them into embeddings, so we get a series of vectors.  We do this by
a lookup into a table, but we can see it conceptually as a projection via a matrix,
from vocab space (where a particular token ID is a one-hot vector) to an
embedding space.
Next, we do the magic with our Transformers layers, getting embeddings for the next token.
The embedding at position
n
in the output sequence, after these layers, is for the predicted token to
come after the token at position
n
in the input sequence, considering that
input token and all other tokens to its left.
Finally, we project those back from embedding space to logits, this time actually using a real
matrix (in the form of a linear layer).  The logits (after being run through
softmax) represent the probabilities for each token of it being the next one.
All of that suggested to me that the dumbest "LLM" I could write just to get started
would be one that just projected token IDs into embedding space, and then projected
back to vocab space.  No Transformer layers at all.
I'd then train it so that instead of trying to predict the next token, it would
try to "predict" what was fed into it in the first place.  In other words, you'd feed
the training loop this input:
The fat cat sat on the mat
...and this target
The fat cat sat on the mat
...rather than the normal setup for an LLM, where you feed it
...and give it targets of
If I could get that to work -- and it felt like the kind of thing where you'd be able
to get the loss down to near-zero without a huge amount of training -- then I could be
reasonably sure that I had a working training loop.
I decided to call this an A-to-A model.
Coding up the model itself was ridiculously simple: it looked like this:
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
emb_dim
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
emb_dim
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
emb_dim
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
There's as much boilerplate in there -- for the parameters that I knew that the model
would need when I built out the full LLM -- as there is actual code doing stuff!
But the training loop was a bit more fun.
Porting over the basics
As I said, my plan here was to make sure my understanding of the internals of LLMs
was correct by rebuilding one just from my notes.  That "notes only" restriction
didn't apply to the training loop itself, so I allowed myself to crib a bit from
the PyTorch
DistributedDataParallel code
that I'd been using to train the original model in the cloud.
The first version that I used is
here
.
Let's start at the bottom, where we have
the
main
function
.
It starts with some boilerplate to handle the concept of "runs".  This is a pattern
I've found myself using in most of my projects.  When working on a model, it's useful to
be able to do multiple training runs, changing things each time.  You want to keep the checkpoints,
metadata and training charts for each one for future reference.
So in my repo, I'll
have a "runs" directory, and in there subdirectories for each training run I want to track.
In those subdirectories, there are JSON files -- one to configure the model,
model.json
,
and one to configure the training hyperparameters and similar stuff,
train.json
.
(It's worth noting that at this stage, a bunch of those hyperparameters were unused;
I kept them in there out of laziness, as I knew I'd need them later.)
So we start our
main
function by loading those.
Our next step is to completely ignore one of the training
hyperparameters,
gradient_accumulation_steps
.  I definitely wanted to do
gradient accumulation
,
but decided to leave it for later.  Better to get a solid, simpler training
run done first, I felt.
Next, we download the dataset we're going to use to our local disk with
download_dataset
(which will only download if there's not an up-to-date copy already there).
The next step is to call
load_dataset
to load it into RAM.  You can see that there's
another hard-coded variable there,
world_size
.  This is a holdover from the multi-GPU
DistributedDataParallel code that this was all based on; in this blog post I'm only
covering the code for single-GPU training, but I decided to leave the DDP stuff in there
for dataset-wrangling purposes, hardcoded
to one GPU, so that it would be easier to re-introduce if I later decide to implement
something similar in JAX.
Let's take a look at
load_dataset
and its related stuff.
If you go up to
line 39
you'll see the code.  Firstly, there's a
BigTrainDataset
that keeps track of our
training data.  If you look closely, you might spot one oddity in that class.  We have this:
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
Remember that at this stage, the plan was to train the model to map tokens to themselves
rather than to make next-token predictions.  So the targets are the same as the inputs, not
the more normal next token, which would look like (and, in the next post, will look like) this:
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
Next, we have a
load_dataset
function to load the appropriate subset of
the data from the copy on the local disk
into one of those
BigTrainDataset
objects.
I hit an out-of-memory issue when I ran the first version of this.
It was trying to load the data into my GPU's VRAM -- JAX's default behaviour if you
have a GPU, and the CUDA version of JAX is installed -- and there was too much to fit in there.
After a bit of digging around
I learned how to change the JAX default device
so that it would be loaded into normal system RAM.
Unfortunately, once I'd done that, I found that iterating through it was super-slow --
it took about 1.2 seconds to get one training batch of 6,144 tokens out of the array,
which meant that I'd have a limit of 5,120 tokens/second of training from that alone.
I eventually learned that the data had been loaded into the main RAM, but was being
copied up to the GPU for processing because it had not been
committed
to the main RAM --
details here
.  Fixing that (with an explicit
call to
jax.device_put
) meant that getting a single training batch from the dataset
and putting it onto the GPU took less than 0.001s, which was much better.
So that was many hours of work that all got packed into lines 55 to 58 of the code:
cpu0
=
jax
.
devices
(
"cpu"
)[
0
]
with
jax
.
default_device
(
cpu0
):
full_dataset
=
load_file
(
dataset_dir
/
f
"
{
split
}
.safetensors"
)[
"tokens"
]
full_dataset
=
jax
.
device_put
(
full_dataset
,
cpu0
)
The remainder of the logic in
load_dataset
is just to make sure that we have a
dataset that is exactly the right size for the world size (even though that's always
one right now), the microbatch size, the gradient accumulation steps, and the sequence
length that we're working with,
Let's
go back to the
main
function
again.  Having loaded our dataset, we create our model, passing in the model configuration
stuff and also the (currently unused) dropout rate training hyperparameter, then we create a Flax NNX optimiser which
wraps an Optax one.  This was essentially a copy/paste from the Flax tutorial,
except we're configuring the optimiser with learning rate and weight decay
hyperparameters from the training config:
optimizer
=
nnx
.
Optimizer
(
model
,
optax
.
adamw
(
learning_rate
=
train_conf
[
"learning_rate"
],
weight_decay
=
train_conf
[
"weight_decay"
],
),
wrt
=
nnx
.
Param
)
Finally, we call
train
to kick off our training loop, passing in some appropriate stuff.  Let's
go to that function
next.
We start off with a bit of housekeeping, then go into the main loop.  You can see
that it's kind of gesturing at gradient accumulation:
for
global_step
in
progress_bar
:
for
accumulation_step
in
range
(
gradient_accumulation_steps
):
...but if you look at the actual body of that loop, it's not doing anything of the
sort.  It's just getting training batches, putting them on the GPU, doing a full
training step, and keeping track of some metrics:
inputs
,
targets
=
train_dataset
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
inputs
=
jax
.
device_put
(
inputs
,
model_device
)
targets
=
jax
.
device_put
(
targets
,
model_device
)
train_loss
=
train_step
(
model
,
optimizer
,
inputs
,
targets
)
train_losses
.
append
(
train_loss
.
item
())
microbatch_size
,
sequence_length
=
inputs
.
shape
tokens_seen_this_rank
+=
microbatch_size
*
sequence_length
So, we're just doing a traditional batch-by-batch training loop without gradient
accumulation right now.  But some of the infrastructure is there, because it was
the next thing I wanted to add after I'd got the basic loop working.
The rest of the
train
function is just housekeeping and checkpointing; we'll come back
to the checkpointing shortly, but first let's take a look at the
train_step
function
that actually trains the model on a set of inputs and targets, and its associated
calculate_loss
function -- they're
just above
train
.
Now, as you might remember from
my first JAX post
,
the best way to JIT a training loop
is at as high a level as possible.  So when I first coded this, I integrated that into the traditionally-named
train_step
function like this:
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
When I actually came around to run it the first time, loss wasn't falling at all,
and after banging my head against it for a while, I
realised I should have used
nnx.jit
rather than
jax.jit
,
fixed that,
and kicked it off again.  Loss started falling immediately.  D'oh!
Now let's take a look at loss.
Cross entropy loss
was clearly what I would need to train an LLM, and also felt like the right thing for the
A-to-A model.
Optax has five loss functions that are related to cross entropy; three of them looked
a bit more complicated than I needed:
poly_loss_cross_entropy
,
safe_softmax_cross_entropy
, and
sigmoid_binary_cross_entropy
.
So it was a choice between
The latter was the right one --
softmax_cross_entropy
expects the labels (that is,
the target token IDs) to be
one-hot vectors, while
softmax_cross_entropy_with_integer_labels
, as it says in
the function name, expects integer labels, which is what we have.
That sounded pretty similar to PyTorch's
cross_entropy
,
but there was an important difference.  For normal use (if you're not using K-dimensional
loss, whatever that might be) PyTorch expects that the inputs are either just a one-dimensional
tensor of
c
logits, or at worst a
b
x
c
matrix, where
b
is the batch size.
I had noted when working through this section of Raschka's book that the
code we wrote flattened things out.  So a batch of six sequences, each
1,024 tokens long, with a vocab size of 50,257, would give us a logits tensor
shaped like this:
The first axis is the batches, the second is the length of the sequences -- remember,
we have logits for every input token in the sequence, with next-token predictions
for that token in the context of all of the other ones to its left.  And the last
axis, with a size equal to our tokeniser's vocabulary size, is the logits themselves.
After flattening, it looked like a "batch" of
6
*
1024
=
6144
logits
vectors:
Likewise our targets -- the token IDs we wanted our model to be predicting --
were batched, and there was one per token in each sequence, so that tensor was
Flattened, it looked like a "batch" of
6
*
1024
=
6144
targets:
Finally, the PyTorch function returned a scalar value -- wrapped in a PyTorch
Tensor
object,
of course, so that it could participate in the backward pass, but a single number.
But I'd forgotten about all of that when I was writing this part of the JAX code, and just fed
the inputs and the targets straight in to the JAX function.  The result was
interesting.  I started with this:
loss
=
optax
.
losses
.
softmax_cross_entropy_with_integer_labels
(
logits
,
targets
)
And printing out the shapes of each variable gave this:
logits.shape=(6, 1024, 50257)
targets.shape=(6, 1024)
loss.shape=(6, 1024)
It had returned a cross entropy number for every element in every sequence, across all
of the batches!
What's interesting
is that the
docs for
softmax_cross_entropy_with_integer_labels
imply that it has the same restrictions as PyTorch's -- it expects a single batch axis
in the tensors that are passed in.  Perhaps they're out of date?  Or perhaps Optax
just assumes that you know that in JAX "a batch axis" should be read as "as many batch axes as you want"?
Well, anyway -- it worked, and I checked that the numbers were solid.
Now, of course, we can't ask JAX for gradients using that
6
×
1024
matrix -- the loss function needs
to return a scalar -- but the
mean
function on a JAX array does exactly what we need.
So I had a solid loss calculation, which you can see in
calculate_loss
:
def
calculate_loss
(
model
,
inputs
,
targets
):
logits
=
model
(
inputs
)
loss
=
optax
.
losses
.
softmax_cross_entropy_with_integer_labels
(
logits
,
targets
)
.
mean
()
return
loss
So that's covered our loss function and the JITted
train_step
that uses it.
The only remaining code that I haven't gone over in this version of the
train.py
script
is the stuff immediately above
calculate_loss
--
get_training_data
and
generate_training_charts
.  These are both called as part of the housekeeping
code I glossed over in the
train
function, after we take checkpoints.
They just redraw a plot of the
loss and other training metrics, using stuff that's stored in the metadata of all of the checkpoints so far.
That means that there's a nice graphical way to keep track of a training run.  Fairly
dull stuff, so there's no need to go
through them, but it is worth taking a look at the checkpointing code
itself.
You can see the version I was working with at this point
here
.
It's not really much of a checkpoint; I was saving the model itself and
the metadata needed for that charting code, but not the optimiser, which would be
needed for a real checkpoint.  After all, the purpose of a checkpoint is to be able
to pick things up again if your training loop crashes, and you can't do that without
the optimiser's state.  Still, it was enough to get started with.
That said, one wrinkle I encountered when writing that simple checkpointing code was
that it was a tad tricky to save them in Safetensors format --
you can see the details here
.
So, that was my initial training code.  It was time to let it rip: could I train
my dumb "LLM" to map from A to A?
The first A-to-A run
As I mentioned earlier, the very first run didn't converge at all -- loss started
at about 10.82, which was promising (it's exactly what you'd expect for a randomly-initialised
network trying to predict GPT-2 tokens -- see
here
for
details), but then it remained there.
But when I fixed the "
jax.jit
should be
nnx.jit
" issue,
it started dropping.  After 92,160,000 tokens seen, it seemed to have hit zero (at least to the three DPs I was printing), so
I baked that into
train.json
and did another training run fixed to that number of tokens.  After about 14 minutes, it finished:
Training complete in 843.547 seconds
Tokens seen: 92,160,000
Throughput: 109,253 tokens/second
Final train loss: 0.000
2026-06-17 19:29:31.667194 Done
A very promising final loss, even though that was just whatever we got on the last
batch!  The actual loss chart looked like this:
If you're used to the loss charts in my previous posts, there's something to highlight
here: I've switched the Y axis over to being log, so those bumps near the end are actually
tiny deviations away from 0.001.
I think it's worth showing what the model actually did at this point.  It was actually
somewhat later that I wrote some code to load up the model checkpoints from these training
runs and do some smoke tests, but I'll show you some results now.
I wrote some code based on
my JAX safetensors post
to load up a model's parameters from a checkpoint's
model.safetensors
file:
def
load_model
(
model
,
file
):
model_state_simple_dict
=
load_file
(
file
)
dict_flat_state
=
{}
for
key
,
array
in
model_state_simple_dict
.
items
():
elements
=
key
.
split
(
"."
)
list_key
=
[]
for
element
in
elements
:
try
:
list_key
.
append
(
int
(
element
))
except
ValueError
:
list_key
.
append
(
element
)
dict_flat_state
[
tuple
(
list_key
)]
=
array
new_flat_state
=
nnx
.
from_flat_state
(
dict_flat_state
)
nnx
.
update
(
model
,
new_flat_state
)
...and then wrote two test scripts.
Firstly, was it really mapping
from A to A?  I wanted to be sure that the loss number was actually reflecting what I
wanted it to reflect.  I wrote
a simple script
that took a Safetensors file on the command line, and ran the first verse of
The Rime of the Ancient Mariner
(chosen because it uses oldish English so there
are some odd tokens in it) through the LLM it loaded from that file.
Here's what the model at the end of the run came up with:
giles@perry:~/Dev/jax-gpt2-from-scratch (main)$
uv
run
test_a_to_a.py
runs/a-to-a/checkpoints/best/model.safetensors
Input:
---
It is an ancient Mariner,
And he stoppeth one of three.
'By thy long grey beard and glittering eye,
Now wherefore stopp'st thou me?
---
Output:
---
It is an ancient Mariner,
And he stoppeth one of three.
'By thy long grey beard and glittering eye,
Now wherefore stopp'st thou me?
---
That's great!  It could certainly handle the mapping.  Out of interest, I decided to
see how quickly it had learned to get that right.  The average training loss in
that "best" checkpoint at the end of the training run was 0.0001, so how did the
mapping improve, and what was the loss, near the start of the training run?
For the first checkpoint, when we'd just run one batch through, we
had an average training loss of 10.8242.  With the model parameters that were
saved then, we get this output:
giles@perry:~/Dev/jax-gpt2-from-scratch (main)$
uv
run
test_a_to_a.py
runs/a-to-a/checkpoints/20260617Z185827-iteration-0/model.safetensors
Input:
---
It is an ancient Mariner,
And he stoppeth one of three.
'By thy long grey beard and glittering eye,
Now wherefore stopp'st thou me?
---
Output:
---
LOADRecommend ptwtacid cheek lunch KaLOAD blondrient Sole Broken engages CrimsplitrelyLOAD Consortium hopefully Fisheries qualardiestern565Financial gallery talked KaLOADhuge admit disappeared SoleERT Heardearth showcasingurancesLOAD
---
As you'd expect from that loss, it's total token salad.
Now let's take a look at the next checkpoint, taken after 375 "global steps" -- that is,
6,000 batches.  In that one, the average train loss since that first
checkpoint was 2.9323.  But that hides something important -- the maximum loss, near the
start, was (as you would expect) 10.78524, not much less than the average loss in the
previous checkpoint.  But the minimum (which we can safely assume was towards the end
of this checkpointing period) was 0.54155, so we can reasonably assume that the model
improved
very
rapidly at this point.  And the A-to-A test bears this out:
giles@perry:~/Dev/jax-gpt2-from-scratch (main)$
uv
run
test_a_to_a.py
runs/a-to-a/checkpoints/20260617Z185848-iteration-375/model.safetensors
Input:
---
It is an ancient Mariner,
And he stoppeth one of three.
'By thy long grey beard and glittering eye,
Now wherefore stopp'st thou me?
---
Output:
---
It is an ancient Mariner,
And he stoppeth one of three.
'By thy long grey beard and glittering eye,
Now wherefore stopp'st thou me?
---
So, we can see that the bulk of the improvement happened right at the start!  It
was able to pass the A-to-A test for that fairly unusual sequence after just 6,001
total batches of 6 1,024-token sequences.
The rest
of the training run was perhaps just grinding out improvement on rarer tokens, and
perhaps making it more certain about already-correct predictions.  After all, the
test script was simply printing the most likely token for each position, so at this state
it might have been predicting some of those tokens as 51% probability.  That would have meant
a penalty in the loss function, even if the answer was actually correct.
So that was an interesting script; I wanted to do another -- the standard smoke test that I've been using, based on Raschka's prompt:
how does the model complete "Every effort moves you" when asked to continue the sentence?
Here's the script
,
and here's what it generated:
giles@perry:~/Dev/jax-gpt2-from-scratch (main)$
uv
run
test_generation.py
runs/a-to-a/checkpoints/best/model.safetensors
Every effort moves you you you you you you you you you you you you you you you you you you you you you
That makes perfect sense.  In order to generate the next token in an autoregressive loop, we're looking at the
logits for the last one in the prompt.  When it first runs, the last token is
" you", and our model is trained to map A to A, so its result is " you".  We append
that to the prompt, run it through again, the last token is still " you", so of course it "predicts" the token " you"
again.  And so on.
So these results were both good news!  The A-to-A mapping was working, and was converging
rapidly in terms of loss -- and even more rapidly in terms of our poetic test.
So, what was next?  I wanted the
training loop to be as similar as possible to the code I used for my
best locally-trained PyTorch model
.
That used three things I had not built into the training loop at this stage:
learning rate scheduling, gradient clipping, and gradient accumulation.  The PyTorch code also had the ability to restart
from a checkpoint -- not super-important in a 14-minute training run like this one,
but I figured it would become important later.  After all, the PyTorch runs on my
local machine had taken almost two days, and if something went wrong halfway through (cat
jumping onto PC power button, etc) then I really wouldn't want to start from scratch.
I decided to handle gradient accumulation first.
Gradient accumulation
In PyTorch, doing
gradient accumulation
is pretty simple: the core of a typical training loop
without it might look something like this:
optimizer
.
zero_grad
()
result
=
model
(
inputs
)
loss
=
loss_function
(
result
,
targets
)
loss
.
backward
()
optimizer
.
step
()
We start off by clearing out any gradients that are stashed on the model's parameters,
then do a forward pass, work out the loss, do a backward pass to put new gradients
on the parameters, and then step the optimiser to apply those gradients.
Accumulating gradients just means changing it to something like this:
optimizer
.
zero_grad
()
for
step
in
range
(
gradient_accumulation_steps
):
result
=
model
(
inputs
)
loss
=
loss_function
(
result
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
optimizer
.
step
()
That is, we do a forward and a backward pass
gradient_accumulation_steps
times.  Because
we're not zeroing out existing gradients between them, the parameters will accumulate
gradients over time -- each backward pass will add its contribution onto what is already
there.  Each time, we
divide the loss by
gradient_accumulation_steps
, so that the gradients
that are put on the parameters are that much smaller, which
means that by the end of our loop we've got gradients that are the average of what
we'd have got if we'd done all of these microbatches in one big batch.  Finally,
once we've exited the loop, we
step the optimiser to apply those averaged gradients.
When I started thinking about implementing this in JAX, I noticed that
Optax has a help page on how to do it
,
but then I had one of those brilliant
shower thoughts that one sometimes has.  I should have learned by my age that they
rarely work out well, but this time I decided to give it a go rather than doing
things the official way.
My brilliant idea was that with some finessing, we could put the whole gradient
accumulation loop inside JITted code.  From what I'd learned so far, the higher up
in our code we put the JIT decorator -- that is, the more of the training loop it
covered -- the faster it would be.  In itself, that wasn't a bad idea.
But my first
implementation was less smart:
def
calculate_loss
(
model
,
inputs
,
targets
):
loss
=
0
for
microbatch_inputs
,
microbatch_targets
in
zip
(
inputs
,
targets
):
logits
=
model
(
microbatch_inputs
)
loss
+=
optax
.
losses
.
softmax_cross_entropy_with_integer_labels
(
logits
,
microbatch_targets
)
.
mean
()
return
loss
@nnx
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
The
inputs
were  full-step arrays (eg. shaped (16, 6, 1024) for
16 gradient-accumulation steps over 6 microbatches of 1024 sequences), and the targets
likewise.  That seemed very clever!  But in retrospect, it was obviously doomed to failure, and
when I ran it, I ran out of VRAM.
The point of gradient accumulation is that what you accumulate over time is, well,
gradients.  So you have to do a full forward pass and then a backward pass over the model
for each microbatch, letting gradients build up, and then apply those in one go, like
the PyTorch code did.
Unfortunately what I was doing with my code was essentially all of the forward passes,
one by one, letting the activations and JAX's internal structures representing what
calculations had been done accumulate -- not the gradients -- and then doing a single
backward pass across all of that.  Mathematically it made sense -- I would have got
the right effect if I'd had enough VRAM -- but it wasn't much more memory-efficient than just doing a single
batch of
gradient_accumulation_steps * batch_size
sequences.  Immediate CUDA OOM.
My second attempt was a bit more sensible and ran OK without the JIT:
#@nnx.jit
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
loss_list
=
[]
grads_list
=
[]
for
microbatch_inputs
,
microbatch_targets
in
zip
(
inputs
,
targets
):
microbatch_loss
,
microbatch_grads
=
nnx
.
value_and_grad
(
calculate_loss
)(
model
,
microbatch_inputs
,
microbatch_targets
)
loss_list
.
append
(
microbatch_loss
)
grads_list
.
append
(
microbatch_grads
)
average_grads
=
jax
.
tree
.
map
(
lambda
*
items
:
jnp
.
array
(
items
)
.
mean
(
axis
=
0
),
*
grads_list
)
optimizer
.
update
(
model
,
average_grads
)
return
jnp
.
array
(
loss_list
)
.
mean
()
You can see that now I was doing both the forward and the backward pass within the
loop, and then working out the mean gradients with that
jax.tree.map
, then
passing those average gradients to the optimizer.
It all made sense, and seemed to work when I ran it:
Training complete in 1,146.173 seconds
Tokens seen: 92,209,152
Throughput: 80,450 tokens/second
Final train loss: 0.001
2026-06-18 19:00:25.739249 Done
...and it wasn't as much slower as I would expect given the lack of JITting: 1,146
seconds versus 843.
It was interesting that the final train loss was higher than the run without gradient
accumulation, but larger effective batch sizes are not always a better thing: it depends
very much on the model you're training and the data.  The batch size and number of gradient
accumulation steps I was using were ones I had optimised for the full 163M-parameter
GPT-2-style LLM, not for this model.  So it was OK if it was a bit worse.
Anyway, I tried adding the
@nnx.jit
to that function, and ran it:
jax.errors.JaxRuntimeError: RESOURCE_EXHAUSTED: Out of memory while trying to allocate 20.71GiB. [tf-allocator-allocation-error=''] [executable_name='jit_train_step']
Ouch.  And looking at the traceback, it appeared that it was the actual JITting that
was running out of VRAM.  Something to do with loop unrolling, perhaps?  I dug around
for a while, trying to use JAX's
fori_loop
rather than a normal Python one, but to no avail -- I would always run out of
GPU memory.
Eventually, after a few hours, the alarm bells on my side quest detector had become
too loud to ignore.  Reluctantly, I gave up on hand-rolling my own gradient accumulation,
and implemented it
the Optax way
.
That was actually really nice and simple.  The
code is here
,
but the change is tiny and simple to explain.  Remember that we had this code to set up the
optimizer:
optimizer
=
nnx
.
Optimizer
(
model
,
optax
.
adamw
(
learning_rate
=
train_conf
[
"learning_rate"
],
weight_decay
=
train_conf
[
"weight_decay"
],
),
wrt
=
nnx
.
Param
)
That creates a Flax NNX optimiser, which uses an Optax AdamW optimiser under the hood.
The Optax way to do gradient accumulation is to wrap the optimiser in a
MultiSteps
helper, which -- with the NNX optimiser wrapping the result -- looks like this:
optimizer
=
nnx
.
Optimizer
(
model
,
optax
.
MultiSteps
(
optax
.
adamw
(
learning_rate
=
train_conf
[
"learning_rate"
],
weight_decay
=
train_conf
[
"weight_decay"
],
),
every_k_schedule
=
gradient_accumulation_steps
),
wrt
=
nnx
.
Param
)
The
MultiSteps
wrapper is really neat.  It has the same interface as a regular
optimiser, so its
update
method can be called with a set of gradients.  But instead
of applying them, it just accumulates them until a particular number of calls to
update
have been made, at which
it actually does apply the mean of the accumulated gradients, and resets its counter
so that it starts accumulating again.
That's actually a really nice API.  And it actually meant that I would have been able
to simplify the training loop.  Remember, we had this:
for
global_step
in
progress_bar
:
for
accumulation_step
in
range
(
gradient_accumulation_steps
):
inputs
,
targets
=
train_dataset
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
inputs
=
jax
.
device_put
(
inputs
,
model_device
)
targets
=
jax
.
device_put
(
targets
,
model_device
)
train_loss
=
train_step
(
model
,
optimizer
,
inputs
,
targets
)
train_losses
.
append
(
train_loss
.
item
())
microbatch_size
,
sequence_length
=
inputs
.
shape
tokens_seen_this_rank
+=
microbatch_size
*
sequence_length
The loop-within-a-loop was needed by the PyTorch code, because we needed to do the
optimizer step at the end to apply the accumulated gradients.  But with the Optax
wrapper, we could have just iterated over our samples in one top-level loop, relying
on the
MultiSteps
to make its updates every
gradient_accumulation_steps
iterations.
However, I decided to leave it in -- keeping track of the training in terms of global steps
meant that the training output with my JAX model would be easier to compare to the PyTorch
versions.  Perhaps if I'd been building the training loop completely from scratch I would
have chosen differently.
Anyway, with that code change in, I ran it, and:
Training complete in 836.409 seconds
Tokens seen: 92,209,152
Throughput: 110,244 tokens/second
Final train loss: 0.001
2026-06-18 20:56:15.220326 Done
I had the same loss at the end as the by-hand un-JITted version, which was reassuring.  And it was slightly faster
than the non-gradient-accumulating version, but it's a small enough difference that
it was probably just in the noise.
So that was gradient accumulation!
Here's the code with that added
.
Next, I wanted to get charting and scheduling of the learning rate, and gradient clipping working.
Charting the learning rate
Scheduling the learning rate means that we'll be changing it over the course of
the run -- like this example from one of my PyTorch training runs:
Having a chart like that one is really useful, as it allows you to sanity-check that
the changes you are making to the learning rate really are the right ones.  So I wanted to add the charting first,
and then the scheduling.  The boilerplate code to actually generate the chart, given
learning rate numbers in the checkpoints' metadata, was already there, so I had to
work out how to extract the current value of the learning rate from the optimiser and
then save it into the checkpoints.
This was the obvious starting point
.
Optax optimisers themselves don't store the learning rate, but if you create them
like this:
optax
.
inject_hyperparams
(
optax
.
adam
)(
...
)
...where the
...
in the brackets is the normal stuff that you'd pass in to the
optimizer when creating it, then you can extract the learning rate later.
However, the code on that help page was using the Optax optimiser directly, whereas my one in the training code
was wrapped inside a
MultiSteps
, which was in turn wrapped inside an NNX
Optimizer
object,
like this:
optimizer
=
nnx
.
Optimizer
(
model
,
optax
.
MultiSteps
(
optax
.
adamw
(
learning_rate
=
train_conf
[
"learning_rate"
],
weight_decay
=
train_conf
[
"weight_decay"
],
),
every_k_schedule
=
gradient_accumulation_steps
),
wrt
=
nnx
.
Param
)
Still, the solution seemed reasonably clear.  I could use the
inject_hyperparameters
trick
on the
adamw
that I was creating, and then pass it in to be wrapped like this:
optax_optimizer
=
optax
.
inject_hyperparams
(
optax
.
adamw
)(
learning_rate
=
train_conf
[
"learning_rate"
],
weight_decay
=
train_conf
[
"weight_decay"
],
)
optimizer
=
nnx
.
Optimizer
(
model
,
optax
.
MultiSteps
(
optax_optimizer
,
every_k_schedule
=
gradient_accumulation_steps
),
wrt
=
nnx
.
Param
)
The next question was how to actually read the learning rate from that optimiser.
The sample code in the Optax docs looked like this:
optimizer
=
optax
.
inject_hyperparams
(
optax
.
adamw
)(
learning_rate
=
schedule
)
params
=
initial_params
state
=
optimizer
.
init
(
params
)
print
(
'initial learning rate:'
,
state
.
hyperparams
[
'learning_rate'
])
_
,
state
=
fit
(
initial_params
,
optimizer
)
print
(
'final learning rate:'
,
state
.
hyperparams
[
'learning_rate'
])
Again, that was using the Optax optimiser directly, rather than trying to use one that was
inside an NNX one.  However, in
the docs for NNX's optimiser
I noticed that it exposes its wrapped Optax one's state as
opt_state
.  I put in
some temporary debug code to print that, and saw that it was the
MultiSteps
' state,
which made sense -- and that, in turn, contained the state of the wrapped
adamw
one
as
inner_opt_state
.
That
inner_opt_state
had a field called
hyperparameters
, which
was a dictionary that included
learning_rate
as a key.
Finally, the value that that key pointed to was a
Variable
object.  To get the actual
value from there, you need to call its
get_value()
to get the actual value,
which is a JNP array, so we needed to call
item()
on it.
All of that led to the following abomination unto God, mankind, and
the Law of Demeter
:
current_learning_rate
=
optimizer
.
opt_state
.
inner_opt_state
.
hyperparams
[
"learning_rate"
]
.
get_value
()
.
item
()
Eurgh.  I mean, really, eurgh.
Well, anyway, I put code to do that into the
train
function and save
the number as part of the metadata.  I did a partial training run, just for long enough
to confirm that the learning rate chart was being generated, and had a flat line on
it at 0.0014, the constant learning rate I was using at that point.
I can't say I was very proud of it, though.
Learning rate scheduling
To recap, the learning rate schedule that I wanted was this:
That's formed of two phases: an initial warmup, where the learning rate started at
0.00001 times the desired peak value, and then rose linearly to the peak, followed
by a cosine wave to decay it to 0.1 times the peak.
In PyTorch I had had to
use different learning rate scheduler objects to handle each phase, with a
SequentialLR
wrapper to bolt them together
:
warmup_scheduler
=
torch
.
optim
.
lr_scheduler
.
LinearLR
(
optimizer
,
start_factor
=
0.00001
,
end_factor
=
1.0
,
total_iters
=
warmup_steps
)
cosine_scheduler
=
torch
.
optim
.
lr_scheduler
.
CosineAnnealingLR
(
optimizer
,
T_max
=
decay_steps
,
eta_min
=
learning_rate
/
10
)
scheduler
=
torch
.
optim
.
lr_scheduler
.
SequentialLR
(
optimizer
,
schedulers
=
[
warmup_scheduler
,
cosine_scheduler
],
milestones
=
[
warmup_steps
],
)
However, it's a common pattern in training loops, and conveniently Optax provides a
warmup_cosine_decay_schedule
class that does all of that for you.
The only oddity in it is that
decay_steps
is kind of misnamed; it's actually total steps,
including the warmup.  So I wound up writing this code:
total_steps
=
(
len
(
train_dataset
)
//
world_size
)
//
gradient_accumulation_steps
warmup_steps
=
(
total_steps
*
train_conf
[
"warmup_period_percent"
])
//
100
learning_rate
=
train_conf
[
"learning_rate"
]
schedule
=
optax
.
warmup_cosine_decay_schedule
(
init_value
=
learning_rate
*
0.00001
,
peak_value
=
learning_rate
,
warmup_steps
=
warmup_steps
,
decay_steps
=
total_steps
,
# !!
end_value
=
learning_rate
/
10
,
)
optax_optimizer
=
optax
.
inject_hyperparams
(
optax
.
adamw
)(
learning_rate
=
schedule
,
weight_decay
=
train_conf
[
"weight_decay"
],
)
I did a training run with that, and it completed with this:
2026-06-19 00:17:25.777629 Tokens seen: 92,209,152
2026-06-19 00:17:25.777633 Throughput: 106,225 tokens/second
2026-06-19 00:17:25.777644 Final train loss: 0.006
2026-06-19 00:17:25.777646 Done
The loss was a bit worse again, but just as with the gradient accumulation steps,
the learning rate schedule I had specified was specifically designed for training
a real (if small) LLM, not for this toy A-to-A task that I was using to test the training
loop.  The important thing was the learning rate chart, and it looked like this:
Perfect!
Here's the code at this point
.
There were two boxes left to check before I had a training loop I could actually use
to build the LLM: gradient clipping and the ability to restart from a checkpoint.  I decided to
do gradient clipping first.
Gradient clipping
Gradient clipping
is where
for each update, you look for gradients that are suspiciously large, and cut them off so that they don't make
excessive changes to the model.
The
Optax docs
made it look pretty simple:
optimizer
=
optax
.
chain
(
optax
.
clip
(
1.0
),
optax
.
adamw
(
learning_rate
=
schedule
),
)
So, you use an
optax.chain
to chain together first a thing that does clipping,
and then the actual optimiser -- presumably the first thing in the chain sees the
gradients and does stuff to them, and then the second receives whatever the first has
returned.
Now, the question was, should we do the chain outside or inside the MultiSteps?  That is,
should we clip gradients each time before we step the MultiSteps optimiser, or do we accumulate
them and clip the average before we step the inner AdamW one?
Looking at
the old PyTorch code
,
I was running the gradient accumulation loop, and then
clipping at the end.  So the gradient clipping was happening to the accumulated
gradients.
That actually felt less intuitively good than the alternative, but I decided that
we should try to mirror what the PyTorch code is doing.  So:
optax_optimizer
=
optax
.
chain
(
optax
.
clip
(
train_conf
[
"clipping_max_norm"
]),
optax
.
inject_hyperparams
(
optax
.
adamw
)(
learning_rate
=
schedule
,
weight_decay
=
train_conf
[
"weight_decay"
],
)
)
So, the
adamw
optimiser would receive clipped gradients.  Because it was wrapped
in the
MultiSteps
, it was receiving the accumulated gradients every time that object
hit its
every_k_schedule
limit.
Unfortunately there was still a problem: that change meant that the optimiser that we were reading the learning rate from with
this horrendous code in the
train
function:
current_learning_rate
=
optimizer
.
opt_state
.
inner_opt_state
.
hyperparams
[
"learning_rate"
]
.
get_value
()
.
item
()
...would now be inside yet another level of nesting -- the
chain
object.  So, of course, when I ran it,
it blew up with an error:
AttributeError: 'tuple' object has no attribute 'hyperparams'
I used some debug prints to work out what was going on, and determined that the
state of the
chain
object was a tuple, the first element being an essentially-empty
state for the clipper, and the second being the hyperparameter-injected state for the
adamw
.
So that meant that the new correct code to get the learning
rate would be this:
current_learning_rate
=
optimizer
.
opt_state
.
inner_opt_state
[
1
]
.
hyperparams
[
"learning_rate"
]
.
get_value
()
.
item
()
Note that we've gained that
[1]
to do the lookup into the
chain
's tuple state.
I remember coming across a comment saying "forgive us for our trespasses in this method"
in a codebase long ago, and I know well how the author felt.
I did have an idea of how to at least limit the blast radius a bit, though.  At this
point in the code, I had the complex optimiser setup in the
main
function, and the
learning-rate-getting abomination in
train
.  I decided instead to define a function
called
get_learning_rate
right next to the optimiser setup, and pass that in to
train
.
So the horror was still there, but at least it was all in one place, like this:
optax_optimizer
=
optax
.
chain
(
optax
.
clip
(
train_conf
[
"clipping_max_norm"
]),
optax
.
inject_hyperparams
(
optax
.
adamw
)(
learning_rate
=
schedule
,
weight_decay
=
train_conf
[
"weight_decay"
],
)
)
optimizer
=
nnx
.
Optimizer
(
model
,
optax
.
MultiSteps
(
optax_optimizer
,
every_k_schedule
=
gradient_accumulation_steps
),
wrt
=
nnx
.
Param
)
def
get_learning_rate
():
return
(
optimizer
.
opt_state
.
inner_opt_state
[
1
]
.
hyperparams
[
"learning_rate"
]
.
get_value
()
.
item
()
)
log
(
"Start train"
)
start_global_step
=
0
## checkpointing
train
(
run_dir
,
model
,
optimizer
,
get_learning_rate
,
train_dataset
,
rank
,
world_size
,
gradient_accumulation_steps
,
start_global_step
,
train_conf
[
"checkpoint_interval"
],
)
...where
train
called
get_learning_rate
where it needed it.
I was just about to kick this off, but by chance happened to take a closer look at
the documentation for
clip
,
and spotted that it said
Clips updates element-wise, to be in
[-max_delta, +max_delta]
That rung a bell!  When I was
originally looking into gradient clipping
for the PyTorch training loop, I noted that that is a perfectly valid way to do
gradient clipping, but it's not the way I ultimately chose.
Instead, I was clipping based on the L2 norm.
The JAX training code was meant to work the same way as the PyTorch code, so that was
a good catch; I switched over from using
optax.clip
to using
optax.clip_by_global_norm
,
and then kicked off another training run:
2026-06-19 01:22:41.964291 Tokens seen: 92,209,152
2026-06-19 01:22:41.964295 Throughput: 105,022 tokens/second
2026-06-19 01:22:41.964308 Final train loss: 0.006
2026-06-19 01:22:41.964311 Done
Everything looked fine; my guess was that the final loss was so similar because
a simple task like A-to-A mapping, with such a shallow network, would be unlikely
to cause gradients to explode.
But it would be nice to be sure.  Was there some way I could track the gradients
and see if clipping had had to cut in?
One neat thing we had in the PyTorch code was that we could track gradient
norms pre-clipping:
pre_clip_norm
=
torch
.
nn
.
utils
.
clip_grad_norm_
(
model
.
parameters
(),
clipping_max_norm
)
.
item
()
grad_norms
.
append
(
pre_clip_norm
)
clipped_steps
.
append
(
pre_clip_norm
>
clipping_max_norm
)
Unfortunately,
clip_by_global_norm
and the general Optax API doesn't provide any way to access
the pre-clipping norms: the
ClipByGlobalNormState
that was the zeroth element
of the state of the
chain
that we were reading in the horrendous learning rate-reading code
is an alias of
EmptyState
.
I considered using
optax.tree_utils.tree_norm
to work out the norms directly, and logging that, but that would be tricky -- because
the gradients we were applying the clipping to were not the ones that were generated
in the
train_step
function, but instead the ones that had accumulated inside the
MultiSteps
object over multiple gradient accumulation steps.
This sounded like a lot of work for a not-enormous benefit, so I decided to leave
it out for this project.
There was, however, one small change that I wanted to make while I was messing around
with gradients -- what to do if non-finite numbers crept into them.
Back when I was first looking into gradient clipping, I was
somewhat horrified to realise
that the scaler object I was using to tell PyTorch to train in 16-bit for things
where it felt it would help (Automated Mixed Precision, or AMP), was silently dropping
any updates with non-finite gradients, and if you didn't use AMP, such gradients
would be happily applied to your model, most likely completely breaking it by setting
parameters to non-finite values.
This felt like the wrong place for that kind of logic to go -- I felt that
it should belong to the optimiser, or at least in some other part of the stack that
wasn't specifically related to the totally orthogonal task of mixed-precision
training.
I checked what JAX's default behaviour with non-finite gradients was, and it turned out
to be to just apply them -- but, with Optax, it actually
was
something you could fix at the
optimiser level.  If you wrap an Optax optimiser with
apply_if_finite
,
it will only apply finite gradients, so we could add it to the optimiser setup like this:
optimizer
=
nnx
.
Optimizer
(
model
,
optax
.
apply_if_finite
(
optax
.
MultiSteps
(
optax_optimizer
,
every_k_schedule
=
gradient_accumulation_steps
),
max_consecutive_errors
=
math
.
inf
,
),
wrt
=
nnx
.
Param
)
I set
max_consecutive_errors
to infinity to mirror the PyTorch code's behaviour.
Now, obviously, this required yet another level of indirection in the learning-rate-getting
function from hell:
def
get_learning_rate
():
return
(
optimizer
.
opt_state
.
inner_state
.
inner_opt_state
[
1
]
.
hyperparams
[
"learning_rate"
]
.
get_value
()
.
item
()
)
If you're keeping track, it's the
.inner_state
in there.  Heigh ho.
So, it was time to run it again:
Training complete in 892.715 seconds
2026-06-19 02:27:16.657056 Tokens seen: 92,209,152
2026-06-19 02:27:16.657059 Throughput: 103,291 tokens/second
2026-06-19 02:27:16.657070 Final train loss: 0.006
2026-06-19 02:27:16.657072 Done
That looked OK -- no change from before.
Here's the code
.
Now, it was time to take the last step
to finish the training loop: the ability to restart from a checkpoint.
Restarting from a checkpoint
At this point,
the checkpointing code
was pretty basic -- it would save the model as a Safetensors file, along with some
metadata like the min, max and average loss since the previous checkpoint, the number
of the global step that we were on, and whether or not this was the best checkpoint
(in terms of average training loss) so far.
In order to restore from a checkpoint, we'd need more information.  In the old PyTorch
code, we needed three extra things on top of the model and the metadata:
The scaler that we used to do automated mixed-precision training.  This JAX loop
was not going to do that, so it was not necessary here.
The learning rate scheduler.  This was built into the optimiser for JAX, so I
didn't think it was needed.
The optimiser itself.  This was important, and we definitely did need to save it.
So that was the job: save the optimiser in
save_checkpoint
, and then implement
a
load_checkpoint
so that we can restart from one.  I could then try kicking off
a training run, waiting for a bit, killing it, then restarting from the most recent
checkpoint.  The loss and learning rate charts would tell me whether or not the restart
really had picked up from where it had left off.
Initially I was thinking that I would just use pickle to save the optimiser, but
that felt like a problem waiting to happen.  Pickle has issues when you change
Python versions or versions of installed packages, which never
feels like
it's
going to be a problem, but all-too-frequently turns out to break stuff in reality.
Using Safetensors looked a bit tricky -- it had been
hard
to get it to work with Flax models, even though it had explicit support.
Now, the recommended library for checkpointing in JAX code is called
Orbax
.   I'd looked into it
before, and it looked a bit heavyweight, so I'd moved on.  But digging in a little
more, I found that it had what looked like
a simple API for saving PyTrees
,
which bypassed the complexity.
Getting it working was still a bit tricky, though.
Firstly, in the docs, they give this example:
import
orbax.checkpoint.experimental.v1
as
ocp
...
ocp
.
save
(
path
,
pytree
)
I tried that in the
save_checkpoint
function with code like this:
ocp
.
save
(
checkpoint_dir
/
"optimizer"
,
optimizer
.
opt_state
)
...and got the error
AttributeError: module 'orbax.checkpoint.experimental.v1' has no attribute 'save'
Huh.  Digging into the library from the command line showed that the function
was actually called
save_pytree
.  Not super-promising if the docs don't
match the API (though to be fair, it does say
experimental
right there in the
package name).
Anyway, changing that appeared to work:
ocp
.
save_pytree
(
checkpoint_dir
/
"optimizer"
,
optimizer
.
opt_state
)
...and then next to the 295 MB file called
model.safetensors
in my checkpoint directories, there was a 353 MB directory called
optimizer
.  In PyTorch-land
the optimiser had always been double the size of the model , but given the wildly different
file formats in play, I was comfortable enough that it was order-of-magnitude the same
as the model and somewhat bigger.  Perhaps Orbax was doing some kind of compression or something
like that.
Next, it was time to write
load_checkpoint
.  I started off by writing the
load_model
function to load up the safetensors file -- that's the one I showed earlier, back
when I showed how the original A-to-A model learned how to map a poem to itself,
and that if you asked it how to complete "Every effort moves you", it would respond
with " you you you you you" and so on.
Once I had that, I created a
load_checkpoint
, which called
load_model
, and then loaded up the
metadata and worked out what our best loss so far had been (which is necessary when
continuing from a checkpoint so that, as you continue training, you can work out
whether each new global step has had a loss that is better than the current best).
That was simple enough:
with
open
(
checkpoint_dir
/
"meta.json"
,
"r"
)
as
f
:
meta
=
json
.
load
(
f
)
restart_global_step
=
meta
[
"global_step"
]
+
1
with
open
(
checkpoints_dir
/
"best"
/
"meta.json"
)
as
f
:
best_loss
=
json
.
load
(
f
)[
"avg_train_loss"
]
Restoring the optimiser turned out to be a bit trickier.  Firstly, of
course, just like with saving, the Orbax function was called
load_pytree
rather than the documented
load
.  The next part was working out how to load it in a fashion that the optimiser
would accept.
If you load a checkpointed PyTree like this:
ocp
.
load_pytree
(
checkpoint_dir
/
"optimizer"
)
Then what you get back is a "basic" PyTree -- it will consist of lists, dictionaries,
tuples, basic Python types like strings, and JAX arrays.  The problem is that the
optimiser's state is formed of objects that can be mapped to such things -- for example,
an object can be mapped to a dictionary where each field is an item in the dict -- but
aren't actually those specific types of objects.
So if you do this:
optimizer
.
opt_state
=
ocp
.
load_pytree
(
checkpoint_dir
/
"optimizer"
)
...you get an error, something like this:
AttributeError: 'list' object has no attribute 'items'
...and likewise if you use the
nnx.update
function I was using in the
load_model
code:
nnx
.
update
(
optimizer
.
opt_state
,
ocp
.
load_pytree
(
checkpoint_dir
/
"optimizer"
))
...you'll get a slightly different but equally confusing error.
After a certain amount of floundering around, limited by the lack of documentation
(and it not seeming to match the API that I was seeing) I had the bright idea of
looking at
load_pytree
's docstring, and that turned out to be excellent.  In IPython:
In [1]: import orbax.checkpoint.experimental.v1 as ocp
In [2]: ocp.load_pytree?
Signature:
ocp.load_pytree(
path: 'path_types.PathLike',
abstract_pytree: 'AbstractPyTree | CheckpointMetadata[AbstractPyTree] | None' = None,
*,
checkpointable_name: 'str | None' = 'AUTO',
) -> 'tree_types.PyTreeOf[tree_types.Leaf]'
Docstring:
Loads a PyTree.
Loads from a ``PyTree`` checkpoint. A ``PyTree`` checkpoint must be a path
containing a subdirectory with the name provided by ``checkpointable_name``,
with default value ``AUTO``. See ``checkpointable_name`` for more details.
This function must be called on all available controller processes.
The operation blocks until complete. For improved performance, consider using
:py:func:``.load_pytree_async`` instead.
If ``abstract_pytree`` is not provided, the ``PyTree`` will be loaded exactly as
saved.
IMPORTANT: Loading is more brittle and error-prone when not providing
``abstract_pytree``. Always provide ``abstract_pytree`` if possible. Note that
you can always obtain the tree structure from a saved checkpoint using
:py:func:``.pytree_metadata``.
Providing the ``abstract_pytree`` guarantees two things:
1. The restored tree will exactly match the structure of ``abstract_pytree`` (or
raise an error if it is impossible to guarantee this). For example, if
``abstract_pytree`` is a custom object registered as a ``PyTree``, the checkpoint
will be restored as the same object, if possible.
2. The leaves of the restored tree will be restored with the properties
indicated by the abstract leaves. For example, if a leaf in ``abstract_pytree``
is a ``jax.ShapeDtypeStruct``, the restored leaf will be a ``jax.Array`` with the
same shape and ``dtype``. Each ``AbstractLeaf`` has a corresponding ``Leaf``
that is restored. See ``orbax.checkpoint.v1.tree`` for a table
of standard supported leaf types.
...
The solution was obviously that
abstract_pytree
.  When you provide it, it's used
as a template.  If in the abstract PyTree it finds a
Foo
object, and in the
loaded PyTree there is a dictionary in the same position with keys
bar
,
baz
and
quz
, it will create a
Foo
object, setting those fields to those values.
That means that you have something with the right structure to apply, so I wound
up with this relatively simple code to load checkpoint into the optimiser:
optimizer
.
opt_state
=
ocp
.
load_pytree
(
checkpoint_dir
/
"optimizer"
,
optimizer
.
opt_state
)
We're using the existing state of the optimiser as a template to tell Orbax how to
structure the loaded one.
I kicked off a training run, hit control-C halfway through, then restarted it
from the checkpoint, and the final loss chart looked like this:
...and the learning rate chart like this:
Perfect!  The interrupt was at about global step 400, and the loss continued to go down properly, and the learning rate followed
its schedule perfectly.
Here's
the checkpoint-loading code
and
the training script
.
Time to build a model!
So with that, phase one was done.  I had a training script.  It was massively overengineered
for training this little A-to-A model, but just right for training a small LLM
from scratch.
And now it was time to do that -- and that's what I'll cover in the next post.
