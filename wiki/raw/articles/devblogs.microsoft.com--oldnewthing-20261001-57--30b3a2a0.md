---
title: "Windows on Itanium also provided for hot-patching, in an even simpler way"
url: "https://devblogs.microsoft.com/oldnewthing/20261001-57/?p=112747/"
fetched_at: 2026-10-02T10:01:05.989293+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Windows on Itanium also provided for hot-patching, in an even simpler way

Source: https://devblogs.microsoft.com/oldnewthing/20261001-57/?p=112747/

Last time, we looked at
Windows hot-patching on 64-bit ARM
. But what about Itanium?
Oh, you remembered Itanium!
Itanium also had fixed-sized instructions, or more accurately, fixed-sized bundles, where each bundle encodes three instructions. Fixed-size bundles mean that, like AArch64, there is no hot-patching restriction on the first instruction of a function.
In fact, there was no spare space for hot-patching at all.
Because none was needed.
During hot-patching, the first bundle of the instruction could be overwritten with
nop
        brl.cond.sptk target64
The second instruction
brl
is a “long branch” that accepts a 64-bit target.¹ This is a “double-wide” instruction that takes up two slots in the bundle, which is why we see a bundle of only two instructions.
Based on my experience with AArch64, I thought at first that the instruction sequence would be more like
movl r8 = target64   /* double-wide 64-bit load instruction */
    br.cond.sptk r8
But then I realized that this doesn’t work because you cannot perform an indirect jump through a general-purpose register. You have to move it to a branch register first. and that would take us to four instructions (since the
movl
occupies two slots), which exceeds the capacity of a bundle.
Bonus chatter
: If you study some old Itanium binaries like I did, you will find that many functions are preceded by an apparent spare bundle:
break.m 0
    break.i 0
    break.i 0
This is a bundle full of breakpoint instructions, and you might be tricked (like me) into thinking that they are there for hot-patching. But then you find that some other functions don’t have this spare bundle, and after closer study, you realize that this spare bundle is not for hot patching. It’s padding to bring the start of every function to a 32-byte boundary.
¹ Formally, it’s a conditional long branch instruction predicated on
p0
, and statically predicted to be taken. The
p0
register is hard-wired to
true
, so the assembler conveniently simplifies the disassembly and omits the
p0
.
