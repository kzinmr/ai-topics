---
title: "New ELF Linker from the LLVM Project"
url: "https://blog.llvm.org/2015/11/new-elf-linker-from-llvm-project.html"
fetched_at: 2026-05-05T07:01:39.750340+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# New ELF Linker from the LLVM Project

Source: https://blog.llvm.org/2015/11/new-elf-linker-from-llvm-project.html

New ELF Linker from the LLVM Project
By Rui Ueyama
Nov 30, 2015
#lld
3 minute read
We have been working hard for a few months now to rewrite the ELF support in lld, the LLVM linker. We are happy to announce that it has reached a significant milestone: it is now able to bootstrap LLVM, Clang, and itself and pass all tests on x86-64 Linux and FreeBSD with the speed expected of an LLVM project.
ELF is the standard file format for executables on Unix-like systems, such as Linux and BSDs. GNU ld and GNU gold are commonly used linkers for such systems today. In many use cases, the linker is a black box for which only speed matters. Depending on program size, linking a program takes from tens of milliseconds to more than a minute. We designed the new linker so that it runs as fast as possible. Although no serious benchmarking or optimization has been conducted yet, it is consistently observed that the new lld links the LLVM/Clang/lld executables in about half the time of GNU gold. Generated executables are roughly the same size. lld is not at feature parity with gold yet, so it is too early to make a conclusion, but we are working hard to maintain or improve lld’s speed while adding more features.
lld is command-line compatible with GNU ld so that it can be used as a drop-in replacement. This does not necessarily mean that we are implementing all the features of the GNU linkers in the same way as they did. Some features are no longer relevant for modern Unix-like systems and can be removed. Some other features can be implemented in more efficient ways than those in the traditional linkers. Writing a new linker from scratch is a rare occasion. We take advantage of this opportunity to simplify the linker while keeping compatibility with the existing linkers for normal use.
The new ELF linker is a relatively small program which currently consists of about 7000 lines of C++ code. It is based on the same design as the PE/COFF (Windows) support in lld, so the design document for the PE/COFF support is directly applicable to the ELF support.
The older ELF support still exists in lld repository in parallel with the new one. Please be careful to not confuse the two. They are separated at the top directory and do not share code. You can run the new linker with ld.lld command or by passing -fuse-ld=lld to Clang when linking.
We are still working on implementing remaining functionality such as improved linker script support or improved support for architectures beyond x86_64. If you are interested in the new linker,
try it out for yourself
.
