---
title: "Accessing unaligned memory"
url: "http://fastcompression.blogspot.com/2015/08/accessing-unaligned-memory.html"
fetched_at: 2026-05-05T07:00:59.984816+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# Accessing unaligned memory

Source: http://fastcompression.blogspot.com/2015/08/accessing-unaligned-memory.html

Thanks to
Herman Brule
, I recently received an access to real ARM hardware systems, in order to test C code and tune them for performance. It proved a great experience, with lots of learnings.
It started with the finding that
xxhash
speed was rubbish on ARM systems. To this end, 2 systems were benchmarked : first, an ARMv6-J, and then an ARMv7-A.
This was a unwelcomed surprise, and among the multiple potential reasons, it turns out that accessing unaligned data became the most critical one.
Since my
latest blog entry on this issue
, I converted unaligned-access code to the QEMU-promoted solution using `memcpy()`. Compared with earlier method (`pack` statement), the `memcpy()` version has a big advantage : it's highly portable. It's also supposed to be correctly optimized by the compiler, to end up to a trivial `unaligned load` instruction on CPU architecture which support this feature.
Well, supposed to is really the right word. It turns out,
this is not true in a number of cases
. While initially only direct benchmark tests were my main investigation tool, I was pointed towards
godbolt online assembly generator
, which became an invaluable asset to
properly understand what was going on at assembly level
.
Thanks to these new tools, the issue could be summarized into a selection between 3 possibilities to access unaligned memory :
1. Using `memcpy()` : this is the most portable and safe one.
It's also efficient in a large number of situations. For example, on all tested targets, clang translates `memcpy()` into a single `load` instruction when hardware supports it. gcc is also good on most target tested (x86, x64, arm64, ppc), with just arm 32bits standing out.
The issue here is that your mileage will vary depending on specific compiler / targets. And it's difficult, if not impossible, to test and check all possible combinations. But at least, `memcpy()` is a good generic backup, a safe harbour to be compared to.
2. `pack` instruction : the problem is that it's a compiler-specific extension. It tends to be present on most compilers, but using multiple different, and incompatible, semantics. Therefore, it's a pain for portability and maintenance.
That being said, in a number of cases where `memcpy()` doesn't produce optimal code, `pack`
tends
to do a better job. So it's possible to `special case` these situations, and left the rest to `memcpy`.
The most important use case was
gcc with
ARMv7
, basically the most important 32-bits ARM version nowadays (included in current crop of smartphones and tablets).
Here, using `pack` for unaligned memory improved performance
from 120 MB/s to 765 MB/s
compared to `memcpy()`. That's definitely a too large difference to be missed.
Unfortunately, on gcc with
ARMv6
, this solution was still as bad as `memcpy()`.
3. direct `u32` access : the only solution I could find for gcc on ARMv6.
This solution is not recommended, as it basically "lies" to the compiler by pretending data is properly aligned, thus generating a fast `load` instruction. It works when the target cpu is hardware compatible with unaligned memory access,
and
does not risk generating some opcode which are
only
compatible with strictly-aligned memory accesses.
This is exactly the situation of ARMv6.
Don't use it for ARMv7 though : although it's compatible with unaligned load, it can also issue
multiple load
instruction, which is a
strict-align
only opcode. So the resulting binary would crash.
In this case too, the performance gain is too large to be neglected : on unaligned memory access, read speed went up
from 75 MB/s to 390 MB/s
compared to `memcpy()` or `pack`. That's more than 5 times faster.
So there you have it, a complex setup, which tries to select the best possible method depending on compiler and target. Current findings can be summarized as below :
Better unaligned read method :
------------------------------
|
compiler
|
x86
/
x64
|
ARMv7
|
ARMv6
|
ARM64
|
PPC
|
|-----------|---------|--------|--------|--------|--------|
|
GCC
4.8
|
memcpy
|
packed
|
direct
|
memcpy
|
memcpy
|
|
clang
3.6
|
memcpy
|
memcpy
|
memcpy
|
memcpy
|
?
|
|
icc
13
|
packed
|
N
/
A
|
N
/
A
|
N
/
A
|
N
/
A
|
A good news is that there is a safe default method, which tends to work well in a majority of situations. Now, it's only a matter of special-casing specific combinations, to use alternate method.
Of course, a better solution would be for all compilers, and gcc specifically, to properly translate `memcpy()` into efficient assembly for all targets. But that's wishful thinking, clearly outside of our responsibility. Even if it does improve some day, we nonetheless need an efficient solution now, for current crop of compilers.
The new unaligned memory access design is currently available within
xxHash source code on github, dev branch
.
Summary of gains on tested platforms :
compiled with gcc v4.7.4
|
program
|
platform
|
before
|
after
|
|--------------------|---------|----------|----------|
|
xxhash32 unaligned |  ARMv6  |  75 MB/s | 390 MB/s |
|
xxhash32 unaligned |  ARMv7  | 122 MB/s | 765 MB/s |
| lz4 compression    |  ARMv6  |  13 MB/s |  18 MB/s |
| lz4 compression    |  ARMv7  |  33 MB/s |  49 MB/s |
[Edit]
: apparently, this issue will help
improve GCC for the better
