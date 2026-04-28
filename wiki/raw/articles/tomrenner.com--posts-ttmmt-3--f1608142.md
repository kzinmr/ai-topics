---
title: "Things that made me think: Cycle time, learning theory, and build chain security"
url: "https://tomrenner.com/posts/ttmmt-3/"
fetched_at: 2026-04-28T07:01:45.045714+00:00
source: "tomrenner.com"
tags: [blog, raw]
---

# Things that made me think: Cycle time, learning theory, and build chain security

Source: https://tomrenner.com/posts/ttmmt-3/

This series
is a place to collect interesting things I’ve seen, read, or heard, along with some brief thoughts (often incomplete and/or inconclusive) that they provoked.
Cycle time is a measure lots of people use, but has no clear audience - developers, managers, CTOs all care about it. This makes it dangerous. Metrics have to be designed and used with psychological safety in mind. If people don’t trust the intention behind the metrics use, they’ll game it.
Cycle time is
massively variable
; between developers, within one developer’s year, annual variations (christmas, summer holidays, OKR timetables, etc.) – you need a
really long
timeframe over which to measure to use it sensibly.
Once you have a metric you’ve measured semi-successfully, don’t use it to benchmark, don’t assume it covers all work (plenty is not tracked by cycle time), and make sure you always connect it to outcomes – eg. shorter cycle time doesn’t mean customers are happy.
… all of which makes me just very cautious about measuring anything in my team! I’m not sure that’s the takeaway I was meant to have…
Firstly, Hazel is such a badass, and I love everything she writes. This post really shaped my thinking about how to successfully use LLMs and not just keep feeding text into the software slot machine in the hope that it eventually gives the right answer.
It made me realise that I need to learn more about learning! Because by building learning theory into the design of our interactions with AI, Hazel superbly articulates what
better
could look like for these tools, and how a sensible product that supported its users’ development might work.
Now I need to review the EDGE framework she mentions in more detail, and reflect on how I approach learning-on-the-job. And if I’m really aiming to be an overachiever, I should put that into terms my team will connect with, so they get the most out of our LLM toolsets as well.
Github Actions are shockingly insecure (it turns out). I was not aware of this previously, and could easily see myself falling into some of the pitfalls that were exploited here. Ellie (
@ptrpaws
, the author) used them to gain read/write access to nixpgs, giving them the ability to nuke the entire system from orbit, had they so chosen.
Supply-chain attacks are so scary - it’s so much harder conceptually to treat your build chain with the same security mindset you treat application code (and most developers sadly don’t treat that very carefully either!), but really that’s the higher-risk attack surface.
And finally - this kind of “not my problem, guv” warning from tools is
never
helpful:
It is not possible for xargs to be used securely
taken directly from the
man page
. Sigh. Almost as useless as the legalese telling users not to rely on Tesla’s “Fully Self Driving” system to actually, you know, drive the car.
If you market the tool as functional, you get zero credit from me for stating in the fine print that a use case is unsupported. Users use the tools you give them, it’s on you to make sure it’s safe to do so.
Reactions collected from around the web using
webmentions
