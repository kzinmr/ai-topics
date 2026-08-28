---
title: "Why do OpenAI's GPT-2 weights beat mine? Part four: digging into dropout"
url: "https://www.gilesthomas.com/2026/08/why-do-openai-gpt2-weights-beat-mine-4-ift-dropout"
fetched_at: 2026-08-28T10:01:35.770274+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Why do OpenAI's GPT-2 weights beat mine? Part four: digging into dropout

Source: https://www.gilesthomas.com/2026/08/why-do-openai-gpt2-weights-beat-mine-4-ift-dropout

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
I'm still digging into a mystery about the models I've been training; although
an increasing number of them beat the OpenAI GPT-2 small weights on the narrow
technical measure of the loss they get on a test set, they're
not as good at an instruction-fine-tuning test
.
While reading about MoE models, I came across this paragraph in the
Switch Transformers paper
:
Our paper considers the common NLP approach
  of pre-training on a large corpus followed by fine-tuning on smaller downstream tasks such
  as summarization or question answering. One issue that naturally arises is overfitting since
  many fine-tuning tasks have very few examples. During fine-tuning of standard
  Transformers, Raffel et al. (2019) use dropout (Srivastava et al., 2014) at each layer to prevent
  overfitting.
So far, when running my IFT test, I'd been aiming to use the same dropout setting
for the fine tune as the model concerned had used in its original
pre-training.  That was just because it seemed natural.
But the goal of dropout is to prevent overfitting when training over multiple epochs
-- or, at least, that's how most of what I've read explains why we
don't need it on modern single-epoch training runs over large datasets.
If that's
the case, though, when we do multiple epochs for a fine-tune with a more restricted dataset --
exactly what I was doing for the IFT test -- it might make sense
to use dropout, regardless of whether or not the model was pre-trained with it.
The fine-tuning setup already tries to avoid overfitting by bailing out when a validation
loss starts rising, but dropout might still help it avoid overfitting prematurely.
On the other hand, something felt a little wrong about fine-tuning a model with
dropout if its pre-training had happened without it.  A model pre-trained with dropout have been trained
on billions of tokens, and so the model will have spent a lot of effort learning
to overcome the issues that dropout causes, but one trained without it won't have that benefit.  Suddenly exposing it to dropout in a much
shorter fine-tuning run felt rather like asking someone who rarely drinks alcohol to take a
few shots of whisky; I felt that the models might not be prepared for the effects.
As I looked into this more, I noticed another surprising thing -- there was an error in the
configuration that I was using when fine-tuning the OpenAI models, both small and
medium.  They were originally trained with dropout (or so it's believed --
the paper
doesn't
say, but "
Build a Large Language Model (from Scratch)
"
says that they were, and
this config on the Hugging Face GPT-2 code
agrees).
But that actually made my original puzzle of why they outperformed my models on the IFT
test seem even more perplexing, at least in the light of this idea.  If dropout
was a good thing for fine-tuning, then so far they had been penalised by
not
using it -- that is,
they were even further ahead of my own models than I thought they were.
It was time to take a careful look.
The fine-tunes
I fixed the config for the OpenAI weights so that my setup had dropout set to 0.1 for
them, then carefully revisited the config for all of my own models, and made sure that those
ones matched reality (which they did).
Now, the IFT test that I've been running has two phases:
Firstly, for each model, I run
ift_generate_test_responses.py
.
This script trains the specified model on an IFT dataset until validation loss
starts rising.  It then uses the model from before that loss started going up to
generate responses to a test set, and saves those responses to disk.  I made a small change
to it so that the dropout used in the fine-tuning phase was a required command-line
parameter, with three options:
model
-- that is, what the model
was pre-trained with --
on
, which forced it to 0.1, or
off
, to force it to 0.
Next, I pass all of the saved test responses for all models into a second script,
ift_judge.py
,
which
sends them to an LLM judge
so that each model can get a score.  The script averages all scores across all
questions for each model.  Check the link for more details of how that script works
and tries to achieve consistency across models and responses.
Now, the nice thing about the judge script was that it didn't really care whether
the result files it got came from different models or the same one; it just printed
out a mapping of result files to scores.  So I realised I could use it to do
a comparison of all models with all possible dropout settings.
For all of the models, I ran the
ift_generate_test_responses.py
three times, once
with each of the dropout settings:
model
,
on
, and
off
.  Then I sent all of the
resulting result files -- all models, and all dropout options for each -- to the LLM judge in
one go, to see what it came up with.
The results
Here are the results, consolidated into one table.  For each model, I have:
Its loss on my test set -- the technical measure of quality I mentioned near the
start.  They're sorted by that column.
Whether or not the base training run -- the pre-train -- had dropout.
The number of fine-tuning epochs before validation loss started rising when the
IFT run used a dropout setting identical to the pre-training (
model
).
The score that the model thus trained got from the LLM judge.
The fine-tuning epochs with dropout forced to be
off
.
The score for the dropout-off model.
The fine-tuning epochs for dropout forced to be
on
.
And finally the score for the resulting model from that.
Test loss
Base dropout
model
epochs
model
score
off
epochs
off
score
on
epochs
on
score
OpenAI weights: medium
3.231442
Yes
2
42.40
2
43.75
2
42.40
JAX, overtrained one long epoch
3.324953
No
3
19.77
3
19.77
19
7.17
JAX, overtrained two normal epochs
3.326482
No
4
19.72
4
19.72
16
12.92
JAX, with MHA bias, no dropout
3.418784
No
4
18.69
4
18.69
13
13.20
JAX, no MHA bias, no dropout
3.420089
No
5
21.46
5
21.46
20
5.25
JAX, no MHA bias, with dropout
3.476802
Yes
7
17.74
5
13.22
7
17.74
OpenAI weights: small
3.499677
Yes
4
23.49
2
26.00
4
23.49
1xrtx3090-stacked-interventions
3.538161
No
4
13.77
4
13.77
13
14.06
8xa100m40-stacked-interventions-1
3.577761
No
4
10.76
4
10.76
19
7.36
Cloud FineWeb, 8x A100 40 GiB
3.673623
Yes
6
19.71
3
17.72
6
19.71
1xrtx3090-baseline
3.683835
Yes
6
13.53
4
15.74
6
13.53
8xa100m40-baseline
3.691526
Yes
4
15.15
3
14.19
4
15.15
Cloud FineWeb, 8x H100 80 GiB
3.724507
Yes
5
14.02
4
14.33
5
14.02
Cloud FineWeb, 8x A100 80 GiB
3.729900
Yes
4
11.25
3
11.34
4
11.25
Cloud FineWeb, 8x B200 160 GiB
3.771478
Yes
4
12.02
4
14.67
4
12.02
Local FineWeb train
3.943522
Yes
7
8.85
5
12.31
7
8.85
Local FineWeb-Edu extended train
4.134991
Yes
7
17.56
5
15.04
7
17.56
Local FineWeb-Edu train
4.166892
Yes
7
17.43
5
14.99
7
17.43
It's quite an intimidating wall of numbers, but there's a bunch of interesting stuff there.
Firstly: I've put the IFT score for each model where it was trained with the
opposite
of
its pre-training dropout in bold.  Let's look at the non-bold numbers first, though.
Sanity checks
If you scan down through the models, you'll see that the non-bold IFT scores -- that is,
the one where the IFT test was done with the
model
dropout, and then the one where it
was done with dropout set explicitly to the same value as the
model
one -- are identical
in every case.  That is a really reassuring sanity check.  Remember, each of those numbers
came from a different run of the
ift_generate_test_responses.py
script -- but because
there is a fixed random seed, they should have been identical.  They were presented to
ift_judge.py
in the same way as a separate model's response.
The fact that it came up with identical scores tells us that it judged them as being
equal, which is solid evidence for its consistency in judging results in this run
(which is something that can be hard to guarantee with an LLM).
Similarly, if you look through the numbers of training epochs, the
model
epochs
for each one matches the epochs with the dropout forced to match the model's pre-training
setting, which is also reassuring -- it's certainly what you'd expect given a
fixed random seed.
Epoch counts
Looking just at the
on
and
off
epochs columns, you can see something else
interesting.  With dropout forced to be on, the number of fine-tuning epochs is
always higher than the number of epochs with no dropout, except in the case of
the OpenAI medium weights and "Cloud FineWeb, 8x B200 160 GiB", where it's the same.
That makes intuitive sense, I think.  If you're discarding 10% of your activations when
training a model, you'd expect it to take longer to converge.
But now let's look at the size of those changes.  If you compare the increase in the
number of epochs needed to train with dropout forced to be on, you can see that the
change is
much
larger for those models that were pre-trained without dropout.
The first of them, for example, "JAX, overtrained one long epoch", went up from 3 epochs
to 19!  That's way larger than, say, the change from 5 to 7 for "JAX, no MHA bias, with dropout".
That was the first indication that something interesting was happening when using
dropout to fine-tune models that had been pre-trained without it.
One question is whether so many epochs on a small dataset might just be a bad idea,
regardless of whether the early-stopping from validation loss helps avoid overfitting.
However, way back I did some
investigations
into the effect of the number of epochs of training, and found that while varying it
changed the results somewhat -- as you'd expect -- the effect was surprisingly
small, and didn't change anything about the fundamental mystery of why the GPT-2
weights were so much better than mine.  So I think we can put that aside for now.
The scores
Now let's dig into those scores.  We can divide them into two groups; models that
were helped by adding dropout, and models that were harmed.
In the "helped" group, we have these:
"JAX, no MHA bias, with dropout", which was pre-trained
with
dropout and gained 4.52 points when the IFT run used dropout.
1xrtx3090-stacked-interventions
, which was pre-trained
without
dropout and gained 0.29 points.
"Cloud FineWeb, 8x A100 40 GiB", which was pre-trained
with
dropout and gained 1.99 points.
8xa100m40-baseline
, which was pre-trained
with
dropout and gained 0.96 points.
"Local FineWeb-Edu extended train", which was pre-trained
with
dropout and gained 2.52 points.
"Local FineWeb-Edu train", which was pre-trained
with
dropout and gained 2.44 points.
In the "harmed" group, we have:
"OpenAI weights: medium", which was pre-trained
with
dropout and lost 1.35 points.
"JAX, overtrained one long epoch", which was pre-trained
without
dropout and lost 12.6 points.
"JAX, overtrained two normal epochs", which was pre-trained
without
dropout and lost 6.8 points.
"JAX, with MHA bias, no dropout", which was pre-trained
without
dropout and lost 5.49 points.
"JAX, no MHA bias, no dropout", which was pre-trained
without
dropout and lost 16.21 points.
"OpenAI weights: small", which was pre-trained
with
dropout and lost 2.51 points.
8xa100m40-stacked-interventions-1
, which was pre-trained
without
dropout and lost 3.4 points.
1xrtx3090-baseline
, which was pre-trained
with
dropout and lost 2.21 points.
"Cloud FineWeb, 8x H100 80 GiB", which was pre-trained
with
dropout and lost 0.31 points.
"Cloud FineWeb, 8x A100 80 GiB", which was pre-trained
with
dropout and lost 0.09 points.
"Cloud FineWeb, 8x B200 160 GiB", which was pre-trained
with
dropout and lost 2.65 points.
"Local FineWeb train", which was pre-trained
with
dropout and lost 3.46 points.
There are some patterns there, and I think that putting them into a table
sorted by the score increase/decrease is a good way to visualise them:
Base dropout
Score change
JAX, no MHA bias, with dropout
Yes
4.52
Local FineWeb-Edu extended train
Yes
2.52
Local FineWeb-Edu train
Yes
2.44
Cloud FineWeb, 8x A100 40 GiB
Yes
1.99
8xa100m40-baseline
Yes
0.96
1xrtx3090-stacked-interventions
No
0.29
Cloud FineWeb, 8x A100 80 GiB
Yes
-0.09
Cloud FineWeb, 8x H100 80 GiB
Yes
-0.31
OpenAI weights: medium
Yes
-1.35
1xrtx3090-baseline
Yes
-2.21
OpenAI weights: small
Yes
-2.51
Cloud FineWeb, 8x B200 160 GiB
Yes
-2.65
8xa100m40-stacked-interventions-1
No
-3.4
Local FineWeb train
Yes
-3.46
JAX, with MHA bias, no dropout
No
-5.49
JAX, overtrained two normal epochs
No
-6.8
JAX, overtrained one long epoch
No
-12.6
JAX, no MHA bias, no dropout
No
-16.21
One thing is pretty clear: with two exceptions, the models that were pre-trained
with dropout are at the top, and the models that were pre-trained without are at
the bottom.
Of the exceptions,
8xa100m40-stacked-interventions-1
is so close to "Local FineWeb train" that perhaps its
position could be due to some kind of noise.
1xrtx3090-stacked-interventions
is much more puzzling, however.
It's a real outlier in terms of the models that were pre-trained with no dropout,
with its
improvement
of 0.29 compared to the next closest, with a decrease of 3.4.
But if we disregard that outlier for the time being, the pattern actually does fit rather
well into my original suspicion about the risks of switching on dropout when fine-tuning
a model that was pre-trained without it.  They really don't handle it very well!
On the other hand, it rather does put the kibosh on the idea that I based on
the quote near the start of this post -- that fine-tuning with dropout is a good
way to help the model learn with less risk of overfitting.  In my particular case -- these
specific models, this particular fine-tuning task, with this IFT data -- dropout
seems to generally have a negative effect on the fine-tuning results.  Even of those that were
pre-trained with dropout, more than half got worse results when fine-tuned with it.
Another interesting thing that stands out from the table above is that the JAX
models are at the top and the bottom.  The model that was pre-trained with dropout
was the one that gained the most from fine-tuning with it (or, contrariwise, lost
out the most if fine-tuned without it).  The models that were pre-trained without
were the ones that were most harmed by being fine-tuned with.
If you look further up, at the original table of results, you'll see that the JAX
models all did better than my other ones (which were trained using PyTorch) in terms of loss on
my test set (the second column).  I've
been chalking that up to two things: the JAX models would have started their pre-training
with different random initial weights, and they were all trained in full-fat float32
(unlike the PyTorch models, which used
AMP
).
Given that I
found
that
AMP had a negligible impact on training loss, I've been thinking that the "initial weights"
aspect was the more important -- by chance, they happened to start in a place on
the loss landscape with a route to a better minimum during training.
I don't think there's anything in these results that pushes against that theory, but
it does suggest that there's some kind of "fragility" in the minima they have found;
changing dropout from what they were pre-trained with seems to knock them out of their exceptional positions.
And finally, of course, the mystery around
1xrtx3090-stacked-interventions
's
anomalous position remains.  I honestly don't have any theories at all about that one
right now.  Interestingly, it was trained with an identical configuration to our
other (but less extreme) exception,
8xa100m40-stacked-interventions-1
.  The difference
is that the first was trained on my local RTX 3090, using gradient accumulation to
get a global batch size of 96, while the second was trained on a cloud machine
with 8x A100 GPUs with 40 GiB each, which (using DDP) got a global batch across all
GPUs of 96 without gradient accumulation.   There's something going on there, but
I'm not sure what.
Anyway, for now, I think it's time to wrap this one up.
Conclusion
The idea I started this post with -- that using dropout for the fine-tuning part
of all of these IFT tests might be a good idea to avoid issues from the multi-epoch
nature of the fine-tuning -- doesn't seem to hold up.  Dropout in the fine-tuning
turned out to be more often harmful than helpful, regardless of whether a model was originally pre-trained
with dropout or not.
However, exactly
how
harmful it was seemed to be pretty strongly correlated with
whether the model was originally pre-trained with dropout, the oddity of
1xrtx3090-stacked-interventions
aside.
I think that while working further on solving this mystery, I should stick to not
using dropout.  Because adding it on for the OpenAI models made their performance
worse, I think that's principled -- it's quite the opposite of making a choice
to try to sweep the mystery I'm trying to solve under the carpet :-)
So that means that my task in future posts in
this series
is to explain this table (to go back to the format
I've been using for the previous posts) -- the dropout
off
numbers from the table above,
with rank added:
Test loss
IFT epochs
IFT score
IFT rank
OpenAI weights: medium
3.231442
2
43.75
1
JAX, overtrained one long epoch
3.324953
3
19.77
4
JAX, overtrained two normal epochs
3.326482
4
19.72
5
JAX, with MHA bias, no dropout
3.418784
4
18.69
6
JAX, no MHA bias, no dropout
3.420089
5
21.46
3
JAX, no MHA bias, with dropout
3.476802
5
13.22
15
OpenAI weights: small
3.499677
2
26.00
2
1xrtx3090-stacked-interventions
3.538161
4
13.77
14
8xa100m40-stacked-interventions-1
3.577761
4
10.76
18
Cloud FineWeb, 8x A100 40 GiB
3.673623
3
17.72
7
1xrtx3090-baseline
3.683835
4
15.74
8
8xa100m40-baseline
3.691526
3
14.19
13
Cloud FineWeb, 8x H100 80 GiB
3.724507
4
14.33
12
Cloud FineWeb, 8x A100 80 GiB
3.729900
3
11.34
17
Cloud FineWeb, 8x B200 160 GiB
3.771478
4
14.67
11
Local FineWeb train
3.943522
5
12.31
16
Local FineWeb-Edu extended train
4.134991
5
15.04
9
Local FineWeb-Edu train
4.166892
5
14.99
10
The OpenAI small model still has a 4.54-point lead over the best of my own models,
"JAX, no MHA bias, no dropout".
Previously I'd considered data quality as a possibility, and felt it was an unlikely
cause.  I now think I may have been premature in that, and it's worth looking into.
Those two "Local FineWeb-Edu" models near the bottom were trained with sub-optimal
hyperparameters and -- while they don't do super-well in this test -- they do much
better than their raw test loss numbers might suggest.
But while thinking about dropout, it occurred to me that there were other
levers that I'd pulled in my
interventions into my original base model
that might be worth investigating :
Weight tying -- I honestly can't think of a reason why it might make a model better
for this kind of task, but it certainly is true that the OpenAI weights use it --
while none of the ones of mine that I've been testing do.  That feels worth a quick look, especially
given that I have a copy of a model that I trained using it lying around.
AMP.  Apart from "JAX, no MHA bias, with dropout", all of the JAX models -- trained without AMP -- did pretty well
in this test (though not close to the OpenAI models).  And again I have a PyTorch model
that was trained without AMP on my disk somewhere, so I may as well throw it in and see how it does.
The learning rate.  All of these fine-tunes are happening with a fixed learning rate of
0.00005.  While I really don't want to do some kind of sweep across multiple values
for all of these models, perhaps there's some way I can try to relate the fine-tuning
learning rate to what the models are "used to" from pre-training and see if that helps?
So, plenty of further possibilities for this investigation.  Stay tuned!
Citing this post
This is a blog, and if you want to link to this post then please do :-)
                However, if you're writing something more academic and need to do
                a proper citation, then here's a BibTeX block to make things easier.
@misc{thomas2026aug-why-do-openai-gpt2-weights-beat-mine-4-ift-dropout,
  author       = {Thomas, Giles},
  title        = {{Why do OpenAI's GPT-2 weights beat mine?  Part four: digging into dropout}},
  year         = {2026},
  month        = aug,
  howpublished = {Blog post},
  url          = {https://www.gilesthomas.com/2026/08/why-do-openai-gpt2-weights-beat-mine-4-ift-dropout},
}
