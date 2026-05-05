---
title: "Rate allocation in Oodle Texture"
url: "http://cbloomrants.blogspot.com/2021/02/rate-allocation-in-oodle-texture.html"
fetched_at: 2026-05-05T07:01:47.998352+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Rate allocation in Oodle Texture

Source: http://cbloomrants.blogspot.com/2021/02/rate-allocation-in-oodle-texture.html

Oodle Texture
does rate-distortion optimization (RDO) BCN encoding, optimizing the BCN encoding for an
R-D two axis score such that the size of the BCN texture after a following lossless compression is
reduced while the distortion (difference from original) is not increased too much.
One way to think about RDO conceptually is as rate
allocation
.
Rate allocation is when an encoder intentionally puts more or fewer bits in parts of the data to control what
the decoder will receive, so that it can use more bits where it helps more, and the result is a better
quality for a given output size.
I want to talk a bit about that viewpoint and how it works in Oodle Texture.
Traditional lossy encoders like JPEG didn't have active rate allocation; they used a fixed scheme (DCT and
quantize) that did a fixed rate allocation (give more bits to the lower frequencies) and didn't try to
optimize that based on image contents.  Modern codecs like H264 use rate allocating encoders and furthermore
have explicit tools in the format to make rate allocation more flexible, such as variable quantizers.
Formats without explicit rate allocation controls can still be rate adjusted, which is what we do in Oodle
Texture, but it's not as easy to dial.
In that context, we think of a traditional non-RDO BCN encoder as allocating rate evenly to all blocks; it
doesn't care where the rate goes and just tries to minimize distortion.  The BCN encoder itself produces
fixed size blocks (8 bytes per block for BC1 or 16 bytes per block for BC7), but the "rate" we care about is
the size of the block after subsequent LZ compression (eg. with Kraken or Zip/deflate).
In Oodle Texture, we use the Lagrange parameter method for RDO.  Specifically we construct a
Lagrange cost :
J = D + lambda * R
and then we can just minimize a single number, J, rather than a two-axis score of {R,D}.
Obviously when lambda=0 this reduces to J=D , minimize D, which is a non-RDO encoding that only cares
about quality and not rate.  As lambda increases your score is more and more a balance of minimizing both
distortion and rate.
We sometimes think of D(R) , distortion just being a function of R, but that's not how it works in an
implementation, you don't actually know the functions for how R and D relate.
In practice there is some encoding, which I will index by "i" , and you have two separate functions :
R(i) and D(i)
That is, you just choose various encodings that look promising, and measure R and D of each.  This will
give you a scattering of points on an R-D plot.  Some points are off the Pareto Frontier - strictly worse in terms of R & D
and we just reject those points.  
See
Fabian's blog on RDO
for some pictures of this.
Henceforth I will assume that points off the Pareto Frontier have been rejected and we now only are looking
at encodings on the Pareto R-D curve.  Also I will sort the index of encodings "i" by rate.
The R(i) and D(i) curves both tend to be hyperbolic-shaped, with minima at opposite ends of the "i" spectrum.
If you minimized either one on their own, they don't have any local minima so you would just go to the edge
of what the encoding format is capable of doing.  By adding them together with lambda, it makes a trough
somewhere in the middle :
High D, low R on the left (very lossy), low D high R (non-RDO) on the right.
At low lambda, the minimum of J is in the high-R, low-D domain.
As lambda increases it shifts the minimum of J to lower R.
In the example chart, the red low-lambda curve has minimum at i=14, the teal medium-lambda curve
has minimum at i=12, the gold high-lambda curve has minimum at i=10.
In this way, lambda can be used to dial rate, but indirectly.
Concretely, if we reparameterize to imagine we have a function D(R) (Distortion as a function of R; there
is only one encoding for each R because we discard non-Pareto encodings), we have :
J(R) = D(R) + lambda * R

minimum is at d/dR J = 0

d/dR J = 0 = d D /dR + lambda

lambda = - dD / dR
lambda is the slope on the D(R) curve.
Because the D(R) curve is hyperbolic-shaped, the slope acts like a parameter of D itself.  That is,
where D is higher, the curve is also steeper, so by dialing the slope we have control over the principle
value D as well.
Aside for experts : we are assuming that D(R) is continuous and monotonic AND dD/dR is continuous and
monotonic; that is, the slope steadily increases from low to high.  The whole idea of lambda
as a slope of D(R) only really works if these curves are smooth and hyperbolic shaped as expected.
We also need J to only have one local minimum.  If these assumptions fail (which in practice they do!)
you can wind up at a minimum that's not where you want, and the lambda-dials-D relationship can break down.
There are some tricks to avoid these pitfalls.  Try to avoid large steps of R/D in your encoding choices;
provide the encoder with a fine grained series of steps; don't use the true R which can have strange
non-monotonic wiggles, instead use an approximation of R which tends to smooth things out; you generally
want to pre-classify the encodings that you think are low R vs high R and force them to be monotonic rather
than measuring true R.
Now, "lambda is the slope on the D(R) curve" sounds a bit unintuitive and abstract, but in fact it is
a concrete simple thing.
Lambda is a price.  It is the gain in D that you must get for a gain in R to be worth it.
By using lambda as your control parameter instead of D, you are dialing quality via the *cost* of quality
in terms of rate.  You are saying "this much gain in quality is worth this much rate to me".  We typically
measure R in bits, so let's say lambda is quality per bit.  In order to make a file bigger by 1 bit, it
must provide at least "lambda" quality gain.  Smaller quality gain, it's not worth it, don't do it.
Having our control paramter be price instead of directly controlling R or D turns out to be very beneficial,
both for us internally and for you externally.
First why it's right externally : lambda control (slope control)
lets you set a single parameter that works for all kinds of data or images.  It automatically gives more rate
to images that are harder to compress ("harder" here very concretely means a steeper slope - they give up more
distortion than average for each step or rate).  So you can have a mix of very vastly different data, lightmaps
and normal maps and cartoon drawings, and they automatically rate adjust to send bits where they help the most.
Many novices prefer to think of "rate reduction" or a "constant quality" kind of setting, like "I want to RDO
all my images to 30% rate reduction", but that's really wrong.  On some images, getting to 30% rate reduction
would do lots of quality damage, while on others you could easily get more rate reduction (say 50%) without
much quality loss at all.  Lambda does that for you automatically.
Internally it's important because it lets us make each coding decision in isolation, just by looking at the J
cost of that one decision in isolation.  It makes the problem separable (which is also great for parallelism),
but still achieve a global minimum.  Lagrange optimization automatically does rate allocation within the image
to different blocks and decisions.
I think it helps to compare to an alternative manual rate allocation method to see how advantageous it is :
Algorithm Manual Rate Allocation :

you have an image of N BCN 4x4 blocks
for each block, find the lowest D (non-RDO) encoding
measure R of that encoding - this is the max rate for each block

now incrementally reduce total rate
you want to take rate from the best block to take rate from of the N

for all N blocks
find the next smaller encoding 
measure the D increase for that step down of R
slope(n) = delta(D) / delta(R)

take the one block change n with the lowest slope(n)

repeat until all slopes(n) are > max_desired_slope

vs.

Algorithm Lagrange Rate Allocation :

for all N blocks in parallel :

try various encodings of the block
compute J = D + lambda * R for each encoding
take the encoding on that block with the best J
In "Manual Rate Allocation" we have this palette of various bins (the blocks) to choose to take rate from, and you take it from the
one that does the least damage to D, if you keep repeating that the slopes will converge until they are all roughly equal.
The powerful thing is that these two algorithms converge to exactly the same solution (caveat: assuming monotonic and smooth R/D curves, which
in fact they are not).  The Lagrange method is actually doing rate allocation between the blocks, even though it's not explicit,
and each block can be considered in isolation.  In an RDO encoder, rate is like water, it flows away from high ground (dD/dR is high)
to low ground, until level is reached.  The Lagrange method is able to do this separably because the total amount of
water (rate) is not conserved.
We can control exactly what the rate allocation does through the choice of the D function.  The R function for rate is relatively
inflexible - we're counting bits of output size (though in practice we may want to use a smoothed rate rather than true rate),
we don't have much choice in R - in contrast, the D function is not absolutely specified and there are lots of options there.
The choice of D changes where rate flows.
For example consider the common choices of D = L1 norm (SAD) vs L2 norm (SSD).  These metric score different errors differently, which
causes rate to flow.  In particular L2 (squaring) puts a very big weight on single large errors vs. smaller multiple errors.
Source data   = { 10, 10 }
Approximation = {  8, 12 }

SAD error = 2 + 2 = 4
SSD error = 2^2 + 2^2 = 8

Source data   = { 10, 10 }
Approximation = { 10, 14 }

SAD error = 0 + 4 = 4
SSD error = 0^2 + 4^2 = 16
Choosing D = SSD would cause rate to flow from the {8,12} approximation to the {10,14} approximation because the error is much
bigger there (relative to where it is with SAD).  All reasonable D functions will be zero for an exact match, and increase as
the approximation gets further from the source data, but they can increase at different rates for different types of distortions.
In a non-RDO encoding, these different D functions might find very similar encodings, but with RDO
by choosing different D you get rate to flow between blocks to different characters of error.
With no further ado, we can get to the fun part : pictures of how rate allocation plays out in practice in Oodle Texture.
These images show the original image, followed by gray scale images of the rate allocation.
These are for BC7 encodings with Oodle Texture.  The non-RDO encoding is Oodle Texture at lambda=0 ;
the RDO encodings are at lambda=40 (typical medium quality setting).
In the rate allocation images, each pixel represents one 4x4 block.  White is full rate (16 bytes per block)
and black is zero bits.  These encodings are not normalized to the same total rate (in particular the
non-RDO is of course much larger).  The images are gamma corrected so that linear light intensity corresponds
to bits per block.  The original images are halved in size for display here.  So for example "mysoup" was 1024x512,
the original shown here is 512x256, and rate map is one pixel per block, so 256x128.
The "rmse" and "perceptual" images use the exact same coding procedure at the same lambda, they differ only
in the D function used to measure distortion.  "rmse" tries to minimize simple L2 norm, while "perceptual"
has some estimation of visual quality (trying to avoid blocking artifacts, for example).
The R measured for these maps is the size of each block after subsequent compression by Oodle's LZA
compressor.
non-RDO
RDO rmse
RDO perceptual
The non-RDO "mysoup" has very high entropy, the BC7 blocks are nearly incompressible by the LZ
(7.759 bpb).  The RDO with D=rmse keeps very high bit rate in the blocks of the bowl rim, but
allocates lots of bits away from the smooth regions in the egg and pumpkin.  In the "perceptual"
allocation, the bits in the rim are reduced, allowing more error there, and the bit rate of the smooth
regions come up to avoid blocking artifacts.
non-RDO
RDO rmse
RDO perceptual
In the house image "test6" the bit rate of the "rmse" allocation goes nearly to zero in the smooth
dark areas of the beams under the eaves.  That's a mistake perceptually and causes bad blocking
artifacts, so the "perceptual" allocator shifts rate back to those blocks.
non-RDO
RDO rmse
RDO perceptual
We can see that Oodle Texture is changing near-even rate allocation to very variable rate per block.
Even though the BC7 blocks are always 16 bytes, we have made some more compressible than others,
shifting rate to where it is needed.  On many blocks, 16 bytes is just too much, that much rate is not
needed to get a good encoding, and the difference in D to a reduced-size encoding is small; these are
low slope blocks and will lose rate in RDO.  After rate allocation, the blocks all have the same dD/dR slope;
they reach an equilibrium where you can't take bits from one block and move it to another block and improve
total quality.
Something you may notice in all the rate allocation maps is there are horizontal lines of higher rate
going through the image.  This is where we slice the images into chunks for parallelism of some
operations that have to work per-chunk instead of per-block.  The stripes of higher rate show that we
could find some improvement there.
Links :
Oodle Texture at radgametools.com
Lagrange space-speed optimization - cbloom blog
Leviathan is a market trader - cbloom blog
Rate-Distortion Optimisation in Dirac
Rate-distortion optimization The ryg blog
