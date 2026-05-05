---
title: "xxHash for small keys: the impressive power of modern compilers"
url: "http://fastcompression.blogspot.com/2018/03/xxhash-for-small-keys-impressive-power.html"
fetched_at: 2026-05-05T07:00:59.102111+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# xxHash for small keys: the impressive power of modern compilers

Source: http://fastcompression.blogspot.com/2018/03/xxhash-for-small-keys-impressive-power.html

Several years ago,
xxHash
was created as a companion error detector for
LZ4
frame format
. The initial candidate for this role was
CRC32
, but it turned out being several times slower than LZ4 decompression, nullifying one of its key strength.
After some research, I found the great
murmurhash
, by
Austin Appleby
, alongside its validation tool
SMHasher
. It nearly fitted the bill, running faster than LZ4, but still a bit too close to my taste. Hence started a game to see how much speed could be extracted from a custom hash formula while preserving good distribution properties.
A lot of things happened since that starting point, but the main take away from this story is : xxHash was created mostly as a checksum companion, digesting long inputs.
Fast forward nowadays, and xxHash is being used in more places than it was originally expected. The design has been expanded to create a second variant, XXH64, which is successful in video content and data bases.
But for several of these uses cases, hashed keys are no longer necessarily "large".
In some cases, the need to run xxHash on small keys resulted in the
creation of dedicated variants
, that cut drastically through the decision tree to extract just the right suite of operations for the desired key. And it works quite well.
That pushes the hash algorithm into territories it was not explicitly optimized for. Thankfully, one of SMHasher's test module was dedicated for speed on small keys, so it helped to pay attention to the topic during design phase. Hence the performance on small key is correct, but the dedicated function push it to another level.
Let's analyse the 4-byte hash example.
Invoking the regular
XXH32()
function on 4-bytes samples, and running it on my Mac OS-X 10.13 laptop (with compilation done by llvm9), I measure
233 MH/s
(Millions of hashes per second).
Not bad, but running the dedicated 4-bytes function, it jumps to
780 MH/s
. That's a stark difference !
Let's investigate further.
xxHash offers an
obscure build flag named XXH_PRIVATE_API
. The initial intention is to make all
XXH_*
symbols
static
, so that they do not get exposed on the public side of a library interface. This is useful when several libraries use xxHash as an embedded source file. In such a case, an application linking to both libraries will encounter multiple
XXH_*
symbols, resulting in naming collisions.
A side effect of this strategy is that function bodies are now available during compilation, which makes it possible to inline them. Surely, for small keys, inlining the hash function might help compared to invoking a function from another module ?
Well, yes, it does help, but there is nothing magical. Using the same setup as previously, the speed improves to
272 MH/s
. That's better, but still far from the dedicated function.
That's where the power of inlining can really kick in.
In the specific case that the key has a predictable small length
, it's possible to pass as length argument a
compile-time constant
, like
sizeof(key)
, instead of a variable storing the same value. This, in turn, will allow the compiler to make some drastic simplification during binary generation, through dead code removal optimization, throwing away branches which are known to be useless.
Using this trick on the now inlined
XXH32()
, speed increases to
780 MH/s
, aka the same speed as dedicated function.
I haven't checked but I wouldn't be surprised if both the dedicated function and the inlined one resulted in the same assembly sequence.
But the inlining strategy seems more powerful : no need to create, and then maintain, a dedicated piece of code. Plus, it's possible to generate multiple variants, by changing the "length" argument to some other compile-time constant.
object
XXH32()
XXH32 inlined
XXH32 inlined +
length constant
dedicated XXH32 function
4-bytes field
233 MH/s
272 MH/s
780 MH/s
780 MH/s
Another learning is that inlining is quite powerful for small keys, but the
XXH_PRIVATE_API
build macro makes a poor job at underlining its effectiveness.
As a consequence, next release of xxHash will introduce a
new build macro, named
XXH_INLINE_ALL
. It does exactly the same thing, but its performance impact is better documented, and I suspect the name itself will make it easier for developers to anticipate its implications.
