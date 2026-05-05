---
title: "LLVM Weekly - #112, Feb 22nd 2016"
url: "https://blog.llvm.org/2016/02/llvm-weekly-112-feb-22nd-2016.html"
fetched_at: 2026-05-05T07:01:39.317526+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #112, Feb 22nd 2016

Source: https://blog.llvm.org/2016/02/llvm-weekly-112-feb-22nd-2016.html

LLVM Weekly - #112, Feb 22nd 2016
Welcome to the one hundred and twelfth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Filip Pizlo has written a
fantastic article
introducing the new B3 JIT compiler for WebKit's JavaScriptCore. This intends to replace LLVM as the optimising backend to their fourth-tier JIT. The article describes in detail their reasons for moving away from LLVM (mainly compile-time) and the design trade-offs made, such as in reducing memory allocations and minimising pointer-chasing in the IR. This reminds me of the trade-offs Mike Pall made in the
LuaJIT 2.0 IR
. Philip Reames also shared
some initial thoughts on B3
. I know some people have expressed disappointment about WebKit moving away from LLVM, but if you'll allow me to insert just a little bit of editorial I'd argue B3 is a very positive development for LLVM and the wider compiler community. B3 explores a different set of design trade-offs to those chosen for LLVM, and these sort of changes are probably easiest to explore in a fresh codebase.Thanks to this write-up (and hopefully future B3/AIR documentation), we can learn from the B3 developers' experiences and consider if some of their choices will make sense for LLVM. It's also good to remember that LLVM isn't the only feasible route for code generation and optimisation, and we shouldn't treat LLVM's design choices as the one-true way to do things. Impressively, B3 was developed to its current state in only
6 months of developer-time
.
Version 0.17.0 of LDC, the LLVM-based compiler for the D programming language has
been released
. You can view a
detailed changelog here
.
GCC6 will feature a whole bunch of new warnings, and
this blog post
details many of them.
The schedule for
EuroLLVM 2016
has now been posted. This will be held March 17th-18th in Barcelona.
On the mailing lists
LLVM commits
The PPCLoopDataPrefetch pass has been moved to Transforms/Scalar/LoopDataPrefetch in preparation for it becoming a target-agnostic pass.
r261265
.
The cmpxchg LLVM instruction now allows pointer type operands.
r261281
.
The X86 backend gained support for a new stack symbol ordering optimisation. This is primarily intended to reduce code size, and produces small but measurable improvements across some SPEC CPU 2000 benchmarks.
r260917
.
The LLVM C API has been extended to allow it to be used to manipulate the datalayout.
r260936
.
Some major work on the LazyCallGraph has been checked in.
r261040
.
The AMDGPU backend gained a basic disassembler.
r261185
.
The PostOrderFuctionAttrs pass has been ported to the new pass manager. As described in the commit message, this actually represents a major milestone.
r261203
.
The Hexagon backend gained support for thread-local storage.
r261218
.
Clang commits
A nullPointerConstant AST matcher was added.
r261008
.
Clang gained a
-Wcomma
warning, which will warn for most uses of the builtin comma operator.
r261278
Other project commits
