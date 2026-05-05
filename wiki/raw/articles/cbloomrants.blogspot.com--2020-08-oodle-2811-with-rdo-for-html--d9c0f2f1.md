---
title: "Oodle 2.8.11 with RDO for BC1_WithTransparency"
url: "http://cbloomrants.blogspot.com/2020/08/oodle-2811-with-rdo-for.html"
fetched_at: 2026-05-05T07:01:48.710492+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Oodle 2.8.11 with RDO for BC1_WithTransparency

Source: http://cbloomrants.blogspot.com/2020/08/oodle-2811-with-rdo-for.html

Oodle Texture 2.8.11 adds support for RDO encoding of "BC1_WithTransparency" and BC2.  We now support RDO
encoding of all BC1-7 variants.
In Oodle, "BC1_WithTransparency" doesn't necessarily mean that the texture has any 1-bit transparency.
(for background: BC1 can encoding alpha values of 0 or 255 (1.0), which binary on/off alpha; when alpha is 0 the
color is always 0 or black).  It means that the transparency bit is preserved.  In our normal "BC1" encoder,
we assume that the alpha value will not be read, so we are free to choose the encoding to maximize RGB quality.
The choice of "BC1_WithTransparency" vs "BC1" should not be made based on whether the source has alpha or not,
it should be made based on whether your shader will *consume* alpha or not.  So for example if you just have
opaque RGB textures and you need to be able to pipe them to a shader that reads A to do alpha blending, and you are unable to manage
the book-keeping to pipe constant 1.0 as a shader source for the A channel, then you must use "BC1_WithTransparency"
to encoding opaque alpha in the texture.
When possible, we think it is best to use the "BC1" format which does not preserve alpha.  Most people do not actually use
binary transparency in BC1 (even for textures where the alpha is binary in the top mip, you typically need full alpha to make
decent mips, so you should use BC7), they use BC1 for opaque textures.  On opaque textures the "BC1" format that is free to
change alpha can give much higher quality.  You can then just map constant 1.0 as the A value source for the shader when binding a
texture that is marked as opaque.
We understand that is not always practical in your pipeline, so we are trying to make "BC1_WithTransparency" work as well
as possible.
Our RDO for "BC1_WithTransparency" will never change the binary alpha state of a pixel.  Because of this the
RMSE is actually only RGB, the A values will never differ from the original, assuming the original only had
alpha values of 0 and 255 in U8.
An example of the quality of "BC1_WithTransparency" RDO on the "mysoup" image available in the
Oodle Texture sample run
:
otexdds bc1 mysoup1024.png r:\mysoup1024.dds --verbose
OodleTex_BC1 RMSE per texel: 7.0511

otexdds bc1a mysoup1024.png r:\mysoup1024.dds --verbose
OodleTex_BC1_WithTransparency RMSE per texel: 7.0510

otexdds bc1 mysoup1024.png r:\mysoup1024.dds --verbose --rdo
OodleTex_BC1 RMSE per texel: 7.5995

otexdds bc1a mysoup1024.png r:\mysoup1024.dds --verbose --rdo
OodleTex_BC1_WithTransparency RMSE per texel: 7.6006
On photographic images like this without a lot of opaque-black, the quality of "BC1_WithTransparency" is
almost identical to "BC1".
On images that mix opaque black and other colors, the quality difference can be severe :
otexdds bc1 frymire.png r:\out.dds --verbose
OodleTex_BC1 RMSE per texel: 6.1506

otexdds bc1a frymire.png r:\out.dds --verbose
OodleTex_BC1_WithTransparency RMSE per texel: 12.1483
On "Frymire" from the Waterloo Bragzone set, the RMSE is nearly double with "BC1_WithTransparency".
We have also updated the Unreal integration for Oodle Texture to use "BC1_WithTransparency", as Unreal expects to
be able to fetch opaque A from the texture on all BC1 encodings.  Prior to 2.8.11 we were incorrectly using our
"BC1" format in Unreal, which could change opaque black texels to transparent black.
Note that "BC1_WithTransparency" RDO's roughly the same as "BC1", so we expect compressed sizes to stay roughly
the same.
