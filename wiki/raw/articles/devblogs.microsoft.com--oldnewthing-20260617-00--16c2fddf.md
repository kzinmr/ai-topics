---
title: "Windows stack limit checking retrospective, follow-up"
url: "https://devblogs.microsoft.com/oldnewthing/20260617-00/?p=112436"
fetched_at: 2026-06-18T07:01:30.363812+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Windows stack limit checking retrospective, follow-up

Source: https://devblogs.microsoft.com/oldnewthing/20260617-00/?p=112436

Aaron Giles
worked on porting Windows to both ARM32 and AArch64, and he
noted a missing detail
in my
retrospective of stack limit checking on arm64
:
Every once in a while Raymond Chen does an architectural comparison series and I get to see (a paraphrased version of) some code I wrote way back when. He’s right about why we passed stack size/16, but surprised he didn’t call out the unconventional x15 usage.
— Aaron Giles (
@aarongiles.com
)
Mar 20, 2026 at 8:08 PM
I’m guessing that by “unconventional x15 usage”, Aaron means “Why is the parameter passed in the
x15
register? The AArch64 calling convention passes the first parameter in the
x0
register, so shouldn’t that parameter be in the
x0
register?”
It seemed so obvious to me that I didn’t consider it worth mentioning.
The function that needs to do a stack probe is in a bit of a bind: It has inbound parameters, some of which might be passed in registers. If the stack size parameter were passed like a normal parameter to the stack probe function, then the calling function has to save its original inbound parameters somewhere. But it can’t save them on the stack because it has to do a stack probe before it can use the stack.
The solution is to give the stack probe function a custom calling convention that limits itself to scratch registers that are not used for receiving inbound parameters.
Architecture
Used for
parameters
Allocation
size
Also modified
8086
ax
bx
,
dx
x86-32
ecx
eax
MIPS
a0
…
a3
t8
PowerPC
r3
…
r10
r12
r0
,
r11
Alpha AXP
a0
…
a5
t12
t8
,
t9
,
t10
x86-64
rcx
,
rdx
,
r8
,
r9
rax
r10
,
r11
AArch64
x0
…
x7
x15
x16
,
x17
The calling conventions for processor architectures designate certain registers as “super-volatile”, typically those used reserved for assembler temporaries or for facilitating function calls between modules. These registers are excellent candidates for use by the stack probe function since there is no way they could be used for normal parameter passing.
For example, PowerPC uses
r11
, and AArch64 uses
r16
and
r17
, all of which are available for use in function glue stubs. Other opportunities were overlooked: MIPS and Alpha AXP could have used
at
, though I can see why they may have wanted to avoid using them because the assembler might use them implicitly when assembling pseudo-instructions.
