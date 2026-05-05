---
title: "Requantization to different UNORM bit depths"
url: "http://cbloomrants.blogspot.com/2021/04/requantization-to-different-unorm-bit.html"
fetched_at: 2026-05-05T07:01:48.013479+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Requantization to different UNORM bit depths

Source: http://cbloomrants.blogspot.com/2021/04/requantization-to-different-unorm-bit.html

I wrote before in
Topics in Quantization for Games
some general basics on quantization.  We're going to continue from there, but focus just on the specific case : GPU convention quantization of
n-bit unsigned values (UNORM).
As noted before, there are two viable conventions for uniform linear quantizers; either "floor" quantization (with bias on reconstruct)
or "round" quantization (bias on quantizer) with direct reconstruction (end points restored directly).  The latter is what GPUs use, therefore
games should always use this convention for all quantizers to avoid mistakes.
(for example
RGBE quantization in the HDR
file format
uses the opposite convention; floor quantize and bias on dequantize; make sure to use the right convention to match the
file format)
The case we will talk about here is :
n-bit value
N = 2^n
quantized values in [0, N-1]
source values in [0.0, 1.0] (inclusive)

quantize(f) = (int)( f * (N-1) + 0.5f )

dequantize(i) = (float) i / (N-1);

quantized 0 -> 0.0
dequantized N-1 -> 1.0
Now we want to talk about "requantization".  Requantization is when you have some n-bit value and need to change the representation into an
m-bit value; we will assume always that both values are in UNORM GPU convention (bias on quantize).
A correct requantizer is one that corresponds to dequantization and quantization to the new bit depth :
x is quantized in n bits

dequantize :

f = (float) x / (N-1);

quantize to m bits :

y = (int)( f * (M-1) + 0.5f);

y = (int)( x * (float)(M-1)/(N-1) + 0.5f);

y is the requantization of x from n bits to m bits
(N = 2^n , M = 2^m)
Okay so back in
Topics in Quantization for Games
we showed that "bit replication" is the correct requantizer for changing n to 2n.
In requantization what we focus on is the denominator of the quantizer, so changing n bits to m bits is changing denominator from (N-1) to (M-1).
The denominator is
also the quantized representation of "One" (1.0 in dequantized range), and we need that to be preserved.  The fact that bit replication is
the correct requantizer is because bit replication is (N+1) (because N+1 = (1<<n) + 1) and (N+1)*(N-1) (that's (N+1)*One) = (N^2 - 1) which
is the new One.
To continue that, we can show that you can repeat bit replication to double bits again :
Start at n bits

Bit replicate once : *= (N+1)

now at 2n bits
2n bits range is N^2

Bit replicate again : *= (N^2+1)

What happens to One in n bits (N-1) :

(N-1)*(N+1)*(N^2+1)
(N^2-1)*(N^2+1)
(N^4-1)

becomes One in 4n bits

Alternatively just write out the requantizer :

y = (int)( (x/(N-1)) * (N^4-1) + 0.5f );

then using the factorization above this is just :

y = (int)( ((x/(N-1)) *  (N^2-1) * (N^2+1) + 0.5f );
y = (int)( (x * (N+1) * (N^2+1) + 0.5f );

y = x * (N+1) * (N^2+1);

exact in ints , which is bit replicate twice
So for example to go from 4 to 16 bits, you bit-replicate 0xA to 0xAAAA
Note that while bit doubling is the correct requantizer for bit doubling you can *not* just truncate bits to bit half.
eg. to requantize from 16 bits to 8 bits, you can not just grab the top 8 bits.  While grabbing the top 8 bits would be
a round-trip from 8 bit values that had been bit-doubled, it would not put the bucket boundaries in the right place
for values that are in between.  eg. 16-bit values in [129,255] should requantize to "1" in 8-bit, not just the 0 you
would get if you truncated to the top 8 bits.
Okay, so let's get into some requantizers.  I want to note that just doing the simple form :
y = (int)( x * (float)(M-1)/(N-1) + 0.5f);
is totally fine and you can just do that and not worry about this.  But that said, our goal here is to work out requantizers
that are exactly equal to that result, but that stay in integer.
There are a couple general techniques that help with this, so I'll do examples of both.
1. Taylor series in the denominator method.
For example, let's find the requantizer from 16 bit to 8 bit.  The simple form is :
y = (int)( x * 255/65535.f + 0.5f);
To find the int form, we can try changing 65535 to 65536.  One way to do that is approximate :
1/65535 = 1/(65536-1) = 1/65536 * 1/(1 - 1/65536)

We can use the Taylor expansion of 1/(1 - x) for x small :

1/(1 - x) = 1 + x + O(x^2)

using x = 1/65536 , it's reasonable to drop terms in x^2

So :

1/65535 ~= 1/65536 * ( 1 + 1/65536 )

y = (int)( x * 255/65535.f + 0.5f);
y = (int)( (x * 255 + 32767.5.f)/65535.f );
y = (int)( (x * 255 + 32767.5.f) * (1/65536) * ( 1 + 1/65536 ) );

y = (int)( (x * 255 + 32767.5.f + x*255/65536 + 32767.5.f/65536) * (1/65536) );

65536/255 = 257.003922.. ; try 257
32767.5.f + 32767.5.f/65536 = 32768 - 0.5f/65536 ; try 32768

y ~= (int)( (x * 255 + (x/257.f) + 32768) * (1/65536) );
y ~= (int)( (x * 255 + (x/257.f) + 32768) ) >> 16;

y = (x * 255 + (x/257) + 32768) >> 16;
and in fact that is the correct 16 to 8 requantizer in integers (in the sense that it matches the simple float
formula exactly).
There is however an even simpler 16 to 8 requantizer which also matches :
int requantize_16_to_8( int x )
{
    ASSERT( x >= 0 && x <= 65535 );

    return ( x * 255 + 32768 + 127 )>>16;
}
which can be made by replacing the (x/257) term with its average.
2. Bit replicating up to make an infinite repeating fraction
Another technique that sometimes works is based on a different conceptual picture.
We have (for example) an 8 bit value; 0x00 is "zero" , and 0xFF is "one" (that's what they dequantize to).
To get 0xFF to mean "one" we think of it as a fixed point fraction, and bit replicate so for 0xFF think :
0xFF = 0. FF FF FF ... forever

then there is no number between that and 1.0 , therefore it is equal to 1.0
so to find requantizers or interpolators, we can bit replicate several times and approximate the infinite
repetition with a finite number , but then we'll be a little bit too low so we'll have to bias up a bit.
To be clear, this repeated fraction is not just hand having and not just right at the end points; if you
could repeat forever it would be exact.  We can see it by using our Taylor expansion again and doing all
the terms :
1/(1-x) = 1 + x + x^2 + x^3 + x^4 + ...

using x = 1/256 , this is :

256/255 = 1 + 2^-8 + 2^-16 + 2^-24 + 2^-32 + ...

or

1/255 = shift down 8 + shift down 16 + shift down 24 + ...

or

0x34/255 = 0 . 34 34 34 34 ...
Any denominator that's a power of two minus one is a repeated binary fraction.
We want to see if we can use just a few repeats and then bias up and get correct requantizer results.
As an example, let's work out the requantizer from 10 bits to 8 bits.  As usual the simple way is :
f = x/1023.f
y = (int)( f * 255.f + 0.5f );
but we'll try to find an exact match to that formula that stays in int.  We guess that we want to start by
making a repeated fraction :
thinking of f as a fraction with decimal 20 places to the left

f = (x << 10) | x;

y = (int)( f * 255.f + 0.5f );

y = ( ((x << 10) | x) * 255 + (1<<19) + bias )>>20;

where we guess we need "bias" because of the fact that we are using a truncated 20 place fraction rather than forever
that is, we need to push up 0.FFFFF slightly to get to 1.0

It turns out it works with bias = (1<<9) (among others)

y = ( x * 1025 * 255 + (1<<19) + (1<<9) )>>20;

( using ( (x << 10) | x ) = x * 1025 )

This is in fact a correct requantizer from 10 to 8 bits :

int requantize_10_to_8( int x )
{
    ASSERT( x >= 0 && x <= 1023 );

    return ( x * 0x03FCFF + 0x080200 )>>20;
}
Okay, so we can see it's frequently possible to use an approximation of the infinite repeated fraction to find correct
requantizers.
(you could also get this from our one term Taylor expansion as well; essentially we just did 1/1023 ~= 1025/(1024^2) )
This requantize_10_to_8 requires 28-bit intermediates, so it fits in 32-bit registers.  For scalar that's fine, but for
SIMD we'd like to be able to do these requantizers in as few intermediate bits as possible (ideally in 16 to get wider SIMD).
If we go back to the verbose form we can see how to get these in fewer bits :
y = ( ((x << 10) | x) * 255 + (1<<19) + (1<<9) )>>20;

y = ( ((x*255) << 10) + ( x * 255 ) + (1<<19) + (1<<9) )>>20;

t = (x*255) + (1<<9)

y = ( (t<<10) + t )>>20;

y = ( t + (t>>10) )>>10;

int requantize_10_to_8_alt( int x )
{
    ASSERT( x >= 0 && x <= 1023 );

    int t = (x*255) + (1<<9);

    return ( t + (t>>10) )>>10;
}
This gives the same result again; it now uses only 18 bit intermediates.
This form is familiar from the classic "mul8bit" from Jim Blinn's "Three Wrongs Make a Right" :
int mul8bit( int a, int b )
{
    int t = a*b + 128;
    return (t + (t>>8) )>>8;
}
mul8bit takes a [0,255] value and makes it act as an interpolator from 0% to 100% , eg. for alpha blending.
It is equivalent to :
(int)( ((a / 255.f) * b) + 0.5f );
which is dequantizing a to UNORM, using it to scale b, then requantizing.
We can now see that the "mul8bit" interpolator is a relative of our requantizers, and we can derive mul8bit by
using the repeated fraction or Taylor series.
The end!
ADDENDUM :
This "Blinnish" requantizer is always correct (for to_bits <= fm_bits) :
int requantize_blinnish( int x , int fm_bits, int to_bits )
{
    int fm_N = (1<
<
fm_bits) - 1;
    int to_N = (1<
<
to_bits) - 1;

    ASSERT( x >= 0 && x <= fm_N );

    int t = (x*to_N) + (1<<(fm_bits-1));

    return ( t + (t>>fm_bits) )>>fm_bits;
}
often you can find simpler requantizers that are correct, but this provides a simple baseline/reference.
