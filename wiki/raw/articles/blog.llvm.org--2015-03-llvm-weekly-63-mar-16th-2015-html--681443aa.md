---
title: "LLVM Weekly - #63, Mar 16th 2015"
url: "https://blog.llvm.org/2015/03/llvm-weekly-63-mar-16th-2015.html"
fetched_at: 2026-05-05T07:01:40.795568+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #63, Mar 16th 2015

Source: https://blog.llvm.org/2015/03/llvm-weekly-63-mar-16th-2015.html

LLVM Weekly - #63, Mar 16th 2015
Welcome to the sixty-third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
as a mentoring organisation. Students can earn a $5500 stipend by working on open source projects over the summer, and applications upon today (March 16th). See
here
for the list of mentoring organisations advertising LLVM-related projects. Please do help spread the word. I am biased, but I'd like to draw particular attention to the wide variety of
lowRISC GSoC ideas
, including a project to implement an LLVM pass using tagged memory to provide protection against control-flow hijacking.
Version 0.11 of Pocl, the portable open-source OpenCL implementation
has been released
. Additions in this release include initial Android support and MIPS architecture support.
Version 1.11 of TCE, the TTA-based (Transport Triggered Architecture) Co-design Environment, which uses LLVM
has been released
. This release adds support for LLVM 3.6.
There will be a
LLVM microconference
at the Linux Plumbers Conference in August. There is a
call for speakers
.
On the mailing lists
LLVM commits
As DataLayout is now mandatory, LLVM APIs have been updated to use references to DataLayout.
r231740
.
Support was added for part-word atomics on PowerPC.
r231843
.
Initial work on enhancing ValueTracking to infer known bits of a value from known-true conditional expressions has landed.
r231879
.
The PowerPC READMEs have been updated to list potential future enhancements.
r231946
.
The
llvm.eh.actions
intrinsic has been added.
r232003
.
The documentation for llvm-cov has been updated.
r232007
.
The getting started docs now describe CMake as the preferred way to build LLVM.
r232135
.
llvm-vtabledump is now known as llvm-cxxdump.
r232301
.
Clang commits
The steady stream of OpenMP patches continues, with the addition of codegen support for the omp task directive and omp for.
r231762
,
r232036
.
Copy-constructor closures for MS ABI support has been added.
r231952
.
Other project commits
LLD gained support for linker script expression evaluation and parsing of the MEMORY and EXTERN commands.
r231707
,
r231928
,
r232110
.
LLDB gained a
CODE_OWNERS.txt
file.
r231936
.
