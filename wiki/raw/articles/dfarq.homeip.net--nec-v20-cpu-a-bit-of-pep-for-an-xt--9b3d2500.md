---
title: "NEC V20 CPU: A bit of pep for an XT"
url: "https://dfarq.homeip.net/nec-v20-cpu-a-bit-of-pep-for-an-xt/?utm_source=rss&utm_medium=rss&utm_campaign=nec-v20-cpu-a-bit-of-pep-for-an-xt"
fetched_at: 2026-09-22T10:00:54.674782+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# NEC V20 CPU: A bit of pep for an XT

Source: https://dfarq.homeip.net/nec-v20-cpu-a-bit-of-pep-for-an-xt/?utm_source=rss&utm_medium=rss&utm_campaign=nec-v20-cpu-a-bit-of-pep-for-an-xt

The NEC V20 was an Intel 8088-compatible CPU that ran slightly faster. It was a niche CPU in the 1980s and 1990s but had a following as a cheap upgrade for power users, especially in instances where motherboard swaps were impractical. It’s popular with retro computing enthusiasts today, as a
period-correct
upgrade. On September 22, 1986, NEC prevailed over Intel in court, clearing the way to sell it.
The NEC V20 was pin-compatible with the Intel 8088 but included some unique forward and backward compatibility features. It included the 80186 instruction set and could also emulate the Intel 8080, in addition to being faster than the 8088.
The NEC V20’s slightly troubled past
In 1982, NEC licensed the rights to produce the Intel 8088 as a second source. But in March 1984, NEC released the V20, an 8088 clone with some performance improvements. It had more than double the transistor count of the 8088 and could perform two data transfers concurrently, allowing it to complete more instructions in a given time than a real 8088.
Intel sued in late 1984. NEC said the V20 was a cleanroom design. Ultimately NEC prevailed on September 22, 1986. The legal questions surrounding the V20 likely caused larger PC makers to shy away from it. By the time it was ruled legal, the market for XT-class machines was still healthy, but XTs were budget machines, so the lower transistor count of the 8088 meant a real 8088 was going to cost less in OEM quantities.
The NEC V20 as a cheap upgrade
An NEC V20 is a cheap and easy upgrade for 8088 systems when you can’t or don’t want to swap a motherboard.
The
NEC V20
plugs directly into the Intel 8088 socket with no modifications necessary. It’s slightly more efficient than an Intel 8088 running at the same clock speed. That means an NEC V20-upgraded machine performs anywhere from 8 to 30 percent faster than an 8088, depending on the application. For most applications, the improvement is around 20 percent. That’s modest but may be enough to be noticeable. One place the V20 improves over the 8088 is performing multiplication and division in hardware, rather than in microcode. So it performs multiplication and division three times faster than an 8088.
For a much more technical deep dive, have a look at MartyPC’s
writeup on the V20
.
With Checkit 3.0, my Tandy 1000EX with an NEC V20 upgrade benchmarks 1.53x faster than the original PC/XT. In its stock configuration with a 7.16 MHz 8088, the 1000EX runs 1.31x faster than the original PC/XT.
The NEC V20 was a good processor upgrade option in machines that used nonstandard motherboards like the
Tandy 1000 and IBM PCjr
, and inexpensive PC/XT clones like the
Leading Edge Model D
. In a genuine IBM PC/XT or other clone that followed the IBM design, swapping in a small-form-factor baby AT motherboard provided more performance. But a motherboard swap cost more too.
Today, replacing the 8088 in an IBM PC or XT or compatible with a NEC V20 remains a popular upgrade option. It improves performance while permitting the owner to continue using the original motherboard. Plus it’s a period correct upgrade involving a vintage part from 1984. And a fair number of people in the know made the swap back then. They’re easy to find on
ebay
, with prices ranging from around $10-$25 (in US dollars) depending on the vintage of the chip and the locale. The lower the price, the greater the danger of a remarked chip.
NEC V20 variants
The NEC V20 was available at speeds of 5 MHz, 8 MHz and 16 MHz. An 8 MHz version is suitable for upgrading PC and XT machines running at 4.77 or 7.16 MHz. The 16 MHz version is suitable for 9.54 MHz turbo XT clones.
The V20 carried a part number of D70108C, so you sometimes hear it referred to by that name. NEC had three licensees who also made the chip in the 1980s. So if you find a Sharp LH70108, Sony CXQ70108, or Zilog Z70108, they are all functionally the same chip.
The V20HL is a slightly later revision that runs cooler than the original.
Even though I frequently see retro computer enthusiasts on Youtube putting heatsinks on their V20s, it’s not really necessary. That’s especially true of the later V20HL variant. The chips run cool anyway, and in PC applications they’re always running at lower than their rated speed. The heatsink doesn’t hurt anything, but it’s overkill.
What’s the point?
When you install an NEC V20 in an
IBM PC 5150
or
XT 5160
, it’s still an IBM. Although a faster motherboard will fit in an XT, it’s not an IBM anymore once you do that. The V20 lets you retain the original motherboard and original BIOS, everything but the CPU, and it runs a little bit faster. And if you ever need to revert the mod, it’s easy. It only takes a couple of minutes to swap the 8088 back into the CPU socket.
In a PCjr or Tandy 1000, the NEC V20 gives you a slightly faster CPU to complement the machine’s enhanced graphics and sound. Some of Sierra’s later titles run poorly on a stock 8088 and benefit from the boost. A
Tandy 1000 TX
or TL with a 286 will give better performance. But that also means you have to find one. The 8088-based Tandy 1000s were more plentiful.
The other nice thing about a NEC V20 is that some network drivers that say they require a 286 will work on a V20. If you want to network your XT-class machine to make it easier to load software on it, this is helpful.
And if your XT motherboard is able to use a third party BIOS like
GLaBIOS
, you can get a build optimized for the V20 that uses its extra instructions to improve overall system performance.
Speeding up your XT IDE interface
If you have an XT IDE interface and use a compact flash card with it, installing a V20 CPU and reassembling the XT IDE BIOS with V20/80186 instructions speeds up IDE access almost 90 percent. If you use a
Tandy 3 in 1 card
, Rob Krenicki has already built and provided a suitable
V20 optimized BIOS
for that purpose. On my Tandy, disk throughput went from around 250K per second to around 500K per second.
So even if the benefits when running software can be inconsistent, an NEC V20 has a very noticeable impact on your loading times, at least if you use XT IDE. And everyone likes faster loading times.
The NEC V20 as an Intel 286 alternative
The NEC V20 implements the Intel 80186 instruction set. The
186 saw limited use as a CPU in PC compatibles
so it’s an obscure chip in retro PC circles today. The later 286 and 386 processors proved far more popular and enduring. But since a fair bit of software that claims to require a 286 processor actually only uses 8086 and 186 instructions, the V20 has reasonable compatibility with the 286.
The V20 isn’t as fast as a 286 partly because it’s limited by the 8088’s 8-bit data bus. A V20 running at 7.16 MHz benchmarks about half as fast as the original IBM PC/AT, which had a 6 MHz 286. But at least it allows some software to run that wouldn’t run before.
One of those pieces of software happens to be the MS-DOS editor that shipped as part of Windows 95. The Windows 95 version of the DOS editor is smaller and faster than its DOS 6.22 counterpart because it doesn’t rely on the QBASIC executable. It’s also compiled with 80186 instructions, rather than the 8086 instructions the version that shipped with DOS 5 and DOS 6 used. So it won’t run on an 8088, but runs happily on the NEC V20. And it’s noticeably faster than the version from DOS 6.22. So you can make your V20-based DOS PC a little bit nicer to use by copying edit.exe from a Windows 95 PC to your DOS directory.
The NEC V20 in the 1980s and 1990s
The big-name PC vendors like IBM and Tandy stuck with Intel 8088s and its
authorized second-source providers
like AMD and Siemens. However, by the late 1980s it wasn’t hard to find XT clone boards with factory-installed V20 processors. These found their way into many white-box PC and XT clones. They provided an alternative for people who needed something faster than an 8088 but couldn’t afford a 286, and
wanted good backward compatibility
. And HP used the V20 in its
HP 95LX palmtop
.
Power users were aware of the V20, and I knew of a few people in the St. Louis area who took advantage of the V20’s Intel 8080 compatibility mode to run
CP/M
software on their PC and XT clones.
It wasn’t necessarily something you’d find at just any computer store. It was more of a
back pages of Computer Shopper
thing.
NEC V20 vs Intel 8088
When it comes to an NEC V20 vs Intel 8088, the chips have obvious similarities. But while there were lots of second-source 8088s, made with Intel’s blessing, the V20 wasn’t one of them. The V20 is more like the spiritual ancestor of
Cyrix 6×86 processors
: independently reverse-engineered and pin-compatible with the dominant Intel processor of the time, with some more advanced technology bolted on. UMC was another company who tried NEC’s approach, in the 486 era, but
UMC’s 486 didn’t survive Intel’s challenges in court
.
The 8088 wasn’t the most efficient CPU of its era and NEC tried to address that, which is why a V20 is a bit faster than an 8088 when running at the same clock speed. The V20 gets about 20% more work done per clock cycle than its more famous competitor.
The V20 also ran at higher clock rates than the 8088, generally at 8, 10, and 16 MHz, but in PC applications it was generally clocked at 7.16 or 9.54 MHz. When you swap it in for an 8088, it runs at the same clock speed as the 8088 it replaced, with the performance increase coming strictly from its improved efficiency.
The V20 is still an XT-class CPU, like the 8088. But if you have an 8088-based system and want to put a little more spring in its step, the V20 is a reasonably priced upgrade to do so. It was affordable in the 1980s. And it’s still readily available and affordable today.
The PC-Sprint and the NEC V20
In the mid 1980s, there was a hack going around called the
PC-Sprint
. This was (and is) a free project that made a cheap accelerator for an IBM PC or XT. It also works in some of the more popular compatibles like the original
Compaq Portable
and the early Tandy 1000/1000A. In theory it might work with some other XT clone motherboards too. By adding the PC-Sprint daughterboard to a PC or XT and swapping the CPU, you can run a PC or XT at 7.16 MHz instead of 4.77 MHz. Some people call this the
first overclocking project
, but it’s not really overclocking. You’re swapping the CPU for one that runs at the rated speed, and the whole point of the mod is running the rest of the motherboard at 4.77 MHz.
In theory you probably
could
run the stock 8088 at 7.16 MHz. And that would be overclocking. But it’s also less reliable.
The PC-Sprint of course works fine with the V20. The V20 is designed to run at 8 or 16 MHz, so 7.16 MHz doesn’t hurt it at all. A PC or XT running a V20 at 7.16 MHz will run noticeably faster than the original. It should give a 50-75% improvement. It still won’t be as fast as a 6 MHz 286, but it will make a PC or XT more enjoyable to use, while retaining the soul of the old machine. And like the V20, you can revert the PC-Sprint mod in a matter of minutes.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
