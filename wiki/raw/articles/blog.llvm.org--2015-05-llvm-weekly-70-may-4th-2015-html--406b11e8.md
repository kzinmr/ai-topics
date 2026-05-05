---
title: "LLVM Weekly - #70, May 4th 2015"
url: "https://blog.llvm.org/2015/05/llvm-weekly-70-may-4th-2015.html"
fetched_at: 2026-05-05T07:01:40.595014+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #70, May 4th 2015

Source: https://blog.llvm.org/2015/05/llvm-weekly-70-may-4th-2015.html

LLVM Weekly - #70, May 4th 2015
Welcome to the seventieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Microsoft have announced their intention to make use of the
Clang frontend on Windows
.
Bjarne Stroustrup has recently been
talking about potential C++17 features
.
The Visual C++ developers are going to be open-sourcing their
GDB/LLDB debug engine
.
The projects accepted into Google Summer of Code for LLVM
have been announced
. Four student projects have been accepted.
The next Bay Area LLVM social is
scheduled for
7pm on Thursday the 7th of May. Please sign up if you are attending.
On the mailing lists
Rui Ueyama has been doing quite a lot of work on LLD of late and has proposed an
LLD improvement plan
. In it, he proposes some major changes that would hopefully ease the path to LLD becoming a fully functional ELF, Mach-O, and PE-COFF linker. The two main proposals are to use the 'section' rather than the 'atom' model and to stop trying to bend the Unix model to work on other platforms, instead directly implementing the necessary native behaviour. There are understandably some concerns that this direction could result in LLD having to maintain essentially three linkers, but discussion is ongoing and much feedback seems positive.
Alex, who will be interning at Apple this summer has posted an
RFC on a proposed machine level IR text serialisation format
. It came out a little mangled on Gmane so you may prefer to read the
pipermail rendering
. A lot of the feedback revolves around the pros and cons of a YAML-based format..
Andrey Bokhanko suggests
replacing libgomp with libiomp
as the default OpenMP runtime library when using
-fopenmp
. Ultimately there seems to be agreement and the only issue seems to be on the library naming.
Nico Weber reports that although
-gline-tables-only
makes debug info much smaller, they've
found with Chromium the resulting stackframes aren't that usable without function parameters and namespaces
. The proposal is to add a new variant that does include function parameter info and namespace info.
LLVM commits
The LLVM performance tips document has gained another two entries.
r235825
,
r235826
.
llvm-symbolizer now works on Windows.
r235900
.
SelectionDAG, DAGCombiner and codegen support for masked scatter and gather has been added.
r235970
,
r236211
,
r236394
.
Debug locations have been added to all constant SelectionDAG nodes.
r235989
.
Dragonegg support has been dropped from the release script.
r236077
.
The debug info IR constructs have been renamed from
MD*
to
DI*
. Duncan suggests that if you're updating an out of tree target, it may be easiest to first get things compiling with the code from before this commit, then continue the merge.
r236120
.
Clang commits
Clang can now generate dependencies in the style accepted by the NMake and Jom build tools.
r235903
.
New AVX-512 intrinsics have been added.
r235986
,
r236218
.
Clang learned
-Wpessimizing-move
and
-Wredundant-move
warnings.
r236075
.
Other project commits
LLDB gained support for the SysV ABI on ARM and AArch64.
r236097
,
r236098
.
The LLVM test suite gained a
frame_layout
test.
r236085
.
