---
title: "LLVM Weekly - #73, May 25th 2015"
url: "https://blog.llvm.org/2015/05/llvm-weekly-73-may-25th-2015.html"
fetched_at: 2026-05-05T07:01:40.558512+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #73, May 25th 2015

Source: https://blog.llvm.org/2015/05/llvm-weekly-73-may-25th-2015.html

LLVM Weekly - #73, May 25th 2015
Welcome to the seventy-third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The LLVM blog has properly
announced
full support for OpenMP 3.1 in Clang.
The Clang-derived
Zapcc
has had
some attention
this week. It claims higher compilation speeds than the baseline Clang or other compilers. Yaron Keren, the principal developer has shared
many more details about its implementation
on the Clang mailing list.
On the mailing lists
LLVM commits
The
dereferenceable_or_null
attribute will now be exploited by the loop environment code motion pass.
r237593
.
Commits have started on the 'MIR serialization' project, which aims to print machine functions in a readable format.
r237954
.
A GCStrategy for CoreCLR has been committed alongside some documentation for it.
r237753
,
r237869
.
libFuzzer gained some more documentation.
r237836
.
libFuzzer can now be used with user-supplied mutators.
r238059
,
r238062
.
Clang commits
Other project commits
C++1z status for libcxx has been updated.
r237606
.
std::bool_constant
and
uninitialized_copy()
was added to libcxx.
r237636
,
r237699
.
libcxx gained a TODO list. Plenty of tasks that might be interesting to new contributors.
r237813
,
r237988
.
LDB has enabled debugging of multithreaded programs on Windows and gained support for attaching to process.
r237637
,
r237817
.
