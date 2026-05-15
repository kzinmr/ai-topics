---
title: "Texas Instruments 486SXL CPU"
url: "https://dfarq.homeip.net/texas-instruments-486sxl-cpu/?utm_source=rss&utm_medium=rss&utm_campaign=texas-instruments-486sxl-cpu"
fetched_at: 2026-05-15T07:01:02.414040+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# Texas Instruments 486SXL CPU

Source: https://dfarq.homeip.net/texas-instruments-486sxl-cpu/?utm_source=rss&utm_medium=rss&utm_campaign=texas-instruments-486sxl-cpu

On May 14, 1992, Texas Instruments licensed
Cyrix
‘s
486SLC
and
486DLC
technologies. The agreement allowed Cyrix to use Texas Instruments’ manufacturing facilities, and for TI to create derivative chips from Cyrix’s technology. In the end, TI didn’t make as many chips for Cyrix as SGS-Thomson or IBM did, but TI did end up making interesting derivatives of Cyrix’s CPUs, including the 486SXL-40, the fastest 386-class CPU ever made. But without the burst transfer feature that Intel and AMD 486s have, none of TI’s 486s ended up performing quite up to par with an Intel or AMD 486.
The TI 486SXL
The TI 486SXL was available in both 386- and 486-compatible versions. The 386-compatible version is a popular chip among 386 enthusiasts.
I think the most interesting chip TI made under its agreement with Cyrix was the TI 486SXL. This was essentially a Cyrix 486DLC with 8K of cache rather than 1K of cache the way Cyrix made them. This chip further blurred the line between 386 and 486 performance and is the fastest CPU available for the 132-pin 386DX socket. Yes, in spite of the 486 name, many variants of this chip plugged into a
386
socket.
But don’t get too excited. Sometimes the SXL wasn’t any faster than the Cyrix 486DLC at the same speed. Usually it had a modest increase, but depending on the software you were running, it was
as low as 3 percent and as high as 16 percent
.
If you wonder why Cyrix only put 1K of cache on its 486SLC and 486DLC chips, maybe this was why. Cyrix’s profit margins were pretty bad because they were paying a premium to use someone else’s fabrication plants, so cutting the cache to 1K kept the transistor count lower and the chip size smaller. Bigger caches tend to be faster, but as cache size increases, the return on investment decreases. The first 1K makes the biggest difference.
In its Nov 15, 1993 issue,
Microprocessor Report
estimated that building the Cyrix-derived chips cost TI $37 per chip to make in late 1993. Intel was able to build 486 CPUs for $19 at the same timeframe. Getting into a price war with a 2x cost of goods isn’t ideal.
Texas Instruments 486SXL vs Cyrix 486DLC
TI’s version is interesting because TI went ahead and implemented an on-chip 8K level 1 cache like
Intel
, and while that improves performance over an
AMD 386
or a Cyrix 486DLC, a TI486SXL still isn’t as fast as an Intel 486 running at the same clock rate. This is because neither Cyrix nor TI implemented burst transfers, one of the tricks Intel used to increase the 486’s performance relative to the 386.
TI also added clock doubling, so you could run the chip on a 1X multiplier if you had a 33 or 40 MHz bus, or 2x multiplier if you had a 20 or 25 MHz bus to get up to 50 MHz.
TI also offered the 486SXL in 486SX packaging that plugged into a 168-pin socket, and the 486SXLC, which plugged into a 386SX socket. But without the burst transfers of the regular 486, TI’s 486 couldn’t keep pace with an Intel 486 when plugged into a 486 motherboard with a regular socket.
Setting the cache and multiplier
Paul Gortmaker wrote a utility for Cyrix CPUs called cyrix.exe that works to control the TI 486SXL’s multiplier.
This post on Vogons
details its use at the very top. Scroll to the end of the first message in the thread to download an archive that contains the cyrix.exe utility.
Ardent Tool also has a page
containing links to the utility.
Depending on your board, to get the cache working, try the following commands and use the one that gives you the best results in your favorite benchmarks:
cyrix.exe -f- -b -m
cyrix.exe -f -b- -m
You can also add the
-cd
parameter to either command to enable clock doubling. Only enable clock doubling when running on a 25 MHz or slower bus. Don’t expect to be able to run your 486SXL at 66 or 80 MHz. If TI had any confidence in the chips being able to run at those speeds, they would have rated them as such and charged higher prices in the 90s.
The TI486SXL didn’t get a lot of talk in the mid 90s, so it’s nice that people are digging into the mysteries of this overlooked CPU in modern times.
TI 486DX2 and 486DX4 CPUs
TI also made 486DX2 and DX4 chips, running at 66, 80, and 100 MHz and using 3.45 volts. These seem to be derivatives of the 486SXL, but benchmarks or any other details of these chips to show how, if at all, they differ from the Cyrix 486DX2 and DX4 chips are hard to find. In the days of the 486, we knew they existed, and sometimes saw them in electronics catalogs. But they were much less commonly used than AMD, Cyrix, and even IBM and ST-branded 486s. They’re also less interesting than the 486SXL because while the 486SXL has the distinction of being the fastest CPU for the 386 socket, TI’s DX2 and DX4 were middling performers, overshadowed by
AMD and Cyrix’s 5×86
CPUs in that generation.
TI had always been a major producer of logic gates and memory chips, so it made sense for them to get into processors in the 1990s. But they didn’t make much of an impact in the 486 generation, so they bowed out before getting into the Pentium generation.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Like this:
Like
Loading...
Related stories by Dave Farquhar
