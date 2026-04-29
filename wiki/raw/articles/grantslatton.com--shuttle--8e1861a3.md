---
title: "Shuttle"
url: "https://grantslatton.com/shuttle"
fetched_at: 2026-04-29T07:02:17.029958+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Shuttle

Source: https://grantslatton.com/shuttle

Shuttle
One of the coolest technologies I have had the pleasure of using recently is the
shuttle
library. It's a concurrency verification tool developed by some of my former coworkers at AWS.
Motivation
Writing correct concurrent code involving locks, message passing, and atomics can be difficult.
A big contributor to the difficulty is that testing and debugging concurrent code is non-trivial. It's common to just write single-threaded unit tests that exercise simple serial behavior.
A more robust technique that I've employed a lot in the past is making a multi-threaded unit test and executing it in a loop hundreds or thousands of times. The idea is that any weird concurrency bugs will be probabilistically exercised.
While you can get a fair amount of mileage out of this technique, it's definitely not foolproof.
A certain subset of possible execution permutations may be much more likely than others due to system-specific details.
Some concurrency bugs that happen to be rare on your particular system sneak through your testing process. Then — inevitably — they show up in hard-to-reproduce production bugs after weeks or months of lurking undetected.
Reproducibility is another issue. Even if you do manage to hit some assertion error after running a concurrent test a hundred thousand times, it's hard to exercise the same path consistently enough to effectively debug.
Solution
The problem can be solved with controlled thread scheduling.
The
shuttle
library vends drop-in replacements of all the standard library's concurrency primitives.
The user runs their concurrent test inside a
shuttle
harness that controls the scheduling behavior of those concurrency primitives.
The harness explores different execution permutations by running the test repeatedly and manipulating the scheduling behavior.
This is basically the same technique used by the
loom
library. The main difference between the two is that
loom
does exhaustive exploration and
shuttle
does random exploration.
You might think that exhaustive exploration is strictly superior, but that's not always the case.
The number of possible execution permutations grows factorially with the number of threads and synchronization points. That means that exhaustive exploration is only feasible for very simple cases.
Random exploration enables exploring arbitrarily complicated execution permutations and is trivially parallelizable. You could spin up thousands of EC2 instances testing some business-critical concurrent code if you wanted.
In practice, nearly all of the bugs that
shuttle
catches for me happen within a few hundred iterations — far from the effectively-infinite number of possible execution permutations any complicated code has.
Worked example
Let's say we wanted to write a
Semaphore
object. Our first attempt might look like this:
Then, being good engineers, we write a
shuttle
test:
Upon running it, we get an assertion failure!
We see that
shuttle
has found some execution that results in all 5 threads acquiring permits. It even gives me a way to re-run the exact execution schedule.
So we re-run the same execution after inserting some tactical
dbg!
statements, and we find the problem.
It's possible for multiple threads to all simultaneously confirm that the remaining permit count is positive and proceed into the body of the
if
-statement.
This is a classic newbie concurrency error.
It's a
little
harder to mess this up in Rust — the clunky
AtomicU64
methods make it obvious that something interesting is going on with regard to concurrency. Nonetheless, this class of error has doubtlessly bitten anyone getting started with multi-threaded programming.
So let's try to fix it with a little optimistic concurrency:
Re-running
shuttle
, we get a new error:
Repeating the debugging process, the new problem becomes clear.
When the remaining permit count is at 0, optimistically subtracting 1 causes it to underflow back to
u64::MAX
. If a second thread checks that the permit count is positive
before
the original thread rolls back the optimistic subtraction, the second thread will succeed (thinking that there are an
absurdly
high number of permits available).
We try again, with a
compare-and-swap
technique reminiscent of a
spinlock
.
Finally,
shuttle
gives us a passing grade.
Integration
Dealing with replacing all of your
std::sync
primitives with
shuttle::sync
primitives is a minor complication. The easy way to do this is with conditional compilation and re-exports. Here's the basic idea:
You should also put your
shuttle
tests behind the same feature flag so they won't be run with non-
shuttle
concurrency primitives.
Conclusion
Testing and debugging concurrent code with
shuttle
is almost trivially easy. I can't imagine going back to writing serious concurrent code without it.
S3 uses
shuttle
to verify the correctness of extremely complicated concurrent software storing exabytes of data.
My coworkers wrote
a paper
about our experience using
shuttle
and wound up winning
Best Paper
at SOSP '21.
