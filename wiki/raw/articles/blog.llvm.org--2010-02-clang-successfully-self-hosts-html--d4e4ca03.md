---
title: "Clang Successfully Self-Hosts!"
url: "https://blog.llvm.org/2010/02/clang-successfully-self-hosts.html"
fetched_at: 2026-05-05T07:01:44.321585+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Clang Successfully Self-Hosts!

Source: https://blog.llvm.org/2010/02/clang-successfully-self-hosts.html

Clang Successfully Self-Hosts!
By Doug Gregor
Feb 4, 2010
#Clang
One minute read
Today, Clang completed its first complete self-host! We built all of LLVM and Clang with Clang (over 550k lines of C++ code). The resulting binaries passed all of Clang and LLVM's regression test suites, and the Clang-built Clang could then build all of LLVM and Clang again. The third-stage Clang was also fully-functional, completing the bootstrap.
Congratulations to all of the Clang developers on this amazing achievement!
