---
title: "NYC, New Webinar, Differential Testing"
url: "https://buttondown.com/hillelwayne/archive/nyc-new-webinar-differential-testing/"
fetched_at: 2026-10-23T10:01:33.164253+00:00
source: "buttondown.com/hillelwayne"
tags: [blog, raw]
---

# NYC, New Webinar, Differential Testing

Source: https://buttondown.com/hillelwayne/archive/nyc-new-webinar-differential-testing/

Been a while! Man, it's so much harder to write essays for a newsletter when I have a full time job writing essays for a company.
So three bits of housekeeping first of all:
As of last month I now live in NYC! Let me know if you want to get coffee or have me swing by an office or something.
My first big Antithesis deliverable is coming out next Thursday, and it's a
webinar on property-based testing
. What's going to make this one interesting is that it's about property testing
web applications
. I've got this crazy idea that the main way to make randomized testing accessible and useful is to focus on state-based system invariants as opposed to algebraic laws and roundtrip properties. Send it to webdevs you know!
Anyway, to make this actually a newsletter and not just a bunch of updates, one thing I've been thinking about recently is nondeterministic
differential testing
. Say we have a python program and we tell a slopinator to convert it to rust. How do we know that it didn't change the program's behavior?
For a totally deterministic program, this is straightforward
differential testing
: feed inputs into both and compare the results. Let's scrap out a quick notation and say that
A -> (x, y)
represents an execution where we input
A
, and observe that the original program output
x
and the new program output
y
. So
A -> (1, 1)
means that the programs agree on input
A
, while
B -> (1, 2)
means they get different values for input
B
. The programs are different if we observe a single disagreement, meaning we can increase our relative confidence in our translating by trying an increasing number of inputs.
That's the base case, anyway. But this only really works because there's no point in repeating observations on the same input. If the program is nondeterministic, we can get situations like this:
A -> (200 OK, 408 request timeout)
A -> (200, 200)
Are the program different? We can't be sure! If the
original
system always returns 200, then they're different. But we don't know that for sure from the observations we have! Maybe a third observation will give us
A -> (408, 200)
. In other words, a table of what we know, given an observation and level of uncertainty:
Deterministic?
A -> (x, y)
A -> (x, x)
Yes
definitely different
¯\_(ツ)_/¯
No
¯\_(ツ)_/¯
¯\_(ツ)_/¯
Once you need mutiple observations you're already dealing with the mess known as
hyperproperties
. But we can make it even more complicated than that! What if we have this set of observations:
A -> (200, 408)
A -> (200, 200)
A -> (408, 408)
You could argue the two programs agree on observations of A. Not so fast! One thing we
haven't
seen is
A -> (408, 200)
. Maybe there's no world where the
old
program times out but the
new
program gets 200. Even though they get the same set of nondeterministic outputs, one can still be more reliable than the other. This makes it much harder to show the two programs are the same: if you observe
A -> (x, y)
, it's not enough to observe
A -> (z, x)
, you have to
specifically
observe
A -> (y, x)
.
Okay, but what if the
relative rate
of values in observations matter? What if the new program gets a
408 timeout
100x as often? What if your LLM converted a fair coin flip to an unfair coin flip? Then even if we see
A -> (H, T)
and
A -> (T, H)
, we still have a program divergence.
In short, two challenges with nondeterministic differential testing are 1) we can't conclude a difference from a single divergent observation and 2) the concept of "difference" is way murkier than in deterministic programs. Though TBF even with deterministic programs the same output can be a divergence if one takes a
lot
longer. It all depends on how you define correctness!
(I think in most cases, we can get away with just showing two nondeterministic programs produce the same set of values. That's still pretty hard, but at least it's not messing with probability.)
