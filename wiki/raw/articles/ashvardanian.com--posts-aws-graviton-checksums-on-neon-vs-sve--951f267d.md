---
title: "2x Faster Hashes on AWS Graviton: NEON → SVE2"
url: "https://ashvardanian.com/posts/aws-graviton-checksums-on-neon-vs-sve/"
fetched_at: 2026-05-05T07:01:49.005191+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# 2x Faster Hashes on AWS Graviton: NEON → SVE2

Source: https://ashvardanian.com/posts/aws-graviton-checksums-on-neon-vs-sve/

AWS is the world’s largest cloud provider.
It’s hard to comprehend how many billions of times per second their instances compute string hashes and SHA-256 file checksums!
After releasing
StringZilla v4
, I spun up instances of the last 3 Graviton generations, exploring optimization opportunities across NEON, SVE, and SVE2 extensions.
Graviton 2
Graviton 3
Graviton 4
Context
Availability year
2020
2022
2024
Process node
7 nm, TSMC
5 nm, TSMC
3nm, TSMC
Architecture
Neoverse N1
Neoverse V1
Neoverse V2
Max cores
64
64
96
AWS instance family
*6g
*7g
*8g
Specifics
Vector extensions
NEON
NEON, SVE
NEON, SVE, SVE2
Encryption extensions
NEON+AES
NEON+AES 🤦‍♂️
NEON+AES, SVE+AES
SVE vector length
128b
256b
128b 🤦‍♂️
Yes, SVE on Gravitons is tricky.
More on that later.
Given how diverse the architectures are across generations, these results likely apply to NVidia’s Grace, Apple’s M-series, Google’s Axion, Microsoft’s Cobalt, and other Arm-based chips.
Small String Keys
#
The most common use-case for string hashing is hash tables, like
std::unordered_map<std::string, ...>
in C++ or
std::collections::HashMap<String, ...>
in Rust.
The latency is often dominated by state construction, unaligned loads, and digest computation, rather than the actual mixing function.
Higher throughput is better.
Hashing Library
Graviton 2
Graviton 3
Graviton 4
Rust standard
Hasher
0.28 GiB/s
0.38 GiB/s
0.52 GiB/s
Google’s
crc32fast
₃₂
0.36 GiB/s
0.48 GiB/s
0.56 GiB/s
MurmurHash3 from
murmur3
₃₂
0.47 GiB/s
0.51 GiB/s
0.64 GiB/s
aHash from
ahash
0.76 GiB/s
1.00 GiB/s
1.04 GiB/s
xxHash3 from
xxhash-rust
0.84 GiB/s
1.11 GiB/s
1.05 GiB/s
StringZilla 🦖
0.40 GiB/s
0.60 GiB/s
1.42 GiB/s
To reproduce the results, check the
StringWars benchmark
.
A typical word-level token is between 6 and 10 bytes long.
aHash
and
xxHash3
perform very well!
Both output high-entropy 64-bit hashes with excellent avalanche resistance as measured in Austin Appleby’s
SMHasher
suite and my
HashEvals
.
Both are far better than the default hashers in C++, Rust, and Python standard libraries, as well as the 32-bit MurmurHash3 and CRC32 algorithms.
StringZilla lags behind on Graviton 2 and 3, but leaps ahead on Graviton 4, where the AES extensions for SVE are available.
It’s interesting to dissect how much of our boost from 0.60 GiB/s to 1.42 GiB/s comes from NEON vs SVE.
For that we can recompile StringWars disabling some of the optimizations:
1
2
3
SZ_USE_NEON
=
0
SZ_USE_NEON_AES
=
0
SZ_USE_NEON_SHA
=
0
SZ_USE_SVE
=
0
SZ_USE_SVE2_AES
=
0
\
RUSTFLAGS
=
"-C target-cpu=native"
STRINGWARS_DATASET
=
xlsum.csv
STRINGWARS_TOKENS
=
words
\
cargo criterion --features bench_hash bench_hash --jobs
1
Results are:
0.1108 GiB/s with serial code only,
0.6577 GiB/s with NEON & AES, but without SVE,
1.4240 GiB/s with SVE2 & AES enabled:
2.16x faster
than NEON!
NEON alone improved 10% between Graviton 3 and 4, but SVE2 AES delivered another 116% on top of that.
In StringZilla the gains come from a separate implementation path for strings up to 16 bytes, combining:
Fast predicated loads:
svld1_u8(svwhilelt_b8(0, len), text)
AES-based mixing:
svaesmc_u8(svaese_u8(state, zero), key)
Similar optimizations are available on x86 and were backported with the
ClickHouse
team to
Intel Westmere
-generation chips, where AVX2 and AVX-512 aren’t available.
Maybe with more community participation we can make the hash functions more friendly to older Arms as well.
Longer Strings and Files
#
For longer strings around 4 KB - roughly one RAM page, the middle ground between a large network packet and a small file - StringZilla’s 64-byte block algorithm really shines:
Hashing Library
Graviton 2
Graviton 3
Graviton 4
Rust standard
Hasher
2.53 GiB/s
3.28 GiB/s
3.71 GiB/s
Google’s
crc32fast
₃₂
14.70 GiB/s
16.47 GiB/s
18.23 GiB/s
MurmurHash3 from
murmur3
₃₂
1.85 GiB/s
2.40 GiB/s
2.58 GiB/s
aHash from
ahash
4.63 GiB/s
6.84 GiB/s
8.87 GiB/s
xxHash3 from
xxhash-rust
10.03 GiB/s
15.77 GiB/s
18.18 GiB/s
StringZilla 🦖
14.00 GiB/s
20.90 GiB/s
23.00 GiB/s
For longer inputs, we often want more than 64 bits of hash.
SHA-256 has become the de-facto standard for file integrity checksums and is ubiquitous in security applications.
It’s in Bitcoin transactions, Git commits, TLS certificates, content-addressable filesystems like IPFS, package managers like NPM, Docker, and Debian’s APT.
In AWS, it’s in S3 ETags starting with SigV4 (2012), Lambda identifiers, DynamoDB streams, and pretty much everywhere else.
Higher is better.
SHA-256 Implementation
Graviton 2
Graviton 3
Graviton 4
Pure Rust
sha2
0.23 GiB/s
0.29 GiB/s
0.34 GiB/s
BoringSSL-based
ring
1.41 GiB/s
1.50 GiB/s
1.63 GiB/s
StringZilla 🦖
1.11 GiB/s
1.16 GiB/s
1.25 GiB/s
This is where I’m declaring an ideological defeat.
I’ve been trying to keep Assembly in StringZilla to a minimum, focusing on C intrinsics instead.
SHA-256 is heavily standardized with little room for innovation.
All state-of-the-art implementations, including most SSL/TLS libraries, rely on the same hand-rolled or Perl-generated Assembly.
My attempts to match or beat them with C intrinsics have failed.
The compiler is too eager to reorder instructions or introduce unnecessary moves.
So the next version of StringZilla may switch to inline Assembly in a few places.
That said, raw performance isn’t everything.
Real-World Performance
#
Despite not being the fastest, StringZilla’s SHA-256 is still very usable given how it integrates with the rest of the library.
It’s exposed to C99 and C++11, as well as Python 3, Node.js via N-API, Swift, and Go via cgo, and works with arbitrary files, including memory-mapped ones.
In Python, the loop that used to look like this:
1
2
3
4
5
6
7
import
hashlib
with
open
(
"xlsum.csv"
,
"rb"
)
as
streamed_file
:
hasher
=
hashlib
.
sha256
()
while
chunk
:=
streamed_file
.
read
(
4096
):
hasher
.
update
(
chunk
)
checksum
=
hasher
.
hexdigest
()
Now looks like this:
1
2
3
from
stringzilla
import
Sha256
,
File
,
Str
mapped_file
=
File
(
"xlsum.csv"
)
checksum
=
Sha256
()
.
update
(
mapped_file
)
.
hexdigest
()
Both output the same hexadecimal digest:
7278165ce01a4ac1e8806c97f32feae908036ca3d910f5177d2cf375e20aeae1
.
OpenSSL, powering Python’s
hashlib
, has a faster pure Assembly kernel.
But StringZilla avoids file I/O overhead with memory mapping and skips Python’s abstraction layers, making the end-to-end time better:
OpenSSL-backed
hashlib.sha256
time: 12.623s.
End-to-end StringZilla time: 4.052s -
3x faster!
SVE’s Broken Promise
#
Arm’s major selling point for SVE was simple: write once, run anywhere with variable vector lengths from 128 to 2048 bits.
In practice, no major CPU has ever shipped with 1024 or 2048-bit SVE.
Worse, AWS regressed from 256-bit SVE in Graviton 3 to 128-bit in Graviton 4.
1
2
3
4
5
ubuntu@graviton4 $ sudo dmesg
|
grep -i sve
>
[
0.008053
]
SVE: maximum available vector length
16
bytes per vector
>
[
0.008054
]
SVE: default vector length
16
bytes per vector
ubuntu@graviton4 $ getconf LEVEL1_DCACHE_LINESIZE
>
64
# 64 bytes per cache line, 16 bytes per vector register
AWS likely traded vector width for more cores within the same power envelope, and that’s not the only trade-off.
The variable vector length creates real software design challenges!
You can’t pack multiple “SVE vectors” into a structure and pass them around - there’s no ABI for that.
SVE code ends up harder to scope and reuse.
Some library maintainers compile with
-msve-vector-bits=128
to get fixed-width SVE, but then you may as well use NEON.
Compared to x86, the situation seems worse at every level:
AVX2 is 256-bit wide and more uniform than the 128-bit fragmented NEON.
AVX-512 is fragmented too, but at least it’s always 512-bit wide and brings substantial new functionality. SVE is almost never even 256 bits wide.
AMX is easier to access than SME, despite little documentation and complex swizzling logic.
After a lot of experimentation with SVE in
StringZilla
,
SimSIMD
, and
USearch
, the wins have been rare.
Scatter/gather
can be 30% faster in synthetic “Less Slow” benchmarks
, some histogram operations benefit, but most code runs just as fast or faster on NEON.
RISC-V’s Vector Extension (RVV) comes with similar challenges, but instead of hiding the vector length (VL), the programming model exposes it.
I’d be curious to see how usable it is in practice beyond micro-kernels in larger systems design tasks.
So far AVX-512 has been by far the most usable ISA beyond tiny kernels, in part because its width matches the cache line size on x86.
Granted, on some CPUs cache-coherency protocols operate on 2x wider 128-byte lines, but that’s a minor issue compared to the overall usability.
Takeaways
#
If you’re optimizing for Arm,
start with NEON
.
Add SVE only where benchmarks prove it wins - like AES operations on Graviton 4.
Don’t bet on wider vectors just yet and let me know if you find workloads where SVE consistently outperforms NEON 🤗
