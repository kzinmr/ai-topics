---
title: "Working around dragons with the Lemote Yeeloong laptop and OpenBSD"
url: "https://oldvcr.blogspot.com/2026/06/working-around-dragons-with-lemote.html"
fetched_at: 2026-06-28T07:01:24.472408+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Working around dragons with the Lemote Yeeloong laptop and OpenBSD

Source: https://oldvcr.blogspot.com/2026/06/working-around-dragons-with-lemote.html

Behold:
the Guru of GNU
! (Photo by Habib Mhenni, Wikimedia Commons, CC BY-SA 3.0.)
True enlightment only comes from a truly free computing experience, probably! And while there is no nerd who lacks an opinion on Richard Stallman personally, likewise let none claim he does not practice what he preaches. Why, the very laptop in front of him was
selected deliberately
because it can operate with no binary blobs and no firmware you couldn't examine or replace with your own, and runs his choice of fully libre operating systems. The fact it has a Chinese MIPS64 derivative in it was undoubtedly just more compound on the heat spreader.
Now, in my case, the fact that it
is
a MIPS-family system meant I certainly needed one in my unusual laptop collection. And since
it can run OpenBSD
...
... it seemed like a good way to get nerdsniped in two ways by one computer: since I mostly run NetBSD as my BSD and server operating system of choice, I figured this was also a good way to learn OpenBSD on a highly portable netbook using an unusual platform. As usual, of course, the whole shooting match turned out to be a much longer journey than I'd anticipated, and my typical insistence on deviating from the beaten path (such as forcing it to run from the SD card slot and trying to build a browser from source) made it more so. But before we embark upon it, let's talk about why there's a Chinese MIPS derivative in this thing in the first place.
This is, of course, not the first MIPS laptop we've played with; a perennially popular article is on
IBM's MIPS not-a-ThinkPad
, and MIPS was also used for a couple of our Sun Ray laptops, including one
you can easily get root on
. But it
is
the first 64-bit MIPS laptop we've had here at Floodgap Orbiting HQ and certainly the smallest, and the provenance of its processor gets even more interesting. I should mention that while later chips in the series are relatively well-documented in English, its earlier entries are largely only discussed in Standard Chinese, and my ability to translate Chinese is even worse than my capacity for Japanese. These early chips are where we'll find the "why," however, so I'll do my best. Where there is disagreement between Chinese primary sources and Western secondary reporting (and there are
many
discrepancies), for obvious reasons I have generally favoured the former's accounts. Please forgive any inaccuracies that result. 谢谢.
The People's Republic of China had long prioritised indigenous technology as a means of securing independence from foreign interests, though early efforts in electronics  primarily concentrated on defense. This dramatically changed after the Chinese government realized it was being left behind by new developments in the 1980s such as the U.S. Strategic Defense Initiative, which apart from zapping nukes in the sky pumped substantial funding through the SDI Organization into basic science research, and parallel similar efforts in the Soviet Union, Japan and Europe. Paramount leader Deng Xiaoping responded with the 863 Program, named for the date of its establishment in March 1986, when it was officially proposed to the Chinese government by multiple scientists and engineers with his explicit endorsement. "The matter must be decided quickly without delay," he allegedly scribbled on the report. Officially dubbed the National High Technology Research and Development Program (国家高技术研究发展计划), the 863 Program focused on general science and technology applications in multiple domains, including biotech, space, lasers, automation, energy, new materials and information technology, with a fifteen-year timeframe. It became state policy as part of the Seventh Five-Year Plan and subsequent Five-Year Plans thereafter, and by 1988 was the country's premier industrial research and development initiative.
Despite leadership's strong interest in semiconductors, foreign processor designs nevertheless dominated in China throughout the 1990s; the lack of cutting-edge fabrication and design capacity made early industry leads insurmountable, and by the beginning of the second millenium established players like ARM and Intel held commanding market shares on the mainland as well. As a result, although more limited native microprocessor designs and clones had previously existed, a Chinese-developed CPU that was in any sense competitive with market leaders took decades to emerge. In 2001 the Institute of Computing Technology (ICT) at the Chinese Academy of Sciences (CAS) under chief architect Hu Weiwu began work on a new higher-performance chip as their own attempt, funded by the Tenth Five-Year Plan and the continuation of the 863 Program, now transformed into a long-term R&D pipeline under Jiang Zemin.
Officially called 龙芯, which would usually be transliterated in Pinyin as
Lóngxīn
and translated as "dragon core," the developers gave it the similar-sounding transliteration of
Gǒdsón
, which comes out something like "dog food"  or "food fit for dogs"  — however, I note there are many puns in Chinese, and this pasty white boy with a dictionary and a linguistics degree is probably not doing this one justice. Assuming this meaning, the intentional dysphemism likely came from the old superstition of giving bad names to children so that evil spirits would be disinclined to harm them, such that the new chip could survive its own infancy, but also fits neatly with the idea of
eating your own dog food
.
As a means of getting Godson off the ground quickly, the ICT designers evaluated existing architectures and selected 32-bit MIPS II: it was well-known and generally unencumbered, still had software support, and didn't (or at least not at first) require them to fight in the crowded x86 space. However, because it was always intended to commercialise the chip, it was important to project managers that the design yield defensible IP; as a result the MIPS
Load/Store Left/Right Word
unaligned memory access instructions, then
still under their own patent
, were thus dropped as part of the specification. Using this spec the team was then able to develop a simulator and boot Linux for the first time on August 19, 2001 (its "birthday"). The initial paper, from which the pictures above titled "Research and development of the Godson-1 general-purpose CPU chip" are taken, described "bold innovations in the microarchitecture" (their words) such as a dynamic pipeline and hardware mitigation for buffer overflows through an early form of the no-execute bit, a first for any MIPS-architecture CPU. The design progressed stepwise from Verilog simulation to a low-speed FPGA prototype, which was itself further refined for tapeout, and then into early hardware you can see at the lower right corner (a prototype logic board, chip, and minitower full system).
The resulting Godson-1 was officially launched on September 28, 2002 by BLX IC Design Corporation Ltd., a fabless joint venture between ICT and Jiangsu Zhongyi Group. It contained four million transistors on a 4mm square die, fabricated by Shanghai-based Semiconductor Manufacturing International Corporation on a 180nm process with six layers of metal; it ran its seven-stage pipeline at up to 266MHz with a power consumption of under a watt (0.4W at 200MHz) by doubling the clock signal from its custom motherboard. Carrying 8K of L1 cache each for instruction and data, it supported register renaming (but integer only from an extra set of eight), branch prediction, dynamic scheduling and out-of-order execution with a single memory access unit, two fixed-point units, and two floating-point units that supported a limited form of SIMD. Unlike SGI MIPS, Godson-1 exclusively ran little-endian, and ports of Red Hat Linux 7.1 and VXWorks were made available. The designers estimated that performance at 200MHz was comparable to a (then) five-year-old SGI O2 with a 180MHz R5000, impaired by its lack of L2 cache support, the larger node size and its relatively unsophisticated circuit design, but it really existed, it was really being manufactured, and it ran real code.
Godson-1's successful introduction naturally delighted its mainland backers and the Chinese government, though one company that
wasn't
smiling was MIPS Technologies, previously spun off in March 1998 by former owner Silicon Graphics for the embedded market. MTI's profound displeasure came from BLX billing Godson-1 as "MIPS-like," despite having no license to the ISA or authorization to use the brand, nor being directly compatible. Nevertheless, their objections didn't prevent AMD from opening a joint Beijing development centre with BLX in December 2003 to produce thin clients based on both Godson-1 and the (MIPS licensed) Alchemy Au1500, the primary chip in
our Sun Ray 2 laptops
. While Godson-1 itself saw limited use as a network computer, its GS232 core subsequently became the basis of numerous later embedded cores alongside heat-tolerant and radiation-hardened variants.
In the meantime, ICT had commenced development on a 64-bit version as early as 2002 that was more appropriate for personal computers, advancing to MIPS III with a design not unlike 1995's R10000. In a 2005 interview with
Microprocessor Reports
, chief architect Hu cited its intended purpose as a CPU for "very low-cost PC" machines affordable to most Chinese, running "high-end embedded applications and low-end desktop applications." The new Godson-2 was 4-way superscalar with out-of-order execution and a longer nine-stage pipeline for higher clock speeds, plus 64K four-way-associative I- and D-caches, a 64-entry translation lookaside buffer (up from 48), 64 GPRs and FPRs each for more effective register renaming, and external L2 cache support up to 8MB while also maintaining Godson-1's no-execute bit per page. Expanded branch prediction hardware compensated for greater pipeline latency with a 4K-entry branch history table, a 9-bit global history register, a four-entry return address stack and a 16-entry branch target buffer, but the same single memory access unit and twin integer and FPU units remained, with additional custom SIMD instructions that unfortunately conflicted with the base MIPS ISA.
Godson-2's first iteration (retroactively the Godson-2A) failed during tapeout due to issues with its register file implementation, necessitating replacement with a custom one which launched as Godson-2B in 2003. Godson-2B was fabricated by SMIC on the same 180nm process with six layers of metal, though ICT's continued (albeit lessened) use of standard cells required it to use more transistors than a more parsimonious design might have, and the 13.5 million transistor die correspondingly enlarged to 6.7mm by 6.2mm. It could run up to 500MHz using around 4W of power (2-3W at 400MHz).
Unsteady evolution followed the release of Godson-2B. Godson-2C streamlined the design further in October 2004 and reportedly ran about three times as fast, but Godson-2D's planned process shrink to 130nm developed its own crippling tapeout problems and likewise failed to enter production. As the situation had become "desperate" (in Hu's words) by 2005, the team decided to leapfrog directly to 90nm for Godson-2E to keep pace and brought in STMicroelectronics as a partner and design consultant. The new chip in March 2006 swelled to 47 million transistors on a 6.8mm by 5.2mm die, but the process shrink enabled the chip to reach 1GHz for the first time while dissipating only around 5W. Die space was conserved by removing the no-execute bit logic, and additional performance came from an on-chip 512K L2 cache and an integrated DDR memory controller.
Godson-2E's advances finally made it sufficiently suitable to power a low-cost homegrown computer just as Hu and the ICT team had planned, and in June 2006 another joint venture spinoff formed, this time between ICT and new partner Jiangsu Menglan Group: Jiangsu Lemote Tech Co., Ltd. (航天龙梦, "aerospace dragon dream"), or Lemote for short. Lemote's first computer product was the small desktop Fuloong 2E 福瓏 in October, running an STMicroelectronics-fabricated CPU at 667MHz to improve yield. It was designed to be inexpensive and go on sale quickly using otherwise off-the-shelf components, shipping with 256MB of DDR SDRAM, Realtek 8139D Ethernet, a 40 or 60GB IDE hard disk, four USB 2 ports and an ATI Radeon 7000 GPU. Notably, the Fuloong ran a Chinese-localized Linux with a modified version of the open-source PMON bootloader, which we'll talk about more shortly.
With the new product and the new company also came a new commercial brand for the chip family —
Loongson
, written with the same Chinese characters, but hewing more closely to the canonical transliteration and overtly embracing the dragon theme for common marketing. Indeed, the characters used to write Fuloong in Chinese suggest a meaning like "dragon blessing" (again, whiteboy alert, don't take anything I translate too seriously). The Godson name remained as its academic designation.
STMicroelectronics formally bought out the chip in December, investing CN¥30 million with ICT and BLX plus per-unit royalties for a five year exclusive deal. The contract terms allowed them to produce both the Loongson-2E and the forthcoming Loongson-2F, though the 2E's FPGA-based Bonito northbridge became expensive to manufacture in quantity and only the Fuloong 2E actually used the processor. The Loongson-2F solved this problem by incorporating a modified Bonito northbridge and 133MHz PCI-X controller on-die, yielding a 51 million transistor chip that ICT called the GS464 core; it was taped out for mass production on July 31, 2007. As part of an agreement between MIPS Technologies and ICT, STMicroelectronics bought a MIPS license explicitly for their Loongson parts, allowing it to be officially promoted as "MIPS-compatible" for the very first time. The company made two forms of the 2F, the early STLS2F01 and the much more common STLS2F02 with slight differences, both using the same 27x27x2.9mm heat spreader over a 416-pin flip-chip ball grid array.
Lemote wasted little time getting the 2F in shipping products, starting with an upgraded Fuloong 2F in June 2008. Using a 1GHz Loongson-2F, it came with 512MB of DDR2 SDRAM, a 120GB hard disk, four USB 2 ports, XGI V2 graphics, Realtek 8110SC Gigabit Ethernet and AMD CS5536 as southbridge providing IDE, USB and the AC'97 codec, selling at an attractive CN¥1800 (about $257 at the spot rate and a bit under $400 in 2026 dollars). At the same time, however, a much smaller system was already in development, and the low power usage of the Loongson-2F now made it plausible.
Announced in October 2008, the Lemote Yeeloong 逸珑 (something like "escaped dragon") was the first Loongson-based laptop and the front of the box even says so, reading "The world's first laptop to use a Loongson processor" on the left. Manufactured under contract by Quanta, it was intended to directly compete with the 2007 Asus Eee PC, strongly patterning itself after its popular netbook form factor and even using a 1024x600 LCD of the same size as the Eee 900 series then available. The slogan on the right, "Innovation makes [the] dragon's dream come true," appears multiple places on the packaging.
This unit was an eBay purchase, nearly complete (as far as I could tell) in the original box. The original Yeeloong came in at least two major models and multiple subconfigurations. The 8089 series, in black or white, had a 8.9" TFT 1024x600 LCD, SiliconMotion SM712 graphics with 4MB of VRAM, Realtek 8139D 10/100 Ethernet and 8187B 802.11b/g Wi-Fi, plus an SD (SDHC) card slot, speaker and microphone, audio in/out ports, VGA out, and the AMD CS5536 southbridge. These weren't fabulous creature comforts for the time, but as with the Fuloong it had to be cheap, as it was more important to its commercial backers — to say nothing of its
political
backers — that the machine should be accessible to the average Chinese buyer (and, hopefully, an international one as well).
The base model appears to have been this 8089A running an underclocked 800MHz STLS2F02 and its standard 512K of L2 cache, with two USB 2.0 ports, plus a 2GB SSD and 512MB of RAM as the label indicates; the 8089D is the same as the 8089A but with an 8GB SSD and 1GB of RAM. On the other hand, the 8089B is the deluxe-ish subconfig, adding a 160GB hard disk, a third USB port, the same 1GB of RAM and a 300Kpixel internal webcam. Confusingly they are all labeled on the bottom as "8089_C" with an underscore; only the box would tell you the actual subconfiguration. The highest-end and much rarer 8101B model uses a 10.1" TFT, but the LCD is the same resolution, and is otherwise the same loadout as the 8089B. (Although there is a later version of the Yeeloong with a different CPU, we'll get to that one at the end.)
On the box's underside is a stock photo and more marketing. The handwritten script at the top left reads something like "Simple use, exquisite form" and also appears multiple places. The bullets in the list (under another "Innovation" slogan) read, approximately:
"Loongson 2F high-performance processor"
"Mobile [and] portable, green energy-saving, sophisticated [and] elegant"
"Independently designed, immune to viruses, safe [and] worry-free"
"Open architecture, full-featured, excellent performance"
And on the bottom: "We constantly strive to make high-quality domestic products!"
Unboxing Shenzhen-style, or something.
The box also included all of the literature, including its original sales receipt and a business card for a Loongson Technology system software engineer, ICT and BLX's rather incestuous new spinoff from 2008. I don't know if he was the original purchaser or just a technical contact. The book in grey is the user's manual; the pamphlet in black is the warranty.
This unit was bought on January 11, 2009 for CN¥2110, about $309 spot price, or around $480 in 2026 dollars. However, by this time the Eee PC 900A was reportedly selling for
around $280
in 2008 dollars, so that price was not nearly as competitive as it should have been. The product name is given as BCSIL2A and was a direct purchase from Zhongke Longmeng (now renamed Aerospace Longmeng) with their sales stamp on the paper; they were a ICT licensee who developed their own Longmeng-1 SoC using a Godson-1 core.
The seller also kindly included the original battery and what looks like a NOS spare. These are off-the-shelf Simplo 916T7980F 2200mAh packs and were reputed to last around two hours and change under average usage, which for the time was acceptable (though for the record the 4400mAh battery in the Eee PC 900 could get about four). However, I don't think this was the original power supply, and pretty much any 20V laptop barrel jack brick should do. This particular unit generates 20V at 3A; the unit requires at least 2A.
One last brag about being the first Loongson laptop on the other side before we plunk it on the desk.
Its shiny surface has been a bit scuffed but still looks very nice in black, though I quibble with the metrics of the "Lemote" font. The Parker pen gives you a rough relative idea of how small it is; its footprint is less than an American letter size piece of paper (8.5"x11"), albeit about an inch (25mm) thick. On my kitchen scale it weighs 958g without its battery and 1126g with (2 lbs 1.8 oz and 2 lbs 7.7 oz), a pleasingly portable figure.
The underside of the unit indicates the model number as "8089_C," but this designation appears to be an integral part of the sticker and not secondarily silkscreened or etched. I suspect it actually refers to the bottom
case
assembly because all 8089s use the same one (proof shortly). Notice that it has FCC clearance — Lemote clearly meant to sell this in the United States if they could, though availability was limited, and most units still operating States-side (very likely this one as well) are probably imports from elsewhere. Due to some additional perforated layers between them and the logic board, the cooling vents, though prominent, actually admit much less air than they appear to. We'll get to that when we turn it on.
Removing the two screws for the bottom door gives you access to the RAM SO-DIMM (minimum DDR2-667, i.e., PC5300) and the storage bay. Both Yeeloong and Fuloong have only a single RAM slot; this unit was secondarily upgraded to 1GB of RAM, though the SSD is stock. It is allegedly possible to get up to 2GB of RAM in the Yeeloong but reports indicate it is very picky about the RAM it will accept: while it's known RAM must be single-rank for the 2F, single-rank SO-DIMMs successfully used in other related systems
haven't worked
in the Yeeloong, even though the machines should all have the same on-chip northbridge.
On the left side (oriented with the laptop lid opening away from you) is a pathetic cooling vent, the barrel power jack, the VGA out, one of the USB ports and the SD card slot.
On the other side is a nearly worthless cooling vent, Ethernet, a pop-out for where the 8089B's third port goes (i.e., it uses the same bottom case), the second USB port, and the audio jacks.
Here you can see the interior and the front-firing speakers, which are "fine." Being dark plastic and previously owned, the matte finish on the keyboard and trackpad can be seen to have worn smooth in various high-traffic places, though the amount suggests this machine did get a fair amount of use.
And that person should probably get a medal, because both are unpleasant in different ways (even considering their unavoidably small size). The trackpad is overly sensitive except when you want it to be, not helped by the generally poor state of open-source drivers, and further undermined by a scroll strip you have to be frustratingly ultradeliberate about. On the other hand, the keyboard was less mushy than I expected and actually has decent travel. Instead,
its
problem is the wacky layout, moving the tilde/backtick next to the Esc key and shifting the numbers over, plus a small spacebar and a ridiculously tiny Tab. The lights and power button at the back are actually on the logic board and shine/push through.
Plugged in and turned on yields this cheery splash screen in both English and Chinese. At least initially, the machine was impressively silent. The LCD is also better than I would have expected for a machine of this class — it's TFT, so the viewing angles are crap, but it's sharp with maybe one or two dud pixels and surprisingly serviceable otherwise. While some users have complained the backlight flickers when turned down, I've never experienced anything like that with this unit.
Holding down Del as directed drops you into the PROM, or in this case PMON, prompt. This is where we will spend some time initially, but a few minutes into me messing around with the unit, the cooling fan suddenly came on at a moderately high RPM and wouldn't stop. The side vents were unobstructed and all four rubber feet were in, so the bottom vents weren't being blocked by the table. It happened consistently enough that I was concerned something inside was blocking airflow despite other user reports of similar phenomena. We'll crack it open to check.
I don't have a service manual for this unit and I suspect I wouldn't be able to easily follow it anyway, so I very carefully disassembled the Yeeloong based on guesses I've made disassembling other laptops. The initial part to come off is the trackpad assembly. This is released by unscrewing the two door screws and removing that, then taking the other six screws out on the bottom. There are no screws under any of the labels, feet or appliques (I checked). A little nylon spudger action (not metal!) should free it, but be careful not to avulse the trackpad's ribbon connector or the microphone's wires. You don't need to disconnect them as long as you carefully get the assembly out of the way.
As with most laptops you'll have to free the keyboard next before you can do much else. Moving the trackpad assembly out of the way reveals two screws. Remove these and carefully lever the keyboard up with the spudger. Make sure you're prying up under the keyboard, not under the keyboard
tray
(we'll do that next). You can remove the keyboard from its own ribbon connector or not at your option.
I was initially stymied by the bottom case bezel until I realized it was all one part with the keyboard tray. Remove the four marked screws and then the bezel and tray can be taken out as a single piece. The bezel-tray is held in by snaps you'll need to pry free with the spudger. It extends up to the inner top quarters of the display hinges which will come off with the bezel-tray as you release it. You don't need to remove the screws in the hinges.
With the tray out, we can now see the laptop's single overworked fan and understand what's going on with the cooling system. There are no visible heat pipes and the plastic case obviously won't conduct heat well, so all cooling must be by air movement, and Lemote chose to put the CPU and most of the major hardware on the bottom of the logic board (possibly to make it more comfortable to type on). Since that would ordinarily trap heat underneath, the fan is intended to pull heated air from below and expel it on the side using the bottom vents for intake. However, the fan is small and not well suited to the task, the bottom vents don't admit much air and and only the left side vent is connected to the fan exhaust, all of which practically demands the fan run at a high RPM to be effective. As the fan race is clear and nothing is in the way, we'll just have to live with the fan whine for now, though at least it's constant and can be mentally edited out. I reassembled the laptop at this point.
To document what we're doing, it would be nice to make regular screen captures using the onboard VGA out port, which strictly mirrors the internal display. Obnoxiously it turns out my Inogeni USB capture box doesn't like 1024x600 WSVGA even though the SM712 did appear to emit a 60Hz signal, and it even confused the Samsung widescreen monitor which thought it was 1360x768 WXGA. The Hall scan converter
sort of
fixed this and was able to reformat the display into a letterboxed 4:3 rendering the Inogeni could grab, but the letterboxed portion is not centered and I couldn't fully compensate for this with phase and clock adjustments, so a bit of the right hand side gets cut off. Most of the time this fortunately isn't noticeable and thus it's what we'll use for the remainder of this article. Finally, I should also note for full transparency that a couple images have been altered to remove sensitive information and/or to clean up artifacts or misfires.
We'll start by doing some low-level digging around in PMON, its internal bootloader.
At the time there was no standardized bootloader for small MIPS-based systems (arguably there still isn't, though RedBoot did support it, and many now run modern Das U-Boot). To support the various MIPS evaluation boards available in the mid-1990s, specifically LSI Logic's but also others, longtime MIPS programmer Phil Bunce developed a simple onboard ROM-based debugging monitor he dubbed
PMON (PROM MONitor)
to manipulate memory, load and run binary objects, and debug them with breakpoints. Bunce's code was freely available and straightforward to cross-compile, and it became widely ported to many MIPS-based devices (even the
Agenda VR3 PDA
).
Lemote's fork of PMON is descended from a prior PMON fork called
PMON2000
, itself based on an even earlier fork of PMON by MIPS vendor Algorithmics UK, the developers of the Bonito northbridge. PMON2000 was built and maintained by Swedish open source consultants Opsycon AB, now defunct, who offered commercial support and porting work under contract; until it was discontinued around 2013, it directly competed with U-Boot in the early 2000s as an alternative near-universal ROM bootloader. Being a PMON descendant, PMON2000 inherited Bunce's excellent MIPS support and Algorithmics' hardware updates, making it attractive to Lemote as an available and easy-to-port option. However, their resulting implementation on the Fuloong and Yeeloong was intended purely to boot a Linux kernel, leaving or adding various other irregularities, and is consequently regarded in some quarters as poor quality.
Although Lemote didn't contribute their modifications for the Fuloong 2E port back to the PMON2000 mainline, they nevertheless published their complete source code under its original BSD license and thus attracted the notice of Richard Stallman during the Yeeloong's development. Because the STLS2F01 and STLS2F02 have no rewriteable microcode and Lemote's PMON2000 fork was open source, it is possible to bring up a Loongson-2F system to a bootloader prompt without any binary blobs, and of course much of the Fuloong's and Yeeloong's onboard hardware had libre drivers in the Linux kernel already. Stallman had previously been using a One Laptop Per Child XO-1 with its own Open Firmware-based ROM, but Nicholas Negroponte's announcement that
Windows XP was coming to the XO-1
caused him to end his public support for the project. Lemote provided him with
a prototype Yeeloong
, a machine he considered acceptable paired with a fully libre Linux rather than the custom spin it shipped with,
in his view
. Today frozen in time, the Lemote PMON2000 fork remains
preserved on Github
.
Indeed, this laptop's PMON was separately updated, but we'll look at everything it can do first. The
h
command lists out several pages of commands, some essential, most not particularly useful for general usage, and even a few that are outright buggy (the 'gui' command in particular is nearly useless).
Besides the usual debugging and memory control commands, there is also primitive networking and filesystem access. PMON is able to read an ext2 filesystem and display or load files from it.
Lemote also seems to have added specific commands for controlling the Realtek 8139 and AMD CS5536.
The version of PMON installed on this laptop is 1.4.9a, descended from PMON2000 2.1. Note the build date of August 31, 2010. The OpenBSD port to Loongson had very recently emerged by this time — it even appears in the info blurb — and I'll have more to say about that when we actually go to install it.
We can enumerate devices from PMON. A single OHCI USB root hub is visible with nothing connected to the USB ports; the keyboard and trackpad are internally PS/2. When we scan the PCI bus, we see the Realtek 8139, the SiliconMotion SM712 ...
... the multiple PCI devices provided by the AMD CS5536 southbridge, including its ISA bridge (not used), IDE (used by the SSD), AC'97 audio codec, ...
... and its USB components, the OHCI and EHCI, the USB device controller (UDC), and the USB option controller (UOC). The host controller interfaces support the two (or three) physical ports as host ports, while the UOC controls whether a fourth port is used as a host port or a device port. This would seem useful for something like a USB disk target feature, but the firmware doesn't appear to support that.
You may have noticed that the Wi-Fi and SD card reader didn't turn up on the USB
or
PCI buses, and there are also two phantom USB ports apparently unaccounted for. More about that a little later.
A set of screens more like a regular PC BIOS are available with the
main
command, suggesting they were intended to be the system's standard interface at some point, though my overall impression is that this work was unfinished. These screens are tabbed. The main tab gives the time (wrong, because it was stored with the battery out), plus the CPU and RAM statistics. The CPU is listed as "796MHz" (note from the future: this is apparently accurate; it's not quite 800MHz) with the 64K I+D caches and the 512K L2, and 1GB of RAM.
Under the boot tab you can do a manual boot from a device and path. The PMON command
devls
will give you the bootable devices, but there are by default only two:
rtl0
, i.e., the onboard Ethernet, and
wd0
, the onboard IDE. Lemote added ext2 support to PMON so it can boot a kernel from the IDE drive's filesystem, or if you have a USB stick connected when PMON starts up, it defaults to booting from that as
usb0
. (You can specify an explicit filesystem type and device with a path like
/dev/fs/ext2@wd0/filename.ext
but the shorthand generally works as-is, and although FAT is allegedly supported, it apparently doesn't work.) Interestingly, the disk option will cycle through not only
rtl0
and
wd0
but also
usb0
,
usb1
and
wd1
even though those are not currently present, and
tftp
assuming you have configured it with the IP setting or under the network tab. The Wi-Fi and SD card reader are not supported as boot targets.
The network tab lets you configure the on-board Ethernet's default IP address, but notice that other interface options are listed (however, it will not cycle through them since they are of course not present).
The advanced tab allows you to do a netboot using the on-board Ethernet, where it will pull a kernel over TFTP. Presumably this is hard-coded to
rtl0
. There is also an option here to update PMON, though the default filename is stuck at 1.4.5, which was likely the version this particular unit originally shipped with. The
,0
in
(usb0,0)
refers to the partition on that device, e.g.,
(wd0,1)
would generally be equivalent to
/dev/wd0b
. This option's path cycles through
(usb0,0)
and
(wd0,0)
as expected but also
(sata0,0)
(bogus) and
(tftp,0)
. You can also do this from the command line with something like
load -r -f bfc00000 (wd0,0)/pmon_v1.5
but make sure you get the path and address correct!
And that's all I have to say about that.
Back in PMON, here are the environment variables in flash (the
set
command).
al
,
rd
and
karg
set the autoloaded kernel path, the path to its
initrd
(if any, not specified here) and any kernel command line arguments respectively. If you remove the
al
option, then the machine will not autoboot and you can fire it up manually.
arg
doesn't appear as a variable in the PMON2000 source that I can find, and IMHO the kernel command line arguments specified here in
karg
look mostly unnecessary. However, there is also a simple GRUB-like boot menu facility and we will use that instead once we get OpenBSD installed. Many of the other options really only apply to PMON.
I mentioned that Lemote added ext2 support and you can use it to explore a storage device (but with
dir
, not
ls
). This shows the root of the IDE SSD upon arrival in the Floodgap lab. Looks like a pretty vanilla Linux install.
Let's test this installed Linux before we install OpenBSD, especially because for reasons to be discussed we'll need to make sure its contents are bootable from PMON. Here's what a full manual boot process might look like, starting with
load
ing the ELF kernel binary into memory. The ELF loader displays the sections, number of symbols and the starting address.
We can then run it with
g
, here from the determined start address, optionally passing arguments. A quick register dump appears before beginning. (PMON's
boot
command obviously handles all this automatically.)
In this case we enter Linux as left on the hard disk, which looks like an older version of stock Debian. This was
not what it originally shipped with
, which was a localized Linux spin (here a much smaller version for the smaller SSD).
Yes, the screen is now rather muddy now compared to the PMON prompt, even considering we're doing analogue grabs as opposed to direct framebuffer captures. Stand by.
As we won't get far without a password and the root password wasn't blanked out or set to something obvious, we'll use kernel arguments to force it into a shell ...
... and edit the password file.
We can now restart and log in.
Here is the complete boot sequence with kernel messages. Although some of the screen tearing is me trying to rapidly pull grabs, you can see that our screen output again became rather worse right as we entered the kernel. Just to make sure it wasn't the Hall or the Inogeni boxes, I hooked it up to my Samsung cheapie monitor and while it looked a bit better, it was quite banded and came up as 800x600. I found that odd as most likely it was directly mirroring the 1024x600 main display, and these messages indicate the same, but the interpolation suggests both the capture system and monitor thought otherwise. We'll fiddle with this shortly. Others have reported
similarly poor external VGA quality
. On the initial messages we see the PCI bus and HCIs, the PS/2 keyboard and mouse, the Silicon Motion driver and the internal ATA SSD flash getting enumerated.
We now finally see both our SD card reader and the Realtek 8187 Wi-Fi. The boot messages show they're both attached over USB internally, thus explaining our two phantom unaccounted-for USB ports; as PMON has no driver for them, they are not bootable. Since the CS5536 is limited to four USB ports total, the 8089B and 8101B have a second separate USB controller for their webcam and third physical USB port.
Bringing up the filesystems. Technically the root volume here is ext3, not ext2, but ext3 is close enough that PMON can still read and boot from it.
Here it loads a thinner font which still looks fine on the interbal LCD but now makes the console captures even harder to read.
Now we login as root.
LXDE seems an appropriate environment for this machine, but the graphics output was so bad that I ended up messing with the X11 modeline to see if I could improve it. It also really did appear to be coming up in 1024x600 given that specifying other resolutions in
xorg.conf
's
Monitor
section didn't make any difference.
Eventually I hit on
ModeLine        "1024x600@60" 52.55 1024 1064 1176 1360 600 601 604 628 -HSync +Vsync
in the
Monitor
section which still looks quite bad on the grabs, but at least restored some of the lower lines to the screen.
Likely due to the small size of the internal storage, the previous owner had only done a very minimal install of what we can now confirm was Debian 6; many pieces were missing or didn't work properly.
Still, we could see (fuzzily) that we were using a 2.6 kernel and that the CPU was detected as a "Loongson-2" on a
lemote-yeeloong-2f-8.9inches
. I noted the BogoMIPS of 522.24. How much performance could we expect from this machine?
Interestingly, "someone" (probably ICT) had already posted
a CoreMark score
of 1813.1 iterations/sec and a CoreMark/MHz of 2.2664. I suspect this was ICT/BLX themselves because it was run on an original 800MHz STLS2F01 but posted rather late in October 2010. This rating was obtained with
gcc
4.4.2 and
-march=loongson2f -O3
on Linux 2.6.32, nearly exactly the setup we have here, so I tried duplicating it myself with CoreMark 1.01 (using
gcc
4.4.5, modifying CoreMark to use the same optimization settings and selecting the best score):
CoreMark Size    : 666
Total ticks      : 16867
Total time (secs): 16.867000
Iterations/Sec   : 1778.620976
Iterations       : 30000
Compiler version : GCC4.4.5
Compiler flags   : -march=loongson2f -O3 -DPERFORMANCE_RUN=1  -lrt
That's pretty close, within about two percent, and yielding a CoreMark/MHz of 2.234. The
-march=loongson2f
does appear to be necessary for best performance; without it CoreMark reported a best score of 1652.619402, about seven percent slower.
But don't miss the forest for the trees — these are not great numbers even compared with older contemporaries. For example, my 2005 Mac mini NetBSD router, with a 1.5GHz PowerPC G4 7447A and 512K of L2, at the default
-O2
and
no
architectural optimization gets 6073.992269 and a CoreMark/MHz of 4.049. Cranked up to
-O3 -mcpu=7450
, it pulls down a score of 6544.892009 and a CoreMark/MHz of 4.363. Even considering the Yeeloong's ultra-low-end market placement, it's not a good look to be beaten so thoroughly by a low-end desktop that's three years older.
The real heck of it is when you compare to the earlier Godson-1B. At 250MHz it manages a
CoreMark of 670.36
, or a CoreMark/MHz of ... 2.6815. And the worst part is this isn't the worst part, and to get to the worst part, let's tell a bit more of the story before we try running OpenBSD.
Although the Yeeloong was the first Loongson laptop, it wasn't long before there was another. STMicroelectronics was a well-known company that had much better yield and greater fab capacity at the time than SMIC did, making the chip both cheap enough and available enough to interest other low-end OEMs, and one machine that actually reached market was the notorious
EMTEC Gdium Liberty 1000
subnotebook. EMTEC was the remnant of BASF Magnetics, BASF's magnetic tape subsidiary, which was spun off in 1991 and sold (acquiring its new name) in 1997. By 2006, after passing through multiple hands and the divestment of its tape business and related IP, it was bought by Dexxon Group, a French computer products company.
The Gdium was EMTEC's first, and eventually only, computer. It was very similar to the 8101B with its own webcam and a similar 10.1" 1024x600 LCD, but ran the STLS2F02 at 900MHz with 512MB or 1GB of RAM, used a different audio codec and a slightly later but compatible SiliconMotion SM502 with 16MB of VRAM for 1280x1024 VGA output, and instead of a hard disk it dedicated one of the three USB ports to a special "G-Key" (a USB flash drive in a unique form factor) for primary storage. The included G-Key was preloaded with G-Linux, a modified version of Mandriva Linux, and came in sizes up to 32GB.
Although slated to emerge in September 2008, possibly even beating the Yeeloong, manufacturing delays held the Gdium back until February 2009 when it was introduced at €379 ($485 at spot, or about $750 in 2026 dollars). Overly expensive to begin with, the base price States-side was quickly slashed to $399 [$620] and then $349 [$540], but reviewers soured on the frustrating trackpad, poor battery life, middling performance and startling levels of heat (measuring 112 degrees Fahrenheit on the bottom in
one review
). Perhaps its most interesting aspect was the
One Laptop Per Hacker
seed program (obviously based on One Laptop Per Child) to foster greater developer interest in MIPS and Loongson, but the idea failed as resoundingly as the computer did, and Gdium sales ended around 2010.
Another planned Loongson-2F laptop, the suspiciously-named
Jisus
(pronounced just like
that
guy?) from Dutch integrator Van Der Led, promised to run the processor at the full 1GHz but inside a smaller shell like the 8089. In fact, the system specs showed it to be a near total clone of the 8089A except for a 4GB flash drive and an even lower resolution 8.9" screen at 800x480, plus your choice of prettier cases so you can admire its colour as the heat melts the plastic before your very eyes. This wouldn't have been terrible for €299, but not days after the initial April 2008 announcement the company announced the x86-based Jisus 2 instead, and then the Jisus 3, and then
never released any of them
. In this case, this Jisus never had a
first
coming, let alone a second. I'll get my coat.
In 2008 ICT began work on the multicore Godson-3, starting with four GS464 cores on a crossbar, plus specialized instructions for faster x86 emulation; that same year, ICT and their own spin-off BLX also established Loongson Technology Corporation Limited as a public-private partnership to further commercialize the architecture. Meanwhile, ICT and MIPS Technologies finally put aside their differences completely and ICT became a direct licensee of the MIPS32 and MIPS64 architectures in 2009 (with LTC following in 2011).
These positive developments started to make the architecture attractive to other operating systems as a new modern MIPS implementation, and early work began in August 2009 on an OpenBSD port starting with the Gdium (NetBSD didn't add support for Loongson CPUs until 2012 with 6.0, and specific support for the Yeeloong with 7.0 in 2015). Unfortunately, the corners Lemote had cut with their PMON port made the booter and installer portions more complicated, and by November a new and critical problem emerged: while the systems could now install and boot, they would then repeatedly freeze, sometimes while appearing to do nothing at all.
It turns out two serious hardware bugs could trigger when the Loongson-2F incorrectly predicts a branch, though the errata initially only appeared in Chinese until a discussion explaining the issue turned up in November on the
binutils
list. Recall that MIPS processors have a delay slot after a branch, an unfortunate holdover from early implementations, which is not always but often filled with a
nop
instruction. Like all delay slots, the instruction in it is always executed whether or not the branch is taken. The canonical MIPS
nop
is
sll $0,$0,0
(shift the hardwired zero register left by zero bits), encoded as 0x00000000.
The first problem was fortunately relatively easy to work around. Loongson-2F has an eight-entry internal branch queue. A branch queue entry is generated when a branch instruction goes into the reorder queue, at most one per cycle. After the branch instruction is executed, the queue entry records the target program counter (for register jumps), the branch direction (for conditional branches), and whether the prediction was erroneous, all of which are used by its other branch prediction support hardware. When a branch is mispredicted, it is marked as "in error" and information from its queue entry is used to cancel instructions in the pipeline downstream of the faulty prediction, including any renamed registers as tracked in the physical register mapping table (PRMT). Entries are evicted from the branch queue as new branches are encountered or mispredicts occur. The bug manifests if the queue is
full
when a mispredict occurs. ICT/BLX's mitigation for this was to change how the assembler renders
nop
: instead of
sll $0,$0,0
, it uses
or $at,$at,$0
, which is practically a no-op because it logical-ORs register $at with the zero register (i.e., result is $at), and then stores that in $at. MIPS and other RISCs use the same or similar notion for register moves generally. The post notes this isn't a complete fix, but the 2F's  prediction accuracy is fairly good to begin with, and with this change the bug apparently becomes so rare as to be practically nonexistent.
The post doesn't say
why
this works, but we can — wait for it —
speculate
from the STMicroelectronics STLS2F01 user manual (which mercifully
is
written in English). When the triggering mispredict happens on a full queue, the processor might access the wrong branch queue entry and thus improperly free or fail to free allocated resources, potentially making insufficient registers available for renaming in future speculation. The processor can't recover if that happens. However, the manual implies there's something special about how the cancellation process handles the instruction in the delay slot (the sentence "Delay slot instructions should be paid special attention in branch canceling" on page 21), because this instruction must always be executed even in a mispredict. The instruction is usually
nop
, and since the canonical
nop
only references the hardwired zero register, no renaming is needed because its value is invariant. But, by replacing every canonical
nop
with
or $at,$at,$0
,
now
at least one mapping will need to be made in the PRMT, and since the delay slot is guaranteed to execute, at least one register can be recovered when this instruction is retired while unwinding the mispredict. A different instruction in the delay slot would generally behave likewise. Assuming I'm right, which is always a good assumption, that appears to be just enough to let the processor right itself in the vast majority of cases.
Such a tweak by itself would have had a negligible impact on performance, but the second flaw is more pernicious. The Loongson-2F does not cancel memory reads occurring as a consequence of a mispredict, even though it will restore any affected registers, based on the expectation the memory will likely be used later anyway and we might as well fill the cache line now. Although doing so would ordinarily be an idempotent operation, some external chipsets will act or fault on such a read, speculative or otherwise — and unfortunately one of those chips is the AMD CS5536 in the Fuloong and Yeeloong, where particular address ranges will cause it to hang. Because a speculative read can theoretically occur of any address, including addresses in the 16-entry branch target buffer, the fault can lock up any machine with vulnerable hardware.
User code is not affected by this because the faulty access will trigger a TLB miss, causing an exception and aborting the prediction. The kernel, however, is not so constrained and can crash readily, most notoriously from a poison leftover branch target buffer entry that originated in user code. The workaround (painfully) is another assembler feature to modify all jumps in the kernel and patch their destination address to avoid the poison address ranges, which, if the destination is in a register, will require inserting additional instructions to modify the target. Doing so will foul the branch prediction cache, but the kernel is also explicitly made to invalidate it anyway crossing a kernel-userland boundary, so the bug can't happen. This somewhat nauseating fix wallpapered what were occasional Linux crashes at the cost of kernel performance and is present in our Debian 6 kernel, but the OpenBSD port was much more severely afflicted to the point of unusability until
Miod Vallat discovered the errata post
.
OpenBSD 4.7 thus introduced support for Loongson-2E and -2F in November 2010, becoming the first BSD to successfully run on the Gdium, Fuloong, Yeeloong, and Lynloong all-in-one (basically a Fuloong strapped to a 1366x768 LCD). While ICT and STMicroelectronics corrected both errata for what was termed the Loongson-2G, first by fixing the branch queue problem and second by eliminating the spurious read, the -2G appears as a -2F to running software and it's currently impossible to know which one your machine has without cracking it open (which we're not going to do for this article, no offense). When OpenBSD
moved from
gcc
to
clang
due to licensing changes, similar changes
had to be made to LLVM
, delaying the migration on Loongson until December 2020. This will become relevant when we look at system performance.
Now, where will we put our second operating system? Remember I said that Lemote PMON will only boot from an ext2 (or ext3) filesystem. On the other hand, the OpenBSD booter that loads the kernel will
not
do so from a Linux filesystem because it has no disklabel. The standard way to install OpenBSD on Lemote-derived hardware, then, is to have a small ext2 partition that only contains the OpenBSD booter, and then the booter will load the OpenBSD kernel from the main partition, and Bob's your malignant spirit in Twin Peaks.
The problem we have is our pathetically small 2GB main drive and I'd like to keep the Debian that's already on it anyway for comparison purposes. That's fine; it's perfectly acceptable to boot from a USB stick, and this is also supported in Lemote PMON. But with only two USB ports on this basic 8089A (note from the future: we'll end up needing one of those ports very soon for something else) we should be able to boot from that nice internal USB card reader, which I verified does work in OpenBSD once you get the kernel up. A 32GB card would be plenty of space for anything we want to do in OpenBSD.
The trick is to not involve the booter at all — PMON is perfectly capable of loading the OpenBSD kernel directly, as long as it's on a filesystem it can access. At this point the OpenBSD fiends reading this have collapsed from apoplexy because the booter does other things like pass entropy. However, at least with current versions, we don't need those particular things to actually start the kernel; it might complain, but it will load. With that in mind, our plan is to let the install run to the SD card, which the OpenBSD installer can see, then copy the kernel to the 2GB internal drive and set the Yeeloong to boot from that. With the kernel up, we can then point the root device back to the main filesystem on the card, finish the boot, and once again Bob's your killer of Laura Palmer.
At the time I embarked upon this project OpenBSD 7.8 was still most current, so from the Linux side I put a copy of its BSD installer (which contains its own RAM disk image) in the root of the ext3 filesystem.
boot -k
is required to start this image or the installer kernel will be unable to identify the system type.
Initial messages. The CPU clock speed is indeed 796MHz. The main PCI-X devices (the Realtek 8139, SiliconMotion SM712 LynxEM+ and AMD CS5536) are enumerated.
On the USB bus, our Realtek internal card reader and the Realtek 8187B Wi-Fi are then detected via EHCI. We are ready to begin installation.
However, when I tried to actually
use
the Realtek Wi-Fi (detected as
urtw0
), we were suddenly
unready
to begin installation and got a big fat kernel panic. To see if it was the hardware in the Yeeloong or the OpenBSD driver, I dug out a TRENDNet TEW-424UB WiFi dongle which uses the same driver (detected as
urtw1
), and it crashed the same way.
I dug out a couple more dongles from the junk box, but those were also the same chipset. I was dithering over using a really long Ethernet cable until finally I found this Belkin F5D7050 "Wireless G USB Network Adapter" using a Ralink chipset (contains an RT2573 medium access controller/baseband processor and an RT2528 RF transceiver). With a little USB extender it sits nicely on top of the microSD card adapter instead of out like the proverbial sore thumb, and has an easy-to-see activity LED.
OpenBSD detects it as
rum0
...
... and successfully configured it. Aren't you glad we still have a port left over?
It is generally my practice with laptops to name them after dog names, and desktops after notable people in their development or culture. To Westerners, Richard Stallman would be the notable person most associated with the Lemote Yeeloong. However, I can find no evidence that Richard Stallman had/has a dog, or indeed any pet. So this machine will simply be named
rms
, though I did toy with naming it
godson
. There's still time to change my mind.
Now we need to format and configure the SD card, which is
sd0
. Since we've chosen this as our root device, the OpenBSD installer also believes this is our boot volume (it's not, that's
wd0
). Right now this card as shipped from the SanDisk elves is all FAT32. At the end of installation the installer will expect it to have two partitions, the OpenBSD root and a Linux ext2 boot partition, and copy the booter to the Linux partition. This is made for us if we let OpenBSD use the "whole disk," but we're going to edit the MBR to explicitly specify the size of the SD card's ext2 partition (which we don't use anyway) as extra space for wear leveling.
Conveniently we know the total number of sectors from the initial state of the card. We edit our first slice, giving it a partition ID of $a6 for OpenBSD and 90% of the sectors, then edit the second, give it a partition ID of $83 for the Linux partition, and allocate it the remainder.
We quit, writing out the new MBR, then move on to the disklabel to configure the BSD (sub)partitions. It has correctly found the ext2 partition and assigned it as
sd0i
, but I'd rather just put everything in
/
(i.e.,
sd0a
) because I'm one of
those
people.
Notice that
sd0c
, the "whole disk," actually ends where our ext2 partition begins.
We manually blow away everything but
/
and swap (and the Linux slice), then move the swap next to the Linux partition so that the root will hold the rest.
Finally, we write out the new disklabel and then proceed to getting our install packages. Since Floodgap Orbiting HQ is in sunny California, we will use
the mirror
provided by the kind folks at Sonic. I am not affiliated with them nor a subscriber, but it's nice of them to provide a mirror anyway.
The Belkin easily downloads the base installation sets ...
... and writes them out to disk.
As the last step of the installer, it will create the Linux filesystem that we will likely never use again and put the booter in it that we will likely always ignore. But don't reboot yet!
To make this boot the way
we
want to, we'll now need to manually mount
/dev/wd0i
(that is, the Linux partition on the main storage) and put the newly installed kernel there. As you can see from the screenshot, this device is not automatically created since the installer technically is unaware of its existence, and the SD card is already on
/mnt
. Using
/mnt2
as a second mount point,
cd /dev
sh MAKEDEV wd0
mount_ext2fs /dev/wd0i /mnt2
cp /mnt/bsd /mnt2
umount /mnt2
will do the copy. We then manually unmount the SD card (
umount /mnt
) and reboot.
Now we're going to boot the new kernel directly. We don't need the
-k
option for this, and you can (briefly) see that the hardware is properly autodetected.
The kernel comes up in a bigger font clearly meant for larger screens. We'll deal with this a little later.
Initial messages.
Because we kickstarted the kernel directly and not through the booter, it doesn't know where it booted from and thus what the root device is. So we tell it. Or rather, we egregiously gaslight it and point to the SD card.
Various critical components are reordered for ASLR protection upon boot from a standard installation. That step is not very fast, especially on this class of machine. Despite not having good initial entropy, it will still make our host keys and do other various first time setup tasks.
We can now log in. The root password and an unprivileged user (me) were already set up during installation.
We were instructed by the installer to read our E-mail on arrival, and here we have a message from Theo!
It's totally personally to me!
Squee! Okay. I'll save it forever.
Now, the next thing you would ordinarily do after an installation is pull down some binary packages to install the extra software you want. While OpenBSD's built-in
ftp
command is actually a pretty serviceable HTTPS client as well,
curl
is always a handy Swiss army tool to have around. The problem is, there aren't OpenBSD binary packages for
mips64el
(in fairness, this is also the case for Alpha, Luna 88K and PA-RISC). There is for
big-endian
mips64
like you'd run on an SGI, and this makes my grizzled old hacker heart glow, but not for this little black monster.
We'll have to build them from source. For this I added myself to the
wsrc
group, created the necessary directories in
/usr
, and then pulled down
the ports tree
over CVS.
Unfortunately OpenBSD's console driver for the Loongson systems does not seem to support multiple TTYs, so I put it in the background and pulled down the kernel source on another process. Pulling down the source and ports trees from CVS took the better part of a day and some of the night, but at least we now have metadata.
While I was at it, I turned off the additional startup reordering (
# rcctl disable library_aslr
), noticeably speeding up reboots, and put myself as allowed to execute
rcctl
in
/etc/doas.conf
. See, I
can
do things the OpenBSD-ish way when I
want
to.
With the kernel source downloaded, so that we can eventually have the machine autoboot OpenBSD in the normal state, we'll create a new configuration hardcoding
sd0
as the root device (
config bsd root on sd0a swap on sd0b dumps on sd0b
).
The kernel build took about two hours and 15 minutes on the wall clock, after which I copied the new BSD kernel directly over to the Linux boot partition. This is
not
the proper way to install a kernel on OpenBSD because you also need to install the pieces to reorder it, which is mandatory and
rcctl disable library_aslr
does not turn off.
make install
will do this for you, but I just wanted to see if it would work first.
And, verily, it did have the correct root device ...
... but independent of the error that the kernel could not be reordered, which I expected, there was another odd error:
ldconfig: pledge: Invalid argument
In fact, this error was occurring all over the place.
pledge(2)
is a way for a process to declare what subsystems or features it needs in advance, such that if Something Evil causes it to request a new one, the process will be righteously terminated into slag. A process can
pledge()
again and reduce its Christmas list further, but it can never increase it.
This is a core part of modern OpenBSD (introduced in 5.9) and lots of parts of the operating system use it now, so something significant had to have gone wrong with the new kernel. I contacted Miod Vallat directly, explained my predicament and invoked our good old days as posters on Nekochan, and he answered me anyway. More to the point, he was able to confirm that the stock 7.8 kernel worked, but not a newly built one off the same stable tree I was using.
After some additional investigation he found the answer in
the OpenBSD errata
, specifically
#18
. This tightens up the
pledge(2)
call to remove the
tmppath
promise, originally for the
mkstemp(3)
family of functions, now obsolete because (in Theo's words) "
it sucks
" and had been completely superseded by
unveil(2)
for requesting parts of a restricted filesystem view (introduced in 6.4). The utilities that were generating this error had already been patched in
earlier
errata
.
We already know we don't have binary packages and that also meant we didn't have binary patches, and
that
also meant I'd have to rebuild those portions of the userland too, which didn't sound like an appetising prospect (and might have other dependencies). Or, Miod suggested, I could just wait for 7.9, which was about a week away.
I decided to wait for 7.9.
***
On the day of release (May 19), I grabbed an installer kernel and got cracking immediately to minimize the possibility one of those "sorry about that" errata would land again. Keeping the old 7.8 installer, I copied it to the Linux SSD ...
... and started it. Here are the initial messages.
Actually, I figured this was a good exercise since now I'd have experience both doing a full install and then doing an in-place upgrade. On the upgrade path most of your settings, such as network interfaces, are read from your filesystem; you just have to tell it what that is.
I did try the
urtw0
adapter in the 7.9 installer and it crashed in the same way, so I should get off my butt and write a proper bug report.
Meanwhile, we then upgrade the sets (it remembered we were using Sonic) ...
... and install them. Notice how few prompts were required. Smooth.
And that's it. The Linux "boot" partition on the SD card is also invisibly updated ...
... so we make sure to do the same before we reboot the system.
Bringing up the new 7.9 kernel. Again, the hardware is properly detected without
boot -k
.
Copyrights ...
... and initial messages.
As before, we'll have to lie to it about the root device until we get our replacement kernel built.
First time startups after the upgrade.
However, I did not get a new OpenBSD 7.9 message from Theo. I will file a bug about that too.
As this was an in-place upgrade, we still have our ports and kernel trees, so we can save some bandwidth by simply updating to the new OpenBSD 7.9 tag.
It still took awhile, though.
Correct tag confirmed.
With our new kernel source, we'll hardcode the root device once again and verify no errors.
The build ran about the same length of time. Parenthetically, the
-mfix-loongson2f-btb
you see in the compiler arguments is what deals with the second mispredict erratum, which is obligatory for the kernel.
Copying over and rebooting ...
... and no errors!
Now to update the ports tree and to try a sample package.
We'll do
tcsh
so I have a proper shell. The ports build runs all the configuration tools for you and installs all necessary patches. Fortunately
tcsh
is pretty much fire and go.
Built with
make
...
... and installed as root with
make install
. Now we have a proper shell.
Since I considered the system minimally-meaningfully configured at this point, I wanted to see if I could duplicate the same performance results on OpenBSD. The result ... wasn't the same. Remember how I mentioned something about "the worst part" before? Here's the worst part.
2K performance run parameters for coremark.
CoreMark Size    : 666
Total ticks      : 15649
Total time (secs): 15.649000
Iterations/Sec   : 1278.036935
Iterations       : 20000
Compiler version : GCCOpenBSD Clang 19.1.7
Compiler flags   : -O3 -DPERFORMANCE_RUN=1
That's surprisingly bad, about 30% slower. Although Clang doesn't appear to support any special optimizations for Loongson, that certainly wouldn't explain the entire delta. CoreMark shouldn't be significantly affected by system call performance or kernel issues, so that leaves the compiler's code quality. My working theory is Clang just doesn't generate good code for Loongson compared to
gcc
(I'll defer to others if it does for MIPS64 generally), and we're going to see the consequences of that shortly.
Let's also see how it functions in X (Wayland? ha ha ha). OpenBSD's flavour of Xorg 7.7 — they're clear it's not a fork — is called
Xenocara
. I like my client systems to boot as text and then to start the window system as a second phase in case something goes awry with the graphics hardware. In the Yeeloong's case the text display is apparently also being run through the framebuffer but I'm going to run this machine the same way. We can manually start Xenocara's display manager (
xenodm
) with
rcctl -f start xenodm
from a root shell, though I forgot I already gave myself
rcctl
permissions in
doas.conf
.
This requires us to log in anew. Now that we have X up, we will use
xwd
for direct pixel perfect grabs while we're there. There is no special acceleration for the SiliconMotion SM712 or the SIMD features of the Loongson-2F.
By default OpenBSD provides
fvwm
, the F? Virtual Window Manager where F can stand for anything you like, long ago forked (one example of an F word) from the venerable
twm
. Its primary claim to fame is
its highly configurable nature
which I will doubtlessly hack on, but this is what the system provides you to start with. With no
~/.xsession
, you get vanilla
fvwm
and an
xterm
, and maybe a leftover
xconsole
from the display manager. Nine workspaces are selectable from the overview in the lower right corner.
The trackpad is as bad in OpenBSD as it is in Linux, which more likely means the trackpad sucks no matter who's trying to read it. The most irritating thing is a lot of phantom pointer motion which is really obnoxious when focus follows the pointer as it does here. My fat fingers also frequently seemed to turn what I merely intended as motion into unexpected drags.
Left click opens the root menu. There is only one standard application pre-installed in it, namely
xterm
.
Right click opens the list of windows, though the console window doesn't appear in this list even when open.
Left click in the window's close gadget opens the window-specific menu with the usual options such as moving, changing stacking order, iconifying or killing outright.
Alternatively, you can go verb-initial and pick an action by "middle click" (both buttons), then pick a window to apply it to.
There is also a scroll strip on the trackpad abutting the right button that basically functions like a set of scroll up and scroll down buttons. Once you understand this, it works largely like you'd expect as long as you're verrrry deliberate about where your finger is.
At this point you could simply quit, or even (a little more pointedly)
rcctl stop xenodm
(as root, or from
doas
).
I like this way of launching X11, even more so than the usual
startx
, so I made an alias:
alias x exec doas rcctl -f start xenodm
The last step of our basic customization is to do something about that big honking console font. The Loongson port doesn't seem to have much, if any,
wscons
support; there is no scrollback and
wsconscfg
gives me an error when I try to add a screen. That leaves (you guessed it) hardcoding the font choice in the kernel configuration, so I added
FONT_SPLEEN8x16
to the
options
and rebuilt it. Now we have the same smaller font as the installer kernel.
We have our kernel the way we want it, but we still have to manually boot it by breaking out of the boot sequence, so we should rectify that as well. Lemote PMON does have some basic provision for a boot menu, stored in
(wd0,0)/boot/boot.cfg
. The previous owner had disabled this by setting the
ShowBootMenu
variable in PMON to
no
, so we'll start by writing up a simple menu file. We'll offer three options, namely booting OpenBSD off the SD card using our customized kernel on the internal storage (the default), booting Debian 6 on the internal storage, or booting an OpenBSD installer kernel on the internal storage. Our file looks like this:
timeout 5
default 0
showmenu 1

title OpenBSD on SD
        kernel  (wd0,0)/bsd
        args    --

title Debian 6
        kernel  (wd0,0)/boot/vmlinux
        args    console=tty root=/dev/sda1 quiet

title OpenBSD on RD
        kernel  (wd0,0)/bsd.rd
        args    --
Finally,
set ShowBootMenu yes
in PMON sets the new default in flash.
On the next reboot (or
reboot
from PMON itself), our menu automatically appears, and option 0 is selected after five seconds, and our kernel boots. We also have an easy way of getting to PMON directly here instead of having to mash Delete.
But what took most of the time after that was when I "just" decided to install a web browser, and I even chose one I thought was small:
NetSurf
. That's a graphical browser lightweight enough that it should let me know if installing a heavier browser would be at all feasible on this hardware, especially given the disappointing CoreMark score. Here is the point at which I complain a little about the taste of the free beer, and for that I apologise (somewhat), so fair warning is hereby given.
Perhaps I went about it the wrong way, but I tried very hard not to build the whole thing as root. I knew there would be dependencies and I thought that the build system would be smart enough to use
doas
or something to properly install the packages for me, and it turns out I thought wrong. Maybe I should figure out
dpb
if I'm going to do this for any non-trivial package, or set something up to cross-compile, but none of those things seemed obviously necessary when I embarked on the whole affair. The magic spell was
doas pkg_add -D unsigned /usr/ports/packages/mips64el/all/package.tgz
and this would (after spuriously checking Sonic for a binary even though I just gave it one as a command line argument, which also seems like a bug) force-install the package in question.
Making it worse was the fact that all the build system requirements that wouldn't ordinarily be required for runtime (e.g.,
meson
,
ninja
, CMake) had to be compiled too, which I'm calling the "build-from-source tax." It
sucks
to pay the build-from-source tax on an underspec'ed platform. In fairness the ports system does at least use a partial GNU
configure
cache between package builds, but this didn't seem to be the case with
meson
or CMake, although they also checked for fewer things.
All of these factors caused the build time for NetSurf to balloon to
two weeks
in a herky jerky fashion where I left it to run while I was at work, or overnight, and pushed a few packages through, let it run again, came back and pushed some more, and so on, and so on, and so on. Someone tell me what I did wrong here. It feels like it shouldn't have been this arduous.
That said, I'd also like to add how amazed I was at the Yeeloong's reliability, not something I was expecting
at all
(especially considering the horror stories around the EMTEC Gdium). I didn't ever have to power it off or reboot it — that poor fan was going full kilter by the end, and the build times were agony, but it never bugged out or locked up throughout the entire ordeal. Maybe this one secretly has a Loongson-2G in it.
I was also amused by how opinionated the linker in OpenBSD is about deprecated or (in its view) dangerous functions, which was a welcome bit of levity in an otherwise drudgerous exercise. Notice in that sea of compiler options that it's building at
-O2
. I'm going to come back to this point.
In the end it was absolutely freaking remarkable how
freaking everything
is a freaking prerequisite for
freaking everything else
. For just NetSurf,
tcsh
and
xv
, these are all the packages it had to build:
rms:/usr/ports/packages/mips64el/all/% ls
adwaita-icon-theme-49.0.tgz             librsvg-2.40.21p11v0.tgz
adwaita-icon-theme-legacy-46.2p0.tgz    libsass-3.6.6v0.tgz
asciidoc-10.2.1p0.tgz                   libsndfile-1.2.2p0.tgz
at-spi2-core-2.58.5.tgz                 libsodium-1.0.22.tgz
autoconf-2.52p6.tgz                     libtextstyle-1.0.tgz
autoconf-2.67p1.tgz                     libtheora-1.2.0v0.tgz
autoconf-2.69p3.tgz                     libtool-2.4.2p3.tgz
autoconf-2.71p0.tgz                     libudev-openbsd-20230921p0.tgz
autoconf-2.72p0.tgz                     libunibreak-7.0.tgz
automake-1.15.1p1.tgz                   libusb1-1.0.29.tgz
automake-1.16.5p0.tgz                   libutf8proc-2.11.3.tgz
automake-1.18.1.tgz                     libuv-1.52.1.tgz
avahi-0.9rc4.tgz                        libvorbis-1.3.7.tgz
avahi-glib-0.9rc4.tgz                   libwapcaplet-0.4.3.tgz
avahi-libs-0.9rc4.tgz                   libwebp-1.6.0p2.tgz
bash-5.3.9.tgz                          libxkbcommon-1.13.1.tgz
bash-completion-2.17.0.tgz              libxml-2.15.3.tgz
bison-3.8.2p0.tgz                       libxslt-1.1.45.tgz
boehm-gc-8.2.12.tgz                     lynx-2.9.2p0.tgz
brotli-1.2.0.tgz                        lz4-1.10.0.tgz
bzip2-1.0.8p0.tgz                       lzo2-2.10p2.tgz
cairo-1.18.4.tgz                        m4-1.4.21.tgz
cdparanoia-3.a9.8p5.tgz                 meson-1.10.2v0.tgz
cmake-core-4.2.3.tgz                    metaauto-1.0p4.tgz
cmake-help-4.2.3.tgz                    mpg123-1.33.4.tgz
cups-2.4.19.tgz                         netsurf-3.11p2.tgz
cups-libs-2.4.19.tgz                    netsurf-buildsystem-1.10.tgz
curl-8.20.0.tgz                         nghttp2-1.68.1.tgz
dav1d-1.5.3.tgz                         nghttp3-1.15.0.tgz
dbus-1.16.2p1v0.tgz                     ngtcp2-1.22.1.tgz
dbus-daemon-launch-helper-1.16.2.tgz    ninja-1.11.1p1v1.tgz
dconf-0.40.0p2.tgz                      nsgenbind-0.9.tgz
desktop-file-utils-0.28p0.tgz           opus-1.6.1.tgz
docbook-4.5p5.tgz                       orc-0.4.42.tgz
docbook-dsssl-1.79p0.tgz                p5-Class-Inspector-1.36p0.tgz
docbook-xsl-1.79.1p0.tgz                p5-Clone-0.47.tgz
epoll-shim-0.0.20240608.tgz             p5-Encode-Locale-1.05p0.tgz
flac-1.5.0.tgz                          p5-File-ShareDir-1.118.tgz
fribidi-1.0.16p0.tgz                    p5-File-ShareDir-Install-0.14.tgz
gdbm-1.26.tgz                           p5-HTML-Parser-3.83.tgz
gdk-pixbuf-2.44.6.tgz                   p5-HTML-Tagset-3.24.tgz
gettext-runtime-1.0.tgz                 p5-HTTP-Date-6.06.tgz
gettext-tools-1.0.tgz                   p5-HTTP-Message-7.01.tgz
ggrep-3.11p0.tgz                        p5-IO-HTML-1.004.tgz
gi-docgen-2026.1.tgz                    p5-LWP-MediaTypes-6.02p0.tgz
giflib-5.2.2p0.tgz                      p5-MIME-Base32-1.303p0.tgz
glew-2.3.1.tgz                          p5-Regexp-IPv6-0.03p0.tgz
glfw-3.4p2.tgz                          p5-Time-TimeDate-2.33.tgz
glib2-2.86.5-bootstrap.tgz              p5-URI-5.34p0.tgz
glib2-2.86.5.tgz                        p5-XML-NamespaceSupport-1.12p1.tgz
glslang-16.2.0.tgz                      p5-XML-Parser-2.57.tgz
gmake-4.4.1p0.tgz                       p5-XML-SAX-1.02p0.tgz
gmp-6.3.0p0.tgz                         p5-XML-SAX-Base-1.09p0.tgz
gmpxx-6.3.0p0.tgz                       p5-XML-SAX-Expat-0.51p0.tgz
gnome-icon-theme-3.12.0p8.tgz           p5-XML-Simple-2.25p0.tgz
gnome-icon-theme-symbolic-3.12.0p6.tgz  pango-1.57.1.tgz
gnugetopt-1.1.6p2.tgz                   pcre2-10.44.tgz
gobject-introspection-1.86.0.tgz        png-1.6.58.tgz
gpatch-2.8.tgz                          py3-MarkupSafe-3.0.3p0.tgz
gperf-3.1p0.tgz                         py3-beaker-1.13.0p2.tgz
graphene-1.10.8p1.tgz                   py3-build-1.4.3.tgz
graphite2-1.3.14.tgz                    py3-cairo-1.29.0.tgz
gst-plugins-bad-1.28.2.tgz              py3-calver-2025.4.17.tgz
gst-plugins-base-1.28.2.tgz             py3-cryptodome-3.23.0.tgz
gstreamer1-1.28.2.tgz                   py3-docutils-0.22.4v0.tgz
gtest-1.15.2.tgz                        py3-editables-0.5p2.tgz
gtk+2-2.24.33p7.tgz                     py3-flit_core-3.12.0p0.tgz
gtk+2-cups-2.24.33p5.tgz                py3-gobject3-3.56.2.tgz
gtk+3-3.24.52.tgz                       py3-hatchling-1.29.0.tgz
gtk+3-cups-3.24.52.tgz                  py3-installer-1.0.0.tgz
gtk+4-4.22.3.tgz                        py3-jinja2-3.1.6p0.tgz
gtk+4-demos-4.22.3.tgz                  py3-mako-1.3.10p0.tgz
gtk4-update-icon-cache-4.22.3.tgz       py3-markdown-3.10.2p0.tgz
harfbuzz-14.1.0.tgz                     py3-more-itertools-10.8.0p0.tgz
harfbuzz-icu-14.1.0.tgz                 py3-packaging-26.0.tgz
help2man-1.49.3.tgz                     py3-pathspec-1.0.4p0.tgz
hicolor-icon-theme-0.18.tgz             py3-pluggy-1.6.0p0.tgz
highway-1.2.0.tgz                       py3-pygments-2.20.0.tgz
hubbub-0.3.8.tgz                        py3-pyproject_hooks-1.2.0p1v0.tgz
icon-naming-utils-0.8.90p1.tgz          py3-setuptools-80.9.0v0.tgz
icontool-0.1.0.tgz                      py3-setuptools_scm-9.2.2p0.tgz
icu4c-78.3v0.tgz                        py3-smartypants-2.0.2.tgz
icu4c-wwwdata-78.3v0.tgz                py3-trove-classifiers-2026.1.14.14.tgz
intltool-0.51.0p2.tgz                   py3-typogrify-2.1.0p0.tgz
iso-codes-4.20.1.tgz                    py3-wheel-0.46.3p0.tgz
iso8879-1986p1.tgz                      python-3.13.13.tgz
jasper-4.2.9.tgz                        python-gdbm-3.13.13.tgz
jpeg-3.1.4.1v0.tgz                      python-idle-3.13.13.tgz
json-glib-1.10.8p0.tgz                  python-tests-3.13.13.tgz
jsoncpp-1.9.6.tgz                       python-tkinter-3.13.13.tgz
lame-3.101pre6531.tgz                   re2c-4.4.tgz
lcms2-2.18pl20260420.tgz                rhash-1.4.6.tgz
lerc-4.1.0.tgz                          sassc-3.6.2.tgz
libarchive-3.8.7.tgz                    shaderc-2025.5p0.tgz
libass-0.17.3.tgz                       shared-mime-info-2.4p1.tgz
libatomic_ops-7.10.0.tgz                soundtouch-2.3.3.tgz
libb2-0.98.1v0.tgz                      spirv-headers-1.4.341.0v0.tgz
libbs2b-3.1.0p6.tgz                     spirv-tools-1.4.341.0v0.tgz
libcroco-0.6.13p4.tgz                   sqlite2mdoc-1.0.1.tgz
libcss-0.9.2.tgz                        sqlite3-3.51.3.tgz
libdaemon-0.14p1.tgz                    tcl-8.6.17.tgz
libdom-0.4.2.tgz                        tcsh-6.24.16.tgz
libevent-2.1.12p3.tgz                   tiff-4.7.1p2.tgz
libexif-0.6.25p0.tgz                    tk-8.6.17.tgz
libffi-3.5.2p0.tgz                      unzip-6.0p18.tgz
libiconv-1.19.tgz                       vala-0.56.19.tgz
libinput-openbsd-1.30.2p1.tgz           vim-9.2.357.tgz
libjxl-0.11.2.tgz                       vulkan-headers-1.4.341.0.tgz
libltdl-2.4.2p3.tgz                     vulkan-loader-1.4.341.0.tgz
libnettle-3.10.2.tgz                    w3m-0.5.6.tgz
libnsbmp-0.1.7.tgz                      wayland-1.24.0p2.tgz
libnsgif-1.0.0.tgz                      wayland-protocols-1.47.tgz
libnslog-0.1.3.tgz                      xdg-utils-1.2.1.tgz
libnspsl-0.1.7.tgz                      xmlto-0.0.29.tgz
libnsutils-0.1.1.tgz                    xmltoman-0.4p0.tgz
libogg-1.3.6.tgz                        xv-5.2.0.tgz
libpaper-2.2.7.tgz                      xz-5.8.3.tgz
libparserutils-0.2.5.tgz                zstd-1.5.7p0.tgz
Rather than me going Q*bert on you some more, let's just fire it up.
A big part of the build was GTK3, which is a runtime requirement (it's invoked with
netsurf-gtk3
, after all).
By default it opens a large window obviously not intended for a screen this vertically compressed.
Fortunately, the executable does accept default window geometry options, and with that we have a web browser up and running.
Now, I expected some things wouldn't work. If you don't want to use JavaScript, you can't use Google, because little computers like this don't help Google sell ads. (I am aware of the irony and/or hypocrisy of hosting this blog entry on a Google property, thanks.) Fortunately it does support DuckDuckGo, which is much nicer about that.
The computer will search for itself on the Net.
And Wikipedia does appear, a little misrendered, but legible. It was not quick about it.
It does have JavaScript support through
Duktape
, but the DOM and certain other constructs are still works in progress, so it's not enough for Google either and ended up breaking other things. Although I turned JavaScript off and left it that way, page layout and overall responsiveness were still pretty sluggish — I'll gladly exchange poor rendering for faster rendering, but I wasn't even getting that. Also, NetSurf doesn't seem to have official support for Gopher, which I personally use quite a bit and would even be appropriate on this hardware.
So let's try
Dillo
. Fortunately most of its prerequisites were of course already built, including most of them for FLTK (its toolkit). The only component that dragged things out was
wget
, which invoked a whole bunch of its own GNU-specific prerequisites. It took about a day and change to build everything.
Dillo was immediately and noticeably quicker, came up with a sane window size, and helpfully printed logging information to the terminal so I could understand what it was doing.
Its rendering is not perfect, but it's good enough for all the sites that matter.
I did the same "test" in Dillo that I did in NetSurf and got coherent search results ...
... and a legible Wikipedia page. NetSurf's rendering is clearly better, but Dillo does it significantly faster.
The other thing that has pushed Dillo into the default slot on this machine is its plugin API, for which
Gopher is available
. The plugin support is arguably Dillo's greatest strength, and I want to play with it some more, but now I can do basic browsing of my own network and services.
Still, I've used NetSurf on other constrained architectures and it shouldn't be
this
bad: that
-O2
is making what I strongly suspect is a bad compiler for this architecture even worse. Thirty percent faster wouldn't be a world of difference, but it would be
some
difference, getting me almost to the point of building
gcc
for this and hacking the ports system to use it. Either way you slice it, upgrading the ports tree on this is going to be a pain.
And that's where we're at. Actually, I've become rather fond of this machine despite the keyboard and the trackpad and the size and the slow; plus, OpenBSD has much better video output than Linux, and (if I'm patient) it can do more. I've also built Kermit,
picocom
and
minicom
to use it as a simple terminal itself, since we still have a spare USB port for a serial dongle or a hub with a couple serial dongles. It makes a more practical microserver than my HP Jornada 690 running NetBSD and I've learned a lot about OpenBSD working with it, especially as a workstation operating system. The Yeeloong 8089A may have been the
wrong
system to learn OpenBSD on, but a challenging system makes a future better-supported machine seem easier, and I might even use OpenBSD for something else now. :)
The Yeeloong got one more upgrade to the Loongson-3A as the Yeeloong 8133, a 13" laptop with four 900MHz GS464 cores as the Loongson-3A1000, plus 2GB of RAM. Few examples of these machines made it to the West, and there were only Linux builds for them; OpenBSD and NetBSD don't currently support the hardware. Attempts to expand the CPU to eight cores as the 3B1000 using enhanced GS464V cores, and then sixteen in the 3C1000, both failed during design. In 2015 LTC regrouped around the GS464E in the 3B2000 and less powerful 3A1500 (fabricated by SMIC on a 40nm process), and boosted the GS464E to 1.5GHz per core for the 3A3000 and 3B3000 in 2017. The B variants of these chips could be used in multiprocessor configurations for servers and the A variants were intended for single-CPU desktops.
The last gasp of the Loongson MIPS64 series, though not the Godson family microarchitecture, was the GS464EV in 2019 as used in the quad-core 3A4000 and 3B4000. These chips were fabricated by STMicroelectronics on a 28nm process with support for DDR4 (with ECC) and core speeds from 1.8GHz to (in the 3A4000) 2.0GHz; the 3B4000 could operate with up to seven other CPUs. Key for national defense were these chips' built-in support for the State Cryptography Administration (国家密码管理局) ShangMi-3 and ShangMi-4 cryptographic hash functions, plus an AES module and a trusted platform module. One wonders exactly what goes on in the silicon when the CPU starts keeping secrets from you, which is why I myself plan to stick to the older, better understood chips. Nothing personal.
In 2021 LTC migrated to LoongArch, their own custom RISC ISA, using aspects of Godson and similar core designs (the LA464 in particular was nearly identical to the previously-aborted GS464V) against an instruction set clearly inspired by MIPS but incompatible with it. The 3A5000 in particular is being used in Chinese computers today in the tens of thousands, and the 3A6000 was fabricated on a 14nm process size, with 7nm expected in the near future. We will likely not see these machines States-side anytime soon; in 2023, under the Biden administration, the U.S. Department of Commerce added LTC to the Bureau of Industry and Security's Entity List for acquisition of American technology in support of the People's Liberation Army.
As for RMS, he upgraded
to something else
(photo credit), but it seems he enjoyed it while he used it, and I'm sure he'd
sing a song
to you about it.
