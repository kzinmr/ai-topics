---
title: "LLVM Weekly - #9, Mar 3rd 2014"
url: "https://blog.llvm.org/2014/03/llvm-weekly-9-mar-3rd-2014.html"
fetched_at: 2026-05-05T07:01:42.582402+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #9, Mar 3rd 2014

Source: https://blog.llvm.org/2014/03/llvm-weekly-9-mar-3rd-2014.html

LLVM Weekly - #9, Mar 3rd 2014
Welcome to the ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
As well as growing another year older last week, I've also started publicising the book I authored with
Ben Everard
,
Learning Python with Raspberry Pi
(
Amazon US
) which should ship soon in paperback or is available right now for Kindle. Hopefully it should be available soon in DRM-free digital formats on oreilly.com. I will be putting more of my Raspberry Pi exploits and tutorials on
muxup.com
, so if that interests you follow
@muxup
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The list of
mentoring organisations for Google Summer of Code 2014
has been released. LLVM is one of them, so any budding compiler engineers who qualify may want to check out the
ideas page
. Other organisations I spotted advertising relevant project ideas are
the Linux Foundation
,
X.org
and of course
GCC
.
At the end of last week, Broadcom made a major step forward in
announcing the release of full register level documentation for the VideoCore IV graphics engine
as well as full graphics driver source. The device most well-known for featuring VideoCore IV is the
Raspberry Pi
. The released documentation opens the door to producing something similar to the
GPU-accelerated FFT library
support that was recently released. Some readers of LLVM Weekly may of course be interested in using this information to produce an LLVM backend. Hopefully the following pointers will help. There are lots of resources linked to at the homepage of the
VideoCore IV reverse engineering project
. I'd draw particular attention to the
QPU reverse engineering effort
which contains good information despite the reverse engineering part of the work being made unnecessary by the Broadcom release. You may want to check out the
raspi-internals mailing list
and
#raspberrypi-internals
on Freenode. It's also worth looking at
the commented disassembly of the VideoCore FFT code
and Herman Hermitage's work in progress
QPU tutorial
.
Code for
Fracture
, an architecture-independent decompiler to LLVM IR has been released.
Olivier Goffart has written about
his proof of concept reimplementation of Qt's moc using libclang
. It's actually from last year, but it's new to me.
Alex Denisov has written a
guide to writing a clang plugin
. He gives an example of a minimal plugin that complains about lowercased Objective C class names.
Coursera are re-running
their compilers course
on March the 17th. See
Dirkjan Ochtman's impressions of the course from the previous run
.
The Qualcomm LLVM team are
advertising for an intern
.
On the mailing lists
LLVM commits
LLVM grew a big-endian AArch64 target
r202024
. Some might consider it a step back, but apparently there's a decent number of people interested in big-endian on AArch64. There's an interesting
presentation from ARM
about running a virtualised BE guest on a LE host.
The flipping of the C++11 switch has allowed a number of simplifications to start to make their way in to the LLVM codebase. For instance, turning simple functors in to lambdas. Like or loathe C++11 lambda syntax, they're certainly less verbose.
r202588
.
OwningPtr<T>
gained support for being converted to and from
std::unique_ptr<T>
, which lays the ground for LLVM moving to using
std::unique_ptr
in the future.
r202609
.
The coding standards document was updated to reflect the C++11 features that can now be used in the LLVM/Clang codebase and to provide guidance on their use.
r202497
,
r202620
.
The loop vectorizer is now included in the LTO optimisation pipeline by default.
r202051
.
DataLayout has been converted to be a plain object rather than a pass. A DataLayoutPass which holds a DataLayout has been introduced.
r202168
.
The PowerPC backend learned to track condition register bits, which produced measurable speedups (10-35%) for the POWER7 benchmark suite.
r202451
.
X86 SSE-related instructions gained a scheduling model. Sadly there is no indication whether this makes any measurable difference to common benchmarks.
r202065
.
The scalar replacement of aggregates pass (SROA) got a number of refactorings and bug fixes from Chandler Carruth, including some bug fixes for handling pointers from address spaces other than the default.
r202092
,
r202247
, and more.
An experimental implementation of an invalid-pointer-pair detector was added as part of AddressSanitizer. This attempts to identify when two unrelated pointers are compared or subtracted.
r202389
.
Shed a tear, for libtool has been removed from the LLVM build system. The commit says it was only being used to find the shared library extension and nm. The diffstat of 93 insertions and 35277 deletions speaks for itself.
r202524
.
Clang commits
The initial changes needed for
omp simd
directive support were landed.
r202360
.
The
-Wabsolute-value
warning was committed, which will warn for several cases of misuse of absolute value functions. It will warn when using e.g. an int absolute value function on a float, or when using it one a type of the wrong size (e.g. using abs rather than llabs on a long long), or whn taking the absolute value of an unsigned value.
r202211
.
An API was added to libclang to create a buffer with a JSON virtual file overlay description.
r202105
.
The driver option
-ivfsoverlay
was added, which reads the description of a virtual filesystem from a file and overlays it over the real file system.
r202176
.
CFG edges have been reworked to encode potentially unreachable edges. This involved adding the AdjacentBlock class this encodes whether the block is reachable or not.
r202325
.
The 'remark' diagnostic type was added. This provides additional information to the user (e.g. information from the vectorizer about loops that have been vectorized).
r202475
.
Other project commits
The compiler-rt subproject now has a
CODE_OWNERS.txt
to indicate who is primarily responsible for each part of the project.
r202377
.
A standalone deadlock detector was added to ThreadSanitizer.
r202505
.
The OpenMP runtime has been ported to FreeBSD.
r202478
.
