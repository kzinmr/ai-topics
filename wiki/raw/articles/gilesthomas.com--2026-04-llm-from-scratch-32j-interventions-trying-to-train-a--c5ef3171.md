---
title: "Writing an LLM from scratch, part 32j -- Interventions: trying to train a better model in the cloud"
url: "https://www.gilesthomas.com/2026/04/llm-from-scratch-32j-interventions-trying-to-train-a-better-model-in-the-cloud"
fetched_at: 2026-05-01T07:02:05.542711+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Writing an LLM from scratch, part 32j -- Interventions: trying to train a better model in the cloud

Source: https://www.gilesthomas.com/2026/04/llm-from-scratch-32j-interventions-trying-to-train-a-better-model-in-the-cloud

Archives
Categories
Blogroll
Since early February, I've been trying various interventions on a 163M-parameter GPT-2-style model that I
trained from scratch on my local RTX 3090
,
using code based on
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
".
My original model got a loss of 3.944 on my test set, while the original GPT-2
weights got 3.500 on the same dataset.  I wanted to see if I could close that gap,
and had a list of potential changes to the
training setup, and to the model itself.  Which of them would help?
I found a list of solid-looking interventions, and in
my last post
I came to the conclusion that the improvements in loss I had seen with all of them -- with
two possible exceptions -- seemed unlikely to be in the noise.  What would happen
if I tried to put them into a new model?
The interventions
Let's start by looking at the results that we have for the interventions so far --
this is the table I've been using as I go through them, but I've updated it to contain
the loss figures for each model to six decimal places instead of three, and
made each model name link to the associated post.  I've also corrected the loss for
the
8xa100m40-weight-decay-cerebras
model, which was mistakenly using the training loss at the
end of the run rather than the loss on the test set .
As I've mentioned before, simply moving to training in the cloud improved things markedly,
getting loss down from 3.944 to 3.691526; I suspect this was due to having a closer-to-optimal
batch size (more about that in my next post).  What to do about the other interventions, though?
It seemed clear that two of them were not helping: weight tying, and the one using the figure
for weight decay that I'd (I suspect incorrectly) derived from a paper by Cerebras
Research.  The "no-AMP" run (which would be better described
as "full-fat float32") had a small positive effect, but was so costly in terms of both time and money
that it wasn't worthwhile.
So we had five interventions to try:
Gradient clipping.
QKV bias (that is, adding bias to the attention weight matrices).
Changing weight decay to the GPT-2 value (0.01 rather than the 0.1 that is typical nowadays).
Removing dropout
Updating the learning rate from 0.0004 to 0.0014, but also scheduling it so that it varies
over the course of the training run.
How would they stack up?  It seemed pretty unlikely that their independent contributions
would just sum up neatly so that we got a total improvement
of 0.013209 + 0.022141 + 0.048586 + 0.050244 + 0.089609 = 0.223789 (though that would
certainly be nice!).
One question to consider was how independent they were.  For any set of interventions,
you can imagine them being independent and adding up nicely, or pulling in separate
directions so that the combined effect is worse than the sum, or pulling in the same
direction so that they amplify each other.
My intuition was that gradient clipping and removing dropout were pretty independent,
at least conceptually.  They might affect other interventions indirectly (eg. via changing the
training run's use of the random number generator) but they'd be unlikely to have a direct
effect.  QKV bias I was less sure about, but it seemed -- again, just intuitively --
at least reasonably independent of the others, with one important exception (which I'll get into below).
By contrast, weight decay and the learning rate interact together quite strongly,
at least in standard gradient descent, and I'd tested them in isolation.  The result for changing the weight
decay to 0.01 was based on a fixed learning rate of 0.0004, and the result for scheduling
the learning rate was based on a weight decay of 0.1.
That felt like an issue, and definitely needed some thought.
Additionally, there were some issues with which interventions might have not had a real
effect, and instead just been the results of the use of randomness.  While my analysis of how that might have affected
things was somewhat limited by the number of test runs I could
afford to do, it did show up two plausible issues:
Adding gradient clipping looked like it might have been within the training run noise.
Adding QKV bias would have had a large effect on the model's initial weights.  All
of the others would have started with essentially the same weights (apart from
weight tying, though even that would have had the same values for the initial
weights apart from the tied ones).  But adding the bias would have completely changed
them, and its effect size was comfortably within the range of differences you might
expect from that.
After some thought, I came up with a plan.  If I were doing this properly and scientifically,
I suppose I'd try every combination of interventions, but that would be ruinously expensive , so a sensible
minimal set of training runs felt like this:
Start a training run with all of the interventions apart from QKV bias.
In parallel (Lambda instance availability permitting) run another one, with
all of the interventions
including
QKV bias.
When those completed, I'd find the test set loss for both models.  I'd choose the best
run, and then do another run with those settings, but with weight decay switched
back to the original value of 0.1.  I chose to revert weight decay rather than the learning rate stuff because this was
the one I was least sure about -- the updated "GPT-2" value of 0.01 is very unusual
by today's standards, and I'd come to it via a rather circuitous route -- see
the post
for more details.
The best of the three runs would be the winning combination of interventions.
Again, this was not an exhaustive plan .  But it seemed to make sense.  Let's see
how it turned out.
Training run 1: without QKV bias
Just to recap, this one had these interventions against the baseline:
Gradient clipping at 3.5
Weight decay changed from 0.1 to 0.01
Dropout removed
Learning rate changed from 0.0004 to 0.0014, with a warmup over 5% of the run
then a cosine decay to 0.00014.
It did not have QKV bias.  You can see
the config here
.
Here's the loss chart over the course of the training run:
As normal with learning rate scheduling, I also charted that to make sure it was
doing the right thing (you can see that it was):
And I also tracked the gradient norms -- you can see that there was some clipping
happening near the start of the run:
At the end of the run, it reported this:
Training complete in 11,437.717 seconds
Tokens seen: 3,260,252,160
Throughput: 285,044 tokens/second
Final train loss: 3.557
That's a slightly lower final train loss than normal, and it took 3h10m, which is
faster than usual, but about the same as the other train we did without dropout --
that makes sense, as the process of zeroing out random activations isn't free.
I downloaded the model --
here it is
-- and then ran the smoke test:
Every effort moves you back to writing. In addition, there is room in your notebook so this will be an opportunity that
...and got its loss on the test set:
Loss against our test dataset: 3.577761
Not bad at all -- the best result we've had so far, albeit not quite
up to the standard of the original GPT-2 weights.
Now the next one, with QKV bias.
Training run 2: all five interventions including QKV bias
This one had these interventions:
Gradient clipping at 3.5
Weight decay changed from 0.1 to 0.01
Dropout removed
Learning rate changed from 0.0004 to 0.0014, with a warmup over 5% of the run
then a cosine decay to 0.00014.
QKV bias switched on.
You can see
the config here
.
Here's the loss chart:
...the learning rate:
...the gradient norms (note that we had more clipping, about halfway through):
...and the final printout at the end.
Training complete in 11,487.294 seconds
Tokens seen: 3,260,252,160
Throughput: 283,814 tokens/second
Final train loss: 3.584
That final train loss is slightly higher, which is normally an indicator that the
test loss will be higher, but we'll have to see.
Time to download the model --
here it is
--
and on to the smoke test:
Every effort moves you to change the color in your image.
Your image’s color will need to match the
...and then the moment of truth -- what was its loss on the test set?
Loss against our test dataset: 3.604342
As I suspected from the training loss at the end, slightly worse than the run without
QKV bias. So, that meant that we should do the next run, with a weight decay of 0.1, with
no QKV bias.
Training run 3: just dropout removal, gradient clipping, and a higher but scheduled learning rate
Given the above results, this one had these interventions vs the baseline:
Gradient clipping at 3.5
Dropout removed
Learning rate changed from 0.0004 to 0.0014, with a warmup over 5% of the run
then a cosine decay to 0.00014.
Weight decay was back to the baseline value of 0.1, rather than the value of 0.01
used in the previous two runs, and QKV bias was switched back off.
You can see
the config here
.
Here's the loss chart:
You can see that it's much choppier than the previous two runs; that initially surprised me,
as the higher weight decay means that we're regularising the model more than we were with
those, which I thought would "calm things down".  But on reflection, I had it backward.
Hand-waving a bit, a more regularised model is fitting less closely every detail to the data it has seen, considering
the typical stuff more than it does the outliers.
That means that when something a bit more out-of-distribution appears, it might not
have yet learned how to integrate it into its model of the world.
Well, it sounds plausible, anyway :-)
On to the learning rate (just to double-check), and it's fine:
And again, the gradient norms:
...which similarly to the loss chart show more occasions where gradients spiked and
had to be clipped -- even towards the end of the training run this time.
The final printout at the end:
Training complete in 11,422.638 seconds
Tokens seen: 3,260,252,160
Throughput: 285,420 tokens/second
Final train loss: 3.570
Once again, although the final train loss is not definitive, it tends to be indicative
of the test loss.  It's in between the last two runs, so we'd expect the test loss to
be likewise in between theirs:
Time to download the model --
here it is
--
and on to the smoke test:
Every effort moves you to make, our service has helped millions of women around the world who were recently hit by car wreck
Hmm.  At least vaguely coherent, though I'm not 100% convinced.  It looks like ads for
personal injury lawyers have crept into FineWeb somehow...
Still, it's time for the test loss (drumroll):
Loss against our test dataset: 3.590266
As predicted from the train loss, it's in between the two runs above.
Conclusion
Let's put these three runs into the results table:
As a reminder:
8xa100m40-stacked-interventions-1
was gradient clipping at 3.5, weight decay changed from 0.1 to 0.01,
dropout removed, and the learning rate intervention, but
no
QKV bias
8xa100m40-stacked-interventions-2
was gradient clipping at 3.5, weight decay changed from 0.1 to 0.01,
dropout removed, and the learning rate intervention,
with
QKV bias
8xa100m40-stacked-interventions-3
was gradient clipping at 3.5,
dropout removed, and the learning rate intervention, but
no
QKV bias, and
no change to weight decay
.
You can see that adding on QKV bias actually made the model
worse
than the learning-rate-only
intervention.  That pushes me slightly away from the "it's all about the initial weights"
direction; perhaps instead the bias adds some kind of stability that the learning rate
scheduling also provides, and they fight against each other?  Unfortunately I think the
only way to pick it apart would be to do a full set of runs, switching each intervention
on and off independently, and that would be too costly.
The fact that the weight decay change from 0.1 to 0.01 actually did help when combined
with the learning rate change and scheduling was a bit of a surprise; because they're both
coupled when we think about standard gradient descent, I was expecting them to be too intertwined for my tests
of them in isolation to have been valid.  Quite pleased that it didn't work out that way,
though, because sweeping across values for different parameters is much easier than
it would be if they were connected.
However, at this point it occurs to me that it
might be because we're using the AdamW optimiser.  As I
understand it, its big difference versus Adam is that it decouples weight decay.  I don't
have a solid mental model of what that means exactly (will read up and post about
it eventually), but it certainly seems pertinent here.
Anyway, I have to say, I'm both pleased with and disappointed by these results.
Pleased because we got a result by putting interventions together that was better
than any of them in isolation, but disappointed that the end result wasn't even
better.
The difference between
8xa100m40-baseline
's loss, at 3.691526, and original GPT-2 small's,
at 3.5, was 0.191526.  Our best result, for
8xa100m40-stacked-interventions-1
,
was 3.577761, so an improvement of 0.113765.  That's about 60% of the way there.
That said, by sheer chance, while trying out the different sizes of cloud machines,
I'd got from a loss of 3.944 training locally to the baseline's value of 3.691526 --
I suspect due to the fact that training in the cloud meant that I could use
batch sizes of 96.
So a different way of looking at it is that we should include that in the calculations too.
From 3.944 to 3.5, the gap with GPT-2 small was 0.444.  And we went from 3.944 to 3.577761,
an improvement of 0.366239.  And that means that we managed to get 82% of the improvement
we needed.
On the other hand, it means that in terms of my improvements, 0.252474 came from a happy
accident, while all of my careful work on interventions only got me 0.113765.  :-(
Anyway, I think that for now, I'll have to rest happy with that as a result -- and next time around,
let's see if we can get to the same level of improvement locally, using gradient accumulation.
Here's a link to the next post in this series
.
