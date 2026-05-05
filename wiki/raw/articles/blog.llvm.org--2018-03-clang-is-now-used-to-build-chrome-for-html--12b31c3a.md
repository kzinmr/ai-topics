---
title: "Clang is now used to build Chrome for Windows"
url: "https://blog.llvm.org/2018/03/clang-is-now-used-to-build-chrome-for.html"
fetched_at: 2026-05-05T07:01:38.087071+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Clang is now used to build Chrome for Windows

Source: https://blog.llvm.org/2018/03/clang-is-now-used-to-build-chrome-for.html

As of Chrome 64, Chrome for Windows is compiled with Clang. We now use Clang to build Chrome for all platforms it runs on: macOS, iOS, Linux, Chrome OS, Android, and Windows. Windows is the platform with the second most Chrome users after Android
according to statcounter
, which made this switch particularly exciting.
Clang is the first-ever open-source C++ compiler that’s ABI-compatible with Microsoft Visual C++ (MSVC) – meaning you can build some parts of your program (for example, system libraries) with the MSVC compiler (“cl.exe”), other parts with Clang, and when linked together (either by MSVC’s linker, “link.exe”, or LLD, the LLVM project’s linker – see below) the parts will form a working program.
Note that Clang is not a replacement for Visual Studio, but an addition to it. We still use Microsoft’s headers and libraries to build Chrome, we still use some SDK binaries like midl.exe and mc.exe, and many Chrome/Win developers still use the Visual Studio IDE (for both development and for debugging).
This post discusses numbers, motivation, benefits and drawbacks of using Clang instead of MSVC, how to try out Clang for Windows yourself, project history, and next steps. For more information on the technical side you can look at the
slides of our 2015 LLVM conference talk
, and the slides linked from there.
Numbers
This is what most people ask about first, so let’s talk about it first. We think the other sections are more interesting though.
Build time
Building Chrome locally with Clang is about 15% slower than with MSVC. (We’ve heard that Windows Defender can make Clang builds a lot slower on some machines, so if you’re seeing larger slowdowns, make sure to whitelist Clang in Windows Defender.) However, the way Clang emits debug info is more parallelizable and builds with a distributed build service (e.g.
Goma
) are hence faster.
Binary size
Chrome installer size gets smaller for 64-bit builds and slightly larger for 32-bit builds using Clang. The same difference shows in uncompressed code size for regular builds as well (see the
tracking bug for Clang binary size
for many numbers). However, compared to MSVC builds using link-time code generation (LTCG) and
profile-guided optimization
(PGO) Clang generates larger code in 64-bit for targets that use /O2 but smaller code for targets that use /Os. The installer size comparison suggests Clang's output compresses better.
Some raw numbers for versions 64.0.3278.2 (MSVC PGO) and 64.0.3278.0 (Clang). mini_installer.exe is Chrome’s installer that users download, containing the LZMA-compressed code. chrome_child.dll is one of the two main dlls; it contains Blink and V8, and generally has many targets that are built with /O2. chrome.dll is the other main dll, containing the browser process code, mostly built with /Os.
mini_installer.exe
chrome.dll
chrome_child.dll
chrome.exe
32-bit win-pgo
45.46 MB
36.47 MB
53.76 MB
1.38 MB
32-bit win-clang
45.65 MB
(+0.04%)
42.56 MB (+16.7%)
62.38 MB
(+16%)
1.45 MB
(+5.1%)
64-bit win-pgo
49.4 MB
53.3 MB
65.6 MB
1.6 MB
64-bit win-clang
46.27 MB
(-6.33%)
50.6 MB
(-5.1%)
72.71 MB
(+10.8%)
1.57 MB
(-1.2%)
Performance
We conducted extensive A/B testing of performance. Performance telemetry numbers are about the same for MSVC-built and clang-built Chrome – some metrics get better, some get worse, but all of them are within 5% of each other. The official MSVC builds used LTCG and PGO, while the Clang builds currently use neither of these. This is potential for improvement that we look forward to exploring. The PGO builds took a very long time to build due to the need for collecting profiles and then building again, and as a result, the configuration was not enabled on our performance-measurement buildbots. Now that we use Clang, the perf bots again track the configuration that we ship.
Startup performance was worse in Clang-built Chrome until we started using a
link-order file
– a form of “PGO light” .
Stability
We A/B-tested stability as well and found no difference between the two build configurations.
Motivation
There were many motivating reasons for this project, the overarching theme being the benefits of using the same compiler across all of Chrome’s platforms, as well as the ability to change the compiler and deploy those changes to all our developers and buildbots quickly. Here’s a non-exhaustive list of examples.
Chrome is heavily using technology that’s based on compiler instrumentation (ASan, CFI,
ClusterFuzz
—uses ASan). Clang supports this instrumentation already, but we can’t add it to MSVC. We previously used
after-the-fact binary instrumentation
to mitigate this a bit, but having the toolchain write the right bits in the first place is cleaner and faster.
Clang enables us to write compiler
plugins
that add Chromium-specific warnings and to write tooling for
large-scale refactoring
.
Chromium’s code search
can now learn to index Windows code.
Chromium is open-source, so it’s nice if it’s built with an open-source toolchain.
Chrome runs on 6+ platforms, and most developers are only familiar with 1-3 platforms. If your patch doesn’t compile on a platform you’re unfamiliar with, due to a compiler error that you can’t locally reproduce on your local development machine, it’ll take you a while to fix. On the other hand, if all platforms use the same compiler, if it builds on your machine then it’s probably going to build on all platforms.
Using the same compiler also means that compiler-specific micro-optimizations will help on all platforms (assuming that the same -O flags are used on all platforms – not yet the case in Chrome, and only on the same ISAs – x86 vs ARM will stay different).
Using the same compiler enables
cross-compiling
– developers who feel most at home on a Linux box can now work on Windows-specific code, from their Linux box (without needing to run Wine).
We can
continuously build Chrome trunk with Clang trunk
to find compiler regressions quickly. This allows us to update Clang every week or two. Landing a major MSVC update in Chrome usually took a year or more, with several rounds of reporting internal compiler bugs and miscompiles. The issue here isn’t that MSVC is more buggy than Clang – it isn’t, all software is buggy – but that we can continuously improve Clang due to Clang being open-source.
C++ receives major new revisions every few years. When C++11 was released, we were still using six different compilers, and
enabling C++11
was difficult. With fewer compilers, this gets much easier.
We can prioritize compiler features that are important to us. For example:
Of course, not all – or even most – of these reasons will apply to other projects.
Benefits and drawbacks of using Clang instead of Visual C++
Benefits of using Clang, if you want to try for your project:
Clang supports 64-bit inline assembly. For example, in Chrome we built libyuv (a video format conversion library) with Clang long before we built all of Chrome with it. libyuv had highly-tuned 64-bit inline assembly with performance not reachable with intrinsics, and we could just use that code on Windows.
If your project runs on multiple platforms, you can use one compiler everywhere. Building your project with several compilers is generally considered good for code health, but in Chrome we found that Clang’s diagnostics found most problems and we were mostly battling compiler bugs (and if another compiler has a great new diagnostic, we can add that to Clang).
Likewise, if your project is Windows-only, you can get a second compiler’s opinion on your code, and Clang’s warnings might find bugs.
You can use
Address Sanitizer
to find memory bugs.
If you don’t use LTCG and PGO, it’s possible that Clang might create faster code.
Clang’s
diagnostics and fix-it hints
.
There are also drawbacks:
Clang doesn’t support C++/CX or #import “foo.dll”.
MSVC offers paid support, Clang only gives you the code and the ability to write patches yourself (although the community is very active and helpful!).
MSVC has better documentation.
Advanced debugging features such as Edit & Continue don’t work when using Clang.
How to use
If you want to give Clang for Windows a try, there are two approaches:
You could use clang-cl, a compiler driver that tries to be command-line flag compatible with cl.exe (just like Clang tries to be command-line flag compatible with gcc). The
Clang user manual
describes how you can tell popular Windows build systems how to call clang-cl instead of cl.exe. We used this approach in Chrome to keep the Clang/Win build working alongside the MSVC build for years, with minimal maintenance cost. You can keep using link.exe, all your current compile flags, the MSVC debugger or windbg, ETW, etc. clang-cl even writes warning messages in a format that’s compatible with cl.exe so that you can click on build error messages in Visual Studio to jump to the right file and line. Everything should just work.
Alternatively, if you have a cross-platform project and want to use gcc-style flags for your Windows build, you can pass a Windows triple (e.g. --target=x86_64-windows-msvc) to regular Clang, and it will produce MSVC-ABI-compatible output. Starting in Clang 7.0.0, due Fall 2018, Clang will also default to CodeView debug info with this triple.
Since Clang’s output is ABI-compatible with MSVC, you can build parts of your project with clang and other parts with MSVC. You can also pass
/fallback
to clang-cl to make it call cl.exe on files it can’t yet compile (this should be rare; it never happens in the Chrome build).
clang-cl accepts Microsoft language extensions needed to parse system headers but tries to emit -Wmicrosoft-foo warnings when it does so (warnings are ignored for system headers). You can choose to fix your code, or pass -Wno-microsoft-foo to Clang.
link.exe can produce regular PDB files from the CodeView information that Clang writes.
Project History
We switched chrome/mac and
chrome/linux
to Clang a while ago. But on Windows, Clang was still missing support for parsing many Microsoft language extensions, and it didn’t have any Microsoft C++ ABI-compatible codegen at all. In 2013, we
spun up a team
to improve Clang’s Windows support, consisting half of Chrome engineers with a compiler background and half of other toolchain people. In mid-2014, Clang could
self-host on Windows
. In February 2015, we had the first fallback-free build of 64-bit Chrome, in July 2015 the first fallback-free build of 32-bit Chrome (32-bit SEH was difficult). In Oct 2015, we shipped a first clang-built Chrome to the Canary channel. Since then, we’ve worked on
improving the size of Clang’s output
,
improved Clang’s debug information
(some of it behind -instcombine-lower-dbg-declare=0 for now), and A/B-tested stability and telemetry performance metrics.
We use versions of Clang that are pinned to a recent upstream revision that we update every one to three weeks, without any local patches. All our work is done in upstream LLVM.
Mid-2015, Microsoft announced that they were building on top of our work of making Clang able to parse all the Microsoft SDK headers with
clang/c2
, which used the Clang frontend for parsing code, but cl.exe’s codegen to generate code.
Development on clang/c2 was halted again
in mid-2017; it is conceivable that this was related to our improvements to MSVC-ABI-compatible Clang codegen quality. We’re thankful to Microsoft for publishing documentation on the PDB file format, answering many of our questions, fixing Clang compatibility issues in their SDKs, and for giving us publicity on their blog! Again, Clang is not a replacement for MSVC, but a complement to it.
Opera for Windows is also
compiled with Clang
starting in version 51.
Firefox is also looking at
using clang-cl for building Firefox for Windows
.
Next Steps
Just as clang-cl is a cl.exe-compatible interface for Clang, lld-link is a link.exe-compatible interface for lld, the LLVM linker. Our next step is to use lld-link as an alternative to link.exe for linking Chrome for Windows. This has many of the same advantages as clang-cl (open-source, easy to update, …). Also, using clang-cl together with lld-link allows using
LLVM-bitcode-based LTO
(which in turn enables using
CFI
) and
using PE/COFF extensions to speed up linking
. A prerequisite for using lld-link was
its ability to write PDB files
.
We’re also considering using libc++ instead of the MSVC STL – this allows us to instrument the standard library, which is again useful for CFI and Address Sanitizer.
In Closing
Thanks to the whole LLVM community for helping to create the first new production C++ compiler for Windows in over a decade, and the first-ever open-source C++ compiler that’s ABI-compatible with MSVC!
