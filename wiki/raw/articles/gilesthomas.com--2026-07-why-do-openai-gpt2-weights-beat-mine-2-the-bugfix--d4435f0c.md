---
title: "Why do OpenAI's GPT-2 weights beat mine? Part two: the bugfix"
url: "https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-2-the-bugfix"
fetched_at: 2026-07-31T10:24:10.727465+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Why do OpenAI's GPT-2 weights beat mine? Part two: the bugfix

Source: https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-2-the-bugfix

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
I'm digging into why my GPT-2 style models score worse on an instruction-following eval than OpenAI's original weights;
I gave the details in
this post
.
While I was writing up the results of my first experiment into possible causes,
I ran the post past ChatGPT -- I always use an "editorial board" of AIs to check my
posts for flow, style, and any technical errors (though all writing is always mine).
It took a look at the eval code that I was running, and highlighted a bug.
Luckily, it doesn't change the important results -- OpenAI's models continue to be
better than mine at instruction-following. But it was
enough to change the baseline numbers, re-ordering how well my own models did.
So I fixed it and regenerated the baseline
so that future experiments are based on solid ground.
The bug
The eval takes a model, and trains it over multiple epochs on a split of a subset of the Alpaca
instruction-following dataset.  At the end of each epoch, it evaluates
the resulting model against a held-back validation split; if the eval loss starts
rising, it bails out.  Finally, it runs a test split of the dataset through the resulting
model, and saves the result.
Once I've run it for a bunch of different models, I use an LLM-as-a-judge script
to get GPT 5.5 to score results -- for each question-answering result, it sees all
of the responses for all of the models
in the same prompt
, shuffled in order each time,
to try to make it judge models against each other as consistently as possible.
Now, the idea was that the generation of the test split answers would use the model from the epoch prior
to the rising-loss one.  So I had code like this:
for
epoch
in
range
(
100
):
model
.
train
()
for
input_batch
,
target_batch
in
tqdm
(
train_loader
,
desc
=
f
"Epoch
{
epoch
}
"
):
optimizer
.
zero_grad
()
loss
=
calc_loss_batch
(
input_batch
,
target_batch
,
model
,
device
)
loss
.
backward
()
optimizer
.
step
()
model
.
eval
()
val_loss
=
calc_loss_loader
(
val_loader
,
model
,
device
,
eval_iter
)
if
last_val_loss
is
None
or
last_val_loss
>
val_loss
:
last_val_loss
=
val_loss
last_params
=
model
.
state_dict
()
print
(
"Val loss still decreasing, continuing"
)
else
:
print
(
"Val loss rising, bailing out"
)
break
model
.
load_state_dict
(
last_params
)
Each time the validation loss went down, I wanted to store the model's parameters
in
last_params
so that they could be restored later in that last line.
If you look closely, the error is pretty obvious.
model.state_dict()
does not return
a copy of the model's parameters -- it produces a dictionary containing references
to the parameters inside the model.  So although I was trying to stash away the parameters
in
last_params
each time loss went down, so that we had a copy of the ones that
were live in the epoch prior to the rising-loss one, what I was actually doing was
just pointlessly saving a reference to the "live" params.  The call to
model.load_state_dict(last_params)
was essentially a no-op.
The solution was simple enough:
from
copy
import
deepcopy
...
last_params
=
deepcopy
(
model
.
state_dict
())
That was enough to make the code do what it was meant to do.
While I was there, I also noticed that the evaluation code was only using the first
five batches in my eval dataset.  This code was originally adapted from an eval
in "
Build a Large Language Model (from Scratch)
",
where the eval was run much more frequently and had to be super-fast.  Because
my own code ran it more rarely, it made more sense to use all of it.
Given that I was going to completely re-run
the script to generate the test responses, I figured that I might as well fix that
at the same time.
A new baseline
I re-ran the fixed script on all of the models I'm comparing, and ran that past
the GPT 5.5 judge; here's what I got:
Test loss
Old IFT epochs
Old IFT score
Old IFT rank
New IFT epochs
New IFT score
New IFT rank
OpenAI weights: medium
3.231442
2
41.62
1
2
42.41
1
JAX, with MHA bias, no dropout
3.418784
4
19.25
4
4
18.12
5
JAX, no MHA bias, no dropout
3.420089
3
14.66
11
5
20.72
3
JAX, no MHA bias, with dropout
3.476802
4
12.94
15
7
16.98
8
OpenAI weights: small
3.499677
2
26.73
2
2
26.11
2
1xrtx3090-stacked-interventions
3.538161
4
17.79
6
4
13.68
11
8xa100m40-stacked-interventions-1
3.577761
4
10.29
16
4
9.81
15
Cloud FineWeb, 8x A100 40 GiB
3.673623
7
20.71
3
6
19.45
4
1xrtx3090-baseline
3.683835
6
15.11
9
6
13.39
12
8xa100m40-baseline
3.691526
4
14.74
10
4
14.64
9
Cloud FineWeb, 8x H100 80 GiB
3.724507
4
13.25
14
4
13.84
10
Cloud FineWeb, 8x A100 80 GiB
3.729900
4
14.50
12
4
11.30
14
Cloud FineWeb, 8x B200 160 GiB
3.771478
4
16.03
8
4
11.82
13
Local FineWeb train
3.943522
7
13.73
13
7
8.93
16
Local FineWeb-Edu extended train
4.134991
7
16.70
7
7
17.10
7
Local FineWeb-Edu train
4.166892
7
18.68
5
7
17.28
6
Let's dig into those numbers.
Training epochs
Let's look into the number of training epochs first; I've highlighted the models for which it changed.
For the "Cloud FineWeb, 8x A100 40 GiB" model, I think that was a result of the change
to the number of validation samples.
For the two JAX models, it's a bit more of a mystery.  There may be some part of the
same "more eval data" variation there, but I have a suspicion that there's something
more, related to dropout.
My methodology to date has been that the IFT training runs
should use the same dropout setting as the original base model training run (I'll
come back to this in a later post).   However, due to differences between the JAX
training script and the evaluation code (which is PyTorch), matching the dropout
rate when evaluating those models is a bit fiddly and error-prone.
I am 100% sure that
I got it right this time around -- I've checked and double-checked the specific commands
I ran.
But I think -- from what I remember doing -- that
I might have messed it up the previous time.
That's not certain, though -- just a suspicion based on half-memories
of some commands I ran several weeks ago, which never wound up in my
.bash_history
(too many terminals open at once).
The ranking
For the IFT scores, remember that they're not strongly comparable between runs.
Let's imagine that the LLM judge is given the following answers to the question "Who was the author of
Pride and Prejudice
?"
"Jane Austen"
"The author of 'Pride and Prejudice' was Jane Austen"
"The author of 'Pride and Prejudice' was Sarah Palin"
"The author of 'Pride and Prejudice' was 'Pride and Prejudice'"
In some cases it might treat the first two as being 100/100, in others it
might give the second 95/100 for being too wordy.  Likewise, in some cases it might
rank the last two as 0/100 for being wrong, in others it might give the "Sarah Palin"
one 5/100 for at least being the name of a person rather than complete nonsense.
Now, we always ask the LLM to judge all of the models' answers for a given question in
one go, so at least we can be sure that it will be consistent for a given prompt about
a given question.  But what we can't keep consistent is which way it leans between
different runs, or different questions within the same run.  Sometimes it might be
feeling "generous" and give the Sarah Palin answer a bit of grace, other times
it might be harsher.
So there's a significant amount of noise there; my rule of thumb is that a variation of
a point or two is within that noise, so OpenAI medium going from 41.62 to 42.41 is
pretty much meaningless, and likewise "JAX, with MHA bias, no dropout"'s move from
19.25 to 18.12.
So what's important is the relative ranking -- which is first, which is second,
and so on.  Naturally, you have to allow for the fact that -- for example -- if one
model goes from position 11 to position 3, like "JAX, no MHA bias, no dropout"
did, then the previous number 3 will have to become number 4, 4 will
become 5, and so on.  You can see that happening in the results table.  Obviously,
as other models rise and fall, that has further knock-on effects.
Anyway, with all of those caveats, the good news is that my original mystery remains.
The OpenAI models were still doing noticeably better than my own ones.  GPT-2 medium
continued to lead the pack (unsurprisingly, given that it's a bigger model), and
GPT-2 small was still in second place.  If that had changed, it would have made
a rather disappointing end to this series: "mystery explained, it was a bug in the
eval :-("
But now let's look at my models.
Firstly, it looked like the "no MHA bias" models might have benefited
from the extra training -- or from having their dropout settings corrected.  They rose from
positions 11 and 15 to 3 and 8 respectively -- a huge swing for "JAX, no MHA bias, no dropout",
and a solid improvement for "JAX, no MHA bias, with dropout".
Most of the other changes in relative rankings can be explained by those two models
having been promoted, but there are some other changes.  In particular, three models
dropped significantly in score (and, as a result, ranking):
1xrtx3090-stacked-interventions
"Cloud FineWeb, 8x B200 160 GiB"
"Local FineWeb train"
My suspicion -- a very weakly-held hypothesis, but an interesting one -- is that those models had previously been
benefiting
from the bug.
Remember that the signal we're using to stop training is that the validation loss
starts rising.  We're using that as a proxy for overfitting, which in turn we're using as
a proxy for "this model has had as much training
on this data as it needs for the eval".
But there's no guarantee that the connection is there.  Perhaps the models weren't
overfitting and if we'd waited for another epoch or two, the validation loss might have
started falling again.  Or maybe some amount of overfitting would be beneficial for this
eval?
Conclusion
There's probably a near-infinite amount of digging in that I could potentially do here.
But I think it's best to stop.  The bugfix was important because it meant that the
eval was now doing what I thought it was doing.
Importantly, it doesn't change the puzzling
fact that my models were worse at this eval than OpenAI's, which is what I'm trying to untangle.
And it means that I can now lean more confidently on the baseline numbers.
So now it's time to actually start changing things to see if I can close the gap!
Here's a link to the next post in this series: does overtraining help?
.
