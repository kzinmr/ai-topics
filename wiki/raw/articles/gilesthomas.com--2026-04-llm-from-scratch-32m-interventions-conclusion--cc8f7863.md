---
title: "Writing an LLM from scratch, part 32m -- Interventions: conclusion"
url: "https://www.gilesthomas.com/2026/04/llm-from-scratch-32m-interventions-conclusion"
fetched_at: 2026-05-01T07:02:05.834828+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Writing an LLM from scratch, part 32m -- Interventions: conclusion

Source: https://www.gilesthomas.com/2026/04/llm-from-scratch-32m-interventions-conclusion

Archives
Categories
Blogroll
Last November, when I finished the main body of
"
Build a Large Language Model (from Scratch)
",
I
set myself a number of follow-on goals
.
One was "training the full GPT-2 base model myself".
I've reached the end of that journey, with a model that is almost -- if not quite
-- as good as GPT-2 small, trained in 44 hours on my own machine,
so I thought it would be worth summarising
how it went.
In December,
I trained my first model
,
taking two days,
but was disappointed to see that it was worse in terms of loss, and in terms
of how well it could be fine-tuned to follow instructions, than the original GPT-2 model.
I expected that a chunk of that difference was likely to be due to the original model having
been trained for longer, but also noticed that there were a number of changes -- interventions -- that
I could make to the model and the training run, and I thought they might help.
In January, I
got a DDP training system together
that would allow me to iterate on those interventions without having to wait for
two days for each result.
In February, I got started by
training a baseline model in the cloud
,
and
I've since ground through all of the interventions, and come up with
a set that lowered the loss nicely, both
in the cloud
,
and
locally
.
Along the way, I've learned about, or refined my knowledge of, a bunch of ML concepts.
In increasing order of how they helped with the loss (with the first two actually making
it slightly worse):
Weight tying
, which
I found made the loss worse, but it was interesting how simple it was to implement.
PyTorch's
Automated Mixed Precision
,
which also harmed the loss a tiny bit, but
had the benefit of making training twice as fast, and 66% cheaper in the cloud
-- well worth the loss penalty.
Gradient clipping
-- a cheap,
but (somewhat to my surprise) not particularly effective intervention for this model.
QKV bias
-- that is,
adding bias to the attention weight matrices -- which also helped a tiny bit, though
I later felt that this might have been in the noise.
Weight decay
-- more effective,
and something
that's simple enough to understand with simple gradient descent.  I still need to
learn more about it in
the context of optimisers, though -- particularly with AdamW.
Dropout
, which
seems to be less than useful for single-epoch training: removing it
helped the model quite a lot.
The learning rate
,
which I built up quite a lot of new knowledge about, and by both increasing it
and scheduling it, I got the biggest bang for the buck.
I've also learned how to
upload my custom models to Hugging Face
,
found out some
interesting things about how random noise affects training
,
and come up with improvements in the setup I have for using an
LLM as a judge for instruction fine-tuned models
.
There was a bit of a mystery when I tried out the instruction fine-tuning tests,
though.  Although two of my models were very close to GPT-2 small in terms of loss,
I found
that while one of them had an instruction fine-tuning result that was likewise close
to GPT-2 small, the other was
much
worse!  A mystery to dig into later, I think.
But it was still very satisfying that my best model -- trained locally in 44 hours
-- was almost as good as GPT-2 small, even if it did fall somewhat short.  So on that
positive note, I'm going to wrap up this "Interventions" series-within-a-series, and move
on to the two other things I wanted to do before wrapping up the "LLM from scratch" series
as a whole:
Going through the appendices in the book to see if there's anything I want
to highlight there.
The final test as to whether I've really understood everything: building my own
LLM from scratch without reference to the book.  I want to do that in a different
framework, not PyTorch, to minimise the risk of just regurgitating code --
I asked people on X/Twitter which one I should use, and
the winner was JAX
-- so it should be interesting to see how that goes!
The appendices first, I think -- I'll post about them shortly.  But I think the big
one will be the JAX implementation -- really looking forward to that.
Here's a link to the next post in this series
.
