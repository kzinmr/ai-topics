---
title: "LLVM Weekly - #13, Mar 31st 2014"
url: "https://blog.llvm.org/2014/03/llvm-weekly-13-mar-31st-2014.html"
fetched_at: 2026-05-05T07:01:42.491563+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #13, Mar 31st 2014

Source: https://blog.llvm.org/2014/03/llvm-weekly-13-mar-31st-2014.html

LLVM Weekly - #13, Mar 31st 2014
Welcome to the thirteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or
@llvmweekly
or
@asbradbury
on Twitter.
Thanks in no small part to a
mention on the Raspberry Pi blog
,
Learning Python with Raspberry Pi
by myself and Ben Everard is at the time of writing #1 in the Programming books section on Amaon UK. Also, keep your eyes on the
X-Dev London meetup page
as I'm expecting to give an LLVM-related talk there on the 9th April, though it's not listed yet and is subject to change.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
It's only a week to go until
EuroLLVM 2014
, which wil be held in Edinburgh on the 7th and 8th of April. Tragically I'm not going to be there as I'm trying to focus on getting my PhD finished, but the schedule looks fantastic.
The Linux Collaboration Summit featured an update on progress of the LLVMLinux project to build the Linux kernel using LLVM/Clang (
slides
). As of right now, there are approximately 48 kernel patches still working their way upstream for the project.
John Regehr has written an interesting blog post on the subject of
using Z3 to prove some things about LLVM optimisations
.
Facebook have
released the Warp C and C++ preprocessor
, written in D. It claims to benchmark much faster than GCC's preprocessor resulting in faster build times, though a
quick comparison with Clang
didn't show it in a favourable light speed-wise.
Meeting C++ have published a helpful summary of
what might make its way in to C++17 or C++1y
.
On the mailing lists
Apple are
contributing their 64-bit ARM backend upstream
. Initially, this will co-exist with the current AArch64 backend (the Apple implementation is called ARM64), and over time the backends will be merged.
Tom Stellard has [announced a tentative release schedule for LLVM and Clang 3.4.1] and is searching for volunteers to test, as well as nominations for patches that should be included. The proposed schedule is Mar 26 - April 9: Identify and backport additional bug fixes to the 3.4 branch. April 9 - April 18: Testing Phase April 18: 3.4.1 Release
Frank Winter started a discussion on
how to specify the alignment of a pointer in LLVM IR
, which yields some interesting responses.
Renato Golin kicked off a
discussion about supporting named registers in LLVM/Clang
. This is a GNU extension not currently supported. There seemed to be some agreement that this is worth supporting, which resulted in a follow-on thread on
how to implement support for named registers
.
A
query from Geoffrey Irving
about how to safely make use of floating point rounding mode resulted in an interesting discussion about how a changing rounding modes could be supported. For example, with the introduction of a
fp_rounding_sensitive
annotation.
LLVM commits
The ARM big-endian targets armeb and thumbeb have been added.
r205007
.
Apple's ARM64 backend has been merged, and will for a time live side-by-side with the existing AArch64 backend (see 'on the mailing lists' for more details).
r205090
.
The
@llvm.clear_cache
builtin has been born.
r204802
,
r204806
.
Windows target triple spellings have been canonicalised. See the commit for full details, but in short i686-pc-win32 is now i686-pc-windows-msvc, i686-pc-mingw32 is now i686-pc-windows-gnu and i686-pc-cygwin is now i686-pc-windows-cygnus.
r204977
.
The first step towards little-endian code generation for PowerPC has been committed. This initial patch allows the PowerPC backend to produce little-endian ELF objects.
r204634
.
Another LLVM optimisation pass has been fixed to be address space aware, and will no longer perform an addrspacecast.
r204733
.
It is now disallowed for an alias to point to a weak alias.
r204934
.
CloneFunctions will now clone all attributes, including the calling convention.
r204866
.
DebugInfo gained support for compressed debug info sections.
r204958
.
Clang commits
The static analyzer is now aware of
M_ZERO
and
__GFP_ZERO
flags for kernel mallocs.
r204832
.
Clang learned how to de-duplicate string the MSVC way.
r204675
.
Capability attributes can be declared on a typedef declaration as well as a structure declaration.
r204657
.
module.private.modulemap
and
module_private.map
are now documented.
r205030
.
Clang's CodeGen module now allows different RTTI emission strategies. This was added for ARM64.
r205101
.
Other project commits
ThreadSanitizer has new benchmarks for synchronization handling.
r204608
.
Initial infrastructure for IEEE quad precision was added to compiler-rt.
r204999
.
LLD gained the
--allow-multiple-definition
and
--defsym
options.
r205015
,
r205029
.
In LLDB, JITed function can now have debug info and be debugged with debug and source info.
r204682
.
ThreadSanitizer vector clock operations have been optimized and are now O(1) for several important use cases.
r204656
.
