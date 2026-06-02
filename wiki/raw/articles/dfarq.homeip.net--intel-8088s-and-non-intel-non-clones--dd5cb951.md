---
title: "Intel 8088s and non-Intel non-clones"
url: "https://dfarq.homeip.net/intel-8088s-and-non-intel-non-clones/?utm_source=rss&utm_medium=rss&utm_campaign=intel-8088s-and-non-intel-non-clones"
fetched_at: 2026-06-02T07:05:05.697276+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# Intel 8088s and non-Intel non-clones

Source: https://dfarq.homeip.net/intel-8088s-and-non-intel-non-clones/?utm_source=rss&utm_medium=rss&utm_campaign=intel-8088s-and-non-intel-non-clones

The Intel 8088 CPU made its debut June 1, 1978. It rose to fame as the CPU powering the IBM PC, PC/XT, and tens of millions of PC and XT clones from the 1980s. But did you know Intel wasn’t the only company that manufactured 8088 CPUs? No fewer than nine other companies produced exact copies of the Intel 8088, and they did it with Intel’s cooperation. In this blog post, I’ll explain why.
Background on the Intel 8088 CPU
This IBM 5150 motherboard has an Intel 8088 in it, surrounded by AMD and other chips. It could have just as easily had an AMD 8088 on it. Note the AMD 8259 directly below the Intel 8088.
The 8088 was Intel’s product. One could argue it wasn’t
entirely
their design. That’s because it was a 16 bit extension to the earlier 8008 and 8080 CPUs. The 8008 was a design commissioned by
Datapoint
, a company that had designed a processor using discrete TTL logic but wanted the processor design consolidated onto a single IC. Datapoint ended up not using Intel’s chip. But Intel guessed correctly that some other companies might be interested in using it. Intel worked out an agreement to acquire the technology. Datapoint ended up regretting the arrangement, but it’s their fault they undervalued it.
The 8088 wasn’t an overnight success, but it caught its big break in 1980, when IBM decided it wanted to use it in an upcoming product. At the time, IBM was the largest computer company in the world, and they were looking to expand into the fledgling microcomputer market.
IBM’s stipulation regarding Intel’s 8088 and second sources like AMD
IBM wanted the Intel 8088, but they had a stipulation. They wanted to be able to buy it from more than one supplier. They didn’t want to find themselves in a situation where they had an order for more computers than they could deliver because they couldn’t get enough CPUs. Every other chip on IBM’s motherboard design was available from at least two manufacturers.
This was a common stipulation at the time, especially for a company the size of IBM.
Why did Intel say yes? Intel would still collect a royalty, so they would still make money if IBM bought some or even all of its 8088s from someone else. It also gave them flexibility. Intel had a finite amount of manufacturing capacity. So in the event there was some other product they could be manufacturing that would give them higher profit margins, Intel didn’t have to allocate that production to 8088s just because IBM needed chips. Presumably some of those second sources would pick up the slack. But if that didn’t happen, it was IBM’s problem, not Intel’s.
When IBM PC and XT clones appeared, most of them used 8088 CPUs as well. Approximately
60 million PCs and clones
sold in the 1980s. That included PCs based on the 8086, 286, and 386 as well. But a substantial chunk of those PCs had 8088s inside, because the 8088 was the most affordable option.
Who made 8088 CPUs besides Intel?
No fewer than 10 companies made the 8088 CPU under license. They included AMD, Fujitsu, NEC, Harris, Mitsubishi, OKI, Siemens, and Texas Instruments. AMD-manufactured 8088s are extremely common today. This suggests they sold a lot of them. IBM also manufactured 8088 CPUs. At the time, IBM was also in the chip fabrication business. Licensing the rights to make the parts they used was one way they could improve profit margins. It also mitigated the risk of IBM not being able to get enough chips from the other secondary sources.
OKI’s 80C88, a CMOS version of the 8088 that used less wattage, powered the
Atari Portfolio handheld PC
.
I personally have Intel, AMD, IBM, and Siemens 8088 CPUs in my collection.
NEC was another company that licensed the rights to manufacture the 8088. A few years later, they developed their own improved version of the 8088, called the
V20
. Intel sued, and it took about 5 years for the lawsuit to reach its conclusion. NEC prevailed and was able to continue selling the chip. But the legal cloud hanging over it may have impacted sales and kept it from being as successful as it could have been. By the time the legal cloud lifted, 8088-class PCs were very much on their last legs. The V20 had a long life in embedded and industrial applications and saw use in
palmtops.
But as a percentage of the total market, I think the NEC V20 is more popular today than it was in the 1980s.
Illegal clones
This Soviet 8088 clone wasn’t sanctioned by Intel. But numerous other companies around the world made 8088s under license.
The Soviet Union produced its own version of the 8088 CPU, the K1810VM88. The K1810VM88 is completely pin-compatible with legitimate versions of the 8088 and provides identical performance, which suggests it was a copy rather than a clean room implementation. During the Cold War, the Soviet Union didn’t care much about US intellectual property laws.
The 8088 clone that wasn’t
I’ve seen a few mentions of Commodore’s plans for the 8088 at Wikipedia and elsewhere, but I’ve never seen a good explanation of it. In 1984, Commodore International licensed to the rights to manufacture 8088 CPUs. Commodore’s subsidiary, MOS Technology, had two chip fabrication plants at the time, and the speculation was they were going to enter the PC clone market and manufacture the chips themselves to allow them to meet a lower price point. While Commodore did go on to release a number of products using 8088 CPUs, as far as I know, they never used any self-made 8088 CPUs in any of their products. Every 8088-based Commodore product I have seen, whether it was a PC or a
bridgeboard for an Amiga
, used a Siemens 8088.
There were probably two reasons for this. Commodore did not have state of the art manufacturing capabilities, so they weren’t getting the number of chips per wafer that most other manufacturers were getting by 1984. This meant they couldn’t produce as many chips as other companies could, and it meant the chips they produced cost more. In 1984, Commodore was selling computers as quickly as they could make them, so they didn’t have any manufacturing capacity to spare. They may not have had the capacity to manufacture 8088s on top of their other obligations. It’s also possible it cost them more to make an 8088 than it cost to just buy an 8088 from Siemens. And in 1985, Commodore closed the older of their two manufacturing plants rather than modernizing that plant.
It’s possible there were other companies who licensed the rights to make the 8088 and then didn’t do anything with it, but Commodore may be the most notorious.
Mostek
After I wrote an earlier version of this, a former Mostek engineer reached out to me with a story. Mostek, not to be confused with MOS Technologies, acquired a license to manufacture the similar
8086 CPU
. He said Mostek’s license allowed them to clone the chip, but Intel did not provide schematics or masks, an interesting detail. Mostek also had licenses to produce the Z80 and Motorola 68000. While Mostek-produced Z80s and 68000s exist, Mostek cancelled its 8086 project, and never released the chip. The 8088 would have been a better choice from a mass market perspective, but at the time Mostek entered the agreement, that may not have yet been clear.
Intel’s change of heart
Intel offered licensees the opportunity to manufacture Intel CPUs as second sources through the
286
generation. But something changed with the 386. Intel introduced the 386 in 1985, but at first, IBM wasn’t interested.
With no need to license the new CPU to anyone else, Intel kept that one to itself. Other PC manufacturers, notably
Compaq
, started releasing 386-based PCs in 1986, but none of them had the clout to demand a second source.
But a nearly-identical 386 did appear from a second source eventually. AMD had been manufacturing the 286 under license and had experience reverse engineering Intel CPUs, having reversed the 8080 and produced their own version called the AMD9080 in 1975. By 1987, AMD had their own version of the 386 that was completely compatible and interchangeable with the Intel version. Intel sued and was able to
keep the AMD 386 off the market unitl 1991
, but AMD prevailed and won the rights to release its new CPU. Intel countered by launching its Intel inside advertising campaign. Another
386 clone from Chips & Technologies
was less successful in court.
Over the years, numerous companies were able to produce CPUs compatible with Intel, including
Cyrix
, IDT, Rise, and
VIA
. Frequently they had to have some patent or other intellectual property that Intel needed in order to force Intel into a
patent sharing agreement
in order to do so. But by the Pentium 4 generation, all but AMD had faded into niche status. Some of those designs remain in use in embedded applications. The
Vortex86
, based on Rise’s mp6 design, is an example of an embedded Pentium-compatible CPU that has recently gained prominence in retro circles.
But for the mass market, the x86 CPU family is a duopoly between AMD and Intel. Ironically, it was one of these patent sharing arrangements that allowed Intel to use
AMD’s 64-bit extensions
to the x86 architecture in its own chips. AMD’s and Intel’s CPUs are no longer pin-compatible or interchangeable at the hardware level, and they haven’t been since the 1990s, but they remain software compatible.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Like this:
Like
Loading...
Related stories by Dave Farquhar
