---
title: "Oodle 2.8.14 with Mac ARM64"
url: "http://cbloomrants.blogspot.com/2021/02/oodle-2814-with-mac-arm64.html"
fetched_at: 2026-05-05T07:01:48.016268+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Oodle 2.8.14 with Mac ARM64

Source: http://cbloomrants.blogspot.com/2021/02/oodle-2814-with-mac-arm64.html

Oodle 2.8.14 is out.  The
full changelog is at RAD
.
The highlights are :
## Release 2.8.14 - February 15, 2021

$* *enhancement* : BC7 encoding is faster ; slightly different encodings at higher speed with similar quality

$* *new* : Mac ARM64 build now provided ; Mac example exes are fat x64+arm64
$* *new* : Apple tvOS build now provided

$* *deprecation* : Mac 32 bit x86 build no longer provided
We're also now shipping plugin integrations for Unreal 4.26
Kraken decompression is wicked fast on the M1 :
Kraken, Win-x64 msvc-1916, lzc99.kraken.zl6
lzt99 : 24,700,820 ->10,013,788 =  3.243 bpb =  2.467 to 1
decode           : 16.444 millis, 2.26 c/B, rate= 1502.09 MB/s

Kraken, Mac-x64 xcode-12.0.0, lzc99.kraken.zl6
lzt99 : 24,700,820 ->10,013,788 =  3.243 bpb =  2.467 to 1
decode           : 16.183 millis, 2.10 c/B, rate= 1526.36 MB/s
(emulated!)

Kraken, Mac-ARM64 xcode-12.0.0, lzc99.kraken.zl6
lzt99 : 24,700,820 ->10,013,788 =  3.243 bpb =  2.467 to 1
decode           : 11.967 millis, 1.55 c/B, rate= 2064.13 MB/s

Win64 run is :
AMD Ryzen 9 3950X (CPU locked at 3393 MHz, no turbo)
Zen2, 16 cores (32 hyper), TSC at 3490 MHz 

Mac runs on Macbook Mini M1 at 3205 MHz

Mac x64 is emulated on the M1
c/B = cycles per byte should be taken with some salt as we have trouble finding real clock rates, but it's clear the M1
has superior IPC (instructions per clock) to the Zen2.  It seems to be about the same speed as the Zen2 in emulated x64!
It will be interesting to see what the M1 high performance variants can do.
Some more speeds cuz I like big numbers :
Macbook Mini M1 ARM64 :

Mermaid, Normal, lzt99 :
24,700,820 ->11,189,930 =  3.624 bpb =  2.207 to 1
encode (x1)      : 299.154 millis, 37.21 c/B, rate= 82.57 MB/s
decode (x30)     : 6.438 millis, 0.80 c/B, rate= 3836.60 MB/s

Mermaid, Optimal2, lzt99 :
24,700,820 ->10,381,175 =  3.362 bpb =  2.379 to 1
encode (x1)      : 3.292 seconds, 409.43 c/B, rate= 7.50 MB/s
decode (x30)     : 7.134 millis, 0.89 c/B, rate= 3462.57 MB/s

Selkie, Normal, lzt99 :
24,700,820 ->13,258,742 =  4.294 bpb =  1.863 to 1
encode (x1)      : 213.197 millis, 26.51 c/B, rate= 115.86 MB/s
decode (x30)     : 3.126 millis, 0.39 c/B, rate= 7901.52 MB/s

Selkie, Optimal2, lzt99 :
24,700,820 ->12,712,659 =  4.117 bpb =  1.943 to 1
encode (x1)      : 1.861 seconds, 231.49 c/B, rate= 13.27 MB/s
decode (x30)     : 3.102 millis, 0.39 c/B, rate= 7962.55 MB/s
