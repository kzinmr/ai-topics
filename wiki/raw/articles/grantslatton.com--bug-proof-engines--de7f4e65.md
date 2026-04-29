---
title: "Designing bug-proof engines"
url: "https://grantslatton.com/bug-proof-engines"
fetched_at: 2026-04-29T07:02:16.704755+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Designing bug-proof engines

Source: https://grantslatton.com/bug-proof-engines

Designing bug-proof engines
Suppose you have to make an engine that's going to operate in an environment with a lot of bugs. There are two strategies you can take:
Design the engine such that it's impossible for bugs to get inside
Design the engine to tolerate bugs getting inside
Which you choose is often downstream of requirements, but you should be aware of both options. Too often, the engineer gets stuck on one option when it would actually be easier to
take the other path
.
What are some other instances of this problem?
Design a rocket engine that never fails
Design a rocket that can tolerate engine failure
The
Saturn V
is an example of #1, whereas the
Falcon 9
is an example of #2.
In programming:
Manual memory management
Garbage collection
C
is an example of #1, whereas
Java
is an example of #2.
In distributed systems:
Storage system with
error correcting memory
Storage system with a corruption detector & fixer
In writing:
Spend a lot of time planning, storyboarding, etc so the first iteration is good
Write a sloppy first draft and edit later
The list goes on, but the pattern is the same.
I first had this thought when working at AWS on distributed systems. Before the "bug-proof engine" analogy, I visualized it like you're designing a device to transfer marbles across a room.
You can design a device that never drops any marbles. Or you can design a device that sometimes drops marbles, and pay a janitor to sweep them up every night. So I'd call this "perfectionism vs sweeper" engineering.
It's often the case that just paying the janitor is 10x cheaper than building the system that never drops marbles, but I'd often see engineers receive the project "move marbles" and just assume that dropping marbles was unacceptable in all circumstances. Always question these requirements!
You'll encounter the flip-side if you inherit a sweeper system. A lot of engineering work goes in to improving the sweeper! But you should always stop and ask: can we just make the marbles stop falling and delete the sweeper?
There is no right answer — you must keep both ends of this solution spectrum in mind.
One final thought: a lot of systems are
bimodal
. They have a perfectionist happy path, and then fall back to a sweeper sad path. This happens when the happy path is a lot cheaper than the sad path, so you keep around the happy path as an optimization.
In this circumstance, I highly recommend thinking if it's possible to simply make the sweeper cheap
enough
to delete the happy path and just do the sad path all the time. Even if this is marginally more expensive, it's often worth it to reduce complexity and delete modes.
Have fun designing bug-proof engines!
