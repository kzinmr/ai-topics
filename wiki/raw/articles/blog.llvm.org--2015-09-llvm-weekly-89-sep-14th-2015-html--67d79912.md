---
title: "LLVM Weekly - #89, Sep 14th 2015"
url: "https://blog.llvm.org/2015/09/llvm-weekly-89-sep-14th-2015.html"
fetched_at: 2026-05-05T07:01:40.037044+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #89, Sep 14th 2015

Source: https://blog.llvm.org/2015/09/llvm-weekly-89-sep-14th-2015.html

LLVM Weekly - #89, Sep 14th 2015
Welcome to the eighty-ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I didn't spot any new LLVM-related articles or news this week. As a reminder, I always welcome tips either via email or Twitter. Seeing as there's nothing new, now seems a good time to point you towards either Stephen Diehl's tutorial on
implementing a JIT compiled language with Haskell and LLVM
or Adrian Sampson's
'LLVM for grad students'
.
On the mailing lists
James Knight is proposing to
deprecate and remove the old SelectionDAG scheduler
, given that machine schedulers are now the preferred approach. He notes that a number of in-tree targets still use the SelectionDAG scheduler. It seems there is
support for this plan
.
Jauhien is curious about the
availability of a C API for the ORC JIT
, with the motivating use case here being to provide a binding for Rust. The
main concern
is that the ORC API is not yet stable, meaning it's not feasible to provide stable C bindings. The proposal is they live in llvm/include/llvm-c/unstable.
Joseph Tremoulet has a whole bunch of questions about addrspacecast semantics, and Chandler Carruth has
a whole bunch of answers
.
David Chisnall has a
useful response
to a question about implementing LLVM intrinsics with multiple return values. As he points out, this is usually done by returning a struct.
LLVM commits
A major modification of LLVM'a alias analysis manager has landed in order to port it to the new pass manager. See the commit message for full details.
r247167
.
The scalar replacement of aggregates (SROA) pass has been ported to the new pass manager. In the commit message, Chandler comments he hopes this serves as a good example of porting a transformation pass with non-trivial state to the new pass manager.
r247501
.
The GlobalsModRef alias analysis pass is now enabled by default.
r247264
.
Emacs users, rest your aching pinky fingers for a moment and rejoice. A range of improvements for the Emacs LLVM IR mode have landed.
r247281
.
The AArch64 backend can now select STNP, the non-temporal store instruction (this hints that the value need not be kept in cache).
r247231
.
Shrink wrapping optimisations are enabled on PPC64.
r247237
.
A whole bunch of StringRef functions have been sprinkled with the
ALWAYS_INLINE
attribute so as to reduce the overhead of string operations even on debug LLVM builds. Chandler has also been making other changes to improve the performance of check-llvm with a debug build.
r247253
.
The LLVM performance tips document has been extended to detail the use of allocas and when to specify alignment.
r247301
.
The
hasLoadLinkedStoreConditional
TargetLoweringInformation callback has now been split in to
bool shouldExpandAtomicCmpXchgInIR(inst)
and
AtomicExpansionKind shouldExpandAtomicLoadInIR(inst)
.
r247429
.
Clang commits
A new control-flow integrity variant has been introduced, indirect function call chacking (enabled with
-fsanitize=cfi-icall
). This checks the dynamic type of the called function matches the static type used at the call.
r247238
.
A new
-analyzer-config
option is available to modify the size of function that the inliner considers as large.
r247463
.
Clang will now try much harder to preserve alignment information during IR-generation.
r246985
.
The
__builtin_nontemporal_store
and
__builtin_nontemporal_load
builtins have been introduced.
r247104
,
r247374
.
Other project commits
libcxx gained implementations of Boyer-Moore and Boyer-Moore-Horspool searchers (for the language fundamentals technical specification).
r247036
.
A trivial dynamic program linked with the new ELF lld now works with musl's dynamic linker.
r247290
.
LLD's COFF linker learned to merge cyclic graphs, which means self-linking now produces a 27.7MB rather than a 29.0MB executable. MSVC manages to produce a 27.1MB executable, so there is still room for improvement.
r247387
.
