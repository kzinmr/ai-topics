---
title: "NumKong: 2'000 Mixed Precision Kernels For All 🦍"
url: "https://ashvardanian.com/posts/numkong/"
fetched_at: 2026-05-05T07:01:49.490759+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# NumKong: 2'000 Mixed Precision Kernels For All 🦍

Source: https://ashvardanian.com/posts/numkong/

I’m killing my
SimSIMD
project and re-launching under a new name — NumKong —
StringZilla
’s big brother.
Around 2'000 SIMD kernels for mixed precision numerics, spread across 200'000 lines of code & docstrings, for 7 programming languages.
One of the larger collections online — comparable to
OpenBLAS
, the default NumPy BLAS (Basic Linear Algebra Subprograms) backend (
detailed comparison below
).
Highlights:
RISC-V Vector Extensions, Intel AMX & Arm SME Tiles
From Vectors to Matrices and Higher-rank Tensors
From BFloat16 and Float16 to Float6 — E3M2 & E2M3 on any CPU
Native Int4 & UInt4 Dot Products via Nibble Algebra
Neumaier & Dot2 for higher-than-BLAS precision
Ozaki Scheme for Float64 GEMMs via Float32 Tile Hardware
Haversine & Vincenty for Geospatial — 5'300x faster than GeoPy
Kabsch & Umeyama Mesh Alignment — 200x faster than BioPython
Fused MaxSim for ColBERT — GPU-Free Late Interaction Scoring
WebAssembly SIMD backend for AI Sandboxes, Edge, & Browsers
C 99, C++ 23, Rust, Swift, JavaScript, GoLang, & Python 🐍
All of that tested against in-house 118-bit floating point numbers and heavily profiled for both numerical stability and speed.
Here’s a preview of performance numbers for the most familiar part — GEMM (General Matrix Multiply)-like batched dot products:
Input
NumPy + OpenBLAS
PyTorch + MKL
NumKong
Float64
65.5 gso/s, 1e-15 err
68.2 gso/s, 1e-15 err
8.6 gso/s, 1e-16 err
Float32
140 gso/s, 9e-7 err
145 gso/s, 1e-6 err
37.7 gso/s, 4e-7 err
BFloat16
—
851 gso/s, 1.8% err
458 gso/s, 3.6% err
Float16
0.3 gso/s, 0.25% err
140 gso/s, 0.37% err
103 gso/s, 0.26% err
Float8
—
0.4 gso/s, 4.6% err
398 gso/s, 0% err
Int8
0.4 gso/s,
overflow
50 gso/s,
overflow
1'279 gso/s, 0% err
Binary Size
30 MB
705 MB
5 MB
Available For
Python
Python, C++
7 languages
Python Wheels
72
39
99
Those are single-threaded numbers for Intel Xeon4 CPUs powering mainstream Nvidia DGX-H100 servers — the workhorse of GenAI in 2025/6.
NumKong makes different tradeoffs around speed vs accuracy, and a big part of the article is about the strategy of prioritizing one above the other.
Backstory
#
The scale wasn’t the hard part — correctness, portability, and UX were.
I started this release 3 years ago, when I first got access to Intel Xeon4 (Sapphire Rapids) CPUs.
I opened the
#220 Pull Request
in 2024… and it’s already 2026.
Around 900 commits in, CI finally passed for the first time; another 200 patches later, it was ready to merge 😅
The original goal was to accelerate Unum’s
USearch
vector search engine, but the library outgrew that scope — projects like
Albumentations
already use it for Image Processing.
The new release is mostly around tiled tensor operations and GPU-era numeric types brought to CPUs, and needed a complete redesign.
Tiled Multiply-Accumulate on Every Chip
#
RISC-V
#
The least mature platform in this story is RISC-V — so let’s start at the bottom and work up.
RISC-V is the open-source Instruction Set Architecture that has made waves online and holds great promise for democratizing chip design.
Even in 2026, it’s still far from usable.
The driving force behind its growing adoption in CPUs (as opposed to external accelerators) isn’t technical merit — it’s growing geopolitical tensions between the US, China, Europe, Russia, and the rest of the world.
Politics aside, what’s the state right now?
Where can we find RISC-V cores and which of those have SIMD (Single Instruction, Multiple Data) extensions like RVV (RISC-V Vector) to enable advanced parallel processing?
Vendor
Availability
Vectors
Notes
Meta
Internal only (MTIA)
Custom
100K+ chips, 16 data centers
Alibaba
Scaleway EU, Alibaba Cloud
0.7.1
C910/C920, €16/mo on Scaleway
Tenstorrent
Koyeb serverless
SFPI
NOT standard RVV
SiFive
Dev boards (X280)
RVV 1.0
Purchase only
QEMU
Local emulation
RVV 1.0
For development
Meanwhile, NVIDIA ships 1B+ RISC-V cores per year embedded in GPUs for power management — not for compute, but a telling sign of the ISA’s reach.
No public cloud offers RVV 1.0 hardware yet — Scaleway’s EM-RV1 with T-Head C910 is the only commercial option, stuck on the draft 0.7.1 spec.
The gap to 1.0 is painful: binary-incompatible encodings, no fractional LMUL, no tail/mask-agnostic policies, different
vsetvl
semantics.
Worse, there’s no ratified matrix extension yet — unlike Intel AMX or Arm SME, you can’t do 2D tiled matmuls, and BFloat16 requires the “Zvfbfwma” extension that C910 doesn’t have.
That said, the instruction set is already humongous — as many have pointed out, “Reduced” doesn’t really belong in “RISC-V”.
Despite all that, RVV does have unique strengths worth exploiting:
vlseg/vsseg
— segment loads that deinterleave AoS (complex numbers, RGB) directly into registers
viota + vcompress
— stream compaction in 3 instructions vs ~10 on AVX-512
vfwredusum
— widening reduction without the horizontal shuffle dance
What does work well:
vfwmacc
for
f16 × f16 → f32
and
vwmacc
for
i8 × i8 → i32
widening dot products.
Even more interesting,
vfwmacc_vv_f64m2
computes
f64 += f32 × f32
in a single instruction with no intermediate rounding — the multiply happens at full Float64 width.
Neither x86 nor SVE has an equivalent; on those ISAs you must widen both operands first, then FMA, eating two extra instructions and an intermediate rounding step.
Here are some of the interesting things that worked on RISC-V better than on other ISAs:
nk_reduce_moments
horizontal accumulations over arbitrarily strided data, where we may be computing the L2 norm of a column in a row-major matrix layout — the RVV kernel may use a combination of
__riscv_vlse32_v_f32m1
strided loads and
__riscv_vfwmacc_vv_f64m2_tu
widening FMA in the hot loop
nk_reduce_minmax
horizontal reductions tracking positions in arbitrary size arrays, where the compared objects and the offsets have clearly different widths — the RVV kernel may use
vfloat32m1_t
for incoming floats and a wider
vuint64m2_t
to track positions
nk_rmsd
,
nk_kabsch
,
nk_umeyama
kernels for computational geometry with applications in Biology and Chemistry leverage RVV’s segmented loads and widening/narrowing logic for tight iterative algorithms like SVD — details in the
mesh alignment section
Thanks to QEMU, I was able to validate all kernels for correctness, but it’s impossible to make throughput claims without hardware.
So let’s switch to more practical cases.
Intel: From AMX on Servers to VNNI on Laptops
#
Intel was the first to bring GPU-style tensor cores to mainstream CPUs.
Advanced Matrix Extensions (or AMX) provide massive 8x 1 KB tile registers (TMMs) and a dedicated TMUL unit for tiled matmuls.
Conceptually similar to scheduling NVIDIA’s tensor cores, but much easier to program.
Xeon4 supports
bf16 × bf16 → f32
and
i8 × i8 → i32
.
Granite Rapids adds
f16 × f16 → f32
.
Some Xeon variants even ship with HBM, further blurring the CPU/GPU line.
1
_tile_dpbf16ps
(
0
,
1
,
2
);
// TMM0 += TMM1 × TMM2 (BFloat16 → Float32)
Important to note, the first and the second multiplication arguments are ordered differently.
More on this in the
GEMMs
section.
For NumKong users, the biggest value of those instructions will come from using:
dots_packed_i8
,
dots_packed_bf16
for BLAS-like GEMMs
dots_symmetric_i8
,
dots_symmetric_bf16
for BLAS-like SYRKs
angulars_packed_bf16
,
euclideans_symmetric_i8
,
angulars_symmetric_e2m3
, and other batched distance calculations and obscure numeric types with overlapping AMX and AVX-512
maxsim_packed_f32
,
maxsim_packed_bf16
for scoring late-interaction
ColBERT
-style document embeddings
For now, those tiled dot-product instructions are limited to server hardware on the x86 side, but not for long.
Intel and AMD are standardizing new ISA extensions that may end up on the consumer chips as well.
Until then, NumKong now has separate backend families for Alder Lake and Sierra Forest CPUs.
Alder Lake and its newer AVX VNNI variants are broadly available on laptops, resulting in up to 2x throughput improvements for heavily quantized USearch indexes compared to the pure AVX2 Haswell baselines.
Sierra Forest brings AVX VNNI variants with symmetric Int8 or UInt8 input pairs, available on servers with up to 144 physical cores and up to 288 cores in a dual-socket configuration.
Apple’s SME — The Best ISA for Mixed-Precision Numerics
#
Ash: What’s the most efficient hardware for quantum simulations?
Anyone: Some major server CPU tuned for a supercomputer, right?
Ash: The last iPad :)
Apple has some of the most confusing hardware on the market.
Every M4 chip ships at least
three
different units that can all do matrix multiplication: the CPU cores (now with Arm SME2, replacing proprietary AMX), a 38 TOPS Neural Engine (or ANE, usable only through CoreML), and the GPU via Metal compute shaders.
Multiple options, each with a different programming model, different precision support, and no clear guidance from Apple on when to use which.
Still, the CPU part alone is worth attention.
Apple is the first hardware vendor to ship Scalable Matrix Extensions (or SME) to the market — starting with M4.
SME combines a “Streaming SVE” subset with outer-product matrix ops, accumulating into persistent ZA registers.
It supports more numeric types than Intel’s AMX and is much more composable if you are implementing something more than a vanilla dense matrix-multiplication.
1
svfmopa_za32_f16_m
(
0
,
predicate
,
predicate
,
tile_a
,
tile_b
);
// za += outer_product(tile_a, tile_b)
This may look similar to Intel AMX, but it’s not.
More on this in the
GEMMs
section.
The next versions of SME are supposed to bring
LUTI2/LUTI4
lookup tables and full SVE compatibility.
I expect it to be a game changer for sparse numerics and advanced algorithms — if only there were a 100+ core server variant.
One thing to note: using SME requires careful CPU state switching to and from streaming mode, which isn’t free.
You can’t mix Streaming SVE code with NEON and your typical LibC code.
Still, this is remarkably programmable tiled hardware, which will translate into gains for all the same kernel families as Intel AMX above, but also:
nk_maxsim_packed
on SME is elegant — on the fly GEMM-like outer-products over column-major packed matrices, then updates a running argmax with SVE compares/selects, and only does a final horizontal reduction at the end
nk_dots_packed_u1_smebi32
,
nk_hammings_packed_u1_smebi32
,
nk_jaccards_packed_u1_smebi32
loads unpacked A rows horizontally into ZA0, reads them back vertically, and feeds those columns into
svbmopa_za32_u32_m
achieving 4'027 gso/s (or 4+ TOPS as most of the industry spells it) on a single core for 4096³ dense input matrix — almost 10x the tiled GEMM-like NEON kernel for the same task.
nk_bilinear_f32c_smef64
kernel for double-precision bilinear forms for single-precision complex numbers — it stages real and imaginary parts separately, then uses
FMOPA
plus
FMOPS
for the subtracting complex term.
I’ve spent a few thousand $ setting up all the AWS instances to validate/test this logic, and only realized that I forgot to get the numbers for this kernel after I’ve returned the dedicated hosts.
Let’s hope it works as well as it looks.
This composability makes Arm SME + SVE the most convenient platform for advanced AI architectures, opening the door to fusing entire Transformer attention blocks — GEMM + SoftMax + GEMM — on Apple M4 and M5 without leaving streaming mode.
How Hardware Converges
#
Every major vendor is arriving at the same answer — tiled mixed-precision multiply-accumulate — just with different register files, predicate models, and memory hierarchies:
Feature
Intel AMX
Arm SME
RVV 1.0
NVIDIA TC
Matrix tiles
8x 1KB
ZA SVL²
Proposed
generation-specific
bf16 × bf16 → f32
✅
✅
Ext
✅
f16 × f16 → f32
Soon
✅
✅
✅
i8 × i8 → i32
✅
✅
✅
✅
HBM option
✅
❌
❌
✅
Consumer silicon
❌
✅
❌
✅
Predicate model
Tile config
SVE-style
Mask v0
generation-specific
CPUs and GPUs look more alike every generation.
But unlike the somewhat specialized
Graphics Processing Unit
, the
Central Processing Unit
can’t always provide the same level of throughput as a task-specific accelerator.
In a modern data-center its role is shifting towards connecting sub-systems and guaranteeing correctness.
That was one of the guiding principles behind NumKong — precision of the numerics has to be sufficient first, and only then do we chase MKL, OpenBLAS, and cuBLAS throughput.
When multiplying a 1'000 by 1'000 matrix, it’s not that big of a deal, but when you are scaling attention beyond 10 Million tokens, or vector search beyond 10 Billion vectors on each machine, numerical stability becomes a big deal.
WebAssembly & Relaxed SIMD
#
There is one more “platform” that doesn’t fit neatly into the hardware table above — the browser.
WebAssembly’s
Relaxed SIMD
proposal, now part of the Wasm 3.0 standard, trades strict determinism for hardware-native fast paths.
Chrome 114+ and Firefox 145+ ship it by default; Safari still has it behind a flag.
WASM SIMD is fixed at 128-bit, but the JIT lowers each instruction to the best native path available:
Relaxed SIMD
x86 lowering options
Arm lowering options
relaxed_madd
vfmadd
(FMA3),
mulps
+
addps
(SSE)
fmla
(NEON)
relaxed_dot_i8x16_i7x16
vpdpbusd
(AVX-512 VNNI, AVX-VNNI),
pmaddubsw
+
pmaddwd
+
paddd
(SSE)
sdot
(Armv8.2+),
smull
+
saddlp
(Armv8.0)
relaxed_swizzle
vpshufb
(AVX),
pshufb
(SSSE3)
tbl
(NEON)
relaxed_laneselect
vpblendvb
(AVX2),
pblendvb
(SSE4.1)
bsl
(NEON)
relaxed_min/max
vminps
(AVX),
minps
(SSE)
fmin
&
fmax
(NEON)
NumKong compiles to WASM via Emscripten and Cranelift, covering every kernel with the
_v128relaxed
suffix — dot products, batched GEMMs, geospatial, mesh alignment, and more.
In the browser, no install needed — just a
<script>
tag:
1
2
3
4
5
6
7
8
<
script
type
=
"module"
>
import
{
dot
,
euclidean
}
from
'https://cdn.jsdelivr.net/npm/numkong@7/dist/numkong.js'
;
const
query
=
new
Float32Array
([
1.0
,
2.0
,
3.0
]);
const
doc
=
new
Float32Array
([
4.0
,
5.0
,
6.0
]);
console
.
log
(
dot
(
query
,
doc
));
// 32 — SIMD-accelerated, client-side
console
.
log
(
euclidean
(
query
,
doc
));
// 5.196...
</
script
>
The entire WASM bundle is under 500 KB — smaller than most JavaScript frameworks.
Possible improvement directions for backends:
Loongson LAPX (
#317
), IBM Power VSX & MMA (
#318
), and Arm FP8 on NVIDIA’s Vera/Olympus cores (
#319
).
Intel’s Nova Lake may also bring native FP16 dot products to the consumer desktop.
Precision Spectrum: From Float118 to Float4
#
IEEE 754
was defined in 1985 and for many years the “single-precision” and “double-precision” numerics it standardized were enough.
Four decades later, every time Jensen Huang appears on stage with a new FLOPS number, you must ask yourself — which exact numeric type is he referring to?
Transistor cost and density is still improving, but not nearly as much as perceived.
So we as an industry shift towards smaller numeric types.
For brevity, in this article, we’ll only look at numerics for these input types:
Type
Bits
Exponent
Mantissa
Min-Max Range
Float118
128
11
~106
same as f64, ~32 digits
Float64
64
11
52
±2.2e-308 to ±1.8e308
Float32
32
8
23
±1.2e-38 to ±3.4e38
Float16
16
5
10
±6.1e-5 to ±65504
BFloat16
16
8
7
±1.2e-38 to ±3.4e38
Float8, E5M2
8
5
2
±6.1e-5 to ±57344
Float8, E4M3
8
4
3
±0.016 to ±448
Float6, E3M2
6
3
2
±0.0625 to ±28
Float6, E2M3
6
2
3
±0.015625 to ±7.5
Float4, E2M1
4
2
1
±0.5 to ±6
Int8
8
—
—
-128 to 127
UInt8
8
—
—
0 to 255
Int4
4
—
—
-8 to 7
UInt4
4
—
—
0 to 15
Float118 is not an IEEE type — it is a “double-double” representation that pairs two Float64 values using Knuth two-sum and FMA for error-free transformations, yielding ~106 bits of effective mantissa (~32 decimal digits).
The range matches Float64, since both components share the same exponent field, but precision is roughly double.
NumKong uses it internally as a ground-truth reference for validating all other kernels.
How does it compare to other extended-precision options?
Type
Speed
Mantissa
Notes
double
1x
53-bit
Native hardware IEEE 754
long double
1.5x
64-bit
x87 80-bit extended, not portable
NumKong’s
f118_t
11x
~106-bit
FMA-based “double-double”
__float128
88x
113-bit
GCC
libquadmath
, not available on all OSes
boost::float128
91x
113-bit
Thin wrapper around
__float128
boost::cpp_bin_float_quad
200x
113-bit
Pure C++ emulation, portable but slowest
boost::cpp_bin_float_50
237x
~166-bit
50 decimal digits, for when 32 aren’t enough
Float6 types follow the
OCP MX v1.0
specification — each value occupies 6 bits stored in an 8-bit byte, with the upper 2 bits unused.
E3M2 has no NaN and supports infinities at ±28; E2M3 has neither NaN nor infinities, with ±7.5 as the maximum representable value.
Int4 and UInt4 are packed as nibble pairs — two 4-bit values per byte, with the low element in bits 0–3 and the high element in bits 4–7.
How many of the mainstream machine learning numerics projects support these types?
To my surprise, with some tweaking — quite many, thanks to Google’s
ml_dtypes
package that almost nobody knows about.
So if you want to deal with
bfloat16
values in NumPy matrices, you can use those extensions:
1
2
3
4
5
from
ml_dtypes
import
bfloat16
import
numpy
as
np
arr
=
np
.
array
([
1.0
,
2.0
,
3.0
],
dtype
=
bfloat16
)
result
=
arr
@
arr
# Dot product, but painfully slow!
Under the hood this implements
NEP 42
to serially convert numbers to a framework-friendly old-school
float32
.
Let’s rephrase the question: in which of those numeric types can you perform a hardware-accelerated matrix multiplication — AI’s most important operation — on CPUs or GPUs?
Type
NumPy
PyTorch
NumKong
Float16
❌
✅ GPU, CPU via oneDNN
✅ x86, Arm, RISC-V
BFloat16
❌
✅ GPU, CPU via oneDNN
✅ x86, Arm, RISC-V
Float8 E5M2
❌
⚡ H100+ via
torch._scaled_mm
✅ x86, Arm, RISC-V
Float8 E4M3
❌
⚡ H100+ via
torch._scaled_mm
✅ x86, Arm, RISC-V
Int8
❌
⚡ via
torch._int_mm
✅ x86, Arm, RISC-V
UInt8
❌
⚡ via
torch._int_mm
✅ x86, Arm, RISC-V
Int4
❌
❌
✅ x86, Arm, RISC-V
UInt4
❌
❌
✅ x86, Arm, RISC-V
Float4 E2M1
❌
⚡ B200+ via
torch._scaled_mm
❌
✅ = standard API, ⚡ = hardware-accelerated via specialized API, ❌ = not supported or serial fallback
A lot of red on this table.
At best, support is hardware-specific, dependent on access to $10K+ expensive data-center GPUs & TPUs, and contingent on downloading a gigabyte-sized framework.
And that’s in Python, by far the most mature ecosystem for machine learning.
Things are much worse if you are developing in C/C++, Rust, Swift, or other programming languages…
Tensors in Python
#
Remember
ml_dtypes
above?
NumPy can
represent
BFloat16 with that plugin, but
arr @ arr
falls back to serial
f32
casts.
NumKong accepts those same buffers — zero copy — but routes through SIMD kernels.
PyTorch tensors also work directly via the buffer protocol:
nk.dot(torch_a, torch_b)
just works, no conversion.
Slice a column from a row-major matrix, and
argmin
or
moments
still fire SIMD — 2.45x faster than
np.argmin
on strided columns, covered in the
reductions section
.
All batched kernels release the GIL, and the
METH_FASTCALL
calling convention avoids
PyArg_ParseTupleAndKeywords
overhead entirely.
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
import
torch
,
numkong
as
nk
embeddings
=
torch
.
randn
(
10_000
,
768
,
dtype
=
torch
.
bfloat16
)
nk
.
dot
(
embeddings
[
0
],
embeddings
[
1
])
# buffer protocol, zero copy from PyTorch
packed
=
nk
.
dots_pack
(
embeddings
,
dtype
=
nk
.
bfloat16
)
# pack once, reuse across query batches
scores
=
nk
.
dots_packed
(
embeddings
[:
128
],
packed
)
# 128×10K batched GEMM
matrix
=
nk
.
Tensor
(
embeddings
.
float
()
.
numpy
())
# float32 for NumPy interop
column
=
matrix
[:,
0
]
# strided view — no copy
column
.
argmin
()
# SIMD reduction on strided data
CUDA unified memory opens up a neat debugging trick.
Wrap a live GPU tensor via
nk.from_pointer
, and you can scan layers of a running network without copying anything back to host explicitly.
Hunting for the layer that started diverging after a quantization pass becomes a one-liner.
1
2
3
4
5
6
model
=
load_my_model
()
.
cuda
()
for
name
,
param
in
model
.
named_parameters
():
view
=
nk
.
from_pointer
(
param
.
data_ptr
(),
tuple
(
param
.
shape
),
nk
.
bfloat16
,
owner
=
param
)
norms
=
view
.
norm
(
axis
=
0
)
# column-wise L2 norms, SIMD-accelerated
if
norms
.
max
()
>
1e3
:
# outlier detector for post-quantization debugging
print
(
f
"
{
name
}
: norm outlier at
{
norms
.
argmax
()
}
=
{
norms
.
max
()
:
.1f
}
"
)
Tensors in C
#
BLAS was standardized in 1979, originally implemented in Fortran, and every scientific computing package on earth links against it.
OpenBLAS — the default NumPy backend — maintains 2'456 kernel files across 1.97M lines of code, 51% of it hand-written assembly, running on 15 CPU architectures from x86 to SPARC to s390x.
GEMM + copy + TRSM account for 58% of all those kernels — for dense Float32 and Float64 matrix multiplication, nothing comes close.
The intro table shows this: OpenBLAS hits 65.5 gso/s on Float64 GEMMs where NumKong reaches 8.6 gso/s, trading throughput for sub-ULP precision.
The type landscape, however, hasn’t kept up.
Complex-double alone is 31% of all OpenBLAS files, while Float16 gets two (conversion stubs, no compute) and Float8 gets zero.
sdsdot
(
f32 × f32 → f64 → f32
) remains the only mixed-precision operation from the original standard.
A Dongarra-led “BLAS G2” proposal in 2016–2019 tried to standardize half/int/quad precision, but no formal standard was ratified — each vendor bolted on their own extensions instead:
BLAS Standard
OpenBLAS
Intel MKL
cuBLAS
NumKong
Hardware
Any CPU via Fortran
15 CPU archs, 51% assembly
x86 only, SSE through AMX
NVIDIA GPUs only
20 backends: x86, Arm, RISC-V, WASM
Types
f32
,
f64
, complex
+ 55
bf16
GEMM files
+
bf16
&
f16
GEMM
+
f16
,
i8
, mini-floats on Hopper+
16 types,
f64
down to
u1
Precision
dsdot
is the only widening op
dsdot
is the only widening op
dsdot
,
bf16
&
f16
→
f32
GEMM
Configurable accumulation type
Auto-widening, Neumaier, Dot2
Operations
Vector, mat-vec, GEMM
58% is GEMM & TRSM
+ Batched
bf16
&
f16
GEMM
GEMM + fused epilogues
Vector, GEMM, & specialized
Memory
Caller-owned, repacks inside
Hidden
mmap
, repacks inside
Hidden allocations, + packed variants
Device memory, repacks or LtMatmul
No implicit allocations
Tensors in C++23
#
Consider a common LLM inference task: you have Float32 attention weights and need to L2-normalize each row, quantize to E5M2 for cheaper storage, then score queries against the quantized index via batched dot products.
In CBLAS, there is no norm-then-quantize primitive — you’d loop over columns with
cblas_snrm2
, manually divide each row, cast element-by-element, and hand-roll the batched GEMM.
Eigen
can do
m.colwise().norm()
but stops at
float
and
double
— no E5M2, no sub-byte types, no runtime SIMD dispatch.
NumKong’s C++ header wraps the C ABI in a zero-cost
tensor
template that handles the full pipeline:
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
19
20
namespace
nk
=
ashvardanian
::
numkong
;
// Float32 attention weights — 1000 vectors × 768 dimensions
auto
weights
=
nk
::
tensor
<
nk
::
f32_t
>::
try_full
({
1000
,
768
},
nk
::
f32_t
{
1
});
// Row-wise L2 norms via moments, then normalize each row in-place
auto
[
sums
,
sumsqs
]
=
nk
::
try_moments
(
weights
.
view
(),
/*axis=*/
1
);
for
(
std
::
size_t
i
=
0
;
i
<
weights
.
extent
(
0
);
++
i
)
{
// or via .rows_spans() iterator
float
inv_norm
=
1.0f
/
std
::
sqrt
<
float
>
(
sumsqs
[
i
]),
zero
=
0.0f
;
auto
row
=
weights
.
row
(
i
).
as_vector
();
nk
::
scale
(
row
.
data
(),
row
.
size
(),
&
inv_norm
,
&
zero
,
row
.
data
());
}
// Quantize f32 → e5m2, pack, and score queries via batched GEMM
auto
quantized
=
nk
::
tensor
<
nk
::
e5m2_t
>::
try_zeros
({
1000
,
768
});
nk
::
cast
(
weights
.
view
().
data
(),
1000
*
768
,
quantized
.
span
().
data
());
auto
packed
=
nk
::
packed_matrix
<
nk
::
e5m2_t
>::
try_pack
(
quantized
.
view
().
as_matrix
());
auto
queries
=
nk
::
tensor
<
nk
::
e5m2_t
>::
try_zeros
({
128
,
768
});
auto
scores
=
nk
::
tensor
<
nk
::
f32_t
>::
try_zeros
({
128
,
1000
});
nk
::
dots_packed
(
queries
.
view
(),
packed
,
scores
.
span
());
Slicing uses C++23 variadic
operator[]
with marker types:
t[i, j]
returns
f32_t&
, while
t[i, j, nk::slice]
returns a rank-zero
tensor_view
, and
t[nk::all, j, nk::slice]
returns a strided
tensor_view
.
The return type changes at compile time, no runtime costs unlike Python.
Sub-byte types keep the same syntax:
tensor<i4x2_t>[idx]
returns
sub_byte_ref<i4x2_t>
— a proxy that reads and writes a nibble.
All scalar types —
f16_t
,
bf16_t
,
e4m3_t
,
i4x2_t
and friends — have
std::formatter
specializations, so
std::format("{:#}", val)
prints
3.14 [0x4248]
and
std::format("{:b}", val)
prints the raw bits.
Eigen has none of that: no sub-byte types, no Float8/Float6, no signed strides, no runtime SIMD dispatch, no widening accumulators.
It expects the compiler to auto-vectorize, which almost never happens for exotic types, and in most cases just bloats the binary.
std::mdspan
gives you layout + accessor but no operations and no sub-byte support; NumKong views interop via raw pointer handoff.
Tensors in Rust
#
The same pipeline in Rust is more concise —
try_norm_axis
and
try_cast_dtype
are first-class methods on
Tensor
:
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
use
numkong
::
{
configure_thread
,
Tensor
,
PackedMatrix
,
MomentsOps
,
ScaleOps
,
CastOps
};
use
numkong
::
types
::
e5m2
;
configure_thread
();
let
mut
weights
=
Tensor
::
<
f32
>
::
try_full
(
&
[
1000
,
768
],
1.0
).
unwrap
();
// Normalize → quantize → pack → score
let
norms
=
weights
.
try_norm_axis
(
1
,
false
).
unwrap
();
for
(
i
,
mut
row
)
in
weights
.
axis_spans
(
0
).
unwrap
().
enumerate
()
{
row
.
try_scale_tensor_into
(
1.0
/
norms
[
i
]
as
f32
,
0.0
,
&
mut
row
).
unwrap
();
}
let
quantized
=
weights
.
try_cast_dtype
::
<
e5m2
>
().
unwrap
();
let
packed
=
PackedMatrix
::
try_pack
(
&
quantized
).
unwrap
();
// 128 queries against the packed index — batched GEMM, SIMD-accelerated
let
queries
=
Tensor
::
<
e5m2
>
::
try_full
(
&
[
128
,
768
],
e5m2
::
from
(
0.5
)).
unwrap
();
let
scores
=
queries
.
dots_packed
(
&
packed
);
For comparison,
ndarray
— Rust’s most popular tensor library — supports only
f32
and
f64
, has no SIMD dispatch, no sub-byte types, and no packed GEMM.
NumKong mirrors the C++ container hierarchy —
Tensor<T, A>
owns,
TensorView
and
TensorSpan
borrow — but all operations are trait-based and monomorphized with zero dispatch overhead.
Sub-byte types like
i4x2
and
u1x8
use
DimRef
/
DimMut
proxy accessors with read-modify-write on
Drop
, and
allclose
gives tolerance-based comparison via the
AllCloseOps
trait — surprisingly absent from both
nalgebra
and
ndarray
.
Possible improvement directions for SDKs:
Zig bindings, a cheaper FFI interface for Go (
#28
), and better compatibility with NumPy.
Kernel Design Patterns
#
Repeating all the documentation here felt silly, but so would burying it in READMEs and forgetting about it until the next iteration.
So here are the most important optimizations missing from previous library versions.
Int8 and UInt8 Symmetric Dot-Products via VNNI
#
Scope:
nk_dot_(i8|u8)_(ice|sierra)
.
Intel’s
DPBUSD
instruction computes a dot product of 8-bit integers — but it expects one
unsigned
and one
signed
operand.
If both your inputs are signed, or both unsigned, you have a problem.
The naive fix is to upcast everything to 16-bit via
cvtepi8_epi16
and use
VPDPWSSD
— but widening runs on port 5, and you need
two
widenings per iteration, so port 5 becomes the bottleneck while port 0 sits half-idle.
The better fix is “algebraic”.
XOR-ing a signed byte with
0x80
flips the sign bit, mapping
[-128, 127]
to
[0, 255]
— which is just adding 128.
So
DPBUSD(a ⊕ 0x80, b)
computes
(a+128)·b
instead of
a·b
, and the correction is trivial: subtract
128 × Σb
at the end.
The unsigned case is symmetric: bias
b
instead and compensate with
128 × Σa
.
WASM’s
relaxed_dot_i8x16_i7x16_add
faces the same mismatch — it constrains one operand to 7 bits [0, 127] so both x86’s unsigned × signed
vpdpbusd
and Arm’s signed × signed
sdot
produce identical results, and NumKong’s WASM backend uses a similar decomposition to handle full-range signed inputs.
The trick is
how
we accumulate those correction sums.
SAD
— sum of absolute differences against zero — gives us Σb cheaply, and it fires on port 5 while
DPBUSD
occupies port 0.
The two instructions run in parallel every cycle, making the compensation essentially free.
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
// Signed i8 × i8: bias a to unsigned, accumulate sum(b) for correction
__m512i
a_biased
=
_mm512_xor_si512
(
a_i8x64
,
_mm512_set1_epi8
(
0x80
));
sum_ab
=
_mm512_dpbusd_epi32
(
sum_ab
,
a_biased
,
b_i8x64
);
// (a+128)·b @ port 0
__m512i
b_unsigned
=
_mm512_xor_si512
(
b_i8x64
,
_mm512_set1_epi8
(
0x80
));
sum_b
=
_mm512_add_epi64
(
sum_b
,
_mm512_sad_epu8
(
b_unsigned
,
zeros
));
// Σb via SAD @ port 5
// Unsigned u8 × u8: bias b to signed, accumulate sum(a) for correction
__m512i
b_signed
=
_mm512_xor_si512
(
b_u8x64
,
_mm512_set1_epi8
(
0x80
));
sum_ab
=
_mm512_dpbusd_epi32
(
sum_ab
,
a_u8x64
,
b_signed
);
// a·(b-128) @ port 0
sum_a
=
_mm512_add_epi64
(
sum_a
,
_mm512_sad_epu8
(
a_u8x64
,
zeros
));
// Σa via SAD @ port 5
After the loop, the epilogue is a single shift-and-subtract —
128 × Σb
is just
Σb << 7
:
1
2
__m128i
correction_i32x4
=
_mm_slli_epi32
(
b_sums
.
xmm
,
7
);
// × 128
results
->
xmm
=
_mm_sub_epi32
(
biased_i32x4
,
correction_i32x4
);
// exact result, no rounding
The new path processes 64 elements per iteration instead of 32.
Here is the full picture:
i8 × i8
u8 × u8
Naive approach
Instructions
cvtepi8_epi16
both →
VPDPWSSD
cvtepi8_epi16
both →
VPDPWSSD
Step width
32 elements/iter
32 elements/iter
Port usage
2× p5 widening, 1× p0 dot —
p5 bottleneck
2× p5 widening, 1× p0 dot —
p5 bottleneck
Efficient approach
Instructions
XOR
a ⊕ 0x80
→
DPBUSD
,
SAD
for Σb
XOR
b ⊕ 0x80
→
DPBUSD
,
SAD
for Σa
Port usage
1× p0 dot, 1× p5 SAD —
parallel, free
1× p0 dot, 1× p5 SAD —
parallel, free
Step width
64 elements/iter -
2x
throughput
64 elements/iter -
2x
throughput
Correction
result − 128 × Σb
result + 128 × Σa
Sierra Forest made this entire dance obsolete.
Intel’s AVX-VNNI-INT8 extension adds
VPDPBSSD
for native signed × signed and
VPDPBUUD
for unsigned × unsigned — no algebraic transform, no compensation terms, just the dot product you wanted.
The Ice Lake workaround remains relevant for the millions of Xeon4 and earlier servers already deployed.
The same algebraic trick extends to 4-bit integers.
Each byte packs two signed Int4 values as nibbles in
[-8, 7]
.
XOR-ing with
0x08
maps them to unsigned
[0, 15]
, and the signed product expands as:
$$
(a \oplus 8 - 8)(b \oplus 8 - 8) = (a \oplus 8)(b \oplus 8) - 8(a \oplus 8 + b \oplus 8) + 64
$$
Extract low and high nibbles with AND + shift, XOR both to unsigned, then fire two
DPBUSD
calls per iteration — one for each nibble position.
The correction sums are accumulated the same way, and the final result is
signed_dot = unsigned_dot - 8 × (Σa' + Σb') + 64 × n
.
Compensated Summation: Dot2 in SIMD
#
Scope:
nk_dot_f64_(sve|neon|rvv)
.
OpenBLAS and MKL accumulate Float64 dot products with naive summation — rounding errors grow as O(√n), reaching 56 mean ULP (Units in the Last Place) at 4096³ matrix size.
NumKong’s Dot2 implementation hits
0 ULP
at the same size.
The algorithm, from
Ogita, Rump, and Oishi
, tracks every rounding error alongside the main sum, achieving O(1) error growth regardless of vector length.
It relies on two error-free transforms.
TwoProd: FMA computes
a×b
at full internal precision, so
fma(a, b, -product)
recovers the
exact
rounding residual of the multiplication.
TwoSum: a similar five-operation dance recovers the exact rounding residual of an addition.
Both residuals get accumulated into a separate compensation register that rides alongside the main sum.
1
2
3
4
5
6
7
8
9
void
nk_f64_dot2_
(
nk_f64_t
*
sum
,
nk_f64_t
*
comp
,
nk_f64_t
a
,
nk_f64_t
b
)
{
nk_f64_t
product
=
a
*
b
;
nk_f64_t
product_error
=
fma
(
a
,
b
,
-
product
);
// TwoProd: exact multiply residual
nk_f64_t
new_sum
=
*
sum
+
product
;
nk_f64_t
recovered
=
new_sum
-
*
sum
;
// TwoSum: exact addition residual
nk_f64_t
sum_error
=
(
*
sum
-
(
new_sum
-
recovered
))
+
(
product
-
recovered
);
*
sum
=
new_sum
;
*
comp
+=
sum_error
+
product_error
;
}
The SIMD main loop is identical — TwoProd+TwoSum across all lanes in parallel, nothing surprising.
The hard part is the horizontal reduction: you hold two vector registers of partial results and need to fold them into one scalar without losing precision.
On NEON with its fixed 2 Float64 lanes, this is trivial — parallel TwoSum on both lanes, extract with
vgetq_lane_f64
, one scalar TwoSum to finish.
On SVE and RVV, vector lengths are unknown at compile time.
The solution is a log₂(VL) tree: at each level, extract the upper half via
svtbl
or
vslidedown
, TwoSum it with the lower half, propagate the rounding error downward.
Out-of-range indices return zero on both ISAs, so the shrinking upper half is harmless.
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
svfloat64_t
merged
=
svadd_f64_x
(
pg
,
partial_sum
,
compensation
);
svfloat64_t
addend
=
svsub_f64_x
(
pg
,
merged
,
partial_sum
);
svfloat64_t
error
=
svadd_f64_x
(
pg
,
svsub_f64_x
(
pg
,
partial_sum
,
svsub_f64_x
(
pg
,
merged
,
addend
)),
svsub_f64_x
(
pg
,
compensation
,
addend
));
for
(
unsigned
half
=
svcntd
()
/
2
;
half
>
0
;
half
>>=
1
)
{
svuint64_t
upper_idx
=
svadd_n_u64_x
(
pg
,
svindex_u64
(
0
,
1
),
half
);
svfloat64_t
upper_merged
=
svtbl_f64
(
merged
,
upper_idx
);
svfloat64_t
upper_error
=
svtbl_f64
(
error
,
upper_idx
);
svfloat64_t
halved
=
svadd_f64_x
(
pg
,
merged
,
upper_merged
);
svfloat64_t
halved_addend
=
svsub_f64_x
(
pg
,
halved
,
merged
);
svfloat64_t
rounding_error
=
svadd_f64_x
(
pg
,
svsub_f64_x
(
pg
,
merged
,
svsub_f64_x
(
pg
,
halved
,
halved_addend
)),
svsub_f64_x
(
pg
,
upper_merged
,
halved_addend
));
merged
=
halved
;
error
=
svadd_f64_x
(
pg
,
svadd_f64_x
(
pg
,
error
,
upper_error
),
rounding_error
);
}
return
svlastb_f64
(
first_lane
,
merged
)
+
svlastb_f64
(
first_lane
,
error
);
Casting via Tabular Lookups on x86 and Arm
#
Scope:
nk_cast
and pretty much every other kernel.
When your numeric type has few enough distinct unsigned magnitudes, a single table lookup replaces all the bit-shifting arithmetic of a traditional float conversion.
The question is where the cutoff falls — and it differs on x86 vs Arm because their LUT instructions have different capacities.
x86 AVX-512BW
has
VPERMUTEXVAR_EPI16
: 32 entries of 16-bit values in one ZMM register, chainable via
VPERMI2W
for larger tables.
Arm NEON
has
VQTBL2Q
: 32 entries of 8-bit values across two registers, with out-of-range indices returning zero — useful for clamping, but impractical to chain for 128+ entries.
Conversion
Magnitudes
x86 AVX-512
Arm NEON
e2m3 → bf16
32
1×
permutexvar
— full LUT
1×
vqtbl2q
— full LUT
e3m2 → bf16
32
1×
permutexvar
— full LUT
1×
vqtbl2q
— full LUT
e5m2 → bf16
128
arithmetic + 4-entry subnormal LUT
arithmetic only
e4m3 → bf16
128
arithmetic + 8-entry subnormal LUT
arithmetic only
The cleanest path is E2M3: every possible 5-bit magnitude fits in one register, subnormals included.
Mask the magnitude, look it up, shift the sign bit into position, OR them together — four operations, no branching, no blending.
1
2
3
4
5
// E2M3 → BF16 on x86: full 32-entry LUT, one permutexvar
__m512i
magnitude
=
_mm512_and_si512
(
widened
,
_mm512_set1_epi16
(
0x1F
));
__m512i
sign
=
_mm512_and_si512
(
widened
,
_mm512_set1_epi16
(
0x20
));
__m512i
result
=
_mm512_permutexvar_epi16
(
magnitude
,
lut_bf16x32
);
result
=
_mm512_or_si512
(
result
,
_mm512_slli_epi16
(
sign
,
10
));
// sign bit 5 → bit 15
E4M3 and E5M2 have 128 unsigned magnitudes — too many for one LUT.
Normals get arithmetic conversion via shift-and-add, while the handful of subnormals still go through a small lookup table.
On Arm, where chaining
VQTBL2Q
is expensive, even subnormals use arithmetic — shifts, adds, and blends.
LUT-free arithmetic upcasts via Giesel-style float-multiplication tricks are
being explored
but depend on rounding-mode control that conflicts with NumKong’s default denormal-to-zero policy.
Use BFloat16 or Float16 for Float8 Arithmetic?
#
Scope:
nk_dot_(e4m3|e5m2)_(genoa|neonfhm)
.
No CPU has a native Float8 dot product yet, so you must upcast to something that does.
The two candidates are BFloat16 and Float16 — both lossless for E4M3 normals, since 3 mantissa bits fit comfortably in either 7 or 10.
NumKong uses BFloat16 on x86 and Float16 on Arm, for different reasons on each side.
On x86,
VDPBF16PS
fuses
two
BFloat16 multiplies per 32-bit lane — doubling throughput compared to a single-multiply instruction.
The upcast from E4M3 goes through the LUT+arithmetic path from the previous section.
1
2
3
a_bf16x32
=
nk_e4m3x32_to_bf16x32_icelake_
(
a_e4m3x32
);
b_bf16x32
=
nk_e4m3x32_to_bf16x32_icelake_
(
b_e4m3x32
);
sum_f32x16
=
_mm512_dpbf16_ps
(
sum_f32x16
,
a_bf16x32
,
b_bf16x32
);
On Arm, there is no BFloat16 dot product instruction, but
FMLAL
from the FHM extension provides a widening
f16 × f16 → f32
FMA that fires at 2-4 per cycle on modern cores.
And the upcast is cheaper: E4M3’s 4-bit exponent maps into Float16’s 5-bit exponent with a single shift, so the conversion is pure arithmetic — no LUT needed.
1
2
3
4
5
6
nk_e4m3x16_to_f16x8x2_neon_
(
vld1q_u8
(
a
),
&
a_low
,
&
a_high
);
// shifts + adds, no LUT
nk_e4m3x16_to_f16x8x2_neon_
(
vld1q_u8
(
b
),
&
b_low
,
&
b_high
);
sum_f32x4
=
vfmlalq_low_f16
(
sum_f32x4
,
a_low
,
b_low
);
// c[0:4] += a[0:4] × b[0:4]
sum_f32x4
=
vfmlalq_high_f16
(
sum_f32x4
,
a_low
,
b_low
);
// c[0:4] += a[4:8] × b[4:8]
sum_f32x4
=
vfmlalq_low_f16
(
sum_f32x4
,
a_high
,
b_high
);
// c[0:4] += a[8:12] × b[8:12]
sum_f32x4
=
vfmlalq_high_f16
(
sum_f32x4
,
a_high
,
b_high
);
// c[0:4] += a[12:16] × b[12:16]
Use Int16 and Int8 for Float6 Arithmetic?
#
Scope:
nk_dot_(e2m3|e3m2)_(haswell|alder|sierra|icelake|neonsdot)
.
Every E2M3 value multiplied by 16 is an
exact
integer in [-120, +120], fitting a signed
i8
.
Why 16?
E2M3 has bias=1 and 3 mantissa bits, so the smallest nonzero subnormal is 1/8 — multiplying by 16 clears the denominator for every representable value.
This means we can replace floating-point dot products with integer ones and divide by 16×16=256 at the very end —
zero rounding error
.
A 32-entry LUT maps each 5-bit unsigned magnitude to its scaled integer.
On Arm,
VQTBL2Q
does the lookup; on x86,
VPERMB
does the same across a full ZMM register.
Then we XOR the sign bits of
a
and
b
, negate
b
where they differ, and feed the result into an integer dot product.
On Arm, that is
VQTBL2Q
+
SDOT
:
1
2
3
4
uint8x16_t
a_mag
=
vqtbl2q_u8
(
lut_pair
,
vandq_u8
(
a
,
mask_0x1F
));
uint8x16_t
b_mag
=
vqtbl2q_u8
(
lut_pair
,
vandq_u8
(
b
,
mask_0x1F
));
int8x16_t
b_signed
=
vbslq_s8
(
negate_mask
,
vnegq_s8
(
b_mag
),
b_mag
);
sum_i32x4
=
vdotq_s32
(
sum_i32x4
,
a_mag
,
b_signed
);
// c[0:4] += a[k:k+4] · b[k:k+4]
On x86,
VPERMB
+
VPDPBUSD
process 64 elements per iteration:
1
2
3
4
__m512i
a_unsigned
=
_mm512_permutexvar_epi8
(
a_magnitude
,
lut_u8x64
);
__m512i
b_unsigned
=
_mm512_permutexvar_epi8
(
b_magnitude
,
lut_u8x64
);
__m512i
b_signed
=
_mm512_mask_sub_epi8
(
b_unsigned
,
negate_mask
,
zeros
,
b_unsigned
);
sum_i32x16
=
_mm512_dpbusd_epi32
(
sum_i32x16
,
a_unsigned
,
b_signed
);
Both paths end with one division:
(float)reduce_add(sum) / 256.0f
— exact, because both operands were scaled by 16 and the integer arithmetic lost nothing.
E3M2 is the trickier sibling — its magnitudes reach 448, blowing past
i8
range.
So it uses the
i16
path instead: same LUT lookup for the low byte via
vqtbl2q_u8
, a comparison
vcgeq_u8(idx, 28)
to generate the high byte, then
vzip
to assemble 16-bit values.
vmlal_s16
accumulates the wider products into
i32
— same zero-error principle, just one lane-width up.
Complex Dot Products: Deinterleave vs FCMLA
#
Scope:
nk_(dot|vdot)_f32c_neon
.
ARMv8.3 introduced
FCMLA
— a dedicated complex multiply-accumulate that processes interleaved real/imaginary pairs with a single instruction per rotation.
Two
vcmlaq
calls with
rot0
and
rot90
should, in theory, replace four separate FMAs.
The alternative is to deinterleave first:
vld2
splits interleaved complex pairs into separate real and imaginary registers, then four independent
vfmaq
instructions compute
real += aᵣ×bᵣ
,
real -= aᵢ×bᵢ
,
imag += aᵣ×bᵢ
,
imag += aᵢ×bᵣ
.
On Apple M4 at n=4096, the deinterleaved path hits 39.7 GiB/s;
FCMLA
manages 17.1 GiB/s —
2.3x
slower.
The reason is instruction-level parallelism.
M4 has four SIMD pipes, and four independent
vfmaq
calls saturate all of them.
FCMLA
’s
rot0
and
rot90
variants have a data dependency —
rot90
reads the result of
rot0
— so the M4 cannot overlap them.
Two dependent instructions on a 4-wide backend leave half the pipes idle.
NumKong’s complex kernels also upcast Float32 inputs into Float64 accumulators for better precision, and the four-pipe parallelism more than compensates for the doubled lane width.
FCMLA
offers neither the throughput nor the precision advantage on this microarchitecture.
Broader lesson: specialized instructions are designed for
specific
pipeline widths.
On cores with fewer SIMD pipes,
FCMLA
may well win.
Measure on your target hardware.
Fast Reductions for Strided Arrays
#
Scope:
nk_reduce_*
.
NumKong requires contiguous inputs for binary operations like dot products, but
reductions
on strided arrays still get SIMD.
The use case: aggregating columns of a tall row-major matrix, or reducing a member field across an array-of-structures layout.
The key idea on AVX-512: instead of expensive gather instructions, do a contiguous load and mask out the bytes you don’t want.
A precomputed 64-bit K-register mask selects every n-th byte.
For stride=2, the mask is
0x5555555555555555
— every other byte, 32 elements per load.
For stride=3, it is
0x9249249249249249
— 22 elements.
All the way down to stride=16 with 4 elements, below which we fall back to scalar.
1
2
3
4
5
6
__mmask64
stride_mask
=
nk_stride_mask_u1x64_
(
stride
);
nk_size_t
step
=
_mm_popcnt_u64
(
stride_mask
)
*
stride
;
for
(;
idx
+
step
<=
total
;
idx
+=
step
)
{
__m512i
data
=
_mm512_maskz_loadu_epi8
(
stride_mask
,
ptr
+
idx
);
// non-column bytes are zero — safe to feed into SAD, VNNI, etc.
}
On Arm,
vld2q
/
vld3q
/
vld4q
deinterleave 2/3/4-strided data directly into separate registers during the load — no masking needed, but limited to strides 2-4.
The stride-3 case for XYZ point clouds is covered in detail in the
mesh alignment section
.
Once we have the strided data in registers, two families of reductions use it very differently.
reduce_minmax
finds extrema and their positions without upcasting mini-floats.
IEEE 754 floats have an order-preserving property: for positive values, the integer representation sorts the same way as the float value.
Negative values need their magnitude bits flipped.
A single XOR transforms any Float8 or Float6 byte into an unsigned integer that compares correctly —
vminq_u8
/
vmaxq_u8
on Arm,
_mm512_min_epu8
/
_mm512_max_epu8
on x86 — no upcast to Float16 or Float32, no floating-point compare.
1
2
3
4
5
// Float8 → order-preserving unsigned byte, one XOR per lane
__mmask64
negative
=
_mm512_test_epi8_mask
(
raw
,
_mm512_set1_epi8
(
0x80
));
__m512i
xor_pos
=
_mm512_set1_epi8
(
0x80
);
// positive: flip sign bit
__m512i
xor_neg
=
_mm512_set1_epi8
(
0xFF
);
// negative: flip all bits
__m512i
comparable
=
_mm512_xor_si512
(
raw
,
_mm512_mask_mov_epi8
(
xor_pos
,
negative
,
xor_neg
));
reduce_moments
computes sum and sum-of-squares for L2 norms — critical in ML normalization layers.
For Float32 inputs, the accumulation widens to Float64:
_mm512_cvtps_pd
upcasts 8 floats, then
_mm512_fmadd_pd
accumulates x² directly in double precision, avoiding the catastrophic cancellation that plagues single-precision norms on long vectors.
For integer inputs, the approach is different —
SAD
computes the biased sum while
VPDPWSSD
accumulates the sum-of-squares in one fused instruction.
But integer accumulators eventually overflow.
For i8 and i16 inputs, NumKong uses a divide-and-conquer strategy: once the element count exceeds what a 64-bit accumulator can safely hold, the array is split in half, each half reduced recursively, and the two 64-bit results merged with a saturating add.
The i64 case is trickier — there is nothing wider to accumulate into, and pairwise saturating addition silently loses information.
Consider
{INT64_MAX, INT64_MAX, -INT64_MAX}
— the true sum is
INT64_MAX
:
1
2
3
4
int64_t
inputs
[]
=
{
INT64_MAX
,
INT64_MAX
,
-
INT64_MAX
};
int64_t
naive
=
inputs
[
0
]
+
inputs
[
1
]
+
inputs
[
2
];
// UB: signed overflow on inputs[0]+inputs[1]
int64_t
pairwise
=
sadd
(
sadd
(
0
,
inputs
[
0
]),
inputs
[
1
]);
// MAX → sadd(MAX, -MAX) = 0 ← WRONG
nk_reduce_moments_i64
(
d
,
3
,
8
,
&
sum
,
&
sumsq
);
// 128-bit: 0 → MAX → 2MAX → MAX ← CORRECT
Early saturation erased the pending cancellation.
NumKong emulates a 128-bit accumulator with
sum_lower
/
sum_upper
register pairs and manual carry propagation, clamping only once after the entire loop.
Vincenty with Masked Convergence
#
Scope:
nk_vincenty_f64_(skylake|genoa)
.
Haversine
gives you the great-circle distance — shortest path on a perfect sphere:
$$
d = 2r \arcsin\sqrt{\sin^2\frac{\Delta\varphi}{2} + \cos\varphi_1\cos\varphi_2\sin^2\frac{\Delta\lambda}{2}}
$$
One closed-form evaluation, no iteration, easy to vectorize.
But Earth is not a sphere — it is an oblate spheroid, roughly 21 km wider at the equator than pole-to-pole.
Vincenty’s formula
accounts for this flattening by iteratively refining an auxiliary longitude λ until convergence:
$$
\sin^2\sigma = (\cos U_2\sin\lambda)^2 + (\cos U_1\sin U_2 - \sin U_1\cos U_2\cos\lambda)^2
$$
where $U_1$, $U_2$ are reduced latitudes on the reference ellipsoid.
The iteration converges in 3-8 steps for most point pairs, but degenerates for coincident points and near-antipodal cases — exactly the kind of variable-rate convergence that makes SIMD interesting.
The Haversine error from ignoring flattening is up to ~0.3%, which matters for surveying, aviation corridors, and high-precision geofencing.
Vincenty is inherently ~10x more expensive per pair, so SIMD parallelism is the only way to keep it practical at scale.
Haversine and Vincenty have vastly different error bounds and behavior at critical points (antipodal, coincident, equatorial).
The numbers below compare throughput only — not accuracy.
f32 → f32
throughput
f64 → f64
throughput
Rust
numkong
Haversine
487 M points/s
152 M points/s
numkong
Vincenty
69 M points/s
18 M points/s
geo
Haversine
39 M points/s
24 M points/s
geo
Vincenty
—
1.2 M points/s
Python
numkong
Haversine
475 M points/s
155 M points/s
numkong
Vincenty
55 M points/s
18 M points/s
geopy
Haversine
—
0.18 M points/s
geopy
Vincenty
—
0.01 M points/s
NumKong’s Vincenty in
f64 → f64
is
15x
faster than Rust
geo
and
1'800x
faster than Python
geopy
— because 8 point-pairs iterate simultaneously in AVX-512.
But those 8 pairs converge at different rates, and this is where the implementation gets interesting.
The solution is a convergence mask:
__mmask8 converged_mask
tracks which lanes are done, and the loop exits when all 8 bits are set.
The mask is not just an optimization — converged lanes may have near-zero denominators that would produce NaN if allowed to keep iterating.
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
__mmask8
converged_mask
=
0
;
__mmask8
coincident_mask
=
0
;
for
(
nk_u32_t
iter
=
0
;
iter
<
MAX_ITER
&&
converged_mask
!=
0xFF
;
++
iter
)
{
__m512d
sin_lambda
=
nk_sin_f64x8_skylake_
(
lambda
);
// ... Vincenty iteration body ...
coincident_mask
=
_mm512_cmp_pd_mask
(
sin_angular_dist
,
threshold
,
_CMP_LT_OS
);
sin_azimuth
=
_mm512_maskz_div_pd
(
_knot_mask8
(
coincident_mask
),
cos_u1_cos_u2_sin_lambda
,
sin_angular_dist
);
__mmask8
equatorial_mask
=
_mm512_cmp_pd_mask
(
cos_sq_alpha
,
eps
,
_CMP_LT_OS
);
quotient
=
_mm512_mask_div_pd
(
passthrough
,
_knot_mask8
(
equatorial_mask
),
two_sin_product
,
cos_sq_alpha
);
converged_mask
|=
_mm512_cmp_pd_mask
(
abs_delta
,
threshold
,
_CMP_LT_OS
);
}
Two separate division-by-zero hazards need two different masked divide flavors.
_mm512_maskz_div_pd
zeroes
the result for coincident points — two identical locations where sin of the angular distance vanishes.
_mm512_mask_div_pd
uses a
passthrough
value for equatorial cases where cos²α vanishes — the passthrough is chosen so the subsequent subtraction yields zero, keeping the iteration stable.
This pattern generalizes to any SIMD convergence loop — Newton-Raphson, iterative solvers, ray-sphere intersection.
Track a mask of done lanes, guard every division with that mask, exit when full.
Mesh Alignment: Deinterleaving XYZ across ISAs
#
Scope:
nk_(rmsd|kabsch|umeyama)_(f32|f64)_(neon|haswell|skylake|rvv)
.
RMSD measures how far apart two point clouds are on average — it’s the “are these similar?” check.
Kabsch
finds the optimal rotation to overlay one cloud onto another, minimizing that RMSD.
Umeyama adds uniform scaling on top of Kabsch — useful when the two clouds differ in size, e.g. comparing a crystal structure to a docked ligand at different resolutions.
All three operate on 3D point clouds stored as interleaved XYZ triplets — the standard Array-of-Structures layout.
The first challenge in every kernel is getting the data
out
of AoS into separate X, Y, Z vectors for vectorized centroid and covariance computation.
Every ISA does this differently, and the choice matters — deinterleaving is the inner loop’s first operation, so it sets the throughput ceiling.
NEON
has hardware stride-3 loads.
vld3q_f32
reads 12 contiguous floats and returns three 4-wide vectors — X, Y, Z separated in one instruction:
1
2
3
4
float32x4x3_t
xyz_f32x4x3
=
vld3q_f32
(
ptr
);
// 4 XYZ triplets → 3 vectors
*
x_f32x4_out
=
xyz_f32x4x3
.
val
[
0
];
// x0, x1, x2, x3
*
y_f32x4_out
=
xyz_f32x4x3
.
val
[
1
];
// y0, y1, y2, y3
*
z_f32x4_out
=
xyz_f32x4x3
.
val
[
2
];
// z0, z1, z2, z3
Haswell
lacks stride-3 loads, so we use
_mm256_i32gather_ps
with pre-computed stride-3 indices
[0,3,6,9,12,15,18,21]
— three gathers offset by 0, 1, 2 for X, Y, Z respectively.
Skylake
avoids gathers entirely with
VPERMT2PS
cross-register permutations.
Load three 512-bit registers covering 48 floats (16 XYZ triplets), then six permutations separate X, Y, Z — 1.8x faster than scalar deinterleaving:
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
__m512
reg0_f32x16
=
_mm512_loadu_ps
(
ptr
);
// floats  0-15
__m512
reg1_f32x16
=
_mm512_loadu_ps
(
ptr
+
16
);
// floats 16-31
__m512
reg2_f32x16
=
_mm512_loadu_ps
(
ptr
+
32
);
// floats 32-47
// X: 6 from reg0, 5 from reg1, 5 from reg2
__m512i
idx_x_01_i32x16
=
_mm512_setr_epi32
(
0
,
3
,
6
,
9
,
12
,
15
,
18
,
21
,
24
,
27
,
30
,
0
,
0
,
0
,
0
,
0
);
__m512i
idx_x_2_i32x16
=
_mm512_setr_epi32
(
0
,
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
,
10
,
17
,
20
,
23
,
26
,
29
);
__m512
x01_f32x16
=
_mm512_permutex2var_ps
(
reg0_f32x16
,
idx_x_01_i32x16
,
reg1_f32x16
);
*
x_f32x16_out
=
_mm512_permutex2var_ps
(
x01_f32x16
,
idx_x_2_i32x16
,
reg2_f32x16
);
*
y_f32x16_out
=
...
;
// similar code for Y
*
z_f32x16_out
=
...
;
// similar code for Z
RVV
uses segmented loads —
vlseg3e32
returns a
vfloat32m1x3_t
tuple, and
vget
extracts each coordinate.
The vector length adapts dynamically via
vsetvl
, so the same code works on any RISC-V implementation:
1
2
3
4
vfloat32m1x3_t
a_f32m1x3
=
__riscv_vlseg3e32_v_f32m1x3
(
a_ptr
,
vector_length
);
vfloat32m1_t
a_x
=
__riscv_vget_v_f32m1x3_f32m1
(
a_f32m1x3
,
0
);
// all x
vfloat32m1_t
a_y
=
__riscv_vget_v_f32m1x3_f32m1
(
a_f32m1x3
,
1
);
// all y
vfloat32m1_t
a_z
=
__riscv_vget_v_f32m1x3_f32m1
(
a_f32m1x3
,
2
);
// all z
After deinterleaving, the pipeline is the same across all ISAs: compute centroids, build the 3×3 cross-covariance matrix via outer products, decompose it with a McAdams branching-free SVD using 16 fixed Jacobi iterations, and apply a reflection correction when det(R) = -1.
Kernel
Apple M4
Intel Xeon4
RMSD in Float32
1'560 M points/s
970 M points/s
Kabsch in Float32
485 M points/s
290 M points/s
Umeyama in Float32
470 M points/s
285 M points/s
This is one of the few workloads where Apple’s M-cores clearly outperform Xeon4 — NEON’s
vld3q
is a single-instruction stride-3 deinterleave, while Skylake needs six
VPERMT2PS
shuffles across three registers.
Through Python bindings, NumKong’s Kabsch reaches 261 M points/s — roughly 19x
SciPy
’s
Rotation.align_vectors
at 14 M points/s, and 200x
BioPython
’s
SVDSuperimposer
at 1.3 M points/s.
Ozaki Matrix Multiplication
#
Ozaki scheme decomposes a multiplication of wide floats into many multiplications of narrower floats, merging the results.
On GPUs, the typical use is leveraging Float16 Tensor Cores for Float32 GEMMs.
NumKong does something different — Float64 products via Float32 SME outer-product instructions on Apple M4.
The idea: split each Float64 value into three non-overlapping mantissa slices of 19+17+17 bits.
Every slice fits within Float32’s 24-bit significand, so each pairwise product is
exact
in Float64 — the widest cross-product is 19+19 = 38 bits, well under 53.
1
2
3
4
5
6
7
8
nk_fui64_t
bits
=
{.
f
=
value
};
bits
.
u
&=
0xFFFFFFFC00000000ULL
;
// mask to top 19 significant bits
nk_f64_t
high
=
bits
.
f
;
nk_f64_t
remainder
=
value
-
high
;
bits
.
f
=
remainder
;
bits
.
u
&=
0xFFFFFFF000000000ULL
;
// mask to next 17 significant bits
nk_f64_t
mid
=
bits
.
f
;
nk_f64_t
low
=
remainder
-
mid
;
// remaining ≤17 bits
All cross-products where the slice indices sum to ≤ 2 must be accumulated: $A_0 B_0$, $A_0 B_1 + A_1 B_0$, $A_0 B_2 + A_1 B_1 + A_2 B_0$ — six
FMOPA
instructions across three ZA tile accumulators.
The tile schedule is carefully ordered to minimize write-after-write pipeline stalls: ZA3, ZA2, ZA1, ZA3, ZA2, ZA3 — nine cycles instead of fifteen with naive round-robin.
Kernel on Apple M4 at 4096³
Throughput
Precision
nk_dots_packed_f64_serial
1.8 gso/s
6 ULP
nk_dots_packed_f64_neon
5.2 gso/s
0 ULP
nk_dots_packed_f64_smef64
12.9 gso/s
0.9 ULP
The Ozaki SME path is
2.5x
faster than the Dot2 NEON path while achieving sub-1 mean ULP.
The serial path at 6 ULP shows what happens without compensated accumulation.
Ozaki schemes
originated in the work of Ozaki, Ogita, Oishi, and Rump on accurate matrix multiplication, building on earlier error-free summation techniques.
The GPU community adopted them to squeeze Float32 accuracy out of Float16 Tensor Cores — NVIDIA’s cuBLAS uses a 2-way split for TF32.
SME’s outer-product tile architecture makes the cross-product scheduling particularly natural — each
FMOPA
is a full rank-1 update, so interleaving slices across tiles maps directly to the hardware.
Possible improvement directions for kernels:
SIMD-accelerated PRNGs (
#299
), fused Attention kernels, trajectory matching for geospatial (
#186
), and a proper traditional GEMM API (
#312
).
Evolution of GEMMs
#
How Software Diverges
#
The
convergence table above
shows that every vendor agrees on
what
to compute — but the implementations are so different that you cannot write one kernel and compile it for both Intel and Apple.
AMX computes $C \mathrel{{+}{=}} A_{tile} \cdot B_{tile}^T$ — an
inner product
that consumes the entire K dimension inside a single instruction.
SME computes $C \mathrel{{+}{=}} a_{col} \otimes b_{row}$ — a rank-1
outer product
that streams through K one step at a time.
Same goal, fundamentally different data flow:
Intel AMX on Xeon4
Arm SME on Apple M4
Tiles
8 TMM registers, 1 KB each
4 ZA registers, up to 512 elements each
Inputs
i8
,
u8
,
bf16
u1
,
i8
,
u8
,
f16
,
bf16
,
f32
,
f64
…
Operation
Inner product: $C \mathrel{{+}{=}} A \cdot B^T$
Outer product: $C \mathrel{{+}{=}} a \otimes b$
BFloat16 ops
8'192 ops/instruction
512 ops/instruction
Int8 ops
16'384 ops/instruction
1'024 ops/instruction
Latency
~16 cy per
TDPBF16PS
~16 cy amortized per
FMOPA
A layout
Row-major
Column-major
B layout
VNNI-like swizzling
Column-major
Boundary tiles
LDTILECFG
reconfigures dimensions
svwhilelt
predicates — same instruction
Composability
Isolated from AVX-512 — no mixing
Streaming SVE available inside SME mode
AMX is an isolated accelerator: you configure tiles, run tile multiplies, store results, then return to AVX-512 for everything else.
SME shares register state with Streaming SVE — you can interleave outer products with predicated vector arithmetic, comparisons, and reductions without leaving streaming mode.
That is what makes fused GEMM+epilogue kernels like
maxsim_packed
and
bilinear
cleaner on SME than on AMX.
The boundary handling difference is equally practical.
On SME,
svwhilelt
generates a predicate for partial tiles — the same
FMOPA
fires with fewer active lanes, zero code duplication.
On AMX,
LDTILECFG
can reconfigure tile dimensions mid-kernel, but NumKong avoids the overhead by pre-packing remainder rows into a separate row-major edge region processed via AVX-512.
Despite all these differences, both AMX and SME provide extraordinary arithmetic density — thousands of multiply-accumulates per instruction, far more than any scalar or even SIMD vector path.
That density is so high that it becomes worthwhile to reformulate
other
operations as matrix multiplications: cosine similarities become a GEMM plus a norm division, L2 distances become a GEMM plus pre-computed squared norms, retrieval scoring becomes a GEMM plus a running argmax.
The cost of admission is packing your data into the hardware’s preferred layout; the payoff is accessing the fastest arithmetic the chip has.
From Pre-Packing to Epilogues
#
The classical BLAS contract hides this: you hand it two matrices, it repacks internally, every call.
That made sense in 1979 when DGEMM was the only operation and the matrices changed between calls.
But if packing is ISA-specific — VNNI interleaving, column-major tiling, edge regions, boundary predicates — and the data is queried millions of times, hiding it inside every call is wasteful.
NumKong makes packing explicit, and fuses the “what do I actually want from this GEMM” into the kernel as an epilogue.
dots_packed
returns raw dot products.
angulars_packed
fuses norm division into the tile loop — cosine similarity without a second pass over the output matrix.
euclideans_packed
adds pre-computed squared-norm terms to convert dots into L2 distances.
maxsim_packed
tracks a running argmax
inside
the GEMM — for ColBERT-style late interaction scoring, the argmax never materializes the full score matrix.
bilinear
streams through metric matrix rows, computing $a \times M \times b$ for learned distance functions.
The packing itself does far more than reordering bytes.
Since GEMM is $O(N^3)$ and packing is $O(N^2)$, even expensive transforms are asymptotically free — but
what
those transforms do matters:
Transform
What?
Why?
Upcast
E4M3 → BF16, E2M3 → Scaled Int8
Amortize LUT upcasts across all query rows, not per GEMM call
Pad Depth
Zero-pad to SIMD width
Inner loops load full vectors without boundary checks
Save Norms
Store $|b_j|^2$ alongside packed data
To convert GEMMs into pairwise distances in $O(N)$
Tile Layout
VNNI in AMX, columnar in SME
Match the hardware’s expected data flow from the
table above
Break Strides
Add gaps for power of 2 strides
Avoid
cache aliasing
: stride-256 can be ~10x slower than stride-257
The last one deserves a moment.
On a set-associative cache, consecutive rows at a power-of-2 stride all map to the same cache sets, effectively shrinking usable L1/L2 capacity to just the associativity.
Adding a single element of padding — stride 257 instead of 256 — spreads rows across different sets and restores full cache utilization.
It costs one wasted byte per row and saves an order of magnitude on large matrices.
What the user sees is: pack once, query many, fuse your metric.
And the payoff is real — on Intel Xeon4, UInt8 Euclidean distances:
Vector-vector
:
nk_euclidean_u8
— 40.8 gso/s
Matrix-matrix
:
nk_euclideans_packed_u8
— 672 gso/s
That is a
16x
throughput increase from reformulating pairwise distances as a tiled GEMM with a fused epilogue — same input data, same output semantics, same hardware.
Don’t Materialize What You Won’t Need
#
ColBERT-style late-interaction scoring is a good example of a fused epilogue in action: for each query token, find the most similar document token, then sum those max similarities.
Getting per-token embeddings from HuggingFace is straightforward:
1
2
3
4
5
6
7
8
from
transformers
import
AutoModel
,
AutoTokenizer
tokenizer
=
AutoTokenizer
.
from_pretrained
(
"colbert-ir/colbertv2.0"
)
model
=
AutoModel
.
from_pretrained
(
"colbert-ir/colbertv2.0"
)
query
=
model
(
**
tokenizer
(
"what is a dog?"
,
return_tensors
=
"pt"
))
.
last_hidden_state
[
0
]
.
detach
()
.
numpy
()
doc
=
model
(
**
tokenizer
(
"a dog is a pet"
,
return_tensors
=
"pt"
))
.
last_hidden_state
[
0
]
.
detach
()
.
numpy
()
assert
query
.
shape
==
(
7
,
768
)
# 7 tokens × 768-dim embeddings
assert
doc
.
shape
==
(
7
,
768
)
# 7 tokens × 768-dim embeddings
The NumPy way materializes the full score matrix — for real workloads with thousands of tokens, that’s megabytes of temporary memory:
1
2
3
4
5
6
7
import
os
os
.
environ
[
"OMP_NUM_THREADS"
]
=
"1"
# single-threaded for fair comparison
import
numpy
as
np
scores
=
np
.
empty
((
query
.
shape
[
0
],
doc
.
shape
[
0
]),
dtype
=
np
.
float32
)
np
.
matmul
(
query
,
doc
.
T
,
out
=
scores
)
# full score matrix materialized
result
=
scores
.
max
(
axis
=
1
)
.
sum
()
# reduce after the fact
NumKong’s
maxsim_packed
never materializes that intermediate matrix — tiles flow from one register to another and are progressively reduced to a single scalar:
1
2
3
4
import
numkong
as
nk
query_packed
=
nk
.
maxsim_pack
(
query
.
astype
(
nk
.
bfloat16
))
doc_packed
=
nk
.
maxsim_pack
(
doc
.
astype
(
nk
.
bfloat16
))
result
=
nk
.
maxsim_packed
(
query_packed
,
doc_packed
)
# no intermediate matrix
At 2048³ on a single Xeon4 core, NumPy’s
f32 → f32
path reaches 129 gso/s.
NumKong’s BFloat16 path hits 428 gso/s — over
3x
faster while using half the input memory for input, and 4x less memory overall.
The same pattern applies to
nk_bilinear
— computing
aᵀ × C × b
without materializing the
C × b
intermediate vector.
The memory discipline doesn’t stop at kernels — it extends to the runtime itself.
Memory Management & Parallelism Model
#
No hidden allocations.
No hidden threads.
OpenBLAS allocates per-thread buffers via
mmap
behind every GEMM — leading to
14 lock/unlock pairs per small multiply
,
deadlocks after
fork()
, and
silently wrong results
from thread-unsafe allocation.
NumKong never allocates — you own the buffer, you own the threads.
But “you own the threads” is harder than it sounds.
Each thread must call
nk_configure_thread
before any kernel — it flushes denormals to zero on x86 to avoid 100x slowdowns on subnormal inputs, requests AMX tile permission from the Linux kernel via
ARCH_REQ_XCOMP_PERM
, and sets the rounding mode.
Then there is the question of
which
threads to use.
#pragma omp parallel for schedule(static)
splits rows evenly — but Apple M4 has 4 performance cores and 6 efficiency cores running at different frequencies, so equal splits leave the fast cores idle waiting for the slow ones.
Intel server chips have a different problem: 2-socket Xeon4 has multiple NUMA nodes with vastly different memory latencies — a thread on socket 1 reading matrix A from socket 0’s memory pays 2-3x the latency.
The efficient pattern for a large GEMM on a NUMA machine looks like this: each node gets a local copy of the small-ish packed B, works on the slice of A that lives in its local memory, and writes to the corresponding row block of C — also local.
This is the problem
ForkUnion
is being built to solve — a work-in-progress NUMA-aware fork-join thread pool with core pinning and heterogeneous QoS awareness:
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
fu
::
linux_colocated_pool_t
first_socket
,
second_socket
;
first_socket
.
try_spawn
(
topology
.
nodes
[
0
],
cores_per_socket
);
// pin to socket 0 cores
second_socket
.
try_spawn
(
topology
.
nodes
[
1
],
cores_per_socket
);
// pin to socket 1 cores
auto
init
=
[](
auto
)
noexcept
{
nk_configure_thread
();
};
// denormals, AMX, rounding
first_socket
.
for_threads
(
init
);
second_socket
.
for_threads
(
init
);
nk_size_t
half
=
query_rows
/
2
;
first_socket
.
for_slices
(
half
,
[
&
](
auto
slice
)
noexcept
{
nk_dots_packed_bf16
(
queries
+
slice
.
first
*
depth
,
packed_b_first
,
columns
,
depth
,
results
+
slice
.
first
*
columns
);
});
second_socket
.
for_slices
(
query_rows
-
half
,
[
&
](
auto
slice
)
noexcept
{
nk_dots_packed_bf16
(
queries
+
(
half
+
slice
.
first
)
*
depth
,
packed_b_second
,
columns
,
depth
,
results
+
(
half
+
slice
.
first
)
*
columns
);
});
No mutexes, no dynamic allocation on the hot path, no CAS primitives.
Each thread is pinned to a physical core, reads from NUMA-local memory, and writes to its own output rows.
Block-Scaling & Ideological Differences
#
For all the things NumKong tries to achieve, there are lines it does not cross.
MXFP4 and NVFP4 block-scaled formats are one of them.
Block scaling couples elements through shared exponents — a group of 32 values shares one scale factor, so each element’s precision depends on its neighbors.
That makes sense inside a model’s forward pass where training adapts to the structural bias.
It does not make sense inside a dot product primitive where the caller expects every element to be self-contained.
NumKong’s stance: dequantize first, then process.
If your data arrives in MXFP4 format, unpack to 8-bit mini-floats without block scaling before calling NumKong.
The conversion cost is trivial compared to the multiply-accumulate, and you preserve the invariant that
dot(a, b)
treats every element independently.
Reproduce These Numbers
#
To get a quick taste, run a 2048³ BFloat16 batched dot product on your machine and see the throughput:
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
uv init nk-demo
&&
cd
nk-demo
&&
uv add numkong numpy
uv run python -c
"
import numpy as np, numkong as nk, time
height, width, depth = 2048, 2048, 2048
a = np.random.randn(height, depth).astype(nk.bfloat16)
b = np.random.randn(width, depth).astype(nk.bfloat16)
packed = nk.dots_pack(b)
t = time.perf_counter()
scores = nk.dots_packed(a, packed)
elapsed = time.perf_counter() - t
gsos = height * width / elapsed / 1e9
print(f'{height}x{width}x{depth} f16 GEMM: {gsos:.1f} gso/s in {elapsed:.4f}s')
"
You can try replacing the
nk.bfloat16
casts with some more obscure mini-floats or jump to
NumWars
benchmarking suite to see how other operations compare against NumPy, SciPy, PyTorch, Rust
ndarray
,
faer
,
geo
, and others on the same workloads.
