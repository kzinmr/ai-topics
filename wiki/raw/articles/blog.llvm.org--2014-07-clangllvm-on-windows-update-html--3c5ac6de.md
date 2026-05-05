---
title: "Clang/LLVM on Windows Update"
url: "https://blog.llvm.org/2014/07/clangllvm-on-windows-update.html"
fetched_at: 2026-05-05T07:01:41.991708+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Clang/LLVM on Windows Update

Source: https://blog.llvm.org/2014/07/clangllvm-on-windows-update.html

Clang/LLVM on Windows Update
It’s time for an update on Clang’s support for building native Windows programs, compatible with Visual C++!  We’ve been working hard over the last few months and have improved the toolchain in a variety of ways.  All C++ features aside from debug info and exceptions should work well.  This
link
provide more specific details.  In February we reached an exciting milestone that we can self-host Clang and LLVM using clang-cl (without fallback), and both projects  pass all of their tests!  Additionally both Chrome and Firefox now compile successfully with fallback!  Here are some of the highlights of recent improvements:
Microsoft compatible record layout is done!  It’s been thoroughly fuzz tested and supports all Microsoft specific components such as virtual base table pointers,
vtordisps
, __declspec(align) and #pragma pack.  This turned out to be a major effort due to subtle interactions between various features.  For example, __declspec(align) and #pragma pack behave in an analogous manner to the gcc variants, but interact with each other in a different manner. Each version of Visual Studio changes the ABI slightly.  As of today clang-cl is layout compatible with VS2013.
Clang now supports all of the calling conventions used up to VS2012.  VS2013 added some new ones that we haven’t implemented yet.  One of the other major compatibility challenges we overcame was passing C++ objects by value on 32-bit x86.  Prior to this effort, LLVM modeled all outgoing arguments as SSA values, making it impossible to take the address of an argument to a call.  It turns out that on Windows C++ objects passed by value are constructed directly into the argument memory used for the function call.  Achieving 100% compatibility in this area required making fundamental changes to LLVM IR to allow us to compute this address.
Most recently support for run time type information (RTTI) was completed.  With RTTI support, a larger set of programs and libraries (for example
ICU
) compile without fallback and dynamic_cast and typeid both work.  RTTI support also brings along support for std::function.  We also recently added support for lambdas so you can enjoy all of the C++11 functional goodness!
