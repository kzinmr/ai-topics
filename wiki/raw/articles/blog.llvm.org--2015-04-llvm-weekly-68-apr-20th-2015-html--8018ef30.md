---
title: "LLVM Weekly - #68, Apr 20th 2015"
url: "https://blog.llvm.org/2015/04/llvm-weekly-68-apr-20th-2015.html"
fetched_at: 2026-05-05T07:01:40.635940+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #68, Apr 20th 2015

Source: https://blog.llvm.org/2015/04/llvm-weekly-68-apr-20th-2015.html

LLVM Weekly - #68, Apr 20th 2015
Welcome to the sixty-eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Last week was of course
EuroLLVM
. It was good to put faces to names for a number of you, or to meet people I've only communicated with over twitter. Slides and videos should be forthcoming, but in the meantime you can read the
liveblog
I maintained for the talks I was able to attend. A big thank you to the organisers and all those who presented.
The highest profile news for some time in the LLVM community is that
Microsoft are working on an LLVM-based compiler for .NET CoreCLR
. What's more, LLILC (pronounced 'lilac') is open source, and they hope to contribute their LLVM changes upstream.
The
Cerberus team
are trying to find an answer to the question '
What is C in practice?
, and you can help by filling out their survey.
Honza Hubička has posted a fantastic overview of the
improvements to link-time and inter-procedural optimisations in GCC5
, featuring figures from Firefox builds. It seems like impressive improvements have been made.
Simon Cook has written a blog post about
using TableGen outside of LLVM
, specifically for things like parameterisable SSH configs. Crazy? Genius? Why not both?
On the mailing lists
LLVM commits
The
dereferenceable_or_null
attribute has been born. As described in the commit message, the motivation is for managed languages such as Java.
r235132
.
A new layer was added to the Orc JIT API for applying arbitrary transforms to IR.
r234805
.
Memory intrinsics can now be tail calls.
r234764
.
A handy Python script has been added for generating C programs that have a control flow graph which is a ladder graph. The intent is to use it to test whether an algorithm expected to be linear time on the CFG really is.
r234917
.
The code for lowering switches and extracting jump tables has been rewritten, and should produce better results now.
r235101
.
Call can now take an explicit type parameter.
r235145
.
Clang commits
Clang learned
-Wrange-loop-analysis
, which will warn when a range-based for loop makes copies of elements in the range.
r234804
.
The
preserve-bc-uselistorder
option is no longer true by default, but Clang will set it for
-emit-llvm
or
-save-temps
.
r234920
.
LLVM has had a lot of changes to the debug API in the last week. This commit updates Clang for them.
r235112
.
Other project commits
Reducing the amount of template use in LLD has reduced the size of AArch64TargetHandler.cpp.o to 4.1MB, down from 21MB.
r234808
,
r234931
.
A large patchset has landed in lldb which adds a big chunk of the work necessary for supporting lldb on ARM.
r234870
.
