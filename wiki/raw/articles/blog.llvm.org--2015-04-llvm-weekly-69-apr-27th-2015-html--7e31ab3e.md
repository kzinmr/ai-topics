---
title: "LLVM Weekly - #69, Apr 27th 2015"
url: "https://blog.llvm.org/2015/04/llvm-weekly-69-apr-27th-2015.html"
fetched_at: 2026-05-05T07:01:40.610943+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #69, Apr 27th 2015

Source: https://blog.llvm.org/2015/04/llvm-weekly-69-apr-27th-2015.html

LLVM Weekly - #69, Apr 27th 2015
Welcome to the sixty-ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Ed Jones at Embecosm has written about his work to
use the GCC regression suite on Clang
and documented how to run the LLVM test suites on an embedded target.
GCC 5.1 has now
been released
. Congratulations to the GCC team. The versioning scheme is potentially confusing - 5.0 is the development version which saw a stable release as 5.1. The next minor releases will be 5.2, 5.3 etc and the next major release will be 6.1 (referred to as 6.0 during development).
On the mailing lists
Sanjoy Das has posted an RFC on
supporting implicit null checks
in LLVM. This is intended to support managed languages like Java, C#, or Go where a null check is required before using pointers.
Alex L interned at Apple last year, and is interning again this summer. He's
posted to the list
about his project, which is to develop a text-based human readable format that allows LLVM to serialize the machine-level IR. The intention is to make debug and testing easier. He welcomes any feedback or suggestions.
libunwind is
moving
to its own repository. Hopefully a git mirror will go live soon.
Roel Jordans gave a talk at EuroLLVM this year about his software pipelining pass. He has
posted to the mailing list
to give a few more details and share his source code.
Tom Stellard is looking to
increase the number of code owners
, i.e. the set of people who review patches or approve merge requests to stable branches on a certain part of the code. His plan is to start nominating new code owners based on git history whenever he gets a new stable merge request for an unowned component.
LLVM commits
Functions can now have metadata attachments.
r235785
.
The stack object allocation for Hexagon has been completely overhauled.
r235521
.
The vim support files have been updated. Changes include a new indentation plugin for .ll files.
r235369
.
llvm-link learned the
-override
option to override linkage rules.
r235473
.
There is now textual IR support for an explicit type parameter to the invoke instruction (much like for the call instruction).
r235755
.
Clang commits
Documentation has been added for SanitizerCoverage (simple code coverage using the Sanitizer tools).
r235643
.
Clang's
__attribute__((aligned))
can now set alignment to a target-specific value, rather than just assuming 16 bytes on all platforms.
r235397
.
Other project commits
lld now understands
--discard-locals
.
r235357
.
lldb's 'operation' and 'monitor' threads on Linux have been merged in to one.
r235304
.
It's now possible to build compiler-rt for MIPS with gcc.
r235299
.
libunwind seems to have been moved into its own project.
r235759
.
