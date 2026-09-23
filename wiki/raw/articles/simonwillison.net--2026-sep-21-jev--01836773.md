---
title: "Jev introduces a new shape of LLM-System One, aka Decision Models"
url: "https://simonwillison.net/2026/Sep/21/jev/"
fetched_at: 2026-09-22T10:00:53.446718+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Jev introduces a new shape of LLM-System One, aka Decision Models

Source: https://simonwillison.net/2026/Sep/21/jev/

Jev introduces a new shape of LLM—System One, aka Decision Models
21st September 2026
Last week
TypeSafe AI
unveiled
Jev
, their first example of a new category of model that they are calling “System One models” (I’m with Maggie Appleton, I think “decision models” is
a better name
for these). Jev is an interesting variant on the usual LLM format: it still accepts text inputs, but instead of text output it returns floating point numbers corresponding to categories, yes/no questions, ratings, and associated confidence scores.
TypeSafe describe Jev like this:
Think of Jev as a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out.
It’s also very fast, and
really cheap
. Regular LLMs
are priced
in terms of input and output tokens, with output generally charged at significantly higher rates. Jev charges only for input—output is free—and the input price of their first model is $0.042 per million tokens—cheaper even than OpenAI’s
GPT-5 Nano
($0.05/million).
Jev lets you ask questions about text or semi-structured data. You compose a “state” object containing a string, array of strings, or set of name-value pairs—this might describe an article, or a customer, or any other kind of record. You then send that to their API with one or more questions, and get a reply back for each.
You can ask three kinds of questions:
Yes/No questions, which Jev calls “Noul” questions—their CEO
confirmed on Hacker News
that this is short for Bernoulli, from the
Bernoulli distribution
. You pose a statement and get back a floating point number between 0 and 1 for how confident the model is that the statement is true.
Choice questions, where the model picks one from a set of provided options—actually a confidence score plus a probability distribution across all of the options.
Score questions, where you provide sequence of numeric levels with descriptions and it provides a floating point score somewhere along that range.
The Jev API can accept a single document (“state”) and as many questions as you can cram into the context window. Questions are evaluated in parallel, so sending many questions should take a similar time to sending just one.
I think the
decision model
framing is useful for understanding where to use Jev. It’s great for anything that can be expressed as a classification task—think spam detection, suggesting labels, prioritization and ranking.
I’ve also been experimenting with it for search reranking, where you fetch 100 likely matches using an inexpensive algorithm like BM25, then have Jev score those 100 candidates for relevance against the original query.
Black boxes are back in fashion
Something I’ve found a little uncomfortable about Jev is how it very much represents a regression even further towards black box machine learning systems.
LLMs are black boxes already—you can ask them to justify their decisions, but you can’t guarantee that what they say is useful or accurate.
Jev doesn’t even give you that: put in all the text you want, the only thing you’re going to get back is a floating point number. If Jev marks something as spam, which content signals tipped it off?
This also means that concerns about bias should be front and center. I really hope nobody uses Jev to rank job applicants—that floating point number could conceal all manner of unseen bias baked into the models, and experimentally picking that bias apart is going to be a tricky business.
(I tried one experiment where I had Jev score every city in the San Francisco Bay Area on a yes/no answer to whether they were a “Good city?”—it rated
Cupertino
top and
East Palo Alto
bottom. Huh.)
In practice, this all means that evals and structured experiments are even more important than they are for regular LLM projects. Thankfully, Jev is so cheap that running hundreds or even thousands of experimental prompts through it costs just a few cents.
Unconventional uses for Jev
It’s been really fun watching the wider community come up with potential use-cases for Jev over the past few days. Here are some creative ones that caught my eye:
jevchat
by Kyle Pena turns Jev into a (terrible) chat model. “At every step it asks Jev one question: Given the user’s question and the reply written so far, which symbol comes next?”.
ericpruitt on Hacker News
: “It’s the digital equivalent of Morty speaking with the death crystal”.
jev-leftpad
by Fatih Kadir Akın implements
left-pad
with the prompt “How many spaces are needed before value to reach targetLength?” and
a choice query
allowing options from “0 spaces are needed” to “10 spaces are needed”.
jev-2048
by Andy Gayton uses Jev to play
the 2048 sliding puzzle game
.
Open weight recreations
There’s also been a flurry of projects attempting to create a model like Jev using on top of open weight models.
Kev
is one interesting example, using Qwen 3.5 to produce 0.8B, 4B, and 9B models. Here’s the
accompanying Hacker News thread
, where someone linked to a
JevBench
benchmark that has already cropped up to compare “Jev-class decision models”.
Given Jev was released just under a week ago, the amount of activity around it is extremely impressive.
