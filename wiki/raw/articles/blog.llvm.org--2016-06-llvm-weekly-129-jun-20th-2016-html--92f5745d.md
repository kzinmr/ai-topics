---
title: "LLVM Weekly - #129, Jun 20th 2016"
url: "https://blog.llvm.org/2016/06/llvm-weekly-129-jun-20th-2016.html"
fetched_at: 2026-05-05T07:01:38.740020+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #129, Jun 20th 2016

Source: https://blog.llvm.org/2016/06/llvm-weekly-129-jun-20th-2016.html

LLVM Weekly - #129, Jun 20th 2016
Welcome to the one hundred and twenty-ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Last week was WWDC, which featured talks on
what's new in LLVM
(
slides
) and
what's new in Swift
(
slides
). Note that the embedded video player suggests you need Safari or the WWDC app to stream the video, but you can find a downloadable version under the "resources" tab.
On the mailing lists
LLVM commits
FileCheck learnt the
--check-prefixes
option as a shorthand for multiple
--check-prefix
options.
r272670
.
A
local_unnamed_addr
attribute was introduced. This can be used by the code generator and LTO to allow the linker to decide whether the global needs to be in the symbol table.
r272709
.
The ScalarReplAggregates pass has been removed as it has been superseded by SROA by a long time.
r272737
.
LLVM's C API gained support for string attributes.
r272811
.
Assembly parsing and lexing has seem some cleanups.
r273007
.
Clang commits
A new loop distribution pragma was added. Loop distribution is a transformation which attempts to break a loop in to multiple loops with each taking part of the loop body.
r272656
.
The nodebug attribute can now be applied to local variables.
r272859
.
The validity check for MIPS CPU/ABI pairings is now performed at initialisation time and a much clearer message is printed.
r272645
.
Other project commits
