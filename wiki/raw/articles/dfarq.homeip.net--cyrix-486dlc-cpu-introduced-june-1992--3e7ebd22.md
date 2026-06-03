---
title: "Cyrix 486DLC CPU: Introduced June 1992"
url: "https://dfarq.homeip.net/cyrix-486dlc-cpu-introduced-june-1992/?utm_source=rss&utm_medium=rss&utm_campaign=cyrix-486dlc-cpu-introduced-june-1992"
fetched_at: 2026-06-03T07:01:41.609496+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# Cyrix 486DLC CPU: Introduced June 1992

Source: https://dfarq.homeip.net/cyrix-486dlc-cpu-introduced-june-1992/?utm_source=rss&utm_medium=rss&utm_campaign=cyrix-486dlc-cpu-introduced-june-1992

In the first week of June 1992,
Cyrix
debuted its 486DLC CPU. Cyrix didn’t have its own fabrication plants so they made arrangements with Texas Instruments to manufacture the chips in May 1992. Part of the agreement allowed TI to make its own derivatives of the chips. The 486DLC was really more a 386DX/486SX hybrid than a true Intel 486 clone. It plugged into a 386DX socket and had the 486 instruction set and 1K of L1 cache. Clock for clock the Intel 486 was faster, though the 486DLC had its uses.
The Cyrix 486DLC CPU
The Cyrix 486DLC clocked as high as 40 MHz. At $119, it was a bargain in 1992.
Released about
three years after Intel’s 486
and initially priced at $119, the Cyrix 486DLC could run at up to 40 MHz. But a 40 MHz 486DLC was closer to a 25 MHz 486SX in performance, slightly faster than an
AMD 386DX
running at 40 MHz. The 486DLC allowed motherboard makers to extend the lifespan of their 386 boards, letting them sell them as 486 boards with a BIOS upgrade, and with the ability to take a 387 math coprocessor. A 486DLC with a math coprocessor still wasn’t as fast as a 25 MHz 486
DX
. But it was faster than a 486SX at math operations and cheaper than an Intel DX.
It wasn’t just the smaller L1 cache that limited its performance. The slower 386 bus also slowed it down, and the Cyrix core was about 10 percent slower than the Intel 486 core, largely because it didn’t implement the Intel 486’s burst mode.
And although the DLC name suggested it competed with the 486DX, it was only competitive with a DX when you added a math coprocessor. Otherwise, it was closer to the Intel 486
SX
.
Why Cyrix only gave you 1K of L1 cache
If you wonder why Cyrix only put 1K of cache on its
486SLC
and 486DLC chips, it was probably cost. Cyrix’s profit margins were pretty bad because they were paying a premium to use someone else’s fabrication plants, so cutting the cache to 1K kept the transistor count lower and the chip size smaller. Bigger caches tend to be faster, but as cache size increases, the return on investment decreases. The first 1K makes the biggest difference.
In its Nov 15, 1993 issue,
Microprocessor Report
estimated that building the Cyrix-derived chips with 8K of L2 cost TI $37 per chip to make in late 1993. At that price, selling the chip for $119 wasn’t possible. But if Cyrix could get the cost of production plus what it owed TI down to $40 or less, they could sell for $119 and do OK. But meanwhile, Intel was churning out 486 CPUs for $19 apiece and getting much more than $119 a pop for them.
Texas Instruments 486SXL vs Cyrix 486DLC
TI’s 486SXL
is interesting because TI went ahead and implemented an on-chip 8K level 1 cache like
Intel
, and while that improves performance over an AMD 386 or a Cyrix 486DLC, a TI486SXL still isn’t as fast as an Intel 486 running at the same clock rate. TI also added clock doubling, so you could run the chip on a 1X multiplier if you had a 33 or 40 MHz bus, or 2x multiplier if you had a 20 or 25 MHz bus to reach 40 or 50 MHz.
TI also offered the 486SXL in 486SX packaging that plugged into a 168-pin socket, and the 486SXLC, which plugged into a 386SX socket. But without the burst transfers of the regular 486, TI’s 486 couldn’t keep pace with an Intel 486 when plugged into a 486 motherboard with a regular socket.
You can also find 486DLC chips with TI branding on them. These are the same as a Cyrix 486DLC, right down to the 1K of L1 cache.
The 486DLC’s legacy
The 486DLC put Cyrix on the map as a scrappy maker of value-priced CPUs. The Cyrix 5×86 of a few years later was the spritual successor to the 486DLC, putting a Pentium-like core in 486 packaging. Its most successful CPU was the 6×86, a Socket 7 chip that was faster clock for clock than a Pentium, at least for integer operations. It beat AMD to market, so the 6×86 sold fairly well until AMD released its
K6
. The 6×86 was overmatched against the K6.
Enabling the cache on a Cyrix CPU
Paul Gortmaker wrote a utility for Cyrix CPUs called cyrix.exe that works to enable the 486DLC’s cache if your motherboard doesn’t.
This post on Vogons
details its use at the very top. Scroll to the end of the first message in the thread to download an archive that contains the cyrix.exe utility.
Ardent Tool also has a page
containing links to the utility.
The command
cyrix.exe -i1 -f
will generally get the Cyrix 486DLC’s cache running on most motherboards and give you the speed increase over an AMD 386DX-40 that you’re looking for.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Like this:
Like
Loading...
Related stories by Dave Farquhar
