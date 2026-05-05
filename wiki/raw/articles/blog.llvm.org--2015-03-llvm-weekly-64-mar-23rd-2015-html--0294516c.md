---
title: "LLVM Weekly - #64, Mar 23rd 2015"
url: "https://blog.llvm.org/2015/03/llvm-weekly-64-mar-23rd-2015.html"
fetched_at: 2026-05-05T07:01:40.799219+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #64, Mar 23rd 2015

Source: https://blog.llvm.org/2015/03/llvm-weekly-64-mar-23rd-2015.html

LLVM Weekly - #64, Mar 23rd 2015
Welcome to the sixty-fourth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Students have until Friday 27th March to get their applications in for Google Summer of Code. This gives the opportunity to get paid $5500 to work on open source over the summer, under the mentorship of someone from the community. See
here
for the list of mentoring organisations advertising LLVM-related projects. Please do help spread the word. I am biased, but I'd like to draw particular attention to the wide variety of
lowRISC GSoC ideas
, including a project to implement an LLVM pass using tagged memory to provide protection against control-flow hijacking.
GCC 5 is starting to
get near to release
. The first release candidate is expected in the first week of April.
On the mailing lists
LLVM commits
The backend for the Hexagon DSP has continued to grow over the past few weeks. Most recently, support for vector instructions has been added.
r232728
.
The LLVM developer documentation grew guidance on writing commit messages.
r232334
.
LLVM learnt to support the ARMv6k target. The commit message has a handy ascii art diagram to explain its position in the ARM family.
r232468
.
Clang commits
The size of a Release+Asserts clang binary has been reduced by ~400k by devirtualising Attr and its subclasses.
r232726
.
Work on MS ABI continues, with support for HandlerMap entries for C++ catch.
r232538
.
A new warning,
-Wpartial-ability
will warn when using decls that are not available on all deployment targets.
r232750
.
C++14 sized deallocation has been disabled default due to compatibility issues.
r232788
.
Other project commits
Performance of a self-hosted lld link has again been improved. It's now down to 3 seconds on the patch author's machine (vs 5 seconds before, and 8 seconds for the GNU BFD linker).
r232460
.
libcxx gained the
<experimental/tuple>
header which implements most of the tuple functionality specified in the library fundamentals TS.
r232515
.
LLD now supports the semantics of simple sections mappings in linker scripts and can handle symbols defined in them.
r232402
,
r232409
.
Mips64 lldb gained an initial assembly profiler.
r232619
.
