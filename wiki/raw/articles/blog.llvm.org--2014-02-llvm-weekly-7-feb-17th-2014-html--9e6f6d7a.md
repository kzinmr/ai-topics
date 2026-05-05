---
title: "LLVM Weekly - #7, Feb 17th 2014"
url: "https://blog.llvm.org/2014/02/llvm-weekly-7-feb-17th-2014.html"
fetched_at: 2026-05-05T07:01:42.616808+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #7, Feb 17th 2014

Source: https://blog.llvm.org/2014/02/llvm-weekly-7-feb-17th-2014.html

LLVM Weekly - #7, Feb 17th 2014
Welcome to the seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
As always, apologies if I didn't pick up your favourite mailing list discussion or commits. Do drop me a line if you think I'm missing something interesting. There haven't been that many external news stories or blog posts (that I've found) in the last week, but it's been a particularly busy week on the mailing lists with a whole bunch of interesting discussions or RFCs.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The
ELLCC Embedded Compiler Collection
now
has precompiled builds available
for ARM, i386, Mips, PowerPC and x86-64. Handily, these are all statically linked. The aim of ELLCC is to provide an easy to use multi-target cross compilation environment for embedded systems, and is of course based on LLVM and clang.
The next Waterloo Region LLVM Social
has been announced for Feb 20th
.
The next Paris LLVM Social
will take place on Feb 24th
, hosted by Mozilla.
On the mailing lists
Philip Reames contributed an RFC on
using GetElementPtr as the canonical form for pointer addressing in LLVM IR before CodeGenPrepare
. The motivation behind this proposal will be interesting to many, particularly the Rust community and other language implementors looking to target LLVM. Philip and his colleagues (at Azul Systems I believe) are looking to support precise garbage collection in LLVM, and excitingly a complete upstreamable implementation should be coming "relatively shortly. (i.e. months, not weeks, not years)"
As a followup to last week's discussions on the GCC mailing list, Renato Golin has written a
detailed proposal on how LLVM and GCC developers can co-operate
. He is welcoming responses
on Slashdot
. Chris Lattner is very much in favour of the effort, though points out that there are some lists already used for this purpose (such as the 'Itanium ABI list', which I assume refers to
cxx-abi-dev
) and perhaps other similar vendor-neutral mailing lists could be created.
Tom Roeder has posted an
RFC on the integration of control-flow integrity techniques in to LLVM
. Control-flow integrity (CFI) helps to protect against a variety of attacks by ensuring control flow at run time matches a path determined ahead of time, and is described in
this 2005 paper
. Tom has an implementation that has been tested on Chromium, producing an overhead of ~4% for the dromaeo benchmark. JF Bastien responded indicating the PNaCl team would be interested in this work, while other respondents discussed representing a jump table in LLVM IR as opposed to inline assembly.
Jordan Rose kicked off a discussion on
the future of the clang static analyzer
. One issue he raises is how to mark issues as false positives, hopefully in a more sophisiticated way than disabling checkers. He also mentions long term plans for adding a full-program analysis mode that would work across translation units. Ted Kremenek
follows up
with more details about treating reported diagnostics as 'issues' which might be suppressed individually.
Andrew Bokhanko from Intel initiated a
discussion on adding some sort of SIMD pragma to Clang
. Options include upstreaming the implementation of OpenMP 4's
#pragma omp simd
from
clang-omp
.
Mahdi Hamzeh writes to the mailing list with a
query about if-converting before register allocation
. Andrew Trick points to the EarlyIfConverter, which can be run before register allocation but only generates conditional moves rather than predicating instructions. He
suggests an approach
for implementing if-conversion as a target-specific pass.
Vadim Chugunov
kicks off a discussion on a compiler-rt roadmap
. Issues include a potential rename, whether libunwind should be removed, and ensuring that it builds for all platforms that LLVM can target.
Matt Arsenault is
seeking ideas on solving a problem where loop induction variables are larger than they need to be
.
Howard Hinnant is stepping down as code owner of libc++ and it
looks like Marshall Clow
is going to take over. Many LLVM devs also drop by to thank Howard for his hard work on libc++.
Ted Kremenek gives a
great summary of the status of ArrayBoundChecker and ArrayBoundCheckerV2
.
LLVM commits
AsmPrinter::EmitInlineAsm() will no longer use the EmitRawText() call for targets with mature MC (MachineCode) support. The MCASMInfo::UseIntegratedAS field was added. When true, the integrated assembler will parse inline assembly even when emitting assembly output.
r201237
.
The RTDyld API learned to precompute the amount of memory required for all sections in a module, and reserveAllocationSpace to reserve the given amount of space.
r201259
.
The LTO API gained
lto_module_create_from_memory_with_path
, which is mainly useful for emitting warning messages from the linker.
r201114
.
ScalarEvolution will now analyze the trip count of loops where there is a switch guarding the exit.
r201159
.
The notes on Phabricator now include a suggestion to provide a link to the Differential revision (the code review) on commits that have been reviewed in this way. Please do this!
r201160
.
The AArch64 backend now recognises Cortex-A53 and Cortex-A57.
r201305
.
The ARM integrated assembler gained partial support for the
.arch_extension
directive.
r201471
.
Clang commits
There have been yet more updates to Clang's Microsoft ABI compatibility. Clang now understands Microsoft's
pointers_to_members
pragma.
r201105
as well as the
vtordisp
pragma
r201274
. In other MS ABI developments, the
-vm{b,g,s,m,v}
are now supported too.
r201175
.
The command line option
-fstack-protector-strong
was added.
r201120
. See also
r200601
for info on the sspstrong function attribute.
Frontend support for the OpenMP
if
clause was committed.
r201297
.
You can use the
--rtlib=compiler-rt
flag to attempt to link against compiler-rt rather than libgcc.
r201307
.
The
-Wignored-pragmas
diagnostic was added, that will warn in any case where a pragma would have a side effect but is ignored.
r201102
.
The name of the checker producing each diagnostic message is now available through
getCheckName()
. This can be used to enable/disable a specific checker.
r201186
.
Clang now understands the
-fbuild-session-timestamp=
and
-fmodules-validate-once-per-build-session
flags which allows you to make it verify source files for a module only once during a build.
r201224
,
r201225
.
Other project commits
The sanitizer projects in compiler-rt gained the beginnings for a deadlock detector.
r201302
,
r201407
..
The original compiler-rt functions (i.e. those that act as a libgcc replacement) now live in the lib/builtins directory.
r201393
.
In lldb, the user can now specify trap-handler-names, a list of functions which should be treated as trap handlers.
r201386
.
