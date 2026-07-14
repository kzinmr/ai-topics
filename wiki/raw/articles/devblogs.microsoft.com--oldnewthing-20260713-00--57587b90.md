---
title: "Why don't we just make the entire stack out of guard pages?"
url: "https://devblogs.microsoft.com/oldnewthing/20260713-00/?p=112528"
fetched_at: 2026-07-14T07:01:12.790786+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why don't we just make the entire stack out of guard pages?

Source: https://devblogs.microsoft.com/oldnewthing/20260713-00/?p=112528

In my earlier overview of
how compilers on different architectures perform stack probes
,
Cole Tobin asked
, “Why not have a page fault handler that detects the faulting address being the stack and page in the other pages?”
Csaba Varga replied
, “My guess: you don’t want an invalid pointer dereference to allocate a huge chunk of stack, just because the pointer happens to be pointing where the stack might grow, eventually. You want an invalid pointer dereference to segfault most of the time.”
I agree with Csaba on this.
If the entire stack were made of guard pages, then it means that a single page fault far below the stack limit could take arbitrary long and allocate arbitrarily large quantities of memory. The program might have said that it wants stacks to default to 1GB, and now a single page fault on the stack could result in a long pause as the system allocates 1GB of memory. If you study the problem in the debugger, what you see is that a single memory read takes several minutes.
And even worse is that there’s no way to stop it, since it’s happening in kernel mode. You see a program starting to balloon and consume all the memory in the system, so you go to Task Manager and terminate it, but the process doesn’t die. It just keeps on growing!
Even if the guard page is more than one page, it’s still a small fixed number of pages, the system can satisfy a guard page fault in a short amount of time. And more importantly, the amount of work is bounded.
