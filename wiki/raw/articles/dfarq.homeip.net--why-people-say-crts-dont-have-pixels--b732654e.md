---
title: "The Silicon Underground"
url: "https://dfarq.homeip.net/why-people-say-crts-dont-have-pixels/?utm_source=rss&utm_medium=rss&utm_campaign=why-people-say-crts-dont-have-pixels"
fetched_at: 2026-05-30T07:01:27.617047+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# The Silicon Underground

Source: https://dfarq.homeip.net/why-people-say-crts-dont-have-pixels/?utm_source=rss&utm_medium=rss&utm_campaign=why-people-say-crts-dont-have-pixels

I keep hearing people say that CRTs don’t have pixels. That is incorrect. We talked about pixels all the time in the 1980s when CRTs were all we had. In this blog post, I will try to clear up the confusion around pixels and the difference in the way CRTs and LCDs handle them.
The pixels on this Commodore 1702 CRT monitor are clear as it plays Flight Simulator II. CRT monitors have pixels. What they don’t have is fixed resolution.
When you fire up your favorite 8-bit computer system or game console connected to a CRT monitor, you see plenty of pixelated glory. The pixels may be a little bit fuzzy, but you can very visibly see pixels as the jagged edges on any shape that deviates from either a straight horizontal line or a straight vertical line. The only exception to this is a vector display, which is why the
1982 Vectrex console was such a big deal
.
Pixels and dot pitch
The pixels on CRT monitors were the whole reason people cared about dot pitch. Dot pitch is the distance between pixels. If a monitors dot pitch was too high, it meant it couldn’t clearly display images above a certain resolution. It would go ahead and try, but the image would be soft. A
Commodore 1702 monitor
didn’t have a high enough dot pitch to display 640 pixels across. You can connect it to a Commodore 128 80 column display or to a Tandy 1000, and it will display it without distorting it, but it won’t be sharp. This was the problem with
Tandy’s CM-5 monitor
. Its tube had too little dot pitch, so it looked fuzzy next to the more expensive
Tandy CM-11
.
Dot pitch imposes a limitation on how much the resolution can scale upward, but it doesn’t impose a limitation on scaling down. That’s why a vintage computer or game console can look pixel perfect on a CRT but the image look distorted on an equivalent sized LCD.
Why people say CRTs don’t have pixels
What CRTs
don’t
have is a fixed resolution. LCD panels consist of millions of individual points of light. A single pixel consists of a red, green, and blue point of light. By mixing the intensity of those three, it can produce more colors than the human eye can discern. A full HD display has 1,920 pixels across and 1080 pixels down.
When you feed a flat panel display with a resolution other than its native resolution, it has to letterbox it and scale it, using multiple pixels to represent the larger pixels on the lower resolution display. When the two resolutions are not even multiples of one another, the display ends up scaling unevenly and doesn’t look its best. Sending a 640×480 image to a panel with a native resolution of 1024×768 or 1280×1024 won’t scale evenly, and the older the panel is, the worse it will probably look. Newer panels have enough pixels to spare to letterbox the image in addition to scaling it, and if that’s not enough, they have logic to interpolate the image to make it look better. But all of this adjustment can introduce lag. Plus, you’re letterboxing a 4:3 image on a16:9 display.
That said, when the resolution of the panel matches the resolution of the signal, the LCD panel will usually look better than a CRT, because you get a pixel perfect image, and the image is sharper.
How CRTs work differently
A CRT doesn’t care about the resolution because it just has three guns that fire electrons at the tube while drawing each raster line. To get higher resolution, the guns just fire more times. It is drawing the picture one pixel at a time, but it happens so quickly you barely perceive it.
Depending on the quality of the tube, it may not be able to draw a high resolution image enough times per second to be imperceptible. I once owned a monitor that could display 1024×768, but it could only do it at 43 HZ. 43 HZ looked very flickery to me at the time. It might look less bad to me now, or it may look worse. Everyone is different. I used to know someone who claimed anything lower than 75 Hz was blinding. Meanwhile, I could barely see the difference between 60 and 75. I couldn’t tell a difference between 70 and 75. But he claimed he could.
Panels refresh rates too, but the refresh rate has a different effect on panels. With CRTs, you get flicker. Panels don’t have flicker, but a lower refresh rate causes more lag.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Like this:
Like
Loading...
Related stories by Dave Farquhar
