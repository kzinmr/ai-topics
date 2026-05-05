---
title: "fastent - Faster entropy estimation."
url: "https://iczelia.net/posts/fastent/"
fetched_at: 2026-05-05T07:01:20.967572+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# fastent - Faster entropy estimation.

Source: https://iczelia.net/posts/fastent/

Introduction
⌗
I am a long-time user of the
ent
utility originally developed by
Fourmilab
and now maintained primarily in Debian. While it was particularly enjoyable to use it throughout my data compression journey, it ultimately proved itself to be suboptimal when it comes to handling large files.
Having to wait over ten seconds to estimate entropy information of a mid-size file (~50-100MiB) made me wonder about the source code of
ent
and the cause behind all the inefficiencies. As a result of this, I re-wrote
ent
from scratch preserving (more or less) the same command-line interface, messages and feature list.
What’s wrong with ent?
⌗
The first issue is associated with the way
ent
- available from the Debian repositories - is built. The main culprit here is limited optimisation, the executable not making use of available vector instructions (due to
-march=x86-64
disallowing the use of AVX) and the choice of auxiliary compiler flags. Obviously, these issues are the inescapable harsh reality that Debian users must face, but as it turns out, these issues play a large role in performance, as demonstrated later.
Let’s dive into the source code, a mirror of which I found
on Github
. In particular, let’s focus on
src/ent.c
and
src/randtest.c
, because these appear to contain most of the interesting code. A few initial observations:
The author’s frustration regarding Windows file modes applied to stdin by default and the CRLF line endings is very clearly visible throughout the entire source file. Because Windows will “normalise” line endings that appear in standard streams by default, it will garble binary data and provide slightly incorrect results, hence the file needs to be switched to binary mode to avoid this.
Despite most inputs to
ent
being regular files, the code opts for standard I/O disregarding the fact that files could be mapped into memory (if possible) to reduce the overhead associated with copying data between the kernel and user modes.
The tool has modes that I (nor any of my friends) do not recall using. While this is not an issue on its own, their presence makes it more difficult to implement certain functionality (e.g. because
ent
supports the
-f
flag for case folding on the input, the input needs to be processed first before passing it on to other functions, which is going to be detrimental to performance should
ent
opt in for memory mapped files).
The code that handles entropy estimation, Monte Carlo simulation and serial correlation coefficient computation is located in
randtest.c
, while the code that calls on the input data is located in
ent.c
. Because most builds will not enable link-time optimisation, the functions responsible for performing computation on the data will not be inlined and interprocedural optimisation will not be applied. The penalty for this is further exercebated considering the observations below.
The function that processes a buffer of bytes and updates the state accordingly (
void rt_add(void *, int)
in
randtest.c
) handles Monte Carlo simulation suboptimally. The code of the entire function relies on compiler strength reduction and other optimisations too heavily. The issue with Monte Carlo simulation is that it follows the following idea:
The issue is obvious: after every invocation of
rt_add
, it needs to synchronise the contents of all global variables that are otherwise kept in registers (montex, montey, monte, …) so that other functions can access them. The code above is placed in a loop that is invoked for each bit of the input and gated behind a check that lets it run only when the current position in the byte is 0. The serial correlation coefficient calculation code needs to rely on strength reduction to eliminate a branch that is taken only once in the program:
Histogram computation code in
ent.c
is extremely inefficient in bit-wise mode:
Instead of performing this operation, it is significantly easier to state
count[1] += popcount(ob);
and then when the end of file is hit, compute
count[0] = file_size * 8 - count[1];
.
Histogram computation code in byte-wise mode is also inefficient. To utilise out-of-order execution and other performance-enhancing features that modern processors have, it is necessary to split the histogram into multiple buckets and then sum the partial results. Because the histogram code writes into a large frequency table, this data can’t be cached within registers. Writing to a table cell means the result must necessarily be written to memory. The data is likely cached in L1 and the CPU will not suffer any delay for a single write. The following bytes however introduce an additional difficulty. If a file is not very entropic, there is a high possibility that there are long runs (or “almost runs” - i.e. interleaved symbol sequences) of the same character in it. So, when the program increments a cell in the frequency table, write commit delay gets into the way. An increment means that the CPU has to perform both a read and then a write to this memory address. If the previous increment operation is still not entirely committed, cache will make the CPU wait a bit more before delivering the data. Using multiple buckets for this purpose alleviates this issue, as the memory locations accessed by a single iteration of a loop that processes 16 or more bytes in a single iteration are always distinct.
The final and most significant flaw is that the program always reads one byte at a time and then passes it to the function that accepts a buffer of data to take into account when computing various statistical variables of the input. This is the main source of bottleneck in the application
An overview of fastent.
⌗
fastent
provides the following improvements and changes to
ent
:
Removes the case folding feature.
Uses memory-mapped files where possible.
Processes files in large chunks.
Uses standard ASCII
<ctype.h>
functions.
Optimises histogram computation avoiding the bottleneck pointed in the section above.
Doesn’t rely on the compiler performing strength reduction and instead hoists the serial correlation coefficient check out, making the computation algorithm branchless.
Uses the x86-64
popcnt
instruction for bitwise histogram building.
Avoids copies in Monte Carlo simulation by aligning
mp
to
MONTEN
for every data chunk and then inlining the simulation function to the loop making it use the input buffer instead (basically, I applied a modified variant of a Duff’s device of order 6
).
Makes extensive use of AVX intrinsics to improve performance.
Downloads.
⌗
Benchmarks.
⌗
First test file:
Second test file:
