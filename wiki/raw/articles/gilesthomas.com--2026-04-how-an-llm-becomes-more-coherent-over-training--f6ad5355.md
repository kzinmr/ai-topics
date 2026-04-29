---
title: "How an LLM becomes more coherent as we train it"
url: "https://www.gilesthomas.com/2026/04/how-an-llm-becomes-more-coherent-over-training"
fetched_at: 2026-04-29T07:02:02.883585+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# How an LLM becomes more coherent as we train it

Source: https://www.gilesthomas.com/2026/04/how-an-llm-becomes-more-coherent-over-training

Archives
Categories
Blogroll
Posted on 17
April 2026
in
AI
I remember finding it interesting when, back
in 2015, Andrej Karpathy posted about RNNs and
gave an example of how their output improves over the course of a training run
.
What might that look like for a (relatively) modern transformers-based LLM?
I recently trained a GPT-2-small-style LLM, with 163 million parameters, on about
3.2 billion tokens (that's about 12.8 GiB of text) from the Hugging Face
FineWeb
dataset, and
over the course of that training run, I saved the current model periodically
-- 57 checkpoints over two days.
Here's what it looked like -- the start, the end, and some interesting waypoints
in between.
For each checkpoint, I asked it to generate a completion to the words "Every effort
moves you".   When the model was first created, before any training had been done, it
came up with this:
Every effort moves youhhhh esoteric Suns 1896ricia enormous initially
speculative arenaelse anth Zimmerman Insight Sketch demonstr despicable
capitalists clamp flung condemnation
If you've read the Karpathy essay, you'll see one important difference -- it's already got words in there.
His RNNs were generating complete noise at this stage.
Even by the 100th iteration, he gives an example like this:
tyntd-iafhatawiaoihrdemot  lytdws  e ,tfti, astai f ogoh eoase rrranbyne
'nhthnee e plia tklrgd t o idoe ns,smtt   h ne etie h,hregtrs nigtike,aoaenns lng
That's an important difference between the RNNs he was talking about, which were
character-based and had to learn about words and the like, and LLMs like this one,
where the text is input and then output one token at a time.
(
More info here
).
Still, even though it has what looks like words, it's essentially content-free token
salad with no structure or coherence .  Let's see what happens if we train it more.
In my training loop, it sees 96 sequences of 1,024 tokens, and then we update it
based on its loss (an index of how wrong it was at predicting next tokens), so that's 98,304 tokens for each step.
After 617 of these  it seems to have mostly learned something about which
tokens are most common:
Every effort moves you and to was, in the, a, The
 your of- and
| to the The
By the next checkpoint at step 1234, we've got
something that's starting to come together.
It doesn't make sense, but there's some kind of glimmering of meaning:
Every effort moves you’ll take the rest of the mainstay in all of his team. This
year with a
And just a little while later, at the checkpoint at step 2468, we have something
that actually makes some kind of sense (at least at the start)!
Every effort moves you to a different country. For all the most part, a world
map can only see the world map
Now, the training data I'm using was scraped from the Internet, and unsurprisingly
there's a lot of somewhat cheesy business content there.  By step 9255, we're starting
to get a lot of stuff like this:
Every effort moves you forward and it is important to make sure that your
clients are satisfied. A number of people have
...or even more cheesy self-help stuff (step 10489):
Every effort moves you to be the best that you will ever have. To be your best,
you should be able to
To be fair, the starting point of "Every effort moves you" is probably biasing things
a bit there.
But let's be clear: by this point it's seen 1,031,110,656 tokens -- that is, it's about
one third trained.  And it's coming up with pretty coherent text!  The rest of the training
run is more about refining things -- the loss chart for this training run looks like this:
Loosely speaking, the lower the loss number, the better the model is, so you can see that the bulk of the improvement had happened by this point.
From here on, I'll just give a few of the more interesting samples:
By step 14191, it's started using bullet points...
Every effort moves you towards your goals.
- Develop meaningful habits or habits that promote your business
- Keep personal and
Step 24680 -- more motivational stuff:
Every effort moves you forward and keeps you motivated. You make sure you don’t
leave it alone.
A
Step 25297 -- small models like this do like repeating themselves.  You might remember
seeing ChatGPT output back in 2023 or so that had tics like this:
Every effort moves you from a simple position to a complex issue of complexity
and complexity.
As soon as the book takes
And again at step 26531
Every effort moves you, the company, the company, the community and all those
involved. I will be pleased to say
At step 27765 it decides that it has had enough after generating just a couple of
words and tries to start a new document:
Every effort moves you to the next level.<|endoftext|>Hip Hop: The New York
Times, April 23, 2017
But step 28382 is actually rather good.  I particularly like the "however":
Every effort moves you, however, towards a better future, and that’s what counts
as a win.
And finally, the training run finishes at step 33164 with these wise words of caution:
Every effort moves you, and you’re rewarded, but not to your potential. You’ve
got to
Well worth remembering, I'm sure we can all agree.  I wonder what deep wisdom
we'd have gained if I had asked it to generate more than 20 new tokens...
What I found most surprising when I first
started playing with this is how
fast
even simple LLMs got to a stage where they could generate
plausible text.  Just one third of the way through the training run, this model
was making some kind of sense.
The problem, of course, is that we don't just want generators of plausible content --
we want that content to make sense and be correct.  And that's why it's worth
grinding through the other two thirds -- in the hope that when you ask it to complete
"The capital of France is", it will reply with "Paris" rather than a coherent but
wrong answer like "Rouen".
