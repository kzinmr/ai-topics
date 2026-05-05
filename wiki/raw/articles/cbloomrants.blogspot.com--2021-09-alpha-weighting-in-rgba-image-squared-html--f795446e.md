---
title: "Alpha Weighting in RGBA Image Squared Distortion Measure"
url: "http://cbloomrants.blogspot.com/2021/09/alpha-weighting-in-rgba-image-squared.html"
fetched_at: 2026-05-05T07:01:47.638895+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Alpha Weighting in RGBA Image Squared Distortion Measure

Source: http://cbloomrants.blogspot.com/2021/09/alpha-weighting-in-rgba-image-squared.html

I'm going to look at how the Alpha channel should be weighted vs the RGB components when measuring distortions in RGBA textures,
when that RGBA texture is used for alpha blending.
(aside: of course many RGBA 4-channel images are not actually using A for opacity in alpha blending and this discussion does not
apply to those; if your RGBA image is really 4 scalar channels of the same type of signal then the weight of each channel should be the same)
For concreteness, an RGBA image used for alpha blending means that we construct an output pixel like :
out = A * RGB + (1 - A) * background

RGBA in [0,1] scale here
and for most of this discussion I will assume that the distortion measure we are looking at is weighted squared difference (L2 norm) :
' = prime = indicates values in the modified texture

SD(RGB) = ( RGB' - RGB )^2 = (R' - R)^2 + (G' - G)^2 + (B' - B)^2

SD(RGBA) = SD(RGB) + (A' - A)^2

WSD(RGBA) = SD(RGB) + W(A) * (A' - A)^2

W(A) is the weight of the A term in the RGBA squared difference
In the end what we care about is what the user sees, which are the "out" pixel values after alpha blending.  So the correct error metric
(or weight for A) should be determined by minimizing the error in the output pixel.
(choosing a weight for A is equivalent to choosing a bit allocation ratio between RGB color channels and the A channel; in an RD encoder,
changing W(A) corresponds to transferring bits)
The output pixel is RGB only (no A), and we'll assume that we want to minimize the squared difference of the output pixel.  So the question is
how should that be expressed in an error metric on the RGBA texture.
There are three intuitive factors which should obviously affect this issue, and we will see them come out in the math.  They are :
1. When background RGB is nearly equal to the texture RGB, A doesn't matter at all.   If background == RGB , then any A value produces the
same output pixel.  The bigger difference there is between background and the current texture, the more important A is.
2. When A is smaller, the texture RGB is less important.  In the extreme case of A=0, the texture RGB doesn't matter at all, it isn't used
and is fully redundant.  This is a well known problem in texture compression and is why we prefer premultiplied alpha (see more later).
3. Ignoring those factors, A affects the output color in all 3 channels, so will be something like ~3 times more important than each RGB channel.
So, without further ado let's do the simple math :
E = (out' - out)^2

out = A * RGB + (1 - A) * background

let background = RGB + D

(background is an RGB vector; D is a scalar difference on each channel)

out = A * RGB + (1 - A) * (RGB + D) = RGB + (1 - A)*D

out(R) = R + (1-A)*D

out' = A' * RGB' + (1 - A') * (RGB + D)

(note the background RGB in out' is not RGB' ; the background color stays the same)

R' = R + dR
A' = A + dA

out'(R) = (A + dA) * (R + dR) + (1 - A-dA) * (R+D)

out'(R) = (A + dA) * dR + R + (1 - A-dA) * D

out'(R) = A * dR + R + (1 - A)*D -dA * D

(dropping terms squared in the delta d)

(out' - out)(R) = A * dR - dA * D

E = A^2 dRGB^2 + 3*D^2 dA^2 + linear terms

linear terms = - 2 * A * D * dA * dRGB

dropping the linear terms (see later on why) :

E = A^2 * dRGB^2 + 3*D^2 * dA^2
This is equivalent to a weight on alpha :
W(A) = 3 * D^2 / A^2

D = difference between texture and background (scalar)

note instead of 3*D^2 you could use the vector RGB difference to background :

W(A) = D_RGB^2 / A^2
This weight term encapsulates the three intuitive principles we saw at the beginning: when the foreground and background are the same RGB color,
then A doesn't matter, W(A) ~ D^2 goes to zero.  As A goes to zero, RGB doesn't matter; W(A) goes to infinity like 1/A^2  (if you prefer, the weight
of RGB goes to zero like W(RGB) ~ A^2).  Other than that, if A is ~ D, then W(A) is ~ 3X the RGB weight because it affects all three channels.
(revisiting the note on dropping the linear terms : several reasons why I think this is right.  First of all, because these are signed linear terms, they
will average out to zero when summing over pixels, assuming your distortions dRGB are random around the target value and not net biased to one side.
Second of all, because we don't really want to be measuring this effect.  What the linear term measures is ways that you can compensate for miss-blending
the background with a wrong A by using a wrong RGB to fix it.  Say you're blending white onto a black background and your A is too high, you can compensate
and lower E by making RGB lower to get the right output color.  When that does happen to work in our favor we just don't even want to know about that.
It also assumes exact knowledge of the background.)
Now we can't assume that we know the background.  We could look at the worst case, D = 1.0, blending black on white or vice versa.
That's when A matters the most, and W(A) = 3 / A^2  ; in that case :
maximal difference to background, D = 1.0

W(A = 1) = 3
W(A = 0.5) = 12
W(A = 0.25) = 48
Alpha should be weighted much higher than RGB.
(note that because of interpolation we probably don't want the weight of RGB to ever go completely to zero)
But D = 1 is rare in practice.  In fact in games we very often do alpha blending when D is closer to zero.  For example say you're doing some alpha blended
particle effects, often you blend many fire or smoke puffs on top of each other, so they are often blending onto other fire and smoke that is very similar.
On many games, the RGB palette is squarely in the gray/brown domain so we expect D to be much less than 1 most of the time.
If we assume that foreground and background are both random numbers on the unit interval [0,1] , then we would have :
D = < |x - y| >  (x and y uniform random on the unit interval)

(this is simple integral and fun exercise for the reader)

D = 1/3

W(A) = (1/3) / (A^2)

W(A = 0.5) = 4/3
Now, assuming the colors are random is also clearly wrong, don't take this as "the answer", it's just another data point, perhaps
more realistic than D=1, but still not using any assumption about texture and background often matching, which would make D even smaller
than 1/3.
If you assume the worst case (D=1) you are over-weighting A when it's not always necessary, but assuming D very small would make you
under-weight A when the background is in fact very different from the texture.
Let's set that aside and revisit something we mentioned early on : premultiplied alpha.
We like premultiplied alpha in texture compression because without it you are sending totally unnecessary bits in RGB values when A=0.
With some types of textures that are largely transparent this can be a huge amount of bits wasted.
(some texture codecs will not encode RGB when A=0 exactly, but premultiplied also correctly down-weights the importance of RGB when A is
finite but tiny; premultiplied also filters/interpolates better)
With premultiplied alpha the blending equation is :
out = RGB + (1 - A) * background

(no *A on the RGB from the texture, A is only used to multiply the background)
Let's compute what the squared difference weight W(A) should be for RGBA textures used in premultiplied alpha.  For laughs I'll do it a different way.
for small deltas :

out_R = R + (1 - A) * background_R

d(out_R)  = d/dR(out_R) * dR + d/dA(out_R) * dA

d/dR(out_R) = 1
d/dA(out_R) = - background_R

d(out_R) = (dR - background_R * dA)

E = d(out)^2 = d(out_R)^2 + d(out_G)^2 + d(out_B)^2

dropping linear terms (see arguments above)

E = dR^2 + dG^2 + dB^2 + (background_R^2 + background_G^2 + background_B^2) * dA^2

E = SD(RGB) + WPM(A) * dA^2

WPM(A) = background_R^2 + background_G^2 + background_B^2

WPM(A) = background_RGB^2

WPM(A) = 3 * background^2  (assuming the same scalar "background" value on all channels)
The weight for pre-multiplied alpha is similar to the non-PM case, but without the annoying 1/A^2 in the denominator, which is a big advantage.
Our weighting no longer depends on our A at all, which means the channels can be treated independently.  The A weight has been taken in the "premultipy" scaling of RGB.
This is just a way of saying that our intuition for premultiplied alpha was correct : using premultiplied alpha has correctly
scaled the RGB component for its importance with alpha, so that you can use the L2 norm on the RGBA channels without any inter-channel
correction factor.
Rather than a scaling by D (difference of texture and background), we now have a scaling with just "background".  It's obvious
from the premultiplied blending equation that if background == 0, then A has no affect on the output color.
Obviously when encoding a texture we don't know the value of the background.  Looking at a few values :
WPM(A) , background=0   : = 0
WPM(A) , background=1/2 : = 3/4
WPM(A) , background=2/3 : = 4/3
WPM(A) , background=1 :   = 3
it's probably okay to just use WPM(A) = 1, that is just weight all channels the same, use RGBA squared difference.
This a compromise given the unknown background; it's convenient that equal weight is not too bad for pre-multiplied alpha.
If you have domain-specific knowledge you could use something different.  For example on the web or word-processing where you are
mostly blending onto white backgrounds, alpha weight closer to 3 would be better.
Conclusion :
When measuring distortion on RGBA textures that you know will be used for alpha-blending, we can find a squared-difference in texture-space
that approximates the error in the visible output pixel.
This can be expressed as a weight on the alpha component of the squared difference :
SD(RGBA) = SD(RGB) + W(A) * dA^2


for standard alpha blending :

W(A) = 3 * D^2 / A^2

D = difference between texture and background (scalar)

or W(A) = D_RGB^2 / A^2


for pre-multiplied alpha :

WPM(A) = background_RGB^2

WPM(A) = 3 * background^2
For pre-multiplied alpha, using WPM(A)=1 is reasonable, and just using 4-channel uniform RGBA squared difference is probably fine.
This is just another great reason to prefer pre-multiplied alpha.
For non-pre-multiplied alpha, it's hard to escape the need to scale RGB by A for purposes of the error metric.
( W(A) ~ 1/A^2 is equivalent to W(RGB) ~ A^2 which is equivalent to scaling RGB by A).  If you aren't scaling RGB by A then you're giving
too many bits to RGB when A is low, and not enough when A is high.  Assuming you want a scalar weight that doesn't depend on background or A,
then plain old uniform W(A) = 1 is not too bad.  (D ~ 1/3 and A ~ 1/2 gives W(A) = 4/3 , so W(A)=1 is in the right ballpark).
