---
title: "cbloom rants: AVIF Test"
url: "http://cbloomrants.blogspot.com/2021/01/avif-test.html"
fetched_at: 2026-05-05T07:01:48.546138+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# cbloom rants: AVIF Test

Source: http://cbloomrants.blogspot.com/2021/01/avif-test.html

AVIF is an image format derived from I-frames of AV1 video (similar to HEIC/HEIF from H265/HEVC).

See also my
2014 Test of BPG
, which is an H265 I-frame image format.
Here are some links I've found on AVIF :
AVIF image format supported by Cloudflare Image Resizing
GitHub - AOMediaCodeclibavif libavif - Library for encoding and decoding .avif files
GitHub - googlebrunsli Practical JPEG Repacker
Releases · kornelskicavif-rs · GitHub
GitHub - link-ucavif avif encoder, using libaom directly.
GitHub - xiphrav1e The fastest and safest AV1 encoder.
AVIF for Next-Generation Image Coding by Netflix Technology Blog Netflix TechBlog
Submissions from xiph.org Hacker News
Image formats for the web HEIC and AVIF – The Publishing Project
Squoosh
Comparing AVIF vs WebP file sizes at the same DSSIM
AV1 Codec
AVIF images color losschange AV1
Unfortunately I have not found a standard encoder with recommended settings.  There appears to be zero guidance on settings anywhere.
Because of that I am using the simplest encoder I could find, Kornelski's "cavif" which has a simple --quality parameter.  I run thusly :
cavif --quality=X -o out.avif in.png
avifdef out.avif dec.png
imdiff in.png dec.png
CALL FOR HELP : if you know better programs/settings for encoding AVIF, please let me know
; in avifenc , what is the min max Q parameter?
adaptive quantization appears to be off by default, don't we want that on?
I measure results using my
imdiff
I will compare AVIF to what I call "JPEG++" which is JPEG with the packjpg/Lepton back end, and a deblocking decoder (my "jpegdec").  This a rough
stand-in for what I think a real JPEG++ should be (it should really have an R-D front-end and chroma-from-luma as well; that's all very easy and
unequivocably good).
With no further ado, some results :
(imdiff "fit" is a quality in 0-10 , higher is better)
porsche640.bmp :
PDI_1200 :
Results are a bit disappointing.  AVIF is much beter on RMSE but slightly worse on my other two scores.
Overall that means it's most likely better overall, but it's not a huge margin.
(I'm sure AVIF is a big win on graphic/text images where JPEG does poorly)
AVIF results here look worse than what I saw from BPG (HEIC).  Perhaps better encoders/settings will fix that.
Looking at the results visually, AVIF preserves sharp lines much better, but is completely throwing away detail
in some places.  There are some places where I see AVIF actually *change* the image, whereas JPEG is always just
making the same image but slightly worse.
7z of encoded images to compare (2 MB)
NOTE : the fact that AVIF wins strongly in RGB RMSE but not in my other perceptual metrics indicates that is is not optimizing
for those metrics.  Perhaps in other perceptual metrics it would show a strong win.  The metrics I use here from
imdiff were chosen because I found them to be the best fit to human quality scores.  Lots of the standard scores
that people use (like naive SSIM) I have found to be utter junk, with no better correlation to human quality than
RMSE.  MS-SSIM-IW is the best variant of SSIM I know, but I haven't tested some of the newer metrics that have come
out in the last few years.
