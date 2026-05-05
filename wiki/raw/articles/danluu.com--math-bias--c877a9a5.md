---
title: "Do programmers need math?"
url: "https://danluu.com/math-bias/"
fetched_at: 2026-05-05T07:01:35.395036+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Do programmers need math?

Source: https://danluu.com/math-bias/

Dear
David
,
I'm afraid my off the cuff response the other day wasn't too well thought out; when you talked about taking calc III and linear algebra, and getting resistance from one of your friends because "wolfram alpha can do all of that now," my first reaction was horror-- which is why I replied that while I've often regretted not taking a class seriously because I've later found myself in a situation where I could have put the skills to good use, I've never said to myself "
what a waste of time it was to learn that fundamental mathematical concept and use it enough to that I truly understand it
."
But could this be selection bias? It's easier to recall the math that I use than the math I don't. To check, let's look at the nine math classes I took as an undergrad. If I exclude the jobs I've had that are obviously math oriented (pure math and CS theory, plus femtosecond optics), and consider only whether I've used math skills in non-math-oriented work, here's what I find: three classes whose material I've used daily for months or years on end (Calc I/II, Linear Algebra, and Calc III); three classes that have been invaluable for short bursts (Combinatorics, Error Correcting Codes, and Computational Learning Theory); one course I would have had use for had I retained any of the relevant information when I needed it (Graduate Level Matrix Analysis); one class whose material I've only relied on once (Mathematical Economics); and only one class I can't recall directly applying to any non-math-y work (Real Analysis). Here's how I ended up using these:
Calculus I/II
: critical for dealing with real physical things as well as physically inspired algorithms. Moreover, one of my most effective tricks is substituting a Taylor or Remez series (or some other approximation function) for a complicated function, where the error bounds aren't too high and great speed is required.
Linear Algebra
: although I've gone years without, it's hard to imagine being able to dodge linear algebra for the rest of my career because of
how general matrices are
.
Calculus III
: same as Calc I/II.
Combinatorics
: useful for impressing people in interviews, if nothing else. Most of my non-interview use of combinatorics comes from seeing simplifications of seemingly complicated problems; combines well with probability and
randomized algorithms
.
Error Correcting Codes
: there's no substitute when you need
ECC
. More generally, information theory is invaluable.
Graduate Level Matrix Analysis
: had a decade long gap between learning this and working on something where the knowledge would be applicable. Still worthwhile, though, for the same reason Linear Algebra is important.
Real Analysis
: can't recall any direct applications, although this material is useful for understanding topology and measure theory.
Computational Learning Theory
: useful for making the parts of machine learning people think are scary quite easy, and for providing an intuition for areas of ML that are more alchemy than engineering.
Mathematical Economics
:
Lagrange multipliers
have come in handy sometimes, but more for engineering than programming.
Seven out of nine. Not bad. So I'm not sure how to reconcile my experience with the common sentiment that, outside of a handful of esoteric areas like computer graphics and machine learning, there is
no
need
to
understand
textbook
algorithms
, let alone more abstract concepts like math.
Part of it is selection bias in the jobs I've landed; companies that do math-y work are more likely to talk to me. A couple weeks ago, I had a long discussion with a group of our old
Hacker School
friends, who now do a lot of recruiting at career fairs; a couple of them, whose companies don't operate at the intersection of research and engineering, mentioned that they politely try to end the discussion when they run into someone like me because they know that I won't take a job with them.
But it can't all be selection bias. I've gotten a lot of mileage out of math even in jobs that are not at all mathematical in nature. Even in low-level systems work that's as far removed from math as you can get, it's not uncommon to be find a simple combinatorial proof to show that a solution that seems too stupid to be correct is actually optimal, or correct with high probability; even when doing work that's far outside the realm of numerical methods, it sometimes happens that the bottleneck is a function that can be more quickly computed using some freshman level approximation technique like a Taylor expansion or Newton's method.
Looking back at my career, I've gotten more bang for the buck from understanding algorithms and computer architecture than from understanding math, but I really enjoy math and I'm glad that knowing a bit of it has biased my career towards more mathematical jobs, and handed me some mathematical interludes in profoundly non-mathematical jobs.
All things considered, my real position is a bit more relaxed than I thought: if you enjoy math, taking more classes for the pure joy of solving problems is worthwhile, but math classes aren't the best use of your time if your main goal is to transition from an academic career to programming.
Cheers,
Dan
Russian translation available here
