---
title: "Why do we need ud2 when int 6 is right there?"
url: "https://devblogs.microsoft.com/oldnewthing/20261019-00/?p=112781/"
fetched_at: 2026-10-20T10:01:30.453931+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why do we need ud2 when int 6 is right there?

Source: https://devblogs.microsoft.com/oldnewthing/20261019-00/?p=112781/

Some time ago, I mentioned that
the
ud2
instruction was created to be an architecturally undefined instruction
. But why not just use an
int 6
instruction? It’s a two-byte instruction, just like
ud2
, and interrupt vector 6 is the invalid opcode vector, so a program could just invoke it manually and get whatever behavior the operating system assigns to an attempt to execute an invalid opcode.
Well, not exactly.
Architecturally, the invalid opcode is a
fault
, which means that the address of the faulting instruction is reported to the exception handler. On the other hand, the
int 6
is a
trap
, which means that the address of the instruction
after
the
int 6
is reported to the handler.
This distinction between faults and traps reflects how they are used. A fault represents an error that the kernel could attempt to repair and retry. For example, a page fault could be repaired by paging the memory in. An access violation could be repaired by changing the page protections. A trap reports an operation that has already occurred and gives you a chance to do some special work in response to it before resuming execution. In the case of a software interrupt, the handler wants to process whatever the interrupt means, and then resume execution with the next instruction.
Now, some faults are unlikely to be repaired, but reporting them as faults means that you have to take extra steps if you want to execute past them. If you just ignore the fault, the instruction restarts and faults again.
If you manually raise the
int 6
interrupt to simulate a
#UD
undefined instruction fault, the handler will think it’s dealing with a CPU-generated undefined instruction fault, so it expects the instruction pointer in the fault frame to point to the undefined instruction. But since
int
puts the address of the
next
instruction into the fault frame, the fault handler will look at the instruction and get confused as to why the invalid instruction fault was raised. “It says here that the faulting instruction is a
xor eax, eax
. That’s a perfectly legitimate instruction. Why did it fault?”
One case for inspecting the faulting instruction is to emulate missing instructions on older processors.
Furthermore, in protected mode, you need to have permission to issue an
int 6
. The interrupt descriptor table describes what to do for each interrupt, as well as what CPU privilege level is permitted to invoke it explicitly. And to avoid exactly these types of problems where a user-mode program issues an
int 6
and confuses the
#UD
handler, all operating systems deny
int 6
privileges to user mode.
So even if you try to fake a
#UD
via an explicit
int 6
, it doesn’t work. To get the
#UD
undefined instruction fault, you have to issue an actual undefined instruction.
