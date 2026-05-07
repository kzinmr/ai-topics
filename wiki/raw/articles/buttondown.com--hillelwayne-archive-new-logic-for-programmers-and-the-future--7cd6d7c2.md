---
title: "New Logic for Programmers (and the future of this newsletter)"
url: "https://buttondown.com/hillelwayne/archive/new-logic-for-programmers-and-the-future-of-this/"
fetched_at: 2026-05-07T07:01:38.971615+00:00
source: "buttondown.com/hillelwayne"
tags: [blog, raw]
---

# New Logic for Programmers (and the future of this newsletter)

Source: https://buttondown.com/hillelwayne/archive/new-logic-for-programmers-and-the-future-of-this/

So first the immediate news: I just released version 0.14 of
Logic for Programmers
! This release is pretty similar to 0.13. There are a few rewrites but the vast majority of the changes are layout, copyediting, and technical editing. Full notes
here
.
In related news, I've started doing test prints of the book:
There's not a whole lot left to be done. I've gotta fix up some diagrams, do more formatting and proofreading, incorporate some fixes raised by readers, and make a website and back cover. After that, the book should be ready for 1.0. I'm aiming to have print copies purchasable by the end of June!
Now the big news: starting August, I'll be a full-time employee of
Antithesis
, a generative testing platform. Officially my role is "developer educator", and I'll be tasked with making "property-based testing, fuzzing, fault injection,
Hegel
,
Bombadil
, and the Antithesis platform understandable to everyday engineers". So the same kind of work I do now, except with far more support and a matching 401(k).
I already have three pages of topic ideas you have no idea how excited I am about this
So how is this going to affect the newsletter? First, I want to make clear that this is
not
going to become an Antithesis newsletter. My Antithesis-related work is going to be on their official platforms. I do think one of the best ways to make a topic "understandable" is to write foundational material that's useful to all engineers, whether they're invested in the topic or not. I might share links to things I make along those lines, but they'll be just that, links.
At the same time, the content of
this
newsletter will change a little. Property testing and fuzzing aren't the same as formal methods, but a lot of the foundations overlap, especially in how we think about properties and correctness. I don't know for sure yet, but I suspect that I'll start biasing this newsletter away from Antithesis related topics. So there will probably be less theoretic things like
what does undecidable mean
and
Some tests are stronger than others
and more history and software weirdness things like
Why do we call it "boilerplate code"
and
esoteric programming paradigms
.
The other change is going to be frequency. For the past six years I've kept updates to (mostly) a weekly schedule. For the past six years I've also been totally self-employed. I don't know how much time I'll have with a full time job! Once I'm settled in I'd like to keep writing newsletters, but it might slow down from weekly to biweekly or monthly. We'll feel it out as we go.
Anyway, this has been a pretty software-light newsletter, so let's close out with a fun thing.
f(x) = x+2
is a
monotonically increasing function
: increasing
x
increases
f(x)
and decreasing
f(x)
decreases
f(x)
.  Similarly,
f(x) = -x+1
is monotonically decreasing, and
f(x) = x^2
is neither.
While working on the book I realized that the
all
quantifier is monotonically false with respect to adding elements and true with respect to removing them. Let
A(set) = all x in set: P(x)
. Then if
A(S)
is false,
A(S | {e})
is also false, and if
A(S)
is true,
A(S - {e})
is also true.
some
goes the other way: if it's true, it's true if you add an element, and if it's false it's still false if you take one away.
An interesting consequence is that
all
must
be true for the empty set, because if it was false it would be false for all values! This is another justification why, in Python,
all([]) == True
.
Similarly, in temporal logic:
always A
is monotonically false with respect to system behavior and
eventually A
is monotonically true. I realized this when messing with this
LTL visualizer
my friend (and soon to be coworker!) Oskar Wickström. I think this is pretty neat!
