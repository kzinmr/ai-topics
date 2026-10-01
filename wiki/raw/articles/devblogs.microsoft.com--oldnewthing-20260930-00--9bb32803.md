---
title: "Windows on AArch64 also provides for hot-patching, but it's much simpler than on x86"
url: "https://devblogs.microsoft.com/oldnewthing/20260930-00/?p=112744/"
fetched_at: 2026-10-01T10:00:42.494358+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Windows on AArch64 also provides for hot-patching, but it's much simpler than on x86

Source: https://devblogs.microsoft.com/oldnewthing/20260930-00/?p=112744/

I have noted in the past that
x86-32
and
x86-64
versions of Windows are careful to start each function with a patch point. But what about AArch64 (known in Windows as arm64)?
Windows also inserts patch points for functions on AArch64, but they are much simpler due to the fixed-length instruction set. You don’t have to worry about patching an instruction when the instruction pointer happens to be in the middle of the byte sequence, because the instruction pointer is
never
in the middle of the byte sequence. The instruction pointer is always on a multiple of 4.
Therefore, there is no special restriction on the first instruction of a function. All instructions meet the requirements of being atomically updatable without risk of the instruction pointer being in the middle of the instruction.
Before each function is a patch space of 12 bytes, which is
exactly enough for a three-instruction trampoline
:
; overwrite the patch space with these three instructions
    adrp    xip0, PageStart(replacement)
    add     xip0, xip0, PageOffset(replacement)
    br      xip0

function_entry_point:
; overwrite the function entry point with one instruction
    br      $-12 ; jump to the patch space
The
xip0
register is
one of the two intra-procedure call scratch registers
, and the convention is that this register can be clobbered by any branch instruction. Since the caller had to use a branch instruction to reach
function_
entry_
point
in the first place, it cannot be using
xip0
for anything, so we are free to clobber
xip0
as part of our trampoline.
Bonus chatter
: The first instruction at the function entry point is almost certainly
pacibsp
, the
pointer authentication instruction for signing the return address
to make code more resistant to ROP attacks and attacks that overwrite the return address.
