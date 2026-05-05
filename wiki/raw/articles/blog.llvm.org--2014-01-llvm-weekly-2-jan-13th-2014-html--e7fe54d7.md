---
title: "LLVM Weekly - #2, Jan 13th 2014"
url: "https://blog.llvm.org/2014/01/llvm-weekly-2-jan-13th-2014.html"
fetched_at: 2026-05-05T07:01:42.770114+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #2, Jan 13th 2014

Source: https://blog.llvm.org/2014/01/llvm-weekly-2-jan-13th-2014.html

LLVM Weekly - #2, Jan 13th 2014
Welcome to the second issue of LLVM Weekly (and the first to appear on the LLVM blog). LLVM Weekly is a newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. Thank you to everyone who has given positive feedback or suggestions, I'm planning in future editions to integrate some sort of statistics of git activity and contributions as well as activity on Bugzilla. LLVM Weekly is brought to you by
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
Stephen Diehl has published a
Haskell adaptation of the 'Kaleidoscope' tutorials
on how to implement aJIT compiled language using LLVM. This was received very positively and prompted some
discussion on HN
.
Registration for EuroLLVM is
now open
. There's still time to submit your talk, poster or workshop proposals too.
Rust 0.9 has been released
. Rust is a systems programming language which targetting LLVM with a particular emphasis on type safety, memory safety and concurrency. One of the core Rust developers at Mozilla, Niko Matsakis, also gave a
talk at linux.conf.au introducing Rust
.
Coverity 7
now includes Clang compiler support
.
On the mailing lists
Apple are
advertising for interns
with their LLVM compiler frontend and runtime teams this summer. Note internships are restricted to students.
Amara Emerson shares a
proposal on handling the removal of the -mfpu option for AArch64
. This proposal aims to match gcc, where instead of
-mfpu
to specify FPU/NEON, the same information will be passed using feature modifiers on
-march
. It was pointed out that GCC also has
-mcpu
to complicate things. It's hoped collaboration with the GCC devs will lead to a simplification that both can use.
Tobias Grosser has
set up some new machines tracking performance at -O3
using
LNT
, which is a framework used for performance tracking of LLVM over time. Tobias is asking for someone to step in and improve the LNT infrastructure to take advantage of this new data. LNT is written in Python, using Flask and SQLAlchemy so this would be an ideal project for someone interested in contributing to LLVM but perhaps doesn't match the typical profile of the LLVM contributor.
Timothy Baldridge asks whether
LLVM can inline external library functions in a JITted method
. Replies point out that for the specific example given (memcpy), LLVM is already able to inline. Kevin Modzelewski
describes a technique he's used
.
Rafael Espíndola announces a new milestone, all in-tree backends
now use MCInst for printing assembly
. Out of tree targets will need to lower MachineInstr to MCInst to use the new printer and the recent
conversion of the Sparc backend
to do this is probably as good a guide as any.
As part of the effort to use C++11 inside the LLVM codebase, Chandler Carruth has asked anyone running build-bot to look at
upgrading to the new baseline compiler versions
. These are MSVC 2012, GCC 4.7, or Clang 3.1.
Jasper Neumann has been
working on switch lowering using hashing
as an alternative to using a jump table. He later
further elaborates on the technique
and points to an interesting looking paper,
Multiway Branch Code Generation
by Roger Anthony Sayle.
Kevin Modzelewski is encountering
disappointing bitcode parsing performance
, in particular when debug info is present. The issue is not identified or solved yet, I'm hoping to be able to point to an explanation of the problem in next week's issue!
Chandler Carruth suggests that the
interprocedual analysis passes be merged in to the Analysis library
. Right now, various interprocedural analyses live in lib/Analysis/IPA and are built as the LLVMipa library. Chris Lattner agrees so we can expect the merge to happen in the not too distant future.
Chandler Carruth has
suggested
that the
LLVM coding standards
be updated so that namespaces are never indented, as opposed to the current confusing mixture. Despite the fact that debating whitespace is a favourite pastime of most programmers, the thread has been fairly uncontroversial thus far.
Milian Wolff wonders about
using the clang C API to parse default values
.
Renato Golin is working towards
adding various pragmas to Clang
and is seeking feedback on how to implement it. A few people on the mailing list suggest it might be worth trying to instead implement these using
C++11 generalized attributes
and perhaps enabling support for the syntax in C99.
The
__has_attribute
feature macro is commonly used to detect support for a particular attribute in the compiler. Aaron Ballman
suggests extending it
so you can test for the precise form of attribute syntax you are after.
LLVM commits
The Sparc ASM parser has seen further development, learning to parse branch instructions, conditional moves, and floating point instructions and more. It also gained an initial disassembler implementation.
r198738
,
r199033
,
r198591
In SimplifyCFG will now understand that when building a lookup table for a switch with no holes that it doesn't need a default result. According to the commit message, this saves 164KB off the clang binary in a bootstrap build.
r199025
The new pass manager saw further developments.
r198998
and many others (prefixed with
[PM]
in the commit logs)
The SampleProfile pass saw further development. Profile samples are propagated through the CFG, heuristically converting instruction samples to branch weights. Work was done to extend and simplify the format of sample profile input files.
r198972
,
r198973
The LoopVectorizer can use versioning for strided memory access.
r198950
In DataLayout, 'w' is now used rather than 'c' for win32 name mangling.
r198938
The LLVM developer policy was updated to more clearly spell out how to submit patches to the project.
r198901
WriteAsOperand has been killed in favour of the the printAsOperand method.
r198836
The x86 backend learned some more AVX-512 intrinsics.
r198745
Clang commits
Support for the
enable_if
attribute was added. This can be placed on function declarations to control which overload is selected based on the values of the function's arguments. See the commitdiff (particularly the docs change) for more info.
r198996
More work on MS VC++ ABI compatibility was committed.
r198907
,
r198975
,
r198977
,
r198900
and more.
__has_attribute
now understands target-specific attributes.
r198897
The clang plugin infrastructure is now covered by at least some tests.
r198747
The documentation on clang internals was updated with more up to date information on adding new attributes.
r198705
An initial instrumentation-based profile guided optimisation implementation landed.
r198640
