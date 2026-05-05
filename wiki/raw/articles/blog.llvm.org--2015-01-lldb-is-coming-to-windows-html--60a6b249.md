---
title: "LLDB is Coming to Windows"
url: "https://blog.llvm.org/2015/01/lldb-is-coming-to-windows.html"
fetched_at: 2026-05-05T07:01:41.021230+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLDB is Coming to Windows

Source: https://blog.llvm.org/2015/01/lldb-is-coming-to-windows.html

LLDB is Coming to Windows
By Zachary Turner
Jan 20, 2015
#LLDB
,
#Clang
3 minute read
We've spoken in the
past
about teaching Clang to fully support Windows and be compatible with MSVC.  Until now, a big missing piece in this story has been debugging the clang-generated executables.  Over the past 6 months, we've started working on making LLDB work well on Windows and support debugging both regular Windows programs and those produced by Clang.
Why not use an existing debugger such as GDB, Visual Studio's, or WinDBG?  There are a lot of factors in making this kind of decision.  For example, while GDB understands the DWARF debug information produced by Clang on Windows, it doesn't understand the Microsoft C++ ABI or debug information format.  On the other hand, neither Visual Studio nor WinDBG understand the DWARF debug information produced by Clang.  With LLDB, we can teach it to support
both
of these formats, making it usable with a wider range of programs.  There are also other reasons why we're really excited to work on LLDB for Windows, such as the tight integration with Clang which lets it support all of the same C++ features in its expression parser that Clang supports in your source code.  We're also looking to continue adding new functionality to the debugging experience going forward, and having an open source debugger that is part of the larger LLVM project makes this really easy.
The past few months have been spent porting LLDB's core codebase to Windows.  We've been fixing POSIX assumptions, enhancing the OS abstraction layer, and removing platform specific system calls from generic code.  Sometimes we have needed to take on significant refactorings to build abstractions where they are necessary to support platform specific differences.  We have also worked to port the test infrastructure to Windows and set up build bots to ensure things stay green.
This preliminary bootstraping work is mostly complete, and you can use LLDB to debug simple executables generated with Clang on Windows today.  Note the use of the word "simple".  At last check, approximately 50% of LLDB's tests fail on Windows.  Our baseline, however, which is a single 32-bit executable (i.e. no shared libraries), single-threaded application built and linked with Clang and LLD using DWARF debug information, works today.  We've tested all of the fundamental functionality such as:
Various methods of setting breakpoints (address, source file+line, symbol name, etc)
Stopping at and continuing from breakpoints
Process inspection while stopped, such as stack unwinding, frame setting, memory examination, local variables, expression evaluation, stepping, etc  (one notable exception to this is that step-over doesn't yet work well in the presence of limited symbol information).
Of course, there is still more to be done.  Here are some of the areas we're planning to work on next:
Fixing low hanging fruit by improving the pass-rate of the test suite.
Better support for debugging multi-threaded applications.
Support for debugging crash dumps.
Support for debugging x64 binaries.
Enabling stepping through shared libraries.
Understanding PDB (for debugging system libraries, and executables generated with MSVC).  Although the exact format of PDB is undocumented, Microsoft still provides a rich API for querying PDB in the form of the DIA SDK.
Adding debugging commands familiar to users of WinDBG (e.g. !handle, !peb, etc)
Remote debugging
Symbol server support
Visual Studio integration
If you're using Clang on Windows, we would encourage you to
build LLDB
(it should be in the Windows
LLVM installer
soon) and let us know your thoughts by posting them to
lldb-dev
.  Make sure you
file bugs
against LLDB if you notice anything wrong, and we would love for you to dive into the code and help out.  If you see something wrong, dig in and try to fix it, and post your patch to
lldb-commits
.
