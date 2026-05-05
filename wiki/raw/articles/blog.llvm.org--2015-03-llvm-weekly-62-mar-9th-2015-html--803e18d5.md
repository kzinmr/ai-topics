---
title: "LLVM Weekly - #62, Mar 9th 2015"
url: "https://blog.llvm.org/2015/03/llvm-weekly-62-mar-9th-2015.html"
fetched_at: 2026-05-05T07:01:40.817554+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #62, Mar 9th 2015

Source: https://blog.llvm.org/2015/03/llvm-weekly-62-mar-9th-2015.html

LLVM Weekly - #62, Mar 9th 2015
Welcome to the sixty-second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
LLVM is taking part in
Google Summer of Code
as a mentoring organisation. Students can earn a $5500 stipend by working on open source projects over the summer. See
here
for the list of mentoring organisations advertising LLVM-related projects. Please do help spread the word, applications open on Monday the 16th of March. I am biased, but I'd like to draw particular attention to the wide variety of
lowRISC GSoC ideas
, including a project to use tagged memory to provide protection against control-flow hijacking.
Ravi, a programming language based on Lua 5.3 has been
announced
. It features JIT compilation using LLVM, though in the current
development version
only a fraction of the Lua bytecodes are JIT-compiled.
On the mailing lists
LLVM commits
An initial implementation of a loop interchange pass has landed. This will interchange loops to provide a more cache-friendly memory access.
r231458
.
A high-level support library for the new pass manager has been added.
r231556
.
The LLVM performance tips document has seen some new additions.
r230995
,
r231352
.
DenseMapIterators will now fail fast when compiled in debug mode.
r231035
.
LowerBitSets will now use byte arrays rather than bit sets to represent in-memory bit sets, which can be looked up with only a few instructions.
r231043
.
Another large portion of the DebugInfo changes has landed.
r231082
.
A new optimisation for AddressSanitizer has been added that reduces the amount of instrumentation needed, eliminating it when accessing stack variables that can be proven to be inbounds.
r231241
.
llvm.frameallocate has been replaced with llvm.frameescape.
r231386
.
Clang commits
When the
-pedantic
flag is given, clang will warn when a format string uses
%p
with non-
void*
args.
r231211
.
Work on MS ABI support continues. Throwing a C++ exception under the MS ABI is now supported.
r231328
.
Other project commits
The lld resolver has had a significant performance optimisation. The commit message indicates linking chrome.dll now takes 30 seconds down from 70 seconds.
r231434
.
The static binary size of lldb-server has been reduced due to a reduction in the number of initialised components.
r230963
.
