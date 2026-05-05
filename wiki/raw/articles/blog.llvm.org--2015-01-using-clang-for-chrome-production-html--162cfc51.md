---
title: "Using clang for Chrome production builds on Linux"
url: "https://blog.llvm.org/2015/01/using-clang-for-chrome-production.html"
fetched_at: 2026-05-05T07:01:41.159287+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Using clang for Chrome production builds on Linux

Source: https://blog.llvm.org/2015/01/using-clang-for-chrome-production.html

Chrome 38 was released early October 2014. It is the first release where the Linux binaries shipped to users are built by clang. Previously, this was done by gcc 4.6. As you can read in the
announcement email
, the switch happened without many issues. Performance stayed roughly the same, binary size decreased by about 8%. In this post I'd like to discuss the motivation for this switch.
Motivation
There are two reasons for the switch.
1. Many Chromium developers already used clang on Linux. We've supported
opting in
to clang for since
before clang supported C++
– because of this, we have a process in place for shipping new clang binaries to all developers and bots every few weeks. Because of clang's good diagnostics (
some
of
which
we
added
due to bugs in Chromium we thought the compiler should catch), speed, and because of our
Chromium-specific clang plugin
, many Chromium developers switched to clang over the years. Making clang the default compiler removes a stumbling block for people new to the project.
2. We want to use modern C++ features in Chromium. This requires a recent toolchain – we figured we needed at least gcc 4.8. For Chrome for Android and Chrome for Chrome OS, we updated our gcc compilers to 4.8 (and then 4.9) – easy since these ports use a non-system gcc already. Chrome for Mac has been using Chromium's clang since Chrome 15 and was already in a good state. Chrome for iOS uses Xcode 5's clang, which is also new enough. Chrome for Windows uses Visual Studio 2013 Update 4. On Linux, switching to clang was the easiest way forward.
Keeping up with C++'s evolution in a large, multi-platform project
C++ had been static for many years. C++11 is the first real update to the C++ language since the original C++ standard (approved on July 27 1998). C++98 predated the founding of Google, YouTube, Facebook, Twitter, the releases of Mac OS X and Windows XP, and x86 SSE instructions. The time between the two standards saw the rise and fall of the iPod, several waves of social networks, and the smartphone explosion.
The time between C++11 and C++14 was three years, and the next major iteration of the language is speculated to be finished in 2017, three years from C++14. This is a dramatic change, and it has repercussions on how to build and ship C++ programs. It took us 3+ years to get to a state where we can use C++11 in Chromium; C++14 will hopefully take us less long. (If you're targeting fewer platforms, you'll have an easier time.)
There are two parts to C++11: New language features, and new library features. The language features just require a modern compiler at build time on build machines, the library features need a new standard library at runtime on the user's machine.
Deploying a new compiler is conceptually relatively simple. If your developers are on Ubuntu LTS releases and you make them use the newest LTS release, they get new compilers every two years – so just using the default system compiler means you're up to two years behind. There needs to be some process to relatively transparently deploy new toolchains to your developers – an "evergreen compiler". We now have this in place for Chromium – on Linux, by using clang. (We still accept patches to keep Chromium buildable with gccs >= 4.8 for people who prefer compiling locally over using precompiled binaries, and we still use gcc as the target compiler for Chrome for Android and Chrome OS.)
The library situation is slightly more tricky: On Linux and Mac OS X, programs are usually linked against the system C++ library. Chrome wants to support Mac OS X 10.6 a bit longer (our users seem to love this OS X release), and the only C++ library this ships with is libstdc++ 4.2 – which doesn't have any C++11 bits. Similarly, Ubuntu Precise only has libstdc++ 4.6. It seems that with C++ updating more often, products will have to either stop supporting older OS versions (even if they still have many users on these old versions), adopt new C++ features very slowly, or ship with a bundled C++ standard library. The latter implies that system libraries shouldn't have a C++ interface for ABI reasons – luckily, this is mostly already the case.
To make things slightly more complicated, gcc and libstdc++ expect to be updated at the same time. gcc 4.8 links to libstdc++ 4.8, so upgrading gcc 4.8 while still linking to Precise's libstdc++ 4.6 isn't easy. clang
explicitly supports
building with older libstdc++ versions.
For Chromium, we opted to enable C++11 language features now, and then allow C++11 library features later once we have figured out the story there. This allows us to
incrementally adopt
C++11 features in Chromium
, but it's not without risks:
vector<int> v0{42}
for example means something different with an old C++ library and a new C++ library that has a
vector
constructor taking an
initializer_list
. We disallow using uniform initialization for now because of this.
Since bundling a C++ library seems to become more common with this new C++ update cadence, it would be nice if compiler drivers helped with this. Just statically linking libstdc++ / libc++ isn't enough if you're shipping a product consisting of several executables or shared libraries – they need to dynamically link to a shared C++ library with the right rpaths, the C++ library probably needs mangled symbol names that don't conflict with the system C++ library which might be loaded into the same process due to other system libraries using it internally (for example, maybe using an inline namespace with an application-specific name), etc.
Future directions
As mentioned above, we're trying to figure out the C++ library situation. The tricky cases are Chrome for Android (which currently uses STLport) and Chrome for Mac. We're hoping to switch Chrome for Android to libc++ (while still using gcc as compiler). On Mac, we'll likely bundle libc++ with Chrome too.
We're
working
on
making clang
usable
for compiling Chrome for Windows. The main motivations for this are using
AddressSanitizer
, providing a compiler with great diagnostics for developers, and getting our
tooling infrastructure
working on Windows (used for example
automated large-scale cross-OS refactoring
and for building our
code search index
– try clicking a few class names; at the moment only code built on Linux is hyperlinked). We won't use clang as a production compiler on Windows unless it produces a chrome binary that's competitive with Visual Studio's on both binary size and performance. (From an open-source perspective, it
is
nice being able to use an open-source compiler to compile an open-source program.)
You can reach us at clang@chromium.org
