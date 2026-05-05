---
title: "Float to int casts for data compression"
url: "http://cbloomrants.blogspot.com/2023/07/float-to-int-casts-for-data-compression.html"
fetched_at: 2026-05-05T07:01:48.081235+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Float to int casts for data compression

Source: http://cbloomrants.blogspot.com/2023/07/float-to-int-casts-for-data-compression.html

This is an attempt to survey possible reasonable options for float to int casts for data compression.
As mentioned in the previous post (
Notes on float and multi-byte delta compression
),
when we work with float data in compression, we usually need to reinterpret the bits to an integer so that we can do things like deltas in a
way that is either lossless, or with intentional loss in a quantization step.
If you have domain-specific knowledge of the floats, then you might do other things which are not in the scope of this post.  For example,
as Fabian mentions, if you have an F32 HDR image, you might just convert that to F16, as F16 is a pretty good lossy space for HDR images.
In other cases you might use a quantizer into a finite interval (see
Topics in Quantization for Games
).  For example if you have vertex coordinates in a mesh, you might send the bounding box and then
fixed point coordinates in the box.  For mapping and scientific work it may be best to use a fixed point encoding with definite units, such
as 1 integer step = 1 nanometer.
With that disclaimer out of the way, let's go through the possible mappings.
"just_cast" : just reinterpret the F32 to U32.
"lossless_fix_negatives" : change the F32 sign bit into two's complement.
uint32 forward(float f)
    {
        int32 ret = fbits_as_u32(f);

        int32 propagated_sign = ret>>31;

        ret ^= uint32(propagated_sign)>>1;  // not top bit
        return ret;
    }
This is totally lossless/reversible (obviously, because it's just xoring the same propagated bit, so it's
self-invertible).  This preserves -0.f ; it maps 0.f to int 0 and -0.f to int -1, so they are different but
adjacent.
"fix_negatives_lossyzeronan" : fix negatives, non-bit preserving (lossy), but it is lossless in the sense of
float compares.  That is, it preserves f==g when done on floats, but not if reinterpretted to uint32 bits.
uint32 forward(float f)
    {
        if ( f > 0.f )
        {
            return t_positives_mapper::forward(f);
        }
        else if ( f < 0.f )
        {
            return - (int32) t_positives_mapper::forward(-f);
        }
        else if ( f == 0.f )
        {
            return 0; // also -0.f
        }
        else
        {
            // nan fails all compares so goes here
            
            return 0x80000000U; // all nans changed to same value
        }
    }
Float 0.f and -0.f both map to 0, all nans map to 0x80000000U (there are almost 2^24 nan values but if you only care
about float equality, there's not reason to preserve those bits).
t_positives_mapper only sees floats > 0.f ; it can be just_cast for "fix_negatives_lossyzeronan" , but then
we'll also look at more lossy mappings there.
Those are the interesting lossless mappings (either lossless in full 32 bits, or in float equality, which is
weaker).  We can also look at lossy mappings.  For lossy mappings we are mainly interested in reducing the
bits of precision around 0.f.  Why?  In the integer mapping, the space between -1.f and +1.f is nearly 2^31 ;
it's half of the entire number space.  This is usually not where you want all your bits allocated, and hurts
compression when you have values near zero or crossing zero.
(note that in contrast, we don't really care too much about reducing the unused exponent space at the high end;
that may also be more than we need, but if it's not used then those values simply aren't encoded, and it doesn't
hurt compression much; the unused high exponents will just be entropy-coded out)
So, assuming you do know that you want to remove some precision at the low end (but for whatever reason you
don't want to use one of the more domain-aware mappings mentioned at the start), how?  We'll assume that you
are first using a mapping like "fix_negatives_lossyzeronan" , then further doing a lossy step for "t_positives_mapper".
I mentioned in the
last post
that one very simple lossy mapping is just to do float += 1.f  (or more generally float += C , where choice of C
controls where your precision cutoff is).
So one option is to do +1.f and then just cast.
Another option is to treat the space in [0.f,1.f] as denormal ; that is, forbid negative exponents and just make
that a linear range.
You can either do that explicitly :
"lossy_logint" :

    uint32 forward(float f)
    {
        ASSERT( f > 0.f );
        if ( f >= 1.f )
        {
            uint32 u = fbits_as_u32(f);
            return u - 0x3F000000U;
        }
        else
        {
            uint32 u = ftoi_round_banker( f * 0x1.p23f );
            return u;
        }
    }
or by multiplying by a tiny value to use the IEEE float denormal/subnormal from the CPU :
"lossy_denorm1" :

    static uint32 forward(float f)
    {
        ASSERT( f > 0.f );
        f *= 0x1.p-126f;
        uint32 u = fbits_as_u32(f);
        return u;
    }
these produce exactly the same mapping (except for "inf").  Caveat that using the IEEE denormal on the CPU like
this relies on fast hardware support which is not always present.  (I couldn't find a good table of where that is
okay or not, does that exist?)
The denorm/logint method is strictly better than the just adding a bias method, so it's hard to see why you would
use that, unless it fits into your optimization particularly well.  Choice of a mapping like this for compression
must be evaluated in a space-speed framework, which is outside of the scope of this post, I'm only trying to
enumerate the possible good options here.
Errors are :
!
just_cast                     : exact bits
lossless_fix_negatives        : exact bits
fix_negatives_lossyzeronan    : equal floats
lossy_logint                  : max error : 5.96046e-08 = +1.00000000000000000000000x2^-24
lossy_denorm1                 : max error : 5.96046e-08 = +1.00000000000000000000000x2^-24
lossy_add1                    : max error : 1.19209e-07 = +1.11111111111111111111110x2^-24
("max error" is absolute for values <= 1.f and relative for values >= 1.f)
downloadable code for reference :
main_float_conversions.cpp
cblib.zip
