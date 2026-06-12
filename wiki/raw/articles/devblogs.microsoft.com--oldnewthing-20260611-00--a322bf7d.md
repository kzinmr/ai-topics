---
title: "Understanding the rationale behind a rule when trying to circumvent it"
url: "https://devblogs.microsoft.com/oldnewthing/20260611-00/?p=112415"
fetched_at: 2026-06-12T07:00:52.344045+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Understanding the rationale behind a rule when trying to circumvent it

Source: https://devblogs.microsoft.com/oldnewthing/20260611-00/?p=112415

In the documentation for
best practices for implementing process and thread-related callback functions
, it calls out
Keep routines short and simple.
Don’t make calls into a user mode service to validate the process, thread, or image.
Don’t make registry calls.
Don’t make blocking and/or Interprocess Communication (IPC) function calls.
Don’t synchronize with other threads because it can lead to reentrancy deadlocks.
So far so good. It seems that these callback functions need to operate quickly and cannot block. These are callbacks that are invoked when a process starts or exits, when a thread starts or exits, when a DLL or EXE is loaded or unloaded, and various other low-level events.
The various prohibitions above suggest that these callouts are called during the process creation/termination sequence, so if you take a long time to deal with them, you are slowing down the entire system. And the rather extreme requirements, like “Don’t make registry calls,” suggest that they might even be called while the system holds internal locks.
The list of best practices continues:
Use System Worker Threads to queue work especially work involving:
Slow APIs or APIs that call into other process.
Any blocking behavior that could interrupt threads in core services.
Okay, so this is providing a suggestion on how you can offload expensive work to code running outside the callback. This once again highlights that the callback itself needs to be fast with minimal blocking.
My colleagues in enterprise support often run into cases where the reason for a system hang is a driver violating the rule that these callbacks must return quickly. For example, a common anti-pattern is a driver whose callback starts by following the guidance above to queue work to a System Worker Thread, but then they block until the work item completes.
This is a case of following the rules without understanding why the rules are there.
The rule is that the callback needs to be fast and return quickly. The driver followed the letter of the law by delegating the work to a System Worker Thread, and there’s no rule that says “Don’t wait for work items”, so they must have figured that this gave them a loophole for executing synchronous long-running work.
But the rules “Don’t make blocking and/or Interprocess Communication (IPC) function calls” and “Don’t synchronize with other threads because it can lead to reentrancy deadlocks” make it clear that you shouldn’t be blocking in your callback for extended periods of time. The “Don’t”s are just calling out some common ways that your callback can block.
And it looks like the documentation was updated in 2020 to call out this specific case:
If you use System Worker Threads, don’t wait on the work to complete. Doing so defeats the purpose of queuing the work to be completed asynchronously.
One could argue that this rule is already covered by the “Don’t synchronize with other threads” rule, but I guess the driver vendor interpreted it as “But I’m not synchronizing with another thread. I’m synchronizing on an event!” But of course, the event is set by another thread, so you are effectively synchronizing with another thread.
My colleague in enterprise support describes this as the “It wasn’t me, it was my brother” excuse. You are told by your parents not to turn on the television set, so you tell your brother to do it. Technically, you didn’t turn the television set on, but in effect, you did because your brother is acting under your instructions. (This is why contracts often contain wording like “may not disclose or cause to be disclosed,” so that you can’t say “No, I totally didn’t disclose it. I gave the information to Bob, and it was Bob who disclosed it!”)
The documentation should open with something like this:
The callback function must perform its work quickly without blocking. If you need to do complex work or synchronize with other threads or processes, do the work asynchronously, such as by using System Worker Threads.
And then it can give a list of examples of things that count as blocking.
Some examples of blocking that is not allowed from the callback function:
And then it can follow up with additional constraints.
Furthermore, the callback function may not perform any of the following operations:
