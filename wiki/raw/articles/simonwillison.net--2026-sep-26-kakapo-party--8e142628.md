---
title: "Tool: Kākāpō Party"
url: "https://simonwillison.net/2026/Sep/26/kakapo-party/"
fetched_at: 2026-09-27T10:01:13.249658+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Tool: Kākāpō Party

Source: https://simonwillison.net/2026/Sep/26/kakapo-party/

I presented a closing keynote for the
WeAreDevelopers World Congress North America
yesterday. As
a STAR moment
I decided to weave in references to the record breaking
kākāpō breeding season
we had in 2026.
For my closing slide I wanted to celebrate, and I had seen some buzz around how good Claude Opus 5.5 was at creating pixel art animations. So I rounded up three Kakapo photos from Google image search and dropped them into Claude with this prompt:
Here are some photos of kakapo parrots just to remind you what they look like
I need you to make an animation in animated pixel art on HTML 5 canvas of obviously pixel art kakapo jumping up and down having a party with confetti and suchlike - there should be at least 20 of them
Here's
the transcript
, and this is the
resulting page
. It's pretty great!
I wanted to embed it in a Keynote presentation file, so I downloaded the HTML and told a local Claude Code session:
Make me a video of file:///Users/simon/Downloads/kakapo-party.html - you need to load it in a browser and click on it a few times to get the confetti effect, the video should be 15s long
don't start clicking until 3s in
make sure several clicks are spread around the clickable area
Claude Code used Playwright (
transcript here
) and produced this video, which was exactly what I needed for my final slide:
Your browser does not support HTML5 video.
Here's the full Playwright script it used, which was pleasingly short:
# /// script
# dependencies = ["playwright"]
# ///
import
time
from
playwright
.
sync_api
import
sync_playwright
W
,
H
=
1280
,
720
# Canvas fills the viewport; spread clicks across corners, edges and centre
clicks
=
[
    (
3.0
,
640
,
360
),
# centre
(
4.2
,
160
,
120
),
# top-left
(
5.4
,
1120
,
120
),
# top-right
(
6.6
,
180
,
600
),
# bottom-left
(
7.8
,
1100
,
600
),
# bottom-right
(
9.0
,
640
,
100
),
# top-centre
(
10.0
,
380
,
380
),
# mid-left
(
11.0
,
900
,
380
),
# mid-right
(
12.2
,
640
,
620
),
# bottom-centre
(
13.2
,
640
,
300
),
# finale centre
]
with
sync_playwright
()
as
p
:
b
=
p
.
chromium
.
launch
()
ctx
=
b
.
new_context
(
viewport
=
{
"width"
:
W
,
"height"
:
H
},
record_video_dir
=
"vids"
,
record_video_size
=
{
"width"
:
W
,
"height"
:
H
})
page
=
ctx
.
new_page
()
t0
=
time
.
time
()
page
.
goto
(
"file:///Users/simon/Downloads/kakapo-party.html"
)
for
t
,
x
,
y
in
clicks
:
time
.
sleep
(
max
(
0
,
t
-
(
time
.
time
()
-
t0
)))
page
.
mouse
.
click
(
x
,
y
)
time
.
sleep
(
max
(
0
,
16.0
-
(
time
.
time
()
-
t0
)))
ctx
.
close
();
b
.
close
()
