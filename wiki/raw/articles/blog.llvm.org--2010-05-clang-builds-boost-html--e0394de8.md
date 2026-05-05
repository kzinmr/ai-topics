---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2010/05/clang-builds-boost.html"
fetched_at: 2026-05-05T07:01:44.105947+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2010/05/clang-builds-boost.html

Clang is.
This morning, Clang++ had its first fully-successful Boost regression test run, passing every applicable C++ test on the Boost release branch [*]. According to today's
results
, Clang is successfully compiling more of Boost than other, established compilers for which Boost has historically been tailored (through various workarounds and configuration switches). In fact, Clang's
compiler configuration
in Boost is completely free of any of Boost's C++98/03 defect macros.
