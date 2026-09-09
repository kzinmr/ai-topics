---
title: "Simon Willison: 800 Lines of Ruby (Sep 2026)"
source_url: https://simonwillison.net/2026/Sep/7/800-lines-of-ruby/
ingested: 2026-09-09
sha256: 86e6168121c76c2115913993f6cc232172e623346725dc74e5db0c604f07d998
note: |
  Already fully ingested in an earlier session. Raw retained only for sha256
  source-drift tracking; no wiki page was created or updated by this crawl.
  Related existing coverage: concepts/ai-benchmarks/swe-bench.md, entities/simon-willison.md.
---

# 800 Lines of Ruby

I've spent the past week writing a good chunk of my pelican-weblog clone in Ruby,
and I'm delighted to report that it's now at 800 lines and doing everything I
need it to do.

The interesting part, for me, is how much of that work was done by the models. I
started from a description of the features I wanted, and Claude Code did most of
the transcription - file upload, thumbnail generation, EXIF extraction, the
Markdown pipeline, the whole thing. My contribution was mostly in deciding what
to build and in reviewing the diffs.

There's a specific kind of maintenance tax that a project like this used to
carry. I've maintained four implementations of this blog engine over the years -
Django, Django again, Datasette-backed, and now Ruby. Every time I add a feature
I have to think about whether it belongs in a plugin or in the core, and whether
I'll still understand the code in three years.

That tax is what made side projects slow. What I'm finding is that the models
have collapsed the cost of *starting* a project to nearly zero, and they've
mostly collapsed the cost of *continuing* one - but they have not collapsed the
cost of *knowing what you want*. The 800 lines are cheap. The decisions are not.

I keep coming back to the same conclusion: the bottleneck is no longer typing the
code, it's having a clear idea of the thing you want and being able to describe
it precisely enough that you can tell when the output is wrong. That's a design
skill, not a programming skill, and I suspect it's the skill that increasingly
separates people who get a lot out of these tools from people who don't.

The code is on GitHub if you want to see how the models and I structured it.
