---
title: "LLVM Weekly - #29, Jul 21st 2014"
url: "https://blog.llvm.org/2014/07/llvm-weekly-29-jul-21st-2014.html"
fetched_at: 2026-05-05T07:01:41.850910+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #29, Jul 21st 2014

Source: https://blog.llvm.org/2014/07/llvm-weekly-29-jul-21st-2014.html

LLVM Weekly - #29, Jul 21st 2014
Welcome to the twenty-ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects.LLVM Weekly is brought to you by
Alex Bradbury
.Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or
@llvmweekly
or
@asbradbury
on Twitter.
This is a special extended issue which I'm choosing to subtitle "LLVM Weekly visits the GNU Tools Cauldron". The
event
took place over the weekend and had a wide range of interesting talks. You can find my notes at the end of this newsletter. Talks were recorded and the videos should be made available in the next month or two.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The eighth annual LLVM Developers meeting has been
announced
and will take place on October 28th and 29th in San Jose, CA. It is looking for sponsors and talk/poster submissions.
A new blog post as been published on the LLVM Blog giving
more details on FTL: WebKit's LLVM-based JIT
.
A tentative
schedule for the release of LLVM/Clang 3.5
has been posted.
Botond Ballo has posted a
summary of June's C++ Standards Committee Meeting
.
On the mailing lists
LLVM commits
A dereferenceable attribute was added. This indicates that the parameter or return pointer is dereferenceable (i.e. can be loaded from speculatively without a risk of trapping). This is subtly different to the nonnull attribute which doesn't necessarily imply dereferenceability (you might for instance have a pointer to one element past the end of an array).
r213385
.
A new subtarget hook was added to allow targets to opt-out of register coalescing.
r213078
,
r213188
.
A MergedLoadStoreMotion pass was added.
r213396
.
RegionInfo has been templatified to it works on MachineBasicBlocks.
r213456
.
A monster patch from Nvidia adds a whole bunch of surface/texture intrinsics to the NVPTX backend.
r213256
.
Support was added for emitting warnings if vectorization is forced and fails.
r213110
.
Improvements to FastISel continue with the implementation of the FastLowerCall hook for X86. This actually reproduces what was already being done in X86, but is refactored against the target independent call lowering.
r213049
.
The ARM dmb, dsb and isb intrinsics have been implemented for AARch64.
r213247
.
Clang commits
Clang's rewrite engine is now a core feature (i.e. it can not be disabled at configure time).
r213171
.
Error recovery when the programmer mistypes
::
as
:
was improved.
r213120
.
The AARch64 Clang CLI interface proposal for
-march
has been implemented. See the commit message for details.
r213353
.
OpenMP work continues with the addition of initial parsing and semantic analysis for the
final
,
untied
and other clauses, and the
master
directive.
r213232
,
r213257
,
r213237
, and more.
Other project commits
The 'Kalimba' platform is now supported by lldb (presumably this refers to the CSR processor).
r213158
.
LLVM Weekly at the GNU Tools Cauldron
For full details on the conference and details on the speakers for the talks I've summarised below see the
GNU Tools Cauldron 2014 web page
. Apologies for any inaccuracies, please do get in touch if you spot anything I may have noted incorrectly. LLVM followers may be particularly interested in Renato Golin's talk on collaboration between the GCC and LLVM communities.
Glibc BoF
2.20 is in "slushy" freeze mode. What else is left? fmemopen, fd locking, some
-Wundef
work
Anyone planning to check in something big for 2.21?
Mentor Graphics planning to check in a NIOS II port. They won't be accepted until Linux kernel patches are in a kernel release.
A desire for AArch64 ILP32 ABI to get in. Kernel patches currently in review, compiler work is ready.
OpenRISC
NaCl (nptl)
Benchmarking glibc? Does anyone have a good approach. There is a preload library approach (see notes from Ondrej's talk).
Glibc has been built with AddressSanitizer, help needed to get it integrated into the build system. There was a comment this would be nice to get in to distributions.
Red Hat are working on supporting alternate libm implementations, including a low-precision and high-precision implementation. Intel are looking to add math functions that work on small vectors.
Abigail: toward ABI taming
Want to determine if changes to your shared library break apps for users, and users want to know whether an updated library remains compatible with their code. The bidiff tool will tell you the differences in terms of ABI given two object files as its input.
libabi consists of modules such as a DWARF reader, the comparison engine. Tools such as bidiff are built on this API
What's next for libabigail?
bicompat will help application authors determine whether their application A is still compatibile with an updated version of a given library L by examining the undefined symbols of A that are resolved by L.
More amenable to automation (such as integration into build systems)
Support for un-instantiated templates. This would require declarations of uninstantiated templates to be represented in DWARF.
A first official release (though source is available at
https://sourceware.org/libabigail/
)
Writing VMs in Java and debugging them with GDB
Oracle Labs have been working on various dynamic language implementations in Java (e.g. Ruby, Python, R, JS, ...).
FastR is a reimplementation of R in Java featuring an interpreter (Truffle) and dynamic compiler (Graal).
Truffle and Graal starts with an AST interpreter. The first time a node is evaluated it is specialised to the type that was seen at runtime. Later the tree is compiled using partial evaluation.
It may be deployed on standard HotSpot (no compilation), GraalVM, or the SubstrateVM (SVM) which uses Graal to ahead-of-time compile the language implementation. Debugging the SVM is difficult as Java debugging tools are not available. The solution is to generate DWARF information in the SVM's output.
Truffle and Graal are open source, the SubstrateVM is not (yet?).
GCC and LLVM collaboration
Good news: license issues, personal grudges and performance are off-topic.
Users should be protected from whatever disagreements take place. In the future we should have more pro-active discussions on various issues as opposed to reactive discussions regarding e.g. compiler flags that have been noticed to be arbitrarily different after the fact.
Renato lists common projects that we may collaborate on: binutils, glibc, sanitizers. Sanitizers are a collaboration success story.
Can we agree on a (new?) common user interface?
There's a surprising amount of confusion about
-march
,
-mtune
, and
-mcpu
considering we're in a room of compiler developers. It sounds like there's not much support for re-engineering the set of compiler flags as the potential gain is not seen as being great enough.
Can we agree to standardise on attributes, C/C++ extensions, builtins, ASM, the linker API?
GCC docs have just been rewritten, so some criticisms about how difficult it is to dig in are no longer valid.
Machine Guided Energy Efficient Compilation
Initial investigations in 2012 found that compiler flags can have a meaningful effect on energy consumption. This raises the question of how to determine which flags to use.
MAGEEC will target both GCC and LLVM initially. It is implemented as a compiler plugin which performs feature extraction and allows the output of the machine learning algorithm to change the sequence of passes which are run. Fractional Factorial Design is used to reduce the optimisation space to explore.
Turning passes on/off arbitrarily can often result in internal compiler errors. Should the machine learning algorithm learn this, or should GCC better document pass requirements?
It would be useful to MAGEEC if the (currently internal) plugin API could be stabilized. They also currently have to use a hacked up Clang as it doesn't provide plugin hooks.
The project has produced a low cost energy measurement board as well as their own benchmark suite (Bristol/Embecosm Embedded Benchmark Suite, or BEEBS). BEEBS 2.0 is schedule for release by 31st August 2014 with a much wider range of benchmarks (currently 93). Jeremy showed a rather pleasing live demo where you can run a benchmark on a microcontroller development board and immediately find the number of mJ consumed in running it.
The current state of the project has it not achieving better results than GCC O2, but this is expected to change over the coming months.
Just-in-time compilation using GCC
libgccjit.so
is an experimental branch of GCC which allows you to build GCC as a shared library and embed it in other programs in order to allow in-process code generation at runtime.
A dedicated API for JIT will allow better stability guarantees. It provides a high-level API designed for ease of use.
The API doesn't offer solutions for type inference, escape analysis, unboxing, inline caching, etc.
It has a C++ API wich includes some cunning operator overloading to massively reduce verbosity, and a Python API.
David Malcolm has written
Coconut
, a JIT compiler for Python using libgccjit.so. It is incomplete and experimental.
Drawback: currently have to write out a .s to a file and invoke gcc on it.
Some might make a cheeky comment about the benefits of architecting a compiler so it can be used as a library, but I of course wouldn't dare. The good news is the speaker is actively looking at what would be needed to use GAS and GNU ld as a library.
Introduction to new Intel SIMD ISA and its impact on GCC
AVX-512 offers 64 simple precision or 32 double precision floating point operations per cycle. It also has 8x64-bit mask registers.
Rounding modes can be set on a per-instruction process
Basic support is available from GCC 4.9.x.
News from Sanitizers
MemorySanitizer detects use of uninitialized memory. Increases CPU by about 2.5x and RAM by 2x. Was released in LLVM in 2013. It is currently Linux/x86-64 only.
History growth is limited by limiting the history depth and the number of new history nodes per stack trace.
MSan has found hundreds of bugs across Google internal code, Chromium, LLVM, etc. It was more challenging for Chromium due to the number of system libs that had to be rebuilt.
AddressSanitizer annotations allows you to detect access to the regions of e.g.
std::vector<>
which has been allocated as part of its capacity but not yet been used (i.e. will start to be used in the next
push_back
). Next is to do the same for
std::string
and
std::deque
.
Glibc uses GNU-C instead of ANSI C which currently prevents compilation with Clang (nested functions in particular are problematic). It can however be built with ASan by GCC.
Evgeniy comments that the lack of standardisation between Clang and GCC for things like
__has_feature(address_sanitizer)
vs
__SANITIZE_ADDRESS__
is irritating. This is just the sort of thing Renato was talking about yesterday of course.
glibc performance tuning
Use memset as an example. Look at 3 variants.
Writing a useful benchmark is more difficult than you might think. Simply running
memset
many times in a loop is not a good benchmark when using the same memory locations due to the processor's load-store forwarding. Even when fixing this, the branch predictor may perform much better than it would when memset is used in a real world scenario and lead to unrepresentative results.
To move beyond microbenchmarks, Ondrej has been using
LD_PRELOAD
to link against instrumented versions of the functions which record details about the time taken.
See
here
for memset benchmarks and
here
for more background.
strcmp was the most frequently called glibc function in Ondrej's testing (when running Firefox).
Devirtualization in GCC
This is a special case of indirect call removal, and although the talk is given in the context of C++ the techniques apply to other languages too. Some basic cases are handled in the front-end and even specified by the language standard.
It is a special case of constant propagation across aggregates, which is already done by Global Value Numbering and Interprocedural Constant Propagation. But these passes only catch a tiny number of possible cases.
Loss of information between the frontend and middle end can make some cases almost impossible. The intermediate language can be extended with explicit representations of base types, locations of virtual table pointers, and vtables. Also annotate polymorphic calls specifying instance and polymorphic call type and flags to denote constructors/destructors.
I'm not able to summarise details on the GCC devirt implementation better than the slides do. Hopefully they'll be made available online.
A particular challenge is to match types between different compilation units. The C++ One Definition Rule is used.
It can be used to strengthen unreachable function removal.
Feedback-directed devirtualization was extended in GCC 4.9 to work inter-module with LTO.
