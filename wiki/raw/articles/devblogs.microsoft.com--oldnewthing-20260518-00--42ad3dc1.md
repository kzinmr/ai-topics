---
title: "Just shows that nobody cares about debugging the parity flag any more"
url: "https://devblogs.microsoft.com/oldnewthing/20260518-00/?p=112334"
fetched_at: 2026-05-19T07:01:16.685242+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Just shows that nobody cares about debugging the parity flag any more

Source: https://devblogs.microsoft.com/oldnewthing/20260518-00/?p=112334

The x86-64 architecture inherited the parity flag (PF) from the x86-32, which in turn inherited it from the 8080, which inherited it from the 8008, which implemented it because it was the processor for the Datapoint 2200 serial terminal.
The parity flag also has a secondary purpose of being a place for the
FXAM
(x87) and
UCOMISD
(SSE) instructions to record the results of floating point comparisons. You can still entice compilers into checking the parity flag by checking a value for NaN or performing a floating point equality or inequality comparison (because NaN always fails equality and inequality comparison).
It turns out that the Windows debugging engine for x86-64 had a bug where it reported the parity flag as the opposite of what it actually is. When the parity flag was set, it said “po” instead of “pe”, and vice versa.
The fact that this went unreported for over two decades tells you that nobody cares about debugging the parity flag.
A fix has gone in. We’ll see if it makes it out before this article gets posted.
