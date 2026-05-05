---
title: "How a String Library Beat OpenCV at Image Processing by 4x"
url: "https://ashvardanian.com/posts/image-processing-with-strings/"
fetched_at: 2026-05-05T07:01:49.165229+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# How a String Library Beat OpenCV at Image Processing by 4x

Source: https://ashvardanian.com/posts/image-processing-with-strings/

To my great surprise, one of the biggest current users of my
StringZilla
library in the Python ecosystem is one of the world’s most widely used Image Augmentation libraries -
Albumentations
with over 100 million downloads on PyPI, growing by 5 million every month.
Last year, Albumentations swapped parts of OpenCV - the world’s most widely used image processing library with 32 million monthly downloads in Python - for my strings library 🤯
The reason for that surprising move?
The quality of Look-Up Tables (LUTs) implementation in StringZilla.
What are LUTs?
#
A LUT is simply a 256-byte array where each byte value (0-255) maps to another byte value.
In Python, you’d implement it naively like this:
1
2
3
4
5
6
# Create a LUT for inverting pixel values
lut
=
bytes
(
255
-
i
for
i
in
range
(
256
))
# Apply it to an image (slow way)
for
i
in
range
(
len
(
image
)):
image
[
i
]
=
lut
[
image
[
i
]]
LUTs are everywhere in image processing: gamma correction, histogram equalization, color channel swapping, threshold operations.
Here’s how you’d apply one in practice:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
# Create a gamma correction LUT
import
numpy
as
np
gamma
=
2.2
lut
=
np
.
array
([((
i
/
255.0
)
**
(
1.0
/
gamma
))
*
255
for
i
in
range
(
256
)])
.
astype
(
np
.
uint8
)
# Load an image & correct with OpenCV
import
cv2
image
=
cv2
.
imread
(
'photo.jpg'
,
cv2
.
IMREAD_GRAYSCALE
)
corrected
=
cv2
.
LUT
(
image
,
lut
)
# Do the same with StringZilla
import
stringzilla
as
sz
corrected
=
sz
.
translate
(
image
.
tobytes
(),
bytes
(
lut
))
I’ve implemented those in StringZilla for byte-level mappings, like a generic foundation for
to_lower
and
to_upper
string operations and translating biological alphabets, like
ACGT
to
TGCA
for
DNA complements
or to ${0,1,2,3}$ for efficient storage and processing.
Performance Comparison
#
The newer your hardware - the bigger the performance gap compared to OpenCV, the industry standard for image processing.
Running on server-grade Intel Sapphire Rapids and consumer-grade Apple M2 Pro CPUs, one may expect the following results:
Library
Intel Sapphire Rapids
Apple M2 Pro
Short Words
Long Lines
Short Words
Long Lines
Rust 🦀
to[i] = lut[from[i]]
0.61 GiB/s
1.49 GiB/s
0.16 GiB/s
3.57 GiB/s
stringzilla::lookup_inplace
0.54 GiB/s
9.90 GiB/s
0.19 GiB/s
9.38 GiB/s
Python 🐍
bytes.translate
0.05 GiB/s
1.92 GiB/s
0.08 GiB/s
2.52 GiB/s
numpy.take
0.01 GiB/s
0.85 GiB/s
0.01 GiB/s
0.47 GiB/s
opencv.LUT
0.01 GiB/s
1.95 GiB/s
0.01 GiB/s
1.60 GiB/s
opencv.LUT
inplace
0.01 GiB/s
2.16 GiB/s
0.02 GiB/s
1.97 GiB/s
stringzilla.translate
0.07 GiB/s
7.92 GiB/s
0.07 GiB/s
7.49 GiB/s
stringzilla.translate
inplace
0.06 GiB/s
8.14 GiB/s
0.03 GiB/s
4.87 GiB/s
Words are around 8.5 bytes long on average.
Lines are typically around 4 KB long.
The benchmarks show throughput in Gigabytes per second - higher is better.
The source of this gap?
As with many performance wins I write about, it’s the clever use of SIMD instructions.
SIMD (
Single Instruction, Multiple Data
) lets modern CPUs process multiple bytes in parallel—
AVX-512
handles 64 bytes at once on Intel, while
ARM NEON
processes 16 bytes.
LUTs on Intel Ice Lake and Newer
#
For full code, refer to
sz_lookup_ice
in StringZilla’s source.
On Intel’s
Ice Lake CPUs
and newer,
AVX512_VBMI
(Vector Byte Manipulation Instructions) introduces several convenient instructions for LUTs.
Most importantly, the
VPERMB
instruction, which can do 64 parallel byte lookups from a 64-byte table.
For a 256-entry alphabet, we need 4 such lookups combined with several other instructions:
4x
_mm512_permutexvar_epi8
maps to
VPERMB (ZMM, ZMM, ZMM)
:
On Intel Ice Lake: 3 cycles latency, on port 5
On AMD Genoa: 6 cycles latency, on ports 1 and 2
3x
_mm512_mask_blend_epi8
maps to
VPBLENDMB_Z (ZMM, K, ZMM, ZMM)
:
On Intel Ice Lake: 3 cycles latency, on ports 0 and 5
On AMD Genoa: 1 cycle latency, on ports 0, 1, 2, and 3
2x
_mm512_test_epi8_mask
maps to
VPTESTMB (K, ZMM, ZMM)
:
On Intel Ice Lake: 3 cycles latency, on port 5
On AMD Genoa: 4 cycles latency, on ports 0 and 1
Here’s how the algorithm works:
LUT Partitioning
: Split the 256-byte LUT into four 64-byte segments
Bit Testing
: Use the top 2 bits of each byte to determine which segment to use
Parallel Lookups
: Perform lookups in all four segments simultaneously
Selective Blending
: Use mask operations to mix parts of different segments
Which roughly translates into this C code:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
// Parallel lookups in all four LUT segments
lookup_0_to_63_vec
.
zmm
=
_mm512_permutexvar_epi8
(
source_vec
.
zmm
,
lut_0_to_63_vec
.
zmm
);
lookup_64_to_127_vec
.
zmm
=
_mm512_permutexvar_epi8
(
source_vec
.
zmm
,
lut_64_to_127_vec
.
zmm
);
lookup_128_to_191_vec
.
zmm
=
_mm512_permutexvar_epi8
(
source_vec
.
zmm
,
lut_128_to_191_vec
.
zmm
);
lookup_192_to_255_vec
.
zmm
=
_mm512_permutexvar_epi8
(
source_vec
.
zmm
,
lut_192_to_255_vec
.
zmm
);
// Test bits to determine which segment to use
first_bit_mask
=
_mm512_test_epi8_mask
(
source_vec
.
zmm
,
first_bit_vec
.
zmm
);
second_bit_mask
=
_mm512_test_epi8_mask
(
source_vec
.
zmm
,
second_bit_vec
.
zmm
);
// Hierarchical blending to select correct results
blended_0_to_127_vec
.
zmm
=
_mm512_mask_blend_epi8
(
second_bit_mask
,
lookup_0_to_63_vec
.
zmm
,
lookup_64_to_127_vec
.
zmm
);
blended_128_to_255_vec
.
zmm
=
_mm512_mask_blend_epi8
(
second_bit_mask
,
lookup_128_to_191_vec
.
zmm
,
lookup_192_to_255_vec
.
zmm
);
blended_0_to_255_vec
.
zmm
=
_mm512_mask_blend_epi8
(
first_bit_mask
,
blended_0_to_127_vec
.
zmm
,
blended_128_to_255_vec
.
zmm
);
Optimizing for Small and Large Inputs
#
For small inputs, the idea is simple - avoid the overhead of setting up AVX-512 state, and fall back to serial code.
This also helps prevent CPU energy state transitions that can add latency.
For larger inputs, we want to ensure our main loop uses aligned stores to maximize throughput.
Emphasis on “stores”-unaligned reads are rarely a bottleneck on modern CPUs:
1
2
3
// Calculate head and tail lengths for alignment
sz_size_t
head_length
=
(
64
-
((
sz_size_t
)
target
%
64
))
%
64
;
sz_size_t
tail_length
=
(
sz_size_t
)(
target
+
length
)
%
64
;
This approach processes:
Head
: Unaligned portion at the beginning using masked operations
Body
: 64-byte aligned chunks using slightly faster aligned stores
Tail
: Remaining unaligned bytes at the end using masked operations
Those masked operations are becoming the new norm, present both in x86 starting with Skylake, on Arm, starting with SVE, and even RISC-V with V extension.
LUTs in Arm NEON
#
For full code, refer to
sz_lookup_neon
in StringZilla’s source.
ARM’s
NEON
implementation is simpler than x86.
NEON is ARM’s SIMD extension, available on virtually all modern ARM processors including Apple Silicon, Android phones, and AWS Graviton servers.
We don’t have 512-bit registers on most Arm systems (except for the SVE-capable
Fujitsu A64FX
), but that’s not our target platform.
Still, there is a logical abstraction for 4x 128-bit vectors, called
uint8x16x4_t
, which is perfect for our 256-byte LUT.
A potential challenge with NEON is
register pressure
.
AArch64 provides 32 vector registers of 128 bits each (only 512 bytes in total), while our algorithm uses:
4x
uint8x16x4_t
or 16x
uint8x16_t
for LUT
4x source values, 3x masks, 3x intermediaries
3x blend registers
So we fit within the 32-register limit anyway, but even if we didn’t-it wouldn’t be a big deal.
The physical register file can be 10x larger than the architectural one, but that’s a topic for another post.
Without overcomplicating things, the main body translation loop (excluding misaligned head and tail) is:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
// Load 256-byte LUT into 16 NEON registers
uint8x16x4_t
lut_0_to_63_vec
=
vld1q_u8_x4
(
lut
+
0
);
uint8x16x4_t
lut_64_to_127_vec
=
vld1q_u8_x4
(
lut
+
64
);
uint8x16x4_t
lut_128_to_191_vec
=
vld1q_u8_x4
(
lut
+
128
);
uint8x16x4_t
lut_192_to_255_vec
=
vld1q_u8_x4
(
lut
+
192
);
// Core lookup loop - 16 bytes per iteration
source_vec
.
u8x16
=
vld1q_u8
(
source
);
lookup_0_to_63_vec
.
u8x16
=
vqtbl4q_u8
(
lut_0_to_63_vec
,
source_vec
.
u8x16
);
lookup_64_to_127_vec
.
u8x16
=
vqtbl4q_u8
(
lut_64_to_127_vec
,
veorq_u8
(
source_vec
.
u8x16
,
vdupq_n_u8
(
0x40
)));
lookup_128_to_191_vec
.
u8x16
=
vqtbl4q_u8
(
lut_128_to_191_vec
,
veorq_u8
(
source_vec
.
u8x16
,
vdupq_n_u8
(
0x80
)));
lookup_192_to_255_vec
.
u8x16
=
vqtbl4q_u8
(
lut_192_to_255_vec
,
veorq_u8
(
source_vec
.
u8x16
,
vdupq_n_u8
(
0xc0
)));
// Combine results from all four lookups
blended_0_to_255_vec
.
u8x16
=
vorrq_u8
(
//
vorrq_u8
(
lookup_0_to_63_vec
.
u8x16
,
lookup_64_to_127_vec
.
u8x16
),
vorrq_u8
(
lookup_128_to_191_vec
.
u8x16
,
lookup_192_to_255_vec
.
u8x16
));
vst1q_u8
((
sz_u8_t
*
)
target
,
blended_0_to_255_vec
.
u8x16
);
Daniel Lemire has
discussed similar NEON LUT implementations
, but the variations suggested in the comments don’t yield significant improvements over this approach.
Instead of Conclusion
#
Sometimes, when optimizing code, solutions come from unexpected places.
A string library beating OpenCV at image processing is one such example.
These LUT kernels were integrated into Albumentations alongside other SIMD kernels from
SimSIMD
.
Since then,
StringZilla v4
has grown to include CUDA kernels for GPUs and SVE/SVE2 implementations for newer ARM processors.
The same byte manipulation techniques now accelerate bioinformatics pipelines processing DNA sequences.
4x speedups mean 4x less energy wasted and 4x more we can do with the same hardware.
And if you find that useful, spread the word about
StringZilla
🤗
