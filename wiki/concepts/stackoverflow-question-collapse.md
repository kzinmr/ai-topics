---
title: "Stack Overflow question collapse"
created: 2026-10-30
updated: 2026-10-30
type: concept
tags:
  - ai-agents
  - coding-agents
  - ai-industry
  - information-ecosystem
  - community
  - hn-popular
sources:
  - raw/articles/2026-10-28_hn-discussion_stackoverflow-under-1000-questions-month.md
related:
  - concepts/ai-slop
  - concepts/zombie-internet
  - concepts/coding-agents/agentic-coding
  - concepts/llm-assisted-writing
confidence: medium
---

# Stack Overflow question collapse

In late October 2026 the Stack Exchange Data Explorer query
["Total monthly number of StackOverflow questions over time"](https://data.stackexchange.com/stackoverflow/query/1926661)
crossed a symbolic threshold: **fewer than 1,000 new questions per month** on
stackoverflow.com. The graph hit HN on 2026-10-28 at **789 points / 718 comments**.
It is the clearest single time-series datapoint for what conversational coding agents
did to the public Q&A corpus that those same agents were trained on.

Extraction caveat: `data.stackexchange.com` returns HTTP 403 to programmatic fetches,
so the raw article for this page captures the HN submission metadata plus the top-level
thread rather than the query itself. The number below 1,000 is the story title as
submitted; the query is the primary source and is worth opening interactively.

## Why the datapoint matters beyond nostalgia

Three properties make this more than a "site is dying" story:

1. **It closes a loop.** Stack Overflow answers were a high-signal, human-verified
   corpus and a standard pretraining/fine-tuning and retrieval source for code models.
   The tool that consumed it is now the substitute for asking it. The supply of
   human-authored public programming Q&A has been hollowed out by its own best customer.
2. **The threshold is below the noise floor.** At <1,000 questions/month across a
   site that once peaked in the tens of thousands per month, per-question curation
   (close votes, duplicate closure, accepted answers) no longer meaningfully shapes
   what enters the corpus. The remaining corpus is effectively frozen.
3. **It is a leading indicator for other knowledge commons.** The same mechanism —
   a generative substitute for a contributed corpus — applies to
   [[concepts/zombie-internet]]-style content decay and to any
   [[concepts/agentic-knowledge-work]] surface that depends on public human answers.

## The causation dispute (the actual content of the thread)

The thread splits on *why*, and the disagreement is unresolved. Both sides are
recorded here rather than averaged:

**"AI did it":**
- "Unfortunately they changed ownership very close to when ChatGPT got released, so I
  can't point to timing, but there's just no way this is not because of AI."
- The decline is visible "on all Stack Exchange sites, regardless of moderation
  policy" — which cuts against a site-specific-management explanation, since the
  sister sites have different moderation cultures.
- "AI is so good now I think I'd use it even if Stackoverflow was really friendly."

**"Stack Overflow did it to itself":**
- "AI didn't do it to SO. SO's new ownership did it to SO. It's a hostile place with or
  without AI."
- "All Stack Exchange sites had the same user hostility problem, though SO was by far
  the worst at it."
- Synthesis offered in-thread: hostility determined the *rate*, not the destination —
  "SO's extreme hostility definitely drove people to the first viable alternative (AI)
  as quickly as possible, so it might have survived longer if it hadn't been so
  hostile. But … that would have just delayed its death."

**Confounding, stated by participants:** the ownership change and the ChatGPT release
are near-simultaneous, so the thread itself concedes the timing cannot separate the two
causes. Treat any single-cause version of this story as unsupported by the evidence
available.

**An unanswered question worth tracking:** one commenter notes that AI itself is a huge
new body of programming questions, and asks why that did not slow the decline — i.e.
whether the collapse is a substitution effect across *all* question topics or is
concentrated in legacy topics. No data is offered either way in-thread.

## Related prior datapoints (same SEDE instance)

- "Total monthly number of StackOverflow questions over time" — query 1926661,
  previously 1,550 HN points.
- "What AI did to stackoverflow in a graph" — query 1953768, 483 points / 595 comments,
  roughly three months before the October crossing. That earlier thread is the
  pre-cursor to this one and is where the AI-attribution framing was first stress-tested
  at scale.

## Limits of this page

`confidence: medium`. The primary artifact is a queryable graph behind a 403 for
automated access; the numbers here come from the story title and thread context, not
from a scrape of the series. The site-level question count also does not distinguish
answered-vs-unanswered, closed, or deleted questions, none of which are separable from
the HN discussion. What is solidly established: the threshold crossing was reached, it
was the day's dominant AI-adjacent HN story, and the causation debate is
AI-substitution vs. community-governance-failure with a conceded timing confound.

## Related pages

- [[concepts/ai-slop]] — the reciprocal: generated content flooding what remains
- [[concepts/zombie-internet]] — dead-web / unattended-web content decay
- [[concepts/coding-agents/agentic-coding]] — the substitute workflow
- [[concepts/agentic-knowledge-work]]
- [[concepts/llm-assisted-writing]]
- [[concepts/how-coding-agents-work]]
