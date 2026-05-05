---
title: "cbloom rants: Some JPEG Tools"
url: "http://cbloomrants.blogspot.com/2021/01/some-jpeg-tools.html"
fetched_at: 2026-05-05T07:01:48.101729+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# cbloom rants: Some JPEG Tools

Source: http://cbloomrants.blogspot.com/2021/01/some-jpeg-tools.html

A couple of tips and tools for working with JPEG files.  I use :
jhead
jpegcrop
Of course you can use exiftool and jpegtran but these are rather simpler.
1. Strip all personal data before uploading images to the web.
JPEG EXIF headers contain things like date shot and location.  If you don't want Google to scrape that and use it
to track your movements and send drones to follow you carrying advertisements, you might want to strip all that private
data before you upload images to the net.  I use :
jhead -purejpg %*
jhead -mkexif %*
jhead -dsft %*
with the very handy jhead tool.  This removes all non-image headers, then makes a blank exif, then sets the exif time from the mod time.
The last two steps are optional, if you want to preserve the shot time (assuming the mod time of the file was equal to the exif time).
Note if the times are not equal you can use "jhead -ft" to set modtime from exif time before this.
Also note that if you use tools to modify images (resizing, changing exposure, what have you), they may or may not carry through the old exif data; whether that's
good or bad is up to you, but it's very inconsistent.  They also will probably set the modtime to now, whereas I prefer to keep the modtime = shot
time so that I can find files by date more easily.
2. Remove orientation tags
iPhones are the only device I know of that consistently make use of the JPEG orientation tags rather than actually rotate the pixels.
Unfortunately lots of loaders don't support these tags right, so if you load the image in a non-compliant loader it will appear sideways
or upside down.
(this is a classic problem with data formats that have too many features; inevitabily many implementers only support a subset of the features
which they deem to be the necessary ones; then some bone-head says "oh look the format has this weird feature, let's use it", and they output
data which most loaders won't load right (then they blame the loaders).  This is a mistake of the people defining the format; don't include unnecessary features, and make
the practical subset a well-defined subset, not something that forms ad-hoc from use.)
To fix this, you want to read the orientation tag, rotate the pixels, then blank out the orientation tag (you have to do the last step or
compliant loaders will doubly rotate).  I used to have scripts to do all that with jpegtran, but it's super easy to do with jhead, you just :
jhead -autorot %*
3. Lossless crop
Avoid loading a JPEG, modifying it, and saving it out again.  It destroys the image by re-applying the lossy quantization.  I think by
far the most common modification people do is cropping and there's no damn reason to re-encode for a crop.  You can crop at 8x8 granularity
losslessly, and you should.  (all the web image uploaders that give you a crop tool need to do this, please, stop sucking so bad).
jpegcrop
is a GUI tool that provides a decent lossless crop.
FreeVimager is okay too.  Lossless crop is hidden in "JPEG Advanced".
We've got JPEG-XL coming soon, which looks great, but all the tech in the world won't help if people like
Instagram & Youtube keep re-encoding uploads, and re-encoding every time you modify.
