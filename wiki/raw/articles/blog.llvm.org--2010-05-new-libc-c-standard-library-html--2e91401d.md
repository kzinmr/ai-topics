---
title: "New \"libc++\" C++ Standard Library"
url: "https://blog.llvm.org/2010/05/new-libc-c-standard-library.html"
fetched_at: 2026-05-05T07:01:44.101168+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# New "libc++" C++ Standard Library

Source: https://blog.llvm.org/2010/05/new-libc-c-standard-library.html

New "libc++" C++ Standard Library
By Chris Lattner
May 11, 2010
#C++
,
#Clang
One minute read
I'm happy to announce a new subproject of LLVM: "libc++". libc++ is an implementation of the C++ Standard Library, with a focus on standards compliance, highly efficient generated code, and with an aim to support C++'0x when the standard is ratified. libc++ is written and maintained by Howard Hinnant, but we look forward to contributions from the LLVM community.
libc++ is approximately 85% complete at this point (including C++'0x features), and while it is intended to support and complement the Clang++ compiler, it can be ported to work with a broad variety of different C++ compilers. For more information, see the
http://libcxx.llvm.org
web page.
-Chris
