---
title: "LLVM Weekly - #82, Jul 27th 2015"
url: "https://blog.llvm.org/2015/07/llvm-weekly-82-jul-27th-2015.html"
fetched_at: 2026-05-05T07:01:40.298428+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #82, Jul 27th 2015

Source: https://blog.llvm.org/2015/07/llvm-weekly-82-jul-27th-2015.html

LLVM Weekly - #82, Jul 27th 2015
Welcome to the eighty-second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'd just like to highlight how much I really do appreciate people sending me links for inclusion, e.g. LLVM-related blog posts or new releases of software using LLVM (feature releases rather than simple bugfix updates). I'm not omniescent - if an interesting blog post or software release goes unmentioned here, I probably just didn't know about it!
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The
call for papers
for the 2015 LLVM Developers' meeting has now gone out. The submission deadline is August 20th. Registration is also
now open
.
John Regehr and his collaborators working on Souper have
shared some initial results from the synthesizing superoptimizer
. John is very interested in collecting representative IR from frontends other than Clang. There is also some discussion about these results
on the mailing list
.
Microsoft have
open sourced their GDB/LLDB 'debug engine'
.
On the mailing lists
LLVM commits
dsymutil gained support for one-definition-rule uniquing for C++ code. When linking the DWARF for a debug build of clang, it generates a 150M dwarf file instead of 700M.
r242847
.
The last remnant of the AliasAnalysis legacy update API have been removed.
r242881
.
LoopUnswitch can now unswitch multiple trivial conditions in a single pass invocation.
r243203
.
Clang commits
Other project commits
A new ELF linker has been born, based on the PE/COFF linker.
r243161
.
libcxx gained a default searcher for
std::experimental::search
.
r242682
.
