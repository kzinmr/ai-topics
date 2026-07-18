---
title: "Regressive JPEGs:"
url: "https://maurycyz.com/projects/bad_jpeg/"
fetched_at: 2026-07-18T07:00:47.400063+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Regressive JPEGs:

Source: https://maurycyz.com/projects/bad_jpeg/

Regressive JPEGs:
2026-07-17
One of the cool features of JPEG files is that there's the option to save low frequency components first.
This means that a partially downloaded image will be displayed at low resolution instead of being cut off.
In the file, this works by breaking up the compressed data into multiple "scans", each prefixed with a header.
Here's the first scan of a representive image:
FF DA
- "start of scan" marker
00 0C
- Big endian length field (12 bytes)
Includes itself
03
- Number of channels in scan (3)
01
- Global id of first included channel
00
- Huffman table index #1 (DC: 0, AC: 0)
02
- Global id of second included channel
10
- Huffman table index #2 (DC: 1, AC: 0)
03
- Global id of third included channel
10
- Huffman table index #2 (DC: 0, AC: 0)
00
- Starting DCT bin (DC)
00
- Ending DCT bin (also DC)
01
- Precision: half, no pre-existing data. 

f8ad 512d d3f1 cd96
- Huffman coded DCT coefficients
bcb0 58df 53d5 5d97
[...and a lot more]
... this one includes the lowest (DC) Fourier bin for all three color channels.
The three color channels are YCbCr instead of the usual RGB.
The luminance (Y) seperated because it must be high quality, but the color can be fudged quite a bit while looking fine.
Very roughly: Y = G, Cb = B - G, Cr = R - G
After it, the file contains eight more scans to fill in the rest of the data:
Scan number
Channels
DCT bin range
Precision
0
Y Cb Cr
0 - 0
Half (-1 bit)
1
Y
1 - 5
Quarter (-2 bits)
2
Cb
1 - 63
Half
3
Cr
1 - 63
Half
4
Y
6 - 63
Quarter
5
Y
1 - 63
Half
6
Y Cr Cb
0 - 0
Full
7
Cr
1 - 63
Full
8
Cb
1 - 63
Full
9
Y
1 - 63
Full
Scan #0 contains a very low resolution preview of the image.
Scan #1 adds some details to the luminance.
Scans number two through five contain full low precision data.
Scan 4 has an unusual spectral range because it's filling in the gap left by #1.
That way, number 5 has full quarter precision data to build on.
Scans six through nine add the final missing bit to bring the image to full quality.
Given what I said about color being less important, it might seem weird that my example has the color data first:
This works because the the chrominance is saved at half resolution (quarter pixel count).
As a result, full chrominance data (Cr + Cb) only weighs half as much as luminance.
Since each scan explicitly sets its spectral range
,
it should be possible to construct a JPEG file
where future scans overwrite already rendered image data.
Actually, it's very easy to do this:
Concatenate multiple images with the same resolution and filter out the start-of-image, start-of-frame and end-of-image markers.
This can be done in a hex editor, but I used a quick and dirty C program.
When served over a slow network
, this concatenated file will switch between multiple images:
Click to open in new tab
But, most decoders will give up after some number of scans
:
I think this is done to avoid a zip bomb style problem...
but it prevents this from working on more than 9 frames, which is not enough for a proper animation.
To do that, I'd have to minimize the number of scans in each frame. 
The simplest idea is to start with baseline JPEGs that only have a single scan.
... but it doesn't work:
In progressive mode, a scan can't contain both AC (bins above 0) and DC (bin 0) data at the same time.
This limitation doesn't exist for baseline mode, but the baseline decoder stops after the first scan.
Since AC data must follow DC data, the smallest possible "progressive" JPEG contains a single DC-only scan.
Because the DCT runs on 16x16 blocks, such an image won't a solid color:
it'll be 1/16th of the original resolution.
Scan number
Channels
DCT bins
Precision
0
Y Cb Cr
0 - 0
Full
Doing this, I can get Chrome to render around 90 frames before giving up.
Other browsers like Firefox have more patience, but a 90 scan image seems to work almost everywhere.
As a bonus, this avoids the ghosting of the naive attempt:
that happened because AC scans are supposed to refine old data.
Normally, this allows images to include multiple precision levels without inflating file size...
but doesn't play nicely with my tricks.
If the file only includes DC scans with no actual progression, this isn't a problem.
Since a "DC-only" frame is a standards-compliant images
, creating them doesn't require anything special:
cat
>
frame.scans
<<EOF
# DC only scan:
0,1,2:0-0,0,0;
# and nothing else
EOF
jpegtran
-scans
frame.scans
-outfile
out.jpg in.jpg
Using these, it's possible to pack a whole video inside a single image:
Click to open in new tab
Besides unconventional rickrolls and other trolling, this has no practical applications:
there's no way to add timing information, so playback is entirely dependent on network delay.
... although there is a lot of fun to be had using partial rendering:
This is a pure HTML video using <dialog> tags:
badapple.rose.systems
Of course, there's no rule that the data must be hardcoded:
here's a
interactive single-page application
with no CSS or JavaScript.
Related
:
