---
title: "Notes on float and multi-byte delta compression"
url: "http://cbloomrants.blogspot.com/2023/07/notes-on-float-and-multi-byte-delta.html"
fetched_at: 2026-05-05T07:01:47.721937+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Notes on float and multi-byte delta compression

Source: http://cbloomrants.blogspot.com/2023/07/notes-on-float-and-multi-byte-delta.html

When attempting to encode and compress delta values that are larger than 1 byte, and then feeding them to a back-end compressor which
inherently works on bytes, you need to transform them to make the larger integer values more friendly to the byte-based compressor.
Say you have S16 or S32 values that have a mean around zero.  For example maybe you started with U32 or F32 values and took
deltas of neighbors, so now you wind up with S32 delta values with an expected mean of zero to send.
Let's talk about the S16 case to be concrete.  The mean is zero, the most likely values are +1,-1, then +2,-2, etc.
If you just transmit those as bytes, you have :
0 : 0x0000
+1,-1 : 0x0001 , 0xFFFF
+2,-2 : 0x0002 , 0xFFFE
Now if you feed those to a compressor which does byte-oriented entropy coding, it is seeing the bytes :
00,00,00,01,FF,FF,00,02,FF,FE
The bad thing that's happened here is that for -1 and -2, the sign bits have changed the top byte, so we've introduced the 0xFF
high byte as a very probable event.  We're actually requiring the entropy coder to send the sign bit *twice*.  To differentiate
between +1 and -1, the low byte is either 01 or FF , so that is equivalent to sending the absolute value and a sign bit; but then
the high byte is 00 or FF, so we are sending the sign bit again.
(an alternate way to say it is we have created a very strong correlation between the high and low byte of each S16, but since we
are entropy coding with bytes we should have *decorrelated* the two bytes; by creating a correlation which is not used by the compressor
we are wasting bits)
One solution is to
"fold up" negatives
.  That is,
fold up the negative numberline and interleave it with the positive, so we get :
0 : 0x0000
+1,-1 : 0x0002 , 0x0001
+2,-2 : 0x0004 , 0x0003
Now the high byte just models magnitude, not the sign bit.  There is still some correlation (a zero in the high byte makes it
much more likely that the low byte is low), but it's less wasteful.
Folding up negatives is common practice when you want to send a signed value (like a delta) using a variable bit length method like
Golomb coding that only works on positive values.
However, there is a very simple alternative to folding up negatives which often works as well or better : just bias by 0x80.
0 : 0x0080
+1,-1 : 0x0081 , 0x007F
+2,-2 : 0x0082 , 0x007E
Now for the key range of small delta in [-128,+127] the high byte is always zero, so it is not redundantly encoding the sign.
Once the delta gets bigger, the high byte is affected, but at that point the low byte is becoming more random, so it's not terrible.
If you are not separating the high and low byte for entropy coding, then it's slightly better to bias by 0x8080.  This makes the
most probable value of the high and low byte both equal to 0x80 which is better if their statistics are mixed in the entropy coder.
The high and low byte of the S16 delta will have quite different statistics (the high byte is much more likely to be zero).  There are a variety of ways to handle this : 1. Using a compressor like
LZMA or Oodle Leviathan that has "pos bits" ("suband3") in the context for encoding literals.  If you are using a good compressor
like LZMA or Leviathan, it's often/sometimes best to leave the values alone and let it capture this model in the way it chooses.
2. De-interleave values to separate them into blocks of like statistics; eg. HLHLHL -> HHHHLLLL.  This allows compressors that do
entropy splits to find those blocks.  Oodle will find optimal split points at higher compression level.  (zip optimizers like kzip will
also).  Many other compressors will just reset entropy at fixed intervals, like every 64K bytes, which will work fine if your
data is big enough.  Deinterleaving can also helps when the compressor cuts the data into independent chunks, or if it has a small window.
There are other options if the high byte is very often 00, such as run-length encoding the high bytes, or using variable-length byte
encodings, but those cause you to break the regular structure pattern of the data, which plays poorly with modern LZ's like Leviathan
and LZMA that can use structure stride patterns to improve compression, so we generally don't use them anymore (YMMV).
For S32 deltas, you should bias by 0x80808080.  Again when the delta is exactly zero, we are feeding all 0x80 bytes to the entropy coder;
when the delta is small but non-zero we are changing only the bottom byte and keeping as many top bytes 0x80 as possible.  Essentially we're trying
to prevent carries from the low bits affecting the higher bytes as much as possible.
TLDR:
For S16 deltas, bias by 0x8080 , for S32 deltas, bias by 0x80808080.
De-interleaving multi-byte integers into homogenous streams can help, particularly with weaker back-end compressors.


(note that it's pretty impossible to draw any reliable rules about whether de-interleaving helps or not, it depends a lot on the data
and the details, from file to file it can vary a lot whether it helps or not)
Okay, now if your data was float (F32), we're still going to use the integer delta scheme.
What we do is just reinterpret the F32 as U32.  That gives us an integer that is the exponent and mantissa {E.M} in a piecewise linear
logarithmic scale.  See reference on that :
05-26-09 - Storing Floating Points ("log int")
Lossless Compression of Predicted Floating-Point Values
You might think that doing linear predictors on the piecewise logarithmic integer is a bit funny, but it's sort of not.  Who's to say that
the linear scale of the values is the right one?  And we use different curves for values all the time, for example we do linear math on U8 pixels
which are in sRGB gamma encoding, and that is actually better for compression than doing it in linear light.
What is a problem for this simple reinterp of F32 to U32 is signed values.  If all your F32 values are positive or all are negative, it's no problem, but if there's a mix of positive and
negative you have a problem, because just reinterpretting to U32 does not give you values that linearly delta in the right way. (the negative number line is reversed)
That's sort of easy to fix.  You just take the negative floats (which use a flag bit in the top position) and turn them into proper negative
two's complement integers.  eg. take off the sign bit and negate the integer, which is the same as replicating down that sign bit and xor'ing.
(Floats also have this quirk that -0.f and 0.f are distinct, which you can choose to preserve or not in the conversion to int)
That gets you integers that you can delta across zero, but there's still a problem, which is that floats have this huge range across zero.
See
05-26-09 - Storing Floating Points ("log int")
for more about that.
If you want to losslessly encode the floats, you're stuck.
If you are okay with some lossiness, then changing the very small floats to denormal (the lossy "log int" scheme) works great.
Fundamentally, floating point data is always problematic because it's encoding precision that's not
actually helpful, and rarely has the source of the data actually put the precision in a useful place.
That is, in a bit rate allocation sense, the floats have allocated tons of bits to represent values very close to zero, and that is rarely
actually helpful.
For example in geometry meshes, you don't actually want vertices near zero to have way more precision, and values that cross the origin to
be almost infinitely far apart in number-line space.  It would be much better to store verticies in fixed point so the precision is some
known quantity (say 0.1 millimeter or whatever), rather than the variable mess we get with F32.
Similarly for float images, we often store the LDR range in [0.0,1.0] , but that also makes no sense.  Between [0.0] and [0.0000000000000000001]
you have as many points as between [0.0000000000000000001] and [1.0].  We use [0,1] as a convenient standard convention, but it actually sucks
for bit allocation because it's putting way too number-line points between black and so-dark-it-is-for-all-practical-purposes-black, which makes
the integer delta between black and "very dark" be a huge number.
If you know that you have only non-negative floats and you're okay with a lossy encoding, one option is to just add a constant, such
as += 1.0 ; this makes all your floats >= 1.0 and gets rid of all the negative exponent number-line space that you didn't actually want.
If you started with floats in [0,1] , then doing += 1 takes them to [1,2] which has all the same exponent, so they are now all of equal
precision.  If you want more precision near zero, you can do += 0.5 or 0.25, etc. depending on your knowledge of how much precision you actually
need.  If you decide you wants 2^-b to be the smallest step you care about, then you add 2^-(b-23) bias (b >= 23).
TLDR:
For floats, just reinterpret F32 as U32.
If the floats have a mix of positive and negative, convert the sign bit to two's-complement signed S32.
Consider lossy elimination of negative zero -0.f
If you didn't actually want the huge precision for floats near zero, a simple lossy encoding is just to do float += constant,
which works for non-negative floats where you don't know the high end of the range so you can't just use fixed point.
(since we'll follow up with delta'ing values, we don't care about the net bias that adding a constant causes; if
we were not delta'ing you could subtract off that constant as an integer after the reinterpret to integer)
Okay, so now that we have the basics, let's try compressing some float deltas.
I will show some results on the data used in
Aras P's Float Compression series
which you can download here :
github float_compr_tester
Numbers :
Oodle Kraken level 5 (Optimal1) with no chunking :

textest losslesscompress r:\aras\rrs -c8 -l5 -s0

 uncompressed_size = 99,045,768
 comp_size_nofilter = 26,701,149 = 2.16 bpb
 comp_size_deinterleaved = 24,287,665 = 1.96 bpb
 comp_size_deinterleaved_bytedelta = 22,841,299 = 1.84 bpb
 comp_size_dpcm = 24,367,933 = 1.97 bpb
 comp_size_dpcm_deinterleaved = 21,854,276 = 1.77 bpb
 comp_size_best = 20,291,724 = 1.64 bpb

"nofilter" = just compress the dat a with no transforms
"deinterleaved" = convert HLHLHL to HHHLLL
"deinterleaved_bytedelta" = deinterleave then delta on the bytes in each section (Aras' scheme)
"dpcm" = predictor delta on the floats
"dpcm_deinterleaved" = dpcm then deinterleave bytes
"best" = take the best filter choice per file
I have confirmed that "comp_size_deinterleaved_bytedelta = 22,841,299" exactly matches what Aras P's float_compr_tester testbed produces.
This is "Reorder bytes + Delta" in
this blog post
.
What I see is that doing the delta on the full-integer sized units (F32 here) and then deinterleaving after is best.
("comp_size_dpcm_deinterleaved").
The fact that "best" is quite a bit better than "comp_size_dpcm_deinterleaved" tells us that there is no clear answer of what is
best for all files, it varies a lot with the data, and choosing per file could provide big wins.
Doing "fmap" to convert the sign flag to S32 correctly helps a bit more :

textest losslesscompress r:\aras\rrs -c8 -l5 -s0 -f

 uncompressed_size = 99,045,768
 comp_size_nofilter = 26,402,165 = 2.13 bpb
 comp_size_deinterleaved = 24,112,350 = 1.95 bpb
 comp_size_deinterleaved_bytedelta = 22,652,786 = 1.83 bpb
 comp_size_dpcm = 24,065,874 = 1.94 bpb
 comp_size_dpcm_deinterleaved = 21,657,552 = 1.75 bpb
 comp_size_best = 20,053,022 = 1.62 bpb
(for the record, "fmap" is lossy in that it does not preserve -0.f , but it does preserve nans)
(that's optional, you can easily preserve -0.f if you want to, but it helps compression not to)
For another reference point, let's do some images from OpenEXR :
m:\test_data\image\hdr\openexr-images-1.7.0\
   Blobbies.exr             6,109,568    CandleGlass.exr          2,629,900
   Desk.exr                 2,424,523    MtTamWest.exr            3,323,365
   PrismsLenses.exr         4,380,714    StillLife.exr            3,783,165
   Tree.exr                 3,716,423
  0 dirs - 7 files- 26,367,658 bytes occupied
(these are all F16 compressed with EXR Zip with unknown options, as found in the distro)
On "openexr-images-1.7.0" :

textest losslesscompress m:\test_data\image\hdr\openexr-images-1.7.0 -c8 -l5 -s0
Oodle Kraken level 5 (Optimal1) with no chunking :

 uncompressed_size = 43,484,672
 comp_size_nofilter = 26,317,526 = 4.84 bpb
 comp_size_deinterleaved = 22,153,449 = 4.08 bpb
 comp_size_deinterleaved_bytedelta = 22,050,228 = 4.06 bpb
 comp_size_dpcm = 24,090,408 = 4.43 bpb
 comp_size_dpcm_deinterleaved = 21,529,703 = 3.96 bpb
 comp_size_best = 21,243,281 = 3.91 bpb
On some float images from Epic (mix of F16 and F32) :
textest losslesscompress m:\test_data\image\epic\epic_dump_test_floats

default args = Kraken 3 (Fast) with 256 KB LZ chunking and no filter chunking :

 uncompressed_size = 134,217,728
 comp_size_nofilter = 30,956,125 = 1.85 bpb
 comp_size_deinterleaved = 32,075,290 = 1.91 bpb
 comp_size_deinterleaved_bytedelta = 32,688,663 = 1.95 bpb
 comp_size_dpcm = 32,830,366 = 1.96 bpb
 comp_size_dpcm_deinterleaved = 30,760,719 = 1.83 bpb
 comp_size_best = 25,008,275 = 1.49 bpb
"dpcm_deinterleaved" is the best single option (barely beating "nofilter") but note that "best" is quite a bit better, so any single choice is losing a lot.
Also note that "nofilter" is very good here and probably the best space-speed choice!
("best" is either "nofilter" (none) or "dpcm_deinterleaved", choosing between those two gets you a lot).
textest losslesscompress m:\test_data\image\epic\epic_dump_test_floats -c13 -l6 -s0 :

Leviathan Optimal2 no chunks :

 uncompressed_size = 134,217,728
 comp_size_nofilter = 21,429,732 = 1.28 bpb
 comp_size_deinterleaved = 25,431,382 = 1.52 bpb
 comp_size_deinterleaved_bytedelta = 27,091,215 = 1.61 bpb
 comp_size_dpcm = 26,063,778 = 1.55 bpb
 comp_size_dpcm_deinterleaved = 26,863,554 = 1.60 bpb
 comp_size_best = 18,628,509 = 1.11 bpb
Leviathan with no filters is now strongly the best option, deinterleaving hurts quite a bit (vs the same
filter non-deinterleaved),
but "best" is quite a bit lower still, so dpcm is still helping on some images.
TLDR:
The best way to compress numeric data that is larger than bytes (F32,F16,S32,S16) is usually to delta them in their original
size integer, then de-interleave after the delta.
Sometimes no filter or no deinterleave is best, particularly with stronger compressors, so being able to select filter on/off per-file
can give big wins.
Tangentially, we are badly in need of a simple interchange file format for images of bit depth over 8, something like :
SBM (simple bitmap) :
width,height,slices/zdepth (U64)
# channels per pixel, # bytes per channel (1,2,4), channel type (signed int,unsigned int,float)
links:
cbloom rants- 05-26-09 - Storing Floating Points
cbloom rants 02-24-11 - RRZ On 16 bit Images
cbloom rants 04-04-13 - Oodle Compression on BC1 and WAV
cbloom rants- 03-14-14 - Fold Up Negatives
Float Compression 3- Filters · Aras' website
GitHub - aras-p-float_compr_tester- Testing various libraries-approaches for compressing floating point data
Lossless Compression of Predicted Floating-Point Values
