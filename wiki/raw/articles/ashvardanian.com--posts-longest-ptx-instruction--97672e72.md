---
title: "The Longest Nvidia PTX Instruction"
url: "https://ashvardanian.com/posts/longest-ptx-instruction/"
fetched_at: 2026-05-05T07:01:49.684406+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# The Longest Nvidia PTX Instruction

Source: https://ashvardanian.com/posts/longest-ptx-instruction/

The race for AI dominance isn’t just about who has the most computing - it’s increasingly about who can use it most efficiently.
With the recent emergence of DeepSeek and other competitors in the AI space, even well-funded companies are discovering that raw computational power isn’t enough.
The ability to squeeze maximum performance out of hardware through low-level optimization is becoming a crucial differentiator.
One powerful tool in this optimization arsenal is the ability to work directly with PTX, NVIDIA’s low-level
Instruction Set Architecture (ISA)
.
However, PTX instructions are quite different from those for traditional CPU assembly.
PTX
Intermediate Representations (IR)
live between high-level languages like CUDA and the actual hardware-specific Streaming Assembler (SASS) instructions.
PTX is more akin to
Java bytecode
than
x86 Assembly
.
And as we’re about to discover, they can reach lengths that would make even the most verbose x86 “opcodes” blush!
The Longest PTX Mnemonic for Tensor Cores
#
As everyone probably knows, Nvidia chips, starting with 2017
Volta
, come with specialized Tensor Cores for tiled matrix multiplications.
Diving into the somewhat outdated
PTX 8.5 ISA documentation
, we find an interesting specimen on page 432.
Here’s the syntax description for one of such matrix multiplication instructions for the newer generation of Tensor Cores:
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
mma.spvariant.sync.aligned.shape.row.col
{
.satfinite
}
.s32.atype.btype.s32
d
,
a
,
b
,
c
,
e
,
f
;
.shape
=
{
.m16n8k32
,
.m16n8k64
}
.atype
=
{
.u8
,
.s8
}
;
.btype
=
{
.u8
,
.s8
}
;
.spvariant
=
{
.sp
,
.sp
::
ordered_metadata
}
;
mma.spvariant.sync.aligned.shape.row.col
{
.satfinite
}
.s32.atype.btype.s32
d
,
a
,
b
,
c
,
e
,
f
;
.shape
=
{
.m16n8k64
,
.m16n8k128
}
.atype
=
{
.u4
,
.s4
}
;
.btype
=
{
.u4
,
.s4
}
;
.spvariant
=
{
.sp
,
.sp
::
ordered_metadata
}
;
This describes the
mma
“mnemonic” variants for 8-bit and 4-bit integer inputs.
The second variant is particularly interesting as it contains a three-digit dimension in the
shape
field.
Choosing the longest combination, we will end up with the following operation code:
1
2
mma.sp:
:
ordered_metadata.sync.aligned.m16n8k128.row.col.satfinite.s32.u4.u4.s32
d
,
a
,
b
,
c
,
e
,
f
;
At 79 characters (excluding operands), this is one of the longest PTX instructions, and every part of its verbose name serves a specific purpose:
mma
is “Matrix Multiplication & Accumulation”, where 4 of the 6 operands contain the matrices:
a
,
b
,
c
, and
d
.
sp::ordered_metadata
is for the “Structured Sparsity” feature of Tensor Cores, with
e
and
f
operands providing “sparsity metadata” and “sparsity selector” values as 32-bit integers ranging 0-3. This way, we inform the core that some input matrix values are zero.
sync
and
aligned
imply that the operation is synchronous with aligned matrices.
m16n8k128
defines the multiplication shape as $16 \times 8 \times 128$ for $M \times N \times K$ dimensions.
row.col
specifies row-major matrix ordering.
satfinite
enables result saturation and finite clamping for integer inputs.
s32.u4.u4.s32
fixes types to 32-bit integers for
d
and
c
, 4-bit unsigned integers (range 0-15) for
a
and
b
.
This instruction debuted in PTX ISA version 8.5, which coincided with the introduction of Hopper-generation H100 cards featuring the SM 9.0 architecture.
The Longest PTX Instruction for Tensor Cores
#
The instruction becomes even more impressive when we include operands, which are typically arrays of register names.
Here’s a complete example:
1
2
3
4
5
6
7
.reg
.b32
%Ra
<
4
>
,
%Rb
<
4
>
,
%Rc
<
4
>
,
%Rd
<
4
>
;
.reg
.u32
%Re
;
mma.sp:
:
ordered_metadata.sync.aligned.m16n8k128.row.col.satfinite.s32.u4.u4.s32
{%
Rd0
,
%Rd1
,
%Rd2
,
%Rd3
}
,
{%
Ra0
,
%Ra1
,
%Ra2
,
%Ra3
}
,
{%
Rb0
,
%Rb1
,
%Rb2
,
%Rb3
}
,
{%
Rc0
,
%Rc1
,
%Rc2
,
%Rc3
}
,
%Re
,
0x0
;
PTX supports a rich type system with various
variable
declarations, including
vectors
and
multi-dimensional arrays
:
1
2
3
4
5
.global
.v4
.f32
V
;             // a length-4 vector of floats
.shared
.v2
.u16
uv
;            // a length-2 vector of unsigned ints
.global
.v4
.b8
v
;             // a length-4 vector of bytes
.local
.u16
kernel
[
19
][
19
]
;    // a 19x19 array of unsigned shorts
.shared
.u8
mailbox
[
128
]
;      // a 128-byte array of unsigned chars
While PTX restricts register names to ASCII characters, it doesn’t explicitly limit their length.
Documentation
suggests that all implementations support a minimum length of at least 1024 characters.
The NVIDIA PTX assembler (
ptxas
) may have internal limits, but they’re generous enough that most developers never encounter them.
Myself included.
Compiling SASS
#
Understanding the supported matrix shapes and data types is crucial, but it doesn’t tell us everything about the underlying hardware-specific SASS instructions.
Let’s see what happens when we compile our PTX code:
1
2
$ ptxas -o longest_ptx.cubin -arch
=
sm_90a longest_ptx.ptx
$ cuobjdump -sass longest_ptx.cubin
|
grep -i MMA
Initially, we won’t see anything - the instructions get optimized out.
However, if we add load and store operations, we’ll see:
1
2
3
4
5
$ ptxas -o longest_ptx.cubin -arch
=
sm_90a longest_ptx.ptx
$ cuobjdump -sass longest_ptx.cubin
|
grep -i MMA
> /*0150*/ IMMA.SP.16864.U8.U8 R4, R4.ROW, R8.COL, RZ, R0, 0x0
;
/* 0x0000000804047237 */
> /*0230*/ IMMA.SP.16864.U8.U8 R8, R8.ROW, R12.COL, RZ, R0, 0x0
;
/* 0x0000000c08087237 */
Interestingly, on Hopper, our $16 \times 8 \times 128$ matrix multiplication gets split into two $16 \times 8 \times 64$ operations, as indicated by the
16864
code.
Moreover, it’s emulated with
uint8_t
multiplication, not physically implemented in
uint4_t
!
That’s true for both Hopper and the same on the upcoming Blackwell!
More Tensor Core Instructions
#
The H100 introduced a new family of instructions - “Warp-Group Matrix-Multiply-Add” (
wgmma
).
These offer more flexibility in matrix shapes and data types but with some trade-offs:
At least one operand must reside in shared memory, with dual shared memory operands potentially offering 5-10% better performance
Thread synchronization has evolved significantly:
Pre-Volta: Threads individually perform scalar
FMA
.
Volta:
HMMA
instruction synchronizes 8-thread “quadpairs”.
Ampere: Synchronization spans all 32 threads in a warp.
Hopper: Synchronizes 4 continuous warps, meaning 128 threads.
Blackwell (SM 100a) with PTX ISA 8.7 introduces yet another paradigm shift with the
tcgen05
family of instructions, including countless new asynchronous primitives like
tcgen05.alloc
,
tcgen05.dealloc
,
tcgen05.relinquish_alloc_permit
,
tcgen05.ld
,
tcgen05.st
,
tcgen05.wait
,
tcgen05.cp
,
tcgen05.shift
,
tcgen05.mma
,
tcgen05.mma.sp
,
tcgen05.mma.ws
,
tcgen05.mma.ws.sp
,
tcgen05.fence
and
tcgen05.commit
.
Some of those instructions have an extremely wide type palette, including 4- and 6-bit floating point representations and additional operands for scaling factors and rounding modes.
Honorable Mentions
#
While our MMA instruction is impressive, there are other contenders for the longest instruction title.
Reduction operations
with vector types can be quite verbose:
1
2
3
4
red.relaxed.cluster.global.add.noftz.L2:
:
cache_hint.v4.bf16x2
[
a
],
b
;
red.async.relaxed.cluster.shared:
:
cluster.mbarrier:
:
complete_tx:
:
bytes.min.u32
[
addr
],
b
,
[
mbar_addr
]
;
Parallel Synchronization instructions
also pack quite a few characters:
1
2
clusterlaunchcontrol.try_cancel.async.shared:
:
cta.mbarrier:
:
complete_tx:
:
bytes.multicast:
:
cluster:
:
all.b128
[
addr
],
[
mbar
]
;
At 107 characters, this last one beats our MMA instruction in the raw character count.
However, the MMA instruction still seems more complex in practice with only two operands versus MMA’s six and fewer period-separated tokens (7 vs 12).
Closing Thoughts on CUTLASS
#
I’ve been fighting against high-level abstractions for many years, but in rare cases, they make sense.
The increasing complexity of the PTX ISA is one of those cases.
With Volta, Nvidia became the first major hardware vendor to switch from C-like compiler intrinsics to more expressive
wmma::
C++-like intrinsics for tiled matrix multiplications:
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
using
namespace
nvcuda
;
wmma
::
fragment
<
wmma
::
matrix_a
,
16
,
16
,
16
,
half
,
wmma
::
row_major
>
a_frag
;
wmma
::
fragment
<
wmma
::
matrix_b
,
16
,
16
,
16
,
half
,
wmma
::
col_major
>
b_frag
;
wmma
::
fragment
<
wmma
::
accumulator
,
16
,
16
,
16
,
half
>
c_frag
;
// To initialize, we can call `wmma::fill_fragment`
// or skip it for synthetic benchmarks:
wmma
::
mma_sync
(
c_frag
,
a_frag
,
b_frag
,
c_frag
);
// Impossible condition to prevent optimization:
if
(
threadIdx
.
x
==
-
1
)
wmma
::
store_matrix_sync
(
NULL
,
c_frag
,
16
,
wmma
::
mem_row_major
);
Now that the instructions are becoming so complex, the
CUTLASS
and its underlying CuTe “atoms” library are becoming the new de facto standards for writing high-performance code.
Coming from Nvidia’s in-house engineers, they pack a ton of first-party knowledge on how to optimize for their hardware.
An argument can be made that they should have become part of the CUDA Toolkit before the amazing
CCCL
project, but integrating both into a CMake-based C++ project isn’t hard.
Check out
less_slow.cpp
repository
for examples on how to integrate them and feel free to suggest new kernels for
less_slow.ptx
and
less_slow.cu
files 🤗
It’s important to note that CUDA programming isn’t as niche as it was 10 years ago, and NVIDIA’s developer portals can be a great source of information and a platform to meet some of the NVIDIA engineers who are working on the next generation of CUDA compilers and libraries.
There is an
official Discord server
, and
Pradeep Ramani
from the CUTLASS team has helped me a lot with navigating the project 🙏
Appending
#
PTX Sources
#
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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
.version
8
.5
// `sp::ordered_metadata` requires PTX 8.5+
.target
sm_90a
// `sm_90a` maps to Hopper-generation Streaming Multiprocessors
.address_size
64
// 64-bit addressing
.visible
.entry
my_kernel_name
(.
param
.u64
output_ptr
)
{
// Allocate PTX registers for the operands.
.reg
.b32
%Ra
<
4
>
,
%Rb
<
4
>
,
%Rc
<
4
>
,
%Rd
<
4
>
;
.reg
.u32
%Re
;
.reg
.u64
%out
;
// Load the pointer to global memory from the parameter.
ld.param.u64
%out
,
[
output_ptr
]
;
// Perform the matrix multiplication. On Hopper this should compile into two
// IMMA instructions, emulating U4 operations with U8:
//
//      IMMA.SP.16864.U8.U8 R4, R4.ROW, R8.COL, RZ, R0, 0x0 ;
//      IMMA.SP.16864.U8.U8 R8, R8.ROW, R12.COL, RZ, R0, 0x0 ;
//
// Each will perform half of the operation resulting in a 16x8x64 product.
mma.sp:
:
ordered_metadata.sync.aligned.m16n8k128.row.col.satfinite.s32.u4.u4.s32
{%
Rd0
,
%Rd1
,
%Rd2
,
%Rd3
}
,
{%
Ra0
,
%Ra1
,
%Ra2
,
%Ra3
}
,
{%
Rb0
,
%Rb1
,
%Rb2
,
%Rb3
}
,
{%
Rc0
,
%Rc1
,
%Rc2
,
%Rc3
}
,
%Re
,
0x0
;
// Store the result in global memory... without this, the `mma` will be optimized out.
st.global.b32
[
%out
],
%Rd0
;
st.global.b32
[
%out
+
4
],
%Rd1
;
st.global.b32
[
%out
+
8
],
%Rd2
;
st.global.b32
[
%out
+
12
],
%Rd3
;
ret
;
}
To compile for Hopper:
1
2
$ ptxas -o longest_ptx.cubin -arch
=
sm_90a longest_ptx.ptx
$ cuobjdump -sass longest_ptx.cubin
|
grep -i mma
To compile on Blackwell, change the file header to:
1
2
3
.version
8
.7
// needed for Blackwell support
.target
sm_100a
// `sm_100a` maps to Blackwell-generation Streaming Multiprocessors
.address_size
64
// 64-bit addressing
