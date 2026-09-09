---
title: "Terence Tao: AI, Mathematics, and the Honest Midterm (Sep 2026)"
source_url: https://www.terrytao.wordpress.com/2026/09/08/ai-mathematics-and-the-honest-midterm/
ingested: 2026-09-09
sha256: 417948a35f73938f853795cf5f402419151994b45a07a6d6297389484096b216
note: |
  Fetched and hashed, but NOT promoted to its own wiki page: the post is a
  re-delivery of Tao's earlier "frontiers of AI in mathematics" survey material
  plus one SWE-Lancer anecdote, with no new claims beyond what
  entities/terry-tao.md already carries. Retained here for source-drift tracking
  and because the SWE-Lancer single-shot-vs-multi-run lesson is cross-linked
  from concepts/ai-benchmarks/hyper-tau-bench.md.
---

# AI, Mathematics, and the Honest Midterm

I have previously discussed the impact of AI on mathematics education
("Mathematical error checking and AI assistance", "Master's and PhD theses in the
age of generative AI", "The Honest Midterm") and the impact of AI on
mathematical research ("Frontiers of AI in mathematics").  In this talk I will
combine these two threads together, discussing a phenomenon that I call the
"honest midterm" - the way in which the availability of AI assistance can cause
students to learn less, while also causing their grades to improve.  I will also
be discussing how this phenomenon impacts not just students, but also
mathematicians and the general public, before concluding with some thoughts on
how one might design assessments, curricula, and evaluation pipelines to be more
"AI-resistant".

(The talk is largely based on my earlier survey "Frontiers of AI in mathematics",
updated with recent developments, and is intended for a general audience; I will
also be describing some recent anecdotes involving the SWE-Lancer benchmark
illustrating how easily AI capability claims can be over- or under-reported when
the precise evaluation protocol - single-shot versus multi-run, with or without
scaffolding - is not stated alongside the number.)

Roughly speaking, the honest midterm is a form of the more general phenomenon of
"evaluation hacking" or "reward hacking" in which a metric (a grade, a benchmark
score, a leaderboard position) is improved without the underlying capability
that the metric was supposed to measure actually improving.  Students,
mathematicians, and the public are all subject to this failure mode, and the
appropriate response in each case is to redesign the measurement so that it
cannot be satisfied without the real skill - which is exactly what an
"AI-resistant" assessment or benchmark attempts to do.

This is why I have been cautious about quoting headline capability numbers
without the protocol attached.  A single-shot score on a coding benchmark is not
the same object as a two-run average with tool use and iteration; a "100%" that
measures one attempt at a task is not a refutation of a published multi-run
number, and treating it as one conflates the two protocols.  The same discipline
applies to the AI-resistant evaluation designs I discuss: the value of the
benchmark is in the protocol, not in the scalar.

(See also my notes on AI assistance in mathematical practice: the appropriate
level of AI assistance in undergraduate education, in graduate education, in
research, and in exposition.)
