---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2013/06/lldb-33-and-beyond.html"
fetched_at: 2026-05-05T07:01:43.200466+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2013/06/lldb-33-and-beyond.html

LLDB 3.3 and beyond
The LLVM project debugger (LLDB) has seen a recent upswing of activity around the LLVM 3.3 release.  While the debugger has long been the default tool with Xcode, its potential beyond Darwin has had room to grow.  Especially within the last year, the development community has grown beyond its roots with OS/X and iOS to include substantial contributions for Linux, Windows, and FreeBSD. In addition, experimental packages are available for a growing number of distributions including Debian, Ubuntu and Arch.
Much of the potential draws from the architecture of LLDB.  The debugger is well suited to debugging the latest C++ code because of its reuse of LLVM and Clang.  This includes the LLVM dynamic execution engine (MCJIT) for expression evaluation, the LLVM disassembler and the use of the Clang AST parser.  The reuse of LLVM project components has kept LLDB lightweight and has focused developer efforts on the core tasks of being a good debugger.
Overall, this modern debugger has been well designed from the ground up for multi-threaded debugging, lazy symbolication, versatile unwind, and a hierarchical command set including both C++ and Python interfaces.  The availability of these core interfaces allows LLDB to fulfill its name as a low-level debugger.  Developers can use the LLDB libraries for format-neutral access to information in object files such as debug information, symbols, types, functions, line tables and more.   This information is useful to develop debuggers, symbolication tools, and analysis tools.
Python is currently embedded inside of LLDB and available through an interactive interpreter.  The available command set allows arbitrary Python code to be run on breakpoints, watch-points, data summaries and formatters, and the like. The LLDB shared library can also be accessed in Python scripts on the command line.  Overall, the ability to customize LLDB behavior using arbitrary Python code, write extensions using Python, and to evaluate arbitrary C++ expressions contribute to the versatility of this project.
Recent LLDB packages have closed some of the feature gap with LLDB on Linux relative to Darwin.  This includes support for multi-threaded debugging, watch-points and vector register sets.  In addition there have been many improvements to process control, expression evaluation, the build system and support of i386 targets.  Upcoming features include JIT debugging, core file support and support of new processor features.  Much of this work impacts any POSIX distribution including FreeBSD.  Currently, x86-64 Linux builds and targets are tested on trunk (using GCC and Clang) with every commit to LLVM, Clang and LLDB.
The activity on Linux for x86-64 is just part of the picture.  A Windows branch has been developed with the first port of remote debugging to a non-Darwin platform.  Work is just underway to assess LLDB on FreeBSD, with ICC and for i386 targets.  In fact, the number of active contributors to LLDB has more than doubled in the last year alone.
At this point in the growth of LLDB, feedback is very welcome, as we grow the test coverage and use the tool to debug increasingly more complex applications.  Increasingly, LLDB is a responsive debugger that can handle some of the harder cases of multi-threaded C++ debugging effectively.
For more information about LLDB architecture, features, source code, packages, feature status or build information, visit
lldb.llvm.org
.  If you have questions or comments about this release, please contact the
lldb-dev
mailing list!
