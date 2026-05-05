---
title: "LLVM Weekly - #93, Oct 12th 2015"
url: "https://blog.llvm.org/2015/10/llvm-weekly-93-oct-12th-2015.html"
fetched_at: 2026-05-05T07:01:39.970102+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #93, Oct 12th 2015

Source: https://blog.llvm.org/2015/10/llvm-weekly-93-oct-12th-2015.html

LLVM Weekly - #93, Oct 12th 2015
Welcome to the ninety-third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or
@llvmweekly
or
@asbradbury
on Twitter.
Apologies that this week's issue comes rather late in the day, my laptop gave up the ghost over the weekend while I was travelling leaving me with no way to write it. Now I'm back, I've managed to dust off an old desktop from my closet to write this issue (and to keep my unbroken streak). LLVM Weekly has been sent out every Monday since it started on the first Monday of January 2014. This weekend I was talking about
lowRISC
at
ORConf 2015
. You can find my slides
here
. There was a wide array of talks on open source hardware, including many on lowRISC and RISC-V. The videos should hopefully be posted in the next week or so.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The LLVM project has hit 250,000 commits. The commit that managed to hit this milestone was
this one-liner
.
A
new paper
by Bjarne Stroustrup, Herb Sutter, and Gabriel Dos Reis gives more details on their plans for memory safety in C++.
Videos from CppCon2015 are
being posted to Youtube
.
On the mailing lists
LLVM commits
The Hexagon architecture gained an early if-conversion pass.
r249423
.
ThinLTO has started to land, in particular support for function summary index bitcode sections and files.
r249270
.
Codegen for ARM's memcpy intrinsic has been modified to make better use of LDM/STM.
r249322
.
The llvm.eh.exceptioncode intrinsic was added.
r249492
.
It is now possible to turn off MMX support without disabling SSE.
r249731
.
Clang commits
The policy for adding new style options to clang-format has been documented.
r249289
.
The libclang bindings have been extended with accessors for C++ function attributes (pure virtual, virtual, or const).
r250008
.
Other project commits
GoLanguageRuntime was introduced to LLDB, which supports finding the runtime type for Go interfaces.
r249456
,
r249459
.
The new LLD ELF linker now supports the
--as-needed
option.
r249998
.
LLDB for MIPS is now able to emulate microMIPS instructions.
r249381
.
liblldb is working towards being able to work under both Python 2.x and 3.x.
r249886
.
