---
title: "LLVM Weekly - #117, Mar 28th 2016"
url: "https://blog.llvm.org/2016/03/llvm-weekly-117-mar-28th-2016.html"
fetched_at: 2026-05-05T07:01:39.160439+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #117, Mar 28th 2016

Source: https://blog.llvm.org/2016/03/llvm-weekly-117-mar-28th-2016.html

LLVM Weekly - #117, Mar 28th 2016
Welcome to the one hundred and seventeenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Google Summer of Code applications are now closed. Applicants and interested third-parties can look forward to finding out which projects were selected
on April 22nd
.
Ramkumar Ramachandra has written a blog post giving a
whirlwind tour of the internals of LLVM's fast register allocator
(FastRegAlloc.cpp).
Alex Denisov has blogged about
the various test suites used within the LLVM project
.
Version 1.13 of the TTA-based Co-design Environment (TCE) has
been released
. This adds support for LLVM 3.8.
On the mailing lists
LLVM commits
A new utility,
update_test_checks.py
was added to update opt or llc test cases with new FileCheck patterns.
r264357
.
Non-power-of-2 loop unroll count pragmas are now supported.
r264407
.
The NVPTX backend gained a new address space inference pass.
r263916
.
Instances of Error are now convertible to
std::error_code
. Conversions are also available between
Expected<T>
and
ErrorOr<T>
.
r264221
,
r264238
.
Hexagon gained supported for run-time stack overflow checking.
r264328
.
Clang commits
Other project commits
LLDB will fix inputted expressions with 'trivial' mistakes automatically.
r264379
.
ThreadSanitizer debugging support was added to LLDB.
r264162
.
Polly gained documentation to describe how it fits in to the LLVM pass pipeline.
r264446
.
LLDB has been updated to handle the UTF-16 APIs on Windows.
r264074
.
