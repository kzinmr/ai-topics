---
title: "LLVM Weekly - #111, Feb 15th 2016"
url: "https://blog.llvm.org/2016/02/llvm-weekly-111-feb-15th-2016.html"
fetched_at: 2026-05-05T07:01:39.515089+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #111, Feb 15th 2016

Source: https://blog.llvm.org/2016/02/llvm-weekly-111-feb-15th-2016.html

LLVM Weekly - #111, Feb 15th 2016
Welcome to the one hundred and eleventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
There has been a
new release of the CilkPlus compiler
. This includes an update to the latest LLVM and Clang trunk. CilkPlus implements the Cilk Plus language extensions for data and task parallelism in Clang.
There's been some more papers appearing from the C++ standards committee. P0225R0, or as you may prefer to call it "
Why I want Concepts, and why I want them sooner rather than later
" is worth a read. There's also been a few
other recently published papers
on iterator facades, the filesystem technical specification, and unified function call syntax.
On the mailing lists
Jacques Pienaar has proposed
upstreaming the 'Lanai' backend
. This is for a CPU design used internally at Google, and the posting of these patches did attract some
attention in the press
. A good chunk of the ensuing discussion focused on what the bar should be for accepting a new backend upstream. There seem to ultimately be far more people for the upstreaming than against it, but some concern was raised about the ability for others to test the generated code without access to hardware or even simulators.
Natanael Ramos recently worked with LLVM for his bachelor thesis, and as a result
wrote and submitted a tutorial for writing a new LLVM register allocator
. This can also be found
on github
.
Nolan has been working on an
experimental 6502 backend
, and sought some help with a
memory operand folding problem
. He later followed up to the list
with his solution
, and David Chisnall added some
extra thoughts on potential approaches to targeting 6502 or similar architectures
.
Hans Wennborg is
looking for help in expanding the release notes for the 3.8 release
.
Vaivaswatha Nagaraj has been working on a
control structure analysis
capable of detecting control structures in the CFG and is seeking feedback on his code.
Lang Hames has followed up to his RFC on error handling in LLVM libraries with a detailed post
summarising his thoughts and responding some some feedback
.
Sadly, CMake's current Ninja generator
is non-deterministic
. The good news is there is
already a fix in upstream CMake
.
Peter Collingbourne prototyped
a change to reduce DWARF emitter memory consumption
. Early results are very positive.
Philip Reames proposes
removing the inaccessiblememonly attribute from the 3.8 branch
, on the grounds that the major motivating patch was reverted, there has been no further development, and including it in a release may pose a backwards-compatibility concern. There appears to be agreement so far in the responses.
LLVM will be applying for inclusion in the Google Summer of Code this year. If you have a project listed on the 'open projects' page,
please review and update it if necessary
, or suggest new projects.
LLVM commits
The WholeProgramDevirt pass has been added. This implements whole program optimization of virtual calls where the list of callees is known to be fixed.
r260312
.
The AVR backend upstreaming continues with the addition of the AVR tablegen instruction definitions.
r260363
.
There's been a bunch of other work on the new global instruction selection mechanism this week, but the commits I'd pick out are the addition of support for translating Add instructions and for lowering returns. It is currently being tests with the AArch64 backend.
r260549
,
r260562
,
r260600
.
The AArch64 backend gained support (including a scheduling model) for the Qualcomm Kryo CPU.
r260686
.
LoopUnrollAnalyzer has been abstracted out from LoopUnrollPass, and gained unit tests for its functionality.
r260169
.
llvm-config gained preliminary Windows support.
r260263
.
The details of the convergent attribute have been clarified in the language reference. The convergent attribute will now be removed on functions which provably don't converge or invoke any convergent functions.
r260316
,
r260319
.
Clang commits
It is now possible to perform a 3-stage Clang build using CMake. It is suggested in the commit message this may be useful for detecting non-determinism in the compiler by verifying stage2 and stage3 are identical.
r260261
.
ARMv8.2-A can be targeted using appropriate Clang options.
r260533
.
Clang's CMake build system learned the
CLANG_DEFAULT_CXX_STDLIB
to set the default C++ standard library.
r260662
.
Other project commits
The new LLD ELF linker gained initial link-time optimisation support.
r260726
.
LLDB has seen some more updates for Python 3 support, though not yet enough for a clean testsuite run.
r260721
.
