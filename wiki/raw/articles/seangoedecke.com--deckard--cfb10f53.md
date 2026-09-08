---
title: "Automatically detecting AI text in my browser"
url: "https://seangoedecke.com/deckard/"
fetched_at: 2026-09-08T10:01:10.828370+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# Automatically detecting AI text in my browser

Source: https://seangoedecke.com/deckard/

Automated AI text detection is currently an underserved niche. The only game in town is
Pangram
, which does an excellent job but desperately needs more competition. In a few years, I would be surprised if every major social network doesn’t scan new posts
and comments for AI content in order to tag them (or simply remove them).
I like that I can rely on Pangram to confirm my suspicions when I read
something
that sounds like AI. But it’d be much better if I could choose to avoid AI-generated text in the first place. What I want is something that runs in the background and automatically scans text on websites I visit, without me having to ask for it. I could build something like this on top of Pangram, but it’d
cost money
, and in general I don’t like the idea of sending every piece of text my browser sees to a third-party service. What about local models?
The open-source models available for AI text detection are
fine
. Pangram
claims
a 99.66% detection rate with a 0.004% false positive rate. I benchmarked
a bunch of small local models against a combination of AI-detection datasets and got these results:
I’m not surprised these are so much worse. I didn’t even benchmark Pangram’s own EditLens 3B model, since that’s too big to keep running in the background on my laptop, and the real production Pangram model is likely one or two orders of magnitude bigger than that. But these models are still good enough to be useful to someone who understands their limitations. If you want to flag an AI-written article, you don’t need to flag all of it, just enough to be suspicious. And so long as you’re aware that the false-positive rate is ~2%, you can avoid treating a single flag as solid proof of AI use.
Encouraged by this, I vibed up
Deckard
: a Chrome extension that talks to a locally-running model (the bolded one in the table above) on your Mac. One nice thing is that I didn’t have to start a web server: the Chrome extension is happy to start the model as-needed and can talk with it over
native messaging
. It uses about 400MB-1.2GB of memory while active (so it’s like having five or six extra Chrome tabs open), and it turns itself off if you go five minutes without using the model.
I was pleasantly surprised to see Deckard successfully mark text I knew was AI-generated, such as the built-in YouTube AI summary or the AI
snippets
in my own posts:
It’s lightweight enough that I have it running all the time. I haven’t noticed my MacBook Pro get hot at all or any decrease in battery life, though your mileage may vary on different machines.
Is Deckard good yet? That depends. It’s good enough that I’m planning to use it, and I recommend it to anyone who’s interested in automatic AI checking. It’s way, way worse than Pangram, and way worse than I think tooling like this is going to be in the next few years.
Way back in November 2023, I
wrote
that AI-driven agents were going to be a really big deal. I recommended starting to develop harnesses early, so you can be ready when the models get good enough:
As with most modern language model engineering, a ReAct agent can also see massive sudden improvements by swapping out the underlying model for a better one. … I think this is another reason to invest in agents like this early, in order to take advantage of more powerful models as they come out.
I was right about that, and I (although it’s lower-stakes) think I’m also right about this. AI detection models are only going to get better
over time: Pangram is not going to be the only game in town forever, and we’re eventually going to see small local models that do a good-enough job at identifying AI-written text. I look forward to swapping out the local model in
Deckard
with something that’s 2x or 10x better.
Here's a preview of a related post that shares tags with this one.
