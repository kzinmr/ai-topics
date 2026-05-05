---
title: "Closing the gap: cross-language LTO between Rust and C/C++"
url: "https://blog.llvm.org/2019/09/closing-gap-cross-language-lto-between.html"
fetched_at: 2026-05-05T07:01:37.775898+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Closing the gap: cross-language LTO between Rust and C/C++

Source: https://blog.llvm.org/2019/09/closing-gap-cross-language-lto-between.html

Closing the gap: cross-language LTO between Rust and C/C++
By Michael Woerister
Sep 19, 2019
#LTO
10 minute read
Link time optimization (LTO) is LLVM's way of implementing whole-program optimization.
Cross-language
LTO is a new feature in the Rust compiler that enables LLVM's link time optimization to be performed across a mixed C/C++/Rust codebase. It is also a feature that beautifully combines two respective strengths of the Rust programming language and the LLVM compiler platform:
Rust, with its lack of a language runtime and its low-level reach, has an almost unique ability to seamlessly integrate with an existing C/C++ codebase, and
LLVM, as a language agnostic foundation, provides a common ground where the source language a particular piece of code was written in does not matter anymore.
So, what does cross-language LTO do? There are two answers to that:
From a technical perspective it allows for codebases to be optimized without regard for implementation language boundaries, making it possible for important optimizations, such as function inlining, to be performed across individual compilation units even if, for example, one of the compilation units is written in Rust while the other is written in C++.
From a psychological perspective, which arguably is just as important, it helps to alleviate the nagging feeling of inefficiency that many performance conscious developers might have when working on a piece of software that jumps back and forth a lot between functions implemented in different source languages.
Because Firefox is a large, performance sensitive codebase with substantial parts written in Rust, cross-language LTO has been a long-time favorite wish list item among Firefox developers. As a consequence, we at Mozilla's Low Level Tools team took it upon ourselves to implement it in the Rust compiler.
To explain how cross-language LTO works it is useful to take a step back and review how traditional compilation and "regular" link time optimization work in the LLVM world.
Background - A bird's eye view of the LLVM compilation pipeline
Clang and the Rust compiler both follow a similar compilation workflow which, to some degree, is prescribed by LLVM:
The compiler front-end generates an LLVM bitcode module (
.bc
) for each compilation unit. In C and C++ each source file will result in a single compilation unit. In Rust each crate is translated into at least one compilation unit.
.c --clang--> .bc
.c --clang--> .bc
.rs --+
|
.rs --+--rustc--> .bc
|
.rs --+
In the next step, LLVM's optimization pipeline will optimize each LLVM module in isolation:
.c --clang--> .bc --LLVM--> .bc (opt)
.c --clang--> .bc --LLVM--> .bc (opt)
.rs --+
|
.rs --+--rustc--> .bc --LLVM--> .bc (opt)
|
.rs --+
LLVM then lowers each module into machine code so that we get one object file per module:
.c --clang--> .bc --LLVM--> .bc (opt) --LLVM--> .o
.c --clang--> .bc --LLVM--> .bc (opt) --LLVM--> .o
.rs --+
|
.rs --+--rustc--> .bc --LLVM--> .bc (opt) --LLVM--> .o
|
.rs --+
Finally, the linker will take the set of object files and link them together into a binary:
.c --clang--> .bc --LLVM--> .bc (opt) --LLVM--> .o ------+
|
.c --clang--> .bc --LLVM--> .bc (opt) --LLVM--> .o ------+
|
+--ld--> bin
.rs --+                                                  |
|                                                  |
.rs --+--rustc--> .bc --LLVM--> .bc (opt) --LLVM--> .o --+
|
.rs --+
This is the regular compilation workflow if no kind of LTO is involved. As you can see, each compilation unit is optimized in isolation. The optimizer does not know the definition of functions inside of other compilation units and thus cannot inline them or make other kinds of decisions based on what they actually do. To enable inlining and optimizations to happen across compilation unit boundaries, LLVM supports link time optimization.
Link time optimization in LLVM
The basic principle behind LTO is that some of LLVM's optimization passes are pushed back to the linking stage. Why the linking stage? Because that is the point in the pipeline where the entire program (i.e. the whole set of compilation units) is available at once and thus optimizations across compilation unit boundaries become possible. Performing LLVM work at the linking stage is facilitated via a
plugin
to the linker.
Here is how LTO is concretely implemented:
the compiler translates each compilation unit into LLVM bitcode (i.e. it skips lowering to machine code),
the linker, via the LLVM linker plugin, knows how to read LLVM bitcode modules like regular object files, and
the linker, again via the LLVM linker plugin, merges all bitcode modules it encounters and then runs LLVM optimization passes before doing the actual linking.
With these capabilities in place a new compilation workflow with LTO enabled for C++ code looks like this:
.c --clang--> .bc --LLVM--> .bc (opt) ------------------+ - - +
|     |
.c --clang--> .bc --LLVM--> .bc (opt) ------------------+ - - +
|     |
+-ld+LLVM--> bin
.rs --+                                                 |
|                                                 |
.rs --+--rustc--> .bc --LLVM--> .bc (opt) --LLVM--> .o -+
|
.rs --+
As you can see our Rust code is still compiled to a regular object file. Therefore, the Rust code is opaque to the optimization taking place at link time. Yet, looking at the diagram it seems like that shouldn't be too hard to change, right?
Cross-language link time optimization
Implementing cross-language LTO is conceptually simple because the feature is built on the shoulders of giants. Since the Rust compiler uses LLVM all the important building blocks are readily available. The final diagram looks very much as you would expect, with
rustc
emitting optimized LLVM bitcode and the LLVM linker plugin incorporating that into the LTO process with the rest of the modules:
.c --clang--> .bc --LLVM--> .bc (opt) ---------+
|
.c --clang--> .bc --LLVM--> .bc (opt) ---------+
|
+-ld+LLVM--> bin
.rs --+                                        |
|                                        |
.rs --+--rustc--> .bc --LLVM--> .bc (opt) -----+
|
.rs --+
Nonetheless, achieving a production-ready implementation still turned out to be a significant time investment. After figuring out how everything fits together, the main challenge was to get the Rust compiler to produce LLVM bitcode that was compatible with both the bitcode that Clang produces and with what the linker plugin would accept. Some of the issues we ran into where:
The Rust compiler and Clang are both based on LLVM but they might be using different versions of LLVM. This was further complicated by the fact that Rust's LLVM version often does not match a specific LLVM release, but can be an arbitrary revision from LLVM's repository. We learned that all LLVM versions involved really have to be a close match in order for things to work out. The Rust compiler's documentation now offers a
compatibility table
for the various versions of Rust and Clang.
The Rust compiler by default performs a special form of LTO, called
ThinLTO
, on all compilation units of the same crate before passing them on to the linker. We quickly learned, however, that the LLVM linker plugin crashes with a segmentation fault when trying to perform another round of ThinLTO on a module that had already gone through the process. No problem, we thought and instructed the Rust compiler to disable its own ThinLTO pass when compiling for the cross-language case and indeed everything was fine -- until the segmentation faults mysteriously returned a few weeks later even though ThinLTO was still disabled.
We noticed that the problem only occurred in a specific, presumably innocent setting: again two passes of LTO needed to happen, this time the first was a
regular LTO
pass within
rustc
and the output of that would then be fed into ThinLTO within the linker plugin. This setup, although computationally expensive, was desirable because it produced faster code and allowed for better dead-code elimination on the Rust side. And in theory it should have worked just fine. Yet somehow
rustc
produced symbol names that had apparently gone through ThinLTO's mangling even though we checked time and again that ThinLTO was disabled for Rust. We were beginning to seriously question our understanding of LLVM's inner workings as the problem persisted while we slowly ran out of ideas on how to debug this further.
You can picture the proverbial lightbulb appearing over our heads when we figured out that Rust's pre-compiled standard library would still have ThinLTO enabled, no matter the compiler settings we were using for our tests. The standard library, including its LLVM bitcode representation, is compiled as part of Rust's binary distribution so it is always compiled with the settings from Rust's build servers. Our local full LTO pass within
rustc
would then pull this troublesome bitcode into the output module which in turn would make the linker plugin crash again. Since then ThinLTO is
turned off
for
libstd
by default.
After the above fixes, we succeeded in compiling the entirety of Firefox with cross-language LTO enabled. Unfortunately, we discovered that no actual cross-language optimizations were happening. Both Clang and
rustc
were producing LLVM bitcode and LLD produced functioning Firefox binaries, but when looking at the machine code, not even trivial functions were being inlined across language boundaries. After days of debugging (and unfortunately without being aware of
LLVM's optimization remarks
at the time) it turned out that Clang was emitting a
target-cpu
attribute on all functions while
rustc
didn't, which made LLVM reject inlining opportunities.
In order to prevent the feature from silently regressing for similar reasons in the future we put quite a bit of effort into extending the Rust compiler's testing framework and CI. It is now able to compile and run a compatible version of Clang and uses that to perform end-to-end tests of cross-language LTO, making sure that small functions will indeed get inlined across language boundaries.
This list could still go on for a while, with each additional target platform holding new surprises to be dealt with. We had to progress carefully by putting in regression tests at every step in order to keep the many moving parts in check. At this point, however, we feel confident in the underlying implementation, with Firefox providing a large, complex, multi-platform test case where things have been working well for several months now.
Using cross-language LTO: a minimal example
The exact build tool invocations differ depending on whether it is
rustc
or Clang performing the final linking step, and whether Rust code is compiled via Cargo or via
rustc
directly. Rust's
compiler documentation
describes the various cases. The simplest of them, where
rustc
directly produces a static library and Clang does the linking, looks as follows:
# Compile the Rust static library, called "xyz"
rustc --crate-type=staticlib -O -C linker-plugin-lto -o libxyz.a lib.rs
# Compile the C code with "-flto"
clang -flto -c -O2 main.c
# Link everything
clang -flto -O2 main.o -L . -lxyz
The
-C linker-plugin-lto
option instructs the Rust compiler to emit LLVM bitcode which then can be used for both "full" and "thin" LTO. Getting things set up for the first time can be quite cumbersome because, as already mentioned, all compilers and the linker involved must be compatible versions. In theory, most major linkers will work; in practice LLD seems to be the most reliable one on Linux, with Gold in second place and the BFD linker needing to be at least version 2.32. On Windows and macOS the only linkers properly tested are LLD and
ld64
respectively. For
ld64
Firefox uses a patched version because the LLVM bitcode that
rustc
produces likes to trigger a
pre-existing issue
this linker has with ThinLTO.
Conclusion
Cross-language LTO has been enabled for Firefox release builds on Windows, macOS, and Linux for several months at this point and we at Mozilla's Low Level Tools team are pleased with how it turned out. While we still
need to work
on making the initial setup of the feature easier, it already enabled removing duplicated logic from Rust components in Firefox because now code can simply call into the equivalent C++ implementation and rely on those calls to be inlined. Having cross-language LTO in place and continuously tested will definitely lower the psychological bar for implementing new components in Rust, even if they are tightly integrated with existing C++ code.
Cross-language LTO is available in the Rust compiler since version 1.34 and works together with Clang 8. Feel free to give it a try and report any problems in the Rust
bug tracker
.
Acknowledgments
I'd like to thank my Low Level Tools team colleagues David Major, Eric Rahm, and Nathan Froyd for their invaluable help and encouragement, and I'd like to thank Alex Crichton for his tireless reviews on the Rust side.
