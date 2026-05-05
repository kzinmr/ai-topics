---
title: "LLVM Weekly - #87, Aug 31st 2015"
url: "https://blog.llvm.org/2015/08/llvm-weekly-87-aug-31st-2015.html"
fetched_at: 2026-05-05T07:01:40.169800+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #87, Aug 31st 2015

Source: https://blog.llvm.org/2015/08/llvm-weekly-87-aug-31st-2015.html

LLVM Weekly - #87, Aug 31st 2015
Welcome to the eighty-seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
It's a bank holiday weekend here in the UK, so apologies that you're reading this a few hours later than usual. As a quick reminder, if you're able to be in Geneva for the 9th-11th October then you should definitely
come along to ORConf
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
At the time of writing, LLVM 3.7.0 has not yet seen its official release,
but it has been tagged
. The final release should be out within the next day or so. Congratulations to everyone involved.
The deadline for submissions to the LLVM in HPC workshop has been
extended to Friday, September 4th
.
Save the date! The next Cambridge LLVM Social will be
on Wednesday 30th September
.
On the mailing lists
LLVM commits
The 'kaleidoscope' tutorial has seen a major update. Now, rather than introducing MCJIT it describes how to use ORC, building a custom JIT called KaleidoscopeJIT.
r246002
.
WebAssembly backend implementation work has been continuing over the past few weeks. The individual commits tend to be small and focused (as good commits should be). I mainly wanted to include a mention to highlight how work is ongoing. e.g. this recent commit added support for emitting simple call s-expressions.
r245986
.
The documentation on statepoints now has more to say about base pointers and related assumptions and optimisations.
r246103
.
Constant propagation is enabled for more single precisions math functions, such as acosf, powf, logf.
r246194
.
The function
llvm::splitCodeGen
has been introduced in order to support the implementation of parallel LTO code generation. It uses SplitModule to split the module in to linkable partitions that are distributed among threads to be codegenned.
r246236
.
There's been another change to DebugInfo. DISubprogram definitions must now be marked as distinct. The commit message includes a suggested script for updating IR.
r246327
.
Chandler has been doing some refactoring of the ARM target parsing code with the hope of making it more efficient. He's reduced the cases where the code is called, which has a noticeable effect on some LLVM timings (e.g. check-llvm with non-optimized builds is 15 seconds faster).
r246370
,
r246378
.
Clang commits
A NullabilityChecker has been introduced, which is designed to catch a number of nullability-related issues.
r246105
.
Other project commits
ThreadSanitizer is now enabled for AArch64 with 42-bit virtual addressing on Linux.
r246330
.
libcxx now contains release goals for 3.8 in its TODO.txt. This includes the Filesystem TS and the asynchronous I/O TS.
r245864
.
LLD's ELF linker gained a basic AMDGPU ReaderWriter that enables it to emit binaries that can be consumed by the HSA runtime.
r246155
.
LLD's COFF linker gained support for parallel LTO code generation.
r246342
.
LLDB now supports hardware watchpoints on ARM.
r245961
.
The concept of 'language plugins' was introduced to LLDB. These will provide language-specific data formatters or expression evaluation.
r246212
.
