---
title: "LLVM Weekly - #12, Mar 24th 2014"
url: "https://blog.llvm.org/2014/03/llvm-weekly-12-mar-24th-2014.html"
fetched_at: 2026-05-05T07:01:42.559958+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #12, Mar 24th 2014

Source: https://blog.llvm.org/2014/03/llvm-weekly-12-mar-24th-2014.html

LLVM Weekly - #12, Mar 24th 2014
Welcome to the twelfth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
On the mailing lists
LLVM commits
The MIPS64r2-based Octeon CPU has been added.
r204337
.
The ProfileData library,
discussed last week
was committed.
r204482
,
r204489
.
The constant hoisting pass saw some refactoring and improvements.
r204431
,
r204433
,
r204435
,
r204537
.
The ARM integrated assembler learned how to handle the
.thumb_set
directive.
r204059
.
Assembler directives were added to create version-min load commands for iOS or Mac OSX. e.g.
.ios_version_min 5,2,0
.
r204190
.
It is now possible to specify the 'noduplicate' attribution for intrinsics.
r204200
.
The TableGen backends documentation was fleshed out a bit.
r204479
.
Scheduling annotations have been added to NEON AArch64 instructions.
r204505
.
Clang commits
Counters used in instrumentation-based profiling are now represented in a static array. This is the first commit of a larger project to reduce runtime overhead (initialization in particular) for instrumentation-based profiling.
r204080
. Other commits for instrumentation-based profiling include
r204186
,
r204379
,
r204390
. There's a matching set of commits in compiler-rt.
The deprecated
-faddress-sanitizer
,
-fthread-sanitizer
, and
-fcatch-undefined-behavior
flags were removed. Users whould use
-fsanitize=
instead.
r204330
.
Support for parsing the OpenMP safelen clause (for 'omp simd') was committed.
r204428
.
Other project commits
Support was added to MemorySanitizer for 'advanced origin tracking', which records all locations where an uninitialized value is stored to memory rather than just the creation point.
r204152
.
The lldb backtrace view has been changed to a process view where you can expand the process, its threads, and see all frames under each thread.
r204251
.
In compiler-rt, Google have re-licensed the Android ucontext implementation under the standard dual license of compiler-rt.
r204128
.
