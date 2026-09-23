---
title: "Abusing CD-Rs, DVD-Rs, and BD-Rs for Science"
url: "https://jayd.ml/2026/09/05/burned-media-torture-test.html"
fetched_at: 2026-09-22T10:00:53.850473+00:00
source: "jayd.ml"
tags: [blog, raw]
---

# Abusing CD-Rs, DVD-Rs, and BD-Rs for Science

Source: https://jayd.ml/2026/09/05/burned-media-torture-test.html

I’ve been on an optical media kick lately, having a grand old time burning
discs and whatnot. One bit of advice that consistently comes up: don’t let your
burned discs get exposed to sunlight; the dye layer is UV after all, and since
the
sun is a deadly laser
it can damage
your precious bits.
Naturally, this advice needs to be tested to determine what
actually
happens 
if you disregard it.
I had a friendly LLM
shart out some scripts
to generate max-size iso images and sha256sum them from the disc, and burned 
using k3b:
Verbatim CD-R
(at max speed, 40x)
Verbatim CD-RW
(at max speed, 40x)
Verbatim DVD-R
(at max speed, 16x)
I also have a second DVD-R that long story short had 615 buffer underruns
while burning. It passed verification, but it seemed like a poor test subject.
I exposed it though because it would be interesting if using Burnfree made
it degrade faster
Verbatim BD-R
(at max speed, 12x)
The CD and DVD were burned with a brand new (old stock) Hitachi-LG data storage
GHD0N
, the Blu-ray with
a brand new LG
WH16NS60
. The blanks were also just purchased
from Amazon, so hopefully they are fresh.
I verified each burn with k3b as well as my slop-script, and placed them in 
a ziplock baggie (so they don’t get physically dirty and ruin by readers) with
the media side facing west in a window. They’ll get blasted by the sun for hours
each day, and are physically warm to the touch.
I’ll update this post as I go along.
Updates
2026-09-06
Hung the discs in the window.
2026-09-21
Finally had time to check on these. Looks like I waited too long.
I’ll hang them back up and check in again later.
