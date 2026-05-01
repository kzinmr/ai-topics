---
title: "A real PowerBook: the Macintosh Application Environment on a PA-RISC laptop"
url: "https://oldvcr.blogspot.com/2025/08/a-real-powerbook-macintosh-application.html"
fetched_at: 2026-05-01T07:01:28.449734+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# A real PowerBook: the Macintosh Application Environment on a PA-RISC laptop

Source: https://oldvcr.blogspot.com/2025/08/a-real-powerbook-macintosh-application.html

I like the Power ISA very much, but there's nothing architecturally obvious to say that the next natural step from the Motorola 68000 family must be to PowerPC. For example, the Palm OS
moved from the DragonBall to ARM
, and it's not necessarily a well-known fact that the successor to Commodore's 68K Amigas was intended to be based on PA-RISC, Hewlett-Packard's "Precision Architecture" processor family. (That was
the Hombre chipset
, and
prototype chips existed
prior to Commodore's demise in 1994, though controversy swirled regarding backwards compatibility.) Sure, Apple and Motorola were two-thirds of the AIM alliance, and there were several PowerPC PowerBooks available when the fall of 1997 rolled around. But what if the next PowerBooks had been based on PA-RISC instead?
Well, no need to strain yourself imagining it. Here's nearly as close as you're gonna get.
In October 1997 you could have bought a PowerBook 3400c running up to a 240MHz PowerPC 603e for $6500 [about $13,000 in 2025 dollars], which was briefly billed as the world's fastest laptop, or you could have bought this monster new to the market, the RDI PrecisionBook running up to a 160MHz (later 180MHz) PA-7300LC starting at $12,000 [$24,000]. Both provided onboard Ethernet, SCSI and CardBus PCMCIA slots. On the other hand, while the 3400c had an internal media bay for either a floppy or CD-ROM, both external options on the PrecisionBook, the PrecisionBook gave you a 1024x768 LCD (versus 800x600 on the 3400c), a bigger keyboard, at least two 2.5" hard disk bays and up to 512MB of RAM (versus 144MB) — and HP-UX.
And, through the magic of Apple's official Macintosh Application Environment, you could do anything on it an HP PA-RISC workstation could do and run 68K Mac software on it at the same time. Look at the photograph and see: on our 160MHz unit we've got HP-UX 11.00 CDE running simultaneously with a full Macintosh System 7.5.3 desktop. Yes, only a real Power Mac could run PowerPC software back then, but 68K software was still plentiful and functional. Might this have been a viable option to have your expensive cake and eat it too? We'll find out and run some real apps on it (including
that
game we must all try running), analyze its performance and technical underpinnings, and uncover an unusual artifact of its history hidden in the executable.
(A shout-out to Paul Weissman, the author and maintainer of the incomparable PA-RISC resource
OpenPA.net
, who provided helpful insights for this article.)
In this entry the hardware is at least as unusual as the software we'll be running on it, so let's start with the story of the hardware since it's a bit shorter. Yet another computer manufacturer
near my childhood hometown
, RDI Computer Systems was founded in 1989 as Research, Development and Innovations Incorporated in La Costa, California, a neighbourhood of Carlsbad annexed in 1972 in northern San Diego county. (It is completely unrelated to earlier Carlsbad company RDI
Video
Systems, short for "Rick Dyer Industries" and the developers of laserdisc games like
Dragon's Lair
and
Space Ace
, who folded in 1985 after their expensive Halcyon home console imploded mid-development from the 1983 video game crash.)
RDI, like several of its contemporaries, was established to capitalize on Sun Microsystems' attempt to commoditize SPARC and open up the market to other OEMs. While most such vendors like
Solbourne Computer
heavily invested in the desktop workstation segment, RDI instead went even smaller, producing what would become the first SPARC laptops in the United States. Basically SPARCstation IPC and IPX systems crammed into boxy off-white portable cases, the BriteLite series weighed a bit over 13 pounds and started at $10,000 [$24,600]. They were lauded for their performance and compatibility but not their battery life, and RDI became an early adopter of Sun's lower-power microSPARC for the sleeker, sexier PowerLites, using a more dramatic jet-black case. An 85MHz microSPARC II PowerLite 85 was the machine that computational physicist Tsutomu Shimomura, then at the San Diego Supercomputer Center, used to track down hacker Kevin Mitnick in 1995.
RDI's initial success enabled its expansion into a bigger 40,000-square foot industrial park facility at 2300 Faraday Avenue, which apparently still exists today. Unfortunately for the company, however, microSPARC hit a performance wall above 125MHz and Sun abandoned further development in 1994, which RDI management took as an indication they needed to diversify. By then the RISC market had started to flourish with many architectures competing for dominance, and RDI decided to throw in with Hewlett-Packard's PA-RISC which had extant portable systems already from Hitachi
and SAIC
. Neither of those systems had ever existed in large numbers (and the SAIC Galaxys only in military applications at that), giving RDI a new market opportunity with a respected architecture that was already mobile-capable. Producing a final PowerLite in 1996 with the 170MHz Fujitsu TurboSPARC, RDI expanded the PowerLite case substantially for their next systems, replacing the trackball with a touchpad and adding an icon-based LCD status display but keeping its multiple hard disk bays and port options. In the same way the original BriteLites were SPARCstations in every other respect, the new RDI PA-RISC laptop was an otherwise standard HP Visualize B132L or B160L workstation, just inside a laptop case.
And thus was the PrecisionBook introduced in October 1997 along with the UltraBook, the first of their new SPARC laptop line based on Sun's original 200MHz UltraSPARC using the same case as the PrecisionBook. These two systems, made siblings through their common chassis, were branded by RDI as "MobileStations."
This particular system you've already met
in our demonstration of Hyper-G
, which I've christened
ruby
after HP chief architect
Ruby B. Lee
, a key designer of the PA-RISC architecture and its first single-chip implementation. This time around, however, we'll take a closer look at
ruby
's hardware as a comparison point since it will inform some of the choices we'll make running the Macintosh Application Environment.
So that I can save some typing, I'm going to liberally abbreviate "PrecisionBook" to "PABook" for the remainder of this article (avoiding "PBook" so we don't confuse it with PowerBooks).
This particular 160MHz machine wasn't what would become the top of the line unit — some early press materials teased a 167MHz or 200MHz CPU, but eventually the last unit was 180MHz — but it did originally ship with the high-end spec 256MB of RAM; the second module was added later for a full 512MB. Memory modules are installed through a door on the bottom with a bizarre form factor unique to the PABook. The modules are 60ns ECC and up to 256MB in size; both modules here are the largest supported. A single module is allowed, though if two modules are installed, they must match.
Visible in this view are two ejectable bays on the right and one on the left (in this orientation), which we'll discuss when we look at the unit from the side.
Here's the machine booted up waiting at the HP-UX Common Desktop Environment (CDE) login prompt. While RDI mentions 12" displays in the technical manual, I've personally only seen the 14" TFT active matrix LCD presented here, and both are the same 1024x768 resolution. It has a bit of scuffing on the extreme right and has slipped a bit in its moorings, but the backlight is still good and the screen remains sharp and vivid. Being the same as the B160L, right down to self-identifying as the same model 9000/778, the PrecisionBook also comes with the same on-board HP Visualize-EG graphics chipset (more about the graphics shortly).
The MobileStation case offered a full keyboard for most keys with the remainder moved to a reduced-size upper block. Both machines use the same trackpad and keyboard layout, but only some of the upper keys are defined (or even labeled) on the PABook, while the full set is defined on the UltraBook and its successors.
Another, er, key advance introduced with the MobileStation case is its status LCD panel, which is active even with main power off. The status LCD includes not only indicators for caps lock and shift lock, but also for general system operation. Six indicators are shown here with the system in a relatively idle state, described top to bottom, left to right: the current charge of the battery, A/C power detected, system powered on, operating system "heartbeat," audio enabled, and external video enabled. (The video indicator shows when external graphics have been enabled from the boot menu regardless of whether anything is actually connected.) Other indicators that can appear here include hard drive, CD-ROM or floppy disk activity, network activity, an overtemperature warning, or if reduced "economy mode" power usage is enabled.
While RDI's battery life had come a long way from the BriteLites, you were nevertheless still dealing with CPUs and chipsets that weren't monsters but weren't exactly thrifty either. Its standard LiIon battery is only 40 watt-hours with an estimated runtime of at most two hours, and that was
RDI
's estimate. I haven't bothered trying to recell this one, and although the status LCD claims it's fully charged, it currently lasts maybe a minute or so which is enough to ride out a AC voltage drop and not much else.
Another edge the PowerBooks definitely had over the PABook (and, for that matter, the UltraBook) is noise. Two fans keep the system and installed hard disks cool. They don't run particularly hot, but this unit only has one disk and isn't the fastest CPU available, and they can be a bit loud.
There are, however, plenty of ports and the MobileStations could both be docked to a "Peripheral Expansion Module" for even more features by using the large rear connector. These expansion units are uncommon and I've never seen one personally, and some of the icons on the status LCD (like the CD-ROM) are activated only by devices installed in this chassis. The power connector is a non-standard 5-pin barrel jack on this early unit carrying two +18V lines and returns, plus an indicator line for AC failure, though later machines reportedly used a regular +19V laptop jack. The other non-standard port, a bit hidden by the Ethernet, is a connector for a breakout box providing an AUI port, two serial ports and a parallel port, but I don't have this breakout unit either. Otherwise, the remainder are PS/2 ports for the keyboard and mouse, a DE-15 VGA port and a jack for 10BaseT Ethernet. Connecting to these ports doesn't necessarily disable the internal devices; it will accept input from both the built-in and an external keyboard simultaneously, for example. Irritatingly the rear port door had snapped off before I purchased this unit.
The PABook uses Visualize-EG graphics connected to the core GSC (General System Connect) bus via HP's LASI chipset, but only one instance of the Visualize-EG is present, meaning it's not possible to dual-head this machine (unlike the SAIC Galaxy family which effectively has two HP Artists, one each for the internal and external displays). Although this chipset has no 3-D capability, HP-UX supports it for 2-D acceleration and it was considered to have good performance for the time. RDI provided a base 2MB framebuffer and advertised an additional 2MB option for more resolutions; this upgrade is installed in this machine and later spec sheets conflict on whether it came standard. While the LCD panel is perfectly capable of 24-bit colour, the standard visual is limited to 8-bit colour depth/256 colours, using HP Color Recovery for a pseudo-24-bit visual in those applications that support it. The built-in LCD natively displays 1024x768 at 62Hz (not 60Hz) which my capture boxes don't like when mirrored through the VGA port. It is also possible to drive the standard 2MB video up to 1280x1024 or all the way down to 640x480, but the built-in LCD is automatically disabled for any resolution other than 1024x768. If the extra 2MB VRAM is present, as it is here, resolutions up to 1600x1200 are supported. The display resolution can only be configured through the boot monitor.
On the left side (as you look at the keyboard) are the hard disk bays. These hard disks are notionally 2.5" SCSI but stocks of them got scarce, so this unit, as well as most later units, actually has a 2.5" IDE drive with an ADTX IDE-to-SCSI converter instead. This unit shipped with a single 4GB hard disk, the baseline configuration, which in later models was upgraded to 6GB.
On the right is the battery bay (under the audio jacks, supporting 16-bit stereo up to 44.1kHz), which can be equipped to take a third disk instead, and this unit is able to even though the battery is there. The third disk capability was an option in early models and later became standard.
Next to the battery are two I/O doors. The first door contains the PCMCIA slots, which also support CardBus through a GSC-to-PCI bridge even though this isn't mentioned many places. It can accept up to two Type I/II cards or one Type III. Officially the PCMCIA slots were only supported for an optional 56K fax/modem (an OEMed Clippercom 56K Data/Fax), an unspecified wireless modem (not Wi-Fi), and a 10/100BaseT Ethernet upgrade (D-Link DFE-650TX). Under that is a small 15-pin connector for the optional external 3.5" floppy drive which I don't have either, and behind the other door is the external micro 50-pin SCSI-2 port. A diagram sheet shows that an IR transceiver was planned to be next to the SCSI port, but I don't see one on mine.
I took some grabs of the boot process before starting the operating system using a different video mode that my Inogeni VGA capture box would tolerate (my
Hall scan converter
didn't like it either), though this turned the LCD off, so we won't be bringing up the operating system in this configuration. There is no separate service processor; this all runs on the main CPU.
Main screen turn on. Main screen can also changed for great justice by press TAB key.
After timing out (or pressing some other key), the basic POST result appears with the CPU information, RAM test and boot "paths." The PA-7300LC is the next step up from the "low end" consumer-focused PA-7100LC in the "Gecko" 9000/712 and the
SAIC Galaxy family
, and the last and fastest-clocked of the 32-bit PA-RISC 1.1 chips (though the earlier PA-7150 and PA-7200 with their comparatively massive caches can easily beat the 132MHz part). Being effectively a hopped-up PA-7100LC, it inherits most of the characteristics of the earlier chip including a two-way superscalar design, bi-endian support, two asymmetric ALUs, a slightly gimped FPU (the "coprocessor" in the POST summary) with greater double precision latency, and MAX-1 multimedia SIMD instructions. It also incorporates the GSC bus controller on-board.
Where the PA-7300LC exceeds its ancestor is in its faster clock speeds — from 132 to 180MHz versus 60 to 100MHz — on a slightly longer six-stage pipeline instead of five, and much larger 64K/64K L1 caches (versus just 1K of I-cache) that were on-die for the first time. In keeping with its "consumer" roots the PA-7300LC additionally includes an L2 cache controller like the PA-7100LC, but here as shown on-screen the PABook's L2 is a full megabyte, and up to 8MB was supported. This is particularly notable given L2 cache was rarely a feature with PA-RISC — large L1s were more typical — and it would not be seen again on a PA-RISC CPU until the PA-8800 seven years later. Other improvements include a 96-entry unified translation lookaside buffer (versus 64) and a four-entry instruction lookaside buffer (versus one) specifically for instruction addresses, which also supported prefetching. The die was fabbed by HP on a 0.5μm process with 9.2 million transistors, 8 million of which were for the L1 cache which consumed most of its 260 square millimetres. A velociraptor can famously be seen in
die photos
.
And here the PowerBook 3400c has a run for its money. This is the point at which I get conflicted because I'm a big fan of the Power ISA, yet I have a real soft spot for PA-RISC because it was
my first job out of college
, so this is like trying to pick which of my "children" I like best. Although the 3400c with a 240MHz PowerPC 603e was briefly the "world's fastest laptop," at least according to Apple, on benchmarks this 160MHz PA-7300LC wins handily. The last generation 300MHz 603e got SPEC95 numbers of
7.4/6.1
, while the 180MHz PA-7300LC recorded scores of
9.22/9.43
, with 9.06/9.35 officially recorded for the 180MHz PABook. If we linearly adjust both figures for clock speed we get 5.92/4.88 versus 8.20/8.38, and even using the lower figures in the PABook's technical manual (7.78/7.39 at 160MHz and 6.49/6.54 at 132MHz) the PABook still triumphs. While this isn't a completely fair fight due to the 603's notoriously underpowered FPU, clock for clock the PA-7300LC could challenge both the Pentium Pro and the piledriver PowerPC 604e; the Alpha 21164 could only beat it by revving to 300MHz. And I say all this as a pro-PowerPC bigot!
Processing power isn't everything, of course: the 160MHz PA-7300LC does this with a TDP of 15W, while the 300MHz 603e displaces just four to six watts, and the 240MHz part (fabbed on the same 290nm process) is on the lower end of that range. In real world terms that translated to battery life that was at least twice as long on the 3400c.
The PABook normally boots from the drive bay closest to the rear (SCSI ID 0; the others are 1 and 2) and the 4GB drive as shipped is in that position, but it can also boot from an external device (SCSI ID 3 or higher) if necessary. The console path is virtually always
GRAPHICS(0)
for the on-board Visualize-EG and the keyboard path is likewise PS/2, but this can apply to both an external keyboard or the built-in keyboard, which is internally connected the same way.
Halting at the boot menu to show the loadout. Parenthetically, you'd change the resolution under
COnfiguration
, with the
RDI
commands for RDI-specific features like mirroring the LCD, but here we'll be asking for
INformation
on what's installed.
Specifications on the processor, as well as the 40MHz GSC bus speed. On the 132MHz PABook the bus speed is 33MHz.
Coprocessor, cache and memory status. I'm not sure how the memory system works exactly and it may be artifactual, but all the RAM this system contains you saw on the underside of the unit with the door off; there is nothing soldered to the logic board. It looks like only three of those 128MB aliquots are treated as "expansion RAM" despite each card having two such aliquots each.
The list of onboard devices. The PA-7300LC itself is numbered #62. It is directly connected to the RAM via its on-board Memory, I/O and Cache (MIOC) controller, numbered #63, and then to the GSC bus with its own on-board controller numbered #8 (listed as a "Bus Converter" both here and in HP's PA-7300LC SoC whitepaper), which everything else ultimately hangs off. The Visualize-EG graphics chipset, listed as
INTERNAL_EG_X800
, is directly connected to the GSC, but most of the rear ports are connected to a "Bus Adapter." This is the HP LASI ("LAN SCSI") combo chip updated for the PA-7300LC, implementing an Intel i82C596CA 10Mbit NIC, NCR 53C710 SCSI-2 controller, a 16550 UART for RS-232, a WD16C522-compatible parallel port, PS/2 controllers, floppy drive controller and HP Harmony audio. Not enumerated here, a secondary low-speed bus from the LASI called the PHD bus connects to its 1MB flash boot memory, NVRAM and power supply controller. The LASI only supports one serial port, so a second UART is attached to a "Bus Bridge" to provide the second one. This "Bus Bridge" is Dino, a GSC-to-PCI bridge.
Dino has its own bus which is listed separately. In addition to implementing the two CardBus-ready slots, Dino also apparently supports an on-board IDE controller completely unmentioned by any of the PABook technical documentation I have access to. This is different from the IDE-as-SCSI hard disks because those would still look like SCSI drives to the computer and they would still be connected to the SCSI bus. I can't find any obvious physical interface for this phantom IDE controller (perhaps it's part of the expansion chassis I don't have), yet the system nonetheless insists it's there. Below the "Dino bus" list is the boot information, boot paths, MAC address and a completely bogus date and time.
Finally, firmware and hardware revisions. If you are
mikec
, I'd like to ask about your experiences with the hardware: please say hi in the comments or drop me a line at ckaiser at floodgap dawt com.
Bringing up the system in its standard (incompatible) video mode, so I'll just switch to photographs here. The ADTX AXSITS2532R is the IDE-to-SCSI converter in this unit. Once the unit is identified as bootable, the HP Initial System Loader starts up and automatically boots the HP-UX kernel; the ISL can also be started in manual mode for recovery purposes from the boot menu.
This PABook runs HP-UX 11.00, the last version officially supported by the manufacturer, though the PABooks initially shipped with 10.20 and a power management utility was also provided. The choice of OS will become relevant to our specific task shortly. HP-UX 11i v1 (11.11) will run on this machine through at least 12/04, but not any later version, as that was the last release compatible with the B132L/B160L (and 11i v1 the last to support 32-bit PA-RISC generally). The B180L and thus the 180MHz PABook will run up to 12/05. Fortunately, all are well-supported by NetBSD and OpenBSD, though not NeXTSTEP.
Going through the HP-UX startup sequence.
Now at the CDE login prompt, we can move on to the task at hand: making it into a big honking Macintosh. And that brings us to the Macintosh Application Environment, or the software story. Apple did a lot of weird things in the 1990s and potentially cannibalizing their own hardware sales by releasing an official emulator was only moderately odd by comparison. But the more interesting thing about the Macintosh Application Environment was where it came from originally: A/UX.
A/UX was Apple's first Unix, originally introduced in 1988 as a port of System V Release 2.2 and later incorporating features from BSD 4.x. Initially it could run text and X11R3 programs, but more relevantly it could also run well-behaved Macintosh System 6 applications using a modified Finder and operating system that ran as an A/UX process. In 1991, in the wake of the newly formed AIM alliance between IBM, Apple and Motorola, Apple and IBM announced that A/UX "4.0" along with IBM's AIX and the successor to System 7 would all become personalities over a new unified operating system for the forthcoming PowerPC, internally called PowerOpen. As an interim step A/UX's Macintosh compatibility layer was updated to System 7.0.1 and shipped as A/UX 3.0.
By 1994 this strategy was unraveling. Pink, the intended successor to System 7, had metastasized into sundry Taligent spins and the doomed Copland, all of which were slowly succumbing to various terminal stages of life support. Apple's rush to market with their new hardware had fractured IBM's attempts to build a PowerPC platform standard (PrEP), and the situation so greatly irked IBM that they released AIX 4 on their own in February prior to the new Power Macintoshes — which couldn't run it or anything else other than System 7.1.2 — coming out in March.
Nevertheless, development on the PowerOpen-based A/UX 4.0 continued to plod along in parallel, which would still run existing 68K Mac applications but this time as a PowerOpen compatibility layer on top of a dissimilar alien architecture (i.e., PowerPC). New PowerPC software would be PowerOpen-native; the compatibility layer would exist solely to run previously written programs under emulation. Now, does this sound a little like what we're planning to do? (We'll show an artifact of its lineage still buried in the MAE executable at the end.)
Although Apple CEO Michael Spindler was firmly committed to the PowerPC transition (even cancelling Star Trek, Apple's first attempt to jump to x86, as a potential threat), Apple's finances were shaky and Spindler liked to hedge his bets. It was by no means a foregone conclusion that the new Power Macs would revitalize Apple. Indeed, Spindler was already considering ways System 7 could be licensed to other computer makers to raise cash and the A/UX 4.0 compatibility layer presented a new means to transplant the Macintosh ecosystem onto an alternative platform using code and resources that Apple fully controlled. While A/UX 4.0 as a whole was nowhere near a full release, this specific component of it, being built on existing and working code from A/UX 3.0, was sufficiently far along that it could be a product all by itself.
With the confetti from the Power Macintosh launch still on the carpet, Apple announced shortly afterwards that it would also support running Macintosh applications on Sun Microsystems' Solaris and Hewlett-Packard's HP-UX 9.x, recompiling the compatibility layer for SPARC and PA-RISC, yet otherwise sharing as much code as possible between the two platforms and the future A/UX 4.0. This was the first release of the Macintosh Application Environment (MAE), internally codenamed as "Cat-in-the-Hat," retailing for $549 [$1190 in 2025 dollars] and running System 7.1. The lack of AIX in the announcement was considered highly conspicuous to industry observers, but rather than releasing the A/UX 4.0 components as written for AIX, Apple and IBM announced instead that new PowerPC-native Macintosh applications would run
directly
on AIX — which also used the same PowerOpen ABI — through a thinner runtime layer called Macintosh Application Services (MAS) exclusively for IBM's operating system.
In the meantime, MAE 2.0, a substantial upgrade, emerged in March 1995 for $599 [$1320]. The core OS was upgraded to System 7.5 and now offered sound, cut-and-paste between X11 and the Mac, dynamic recompilation for faster emulated applications, and networking support over AppleTalk and MacTCP. MAE 2.0's updated 68K emulator core was likely derived from Eric Traut's new DR Emulator intended for the upcoming PCI Power Macs, but dynamic recompilation came to MAE first, months before the Power Macintosh 9500 started shipping it in June.
Unlike MAE, however, MAS was floundering. Since it was "only" a ported Toolbox and system components using the same instruction set and ABI, MAS should have been an easy win on AIX, but Apple could not financially sustain its development and cancelled it at the same time. It was also unclear how 68K applications would execute in a MAS world and IBM and Apple couldn't even agree on who would pay for a simple backport of MAE. In the end AIX never ran either one, and
only one Apple computer
ever ran AIX.
In May 1996 Apple updated MAE to version 3.0 with System 7.5.3. This release added compatibility with HP-UX 10.x and made the CPU emulation even faster, primarily through improved handling of condition codes and floating point instructions. It also touted better application compatibility and faster screen updates for users running MAE over a remote X11 session. MAE 3.0 received four point updates up to 3.0.4, badged as "Version 3.0 (Update 4)," which is the final release and the version we'll use.
At this point we'll switch over to getting screen grabs directly from the framebuffer with
xwd
. The installation process is with a shell script and binary installer, both running from within a CDE shell window. Apple offered a trial version so that people could test their software and unlocking the trial limitations requires a license key which you may or may not be able to find on any Archive on the Internet. I won't show the installation process here since it's not particularly interesting or customizeable, but ideally it should be installed to
/opt/apple
, and even though this version of MAE includes it we're not going to install AppleTalk:
The AppleTalk drivers are kernel modules and only supported on HP-UX 9.x and 10.x (and Solaris). The 9.x and 10.x stacks are based on related code but pre-compiled for the specific kernel and then linked into it by the installer. There are significant differences between the 10.x and 11.00 kernel, so even if it linked and booted — which isn't guaranteed — I suspect it has a good chance of simply not working. If you try it, let me know, but with a solid pre-installation probability of failure, I didn't feel like trying to pick out all the pieces to undo it afterwards. We've got other ways of getting software onto the system in any case.
Once the installation is complete, we simply execute
./mae
in
/opt/apple/bin
. The very first run requires us to accept the EULA; there is a specific binary for this and we'll look at it when we take the code apart a bit.
After that the System Folder is created, interestingly with a text prompt ...
... and the emulated Mac starts, using this copyright screen instead of a Happy Mac. It also makes a Quadra-era bong.
Welcome to Macintosh.
Loading extensions.
Another thing that occurs on first run is rebuilding the desktop ... for
/opt
? Hang on and we'll get to the on-disk representation.
Now at the Finder. We have two volumes mounted, our home directory and
/opt
. Again, explanations presently.
About This Macintosh, showing the default configuration with 16MB of RAM on System Software 7.5.3 with "MAE Enabler 3.0 Update 4." (MAE 2.0 and earlier defaulted to 8MB memory.) The emulated Mac's name is given as, quite reasonably, the Macintosh Application Environment.
Let's shut down (shut it down like you would any regular Mac from Special, Shut Down) and look at what's now in our home directory.
ruby:/home/spectre/% ls
System Folder  bin            src            uploads
ruby:/home/spectre/% ls -l System\ Folder/
total 1650
drwxr-xr-x   2 spectre    users         1024 Jul 23 21:23 Apple Menu Items
-rw-r--r--   1 spectre    users         2846 Jul 23 21:23 Clipboard
drwxr-xr-x   2 spectre    users         1024 Jul 23 21:23 Control Panels
drwxr-xr-x   2 spectre    users         1024 Jul 23 21:23 Control Strip Modules
drwxr-xr-x   3 spectre    users         1024 Jul 23 21:23 Extensions
-rw-r--r--   1 spectre    users        35921 Jul 23 21:23 Finder
drwxr-xr-x   2 spectre    users         1024 Jul 23 21:23 Fonts
-rw-r--r--   1 spectre    users       152162 Jul 23 21:23 MAE Enabler
-rw-rw-r--   1 spectre    users        18952 Jul 23 21:24 MacTCP DNR
drwxr-xr-x   3 spectre    users         1024 Jul 23 23:04 Preferences
-rw-r--r--   1 spectre    users        72200 Jul 23 21:23 Scrapbook File
drwxrwxr-x   2 spectre    users           96 Jul 23 21:24 Shutdown Items
drwxrwxr-x   2 spectre    users           96 Jul 23 21:24 Startup Items
-rw-r--r--   1 spectre    users       553762 Jul 23 23:59 System
The System Folder that MAE created on first run is actually a folder in our home directory. It looks otherwise like an ordinary System Folder, so how can it contain Mac resource forks (and most importantly
CODE
resources) on a native HP-UX Veritas filesystem? The answer is that these files are all AppleSingle, which is to say with their resource and data forks combined, and MAE reads and writes AppleSingle on the fly.
There is another interesting folder that gets created.
ruby:/home/spectre/% cd .mac
ruby:/home/spectre/.mac/% ls
ruby
ruby:/home/spectre/.mac/% cd ruby/
ruby:/home/spectre/.mac/ruby/% ls
222836       224386       3536437      FileIDs      sm.vpram
223119       224418       47           LinkAliases
224064       261985237    57321540     MIVAliases
This directory is effectively where the virtual Mac lives. It contains the contents of the virtual Mac's "PRAM" (
sm.vpram
) plus various databases for files and aliases.
The numbered directories require specific explanation. Since each Macintosh volume is its own root, which is certainly not the case in Unix, this directory collects the virtual Mac's volumes here. These aren't symbolic links elsewhere in the filesystem; these are MIVs, or MAE Independent Volumes. They correlate with all the mount points in
/etc/fstab
by default but any directory can be designated as an MIV, "mounted," and then treated as a volume.
ruby:/home/spectre/.mac/ruby/% cat /etc/fstab
# System /etc/fstab file.  Static information about the file systems
# See fstab(4) and sam(1M) for further details on configuring devices.
/dev/vg00/lvol3 / vxfs delaylog 0 1
/dev/vg00/lvol1 /stand hfs defaults 0 1
/dev/vg00/lvol4 /tmp vxfs delaylog 0 2
/dev/vg00/lvol5 /home vxfs delaylog 0 2
/dev/vg00/lvol6 /opt vxfs delaylog 0 2
/dev/vg00/lvol7 /usr vxfs delaylog 0 2
/dev/vg00/lvol8 /var vxfs delaylog 0 2
/dev/vg00/lvol11 /pro vxfs delaylog 0 2
ruby:/home/spectre/.mac/ruby/% ls -lR [2345]*

222836:
total 2
drwxrwx---   4 spectre    users         1024 Jul 23 23:59 opt

222836/opt:
total 810
-rw-rw----   1 spectre    users          294 Jul 23 21:33 %Desktop DB
-rw-rw----   1 spectre    users          294 Jul 23 21:33 %Desktop DF
-rw-rw----   1 spectre    users        38912 Jul 23 23:59 Desktop DB
-rw-rw----   1 spectre    users       371714 Jul 23 21:24 Desktop DF
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Desktop Folder
-rw-rw-r--   1 spectre    users          294 Jul 23 23:59 MAE-dtdf
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Trash

222836/opt/Desktop Folder:
total 0

222836/opt/Trash:
total 0

223119:
total 0
drwxrwx---   3 spectre    users           96 Jul 23 21:24 pro

223119/pro:
total 0
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Desktop Folder

223119/pro/Desktop Folder:
total 0

224064:
total 0
drwxrwx---   3 spectre    users           96 Jul 23 21:24 tmp

224064/tmp:
total 0
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Desktop Folder

224064/tmp/Desktop Folder:
total 0

224386:
total 0
drwxrwx---   3 spectre    users           96 Jul 23 21:24 var

224386/var:
total 0
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Desktop Folder

224386/var/Desktop Folder:
total 0

224418:
total 0
drwxrwx---   3 spectre    users           96 Jul 23 21:24 usr

224418/usr:
total 0
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Desktop Folder

224418/usr/Desktop Folder:
total 0

261985237:
total 2
drwxrwx---   4 spectre    users         1024 Jul 23 23:59 spectre

261985237/spectre:
total 210
-rw-rw----   1 spectre    users          294 Jul 23 21:33 %Desktop DB
-rw-rw----   1 spectre    users          294 Jul 23 21:33 %Desktop DF
-rw-rw----   1 spectre    users        11264 Jul 23 23:59 Desktop DB
-rw-rw----   1 spectre    users        92608 Jul 23 22:24 Desktop DF
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Desktop Folder
-rw-rw-r--   1 spectre    users          294 Jul 23 23:59 MAE-dtdf
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Trash

261985237/spectre/Desktop Folder:
total 0

261985237/spectre/Trash:
total 0

3536437:
total 0
drwxrwx---   3 spectre    users           96 Jul 23 21:24 home

3536437/home:
total 0
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Desktop Folder

3536437/home/Desktop Folder:
total 0

47:
total 0
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Desktop Folder

47/Desktop Folder:
total 0

57321540:
total 0
drwxrwx---   3 spectre    users           96 Jul 23 21:24 stand

57321540/stand:
total 0
drwxrwx---   2 spectre    users           96 Jul 23 21:24 Desktop Folder

57321540/stand/Desktop Folder:
total 0
We only saw two of them on the desktop because only two of them are "mounted" in
/opt/apple/lib/Default_MIV_file
, and only those two "volumes" have desktop databases. The home directory is obvious, but
/opt
was also given a mount because we're running MAE from it and there are various resources in
/opt/apple/lib
it will try to access. (Some of these are global resources and are treated as part of the System Folder, such as fonts, additional standard applications for the Apple menu, keymaps, locales and, of course, the license key.) These MIVs can be renamed and otherwise treated as if they were any other mounted Macintosh fixed volume.
Two other hidden files are also present in this directory,
.fs_cache
and
.fs_info
, which maintain the virtual Mac's file and volume information respectively.
.fs_cache
in particular is very important as it is roughly the global equivalent of an HFS catalog file (and, like a real HFS catalog file, is stored on disk as a B-tree), storing similar metadata like type and creator, timestamps and so forth. This file is so important to MAE that Apple distributed a separate tool called
fstool
to validate and repair it, sort of like MAE's own Disk First Aid from the shell prompt.
You'll have also noticed above that the desktop database in
spectre
and
opt
is made up of
four
files.
Desktop DB
and
Desktop DF
are present as usual for the bundle database and Finder information respectively, but there are also two more files
%Desktop DB
and
%Desktop DF
, named exactly the same except for a percent sign sigil. This is the other way that resource forks can be represented in MAE, as AppleDouble. Here, the data fork and resource fork are split, with the percent sign indicating the resource fork.
Let's explore the MAE System 7.5.3 some more before we attempt to install anything.
Our window is a bit cramped and we have plenty of real estate in CDE, so let's enlarge it. This can be done by selecting a different virtual resolution from the Control Strip or Monitors control panel, or by simply resizing the window. Likewise, if you are on a display with other colour options, you could also select a different colour depth in the same fashion, just as with a real Macintosh. In our case we only have 8-bit colour from the Visualize-EG and MAE doesn't support HP Color Recovery, so there is no greater colour depth than 256 available this way. (We'll come back to this situation when we try running MAE over remote X.)
Here's my home directory and
/opt
as they appear in the Finder.
/opt
is read-only to my uid, so I can't write directly to it. If I had permissions, I could change them from the Permissions dialogue, which is MAE's equivalent of
chown
,
chmod
and
chgrp
all in one. You can also view the (composite) System Folder here and see that it looks pretty much like any other System Folder on any other Mac with the exception of the MAE Enabler.
At the bottom of the screen is the MAE Toolbar. The MAE Toolbar allows you to grab a Mac-formatted floppy or CD as a volume, cut and paste data or screen bitmaps, or box the pointer into the window as if it were grabbed. This functionality is how you can exchange data between applications running in MAE and applications running in CDE or VUE.
The toolbar is actually maintained and drawn by the emulated Mac as a component of the MAE Enabler, not as chrome by the MAE executable, so the emulated Mac's true resolution is in fact taller than the 832x624 dimensions I'm "officially" using. It is also subject to the same colour depth limitations, which we'll see when we try to play games on it.
The Toolbar can be hidden and used as a pop-up menu instead. We're not going to do that here, but on constrained screens or to make the Mac resolution exactly match the screen, this option would be very handy. The emulator's performance does not perceptibly change either way.
Of course, our PABook doesn't have a floppy or a CD-ROM connected. But we have other options and we'll get to those soon enough.
MAE includes a number of unique Control Panels along with MAE-specific changes to the usual set. The most obvious are the "MAE" ones, and arguably the most important settings are in the MAE General CDEV. This sets performance and efficiency options, like when to idle-throttle the MAE process or how to best to optimize the available palette, how quickly Finder windows update based on changes to the underlying filesystem, and configuring a TIV (Temporary Installer Volume) to allow installers to run and deposit files there without them ending up in unexpected locations, or writing to the volume root and failing. You can then fish out the pieces you want.
But other changes in more "standard" control panels exist. Beyond picking the correct network interface (this machine just has one) the MacTCP control panel isn't configurable, because you do that on the HP-UX side. MAE picks up your IP, which I've partially obscured here because some of you are naughty but trust me that it matches the machine's, and life goes on.
What about Mac keys? Those work. MAE automatically detected the HP keyboard the PABook has and assigned the Command key to left Alt and the Option key to right Alt. And I found the default choice got into my muscle memory quickly, especially since the Alt keys on the PABook are a bit wide and easy to hit.
A large number of keyboard layouts are offered, including an interesting A/UX Mac II layout. That's not the echo of A/UX I want to talk about later but it's noteworthy nonetheless. A less conspicious absence in MAE's supported platforms was IRIX, but although the presence of Silicon Graphics in the list might imply an SGI port was considered (and I'm sure it was), it could also simply refer to using a PS/2 Silicon Graphics keyboard on any of the supported systems with a PS/2 port — like this one. We'll come back to this control panel when we talk about MAE over remote X.
Another interesting panel which is included is a bespoke version of
SoftwareFPU
. Since not all 68K Macs have floating point units, applications are supposed to use Apple's SANE IEEE-754 library which computes the result in software if no FPU is available. Not all software does this, of course (the Magic Cap 1.0 simulator comes to mind), and this is particularly relevant with Power Macs because the 68K emulator only provides a virtual 68LC040. SoftwareFPU, then, is very simple conceptually: it traps F-line instructions intended for the non-existent coprocessor and turns them into SANE calls. This is slow but it means certain software is able to run that otherwise could not.
The MAE SoftwareFPU, which Apple licensed from John Neil & Associates and modified for MAE 3.0, goes a bit further. This version implements a fast path where 68K floating point instructions are directly forwarded to MAE, effectively making F-line traps into hypercalls. Apple estimated this was about 50 percent faster than using regular SoftwareFPU. That said, you'll notice that SoftwareFPU is
disabled
, which is the default. We'll come back to this when we benchmark the emulator.
In MAE 3.0, SANE was changed to directly use host FPU instructions (either SPARC or PA-RISC) for the most commonly performed floating point operations. This works for single and double precision and ran substantially faster than MAE 2.0, but it doesn't work for the 68K's 80-bit extended-precision type, where double precision operations are performed instead and converted (but with a corresponding loss of precision). The previous behaviour, where SANE is simply run under emulation, can be restored with the
-sane
command line option.
A better solution on Power Macs is
Tom Pittman's PowerFPU
, which (where possible) uses PowerPC floating point instructions directly rather than SANE. All Power Macs have an FPU, so this works on all Power Macs, and is over ten times faster than SoftwareFPU.
MAE can also launch Unix-side programs, not just Mac ones. The MAE File Launching control panel will hand off designated files you try to open in the MAE Finder to the corresponding Unix command outside of MAE.
Normally this process requires a shell window, so you can also designate Unix-side executables that explicitly don't need one and will execute directly, like
xclock
or
xcal
.
Regardless, no configuration of MAE is necessary to just open up random Unix executables. Here we're running the HP-UX build of the
Frodo Commodore 64 emulator
, which I installed in
/opt
. The terminal window opens, which is important to capture any standard error or output, but otherwise it runs normally outside of MAE.
That makes you can use the MAE Finder as ... your desktop. You could make MAE take up the entire screen by passing
/opt/apple/bin/mae
the appropriate
-geometry
option and setting the X resource
Vuewm*mae*clientDecoration
to none, effectively making it rootless, and Apple fully supported and documented doing so. Now you've got a virtual Mac that will launch your native X11 applications as well. Who needs CDE when you've got this?
We'll look at another standard control panel that MAE uses for a different purpose in a little while. Meantime, having made a basic survey of the emulator, it's now time to actually run software on it. A benchmark would be a good first test but to do that we need to actually
put
software on it.
If this were any other Mac I was setting up, I'd get AppleTalk started (either via EtherTalk or LocalTalk) and then grab stuff from
thule
, my little 128MB Macintosh IIci running NetBSD and Netatalk for AppleShare. I have lots of basic software on here including useful INITs and CDEVs and essential tools like StuffIt Expander. It still runs NetBSD 1.5.2 because I had trouble getting regular AppleTalk DDP working with 1.6 and up, so it's a fun time capsule too.
But we don't have AppleTalk in MAE, so how are we going to get files from it? Easy: we're going to download the files from
thule
with FTP and put them into my home directory while MAE is running. The Finder will see the new files and incorporate them.
What about the resource forks? The fact that the files are being served by Netatalk from a non-HFS volume (i.e., BSD FFS) actually makes that easier. Netatalk natively stores anything with a resource fork as AppleDouble, depositing the resource fork itself as a separate file
into a hidden directory
.AppleDouble
. We pull down both the data fork and the resource fork, rename the resource fork with a
%
, and move them both at the same time into my home directory. On the next Finder update, it sees the "whole" file and it becomes accessible.
Ta-daaa. We now have StuffIt Expander 5.5.
All resources transferred and it works perfectly. So that I'm not storing lots of Mac stuff in the root of my home directory, I made a new folder named
Mac
and moved StuffIt Expander there. We can now work with StuffIt archives and only have to download one file, which saves having to get the resource fork separately.
An alternative approach, especially if you
are
transferring a file directly from an HFS or HFS+ volume, is to turn it into AppleSingle first and copy that over; MAE will use the file as-is. Apple provided a tool for this in later versions of Mac OS X/macOS, though 10.4 and prior, arguably where it would have been most useful because those versions still support the Classic Environment, don't seem to have it. The best alternative there is
/Developer/Tools/SplitForks
, which doesn't do AppleSingle but does create separate AppleDouble data and resource fork files, so at least you can copy those. We'll get to a somewhat more automatic way of specifically handling Netatalk's AppleDouble directories a bit later.
The corollary to "don't roll your own crypto" is "don't roll your own benchmark" but I did that
over 23 years ago
and here we are. I wrote SieveAhl in Modula-2 using the unfortunately named
MacMETH compiler
just to be weird, rolling all the Toolbox calls by hand. It implements the Sieve of Eratosthenes and a modified version of the FPU-dependent Ahl's Simple Benchmark and issues a score relative to my Macintosh Plus which I have as a reference standard. The main advantage SieveAhl has over other benchmarks is that I wrote it intentionally to run on just about
any
Mac, even down to System 1.1 (tested in vMac). Here, I'm simply grabbing the StuffIt archive using Internet Explorer 5 for UNIX on the CDE side and saving it into the Mac folder.
UnStuffing pretty much just works in MAE. It's not especially fast but unStuffing large
.sit
files isn't too swift on other 68K systems either. We now have a Mac directory that looks like this from the Unix side:
ruby:/home/spectre/% ls -lR Mac
total 2560
-rw-rw-r--   1 spectre    users          798 Jul 25 10:03 %SieveAhl.sit
-rw-rw-rw-   1 spectre    users       878980 Jul 25 09:51 %StuffItExpander
drwxrwxr-x   2 spectre    users           96 Jul 25 10:03 SieveAhl Folder
-rw-rw-r--   1 spectre    users        47470 Jul 25 10:03 SieveAhl.sit
-rw-rw-rw-   1 spectre    users       381116 Jul 25 09:51 StuffItExpander

Mac/SieveAhl Folder:
total 236
-rwxrw-r--   1 spectre    users       107908 Aug 18  2002 SieveAhl
-rw-rw-r--   1 spectre    users         3353 Aug 19  2002 SieveAhl README
Our newly created files in the
SieveAhl Folder
are now AppleSingle, for example the readme file:
ruby:/home/spectre/% xd -c Mac/SieveAhl\ Folder/SieveAhl\ README | head -10
0000000 \0 05 16 \0 \0 01 \0 \0  M  a  c  i  n  t  o  s
0000010  h                      \0 03 \0 \0 \0 \t \0 \0
0000020 \0 e0 \0 \0 \0    \0 \0 \0 02 \0 \0 02 \0 \0 \0
0000030 02  d \0 \0 \0 01 \0 \0 06 \0 \0 \0 07 19 \0 \0
0000040 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0
*
00000e0  t  t  r  o  t  t  x  t \0 \0 ff ff ff ff \0 \0
00000f0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0 \0
*
0000200 \0 \0 01 \0 \0 \0 02  2 \0 \0 01  2 \0 \0 \0  2
We'll get to the rules about when MAE creates AppleSingle and AppleDouble files in a moment. Let's see the numbers we get.
The About box, for posterity.
Each SieveAhl benchmark asks for the number of runs (too few on a fast system impairs accuracy due to the timekeeping method used). Our integer run with the Sieve clocks in at 4,701% (i.e., 4.7x) the speed of our reference ~8MHz Mac Plus. This is a Modula-2 version of the implementation originally published in
Byte
in September 1981. It iterates over the interval 0-8190, in which 1,899 primes are expected.
The FPU test is based on David Ahl's Simple Benchmark from
Creative Computing
, intended originally to evaluate performance and precision differences between various microcomputer BASIC implementations. We don't care about the accuracy or randomness values his benchmark would compute (well, we don't care
much
), so we just compute those and throw them away. This gets 4,863% the speed of a Mac Plus, which we would expect to be roughly the same because we have no floating point hardware. Repeated runs of both tests were nearly identical.
I mentioned that SoftwareFPU was turned off, so let's turn it on and see if it makes any difference to the floating point score. It does, but roughly only about 1% (!) better. However, it should be kept in mind that Apple's advertised 50 percent improvement was against using
regular
SoftwareFPU, not against using it at all. Additionally, MacMETH generates well-behaved code that calls SANE as it should and doesn't emit floating point instructions.
How does this compare to a real 68LC040? Conveniently, we have one handy to try it out on!
This is
rintintin
, my PowerBook 540c with a 33MHz 68LC040 and 12MB of RAM running Mac OS 7.6.1, and the most powerful Blackbird PowerBook sold in the United States (the later Japanese 550c is the same speed, but with a full 68040 and FPU). It was the first PowerBook with any '040 processor, stereo speakers, on-board Ethernet (via AAUI), a trackpad instead of a trackball, twin battery bays and a full-size keyboard. The PowerBook 520/520c and 540/540c came out just a couple months after the first Power Macs and Apple placed the processor onto a daughtercard as a promise that it could be eventually upgraded. As such, the "Ready for PowerPC upgrade" sticker came on these models from the factory, though this particular one is a slightly larger reproduction I printed up a few copies of so I could surreptitiously slap them on the Intel Macs at the Apple Store. Apple nevertheless greatly underestimated demand for the line, mistakenly believing people would rather wait for what eventually was the PowerBook 5300, and the Blackbirds were chronically short-stocked for months.
I upgraded this particular unit with an additional 8MB of RAM (on top of the base 4MB) and a SCSI2SD, making it an almost silent unit in operation. The only flaw it has is an iffy cable connection between the display and the top case, which is unfortunately a common problem with these models.
The Blackbird PowerBooks were also movie-famous, most notably in the first 1996
Mission: Impossible
movie with Tom Cruise and Jon Voight. A regular Blackbird in the standard two-tone grey, most likely a 540c, was what Luther used to block the NOC list transmission on the TGV in the third act.
Similarly, both Phelps and Ethan use another PowerBook, this one painted jet black with no visible logos. However, if you look at the ports ...
... they also match the Blackbirds', making it either a 550c (which was, in fact, black) or a spray-painted 520c or 540c. Since Apple wasn't actually selling
any
Blackbird laptop anymore by the time the movie came out, neither computer's model badge is ever visible, though you can at least see a rainbow apple on Luther's.
One other fun sighting is an IBM ThinkPad 701 with its famous butterfly keyboard, but the really wacky part is what's onscreen, apparently some fevered mock mashup of Mac OS 8 and Sun's OPEN LOOK. Other Apple computers and hardware visible in the movie include a SuperMac monitor and AppleDesign keyboard as the console of the CIA's standalone terminal (and what might have been a Kensington TurboMouse ADB trackball), and a boxed Power Macintosh 8100 in the TGV's baggage hold. These were all part of Apple's $15 million [$29.4 million in 2025 dollars] movie sponsorship, even an Apple-specific movie poster that I have in my lab, but Apple themselves are never mentioned by name.
MAE actually exceeds the 540c on both benchmarks, which clock in at 3,572% and 3,862% respectively. Not bad! While the relationship is probably not linear due to the nature of dynamic recompilation, we can give a ballpark estimate for MAE's relative "clock speed" running on this 160MHz PABook as around 43MHz.
Let's try a web browser next. And, of course, we'll use a browser I'm maintaining as well:
MacLynx
, the venerable text browser natively ported to the MacOS. Here we'll run beta 6.
MacLynx starts up and shows the default on-disk home page. This is in fact a good test for MAE specifically because to do something like view Hacker News or Lobste.rs we need to change
lynx.cfg
to point to our local
Crypto Ancienne TLS 1.3 proxy server
. However, we don't have a proper text editor installed other than SimpleText.
We could certainly grab BBEdit Lite from the server as well, but MAE gives us an alternative. The manual indicates that "[b]y default, MAE stores files (except text files) in AppleSingle format." Text files, however, are stored as AppleDouble. If we look at our directory listing after unStuffing MacLynx, we can see this rule has been followed:
ruby:/home/spectre/Mac/MacLynx 2.7.1b6 68K/% ls -l
total 2004
-rw-rw-r--   1 spectre    users         8429 Apr  5 15:41 %MacLynx b6 ReadMe
-rw-rw-r--   1 spectre    users        10925 Apr  5 15:54 %MacLynx b6 Release Notes
-rw-rw-r--   1 spectre    users         2086 Apr  5 15:37 %index.html
-rw-rw-r--   1 spectre    users        68743 Aug 18  2023 %lynx.cfg
-rw-rw-r--   1 spectre    users         7748 Apr  5 15:53 %lynxrc
-rwxrw-r--   1 spectre    users       829276 Apr  5 20:31 MacLynx 680x0
-rw-rw-r--   1 spectre    users         5869 Apr  5 15:41 MacLynx b6 ReadMe
-rw-rw-r--   1 spectre    users         7341 Apr  5 15:54 MacLynx b6 Release Notes
drwxrwxr-x   2 spectre    users         1024 Apr  5  1997 about_lynx
-rw-rw-r--   1 spectre    users         1062 Apr  5 15:37 index.html
-rw-rw-r--   1 spectre    users        67719 Aug 18  2023 lynx.cfg
drwxrwxr-x   3 spectre    users         1024 Aug 18  2023 lynx_help
-rw-rw-r--   1 spectre    users         7236 Apr  5 15:53 lynxrc
You'll notice that all the text files — the readmes,
index.html
,
lynx.cfg
and
lynxrc
— got separate resource forks as AppleDouble, but the main executable did not. Now, the smart ones among you will say, "But wait! The SieveAhl readme file is text, and it was AppleSingle!" That's right — except
that
file's text is all stored in styled text resources and there's nothing in the data fork at all. MAE seems to content-sniff files to figure out what to do with them, so BinHex files (which are valid text) will be treated as a text file and made AppleDouble, but a read-only SimpleText file with nothing in the data fork will be treated as a binary and made AppleSingle. The AppleDouble control panel allows you to always force storing files as AppleDouble with specific applications and the separately distributed
asdtool
will convert a Mac file between AppleSingle and AppleDouble from the shell prompt.
The upshot is that we now have a file we can simply edit from the Unix side with
vi
or, for the mentally deranged,
emacs
— and the resource fork will remain undisturbed. With MacLynx thus configured for the proxy server, we can view modern HTTPS sites inside MAE no problem.
I pulled over some more software to work on. When I'm installing my usual software set I ordinarily put either the StuffIt Expander app or an alias on the desktop as a shortcut.
But this is also something MAE handles differently: instead of moving it, by default it creates an alias. (Aliases in MAE are still aliases, not symbolic or hard links, though a previously created symbolic link will also look like an alias.) You can copy the file by dragging it to the desktop with the Option key held down, but there's no way to indicate you want to
move
it. That almost sounds like that the MAE desktop doesn't belong to any MIV even though it is, in fact, part of the MIV for your home directory and that's where we had StuffIt Expander:
ruby:/home/spectre/% find . -name 'StuffItExpander alias' -print
./.mac/ruby/261985237/spectre/Desktop Folder/StuffItExpander alias
Conveniently, if you open an alias to something on an MIV that's defined but not yet mounted, MAE will automount it on the desktop for you.
Our next set of programs will be TattleTech 2.8 and
Gestalt.Appl
so we can see what's going on under the hood. There are some surprises here.
The first surprise is the Gestalt ID MAE uses to identify itself: 19, corresponding to the Macintosh LC. I have no idea if this is why, but the original Cognac RISC prototype was the RISC LC (because it was built into an LC case), and it certainly seems like a rather suspicious coincidence. I am also amused that the last PRAM hard reset date is September 25, 1991. That would probably correlate to when the virtual PRAM data was first written to disk during the very early days of A/UX "4.0."
TattleTech comes up with a rather low estimate of the system's clock speed and also suggests the emulated bus speed is only 20MHz. Neither number is likely reliable.
No FPU is detected, either in the previous slide (where SoftwareFPU was still on from our testing with SieveAhl) or here where we turn it back off.
A single virtual NuBus slot is present. This is the emulated MAE video card ("Rev 2.0") and carries a revision date of June 13, 1994. The
_L
at the end of the
Device sResource Name
is significant because
/opt/apple/bin/macd
defines
six
such resources:
Display_Video_Apple_MAE_S
,
Display_Video_Apple_MAE_M
,
Display_Video_Apple_MAE_L
,
Display_Video_Apple_MAE_F
,
Display_Video_Apple_MAE_C1
and
Display_Video_Apple_MAE_C2
. These apparently correlate to specific resolutions, namely (in the order they appear) "512 x 342 (9" Macintosh)",
"640 x 480 (14" Macintosh)",
"832 x 624 (17" Macintosh)",
"864 x 864 Resolution",
"640 x 800 Resolution" and
"640 x 640 Resolution". Since we're at 832x624, we get the
_L
(presumably small, medium, large, full and two custom?) "card." The emulated DeclROM used by these virtual cards is part of the big blob stored in
/opt/apple/lib/engine
, along with the Toolbox ROM and other goodies. We'll come back to this when we explore its Gestalt selectors.
There are no SCSI devices, or spoons.
Interestingly, the two usual Mac serial ports
are
defined, but neither appears to be supported. MAE naturally supports printing, but only to a "UNIX PostScript printer" (i.e.,
lpr
) or via AppleTalk, and it does not support using the modem port for a modem or even as a serial port.
No surprises that TattleTech reports the operating system as 7.5.3 ("7.53") and reports on the presence of the MAE Enabler, but there are irregularities here too. The Finder is version "MAE 3.0 Update 4." AppleScript is present, as expected, but the Finder script extension version is "MAE 3.0.1."
A/UX is indicated as not present despite its provenance, CloseView is present (but again in a special "MAE 3.0" version), and the Code Fragment Manager isn't. Although CFM-68K was of course a thing, Apple had
deprecated it for 68K
in 1996.
The PPC (Process-to-Process Communications) ToolBox is also present, which we last exploited to
allow the Apple Network Server to numbercrunch for connected clients
. It should be possible to do something similar with MAE and have the local host do the work, but there are no local AppleTalk interfaces or headers to compile against.
QuickDraw is naturally present (no GX or 3D, of course). In MAE 3.0 QuickDraw is especially important and we'll get to that when we try playing a couple rather famous games. QuickTime is also present, version 2.5, though not everything is enabled (no software MIDI synthesizer, for example).
It's also worth pointing out that there is no Speech Manager. Apple specifically mentions the Speech Manager as incompatible in the MAE documentation, although it doesn't explain why. If an application installs it anyway, such as HyperCard, you can make MAE start with extensions off by passing
-noextensions
.
In the processes list, we see an otherwise invisible process called the MAE Helper. This process is what draws the MAE toolbar and chrome and manages its functions, and is started by the MAE Enabler.
The MAE Helper does not appear as a discrete task in About This Macintosh and is simply treated as part of the system software.
Now for some Gestalt selectors of note. One I'm going to point out immediately is the
cith
selector ("Sith"? Darth Mac?), which is unique to MAE and is conveniently set to $00000304 (i.e., major version 3, minor version 4). While I don't have MAE 1.0 here to test with, René Ros indicates in his Gestalt reports that it
has a
cith
value of 0
, though it does exist there too. I don't know what version MAE 2.0 reports but I'm sure someone is firing it up right now to find out and will post in the comments.
To more easily decipher the others we'll turn to Gestalt.Appl and I'll point out the highlights.
micn
is not interesting for the icon (just generic Mac) but rather the string shown, which is a
STR#
resource indexed by the value of
mach
(-16395). The string is "Macintosh ApplicationEnvironment" [sic].
There is no MMU indicated in "
mmu
" (note space), but this isn't a surprise for an emulator. Consequently, there is also no virtual memory support within MAE (the host is supposed to handle that).
The ROM version (
romv
) is more interesting. Although a great many Old World Mac ROMs are tagged as version 1917, the particular ROM that MAE is using is from the Quadra 660AV and 840AV because we can find its checksum (
5b f1 0f d1
) and version (
07 7d
) at offset $001c0000 in
/opt/apple/lib/engine
. No other valid checksum and version appears anywhere else in this file, and no true
Scotsman
Macintosh LC would have used a ROM that recent. Thus, if you get a Gestalt ID of 19 but a ROM version of 1917, that's a pretty good indication you're running under MAE. René's list also shows a ROM version of 1917 for MAE 1.0, so MAE 2.0 almost certainly does as well.
Despite TattleTech finding the virtual NuBus video card,
sltc
insists there aren't any NuBus slots.
Finally, one more unique selector value is under
snhw
for the sound hardware, which reports a driver
cith
. This likewise appears nowhere else and is specific to the MAE emulated audio hardware. Oddly, although MAE 1.0 lacked sound, René's list indicates an
snhw
of
awac
which would suggest
an AWACS
.
Let's get back to running some more apps. I'm going to bump up the emulated RAM now because a couple near the end will likely benefit.
In MAE, since there's no virtual (or for that matter actual physical) memory, the Memory control panel serves a largely different purpose. You can still set the disk cache size (it helpfully reminds you this applies to "Macintosh volumes only"), but you can also set MAE's total memory size up to 45MB. We have 512MB in this PABook, so we'll just max it out for the remainder of this article.
And, after restart, we now have 45MB of RAM.
Fetch, the venerable Macintosh FTP client —
still sold!
— was a bit of a mixed bag on MAE. 2.1.2 was the 68K version I had on
thule
, so I tried that first. It starts and runs fine, but when I actually tried to download anything with this version of Fetch it locked up the entire emulated Mac as soon the file was transferred. That said, I'm not sure if this is a fault of MAE or Fetch because at the exact same point of the exact same file with the exact same version of Fetch on the 540c, it abruptly dropped the connection and threw an error message — though I note transfer speeds were faster on MAE, probably because of the better hardware, right up until it hit the wall.
Fortunately the later Fetch 3.0.1 behaves correctly and Apple even offered that specific version for download from the MAE website. There are specific advantages to using Fetch in MAE because of its transparent support for AppleSingle transfers. Still, grabbing files with MacLynx works fine too (hurray for eating your own dogfood), so I'll mostly use that.
Unfortunately,
ssheven
, which works great on my real Macs, crashes on MAE and I'm not sure why.
In fact, at one point the crash was so severe it actually caused MAE itself to quit, whereupon I was chastised for an improper shutdown when bringing it back up. This special variant of the usual Mac "didn't Shut Down" window is unique to MAE. I'm not sure if the crash is exploitable but it's not good news regardless. This is probably a problem in MAE specifically rather than
ssheven
, though I'd have to get a better debugger up on it to figure it out.
The old MacSSH didn't do much better. Telnet was fine and worked fine, and I had already expected that SSH2 sessions would take a while to negotiate keys (back in the day when I used my Quadra 605 for this with a 25MHz full 68040, it took about 45 seconds). However, this connection to a local test host locked up hard. The MAE manual says that Command-Option-Esc doesn't work for quitting a hung Mac application, but it actually does — you just have to blindly click the Force Quit button (leftmost). As with any real Mac, though, you really should restart afterwards.
These aren't fatal flaws, however, because we could also just use a CDE terminal window for Telnet and
ssh
, and that would even be more useful. Instead, we should  try something
really
important next.
The Macintosh port of Wolfenstein 3D was done by Rebecca Heinemann and her team when she was still at Interplay, under their MacPlay label. It came in both this full version on multiple floppies, which is the one I bought at retail back in the day, and a shareware three-level "First Encounter" which was criticized as poor value for free. The Mac version is related to the enhanced Atari Jaguar port and uses higher resolution textures, sprites and sound than the original DOS version, plus a different status bar, new weapons and thirty more "Second Encounter" levels from the Super NES and Jag; the 3DO and
Apple IIgs
versions are derived from the Mac version. This port was released in 1994 and the "Accelerated for Power Macintosh" and "System 7 Savvy" stickers give the rough timeframe. It requires a 25MHz 68030 or better and is a fat binary.
Given that the PABook doesn't have a floppy drive, I copied over this version by simply Stuffing the installed folder on my Power Macintosh 7300 and downloading it over shell FTP (NCSA Telnet on the Mac contains a very basic FTP server which is handy for this).
To give it the best chance of working well, I bumped up its preferred memory partition to a full ten megabytes and, based on the advice in the MAE administrator's manual, knocked the audio output sample rate down to 22.050kHz instead of 44.1kHz: "On low-performance workstations, you may need to lower the sampling rate if you experience pauses or gaps in sound output." (This is a big heaping bowl of foreshadowing, kids.)
I was expecting it to crash, but not only did it not crash, but the music was just as brassy as ever.
Notice that the palette, being a 256-colour mode, is affecting the MAE toolbar, demonstrating it is indeed drawn and maintained by the guest Mac. In fact, when the screen fades out between slides, the icons in the toolbar partially fade out also. It would have been nice if Apple had come up with an auto-hide option.
Selecting the game episodes. The "First Encounter" is just the first three levels from the "Second Encounter." The other six episodes are the classic levels from the O.G. MS-DOS game.
It originally came up in this postage-stamp view at 320x200. This was small, but it was totally playable.
There is an extension called
Wolfenzoom
(Gopher link) that will scale-blit the 320x200 to 640x400, and I used to use it on my unaccelerated desktop Macintosh IIci when I first bought this game. However, since I'm all about pushing my luck, let's try the highest resolution.
And, well, it worked! ... mostly. The game played well. Frame rate wasn't butter smooth but it was decent and you could mow down Nazis with little fuss. Sounds, however, were very delayed, sometimes for surprisingly long periods: you'd shoot a trooper, and about five seconds later eventually hear the gunfight and his guttural German demise. The really surprising part is the audio lag got even worse when I dropped the sound quality further still to 11.025kHz.
As it happens, not only is a full 44.1kHz sample rate needed for audio to play in a timely fashion, but it also didn't really seem to slow the game down much at all. Music and sound effects all came through great once I cranked the sample rate back up. (This might be different on Solaris.) In fact, to my delight I found Wolfenstein 3D played better overall on MAE than on the 540c. It looks like the HP audio server handles audio so well that it's unlikely it would be the direct cause of most performance problems.
One particular reason I wanted to test Wolf3D is because it can operate in both QuickDraw and direct-to-video memory modes. When Use QuickDraw is checked (the default), Wolf3D restricts itself to documented QuickDraw calls, which is the slowest but most compatible option and works with pretty much any video card or machine. When Use QuickDraw is
un
checked, the game will try to draw directly to video memory. This doesn't always work, and as you can see in this screenshot, not all of the screen was updating properly in this mode.
This observation will become relevant when we try running our next game. You do see where this is going, don't you?
These are my retail copies of Ultimate Doom and Doom II I bought at CompUSA in their Mac-specific boxes, ported by Lion Entertainment for GT Interactive. (Lion also did the Mac ports of Duke Nukem 3D and Shadow Warrior, but there were never official ports of Strife or the original Heretic, and the Hexen port was by Presage.) The Mac ports play unmodified PC WADs but can do so at double resolution, and they support deathmatch both over IPX and AppleTalk, though an update is needed to support AppleTalk netplay on later versions of MacOS. Again, our PABook doesn't have a CD-ROM drive, so I pulled a copy of it from the Power Macintosh 7300 too.
This is our first bad sign. There is no music, though this is expected because the QuickTime that comes with MAE doesn't implement a MIDI synthesizer, but half the screen isn't updating. These ports expect to write directly to video memory; they don't generally go through QuickDraw.
The Mac-specific loading screen
does
use QuickDraw, and appears correctly, but ...
... as the Phobos Lab demo runs, you can see it start to accumulate stale areas of the screen.
You can force the screen to update by messing with the interface or the menu, but the gaps suggested we might have better luck with a smaller screen resolution, so we'll quit and try that.
While a bit of the bottom of the screen is cut off at 640x480, this seems better immediately.
Shrinking down the viewport and enabling low detail makes a reasonably playable game and you can see enough of the numbers in the status bar to be useful (except for rockets and energy cells). It can be periodically forced to repaint by interacting with the GUI or Doom main menu.
Interestingly, reducing the size of the drawport even further (Options, Small Graphics) yielded some of the same repainting problems that we saw in Wolf3D with QuickDraw off.
These resolve promptly with Large Graphics, so however it works, this configuration appears to be the sweet spot for Doom on MAE.
Just for yuks, let's see if it gets any better if we reduce the Mac screen down even further to the "minimum" 512x342.
Since even the QuickDraw-drawn loading screen is getting cropped, I suspect that Doom won't handle this screen resolution ...
... and although it will play, it crashes hard after only a brief period. In fact, in my second experiment with this resolution, it also ended up taking MAE down completely. That said, I suspect it wasn't ever designed for a viewport that small.
If you're fine with a bit of the status bar being cut off, Doom at 640x480 runs acceptably well with the viewport reduced. (I haven't tried it with a non-standard screen size but I suspect it would misbehave similarly.) Note that there is no MIDI music, though sound effects played fine. However, as far as performance goes, Doom was where the 540c did better overall: it played more smoothly with larger viewports, and did so with a consistent framerate. On MAE the game's responsiveness was rather variable, probably some weird thrashing in the dynamic compilation alternating between reasonably zippy and an occasional crawl. It's hardly unplayable but overall better on a real 68K (and of course better still on any Power Macintosh).
In a vague attempt at productivity I loaded the classic Microsoft Word 5.1 onto MAE, though I was pretty sure Apple would have tested an app that common to ensure it would work. This is also on the Netatalk share on
thule
, but copying Word 5.1 over was a much bigger situation than simply grabbing a single file and its resource fork; we had a number of double-forked files we needed to move
en masse
. This Perl script, which works on both Perl 5 and 4.036, will iterate over a copy and move Netatalk's AppleDouble resource files into the proper location for MAE, resolving ambiguities in filenames if needed.
#!/usr/bin/perl

sub starts { return substr($_[0], 0, length($_[1])) eq $_[1]; }
select(STDOUT); $|++;

while(<>) {
        print; chop;
        if ($pid = fork()) {
                wait;

                @call = ("/usr/bin/rmdir", $_);
                print join(" ", @call), "\n";
                system(@call);
                die("returned $?, aborting\n") if ($?);
        } else {
                $x = 0;

                chdir($_) || die("chdir $_: $!");
                $dir = $_;
                $x++ while (/ESCAPE_SEQUENCE$x/);
                $dir =~ s/\\\//ESCAPE_SEQUENCE$x/g;
                (@pieces) = split(/\//, $dir);
                for($x=0;$x<scalar(@pieces);$x++) {
                        $pieces[$x] =~ s/ESCAPE_SEQUENCE$x/\\\//g;
                }
                @x = <.*>; shift @x; shift @x; # drop . , ..
                push(@x, <*>);
                if (!scalar(@x)) {
                        print "\tno files\n";
                        exit(0);
                }
                foreach $f (@x) {
                        print "\t$f\n";
                        if ($f eq '.Parent') {
                                @k = @pieces; pop @k; $ff = pop @k;
                                $nf = "../../%$ff";
                        } elsif (-e "../$f") {
                                $nf = "../%$f";
                        } else {
                                opendir(D, "..") || die("opendir: $!\n");
                                @guesses = grep(&starts($_, $f), readdir(D));
                                closedir(D);
                                if (scalar(@guesses) > 1) {
                                        print "\t\tAMBIGUOUS, SKIPPING\n";
                                        next;
                                }
                                $nf = "../%" . $guesses[0];
                        }
                        @call = ("/usr/bin/mv", $f, $nf);
                        print "\t\t", join(" ", @call), "\n";
                        system(@call);
                        die("returned $?, aborting\n") if ($?);
                }
                exit(0);
        }
}
Call it with
find [directory] -name '.AppleDouble' -print | perl ad2mae
to run. Only run this on a copy! When everything was in the right place, I moved the directory into my
Mac
folder and it was ready to go.
It worked fine, of course. I had no printer configured and no need to set one up, but loading and saving Word documents "just worked." I'm quite sure Microsoft Excel and pretty sure Adobe Photoshop would also work this way, though since we're at 256 colours and using an "Approximate" palette, Photoshop's utility would likely be reduced for all but bitmap art due to poor colour fidelity.
Incidentally (especially since I didn't have the execute bits on it), when I double-clicked the Perl script
ad2mae
from the MAE Finder, the Finder determined it was a text file and opened it up in
vi
in a CDE window ready for editing. Not bad!
As MAE 3.0 specifically advertised that it was faster than previous versions over remote X, let's test how well that works from my POWER9 Raptor Talos II in Fedora 42. Being the Wayland refusenik I am, I still run KDE Plasma in X11, so with
xhost
set appropriately and
AllowByteSwappedClients
enabled (because the POWER9 is running Power ISA little-endian and the PABook is running big) we should be able to connect:
And poof, here we are. We get no audio because we're obviously not running an HP-compatible audio server, but even remote audio should work if you were running a little HP workstation off a bigger HP server (like, say, the dual PA-8900 C8000 I have on the shelf gathering dust that I really need to find a place for).
Because we're running this window with a 24-bit visual on a much bigger screen, we now have many more choices in colour depth ...
... and an interesting new 1920x1050 (not 1080) resolution. Naturally you can resize the window to whatever you want, of course.
The key improvement is that MAE 3.0 is much more efficient with Xlib calls. In MAE 2 and earlier, apps would draw to the frame buffer, either through QuickDraw or direct access, and MAE would then push the changed portion of the framebuffer to the X server. This is a very compatible and straightforward approach to screen updates but could lead to large amounts of bitmap data being pushed, significantly bottlenecking the networks of the time if the session were remote. In MAE 3.0, MAE will turn QuickDraw operations themselves into Xlib calls, inckuding pushing much smaller bitmaps like icons, fonts and parts of interfaces which can even be pre-cached by the X server in the pixmap cache. The framebuffer is only directly referenced in corner situations such as the window being restored or revealed, which Apple estimated made MAE 3.0's network overhead only ten percent of MAE 2.0's.
For apps with a modest amount of screen updates, this works very well. Pull-down menus had a little bit of lag but typing into a Word document was fine. I did have to go into the Keyboard control panel and remap my
actual
Command and Option keys, though (I use a white A1048 USB Apple Keyboard with the Quad G5 and the Talos II).
Wolf3D chugged pretty badly this way, however, because it's frequently pushing almost an entire bitmap and the PABook LASI only supports 10Mbit Ethernet. (It may have worked better with the 10/100 PCMCIA option.) At the 320x200 screen size it was cautiously playable but Use QuickDraw had to be checked to make screen updates in any way consistent.
Of course, that's not what MAE-over-remote-X was intended for. Rather, it was intended for a multi-seat license where some big K- or L-Class or SunFire hulking in the server room served multiple simultaneous MAE sessions to multiple remote clients and kept all their files and documents centrally. In my brief experience, it seems like it would have been more than suitable for that purpose.
We'll close now with one last application — ResEdit — because now that we've seen it ticking we'd like a few insights into what
makes
it tick.
ResEdit runs, of course. We'll make a copy of the MAE Enabler (since it's in use) and analyse it since it's where most of the meat is on the Mac side. I'll scrub through the Unix executables momentarily.
The Enabler contains the GUI-level pieces of the MAE Helper (which makes sense, since it contains the MAE Helper generally). Here's the
DLOG
modal when MAE is formatting the TIV.
And here's one of the
DLOG
s for the MAE Toolbar help we saw earlier.
This
DLOG
is one of the modals for the floppy/CD mounter.
This
DITL
looks like it's part of a credits easter egg, though I haven't figured out yet how to trigger it. I'm assuming the dog is named Rosco ("In Memory of Rosco - 10/5/96"). Also note the dog's Dr Seuss hat, a callback to MAE's "Cat-in-the-Hat" codename.
Here's the MAE 3.0 development team: Peter Blas, Michael Brenner, Matthew Caprile, Mary Chan, Bill Convis, Jerry Cottingham, Ivan Drucker, Gerri Eaton, Tim Gilman, Gary Giusti, Mark Gorlinsky, John Grabowski, Cindi Hollister, Richard W. Johnson, John Kullmann, Tom Molnar, John Morley, Stephen Nelson, Michael Press, Jeff Roberts, Shinji Sato, Marc Sinykin, Earl Wallace, Gayle Wiesner. This list of credits will show up again later.
These members of the MAE team, however, don't seem to be listed anywhere else.
Marketing and Support: J. Eric Akin, Ruthanne Baker-Mander, Dennis Chen, Richardo Gonzalez, Suzanne Seibert
Product Testing: Paul Burriesci, Dan Carpenter, Chris Chapman, Kevin Walters
Thanks: Kent Burke, Andrea Cheung, Thomas Chin, David X. Clancy, Paul Dumais, Kevin Fowler, Stu Freiman, Liz Galbraith, Ray Gans, Michelle Gaskill, Dick Gemoets, Stella Hackell, Mark Himelstein, Jay Hosler, Jonathan Hudgins, Channing Hughes, Lauren Kahn, Michael Kellner, Ron Morton, Tom O'Brien, Steve Peters, Paul Pavelko, Bill Vaughan, Adam Zell
Are you one of these people (from the development team or these groups)? Say hi in the comments or drop me a line at ckaiser at floodgap dawt com (I'll keep you anonymous if you're concerned about your NDAs). I would love to pick your brain on any interesting details you remember.
I also noticed these icons in amongst the other expected
PICT
s. I'm not sure what they refer to. Notice that the
Toolbar Menu
when you use the third mouse button is actually just a bunch of PICT resources.
There are some other interesting things of note when we start going through the binaries. I separately extracted the files from the installer packages (they're just
cpio
archives) to preserve their time stamps for analysis. Let's look at everything that's there and then dig into the most notable individual files.
% ls -l bin
total 12648
-rwxr-xr-x  1 spectre  staff   167488 Jan 23  1997 appleping
-rwxr-xr-x  1 spectre  staff   282192 Jan 23  1997 appletalk
-rwxr-xr-x  1 spectre  staff    24660 Jan 23  1997 asdtool
-rwxr-xr-x  1 spectre  staff   213136 Jan 23  1997 atlookup
-rwxr-xr-x  1 spectre  staff   948947 Jan 23  1997 legal
-rwxr-xr-x  1 spectre  staff   444541 Jan 23  1997 macd
-rwxr-xr-x  1 spectre  staff  4381952 Jan 23  1997 mae
All of the core binaries have a modification date of January 23, 1997, presumably the RTM date.
% ls -alR lib
total 28872
drwxr-xr-x  11 spectre  staff       352 Jan 23  1997 .
drwxr-xr-x   7 spectre  staff       224 Aug  1 09:24 ..
-rw-r--r--   1 spectre  staff      1374 Nov  6  1996 .MIV_file
-rw-r--r--   1 spectre  staff      4194 Nov 12  1996 KeymapDepotDB
-rw-r--r--   1 spectre  staff     10073 Nov 12  1996 MajorUpdate
-rw-r--r--   1 spectre  staff    209218 Nov  6  1996 btree
drwxr-xr-x   9 spectre  staff       288 Nov  6  1996 ccm
-rw-r--r--   1 spectre  staff  10606478 Nov  6  1996 data
-rw-r--r--   1 spectre  staff   3932416 Jan 23  1997 engine
drwxr-xr-x   4 spectre  staff       128 Jan 23  1997 legal
drwxr-xr-x   3 spectre  staff        96 Jan 23  1997 locale
Of the library files,
data
and
engine
are probably the most notable. We will look at those seprately.
KeymapDepotDB
is where the default keymaps MAE uses are kept, and
MajorUpdate
is instructions to the installer script for how to perform an upgrade to a new major release. Since there's no MAE 4.0, this presumably will never be used again. The manual does not document what
btree
does, and it has only a single readable string in it:
Copyright 1991 Apple Computer, Inc. All Rights Reserved. Ricardo Batista
The rest are character set mappings and the EULAs in graphic form for both the MAE demo and the full version (with X bitmap buttons for accept/don't accept in all languages except English):
lib/ccm:
total 56
drwxr-xr-x   9 spectre  staff  288 Nov  6  1996 .
drwxr-xr-x  11 spectre  staff  352 Jan 23  1997 ..
-rw-r--r--   1 spectre  staff  335 Nov  6  1996 ISO8859-1Right
-rw-r--r--   1 spectre  staff  326 Nov  6  1996 ISO8859Left
-rw-r--r--   1 spectre  staff  326 Nov  6  1996 JISX0201Left
-rw-r--r--   1 spectre  staff  327 Nov  6  1996 JISX0201Right
-rw-r--r--   1 spectre  staff  804 Nov  6  1996 RomanScript
-rw-r--r--   1 spectre  staff   40 Nov  6  1996 m2xConv.dir
-rw-r--r--   1 spectre  staff   94 Nov  6  1996 x2mConv.dir

lib/legal:
total 0
drwxr-xr-x   4 spectre  staff  128 Jan 23  1997 .
drwxr-xr-x  11 spectre  staff  352 Jan 23  1997 ..
drwxr-xr-x   3 spectre  staff   96 Jan 23  1997 demo
drwxr-xr-x   3 spectre  staff   96 Jan 23  1997 full

lib/legal/demo:
total 0
drwxr-xr-x   3 spectre  staff   96 Jan 23  1997 .
drwxr-xr-x   4 spectre  staff  128 Jan 23  1997 ..
drwxr-xr-x  24 spectre  staff  768 Jan 23  1997 bitmaps

lib/legal/demo/bitmaps:
total 808
drwxr-xr-x  24 spectre  staff    768 Jan 23  1997 .
drwxr-xr-x   3 spectre  staff     96 Jan 23  1997 ..
-rw-r--r--   1 spectre  staff  48676 Nov  6  1996 dutch.gif
-rw-r--r--   1 spectre  staff   2335 Nov  6  1996 dutchn.xbm
-rw-r--r--   1 spectre  staff   2335 Nov  6  1996 dutchy.xbm
-rw-r--r--   1 spectre  staff  43198 Nov  6  1996 english.gif
-rw-r--r--   1 spectre  staff  45620 Nov  6  1996 french.gif
-rw-r--r--   1 spectre  staff   2338 Nov  6  1996 frenchn.xbm
-rw-r--r--   1 spectre  staff   2338 Nov  6  1996 frenchy.xbm
-rw-r--r--   1 spectre  staff  44545 Nov  6  1996 german.gif
-rw-r--r--   1 spectre  staff   2338 Nov  6  1996 germann.xbm
-rw-r--r--   1 spectre  staff   2338 Nov  6  1996 germany.xbm
-rw-r--r--   1 spectre  staff  39604 Nov  6  1996 italian.gif
-rw-r--r--   1 spectre  staff   2341 Nov  6  1996 italiann.xbm
-rw-r--r--   1 spectre  staff   2341 Nov  6  1996 italiany.xbm
-rw-r--r--   1 spectre  staff  39800 Nov  6  1996 japanese.gif
-rw-r--r--   1 spectre  staff   2344 Nov  6  1996 japanesen.xbm
-rw-r--r--   1 spectre  staff   2344 Nov  6  1996 japanesey.xbm
-rw-r--r--   1 spectre  staff  44405 Nov  6  1996 spanish.gif
-rw-r--r--   1 spectre  staff   2341 Nov  6  1996 spanishn.xbm
-rw-r--r--   1 spectre  staff   2341 Nov  6  1996 spanishy.xbm
-rw-r--r--   1 spectre  staff  40387 Nov  6  1996 swedish.gif
-rw-r--r--   1 spectre  staff   2344 Nov  6  1996 swedishn.xbm
-rw-r--r--   1 spectre  staff   2344 Nov  6  1996 swedishy.xbm

lib/legal/full:
total 0
drwxr-xr-x   3 spectre  staff   96 Jan 23  1997 .
drwxr-xr-x   4 spectre  staff  128 Jan 23  1997 ..
drwxr-xr-x  24 spectre  staff  768 Jan 23  1997 bitmaps

lib/legal/full/bitmaps:
total 840
drwxr-xr-x  24 spectre  staff    768 Jan 23  1997 .
drwxr-xr-x   3 spectre  staff     96 Jan 23  1997 ..
-rw-r--r--   1 spectre  staff  48468 Nov  6  1996 dutch.gif
-rw-r--r--   1 spectre  staff   2335 Nov  6  1996 dutchn.xbm
-rw-r--r--   1 spectre  staff   2335 Nov  6  1996 dutchy.xbm
-rw-r--r--   1 spectre  staff  41700 Nov  6  1996 english.gif
-rw-r--r--   1 spectre  staff  44834 Nov  6  1996 french.gif
-rw-r--r--   1 spectre  staff   2338 Nov  6  1996 frenchn.xbm
-rw-r--r--   1 spectre  staff   2338 Nov  6  1996 frenchy.xbm
-rw-r--r--   1 spectre  staff  44130 Nov  6  1996 german.gif
-rw-r--r--   1 spectre  staff   2338 Nov  6  1996 germann.xbm
-rw-r--r--   1 spectre  staff   2338 Nov  6  1996 germany.xbm
-rw-r--r--   1 spectre  staff  44990 Nov  6  1996 italian.gif
-rw-r--r--   1 spectre  staff   2341 Nov  6  1996 italiann.xbm
-rw-r--r--   1 spectre  staff   2341 Nov  6  1996 italiany.xbm
-rw-r--r--   1 spectre  staff  37978 Nov  6  1996 japanese.gif
-rw-r--r--   1 spectre  staff   2344 Nov  6  1996 japanesen.xbm
-rw-r--r--   1 spectre  staff   2344 Nov  6  1996 japanesey.xbm
-rw-r--r--   1 spectre  staff  52482 Nov  6  1996 spanish.gif
-rw-r--r--   1 spectre  staff   2341 Nov  6  1996 spanishn.xbm
-rw-r--r--   1 spectre  staff   2341 Nov  6  1996 spanishy.xbm
-rw-r--r--   1 spectre  staff  47592 Nov  6  1996 swedish.gif
-rw-r--r--   1 spectre  staff   2344 Nov  6  1996 swedishn.xbm
-rw-r--r--   1 spectre  staff   2344 Nov  6  1996 swedishy.xbm

lib/locale:
total 0
drwxr-xr-x   3 spectre  staff   96 Jan 23  1997 .
drwxr-xr-x  11 spectre  staff  352 Jan 23  1997 ..
drwxr-xr-x   2 spectre  staff   64 Jan 23  1997 mae

lib/locale/mae:
total 0
drwxr-xr-x  2 spectre  staff  64 Jan 23  1997 .
drwxr-xr-x  3 spectre  staff  96 Jan 23  1997 ..
After installation
Default_MIV_file
also lives in
/opt/apple/lib
, and optionally
AliasList
for default aliases to appear when starting MAE.
To reduce the size of individual users' System Folders, a substantial portion of the composite MAE System Folder is pulled from the
shared
directory, and other pieces from
/opt/apple/lib/data
.
% ls -alR shared
total 5424
drwxr-xr-x   9 spectre  staff      288 Nov  8  1996 .
drwxr-xr-x   7 spectre  staff      224 Aug  1 09:24 ..
-rw-r--r--   1 spectre  staff    46942 Nov  6  1996 About Apple Guide
-rw-r--r--   1 spectre  staff   268047 Nov  6  1996 Find File
-rw-r--r--   1 spectre  staff  1860608 Nov 14  1996 MAE Guide
-rw-r--r--   1 spectre  staff   126881 Nov  6  1996 MAE Shortcuts
drwxr-xr-x  38 spectre  staff     1216 Nov  6  1996 Printer Descriptions
-rw-r--r--   1 spectre  staff   366816 Nov  6  1996 SimpleText Guide
-rw-r--r--   1 spectre  staff    97701 Nov  6  1996 Stickies

shared/Printer Descriptions:
total 2840
drwxr-xr-x  38 spectre  staff   1216 Nov  6  1996 .
drwxr-xr-x   9 spectre  staff    288 Nov  8  1996 ..
-rw-r--r--   1 spectre  staff  29587 Nov  6  1996 HP DeskJet 1600CM
-rw-r--r--   1 spectre  staff  17797 Nov  6  1996 HP LaserJet 4 Plus
-rw-r--r--   1 spectre  staff  17740 Nov  6  1996 HP LaserJet 4MP
-rw-r--r--   1 spectre  staff  34220 Nov  6  1996 HP LaserJet 5M
-rw-r--r--   1 spectre  staff  26131 Nov  6  1996 HP LaserJet 5MP
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter
-rw-r--r--   1 spectre  staff  81600 Nov  6  1996 LaserWriter 12:640 PS
-rw-r--r--   1 spectre  staff  65737 Nov  6  1996 LaserWriter 16:600 PS
-rw-r--r--   1 spectre  staff  65737 Nov  6  1996 LaserWriter 16:600 PS Fax
-rw-r--r--   1 spectre  staff  65737 Nov  6  1996 LaserWriter 16:600 PS-J
-rw-r--r--   1 spectre  staff  30740 Nov  6  1996 LaserWriter 4:600 PS
-rw-r--r--   1 spectre  staff  32665 Nov  6  1996 LaserWriter Color 12:600 PS
-rw-r--r--   1 spectre  staff  32665 Nov  6  1996 LaserWriter Color 12:600 PS-J
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter II NT
-rw-r--r--   1 spectre  staff  17940 Nov  6  1996 LaserWriter II NTX
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter II NTX v50.5
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter II NTX v51.8
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter II NTX-J v50.5
-rw-r--r--   1 spectre  staff  56521 Nov  6  1996 LaserWriter IIf v2010.113
-rw-r--r--   1 spectre  staff  57545 Nov  6  1996 LaserWriter IIf v2010.130
-rw-r--r--   1 spectre  staff  57545 Nov  6  1996 LaserWriter IIg v2010.113
-rw-r--r--   1 spectre  staff  57545 Nov  6  1996 LaserWriter IIg v2010.130
-rw-r--r--   1 spectre  staff  57545 Nov  6  1996 LaserWriter Personal 320
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter Personal NT
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter Personal NTR
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter Plus v38.0
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter Plus v42.2
-rw-r--r--   1 spectre  staff  22548 Nov  6  1996 LaserWriter Pro 400 v2011.110
-rw-r--r--   1 spectre  staff  26132 Nov  6  1996 LaserWriter Pro 405 v2011.110
-rw-r--r--   1 spectre  staff  57545 Nov  6  1996 LaserWriter Pro 600 v2010.130
-rw-r--r--   1 spectre  staff  57545 Nov  6  1996 LaserWriter Pro 630 v2010.130
-rw-r--r--   1 spectre  staff  40704 Nov  6  1996 LaserWriter Pro 810
-rw-r--r--   1 spectre  staff  40704 Nov  6  1996 LaserWriter Pro 810f
-rw-r--r--   1 spectre  staff  44935 Nov  6  1996 LaserWriter Select 360
-rw-r--r--   1 spectre  staff  44935 Nov  6  1996 LaserWriter Select 360f
-rw-r--r--   1 spectre  staff  30740 Nov  6  1996 LaserWriter Select 610
/opt/apple/lib/data
contains the rest of the System Folder, with common pieces like the System 7.5 jigsaw puzzle (licensed by Apple from Captain's Software), note pad (Light Software), scrapbook, menu bar clock (from Steve Christensen's SuperClock!), desktop patterns, compressed System resources and standard INITs and CDEVs.
/opt/apple/sys
, however, which we won't do much more with here, is the master template for creating each user's own System Folder. We don't need to look at it again because we already saw my own copy of it.
/opt/apple/lib/engine
is a mashup of many miscellaneous tools. There are various conglomated binaries in it ratted out by the presence of
.text
,
.data
and
.bss
, plus the fake DeclROM for the virtual video card and the Quadra 660AV/840AV Toolbox ROM it uses. There are also many other interesting strings, and being a 10MB file, there are a lot of them:
% strings engine | fgrep '$Id:'
$Id: filesystems.c,v 3.22 1996/10/27 04:03:36 mg Exp $
$Id: 
$Id: adb.c,v 3.0 1995/03/23 20:49:59 cvs Exp $
$Id: aliases.c,v 3.28 1996/11/08 22:07:04 jerry Exp $
$Id: aux.c,v 3.28 1996/10/22 21:12:05 mg Exp $
$Id: both.c,v 3.22 1997/01/14 03:25:49 johng Exp $
$Id:
$Id: cursor.c,v 3.12 1996/12/13 21:44:52 johng Exp $
$Id: devmgr.c,v 3.5 1996/09/24 21:24:15 gwiesner Exp $
$Id: dialog.c,v 3.2 1996/05/31 04:47:57 mg Exp $
$Id: displaymgr.c,v 3.2 1996/06/16 06:10:00 johng Exp $
$Id: eventmgr.c,v 3.0 1995/03/23 20:50:19 cvs Exp $
$Id: fm_fsm.c,v 3.7 1996/08/21 01:43:24 jerry Exp $
$Id: foldermanager.c,v 3.10 1996/08/14 16:40:03 jerry Exp $
$Id: fsprefs.c,v 3.8 1996/11/09 00:31:34 mfc Exp $
$Id: gestalt.c,v 3.4 1996/08/15 19:18:27 maryc Exp $
$Id: macdriver.c,v 3.9 1996/11/09 00:31:33 mfc Exp $
r$Id: machine.c,v 3.4 1996/09/26 07:21:40 shin Exp $
$Id: macopen.c,v 3.2 1996/10/23 17:40:31 mfc Exp $
$Id: maxbug.c,v 3.0 1995/03/23 20:50:32 cvs Exp $
$Id: memmgr.c,v 3.2 1996/05/07 00:32:55 shin Exp $
$Id: misc.c,v 3.3 1996/06/06 20:29:23 mg Exp $
$Id: nmgr.c,v 3.0 1995/03/23 20:50:40 cvs Exp $
$Id: pinitmac.c,v 3.23 1996/11/05 01:37:04 shin Exp $
$Id: printing.c,v 3.1 1996/05/07 00:34:39 shin Exp $
$Id: romutil.c,v 3.2 1996/07/23 11:48:50 johng Exp $
$Id: scrapmgr.c,v 3.5 1996/03/11 22:25:32 jerry Exp $
$Id: shutup.c,v 3.2 1996/08/21 01:43:26 jerry Exp $
U$Id: signal.c,v 3.3 1996/05/07 00:51:10 shin Exp $
$Id: sigsupport.c,v 2.1 1996/01/26 17:50:37 jhudgins Exp $
$Id: slot.c,v 3.1 1996/06/01 22:47:58 gwiesner Exp $
$Id: sonydriver.c,v 3.3 1996/11/01 07:17:25 mfc Exp $
$Id: startmac.c,v 3.9 1997/01/14 02:37:04 johng Exp $
$Id: strings.c,v 3.2 1996/07/23 16:34:09 johng Exp $
$Id: table.c,v 3.1 1996/09/04 20:25:59 johng Exp $
$Id: timemgr.c,v 3.4 1996/09/20 04:30:52 skate Exp $
$Id: video.c,v 3.4 1996/09/12 22:54:16 skate Exp $
$Id: virtpram.c,v 3.2 1996/03/19 20:00:15 jerry Exp $
$Id: vm.c,v 3.0 1995/03/23 20:51:12 cvs Exp $
$Id: window.c,v 3.0 1995/03/23 20:51:14 cvs Exp $
$Id: xccm.c,v 3.3 1996/05/07 20:23:03 johng Exp $
$Id: xconv.c,v 3.1 1996/05/07 20:23:04 johng Exp $
$Id: xevent.c,v 3.25 1996/10/31 11:11:39 skate Exp $
$Id: ximage.c,v 3.24 1996/10/15 09:58:36 johng Exp $
$Id: ximage_colors.c,v 3.1 1996/01/26 04:12:01 johng Exp $
$Id: ximage_high.c,v 3.6 1996/09/11 08:19:50 johng Exp $
$Id: ximage_icon.c,v 3.0 1995/03/23 20:51:23 cvs Exp $
$Id: ximage_macdrvr.c,v 3.7 1996/10/25 17:59:47 skate Exp $
$Id: ximage_macui.c,v 3.2 1996/05/30 09:35:06 johng Exp $
$Id: ximage_scale.c,v 3.4 1996/11/05 00:33:04 johng Exp $
$Id: ximage_set_tear.c,v 3.14 1996/10/17 04:32:26 johng Exp $
$Id: ximage_tables.c,v 3.3 1996/04/11 16:12:58 johng Exp $
$Id: ximage_transmit.c,v 3.30 1996/11/06 02:34:09 johng Exp $
$Id: ximage_util.c,v 3.5 1996/09/20 04:30:55 skate Exp $
$Id: ximage_xform.c,v 3.1 1996/03/15 12:17:09 johng Exp $
$Id: ximageopt.c,v 3.38 1996/10/15 01:13:10 johng Exp $
$Id: xkeyboard.c,v 3.30 1996/11/21 23:09:36 jerry Exp $
$Id: xpixmap.c,v 3.0 1995/03/23 20:51:36 cvs Exp $
$Id: xselection.c,v 3.3 1996/07/25 22:33:52 johng Exp $
$Id: xsupersel.c,v 3.1 1995/11/21 21:47:56 scp Exp $
$Id: xtoolbar.c,v 3.7 1996/10/13 09:43:29 johng Exp $
$Id: xutil.c,v 3.0 1995/03/23 20:51:51 cvs Exp $
$Id: driverutils.c,v 3.0 1995/03/23 20:47:38 cvs Exp $
$Id: ether.c,v 3.0 1995/03/23 20:47:39 cvs Exp $
$Id: icmp.c,v 3.2 1996/09/10 18:52:40 maryc Exp $
$Id: mactcp.c,v 3.4 1996/06/12 00:25:55 maryc Exp $
$Id: mactcpctl.c,v 3.1 1996/06/12 00:25:56 maryc Exp $
$Id: mactcpdrvr.c,v 3.1 1996/02/26 22:55:30 maryc Exp $
$Id: tcp.c,v 3.8 1996/10/02 00:05:35 maryc Exp $
$Id: tcputil.c,v 3.6 1996/10/02 00:05:31 maryc Exp $
$Id: udp.c,v 3.3 1996/08/16 19:48:20 maryc Exp $
$Id: udputil.c,v 3.1 1996/06/12 00:25:54 maryc Exp $
$Id: utils.c,v 3.3 1996/06/12 00:25:58 maryc Exp $
% strings engine
[...]
Copyright 1988 Apple Computer, Inc.
[...]
B-Tree overflow.
type = %s n_records = %d
[...]
ordering wrong
Oh no!
Here's the left leaf
Here's the problem leaf
[...]
%d block%s.
%d record%s.  
%d lea%s.  
%d branch%s.
.fs_cache
>> Making a new cache database <<
.fs_dirIDs
** Unable to restore from backup **
FS CACHE INFO:
vers: %d
next dirID: %d
last cnid saved: %d
-> DirID = %x is UNKNOWN!!!! <-
[...]
/usr/vice/etc/ThisCell
%s/%s
%s/%s
/usr/vice/etc/CellNamesMAE
%s/%s
CellNamesMAE
%s/%s
CellNamesMAE
[...]
File "%s" has invalid information in it. 
 Try rebuilding your .mac directory.  
The following line in the .MIV_file is invalid because it refers to one
of the special MAE directories.  You cannot create a MIV for the apple
directory, .mac directory, or system folder.  You also cannot create a
MIV for any directory enclosed in one of the MAE special directories.
This line will be ignored until the problem is corrected.
"%d:%s"
The following line in the .MIV_file references the same directory as
a line which was already processed. The pathnames of these duplicates may
not be identical in the .MIV_file if symbolic links or the '~' character
were used.
This line will be ignored until the problem is corrected.
"%d:%s"
Your .macdir is not at the root of a Mac volume.
You will have Apple file sharing problems using this configuration.
[...]
 You have exceeded the maximum number of open files on this workstation.
 This is a serious error.
 MAE may not be able to function if it cannot open critical system files.
 Shut down MAE immediately.
 Refer to the MAE Administrator's Manual for more information about this
 error. 
[...]
ck_asd_header: ASD Header corrupt. Overlapping blocks
cith
/mac/sys/System Folder
[...]
UNIX vol name = '%.*s'
 You have exceeded the maximum number of mounted volumes.
 The mount for '%s' has failed.
 Unmount unneeded volumes by dragging their icon to the trash. 
Opened '%s', fork ID = %d, perm = %d[rn = %d]
** Unable to find FCB for vfile '%s' (%d)? **
Close: file '%.*s'[rn = %d]
[...]
cithSHEL
!<arch>
070707
#!/bin/sh
#!/bin/csh
#!/bin/ksh
#!/bin/tsh
#!/bin/bsh
#!/bin/tcsh
<aiaff>
070707
#!/bin/sh
#!/bin/csh
#!/bin/ksh
#!/bin/tsh
#!/bin/bsh
#!/bin/tcsh
[...]
AUX_SET_SELRECT
AUX_CHECK_KIDS
AUX_GET_UDEVFD
AUX_SWITCH
AUX_GETTASK
AUX_GETANYEVENT
AUX_SETAUXMASK
AUX_STOPTIMER
AUX_STARTTIMER
AUX_SETTIMEOUT
AUX_SETBOUNDS
[...]
usage:  %s [-options ...]
where options include:
    -display dpy                X server on which to display
    -geometry WxH+X+Y           size and location of window
                                  (Mae.geometry)
[...]
XS - unsuccessful attempt to send_message to MACD. - sent %d bytes
get_message:readn
XS - unsuccessful readn(read %d chars, expected 4).
XS - unsuccessful get_message attempt from MACD, nread=%d.
[...]
MAE Video
Apple Computer
Rev 2.0
June 13, 1994
512 x 342 (9" Macintosh)
640 x 480 (14" Macintosh)
832 x 624 (17" Macintosh)
864 x 864 Resolution
640 x 800 Resolution
640 x 640 Resolution
Display_Video_Apple_MAE_S
Display_Video_Apple_MAE_M
Display_Video_Apple_MAE_L
Display_Video_Apple_MAE_F
Display_Video_Apple_MAE_C1
Display_Video_Apple_MAE_C2
[...]
/mac/ROMMondo is wrong size
[...]
small_decomp_rle_6(): Holy shit!  Contaminated data.
[...]
Exit due to signal (%d) at PC=0x%x, bad address = 0x%x %s
sigsetmask failed in signal handler
unexpected handler(0x%08x) result (%d)
sigsetmask failed in signal handler
[...]
You will not be able to use Macintosh floppies with MAE because Solaris' Volume Manager is not available now.
See vold(1M) to learn how to start the Volume Manager.
[...]
/bin/cp %s %s
Copy failed: (%d)
%s/%s
/bin/rm -rf %s
Remove failed: (%d)
/bin/rm -rf %s
Remove failed: (%d)
%s/%s
/bin/mv %s %s
Move failed: (%d)
/bin/mv %s %s 1>/dev/null 2>&1
Move failed: (%d)
[...]
cGetDevPixmap, could not emulate Macintosh color table (%d), exiting.
cGetDevPixmap, unknown depth %d in encountered.
doVideo, error installing video driver, exiting.
doVideo, error initializing NewGDevice, exiting.
doVideo, could not emulate any Macintosh video devices.
Insufficient shared memory or swap space.  Using malloc instead.  
Performance could be increased by adding more swap space and/or
configuring more shared memory into the kernel.
ERROR: MAE could not allocate the video screen (%dx%d, %dk).
Please increase swap space or kill other processes before restarting MAE.
Could not malloc new screen buffer, restoring previous size.
Not enough shared memory, using malloc instead.  Performance would be
increased by configuring more shared memory into the kernel.
[...]
BUGS on MacPlus/SE, NuMc on later
[...]
Got the OKAY to clear %s (0x%02x bytes at pram 0x%02x) - 
[...]
QDtoGC: (penMode & kHilitePenModeMask); *punting*
QDtoGC: penmode=invert (but not well matched); *punting*
[...]
Aae:  AAAAARGH!  Fatal X Error
[...]
Copyright (c) 1987 Apple Computer, Inc., 1985 Adobe Systems Incorporated, 1983-87 AT&T-IS, 1985-87 Motorola Inc., 1980-87 Sun Microsystems Inc., 1980-87 The Regents of the University of California, 1985-87 Unisoft Corporation, All Rights Reserved.
[...]
This file also contains X bitmaps for the Apple logo, both black and white and colour, in several places.
36 41 2 1
  c #FFFFFFFFFFFF
. c #000000000000
                                    
                                    
                                    
                                    
                      ...           
                     ....           
                    .....           
                   .....            
                   .....            
                  .....             
                  ....              
                  ..                
          ......     ......         
        .......... ..........       
       .......................      
      .........................     
      .......................       
     .......................        
     .......................        
     ......................         
     ......................         
     ......................         
     ......................         
     .......................        
      ......................        
      .......................       
      .........................     
       .......................      
       .......................      
        .....................       
        ....................        
         ...................        
          ........ ........         
            ....     ....           
                                    
                                    
                                    
                                    
                                    
                                    
                                    
36 41 9 1
c #FFFFFFFFFFFF
c #0000BBBB0000
c #FFFFFFFF0000
c #FFFF66663333
c #FFFF64640202
c #DDDD00000000
c #999900006666
c #999900009999
c #00000000DDDD
                                    
                                    
                                    
                                    
                                    
                      ...           
                     ....           
                    .....           
                   .....            
                   .....            
                  .....             
                  ....              
                  ..                
          ......     ......         
        .......... ..........       
       .......................      
      ........................      
      XXXXXXXXXXXXXXXXXXXXXXX       
     XXXXXXXXXXXXXXXXXXXXXXX        
     XXXXXXXXXXXXXXXXXXXXXX         
     oOOOOOOOOOOOOOOOOooooo         
     oOOOOOOOOOOOOOOOOOOOOo         
     oOOOOOOOOOOOOOOOOOOOOo         
     oOOOOOOOOOOOOOOOOOOOOOo        
     +++++++++++++++++++++++        
      ++++++++++++++++++++++        
      +++++++++++++++++++++++       
      ++@+@+@+@+@+@+@+@+@+@+@+      
       @@@@@@@@@@@@@@@@@@@@@@@      
       @@@@@@@@@@@@@@@@@@@@@@       
        @@@@@@@@@@@@@@@@@@@@#       
        $$$$$$$$$$$$$$$$$$$$        
         $$$$$$$$$$$$$$$$$$         
          $$$$$$$$ $$$$$$$          
            $$$$     $$$$           
                                    
                                    
                                    
                                    
                                    
                                    
# CREATOR: MAE 3.0
%d %d
%3d %3d %3d 
GIF87a
$Id: ximage_high.c,v 3.6 1996/09/11 08:19:50 johng Exp $
$Id: ximage_icon.c,v 3.0 1995/03/23 20:51:23 cvs Exp $
X36 41 2 1
  c #FFFFFFFFFFFF
. c #000000000000
                                    
                                    
                                    
                                    
                      ...           
                     ....           
                    .....           
                   .....            
                   .....            
                  .....             
                  ....              
                  ..                
          ......     ......         
        .......... ..........       
       .......................      
      .........................     
      .......................       
     .......................        
     .......................        
     ......................         
     ......................         
     ......................         
     ......................         
     .......................        
      ......................        
      .......................       
      .........................     
       .......................      
       .......................      
        .....................       
        ....................        
         ...................        
          ........ ........         
            ....     ....           
                                    
                                    
                                    
                                    
                                    
                                    
                                    
36 41 9 1
c #FFFFFFFFFFFF
c #0000BBBB0000
c #FFFFFFFF0000
c #FFFF66663333
c #FFFF64640202
c #DDDD00000000
c #999900006666
c #999900009999
c #00000000DDDD
                                    
                                    
                                    
                                    
                                    
                      ...           
                     ....           
                    .....           
                   .....            
                   .....            
                  .....             
                  ....              
                  ..                
          ......     ......         
        .......... ..........       
       .......................      
      ........................      
      XXXXXXXXXXXXXXXXXXXXXXX       
     XXXXXXXXXXXXXXXXXXXXXXX        
     XXXXXXXXXXXXXXXXXXXXXX         
     oOOOOOOOOOOOOOOOOooooo         
     oOOOOOOOOOOOOOOOOOOOOo         
     oOOOOOOOOOOOOOOOOOOOOo         
     oOOOOOOOOOOOOOOOOOOOOOo        
     +++++++++++++++++++++++        
      ++++++++++++++++++++++        
      +++++++++++++++++++++++       
      ++@+@+@+@+@+@+@+@+@+@+@+      
       @@@@@@@@@@@@@@@@@@@@@@@      
       @@@@@@@@@@@@@@@@@@@@@@       
        @@@@@@@@@@@@@@@@@@@@#       
        $$$$$$$$$$$$$$$$$$$$        
         $$$$$$$$$$$$$$$$$$         
          $$$$$$$$ $$$$$$$          
            $$$$     $$$$           
                                    
                                    
                                    
                                    
                                    
                                    
PaintIconIntoImage, unknown message type %d.
%d %d %d
Unable to get Icon window id from MACD, exiting.
Another set of credits appears here,
The SuperROM SuperTeam:
Central:
Ricardo Batista, Rich Biasi, Philip Nguyen, Roger Mann
Kurt Clark, Chas Spillar, Paul Wolf, Clinton Bauder
Giovanni Agnoli and Debbie Lockett
RISC:
Scott Boyd, Tim Nichols and Steve Smith
MSAD:
Jeff Miller and Fred Monroe
Cyclone:
Tony Leung, Greg Schroeder, Mark Law, Fernando Urbina
Dan Hitchens, Jeff Boone, Craig Prouse, Eric Behnke
Mike Bell, Mike Puckett, William Sheet, Robert Polic
and Kevin Williams
Thankzzz to all who contributed to past ROMs...and System 7.x
but it's the same credits as in the regular Quadra ROM we know it's already using.
Next we'll go through the main binaries, starting with
legal
, which is the program that requires you to accept the EULA on first run.
% strings legal | fgrep '$Id:'
# $Id: ui.tcl,v 1.11 1996/06/14 03:01:22 johng Exp $
% strings legal
$Revision: 92453-07 linker linker crt0.o A.10.44 951031 $
/usr/lib/dld.sl
ERROR: mmap failed for dld
Error
TCL_LIBRARY=/tmp
TK_LIBRARY=/tmp
set file %s
Error
wrong # args (must be 1)
font_exists
#!/usr/bin/wish -f
# Created Fri Jan 12 16:05:53 1996  John Grabowski <johng@jet.mae.apple.com>
# $Id: ui.tcl,v 1.11 1996/06/14 03:01:22 johng Exp $
[...]
proc no_more_wait {} {
    destroy .wait
# Since english is so fast, we don't put up a wait dialog.
# please_wait english 1
############################################################
set english_message_demo "\
ENGLISH
Apple Computer, Inc. Software License
PLEASE READ THIS SOFTWARE LICENSE AGREEMENT \"LICENSE\" CAREFULLY BEFORE DOWNLOA
DING THE SOFTWARE.  BY DOWNLOADING THE SOFTWARE, YOU ARE AGREEING TO BE BOUND BY
 THE TERMS OF THIS LICENSE.  IF YOU DO NOT AGREE TO THE TERMS OF THIS LICENSE, Y
OU ARE NOT AUTHORIZED TO DOWNLOAD THIS SOFTWARE.
[...]
% strings appleping
$Revision: 92453-07 linker linker crt0.o A.10.44 951031 $
/usr/lib/dld.sl
ERROR: mmap failed for dld
Usage:  appleping net.node [data size] [npackets]
   or:  appleping name:type@zone [data size] [npackets]
examples:  appleping 'John Sculley:Macintosh SE@Pepsi' 
      or:  appleping 6b16.54 
appleping: nbp_parse_entity
appleping: nbp_lookup
appleping: Can't find %s
Pinging %04.4x.%02.2x.04
%x.%x
appleping: ddp_open
Pinging %s: %d data bytes
appleping: read
appleping: write
appleping: wrote %s %d chars, ret=%d
%d bytes from %04.4x.%02.2x.%02.2x: 
hop=%2d, 
time=%4d. ms
----%s ApplePing Statistics----
%d packets transmitted, 
%d packets received, 
%d%% packet loss
round-trip (ms)  min/avg/max = %d/%d/%d
hop-count        min/avg/max = %d/%d/%d
@(#)appleping.c: 3.0d1, 1.6; 7/18/89; Copyright 1988-89, Apple Computer, Inc.
nbp_send failed, errno is %d  
/dev/appletalk/ddp/socket
max <= 0 
DDPopen failed 
validate entity failed 
HP92453-02A.10.00 HP-UX SYMBOLIC DEBUGGER (END.O) $Revision: 74.03 $
% strings appletalk
$Revision: 92453-07 linker linker crt0.o A.10.44 951031 $
/usr/lib/dld.sl
ERROR: mmap failed for dld
usage: %s [-n] [-s] [-u] [-b interface] [-p] [-D] 
        -n print initial and current AppleTalk address
        -s print AppleTalk statistics and error counts for this node
        -u bring-up AppleTalk services on the specified interface
        -b specify the network interface to use when bringing-up AppleTalk with the '-u' option
        -p print saved AppleTalk PRAM information
        -D force shutdown of AppleTalk services for this node
One or more instances of Macintosh Application Environment may be running. 
Results of forcing down the AppleTalk stack are unpredicable. 
Would you like to continue [y/n]?
lan0
:nmDusb:p
%s: -u and -d options are incompatible
%s: -b & -z options can only be used with -u option
ethertalk
ethertalk
%s: option -z applicable only to ethertalk
%s: option -b applicable only to ethertalk
AppleTalk interface: LocalTalk
AppleTalk interface: EtherTalk
[...]
% strings atlookup
[...]
@(#)atlookup.c: 3.0d1, 1.16; 8/1/90; Copyright 1988-89, Apple Computer, Inc.
ITEM 
   NET-ADDR  
 NET-ADDR 
    OBJECT : TYPE @ ZONE
    OBJECT : TYPE
%3d: 
%05.5d.%03.3d.%03.3d 
%04.4x.%02.2x.%02.2x 
0123456789ABCDEF
@(#)tuple_pr.c: 3.0d1, 1.4; 8/1/90; Copyright 1988-89, Apple Computer, Inc.
[...]
legal
in particular looks like it's just an embedded Tcl/Tk script. It's also notable that
appleping
,
appletalk
,
atlookup
,
asdtool
and
legal
still have symbol tables. The AppleTalk tools in particular list functions related to DDP, LAP, NBP and RTMP, but you'd expect that (
legal
has symbols for Tcl/Tk instead). Interestingly, a few of the strings in
appletalk
suggest that LocalTalk might have been, or at least was considered for being, supported at one time.
Although
mae
is the binary that you run directly,
macd
is what handles a lot of the background stuff and
mae
communicates with it over IPC. The administrator's manual is (probably intentionally) vague about its exact functions, saying only that it "is a daemon that runs whenever
apple/bin/mae
runs and helps MAE interact with the UNIX environment. It also cleans up after
mae
if the
mae
process is killed." We can get a little better idea of what it does from its own set of strings at least:
% nm macd
nm:  macd:  no symbols
% strings macd | fgrep '$Id:'
@(#)$Id: macd.c,v 3.17 1997/03/26 01:25:19 mg Exp $
% strings macd
$Revision: 92453-07 linker linker crt0.o A.10.44 950920 $
[...]
TBNOATINIT
ethertalk0
MACD - COULDN'T GET MEMORY FOR ip STRUCT
RENAME ERROR %s %s %s
/tmp/fid_log
MACD: Unexpected end of data error in FileIDs.
/FileIDs
MACD - unsuccessful send_message() to xstartmac. - sent %d bytes
MACD: couldn't read length of message
MACD - unsuccessful get_message from xstartmac. - read %d
MACD - couldn't read length of message
MACD - unsuccessful get_message_mb from xstartmac. - read %d
writen
readn
MACD - failure to get command in do_system.
FAILURE
/bin/sh
SUCCESS
MACD - failure in get_perm_win_id().
MACD - failure in get_toolbar_height().
MACD - failure in get_SFlockfile.
MACD - failure in get_DMlockfile.
MACD - failure in get_container_info.
MACD - Couldn't open Display
can't open display, name: %s:
[...]
SOFTMAC_RESTARTING_NOW
macd: Please unset "SOFTMAC_RESTARTING_NOW".
macd: Please don't execute this command directly!
[...]
The MAE 3.0 Team
Peter Blas, Michael Brenner, Matthew Caprile, Mary Chan, Bill Convis
Jerry Cottingham, Ivan Drucker, Gerri Eaton, Tim Gilman, Gary Giusti
Mark Gorlinsky, John Grabowski, Cindi Hollister, Richard W. Johnson
John Kullmann, Tom Molnar, John Morley, Stephen Nelson, Michael Press
Jeff Roberts, Shinji Sato, Marc Sinykin, Earl Wallace, Gayle Wiesner
[...]
One or more instances of Macintosh Application Environment may be running. 
Results of forcing down the AppleTalk stack are unpredicable. 
[...]
Permission denied; must be a super-user to use the -D option.
Continuing with shutdown...
appletalk: interface %s is not running 
%s/%s/%s
/dev/appletalk/lap
control
Unable to configure the AppleTalk kernel modules.
No such interface, please specify a valid lan interface to use.
Unable to start up AppleTalk. 
 Starting over with the zone list...
[...]
MacsBug
MacsBug @ 
monaco-9
Inside Macsbug code, XLoadQueryFont protocol error.
-misc-fixed-medium-r-semicondensed--13-120-75-75-c-60-iso8859-1
Inside Macsbug code, XLoadQueryFont protocol err2.
fixed
Inside Macsbug code, XLoadQueryFont protocol err3.
Could not allocate fixed font, so Macsbug will not
be able to draw any characters.
[...]
And now
mae
itself. Some of these strings and components are duplicative of what we saw in
/opt/apple/lib/engine
. I'm not sure why they're being used twice.
% nm mae
nm:  mae:  no symbols
% strings mae | fgrep '$Id:'
$Id: filesystems.c,v 3.22 1996/10/27 04:03:36 mg Exp $
$Id: 
$Id: adb.c,v 3.0 1995/03/23 20:49:59 cvs Exp $
$Id: aliases.c,v 3.29 1997/01/22 02:24:32 shin Exp $
$Id: aux.c,v 3.31 1997/01/23 18:35:05 jerry Exp $
$Id: both.c,v 3.24 1997/04/04 19:14:50 skate Exp $
$Id:
$Id: cursor.c,v 3.12 1996/12/13 21:44:52 johng Exp $
$Id: devmgr.c,v 3.5 1996/09/24 21:24:15 gwiesner Exp $
$Id: dialog.c,v 3.2 1996/05/31 04:47:57 mg Exp $
$Id: displaymgr.c,v 3.2 1996/06/16 06:10:00 johng Exp $
$Id: eventmgr.c,v 3.0 1995/03/23 20:50:19 cvs Exp $
$Id: fm_fsm.c,v 3.8 1997/02/06 02:26:37 gwiesner Exp $
$Id: foldermanager.c,v 3.10 1996/08/14 16:40:03 jerry Exp $
$Id: fsprefs.c,v 3.9 1997/04/15 00:39:28 mfc Exp $
$Id: gestalt.c,v 3.4 1996/08/15 19:18:27 maryc Exp $
$Id: macdriver.c,v 3.10 1997/04/08 01:42:28 gwiesner Exp $
r$Id: machine.c,v 3.5 1997/02/12 01:45:00 johng Exp $
$Id: macopen.c,v 3.2 1996/10/23 17:40:31 mfc Exp $
$Id: maxbug.c,v 3.0 1995/03/23 20:50:32 cvs Exp $
$Id: memmgr.c,v 3.2 1996/05/07 00:32:55 shin Exp $
$Id: misc.c,v 3.3 1996/06/06 20:29:23 mg Exp $
$Id: nmgr.c,v 3.0 1995/03/23 20:50:40 cvs Exp $
$Id: pinitmac.c,v 3.24 1997/01/22 02:25:19 shin Exp $
$Id: printing.c,v 3.1 1996/05/07 00:34:39 shin Exp $
$Id: romutil.c,v 3.2 1996/07/23 11:48:50 johng Exp $
$Id: scrapmgr.c,v 3.5 1996/03/11 22:25:32 jerry Exp $
$Id: shutup.c,v 3.2 1996/08/21 01:43:26 jerry Exp $
U$Id: signal.c,v 3.3 1996/05/07 00:51:10 shin Exp $
$Id: sigsupport.c,v 2.1 1996/01/26 17:50:37 jhudgins Exp $
$Id: slot.c,v 3.1 1996/06/01 22:47:58 gwiesner Exp $
$Id: sonydriver.c,v 3.7 1997/03/20 06:47:39 gwiesner Exp $
$Id: startmac.c,v 3.10 1997/02/12 01:45:01 johng Exp $
$Id: strings.c,v 3.2 1996/07/23 16:34:09 johng Exp $
$Id: table.c,v 3.1 1996/09/04 20:25:59 johng Exp $
$Id: timemgr.c,v 3.6 1996/12/05 15:20:31 johng Exp $
$Id: video.c,v 3.4 1996/09/12 22:54:16 skate Exp $
$Id: virtpram.c,v 3.3 1997/02/19 22:57:33 jerry Exp $
$Id: vm.c,v 3.0 1995/03/23 20:51:12 cvs Exp $
$Id: window.c,v 3.0 1995/03/23 20:51:14 cvs Exp $
$Id: xccm.c,v 3.3 1996/05/07 20:23:03 johng Exp $
$Id: xconv.c,v 3.1 1996/05/07 20:23:04 johng Exp $
$Id: xevent.c,v 3.27 1997/02/18 19:38:03 skate Exp $
$Id: ximage.c,v 3.24 1996/10/15 09:58:36 johng Exp $
$Id: ximage_colors.c,v 3.1 1996/01/26 04:12:01 johng Exp $
$Id: ximage_high.c,v 3.6 1996/09/11 08:19:50 johng Exp $
$Id: ximage_icon.c,v 3.0 1995/03/23 20:51:23 cvs Exp $
$Id: ximage_macdrvr.c,v 3.7 1996/10/25 17:59:47 skate Exp $
$Id: ximage_macui.c,v 3.2 1996/05/30 09:35:06 johng Exp $
$Id: ximage_scale.c,v 3.4 1996/11/05 00:33:04 johng Exp $
$Id: ximage_set_tear.c,v 3.14 1996/10/17 04:32:26 johng Exp $
$Id: ximage_tables.c,v 3.3 1996/04/11 16:12:58 johng Exp $
$Id: ximage_transmit.c,v 3.30 1996/11/06 02:34:09 johng Exp $
$Id: ximage_util.c,v 3.9 1996/12/05 16:58:26 johng Exp $
$Id: ximage_xform.c,v 3.1 1996/03/15 12:17:09 johng Exp $
$Id: ximageopt.c,v 3.38 1996/10/15 01:13:10 johng Exp $
$Id: xkeyboard.c,v 3.34 1997/03/12 00:18:29 skate Exp $
$Id: xpixmap.c,v 3.0 1995/03/23 20:51:36 cvs Exp $
$Id: xselection.c,v 3.3 1996/07/25 22:33:52 johng Exp $
$Id: xsupersel.c,v 3.1 1995/11/21 21:47:56 scp Exp $
$Id: xtoolbar.c,v 3.7 1996/10/13 09:43:29 johng Exp $
$Id: xutil.c,v 3.0 1995/03/23 20:51:51 cvs Exp $
$Id: driverutils.c,v 3.0 1995/03/23 20:47:38 cvs Exp $
$Id: ether.c,v 3.0 1995/03/23 20:47:39 cvs Exp $
$Id: icmp.c,v 3.2 1996/09/10 18:52:40 maryc Exp $
$Id: mactcp.c,v 3.4 1996/06/12 00:25:55 maryc Exp $
$Id: mactcpctl.c,v 3.1 1996/06/12 00:25:56 maryc Exp $
$Id: mactcpdrvr.c,v 3.1 1996/02/26 22:55:30 maryc Exp $
$Id: tcp.c,v 3.8 1996/10/02 00:05:35 maryc Exp $
$Id: tcputil.c,v 3.6 1996/10/02 00:05:31 maryc Exp $
$Id: udp.c,v 3.3 1996/08/16 19:48:20 maryc Exp $
$Id: udputil.c,v 3.1 1996/06/12 00:25:54 maryc Exp $
$Id: utils.c,v 3.3 1996/06/12 00:25:58 maryc Exp $
$Id: sigsupport.c,v 3.1 1995/08/29 02:56:54 zell Exp $
$Id: ximage_xform.c,v 3.1 1996/03/15 12:17:09 johng Exp $
$Id: ximage_scale.c,v 3.4 1996/11/05 00:33:04 johng Exp $
$Id: xwrappers.c,v 3.3 1996/07/31 19:49:08 morley Exp $
$Id: c_aux_trap.c,v 3.28 1997/04/01 00:43:27 gwiesner Exp $
$Id: cgetsbrk.c,v 3.1 1996/08/30 11:16:51 johng Exp $
@(#) $Id: vlm.c,v 3.27 1997/03/15 02:05:54 mfc Exp $
% strings mae
[...]
Copyright 1988 Apple Computer, Inc.
 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`ABCDEFGHIJKLMNO
PQRSTUVWXYZ{|}~
B-Tree overflow.
        type = %s n_records = %d
LEAF
BRANCH
        previous = %d next = %d
        %2d: %4d %4d %2d %2d:
        %d."%.*s"       %d
        type = %s n_records = %d
LEAF
BRANCH
        leftchild = %d
        %3d: key = %3d rightchild = %3d
ordering wrong
Oh no!
Here's the left leaf
Here's the problem leaf
        i = %d lb = %d
Validating...  
[...]
$Id: filesystems.c,v 3.22 1996/10/27 04:03:36 mg Exp $
/usr/vice/etc/ThisCell
%s/%s
%s/%s
/usr/vice/etc/CellNamesMAE
%s/%s
CellNamesMAE
%s/%s
CellNamesMAE
/LinkAliases
Dummy_Symlink_Alias
APPLadrpamnufaamctrlfactextnfaexfontfdrpdeskfdrppreffapfprntfapnstrtfastmacsfasy
tempfdrptrshtrshemptfdrpTEXTTEXTBIN BIN 
%s%d
tmp_mnt
DoMinimalLinkAlias - for theLinkPtr at '%x' 
This-is-a-bad-sym-link
DoCreateEmptyCompletion - for theioPBPtr at '%x' 
DoCreateEmptyCompletion - failed!!!!!!! 
DoGetCatEmptyCompletion - for theioPBPtr at '%x' 
DoGetCatEmptyCompletion - failed!!!!!!! 
DoSetCatEmptyCompletion - for theioPBPtr at '%x' 
DoSetCatEmptyCompletion - failed!!!!!!! 
Can't create the Mac file system structures. 
 This is a memory allocation problem. 
.MIV_file
Can't open "%s". 
  You need READ/WRITE access permissions.  
.MIV_file
Can't create "%s". 
  You need READ/WRITE access permissions.  
.fs_info
File "%s" has invalid information in it. 
 Try rebuilding your .mac directory.  
The following line in the .MIV_file is invalid because it refers to one
of the special MAE directories.  You cannot create a MIV for the apple
directory, .mac directory, or system folder.  You also cannot create a
MIV for any directory enclosed in one of the MAE special directories.
This line will be ignored until the problem is corrected.
"%d:%s"
The following line in the .MIV_file references the same directory as
a line which was already processed. The pathnames of these duplicates may
not be identical in the .MIV_file if symbolic links or the '~' character
were used.
This line will be ignored until the problem is corrected.
"%d:%s"
Your .macdir is not at the root of a Mac volume.
You will have Apple file sharing problems using this configuration.
Your .macdir is currently at UNIX path:
[...]
 You have exceeded the maximum number of open files on this workstation.
 This is a serious error.
 MAE may not be able to function if it cannot open critical system files.
 Shut down MAE immediately.
 Refer to the MAE Administrator's Manual for more information about this
 error. 
[...]
ERROR: your home directory path, System Folder path, and Mac directory path
 must all be less than %d characters long.
Current path lengths are at least this long:
 Home directory: %3d
 System Folder: %3d
 Apple directory: %3d
 Mac directory: %3d
ERROR: no component of your home directory path, Apple path, System Folder path,
or Mac directory path can be larger than %d characters.
For the path '/foo/bar', components are 'foo' and 'bar'.
[...]
XS - unsuccessful attempt to send_message to MACD. - sent %d bytes
get_message:readn
XS - unsuccessful readn(read %d chars, expected 4).
XS - unsuccessful get_message attempt from MACD, nread=%d.
UNAVAIL
UNAVAIL
bin/macd
/bin/macd
[...]
MAE Video
Apple Computer
Rev 2.0
June 13, 1994
512 x 342 (9" Macintosh)
640 x 480 (14" Macintosh)
832 x 624 (17" Macintosh)
864 x 864 Resolution
640 x 800 Resolution
640 x 640 Resolution
Display_Video_Apple_MAE_S
Display_Video_Apple_MAE_M
Display_Video_Apple_MAE_L
Display_Video_Apple_MAE_F
Display_Video_Apple_MAE_C1
Display_Video_Apple_MAE_C2
[...]
Hey! Invalid HFS_Stat operation! (%d)
[...]
lib/ROMMondo
/lib/ROMMondo
/mac/ROMMondo
Can't find /mac/ROMMondo
shmget(ROM_COPY) failed
Can't create segment for copy of ROM
shmat(ROM_ADDR) failed
Can't attach to segment for ROM copy
/mac/ROMMondo is wrong size
[...]
36 41 2 1
  c #FFFFFFFFFFFF
. c #000000000000
                                    
                                    
                                    
                                    
                      ...           
                     ....           
                    .....           
                   .....            
                   .....            
                  .....             
                  ....              
                  ..                
          ......     ......         
        .......... ..........       
       .......................      
      .........................     
      .......................       
     .......................        
     .......................        
     ......................         
     ......................         
     ......................         
     ......................         
     .......................        
      ......................        
      .......................       
      .........................     
       .......................      
       .......................      
        .....................       
        ....................        
         ...................        
          ........ ........         
            ....     ....           
                                    
                                    
                                    
                                    
                                    
                                    
                                    
36 41 9 1
        c #FFFFFFFFFFFF
.       c #0000BBBB0000
X       c #FFFFFFFF0000
o       c #FFFF66663333
O       c #FFFF64640202
+       c #DDDD00000000
@       c #999900006666
#       c #999900009999
$       c #00000000DDDD
                                    
                                    
                                    
                                    
                                    
                      ...           
                     ....           
                    .....           
                   .....            
                   .....            
                  .....             
                  ....              
                  ..                
          ......     ......         
        .......... ..........       
       .......................      
      ........................      
      XXXXXXXXXXXXXXXXXXXXXXX       
     XXXXXXXXXXXXXXXXXXXXXXX        
     XXXXXXXXXXXXXXXXXXXXXX         
     oOOOOOOOOOOOOOOOOooooo         
     oOOOOOOOOOOOOOOOOOOOOo         
     oOOOOOOOOOOOOOOOOOOOOo         
     oOOOOOOOOOOOOOOOOOOOOOo        
     +++++++++++++++++++++++        
      ++++++++++++++++++++++        
      +++++++++++++++++++++++       
      ++@+@+@+@+@+@+@+@+@+@+@+      
       @@@@@@@@@@@@@@@@@@@@@@@      
       @@@@@@@@@@@@@@@@@@@@@@       
        @@@@@@@@@@@@@@@@@@@@#       
        $$$$$$$$$$$$$$$$$$$$        
         $$$$$$$$$$$$$$$$$$         
          $$$$$$$$ $$$$$$$          
            $$$$     $$$$           
                                    
                                    
                                    
                                    
                                    
                                    
[...]
small_decomp_rle_6(): Holy shit!  Contaminated data.
[...]
SOFTMAC_RESTARTING_NOW=TRUE
ERROR of execv
EXIT
Fatal error in Toolbox
%s: Error #%d
%s: %s
trap 0x%x, pc = 0x%x
A/UX
HP-UX
SunOS
APPLE_NATIVE_SYSNAME
[...]
exiting becuase no support to skip instructions on a/ux
[...]
You will not be able to use Macintosh floppies with MAE because Solaris' Volume 
Manager is not available now.
[...]
BUGS on MacPlus/SE, NuMc on later
[...]
Aae:  AAAAARGH!  Fatal X Error
[...]
Copyright (c) 1987 Apple Computer, Inc., 1985 Adobe Systems Incorporated, 1983-87 AT&T-IS, 1985-87 Motorola Inc., 1980-87 Sun Microsystems Inc., 1980-87 The Regents of the University of California, 1985-87 Unisoft Corporation, All Rights Reserved.
Then we start getting into an unusual section.
../BUILD.hp/emulator/midnight
[...]
%4.4x: Compiled %d 68K at %x into %4.4x (%d native at %x)
%8.8x-%8.8x ============================
Expanded opcode %4.4x into %d native at %x
UNKNOWN OPCODE
[...]
midnight
noon
Usage: midnight [-debug] [-i <infile>] [-o >outfile>] [-step]
                 [-remote_debug] decimalinetport hexinetaddr
                 <A/UX COFF file> [<arg1>] ... [<argn>]
emulator: cannot uname(2) local system errno = %d
TBATDEBUG
SOFTMAC_RESTARTING_NOW
TBWARN
Midnight Emulator version %s Remote Debug version built %s at %s, loading %s
[...]
Midnight Debugger
Unless otherwise specified, the following rules apply:
  -  Commands are single-letter and case matters a whole lot!
  -  Whitespace between the command and arguments are allowed.
  -  Values are hex by default.
  -  Addresses are automatically forced to be on even address boundaries.
  -  '<68kaddr>' is an address which will be offsetted automatically by
     the emulator so it lies within the 68k image.  For example, on this
     HP system a <68kaddr> of 0x4600 is a real address of 0x%x.
  -  '<emuaddr>' is an address which is not mucked with in any manner.  It
     can be any address within the emulator address space.
[...]
HUGGERZ
What About Bob?
                ___                  ____                  ___
           ____(   \              .-'    `-.              /   )____
          (____     \_____       /  (O  O)  \       _____/     ____)
         (____            `-----(      )     )-----'            ____)
          (____     _____________\  .____.  /_____________     ____)
            (______/              `-.____.-'              \______)
            *Hug*     *Hug*    *Hug*     *Hug*          *Hug*
            *Hug*     *Hug*    *Hug*     *Hug*       *Hug* *Hug*
            *Hug*     *Hug*    *Hug*     *Hug*      *Hug*   *Hug*
            *Hug*     *Hug*    *Hug*     *Hug*     *Hug*
            *Hug**Hug**Hug*    *Hug*     *Hug*    *Hug*
            *Hug**Hug**Hug*    *Hug*     *Hug*    *Hug*    *Hug**Hug*
            *Hug*     *T3W*    *Hug*     *Hug*     *Hug*     *Hug*
            *Hug*     *Hug*     *Hug*   *Hug*       *Hug*   *Hug*
            *Hug*     *Hug*      *Hug* *Hug*         *Hug* *Hug*
            *Hug*     *Hug*         *Hug*               *Hug*
                Here goes a big hug from the MAE Team!!!!!
[...]
It turns out that the
mae
binary has a second executable binary in it, called the Midnight Emulator. And we can run it!
ruby:/opt/apple/bin/% ln -s mae midnight
ruby:/opt/apple/bin/% ./midnight
Usage: midnight [-debug] [-i <infile>] [-o >outfile>] [-step]
                 [-remote_debug] decimalinetport hexinetaddr
                 <A/UX COFF file> [<arg1>] ... [<argn>]
ruby:/opt/apple/bin/% ./midnight -h
Midnight Emulator version 12:02:00 Remote Debug version built Mar 25 1997 at 10:26:25, loading -h
must set LM_LICENSE_FILE env var for midnight
ruby:/opt/apple/bin/% setenv LM_LICENSE_FILE /opt/apple/XXXXXXX
ruby:/opt/apple/bin/% ./midnight -h
Midnight Emulator version 12:02:00 Remote Debug version built Mar 25 1997 at 10:26:25, loading -h
Unable to open file -h
The Midnight Emulator uses the same license file as regular MAE and wants an A/UX COFF file, an echo of its past. Fortunately we have an A/UX machine handy here too, our old friend
spindler
, my clock-chipped Quadra 800. We'll fire it up in A/UX 3.1.
spindler:/bin/% uname -a
A/UX spindler 3.1 SVR2 mc68040
spindler:/bin/% file sync
sync:           COFF object     paged executable 
spindler:/bin/% ls -l sync
-rwxr-xr-x   1 bin      bin          764 Feb  4  1994 sync
spindler:/bin/% dis sync
                ****   DISASSEMBLER  ****


disassembly for sync

section .text
        $  a8:  23c0 0040 0150                   mov.l   %d0,0x400150.l
        $  ae:  518f                             subq.l  &8,%sp
        $  b0:  2eaf 0008                        mov.l   0x8(%sp),(%sp)
        $  b4:  41ef 000c                        lea      0xc(%sp),%a0
[...]
        $ 144:  480e ffff fffc                   link.l  %fp,&-4
        $ 14a:  4e71                             nop
        $ 14c:  4e5e                             unlk    %fp
        $ 14e:  4e75                             rts
/bin/sync
looks like a very small, yet valid A/UX binary we can pull over and see if Midnight will run it. First, a quick negative control by running it on itself:
ruby:/opt/apple/bin/% ./midnight midnight
Midnight Emulator version 12:02:00 Remote Debug version built Mar 25 1997 at 10:26:25, loading midnight
file midnight is neither COFF nor engine
The complaint that it's
neither COFF nor engine
suggests that its normal state is to be running
/opt/apple/lib/engine
, though this isn't too interesting, since we would assume MAE does that ordinarily. Regardless, it doesn't like our real A/UX COFF binary, even though it does try to load it.
ruby:/opt/apple/bin/% ./midnight sync.aux
Midnight Emulator version 12:02:00 Remote Debug version built Mar 25 1997 at 10:26:25, loading sync.aux
Error - text section below start of
 shared memory - a8
ruby:/opt/apple/bin/% ./midnight -debug sync.aux
Midnight Emulator version 12:02:00 Remote Debug version built Mar 25 1997 at 10:26:25, loading sync.aux
Error - text section below start of
 shared memory - a8
It is particularly strange that
mae
has a modification date of January 23, 1997, but the Midnight Emulator claims to have been built on March 25, over two months later. More explorations to come, especially into whether this could help to debug MAE itself.
At the end of this extensive strange trip, I found I rather liked the way MAE worked, and the integration features with HP-UX in particular really tempt me to try running it as my primary environment on top of CDE or VUE. Its performance was surprisingly good and I think if I had the choice back in the day between buying new a 3400c or this thing, even as noisy, heavy and costly as it is, I might strongly have considered buying the latter. Also, I bet MAE would run like a bat out of hell on my maximally configured C8000 and some additional explorations of the Macintosh Application Environment, possibly also on one of my SAIC Galaxys with a floppy drive and an earlier version of HP-UX, might be the subject of
a future article
.
The MAE team clearly didn't think 3.0 was the end of MAE; in the MAE 3.0 white paper's "Future Directions" they indicate that support for additional hardware platforms and "additional UNIX systems" are "being considered." They acknowledge the fact it doesn't run Power Mac software, even saying that "Apple is also investigating the viability of supporting PowerPC Macintosh applications on MAE." However, the document also adds that "Apple wants to ensure that the performance of RISC-on-RISC emulation will meet customer requirements before committing to this development effort." It's not clear if any work on this was ever done.
In the wake of Apple's purchase of NeXT in 1997 there was a mention in
Informationweek
that MAE would be ported to NeXTSTEP as a solution for legacy applications, but this would have been a limiting choice because of the existing PowerPC software that people wanted to run and I don't think it was ever a truly serious proposal. Although I couldn't find anything obvious in the trade rags about exactly when MAE was cancelled, I suspect Gil Amelio did it at Steve Jobs' suggestion after the buyout, like what happened with the
Apple Network Server
and
OpenDoc
. After all, MAE had just become superfluous after Apple adopted Rhapsody as the future Mac OS: now that Apple had its own Unix, there was no reason to support anyone else's. Nevertheless, although the Classic Environment in PowerPC versions of Rhapsody and Mac OS X (nicknamed the "Blue Box") is not a direct descendant of MAE, it's very possible that MAE informed its design. In practice, Classic is actually closer to MAS in concept in that it runs native PowerPC code directly in the so-called "problem state" on a paravirtualized Mac OS 8 or 9, using the standard ROM 68K emulator for 68K applications. Classic is less flexible than MAE in that only one instance can be running on any one Power Mac and only one user can be running it, but it was never going to be the future anyway.
As for RDI, in 1998 it was bought by its primary British competitor Tadpole, who also specialized in high-performance RISC laptops and had a SPARC line of their own. Tadpole turned the Carlsbad facility into their North American operations and continued to sell the PrecisionBook now under the Tadpole-RDI brand, adding the faster 180MHz version. Although no Tadpole or RDI laptop sold in massive commodity numbers, HP's concern over the looming one instruction per cycle limit caused them to begin moving away from PA-RISC to their experiments with EPIC VLIW, culminating in the fiddly and underwhelming early generation of Itanium. This hurt the PA-RISC workstation market the most, including niche systems like the PABook, and Tadpole eventually dropped it from their product line around 2001. In 2003 Tadpole renamed itself to Tadpole Computer, eliminating the last vestiges of RDI, and jettisoned all but their remaining SPARC line as they moved to Cupertino, California. General Dynamics bought them in 2005 and merged the company with General Dynamics' other recent acquisition, luggables manufacturer Itronix; the Itronix division closed its doors in 2013.
Again, if you were part of the MAE team and can shed a little light on how this all worked and your remembrances, please post in the comments or drop me a line privately at ckaiser at floodgap dawt com if you'd prefer to remain anonymous. It's a great little tool and more should be understood about everything that went into it.
