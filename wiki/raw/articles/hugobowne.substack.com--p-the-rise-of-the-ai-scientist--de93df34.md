---
title: "The Rise of the AI Scientist — Vanishing Gradients (Hugo Bowne-Anderson & Hamel Husain)"
url: "https://hugobowne.substack.com/p/the-rise-of-the-ai-scientist"
fetched_at: 2026-09-05T22:50:00+00:00
source: "hugobowne.substack.com"
tags: [podcast, raw]
---

# The Rise of the AI Scientist

Subtitle: *How to Build AI People Can Verify*
Authors: Hugo Bowne-Anderson & Hamel Husain
Published: 2026-09-04
Podcast: Vanishing Gradients
YouTube: https://www.youtube.com/watch?v=QCBLUokyvHA

## Key arguments

Hamel Husain's two connected theses:

1. **"If you feel that a product is hard to eval, or you feel like, 'I don't even
   know how to eval this,' it's a strong smell that your product isn't good."**
   The eval problem is *evidence of bad product design*. If the user can't
   inspect the work well enough to decide whether the answer is right, another
   scoring pipeline won't rescue the experience. The fix begins by exposing the
   evidence and checks a domain expert actually uses.

2. **AI is not killing data science; it's creating more noisy, black-box systems
   that need hypotheses, experimentation, search expertise, and judgment.** The
   people doing this work may eventually be called **AI scientists**.

> "AI has made data science way more valuable than ever before, because now you
> have way more data and way more noisy signals that you need to reason about and
> debug." — Hamel Husain

## The motivating example

An AI data agent tells you last quarter's net revenue. It doesn't show the
metric definition, source tables, filters, query, intermediate calculations, or
assumptions. You can't trust the answer without asking a data scientist to
reproduce it.

## In this episode

- The data agent everyone is building, and why a net-revenue answer without
  definitions, calculations, provenance, or uncertainty only creates more work.
- Hamel's case that AI has made data science more valuable by producing more
  traces, more nondeterministic output, and more noisy systems to understand.
- How agents can learn from human annotations, improve sampling, and help
  validate LLM judges without taking human understanding out of the loop.
- **"Forget evals. Inspect ten traces."** What teams learn by starting with real
  failures instead of an evaluation framework.
- Three AI products redesigned around the expert's actual process: verifying a
  financial number, reviewing a workers' compensation case, and adapting a
  trusted lesson plan.
- Why generic skills have an upper limit; when sharing the sh… (transcript
  continues on the source page).

## Announcement context

Promotes Hamel Husain & Shreya Shankar's *AI Evals For Engineers & PMs* course
starting Sep 6, 2026 — covers instrumenting an agent, inspecting traces,
validated evaluators, regression testing, red teaming, and improving accuracy,
latency, and cost.
