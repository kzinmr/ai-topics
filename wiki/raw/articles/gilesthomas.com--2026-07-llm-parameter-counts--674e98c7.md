---
title: "Building intuition about LLM parameter counts"
url: "https://www.gilesthomas.com/2026/07/llm-parameter-counts"
fetched_at: 2026-07-11T07:00:48.109001+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Building intuition about LLM parameter counts

Source: https://www.gilesthomas.com/2026/07/llm-parameter-counts

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
Posted on 10
July 2026
in
AI
When I was
building my GPT-2 implementation in JAX
,
I started with just token embeddings for the input, and a separate output head (as I was not using
weight tying
).  It wasn't an
LLM -- no Transformer blocks, no attention, no feed-forward networks.
I was somewhat surprised when I noticed that even that stripped-down model had 77 million parameters
with the "small" settings I was using to train -- specifically, an embedding dimension of 768.
However, I realised I shouldn't be -- with a vocab size of 50,257, each of those components is essentially
a
768
×
50
,
257
matrix, and that is indeed over 38 million numbers.
But the finished LLM at the end of the project was only 163 million parameters -- that meant that the
input and output components alone were almost half of it.  That felt
like a surprisingly large percentage.
I had a similar shock when I was first looking into
the feed-forward network
,
and realised that it had roughly twice as many parameters as the attention layers.
When we learn about the internals of LLMs, a lot of the focus is on the attention
mechanism.  This makes sense -- it's the hardest part to get your head around.  The
rest of the setup, at least for simple GPT-2 type models, is fairly standard stuff.
But that means that it is easy to overestimate how much of the total
parameter count of the model attention uses up -- especially for smaller models,
where the token embeddings and the output head are so large in comparison to
the Transformer layers that make up the actual body of the LLM.
OpenAI released GPT 5.6 today, so I decided to take its "Sol" variant for a ride
in Codex and asked it to write
a visualiser
.
It shows
breakdowns of how the parameters are split between embeddings, attention, the FFNs, and
the output head
for different sizes of GPT-2 models (or your own custom settings
with the same architecture), and you can also add/remove weight tying and QKV bias.
It did a really good job -- check it out!  Here's a screenshot of what it showed
for GPT-2 small without weight tying.
It's well worth a play.  In particular, it's interesting to see what happens
as the number of tokens in the vocab gets very large (many modern models have
hundreds of thousands).  You can very easily create a "tiny" model which is
almost entirely embeddings and the output head.
