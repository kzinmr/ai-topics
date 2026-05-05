---
title: "LLVM Weekly - #5, Feb 3rd 2014"
url: "https://blog.llvm.org/2014/02/llvm-weekly-5-feb-3rd-2014.html"
fetched_at: 2026-05-05T07:01:42.948012+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #5, Feb 3rd 2014

Source: https://blog.llvm.org/2014/02/llvm-weekly-5-feb-3rd-2014.html

LLVM Weekly - #5, Feb 3rd 2014
Welcome to the fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or
@llvmweekly
or
@asbradbury
on Twitter. I've been keeping the
@llvmweekly Twitter account
updated throughout the week, so follow that if you want more frequent news updates.
I'm afraid my summary of mailing list activities is much less thorough than usual, as I've been rather busy this weekend both moving house and suffering from a cold. Do ping me if you think I've missed anything important.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
This weekend there was an LLVM devroom at FOSDEM 2014. Slides have
already been posted
for some of the talks. Hopefully videos will follow.
Pocl (Portable Computing Language) 0.9 has been
released
. Pocl aims to be an efficient MIT-licensed implementation of the OpenCL 1.2 standard.
Mike Ash has published a useful
introduction to libclang
.
Ever wanted to use LLVM from within Rust? This
blog post will tell you how
.
Phoronix has published a
benchmark of Clang 3.4 vs GCC 4.9.0 20140126 on AMD Kaveri
.
On the mailing lists
LLVM commits
The ARM exception handling ABI (
EHABI
) is now enabled by default.
r200388
.
TargetLowering gained a hook which targets can implement to indicate whether a load of a constant should be converted to just the constant.
r200271
.
Line table debug info is now supported for COFF files when targeting win32.
r200340
.
LLVM now has the beginnings of a line editor library, initially to be used by clang-query but possibly consumed by LLDB as well in the future.
r200595
.
The R600 backend learned intrinsics for
S_SENDMSG
and
BUFFER_LOAD_DWORD*
instructions.
r200195
,
r200196
.
The loop vectorizer gained a number of flags to help experiment with changing thresholds. It now also only unrolls by powers of 2.
r200212
,
r200213
.
The loop vectorizer now supports conditional stores by scalarizing (they are put behind an if). This improves performance on the SPEC libquantum benchmark by 4.15%.
r200270
.
MCSubtargetInfo is now explicitly passed to the
EmitInstruction
,
EmitInstTo*
,
EncodeInstruction
and other functions in the MC module.
r200345
and others.
llvm-readobj learned to decode ARM attributes.
r200450
.
Speculative execution of llvm.{sqrt,fma,fmuladd} is now allowed.
r200501
.
Clang commits
Position Independent Code (PIC) is now turned on by default for Android targets.
r200290
.
The Parser::completeExpression function was introduced, which returns a list of completions for a given expression and completion position.
r200497
.
The default CPU for 32-bit and 64-bit MIPS targets is now mips32r2 and mips64r2 respectively.
r200222
.
The ARM and AArch64 backends saw some refactoring to share NEON intrinsics.
r200524
and others.
Other project commits
Compiler-rt gained a cache invalidation implementation for AArch64
r200317
.
Compiler-rt now features an optimised implementation of
__clzdi2
and
__clzsi2
for ARM.
r200394
.
Compiler-rt's CMake files will now compile the library for ARM. Give it a go and see what breaks.
r200546
.
The iohandler LLDB branch was merged in. The commit log describes the benefits.
r200263
.
