---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2010/06/new-lldb-debugger.html"
fetched_at: 2026-05-05T07:01:44.010179+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2010/06/new-lldb-debugger.html

New "lldb" Debugger
I'm happy to announce a great new subproject of LLVM: LLDB. LLDB is a modern debugger infrastructure which is built (like the rest of LLVM) as a series of modular and reusable libraries. LLDB builds on existing LLVM technologies like the
enhanced disassembler
APIs, the Clang ASTs and expression parser, the LLVM code generator and JIT compiler.
While still in early development, LLDB supports basic command line debugging scenarios on the Mac, is scriptable, and has great support for multithreaded debugging. LLDB is already much faster than GDB when debugging large programs, and has the promise to provide a much better user experience (particularly for C++ programmers). We are excited to see the new platforms, new features, and enhancements that the broader LLVM community is interested in.
If you'd like to try out LLDB and participate in its development, please visit
http://lldb.llvm.org/
and consider signing up for the
lldb-dev
and
lldb-commits
mailing lists.
-Chris and the LLDB Team
