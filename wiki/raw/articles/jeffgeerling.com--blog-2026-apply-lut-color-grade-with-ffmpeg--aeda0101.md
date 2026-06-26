---
title: "Quickly apply LUTs (color grading) with ffmpeg"
url: "https://www.jeffgeerling.com/blog/2026/apply-lut-color-grade-with-ffmpeg/"
fetched_at: 2026-06-26T07:00:57.002092+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Quickly apply LUTs (color grading) with ffmpeg

Source: https://www.jeffgeerling.com/blog/2026/apply-lut-color-grade-with-ffmpeg/

This is a quick post, mostly for my own reference.
I've avoided LUTs and 'Log' video footage for years
, mostly because of the extra tiny bit of workflow involved. Like RAW photos, 'Log' footage retains the video sensor's full dynamic range, so you can pull more color and luminance information out of the footage later.
But unlike photography, where RAW has been a thing for decades, and many workflows 'just work' without me having to 'grade' every individual photo, in video precious few consumer apps handle Log footage gracefully. You generally end up with a muddy grey mess.
I don't want to launch DaVinci Resolve or Final Cut Pro to process every video I shoot. Especially if I
am
recording in Log for a particular reason, but forget to switch back to 'normal' mode and shoot more clips later.
The difference is stark
, as illustrated by this clip (above) I was shooting with my kids around the house with my
DJI Osmo Pocket 4
. I just picked it up and was testing it, and I realized I still had it in '10-bit D-Log' mode after I imported the footage to my computer.
I didn't want to go through launching Final Cut Pro just to grade a half-dozen clips to put them into our family video library, so I turned to
ffmpeg
, after seeing
this mention of the built-in
lut3d
filter
.
ffmpeg for LUTs
The full
ffmpeg
command I'm using is:
ffmpeg \
-
i
/
Users
/
jgeerling
/
Downloads
/
DJI_20000219193052_0005_D
.
MP4 \
-
vf
"lut3d=osmo-vivid.cube"
\
-
c:v hevc_videotoolbox \
-
profile:v main10 \
-
b:v
30
M \
-
pix_fmt p010le \
-
tag:v hvc1 \
-
c:a copy \
DJI_0005_D_converted
.
mp4
Some of those flags will only work on a Mac, where Apple's hardware H.265 video encoder is present. The main thing is
-vf "lut3d=osmo-vivid.cube"
, which is the path to a
.cube
file for your specific camera/footage.
In this case, I'm using the
DJI Osmo Pocket 4 'vivid' LUT
.
If you'd like to modify the
ffmpeg
flags to target your own hardware's H.264 or H.265 acceleration, just grab the command above and run it through your favorite LLM. After a couple decades using
ffmpeg
, it still feels like AP Calculus 2 trying to remember all the various flags and abbreviations :D
I'd love there to be a standard for 'LUT sidecars'. Apple, BlackMagic, Sony, and others
do
embed LUT data in video files... but there's no standard, so you need DaVinci Resolve for Blackmagic camera clips, QuickTime for iPhone clips... and in the end, most non-pro apps will just show a muddy video file if you don't process it like I'm doing with
ffmpeg
.
Sigh
.
Given a particular .cube file, here's how you can apply the LUT to all the MP4 files in a given folder:
#!/bin/bash
CUBE
=
"osmo-vivid.cube"
DIR
=
"video_files"
files
=(
"
$DIR
"
/*.MP4
)
total
=
${#
files
[@]
}
count
=
0
for
input in
"
${
files
[@]
}
"
;
do
[
-e
"
$input
"
]
||
continue
((
count++
))
echo
"Processing file
$count
of
$total
:
$(
basename
"
$input
"
)
"
ffmpeg -i
"
$input
"
-vf
"lut3d=
$CUBE
"
-c:v hevc_videotoolbox -profile:v main10 -b:v 30M -pix_fmt p010le -tag:v hvc1 -c:a copy
"
${
input
%.MP4
}
_converted.mp4"
done
Put the path to your
.cube
file in
CUBE
, and the path to a directory with a bunch of ungraded .MP4 files in
DIR
. Save the script, make it executable, and run it!
