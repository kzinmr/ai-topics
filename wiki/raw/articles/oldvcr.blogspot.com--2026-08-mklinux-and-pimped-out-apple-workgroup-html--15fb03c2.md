---
title: "MkLinux and the pimped-out Apple Workgroup Server 9150"
url: "https://oldvcr.blogspot.com/2026/08/mklinux-and-pimped-out-apple-workgroup.html"
fetched_at: 2026-08-02T10:14:20.459621+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# MkLinux and the pimped-out Apple Workgroup Server 9150

Source: https://oldvcr.blogspot.com/2026/08/mklinux-and-pimped-out-apple-workgroup.html

As is typical here in the Floodgap lab, it all started so innocently: rebuilding a flaky Apple Workgroup Server 9150, the odd duck of the Workgroup Server line and older cousin to our beloved Apple Network Server. And then I just
had
to pimp it out for MkLinux.
Before the
sui generis
IBM AIX-based
Apple Network Server
, one of our favourite machines here at Floodgap, there were the WGSes, the Workgroup Servers, Apple's well-intentioned but conflictingly received line of Macintosh rebadges hopped up with high-spec options and special server software. While certain users had long repurposed desktop Macs as ad-hoc servers, these computers were the first Apple systems explicitly positioned and sold as such, and the first generation was even advertised with A/UX, Apple's own hybrid System V UNIX implementation.
A/UX ultimately didn't survive the 1994 68K transition to PowerPC, but in 1996 Apple publicly offered another option: run Linux, using the Mach microkernel. Although MkLinux emerged after the 9150's discontinuation, it's still just an overgrown NuBus Power Mac, so between more RAM, a beefier CPU upgrade and various video cards, by the end of this article we ought to have a configuration that gives us the best of two worlds — classic MacOS and MkLinux — in one server.
But first we're going to have to rebuild it. And these plastics definitely don't want to stay in one piece.
Rebuilding the Green Giant
Before we get into that, however, I've previously talked at length about Apple's early 1990s server strategy as it pertained to
how the Apple Network Server ended up running IBM AIX
, though not much about
why
CEO John Sculley's Apple embarked on a server line in the first place. Likewise, we've said very little about the parallel evolution of the Workgroup Servers and their relationship to the core Macintosh product line. Let's consider those topics now.
As an upstart in the age of microcomputers, Apple never had a history of making big iron, and the emergence of its server line can actually be traced back almost directly to the failed Macintosh Office concept. In January 1985, Apple's infamous
"Lemmings" ad
led its new hardware and peripherals announcement, including the AppleTalk Personal Network (what we now call LocalTalk) to set up multidrop serial links between computers and networked devices, the new LaserWriter printer, and a revamped Lisa 2/10 with more RAM and hard disk space newly subsumed into the Mac fold as the Macintosh XL. For a not
completely
eye-watering amount of money, Macintoshes could talk amongst themselves and send jobs to a high-quality shared printer, with network file storage on the XL's 10MB "Widget" hard disk to come shortly and support for
suitably equipped PCs
to follow. Steve Jobs, then both chairman of the board and veep of the Macintosh division, confidently predicted 10,000 Macintosh Office networks by the end of the year.
While the LaserWriter started at $6995 [$21,750 in 2026 dollars], the refreshed Lisa, er, Macintosh XL now started at a surprisingly competitive $3995 [$12,450], some $6000 less. However, the dirty little secret was that the Macintosh XL was only supposed to be a stopgap, a way to both slowly wind down the hardware and also buy time pending the
real
Macintosh Office centrepiece: Jobs' new leap forward, the "Big Mac." Big Mac had many vague ideas associated with it, though most of them converged on it being a file server or high-end workstation running some sort of Unix, possibly with the Macintosh interface layered on top. As such, being the most powerful machine in the constellation, it couldn't help but be fated for a central role in the new Macintosh Office. Later in design it was also internally known as the "3M" project, because it would generate at least a megapixel display (its most famous surviving mockup even put it in portrait orientation), provide at least a megabyte of memory, and run at least a million instructions per second on the new 68020.
Unfortunately for John Sculley, the company grossly underestimated the XL's appeal at its new lower price. What Apple expected to sell in eighteen months sold in three, emptying the parts inventory so rapidly that Sculley was forced to end its availability in April with Big Mac and its software still stuck in development. ("Apple's strategy may have been too good," mused InfoWorld.) Neither could Apple keep up with demand for the LaserWriter, becoming deeply backordered from manufacturing delays and only shipping 2,500 printers by June. Third-party products ended up filling the gaps, including networking hardware from 3Com and the Centram TOPS file sharing suite. Meanwhile, the Apple board, increasingly concerned about Jobs' excesses in his dual role, ordered Sculley to contain him, after which Jobs was cashiered in May and departed in September. Now in practical ruins, even though Apple promised all shipping products would remain available, the Macintosh Office initiative was officially shut down the same month.
Big Mac
sensu stricto
was so identified with Jobs internally that it became a political liability in the wake of his precipitous exit. For his part, new Mac product manager Jean-Louis Gassée considered it a "toy" and wasted little time officially canning it, instead promoting the Milwaukee project which had been quietly launched without Jobs' knowledge to create the future Macintosh II. Consequently, Apple's image began to suffer with corporate consumers as they lost confidence in the company's suitability for large office deployments. Sculley addressed this perception head-on at the 1986 introduction of the Macintosh Plus, telling attendees, "I know the real commitment from business customers must be earned by meeting customer needs, by living up to expectations and by keeping promises. We intend to do all of that."
The legacy of Big Mac nevertheless persisted in the Macintosh II's development, which at one point was even codenamed "Little Big Mac," and AppleShare's tardy arrival in January 1987 finally made a basic server platform possible. At launch AppleShare was targeted at any Macintosh Plus with sufficient external storage, though in initial versions a machine chosen for server duty had to be all but completely dedicated to the task. Introduced in March, the Mac II, compatible with the new AppleShare as well, would subsequently go on to largely achieve the 3M project's aims.
Another idea also originally intended for Big Mac emerged as a beta test later that year: Apple's own Unix, christened A/UX, based on UNIX System V Release 2.2 with extensions from 4.2BSD and 4.3BSD. For this work Apple contracted with UniSoft, then on the other side of the Bay in Emeryville, and well-known in the industry for their Unix ports such as the initial operating system of the Sun-1. After the kernel and userland were largely complete, development returned to Apple to graft on the Toolbox layer, a complex undertaking that suffered from months of delays fixing bugs. A/UX 1.0 (amusingly codenamed "Pigs in Space" after the Muppets sketch) finally emerged at Uniforum in February 1988 and was immediately available as a special Macintosh II configuration ($8597, approximately $24,250 in 2026 dollars) or on a pre-configured 80MB hard disk with a PMMU chip and extra RAM (up to $4979, or $14,050 in 2026 dollars), plus another $650 [$1835] for the book manuals.
Although A/UX 1.0's Toolbox had no MultiFinder support and could only run one GUI application at a time — and only about five to ten percent of existing Macintosh applications — the new operating system still achieved its greater purpose: credible entry to the high-end workstation market and new interest from government and educational customers who needed a Unix-based option, yet still keeping much of the Mac's secret sauce. "In terms of broadening the Unix platform," Sculley intoned at its introduction, "useability is probably even more important." Users generally agreed, though it was necessary to reboot back into System 6 to run most Mac applications, and developers objected to the A/UX Toolbox's front-end limitations and un-Mac-like programming interface when building hybrid apps. While
System 7's impending development
continued in the background, Apple added X11 support as an option in part to address these and other deficiencies in the graphical interface. "Our first goal was to do a solid Unix," argued Michael J. Homer, technical markets director.
A/UX 2.0, introduced in 1990 before System 7's rollout, made good on the majority of Apple's promises: most 32-bit clean applications could now run under a new compatibility layer, MultiFinder was supported, and Macintosh, command line and X11 applications were finally able to coexist on one screen. It was exceptionally well-received by reviewers and users alike, with MacUser approvingly calling it "the most interesting and impressive software to have come out of Apple since HyperCard." Subsequently in July 1991, after System 7's May launch, Apple and IBM announced their new partnership around the PowerPC and
a future AIX incorporating the Mac Toolbox
. In November this idea was broadened into the future A/UX 4.0, with Apple introducing the System 7-based A/UX 3.0 at the same time. (Another, less-well-known alternative also emerged around this period, but we'll talk about that later when we discuss the history of MkLinux.)
Despite these positive moves on the server software side, there had yet to be any corresponding server
hardware
, and Macs pressed into server duty in those days were otherwise just Macs. One I particularly remember as an undergraduate at the University of California San Diego was an SE/30 (
userserve.ucsd.edu
) down in the AP&M B337 lab, running AppleShare version something-or-other and an unknown Gopher server that we all accessed for software resources. I was fortunately able to
save its contents
before it was decommissioned, since it could still be accessed off-campus at the time.
As such, Apple management concluded their persistent lack of a turnkey server configuration was harming additional institutional uptake. At Mactivity '92, the Enterprise Systems Division (what would become Apple's Server Group) quizzed attendees for desired features; respondents
nearly unanimously
favoured high-end hardware on a Unix platform. Fortunately, Apple now credibly had one. In March 1993 the company announced the first Macintoshes to officially be called servers: the Workgroup Server 60, Workgroup Server 80, and Workgroup Server 95.
Of course, these machines at their core were also "just" Macs, or more specifically they were "just" Quadras: the AWS 95, the first one out of the gate in April, was a rebadged Quadra 950 (complete with the same keyswitch that debuted in the Q900), the Workgroup Server 80 was a rebadged Quadra 800, and the Workgroup Server 60 was a Centris 610 (that later became the Quadra 610). The main difference from the consumer models was that all three systems shipped with full 68040s plus extra base RAM and larger hard disks up to a full gigabyte, and true to their word, all three systems were A/UX-capable.
But the AWS 95 (codenamed "Chinook") did the other two one better: it
came
with A/UX 3.0.1, a
requirement
of the included high-performance PDS SCSI and L2 cache (128K to 512K) card, plus an optional 200-seat AppleShare Pro license for file and print services (a separate configuration targeted databases, with Oracle 7 specifically mentioned). In fact, when the demo machine
reportedly got stolen
shortly before
Mactivity93
, product manager
Marv Su
had to "make one" out of a Quadra 950 and a spare card to show to attendees. An optional tray could carry up to five internal hard disks, sitting on top of the system's drive shelf. While the AWS 95 could still run System 7, the PDS SCSI/L2 card was only fully supported in A/UX, and blocked one of the five NuBus slots when installed.
The other two systems came with a 50-seat AppleShare 4.0 license and System 7.1, and both the AWS 95 and the AWS 80 had optional built-in DDS (DAT) tape backup. The 60 and 80 launched two months after the 95 in June; Apple started the three systems at $3079, $6399 and $7589 [$7150, $14,850 and $17,600] respectively. The most expensive AWS 95 loadout had 48MB of RAM, a 230MB and a 1GB disk drive, DDS-1 tape and 512K of L2 cache, and sold for $12,929 [$30,000].
All three servers were generally well-reviewed, though the value proposition of the two lower-end models was somewhat questionable, and their sales were correspondingly tepid. On the other hand, in certain stratospheric market niches the AWS 95 became especially prized as both a high-end Mac workstation as well as a server. With institutional customers clamouring for an even higher-performance version, Apple wanted to keep that momentum going through the transition to PowerPC.
Meanwhile, Sculley himself exceeded the Apple corporate board's collective patience (particularly over Newton, cratering sales, various failed merger talks and Apple's biggest loss in any fiscal quarter to date) and was replaced as CEO by Michael Spindler in June 1993. Spindler's initial layoff moves were tough to swallow, but PowerPC had serious street cred and an obvious role driving Apple's next server generation. Officially Apple promised it would be helmed by an AWS 95 successor, incorporating its generous case and oodles of options, maybe even 64-bit with the any-day-now top-tier PowerPC 620, and of course running A/UX 4.0 powered by the Mach-based OSF/1 on top of the common PowerOpen platform.
Unofficially, just about none of that came true except the case, and even the case was to endure notable modifications. The 620 was intended to be the first 64-bit PowerPC implementation, capping the original 1991 roadmap above the 601, 603 and 604, but by late 1993 IBM was still working bugs out of the design and even the 603 and 604 weren't yet in production. Although the 601 was shaping up to be a powerful CPU for the era, for this high-end server's release to be at all timely its CPU could only practically differ from a desktop Power Mac in terms of clock speed and L2 cache. Likewise, on the operating system side PowerOpen-A/UX and the various Pink and Taligent projects the new server might have run remained victims of scope creep and slow development, while PowerOpen-AIX still didn't have its promised compatible Mac Toolbox, leaving only the same System 7 that every other upcoming Power Mac was going to run. Although System 7 software on PowerPC used the same PowerOpen ABI that A/UX was planned to, which would hopefully smooth out any later transition to A/UX 4 or AIX, the new A/UX wasn't even close to a beta.
Spindler's solution was an unexpected partnership with Novell to port what was then called Portable NetWare, an implementation of the NetWare 3 server platform running atop a separate host operating system, instead of the traditional architecture where NetWare
itself
was the operating system. This port was variously codenamed "Wormhole" and/or "Deep Space Nine," borrowing code from the existing IBM AIX port of Portable NetWare — AIX was PowerOpen too, after all — but modified to run via System 7; Wormhole would then run on the new high-end server, codenamed "Green Giant," using the fastest PowerPC 601 then available in a Quadra 950-style case. Novell NetWare was, of course,
the
premier network operating system of the early 1990s, but many believed it was already on a slow decline, and the overwhelmingly negative reaction Wormhole provoked from testers who still preferred Unix caught the Enterprise Systems Division off guard. Spindler remained doggedly convinced NetWare was the way forward, but as it was imperative the PowerPC server reach market with or shortly after the desktop Power Macintosh, at least initially Green Giant would have to be System 7 — any other options could come later. (As we'll discuss.)
To supplement the line the Power Macintosh 6100 and 8100, in nearly the same form factors as the Quadra 610 and 800/AWS 60 and 80, were retrofitted as the Workgroup Servers 6150 and 8150, collectively codenamed "Starbucks." Both these systems had CD-ROMs, however, and there was only one drive bay in the Q950/AWS 95 case which was used for the DDS tape drive, a previously popular option which Apple now intended to provide standard with the 8150 and Green Giant. The 8150 still had a bay available for it, but Green Giant required the aforementioned case modification: the floppy drive, formerly at the top of the Q950/AWS 95, was moved down to the bottom half of the front and the top reworked into a new bay for the DAT/DDS so the CD-ROM could go in below it. This made Green Giant the first, and ultimately the only, Macintosh in history to come with a low-mounted floppy, and the only Workgroup Server that didn't correspond to any existing desktop Mac. Green Giant also kept the AWS 95's five-drive tray, but got a new name to go with the new case: the Workgroup Server 9150. (There was never a "Power Macintosh 9100," for the record.)
As shipped, in hardware terms the WGS 6150 was nearly identical to the 6100/60, with the same 60MHz 601, the same processor direct slot convertible to NuBus, and the same 8MB of motherboard RAM, plus a 256K L2 cache and 500MB hard disk for $4219 [$9535]; the WGS 8150 was in turn based on the 8100/80, with an 80MHz 601, three NuBus slots and a PDS, but 8MB or 16MB of total RAM, 256K L2 cache, DDS tape and a 500MB or 1GB hard disk. The WGS 9150 (also seen as the "WS 9150" in various Apple documentation) used the same 80MHz 601 and added an extra NuBus slot, plus 512K of L2 cache and one or two 1GB drives, but you could also buy the biggest $10,269 [$23,200] configuration with two
2GB
drives and 24MB of RAM. You could also get a 9150 logic board to install in a Quadra 900 or Quadra 950 or, for that matter, an AWS 95, and it would fit your physical case if not your use case (if you were using A/UX).
Apple still kept the AWS 95 (and at least initially the AWS 60 and AWS 80) in the product line for users who wanted A/UX 3. To otherwise entice new users and soften the blow of its absence, the new PowerPC servers included software RAID 0 and 1 and the new PowerPC-compatible AppleShare 4.0.2, plus AppleSearch, Apple Internet Router and Apple Remote Access 2.0, and the DAT-equipped 8150 and 9150 also got Dantz Retrospect Remote for backups. The new PowerPC Workgroup Servers emerged in April 1994, just a month after the Power Macintosh 6100, 7100 and 8100 in March.
The machine we'll be rebuilding and then retrofitting is one of these original WGS 9150 machines, originally shipped in 1994. I had a 9150 a number of years prior but stripped it for parts, a shame I wear to this day, so this project was as much for penance as it was for pleasure (of sorts). This one was an eBay grab way back when, though it came somewhat stripped also, with its hard disk wiped, one NuBus slot cover missing, no RAM at all (just the 8MB soldered to the logic board), none of the pack-in software, and no cache stick. I suppose I should be glad it still had its special pre-terminated internal SCSI cable, the ROM SIMM and the PDS terminator, because these systems didn't come with a PDS video card standard and the PDS terminator is required if you'll be using motherboard video. I loaded it up with 128MB SIMMs (to equal 136MB), a couple hard disks and a 256K cache from a 7100. Its name is Brinton, after Brinton Baker, the server group's senior director of product marketing.
The rebuild came when it started getting flaky last year and intermittently crashing, but the RAM tested good and replacing the boot disk didn't make it better. Since these early 601s can run a little warm, I next redid the heat grease with proper modern compound to see if that would help, and it didn't. While my personal experience has been that these systems don't universally have the bad capacitors that '030 Macintoshes and their contemporaries (e.g., the Macintosh Portable) do, others have reported bad caps on their own early Power Macs, so that was the last thing to try. I sent the board off to
Garrett Bunge
for a professional recap, who reported there might have been a tiny bit of leakage, but either way it came back looking great.
We'll come back to the history when we get to our choices of operating system. Let's first get it back together, starting with the bare case.
Like most of its generation, these units have a metal skeleton with plastic on top and inside.
Unfortunately, that plastic is Spindlerplastic, typically ABS plastic where the plasticizer (probably a phthalate of some sort) has since evaporated with age and left the now-brittle polymer. There is no way to rehabilitate the plastic short of remelting it and adding new plasticizer; modern plasticizers are much less volatile. The Quadra 900 and its descendant designs (Q950, AWS 95, WGS 9150) are tower systems, so the logic board sits vertical and is supposed to stay in place with those snaps and tabs, which becomes a significant problem when the tabs and snaps snap. We're going to deal with that very issue later on, so take a good look at the image since it's the last time you'll see most of the pieces intact. The same root problem afflicts Amelioplastic, such as in
the PowerBook 1400
.
The exterior door is plastic, but backed with metal. It has guides for the cards.
It also shows how to properly loop and secure the cabling, though we're going to modify this somewhat since we'll be upgrading the unit to a single ZuluSCSI as part of the rebuild (keeping the original CD-ROM and DAT drives). However, note the slim cable coming from the top bay: this is actually a floppy cable, not Molex power or SCSI, because the diagram is really for the AWS 95 and the door is the same. The same incorrect diagram likewise appears in the 9150's administration manual, probably to save time writing it.
Although the backplate label shows model number M3125, the actual serial number is located next to the card slots. This unit is serial# XC44600P36R, manufactured 46th week 1994 ("446") by Apple at their Elk Grove, CA facility (factory code XC;
this post
explains how Apple's serial numbers worked at the time).
The Quadra 900 introduced a wafer lock keyswitch which controls both power and security. If the key is turned all the way to the left "off" position, the server is powered down (or is powered down immediately) and will not start up, even if the reset key is pressed on a connected keyboard. If turned to the middle "on" position, the server operates normally. If turned to the rightmost "secure" position, the server powers on (and stays on), automatically powers on after an outage, and also locks out the floppy drive and connected ADB devices. The Quadra 950 inherited this case and keylock as did the AWS 95 and the WGS 9150. The same wafer lock keyswitch is also used on the Apple Network Server for setting the operating system mode and locking its front door, but its three settings behave differently, and the ANS also has a separate two-position rear lock of similar type.
The keys have a small three-digit code engraved in the metal. Not all of the keyswitches still have their corresponding tag, but if they do, the tag's code should match the key's. These keys are otherwise straightforward to duplicate with a blank of similar size and any good locksmith should be able to fashion a copy.
Giving it a good scrub before we put the logic board in.
Our freshly recapped logic board. Despite the case serial, and the board serial (SS42704F3B6) which indicates 27th week 1994, at least one chip has a 1995 copyright date and the CPU is also from 1995 (I'll show you in a second), so either this board was repaired or final assembly was done later. The WGS 9150 logic board is the same size and has nearly the same port and slot configuration as the Q950/AWS 95's because it had to fit that case as well, but the 9150 requires less board space to do its job, so consequentially a fair bit of it is empty.
Still, there are various landmarks. In the northwest/top left corner is the 8MB of motherboard RAM, which would be frustrating if any of it failed since replacement obviously entails desoldering. Left/west of it are the interrupt and reset switches, which we will be revisiting later more than we would like to; above/north of it is the header for the keyswitch, which you can use to short it if you don't have a key; and to the upper right/northeast of it is the power LED, which is refracted by a light pipe to the front. Below/south of the soldered motherboard RAM are eight 72-pin SIMM slots. RAM must be installed in matched pairs to a maximum of 256MB in the SIMM slots, equaling 264MB.
Below/south of the SIMM slots are other various internal connectors, including the low-mounted floppy (J19), internal SCSI port (J23, I'll talk about this a little more momentarily), CD audio input (J18), PRAM battery (BT1), and way at the bottom, the internal speaker header (J17).
The NuBus slots, the CPU, and their satellite electronics dominate most of the rest of the logic board. The CPU is under the large heat sink, which I will demount for show in the next series of photos, with an unpopulated debugging header at the very top/north at J28. Around it, clockwise from lower left/southwest, are (U19) the 343S0148-01 Fat AMIC "Apple Memory-Mapped I/O Controller" unique to the WGS and used for DMA to its full set of NuBus slots (3-slot NuBus Macs use the regular AMIC), also providing DMA for on-board Ethernet, sound, SCSI, floppy, and serial I/O; (U24) a 343S0802-A HMC "High-speed Memory Controller" used in at least all first-generation NuBus Power Macs; (U62) a 343S0137-A SWIM III floppy controller with DMA despite the floppy connector being low; (U37 and U36) twin 343S1144-01 Data Paths for buffering the bus and routing video data, and also used in at least all first-gen NuBus Power Macs; and (U35) a 343S1124-04 BART NuBus controller. Note also the same slots for the cache stick and ROM stick, plus the power supply connector and Processor Direct Slot. Right/east of the second Data Path at U36 is a smaller chip, the 343S1069-B "Ariel" video chip at U13. This is the same video chip used for motherboard video on the other first-generation NuBus Power Macs, but the 9150 uses a more typical Macintosh DA-15 video port like the Quadras — remember, it has to fit their cases — instead of its contemporaries' oddball HDI-45. Right/east of the BART at U35 is an AMD AM79C950KC "Super Combo" CURIO chip at U10, containing the equivalent of an NCR 53C96 SCSI controller (for the external port), an AMD 85C30 serial chip and an AMD 79C940 Media Access Controller for Ethernet (MACE).
The CURIO, however, only services the external SCSI port — the internal SCSI controller is southwest/to the lower left of the Fat AMIC at U47, a MESH "Macintosh Enhanced SCSI Hardware" NCR 53CF96 which provides support for SCSI-2 and is the chip closest to the explicitly-marked "INT SCSI" 50-pin connector at J23. However, next to the 25-pin external SCSI connector at J8 (above/north of the serial port at J4) is an
additional
50-pin header at J9 with
no
markings. This port is yet another holdover from the Quadra 900, the first Macintosh to implement a separate internal SCSI bus, and later duplicated on the Q950 and AWS 95. On these machines the internal SCSI is a separate second bus from the external SCSI, but there are internal headers for both busses so that internal devices can be on either bus. The 9150 still has this feature and thus still has a port in the same place to handle upgrading machine configurations that need it, but it was officially undocumented and its use otherwise discouraged, and any internal devices connected to J9 will be on the slower CURIO. We won't be using it here.
As for the CPU, here are some pictures from when I demounted the heat sink. The heat transfer compound Apple used was "fine" at the time but 30 years later has turned to heat transfer brick mortar. Some folks have reported erratic behaviour from the CPU overheating which was fixed by cleaning it off and applying better thermal paste, so I tried doing that first. Apple used this heat sink or a close variation for all their 601 processors, even the one in the Power Macintosh upgrade card, with four metal claws to clamp the heatsink tightly on the die by gripping corresponding holes in the logic board. The tips of the claws can be gently released from the other side using a spudger or gloved finger.
After some careful cleaning with 91% isopropyl alcohol and a handful of Q-tips, this is our CPU and die (under the heat spreader), produced 4th week 1995. Only IBM was making the 601, and only at their Burlington, VT and East Fishkill, NY facilities at the time, so since the East Fishkill plant was fully CMOS by 1995 and used for manufacturing higher-value and server grade chips, I suspect this one came from there. The PowerPC 601 was packaged in a 304-pin ceramic QFP which, in most Power Macs using it except for the 7500's daughter card, is permanently soldered to the logic board as shown here. Fortunately most 601-based Macs have
some
sort of upgrade pathway, either through their CPU slot or (in this case) as a PDS card, with the notorious exception of the Power Macintosh 7200, 8200 and Workgroup Server 7250 for which Sonnet eventually produced a PCI card to carry a G3.
The first-generation PowerPC 601 was produced in speeds from 50MHz to 80MHz, though Apple never used the 50MHz part in a shipping Power Mac. It was fabricated on a 600nm CMOS-4s process by IBM with four layers of metal, producing a 2.8 million transistor die measuring 121mm². The CPU has a 32K unified L1 I+D cache, which for the era was considered generous, and overall the chip could meet or exceed contemporary Intel Pentium performance. The 603 and 604 have more typical split caches.
For comparison I have placed it next to a non-functional 90MHz PowerPC 601v (also known as the PowerPC 601+) that I use as a display piece, which shrunk the die to 74mm² using a 500nm CMOS-5 process. Introduced in late 1994, the process shrink enabled the CPU to run from 90MHz to 120MHz, though with a corresponding increase in heat. Apple used the top-end 120MHz part in the 9150's only model upgrade, which I'll talk about once we have this one reassembled, and later for upgraded models in the 7200 family as well. These fastest systems require an active Peltier thermocooler to keep the chip's temperatures down.
Another point of comparison is this 200MHz PowerPC 604e from an Apple Network Server processor card I was trying to refurbish. (It's dead, Jim, even after a recap and replacing the sludged-over heat grease.) Although the heat spreader is larger than the 601, the die is smaller at 47mm², containing 5.1 million transistors fabricated on a 250nm CMOS process by IBM with five layers of metal.
Reapplying a more modern heat compound to the 601.
Getting the CPU heatsink back on a 601 needs to be done a little more carefully than taking it off. The ceramic QFP is sheathed in glass and this glass can crack (people have done it!) if the heatsink exerts uneven or excessive pressure, so it's important to get the claws through the holes without grinding too hard on the CPU package's top layer.
We place the board into the case and line the notches up with the snaps and guides.
Then we push it back into the openings for the ports. In theory a large plastic clip in front will keep it in position along with the smaller snaps and clips, but this big clip also snapped. There is no point in repairing these because they're just plain weak and they'd fracture somewhere else. We'll explore an alternative for keeping the board in position later on.
Ensuring the ports are all lined up. From top to bottom, identical to the Quadra 900 and progeny, they are DA-15 ("DB-15") video, AAUI Ethernet, 25-pin SCSI, modem and printer serial ports, ADB, separate right and left audio input channels as BNC jacks (intended as line-level inputs), audio input as a 1/8" stereo jack (intended for microphones), and 1/8" stereo output. The audio features made sense on the Q900 and Q950 as high-end workstations, and the AWS 95 probably got pressed into that role from time to time, but it seems the sole reason they persist on the 9150's board is once again to fit in those cases.
We don't have the original 512K cache stick, but we do have its ROM DIMM (top) and PDS terminator (bottom). The PDS terminator is theoretically required for all first-generation Power Macs when nothing is installed in the Processor Direct Slot, but the AV Power Macs ship with an AV PDS card there, and non-AV 7100 and 8100 systems (but not the WGS 8150) have the High-Performance Video card instead. We will explore both these cards a little later. The situation is a little different with the 6100 family: many of those computers will have an PDS-to-HDV or PDS-to-NuBus adapter in that slot, especially those that are or originated as 6100AVs, and our own Performa 6116CD ran just fine
with nothing installed at all
. In fact, according to Apple's
own tech note
, the PDS terminator was only ever intended and shipped with the WGS 8150 and 9150, and it cautions these systems will not work without one if the Processor Direct Slot is empty.
The CACHE/ROM slots have exactly the same pinout on these early Power Macs and you can put the cache stick or the ROM stick in either one (but a note from the future: put the ROM in the top slot, not bottom as I did here initially, because the top slot tends to get blocked by the power supply and makes accessing a cache DIMM there difficult). The PDS terminator goes in the PDS connector.
Since the last rebuild I had accumulated a big stock of 72-pin RAM SIMMs, so this time I loaded it up with a full 256MB. This will come back to bite us too.
The AWS 95 supported a five-drive carrier as an option (it would also fit in the Q900 and Q950), but for the 9150 it came standard. Accordingly a special extra-long (but otherwise "regular") SCSI cable with its own internal terminator was used for these drives as well as the CD-ROM and DAT.
With the long SCSI cable on, plus CD audio, the keyswitch and the floppy cable.
The floppy drive's metal frame attaches with a couple screws.
Now the power supply. This monstrous metal-encased hunk was also introduced with the Q900 and provides both power and ventilation. While it can be substituted for between the Q900, Q950, AWS 95 and WGS 9150, the upgraded 601+ 9150's power supply also has a fan for its Peltier-effect thermocooler. This additional fan is attached both to the power supply using a clip and to the logic board for power.
The power supply, besides providing the system's 292 watts (nominal maximum at 10A; up to 424 watts and 18A for "a period of 12 seconds maximum"), is a major structural element. Unlike the logic board, even a brand new ABS plastic frame could not have possibly supported its weight, so it is secured to the metal casing with screws. Unfortunately, not only is it bulky and heavy, but it also prevents easy access to the RAM SIMMs, floppy drive and the top CACHE/ROM slot when installed. The drive carrier and top device bays rest on it, though we must also make sure the CD audio and keyswitch cables can exit to the top behind the power supply in the channel provided for that purpose.
Next the bezels for the DAT and CD-ROM. These have already lost pieces but fortunately enough tabs persist so that the other bezel and the speaker panel can keep them in place.
After that we install the buttons for the reset and interrupt switches — again something that will become a regular irritant in this entry — and put on the bottom speaker bezel, which has lost a couple chips of its own, but enough to still grip the holes in the metal and hold everything together.
Now the top bay drives. The DAT is the original one shipped, a DDS-2 HP C1533A tape drive supporting tapes up to 120m, and the same one used in the AWS 95 and WGS 8150. The Apple Network Server also used this drive.
The CD-ROM is also the original one shipped, an internal 2x AppleCD 300i Plus. You'll notice it is secured to a plate. This is the plate that goes on top of the power supply.
The DDS-2/DAT drive's sled fits into the CD-ROM's sled, and the CD-ROM's sled is attached to the plate. We place the plate at the back of the power supply ...
... and slide it forward to lock it in position. There are screws to secure it, but unlike the ABS plastic tabs, these metal tabs hold well without them.
This is sufficient to boot the machine from CD. Because it was flaky before, I decided to leave the cache stick out to eliminate one potential variable. I then connected the SCSI cable to the CD-ROM (remember, it's already terminated), plugged in the power connector, plugged in an ADB keyboard and mouse, plugged in an LCD VGA panel (with a video dongle), turned the key to the middle position and pressed RESET on the ADB keyboard.
We got
the musical sting
! (These Power Macs do not make a Mac "bong.") I then got out my customized Mac OS 8.6 boot CD — I prefer 8.6 on Macs on beige pre-G3 Macs without an upgrade card — and put it in the optical drive, and got a Happy Mac! But was it stable? Let's burn it in before we go further with this process.
Waiting for 8.6 to boot from CD, which is not fast with no cache and a 2x CD-ROM.
I plugged in an AAUI Ethernet dongle and started the Gauge Pro memory test on loop from the Macintosh IIci NetBSD fileserver, and then watched a couple movies on the couch.
Four hundred and fifty-two memory tests later, the CPU was running fine and the hardware had not glitched. Between Garrett's recap and our refurbished heat grease, we appear to have a working system once again. Let's install the cache stick and a ZuluSCSI now.
These are both 256K L2 cache sticks, which is annoying, but they are what I had in stock. Although my
Power Mac 6500
has a 1MB cache, I left it there because that machine is intended primarily as a BeOS box and BeOS doesn't support L2 G3 upgrades, whereas we might be able to dual boot with a G3 in this one even if MkLinux won't support it. (Note from the future: this can work.)
Now that we have the power supply connected, the service manual warns us
not
to mess around with the NuBus, PDS or cache slots without unplugging the machine, even if the key is turned to off — there's apparently some trickle power even in the fully-off key position. With the plug out I switched (with difficulty) the ROM into the top slot and put one of the 256K cache sticks in the bottom one.
For storage, next we'll prep the ZuluSCSI. I got out a new SD card and created three disk images: a 4GB disk image exclusively for Mac OS (as HFS+), a 4GB disk image for MkLinux (as ext2), and a 1GB image to be partitioned into MkLinux swap and an HFS (not HFS+) exchange partition, since the HFS toolkit included with MkLinux only understands original HFS. We'll need this exchange partition for building custom kernels, since the kernel is booted from the Mac OS side. I chose to make smaller individual devices rather than carving up a larger disk into LUNs simply for ease of organization; the SCSI emulator doesn't really care one way or the other, and I can also separately back the image files up.
I then got out a ZuluSCSI in a plastic carrier, installed the card and perched it on top of the power supply. Although I had a power connector on it, it seemed fine with termination power alone.
We'll now boot again from the Mac OS 8.6 CD, with a perilous conga line of dongles to yield a 60Hz video signal the Inogeni VGA capture rig will accept.
Loading the OS.
In Drive Setup we see our three images.
We'll install Mac OS on ID 0, using the entire disk.
Starting the Installer.
The installation is not very fast from the internal CD-ROM, and if I'd thought about it, I should have simply loaded the image on the ZuluSCSI as well, but we'll only have to do this once.
Complete.
Restarting now from the ZuluSCSI instead of the CD.
For the record, here's the output from Apple System Profiler. All 264MB of our RAM is enabled, as is our 256K of L2 cache, and the CPU is correctly detected as an 80MHz 601. The Gestalt ID for the original 9150 is 39 (the upgrade is Gestalt ID 57), but notice the spelling of "Work Group Server" in the model name string which is where WGS comes from.
MkLinux, or, Linux at Mach 3
At this point we'll configure the machine to dual-boot MkLinux, so let's talk some more backstory before we do.
Apple's erratic push towards a true enterprise server continued taking odder turns, even starting when the PowerPC Workgroup Servers first emerged, and once again the marquee headline was ... NetWare. At the same April 25, 1994 event, Spindler demonstrated a newly commissioned port of Processor Independent NetWare, a top-to-bottom portable form of NetWare 4.1 where now the entire operating system could run on non-x86. Codenamed "Cyberpunk," the famous NetWare worm is shown here running on what is most likely a Workgroup Server 8150, the machine's demonstration target (though much of it was done on Piltdown Man, i.e., the 6100 family). Cyberpunk was intended first and foremost for Shiner, Apple's new large server under development, though its specific build was never publicly demonstrated and is believed lost, but
the NuBus-compatible version has survived
. Because of the age of its System file, the 9150 ironically can't boot from this only known build. (Photo credit, Joe Pugliese, Associated Press.)
Meanwhile, delays continued to plague the 620 at IBM and Shiner temporarily stalled out from multiprocessor cache coherency problems in early 604s, forcing the server group to squeeze out as much as it could from the 601. Almost exactly one year after the original 9150 came out, the new version I'd previously hinted at emerged in April 1995 and bumped the specs to a 120MHz active-cooled 601+ with 1MB of L2 cache. (This particular machine, codenamed "Zephyr," had an
arresting crimson prototype board
complete with populated debug header, additional test points and a silkscreened train logo.) All three PowerPC Workgroup Servers now came with 16MB of base RAM plus System 7.5 and AppleShare 4.1, the 6150 and 8150 got smaller speed bumps of their own to 66MHz and 110MHz, and Apple's software RAID remained supported.
But what puzzled potential customers more was how increasingly inconsistent Apple's server
software
strategy was becoming. PowerOpen-A/UX 4-AIX and Taligent-Pink were still shambling around Cupertino development hell, causing Apple in May 1994 to embark upon an alternative stepwise approach in the form of Copland. Meanwhile, despite claims of Cyberpunk's continued progress, at the April 1995 refresh Spindler had little other choice than to double down on then-current Mac OS with the Apple Internet Server Solution. AISS had the distinct stench of a product assembled under duress, nothing more than a cobbled-together bundle of largely pre-existing software shipped with your choice of Workgroup Server, though the software would of course run on any Power Mac. Other than MacDNS, which wasn't even finished when AISS was launched, plus AppleSearch and "player" versions of HyperCard and FileMaker Pro, everything else was third-party: WebSTAR for server software, Bare Bones' BBEdit as an HTML editor, Adobe Acrobat Pro as, uh, Adobe Acrobat, Netscape Navigator and Everywhere Butler SQL. Apple threw in CGI support for AppleSearch and templates for web pages to be customized.
AISS' spec sheet promised even the wimpiest 6150 could handle 3,000 to 5,000 connections per hour (how cute!) and more still was possible by using MacDNS for round-robin load balancing against multiple redundant Workgroup Servers. However, there was one Workgroup Server that
couldn't
run AISS: the AWS 95. Even as Shiner was supposed to be Apple's next big Unix box, the company seemed to outright repudiate its previous Unix efforts, explicitly claiming that "you don't need to be a Unix nerd" to use a Mac server. The AWS 95 was quietly cancelled in October 1995 at nearly the same time as the collapse of Cyberpunk, marking the end of Apple's inexplicable flirtation with NetWare.
With the recognition that A/UX 4 might never ship, Shiner was retrofitted to run standard AIX 4.1 with Apple's extensions, yielding our beloved
Apple Network Server
in January 1996. Unfortunately for Spindler, Apple's finances were thoroughly in the weeds by then, and his announcement of further staff and model cuts was too much for shareholders who hastily replaced him with Gil Amelio in February. However, the Network Server, defiantly no Macintosh, turned out to be not the only Unixy thing at Apple then either.
In 1989 Apple bought out Coral Software in Cambridge, MA (not Cor
e
l), developer of Allegro Common Lisp for the Mac, as part of an initiative for new programming paradigms on the Macintosh but also the Newton PDA. The deal involved Coral's team joining Apple's Advanced Technology Group at a new ATG lab to be established there, and Ike Nassi, a veteran engineer and scientist at DEC and part of the initial team at Encore Computer Corporation, was recruited to Apple by then-Newton chief Larry Tesler to run it. Initially Nassi managed the Dylan programming language (at the time written in Macintosh Common Lisp and originally intended for, but never used by, the Newton) and Sculley's Knowledge Navigator passion project before Apple software VP Dave Nagel asked him to move west in 1993 to assist with the software division. Nassi started as VP of development tools, his portfolio notably containing MacApp and the Macintosh Programmers' Workshop, but less than a year later was asked to take over the operating system group. As the PowerPC transition progressed, Nassi became concerned by efforts to build the Common Hardware Reference Platform, believing it would stunt the growth of the Power Macintosh, and positively alarmed by the growing debacle around Copland's infamous NuKernel core, which he said later to the
Computer History Museum
"was just not going to fly."
At Encore Nassi had first encountered the Mach microkernel, created at Carnegie Mellon University by Richard Rashid and Avie Tevanian, as part of a 1987 port to the Encore Multimax. This port was particularly important to the microkernel's development as the Multimax used multiple CPUs, some installations running as many as ten or more
pairs
of National Semiconductor NS32032-family processors. (At my first job out of college, the HP 9000-K250 I was hired to work on had recently replaced what I think was a Multimax.) In fact, Apple already had experience with the Mach microkernel in the form of MacMach, a 1991 CMU research prototoype which ran 68K System 7 as a virtualized task under Mach parallel with its 4.3BSD-derived operating system core — not unlike Classic under Mac OS X many years later, and not to be confused with
MachTen
, a separate commercial effort from Tenon Intersystems developed independently from CMU or Apple, which runs Mach as a task under Mac OS. MacMach was the product of a joint effort to allow programs from CMU's Andrew Project distributed environment to run directly on the Macintosh II, and Apple provided both financial support and source code from System 7 to aid in development.
Notwithstanding the impressive technology, however, MacMach's potential was unavoidably limited. Its reliance on the 4.3BSD codebase incurred the strict requirement that users hold a valid AT&T Unix source code license, all but ensuring it could never be a plausible alternative, let alone threat, to A/UX; and like A/UX, it was never directly ported to PowerPC, condemning it to obsolescence. In the time since, Nagel had moved to VP of engineering; Nassi, who succeeded him as head of the software division, convinced Nagel in August 1995 that resurrecting the concept might pay off. The idea was controversial within Apple, especially with Macintosh division head Howard Lee, who believed it would maroon the Macintosh if IBM considered Mach's highly portable nature as evidence Apple wasn't committed to PowerPC. Lee's fear was not without reason: Spindler previously had to cancel the System 7 port to Intel (i.e., the Star Trek project, instigated by Novell) as a potential threat to the alliance, and of course Project Marklar much later directly led to Apple indeed leaving PowerPC in 2006.
Becaue of the internal political ramifications, the PowerPC Mach group initially had few staff resources and operated in near-secrecy for many months. Brett Halle, then manager of the kernel team, suggested to Nassi that a Linux port, modifying the Linux kernel to run as a task under Mach, could demonstrate the microkernel's viability. It even had an obvious name: MkLinux.
Early work on a Power Mac Linux by independent developer Gary Thomas already existed by that point. With Nassi's blessing, Halle quietly sponsored a small team from the Open Software Foundation's Grenoble, France office to begin both the Mach port work and the Linux kernel conversion to run under it. OSF had extensive experience with Mach dating back to their 1989 use of Mach 2.5 as the basis of OSF/1 ("
osfmk
," intended also as part of the foundation of A/UX 4.0) but this team operated separately, later with a single part-time Apple engineer. The host machines used for initial development were both x86 PCs running regular Linux and HP 9000/700 PA-RISC workstations with OSF/1, with the x86 hosts migrated to an MkLinux port of their own as a self-hosting alpha test. PowerPC objects were cross-compiled using
gcc
2.7.1, with cross-platform debugging with
gdb
over a serial port. For simplicity of development, the Linux task ran under OSF MK as a single monolithic server, though the developers admitted this wouldn't be an ideal system design for a Mach-based platform.
The group's rapid progress impressed Nassi, and shortly before the first Developer Release in May 1996 he made the effort official as Apple's "Leveraged Technologies Group." Using the new kernels with tools and pieces previously ported by Thomas and others on top of a modified Red Hat distro, MkLinux DR1 CDs were finished, pressed and handed out, complete with source code, to WWDC attendees that year. The LTG represented Apple's first official attempt to support an open-source software project, and within six months had increased to seven members, five at Apple and two at OSF.
An important consequence of its isolated development, however, was its limited hardware support. Apple had since moved from NuBus to PCI with the introduction of the Power Macintosh 9500 in June 1995, and the Workgroup Server line subsequently followed suit. In February 1996 Apple introduced the Workgroup Server 7250 (derived from the Power Macintosh 7200), using the same 120MHz 601+ as the 9150/120, and the first Workgroup Server to use a 604, the 132MHz Workgroup Server 8550 (from the Power Macintosh 8500), along with an updated AISS 2.0 — at which point the 6150, 8150 and 9150 were all discontinued, though the new AISS would still run on them. But, because the LTG had only developed on NuBus Macs, DR1 only officially ran on the 6100, 7100, and 8100 (plus Power Computing's clone Power 100 family), all of which had also been discontinued by the time DR1 emerged. Not even the NuBus PowerPC Workgroup Servers officially appeared in the support list, though of course it would run on them too. As the distribution files were large downloads for the era, partner Prime Time Freeware produced pressed CD-ROMs for a nominal cost.
Developers were surprised and impressed by DR1, though bugs and the initial inability to run on current hardware tempered their enthusiasm, and the overhead of both the microkernel and its monolithic Linux task made it slower than a port running directly on the metal would have been. DR1 was quickly
replaced by DR2
in September 1996, primarily a bug-fix and performance release, which in turn was used to supplement an
early direct port
of the Linux kernel (then called
linux-pmac
) to PCI Power Macs.
For his part, Nassi was pleased with MkLinux's promising launch. However, without a compatibility pathway it could not be an obvious successor to Mac OS, and while Nassi had plans for running the Mac OS under this "PowerPC MacMach" as 68K MacMach did, that goal was never achieved. Nassi quietly disagreed with Gil Amelio's pursuit of Jean-Louis Gassée's BeOS, believing Mach to be the superior platform, and left Apple in November 1996 before Apple's acquisition of Steve Jobs' NeXT — itself of course powered by a Mach-based OS, as is its descendant, modern macOS.
MkLinux nevertheless progressed further at Apple after his departure. DR2.1
was announced in March 1997
as the first release to itself run on both NuBus and PCI systems, supporting the 601 and 604 CPUs in the Power Macintosh 6100, 7100, 8100 and 7200, 7500, 7600, 8200, 8500, and 9500. Prime Time duly released CDs of these as well and Apple dubbed 2.1 the "Reference Release," sponsoring Prime Time and editor Rich Morin to release a book-and-CD kit with the tree from January 1997, just before the official announcement. The x86 and PA-RISC ports were also made available (since they already existed), though of course OSF MK could run on many more architectures than that. On the other hand, the Apple Network Server, at the time Apple's only true-Unix machines, never ran it.
After Apple's acquisition of NeXT and Steve Jobs' return as Apple CEO in a July 1997 boardroom coup — this time at Gil Amelio's expense — porting NeXTSTEP (then branded OPENSTEP) to Power Macintosh became top priority for the new Mac OS. Apple's cash crisis and Jobs' ruthless focus had already combined to end projects like
Cyberdog and OpenDoc
and terminate
further development of the Network Server
, and MkLinux was just as vulnerable because in Jobs' mind it had already achieved its maximal corporate utility: OSF and the LTG had done most of the work porting the microkernel, and with NeXTSTEP's ready BSD foundation Apple had no further need of Linux.
Apple disbanded the LTG and transferred control to the community
MkLinux Developers Association
in 1998 for the release of DR3 in July, by which point MkLinux could run on
nearly every four-digit Power Macintosh
(now explicitly
including
the Workgroup Servers) and even early beige G3 models, plus the PowerBook 3400 and the Kanga PowerBook G3. (Apple had since abandoned the 620, which had become hot, expensive, and increasingly surpassed by the cheaper 604 family. Notably, although the 750/G3 completely outclassed it as well, the G3 did so with some features introduced in the 620 like backside L2 cache.) In those days the website was reportedly even
hosted on an 80MHz 7100
for some period of time, and allegedly other PowerBooks like the 5300 could boot it also. Mac-specific device support lagged, however, and the project's lack of resources combined with the continual need for Mach-specific changes to the Linux kernel slowed progress further during Apple's transition to the New World Mac. R1 was released in December 1999 and the final release, "pre-R2" (but basically R2 and that's what I'm going to call it), was closed out in August 2002. Although the MkLinux website remains up and accessible today, no new official work on it was subsequently done, and the direct LinuxPPC port replaced it as the
de facto
Linux basis for Power Macintoshes and the Network Server.
Given that complicated tale you might well wonder why we're even bothering with MkLinux at all, especially since non-Mach Linux also eventually supported NuBus Power Macs, including the 9150. The reason is simply historicity: it was the only official "Apple Linux," the only Linux distribution Apple had a direct hand in developing, the only Unixy thing of
any
kind Apple even vaguely supported on any PowerPC Workgroup Server, and for years was the only Linux that could run on the NuBus ones. With the weight of that behind it and me being a history nerd first and foremost, I never considered running anything else. Before Brinton's freakout and rebuild, I had MkLinux "pre-R2" on it, so now that we're starting fresh we'll hopefully learn from those mistakes I made the first time (at least, if I can remember them).
Like many Linux installs of that era, the process begins with pre-partitioning the hard disk. As a nice little connection with the past, and typical of then-extant Unix-on-Mac packages like MacBSD (merged to become NetBSD/mac68k), MkLinux uses A/UX partitions which are then reformatted during the installation process into ext2, so we'll grab a copy of Apple HD SC Setup 7.3.5 for this purpose from the IIci fileserver. This copy of HD SC Setup is prepatched to work on any real or emulated hard disk, even ones that aren't seen as official Apple drives, though ZuluSCSI volumes can certainly be configured to mimic them. (Ignore the wacky 1956 file modification times; this is because the Mac OS install was done without the clock set properly.)
We start by formatting and initializing device 1, the second of our 4GB disk images.
This process is very fast on the ZuluSCSI.
Device 1 will be our main MkLinux volume and we'll name it accordingly, though when we're finished this device will not have any HFS or HFS+ volume on it and will not appear on the Desktop.
Now to partition it.
MkLinux requires around 1.7GB to install every single package off the CD, and nowadays there's really no reason not to do so. We'll split the 4GB image into two ~2GB A/UX partitions, one for
/home
and one for everything else in
/
. Since we want to do this precisely, we'll click Custom.
The first partition on the disk is the unseen Mac device driver and should be left alone. Once we delete the other part (the HFS partition created as part of the format), the rest of this clean volume becomes unallocated space and we'll click anywhere in it to make the first A/UX partition.
This will be tagged as "A/UX Root&Usr slice 0" (or what I call the "ute-and-root"). We manually set it to 2GB.
With that partition created, we click in the second portion of unallocated space to make the second one.
This will be a "Free A/UX slice" (we'll use "slice 3" arbitrarily). We set it to the maximum remaining space, which is a little less than 2GB, but we'll deal, won't we?
Finally, we'll click Done to commit the new partition map.
This is quick first because of the ZuluSCSI, but also because HD SC Setup does not actually create the filesystems. We'll do that from within the MkLinux installer.
Finally device 2, our swap and HFS exchange disk.
We'll format and initialize this as well.
More custom partitioning.
MkLinux uses A/UX swap partitions, and can use multiple partitions as unified swap, but has a hard limit of 128MB per individual swap partition. Being an old fart, I prefer at least 2:1 swap:physical RAM, so I want 512MB. We'll blow away the HFS partition ...
... and create our first swap partition ("A/UX Swap slice 1"), manually setting the maximum size of 128MB (131072K).
Three more partitions later, we have our swap.
We soak up the rest in a "Macintosh Volume" (HFS).
Committing the final partition layout.
All done. We can quit HD SC Setup.
Now we'll insert our (real) MkLinux R2 CD, though of course you could also put an .iso on the ZuluSCSI and that would run very quickly. We will use R2RC5 here, the last official release, which you can get
from the Internet Archive
or a Garden of other Macintosh sites. The R2RC5 CD also contains components for the contemporary release of LinuxPPC, but it doesn't run on the 9150, so we will not discuss it further in this article.
Inside the
MkLinux-install
folder are multiple pieces to copy to your main Mac OS volume's system folder (to the Control Panels, Extensions and Preferences folders). A booter extension (named, oddly enough,
MkLinux Booter
) is used to launch the Mach kernel portion before the rest of Mac OS loads. This kernel is stored on the
Mac
filesystem, not the Linux one. The MkLinux control panel is used to pick the boot default, either Linux or Mac OS.
The MkLinux Booter extension understands LILO configuration files and one is provided. Open
lilo.conf
from your Preferences folder after you've copied it. Alternatively, you can click the Custom... button in the MkLinux CDEV.
The configuration file looks like this. Since we need to boot from the 9150's SCSI CD-ROM, make sure the
rootdev=/dev/scd0
line is uncommented, and no other
rootdev=
lines are specified. If you have multiple possible CD-ROM drives or emulated CDs available, you may need to change this number.
The other important part of this file is the
mach_options=
line, down at the bottom. These are the command line arguments passed to Mach. Despite the
-v
option shown there prominently, which would be expected to trigger a verbose boot, pretty much any boot is verbose in MkLinux. We'll have another use for this field when we get to our upgrades.
If you made any changes, save them, and then restart the 9150.
Shortly after we reboot ...
... we get this. This is the Booter. It has a Type of
scri
(technically a WorldScript extension, but otherwise loadable as a "regular" extension), not
INIT
, which causes it to load before other INITs and CDEVs without resorting to trickery like putting a whole lot of spaces before the name. BootX uses the same method.
The window here is as close to an About box as you'll get for MkLinux. The staff list appears to date from just before the disbanding of the LTG: from Apple, Brett Halle, Michael Burg, Vicki Brown, Gilbert Coville and Eryk Vershen, and from OSF Research Institute, Nick Stephen, F. Barbou des Places, Éamonn McManus and Gary Thomas.
Notice that in this screen booting MkLinux is the default. The default choice is set in the MkLinux control panel. Regardless of what the default actually is, press RETURN to accept it, and ESC to accept the other option.
This starts the Mach kernel and displays debugging messages. Please note that the shift of the screen to the left is not an artifact of my capture box: it looks like this on my LCD monitor also. MkLinux uses the icky VGA font for its text console, which to me seems very un-Mac-like.
The Mach kernel detects we are on a "Power Macintosh NuBus class machine" and sees all 264MB of RAM, but we immediately get some concerning messages when trying to construct the PowerPC hash table. Due to various alignment restrictions and the use of on-board RAM for video memory, we also end up with some holes in the memory map, though these holes will shortly be papered over by the virtual memory manager. This portion of the boot sequence is where memory for the MkLinux bootstrap task is allocated, though it isn't started yet.
Mach next proceeds to scan absolutely zero PCI buses, and then the SCSI bus, detecting all "five" of our devices.
It also enumerates the built-in Mac hardware, including the CUDA, ADB (keyboard and mouse), PRAM, colour console, floppy drive, AWACS sound and Ethernet. MACE Ethernet from the CURIO is detected but not BMac, which in this case also stands for "Big Mac" but has no relationship to Jobs' original Big Mac; BMac is in fact a different Ethernet media access controller (a MAC, get it?) component licensed from Sun and integrated in the Power Macintosh G3 Heathrow and Paddington I/O controllers.
Notice the
C
O
L
O
R
line when specifying the video console, and compare it with this:
These messages are from a verbose boot of Mac OS X Jaguar (10.2) in QEMU. The same
C
O
L
O
R
line appears, with
the same colours in the same order
, and almost certainly descends from
the same block of code
. Apple implied as much in the December 2000
Kernel Environment
documentation, saying, "Other parts of the system software, such as Mach, are based on technology previously used in Apple’s MkLinux project, in Mac OS X Server, and in technology acquired from NeXT." This particular message
disappeared in 10.3
as there was no need to specifically call out the console as colour by then.
The bootstrap task is now started, and the default pager (
default_pager
), the virtual memory manager, is started next. The bootstrap loads the Linux kernel as the next task, which should start from its initrd and finally enter the installer. Unfortunately, at this point we got no more messages from the MkLinux Mach kernel and the 9150 completely ground to a halt. A brief moment of panic ensued because MkLinux used to work. Was the machine shot after all?
After I got the conniption out of my system, I thought a little more carefully and realized that this new 9150 configuration was
not
the same as the old 9150 configuration: we have a ZuluSCSI, and we have approximately double the RAM. I could believe the ZuluSCSI was at fault if we were booting from it, but we were booting from the same CD-ROM I installed MkLinux from before, so that possibility seemed unlikely. That left pulling out half the RAM SIMMs.
It turns out you
can
do that much without having to disassemble the machine again to get the power supply out. It's putting the SIMMs back
in
that's the fun part, but right now we just have to make sure this can work.
We now see different messages: one less complaint about the hash table, and paradoxically a
larger
fifth free region.
This time, the bootstrap is able to successfully start the Linux kernel task. Yay!
The screen turns blue and we start getting Linux kernel messages. Notice that the default pager has smoothed out the memory map holes: the Linux task only sees a continuous, huuuuge tract of RAM.
By R2 the 2.0.38 kernel was in use, built on
gcc
2.95.2 (I don't know where the line noise came from there, and I don't know why it says "hello"). The initrd then transfers control to the Red Hat installer, without using
systemd
, which we shall consider a feature.
Now the installer, which devotees of vintage Linux will immediately recognize as "hacked Red Hat" (more specifically this is a modified Red Hat Linux 6.2). I'm still going to go through it in detail because MkLinux has some unique parts. Even though this is legit pre-R2, everything still says R1.
I should also note that on this lower-spec system, there will be multiple long pauses where the computer doesn't seem to be doing anything, and you may also get weird messages depending on what state your disks were in prior to the install. These can mostly be ignored (I think). Well,
I
ignored them, anyway.
Select your language, though I haven't checked any of the others apart from English.
And select your keyboard. This is invariably any number of ADB keyboard layouts. I'm using an AppleDesign keyboard which looks like an Apple Extended Keyboard, but
mac-us-std
suffices.
You can do a network install or from another hard disk, but we'll just use the CD-ROM ...
... which is already in the drive, and is not a Red Hat CD.
In the future I'm just going to stick the .iso on the ZuluSCSI.
Example of said spurious system messages.
Yes, I'd love to install Red Hat, er, MkLinux.
Yes, I'd love to use Disk Druid.
I mean, I can't think of anything worse than using Disk Druid.
Yes, I'd love to use fdisk and not Disk Druid.
However, we've already got our partitions set up and we really only need to assign mount points, so we select Done to move on and end up not using fdisk at all.
We now go to our
second
volume on
/dev/sdb
. The two 2GB partitions we created are
/dev/sdb3
and
/dev/sdb4
, which the MkLinux installer has treated as "Linux native." We move to
/dev/sdb3
and select Edit.
/dev/sdb3
will be
/
, so we provide that path and select OK.
Likewise,
/dev/sdb4
will be
/home
.
With our mountpoints entered, we can now select OK.
Next we ensure all the swap partitions are selected (the installer will hunt them down), though we obviously have no need to check for bad blocks, and select OK again.
After a pause while it scans packages on the CD, we are asked which partitions to format as ext2. Naturally we want both
/
and
/home
formatted, but we needn't check for bad blocks on them either, and select OK once again.
There is no reason not to install Everything.
And there is no reason not to install the Dependencies of Everything, because Everything is a Dependency for Everything Else.
An install log is left at the end of the process.
At this point the two ext2 filesystems on
/
and
/home
are created, the packages are scanned ...
... and the installation begins.
A few points of interest during the install (the time estimates are wildly inaccurate initially). The
glibc
provided is 2.1.3.
The modified Linux kernel source is naturally included ...
... along with the Mach 3.0 kernel itself.
XFree86 3.3.6 provides the X server (Wayland? ha ha ha). I'll just say now that in my prior experience X on the 9150/80 is not a lot of fun. By default it comes up in classic GNOME with Sawfish as the window manager (yes, predating Metacity), which is
dreadfully
slow, and the weak onboard video does it absolutely no favours. I recall finding AfterStep (ah, the irony), also included, more tolerable. Admittedly, Apple didn't really intend the 9150 to be a workstation and as such we're not going to struggle with it this time around, but we may possibly do so
in a future article
.
The last package, six hours and 34 minutes later.
More weird messages.
The ADB support can't determine what type of mouse you have, other than that there is (should be) one.
This is a regular Apple 1-button mouse. I would be impressed if the PS/2 options worked.
MkLinux supports dialup networking but why make it any slower than it already is? We have a 10BaseT dongle connected to the 9150's AAUI port, so we'll set up the Ethernet.
I use a static address, but BOOTP and DHCP are also supported.
Address details censored because you don't need to know what's on the internal secured network, you little sneaks.
Configuring, once again, as
brinton.floodgap.com
.
Pacific timezone, though note this predates the 2007 daylight savings change, of course. I will likely fix this later.
For the services running, we'll just use the default for illustrative purposes, though ones you know you'll want to disable can be done here directly from the installer.
No, I do not want to configure a printer.
No, I will not tell you what the root password is either.
Okay, sure.
The installer will remind us we need to change
lilo.conf
in the Mac side's Preferences folder to now point to the new root on
/dev/sdb3
. I have never tried this with an HFS file system, but it cannot mount (let alone write to) an HFS+ file system, so we'll need to do that on the 8.6 side afterwards.
As the last step, it will probe for the video settings. Again, we won't be playing with X this time, but we might later.
What it comes up with isn't too illuminating, and I'm not sure how it could be otherwise since the Mach kernel is in the way.
That's it. The installation is complete. Wasn't that fun? I hope you had something else to do for those six hours and didn't spend it like I did intermittently jumping on the "grab frame" keys.
Edit
lilo.conf
as instructed (from Preferences, or by clicking Custom...), and then restart the Mac.
Waiting for startup messages.
This time, the bootstrap task loads the Linux kernel without the installer initrd.
Bringing up the Linux kernel.
Upon entering startup, we immediately hit a mandatory
fsck
since for some reason the installer did not cleanly unmount the root filesystem.
After that it drops us into a root shell, but we'll just exit immediately, which will cause the system to reboot again.
All is clean now.
The default set of services is rather slow to start up and I'll thin these out at some point, but here is everything that would ordinarily load. Note the AppleTalk services — this is
Apple
's Linux, after all, even though
it was recently removed
from the modern Linux kernel —
and
SMB services. If you had period clients, this could definitely have been your file server, and that would have been an absolutely appropriate purpose for the 9150.
Now you can log in! Yay! The login banner does say "Release 2.0," finally acknowledging that this is almost-R2, and displays the CPU and kernel version in use.
Some basic info, for the record (from a telnet session):
brinton:/home/spectre/% uname -a
Linux brinton.floodgap.com 2.0.38-osfmach3 GENERIC_09 #9 Tue Mar 7 10:51:13 PST 2000 ppc unknown
brinton:/home/spectre/% gcc -v
Reading specs from /usr/lib/gcc-lib/ppc-yellowdog-linux/2.95.4/specs
gcc version 2.95.4 20010319 (prerelease/franzo/20011204)
brinton:/home/spectre/% ls -l /mach_servers
total 3615
-rwxr-xr-x    1 root     root      1349896 Jan  7  2001 Mach_Kernel
-rw-r--r--    1 root     root       119033 Jan  7  2001 Mach_Kernel.map
-rwxr-xr-x    1 root     root       131314 Apr 19  2000 System.map
-r--r--r--    1 root     root          123 Feb 22  1998 bootstrap.conf
-rwxr-xr-x    1 root     root       205690 Jan  7  2001 default_pager
-r-xr-xr-x    1 root     root       257371 Feb 22  1998 mach_init
-rwxr-xr-x    1 root     root      1614475 Apr 19  2000 vmlinux
You'll notice a couple files dated 1998 — those are basically historical artifacts from earlier versions that got installed along with everything else.
As I have shown you startup, I should now show you shutdown. (
Sing it
with me: Startup, shutdown, startup, shutdown, swiftly fly the rc files ...)
CPU halted.
Pimp My Green Giant Ride
We have now returned to the functionality of our prior configuration: we can dual-boot MacOS and Linux. However, with motherboard video, the baseline CPU, half its maximum RAM, and half the L2 cache it originally shipped with, right now it's not a particularly strong performer in either operating system.
Of course, the set of what upgrades are supported in Mac OS 8.6 is rather larger than the set of what upgrades are supported in MkLinux R2. For example, while G3 upgrades are available for the PDS connector in NuBus Power Macs and generally work well in Mac OS, most of them don't work in MkLinux, and MkLinux doesn't support NuBus video cards either. There is also the matter of that 128MB of RAM we had to remove that we would like back. Ideally, with these plastics continuing to crumble, we would like to find a maximal configuration suitable for both operating systems that can be changed through software as needed, rather than having to keep opening it up.
The
MkLinux FAQ-O-Matic
has somewhat conflicting information about which CPU upgrade cards work where and how, though the various reports do seem to agree that Sonnet cards won't work at all. On the other hand, while one reporter indicated success with a Newer Technology MAXpowr G3, I'm not entirely confident in his recollection because despite being a PDS card he said it displaced the
L2 cache
. The MAXpowr G3 PDS also lists the 6150 and 8150 but not the 9150
as compatible
, even though the PDS connectors are the same; there may be a form factor limitation.
But the 9150
is
specifically listed as compatible for the Sonnet G3, and Sonnets are much more common. As long as the Sonnet extension loads
after
the MkLinux Booter extension, the upgrade card should remain inactive, and MkLinux can run unmolested on the 601 (we can leave the L2 cache stick in, even). For the Mac OS, we can use the G3 there. As it happens, I have a couple spare G3 cards in the stock closet and this seems like the perfect time to put one in service.
Sonnet produced multiple G3 NuBus upgrades up to 500MHz, but also a much less common 360MHz G4 (7400). All shipped with L2 backside cache.
Unpacking the NOS upgrade along with a "Powered by Sonnet" sticker and the Crescendo INIT installer floppy.
Sonnet branded the two highest-tier G3 cards as "Fortissimo." These cards have 1MB of L2 and run at either 400MHz or 500MHz; this particular card is one of the slower 400MHz ones, but still a substantial speed boost over the stock CPU. They carry their own PDS connector for daisychaining a video card. We'll revisit this in a little while.
Initially I put the PDS terminator in it, turned the system on and got nothing. Intemperate statements not fit for a family blog may have been uttered. I pulled the PDS terminator out, turned the system on and still got nothing.
After the screaming subsided, I noticed that the logic board — increasingly free of the case's degenerating snaps and clips — had slightly tipped forward off its moorings into the plungers for the interrupt and reset switches and caused their buttons to be held down. I pushed the board back with a gloved hand and got
the Power Mac car crash sound
(further yelling censored). After unplugging it, pulling the G3 completely and putting the PDS terminator back in, I got the normal startup chime and a normal boot, so I put the G3 back in. This time it booted as well. (It also appears that the PDS terminator is not needed in this card; it seems to terminate the bus just fine by itself.)
The floppy contains the Sonnet extension installer.
Splash screen.
We'll go ahead and install everything ...
... and then reboot.
After cancelling out of the MkLinux Booter into Mac OS, the Sonnet INIT loads and enables the processor on the PDS card.
The Metronome utility (also on the floppy) clocks out the bus and backside cache speeds. As with most CPUs of the time, the 601 runs at a fixed multiple of the bus speed. The NuBus Power Macs run their CPUs at either 2x or 3x the system bus, which varies up to a rated maximum. For example, the 66MHz 7100 has a 33MHz system bus and the processor runs at a 2x multiplier, while the 110MHz 8150 has a 36.7MHz bus and runs the CPU at a 3x multiplier. Prior 604 and early G3 cards worked on the same principle with additional possible multipliers; the 604, for example, can run at 1x, 1.5x, 2x or 3x bus speed, and later 4x.
While the G3 can have a multiplier as high as 10x, this would only get you, say, 333MHz on a 33.3MHz bus, and none of these early Power Macs has a bus speed over 40MHz. The Fortissimo cards solve this problem by feeding a double-pumped bus to their CPUs, then using a standard multiplier from there to get as close as possible to their rated maximum. This actually means that most configurations won't get all 500MHz in the top-end card; only on the 100MHz 8100 is full speed achieved with the others between 477MHz and 495MHz. On the other hand, the 400MHz card here will get 400MHz on all systems with at least a 33.3MHz bus, and the 8100/110 and 8150/110 actually eke out 403MHz because they use a 5.5x multiplier on a doubled 36.7MHz bus. (Sonnet's 466MHz G3 upgrade for the PowerBook 1400, internally NuBus as well, uses the same trick on a 33.3MHz bus for an effective 14x multipler.)
Note that the
actual
system bus is
not
doubled, which is to say that any bus access these CPUs make could stall depending on whether it corresponds to the real bus clock. These cards therefore must have a crapload of cache to smooth such gaps out, and indeed both of these fastest cards have a full 1MB of backside L2. The backside cache bus runs at double the system bus speed, but the cache is on the doubled "local" bus, so the cache speed is effectively 4x the system bus.
The 9150/80 here is a 40MHz bus system, meaning the G3 card's local bus runs at 80MHz, the backside cache at 160MHz, and the CPU at a 5x multiplier for the full 400MHz. Even if I hunted down a 500MHz G3, and while I'm crazy I'm not made of money here, I would only see 480MHz on this system (6x multiplier). Sonnet's Metronome faithfully reports all these numbers, but Apple System Profiler doesn't know about the doubled "local" bus, so it erroneously thinks the CPU is only 200MHz.
It is possible to make the Sonnet extension load before the MkLinux Booter extension by also setting its Type to
scri
, then inserting spaces and/or changing its filename to sort above it.
Unfortunately and as reported, starting the Mach kernel with the G3 activated indeed causes it to hang immediately with the message "System booting". Most likely this is because Mach can't handle the system being detected one way but the CPU being detected another, especially because the 601 has important differences from all subsequent PowerPC CPUs, and the bus skulduggery probably doesn't help. I'd be fine if I could get even 200MHz out of it, but the Sonnet extension proudly doesn't allow any frobbing, and using the MAXpowr G3 PDS extension with the Sonnet doesn't work either (the extension sees it's not a MAXpowr, and refuses to enable it).
For the time being, I reverted the Sonnet extension's Type back to
INIT
to load it later. That way we can continue to boot MkLinux normally on the 601 (with the motherboard L2 cache, which we never removed), yet still enjoy the benefits of the G3 — and it is
much
snappier — in Mac OS 8.6.
Now for the RAM. If I had done a little more reading of the fine manual, which hadn't been necessary before because it "just worked" with "only" 136MB, I would have discovered
an
-m
option
that caps the amount of RAM Mach will use. You pass it on the
mach_options=
line in
lilo.conf
, e.g.,
mach_options=-m136
.
To test this, we'll need to install the full 264MB. With some difficulty you can worm the SIMMs back in without removing the power supply. However, that also knocked the board back into the interrupt and reset switches again, and the second time around was not much more reassuring.
Too much memory was apparently
a significant problem
in some configurations of MkLinux, and values that work for booting the installer for testing purposes may not necessarily work for an installation (for example, I tried
-m200
, and while this worked for the installer it could not start the kernel installed on the ZuluSCSI image). A cursory look at the Mach kernel source suggests that there is a hard upper limit on the number of VM hash buckets and when this overflows, the kernel goes into never-never land.
-m191
seemed to be the highest value that would work either way, but I left it at
-m136
since that was the RAM amount that we started with and that I knew was reliable.
I was now pretty thoroughly irked by the problem with the front switches and decided I needed to do something about that.
At this point I disassembled the machine back down to the plastic backing. I told you everything was breaking apart and now you can see it. What was not restraining the board anymore was the big clip in the front which had simply fractured, though you should also be able to see that a number of the smaller clips came off as well. It's just crap plastic now.
The board does have a few screw-size-ish holes in various random places. I surmise they were used to mount it during testing, since they don't appear to have any other obvious purpose. I used a pencil to mark them on the plastic.
Next I got out my box of nylon screws, to avoid both the risk of shorting anything and damaging the board, picked a couple long enough that would fit and selected a drill bit to match. With the drill I reamed out the marked holes down to the metal shell
carefully
at low speed.
This was not uniformly successful, because one hole cracked and another I misaligned marking it (and it was too close to the real position to correct), but the other four were suitable for hanging. I screwed in the nylon screws by hand and this was good enough to keep it better suspended and
mostly
stable.
Still, they're nylon and they bend, and while it helped they were not precise enough to fully correct the problem. By the end of this work I ended up using binder clips carefully positioned between the case front and the edge of the board to give it sufficient clearance. The large binder clip at the bottom was the first try (the Velcro is there to hold it while I experimented with positions), but the one that seems to have finally fixed the problem is the little one installed horizontally between the switches. This clip was big enough to be tight, but still small enough to fit, and you can see now that the plastic plungers are just resting on the switch buttons as they should be. If I end up taking this apart again (oh boy) then I think I'll try putting the small clip in the back and installing the plungers over its metal wings.
The big clip still serves a purpose for the lower portion of the board and I ended up relocating it there. You'll see various iterations I was trying in the pictures below.
Since we're still mounting stuff, I decided this was a good time to get the disk tray back in. This two-story metal hard disk condo came standard and stacks five hard disks with selectable SCSI ID encoders. In Brinton's previous iteration there were two HP disks here and it worked well. Since we're now moving to a single ZuluSCSI, and its plastic tray does not quite match the mounting holes, I used a tight screw as a pivot and mounted it facing backwards but with the SD slot still accessible.
We're obviously not going to loop the cable as instructed on the side door, and with terminator power we don't even need the Molex power connectors (I threaded a set through the back for the DAT and CD-ROM), but we
will
use the Velcro straps to neaten everything up. I put the SCSI cable's excess length into the bottom compartment of the hard disk tray.
Now for video cards. Again, the set that MkLinux supports is a much smaller set than what Mac OS supports, but motherboard video is not a lot of fun on this system. Although the documentation says NuBus video cards won't work, I decided to see just how
much
they wouldn't work.
In my parts bin is a Radius PrecisionColor Pro 24XK. The reason I marked the name on it is that the 24X, 24XK and 24XP are closely related and can be hard to distinguish visually. From my experience the highest-end 24X has all 12 RAM chips along the top instead of the 11-1 arrangement here on the 24XK and 24XP. Another difference appears to be the speed of the Brooktree Bt473 RAMDAC, which is the silkscreened number at the end of the chip identifier (the 24X is 110MHz, this 24XK is 80MHz and the 24XP is 66MHz).
Installed.
The primary functional difference, other than RAMDAC speed, between the lowest-binned 24XP and this midrange 24XK are the supported resolutions. All three cards support 640x480, 800x600 and 832x624; the 24XK adds 1024x768, and the 24X adds 1152x870 and 1152x882. As the name suggests, they are all 24-bit colour capable. I don't have the accelerator extension installed, a necessity because of the NuBus overhead, but doing so would be pointless if it doesn't work in MkLinux.
And, well, it doesn't. Although the Mach kernel appears to detect it as a directly attached video card (more on that later) and is able to start the Linux task, the Linux task dies very early with a machine check, yielding a kernel panic and a nearly illegible backtrace. I didn't even bother checking lower colour or screen resolutions since we have alternatives, and it wouldn't be accelerated in Linux even if it were in Mac OS.
The other way to upgrade video in this class of Power Mac is with a PDS video card, which we talked briefly about when we discussed the PDS terminator. Recall from before that most Power Macs of this generation either shipped or were upgraded with PDS video cards, primarily the High-Performance Video (HPV) card, but AV Power Macs had a separate, slightly slower yet more capable option with video input as the (wait for it) A/V Card. They are unaccelerated, but are still rather more sprightly than NuBus video because they're directly attached to the processor bus, making them basically a faster framebuffer. On the other hand, the Workgroup Servers 8150 and 9150 were notable for shipping only with motherboard video, so they came with the terminator.
Because the G3 PDS upgrades necessarily occupy the same slot, it wouldn't be much of an upgrade if boosting your CPU required you to work at a lower resolution or colour depth or use a weaker graphics card, and the perpendicular orientation of the second PDS connector on the G3 card itself makes it only functional for the 6100 family (including the WGS 6150). On the other systems a more creative (read: hacky) solution is required.
This is my "SR-7100," which also has a PDS G3/400, plus a PDS A/V card taken from a 7100AV. On these systems the video problem is solved by putting the PDS video card into a NuBus slot. How, you ask? By a really tough ribbon cable running from the PDS connector on the G3 to the card edge of the PDS video card, and then using a dummy bracket to mount the video card on the NuBus slot. The NuBus connector is only used for structural support — electrically everything looks the same to the Mac. The same setup is used for the 8100 and 8150.
This solves the problem, though with a couple obvious disadvantages. The interposer ribbon cable has to be especially tough because it has active components and may need to be bent into unusual contortions to fit into both sides, and you usually can't put the bracket immediately next to the G3 because the angle is too tight. As such, you not only lose the NuBus slot that the PDS video card is mounted in but possibly also the slots between them too. But the SR-7100 doesn't have any other cards, so it's fine.
Also, you'll have noticed that in this 7100 the PDS connector on the G3 is on top and the cable sweeps above to the card edge of the A/V card (in this view at the top/north). However, this is not the situation for the 8100 and 8150, where the connector ends up facing down. In that case, the bracket has to be flipped and the video card's tab manually bent backwards.
As it happens, the 9150 — notably never advertised as compatible with this kit — is the same way, so we'll set up our video cards like an 8100.
These adapter kits were not super-common back in the day and like all legacy Sonnet upgrade cards now go for stupid money, so since I'm thinking this will probably become my new workhorse NuBus Power Mac, I decided to pull the entire assembly from the SR-7100 and we'll use the 24XK in that machine instead.
We'll first try the A/V Card, since it's already attached. Again, the documentation says this won't work in MkLinux either, but
Kan's page
claims it does, so I just have to push it. This card has both composite video in and out as well as a conventional Mac DA-15 video port. Although the card is slower than the HPV card, it has 2MB of VRAM and correspondingly more colour depth and resolutions, so it's worth giving a shot.
Before we go bending the card tab or flipping the bracket, we'll just run the cable out beside the machine, put the card on an antistatic mat and test them that way.
Getting the A/V card configured as the primary monitor.
The stock 2MB on the A/V card gets you up to 1024x768 in 16-bit colour. With two 1MB VRAM sticks in its slots, which I don't have, this gives you up to 24-bit colour. All slots must be populated.
Booting MkLinux, it's interesting that it does detect it correctly, but halts anyway. The pager and Linux tasks never even get started. Since the whole reason to use this over the HPV card is the additional colour depth, and it's slower too, once again there's not much point in checking other resolutions or depths.
That leaves us with the regular HPV card. The HPV card came in two variants, the 2MB 8100 (more desirable and less common) and the 1MB 7100 (less desirable and more common), which is what this is. The 1MB card can be expanded to 2MB; the 2MB can be expanded to 4MB. Again, all slots must be populated.
Configured with our perilous chain of dongles to the capture box.
This card is identified as a "HPV Display Card v1.0a2" (by the way, as someone whose day job is in public health, Apple should generally avoid confusing their products with papillomavirus).
This time we only get 8-bit colour depth, but we still get it at 1024x768.
Unlike the A/V card, the Mach kernel fails to detect the HPV card as such. In fact, it uses the same string it did for the Radius 24XK ("unknown (using VDS port)"). However, it successfully gets into the bootstrap ...
... and boots the installer kernel, so it works. I'll see if I can max out the VRAM later, but for now, we have faster video and larger video even if it's still 8-bit. Hey, it's no worse than the Apple Network Server's onboard VGA.
Now we have to worm the card in there. The bracket Sonnet provides is designed to be reversible, so I flipped it over, bent the tab back on the HPV card
as directed
and installed it that direction in the middle NuBus slot. It still needed some squeezing to make it and may have nailed the frame around the NuBus slots, but it fits.
This position does end up pushing the DA-15 port into the back and makes it harder to plug in a dongle, so I got out an extension cable which I'll leave permanently connected.
Near the end of this project, because this machine keeps finding new and exciting ways to malfunction, what I thought was the front switches getting mashed again turned out to be a defective speaker. Naturally it's difficult to find an exact replacement: this is a 4" 16 ohm 3W speaker, the same one (as usual) as in the Quadra 900, 950 and AWS 95, and it seems that 4" speakers of that impedance are not especially common nowadays. I confirmed the speaker was bad by getting a 3" 16 ohm that came from another Mac, connecting that and getting a chime, but that speaker may not mount very well and it's only 1W. I'm toying with finding a 4 or 8 ohm one of the right size and putting a resistor on it so I don't pull more current than the board is expecting.
That can be a project for later. For now, we have a NuBus Power Mac server, the only one of its kind, that can dualboot Mac OS and MkLinux in nearly maximal configurations  without requiring me to mess around some more in its degenerating interior. It's time to put the door back on and close it up before more plastic starts snapping off.
Incredibly, the two portions I thought would have broken long ago still haven't: the two clips on the door. (I've probably just jinxed it, haven't I?) These are semi-spring loaded (the springy part of the plastic is intact but not too springy now) and clip the back of the case. But that also probably says something about how long the side door was off this thing rebuilding it.
We finally close it up completely with the security screw. We're ready to dig more into MkLinux in
a future article
and see if any hacks in the kernel are possible to improve the situation. If not, at least we'll have fun exploring the infrastructure.
The Workgroup Servers did not survive the axe of Jobs either: after the 7250 and 8250, the last Macintosh systems to bear the Workgroup Server name were the Workgroup Server 7350 and Workgroup Server 9650 in April 1997, which were cancelled less than a year later in March 1998. With the introduction of the beige G3, the "Workgroup Server" brand was retired for the "Macintosh Server G3," which encompassed both the beige mini-tower in March 1998 and later the "Yosemite" Blue and White G3 in January 1999. Apple did not reintroduce bespoke server hardware to their product line until the rackmount Xserve G4 in 2002, which survived in G5 and Intel-based incarnations until 2011 when they were cancelled — per Jobs — "
because hardly anyone was buying them
"; a 2009 server version of the Intel Mac mini, in some ways a spiritual descendant of the Workgroup Servers, was itself cancelled in 2014. Even though there are still lots of Macs in offices, to date no official server hardware has ever returned to Apple's product line-up since.
