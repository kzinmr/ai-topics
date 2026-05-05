---
title: "Patcher Part 2 : Some Rolling Hashes"
url: "http://cbloomrants.blogspot.com/2023/09/patcher-part-2-some-rolling-hashes.html"
fetched_at: 2026-05-05T07:01:47.395112+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Patcher Part 2 : Some Rolling Hashes

Source: http://cbloomrants.blogspot.com/2023/09/patcher-part-2-some-rolling-hashes.html

Let's go through some options for rolling hashes.
By "rolling hash" I mean a hash that works on a finite window of bytes, and
that window slides incrementally across a buffer.  To compute a rolling hash
efficiently, you may want be able to incrementally add new bytes to the hash and
subtract out bytes as they leave the window (emphasis on "may").
We'll need two types of rolling hash in later discussion : small window (64 bytes or less)
rolling hash to fingerprint a small run of bytes, and large/arbitrary window.
For very small windows, eg. 16 bytes or less, you may want to just grab two 64-bit words,
mask them to the window length you need, then hash them.  This may be better than explicit
rolling.
For windows of 32 or 64 bytes, it is handy to use the size of the machine word to make a
finite window hash for you.
Any hash function can be made to roll over 32 or 64 bytes by making the hash value shift up
in the machine word as you add each byte.  That makes it so the contribution of each byte
is shifted out after 32 or 64 steps.  No explicit removal is needed.
h = (h<<1) + func(byte)

or

h = (h * M) + func(byte)

with M even
this method is used by "Fast CDC" with "func" as a table lookup, which they call a "gear" for
unknown reasons.  This method is also used in zpaq with an even multiply and "func" = (byte + constant).
Obviously many variations are possible here.
In my patcher, the speed of this operation is crucial, it's on the critical path.  The best I found,
in terms of being sufficiently strong and very fast were :
#define RollHash(h,ptr) (((h)+(*(ptr))+271828182u)*(1865811235122147682ULL))

or

#define RollHash(h,ptr) ( ((h)<<1) + c_hashes_table64[*(ptr)] )
The table lookup method seems to be slightly faster in scalar code, but the multiplicative method
may be more amenable to SIMD and other cases where fast table lookups are not available.  YMMV.
Next on to rolling hashes with long/arbitrary windows.
A well known rollable hash is the simple multiplicative hash ("Rabin-Karp") :
to add one byte B to the hash H :

H = H * M + B;

with some multiplier constant M
After k bytes this becomes :
H = M^(k-1) * B[0] + M^(k-2) * B[1] + ... B[k-1]
We can then obviously roll out old bytes from the front of the window by subtracting them off :
H contains B[0..k-1]
roll out B[0]
roll in B[k]

H -= M^(k-1) * B[0]
H = H * M + B[k]
(of course M^(k-1) is pre-computed)
In the literature they talk about these hashes being over a finite field and do funny modulos, but in the real world we never want to do
that, we want H to be a full 32 or 64 bit machine word, and choose M to be a large prime with good bit scattering properties.
Note that this form of hash has some strength issues.  It has a degeneracy for B=0.  New bytes that are added only affect the bottom
bits of the hash, but the hash has its strongest bits at the top of the word.  To help fix this you can run some kind of bit mix on it
before actually using it for hash table lookup.  Something like :
(_lrotl(H,16) ^ H)
is the simplest option, but there are many others.
Also note that rather than just adding in the new byte B, you can of course also add (B+C) with a constant C, or table[B] with some table lookup.
Newer librsync (librsync 2.2.0) uses Rabin-Karp with M = 0x08104225U , and a non-zero initial seed, which acts to count the number of bytes that have been
hashed.
The rolling hash used by (older) rsync is a two-part checksum, inspired by Adler-32.
It does :
to add one byte B to two hashes :

H1 += B;
H2 += H1;
After k bytes this becomes :
H1 = B[0] + B[1] + B2[] ...  

just the sum

H2 = B[0]*k + B[1]*(k-1) + B[2]*(k-2) + ... B[k-1]

sum of bytes multiplied by how long they've been in the window
This is obviously rollable, with :
remove old byte :

H1 -= B[0];
H2 -= B[0]*k;

add new byte :

H1 += B[k];
H2 += H1;
to actually use these for hash lookups, they are mixed, like :
H = ((H2&0xFFFF)<<16) | (H1&0xFFFF);
There are well-known weaknesses of this Adler-32-like hash.
rsync suggests that using (B+C) instead of B helps a bit.  You could of course also use table[B].
I think that this scheme is strictly weaker, and also slower, than the multiplicative method, so I think it is simply deprecated.
