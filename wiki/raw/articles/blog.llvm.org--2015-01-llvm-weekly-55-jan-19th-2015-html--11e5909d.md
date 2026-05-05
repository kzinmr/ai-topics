---
title: "LLVM Weekly - #55, Jan 19th 2015"
url: "https://blog.llvm.org/2015/01/llvm-weekly-55-jan-19th-2015.html"
fetched_at: 2026-05-05T07:01:41.030777+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #55, Jan 19th 2015

Source: https://blog.llvm.org/2015/01/llvm-weekly-55-jan-19th-2015.html

LLVM Weekly - #55, Jan 19th 2015
Welcome to the fifty-fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
It seems to have been a very busy week in the world of LLVM, particularly with regards to discussion on the mailing list. Due to travel etc and the volume of traffic, I haven't been able to do much summarisation of mailing list discussion I'm afraid.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
LLM/Clang 3.6
has been branched
and subsequently, 3.6 RC1
has been tagged
.
LLVM/Clang 3.5.1 seems to have been
quietly released
.
Registration for
EuroLLVM 2015
, to be held at Goldsmiths College in London, UK on April 13-14th is
now open
.
All slides and videos from the last LLVM Developers' meeting are
now live
, including those from Apple employees.
On the mailing lists
LLVM commits
A new code diversity feature is now available. The NoopInsertion pass will add random no-ops to x86 binaries to try to make ROP attacks more difficult by increasing diversity.
r225908
. I highly recommend reading up on the
blind ROP
attack published last year. It would also be interesting to see an implementation of
G-Free
for producing binaries without simple gadgets. The commit was later reverted for some reason.
A nice summary of recent MIPS and PowerPC target developments, as well as the OCaml bindings is now there in the form of the 3.6 release notes.
r225607
,
r225695
,
r225779
.
LLVM learned the llvm.frameallocate and llvm.framerecover intrinsics, which allow multiple functions to share a single stack allocation from one function's call frame.
r225746
,
r225752
.
An experimental (disabled by default) 'inductive range check elimination' pass has landed. This attempts to eliminates range checks of the form
0 <= A*I + B < Length
.
r226201
.
StackMap/PatchPoint support is now available for the PowerPC target.
r225808
.
Initial support for Win64 SEH catch handlers has landed. See the commit message for current missing functionality.
r225904
.
A new utility script has been started to help update simple regression tests. It needs some work to generalise it beyond x86.
r225618
.
TargetLibraryInfo has been moved into the Analysis library.
r226078
.
Clang commits
The new
-fno-inline-asm
flag has been added to disallow all inline asm. If it exists in the input code it will be reported as an error.
r226340
.
-fsanitize-recover
command line flags are again supported.
r225719
.
The integrated assembler is now used by default on 32-bit PowerPC and SPARC.
r225958
.
Other project commits
The libcxx build system learnt how to cross-compile.
r226237
.
LLD gained a nice speedup by speculative instantiating archive file members. This shaves off a second or two for linking lld with lld.
r226336
.
LLD learnt the
--as-needed
flag (previously this was the default behaviour).
r226274
.
OpenMP gained an AARch64 port.
r225792
.
