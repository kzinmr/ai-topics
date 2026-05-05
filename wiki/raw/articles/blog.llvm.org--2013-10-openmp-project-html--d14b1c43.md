---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2013/10/openmp-project.html"
fetched_at: 2026-05-05T07:01:42.988529+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2013/10/openmp-project.html

I am extremely glad to announce that Intel has decided to provide a copy of our Intel® open-source OpenMP* runtime as an LLVM sub-project (and the LLVM project has been kind enough to accept our contribution!). This gives the community a fully LLVM license compatible version of the OpenMP runtime for use in  OpenMP development projects.
The complete source code is now available at
openmp.llvm.org
.
We open-sourced the Intel OpenMP runtime code to support the development of a full LLVM-based implementation of the OpenMP specification. Intel’s compiler team in Moscow has made outstanding progress in implementing the Clang changes to support the OpenMP language extensions (you can see their work at
http://clang-omp.github.io
), and now we’ve reached a milestone where we can create an LLVM sub-project for some of the other components that are needed to build a complete OpenMP system.
Personally, I am very happy (and proud) to be associated with LLVM, and I look forward to a long and productive collaboration.
-- Jim Cownie
