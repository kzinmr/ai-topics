---
title: "LLVM Weekly - #20, May 19th 2014"
url: "https://blog.llvm.org/2014/05/llvm-weekly-20-may-19th-2014.html"
fetched_at: 2026-05-05T07:01:42.191066+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #20, May 19th 2014

Source: https://blog.llvm.org/2014/05/llvm-weekly-20-may-19th-2014.html

LLVM Weekly - #20, May 19th 2014
Welcome to the twentieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
This week's issue is perhaps a little less thorough than normal. I've been in San Francisco most of the week for Maker Faire this weekend, where I was at the Raspberry Pi booth with some other Foundation members. As this issue goes out, I'll be enjoying my last day in SF before heading to the airport for the long flight home and the ensuing jetlag.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The WebKit blog features an
excellent and detailed article about the new Fourth Tier LLVM JIT
which sheds light on the how and why.
The
Neu framework
has recently been announced. It is a C++11 framework, collection of programming languages and software system designed for artificial intelligence applications and technical computing in general. It makes use of the LLVM MC JIT for its NPL language as well as generating high performance neural networks.
On the mailing lists
LLVM commits
The inliner has been taught how to preserve musttail invariants.
r208910
.
A new C API has been added for a thread yielding callback.
r208945
.
Another patch in the series to improve MergeFunctions performance has been committed. A total ordering has now been implemented among operations.
r208973
,
r208976
.
The ARM load/store optimisation pass has been fixed to work with Thumb1.
r208992
.
GlobalValue has been split into GlobalValue and GlobalObject, which allows a code to statically accept a Function or a GlobalVariable but not an alias.
r208716
.
Integral reciprocal was optimised to not use division. This optimisation was influenced by
Souper
.
r208750
. Another optimisation opportunity uncovered by Souper was signed icmp of -(zext V).
r208809
.
I rather like that these transforms for single bit tests were
verified with Z3
.
r208848
.
PowerPC gained global named register support, for r1, r2 and r13 (depending on the subtarget).
r208509
.
Documentation was added for the ARM64 BigEndian NEON implementation.
r208577
.
The constant folder is now better at looking through bitcast constant expressions. This is a first step towards fixing this
poor performance of these range comprehensions
.
r208856
.
Clang commits
Initial support for MS ABI compliant RTTI mangling has been committed.
r208661
,
r208668
.
Clang will no longer copy objects with trivial, deleted copy constructors. This fixes bugs and improves ABI compatibility with GCC and MSVC.
r208786
. Though the itanium C++ ABI part was reverted for now.
r208836
.
Other project commits
The LLDB Machine Interface has been committed. This is an implementation of the
GDB Machine Interface
, useful for implementing your own frontend to LLDB.
r208972
.
AddressSanitizer started to gain some windows tests.
r208554
,
r208859
,
r208873
and more.
The instrumented profiling library API was fixed to work with shared objects, and profiling is now supported for dlopened shared libraries..
r208940
,
r209053
.
