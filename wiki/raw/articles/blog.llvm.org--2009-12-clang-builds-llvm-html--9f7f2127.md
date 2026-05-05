---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2009/12/clang-builds-llvm.html"
fetched_at: 2026-05-05T07:01:44.328166+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2009/12/clang-builds-llvm.html

Clang Builds LLVM
By Doug Gregor
Dec 24, 2009
#C++
,
#Clang
One minute read
Just in time for the Christmas holiday, the Clang project has hit a major milestone: Clang can now build all of LLVM and Clang!
The resulting Clang-built-Clang is not yet functional, so this "self-build" milestone is well short of full self-hosting. However, self-building indicates that C++ parsing, semantic analysis, and code generation is solid enough to compile the entirety of LLVM (~350k lines of C++ code) and Clang (~200k lines of C++ code) and produce object files that link together properly. To get to this point, we've fixed many bugs in Clang (when compiling C++ code), but also several bugs in LLVM and Clang that were found by Clang itself.
We are tracking
a number of Clang bugs
that manifest when building LLVM and Clang, as we make our way to the next big milestone: full self-hosting of Clang!
