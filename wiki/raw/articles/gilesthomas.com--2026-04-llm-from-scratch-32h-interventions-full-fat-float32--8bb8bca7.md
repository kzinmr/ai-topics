---
title: "Writing an LLM from scratch, part 32h -- Interventions: full fat float32"
url: "https://www.gilesthomas.com/2026/04/llm-from-scratch-32h-interventions-full-fat-float32"
fetched_at: 2026-04-29T07:02:02.652423+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Writing an LLM from scratch, part 32h -- Interventions: full fat float32

Source: https://www.gilesthomas.com/2026/04/llm-from-scratch-32h-interventions-full-fat-float32

Archives
Categories
Blogroll
This is the last of the interventions I'm trying out to see if I can improve the
test loss for a from-scratch GPT-2 small base model, trained on code based on
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
".
Back when I did my first training run for a base model,
on my local RTX 3090
,
I used two optimisations:
The first of those boosted training speed from 12,599 tokens per second to 15,402
in my test harness, while AMP on its own boosted it to 19,921 tps (and also allowed me
to increase the batch size from 5 to 6).  Doing both appeared to hit some kind of
diminishing returns -- it maxed out at 19,997 tps, only a little better than AMP on its
own.
But intuitively, you'd expect that might come at a cost.  While I'm sure the PyTorch
developers have solid understanding of where switching to 16-bit will have a minimal
impact on training quality, it seems too good to be true that it would have no impact
at all.
Let's see what happens if we switch both of these optimisations off!
I added a new flag to the
train.json
config file for the training harness,
use_amp
with a default of
True
.  The core implementation was pretty simple;
where we had the call to
torch.set_float32_matmul_precision
, we needed to guard it:
if
use_amp
:
torch
.
set_float32_matmul_precision
(
"high"
)
...and where we did the forward pass and the loss calculation, we had to not
wrap it in a
with torch.amp.autocast
:
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
We also had to avoid
unscaling when clipping gradients
; I did that by just not
creating a scaler when in non-AMP mode, and then:
if
scaler
is
not
None
:
scaler
.
unscale_
(
optimizer
)
...and likewise, instead of using the scaler to step the optimiser, we step it
directly if we don't have one:
if
scaler
is
not
None
:
scaler
.
step
(
optimizer
)
scaler
.
update
()
else
:
optimizer
.
step
()
However, there was an issue: non-finite gradients.  As I discovered when
looking into gradient clipping
,
the scaler was actually doing something quite useful for us.   Somewhat buried in
the
AMP recipes page
is a comment:
# ``scaler.step()`` first unscales the gradients of the optimizer's assigned parameters.
# If these gradients do not contain ``inf``s or ``NaN``s, optimizer.step() is then called,
# otherwise, optimizer.step() is skipped.
Now, from the gradient clipping train, I'd come to the conclusion that we were occasionally
getting non-finite gradients, and the scaler was saving us from applying junk updates
when that happened.
If our new code was stepping the optimiser directly, we'd not have that safety net.  We'd
need something to save us from that.
My first cut at this was to use the one other API feature I'd seen that handled
non-finite gradients for you:
torch.nn.utils.clip_grad_norm_
has a
error_if_nonfinite
parameter, so if we were using gradient clipping, we could
set that to
True
and use the exception to skip stepping the optimiser if it was
raised.  To avoid actually doing any gradient clipping when that happened, if we did not
have gradient clipping explicitly enabled, we could set the
max_norm
to infinity.
Here's
the code for that version
.
I wasn't very happy with it, though.  The use of a gradient clipping API just for
its side-effect of telling us about non-finite gradients felt a bit ugly, and even worse,
the exception it raised was just a generic
RuntimeError
, not a custom exception type,
which meant that I had to distinguish between it and other
RuntimeErrors
by looking
at the exception message -- not terribly safe, as that's something that could easily change
in the future.
So I switched to a more explicit, simpler version: scan through the parameters looking for
non-finite gradients, and skip the optimiser step if any are found:
if
scaler
is
not
None
:
scaler
.
step
(
optimizer
)
scaler
.
update
()
else
:
# The scaler skips non-finite gradients, but if we're not using it we have
# to do that for ourselves.
found_nonfinite
=
False
for
p
in
model
.
parameters
():
if
p
.
grad
is
not
None
and
not
torch
.
isfinite
(
p
.
grad
)
.
all
():
found_nonfinite
=
True
break
if
not
found_nonfinite
:
optimizer
.
step
()
I did have some concerns about the performance impact of that; on my local machine
it took about 0.13 seconds to scan all of the parameters like that for one step.
However, it's better than failing to train the model
at all due to garbage updates!
So with that, it was time to do the training run.
The train
It was pretty clear that I would not be able to run this with my normal microbatch
size of 12 on the 8x A100 40 GiB machines that I'd been using so far for these intervention
tests -- AMP and the lower-precision matrix multiplications save a bit of VRAM, and
I was already pretty much at the limit of what would fit in there.
Changing the batch size would make this a poor test of the effects of removing the
FP precision stuff in isolation, so I decided that the safest minimal change was to
use a machine with more VRAM -- specifically an 8x A100 80 GiB, as that was the closest
to what I was using (switching to eg. H100s would add all kinds of confounding changes).
The next problem was getting any kind of machine at all!
Lambda
(they
appear to have rebranded away from "Lambda Labs") very rarely seemed to have any
available instances, never mind the specific type that I wanted.  Eventually,
I
put together a system to poll their API and launch an instance
when one was available.  At 3:25am today , I got a Telegram message from the script saying
that it had managed to find and start one.
I kicked off the training run, and watched as it got started.  I could see it was using
43.8 GiB/GPU, so it definitely did need the larger instance type.  And it quickly became clear
that this was going to be a long one -- it was estimating 8 hours to do the complete
run!
In a way that was good news, though, as I could just set an alarm and go to bed.
When I woke up, it was done:
Training complete in 29,230.838 seconds
Tokens seen: 3,260,252,160
Throughput: 111,535 tokens/second
Final train loss: 3.729
That's 8h7m.  For comparison, the baseline train took 3h24m, so we're taking more
than double the time.
Cost-wise, things were even worse -- more than US$135 in server costs, because as
well as needing the server for much longer, being a larger machine it cost US$16.48/hour rather than
$11.84.  So that's more than three times as expensive
as the US$42 that a typical recent
train has cost me (Lambda raised their prices, so it went up from about US$35 in February).
Still, at least it looked like a solid run:
Very similar to the others we've seen in this series.
Time to upload it to
Hugging Face Hub
, and
on to the evals to see if all of this extra cost was worthwhile.
Evals
Firstly, the smoke test -- how did it complete
Every effort moves you
?
Every effort moves you towards greater success. And even then, they’re on your way to winning a prize and
Not bad at all!  But the important metric is the loss on the test set, and for that
I got 3.679.  Let's add it to the table to see how that compares to the other training runs:
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
8xa100m80-no-amp
3.679
0.013
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
So, a
tiny
improvement over our baseline.  Taking more than twice as long on the training run, and
spending three times as much, gained us a loss improvement that's smaller than any other
successful intervention.
Conclusion
The first question is, did removing AMP and lower-precision matrix multiplications
lead to a better model?  The answer appears to be "yes" -- but it's a tiny enough
difference that it could well be in the noise.
But the follow-up has to be, was it worth the extra cost in time and money?  And for
that I'm certain that the answer is "no".  If we'd spent twice the time
training with AMP -- on an extra 3B-odd tokens, or on a second epoch with the same
3B -- it seems implausible that the resulting loss would not have been better.
And anyway, given that my goal with these interventions is to train the best model
I can in two days locally (or 3h30m or so on an 8x A100 40 GiB), it's pretty clear that
if we'd cut this run off about halfway through it would have been worse -- and that's not
even accounting for it being more memory-hungry.
So, I think the takeaway from this is that AMP appears to be a huge win, at least for
this model.  It has a tiny cost (if any) in model quality, and a huge benefit in training
speed, plus a smallish but still useful benefit in training VRAM requirements.
And with that, I've reached the end of
the interventions that I wanted to try
!  Next,
I'll need to think through what we need to do to try to stack them up.  In particular,
is there any easy way to work out whether any of the improvements I've seen might
be due to random noise?  After all, even though I've been carefully using explicit
seeds, each intervention will have changed the way the training run uses the random
number stream, and that could easily have an effect.
Stay tuned!
Here's a link to the next post in this series
.
