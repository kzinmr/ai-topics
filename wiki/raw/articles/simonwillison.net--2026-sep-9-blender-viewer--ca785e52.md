---
title: ".blend URL Viewer"
url: "https://simonwillison.net/2026/Sep/9/blender-viewer/"
fetched_at: 2026-09-10T10:01:25.565907+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# .blend URL Viewer

Source: https://simonwillison.net/2026/Sep/9/blender-viewer/

I'm continuing to have a lot of fun with GPT-6 Astra and Blender (see
my TIL
).
As a big fan of the
Imperial Fabergé Easter eggs
, I've always thought it would be fun to make some new ones that celebrate popular culture.
Yesterday I decided to try out the new
ChatGPT Images 2.5
by
running this prompt
:
Generate a photo of a faberge egg that's themed after the TV show Pluribus - research first
It gave me this - honestly not bad for a first attempt!
Then, just to see what would happen, I pasted that image into Codex running GPT-6 Astra (high) and prompted:
Use your blender local skill to create a blender model of this faverge egg
(Here's
the skill file
, which I created
like this
.)
It churned away for 17m51s and built me
several
.blend
files
. I already had this vibe-coded Blender viewing experiment lying around, so I added that to my
tools collection
and now you can use it to
see my Pluribus blender model in your browser
:
