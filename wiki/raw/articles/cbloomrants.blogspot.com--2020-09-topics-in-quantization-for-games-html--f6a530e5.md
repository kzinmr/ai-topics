---
title: "Topics in Quantization for Games"
url: "http://cbloomrants.blogspot.com/2020/09/topics-in-quantization-for-games.html"
fetched_at: 2026-05-05T07:01:48.832108+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Topics in Quantization for Games

Source: http://cbloomrants.blogspot.com/2020/09/topics-in-quantization-for-games.html

I want to address some topics in quantization, with some specifics for games.
We do "quantization" any time we take a high precision value (a floating point, or higher-bit integer) and store it
in a smaller value.  The quantized value has less precision.  Dequantization takes you back to
the space of the input and should be done to minimize the desired error function.
I want to encourage you to think of quantization like this :
quantization takes some interval or "bucket" and assigns it to a label

dequantization restores a given label to a certain restoration point

"quantization" does not necessarily take you to a linear numeric space with fewer bits

The total expected error might be what we want to minimize :

Total_Error = Sum_x P(x) * Error( x,  dequantization( quantization(x) ) )
Note that in general the input values x do not have uniform probability, and the Error is not just linear L1 or L2
error, you might care about some other type of error.  (you might also care more about minimizing the maximum rather
than the average error).
I like to think of the quantized space as "labels" because it may not be just a linear numerical space where you can
do distance metrics - you always dequantize back to your original value space before you do math on the quantization labels.
I started thinking about this because of my recent posts on
Widespread error in RGBE
and
Alternative quantizers for RGBE
,
and I've been looking in various game-related code bases and found lots of mistakes in quantization code.  These are really
quite big errors compared to what we work very hard to reduce.  I've found this kind of thing before outside of games too.
For example it's very common for the
YUV conversions in
video and image codecs
to be quite crap, giving up lots of error for no good reason.  Common errors I have seem in the
YUV conversions are : using the terribad 16-235 range, using the rec601/bt709 matrix so that you encode with one and decode
with the other, using terribad down and/or up filters for the chroma downsample).  It's frustrating when the actual H264 layer
works very hard to minimize error, but then the YUV-RGB layer outside it adds some that could be easily avoided.
We do quantization all the time.  A common case is for 8-bit RGB colors to float colors, and vice versa.  We do it over and
over when we do rendering passes; every time you write values out to a render target and read them back, you are quantizing
and dequantizing.  It is important to take care to make sure that those quantization errors are not magnified by later passes.
For example when writing something like normals or lighting information, a quantization error of 1/256 can become much larger
in the next stage of rendering.
(a common example of that is dot products or cosines; if you have two vectors and store something that acts like
a dot product between them (or a cosine of an angle), the quantization bucket around 1.0 for the two vectors being
parallel corresponds to a huge amount of angular variation, and this often right where you care most about having
good precision, it's much better to store something that's like the acos of the dot product)
If you aren't going to do the analysis about how quantization errors propagate through your pipeline, then the easiest thing
to do is to only quantize once, at the very end, and keep as much precision through the stages as possible.  If you do
something like a video codec, or an image processing pipeline, and try to work in limited precision (even 16 bit), it is important to
recognize that each stage is an implicit quantization and to look at how those errors propagate through the stages.
(aside: I will mention just briefly that we commonly talk about a "float" as being the "unquantized" result of
dequantization; of course that's not quite right.  A "float" is a quantized representation of a real number,
it just has variable size quantization bins, smaller bins for smaller numbers, but it's still quantized with steps
of 1 ulp (unit in last place).  More correctly, going to float is not dequantization, but rather requantization to
a higher precision quantizer.  The analysis of propagating through quantization error to work in 8 bits or whatever
is the same you should do for how float error propagates through a series of operations.  That said I will henceforth
be sloppy and mostly talk about floats as "dequantized" and assume that 1 ulp is much smaller than precision that we
care about.)
So lets go back and start at the beginning :
Linear uniform scalar quantization
If our input values x are all equally probable ( P(x) is a constant ), and the error metric we care about is linear L1 or L2
norm, then the optimal quantizer is just equal size buckets with restoration to center of bucket.
(for L1 norm the total error is actually the same for any restoration point in the bucket; for L2 norm total error is minimized
at center of bucket; for L1 norm the maximum error is minimized at center of bucket)
We'll now specifically look at the case of an input value in [0,1) and quantizing to N buckets.  The primary options are :
int quantize_floor( float x , int N )
{
    return (int)( x * N );
    // or floor( x * N );
    // output is in [0, N-1] , input x in [0,1) not including 1.0
}

float dequantize_floor( int q, int N )
{
    return (q + 0.5f ) * (1.f / N);
}

int quantize_centered( float x, int N )
{
    return (int)( x * (N-1) + 0.5f );
    // or round( x * (N-1) )
    // output is in [0, N-1] , input x in [0,1] , including 1.0 is okay
}

float dequantize_centered( int q, int N )
{
    return q * (1.f / (N-1));
}
The rule of thumb for these quantizers is you either bias by 0.5 in the quantizer, or in the dequantizer.  You must bias on
one side or the other, not both and not neither!  The "floor" quantizer is "bias on dequant", while the "centered" quantizer
is "bias on quant".
Visually they look like this, for the case of N = 4 :
(the top is "floor" quantization, the bottom is "centered")
(the top is "floor" quantization, the bottom is "centered")
In both cases we have 4 buckets and 4 restoration points.  In the "floor" case the terminal bucket boundaries correspond to the
boundaries of the [0,1) input interval.  In the "centered" case, the terminal buckets are centered on the [0,1) endpoint, which means
the bucket boundaries actually go past the end, but they restore exactly to the endpoints.
If your input values are actually all equally likely and the error metric that you care about is just L2 norm, then "floor"
quantization is strictly better.  You can see that the bucket size for "floor" quantization is 1/4 vs. 1/3 for "centered",
which means the maximum error after dequantization is 1/8 vs. 1/6.
In practice we often care more about the endpoints or the integers, not just average or maximum error; we suspect the
probability P(x) for x = 0 and 1 is higher, and the error metric Error( dequantization( quantization(x) ) - x ) may also be
non-linear, giving higher weight to the error when x = 0 and 1.
"centered" quantization also has the property of preserving integers.  For example say your input range was [0,255) in floats.
If you quantize to N=256 buckets with "centered" quantization, it will restore exactly to the integers.
Games should only be using centered quantization!
While in theory there are cases where you might want to use either type of quantization, if you are in games don't do that!
The reason is that the GPU standard for UNORM colors has chosen "centered" quantization, so you should do that too.
Certainly you need to do that for anything that interacts with the GPU and textures, but I encourage you to just do it
for all your quantization, because it leads to confusion and bugs if you have multiple different conventions of quantizer
in your code base.
The GPU UNORM convention is :
float dequantize_U8_UNORM( unsigned char u8 )
{
  return u8 * (1.f/255);
}
which implies centered quantization, so please use centered quantization everywhere in games.  That means : bias 0.5 on quantize,
no bias on dequantize.
While on the topic of UNORM, let's look at conversion between quantized spaces with different precision.  Let's do U8 UNORM to U16 UNORM
for example.
The way to get that right is to think about it as dequantization followed by quantization.  We dequantize the U8 UNORM back to
real numbers, then quantize real numbers back to U16 :
dequant = u8 * (1.f/255);

u16 = round( dequant * 65535 );

u16 = round( u8 * (1.f/255) * 65535 );

u16 = round( u8 * 257 );

u16 = u8 * 257;

u16 = u8 * (256 + 1);

u16 = (u8<<8) + u8;
So U8 to U16 re-quantization for UNORM is : take the U8 value, and replicate it shifted up by 8.
requantize U8 UNORM to U16 UNORM :

0xAB -> 0xABAB
This obviously has the necessary property that 00 stays zero, and 0xFF becomes 0xFFFF, so 1.0 is preserved.
This is something we call "bit replication".  Let's take a moment to see why it works exactly in some cases and only
approximately in others.
Bit Replication for re-quantization to higher bit counts
Bit replication is often used in games to change the bit count of a quantized value (to "requantize" it).
For example it's used to take 5-bit colors in BC1 to 8-bit :
The top 3 bits of the 5-bit value are replicated to the bottom :

abcde -> abcde|abc

giving an 8 bit value
Bit replication clearly gets the boundary cases right : all 0 bits to all 0's (dequantizes to 0.0), and all 1 bits
to all 1 bits (dequantizes to 1.0); in between bit replication linearly increases the low bits between those
endpoints, so it's obviously sort of what you want.  In some cases bit replication corresponds exactly to requantization,
but not in others.
With a B-bit UNORM value, it has N = 2^B values.  The important thing for quantization is the denominator (N-1).
For example with a 5-bit value, (N-1) = 31 is the denominator.  It becomes clear if we think about requantization as
changing the *denominator* of a fraction.
Requantization from 5 bits to 10 bits is changing the denominator from 31 to 1023 :

dequant( 5b ) = 5b / 31.0;
requant_10( x ) = round( x * 1023.0 );

requant_5_to_10 = round( x * 1023 / 31 );

1023/31 = 33 exactly, so :

requant_5_to_10 = x * 33

in integers.  And 33 = (32 + 1) = shift up 5 and replicate

requantization from 5 to 10 bits is just duplicating the bits shifted up
abcde -> abcde|abcde
What that means is bit replication from B to 2B is exactly equal to what you would get if you dequantized that number to
UNORM and requantized it again.
This is of course general for any B :
denominator for B is (N-1)
denominator for 2B is (N^2 - 1)

requantiztion is *= (N^2 - 1) / (N-1)

(N^2 - 1) = (N-1) * (N+1)

so 

requantization is *= (N+1)

which is bit replication
Now more generally for bit replication to some number of bits that's not just double (but <= double, eg. between
B and 2B) :
b between B and 2B
n = 2^b

requant_B_to_b(x) = round( x * (n-1) / (N-1) )

requant_B_to_b(x) = round( x * (N+1) * (n-1) / (N^2-1) )

requant_B_to_b(x) = round( (x bit replicated to 2B) * ( scale down ) )

bit replication from B to b is :

bitrep(x) = (x bit replicated to 2B) >> (2B - b)

that is, just replicate to 2B and then truncate low bits to get to b

when b = 2B , these are exactly equal as we showed above

obviously also at b = B (NOP)
and also at b = B+1 (adding one bit)

in the range b = [B+2, 2B-1] they are not quite exactly equal, but close

Let's look at an example, 5 bits -> 8 bits :

bitdouble( 5b ) = (5b * 33)

requant_5_to_8(5b) = round( (5b * 33) * ( 255.0 / 1023.0 ) )

bitrep_5_to_8(5b) = (5b * 33) >> 2

we can see where the small difference comes from :

bit replication just truncates off the 2 bottom bits

requantization does * (255/1023) , which is almost a /4 (like >>2) but not quite
and the requantization also rounds instead of truncating
so we should see how bit replication is similar to centered UNORM requantization, but not quite the same.
Now, bit replication is used in BC7, ASTC, etc.  Is it a source of error?  No, not if you do your encoder right.  What it
does mean is that you can't just find the 5-bit color value by doing a centered quantizer to 5 bits.  Instead you
have to ask what does the 5-bit value bit-replicate to, and find the closest value to your input.
Quantizing infinite signed values and the deadzone quantizer
So far we've talked about quantizing finite ranges, specifically [0,1) but you can map any other finite range to that
interval.  Let's have a brief look at quantizing infinite ranges.
If you just quantize a signed number to a signed quantized number, then you can use the above _floor or _centered quantizers
without thinking any more about it.  You will have uniform buckets across the whole number line.  But what we often want
to do is take a signed input number and quantize it to *unsigned* and separate out the sign bit, to create a sign+magnitude
representation.  (this makes the most sense with values whose probability P(x) is symmetric about zero and whose mean is
at zero; eg. after a transform that subtracts off the mean)
One reason we might want to do that is because most of our schemes for sending unbounded (variable length) numbers work
on unsigned numbers.  For example :
Encode Mod
and
Exp Golomb
.
Now one option would be to quantize to signed ints and then
Fold up Negatives
to make an unsigned number to feed to your variable length scheme.
There are reasons we don't like that in data compression.  Folded up negatives have a number line like :
{0, -1, 1, -2, 2, -3 ... }
The annoying thing about that for data compression is that if you have a probability model like a Laplacian that
decreases with absolutely value of x, the probabilities have these steps where values are repeated :
{ P(0), P(1), P(1), P(2), P(2), ... }

and coding them with something like exp-golomb is no longer quite correct as they don't progressively fall off.
Some codecs in the past have used tricks to reduce this (eg. JPEG-LS and CALIC) by doing things like being able to
flip the sign so that you get either {0, -1, 1, -2, ... } or {0, 1, -1, 2, ... } depending on whether positive or
negative is more probable.
Rather than do all that, let's assume you want to extract the sign bit and send it separately.  So you are sending
only the magnitude.
So we have taken the sign out and now only have a one sided interval [0, inf) to quantize.
You can take that one-sided interval and just apply floor or centered quantization to it :
unsigned half_line_quantize( float x )
{
    ASSERT( x >= 0.f );
    //return floor( x ); // floor quantizer
    //return round( x ); // centered quantizer
    float bias = 0.f for floor and 0.5 for centered;
    return (unsigned) ( x + bias );
}
but something a bit funny has happened.
Floor and centered quantization now just act to shift where the boundary of the 0 bin is.  But the 0 bin now
occurs on both sides of the half interval, so to make the 0 bin the same size as the other bins, it should have
a boundary at 0.5 (half the size of the other bins on the half interval).  (I'm assuming here that your quantization bucket size is 1.0 ;
for general sized quantization buckets just scale x before it gets here).
It's clear that the zero bin is a bit special, so we usually just go ahead and special case it :
pseduocode signed_line_quantizer( float x )
{
    // x signed

    float ax = fabsf(x);

    if ( ax < deadzone )
    {
        // special bucket for zero :
        // don't send sign bit
        return 0;
    }
    else
    {
        // do send sign bit of x
        // do floor quantizer above the zero bucket :
        return floor(ax - deadzone);
    }
}
Now if you want the zero bucket to have the same size as all others, you would set deadzone = 0.5 (it's half the zero
bucket size on the full line).  If you want to use a uniform floor quantizer on the half line, that would correspond to
deadzone = 1.0 (making the zero bucket actually twice the size of others after mirroring to the negative half of
the line).
What's been found in data compression is that a "deadzone" larger than equal size buckets (larger than 0.5) is beneficial.
There are two primary reasons :
We use codecs where coding zeros is especially cheap, so sending more zeros is very desirable.  So larger deadzone in the
quantizer will give you more zeros, hence cheaper coding, and this is a greater benefit than the loss in quality.  This
is sort of a hacky way of doing some rate-distortion optimization, like trellis quantization but without any work.
The other reason is perceptual modeling; many human perception systems (eyes and ears) are less sensitive to the
initial onset of a signal than they are to variations once the signal is present.  Signals near zero are not detected by
humans at all until they reach some threshold, and then once they pass the threshold there's a finer discrimination of level.
For example the human ear might not detect a harmonic until it is 10 dB, but then distinguish volume levels at 1 dB changes
after that.
Essentially your quantizer has two parameters, the bucket size for zero, and then the bucket size for values above zero.
This is a very simple form of a more general variable quantizer.
In theory you would like to have variable size bins, such that each bin corresponds to an equal amount of perceptual
importance (eg. larger bins where the values are less important).  For the most part we now do that by applying a nonlinear
transformation to the value before it reaches the uniform quantizer, rather than trying to do variable size bins.
For example you might take log(x) before quantizing if you think precision of high values is less important.
Another common example is the "gamma corrected" color space (or sRGB) for images; that's a non-linear transform applied
to the signal (roughly pow 2.2) to map it to a space that's more perceptually uniform so that the quantization buckets give
more precision where it's needed.
Something to watch out for is that a lot of code uses a deadzone quantizer without being clear about it.
If you see something like :
!
int half_line_quantizer_thats_actually_a_deadzone( float x )
{
  ASSERT( x >= 0.f );
  return (int) x;
}
That's actually a deadzone quantizer with a 2x sized bin zero, if it's being used after sign removal.
In the olden days, variable-size quantization buckets were used as a kind of entropy coder.  They would have
smaller buckets in higher probability regions and larger buckets in lower probability regions, so that the
quantized output value had equal probability for all bins.  Then you could send the quantized value with no
entropy coding.  This is now almost never done, it's better to use quantization purely for error metric
optimization and use a separate entropy coder on the output.
Topics in dequantization
Just briefly some topics in dequantization.
For values that are all equally likely, under an L2 (SSD/RMSE) error norm, dequantization to the center of the bucket is
optimal.  More generally the restoration point for each bucket should minimize the error metric weighted by the probability
of that input value.
An easy case is with an L2 error metric but a non-uniform probability.  Then the error in a given bucket for a restoration point is :
L2 error of restoring to r in this bucket :

E = Sum_x P(x) * ( r - x )^2

( Sum_x for x's in this bucket )

find r that minimizes E by taking d/dr and setting to zero :

d/dr E = 0

d/dr E = Sum_x P(x) * ( r - x ) * 2

Sum_x P(x) * ( r - x ) = 0

Sum_x P(x) * r = Sum_x P(x) * x

r = ( Sum_x P(x) * x ) / ( Sum_x P(x) )

that's just the expectation value of x in the bucket
we should restore to the average expected 'x' value in the bucket.
A common case of that is for a skewed probability distribution - something like Laplacian or Poisson with a falloff of
probabilities away from the peak - we should restore each bucket to a value that's skewed slightly
towards the peak, rather than restoring the center.
Now if you have a mathematical model of P(x) then you could compute where these centers should be, and perhaps store
them in a table.
What's often better in practice is just to measure them experimentally.  Do trial runs and record all the values that
fall into each quantization bucket and take their mean - that's your restoration point.
Then you could store those measured restoration points in constants in your code, OR you could measure them and store
them per-data item.  (for example an image compressor could transmit them per image - maybe not all but a few of the
most important ones).
Another thing you can do in dequantization is to not always restore to the same point.  I noted briefly previously that
if what you care about is L1 norm, then any restoration point in the bucket has the same error.  Rather than just pick
one, you could restore to any random point in the bucket and that would give the same expected L1 norm.
L2 norm strongly prefers the mean (minimizing L2 is blurring or smoothing, while L1 allows lots of noise), but perceptually
it may be better to add some randomness.  You could restore to mean in the bucket plus a small amplitude of noise
around there.  Again this noise could be global constant, or could be sent per-image, or per-band; it could also be
predicted from local context so you could have more or less noisy areas.
Note that adding noise in dequantization is not the same as just adding noise arbitrarily after the fact.  The values
are still within the quantization bucket, so they could have been the true source values.  That is, we can reframe
dequantization as trying to guess the source given the quantized version :
Encoder had original image I

made Q = quant( I )

Q was transmitted

rather than just run I' = dequant( Q )

we instead pose it as :

we want to find I'
such that
Q = quant( I' )
and I' has the maximum probability of being the original I
or I' has the most perceptual similarity to our guess of I
The key thing here is that noise within the quantization bucket keeps the constraint Q = quant(I') satisfied.
As an example I'll mention something I've done in the past for wavelet bit-plane truncation.
Wavelet coding converts an image into activity residuals at various frequency subbands.  These are initially quantized
with a uniform+deadzone quantizer (if a floating point wavelet transform was used).  Then in many codecs they are sent progressively in bit planes, so the highest bits
are sent first, then lower bits, so that you get the most important bits first.  You can then truncate the stream, cutting
off transmission of lower bits in the higher subbands, effectively increasing the quantizer there.  This is done in
JPEG2000 with the EBCOT scheme for example.
So a given wavelet residual might be sent like :
value 45

= 101101

only top 2 bits sent :

10xxxx

the others are cut off.
In the decoder you know which bits you got and which are missing, which is equivalent to a larger quantization
bucket.
The classic option (eg. SPIHT) was just to fill the lost xx bits with zeros :

10xxxx -> 100000

This makes values that are too low and is generally very smoothing (high frequency detail just goes away)

You might think, it's a quantization bucket, we should restore to the middle, which is 0.5 which is the
next bit on :

10xxxx -> 101000 or 100111

That is much too high, it's larger than the expectation and actually looks like a sharpen filter.
The reason is that wavelet amplitudes have P(x) strongly skewed towards zero, so the mean value is
way below the middle of the bucket.

Restoring to 0.25 is a bit better :

10xxxx -> 100100

but even better is to just measure what is the mean in the image for each missing bit count; that
mean depends on how large our value was (the part that's not truncated).
Finally in addition to restoring the missing bits to mean, you could add randomness in the dequantization,
either within the quantization bucket (below the bottom bit), or in the low part of the missing bits
(eg. if 4 bits are missing the bottom 2 might get some randomness).  You can compute the amount of
randomness desired such that the decompressed image matches the high frequency energy of the original image.
And that's enough on quantization for now!
