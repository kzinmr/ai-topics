---
title: "The Zig project's rationale for their firm anti-AI contribution policy"
url: "https://simonwillison.net/2026/Apr/30/zig-anti-ai/#atom-everything"
fetched_at: 2026-05-01T07:13:05.389309+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# The Zig project's rationale for their firm anti-AI contribution policy

Source: https://simonwillison.net/2026/Apr/30/zig-anti-ai/#atom-everything

Zig
has one of the most stringent
anti-LLM policies
of any major open source project:
No LLMs for issues.
No LLMs for pull requests.
No LLMs for comments on the bug tracker, including translation. English is encouraged, but not required. You are welcome to post in your native language and rely on others to have their own translation tools of choice to interpret your words.
The most prominent project written in Zig may be the
Bun
JavaScript runtime, which was
acquired by Anthropic
in December 2025 and, unsurprisingly, makes heavy use of AI assistance.
Bun operates its own fork of Zig, and recently
achieved a 4x performance improvement
on Bun compile after adding "parallel semantic analysis and multiple codegen units to the llvm backend". Here's
that code
. But
@bunjavascript says
:
We do not currently plan to upstream this, as Zig has a strict ban on LLM-authored contributions.
(Update: here's
a Zig core contributor
providing details on why they wouldn't accept that particular patch independent of the LLM issue - parallel semantic analysis is a long planned feature but has implications "for the Zig language itself".)
In
Contributor Poker and Zig's AI Ban
(
via Lobste.rs
) Zig Software Foundation VP of Community Loris Cro explains the rationale for this strict ban. It's the best articulation I've seen yet for a blanket ban on LLM-assisted contributions:
In successful open source projects you eventually reach a point where you start getting more PRs than what you’re capable of processing. Given what I mentioned so far, it would make sense to stop accepting imperfect PRs in order to maximize ROI from your work, but that’s not what we do in the Zig project. Instead,
we try our best to help new contributors to get their work in, even if they need some help getting there
. We don’t do this just because it’s the “right” thing to do, but also
because it’s the smart thing to do
.
Zig values contributors over their contributions. Each contributor represents an investment by the Zig core team - the primary goal of reviewing and accepting PRs isn't to land new code, it's to help grow new contributors who can become trusted and prolific over time.
LLM assistance breaks that completely. It doesn't matter if the LLM helps you submit a
perfect
PR to Zig - the time the Zig team spends reviewing your work does nothing to help them add new, confident, trustworthy contributors to their overall project.
Loris explains the name here:
The reason I call it “contributor poker” is because, just like people say about the actual card game, “you play the person, not the cards”. In contributor poker, you bet on the contributor, not on the contents of their first PR.
This makes a lot of sense to me. It relates to an idea I've seen circulating elsewhere: if a PR was mostly written by an LLM, why should a project maintainer spend time reviewing and discussing that PR as opposed to firing up their own LLM to solve the same problem?
