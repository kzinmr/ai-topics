---
title: "Tuning TLS: AES-256 Beats ChaCha20 on Every CPU"
url: "https://ashvardanian.com/posts/chacha-vs-aes-2025/"
fetched_at: 2026-05-05T07:01:48.982441+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Tuning TLS: AES-256 Beats ChaCha20 on Every CPU

Source: https://ashvardanian.com/posts/chacha-vs-aes-2025/

Ten years ago Cloudflare published the
“Do the ChaCha: better mobile performance with cryptography” blog post
showing
“ChaCha20-Poly1305”
edging out “AES-256-GCM” on phones that lacked AES acceleration.
Today almost every CPU ships with wide
SIMD
registers and
AES instructions
.
Apple’s A14 ₂₀₂₀, M1 ₂₀₂₀, and every successor include AES acceleration, and the same is true for most mid-range and flagship Android SoCs.
So does that 2015 advice still hold in 2025?
I wanted a definitive answer for the ongoing
UCall
rewrite, so I compared them across different AWS server SKUs with the
ring
Rust crate, which keeps the benchmarks reproducible while exercising the same kernels shipped in mobile TLS stacks.
TLDR: AES wins.
Sometimes, by 3x!
Benchmark Results
#
The benchmarking setup is as follows:
Workloads: encryption and decryption.
Input sizes: tiny inputs ~100 bytes (for header-only HTTP messages), larger messages ~1 KB (closer to TCP Maximum Transmission Unit).
Hardware: Apple M2 Pro, Intel Ice Lake on
*6i
and Sapphire Rapids on
*7i
, AMD Zen 3 on
*6a
, Zen 4 on
*7a
, Zen 5 on
*8a
, AWS Graviton 2 on
*6g
, Graviton 3 on
*7g
, Graviton 4 on
*8g
.
The suite also includes the
sodiumoxide
bindings for the minimalistic
libsodium
, as well as OpenSSL bindings and key generation benchmarks.
Assuming that key generation is not on the critical path for most applications, I’ve excluded those numbers here.
You can reproduce them by cloning the
StringWars repository
and running:
1
2
3
RUSTFLAGS
=
"-C target-cpu=native"
STRINGWARS_DATASET
=
dataset/path.txt
\
STRINGWARS_TOKENS
=
lines
STRINGWARS_FILTER
=
"cryption/ring"
\
cargo criterion --features bench_encryption bench_encryption
The “Speedup” column lists the AES-256-GCM throughput divided by ChaCha20 across the ~100 B and 1 KB payloads, so 150% means AES is 1.5× faster.
I’ve tried to sort the table by the approximate release date of the CPU architecture - from 2020 to 2025, but there is often a year-long gap between the architecture announcement and the actual availability of consumer hardware, so take it with a grain of salt.
Each cell contains the single-core throughput in MB/s for the given cipher and operation, defining a range between the tiny and larger inputs.
Naturally, heavily vectorized encryption kernels perform better on larger inputs.
CPU
ChaCha20
AES-256
AES Speedup
Encryption
Decryption
Encryption
Decryption
Graviton 2
168 - 503
197 - 491
292 - 1,065
412 - 1,104
91 - 118%
Zen 3
436 - 1,425
598 - 1,296
524 - 2,849
770 - 2,420
24 - 93%
Ice Lake
396 - 1,158
461 - 1,151
577 - 2,617
820 - 2,618
62 - 127%
Zen 4
456 - 1,410
486 - 1,244
652 - 3,040
796 - 2,290
53 - 100%
Graviton 3
249 - 778
275 - 696
470 - 1,926
656 - 2,246
114 - 185%
Sapphire
393 - 1,195
422 - 1,081
614 - 2,891
850 - 2,476
79 - 135%
M2 Pro
327 - 1,088
402 - 1,021
661 - 3,131
1,069 - 3,932
134 - 236%
Zen 5
467 - 1,580
475 - 1,755
862 - 3,731
1,012 - 5,044
99 - 162%
Graviton 4
280 - 895
310 - 794
563 - 2,436
753 - 2,781
122 - 211%
Most OpenSSL- or GnuTLS-based stacks already prioritize AES-GCM suites, so these figures mirror what production servers negotiate today; ChaCha mainly surfaces when clients lack AES hardware and force the fallback.
It’s worth noting that the
ring
crate borrows most of its assembly kernels from BoringSSL, which in turn is a fork of OpenSSL.
So these numbers are representative of what you would get in most production-grade TLS libraries.
That said, Rust bindings of several crypto libraries showed 3x lower performance, so binding quality matters as well.
Conclusion
#
If you need a hardware-friendly TLS cipher in 2025 you should probably pick AES-256-GCM, which conveniently matches the default ordering in modern OpenSSL and GnuTLS builds.
The “mobile devices need ChaCha20” advice from 2015 no longer applies to modern chips.
Skip standards compliance and you can push even further.
The
“Too Much Crypto” 2019 paper
suggests that both ChaCha20 and AES are overkill:
AES-256: performs 14 rounds, but needs only ~11.
ChaCha20: performs 20 rounds, but needs only ~8.
I’ve used the same AES primitives to build the high-velocity, high-throughput StringZilla hashes
described a couple of articles ago
.
SVE2 AES extensions, which most TLS stacks ignore, already delivered a
40% hashing uplift on Graviton 4
for tiny inputs.
Wider CPUs only amplify SIMD-friendly code, and the fresh Zen 5 based
*8a
instances pushed StringZilla to 2'241 MiB/s — roughly 2× faster than xxHash3 and aHash.
So pick AES and vectorize!
