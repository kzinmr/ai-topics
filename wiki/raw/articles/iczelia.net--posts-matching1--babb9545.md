---
title: "Matcher Redux: Demystifying Regular Expressions (Part 1: Exact Matching I)"
url: "https://iczelia.net/posts/matching1/"
fetched_at: 2026-05-05T07:01:19.348549+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Matcher Redux: Demystifying Regular Expressions (Part 1: Exact Matching I)

Source: https://iczelia.net/posts/matching1/

Programmers often see regular expressions and the respective matching engines as a complex, almost unattainable blackbox. PCRE spans hundreds of thousands of lines of code. It supports a large and evolving feature set. Lookarounds, backreferences, Unicode properties, and multiple matching modes are all present. On top of this, PCRE includes a JIT compiler that translates patterns into machine code for speed.
While all these features are important for a production-grade regex engine, they can obscure the fundamental concepts behind pattern matching. In this blog post, we will start our journey towards the exploration of the process of building a matcher from scratch, all by ourselves.
1. Exact match
⌗
In this section we focus on exact string matching. The goal is to find occurrences of a given pattern, verbatim within a text. The constrained form of this problem opens up many optimisation tricks and algorithmic techniques that we can leverage.
Much ink has been spilled on this topic and many algorithms have been proposed over the years. Nonetheless, we take a stab at deriving some of the folk wisdom techniques ourselves, bottom-up.
1.1. Exact match of a single character
⌗
The simplest case of exact matching is to find a single character within a text. Programmers are already used to the function
strchr
from the C standard library, which does exactly that:
The function
strchr
scans the input string
text
character by character, comparing each character to the
target
. If a match is found, it returns a pointer to the first occurrence; otherwise, it returns
nullptr
. A naive implementation of this idea could look like this:
A quick skim at the generated assembly code (from clang 21.1 with
-O3
optimizations) reveals that the compiler does not bother unrolling the loop or using SIMD instructions, preferring to translate the function almost verbatim to x86-64 assembly:
The use of C-style strings (i.e., with a null terminator) prevents us from knowing the length of the input string in advance. This limitation hinders our ability to apply certain optimizations, such as processing multiple characters simultaneously using SIMD instructions. One alternative is the
memchr
function, which takes an explicit length parameter:
1.1.1. Naive search.
⌗
In this case, the implementation can take advantage of the known length to optimize the search process. Once again we can implement a simple version of
memchr
ourselves:
1.1.2. Search via SWAR.
⌗
Disappointingly, the compiler
chose to not vectorise it
either. Our first idea for optimisation is to process multiple characters in each iteration. We will load 8 bytes at a time, treating them as a single integer, and comparing them via the bit-xor (
^
) operation. If any byte matches the target character, the corresponding byte in the result of the xor will be zero. We can then check for the presence and location of the zero byte using some bit-twiddling tricks. Here is the implementation:
Forfeiting some auxiliary explanations and assuming a sufficient level of C-fu in the reader, we can express this more compactly:
Using a
quickly hacked together
benchmark harness, we compare the three implementations of
memchr
for throughput on my Ryzen 7 PRO 7840U laptop:
Skewing the test so that the latency becomes more prominent (smaller buffers) yields:
Our SWAR (SIMD Within A Register) implementation of
memchr
is about 2.5-3x slower than the highly optimized glibc version, which is not bad for a first attempt.
1.1.3. Search via SSE4.2 PCMPESTRI.
⌗
There is still room for improvement, and we will reach for an indispensable trick: x86-64 SIMD intrinsics. We will specifically target the
PCMPESTRI
instruction from the SSE4.2 instruction set, which essentially does the bulk of our work for us.
To quote the Intel® 64 and IA-32 Architectures Software Developer’s Manual, Volume 2B:
PCMPESTRI — Packed Compare Explicit Length Strings, Return Index
Instruction Summary
⌗
Opcode / Instruction
Op/En
64/32-bit Mode
CPUID Flag
Description
66 0F 3A 61 /r imm8
PCMPESTRI xmm1, xmm2/m128, imm8
RMI
V / V
SSE4_2
Perform a packed comparison of string data with explicit lengths, generate an index, and store the result in
ECX
.
VEX.128.66.0F3A 61 /r ib
VPCMPESTRI xmm1, xmm2/m128, imm8
RMI
V / V
AVX
Perform a packed comparison of string data with explicit lengths, generate an index, and store the result in
ECX
.
Instruction Operand Encoding
⌗
Op/En
Operand 1
Operand 2
Operand 3
Operand 4
RMI
ModRM:reg (r)
ModRM:r/m (r)
imm8
N/A
Description
⌗
The instruction compares and processes data from two string fragments based on the encoded value in the
imm8 control byte
(see
Section 4.1, “Imm8 Control Byte Operation for PCMPESTRI / PCMPESTRM / PCMPISTRI / PCMPISTRM”
).
It generates an index that is written to the count register
ECX
.
Each string fragment is represented by
two values
:
Data vector
An
xmm
register for the first operand.
An
xmm
register or
m128
memory operand for the second operand.
Contains byte or word elements of the string.
Length
For
xmm1
: length is taken from
EAX/RAX
.
For
xmm2/m128
: length is taken from
EDX/RDX
.
The length specifies how many bytes or words are valid in the corresponding vector.
Length Interpretation
⌗
The effective length is the
absolute value
of the length register.
The absolute-value computation
saturates
:
Bytes
: maximum 16
Words
: maximum 8
Saturation occurs when the length register value is:
Greater than 16 (or 8 for words), or
Less than −16 (or −8 for words)
Whether data elements are bytes or words is determined by
imm8[3]
.
Comparison and Result
⌗
Comparison and aggregation behavior is controlled by fields in
imm8
(see Section 4.1).
The instruction computes an intermediate result mask (
IntRes2
, see Section 4.1.4).
The index of the
first
or
last
set bit of IntRes2 is returned in
ECX
, depending on
imm8[6]
:
If
imm8[6] = 0
: first (least significant) set bit
If
imm8[6] = 1
: last (most significant) set bit
If
no bits are set
in IntRes2:
ECX = 16
(byte elements)
ECX = 8
(word elements)
We proceed with the implementation in the same vein as the previous SWAR
memchr2
function:
The results are promising. Our implementation is now only about 2x slower than glibc’s highly optimized version:
The source of the remaining gap is a disappointing but frequently recurring story in performance engineering on x86-64 platforms. Looking up the instruction on
uops.info
reveals the following picture for my Zen4 CPU:
Instruction
Lat
TP
Uops
Ports
PCMPESTRI (XMM, M128, I8)
[≤11; ≤29]
2.00 / 4.00
12
1*FP01 + 2*FP1 + 2*FP45
PCMPESTRI (XMM, XMM, I8)
[≤11; 15]
2.00 / 3.00
8
1*FP01 + 2*FP1 + 2*FP45
PCMPESTRI64 (XMM, M128, I8)
[≤11; ≤29]
2.00 / 4.00
12
1*FP01 + 2*FP1 + 2*FP45
PCMPESTRI64 (XMM, XMM, I8)
[≤11; 15]
2.00 / 3.00
8
1*FP01 + 2*FP1 + 2*FP45
The instruction has a high latency (up to 29 cycles when reading from memory!) and consumes multiple micro-operations (uops) that occupy several execution ports. This means that even though we are processing 16 bytes at a time, the instruction’s throughput is limited by its latency and port usage. A natural conclusion would be that glibc clearly uses more advanced techniques that certainly don’t involve
PCMPESTRI
. But why? Wasn’t the point of CISC CPU architectures to have complex instructions that do more work per instruction?
This is neither the first nor last time we see that complex, purpose-built instructions do not necessarily lead to better performance. It’s quite difficult to wrap one’s head around such a paradox. Other examples include:
REP STOSB
is not the fastest way to zero out memory (
memset
/
bzero
), despite being a single instruction that does exactly that.
Even more counterintuitively, seemingly unrolled
REP STOSQ
is typically even slower than
REP STOSB
for the same purpose. The reason is in fact simple: the microcode that makes
REP STOSB
relatively efficient is simply not present for this opcode.
REP MOVSB
is not the fastest way to copy memory (
memcpy
), even though it is designed for that purpose.
REPNE SCASB
is not the fastest way to search for a byte in memory (
memchr
), despite being a single instruction that performs that operation. And finally, here we are: another purpose-built instruction,
PCMPESTRI
, that does not deliver the expected performance boost.
Tangentially, on the topic of
REPNE SCASB
, let’s probe the performance of this. The
memchr
implementation using this instruction is a simple wrapper over inline assembly:
As expected, the performance is underwhelming, but but the biggest surprise is that it is even worse than our naive
simple_memchr
implementation:
1.1.4. Search via SSE2 PCMPEQ + PMOVMSKB.
⌗
To go one step further, we can come back to the SSE4.2,
PCMPESTRI
-based implementation and simply use two instructions with lower latency:
PCMPEQ
(compare), followed by
PMOVMSKB
(move mask). This combination allows us to achieve similar functionality with reduced latency and better throughput. We will also forfeit the alignment loop: since we have tied to machine specific code, we are free to use unaligned loads. Here is the implementation:
To justify this, we come back to the instruction table for Zen 4:
Instruction
Lat
TP
Uops
Ports
PCMPESTRI (XMM, M128, I8)
[≤11; ≤29]
2.00 / 4.00
12
1*FP01 + 2*FP1 + 2*FP45
PCMPEQB (XMM, M128)
[1;≤9]
0.25 / 0.50
1
1*FP0123
PMOVMSKB (R32, XMM)
≤6
0.50 / 1.00
1
1*FP45
It is clear that this combination of opcodes has better throughput guarantees, throughput and requires less Uops. The execution port usage of the CPU is also better, further suggesting better practical performance. Validation of this result is quite easy:
The soundness of this optimisation is further suported by the outputs of e.g. the LLVM machine code analyser; we can compare
the movemask version
and the
the PCMPESTRI version
.
The MCA dumps are for the same overall structure (scalar align/peel into a 16B loop, followed by scalar tail), but with different 16B core, as illustrated by the C code. In terms of assembly code, we see:
Variant 1 core:
vpcmpestri xmm0, [rdi], imm8=0
(SSE4.2 string-compare instruction)
Variant 2 core:
vpcmpeqb + vpmovmskb + tzcnt
(SIMD compare + mask + bit-scan)
f99 over ~100 iterations. Every indicator favours the second version:
Metric
vpcmpestri
vpcmpeqb + pmovmskb + tzcnt
Analysis
Total cycles
3199
1511
Variant 2 is, on paper, about 2.1 times faster
Instructions
5000
4900
Similar instruction count
Total uOps
6400
5600
Variant 2 uses fewer uops
uOps/cycle
2.00
3.71
Variant 1 is throughput-starved.
IPC
1.56
3.24
Variant 2 keeps frontend/backend busy
Block RThroughput
16.0
14.0
Variant 2 has a better steady-state loop throughput
MCA also shows us some auxiliary information about stalls and port usage. In the core, we see
vpcmpestri
as annotated with “9 uops, lat 23, RThroughput 4.00”. It also loads (
MayLoad
). The reciprocal throughput of 4.00 is particularly damning: in the best case, we can only issue one such instruction every 4 cycles. This is a hard limit on the loop throughput, regardless of other factors.
1.1.5. Search via AVX2 (improved).
⌗
Naturally increasing the vector width to 256 bits (32 bytes) should yield further performance improvements. This is however not the case, or at least it will not be as straightforward as before.
The benchmark results are as follows:
The AVX2 version uses the same techniques as the
glibc
memchr
, but we are still quite far away from the 250GiB/s ballpark. The way forward is to capitalise on the broader vector width even more and modify the core loop to scan 128 bytes at a time. This can be achieved by unrolling the loop four times and combining the results using bit-wise OR, scanning for the precise location of the match only when the return is guaranteed:
This almost brings us to parity with
glibc
on large buffers:
1.1.6. Search via SSE2 + BMI (improved).
⌗
The previous AVX2 version uses unaligned loads everywhere (
_mm256_loadu_si256
), and relies on modern CPUs handling that well enough. This is not a great assumption to make for SSE2 code - if your CPU is old enough to not support AVX2, it is likely to have worse performance for unaligned loads. We can therefore revisit the SSE2 version and improve it by adding proper alignment handling.
The new version will spend a lot of code up front to avoid bad alignment situations and to enable aligned loads (
_mm_load_si128
) in the hot loops. We will explicitly consider
p & 63
(position within a 64-byte cache line),  a crosscache path when the initial 16B load would straddle a cache-line boundary (more likely to be slower on some microarchitectures), adjusting p to a 16-byte boundary, then later to a 64-byte boundary (aligned) for the main loop.
The AVX2 code has clean loop tiers: 128B AVX2-unroll, then 32B AVX2, then scalar. Our new version that treats old processors slightly better will do early probing loads that may read past
len
(still within an aligned block on the same page, which does not trigger a fault) and then checks the found index against len before returning.
For example, if we load 16 bytes even if
len
< 16, assuming that we don’t cross a page boundary (which would cause a segmentation fault), then we can simply do:
This is a typical speculative read within the same page / valid mapped memory assumption-style trick, often used in high-performance code.
The special cases have crept up and lead us to produce the following code:
Benchmarking this version shows that we have attained significantly better throughput:
1.1.7 Conclusion
⌗
Through a series of optimisations and careful use of SIMD instructions, we have developed a
memchr
implementation that approaches the performance of
glibc
’s highly optimized version. They also extend to other similar functions like
strlen
(equivalent to
memchr
searching for zero) or
strchr
(equivalent to
memchr
searching for either a specific character or zero) with analogous techniques.
A straightforward implementation of
strlen
given the techniques that we have just covered achieves performance that is on-par with glibc’s
strlen
:
As evidenced by a benchmark in similar vein to the previous ones:
And finally, an implementation of
strchr
:
1.2. Exact match of a pair of characters in overlapping regions.
⌗
For the sake of illustrating the techniques involved, we will consider the problem of searching for either of two characters in a memory block (like a variant of
wmemchr
or such).
1.2.1. Baseline scalar/SWAR implementations.
⌗
We have a couple of the obvious ones. Simple scalar version with 8-bit loads:
Simple scalar version with direct, unaligned 16-bit loads:
An attempt to save a load in each iteration:
A SWAR-based version that processes 8 bytes at a time, pre-filtering candidates that contain either of the two bytes in any order in succession:
Checking for both
hc1
and
hc2
helps to convince the compiler to vectorise the inner loop, leading to - paradoxically - better performance than checking for just one of them.
Also unexpectedly, the SWAR version beats all others in benchmarks by a wide margin, and the second runner-up is the naive, 8-bit direct load version:
1.2.2. SSE2 and SSSE3 implementations.
⌗
The obvious next step is to try to vectorise the search. Without minding unaligned loads, we can do it the obvious way:
The result? A twice speedup over the SWAR version!
Using SSSE3 we can sidestep the nasty unaligned loads by using
PALIGNR
, like so:
Disappointingly, that doesn’t seem to win us much:
Judging by the output of the profiling tool
perf
, most of the time is spent in the hot loop, suggesting that nothing funny is going on with the tail or
tzcnt
again. Zen2 analysis via
llvm-mca
is also somewhat insubtantial:
It also appears that we don’t have enough execution ports to unroll and interleave the loop further.
1.2.3. AVX2 implementation.
⌗
We start tame, by widening the SSE vectors to AVX2 256-bit ones. Unfortunately, life is never as simple as one would have hoped. AVX2 likes to include opcodes that operate on 128-bit lanes of 256-bit vectors only. Reportedly this was dictated by microarchitectural considerations in Intel’s implementation of AVX2 that are now long obsolete, but we have to deal with it nonetheless.
Our implementation will use
permute2x128
and
valignr
to construct the shifted vectors:
Instinctively, we will also try to shove a couple of
_mm256_movemask_epi8
away from the hot path. To do this we will apply the same optimisation idea as in the regular
memchr
implementation:
Benchmarks show that the second AVX2 version is about the same in terms of performance as the first one, except it seems to stall on the
vtest
instruction on both Zen2 and Zen4 CPUs. A test on a Zen2 CPU (5900X) gives:
The kernel of the improved AVX2 loop appears to be:
Unrolling four times gives the following kernel:
0.79 │ 40:   vmovdqu      ymm4,YMMWORD PTR [rdi+rsi*1+0x20]
   0.53 │       vmovdqu      ymm5,YMMWORD PTR [rdi+rsi*1+0x40]
   0.50 │       vmovdqu      ymm6,YMMWORD PTR [rdi+rsi*1+0x60]
   0.52 │       vpcmpeqb     ymm7,ymm0,ymm2
   1.73 │       vperm2i128   ymm3,ymm2,ymm4,0x21
   1.86 │       vpalignr     ymm3,ymm3,ymm2,0x1
   2.43 │       vmovdqu      ymm2,YMMWORD PTR [rdi+rsi*1+0x80]
   2.29 │       vpcmpeqb     ymm3,ymm3,ymm1
   1.95 │       vpand        ymm3,ymm7,ymm3
   2.29 │       vperm2i128   ymm7,ymm4,ymm5,0x21
   1.10 │       vpalignr     ymm7,ymm7,ymm4,0x1
   0.94 │       vpcmpeqb     ymm4,ymm0,ymm4
   0.84 │       vpcmpeqb     ymm7,ymm7,ymm1
   0.69 │       vpand        ymm4,ymm4,ymm7
   0.71 │       vperm2i128   ymm7,ymm5,ymm6,0x21
   1.04 │       vpor         ymm8,ymm3,ymm4
   0.76 │       vpalignr     ymm7,ymm7,ymm5,0x1
   1.06 │       vpcmpeqb     ymm5,ymm0,ymm5
   0.72 │       vpcmpeqb     ymm7,ymm7,ymm1
   1.04 │       vpand        ymm5,ymm5,ymm7
   0.93 │       vperm2i128   ymm7,ymm6,ymm2,0x21
   0.98 │       vpalignr     ymm7,ymm7,ymm6,0x1
   1.21 │       vpcmpeqb     ymm6,ymm0,ymm6
   1.51 │       vpcmpeqb     ymm7,ymm7,ymm1
   1.23 │       vpand        ymm6,ymm6,ymm7
   3.14 │       vpor         ymm7,ymm5,ymm6
   1.50 │       vpor         ymm7,ymm8,ymm7
  19.06 │       vptest       ymm7,ymm7
   9.21 │     ↓ jne          140
   8.78 │       lea          r8,[rsi+0x80]
   8.29 │       add          rsi,0x120
   8.92 │       cmp          rsi,rax
   0.56 │       mov          rsi,r8
   0.62 │     ↑ jbe          40
Which also stalls on
vtest
, albeit less frequently.
1.2.4. AVX512 (AVX-512F + AVX-512BW + AVX-512VBMI) implementation.
⌗
Straightforward translation using
_mm512_permutex2var_epi8
yields us:
The
perf
profiling output tells us that we may have overdone a little with the vector width, but the stall persists:
Percent │      mov          rax,rsi
   0.01 │      cmp          rsi,0x2
        │    ↓ jb           7b
   0.01 │      movzx        ecx,dx
   0.02 │      shr          ecx,0x8
        │      cmp          rax,0x80
        │    ↓ jb           7f
   0.01 │      vmovdqu64    zmm2,ZMMWORD PTR [rdi]
   0.25 │      vpbroadcastb zmm0,edx
   0.04 │      vpbroadcastb zmm1,ecx
   0.01 │      xor          r8d,r8d
        │      nop
   4.02 │30:   vmovdqa64    zmm3,zmm2
   4.02 │      vmovdqu64    zmm2,ZMMWORD PTR [rdi+r8*1+0x40]
   4.52 │      vpcmpeqb     k0,zmm0,zmm3
   4.48 │      valignq      zmm4,zmm2,zmm3,0x2
   6.98 │      vpalignr     zmm4,zmm4,zmm3,0x1
   7.18 │      vpcmpeqb     k1,zmm4,zmm1
  20.62 │      ktestq       k0,k1
   9.31 │    ↓ jne          b0
   9.61 │      lea          rsi,[r8+0x40]
   6.78 │      add          r8,0xc0
   6.66 │      cmp          r8,rax
   0.73 │      mov          r8,rsi
   0.76 │    ↑ jbe          30
   0.09 │      lea          r8,[rsi+0x1]
   0.05 │      cmp          r8,rax
        │    ↓ jb           8a
   0.12 │7b:   vzeroupper
   0.01 │    ← ret
   0.02 │7f:   xor          esi,esi
        │      lea          r8,[rsi+0x1]
   0.01 │      cmp          r8,rax
        │    ↑ jae          7b
   0.03 │8a:   lea          r8,[rax-0x1]
   0.04 │    ↓ jmp          98
   2.39 │90:   inc          rsi
   1.90 │      cmp          r8,rsi
        │    ↑ je           7b
   6.05 │98:   cmp          BYTE PTR [rdi+rsi*1],dl
        │    ↑ jne          90
   0.12 │      movzx        r9d,BYTE PTR [rdi+rsi*1+0x1]
   0.11 │      cmp          cx,r9w
        │    ↑ jne          90
        │      mov          rax,rsi
        │      vzeroupper
        │    ← ret
   1.49 │b0:   kandq        k0,k0,k1
   1.09 │      kmovq        rax,k0
   0.47 │      tzcnt        rax,rax
        │      add          rax,r8
   0.01 │      vzeroupper
   0.01 │    ← ret
Perhaps interestingly, the AVX-512 implementation seems to not incur too much code bloat:
We also observe a significant performance boost over AVX2:
With the target feature that discourages the compiler from splitting permutex2var into multiple instructions, we see the assembly output:
Without major performance improvements.
1.3. Exact match of a pair of characters in non-overlapping regions.
⌗
This is an easier but less useful problem (applicable only to
wmemchr
or related problems). Essentially, all of our solutions are derivative of the previous
memchr
implementations, except we operate on two-byte chunks directly.
1.3.1. Baseline and SWAR implementations.
⌗
Three preliminary implementations (simple, SWAR,
repne scasw
) follow:
Benchmarks show:
Unsurprisingly, as we have remarked previously,
repne scasw
is not competitive here due to the missing microcode. The SWAR version is the fastest, but only marginally so. More significant performance improvements will be obtained using SIMD techniques, similar to those used in the previous section.
1.3.2. SIMD implementations.
⌗
The only issue with porting the previous
memchr
SIMD implementations to
wmemchr
is that we have to deal with 16-bit elements instead of 8-bit ones in the
_mm_movemask_epi8
instruction. This means that we have to adjust the way we compute the positions from the comparison results.
The final benchmarks look like this:
We leave the problem be here, as we believe the problem to be memory-beyond this point.
1.4. Exact match of a triplet of consecutive characters.
⌗
Matching triplets is of particular interest to us and poses a challenge:
There isn’t a single instruction to load a triplet from memory, unlike before.
Naive scaling of the 16-bit variant will increase the volume of code and provide strictly worse performance.
The needle is staring to become large enough to stack the statistics within random data against us.
Because at this length the concrete underlying distribution of substrings in the input data matters, we will conduct two benchmarks: one with uniformly random data, and another with a prefix of
enwik8
, 100MB of Wikipedia in XML format.
1.4.1. Baseline and SWAR implementations.
⌗
We once again compare the “rolling read” and baseline approaches:
Benchmarks show that the rolling read approach (
musl
-like) still isn’t worth the effort here; Zen2 benchmarks show:
Moving on to the SWAR implementation, we have three choices that make assumptions about the underlying distribution: test all bytes (most general, also most overhead on the hot path, no false positives), test only the first and last bytes (moderate overhead, some false positives), and test only the middle byte (least overhead, most false positives). We implement all three without excessive commentary:
The runtimes suggest that for real data, searching the first and last bytes is the best compromise:
Conversely, because the random data is, well, random, checking only the first byte is the best option there as it filters out most candidates with minimal overhead.
1.4.2. SSE searcher.
⌗
We will naively extend the unaligned load idea from before:
We see the following performance characteristics:
The SSSE3 versions (basic, unrolled) which avoid excessive loads still do not prove themselves worthwhile:
NOINLINE size_t
memchr3_ssse3_bmi1
(
const
void
*
ptr
,
size_t n
,
uint32_t
needle
)
{
const
uint8_t
*
p
=
(
const
uint8_t
*
)
ptr
;
if
(
n
<
3
)
return
n
;
const
uint8_t
b0
=
(
uint8_t
)
needle
;
const
uint8_t
b1
=
(
uint8_t
)
(
needle
>>
8
)
;
const
uint8_t
b2
=
(
uint8_t
)
(
needle
>>
16
)
;
const
__m128i v0
=
_mm_set1_epi8
(
(
char
)
b0
)
;
const
__m128i v1
=
_mm_set1_epi8
(
(
char
)
b1
)
;
const
__m128i v2
=
_mm_set1_epi8
(
(
char
)
b2
)
;
size_t i
=
0
;
if
(
n
>=
32
)
{
__m128i A
=
_mm_loadu_si128
(
(
const
__m128i
*
)
(
p
+
0
)
)
;
for
(
;
i
+
32
<=
n
;
i
+=
16
)
{
__m128i N
=
_mm_loadu_si128
(
(
const
__m128i
*
)
(
p
+
i
+
16
)
)
;
__m128i B1
=
_mm_alignr_epi8
(
N
,
A
,
1
)
;
__m128i B2
=
_mm_alignr_epi8
(
N
,
A
,
2
)
;
__m128i eq0
=
_mm_cmpeq_epi8
(
A
,
v0
)
;
__m128i eq1
=
_mm_cmpeq_epi8
(
B1
,
v1
)
;
__m128i eq2
=
_mm_cmpeq_epi8
(
B2
,
v2
)
;
__m128i m01
=
_mm_and_si128
(
eq0
,
eq1
)
;
__m128i both
=
_mm_and_si128
(
m01
,
eq2
)
;
unsigned
mask
=
(
unsigned
)
_mm_movemask_epi8
(
both
)
;
if
(
mask
)
return
i
+
(
size_t
)
_tzcnt_u32
(
mask
)
;
A
=
N
;
}
}
for
(
;
i
+
2
<
n
;
++
i
)
{
if
(
p
[
i
]
==
b0
&&
p
[
i
+
1
]
==
b1
&&
p
[
i
+
2
]
==
b2
)
return
i
;
}
return
n
;
}
static
inline
unsigned
mask3_ssse3
(
__m128i A
,
__m128i B
,
__m128i v0
,
__m128i v1
,
__m128i v2
)
{
__m128i B1
=
_mm_alignr_epi8
(
B
,
A
,
1
)
;
__m128i B2
=
_mm_alignr_epi8
(
B
,
A
,
2
)
;
__m128i m
=
_mm_and_si128
(
_mm_and_si128
(
_mm_cmpeq_epi8
(
A
,
v0
)
,
_mm_cmpeq_epi8
(
B1
,
v1
)
)
,
_mm_cmpeq_epi8
(
B2
,
v2
)
)
;
return
(
unsigned
)
_mm_movemask_epi8
(
m
)
;
}
NOINLINE size_t
memchr3_ssse3_fast
(
const
void
*
ptr
,
size_t n
,
uint32_t
needle
)
{
const
uint8_t
*
p
=
(
const
uint8_t
*
)
ptr
;
if
(
n
<
3
)
return
n
;
const
uint8_t
b0
=
(
uint8_t
)
needle
;
const
uint8_t
b1
=
(
uint8_t
)
(
needle
>>
8
)
;
const
uint8_t
b2
=
(
uint8_t
)
(
needle
>>
16
)
;
const
__m128i v0
=
_mm_set1_epi8
(
(
char
)
b0
)
;
const
__m128i v1
=
_mm_set1_epi8
(
(
char
)
b1
)
;
const
__m128i v2
=
_mm_set1_epi8
(
(
char
)
b2
)
;
size_t i
=
0
;
if
(
n
>=
32
)
{
__m128i A
=
_mm_loadu_si128
(
(
const
__m128i
*
)
(
p
+
0
)
)
;
i
=
0
;
for
(
;
i
+
80
<=
n
;
i
+=
64
)
{
__m128i B
=
_mm_loadu_si128
(
(
const
__m128i
*
)
(
p
+
i
+
16
)
)
;
__m128i C
=
_mm_loadu_si128
(
(
const
__m128i
*
)
(
p
+
i
+
32
)
)
;
__m128i D
=
_mm_loadu_si128
(
(
const
__m128i
*
)
(
p
+
i
+
48
)
)
;
__m128i E
=
_mm_loadu_si128
(
(
const
__m128i
*
)
(
p
+
i
+
64
)
)
;
unsigned
m0
=
mask3_ssse3
(
A
,
B
,
v0
,
v1
,
v2
)
;
unsigned
m1
=
mask3_ssse3
(
B
,
C
,
v0
,
v1
,
v2
)
;
unsigned
m2
=
mask3_ssse3
(
C
,
D
,
v0
,
v1
,
v2
)
;
unsigned
m3
=
mask3_ssse3
(
D
,
E
,
v0
,
v1
,
v2
)
;
if
(
m0
|
m1
|
m2
|
m3
)
{
if
(
m0
)
return
i
+
0
+
(
size_t
)
_tzcnt_u32
(
m0
)
;
if
(
m1
)
return
i
+
16
+
(
size_t
)
_tzcnt_u32
(
m1
)
;
if
(
m2
)
return
i
+
32
+
(
size_t
)
_tzcnt_u32
(
m2
)
;
return
i
+
48
+
(
size_t
)
_tzcnt_u32
(
m3
)
;
}
A
=
E
;
}
for
(
;
i
+
32
<=
n
;
i
+=
16
)
{
__m128i B
=
_mm_loadu_si128
(
(
const
__m128i
*
)
(
p
+
i
+
16
)
)
;
unsigned
m
=
mask3_ssse3
(
A
,
B
,
v0
,
v1
,
v2
)
;
if
(
m
)
return
i
+
(
size_t
)
_tzcnt_u32
(
m
)
;
A
=
B
;
}
}
for
(
;
i
+
2
<
n
;
++
i
)
{
if
(
p
[
i
]
==
b0
&&
p
[
i
+
1
]
==
b1
&&
p
[
i
+
2
]
==
b2
)
return
i
;
}
return
n
;
}
Giving:
However, we can once again re-use the idea of checking the first and last positions as a pre-filter, and together with some unrolling attain better performance:
The performance has improved and the code has no glaring red stall spots as evidenced by
perf
, hence we are satisfied with the following outcomes:
1.4.3. AVX2 searcher.
⌗
We simply widen the SSE2 approach to AVX2 and use the same solution as before to the problem of lane-wise operations:
NOINLINE size_t
memchr3_avx2_prefilter_bmi1
(
const
void
*
ptr
,
size_t n
,
uint32_t
needle
)
{
const
uint8_t
*
p
=
(
const
uint8_t
*
)
ptr
;
if
(
n
<
3
)
return
n
;
const
uint8_t
b0
=
(
uint8_t
)
(
needle
)
;
const
uint8_t
b1
=
(
uint8_t
)
(
needle
>>
8
)
;
const
uint8_t
b2
=
(
uint8_t
)
(
needle
>>
16
)
;
const
__m256i v0
=
_mm256_set1_epi8
(
(
char
)
b0
)
;
const
__m256i v1
=
_mm256_set1_epi8
(
(
char
)
b1
)
;
const
__m256i v2
=
_mm256_set1_epi8
(
(
char
)
b2
)
;
size_t i
=
0
;
uintptr_t mis
=
(
uintptr_t
)
p
&
31u
;
if
(
mis
)
{
size_t lim
=
32u
-
(
size_t
)
mis
;
if
(
lim
>
n
)
lim
=
n
;
for
(
;
i
<
lim
&&
i
+
2
<
n
;
++
i
)
{
if
(
p
[
i
]
==
b0
&&
p
[
i
+
1
]
==
b1
&&
p
[
i
+
2
]
==
b2
)
return
i
;
}
if
(
i
+
2
>=
n
)
return
n
;
}
const
uint8_t
*
q
=
p
+
i
;
size_t m
=
n
-
i
;
if
(
m
>=
64
)
{
__m256i A
=
_mm256_load_si256
(
(
const
__m256i
*
)
(
const
void
*
)
q
)
;
size_t j
=
0
;
for
(
;
j
+
128
<=
m
;
j
+=
128
)
{
__m256i N0
=
_mm256_load_si256
(
(
const
__m256i
*
)
(
const
void
*
)
(
q
+
j
+
32
)
)
;
__m256i X0
=
_mm256_permute2x128_si256
(
A
,
N0
,
0x21
)
;
__m256i B10
=
_mm256_alignr_epi8
(
X0
,
A
,
1
)
;
__m256i B20
=
_mm256_alignr_epi8
(
X0
,
A
,
2
)
;
unsigned
m0
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
A
,
v0
)
)
;
unsigned
m2
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B20
,
v2
)
)
;
unsigned
cand
=
m0
&
m2
;
if
(
cand
)
{
unsigned
m1
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B10
,
v1
)
)
;
unsigned
hit
=
cand
&
m1
;
if
(
hit
)
return
i
+
j
+
(
size_t
)
_tzcnt_u32
(
hit
)
;
}
__m256i A1
=
N0
;
__m256i N1
=
_mm256_load_si256
(
(
const
__m256i
*
)
(
const
void
*
)
(
q
+
j
+
64
)
)
;
__m256i X1
=
_mm256_permute2x128_si256
(
A1
,
N1
,
0x21
)
;
__m256i B11
=
_mm256_alignr_epi8
(
X1
,
A1
,
1
)
;
__m256i B21
=
_mm256_alignr_epi8
(
X1
,
A1
,
2
)
;
m0
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
A1
,
v0
)
)
;
m2
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B21
,
v2
)
)
;
cand
=
m0
&
m2
;
if
(
cand
)
{
unsigned
m1
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B11
,
v1
)
)
;
unsigned
hit
=
cand
&
m1
;
if
(
hit
)
return
i
+
j
+
32
+
(
size_t
)
_tzcnt_u32
(
hit
)
;
}
__m256i A2
=
N1
;
__m256i N2
=
_mm256_load_si256
(
(
const
__m256i
*
)
(
const
void
*
)
(
q
+
j
+
96
)
)
;
__m256i X2
=
_mm256_permute2x128_si256
(
A2
,
N2
,
0x21
)
;
__m256i B12
=
_mm256_alignr_epi8
(
X2
,
A2
,
1
)
;
__m256i B22
=
_mm256_alignr_epi8
(
X2
,
A2
,
2
)
;
m0
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
A2
,
v0
)
)
;
m2
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B22
,
v2
)
)
;
cand
=
m0
&
m2
;
if
(
cand
)
{
unsigned
m1
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B12
,
v1
)
)
;
unsigned
hit
=
cand
&
m1
;
if
(
hit
)
return
i
+
j
+
64
+
(
size_t
)
_tzcnt_u32
(
hit
)
;
}
__m256i A3
=
N2
;
__m256i N3
=
_mm256_load_si256
(
(
const
__m256i
*
)
(
const
void
*
)
(
q
+
j
+
128
)
)
;
__m256i X3
=
_mm256_permute2x128_si256
(
A3
,
N3
,
0x21
)
;
__m256i B13
=
_mm256_alignr_epi8
(
X3
,
A3
,
1
)
;
__m256i B23
=
_mm256_alignr_epi8
(
X3
,
A3
,
2
)
;
m0
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
A3
,
v0
)
)
;
m2
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B23
,
v2
)
)
;
cand
=
m0
&
m2
;
if
(
cand
)
{
unsigned
m1
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B13
,
v1
)
)
;
unsigned
hit
=
cand
&
m1
;
if
(
hit
)
return
i
+
j
+
96
+
(
size_t
)
_tzcnt_u32
(
hit
)
;
}
A
=
N3
;
}
for
(
;
j
+
64
<=
m
;
j
+=
32
)
{
__m256i N
=
_mm256_load_si256
(
(
const
__m256i
*
)
(
const
void
*
)
(
q
+
j
+
32
)
)
;
__m256i X
=
_mm256_permute2x128_si256
(
A
,
N
,
0x21
)
;
__m256i B1
=
_mm256_alignr_epi8
(
X
,
A
,
1
)
;
__m256i B2
=
_mm256_alignr_epi8
(
X
,
A
,
2
)
;
unsigned
m0
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
A
,
v0
)
)
;
unsigned
m2
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B2
,
v2
)
)
;
unsigned
cand
=
m0
&
m2
;
if
(
cand
)
{
unsigned
m1
=
(
unsigned
)
_mm256_movemask_epi8
(
_mm256_cmpeq_epi8
(
B1
,
v1
)
)
;
unsigned
hit
=
cand
&
m1
;
if
(
hit
)
return
i
+
j
+
(
size_t
)
_tzcnt_u32
(
hit
)
;
}
A
=
N
;
}
i
+=
j
;
}
for
(
;
i
+
2
<
n
;
++
i
)
if
(
p
[
i
]
==
b0
&&
p
[
i
+
1
]
==
b1
&&
p
[
i
+
2
]
==
b2
)
return
i
;
return
n
;
}
The results are still underwhelming:
α. Fun House
⌗
While we’re at re-implementing a couple of libc methods, why not
strfry
? This function randomizes the order of characters in a string via a Fisher-Yates shuffle.
It has been reported
that glibc’s implementation is suboptimal and the distribution of characters is not uniform. Later on in the thread,
we learn that Ulrich Drepper’s mother was a hamster, while his father smells of elderberries
.
We opt in for an approach based on
rdseed
mixed together with clever use of AES-NI to generate high-quality uniformly random numbers at a good speed, followed by a binary algorithm for sampling indices in range
[0..n)
without modulo bias or the general slowness of Lemire’s method.
static
ALWAYS_INLINE
uint64_t
rdseed64
(
void
)
{
uint64_t
x
;
while
(
_rdseed64_step
(
&
x
)
==
0
)
{
}
return
x
;
}
#
define
aes128_keyassist
(
key
,
rcon
)
\
(
{
\
__m128i tmp
=
_mm_aeskeygenassist_si128
(
(
key
)
,
(
rcon
)
)
;
\
tmp
=
_mm_shuffle_epi32
(
(
tmp
)
,
_MM_SHUFFLE
(
3
,
3
,
3
,
3
)
)
;
\
__m128i k
=
(
key
)
;
\
k
=
_mm_xor_si128
(
(
k
)
,
_mm_slli_si128
(
(
k
)
,
4
)
)
;
\
k
=
_mm_xor_si128
(
(
k
)
,
_mm_slli_si128
(
(
k
)
,
4
)
)
;
\
k
=
_mm_xor_si128
(
(
k
)
,
_mm_slli_si128
(
(
k
)
,
4
)
)
;
\
_mm_xor_si128
(
(
k
)
,
(
tmp
)
)
;
\
}
)
static
ALWAYS_INLINE
void
aes128_expand_key
(
__m128i rk
[
11
]
,
__m128i key
)
{
rk
[
0
]
=
key
;
rk
[
1
]
=
aes128_keyassist
(
rk
[
0
]
,
0x01
)
;
rk
[
2
]
=
aes128_keyassist
(
rk
[
1
]
,
0x02
)
;
rk
[
3
]
=
aes128_keyassist
(
rk
[
2
]
,
0x04
)
;
rk
[
4
]
=
aes128_keyassist
(
rk
[
3
]
,
0x08
)
;
rk
[
5
]
=
aes128_keyassist
(
rk
[
4
]
,
0x10
)
;
rk
[
6
]
=
aes128_keyassist
(
rk
[
5
]
,
0x20
)
;
rk
[
7
]
=
aes128_keyassist
(
rk
[
6
]
,
0x40
)
;
rk
[
8
]
=
aes128_keyassist
(
rk
[
7
]
,
0x80
)
;
rk
[
9
]
=
aes128_keyassist
(
rk
[
8
]
,
0x1B
)
;
rk
[
10
]
=
aes128_keyassist
(
rk
[
9
]
,
0x36
)
;
}
static
ALWAYS_INLINE __m128i
aes128_encrypt_block
(
const
__m128i rk
[
11
]
,
__m128i in
)
{
__m128i x
=
_mm_xor_si128
(
in
,
rk
[
0
]
)
;
x
=
_mm_aesenc_si128
(
x
,
rk
[
1
]
)
;
x
=
_mm_aesenc_si128
(
x
,
rk
[
2
]
)
;
x
=
_mm_aesenc_si128
(
x
,
rk
[
3
]
)
;
x
=
_mm_aesenc_si128
(
x
,
rk
[
4
]
)
;
x
=
_mm_aesenc_si128
(
x
,
rk
[
5
]
)
;
x
=
_mm_aesenc_si128
(
x
,
rk
[
6
]
)
;
x
=
_mm_aesenc_si128
(
x
,
rk
[
7
]
)
;
x
=
_mm_aesenc_si128
(
x
,
rk
[
8
]
)
;
x
=
_mm_aesenc_si128
(
x
,
rk
[
9
]
)
;
x
=
_mm_aesenclast_si128
(
x
,
rk
[
10
]
)
;
return
x
;
}
typedef
struct
{
__m128i rk
[
11
]
;
uint64_t
ctr_lo
,
ctr_hi
;
uint32_t
buf
[
4
]
;
int
idx
;
}
aesctr_rng_t
;
static
ALWAYS_INLINE
void
aesctr_init_rdseed
(
aesctr_rng_t
*
g
)
{
uint64_t
k0
=
rdseed64
(
)
,
k1
=
rdseed64
(
)
;
uint64_t
c0
=
rdseed64
(
)
,
c1
=
rdseed64
(
)
;
__m128i key
=
_mm_set_epi64x
(
(
long
long
)
k1
,
(
long
long
)
k0
)
;
aes128_expand_key
(
g
->
rk
,
key
)
;
g
->
ctr_lo
=
c0
;
g
->
ctr_hi
=
c1
;
g
->
idx
=
4
;
}
static
ALWAYS_INLINE
void
aesctr_refill
(
aesctr_rng_t
*
g
)
{
__m128i ctr
=
_mm_set_epi64x
(
(
long
long
)
g
->
ctr_hi
,
(
long
long
)
g
->
ctr_lo
)
;
__m128i block
=
aes128_encrypt_block
(
g
->
rk
,
ctr
)
;
g
->
ctr_lo
++
;
if
(
g
->
ctr_lo
==
0
)
g
->
ctr_hi
++
;
_mm_storeu_si128
(
(
__m128i
*
)
g
->
buf
,
block
)
;
g
->
idx
=
0
;
}
static
ALWAYS_INLINE
uint32_t
aesctr_u32
(
aesctr_rng_t
*
g
)
{
if
(
g
->
idx
>=
4
)
aesctr_refill
(
g
)
;
return
g
->
buf
[
g
->
idx
++
]
;
}
static
ALWAYS_INLINE
uint32_t
bounded_mask
(
aesctr_rng_t
*
g
,
uint32_t
bound
)
{
if
(
bound
<=
1
)
return
0
;
uint32_t
range
=
bound
-
1
;
uint32_t
mask
=
~
0u
;
mask
>>=
__builtin_clz
(
range
|
1u
)
;
uint32_t
x
;
do
{
x
=
aesctr_u32
(
g
)
&
mask
;
}
while
(
x
>
range
)
;
return
x
;
}
void
strfry_bytes
(
uint8_t
*
a
,
size_t n
)
{
if
(
n
<=
1
)
return
;
if
(
n
-
1
>
UINT32_MAX
)
return
;
aesctr_rng_t g
;
aesctr_init_rdseed
(
&
g
)
;
for
(
size_t i
=
n
-
1
;
i
>
0
;
--
i
)
{
uint32_t
j
=
bounded_mask
(
&
g
,
(
uint32_t
)
(
i
+
1
)
)
;
uint8_t
tmp
=
a
[
i
]
;
a
[
i
]
=
a
[
j
]
;
a
[
j
]
=
tmp
;
}
}
char
*
strfry
(
char
*
s
)
{
size_t n
=
strlen
(
s
)
;
strfry_bytes
(
(
uint8_t
*
)
s
,
n
)
;
return
s
;
}
Benchmarking against
glibc
is pointless (it’s not uniform, not fast and not “secure”). We can probe for uniformity using Lehmer codes; a base-64 alphabet that counts permutations by index shows us some concrete data:
Our code could be adapted to shuffle objects of any size, but since this is a simple exercise in programming, we leave this to the reader. Other interesting functions that we may tackle in the future are
strtok
,
strspn
,
strrchr
,
strpbrk
or
memcmp
.
In the next post, we will be looking more closely into longer (>= 4 bytes), sparser (as in, matching with gaps) and finer (non-overlapping 2-bit or 4-bit sequences, useful in Bioinformatics) needles before moving on to string algorithms based on suffix trees, suffix arrays and the BWT and the FM-index in part three.
