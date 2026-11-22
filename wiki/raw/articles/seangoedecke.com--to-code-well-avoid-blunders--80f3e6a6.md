---
title: "To code well, avoid blunders"
url: "https://seangoedecke.com/to-code-well-avoid-blunders/"
fetched_at: 2026-11-22T10:01:11.724209+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# To code well, avoid blunders

Source: https://seangoedecke.com/to-code-well-avoid-blunders/

The secret to writing good code
1
is to avoid catastrophic mistakes. Many engineers think about programming as if the goal is to have brilliant insights, but they’re wrong. If you don’t blunder, you will win.
Many other domains are like this. If you can play chess without ever hanging pieces, you will win against almost any
2
opponent. If you are very good at
returning
tennis balls, you will beat most players even if you never hit a winner. People are really bad at internalizing this. They think that being good at chess means finding brilliant tactical combinations, or that being good at tennis means crushing balls into the corner of the court, or that being a good programmer means discovering beautiful new abstractions. Not so! All of those things are valuable, but they are not the main thing. The main thing is to avoid catastrophic mistakes.
The reason programming is like this is that it is impossible to build a durable winning advantage. In basketball, if you are up 99-1, the worst consequence of a blunder is still being up 99-4. However, in programming, one blunder can turn an elegant codebase into a janky one. For instance, consider these blunders:
Introducing a parallel system to perform the same task
Introducing a second source of truth for some key piece of data
Turning a safe sync operation into a delicate async one
Adding new subtle points of failure
Complicating a key interface
The cardinal sins here are
inconsistency
and
introducing unnecessary requirements
3
. Even a little bit of inconsistency is dangerous because it breaks trust: instead of assuming your code works the sensible way, engineers must now go looking for surprises.
Unnecessary requirements are dangerous for two reasons. First, they’re
sticky
. When you’re implementing a new requirement, you have the context to decide whether it’s necessary or not. If you see one in the codebase, you must assume it’s necessary unless you’re willing to spend a bunch of time researching. So requirements tend to remain in codebases long after they could be removed. Second, they often interrelate in dangerous ways: if your codebase supports X, then you must consider how each new feature will interact with X. This combinatorial explosion is what makes working in large codebases so hard
4
.
When you’re writing code, you must
at all costs
try to:
Identify where your task could fit most normally into the current codebase
Trim your task down into
the smallest set of requirements
that you can
In fact, you should be so focused on this — on avoiding blunders — that you don’t really have mental energy to be worrying about cool tricks or “extra credit” features. As with
shipping projects
, if you find yourself thinking things like “oh, I could implement it with this clever pattern”, this is a warning sign: you are likely becoming distracted from the main thing, and you risk blundering.
You don’t have to be
clever
to do great programming work. In fact, sometimes cleverness can be a
disadvantage
. What you need is attention to detail and a laser focus on what actually matters: avoiding blunders by maintaining consistency and skipping unnecessary requirements.
