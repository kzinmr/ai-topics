---
title: "On the Navier-Stokes Millennium Prize Problem"
url: "https://simonwillison.net/2026/Sep/8/on-navier-stokes/"
fetched_at: 2026-09-09T10:00:59.776958+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# On the Navier-Stokes Millennium Prize Problem

Source: https://simonwillison.net/2026/Sep/8/on-navier-stokes/

On the Navier–Stokes Millennium Prize Problem
(
via
) Impressive result from OpenAI, who used an unreleased model to produce a resolution to
the Navier–Stokes existence and smoothness problem
, one of the seven
Millennium Prize Problems
that have been subject to a $1,000,000 prize since May 24th, 2000.
The discovery is somewhat overshadowed by accusations of skulduggery from Tristan Buckmaster, an NYU mathematics professor who was collaborating on related problems with Levent Alpöge, an accomplished mathematician who currently works for Anthropic.
Tristan's complaint accompanied
a hastily published version
of their own results.
Here's the PDF describing what happened
. The
very
short version is that Tristan and Levent worked on the problem for almost a year, making extensive use of Claude and Codex (mainly GPT-5.6 Sol), then had a breakthrough on August 15th. The mathematical rumour mill kicked into gear and Tristan and Levent heard that OpenAI had heard that Anthropic had resolved "a major open problem", so they reached out and learned that OpenAI had a team working on a related problem, with a similar approach. Quoting Tristan:
I asked when the first prompt had been sent by them. This question was not answered directly by OpenAI for some time. Eventually it was agreed that it had been sent in the past few days, after information about our work had reached OpenAI.
I asked whether the model had been trained on, or had access to, our sessions in Codex, into which we had been putting all our drafts for the whole of this project. I was told the model did not look up user data. I asked again, about training, and I did not get an answer.
It gets more complicated from there. The OpenAI team offered to wait for Tristan to publish, or to have him author a paper about their result, but were clear that Levent would
not
be invited as a co-author due to OpenAI's competitive relationship with his employer.
Here's how OpenAI described their work:
On Tuesday, September 1, we heard rumors that two Millennium Prize problems had been resolved. Inspired by these rumors and by the step change in performance of our internal model, we launched an effort to evaluate it on all open Millennium Prize problems and a few other high-impact problems. [...]
The agents arrived at their resolution on Saturday, September 5, about 88 hours after the first agents were launched. Lean formalization and verification took an additional 17 hours via GPT‑6 Astra.
Across all attempted problems, the agents sent 4.9 million messages and used about 300 billion output tokens. In the process of resolving the Navier–Stokes problem, the agents sent 2.7 million messages and used approximately 130 billion output tokens.
(We don't know the cost structure of the internal model they used, but 300 billion output tokens at public API prices for GPT-6 Astra would cost
$15,000,000
.)
Here's where they provide their perspective on Tristan and Levent's work (emphasis mine):
Our effort began on September 1st after hearing a rumor which we later realized was related to Levent Alpöge, an Anthropic employee, and Tristan Buckmaster, a math professor at NYU. After the completion of our full project and Lean verification (on September 6th), believing from the rumor they also had a solution of Navier–Stokes, we reached out to them to offer a concurrent release of our result and to recognize their priority in a joint announcement. [...]
We (the researchers and the agents) did not see any of their work through any means until they released it publicly — in particular, no specific user data was accessed in order to solve this problem.
While unlikely, we cannot rule out that de-identified data derived from their usage of our products helped
improve our models
. However, our proofs differ significantly and even the precise results proved are different in the Euler case (forced vs unforced).
My interpretation of what happened here is that OpenAI heard that some Millennium Prize problems had been solved using LLMs and saw this as an opportunity to demonstrate the power of their latest model, without thinking too hard about the optics of scooping a team who had been using OpenAI's own models to work on this problem for the best part of a year.
This situation appears to mirror what's happening in the world of computer security right now. Anil Madhavapeddy recently pointed out that
Just a rumour of a bug is enough to find a security exploit these days
, because if someone knows that some software has an unpatched vulnerability, they can set their agents the task of finding it. Is the same now true of mathematics? Just knowing that there is an unpublished solution to a problem might trigger millions of dollars in LLM spending to get there first.
This also highlights one of my ongoing frustrations about how all of this works. When an AI lab says that my data is "used to improve model performance",
what does that actually mean
?
My two favourite hypothetical questions regarding this used to be:
If I'm running Codex and one of my API keys accidentally gets consumed in the context, what are the chances that someone else might ask for an API key in the future and get mine back? (I asked someone at OpenAI once and they called this the "regurgitation" problem and assured me that they take great pains to prevent that... but wouldn't describe how.)
If I brainstorm with ChatGPT about potential new directions for my company, what's the chance that information might be exposed to a competitor in six months' time who asks "what might company X plan to do next"?
My new preferred hypothetical for this is:
If I use ChatGPT to help me partially solve a Millennium Prize problem, what are the chances that my work will influence training such that a later model helps someone
else
solve it first?
