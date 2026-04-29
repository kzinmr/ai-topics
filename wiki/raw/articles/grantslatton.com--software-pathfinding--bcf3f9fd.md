---
title: "Algorithms we develop software by"
url: "https://grantslatton.com/software-pathfinding"
fetched_at: 2026-04-29T07:02:16.813435+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Algorithms we develop software by

Source: https://grantslatton.com/software-pathfinding

Algorithms we develop software by
I recently had a conversation with a distinguished tech CEO and engineer. I loved hearing his description of a software development methodology he's occasionally used, and it got me thinking about other heuristics and generalizations.
His method
Start working on the feature at the beginning of the day. If you don't finish by the end of the day, delete it all and start over the next day. You're allowed to keep unit tests you wrote.
If, after a few days, you can't actually implement the feature, think of what groundwork, infrastructure, or refactoring would need to be done to enable it. Use this method to implement
that
, then come back to the feature.
He said he didn't invent this, but it was something adjacent to the
Extreme Programming
movement of the late 90s and early 00s.
Some thoughts on the method
"Write everything twice"
A piece of advice I've given junior engineers is to write everything twice. Solve the problem. Stash your code onto a branch. Then write all the code again.
I discovered this method by accident after the laptop containing a few days of work died. Rewriting the solution only took 25% the time as the initial implementation, and the result was
much better
.
So you get maybe 2x higher quality code for 1.25x the time — this trade is usually a good one to make on projects you'll have to maintain for a long time.
N.B. Obviously, don't write
literally everything
twice. It's a heuristic. Apply intelligently.
The "start over each day" method is an even more extreme version of this. Every time you rewrite, you carve a smoother path to the solution. The final solution can be really, really clean.
"Quantity has a quality all of its own"
Almost certainly apocryphal Stalin quote is applicable to becoming a good software engineer. As a junior engineer, there's simply no substitute for getting the first 100K lines of code under your belt. The "start over each day" method will help get you to those 100K lines faster.
You might think covering the same ground multiple times isn't as valuable as getting 100K diverse lines of code. I disagree. Solving the same problem repeatedly is actually really beneficial for
retaining
knowledge of patterns you figure out.
You only need 5K perfect lines to see all the major patterns once. The other 95K lines are repetition to rewire your neurons.
Comparison to the "gun to the head" heuristic
Another heuristic I've used is to ask someone to come up with a solution to a problem. Maybe they say it'll take 4 weeks to implement. Then I say "gun to your head, you have to finish in 24 hours, what do you do?"
The purpose here is to break their frame and their anchoring bias. If you've just said something will take a month, doing it in a day must require a radically different solution.
The surprising thing about this technique is
how often it works
. How often someone — minutes after presenting their month-long plan — can be induced to figure out a plan that could potentially be done in a day.
In practice, none of the day-long plans are actually a day. The gun isn't actually to your head. You can go home and sleep. But the new solution can often actually be done in just a few days. A ten-minute thought experiment becomes a 10x time saving.
The purpose of the thought experiment isn't to generate the
real
solution. It's meant to put a lower bound on the solution. Then you think of a
real
solution with that lower bound in eyesight, and you'll find it's often better than your original solution.
Pathfinding
The core of the matter here is pathfinding in problem space. Each path is a solution, and it's the engineer's job to find the best one.
There are a lot of kind of sketchy analogies to be drawn between these heuristics and different pathfinding algorithms. There's some relation to
iterative deepening
,
bounded relaxation A*
,
beam search
,
simulated annealing
, and others.
I don't think there's
too
much to be learned by trying to concretize that analogy, but it's valuable to think about it conceptually. All the different search algorithms have different pros and cons, depending on your constraints and knowledge of the domain.
So too with the engineering heuristics. Becoming a better engineer is becoming a better pathfinder in problem space.
There's probably a compelling general theory to be concocted in this space, but that's beyond the scope of this post. Spin up a background thread in your brain and think about it. Maybe you'll find a good path to an answer.
