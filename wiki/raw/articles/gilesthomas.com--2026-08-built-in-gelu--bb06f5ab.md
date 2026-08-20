---
title: "Use the built-in GELU, don't roll your own!"
url: "https://www.gilesthomas.com/2026/08/built-in-gelu"
fetched_at: 2026-08-20T10:00:47.140016+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Use the built-in GELU, don't roll your own!

Source: https://www.gilesthomas.com/2026/08/built-in-gelu

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
Unsurprisingly,
PyTorch's own built-in GELU function
is faster than the hand-rolled one I've been using to date.  But I
was
surprised at
how
much
faster using it made things when training my models.  I discovered this
accidentally just now while working on something unrelated, but am logging the details
here for anyone else that might find it useful.
The headline numbers: the same code, training the same model on the same data, ran
at about:
21,000 tokens per second using the hand-rolled GELU from
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
".
25,000 tokens per second using PyTorch's built-in GELU with no arguments.
25,000 tokens per second using the built-in GELU with
approximate="tanh"
, which
uses the same maths as Raschka's version under the hood.
That's a 20% increase in throughput for both of the built-in versions -- definitely nothing to be sneezed at.
And what is particularly
interesting is that there aren't that many GELUs going on -- it's a GPT-2 small-style
model, with 12 layers.  So that's 12 GELUs handling tensors
shaped
(batch_size, seq_len, 4 * d_emb)
, which is
(6, 1024, 3072)
for my training setup.
Given that the rest of the model is doing all of the normal full attention stuff for GPT-2, it's
really
surprising that the GELUs alone must have been taking up so much of the time.  The throughput
numbers mean that we must have been spending about 17% of our time on the extra overhead from the hand-rolled
version, so that sets a lower bound for how much time the GELUs were taking up.
More info below the fold.
Back when I was doing the "interventions" part of my
LLM from scratch series
, training
dozens of GPT-2 small-sized models in the cloud and on my local machines, to keep things simple I used
the original model code from Raschka's book.
That happens to have its own implementation of the GELU function --
you can see
my copy here
.
I'm not that sure why the hand-rolled version is in there -- he covers the maths, but the specific implementation isn't explained
in that much depth, and it seems rather like boilerplate, just a "type this in and use it"
kind of thing.  By contrast, for example, while he does explain the maths behind cross-entropy loss in similar detail,
we use the built-in function for it rather than coding it up ourselves.
When I switched to using JAX for
my own from-scratch implementation
,
I decided to not bother porting the boilerplate, and just used
JAX's own built-in version
.
I was revisiting the PyTorch code -- I'm in the process of extending it with mixture-of-experts
support, about which more in a later post -- and decided to switch from the hand-written GELU to the PyTorch one just to
tidy things up a bit.
I noticed something interesting -- my new MoE code suddenly seemed to speed up.
Was that a mirage?  Or had I discovered part -- or even all -- of the reason why the
JAX code was so much faster than the PyTorch code?  With PyTorch, I was typically
getting training speeds of about 21,000 tokens per second, while in JAX I was getting 24,000 tps or so.
I'd been chalking that up to JAX's JIT compilation, but could it have been just a result
of a random implementation choice I'd made?
I did three partial test training runs, letting each one run for 20 minutes to allow the
training speed to settle down from any startup overhead.  Firstly, with the old
hand-coded GELU:
giles@poppy:~/Dev/ddp-base-model-from-scratch
((
HEAD
detached
at
16dd249
))
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
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
4
/4
[
00
:00<
00
:00,
3173
.90it/s
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
19
,982
]
Checkpoint

Continuing
training
1
%
|
▊
|
257
/33165
[
20
:07<
42
:53:57,
4
.69s/it,
loss
=
6
.570,
tps
=
20
,920
]
So it was getting 20,920 on average over those 257 global steps.  That speed was in line with
the original run
of the configuration I was using.
Next, I introduced the built-in PyTorch GELU with no arguments:
-
-class GELU(nn.Module):
-
-    def forward(self, x):
-        return 0.5 * x * (1 + torch.tanh(torch.sqrt(torch.tensor(2.0 / torch.pi)) * (x + 0.044715 * torch.pow(x, 3))))
-
-
-
class FeedForward(nn.Module):
def __init__(self, cfg):
super().__init__()
self.layers = nn.Sequential(
nn.Linear(cfg["emb_dim"], cfg["emb_dim"] * 4),
-            GELU(),
+            nn.GELU(),
nn.Linear(cfg["emb_dim"] * 4, cfg["emb_dim"])
)
That does the full calculations for GELU, rather than using the
tanh
-based approximation that
the hand-rolled code did.  After 20 minutes, it looked like this:
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
1xrtx3090-baseline
datasets/
Fetching
4
files:
100
%
|
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████
|
4
/4
[
00
:00<
00
:00,
11222
.22it/s
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
23
,953
]
Checkpoint

Continuing
training
1
%
|
▉
|
307
/33165
[
20
:00<
35
:40:59,
3
.91s/it,
loss
=
6
.331,
tps
=
25
,134
]
So this time we were getting 25,134 tokens per second -- 20% faster!
By default, PyTorch's GELU uses an exact calculation of the function -- the hand-written
code from the book uses an approximation using
tanh
.  Luckily, you can get that same
approximation from PyTorch:
super().__init__()
self.layers = nn.Sequential(
nn.Linear(cfg["emb_dim"], cfg["emb_dim"] * 4),
-            nn.GELU(),
+            nn.GELU(approximate="tanh"),
nn.Linear(cfg["emb_dim"] * 4, cfg["emb_dim"])
)
So, training with that for 20 minutes:
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
1xrtx3090-baseline
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
4115
.09it/s
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
23
,875
]
Checkpoint

Continuing
training
1
%
|
▉
|
307
/33165
[
20
:00<
35
:39:42,
3
.91s/it,
loss
=
6
.332,
tps
=
25
,142
]
25,142 tokens per second -- basically the same as the non-approximate version.
So: switching to the built-in GELU made my PyTorch code run 20% faster, at about 25,000 tps
rather than 21,000.
My JAX code, which used JAX's built-in GELU, ran at around 24,000 tps.  I'd actually
found that rather surprising, because in JAX I was training in full-fat 32-bit floating point, while in PyTorch I was using
Automatic Mixed Precision (AMP) -- a special mode that allows it to use 16-bit calculations
where it won't hurt the model much.
I'd
found
that
AMP gave PyTorch a huge speedup -- from 15,402 tps to 19,797 on one test.  So JAX without AMP
being so much faster than PyTorch with AMP was a bit of a surprise.  Its JIT is pretty
amazing, but I didn't expect it to be
that
much faster.
Now I think that we have at least part of an explanation.  I was using JAX's
built-in GELU (interestingly, with its default parameters, which means that it used the
tanh
approximation), but the PyTorch code was using the hand-rolled one, and that unduly
penalised it and erased some of the gains it got from AMP.
If I really wanted to dig into this, I suppose I might try JAX with a hand-rolled GELU
to see what happened.  My guess is that because of its JIT, it might actually handle it
better -- the whole hand-rolled thing could be compiled into one thing on the GPU.  Perhaps
it would also be interesting to try the non-AMP PyTorch code with the built-in GELU.
But I doubt that would really be the best use of my time (and my electricity bill),
so I'll leave it here.
On the other hand, I do intend to have a look at
torch.compile
in the future, to see
what kind of speedup I can get from it.  And it might be able to compile and fuse together
the hand-rolled GELU -- so that would be an interesting thing to experiment with in that
post: does the built-in GELU advantage disappear if we're compiling?
But anyway, for now, lesson learned: use built-in PyTorch modules when you can.
It's a pretty obvious one ;-)
[Update] On X,
Sebastian Raschka noted
that
he used the approximate version of GELU in his code so that the models were compatible with the
OpenAI weights -- they were trained with that version, so they may behave slightly differently
if you use the "pure" version.  That's a great point, and so I've updated my own copy of the
code to use
approximate="tanh"
.
