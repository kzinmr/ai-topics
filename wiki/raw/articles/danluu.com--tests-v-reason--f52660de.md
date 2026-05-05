---
title: "Testing v. informal reasoning"
url: "https://danluu.com/tests-v-reason/"
fetched_at: 2026-05-05T07:01:34.810800+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Testing v. informal reasoning

Source: https://danluu.com/tests-v-reason/

This is an off-the-cuff comment for Hacker School's Paper of the Week Read Along series for
Out of the Tar Pit
.
I find the idea itself, which is presented in sections 7-10, at the end of the paper, pretty interesting. However, I have some objections to the motivation for the idea, which makes up the first 60% of the paper.
Rather than do one of those blow-by-blow rebuttals that's so common on blogs, I'll limit my comments to one widely circulated idea that I believe is not only mistaken but actively harmful.
There's a claim that “informal reasoning” is more important than “testing”, based mostly on the strength of this quote from Dijkstra:
testing is hopelessly inadequate....(it) can be used very effectively to show the presence of bugs but never to show their absence.
They go on to make a number of related claims, like “The key problem is that a test (of any kind) on a system or component that is in one particular state tells you nothing at all about the behavior of that system or component when it happens to be in another state.”, with the conclusion that stateless simplicity is the only possible fix. Needless to say, they assume that simplicity is actually possible.
I actually agree with the bit about testing -- there's no way to avoid bugs if you create a system that's too complex to formally verify.
However, there are plenty of real systems with too much irreducible complexity to make simple. Drawing from my own experience, no human can possibly hope to understand a modern high-performance CPU well enough to informally reason about its correctness. That's not only true now, it's been true for decades. It becomes true the moment someone introduces any sort of speculative execution or caching. These things are inherently stateful and complicated. They're so complicated that the only way to model performance (in order to run experiments to design high performance chips) is to simulate precisely what will happen, since the exact results are too complex for humans to reason about and too messy to be mathematically tractable. It's possible to make a simple CPU, but not one that's fast and simple. This doesn't only apply to CPUs -- performance complexity
leaks all the way up the stack
.
And it's not only high performance hardware and software that's complex. Some domains are just really complicated. The tax code is
73k pages long
. It's just not possible to reason effectively about something that complicated, and there are plenty of things that are that complicated.
And then there's the fact that we're human. We make mistakes. Euclid's elements contains a bug in the very first theorem. Andrew Gelman likes to use
this example
of an "obviously" bogus published probability result (but not obvious to the authors or the peer reviewers). One of the famous Intel CPU bugs allegedly comes from not testing something because they "knew" it was correct. No matter how smart or knowledgeable, humans are incapable of reasoning correctly all of the time.
So what do you do? You write tests! They're necessary for anything above a certain level of complexity. The argument the authors make is that they're not sufficient because the state space is huge and a test of one state tells you literally nothing about a test of any other state.
That's true if you look at your system as some kind of unknowable black box, but it turns out to be untrue in practice. There are plenty of
unit testing tools
that will do state space reduction based on how similar inputs affect similar states, do symbolic execution, etc. This turns out to work pretty well.
And even without resorting to formal methods, you can see this with plain old normal tests. John Regehr has noted that when
Csmith
finds a bug, test case reduction often finds a slew of other bugs. Turns out, tests often tell you something about nearby states.
This is not just a theoretical argument. I did CPU design/verification/test for 7.5 years at a company that relied primarily on testing. In that time I can recall two bugs that were found by customers (as opposed to our testing). One was a manufacturing bug that has no software analogue. The software equivalent would be that the software works for years and then after lots of usage at high temperature 1% of customers suddenly can't use their software anymore. Bad, but not a failure of anything analogous to software testing.
The other bug was a legitimate logical bug (in the cache memory hierarchy, of course). It's pretty embarrassing that we shipped samples of a chip with a real bug to customers, but I think that most companies would be pretty happy with one logical bug in seven and a half years.
Testing may not be sufficient to find all bugs, but it can be sufficient to achieve better reliability than pretty much any software company cares to.
Thanks (or perhaps anti-thanks) to David Albert for goading me into writing up this response and to Govert Versluis for catching a typo.
