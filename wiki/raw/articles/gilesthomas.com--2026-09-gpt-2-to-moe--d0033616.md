---
title: "Extending Raschka's GPT-2: an MoE trained from scratch on an RTX 3090"
url: "https://www.gilesthomas.com/2026/09/gpt-2-to-moe"
fetched_at: 2026-09-11T10:01:13.141116+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Extending Raschka's GPT-2: an MoE trained from scratch on an RTX 3090

Source: https://www.gilesthomas.com/2026/09/gpt-2-to-moe

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
Mixture-of-experts models are really nifty.  You get inference speed close to
a small model's, with a lot of the smarts and knowledge of a large one.  While they
use as much memory as an equivalently-sized dense (non-MoE) model, they're much faster.
The frontier labs don't publish their architectures, but Claude and ChatGPT are widely
rumoured to be MoEs these days -- and certainly many large open-weights models like
DeepSeek
and
Kimi K3
are.
In this post, I'll show you how I added MoE support
to the GPT-2-style code from
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
",
then used that to train a 446M-parameter model with 220M active parameters
from scratch on my RTX 3090 -- essentially, GPT-2 small with 6 experts, 2 active per token.
I wanted to understand how MoEs work, and as always, felt that the best way to do
that is to build one (and then to write it up like this).  Hopefully because it's all
fresh in my mind as I write this, I should be able to explain things clearly for others
who've finished Raschka's book.
The training run took just less than eight days, and the resulting model
got a better loss on my test set than any of the other models I've trained
so far -- which was a good thing, given that it took
four times longer
to train!  It was also better
than the original OpenAI GPT-2 small (124M parameters), but not as good as GPT-2 medium
(345M parameters), although it was close.  That second result was interesting, as my
model had more total parameters than GPT-2 medium, but fewer active ones.
On an instruction fine-tuning test, it did
better than any of my other models, but worse than both OpenAI models (why OpenAI's models are
so good on that particular test is a
mystery
I'm digging into separately).
I'll go into those numbers in more depth later on.
Firstly, though, I'll run through the code that I needed to add to GPT-2 to make this
work -- not just the code for the experts themselves,
but the additional code for training it.  With MoEs you can't just train to minimise loss on your training set --
you need to add on an "auxiliary" loss to make sure they actually use
all of their experts, and that was where it became most interesting.
Before we get into the weeds, though, let's start off with the basics; how do MoEs work in Transformers-based LLMs?
How MoEs work
The phrase "mixture of experts" evokes an idea of a model which has separate parts
that are knowledgeable in different domains.  Maybe one part would know about coding,
another about history, another about philosophy, and so on.  You can imagine something
that had separate LLMs for different topics, and routed incoming inputs
appropriately.
That's actually not a bad design for a system -- Sakana.ai got a lot of interest for
their
Fugu
system back in June of this year, and it works rather like that.  But the "experts"
in an MoE are at a much lower level, and (as with
so many things
in LLMs) their expertise is in some weird and alien thing
that they determined was helpful for modelling language during their training.
Let's look at how they fit in mechanically.  The GPT-2-style LLM that we will start
from -- the one Raschka describes in his book -- looks like this:
Diagram 1
: a GPT-2-style LLM at the top level
The MoE magic happens inside those Transformers layers, so let's zoom in on one of them:
Diagram 2
: a GPT-2-style Transformers block
Specifically, what we do to make our LLM an MoE is to replace that feed-forward network (FFN) with multiple
separate FFNs -- our experts.  Different context vectors get routed to different experts based
on their contents.
The FFNs themselves -- in both the dense and MoE versions --
are surprisingly simple
.  In GPT-2, they
take in the incoming context vectors, run them through a normal linear layer
to expand the number of dimensions by four, run the result through a GELU activation
function, then project it back into the original incoming dimensionality with another
linear layer.
It's a really simple two-layer neural network, and at first glance seems somewhat arbitrary.
Tutorials about LLMs tend to spend pages and pages explaining attention mechanisms,
and pretty much gloss over the FFNs.
But the FFNs take up
twice as many parameters
as the attention mechanism in GPT-2.
They're clearly highly important, and my (very loose) metaphor for why that is,
is that attention is how the LLM works out what to think about, and the FFNs are where
it does its thinking.  It's not a perfect match for what's going on, but I think it's
a decent working model for intuition.
An MoE leverages this.  Instead of having just one FFN per Transformers block, we have
multiple, and we use a subset of them for each context vector.  We have what is called a
router, or a gating network.  It takes the incoming context vectors, and for each one, decides
which of these FFNs -- which experts -- to use.  Then we feed the input into the experts that were selected for it, combine
their results, and that's our final output -- like this:
Diagram 3
: an outline of an MoE block
Doing this gains us more "space" in the LLM for it to remember facts and ways of thinking
about things -- we have multiple experts for that knowledge to be spread over.  We could,
of course, do that by dedicating more space to the FFNs -- for example, by having one bigger one.
But with an MoE, because we only activate a subset of the experts for each context vector,
we save on the amount of computing we do for each context vector.  We need to keep all of
the experts in RAM -- remember that we're routing to them per-context vector, so in a batch
of sequences we're likely to be using most if not all of them.  But we don't have to feed everything
through all of them.
So, that's the basics -- nothing conceptually difficult.  What becomes more tricky
is the implementation.  How, concretely, does the router choose which experts to use for a given context vector,
how do we implement that choice -- and how can we do all of that efficiently?  And how do we
train the router to make its choices?
How I put this all together
When I started on this project, my first step was a Google search for useful references.
I came across this
excellent summary
from IBM.
In that post, they mention a number of papers; four seemed relevant :
"
Adaptive Mixtures of Local Experts
", the 1991 paper that introduced
the name (but used a model where all of the experts were run for each input -- they were thinking
less in terms of efficiency, and more in terms of having different parts of a network specialise in different things).
"
Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer
",
from 2017, which showed that you could use gating on MoE models to reduce the amount of computation
by only running the "best" of the experts for each input.
"
GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding
",
from 2020, which built on the above, applied it specifically to Transformers models, and simplified some things --
more on that later.
"
Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
",
from 2021, which did some nice additional simplification.
I decided to take a look at them, and was pleasantly surprised about how readable
they all were.  It looked to me like I'd be able to put together a working MoE
model by following what they (and the IBM summary) said, and that turned out to
be true -- the model worked, and trained well.  Of the four papers, I found the
Switch Transformers one the most useful, but the original 1991 paper also clarified
a lot to me.  I really do recommend skimming through them if you want to learn more
background about this stuff.
Anyway, once I'd got
it all put together, and trained the model,
I compared what I'd written to
the Hugging Face source code
for
Mixtral
, which was the first open
MoE model I remember hearing about.  Mixtral has a bunch of other improvements over GPT-2 beyond its MoE
support (RMSNorm, RoPE, and so on), and it's a much larger model than mine.  But
it turns out that the specific way
it handles the MoE side of things is largely the same as mine, apart from one
difference in how it calculates auxiliary loss (about which more later).  So that
was reassuring.
I also ran the final codebase past three LLMs -- ChatGPT, Claude, and Kimi K3 -- just to make sure that I
hadn't drifted from the mainstream or screwed up in other ways.  I did this in an
anonymous/private session so that they wouldn't use any memories they have of conversations
we'd had in the past, and asked them
Please take a look at the attached and tell me what you see.  I'm particularly interested in the MoE stuff.
All of them came back with some variation of "it's a pretty standard MoE implementation
on top of GPT-2, with load-balancing adapted from Switch Transformers".  Even more reassuring!
So I'm comfortable that what I've built is a normal implementation, and that's what I'll
describe in the rest of this post.  It's all fresh in my mind, so hopefully by describing
it in terms that would have made sense to me when I just finished Raschka's book, the result
will be useful to other people coming to this for the first time.
Let's get started by digging into the mechanics of how the router works.
The router, first cut
The problem we want to solve is that we have a context vector coming into our MoE
block -- as per
the diagram above
-- and we want to decide which experts we want to
route it to.  Let's say that we have
n
total experts, and we want to send
each input to
k
of them (where
0
<
k
<
n
, of course).  We'll also say that our context
vectors are of dimensionality
d
emb
.
Taking a
d
emb
-sized input and categorising it into probabilities across a number of
options is a pretty standard job for a neural network.  In fact, we can use a single
linear layer for it.  Imagine that we create one with
d
emb
inputs and
n
outputs.
For a given context vector, it might produce (for
n
=
6
) something like this:
In
[
5
]:
router
(
inputs
)
Out
[
5
]:
tensor
([
0.0418
,
-
0.1140
,
0.4254
,
0.1342
,
0.5106
,
-
0.1385
],
grad_fn
=<
ViewBackward0
>
)
So we can imagine picking out the indexes of the top
k
of those.
Let's be specific,
and say that
k
=
2
.  That means that we have indexes 4 and 2 -- the positions of the two
largest numbers -- so we want to route
our original context vector to experts 4 and 2.  They do their calculations,
we get output context vectors from them, and we can combine them.
How might we combine them?  Well, we do a lot of adding context vectors together in
our GPT-2-style LLM code, and treat the results as meaningful -- token embeddings
get added to position embeddings, shortcuts around attention and the FFN get added back
in to their results, and so on.  So perhaps we could do that?
That kind of setup has a problem, though -- it doesn't train the router.
Let's think about the MoE block again; here's the diagram again:
Diagram 3
(repeated): an outline of an MoE block
Think about the flow of data through it.  The context vectors flow into
the router.  We use the output of the router to select the two experts, and then
the original context vectors -- the ones that were fed into the router -- flow into those experts,
then are combined, and we get our result.
Now, consider what happens when you're training a model.  You run some training data through it, then calculate the loss -- how
good your model's results for that data are.  You then use that to work out
the gradients that you want to apply to the parameters to make it better.  You work
out the gradients by using back-propagation, working back from the loss, through the network, retracing the
computation graph in reverse.
When your backprop gets to this part of the model, it will start with the output context
vectors, trace back through the combination step, then back through the two chosen
experts, then back to the input context vectors -- and then it will go back to whatever
step came before the MoE block.
The calculations inside the router that selected our two experts did actually happen in our
forward pass -- but they're
not in the computation graph as we trace it backwards from the loss.  It's kind of a dead-end.
There's nothing in there to connect our selection of which experts we used to the path through the computation
that ended up at the loss.  (Interestingly, the effort of doing that diagram made that particularly
clear to me -- that slightly-messy labelling of the arrows at the top, with numbers to
show the sequence, is a direct result of the same issue.)
What that all means is that the router will not be trained.  The backward pass of our
training will completely ignore it, and so there will be no gradients to apply to it.
A starting model with random weights will randomly allocate context vectors to experts,
and it will continue to do that.
Clearly, we need to somehow modify our computation graph so that the router is connected --
so that when the backward pass flows up from the output context vectors, it sees the
router -- and ideally sees some aspect of it that will allow it to be trained to
do its job better.
The router's output as weights
"Adaptive Mixtures of Local Experts" starts by describing some previous work which treats the router's
outputs as weights for each of the experts.  That's a nice trick, and while it does
have some problems (as we'll see in a bit), it fixes the backprop issue.  (Interestingly,
they actually decided to do things differently -- but later work, like Switch Transformers,
goes back to doing things this way, with some important tweaks.)
As I said earlier, back in 1991 they weren't thinking of
MoEs as being a way to save on computation.  Instead, their focus was on training
better models to handle specific tasks, and they felt that having some way to split
those tasks up might make that easier.
So, for their case, they might take those outputs from above and normalise them:
In
[
7
]:
logits
Out
[
7
]:
tensor
([
0.0418
,
-
0.1140
,
0.4254
,
0.1342
,
0.5106
,
-
0.1385
],
grad_fn
=<
ViewBackward0
>
)
In
[
8
]:
torch
.
softmax
(
logits
,
dim
=-
1
)
Out
[
8
]:
tensor
([
0.1459
,
0.1249
,
0.2141
,
0.1600
,
0.2332
,
0.1218
],
grad_fn
=<
SoftmaxBackward0
>
)
...and then run their inputs through all six experts, then add together the outputs
weighted by those numbers -- 0.1459 times expert 0's output, 0.1249 times expert 1's, and so on.
Rather like this:
Diagram 4
: An MoE with all experts active
With that, we have something where the router is on the backward pass through the
computation graph from the output context vectors (and thus from the loss).  The weights
provide a route back, so the router will get trained.
But that version, of course, is running all of the experts for every token, so it
doesn't have the computational benefit of a modern sparse MoE.
It also has an issue,
as they point out in the paper, that if you imagine that you want each expert to have a well-defined
responsibility, things get messy.  Imagine that expert 2 in the above example was
the one that knew how to solve a particular task; all of the other experts would be contributing
too, and unless you find some way to train their weights down to exactly zero for that task, to get
a good loss on your training run they'd need to learn to balance each other out.
Their solution was to run all of the experts then to use a gating function on the
output -- that is, it would drop all of the results from the non-selected experts (see their figure 1).
But the modern solution is a bit different; for that, let's move
on to "Outrageously Large Neural Networks".
Making the router's output sparse
What we really want is an output from the router where some of the weights are zero.
Specifically, with our
k
active experts,
n
total, we want all but the
top
k
of them to have a weight of zero.  Then when we're running the network, we can skip those
zero-weighted experts and get a result that will be identical to what we would have
got without skipping them.
"Outrageously Large Neural Networks" does this with a trick that will be familiar from
the
causal mask
in the GPT-2 code.
Let's call the "raw" weights from our router
logits
:
In
[
7
]:
logits
Out
[
7
]:
tensor
([
0.0418
,
-
0.1140
,
0.4254
,
0.1342
,
0.5106
,
-
0.1385
],
grad_fn
=<
ViewBackward0
>
)
Let's run that through softmax again:
In
[
9
]:
torch
.
softmax
(
logits
,
dim
=-
1
)
Out
[
9
]:
tensor
([
0.1459
,
0.1249
,
0.2141
,
0.1600
,
0.2332
,
0.1218
],
grad_fn
=<
SoftmaxBackward0
>
)
That gives us some initial weights.  But we want all but the top
k
to be zero.
Now, if we want something to be zero after softmax, then it needs to be
−
∞
on
the way in.  I'll show the code to do this later, but for now, let's just assume that
we have some magic to set all but the top-
k
values to that.  In our
concrete example with
k
=
2
, the original
logits
with
that change applied would be:
In
[
15
]:
masked_top_k_logits
Out
[
15
]:
tensor
([
-
inf
,
-
inf
,
0.4254
,
-
inf
,
0.5106
,
-
inf
],
grad_fn
=<
ScatterBackward0
>
)
Now we can run that through softmax:
In
[
17
]:
torch
.
softmax
(
masked_top_k_logits
,
dim
=-
1
)
Out
[
17
]:
tensor
([
0.0000
,
0.0000
,
0.4787
,
0.0000
,
0.5213
,
0.0000
],
grad_fn
=<
SoftmaxBackward0
>
)
And we have some weights! With those, we can conceptually run this "all-experts-active" kind
of network:
Diagram 4
(repeated): An MoE with all experts active
...but skip the experts whose weights are zero.  The weights that we provide through
the steps above will mean that the router will get trained.
That's pretty neat!
There is one thing to highlight, though.  Imagine if we have one active expert -- that
is,
k
=
1
.  We'd mask out all of the other ones:
In
[
15
]:
masked_top_k_logits
Out
[
15
]:
tensor
([
-
inf
,
-
inf
,
-
inf
,
-
inf
,
0.5106
,
-
inf
],
grad_fn
=<
ScatterBackward0
>
)
...and softmax:
In
[
17
]:
torch
.
softmax
(
masked_top_k_logits
,
dim
=-
1
)
Out
[
17
]:
tensor
([
0.0000
,
0.0000
,
0.0000
,
0.0000
,
1.0000
,
0.0000
],
grad_fn
=<
SoftmaxBackward0
>
)
The weight will always be one, regardless of the original logits.   And if a function can
only ever return the same result, its derivative will always be zero, so there will
be no gradients and it can't be trained.
Interestingly, that's something that is -- almost silently -- addressed in the Switch
Transformers paper.  They are specifically looking at
k
=
1
MoEs, and
they mention the "Outrageously Large Neural Networks"
paper's routing system, then present their own calculations which
instead of replacing non-top-
k
values with
−
∞
, and then softmax,
do the softmax first, then zero out the non-top-
k
.  They don't highlight
the difference.
I decided that for this experiment, I'd go ahead with the non-Switch Transformers
calculations, anyway, and do the replace-with-
−
∞
-then-softmax system, with some
guard code to prevent it from accidentally being set to
k
=
1
.  Most
recent MoE models I've seen have at least two active experts, after all.
The good news is that not only did it work -- when
I checked later, it also
matched the choice taken in Mixtral, which feels like a solid endorsement.
So, at this point, we know how an MoE works in theory.  Let's start coding.
The actual code (finally!)
I started with the code that I had from
"
Build a Large Language Model (from Scratch)
".
In that, the Transformers block looked like this:
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
self
.
att
=
MultiHeadAttention
(
d_in
=
cfg
[
"emb_dim"
],
d_out
=
cfg
[
"emb_dim"
],
context_length
=
cfg
[
"context_length"
],
num_heads
=
cfg
[
"n_heads"
],
dropout
=
cfg
[
"drop_rate"
],
qkv_bias
=
cfg
[
"qkv_bias"
],
)
self
.
ff
=
FeedForward
(
cfg
)
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
self
.
drop_shortcut
=
nn
.
Dropout
(
cfg
[
"drop_rate"
])
def
forward
(
self
,
x
):
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
x
=
self
.
drop_shortcut
(
x
)
x
=
x
+
shortcut
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
=
self
.
ff
(
x
)
x
=
self
.
drop_shortcut
(
x
)
x
=
x
+
shortcut
return
x
I wanted to keep the capability to run this in MoE or non-MoE mode, and decided
that I'd do that by extending the model config in
cfg
so that it would have an
optional
moe
section, which would include MoE-specific stuff.  If that wasn't present,
then I'd create a normal dense LLM.  To do that, I replaced the line in
__init__
that assigned to
self.ff
with this:
self
.
is_moe
=
"moe"
in
cfg
if
self
.
is_moe
:
self
.
ff
=
MixtureOfExperts
(
cfg
)
else
:
self
.
ff
=
FeedForward
(
cfg
)
Next, it was time to implement the
MixtureOfExperts
class itself.  The obvious
config that it would need was how many experts there were in total, and how many
were active per token:
class
MixtureOfExperts
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
num_experts
=
cfg
[
"moe"
][
"num_experts"
]
self
.
num_active_experts
=
cfg
[
"moe"
][
"num_active_experts"
]
Now, there's that issue where having just one
active expert will pin the softmaxed weight to one, so it won't train -- so I decided to protect against
that (and against another obvious mistake that the config could contain):
if
self
.
num_active_experts
<
2
:
raise
Exception
(
f
"Can't train with ``num_active_experts`` < 2 (got
{
self
.
num_active_experts
}
)"
)
if
self
.
num_active_experts
>
self
.
num_experts
:
raise
Exception
(
f
"
{
self
.
num_active_experts
=}
is larger than
{
self
.
num_experts
=}
"
)
Next, it was time to create our router, mapping from the incoming context vectors
(of size
cfg["emb_dim"]
in this code) to the number of experts:
self
.
router
=
nn
.
Linear
(
cfg
[
"emb_dim"
],
self
.
num_experts
,
bias
=
False
)
I decided to make it unbiased because I have a vague impression that that is the fashion
these days -- nothing more principled than that :-)
Next, we needed the
num_experts
experts themselves, each of which would be one of
the same
FeedForward
modules as we were using in non-MoE mode:
self
.
experts
=
nn
.
ModuleList
([
FeedForward
(
cfg
)
for
_
in
range
(
self
.
num_experts
)
])
They needed to go into an
nn.ModuleList
because if they were just in a regular
list (as I discovered when I tried it) they would not be registered by PyTorch as
things containing parameters belonging to the module.  We create our optimiser
for training with code like this:
optimizer
=
torch
.
optim
.
AdamW
(
model
.
parameters
(),
lr
=
learning_rate
,
weight_decay
=
weight_decay
)
...and so anything that isn't in
model.parameters()
will never get updated, which
would be a Bad Thing.
That was enough to have the pieces in place.  It was time to write the forward
pass -- to get the router logits, do the top-
k
, softmax, and then to use those
results to run the experts.
From context vectors to logits to top-
k
to weights
Getting the logits was simple enough.  Looking at the
forward
method:
...we have an incoming set of context vectors,
xs
.
That is shaped
(batch_size, sequence_length, d_emb)
.
Let's try to visualise that.  Understanding tensor operations is something you can
kind of short-cut with intuition, but I think that in order to really understand the
next steps it's best to have something a bit more tangible in mind.
You can think of an order-3 tensor like this as a cuboid.  With
batch_size
of 3,
sequence_length
of 5, and
d_emb
of 7 -- artificially small values to keep things simple -- it might look like this:
Diagram 5
: The
xs
tensor as a 3-D cuboid
Every dot in that cuboid is a single number.  A single context vector is the numbers
as you follow a line from the "front" of the cube -- the
batch_size
×
sequence_length
face to the left -- to the "back".
That 3-D representation was fiddly to get right, and is likely to get confusing if
we keep using it.  So instead, let's look at two 2-D views of the same thing,
from the front (where you are looking at a
batch_size
×
sequence_length
face), and from one of the sides, where it's
batch_size
×
d_emb
:
Diagram 6
:
xs
as two 2-D views
So in this view, each of the circles in the "Front view" is the first number in a
specific context vector, and each of the rows in the "Side view" is the set of numbers
that make up a specific context vector.  Hopefully that's easy to visualise.
Now, a PyTorch
nn.Linear
layer like our
self.router
operates on the last dimension
in the tensor you pass in.  For our
xs
, shaped
(batch_size, sequence_length, d_emb)
,
it will work on the
d_emb
dimension -- that is, it will operate on each context
vector independently, which is what we want.
routing_logits
=
self
.
router
(
xs
)
That gives us a set of logits shaped
(batch_size, sequence_length, num_experts)
.
In our visualisation, that's a
batch_size
×
sequence_length
×
num_experts
cuboid; let's diagram that with four available experts:
num_experts = 4
:
Diagram 7
:
routing_logits
as two 2-D views
Again, if we look at the front view, each circle represents the first element of the
routing logits for one of the context vectors, and in the side view, each row represents
all of the routing logits for a context vector.  So we have the right data in our
cuboid.  From what we're calling the front view, it's got the same dimensions as
xs
, which
is useful.
In order to work out which of our
experts each context vector should go through, we need to get the top-
k
values
for each context vector in
routing_logits
.  PyTorch has
a
topk
function
to do exactly that:
top_k_values
,
top_k_indices
=
torch
.
topk
(
routing_logits
,
k
=
self
.
num_active_experts
,
dim
=-
1
)
The
dim=-1
tells it to work across the last dimension, which is the
dimension of length
num_experts
.  It returns the top
self.num_active_experts
values
and their positions, as tensors -- both shaped
(batch_size, sequence_length, num_active_experts)
.
So, we have two new tensors, which we can visualise as cuboids, both of
batch_size
×
sequence_length
×
num_active_experts
.
Let's show that with
num_active_experts = 2
:
Diagram 8
:
top_k_values
(or, equivalently,
top_k_indices
) as two 2-D views
Both
top_k_values
and
top_k_indices
are shaped that way.  As normal, the
"front" face is the same; each circle corresponds to a context vector, and for
top_k_values
it holds the highest value in that context vector's logits (because
topk
returns results sorted), while
for
top_k_indices
it holds the index that that highest value sits at in the logits
list.  Looking at the side view, we're seeing a list of top-k logit values or indices
for a given context vector.
Now, we want a version of
routing_logits
that we can run through softmax to get
some weights, and in order to do that we need to replace the non-top-
k
values
with
−
∞
for each of the context vectors.
The solution that I hit on eventually (after various other attempts ) was this.
Let's start with a tensor identical in size to
routing_logits
, but
full of
−
∞
s:
top_k_routing_logits
=
torch
.
full_like
(
routing_logits
,
-
torch
.
inf
)
Now,
top_k_values
contains the values that we want to have in there, and
top_k_indices
contains the indices in the logits lists where they should go.  All of the other values
can remain as
−
∞
.
This will, of course, be the same shape as
routing_logits
:
Diagram 9
:
top_k_routing_logits
as two 2-D views
Both
top_k_values
and
top_k_indices
are compatible in their
first two dimensions with
routing_logits
, and thus with
top_k_routing_logits
--
that is, their front faces in our visualisations are the same -- compare the front
face of the above with the one for
diagram 8
.
For all of our tensors, the first two dimensions correspond ultimately to an incoming
context vector in
xs
.  It's just the last dimension and the data they contain that differ.
PyTorch has a
scatter_
function on its
Tensor
class, which takes a list of positions and list of values.
It takes one specified dimension, and treats that one essentially as a set of lists.
Then it takes two other tensors with the same number of dimensions as each other, each of which matches in size in all but the specified
dimension, and treats the other dimension as being a list of values for one parameter,
and list of indices for the other.  It overwrites the data at the specified indexes
with the specified values.
That sounds useful!  Let's make it concrete.  Remember that in all of these
cuboids we're visualising, the front view we're looking at corresponds ultimately to a context
vector.  In
routing_logits
, it's the raw logits for expert routing for that vector --
the number on the front face is the first of those (corresponding to the logits for
routing to the first expert).  If we look at the side view, each row would correspond
to the set of logits for a given context vector.
Now, let's consider just that.  Inside
routing_logits
, our specific context vector
might have logit values corresponding to it like this:
Diagram 10
: A single CV's routing logits in-place in the cuboid
Visualised the same way, with
k
=
2
the equivalent part of
top_k_indices
would look like this:
Diagram 11
: A single CV's top-k routing logits indices in-place in the cuboid
That is, the
topk
function identified that index 2 in the original logits was the
highest value, and 0 was the second-highest.
Likewise,
top_k_values
would have this:
Diagram 12
: A single CV's top-k routing logits values in-place in the cuboid
These diagrams are getting a bit unwieldy; let's look at this specific context vector's
data as lists.  For our
selected context vector, we have these logits from
diagram 10
:
[
0.4254
,
0.1342
,
0.5106
,
-
0.1385
]
...these top-
k
indices from
diagram 11
:
...and these values from
diagram 12
:
Our
top_k_routing_logits
tensor is just full of
−
∞
s, and is the same shape
as
routing_logits
, so its corresponding part is this:
What
scatter_
will do is select indices 2 and 0 (because of the values in
top_k_indices
),
and copy the corresponding numbers from
top_k_values
on top of whatever is already there:
[
0.4254
,
-
inf
,
0.5106
,
-
inf
]
It will do that for every one of the positions in that front view.
So now we have what we wanted: a grid of routing logits for each context vector,
where the non-top-
k
ones have been replaced by
−
∞
.
That's pretty nifty!  And so here's the code to do it:
top_k_routing_logits
.
scatter_
(
dim
=-
1
,
index
=
top_k_indices
,
src
=
top_k_values
)
I was initially a little worried that the whole "replace the logits
with a 'static' tensor and then scatter the values in there" approach might break the
computation graph, but tests showed that it didn't.  My intuition is that because
the
−
∞
s were summoned out of nowhere, they are dead ends for backprop, but because
the logits that we're copying in come from previous calculations, they are not.
So once we've done that, we have our top-
k
logits, ready for a softmax -- so it's time to do that:
expert_weights
=
torch
.
softmax
(
top_k_routing_logits
,
dim
=-
1
)
...and we have our weights, yet another cuboid like this:
Diagram 13
:
expert_weights
as two 2-D views
Just as before, a given number on our front face is the first of the expert weights
for a specific context vector, and each row in the side view is all of the expert
weights for that context vector across all experts.  Post-softmax, the weights for
active experts for that context vector are positive numbers, and the weights for
the inactive ones are zero.
Running the experts
The next step was to actually feed the context vectors into their experts.  I decided
to keep this simple, and just iterate over the experts, one by one, and for
each one to find which incoming context vectors wanted to go to it, run them all
through, and then reassemble the results.
I believe that larger MoE systems have
smarter routing systems -- for example, for a huge model that can't fit on a single
GPU you might have different experts on different GPUs or even machines, and route to
them in parallel.  But for my toy-sized models, this felt simplest, and felt like it would be efficient enough .
The way I decided to do this was to use an "accumulator" model.  We know that
the shape of the outputs is the same as the shape of the inputs -- that is, if we have
our incoming
xs
shaped
(batch_size, sequence_length, d_emb)
, then the output
will have the same shape.  So I started off by creating a tensor of zeros of that
shape:
all_outputs
=
torch
.
zeros_like
(
xs
)
So, just like
xs
in
diagram 6
, it will look like this:
Diagram 14
:
all_outputs
as two 2-D views
...but it would be filled with zeros in every position.
The plan was that each expert would be run on the appropriate context vectors, its outputs
would be scaled by the weights that were calculated by the router and its associated
top-
k
and softmax for that context vector/expert pair, and then the results could
be added into
all_outputs
.  That would give us the result we wanted: after all experts
had been run on their respective context vectors,
all_outputs
would have the weighted
sums.
So the next step was to iterate over the experts:
for
expert_ix
,
expert
in
enumerate
(
self
.
experts
):
Now, we need to know which context vectors wanted to be fed to this expert.
Let's take a look at our representation of
expert_weights
again:
Diagram 13
(repeated):
expert_weights
as two 2-D views
We can see it as a bunch of
num_experts
"slices", each the same shape as that
front face,
(batch_size, sequence_length)
, where each one is the weights for a given expert.
The front face itself (corresponding to the rightmost column on the side view) is
the weights for expert 0, the next one "back" is for expert 1, and so on.
And in code, we
can get the slice for the expert with index
expert_ix
like this:
expert_weights
[:,
:,
expert_ix
]
That will be a simple 2-D grid of numbers like this:
Diagram 15
:
expert_weights
sliced for one expert
You can see that it's a grid of one number for each context vector in our input --
the same shape as the front face in all of the diagrams so far.  Each number is the
weight that the expert with index
expert_ix
has for the context vector in question.
We can now do a comparison:
this_expert_mask
=
expert_weights
[:,
:,
expert_ix
]
>
0
That will give us a new grid of the same shape, but the numbers have been replaced
with booleans --
True
if the corresponding context vector has a weight for this
expert that is greater than zero,
False
otherwise.  We've got a mask that identifies
exactly the context vectors that we want to run through this expert.
Let's imagine it looks like this for some particular set of context vectors and some specific expert; I've coloured in the circles representing
True
and left the
False
ones white.
Diagram 16
: what
this_expert_mask
might look like for one expert
Now comes the clever part :-)   Remember that our original incoming context vectors,
in
xs
, looked like this:
Diagram 6
(repeated):
xs
as two 2-D views
We can use our mask -- the grid of
True
s and
False
s in
diagram 16
-- to
select a subset of the context vectors in there, like this:
That will return us the subset of the incoming context vectors that we want to run
through this expert.  In terms of our diagrams above, it will be selecting the context
vectors in the front face that are "selected" by our mask, and taking the "cores" as it goes
back through the cuboid from there.
The question is, what shape will it be?  You can see that there's no simple 3-D shape
it could be.  The first sequence in our batch -- the first row on the front face -- has two selected context vectors,
while the second has one, and the third three.
You could imagine a world where the output would be the same shape as the input -- that
is, a tensor the same shape as
xs
-- but with the non-selected numbers replaced with
None
s
or something like that.  But instead, PyTorch produces what amounts to a
list of the selected context vectors for this expert.  We'll call the number of selected
vectors
num_selected_context_vectors_for_this_expert
,
and it's six in the example diagram above, so the shape will be
(num_selected_context_vectors_for_this_expert, d_emb)
,
like this:
Diagram 17
: the "selected" context vectors
Now, note that this is a big change from all of our tensors so far.  It has lost the
connection back to the original
xs
tensor's shape.  In all of the other tensors, we could
map something back to the original context vectors in
xs
.  But with this new
one, we have a bunch of context vectors with no inherent connection to where they
originally came from in
xs
.  We'll come back to that.
But for now, we have the data that we want to run through the expert with index
expert_ix
.  The expert is an FFN -- our two linear layers with a GELU in between them --
and will treat all but the last dimension in whatever we feed it as "batch" dimensions,
so it will work over that
d_emb
dimension, as we want it to.  So the code to
actually select the context vectors -- our
xs[this_expert_mask]
above -- and then
to run it through the expert itself just becomes this:
this_expert_results
,
_
=
expert
(
xs
[
this_expert_mask
])
We get the results of running our selected context vectors through the expert,
still shaped
(num_selected_context_vectors_for_this_expert, d_emb)
.
(If you're familiar with the GPT-2 code, that
_
in the code might seem odd.  We'll come back
to why the expert is returning a tuple and why we are ignoring the second item in
it later.)
So we have
our results -- we've run the appropriate context vectors for this expert through it.
But they're in a slightly funny shape, and we're going to need to fix that later on.
But first, we need to apply the appropriate weights for this expert
to each result.
Remember that
this_expert_mask
is a grid of booleans,
(batch_size, sequence_length)
, like this:
Diagram 16
(repeated): what
this_expert_mask
might look like for one expert
...where
True
-- filled in the diagram -- means that this expert is active for the corresponding context vector, and
False
means it isn't.
expert_weights
looks like this:
Diagram 13
(repeated):
expert_weights
as two 2-D views
Now, previously we did this:
...to pluck out the context vectors from
xs
where the mask was true.  If we were to
do
expert_weights
[
this_expert_mask
]
...then we would be doing something similar.  We'd get a grid like the one of
context vectors in
diagram 16
, with one row for every selected context
vector for this expert, except that instead of each row containing
a context vector, it would contain that context vector's per-expert weights:
Diagram 18
: all expert weights for the "selected" context vectors
Now, on its own, that's not particularly useful -- but you can hopefully see that
column
this_expert_ix
is the weights for our expert for all of the context
vectors that are going to be run through it!  So if we do the same masked lookup as
before, but also select that column, we get code like this:
expert_weights
[
this_expert_mask
,
expert_ix
]
What we're saying is "pick each item in
expert_weights
that matches a
True
in
this_expert_mask
, then take the
expert_ix
th element of it".
It will look like this:
Diagram 19
: this expert's weights for the "selected" context vectors
That is exactly
what we need to get the weights for our results!  We need to multiply the
i
th
element in
this_expert_results
-- an output context vector that is the results for
a particular input context vector -- with the
i
th element of
expert_weights[this_expert_mask, expert_ix]
.
However, there is one tensor-compatibility issue.  What we have is shaped
(num_selected_context_vectors_for_this_expert,)
-- that is, it's essentially just
a list of numbers.
Now, we want to multiply our results by these weights, which means that we want to
broadcast them across
this_expert_results
, which
is shaped
(num_selected_context_vectors_for_this_expert, d_emb)
.
Naively you might think that if you try to multiply a
(num_selected_context_vectors_for_this_expert, d_emb)
tensor by a
(num_selected_context_vectors_for_this_expert,)
one, PyTorch would match
up the two dimensions of the same size and it would just work.  But it would actually
try to match up across dimensions from right to left, and would complain that
num_selected_context_vectors_for_this_expert
does not equal
d_emb
.  So instead,
it's best to feed it an explicit
(num_selected_context_vectors_for_this_expert, 1)
tensor so that it knows which dimensions we're trying to match up, and which ones
it should broadcast over:
this_expert_weights
=
expert_weights
[
this_expert_mask
,
expert_ix
]
.
unsqueeze
(
1
)
...and that will give us
this_expert_weights
of shape
(num_selected_context_vectors_for_this_expert, 1)
That would look identical to
diagram 19
in the way I've been diagramming these things, but it's technically
different and necessary.
So now, with the
unsqueeze
having fixed the dimensionality so that we can do a broadcast, we can do this:
this_expert_results
*
this_expert_weights
...and with that we have our weighted results for this expert -- all of the context
vectors that should have been run through it have been, and they've been multiplied
by the weights that the router gave for them, so we have our backprop channel for
training the router.
The next step is that we need to somehow put these results into
all_outputs
.  Specifically,
because it's initially all zeros, and we want it to hold the results of adding together the
results from each active expert for each context vector, we need to add them to whatever is
already there at this point in the iteration through the experts.
Even though -- as noted earlier -- we have, by this point in the calculations, lost
the connection between the tensors we've been working with and the original "front-facing"
grid of our original tensors like
xs
, where we could link something directly to the
incoming context vector that it related to, it's actually surprisingly easy to patch that
up :-)
Remember that outside our loop through the experts, we created
all_outputs
like this:
all_outputs
=
torch
.
zeros_like
(
xs
)
So, just like
xs
in
diagram 6
, it looked like this:
Diagram 14
(repeated):
all_outputs
as two 2-D views
Now, previously we had code to extract the context vectors that we wanted to go through
our expert from
xs
, and it looked like this:
That gave us what amounted to a list of context vectors, like this:
Diagram 17
(repeated): the "selected" context vectors
Now, the interesting thing about a masked lookup into a tensor like
something[some_mask]
is that not only can you do it to extract a subset of the values from the tensor like
we did with
xs
-- you can also use it to assign to the masked subset of the elements in
the
something
tensor.
To make that concrete: when we did
We got a tensor sized
(num_selected_context_vectors_for_this_expert, d_emb)
.
That means that if we were to do:
all_outputs
[
this_expert_mask
]
...then given that the mask is the same, and
all_outputs
has the same shape as
xs
, then we'd also get a
(num_selected_context_vectors_for_this_expert, d_emb)
result.
But the thing with assignment means that if we had some tensor shaped
(num_selected_context_vectors_for_this_expert, d_emb)
-- let's call it
foo
-- then we could do this:
all_outputs
[
this_expert_mask
]
=
foo
With that, instead of selecting the parts of
all_outputs
and using them in the future,
we're overwriting them with whatever is in
foo
.
Furthermore, we can use the same trick with the augmented assignment operators like
+=
:
all_outputs
[
this_expert_mask
]
+=
foo
...means "select the elements from
all_outputs
that have
True
in
this_expert_mask
,
and then increment them by the elements of
foo
".
So finally, we get our code:
all_outputs
[
this_expert_mask
]
+=
this_expert_results
*
this_expert_weights
That multiplies the results from the expert by the corresponding weights, and then adds
them in to the running totals we're keeping in
all_outputs
.  Because
all_outputs
is the
same shape as
xs
, and thus
all_outputs[this_expert_mask]
is the same shape as
xs[this_expert_mask]
, and we've kept that same shape as we went through the expert itself
and multiplied by the weights, it will work.
And with that, we've done all of the calculations that we need for this specific
expert, so we can go back round the loop for the next one.  When we've finished with
all of the experts, we can return the result:
Phew!  That was quite a lot of explanation, but I think that what is going on in the code needs it.  I originally wrote it in a kind of
flow state of inspiration, and was very pleased with it, but it feels like now that
I've explained it, I actually understand what my subconscious must have known while I was
writing it.  And I hope it's reasonably clear for anyone reading this.
But there was one extra thing I wanted to keep track of before I started running this: the balance between the different experts.
Logging the router logits and weights
We'll
come back to this in some detail later, but a problem with MoEs is that they can
wind up depending heavily on specific experts, and ignoring the others -- the
auxiliary loss I mentioned way back in the intro to this post is required
to avoid that.
I didn't want to implement that yet, but I wanted to log enough data to see if it really
would be necessary with my setup.
A good way to keep track of how much each expert is being used is to record the logits -- the original results
from the router, before the top-
k
and the softmax -- and the actual post-top-
k
,
post softmax expert weights that we actually used.
The changes to do this are dotted around a bit, so I've linked to the appropriate
lines on GitHub and if you have the screen real-estate to do so, I'd recommend that you
use that to follow along.  However, I've tried to put enough code inline in this
post below that it should be comprehensible without that.
I decided that I'd return the logits and the expert weights from the
MixtureOfExperts
module's forward pass as
an extra output
here
:
class
MixtureOfExperts
(
nn
.
Module
):
...
def
forward
(
self
,
xs
):
...
return
all_outputs
,
(
routing_logits
,
expert_weights
)
Now, back in the
TransformersBlock
we were setting
self.ff
to either a
FeedForward
object or a
MixtureOfExperts
depending on
whether MoE was enabled for this model
here
:
class
TransformersBlock
(
nn
.
Module
):
...
def
__init__
(
self
,
cfg
):
...
self
.
is_moe
=
"moe"
in
cfg
if
self
.
is_moe
:
self
.
ff
=
MixtureOfExperts
(
cfg
)
else
:
self
.
ff
=
FeedForward
(
cfg
)
That meant that in our forward pass where we previously just did this (I won't link to this
because it's an old version and having links to different versions would be confusing):
class
TransformersBlock
(
nn
.
Module
):
...
def
forward
(
self
,
x
):
...
x
=
self
.
ff
(
x
)
...then if the model was an MoE, we'd be getting a tuple -- the actual outputs from
the module and then that extra routing information we were returning.  But if it was
a
FeedForward
, we'd just get the outputs.
I decided that the simplest fix was to change the
FeedForward
module so that it returned
values that were compatible with
MixtureOfExperts
.  The old
forward
, which was
this:
def
forward
(
self
,
x
):
return
self
.
layers
(
x
)
...became
this
:
def
forward
(
self
,
x
):
return
self
.
layers
(
x
),
None
That meant that we could do
this
in place of the
TransformersBlock.forward
code above:
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
If we had an MoE in
self.ff
, then we'd get some real MoE routing info in
this_block_moe_routing_info
, whereas if we were running a normal dense model then
we'd get
None
.
This, by the way, explains the odd bit of code in the
forward
for
MixtureOfExperts
that you might remember from earlier --
this bit
:
this_expert_results
,
_
=
expert
(
xs
[
this_expert_mask
])
expert
there is one of the
FeedForward
modules, so what we're doing there with the
underscore is just
ignoring the
None
that we know we're returning from it.
The next step was to work out how to get the extra
(routing_logits, expert_weights)
information
that we had in
this_block_moe_routing_info
out of the
TransformersBlock
, if
self.ff
was a
MixtureOfExperts
.
Now,
TransformersBlock
is used in an
nn.Sequential
in the
GPTModel
class
here
:
def
__init__
(
...
):
...
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
...
def
forward
(
self
,
inputs
):
...
x
=
self
.
trf_blocks
(
x
)
...
That means that the outputs from the
forward
method of the first one are fed directly in as the inputs
to the second one, and so on.  Additionally,
nn.Sequential
assumes that the forward
method just takes a single input.
What I really wanted at the end of this was a list of
(routing_logits, expert_weights)
pairs,
one for each Transformers layer.  So I decided to pass an accumulating list into
TransformersBlock.forward
(allowing it to be
None
), like
this
:
class
TransformersBlock
(
nn
.
Module
):
...
def
forward
(
self
,
inputs
):
x
,
moe_routing_info
=
inputs
if
self
.
is_moe
and
moe_routing_info
is
None
:
moe_routing_info
=
[]
...and then append whatever routing info came from the (potentially
MixtureOfExperts
)
FFN to that
here
:
if
self
.
is_moe
:
moe_routing_info
.
append
(
this_block_moe_routing_info
)
...and then return it from
TransformersBlock.forward
for the next layer
here
:
return
x
,
moe_routing_info
Then, in
GPTModel
I wanted to return it to whatever called the model for inference.
I didn't want to change the implicit API that I was using -- pass in inputs, get
next-token logits -- so I decided to just attach it to the
logits
like
this
:
class
GPTModel
(
nn
.
Module
):
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
=
self
.
drop_emb
(
x
)
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
logits
.
moe_routing_info
=
moe_routing_info
return
logits
I'm not sure, in retrospect, that "smuggling" the routing info out like that was
the right choice.  Perhaps a Hugging Face-like model where the LLM returns some kind
of "output" class that contains
logits
and other stuff like this as explicit fields would be better.  But this setup seemed
to work for my use case, so I've left it as-is for now, with a mental note to revisit
later.
Next, I modified my training script to store the
moe_routing_info
that we got
when we did our forward pass in a list, and then to store that in the metadata associated
with my checkpoints for later analysis.
The training script I'm using is something I developed after working through Raschka's
book, and it's kind of complicated -- although the core is essentially the same as the
one we use to train our model in chapter 5, I've built it out to allow training
across multiple GPUs
, with all kinds of
tweaks
that I've learned about
since.  So I won't dig into that code in any depth in this post; if you've been following
along with my various training posts in the past, though, and want to see how this
all fits in, you can see the code that accumulates the routing information
here
(note that it uses
detach
so that we don't accumulate compute graph information
over time),
the code that passes those details into the checkpointing function
here
,
and the updated checkpointing function
here
.
So: with those changes, I had a plausible-looking MoE setup.  I was confident that
it would be able to train, but suspected that it would not be able to balance load
between the experts well and would collapse to using a subset of them.
It was time to give it a go.
The first, non-load-balanced, training run
The first question was, what total number of experts, and how many active ones, should
I have?  I was pretty limited by what I could fit into my RTX 3090's VRAM, and what
an appropriate training speed might be, but after a bit of fiddling around I came to
the conclusion that six experts with two active would fit into memory and train reasonably
quickly, and that didn't sound
like a crazy balance.  Mixtral is 8 experts, two active, for example.
I wouldn't be able to
fit in the batch size of 6 that I had used in the past when training 163M-parameter dense models;
the largest batch size I could fit in was 3.
(For those who've been following my previous LLM training,
because I'm using
gradient accumulation
over
16 steps with the microbatch size of 6 -- for a global batch size of 96 -- I could get the same effect,
and fit the MoE into VRAM, by going down to a microbatch size of 3, with 32 gradient
accumulation steps.)
The next question was how many tokens to train for.  As an experiment I kicked it off
with the same 3.2 billion tokens that I would normally
use to train my 163M-parameter models.  I knew that this larger model would need to be
trained on more tokens than that, but I just wanted a reasonably serious run to see how the model
behaved.
The training script predicted that it would take just over two days to complete this experimental run,
which was perfect.  I had reached this point during the late afternoon on a Friday, and had stuff to do
over the weekend that would keep me away from my computer, so that run length would mean that it would be ready for me on Monday.
On Monday, I came back to see that it had completed properly:
Training complete in 217,540.703 seconds
Tokens seen: 3,260,252,160
Throughput: 14,987 tokens/second
Over the training run, the loss declined nicely:
Out of interest, I ran an evaluation script to see how it performed on the
held-back test set that I normally use to compare my models:
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
runs/1xrtx3090-moe-no-balancing/model.json
runs/1xrtx3090-moe-no-balancing/checkpoints/latest/model.safetensors
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
2215
.98it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
05
:28<
00
:00,
9
.73it/s
]
Loss
against
our
test
dataset:
3
.501952
That ranked it better than the 163M-parameter models I'd trained using PyTorch, but
worse than the original GPT-2 small, and also worse than the models I've
trained with JAX
(which I believe got lucky with their initial untrained random weights).  That was
a pretty solid result, but as this was an exploratory training run, there's no point in
putting much weight on it.
For a start, this model was clearly undertrained.  The
number of tokens, 3.2B, was
Chinchilla-optimal
for my 163M-parameter
models, but this one had more than twice the total parameters at 446M, and had
220M active for each token.  Larger models need more tokens to be well-trained.
The more important result was the load-balancing between experts.
I put together a
notebook
to
ingest the metrics that I was writing to the checkpoints, and to create two charts for each
layer:
One showing how well-balanced the logits coming out of the router were -- that is,
for each global step, how close was the model to having every expert getting exactly
the same amount of utilisation in terms of the router's raw numbers.
One showing how well-balanced things were
after
the top-k.  This was a belt-and-braces
thing: you can imagine a router that always favours a particular pair of experts, but only
by a small amount, so the raw routing balance might look reasonably good (say, the two favoured
ones get a probability of 0.2 and the others get 0.15 each), but the favoured
two experts would wind up getting all of the "traffic".
In the charts, for each global step, I plotted a line for each expert; if it had
an average probability less than uniform / 3 -- that is, it was getting less than a third
of the tokens that a perfectly flat distribution across all experts would give it -- then
the line was white, meaning that it was being "starved".  If it was getting a number of tokens between uniform / 3 and uniform * 2 --
then the line
was green, because it was getting what felt like a reasonable number of tokens.  And
finally, if it was higher than uniform * 2, it was plotted in red: it was being overfed.
The charts showed exactly the problem I was expecting to see.  Let's look at layer 0:
You can see that it started off pretty well-balanced, but rapidly came to prioritise
expert 5; the remainder of the probability distribution looks like it must have been
scattered over the other experts, with a slight preference for expert 3.
The other layers came back with similar issues: certain experts were strongly preferred
while others were starved:
So the problem was real.  The model was relying heavily on some experts and ignoring
others.  We needed to do extra stuff to balance the load
across the experts.
Load-balancing, the Switch way
The problem with load-balancing across experts has been clear for quite some time, and
it was covered in "Outrageously Large Neural Networks" back in 2017.  The solution they used is simple, and clever:
define an "auxiliary" loss, which goes up as the experts become more unbalanced, and
down as they become more balanced.  You can then add that (scaled by some amount) on to the normal
cross entropy loss
that you get
by comparing the outputs from your model to the training targets, to get a combined
loss number -- and then you back-propagate using that combined loss.
By reducing the combined loss, then you optimise both for correctness -- is the model
doing its job as an LLM -- and for balance across the experts.  Of course, you need to be
careful about the scaling factor that you use to adjust the auxiliary loss before adding it.
If it's too small, then the load-balancing will be de-prioritised and you can wind up with
imbalanced experts anyway.  But if it's too large, the training process will prioritise
balance over quality of the output, and you'll wind up with a crappy model that balances
load across the experts beautifully.  We'll come back to that shortly.
The "Outrageously Large Neural Networks" paper's particular calculations for the auxiliary loss are a little complicated -- they
generate two separate numbers and combine them -- and it was simplified in the GShard
paper, and then again in Switch Transformers.  I found the last of those reasonably
easy to understand, and decided to adapt it.
Let's start off with their formalisation -- but keep in mind that they had only one
active expert per context vector, so we'll need to make some changes.
Firstly, they define a per-expert number,
f
i
-- the
i
subscript means that it's
for expert
i
.
f
i
=
1
T
∑
x
∈
ℬ
1
{
argmax
p
(
x
)
=
i
}
That's a little intimidating-looking but is much simpler than it looks.
They define it as "the fraction of tokens dispatched to expert
i
", and in that light we
can interpret it.
The
x
∈
ℬ
that we're iterating over in the
∑
is basically:
for x in batch_context_vectors:
So, the stuff inside the
∑
is done once for each of our input context vectors
across all sequences in a batch.
The
1
{
.
.
.
}
(which should be rendering with a kind of
doubled-1 -- Chrome, as of this writing, doesn't handle that, though Firefox does) is meant to mean
"1 if the condition in the braces is true, 0 if it's false".
In
argmax
p
(
x
)
=
i
, the function
p
is the "raw" probabilities from our
router.  As I mentioned earlier, they were doing softmax and then zeroing out the
non-top-
k
values, so they had those raw numbers available.  We'll come back to that
in a moment.
But for now, the condition inside
the
1
{
.
.
.
}
just means "true if this expert was the
top one for this particular incoming context vector, false otherwise".
Putting that all together, then we're just counting the number of tokens in our batch
for which expert
i
is the top pick of the routing network.
The
1
/
T
at the start then divides that
by the number of tokens in the batch (which is what they mean by
T
), and for a network
with one active expert like the Switch Transformers ones, we've got -- as they say --
"the fraction of tokens [in this batch] dispatched to expert
i
".
So that works nicely in the one-active Switch Transformers world.
But we can fairly simply extend it to handle multiple active experts, while keeping
similar semantics.  Let's say that we calculate how many of the context vectors in
a batch were sent to expert
i
; we can divide that by the number of tokens to get
something equivalent.  It still means "the fraction of tokens dispatched to expert
i
".
(Ab)using their notation, if we say that our number of active experts is
k
, then it might
look something like this:
f
i
=
1
T
∑
x
∈
ℬ
1
{
is-in-top-k
(
p
(
x
)
,
i
)
}
Let's run with that for now.
As well as
f
i
, they define another
per-expert number,
P
i
:
P
i
=
1
T
∑
x
∈
ℬ
p
i
(
x
)
They describe this as "the fraction of the router probability allocated for expert
i
".
Again, we're iterating over every context vector in every sequence in the batch -- but here we're just adding
together all of the raw probabilities for the expert for each one, then dividing by
the number of elements in the batch.  In other words, we're working out the expert's average probability
across the entire batch.  Much easier!  And in our multiple-active-expert world,
their equation works -- it means exactly the same thing.
Now, both of these calculations, as they're expressed in the maths, depend on something
that we're not currently calculating.  Remember, Switch Transformers worked out the weights
for each expert by doing a softmax across all of the raw logits that came out of the
router's linear layer, then zeroing out the ones that were not in the top-
k
-- that
is, for their
k
=
1
setup, all but the highest (argmax) one.  So they had those "raw" softmaxed probabilities
knocking around.
But because we are replacing the non-top-
k
logits with
−
∞
and then doing
softmax, our router weights aren't the same -- they're just the relative probabilities
of our selected
k
experts.
For
f
i
that doesn't matter; we can use our weights and easily identify the experts
that were routed to for a given element in the batch, because they're the only ones that
are not zero.
But for
P
i
we do need the pre-top-
k
's logits from the router.  And, not entirely
coincidentally, we already have the code to make that available!  In order to do those charts above
-- the ones showing where experts were being starved and when they were being over-fed
in the non-load-balanced training run --
we passed the raw, non-top-
k
'ed, non softmaxed router logits, and the expert weights
after the top-
k
and the softmax, out of the
MixtureOfExperts
module's
forward
:
class
MixtureOfExperts
(
nn
.
Module
):
...
def
forward
(
self
,
xs
):
...
return
all_outputs
,
(
routing_logits
,
expert_weights
)
...and then added code to feed that through to the training loop because it was needed for the
metrics that we used to generate those charts.  The numbers that we kept for the "raw" side of things were the logits rather than the actual
probabilities, but we can fix that with a simple softmax.
So that means that in our training code, we already had the numbers to work out
P
i
and
f
i
for
our experts.
They needed to be combined to make up a single scalar auxiliary loss for the model when run
over a batch, and Switch Transformers does that like this:
loss
=
α
·
N
·
∑
i
=
1
N
f
i
·
P
i
If you imagine
f
as a vector containing all of the per-expert
f
i
s,
and
P
as a similar one containing the
P
i
s, then that
∑
is a simple dot
product,
f
·
P
.
They then scale that up by the number of experts
N
, multiply by a scaling
factor -- the one I mentioned earlier to balance load-balancing auxiliary loss against
"real" cross entropy loss -- which they call
α
.  (We'll come back to
α
later.)
So, we have a set of calculations to work out an auxiliary loss; there are a few extra
things I'd like to highlight before we dive in to the code.
The auxiliary loss for perfect router balance
Let's imagine what a "perfect" router would look like from the perspective of these
calculations, firstly for the Switch-style one-active-expert model, and then for our
own more general case.
Starting with
f
i
; it's the number of tokens in the batch for which expert
i
is the chosen
one, divided by the number of tokens in the batch.  We want all of our experts to get the
same amount of "traffic", so for
N
experts, one active per token, clearly each one will be active
1
/
N
of the time.
So that should be the value of
f
i
if everything is balanced.
Now let's think about
P
i
.  Again, we want each expert to receive
1
/
N
of the
tokens -- so its average probability should also be
1
/
N
.
So, that means that for perfect balance, all of our
P
i
s and all
of our
f
i
s should be
1
/
N
.  That means that
when we do the
∑
in that loss calculation to work out the dot product, then
for a perfectly balanced router, each one will contribute:
f
i
·
P
i
=
1
N
·
1
N
=
1
N
2
There will be
N
of them, so that will come to
1
N
2
·
N
=
1
N
...and then we're multiplying by
N
to get the loss, so the result (disregarding
the scaling factor
α
) will be
1
.
So, when balance across the experts is perfect, the Switch Transformers auxiliary loss has a value of
1
.
However, they have only one active expert, and our equation is slightly different
to allow for the fact that we have
k
of them.
I won't go through the boring derivation again, but if we replay the maths above
with
k
active experts, we get an auxiliary loss for the ideal, perfectly balanced
router of
k
.
That's not a problem in and of itself -- after all, this is just a number we're trying
to minimise, and it's not super-important what we're trying to minimise it to.  But
it does matter when we're talking about
α
, because if the auxiliary loss is larger, we'll need to
scale it down more to stop it from "drowning out" the signal from the actual training loss.
The Switch Transformers paper explains
what values they used for the scaling, but ours will be different because of the
different number of active experts.
Layers
The auxiliary loss calculation above only covers what happens in one layer, so we need
to work out how to combine the contributions from all of the layers.  In the paper, the only mention they make of multiple layers
in this context is:
For each Switch layer, this auxiliary loss is added to the total model loss during training
I took that to mean that we just sum up the scaled auxiliary loss across all layers and then
add that sum to the normal cross entropy loss.  I think that's the most natural interpretation
of what they are saying.
So -- given the value of
k
for a perfectly-balanced router that I
worked out above -- for the model I was planning to train, with 2 active experts, 12 layers,
the auxiliary loss before scaling by
α
would be 24.
This, by the way, is where my implementation differs from Mixtral's -- or, at
least,
the Hugging Face source code
for it as of this writing.
In that, they do something that feels a bit odd.  They treat (for example) expert 1
on layer 1 as being the same as expert 1 on layer 2, and so on throughout the layers,
then do the calculations just once.  That feels
a bit dodgy.  After all, you can imagine that expert 1 on layer 1 might be being
starved but its equivalent on layer 2 might be getting overfed, and the two would
balance out.
I don't know if that's an error in that implementation, or if there's something
I'm missing.  Conceivably I might test it some day by training another model using
their loss function, but I suspect I won't get around to that.
Differentiability
There's also something that made me hesitate a bit in the Switch Transformers paper,
and which I think I still need to ponder a bit.  That calculation for
f
i
:
f
i
=
1
T
∑
x
∈
ℬ
1
{
argmax
p
(
x
)
=
i
}
...did not look differentiable to me.  Things like
argmax
(and our own
equivalent's
is-in-top-k
) are generally not.
Indeed, they confirmed that shortly after
defining it, but in a way that gave me pause:
The objective can also be differentiated as
  the
P
-vector is differentiable, but the
f
-vector is not.
The "objective" they're referring to is the auxiliary loss, and it makes me a bit uncomfortable that
something that is defined in terms of A and B is differentiable if A is, but B isn't.
My hand-wavy way of thinking about it right now is that the undifferentiable bit
can be treated as a constant, so as long as part of the calculation is differentiable,
the whole thing can be treated as such.  But I'm not 100% happy with that, and need
to think further.
But now, I think, we've covered the maths for the auxiliary loss, so it's time to
dive into the code!
The code for auxiliary loss
My old training loop had the following
code
to do the forward then the backward pass:
if
use_amp
:
with
torch
.
amp
.
autocast
(
device_type
=
device
.
type
,
dtype
=
torch
.
float16
):
logits
=
model
(
inputs
)
train_loss
=
calculate_loss
(
logits
,
targets
)
else
:
logits
=
model
(
inputs
)
train_loss
=
calculate_loss
(
logits
,
targets
)
is_last
=
accumulation_step
==
gradient_accumulation_steps
-
1
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
Let's strip out all of the extra enhancements that I have accumulated there on top of the simple
training code from the book; there's
AMP
,
DDP
and
gradient accumulation
and if we remove that it would simply look like this:
logits
=
model
(
inputs
)
train_loss
=
calculate_loss
(
logits
,
targets
)
train_loss
.
backward
()
Hopefully that's familiar!
What I wanted to do was add in the auxiliary loss (if we were training an MoE), scaled by
that
α
scaling factor.  What I came up with (and again, here I've stripped out
all of the stuff required by those enhancements):
logits
=
model
(
inputs
)
train_loss
=
calculate_loss
(
logits
,
targets
)
if
hasattr
(
logits
,
"moe_routing_info"
)
and
logits
.
moe_routing_info
is
not
None
:
moe_router_loss
=
calculate_moe_router_loss
(
logits
.
moe_routing_info
)
moe_router_losses
.
append
(
moe_router_loss
.
item
())
else
:
moe_router_loss
=
0
total_loss
=
train_loss
+
moe_router_loss
*
moe_router_loss_scale
total_loss
.
backward
()
Note that I wanted to keep track of the router losses in that
moe_router_losses
list as well in order to monitor
them as the training run progressed, just like I normally monitor training loss (as you
can see in the loss chart above).
That's all pretty nice and simple -- if we are getting MoE routing info back from
the model, then we call this new
calculate_moe_router_loss
to work out the loss
from the maths in the last section, and then add it on, scaled by
moe_router_loss_scale
, which is what I decided to call the
somewhat-opaquely-named
α
from the Switch Transformers paper.
Adding all of the
AMP, DDP and gradient accumulation gubbins back in, the final code looked like
this
:
with
torch
.
amp
.
autocast
(
device_type
=
device
.
type
,
dtype
=
torch
.
float16
)
if
use_amp
else
nullcontext
():
logits
=
model
(
inputs
)
train_loss
=
calculate_loss
(
logits
,
targets
)
if
hasattr
(
logits
,
"moe_routing_info"
)
and
logits
.
moe_routing_info
is
not
None
:
moe_router_loss
=
calculate_moe_router_loss
(
logits
.
moe_routing_info
)
moe_router_losses
.
append
(
moe_router_loss
.
item
())
else
:
moe_router_loss
=
0
is_last
=
accumulation_step
==
gradient_accumulation_steps
-
1
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
total_loss
=
train_loss
+
moe_router_loss
*
moe_router_loss_scale
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
total_loss
/
gradient_accumulation_steps
)
.
backward
()
else
:
(
total_loss
/
gradient_accumulation_steps
)
.
backward
()
So that was simple enough (for LLM-training values of simple).
The code to route the
moe_router_loss_scale
from the
training configuration file is not really worth going through, and nor is the
code to save average, minimum and maximum values from
moe_router_losses
into the
checkpoint metadata, or to chart those (though I'll show the charts later).
The interesting bit is, of course, that
calculate_moe_router_loss
function.
It's
here
and looks like this:
def
calculate_moe_router_loss
(
moe_routing_info
):
total_routing_loss
=
0
for
routing_logits
,
expert_weights
in
moe_routing_info
:
batch_size
,
seq_len
,
num_experts
=
expert_weights
.
shape
flattened_expert_weights
=
expert_weights
.
view
((
batch_size
*
seq_len
,
num_experts
))
expert_active_counts
=
(
flattened_expert_weights
>
0
)
.
sum
(
dim
=
0
)
expert_frequencies
=
expert_active_counts
/
(
batch_size
*
seq_len
)
raw_routing_weights
=
torch
.
softmax
(
routing_logits
,
dim
=-
1
)
flattened_raw_routing_weights
=
raw_routing_weights
.
view
((
batch_size
*
seq_len
,
num_experts
))
expert_prob_allocation
=
flattened_raw_routing_weights
.
sum
(
dim
=
0
)
/
(
batch_size
*
seq_len
)
layer_routing_loss
=
num_experts
*
torch
.
dot
(
expert_frequencies
,
expert_prob_allocation
)
total_routing_loss
+=
layer_routing_loss
return
total_routing_loss
Let's look at it from the outside in.
We start with a list called
moe_routing_info
.  Remember, this has been passed
back from the MoE model for a single forward pass of a batch.  It contains one item
for each Transformers layer in the model, and those items are pairs of
(routing_logits, expert_weights)
.
We start off with a total routing loss of zero, and then for each layer, we do some stuff
to work out its routing loss, and then at the end of the loop, we add it on to our
running total.  Finally, we return the total.
Obviously, the fun stuff is inside the loop :-)   It's time for some of those
tensor diagrams again.
Let's remind ourselves of the shape of
expert_weights
:
Diagram 13
(repeated):
expert_weights
as two 2-D views
Each cell on the front face relates to one context vector in one sequence in our batch, and the "core" going
into the cuboid from there (horizontally along the side view) is the weights we actually used when routing the context vector
in question to the experts -- zero for unselected experts, some value between zero and one
for the selected ones.
Now let's go back to the code for a moment.
We start off by using the shape of
expert_weights
to work out what our different
dimensions are:
batch_size
,
seq_len
,
num_experts
=
expert_weights
.
shape
Then we do our first block of calculations, trying to work out
f
i
from the maths,
"the fraction of tokens dispatched to expert
i
"
We want to do this efficiently with a vector calculation, working out all of
the
f
i
s (remember, there's one for each expert) in parallel.
Our first step is to flatten out the
(batch_size, seq_len)
grid into a single
dimension -- essentially stacking all of the front view's columns on top of each other to make just one long
column, like this:
Diagram 20
:
expert_weights
flattened, as two 2-D views
...or, more simply, as it's now just a 2-D Tensor, like this:
Diagram 21
:
expert_weights
flattened, as one 2-D view
We can use PyTorch's
view
method to do that without having to copy any data around in memory -- as the name suggests,
it just returns a different view on the same data:
flattened_expert_weights
=
expert_weights
.
view
((
batch_size
*
seq_len
,
num_experts
))
Now, remember that these are the expert weights.  Each one of those cells contains
a number -- zero if the expert was not selected for the context vector that corresponded
to it in the original layout, or some non-zero number if it was.  So if we do this:
flattened_expert_weights
>
0
...then we'll get a tensor of the same shape, where we have
True
if the weight was
more than zero (that is, the expert was active for that context vector),
False
otherwise.
And that means that if we sum down those columns in
diagram 21
, we'll get a new grid of one row,
and
num_experts
columns, which represents the total number of times each expert was active
in the given batch:
Diagram 22
:
expert_active_counts
as one 2-D view
So, in code, we can just do this:
expert_active_counts
=
(
flattened_expert_weights
>
0
)
.
sum
(
dim
=
0
)
If we divide that by the number of context vectors in the batch, we've got a new
tensor, a row with
num_experts
columns -- the same shape as
diagram 22
-- containing exactly what we want:
expert_frequencies
=
expert_active_counts
/
(
batch_size
*
seq_len
)
That is,
expert_frequencies
is a vector
f
in terms of the maths, containing
all of the
f
i
s that we want for our auxiliary loss calculation -- that is, all
of the result across all experts for this:
f
i
=
1
T
∑
x
∈
ℬ
1
{
is-in-top-k
(
p
(
x
)
,
i
)
}
The calculations for the
P
i
s are very similar.  We start off with
routing_logits
like this:
Diagram 7
(repeated):
routing_logits
as two 2-D views
So, each cell on the front face relates to one context vector, and the "core" going
into the cuboid from there is the set of raw routing logits for that context vector,
one number per expert.
Firstly we need to convert
the
routing_logits
into probabilities by running them through softmax, along the
last dimension -- the
num_experts
one that is the horizontal axis on the side view:
raw_routing_weights
=
torch
.
softmax
(
routing_logits
,
dim
=-
1
)
Then we do the same trick with
view
to convert the result to a single column
of lists of length
num_experts
(metaphorically) -- the same shape as in
diagram 21
:
flattened_raw_routing_weights
=
raw_routing_weights
.
view
((
batch_size
*
seq_len
,
num_experts
))
Now if we add them up across the rows like this:
flattened_raw_routing_weights
.
sum
(
dim
=
0
)
Then we get a single row,
num_experts
column result that has, for each expert, the sum of
all of the probabilities it had across all of the context vectors in the batch,
just like the one we had in
diagram 22
.
We can divide that by the number of context vectors in the batch:
expert_prob_allocation
=
flattened_raw_routing_weights
.
sum
(
dim
=
0
)
/
(
batch_size
*
seq_len
)
...and that's our vector
P
containing all of the
P
i
s, where each is one of these:
P
i
=
1
T
∑
x
∈
ℬ
p
i
(
x
)
Finally, we can multiply all of the
f
i
s and their corresponding
P
i
s by
each other, and sum the results, by using a dot product, and then multiply the result by the number
of experts:
layer_routing_loss
=
num_experts
*
torch
.
dot
(
expert_frequencies
,
expert_prob_allocation
)
...and that's this bit done (apart from the
α
):
loss
=
α
·
N
·
∑
i
=
1
N
f
i
·
P
i
And that's our auxiliary code wrapped up!  We've been through
calculate_moe_router_loss
,
and we've already seen the code that scaled it by
α
aka
moe_router_loss_scale
,
so we have a training script with MoE auxiliary loss using the maths in the last section!
Again, I hope that the diagrams helped with that workthrough.  The code is the kind of
thing where it's easy to scan through and get a vague understanding, but I think that
visualising what's going on step-by-step is important if you want it to really stick.
With the code in place, the next thing to do was to explore what the right value
might be for
α
.
Seeking alpha
In the "Switch Transformers" paper, they say:
Finally, a hyper-parameter
α
is a multiplicative
  coefficient for these auxiliary losses; throughout this work we use an
α
=
10
−
2
which was
  sufficiently large to ensure load balancing while small enough to not to overwhelm the
  primary cross-entropy objective. We swept hyper-parameter ranges of
α
from
10
−
1
to
10
−
5
in powers of
10
and found
10
−
2
balanced load quickly without interfering with training loss.
But, as I noted earlier, that worked for them with their single active experts, but
because I had multiple, my auxiliary loss would be larger.  Now, given that their
"ideal" per-layer loss was 1, and mine was 2 for my planned training run, it sounded
like using half of their recommended value,
5
×
10
−
3
, would be appropriate.
However, I was also a little
concerned about the number of layers interfering with things.
The auxiliary loss, as we saw above, was a single value per layer, all of which were
added together.  With my "ideal" per-layer loss of 2, and 12 layers, that meant that
the ideal across all layers was 24.
Now, they mentioned a specific value for
α
, but didn't mention the number of
layers they had, or if they swept for different possibilities across different numbers
of layers.  That seemed strange!
I decided to work on the hypothesis that they had found that as the number of layers increased, you needed
the total contribution of the auxiliary loss to scale up in proportion.  That was only
a guess based on trying to fit together the info in the paper, though, and could well be
wrong.
I was in enough doubt, though, that I felt it would be wise to do my own, minimal sweep
over a few values for
α
.  For each, I'd do a one-hour training run.  At the end
I'd check the training loss -- that is, the pure cross entropy loss saying how well
the model was doing at its real purpose of modeling language -- and the auxiliary
loss, showing how well-balanced its usage of experts was.
I got these results:
α
Training loss
Auxiliary loss
0
6.152867
53.38285
0.001
6.166725
30.00601
0.005
6.106290
25.21015
0.01
6.160989
24.78106
I also generated router usage maps like the ones I gave way back in this post for the two-day
training run with no auxiliary loss.  I won't put them all in there, but:
With
α
=
0
, as you'd expect to see from the very high auxiliary loss, things
started going red and white pretty quickly -- it was focusing on specific experts
and ignoring others.  It didn't do too badly on training loss, though.
With
α
=
0.001
, one tenth of the Switch Transformers number (and one fifth
of what you'd expect to be ideal for ours by converting it naively), the load-balancing
charts weren't quite so bad, but there was a
speckling of red.  I couldn't say for sure that it might not have managed to keep
things reasonably balanced in a longer training run.
α
=
0.005
, however, looked really good!  It actually had the lowest (best) training loss
out of any of these options, and the auxiliary loss was not too bad, only 1.2
above the ideal value of 24.
By the time we got to the
α
=
0.01
that was used by Switch Transformers (with
their ideal auxiliary loss values that were half of ours), although the auxiliary
loss continued downwards, training loss started worsening.  This was certainly in line with what I would expect
to see if the training started prioritising balance over actually creating a good
LLM.
So, on the basis of those results (and, of course, the fact that it fit well with
the Switch Transformers paper's recommendation), I decided to use
α
=
0.005
.
It was time to train this thing!
The training run
I decided not to think too hard about the right number of tokens to train it on.
The Chinchilla number, 20 times as many tokens as parameters, is a heuristic that
works for dense models, but is not meant for MoEs.  You'd intuitively think that the
"ideal" number of tokens to train a model with 446,410,752 parameters, 219,697,152 active
per token would be somewhere between the Chinchilla-optimal numbers for those two
parameter counts.
But overtraining isn't necessarily a bad thing, so long as it's on non-duplicated
data (or
less than four epochs over the same data
),
and I had a 10B token dataset all set up from my previous experiment.  So training
it on what would be the Chinchilla-optimal number of tokens if it was just a
446,410,752-parameter dense model didn't sound like a bad idea, so long as I could
do it in a reasonable amount of time.
That meant 8,928,215,040 tokens, which I had in my normal training dataset without needing multiple
epochs.
A quick check -- running the training script with that number of tokens configured
-- told me that it would take 90,823 global steps to complete, over about eight days.
It looked like each
checkpoint would take up 5.3GiB, and I had about 348 GiB free on my disk, so I calculated
that I could checkpoint every 1,500 global steps -- that would work out as roughly once
every three hours.  Not great, but losing a maximum of three hours work in the case of
a power outage (or cat jumping onto the PC's power button) is not the end of the world.
So I set things up with
this model configuration
and
this training configuration
,
and on my dedicated training box,
poppy
, I kicked it off:
giles@poppy:~/Dev/ddp-base-model-from-scratch
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
1xrtx3090-moe-first-proper-run
datasets/
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
3517
.97it/s
]
moe_router_loss_scale
=
0
.005
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
/90823
[
00
:07<?,
?it/s,
loss
=
10
.963,
tps
=
12
,635
]
Checkpoint

Continuing
training
0
%
|
▏
|
155
/90823
[
19
:32<
190
:23:52,
7
.56s/it,
loss
=
7
.407,
tps
=
12
,999
]
Just less than eight days later, it completed:
100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 90823/90823 [190:13:38<00:00,  7.54s/it, loss=3.377, tps=13,040]
Training complete in 684,818.520 seconds
Tokens seen: 8,928,264,192
Throughput: 13,037 tokens/second
Final train loss: 3.211
The loss chart looked like this:
You can see that the normal cross entropy loss (just tagged as "loss" on the chart)
decreases nice and smoothly from random (about 10.82 with the GPT-2 tokeniser) down
to that final training loss of 3.211, with only a couple of tiny spikes.
I've also plotted the auxiliary loss for the MoE routing, on the right-hand Y axis,
and you can see that while near the start there were a few bumps (and the max values
for single iterations spiked up from time to time), the average was generally pretty
close to 24, our "ideal" number.  Indeed, for the last checkpoint, the average over
all iterations was an almost-perfect 24.0847.
The
notebook
that I
had to plot layer-by-layer expert starving/overfeeding came back with some lovely
green plots showing nice even routing, too:
A couple of issues near the start of the run, but for the last 75% of it, they're all a sea of
green.  Lovely.
I ran my normal
smoke test
, based on Raschka's from the book: what do you get if you ask
your model to complete "Every effort moves you" with 20 tokens, with a temperature of
1?
Every effort moves you closer towards your goals and the results. But the good news is that you are more likely to get
Reasonably coherent!  It was time to do some evals and comparisons.
The results
I ran my normal
loss eval
: on a held-back test set of 19,200
sequences of 1,024 tokens each, what was the model's average loss?
giles@perry:~/Dev/ddp-base-model-from-scratch
(
main
)
$
uv
run
test_loss.py
datasets/
runs/1xrtx3090-moe-first-proper-run/model.json
runs/1xrtx3090-moe-first-proper-run/checkpoints/latest/model.safetensors
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
1515
.56it/s
]
100
%
|
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
3200
/3200
[
05
:41<
00
:00,
9
.38it/s
]
Loss
against
our
test
dataset:
3
.253928
Comparing this against other models that I've trained, and the OpenAI GPT-2
small and medium weights, we get this (it's in bold):
Params
Test loss
OpenAI weights: medium
345M
3.231442
PyTorch MoE, 6 experts, 2 active
446M/220M
3.253928
JAX, overtrained one long epoch
163M
3.324953
JAX, overtrained two normal epochs
163M
3.326482
JAX, with MHA bias, no dropout
163M
3.418784
JAX, no MHA bias, no dropout
163M
3.420089
JAX, no MHA bias, with dropout
163M
3.476802
OpenAI weights: small
124M
3.499677
1xrtx3090-stacked-interventions
163M
3.538161
8xa100m40-stacked-interventions-1
163M
3.577761
Cloud FineWeb, 8x A100 40 GiB
163M
3.673623
1xrtx3090-baseline
163M
3.683835
8xa100m40-baseline
163M
3.691526
Cloud FineWeb, 8x H100 80 GiB
163M
3.724507
Cloud FineWeb, 8x A100 80 GiB
163M
3.729900
Cloud FineWeb, 8x B200 160 GiB
163M
3.771478
Local FineWeb train
163M
3.943522
Local FineWeb-Edu extended train
163M
4.134991
Local FineWeb-Edu train
163M
4.166892
Not too bad, though not amazing.  It was better than any of my 163M-parameter models,
and OpenAI's GPT-2 small.  But it was a bit worse than (but close to) the 345M-parameter
OpenAI GPT-2 medium, which has fewer parameters -- albeit more active ones per token.
I decided to do a second eval.  I have one that I call the IFT test -- fine-tune
the model on an instruction-following dataset, until loss starts rising on its
held-back eval dataset, then run a test set through to get answers to questions
the model has not yet seen.  I then bundle together the responses from a bunch of
models and ask GPT 5.5 to compare them.  It's an extension of Raschka's example in
chapter 7 of the book, modified to make it easier to compare different models.
You can see the scripts
here
and
here
,
and there are more details
here
.
I kicked off the first script, to fine-tune the model and get its responses, and
then handed that plus a bunch of responses from other models to the LLM for it
to compare them.  The results came back like this (note this this is sorted by loss,
the "IFT rank" column is how well it did comparitively in the eval):
Test loss
IFT epochs
IFT score
IFT rank
OpenAI weights: medium
3.231442
2
42.54
1
PyTorch MoE, 6 experts, 2 active
3.253928
4
22.71
3
JAX, overtrained one long epoch
3.324953
3
18.71
6
JAX, overtrained two normal epochs
3.326482
4
19.14
5
JAX, with MHA bias, no dropout
3.418784
4
18.40
7
JAX, no MHA bias, no dropout
3.420089
5
20.83
4
JAX, no MHA bias, with dropout
3.476802
5
13.04
16
OpenAI weights: small
3.499677
2
24.95
2
1xrtx3090-stacked-interventions
3.538161
4
13.30
15
8xa100m40-stacked-interventions-1
3.577761
4
10.33
19
Cloud FineWeb, 8x A100 40 GiB
3.673623
3
16.62
8
1xrtx3090-baseline
3.683835
4
15.20
10
8xa100m40-baseline
3.691526
3
14.15
11
Cloud FineWeb, 8x H100 80 GiB
3.724507
4
13.76
14
Cloud FineWeb, 8x A100 80 GiB
3.729900
3
10.98
18
Cloud FineWeb, 8x B200 160 GiB
3.771478
4
14.07
13
Local FineWeb train
3.943522
5
12.45
17
Local FineWeb-Edu extended train
4.134991
5
14.11
12
Local FineWeb-Edu train
4.166892
5
15.49
9
As you can see, the correlation between loss and performance on this eval is interestingly
loose -- I have an ongoing series trying to work out
why that might be
.
In particular, OpenAI's weights consistently outperform mine, and I'm determined to find out
why.
But it was reassuring, at least, that the new, big model came in at rank 3, beating all of my other ones,
even if it still lost to that pesky 124M-parameter OpenAI GPT-2-small.
So, there we have it: a GPT-2 small model converted to an MoE with 6 experts per layer,
2 active per token.  Its loss on the test set is pretty much where you'd expect,
and its IFT eval makes sense, modulo the OpenAI weights weirdness.
What does that mean, and what should come next?
Conclusion
In this post, I started with the GPT-2 code from
"
Build a Large Language Model (from Scratch)
",
and my own training script (which was originally based on the training code from the book),
added on mixture of experts support including the auxiliary loss calculations that you need
to make it balance load across its experts properly.  After eight days of training,
we wound up with a decent, capable model.
So that's all quite satisfying in an intellectual sense, and -- at least in terms
of how well it did on the test loss -- it landed pretty much where you might expect.
And one thing I'm sure of is that grinding through the calculations has been a great
work-out for my skills with PyTorch and tensor operations.
But the interesting thing about MoEs is that they -- in theory -- provide similar
performance to dense models, at a lower cost in inference computing time.
I think there are some interesting follow-up experiments I can do.  OpenAI's weights
tend to beat mine, so if I exclude them from comparisons (until I've worked out why),
I could try to build a mental model for whether MoEs are a good way to spend my
scarce computing resources when learning more about LLMs.  I could:
Train a small model (say, the 163M-parameter size I've been messing with so far)
on the same amount of compute as I spent on the MoE.  How would it perform?
My guess is that it would be worse.
Train a dense 446M-parameter model on the same amount of compute and see how it matches
up.  It would be undertrained (it would need more calculations
per token, so if I matched the compute, I'd have to train it on fewer tokens).
I don't know if it would be better or worse.
Train a Chinchilla-optimal dense model on the same amount of compute, and see how
that did.
I'm sure there are other options, and I'd love to hear people's thoughts on what they might be.
Anyway, I hope this post has been an interesting journey, and explained things well.
Any feedback much appreciated -- in particular, on whether the diagrams helped.  I
only recently
added D2 support
to my static site generator, and
it's entirely possible that I was overusing my new toy :-)
So: thanks for reading, and as always, comments and questions are very welcome in the
comments below.
Citing this post
This is a blog, and if you want to link to this post then please do :-)
                However, if you're writing something more academic and need to do
                a proper citation, then here's a BibTeX block to make things easier.
@misc{thomas2026sep-gpt-2-to-moe,
  author       = {Thomas, Giles},
  title        = {{Extending Raschka's GPT-2: an MoE trained from scratch on an RTX 3090}},
  year         = {2026},
  month        = sep,
  howpublished = {Blog post},
  url          = {https://www.gilesthomas.com/2026/09/gpt-2-to-moe},
}
