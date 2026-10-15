---
title: "ClangIR and the cost of MLIR"
url: "https://maskray.me/blog/clangir-and-the-cost-of-mlir"
fetched_at: 2026-10-12T10:11:00.446695+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# ClangIR and the cost of MLIR

Source: https://maskray.me/blog/clangir-and-the-cost-of-mlir

ClangIR (CIR) is an MLIR dialect between the AST and LLVM IR, and in
October 2026 the clang area team
accepted
building it by default
. CIR is built on MLIR because each step along
the way was locally reasonable, and together the steps locked MLIR in.
The costs (build time, binary size, MLIR API churn) land largely on
Clang contributors who neither chose MLIR nor use CIR.
This post traces how CIR came to depend on MLIR, collects what the
dependency costs, and uses an MLIR-free CIR as a thought experiment to
separate the costs inherent to MLIR from those that can be reduced.
This post relies heavily on an LLM agent (Claude Code). It read the
Discourse threads, GitHub PRs, slides, and the source tree, computed the
build-closure and contributor numbers, and drafted the text, which I
then edited. My part was steering, and some of what I added to its
context:
the build-by-default and premerge-testing RFCs, and a discussion on
Discord #llvm;
the opportunity-cost framing: contributors without fast machines pay
for MLIR (and Flang) on every llvm/ change, though most of them never
use either.
Treat the numbers as checked but not peer-reviewed.
What ClangIR replaces
Classic Clang lowers the AST to LLVM IR in
clang/lib/CodeGen
. With
-fclangir
,
clang/lib/CIR/CodeGen
(CIRGen) emits CIR instead, a set of
CIR passes runs, CIR is converted to MLIR's
llvm
dialect,
and MLIR translates that to LLVM IR.
CIRGen mirrors the AST-to-IR half of
clang/lib/CodeGen
file by file:
CodeGenFunction
becomes
CIRGenFunction
,
CGExprScalar.cpp
becomes
CIRGenExprScalar.cpp
, and so on. It is 66K lines against
CodeGen's 214K, with 786
errorNYI
calls marking what is
missing.
Work that classic CodeGen does while emitting IR becomes separate
CIR passes: C++ ABI lowering (
CXXABILowering
), calling
conventions (
CallConvLowering
), exception handling
(
EHABILowering
), and structured control flow to a CFG
(
FlattenCFG
).
The optimizer and backend are not replaced. CIR's frontend action
calls
emitBackendOutput
from
clang/lib/CodeGen/BackendUtil.cpp
, so
clangCIRFrontendAction
links
clangCodeGen
.
Some code is shared rather than duplicated:
clang/lib/CodeGenUtils
(
#221001
,
September 2026) holds AST-only helpers used by both, and
llvm/lib/ABI
(LLVMABI) does ABI classification for CIR's
calling-convention lowering and, under
-fexperimental-abi-lowering
, for classic CodeGen.
Nothing in
clang/lib/Analysis
is replaced yet. The CFG,
the analyses behind Sema's analysis-based warnings, the dataflow
framework, lifetime safety, and the Static Analyzer all still work on
the AST and the CFG. Upstream CIR's only analysis is an alias analysis
used by ABI lowering. Replacing CFG-based analysis is an aspiration
rather than a plan: the 2022 RFC argued that the CFG is "discarded after
analysis" and "has lots of known problems", and the area team expects
CIR to replace "the current CodeGen and CFG analysis", but no ClangIR
document schedules it.
The in-tree roadmap,
clang/docs/CIR/CodeDuplication.md
,
is about CodeGen. It plans to raise CIR to a higher level, move ABI
details into later lowering passes, and "replace relevant parts of the
existing implementation, piece by piece" with implementations shared by
both code generators. Calling conventions are the first case (LLVMABI,
plus an MLIR adapter that FIR can also use). The roadmap lists the next
candidates: constant expression evaluation, complex multiplication and
division, builtins, exception handling and C++ cleanups, inline
assembly, and C++ ABI handling (vtables, virtual calls, constructor and
destructor arguments, dynamic casts, base class addresses, type
descriptors, array new and delete). Linkage, alignment, debug info,
TBAA, sanitizers, and lifetime markers are spread through CodeGen and
listed as harder to share. It also aims to run all classic CodeGen tests
through the CIR path.
Where things stand
The area team's decision says "ClangIR is likely to reach the point
where it becomes the replacement for the current CodeGen and CFG
analysis." The same post promises that
-DCLANG_ENABLE_CIR=Off
"will still be a supported
configuration for the forseeable future", and
-fclangir
stays off by default. On main,
clang/CMakeLists.txt
tests
CLANG_ENABLE_CIR
but declares no
option()
for
it, so the flip is still pending.
A separate RFC,
Add
CIR testing to clang and MLIR CI
(
#227834
),
would build and test CIR in premerge for clang/ and mlir/ changes. nikic
is
weakly
-1
: if contributors have to fix CIR failures, "they also need to
build and test CIR locally", so premerge testing and build-by-default
"should go hand in hand". rengolin
calls
asking non-CIR developers to stub out CIR breakage "an unreasonable
request" and suggests a different CI setup.
As for the compiler itself, the
ClangIR
progress report for September 2026
measures
-fclangir
against classic CodeGen: 1.32x the wall time on a typical file, 1.57x
across the tree, 1.17x the memory, and 3% more code.
Why MLIR
ClangIR started at Meta in October 2021. Bruno Cardoso Lopes and
Nathan Lanza proposed it in
RFC:
An MLIR based Clang IR (CIR)
in June 2022, and it moved to an LLVM
incubator in August 2022 (timeline from the
2025
keynote
). The primary goal was "improved diagnostics for modern
C++"; the design had "grown out of implementing a lifetime
analysis/checker pass"; optimization and lowering were "a secondary goal
for now". Clang lacked a suitable IR: the AST is awkward for dataflow,
LLVM IR is too low level, and the Clang CFG is discarded after analysis.
The RFC's entire "Why MLIR?" section reads:
MLIR provides a solid and tested framework to build custom IR and run
passes. Among several other capabilities, it's also in already in tree
and used by Flang to build FIR.
Nobody in the thread argued for a bespoke IR; the closest was John
McCall's
aside
that if MLIR needed in-tree dialects to be useful, "it would be better
to just not use MLIR" and write the IR "from scratch on top of
llvm::ilist". efriedma
wrote
"using MLIR to build it seems like the right approach" and objected to
structured control flow instead. Gábor Horváth
argued
that the CFG suffices for lifetime analysis, and John McCall
wanted
a two-stage lowering like Swift's. Reid Kleckner
asked
for an agreed compile-time ceiling, "like +15-25%, before making this
part of the default pipeline".
-fclangir
is still opt-in,
and 1.32x/1.57x is already past that ceiling.
Lopes's later talks do not revisit the choice. The
2023
Developers' Meeting talk
(
video
) describes
CIR as "Implemented as an MLIR dialect for C/C++". Its pipeline diagram
goes from CIRGen through CIR passes, including the lifetime checker, to
LLVM lowering, with a dashed side path through SCF and Affine. The
lifetime checker was real: the talk reports integration with clangd,
clang-tidy, and an internal IDE, and "Successful detection of lifetime
bug that caused a major internal outage". The same talk lists "Compile
& execution time, binary size, memory usage" among the challenges.
The
project
site
gives today's rationale: MLIR enables "the development of
passes and IR, rapid design iteration, and reuse of community-provided
analyses and transformations". Apart from a few OpenMP passes, clang's
CIR pipeline runs only CIR's own passes.
The lifetime checker never reached upstream CIR. Clang's
lifetime-safety analysis (
#142313
,
July 2025) is built on the CFG, and Horváth is among its authors.
NVIDIA, 2023: OpenACC lives
in MLIR
In October 2023 Erich Keane (NVIDIA) posted
RFC:
Implementation of OpenACC 3.3 for offload in Clang
. Flang lowers
OpenACC through MLIR's
acc
dialect: "It is our intention to
use that as well, so NVIDIA is beginning to participate in the CIR/MLIR
effort". Clang shares more than the dialect with Flang. CIR and FIR
implement the same
acc
type interfaces
(
CIROpenACCTypeInterfaces.cpp
,
FIROpenACCTypeInterfaces.cpp
), and acc-to-GPU passes are
landing in
mlir/lib/Dialect/OpenACC/Transforms
. Classic
CodeGen has no OpenACC lowering (
CodeGenFunction.h
: "TODO
OpenACC: Implement this"), so CIR plus
acc
is Clang's only
OpenACC implementation.
Strictly, the requirement was MLIR's
acc
dialect, not
CIR. Keane's
fallback
was "LLVM-IR based metadata to enable the translation to the OpenACC
MLIR dialect", and the
second
fallback
, "lowering as OMP does", gives up sharing with Flang.
OpenMP has the same sharing benefit without the necessity: CIR emits
omp
ops, but classic CodeGen already lowers OpenMP.
By 2026 the motive had widened. Keane
wrote
that the goal is to "enable further advancement for our compiler stack …
the way to allow those to integrate with C/C++/Clang is to have a
dialect for it".
2024–2026: lock-in
Lopes
proposed
upstreaming
in January 2024, Lanza landed the scaffolding in April
2024, and NVIDIA's first upstream CIR commit (David Olsen) followed in
November 2024. Today CIR is 120K lines (lib + include) on ODS, MLIR
interfaces, and MLIR rewrite drivers, with ~230 ops and 1,269 test
files, 868 of which check
-emit-cir
output in MLIR's
textual format.
Readers might ask whether NVIDIA led the upstreaming. I counted
commits touching
clang/lib/CIR
, both upstream and in the
archived llvm/clangir incubator (excluding incubator commits that also
exist upstream). Affiliation comes from email domains, GitHub profiles,
and LinkedIn; a GitHub profile shows the current employer, not the
employer at commit time.
Author
Incubator only (2,498,
2021-08..2026-02)
Upstream (2,023)
Meta
55%
1.5%
NVIDIA
2.7%
47%
Amr Hesham (GSoC 2025, then kept going)
5%
14%
unknown
28%
27%
Meta wrote the incubator: its share was 100% in 2021, 97% in 2022,
about half in 2023–2024, and 11% in 2025. NVIDIA wrote 45–49% of
upstream commits each year, so by volume NVIDIA led the upstreaming; by
authorship of the RFC and the scaffolding, Meta did. Of the 260 upstream
commits titled "upstream …", the explicit ports from the incubator, Amr
Hesham wrote 37%, NVIDIA 31%, and unknown authors 31%. Most NVIDIA
commits are new code written upstream. The maintainers are Andy Kaylor
(NVIDIA), Bruno Cardoso Lopes (Meta), and Henrich Lauko (NVIDIA since
August 2026, previously Trail of Bits and NextSilicon).
The stated long-term value is mixing dialects. From Lopes's
SC24
talk
(November 2024) on, the slides describe CIR as a way to "Move
Clang onto the MLIR substrate" and "Use MLIR from C, C++ and
extensions", and to "Mix CIR with downstream and custom dialects". The
2025 keynote with Andy Kaylor lists "Lower to other MLIR dialects" among
CIR's uses, next to the lifetime checker, and has a slide titled "CIR
Won't Always Go To LLVM IR", where CIR is consumed by MLIR to "Offload
to GPU or other targets".
clang/docs/CIR/CodeDuplication.md
: "even now we generate
the ACC (OpenACCC) [sic] dialect in combination with CIR, and when
support for OpenMP and CUDA are added, similar mixing will occur". The
area team's acceptance ratifies this direction. Every year of
upstreaming raised the cost of switching, and the main funder's motive
now depends on MLIR itself, not just on the original team's choice of
framework.
The costs
Build
aengelke's
-1
in the build-by-default thread starts from "I usually don't build MLIR".
His measurements of
ninja clang
in a dylib build track the
trimming work:
My #221616 links only the MLIR dialects CIR uses; on 192 cores
PragmaTwice
measured
it alone taking
ninja clang
wall time from +109% to +75%.
#221813 shards the LLVM dialect's generated code, and #222576 gives
MLIRIR a precompiled header. On 2026-09-14,
libclang-cpp.so
in the dylib build was still +91% (+83% stripped); on c-t-t, the
clang
binary was +51% (+68 MiB) and the build's max-rss
+40%. The area team's "roughly 1.2x for a build only building clang" is
wall time of a parallel build, which hides much of the CPU cost.
The c-t-t
comparison
for the "enable clangir" commit lists per-file compile times. Summed,
they add 1,644 s (+48%): 751 s for CIR's own 100 object files
(
CIRDialect.cpp.o
alone takes 44 s) and 893 s for MLIR (853
s in 380 object files, the rest in its precompiled headers and TableGen
tools). These sums measure work, not wall time.
clang
still links a closure of 90 MLIR libraries, and
some are unused:
MLIRArithToLLVM
depends on
MLIRArithTransforms
for one helper,
populateCeilFloorDivExpandOpsPatterns
(
#118839
),
which drags in Bufferization, SparseTensor, Tensor, Vector, and Shard
(~177 s); see
Reducing the cost
.
MLIROpenACCDialect
depends on
MLIRGPUDialect
(~38 s,
#174671
).
PDL (~21 s) can be disabled with the existing
MLIR_ENABLE_PDL_IN_PATTERNMATCH
option.
The often-cited NVVM and ROCDL dialects
(
NVVMDialect.cpp.o
108 s and
ROCDLDialect.cpp.o
134 s in aengelke's 2026-09-05 list) are
no longer in the closure after #221616; only 3.3 s of their TableGen
output remains, via the
mlir-headers
umbrella target.
MLIR's headers are heavy. For files under
tools/mlir/
,
the frontend is 75% of compile time and header parsing 55% (aengelke's
numbers in
#213412
).
MLIRIR now has a precompiled header, but CIR's own libraries do not, and
AddLLVM.cmake
lets a library reuse the precompiled header
of at most one direct dependency. CIRGen reuses clangAST's, so each of
its files reparses the MLIR and CIR dialect headers; a private
precompiled header like clangCodeGen's (
#206018
)
cuts CIRGen's summed compile time by 72%.
Contributors without a build
farm
Most of the numbers above come from many-core machines, and wall time
on a many-core machine hides the cost. On aengelke's 96-thread machine,
ninja clang
used 30% more CPU time but 71% more wall time,
because a few slow files dominate the critical path (on c-t-t,
CIRDialect.cpp.o
takes 44 s and MLIR's
OpenACC.cpp.o
31 s). With fewer cores, wall time approaches
CPU time divided by the core count: the extra 2,100 CPU-seconds of that
build are 4–5 minutes on 8 threads, for every clean build.
Incremental builds matter more to someone iterating on a patch. From
the c-t-t per-file times and the header dependencies of my MLIR-enabled
build:
Linking
clang
is 38% slower on c-t-t (105 s to 145 s);
with lld it stays under a second.
Touching
llvm/ADT/DenseMap.h
,
StringRef.h
,
or
raw_ostream.h
recompiles 2,504 files (3,274 s summed)
without CIR; MLIR adds 380 files (853 s) and CIR another 100 (751 s),
+49%.
Touching
llvm/IR/Function.h
recompiles 58 more MLIR
files (+16%), before counting CIR's lowering.
Touching
clang/AST/Decl.h
recompiles 521 files (1,198
s) without CIR; CIRGen adds at least 51 files and 415 s, +35%. CIRGen
alone costs 2.2x classic CodeGen (104 files, 189 s); in my parallel
build, 1.6x (351 s vs 221 s).
Memory and disk grow too: c-t-t's build max-rss is +40% (+1 GiB),
which matters when running many jobs on a 16 or 32 GiB machine, and
aengelke's build directory grew from 1.5 GiB to 2.4 GiB.
-DCLANG_ENABLE_CIR=Off
stays supported, but once
premerge tests CIR, a contributor who opts out learns about CIR breakage
from CI and then has to build CIR anyway. Flang shows where this goes.
.ci/compute_projects.py
tests flang and mlir for every
llvm/ change, so fixing a breakage means building Flang and MLIR. In my
full build (clang, mlir, flang, lld, …), summed per-file compile time
splits clang 25.6%, mlir 19.7%, llvm 16.2%, flang 14.5%. Users who need
Flang or OpenACC can get them from a vendor toolchain; a contributor
whose llvm/ change breaks them has to build them to fix it. Companies
that fund CIR and Flang have build farms; many volunteers and
contributors from smaller companies have a desktop or a laptop, and each
component that becomes everyone's responsibility raises the bar for
them.
Runtime, for every clang user
Building CIR in costs something even without
-fclangir
.
On c-t-t, stage2-O2-g compile time is +0.18% and max-rss +2.6%. In
aengelke's dylib build,
clang -emit-llvm -c empty.c
executes 12% more instructions, down from +88% when clang still linked
libMLIR.so
, and
clang -c empty.c
still crashed
on 2026-09-14. aengelke names dynamic relocations, global constructors,
and additional
cl::opt
as probable causes.
With
-fclangir
, the five worst files in the progress
report took 2.0–4.1x as long, "almost all in lowering CIR to LLVM IR:
30–92 s per file, roughly split between the CIR-to-LLVM-dialect
conversion and the translation to LLVM IR". A linear scan for comdats
made that quadratic;
#227127
cut
the lowering to 8–11 s. Quadratic paths keep surfacing through the
llvm
dialect:
#198424
for
insertvalue
globals, and Flang's
#140268
and
#209393
.
For typical files, I compiled 29 random C++ files from
llvm/lib
and
clang/lib
with their build flags
(-O3) and
-ftime-trace
, with and without
-fclangir
, using a Release+Asserts clang at a160747d89a3
(after #227127).
-fclangir
took 1.15x as long in total,
1.12x for the median file, below the progress report's 1.32x. The extra
time splits roughly in thirds:
Phase
Extra time
Share of the
-fclangir
compile
CIRGen (vs. classic IR generation)
3.6 s
4.4%
CIR-to-CIR passes
3.0 s
3.6%
CIR to LLVM IR (pre-lowering passes, conversion, translation)
3.8 s
4.7%
optimizer and backend
0.4 s
0.5%
For the median file, lowering to LLVM IR is 3.6% of the compile, and
6.5% with the CIR-to-CIR passes. The lowering row includes the
pre-lowering passes (
HoistAllocas
,
FlattenCFG
,
EHABILowering
,
GotoSolver
);
GotoSolver
alone is 0.64 s, 17% of it. CIRGen's deferred
emission and the module verifier run outside any
-ftime-trace
scope, so I attribute the untraced time to
CIRGen.
Lopes's
AsiaLLVM
2025 report
measured the incubator in June 2025. On the three CTMark
programs that compiled,
-fclangir
took 1.9–2.9x the user
time at -O0 and 1.1–1.6x at -O2. For
clamr_cpuonly.cpp
at
-O0, classic CodeGen took 15 ms and CIRGen 289 ms, 265 ms of it in
CIRGenModule::applyReplacements
, which the slides call "low
hanging fruit".
Some costs are not measured yet. CIR emits no debug info; in Flang,
#146543
cut one type's debug-info nodes from 1.75M to 8K. MLIRContext uniques
types, attributes, and locations and
never
frees them
.
CIRGenFunction::getLoc
eagerly calls
getPresumedLoc
and creates a uniqued
FileLineColLoc
for each call.
Maintenance
CIR re-implements classic CodeGen (ABI lowering, builtins, …), and
CodeDuplication.md
accepts "a significant amount of
technical debt" kept in sync by hand. That would be true of any new IR,
MLIR or not.
MLIR's API churn is MLIR-specific. The 2025 keynote names it among
the growing pains: "The ClangIR build sometimes gets broken by changes
in MLIR or other parts of clang". I counted at least six CIR fixups
since June 2025 caused by MLIR interface changes, e.g. after the
RegionBranchOpInterface
revamp (
#165441
) and
a
MemorySlotInterfaces
rename (
#229068
).
Premerge testing would turn them into every clang and mlir author's
problem.
Compile-time culture
llvm-compile-time-tracker.com measures every LLVM commit, and
regressions get bisected and discussed. I found no per-commit tracker
for MLIR or Flang, and MLIR's in-tree benchmark runner
mlir/utils/mbr
has had no functional change since July
2022. MLIR compile-time work happens after users hit a wall: the
One-Shot
Dialect Conversion driver
(dialect conversion was "by far the
slowest part"), the LLVM dialect sharding, the MLIRIR precompiled
header. Flang's
#58730
, at
4x gfortran's time and memory, has been open since 2022. My reading is
that MLIR's main users (machine learning compilers that compile a model
once and run it many times) tolerate costs that a C++ build, recompiling
large translation units on every edit, does not. Clang's bar has to be
enforced on the CIR side.
Reducing the cost
I keep this table updated as patches land. Local numbers come from my
machine (i7-14700K, 28 threads, Release with assertions, lld), with
summed per-file times from
.ninja_log
.
Patch
Status
Effect
#221616
link
only the MLIR dialects CIR uses
landed 2026-09-07
ninja clang
wall time +109% to +75% (PragmaTwice, 192
cores)
#221813
shard the LLVM dialect's generated ops
landed 2026-09-07
splits
LLVMDialect.cpp.o
, 121 s in aengelke's list
#222576
precompiled header for MLIRIR
landed 2026-09-10
c-t-t build time +58% to +47% across it
#227127
cached symbol tables for comdat lookups
landed 2026-10-02
lowering of the five worst files from 30–92 s to 8–11 s
precompiled header for clangCIR
not yet posted
CIRGen's 54 files from 312 s to 85 s summed (including 6 s for the
header); user CPU 282 s to 78 s
move the ceil/floor div expansion from MLIRArithTransforms to
MLIRArithUtils
not yet posted
clang
links 16 fewer MLIR libraries (90 to 74); 64
fewer object files, 147 s summed (177 s on c-t-t)
MLIROpenACCDialect
without
MLIRGPUDialect
open
~38 s;
acc
declares
gpu
as a dependent
dialect and uses its types
PDL off when MLIR is only a dependency
open
~21 s
shard
CIRDialect.cpp
open
58 s locally, the slowest file in the build; its generated
CIROps.cpp.inc
has 102K lines
Thought experiment: an
MLIR-free ClangIR
What does CIR take from MLIR?
Dialects:
cir
,
builtin
,
llvm
(~900 references),
acc
(402),
ptr
(74),
omp
(~65),
dlti
.
ODS: ~230 ops, 164 declarative assembly formats, 53 verifiers, 22
folders/canonicalizers.
OpBuilder
, symbol tables, and the region-branch, loop,
call, memory-slot, and data-layout interfaces.
The pass manager with 12 CIR passes, the greedy rewrite driver, and
the conversion driver (205 lowering patterns, 125 with hand-written
bodies).
The
llvm
dialect and
ModuleTranslation
.
Not used in clang's pipeline: MLIR's mem2reg and SROA (CIR implements
the memory-slot interfaces, but only
cir-opt
tests run
-mem2reg
), CSE, the inliner, the dataflow framework, and
the loop dialects. The incubator's ThroughMLIR path (to
affine
/
scf
) never went upstream; efriedma
noted
that "translating from ClangIR to the MLIR's loop-based dialects is
probably more complicated than ClangIR itself."
CIRGen would port almost unchanged. Only 8.6% of its 66K lines
mention
mlir::
, mostly
Value
,
Location
,
Type
,
OpBuilder
,
Block
, and
Region
. An API-compatible core
would keep the ~1,300
XOp::create
calls, which depend only
on generated signatures. The
.td
files are TableGen data,
but they carry 818 embedded C++ blocks (521
mlir::
references) and declare MLIR interfaces, so they are reusable only with
a source-compatible core.
The real cost is everything else: an IR core; an ODS-equivalent
emitter including the assembly-format generator (the MLIR emitters it
replaces are ~14K lines, plus 5K in
mlir/lib/TableGen
); the
interfaces; 15K lines of passes rewritten off MLIR's drivers; and the
868
-emit-cir
tests reproduced byte for byte or churned.
CIR would also lose MLIR's reviewers; Lauko was
nominated
as
maintainer for "overseeing the quality of CIR dialect (the MLIR part)".
The gains: most of MLIR's ~890 s of build work, no conversion step or
extra IR copy,
SourceLocation
as the location type, memory
freed with the module, and no MLIR API churn.
OpenACC forces one of three choices: drop it, duplicate Flang's
acc
pipeline, or keep MLIR as an optional island reached
through LLVM IR metadata. Only Keane's one fallback sentence supports
the third; the route (metadata, then
ModuleImport
, then
acc
ops, then the shared passes) is my extrapolation, and I
found no work on it.
So an MLIR-free CIR is technically plausible, but it removes the
property the funders want, and I see nobody who would fund it. Its value
is as a lens. It separates what only leaving MLIR fixes (immortal
context uniquing, the volume of ODS-generated code, the core library
closure) from what can be fixed inside MLIR.
Conclusion
Clang needs a better IR than the AST and the CFG, and CIR is the one
that got funded. Who funds Clang has changed, and that explains much of
this post. Commits under
clang/
by who paid for the work,
usually the author's employer at the time:
Year
Commits
Authors
Google
Apple
Intel
Red Hat
NVIDIA
AMD
other companies
universities and labs
individuals or unknown
2010
8,192
72
5%
79%
0%
0%
0%
0%
3%
6%
7%
2012
7,545
135
23%
54%
0%
0%
0%
0%
7%
2%
13%
2014
6,347
200
43%
18%
3%
0%
0%
0%
20%
1%
15%
2016
5,253
305
38%
21%
5%
0%
0%
2%
16%
1%
17%
2018
4,973
351
30%
19%
8%
0%
0%
2%
19%
4%
18%
2020
5,523
551
29%
10%
4%
1%
0%
5%
26%
2%
22%
2022
6,193
677
21%
7%
8%
6%
0%
3%
22%
6%
27%
2024
7,330
882
12%
6%
5%
12%
4%
6%
26%
0%
29%
2026 (to October)
7,160
1,024
7%
9%
4%
8%
11%
10%
19%
3%
29%
I took the employer from the commit email when it is a company
address. For the authors who used personal addresses, which before the
2019 move to GitHub was most of them, I looked up dated employment for
about 150 of the most active ones from LinkedIn, Developers' Meeting
speaker lists, paper affiliations, and GitHub profiles. Work done in
spare time counts as individual even when the author had an unrelated
employer, such as Craig Topper's X86 work before he worked on it at
Intel and my own Clang work while I was at Google. "Individuals or
unknown" is independent contributors plus authors I could not place;
most of it is the long tail of people with a few commits each. Before
2019, the recorded author is the committer, who often landed other
people's patches, so the early author counts are low. The attribution is
best-effort: public profiles are incomplete or out of date, employment
dates are approximate, and a difference of a few points is within the
error. Corrections are welcome.
Commit counts undercount review, and cleanup commits inflate some
authors: Kazu Hirata's mechanical cleanups were 158 of Google's
clang/
commits in 2024 and 326 in 2025 (24 in 2026). For
2026 I also counted approvals on the 7,005 merged pull requests that
touch
clang/
, each approver once per pull request (8,333
approvals), attributing reviewers the same way; "CIR" means the 1,280
pull requests whose title is tagged CIR:
2026 pull requests
Google
Apple
Intel
Red Hat
NVIDIA
AMD
other companies
universities and labs
individuals or unknown
authored
7%
9%
4%
8%
11%
10%
19%
3%
29%
approved
8%
13%
7%
2%
17%
10%
31%
3%
9%
authored, excluding CIR
8%
11%
5%
10%
3%
11%
19%
3%
30%
approved, excluding CIR
10%
17%
8%
2%
7%
11%
32%
3%
10%
Individuals write 29% of the pull requests but give 9% of the
approvals; review is concentrated in fewer, mostly company-paid people.
Outside CIR, the most active approvers are Corentin Jabot (Bloomberg),
Aaron Ballman (Intel), Balázs Benics and Gábor Horváth (Apple, mostly
the Static Analyzer), Joseph Huber (AMD), and Eli Friedman (Qualcomm).
Inside CIR, NVIDIA gives 57% of the approvals, mostly Andy Kaylor and
Erich Keane.
Google and Apple wrote 84% of Clang commits in 2010 and 61% in 2014,
but 16% in 2026. Their priorities were large C++ code bases, compile
time, and tooling. Red Hat's share is mostly Timm Bäder's bytecode
constant expression interpreter. NVIDIA's is mostly CIR (3% of commits
outside CIR), and its Clang people joined from elsewhere: Erich Keane
from Intel in August 2023, Andy Kaylor from Intel in January 2025, and
Reid Kleckner from Google in December 2025. AMD's is mostly AMDGPU, HIP,
and offloading work. Intel's share includes Aaron Ballman, Clang's lead
maintainer, who describes his job as keeping Clang healthy because
Intel's ICX compiler is built on it. Language conformance work comes
from new sponsors: Bloomberg has sponsored Corentin Jabot's Clang work
since 2022, and he now leads a Bloomberg team on C++ conformance in
Clang; the C++ Alliance employs Krystian Stasiowski and Matheus
Izvekov.
The new funders build GPU and accelerator compilers, and their other
compilers (Flang, Triton, IREE, their own stacks) are built on MLIR. For
them, a Clang that emits an MLIR dialect is the point, not an
implementation detail. For the C++ programmers who were Clang's main
constituency, CIR has to earn its place by being better at what the AST,
the CFG, and classic CodeGen do today: diagnostics, safety analyses, and
optimizations that need C++ semantics, without making the compiler
slower to build or run. Lifetime safety went to the CFG in 2025 rather
than wait for CIR, which shows the bar is real.
The question was never really whether CIR should use MLIR. It is
whether anyone is funded to keep the cheap path cheap. Today the
measurable costs fall on Clang contributors and users, most heavily on
those who build on their own machines, while the benefits of MLIR accrue
to the organizations funding CIR. Tracking
-fclangir
on
c-t-t, keeping
-DCLANG_ENABLE_CIR=Off
working, and landing
the cheap build fixes in
Reducing the
cost
are how the people paying the cost get something back.
