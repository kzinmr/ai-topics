---
title: "Scaling Elections with GPUs and Mojo across Nvidia and AMD 🔥"
url: "https://ashvardanian.com/posts/scaling-elections/"
fetched_at: 2026-05-05T07:01:49.078891+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Scaling Elections with GPUs and Mojo across Nvidia and AMD 🔥

Source: https://ashvardanian.com/posts/scaling-elections/

Last summer, me, Chris Lattner, and a bunch of other people across the industry gathered together for a GPU-programming hackathon at the AGI House in San Francisco.
After one too many LLM optimizations, I decided to accelerate something nobody asked for!
Most elections use simple plurality voting — whoever gets the most votes wins.
But there are “fairer” methods that consider ranked preferences, like the Schulze method used by Wikimedia Foundation, Debian, and pirate parties worldwide.
The catch?
It scales $O(n³)$ with the number of candidates.
For $n=10000$, ten thousand candidates, that’s a trillion operations.
Time to bring out the GPUs!
I don’t carry an illusion that the Schulze method is perfect.
No voting system is.
Nor do I think that direct democracy is a silver bullet.
Nor do I think that governments in short term will transition to it.
Still, the same algorithmic ideas apply to other problems, and later in the article we’ll see what “algebraic graph theory” and “tropical semirings” have to do with it.
Birds Eye View and the Results
#
Let’s start with the dessert - the results!
I wrote an adaptation of the Schulze voting method in a tiled parallel fashion.
There is a reference implementation in Numba, that JIT-compiles our Python code into optimized parallel kernel using LLVM under the hood.
There is a hand-written CUDA C++ implementation, tailored for Nvidia GPUs, wrapped with PyBind11, built without a single line of CMake, callable from Python.
There is a Mojo 🔥 implementation, that runs on both CPUs and GPUs, across Nvidia and AMD.
During the hackathon, our friends from
Nebius
gave everyone access to their Nvidia H100 GPUs.
Later, I’ve compared them to massive AWS
m8i.metal-96xl
with 6th Gen Intel Xeon Scalable CPUs, spanning 384 cores across 2 sockets.
AMD GPU testing proved challenging during this timeframe, though I was eventually able to evaluate MI300 and MI355X with some community help!
Implementation
2'048
4'096
8'192
16'384
32'768
Intel, 384 CPU cores
Numba Python
34.4 gcs
86.8 gcs
74.6 gcs
76.7 gcs
101.4 gcs
Mojo 🔥
37.9 gcs
59.8 gcs
76.6 gcs
80.7 gcs
82.3 gcs
Mojo 🔥, with SIMD
62.1 gcs
171.5 gcs
357.3 gcs
369.0 gcs
293.1 gcs
Nvidia GPUs
CUDA, H100
182.7 gcs
264.1 gcs
495.3 gcs
600.7 gcs
921.4 gcs
Mojo 🔥, H100
153.4 gcs
232.6 gcs
408.0 gcs
635.3 gcs
893.7 gcs
AMD GPUs
Mojo 🔥, MI300
456.7 gcs
906.3 gcs
1.5 tcs
1.9 tcs
2.8 tcs
Mojo 🔥, MI355X
830.8 gcs
1.5 tcs
2.4 tcs
2.9 tcs
3.5 tcs
Each implementation felt different!
I haven’t spent much time optimizing the Mojo code, given the hackathon-ish nature of the project, and didn’t have prior experience with it.
What struck me most was Mojo’s ability to address a challenge that frameworks like OpenAI’s Triton and Nvidia’s CuTile don’t solve: not only can the kernel code be efficient, but the surrounding orchestration logic as well.
More on that later.
Voting Methods 101
#
There’s an entire field of voting theory, and a plethora of voting methods.
You can group them:
By ballot type - single-mark (choose one), approval (choose any), ranking (order all).
By winner count - single-winner (most methods), multi-winner (proportional representation, single transferable vote).
By number of rounds - single-round (plurality, approval), multi-round (runoff, instant-runoff), and iterative (Schulze, Kemeny-Young).
Another way is to group them by computational complexity:
$O(n)$: Plurality, approval
$O(n²)$: Most ranked methods, Borda
$O(n³)$: Schulze, Floyd-Warshall-based Condorcet
NP-hard: Kemeny-Young (optimal Condorcet ranking)
A couple of relevant terms here.
“Floyd-Warshall” refers to the classic algorithm for finding shortest paths in a weighted graph with positive or negative edge weights (but no negative cycles).
“Condorcet” refers to a candidate who would win a head-to-head election against every other candidate.
This term is named after the French mathematician and philosopher Marquis de Condorcet, who proposed the concept in the 18th century.
It’s specific to voting systems, and describes one of many important criteria that voting methods may or may not satisfy.
Method
Condorcet
Complexity
Strategic Risk
Ballot Type
Output
Plurality
No
$O(n)$
High
Single choice
Winner only
Instant Runoff
No
$O(n^2)$
Medium
Ranked
Winner only
Schulze
Yes
$O(n^3)$
Low
Ranked
Winner(s)
Kemeny-Young
Yes
NP-hard
Very Low
Ranked
Complete ranking
But why go through all this trouble instead of a simple plurality vote?
Schulze vs Plurality: Vote Splitting Problem
#
Imagine 100 voters choosing a programming language for a project:
Ranking
Voters
Preference
Group 1
35
Python
Group 2
33
Rust
Group 3
32
Go
Plurality winner is Python with 35% of votes.
But this is wrong!
65% of voters prefer anything but Python!
Let’s assume we have the full rankings for each group:
Voters
1st
2nd
3rd
35 voters
Python
Rust
Go
33 voters
Rust
Go
Python
32 voters
Go
Rust
Python
Now check head-to-head matchups:
Python vs Rust: 35 vs 65 (33 + 32) → Rust wins
Python vs Go: 35 vs 65 (32 + 33) → Go wins
Rust vs Go: 68 vs 32 → Rust wins
So with Schulze, Rust wins as the “Condorcet winner”.
Seems more fair, right?
The Participation Paradox: When Voting Hurts
#
Now imagine a different scenario.
Some rankings are received, Rust is winning.
Then more people show up, who prefer Rust the most…
Yet, paradoxically, their participation causes Rust to lose!
For that, we need to reproduce a “Condorcet cycle”.
Voters
1st
2nd
3rd
4th
1 voter
Python
Java
Rust
Go
2 voters
Python
Java
Go
Rust
2 voters
Rust
Python
Go
Java
4 voters
Go
Java
Rust
Python
1 voter
Java
Python
Rust
Go
Rust beats Python: 6-4.
Python beats Go: 6-4.
Java beats Rust: 8-2.
Go beats Java: 6-4.
There’s a cycle: Rust > Python > Go > Rust, and no clear Condorcet winner exists!
So, the Schulze method resolves this through strongest paths analysis and nominates Java as the winner.
Now, one more voter arrives, ranking: Java > Python > Go > Rust.
Things change!
Rust beats Python: 6-5 (same winner, closer).
Python beats Go: 7-4 (Python strengthened).
Java beats Python: 6-5 (Java strengthened).
Java beats Rust: 9-2 (Java strengthened).
Go beats Java: 6-5 (same winner, closer).
Before Extra Voter
After Extra Voter
The voter’s lower preferences (Python 2nd, Go 3rd) accidentally helped Python more than their first choice (Java) because:
✅ Java’s victory over Rust grew: 8 → 9.
❌ But Python gained NEW victories: 6-6 ties became 7-6 wins over Rust and Go.
🎯 Python went from 0 clear wins to 2 clear wins, while Java maintained 1 clear win.
Python wins!
Bizarre, but here’s a line-count-optimized validation script in Python:
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
import
numpy
as
np
def
pairwise_preferences
(
rankings
):
n
=
max
(
np
.
max
(
r
)
for
r
in
rankings
)
+
1
;
prefs
=
np
.
zeros
((
n
,
n
),
dtype
=
np
.
uint32
)
[[
prefs
.
__setitem__
((
p
,
o
),
prefs
[
p
,
o
]
+
1
)
for
i
,
p
in
enumerate
(
r
)
for
o
in
r
[
i
+
1
:]]
for
r
in
rankings
]
return
prefs
def
widest_paths
(
prefs
):
n
,
p
=
prefs
.
shape
[
0
],
np
.
zeros
((
prefs
.
shape
[
0
],
prefs
.
shape
[
0
]),
dtype
=
np
.
uint32
)
[[
p
.
__setitem__
((
i
,
j
),
prefs
[
i
,
j
])
for
i
in
range
(
n
)
for
j
in
range
(
n
)
if
i
!=
j
and
prefs
[
i
,
j
]
>
prefs
[
j
,
i
]]]
[[[
p
.
__setitem__
((
j
,
k
),
max
(
p
[
j
,
k
],
min
(
p
[
j
,
i
],
p
[
i
,
k
])))
for
k
in
range
(
n
)
if
i
!=
k
and
j
!=
k
]
for
j
in
range
(
n
)
if
i
!=
j
]
for
i
in
range
(
n
)]
return
p
def
winner
(
rankings
):
p
=
widest_paths
(
pairwise_preferences
(
rankings
))
wins
=
[(
p
[
i
]
>
p
[:,
i
])
.
sum
()
for
i
in
range
(
4
)]
return
[
'Python'
,
'Rust'
,
'Go'
,
'Java'
][
np
.
argmax
(
wins
)],
max
(
wins
)
r
=
[
np
.
array
([
0
,
3
,
1
,
2
])]
+
[
np
.
array
([
0
,
3
,
2
,
1
])]
*
2
+
[
np
.
array
([
1
,
0
,
2
,
3
])]
*
2
+
[
np
.
array
([
2
,
3
,
1
,
0
])]
*
4
+
[
np
.
array
([
3
,
0
,
1
,
2
])]
i_w
,
i_n
=
winner
(
r
);
r
.
append
(
np
.
array
([
3
,
0
,
2
,
1
]));
f_w
,
f_n
=
winner
(
r
)
print
(
f
"Initial (10 voters):
{
i_w
}
wins (
{
i_n
}
victories)
\n
After adding Java-first voter:
{
f_w
}
wins (
{
f_n
}
victories)
\n
{
'✓ Paradox confirmed!'
if
i_w
!=
f_w
else
'✗ No paradox'
}
"
)
Optimizing Schulze
#
Serial Baseline Algorithm
#
From the algorithmic perspective, the Schulze procedure contains 3 steps:
Aggregates votes into a matrix of pairwise preferences. On input from every voter we receive a ranking of candidates, and we construct a matrix of pairwise preferences, where
d[i,j]
is the number of voters who prefer candidate
i
to candidate
j
.
Approach the matrix of pairwise preferences as an adjacency matrix of a graph, and compute the strongest paths for all pairs of candidates.
Extract the winners from the graph, based on the strength of the paths between them.
The first and third steps are somewhat easy, but the second step can be quite computationally expensive.
If implemented naively, with the variation of a Floyd-Warshall algorithm, it has a complexity of $O(n^3)$, where $n$ is the number of candidates.
So for a small number of candidates, like 10, it’s not a big deal.
But if you want to build a direct democracy even on a scale of a 100'000 candidates, you’ll be dealing with a matrix 1e10 cells, and would probably want to use parallel hardware like GPUs to handle it.
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
# Input: d[i,j], the number of voters who prefer candidate i to candidate j.
# Output: p[i,j], the strength of the strongest path from candidate i to candidate j.
for
i
in
range
(
n
):
for
j
in
range
(
n
):
if
i
≠
j
:
p
[
i
,
j
]
=
d
[
i
,
j
]
if
d
[
i
,
j
]
>
d
[
j
,
i
]
else
0
for
k
in
range
(
n
):
for
i
in
range
(
n
):
if
i
≠
k
:
for
j
in
range
(
n
):
if
j
≠
k
and
j
≠
i
:
p
[
i
,
j
]
=
max
(
p
[
i
,
j
],
min
(
p
[
i
,
k
],
p
[
k
,
j
]))
Similar to matrix multiplication, the Schulze method contains three nested loops.
Unlike matrix multiplication, the Schulze method contains a sequential dependency over the
k
loop.
That limits the amount of parallelism we can extract from it.
Moreover, similar to a lot of graph algorithms, it uses a semi-ring, where the addition is replaced by the
max
operation, and the multiplication is replaced by the
min
operation.
Unlike addition and multiplication, those operations are not invertible.
That limits the applicability of some of the general purpose GPGPU methods, but makes this a perfect example of Algebraic Graph Theory and a great showcase for the kinds of traversal orders that are used in combinatorial problems implemented on GPUs.
Similar ideas were exploited a couple of articles before to achieve
109x faster Levenshtein distance calculation on Nvidia H100 GPUs
for Bioinformatics, compared to Nvidia’s own CuDF library.
Parallel Algorithm
#
Assuming the core of the Schulze method is similar to the Floyd-Warshall algorithm, we can reuse the ideas published on these topics over the years.
Moreover, there is a nice blog-post and codebase by Jared Moore and Josh Kalapos showcasing the logic:
In Blocked Floyd-Warshall, we use a subroutine that processes each its given block.
However, the blocks are not all independent and must be processed in three separate phases.
First, in the dependent phase, we have to process the
k
-th diagonal block.
Then, in the partially dependent phase, we process the
k
-th row and the
k
-th column of blocks.
Lastly, in the independent phase, we process the remaining blocks.
Their pseudo-code, however, contains a few inconsistencies.
Moreover, in the Schulze method, some of the cells have to be skipped.
Accounting for the logic changes, our Numba kernels will look as follows.
For every tile:
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
@njit
def
compute_strongest_paths_tile_numba
(
c
:
np
.
ndarray
,
c_row
:
int
,
c_col
:
int
,
a
:
np
.
ndarray
,
a_row
:
int
,
a_col
:
int
,
b
:
np
.
ndarray
,
b_row
:
int
,
b_col
:
int
,
):
for
k
in
range
(
tile_size
):
for
i
in
range
(
tile_size
):
for
j
in
range
(
tile_size
):
if
(
(
c_row
+
i
!=
c_col
+
j
)
and
(
a_row
+
i
!=
a_col
+
k
)
and
(
b_row
+
k
!=
b_col
+
j
)
):
replacement
=
min
(
a
[
a_row
+
i
,
a_col
+
k
],
b
[
b_row
+
k
,
b_col
+
j
])
if
replacement
>
c
[
c_row
+
i
,
c_col
+
j
]:
c
[
c_row
+
i
,
c_col
+
j
]
=
replacement
Those tiles will be enumerated in multiple times, and every iteration would contain three phases:
Dependent phase, where we process the
k
-th diagonal block.
Partially dependent phase, where we process the
k
-th row and the
k
-th column of blocks.
Independent phase, where we process the remaining blocks.
Putting it all together, we get the following Numba kernel:
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
35
36
37
38
39
40
41
42
43
44
@njit
(
parallel
=
True
)
def
compute_strongest_paths_numba
(
preferences
:
np
.
ndarray
)
->
np
.
ndarray
:
# Populate the strongest paths matrix based on direct comparisons
num_candidates
=
preferences
.
shape
[
0
]
strongest_paths
=
np
.
zeros
((
num_candidates
,
num_candidates
),
dtype
=
np
.
uint32
)
for
i
in
range
(
num_candidates
):
for
j
in
range
(
num_candidates
):
strongest_paths
[
i
,
j
]
=
preferences
[
i
,
j
]
if
preferences
[
i
,
j
]
>
preferences
[
j
,
i
]
and
i
!=
j
else
0
# Compute the strongest paths using Floyd-Warshall-like algorithm with tiling
tiles_count
=
(
num_candidates
+
tile_size
-
1
)
//
tile_size
for
k
in
range
(
tiles_count
):
# Dependent phase
k_start
=
k
*
tile_size
# f(S_kk, S_kk, S_kk)
compute_strongest_paths_tile_numba
(
strongest_paths
,
k_start
,
k_start
,
strongest_paths
,
k_start
,
k_start
,
strongest_paths
,
k_start
,
k_start
)
# Partially dependent phase (first of two)
for
i
in
prange
(
tiles_count
):
if
i
==
k
:
continue
i_start
=
i
*
tile_size
# f(S_ik, S_ik, S_kk)
compute_strongest_paths_tile_numba
(
strongest_paths
,
i_start
,
k_start
,
strongest_paths
,
i_start
,
k_start
,
strongest_paths
,
k_start
,
k_start
)
# Partially dependent phase (second of two)
for
j
in
prange
(
tiles_count
):
if
j
==
k
:
continue
j_start
=
j
*
tile_size
# f(S_kj, S_kk, S_kj)
compute_strongest_paths_tile_numba
(
strongest_paths
,
k_start
,
j_start
,
strongest_paths
,
k_start
,
k_start
,
strongest_paths
,
k_start
,
j_start
)
# Independent phase (with fewer nested branches)
for
i
in
prange
(
tiles_count
):
if
i
==
k
:
continue
i_start
=
i
*
tile_size
for
j
in
range
(
tiles_count
):
if
j
==
k
:
continue
j_start
=
j
*
tile_size
# f(S_ij, S_ik, S_kj)
compute_strongest_paths_tile_numba
(
strongest_paths
,
i_start
,
j_start
,
strongest_paths
,
i_start
,
k_start
,
strongest_paths
,
k_start
,
j_start
)
return
strongest_paths
Having that many conditionals in
compute_strongest_paths_tile_numba
isn’t great.
We’ll remove them later.
Porting to CUDA for H100 GPUs
#
Translating the Numba code to CUDA can be straightforward, but it was further complicated by the fact that the same high-level procedure has to call 3 separate kernels with completely different grid sizes.
Again, the
moorejs/APSP-in-parallel
was a good starting point.
Its core logic was correct, but it contained several excessive
__syncthreads
calls, and required more addressing logic to skip the cells that have to be skipped.
The basic CUDA kernel follows a similar pattern to the Numba version:
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
template
<
uint32_t
tile_size
>
__global__
void
step_independent_
(
candidate_idx_t
n
,
candidate_idx_t
k
,
votes_count_t
*
graph
)
{
candidate_idx_t
const
j
=
blockIdx
.
x
;
candidate_idx_t
const
i
=
blockIdx
.
y
;
candidate_idx_t
const
bi
=
threadIdx
.
y
;
candidate_idx_t
const
bj
=
threadIdx
.
x
;
if
(
i
==
k
&&
j
==
k
)
return
;
__shared__
alignas
(
16
)
votes_count_t
a
[
tile_size
][
tile_size
];
__shared__
alignas
(
16
)
votes_count_t
b
[
tile_size
][
tile_size
];
__shared__
alignas
(
16
)
votes_count_t
c
[
tile_size
][
tile_size
];
c
[
bi
][
bj
]
=
graph
[
i
*
tile_size
*
n
+
j
*
tile_size
+
bi
*
n
+
bj
];
a
[
bi
][
bj
]
=
graph
[
i
*
tile_size
*
n
+
k
*
tile_size
+
bi
*
n
+
bj
];
b
[
bi
][
bj
]
=
graph
[
k
*
tile_size
*
n
+
j
*
tile_size
+
bi
*
n
+
bj
];
__syncthreads
();
_process_tile_cuda
<
tile_size
,
false
,
true
>
(
//
c
,
a
,
b
,
bi
,
bj
,
//
i
*
tile_size
,
j
*
tile_size
,
//
i
*
tile_size
,
k
*
tile_size
,
//
k
*
tile_size
,
j
*
tile_size
//
);
graph
[
i
*
tile_size
*
n
+
j
*
tile_size
+
bi
*
n
+
bj
]
=
c
[
bi
][
bj
];
}
Hardware-Specific Optimizations
#
I explored several Nvidia Hopper-specific features:
Hopper introduced
DPX instructions
for fused min/max operations.
While these seemed perfect for the tropical semiring operations in Schulze, the available intrinsics (
__vimax3_u32
,
__vimin3_u32
) are symmetric (both min or both max) rather than performing one of each.
Worth keeping in mind for other algorithms though — I successfully used them in StringZilla v4 for
Levenshtein distance calculations
.
The newer Tensor Memory Access (TMA) asynchronous extensions looked interesting as well.
Dealing with TMA, however, was harder than with any other hardware-specific interface I’ve used in years.
I need to debug it further, before I can share any performance characteristics, but I wouldn’t expect massive gains.
TMA provides gains when your compute is already running on Tensor Cores, operating at PetaFLOPs throughput, while our logic is orders of magnitude slower.
Exploring Mojo 🔥
#
Code Generation and Portability
#
One interesting discovery: modern language models generate quite reasonable Mojo code.
I provided Claude Code with the Numba and CUDA implementations plus a few documentation links, and the generated Mojo compiled successfully.
Like most junior developers, it tended to over-allocate temporary structures and missed some idiomatic patterns, but overall provided a solid starting point.
The most impressive aspect was portability.
The Mojo code written for Nvidia GPUs worked on AMD hardware with
zero modifications
— no vendor-specific code paths, no conditional compilation.
For context, adapting the CUDA C++ implementation to run with AMD’s
hipcc
required
200+ lines of changes
.
Language Design Observations
#
Some of the current Mojo design decisions felt unusual at first.
Namely, the name of the
@parameter
decorator
for compile-time evaluation, the mutable-by-default
var
variables.
One area that I struggled with: feature-gating GPU code from CPU-only builds.
CUDA C++ uses
#ifdef __CUDA_ARCH__
for this; Mojo will likely develop similar mechanisms as cross-compilation matures.
Other things, although not traditional, felt quite nice:
LLVM-style
“address spaces”
vs
__shared__
qualifiers in CUDA C++
The
stack_allocation
API for explicit buffer control
Move semantics with
x^
instead of
std::move(x)
That’s syntactic sugar!
What about my bread and butter - GPGPU and SIMD?
GPU Orchestration
#
One of CUDA’s pain points is the boilerplate around kernel launches.
Correctly launching a CUDA kernel
requires ~100 lines when you properly handle errors, streams, and synchronization.
Mojo streamlines this significantly:
var ctx = DeviceContext()
var matrix_size = num_candidates * num_candidates

var host_graph = ctx.enqueue_create_host_buffer[DType.uint32](matrix_size)
var device_graph = ctx.enqueue_create_buffer[DType.uint32](matrix_size)
host_graph.enqueue_copy_to(device_graph)
ctx.synchronize()

ctx.enqueue_function[gpu_independent_kernel[32]](
    device_graph.unsafe_ptr(), num_candidates, k,
    grid_dim=(tiles_count, tiles_count, 1),
    block_dim=(32, 32, 1)
)
ctx.synchronize()

device_graph.enqueue_copy_to(host_graph)
ctx.synchronize()
Better ergonomics with stronger type safety.
This design has room for sophisticated multi-GPU orchestration libraries that interleave device operations more efficiently than traditional CUDA patterns allow.
CPU Vectorization
#
Mojo’s SIMD support works across architectures (AVX-512, NEON, etc.) with the same code:
fn process_tile_cpu_simd_independent[tile_size: Int, simd_width: Int](...):
    constrained[tile_size % simd_width == 0,
                "tile_size must be divisible by simd_width"]()
    for k in range(tile_size):
        for bi in range(tile_size):
            var a_val = a[bi * tile_stride + k]
            for chunk in range(tile_size // simd_width):
                var bj = chunk * simd_width
                var c_vec = c.load[width=simd_width](bi * tile_stride + bj)
                var b_vec = b.load[width=simd_width](k * tile_stride + bj)
                var a_vec = SIMD[DType.uint32, simd_width](a_val)
                var min_val = min(a_vec, b_vec)
                var new_c = max(c_vec, min_val)
                c.store[width=simd_width](bi * tile_stride + bj, new_c)
This code is only marginally longer than the scalar version but delivers
4x speedups
on AVX-512 CPUs.
As someone who maintains on the order of ~1000 open-source hand-written SIMD and GPGPU kernels, I’d love to see more work in the packaging and distribution of such code.
GCC and many other compilers have tried to provide some form of multi-versioning, but all fell short in ergonomics and usability.
Borrowing more ideas from
Halide
would also be a potential value add for people writing HPC kernels, but that’s a topic for another day.
Reflections and Next Steps
#
Overall, it was a great hackathon!
Chris Lattner
talked about Mojo’s GPU support,
Raja Koduri
explained the reasons for the success of the CUDA ecosystem in the last decade,
Tri Dao
gave the first public talk on FlashAttention-3… now superseded by his FlashAttention-4, and
Dylan Patel
shared some insights on the data-center market.
Thanks to
Sasha Krassovsky
,
Pradeep Ramani
, and
Evan Ovadia
for collaborating with me on this one!
The code is available on
GitHub
and there is clearly more exploration coming around async TMA-like memory transfers and tropical algebra applications beyond voting!
Thanks to
Jeremy Nixon
,
Rohan Pandey
, and
Kyle Morris
for bringing the AGI house together and hosting all of us!
Thanks to
Nebius
for compute!
Stay tuned for the next hackathon!
