---
title: "Refurb weekend II: Alpha Micro Eagle 300 and friends"
url: "https://oldvcr.blogspot.com/2026/10/refurb-weekend-ii-alpha-micro-eagle-300.html"
fetched_at: 2026-10-12T10:10:59.934116+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Refurb weekend II: Alpha Micro Eagle 300 and friends

Source: https://oldvcr.blogspot.com/2026/10/refurb-weekend-ii-alpha-micro-eagle-300.html

This Refurb Weekend is a sequel in two ways.
Six years ago
I fixed the power supply and case fan in my 68EC030-based Alpha Microsystems Eagle 300, a more modernized and substantially faster Alpha Micro running AMOS, their unique DEC-inspired multiuser operating system. These blue-collar boxes were very common in many vertical markets due to their tightly integrated business-specific software packages, and are especially unusual for running their big-endian 68000-series processors
little
-endian (for data file backwards compatibility with their WD-16 ancestors). The 1990s-era Alpha Micro Eagle family improves on the originals with later 68K and even ColdFire CPUs, plus Ethernet and faster SCSI.
The second way it's a sequel is to
our previous Alpha Micro refurb weekend
, a double header restoring an Alpha Micro AM-1000 and AM-1200, two members of Alpha Micro's most popular series of computers and some of the closest things they made in the early '80s to desktop workstations.
From the outside, the Eagle comes in a PC-style case, but it's not a PC:
This particular Eagle 300, with a 40MHz 68EC030 CPU, runs
ampm.floodgap.com
using the webserver provided with AlphaTCP — yes, Alpha Micros
can be networked
— and its own on-board Ethernet. At the time the cooling fan failure was putting a lot of strain on the hard disk because it was overheating, and since this was my first Alpha Micro and I wanted to keep it in good nick, I decided I would put a SCSI2SD in it after the repair and get rid of the spinning disk entirely. Fast-forward to last fall, a little over a year ago, when I tried to do exactly that with a ZuluSCSI.
And then it wouldn't start.
It would power on, but it wouldn't enter the boot sequence, not even with the old hard disk back in it, not even to run the internal self-test. I was worried I'd negligently blown one of its two main system boards and that meant I needed another. This entry took as long as it did to come to fruition because Eagles in general aren't easy to find, and on top of that I was looking for a specific one. Through a couple of referrals I managed to get what I
thought
was a replacement unit I could raid for parts, but it turned out to be something rather more special — and then I was even more fortunate when I got the Eagle 300 back out of storage to make one last attempt at reviving it.
To cap it off we'll go stick ZuluSCSIs in everybody else, including my Motorola ColdFire-based Eagle 450, the first ColdFire server ever produced and what
used
to be the fastest Eagle in the house until the new hotness came. I even converted the external BlueSCSI the AM-1200 was using to an internal ZuluSCSI too. Now nearly everybody's got a solid-state boot disk and they're all a good bit more zippy, so we'll gawk at the internals, compare 68K CPU and storage benchmarks and most importantly learn from my mistakes, because as my late father always said, "I'd rather be lucky than good." On a more solemn note, we'll also observe a moment of silence for one of the line's creators who passed away last year. It's time for a Refurb Multi-Weekend Sequel.
Alpha Microsystems, founded in Orange County, California in 1977, produced what were considered some of the earliest "poor man's minicomputers," smaller and more affordable multi-user systems that run a bespoke, Digital Equipment Corporation-influenced operating system named AMOS. In our previous entry we discussed
their history in detail
. First-generation Alpha Micros like the AM-100, designed by Dick Wilcox who also wrote most of the operating system, used large S-100 cases and a CPU chipset called the WD-16, derived from the Western Digital MCP-1600 chipset — the same one used in DEC's LSI-11 CPU — but with higher performance microcode developed by Rich Notari. These machines thoroughly outclassed low-end PDP-11s yet were substantially cheaper, and Alpha Micro found a ready audience initially with hobbyists and then later corporate turnkey environments, where its integrated AlphaBASIC and database functionality gave it a competitive advantage. As the WD-16 had little elbow room to evolve, in 1982 Alpha Micro introduced new systems based on the Motorola 68000, porting AlphaBASIC and AMOS to run natively, but swapping address lines to make it appear little-endian for compatibility with WD-16 data files and AlphaBASIC P-code. These new machines included
the AM-1000
, Alpha Micro's most popular single model, and by 1984 it constituted the majority of the over 20,000 Alpha Micro machines then in active use.
An idealized Alpha Micro office from the 1980s might look like this photo, from their actual advertising of the period. The main system is an AM-1042E, the S-100 box sitting on the pedestal next to the printer, using an AM-100/L CPU with an 8MHz 68000 (the same as the AM-1000, which was integrated into a desktop case), and in the factory-standard configuration shipped with 512K of RAM and a 60MB Winchester ST-506 hard disk. The system served some number of local users connected directly via serial ports, in this case the two administrative assistants with AM-60 terminals (a modified and rebadged Wyse WY-100). The fact everyone here was in the same room with the machine was helpful, because AMOS is a strictly real-memory operating system and executable code ran from where it was loaded in the user's fixed memory allocation — there was no memory protection. Although the admin assistants' explicit permissions were limited by which account they were logged into, using the same style of project-programmer numbers as DEC (e.g., [1,2] being the operator account), an errant job of theirs could readily stomp on another and it was not rare for busy systems with buggy software to regularly crash. On the other hand, this also made it fast and efficient with little separation between you and the hardware, and even Alpha Micros with fairly modest specifications could support hundreds of simultaneous users.
Alpha Microsystems tried multiple times to broaden the line technologically, though these efforts were largely for naught. Early attempts to put equivalent hardware onto a PC ISA co-processor card, with software to interchange between MS-DOS and AMOS, yielded only an expensive and poorly-selling PC that wasn't good at either OS (eventually the company gave up producing turnkey systems and just sold the card). In 1984 Alpha Micro introduced UNIMOS, a licensed version of AT&T System V UNIX which ran on modified AM-1000 hardware with an MMU, but it was likewise too expensive and garnered little interest from new users nor demand from existing ones. The cost of its development, the Unix license and its associated royalties, and a simultaneous lawsuit from DEC over AMOS's similarities subsequently caused lasting damage to the company, and by the end of the decade Alpha Micro found itself almost entirely dependent on legacy AMOS users. In the wake of Wilcox's 1990 retirement and original investor Bob Hitchcock's own departure in 1991, new management tried once more with Unix systems based on the Motorola 88000 — which Motorola abandoned shortly afterwards for the PowerPC AIM alliance, and so no hardware ever shipped.
If the platform couldn't be migrated, reasoned Alpha Micro leadership, then it would have to be modernized. A solution was needed for two problems in particular: more up-to-date yet less expensive and fully backwards-compatible hardware for new sales from their risk-averse userbase, and an upgrade path to entice users flatly refusing to part with their old machines. Up to this point, system upgradability had been somewhat uneven and highly model-dependent. RAM and serial port upgrades were generally bespoke boards made from discrete parts which were tedious to replace and repair. Although Alpha Micro had been quick to incorporate Motorola's subsequent 68K CPUs, these higher-performance processors generally only appeared in their larger, more expensive server systems (with the notable exception of the '020, first in the AM-2000 but later in the AM-1600, notionally a desktop computer). Some machines could be upgraded with board swaps, though this wasn't particularly cost-effective, and at the time the most popular AM-1000 and slightly upgraded AM-1200 systems had no official upgrade path from Alpha Micro at all. The December 1987 AM-3000 was the first 68030 machine available from
anybody
— yes, really, just two months after the '030's October introduction — initially offering a 20MHz CPU, 32K of L2 cache and supporting up to 360 simultaneous terminals, but even the lowliest 30-user configuration started north of $40,000 [about $117,600 in 2026 dollars]. By contrast, Alpha Micro was uncharacteristically tardy in adopting the 68040 and didn't release the 33MHz AM-4000 until 1993. It was nevertheless nearly as expensive, and for most small offices, which were now increasingly Alpha Micro's financial anchor, that kind of money was simply beyond consideration.
In 1993 the company settled on a two-board approach to solve both problems at once. The CPU board, dubbed the Roadrunner and designed by engineer Joshua Stumpf, contained the new processor, standard RAM SIMM slots, L2 cache (if present), and SCSI controller. This board was specifically designed to also fit in legacy machines, specifically the desktop AM-1000, AM-1200 and AM-1600 and server AM-2000 and AM-3000 systems, and initially came in a 68030 and two 68040 versions. A second board served as the CPU board's system interface, linked together using a custom "X-BUS" interconnect over twin 34-pin cables. For legacy installs, this second board was an active interposer physically replacing the original processor, which in elderly units sometimes needed to be desoldered (though that was also true for the few third-party CPU upgrades then extant, like InterLink's Dimension-030, so the Roadrunner was at least no worse). But this second board could be a whole new system architecture of its own, and that was what the I/O board was, designed by Rod Hewitt. It carried the power supply connectors, controlled the system front panel, contained the System Security Device for licensing (more on this later), presented built-in external ports for parallel, SCSI and (for certain loadouts) Ethernet, had an internal port for an optional floppy drive, and provided SIMM-format "paddle card" slots for option cards. Best of all, these boards were smaller and — by using off-the-shelf commodity hardware — cheaper to manufacture, and could be paired into multiple configurations, together becoming the company's long-promised updated low-end and mid-range systems.
In 1994, the new architecture launched — or perhaps I should say took flight, as the Alpha Micro Eagle family. These earliest systems shared a common PC-type minitower deskside case which was also used for a reworked AM-1600LC desktop system and the AM-950 486DX2/66 PC. The central model was the Eagle 300, powered by a 40MHz 68EC030 CPU board (remember, AMOS doesn't need an MMU) and an I/O board with SCSI-2, two parallel ports and Ethernet, plus four paddlecard slots for up to 32 serial ports. The Eagle 400 was correspondingly the same I/O system board with a 33MHz (billed as 66MHz because of the '040's double-speed secondary clock, to be discussed in the second half) full 68040 CPU board and 32K of L2 cache; the Eagle 500 had a 40MHz (80MHz) one. But their best attribute was the price: unlike the big AM systems, these machines started at just a few thousand dollars, depending on license caps, and they'd run all your old software.
If that was still too expensive for you, the company added two more choices that were even cheaper. One was the Eagle 200, which mated the 68EC030 CPU board with a cut-down system board missing Ethernet, one of the parallel ports and two of the paddlecard slots. In November the lowest-end Eagle 100 dispensed with the modularity of the other systems entirely, consolidating the 68EC030 CPU and I/O boards into a single logic board also designed by Hewitt with eight built-in serial ports, no standard Ethernet (offered through a paddlecard upgrade, which I'll show you), only one parallel port and only one paddlecard slot. As promised, Alpha Micro also offered legacy upgrade packages using the same Roadrunner CPU boards, sold separately with their system-specific active interposers for existing installations.
This is my own Eagle 300, shown here when I unpacked it in my apartment in 2007. It came in the standard four 5.25" bay case shared by all five initial configurations, which I was delighted to note was little-yellowed and even now nearly two decades later is still largely unblemished. The case was not custom-built for Alpha Micro and was merely an off-the-shelf one they bought in bulk, though I have not yet found the OEM. This computer was my first fully operational Alpha Micro; I had always intended to own one personally for
reasons I've related elsewhere
, and I managed to land it for just a couple hundred bucks in fully working order. (Boy, are those days gone.)
Based on the software still on the hard disk, this machine was previously used at a chain of three party stores in Washington state as a centralised rental and point-of-sale system, a common turnkey application. On arrival it sported the same loadout as in this article's first picture except for its original smaller-capacity Tandberg QIC tape drive, which in Alpha Micro parlance is called a tape streamer. Since these systems don't boot from CD, QIC tape is your only way to cold start and restore most 68K Alpha Micro computers if the hard disk fails. These systems also don't support the old Alpha Micro VHS backup system, hopefully to be the subject
of a future article
, which was ubiquitous in their early hardware. There is a single hard disk in the second 5.25" bay, though these first-generation systems also supported 5.25" and 3.5" floppy drives using an AM-219 controller board.
Pictures of the case in other Alpha Micro marketing literature showed two "badge" areas which contained the vendor logo and, improbably, a little LCD clock. (This appears to have been stock photography from the OEM; perhaps that tidbit jogs someone's memory about the case.) For the Eagles, Alpha Micro commissioned two customized metal badges for those areas which are seen on most members of the line. They look very nice and give it a pro feeling.
Because it's a PC case, it has a PC front panel, including a "Ace"-style tubular keylock (fortunately unlocked, since I don't have the key), a reset button and a turbo button (for which the manual says, to everyone's great disappointment, "The Turbo button is not functional in AMOS-based Eagle configurations"). Above them are three LEDs, for system power, CPU activity and disk activity, and then to the right a space for a numeric LED. This is where a PC case of the time might have had the system's current speed, but AMOS has another use for it which we'll demonstrate.
The rear of the unit is also fairly standard. The I/O board's external ports emerge on the far left/west edge, and the card slots and external Centronics-style SCSI port are in the middle. This is a two-board system, so there are two case fans, one in the power supply and one down below. The one at the bottom is the Noctua fan I installed during the
original Refurb Weekend
.
The backplate shows the system's vital statistics. Although collectively the family are called Eagles, the internal designation for the Eagle 300 is the AM-3500-E300 (so the E400 would be the AM-3500-E400, and so forth, reflecting their common ancestry), implying it slotted between their AM-3000 and AM-4000 large systems. It is serial #02233 with a stated manufacturing date of January 1998, relatively late in the model's lifespan. This particular machine might have been a warranty replacement because the system initialization file indicates they took delivery of the system in December 1997 and the serial in that file is slightly earlier (#02200).
The plate sticker also carries the SSD serial number as shipped from the factory, or System Security Device (not to be confused with the modern solid-state drive). In
our previous Alpha Micro foray
we discussed the SSD's role, a chip installed in every 68K (and later x86) Alpha Micro, even the earliest S-100 boards, used by the operating system and any installed VAR software packages to enforce copy protection and license caps. The SSD number on the rear is just a serial number, printed on the rear plate for convenience and engraved on the SSD chip inside, which I'll show you in a moment. This number is not the key stored inside the chip, up to 256 bytes in length, which only Alpha Micro recorded. When a VAR wanted to lock an install to a particular system, they would provide their private code to Alpha Micro plus the user's SSD serial number, and Alpha Micro would look up the key and generate an alphanumeric PIC (Product Installation Code) that the VAR either used for direct installation or to provide to the user. During the installation process the PIC (usually irreversibly) encoded a binary overlay for the protected executable(s), making it impossible to run them on a system where the SSD didn't match. To facilitate logic board swaps and upgrades, the SSD is socketed and easily transplanted into a new board, but PICs were expensive then and unobtanium now, another reason hard disk backups were so critical.
From top/north to bottom, the ports on the system board are twisted-pair Ethernet (10BaseT), DIP switches for setting the boot device which will become very important later on, an AUI Ethernet port (same NIC as the TP Ethernet, so both cannot be used simultaneously), and two SPP IEEE-1284 ports for parallel printers.
Although Alpha Micros could be networked with the bespoke AlphaNET system and the Eagles were not the first Alpha Micros to have Ethernet, AlphaTCP was developed at the same time as the Eagles, and ran on Ethernet-equipped Eagles as a first-class citizen (AlphaTCP could also be configured to run over SLIP). The web server I run on this one is how I came by some of the development history of the Eagles because Rod Hewitt himself let me pick his brain, and later AlphaTCP developer Steven Lawson, who were delighted to see their creations still in use and filled in the details. I'll come back to a critical piece of Rod's recollections in a moment.
In the middle is the single Centronics-style external SCSI port, which I removed the external terminator from for this picture, and then eight cutout "slots." These cutouts are actually sized for an RJ-21 Amphenol connector and we'll see such a setup in our second system. The bottom/south four look like Ethernet connectors, but are in fact Alpha Micro-specific 8P8C ("RJ-45") serial ports that can be turned into a more typical RS-232 DE-9 ("DB-9") or DB-25 with a passive modular connector. A straight-thru Ethernet cable can connect the two sides, which is convenient and space-saving. On this unit the prior owners had labeled which port was for which terminal or serial printer.
Here it is running in 2007 with its original AM-65 (modified Wyse WY-150) serial console. Onscreen I'm looking at the contents of the AlphaTCP "directory," which is really a project-programmer number, because as mentioned AMOS is so greatly influenced by DEC operating systems like TOPS-10 and RSTS/E, and to a lesser extent RSX-11, that DEC dealt a heavy financial blow to the small company by unsuccessfully suing them over it in 1984. AMOS not only uses PPNs but the same 6.3 filename structure, and many of the same or similar commands.
In case you're ever unsure whether the site on the other end is an Alpha Micro, here's the HTTP headers from it as of today:
% curl -I http://ampm.floodgap.com/
HTTP/1.0 200 OK
Date: Sun, 11 Oct 2026 23:43:03 GMT
Server: AMOS-HTTPD/1.3C(111)
MIME-version: 1.0
Content-type: text/html
Last-modified: Sun, 11 Oct 2026 23:42:00 GMT
Content-length: 30242
Content-encoding: 7bit
This is an older version of AlphaTCP, but it works, though this version of the webserver is limited to HTTP/1.0 and does not support virtual hosts or keep-alive.
Later on I got it an AM-75 (modified Wyse WY-370) colour head, which is what it uses now and the terminal you saw
in our most recent article
. In this picture it's also attached to an AM-401 CD-ROM, which is the trusty Toshiba XM-5401B in an external case, though only specific ROM versions are supported. It can't boot from this drive, but it can read AMOS-formatted partitions, and with external software can also access ISO 9660 filesystems.
Onscreen is a performance estimate using the built-in
SI.LIT
tool, which we'll be using to benchmark our new solid-state disks when we get them in there. Here's that output.
.si dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(114)

               Computer Type: Eagle
              Main Processor: 68030
                Co-Processor: None
                 MMU present: Yes
            Operating System: AMOS 2.3A(484)
          Boot PROM revision: M00
              Number of SSDs: 1
                Total Memory: 16384 K-bytes
     Resident Monitor Memory: 6218 K-bytes

     Computing Index (CX), relative to AM-100:    36.9
     48 bit FP Index (4X), relative to AM-100:    36.3
Floating Point Index (FX), relative to AM-100/L:  5.6
          Disk Index (DX), relative to ST-506:    15.3
I don't know why it identified the 68EC030 as having an MMU, because it doesn't, but we're mostly interested in the "computing index" figure (SI's equivalent of an integer score) which is 36.9 times faster than Alpha Micro's original AM-100, and the "disk index" hard disk throughput test, which rates the spinning disk it came with as 15.3 times faster than their early ST-506 drives. Remember these figures as a baseline; we'll be referring to them again.
On the front panel in both pictures you can see the number "0" in the LEDs. That's where the system status is displayed, initially by the firmware, then the OS monitor during boot and then in operation. We'll come back to this as well.
Fast-forward now to September 2025, with the outer metal shell removed. Our
original Refurb Weekend
involved replacing the old AT supply with an ATX one and a converter. Since that post I found a NOS AT supply for cheap and I needed the ATX supply for something else, so I removed the converter and installed the new AT supply. This is that unit.
Next, the internals. Here we have its AM-172 68EC030 CPU board, with a copyright date of 1993, mounted to the bottom of the case in this later unit; early units mounted them vertically on a sidepanel which inconveniently blocked access to the I/O board. In the top left/northwest corner is the SCSI cable, and then the two X-BUS cables. Power is provided by a standard Molex connector stuck in the back betweeen them (remember this detail). On the right/east side is a single SIMM slot containing a 72-pin 16MB parity FPM RAM stick. The AM-172 supports up to 64MB in this slot, though the board needs to be jumpered (at JP5 and JP6) to tell the computer how much is there. There are also various testpoints plus two footprints for what look like alternate (or additional) SCSI connectors.
The three big chips are the 68EC030 processor, which is socketed and has a date code of 12th week 1997, along with an NCR 53C710 SCSI-2 controller (manufactured by Symbios Logic, 2nd week 1997) supporting 10MB/s synchronous transfers, and a Lattice Semiconductor MACH130 PLD (manufactured by AMD, 8th week 1997), basically four "PAL26V16-equivalent" blocks jammed into one die. The CPU and the 53C710 are both clocked by an 80MHz crystal divided down to 40MHz; there are also 16MHz and 50MHz oscillators on the board which appear to be used for the PLD and bus logic.
Likely for cost reasons there is no L2 cache, though another thing to keep in mind is — so I'm told — that for compatibility reasons with 68000 and 68010-era AMOS software it is not possible to enable the data cache (or at least not without substantial difficulty). In fact, we observed exactly this phenomenon when looking at the driver for
the InterLink Dimension-030 CPU upgrade
, which puts a 68030 in an AM-1000: it never set the data cache bit in the '030's CACR at all. Although some machines can accept an external L2 cache, including one we'll look at in detail, anything it would provide is strictly I-cache.
And here is the AM-319 I/O board (the Eagle 200's cut-down variant was the AM-319-10, the same general architecture with less hardware). The X-BUS cables from the CPU board plus the two AT power connectors from the main power supply are at the upper left/northwest corner. In the upper right/northeast corner are the jumpers and pinheaders going to the front panel. Interestingly there is a set of pads marked SPEAKER between the AT connectors and the front panel connectors, though AMOS doesn't officially support audio. The BR2325 clock battery is hidden under the ribbon for the front panel.
The main chips on the I/O system board are two large Altera PLDs. Although the datasheet says the SRAM storing the logic is backed by either EPROM or Flash, in these first generation Eagle boards Rod Hewitt explained to me that they get completely reprogrammed from the CPU board's boot PROMs on every powerup (adding, "That saved my butt a couple times!"). The PLDs are clocked by a 32MHz crystal in the lower right/southeast corner, and to the right/east of them is the connector for an AM-219 floppy controller, which these systems still supported.
Between the floppy controller connector and the larger PLD sits a small chip in a PLCC socket. This is the SSD (in earlier units it was a DIP; they are functionally identical). Note that all markings except for its engraved serial number have been removed, but people have decapped these, and found that they are otherwise simply specially programmed PALs. There is no known way to read out the code and/or clone it without cracking it open and there was (allegedly) a cottage industry back in the day that did exactly that. It is socketed for easy transfer to a replacement or upgraded system.
To the left/west of the main PLDs are the two unpopulated paddlecard expansion SIMM slots (the other two we'll get to in the next photo). The Eagles inherited this connector from the AM-1600, which was the original system for many of these paddle cards, and has 42 pins so that a RAM stick can't accidentally fit there. Next to the slots is a 3.6864MHz crystal which will tip off some of you as to what the paddlecard slots are normally used for.
If you didn't figure it out, here's one of the paddle cards it came with, an AM-318 8-port serial card. (3.6864MHz is one of those clock speeds that neatly subdivides into standard baud rates and is a hint that there's likely a UART of some kind nearby; see also 4.9152MHz and several other common values.) The two main chips are Philips (now NXP) SC26C94 quad UARTs, each providing four of the eight ports, using a "bidding" system to consolidate and reduce unnecessary service interrupts. AMOS has special acceleration for these QUARTs which Alpha Micro marketed as "Super I/O." Up to 57600bps is supported. The later AM-318-10 uses the refined SC28C94 or SC68C94, but is functionally equivalent in AMOS.
Each card sends off two ribbons to two additional cards installed in the rear (a total of four). These are the 8P8C "RJ-45" ports you saw and are carried on four-port AM-90 "Lightning" boards, consisting of a large array of Zener diodes with one for every active line. As the name implies, they are intended to protect the hardware from high voltage surges on connected terminals, either repelling the excess voltage entirely or limiting damage to the Lightning card itself where the diodes can easily be replaced (there are no other active electronics). In installations with sometimes distant terminals connected by repeater, lightning strikes and other such surges were a non-theoretical risk, so cards like this served as a reasonable insurance policy.
For even larger port concentrations, the AM-318 can directly drive a single RJ-21 Amphenol connector, putting all eight ports on "one" card. Inconveniently the RJ-21 connector requires a breakout cable and is physically identical to a Centronics-style 50-pin SCSI (but is
not
). I have such an example later on.
Other serial paddlecards can also be installed. The AM-314 provides only four serial ports, but is not merely a cut-down AM-318 — the AM-314 can also be configured for RS-422 (the AM-318 is strictly RS-232) and supports all RS-232 handshake lines (the AM-318 only RTS/CTS), and in certain configurations can trigger a remote reboot from a connected distant console by grounding pin 1 with pin 7. By contrast, the more exotic AM-338 provides an IBM Binary Synchronous Communication "Bisync" link, typically used for Remote Job Entry (RJE) or CICS connections with IBM mainframes, but could theoretically have also worked with some early point-to-point networks like BITNET. It connects to an AM-339 which provides the physical port.
One other possible expansion option comes when we compare those boards with the AM-137 unified board of the Eagle 100. I'm not going to say a whole lot more about the Eagle 100 in this specific article since it's essentially a cost-reduced Eagle 300 with less expansion capability, but because it was so inexpensive to manufacture it ended up outlasting several of its contemporaries. You should be able to identify most of the same landmarks on this one (the SCSI controller, now an LSI part, and the two main system PLDs with stickers on them; the CPU is hidden behind the drive cage and is not visible here) and note that there is only one paddlecard slot next to the single RAM slot. Instead, the E100's serial ports come from an AM-318-10 incorporated into the AM-137 (the QUARTs are in PLCC sockets next to the empty paddlecard slot) and fan out into eight DE-9 ("DB-9") ports mounted directly on the back of the case instead of 8P8C ("RJ-45") ports on cards. These are not regular PC "COM" ports, by the way, and need a passive converter.
The E100 was still capable of Ethernet, though for that you needed an AM-366. These paddlecards were never very common and are now extremely hard to find, and back in the day I ended paying more for the card from an Alpha Micro reseller than I did for the E100 (grrr). It uses a National Semiconductor DP8390D, an ancestor of their later DP83932 SONIC NIC, and is basically a shrunk-down NE1000 card in every other respect. The set of pinheaders at the top is in fact nothing more than a stealth AUI port; the kit came with a mounting bracket and a passive connector cable, but I just connected the cable directly to one of my many AUI transceivers and plugged twisted-pair Ethernet into that. This card is electrically compatible with the other Eagles and theoretically should provide a second interface, but I haven't gotten up the nerve yet to try it. One or both of my E100s may turn up in
a future article
.
Notice how many of these PCBs say "Made in USA"! A different era.
Anyway, back to the work at hand: swap out the E300's SCSI hard disk for a ZuluSCSI. Let's unplug the hard disk and get the bay out.
The rather dusty hard disk, and near as I can tell the original one it shipped with, is a Seagate Hawk ST31051N, a 5400rpm 1GB Fast SCSI drive with a narrow 50-pin interface. Again, because the case was all off-the-shelf PC components, the hard drive likewise sits in an off-the-shelf 5.25"-to-3.5" conversion bracket to which it's bolted, the same sort you'd use for a 3.5" floppy drive in such a bay.
The front drive LED uses standard pinheaders, which we should be able to convert. It looked like someone tried to hotglue the LED cable in position (!) but it was easily convinced to slide off.
I had an old ZuluSCSI RP2040 still on the shelf that I thought would be fast enough for this (note from the future: no, it's not). Using modern emulators like the ZuluSCSI or BlueSCSI for this purpose is helpful because the unit can do the disk copy for you and then store it as a file, making backups as simple as copying the hard disk image file to another computer for safekeeping. Backups are especially critical on systems like these where the operating system is effectively locked to the SSD, and this method of archiving the drive's contents is way easier than tape.
(I should also note for the record that although we're using mostly ZuluSCSIs in this article, I am merely a generally satisfied heavy user, and I have no affiliation or arrangement with their designer other than previously testing some pre-release units.)
Since the ZuluSCSI has no side mounting holes and I didn't have any more plastic enclosures on hand, I used the leftover struts
from my SGI Indigo^2 retrofit
to see if it could sit on them. It did, so I sheathed them in electrical tape as a "bed," put the ZuluSCSI into initiator mode, connected the old hard disk and the ZuluSCSI to my copy rig, and left it to image the drive to the SD card.
While that was going on, I made the fateful decision to try to clean up the cable rat's nest. As part of this task I rerouted some of the Molex power connectors from the PSU, including the one to the CPU board. When the copy completed I snapped off a couple pin headers from my stack in the parts box and slid them into the LED cable, then connected that to the LED activity vias on ZuluSCSI.
Ready for the power-on test before installing it permanently. It showed a zero on the front LEDs, but it
didn't change
: the boot sequence wasn't starting. I freaked out, immediately powered it off, and checked everything inside that I'd touched to find I had not properly reconnected the CPU board's power connector.
When I plugged the CPU board back in and turned the system on again, this code ("2d") showed up. I removed the ZuluSCSI and reconnected the Seagate drive. It still showed up. I removed everything from the SCSI bus. It still showed up. Okay, I said to myself in panic, I must somehow have blown the SCSI controller; maybe I can work around it. I held in the reset button while powering it on to see if I could get it into the ROM self-test. The code still showed up.
I powered it down and consulted the documentation. "If status 2d or 3d remains on the display panel, your computer has encountered an error, perhaps due to faulty memory or addressing. Perform 'Procedure #5: Self-Test [which is what I just did].' If your computer does not pass the self test, call your VAR with the information from the test. Stop." Well, that's just dandy. In the list of status codes later on, there is no explicit 2d, just an "xd" where the boot sequence "failed because of a time-out error. This code may indicate faulty memory or an addressing problem." Here the x indicates either the alternate boot device (2), in this case the tape streamer, or the primary boot device (3), in this case the hard disk. The primary and secondary devices are configured by the DIP set on the back, but I hadn't changed those, and even if they needed to be changed for the ZuluSCSI (note from the future: they do), that didn't explain why it wouldn't boot with the original hard disk either.
Given that it couldn't even enter the self-test, there was clearly more wrong than just the SCSI controller. Since it mentioned faulty memory, I did try one of the SGI Indigo²'s 72-pin SIMMs since those are FPM parity also, though I didn't think that was really the problem and as expected it didn't make a difference. It took me a couple hours to calm down because I really like this machine and I'd somehow just killed it doing what should have been a very low-risk upgrade. Sure, I had the E100s and also since acquired a more powerful later model I'll introduce you to momentarily, but this was my
original
.
I dug up Rod's old E-mail to see if there were any clues in it and recalled what he'd said about the PLDs being dynamically reprogrammed on every startup —
from the CPU board
. I also knew from the service manual that the X-BUS cables, the only connection between the I/O board and the CPU board, had to be correctly connected or the service manual warned damage could result. A horrible theory stirred in my head: perhaps I had managed to accidentally corrupt the PLDs by effectively bringing up the I/O  board
without
the CPU board, where the boot PROMs used to reprogram them are located. However, that also suggested a solution — there are many undocumented jumpers on the AM-319 and I wondered if one of them could be used to trigger a clean reset of the programmable logic.
I typed out a message to Rod and it bounced, which brings us to the memorial portion of this post: it turned out Rod Hewitt had passed away just months prior, in March 2025. Although Rod hadn't worked for Alpha Micro in some time, he still maintained a few systems as a hobby, and was the developer of the Windows ZTERM terminal package that specifically supported Alpha Micro terminal emulation (Alpha Micro even used it for their AM-80 Windows CE thin client, which might itself appear
in a future article
). He also had an interest in digital television, developing TSReader, a way to analyse the MPEG-2 transport streams commonly used for satellite, cable and IPTV transmissions.
ZTERM and in particular TSReader became far and away his most popular software packages. However, a few years prior and unbeknownst to many, he had quietly entrusted a copy of the TSReader source code to a friend officially "just in case," and sold
ZTERM to MicroSabio
, a long-time Alpha Micro support company that
maintains A-Shell
, a way of running AlphaBASIC applications on modern operating systems. The reason became clear later — he was dying, and it was not treatable. The source code for TSReader was duly posted after his passing and
remains today
as his most popular legacy. Rest in peace, Rod, and thank you.
Without Rod's guidance, though, there wasn't much more I could think of to do at that point. I unplugged it, pulled the clock battery and let it sit for a couple days to see if that was enough to reset the PLDs, assuming that was the actual problem, and it didn't. It still seemed like it should be repairable if I could only figure out how, but as there was little point in having it sit fruitlessly on the workbench I removed all the remaining cables from the system board and moved the machine to cold storage until I could come up with something else. In the meantime I turned to my alternative system to get
ampm.floodgap.com
back up and running, though to discuss it we need to bring the history forward some more.
The Eagles were well-received by the user base, though by 1996 it became clear that they couldn't serve the very large installations that were becoming curious about them, and there were just too many models to begin with anyway. The E100 was cheap enough that it sold in good numbers, but few customers fell between it and the E300, making the E200, more expensive to sell and manufacture than the E100, obviously superfluous. Likewise, high-end customers interested in the E500 were interested
only
in the E500: a junior-varsity 68040, which is what the E400 was, didn't have much appeal. Both the E200 and E400 were quietly dropped.
For large installs that required substantial numbers of serial ports, the existing AM-319 board had to be expanded. The revised AM-319-20 board, providing four built-in serial and parallel ports with a UPS monitor port and a higher-performance DP83902 Ethernet NIC, still had two paddlecard slots, but these slots were widened to 60 pins and could now be part of a bus connected to an external chassis. Alpha Micro had long sold the AM-990, a large capacity case (in this image as used for the AM-4000, though I apologise I don't have a better image of it) and the AM-990 Jumbo, which was even larger. A new higher-performance serial card was developed to take advantage of the widened paddlecard slots, an optically-isolated eight-port card called the AM-359. Twelve AM-359s could be installed in the AM-990, yielding 96 ports when connected to a fan-out in one of the AM-319-20's paddlecard slots (the four on-board ones made an even hundred); the Jumbo could take
another
twelve AM-359s for
another
96 ports connected to the second, a whopping total of 196 serial ports when combined with the base four. If you needed even more, the AM-3501 sidecar chassis could take you well beyond. There was no point in supporting the 68EC030 with such a monster: this new Eagle, officially the Eagle 550 Super Eagle, was 68040 or bust.
For users that didn't want to go
that
large, a Super Eagle in the standard case could support up to 60 ports, four on the AM-319-20 and then seven AM-359 cards in the usual position. The E550 Super Eagle additionally came as a separate upgrade kit for the E500 and the few E400s that sold, essentially a system board swap, though when sold as a turnkey system it was always with the 40/80MHz CPU. The E550 introduced a new Seiko timekeeper chip as well which not only maintained the time but also the "CMOS settings," the first Alpha Micro with an on-screen setup utility in ROM allowing boot configuration.
Subsequently the company was tardy once again in adopting Motorola's newest 68K CPU, this time the superscalar 68060, which had come out in 1994 aimed squarely at the Intel Pentium but didn't reach Alpha Micro customers until mid-1997. This took two forms, a new 66MHz '060 Roadrunner upgrade option for the E550 Super Eagle and the AM-4000 (lesser Eagles need not apply), and a new AM-6000 large system. Interestingly, the AM-6000 is strongly based on the E550, reflected in its internal designation as the AM-3500-6000 making it a "stealth" Eagle. The '060 Roadrunner not only included the new CPU but also 64K of L2 cache, support for up to 256MB of RAM in four SIMM slots, and 68-pin Fast and Wide SCSI-2 using the NCR 53C770.
In fall 1997 Alpha Micro proudly announced over a thousand Roadrunner '030 systems alone had been sold, mostly E300s, along with E100s and a smattering of E500s and Super Eagles. However, it was not lost on company management that Motorola believed the 68000 family was fast approaching a performance wall. This was made most clear by their then-enthusiastic participation in the PowerPC AIM alliance, but also the rise of ColdFire, which Motorola had first announced in 1994 as well. ColdFire was in its own way Motorola's oblique admission that 68K was losing desktop competitiveness to x86, an attempt to scale the ISA down to embedded markets where its familiarity could be an asset. Approximately 20% of the instruction set such as BCD and certain addressing modes were eliminated, meaning the canonical ColdFire could not be fully binary-compatible with any extant 68K. On the other hand, such cuts enabled the core to execute nearly every remaining instruction in a single clock cycle, and the initial die was a miniscule 4.4mm² at 0.5μm, a third the size of Motorola's own 68300-series CPU32+.
Some amount of this work was done by altering the microcode of the 68040V, a fully static 68LC040. Mindful that ColdFire's incompatibility might impair adoption, Motorola chose to create a bridge first-generation chip from this altered 68040V where omitted user mode instructions were left in, demonstrated
on die photos
. While the new chip had smaller 2K instruction and 1K data caches than the 68040V, and the MMU was also eliminated, this deviation from spec was still sufficient to run regular 68EC040 code at the user level. Motorola called this first-generation ColdFire chip the MCF5102, produced on a 0.6μm process, and introduced it in 1995 drawing 0.8W at 20MHz and reaching 33MHz. Clock-for-clock there was no way this chip could eclipse an '060, and the emerging "true" ColdFire 520x series couldn't run existing Alpha Micro software, but the MCF5102 was still faster than an '030 and
nearly
as fast as an '040 — in fact, we'll prove it. On top of that it was cheaper and AMOS didn't need the MMU anyway, making for a plausible mid-range machine that wouldn't imperil (much) sales of the E500 or E550.
In August 1998, Alpha Micro announced their first ColdFire system based on the MCF5102, and near as I can tell was the first ColdFire-based server ever produced. To visually demonstrate its break from the past, the new system got a new, more modern minitower case (also off-the-shelf) with a mix of 5.25" and 3.5" bays but kept the same Eagle badges. Intended to slot between the E300 and E500, it was thus dubbed the Eagle 450.
Although Rod Hewitt was no longer working full time for Alpha Micro by then, he still had enough of a relationship with the company that they lent him a pre-production model for evaluation, which he received with enthusiasm. He was generally complimentary in his public review to
alt.sys.alpha-micro
, though credit must be given to John F. G. Leighton, then Alpha Micro's VAR marketing manager, who chose to print the review unedited in marketing materials, even Rod's gentle complaints. Since this is the only E450 I have personally laid my hands on, we will be referring to his comments liberally as a point of comparison, and consequently the E450's history is probably the best documented of any 68K Eagle. It rolled out to users in October at the annual meeting in nearby Riverside, California.
This particular system was a gift from someone who inherited it from an 9-1-1 emergency dispatch centre and wanted to find it a good home, another way that running an Alpha Micro-powered web server has paid off. I was able to quickly get into the system (if it's not clear by now, I
love
hacking into Alpha Micros) and reconfigure it, and it had lurked as the E300's work spare and a test unit since then. Like the E300 it has a bootable tape drive, but this time it's a more modern DDS/DAT.
The E450's new case became the standard for subsequent systems (my E100s are both in this case) but still has the same basic rear layout with eight cutouts for each bank of serial ports, albeit slightly rearranged. Some aspects of the system, like the on-board UPS monitoring port, were derived from the E550 as was the same Seiko timekeeper chip, improved Ethernet NIC, and on-screen "CMOS setup" tool in ROM. On the other hand, its NCR 53C770 Fast and Wide SCSI-2 controller came from the '060 Roadrunner, and the system has but one parallel port and only twisted-pair Ethernet (no AUI). Take note of the pop-out panel just above/north of the RJ-45 Ethernet jack; I will comment on this specifically later. I don't know what the handwritten "#8218" means.
Two fans run at the top, one in the AT supply plus a case fan; just below/south of the case fan is the 68-pin external SCSI connector. There are some shenanigans with this particular unit's documentation and internals, to be demonstrated as well, and I've long wondered if this was some sort of test model (the donor did not know). In particular, the serial number of "9999" on the backplate is clearly bogus, the model number should be AM-3500-
E
450, and it claims not to have an SSD at all (untrue). As such, I'm not sure I can believe the stated manufacturing date of September 2002, and at least one date inside directly contradicts it. It's possible this was a case with a transplanted board.
The E450 is another unified board called the AM-138. Alpha Micro made upgrade kits (again, basically board swaps) for the AM-1600, E100, E300 and E500 that replaced their internal components with this one. The internal SCSI cable can be seen going from the rear port to the DDS tape drive and hard disk ...
... and then to the AM-138, covering up the 53C770 controller behind it. There are two SCSI connectors on the logic board, but not two busses, and they can't be used at the same time. The top 50-pin one is meant for when all you have are narrow devices; the bottom 68-pin one is the higher-performance wide connector, though the SCSI bus on this machine is finicky about what it will talk to. As the AM-138 no longer supports the older AM-219 floppy controller, an optional SCSI floppy disk drive was made available as a substitute.
Although you can see three paddlecard connectors which are compatible with the same AM-314 and AM-318 serial cards, the E450 embeds an SC28C94-based AM-318-10 with Super I/O into its own board similar to the E100. Each four port half goes to its own AM-90 Lightning board to total our eight serial ports. The 3.6864MHz serial clock crystal can just be seen peeping out from behind the rear board in this view.
This is the replacement timekeeper, a Seiko Epson RTC65271. You can pry the BR1225 batteries out of it and replace them far more easily than any dead Dallas timekeeper. Also visible is the SSD in its usual PLCC socket, to the southeast/lower right, and the first of several unpopulated regions on this board, the AUI connector at J3 to the northwest/upper left.
Several more glaringly unpopulated areas are apparent despite a board copyright date of June 2001 (top left/northwest corner, next to the AT power connectors), well after the E450's ostensible introduction. The major one is labeled "PCI," at J6 and J5, kitty-corner to the DP83902VF NIC at U15. That is indeed per Rod's summation where two PCI slots were supposed to go, along with their IDT CA91C860 68K host-to-PCI bridge chip on the empty pads near the centre of the image. The PCI era arrived during the 68K architecture's market decline, making PCI slots unusual in any 68K system, and the manual for the E450 says the PCI slots were "[n]ot supported in initial release" consistent with Rod's observation that the regions were taped over.
However, Alpha Micro was already advertising E450 systems with PCI slots in
1999
as prerequisites for the AM-370, an unidentified off-the-shelf 100Mbit PCI NIC that goes into the "slot" at J5. To access these PCI slots, that rear panel I pointed out needs to be removed. The AM-370's availability implies all shipping E450s should have had them by then — there was even an alleged board-swap program to do so. I've yet to find another one, so I don't know if that's true, but it would be interesting to find out because with this card or the OEM equivalent you would have two fully operational NICs and multihoming was reportedly supported. I also don't know what's going on with the unpopulated "option connector" at P5 to the right/east of the AT power connectors.
At least there are connectors for the
other
slots. The E450 is one of only a few Alpha Micro systems that can accept an optional external L2 cache, though as mentioned this cache is only enabled for instructions, and the form factor does not match any PC cache stick — in fact, it's the same as a 72-pin SIMM, so don't put the wrong one in the wrong place (Rod also objected to this). The only size supported is 64K, the same cache stick used for the AM-6000 and the '060 Roadrunner, part #PDB-00701-00. I've never seen this cache stick and comparison of his numbers with my cacheless E450 suggests it only yields around a fourteen percent boost, not nothing but not much, likely because it can't do anything for the data cache (though stand by for a very important observation on actual clock speed).
The E450 also has two 72-pin SIMM slots, which need not be paired and support up to 256MB, though as with the earlier systems the machine needs to be jumpered to tell it how much is there. The tag on the one in J11 (service order 13009, apparently) is dated January 18, 2002: that makes this machine at least eight months older than its alleged manufacturing date, and to have received an
upgrade
suggests it's even older than that. Between the two sticks this system has 72MB of RAM. Below/south of the RAM SIMMs are the three paddlecard slots.
Also in this image is another obvious non-populated area: a pin-grid array marked "PGA040" at U89 in the northeast/upper right hand corner. That sounds like somewhere the CPU would go, and the footprint looks like an '040. So where's the actual processor?
The ColdFire MCF5102 is in fact hidden behind the drive bays, the only chip with a heatsink, which should tell you it's doing an awful lot of work. How
fast
is it doing it, though? While Rod's review stated his prerelease system was apparently running at 33MHz, the oscillator closest to the CPU can be seen clearly in this photograph, and it's ... 25MHz. There are no other crystals on the board except for the serial port one you saw earlier, the official marketing announcement has a board layout that also clearly labels this crystal as 25MHz, and nothing in the MCF5102 user's manual says the chip does anything tricky with the clock. As it happens, the
only
place in Alpha Micro documentation where the E450's CPU speed is given is Rod's review: everywhere else, even the data sheet, simply says it's a ColdFire and nothing more. Since mine is only 14% slower than his, and his had the cache, his can't possibly have been running at 33MHz either. The E450 is a 25MHz ColdFire, full stop.
In a backwards way, however, this is nothing less than validation of how performant early ColdFires could be. Recall that our E300, a 40MHz 68EC030, had a "CX" computing index score on the
SI.LIT
benchmark of 36.9. The same benchmark on this E450 with a 25MHz MCF5102 gets a score of
59.9
, and Rod's with 64K L2 came in at a whopping 68 (Alpha Micro said 68.5; either one is around 14% higher). By contrast, the E550 Super Eagle, with a full 40MHz ("80MHz") 68040 Roadrunner clocked 60% faster
and
32K of L2 cache, officially gets ... 79.9 (note from the future: my figure is 83.6) — the full cached-up faster-clocked 68040's performance on the same code is only around 33-40% better, and just 16-22% or so if the E450 has its cache too. Put another way, the CX/MHz ratio of the faster 68040 was right around 2.0, while the CX/MHz ratio of the MCF5102 is
2.4
without the cache, and almost 2.75
with
it.
Likely because the lower clock speed would have looked bad in marketing materials, similar to why General Magic never mentioned the clock speed
of the DataRover 840
, Alpha Micro simply chose not to mention it either. Still, this machine's surprising efficiency proves ColdFire, at least early on, definitely had legs. I'm not sure how Rod got it wrong except that an earlier version may indeed have run that part, though with these numbers, if there had ever been a production 33MHz E450 it might have seriously endangered sales of Alpha Micro's remaining '040s — perhaps that's why they didn't use it even though the faster part existed. Best guess is that the AM-138 was originally designed for the 68040 and then quickly retrofitted for ColdFire, leaving the PGA region as an "R&D test point" (as documented).
Here's the front panel connection.
And here it is booting up (the activity lights are hidden LEDs). I copied over the backup of the website, reconfigured its AlphaTCP webserver, which is more recent than the E300's, and pointed the reverse proxy to it instead. With the faster CPU, better Ethernet, more memory and bugfixed TCP stack it performed rather well.
Still, I wanted to fix the original system, and since I wasn't exactly sure what I'd ruined, I figured the simplest thing to do was find another unit and either swap out the boards or move the hard disk, RAM, SSD and serial ports into the new one. However, these systems never turned up much on eBay or similar places even when they weren't nearly as old, and other than a few intermittent AM-1000s in varying states of disrepair I didn't see any other Alpha Micros, let alone an Eagle 300, come through at all.
I eventually contacted Alpha Micro directly through their current website to see what they might have still in stock, or if they had a VAR to recommend for parts. By this point Alpha Microsystems and its remaining IP had been sold to a private consortium and reconstituted as Alpha Microsystems LLC, with the original California business entity ceasing to exist, and it was this new Alpha Micro that I conversed with. I got to spend a couple pleasant hours doing a phone interview with one of AM LLC's principals, which I used to update the website and reported on in
our prior entry
, and he referred me to a longtime Alpha Micro vendor that they still partner with for existing installations. It took a few months, but this vendor was able to locate what appeared to be another E300 with working boards and we negotiated a price and getting it shipped.
Here's how it arrived. A bit more yellowed and dirty, and no tape streamer, but I figured I could just transplant the boards into the old case and use what was there.
The back was a little more interesting. This unit is serial #01300, earlier than my original E300, and its older backplate here doesn't indicate when it was manufactured, though a small sticker at the bottom suggests April 1996. The standard complement of I/O board ports is present, but the topmost eight ports are DE-9 ("DB-9") and the bottom two slots look like Centronics-style SCSI connectors. These connectors are actually RJ-21s that use a breakout cable; the true external SCSI port has a terminator installed for just-in-case. This system must have supported a lot of simultaneous serial ports previously.
Like the E100's, these DE-9 ports are not PC "COM" ports; they need conversion. In one of the ports was a cockeyed AM DE-9 to RJ-45 dongle which makes it basically the same as the RJ-45 serial ports in our other systems. I powered it on and tried using it as the console port, but didn't get anything. Eventually I discovered where it was with my
"everything console"
connected to the top left port (G1) via the dongle at the typical speed of 19200bps.
.
.
.
.systat
Status of AMOS Version 2.3A(489) on Friday, May 15, 2026 06:35:37 PM

JOB1   TRM1    System Service     DSK0:1,4       RN  SYSTAT      1615372  bytes
LOGJOB LOGTRM  System Service     DSK0:1,2       SL  LOGGER           30K bytes
TASK   MANAGR  System Service     DSK0:1,2       SL  TSKIDL         1250K bytes
TASK01 TASK01                     Not logged in  ^C  MEMORY          750K bytes
MALSER MALSER  System Service     DSK0:1,2       SL  MALSER          100K bytes
NETSER NETSER  System Service     DSK0:7,50      MS  NETSER          200K bytes
VTSER  VTSER   System Service     DSK0:1,4       MS  VTSER            75K bytes
NETLOG NETLOG  System Service     DSK0:1,2       MS  NETLOG           40K bytes
TCPEMU TCPEMU  System Service     DSK15:7,50     SI  TCPEMU         3500K bytes
FTPD   FTPD    System Service     DSK15:7,50     SI  FTPD             50K bytes
TELNED TELNED  System Service     DSK15:7,50     SI  TELNED          100K bytes
TELNEE TELNEE  System Service     DSK15:7,50     SI  TELNED          100K bytes
HTTPD  HTTPD   System Service     DSK15:7,50     SI  HTTPD           100K bytes
TAMED  TAMED   System Service     DSK15:7,50     SI  TAMED           200K bytes
50 jobs allocated on system, 14 jobs in use (13 logged in)
Total memory on system is 32M bytes
System uptime is 00:01:42

DSK0    15281 Blocks free       DSK1     2230 Blocks free       
DSK2    46314 Blocks free       DSK3    64972 Blocks free       
DSK4    64972 Blocks free       DSK5    64972 Blocks free       
DSK6    64972 Blocks free       DSK7    64972 Blocks free       
DSK8    64972 Blocks free       DSK9    64657 Blocks free       
DSK10    22105 Blocks free      DSK11    64972 Blocks free      
DSK12    64972 Blocks free      DSK13    64972 Blocks free      
DSK14    64972 Blocks free      DSK15    61819 Blocks free      
DSK16    64972 Blocks free      DSK17    64972 Blocks free      
DSK18    64972 Blocks free      DSK19    64972 Blocks free      
DSK20    64972 Blocks free      DSK21    64972 Blocks free      
DSK22    64972 Blocks free      DSK23    64972 Blocks free      
DSK24    64972 Blocks free      DSK25    64972 Blocks free      
DSK26    64972 Blocks free      DSK27    64972 Blocks free      
DSK28    64972 Blocks free      DSK29    64972 Blocks free      
DSK30    64972 Blocks free      DSK31    64972 Blocks free      
DSK32    64972 Blocks free      DSK33    64972 Blocks free      
DSK34    64972 Blocks free      DSK35    64972 Blocks free      
DSK36    64972 Blocks free      DSK37    64972 Blocks free      
DSK38    64972 Blocks free      DSK39    64972 Blocks free      
DSK40    64972 Blocks free      DSK41    64972 Blocks free      
DSK42    64972 Blocks free      DSK43    64972 Blocks free      
DSK44    64972 Blocks free      DSK45    64972 Blocks free      
DSK46    64972 Blocks free      DSK47    64972 Blocks free      
DSK48    64972 Blocks free      DSK49    14650 Blocks free      
DSK50    30157 Blocks free      DSK51     2835 Blocks free      
DSK52    64972 Blocks free      DSK53    64972 Blocks free      
DSK54    64972 Blocks free      DSK55    64972 Blocks free      
DSK56    64972 Blocks free      DSK57    64972 Blocks free      
DSK58    64972 Blocks free      DSK59    64972 Blocks free      
DSK60    33406 Blocks free      DSK61    40123 Blocks free      
DSK62    53393 Blocks free      DSK63    64972 Blocks free      
DSK64    64972 Blocks free      DSK65    64972 Blocks free      
DSK66    64972 Blocks free      DSK67    30787 Blocks free      

71 devices on system, total of 3991217 blocks free
.log opr:
Transferred from SYS: to OPR:
Caution - other jobs same PPN
Good, it booted fine, we got a dot prompt, we can get into it, networking is already configured, and (as is typical for most Alpha Micro installations of the era) there is no password on the operator account. I powered it off and now that we know where the system thinks the console is, we'll get a proper self-test readout. I powered it back on with the reset button held in and the self-test came right up. The self-test can autosense the baud rate by mashing the spacebar when the front LED flashes "5b," and then the test runs, with the LED showing the current state and additional details sent to the serial port.
----------------
SYSTEM SELF-TEST
----------------
Version 2.1(120)
Prom Rev. N00 for the AM-174 board.
polling complete.

Boot configuration:
 Processor - 68040
 Memory detected - 32M bytes
 Primary serial ports - 4
 SCSI Controller

press [space] to bypass memory test

MEMORY TEST passed - 32M bytes

TIMER TEST passed

SERIAL PORT TEST
 Primary serial ports - 4
  Port # 0 passed
  Port # 1 passed
  Port # 2 passed
  Port # 3 passed

SCSI Controller
 Controller Self-test passed
 SCSI drive Self-test passed
 Find diagnostic cylinder passed
 Write/read test passed
Wait — a 680
40
?! This is
not
a Eagle 300! We need to open this thing up.
Because of all those serial ports I expected a lot more cabling coming off the AM-319 system board, and indeed there was. But what I
didn't
expect was the CPU board on the bottom: it's a full 68040, just like the test said.
This is the faster of the two AM-174 CPU boards, the '040 boards for the original two-piece Eagles I mentioned earlier. Although Alpha Micro eagerly billed this AM-174-02 as having an "80MHz" 68040, that sort of marketing is deliberately simplistic. Recall that 68040s take two clock signals, one labeled
Bclk
for the bus clock, and then a second exactly twice as fast labeled
Pclk
as the so-called processor clock. In the 68020 and 68030, which accept a single clock signal, their internal ALU runs at only half the bus speed such that the 40MHz 68EC030 in the Eagle 300 actually has an ALU running at just 20MHz. For the 68040 Motorola removed this limitation to run its ALU at full bus speed, but the chip designers also studied trace data to optimize for the most common instructions, implementing a 7-stage pipeline where most effective address calculations and fetches occur with no penalty. The upshot of this was to cut most instructions' cycle count in half or more.
The 2x processor clock is truly used, but
not
to speed up the ALU, so it's wrong to say the 68040 is "double-clocked." In a two-part 1990 article in
IEEE Micro
, Motorola explains that "Pclk provides timing reference points within each Bclk period," employing it for synchronous sub-cycle timing, and furthermore explicitly states that "all internal operations cycle at the Bclk rate." Still, the fact this clock signal was present at all gave Apple an excuse to tout
both
timings for '040 Macintoshes, and Alpha Micro cheerfully reported just the faster one, even though the chip only
appears
to run at that comparative speed from its larger 4K L1 cache, unhindered ALU and reduced cycles per instruction.
On this board,
Pclk
is provided by the same 80MHz crystal we saw on the AM-172, divided down by two to yield
Bclk
in the same way the 68EC030 board does for its single 40MHz clock. (For the E400's AM-174-00, this crystal would have been 66MHz divided down to 33MHz.) The single parity FPM SIMM slot and 16MHz and 50MHz oscillators are also present, as well as the same 53C710 SCSI controller, here a genuine NCR part. However, new for this board is 32K of L2 cache at the upper right/northeast corner, implemented with two IDT 71B74 8K cache-tag RAMs together providing 29 bits (512MB) of address comparison, and then four Cypress CY78C185 8K SRAMs for the cache itself. Remember, however, that in AMOS all cache is I-cache.
Effectively this 40/80MHz AM-174 makes our new system a full Eagle
500
, so why is it labeled as "only" an E300? I don't how how these systems originally shipped from the factory nor whether the E500 designation actually appeared on the back, but Alpha Micro did run a promotion in late 1997 where you could upgrade any Roadrunner '030 to a Roadrunner '040 by swapping the CPU board. My guess is this is one of those systems, and because that upgrade kit wouldn't have changed the plate on the back itself, the reseller simply noted it to be a working E300 and sold it to me as such. While that wasn't
exactly
what I was hoping for, it's a really nice bonus, as evidenced by the system benchmark (taken on the SCSI hard disk it shipped with):
.si dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(115)-1

               Computer Type: Eagle
              Main Processor: 68040
                Co-Processor: 68882
                 MMU present: Yes
            Operating System: AMOS 2.3A(489)
          Boot PROM revision: Unknown
              Number of SSDs: 1
                Total Memory: 32768 K-bytes
     Resident Monitor Memory: 25245 K-bytes

     Computing Index (CX), relative to AM-100:    83.6
     48 bit FP Index (4X), relative to AM-100:    34.1
Floating Point Index (FX), relative to AM-100/L:  1700.0
          Disk Index (DX), relative to ST-506:    23.4
That score officially makes it the new fastest Alpha Micro in the shop
by far
(this is where that prior 83.6 number came from, compared to the E450's 59.9 and E300's 36.9). It seemed a shame to carve it up as spare parts, so let's have a little look around.
.log sys: 
Transferred from OPR: to SYS:
Caution - other jobs same PPN

.type amos32.ini
:T
;
JOBS 50
;
JOBALC JOB1,LOGJOB,TASK,TASK01
JOBALC MALSER,NETSER,VTSER,NETLOG,TCPEMU
;
LOAD LOAD.LIT
LOAD DEL.LIT
LOAD SYSMSG.USA
LOAD TRMDEF.LIT
LOAD DEVTBL.LIT
LOAD BITMAP.LIT
LOAD SYSTEM.LIT
LOAD MOUNT.LIT
;
TRMDEF TRM1,AM314=0:19200,FWYCOL,200,200,200,EDITOR=15
;TRMDEF MODEM,AM314=2:57600,AM65A,200,200,200,EDITOR=15
;TRMDEF OKI320,AM314=3:9600,PSEUDO,200,200,100
;
TRMDEF LOGTRM,PSEUDO,NULL,100,100,100
TRMDEF MANAGR,PSEUDO,NULL,100,100,100
TRMDEF TASK01,PSEUDO,AM62A,1000,1000,100
;
TRMDEF MALSER,PSEUDO,NULL,100,100,100
TRMDEF NETLOG,PSEUDO,NULL,100,100,100
TRMDEF NETSER,PSEUDO,NULL,100,100,100
TRMDEF VTSER ,PSEUDO,NULL,100,100,100
TRMDEF TCPEMU,PSEUDO,NULL,100,100,100
;
; --- Terminal Drivers ----
TRMDEF AM62A,PSEUDO,AM62A,10,10,10
TRMDEF FLP62A,PSEUDO,FLP62A,10,10,10
TRMDEF FWYCOL,PSEUDO,FWYCOL,10,10,10
TRMDEF FLWCOL,PSEUDO,FLWCOL,10,10,10
;
[...]
;
; TCP STUFF
SYSTEM DVR:AM319.LDV/N
SYSTEM RPC.SYS/N
SYSTEM TCP:IPCINI/N 500 500K
SYSTEM RTI
SYSTEM TCP:FTPD
SYSTEM TCP:FTPD.RTI
SYSTEM TCP:HTTPD
SYSTEM TCP:HTTPD.RTI
SYSTEM TCP:LPD
SYSTEM TCP:LPD.RTI
SYSTEM TCP:LPR
SYSTEM TCP:LPR.RTI
SYSTEM TCP:SMTPD
SYSTEM TCP:SMTPD.RTI
;SYSTEM TCP:SNTPD
;SYSTEM TCP:SNTPD.RTI
SYSTEM TCP:QPOP3D
SYSTEM TCP:QPOP3D.RTI
SYSTEM TCP:TAMED
SYSTEM TCP:TAMED.RTI
SYSTEM TCP:WEBCNT
SYSTEM
[...]
MEMORY 0
.
A surprising thing about the system configuration file (
SYS:AMOS32.INI
, a/k/a
AMOS32.INI[1,4]
) is that only
one
terminal is actually defined, which makes you wonder what those two RJ-21s are doing. Best guess is that this machine passed through a couple hands and ended its prior service as a single user's toy, much as my own machines are now. In a related phenomenon an annoyingly small number of terminal types are defined, all inconvenient, likely to save memory. On the other hand, the full AlphaTCP suite (based on SpiderTCP and SpiderStreams, best known as the Windows NT TCP/IP stack before 3.5) is defined and present, and we saw it running before, so we ought to be able to make use of that.
.log tcp:
Transferred from SYS: to TCP:
Caution - other jobs same PPN

*****************************************************************************

TCP: Account

*****************************************************************************
.dir /w
DSK15:[7,50]
VUENL  CMD 1    ATCP   GIF 6    NSLOOK HLP 4    BBSERV LIT 66   
BOOTPC LIT 103  BOOTPD LIT 99   FTPD   LIT 178  FTPLOG LIT 31   
HTTPD  LIT 151  IMGMAP LIT 40   IPCINI LIT 2    IPFW   LIT 93   
ITCD   LIT 105  LPD    LIT 109  LPR    LIT 127  NETLOG LIT 52   
POPPWD LIT 93   POP3D  LIT 113  QPOP3D LIT 114  RWHOD  LIT 94   
SLIPD  LIT 106  SMTPD  LIT 207  SNTPD  LIT 115  TAMED  LIT 166  
TCPEMU LIT 380  TDDD   LIT 123  TELNED LIT 110  TFTPD  LIT 127  
TNWRAP LIT 1    VDOM   LIT 4    WEBCNT LIT 5    BBSERV NEW 12   
BOOTPD NEW 1    CONFIG NEW 4    FTPUSR NEW 1    GOTCP  NEW 1    
HOSTS  NEW 1    HTTPD  NEW 6    IPFW   NEW 3    ITCD   NEW 1    
LPR    NEW 1    MYNAME NEW 1    NETWRK NEW 1    POPUSR NEW 1    
RESOLV NEW 1    SERVIC NEW 2    SNTPD  NEW 2    TCPEMU NEW 1    
TDDD   NEW 1    WHOIS  NEW 1    SERVIC OLD 4    BBSERV RTI 1    
BOOTPC RTI 3    BOOTPD RTI 6    FTPD   RTI 19   HTTPD  RTI 4    
IPFW   RTI 6    ITCD   RTI 3    LPD    RTI 3    LPR    RTI 4    
NETLOG RTI 1    POPPWD RTI 6    POP3D  RTI 3    QPOP3D RTI 3    
RWHOD  RTI 3    SLIPD  RTI 2    SMTPD  RTI 7    SNTPD  RTI 6    
TAMED  RTI 6    TCPEMU RTI 13   TDDD   RTI 6    TELNED RTI 2    
TFTPD  RTI 4    SERVIC AGT 4    NETLOG LST 3    VUENL  LST 3    
NETLOG OLD 3    SERVIC     4    TIMZON BAK 1    QKSB20 TMP 1    
TCPEMU     1    TIMZON AGT 1    CONFIG BAK 4    HOSTS      1    
LPR        1    HRPB20 TMP 1    GOTCP  CMD 1    CONFIG AGT 4    
FTPLOG LOG 1    FTPUSR     1    TCPEMU AGT 1    NETWRK AGT 1    
START  CMD 1    MYNAME AGT 1    RESOLV AGT 1    LPR    AGT 1    
HOSTS  AGT 1    FTPUSR AGT 1    RESOLV     1    SMTP   BAK 1    
SMTP   DFT 1    HCOB20 TMP 1    SMTPD  LOC 1    CONFIG     4    
MYNAME BAK 1    SMTPD  FWD 1    MYNAME     1    JNPB20 TMP 1    
AMPB20 TMP 1    HOSTS  BAK 1    3RPB20 TMP 1    RESOLV BAK 1    
P0PB20 TMP 1    SMTPD  BAK 1    SMTPD  ALI 1    7CJB20 TMP 1    
0BJB20 TMP 1    NETWRK     1    TIMZON     1    NETWRK BAK 1    
Total of 120 files in 3150 blocks

.type netwrk.
#ident "@(#)networks    1.4     9/4/90"
#
#   NETWORKS
#
# Contains information on networks comprising the DARPA Internet.
#
#   The fields are:
#
# official network name    network number    alias  [ alias ]  [ alias ]...
# 
#   for example:
#
#        ethernet             89.0.0.0       ether     eth        net
#
ethernet        192.168.0.133   ether eth net
#ethernet       192.168.1.133   ether eth net
#slip           192.168.2.1     serial
loop            127.0.0.1       local
That's its IP address, and we saw Telnet was running (
TCP:TELNED.LIT
), but there's a snag:
.type config.
#  attach the ethernet to the internet package (using AlphaNET NDVs):
#  EXAMPLE: ifconfig <interface> <AlphaNet Network #> arpa <receive buffers>
#ifconfig ec0 101 arpa 100
#  attach the ethernet to the internet package (using standalone LDVs):
#  EXAMPLE: ifconfig <interface> <driver>
ifconfig ec0 am319
#  attach the slip interface to a slip daemon:
#  EXAMPLE: ifconfig <interface> <terminal> <dialup script>
#ifconfig asy0 modem1 dialup.slp
#ifconfig asy1 modem2
#ifconfig asy2 modem3
#ifconfig asy3 modem4
#  change the tcp close timeout to fit the environment
#  EXAMPLE: closetime <seconds>
#closetime 120
#  change the tcp keepalive timeout to fit the environment
#  EXAMPLE: keepalive <minutes>
#keepalive 15
#  disable all packets unless ipfw (or tcpmon) is running
#mustfirewall
#  start up the daemons (servers)
#  EXAMPLE: start <daemon> <memory> <options...>
#  (these assume ftpd, tftpd, smtpd, pop3d, lpr, lpd, and httpd are 
#  in system memory)
#
#start rwhod 75k
start ftpd 50k -n -o -T
start httpd 100k -mHTM:
#start telned 100k "-lLOGON" 1965 400K flwcol "Local Access"
start telned 100k "-lLOGON" 0 400K fwycol "Local Access"
start telned 100k "-lLOG SYSTEM SERVICE" 7666 400K FWYCOL "Remote Access"
[...]
The
TCP:CONFIG.
file sets up
TCPEMU
, AlphaTCP's master daemon, acting as its service description file (really a sort of up-script). This line for the Telnet daemon causes an automatic log-on from a Telnet session and inconveniently forces the
FWYCOL
terminal type, intended for a real Wyse WY-370. That's also the terminal setting for the single serial port which our "everything console" doesn't speak, meaning I can't visually edit anything without making a big mess. Ironically, that AM-75 colour head my E300 uses is itself a modified WY-370, but no longer speaks that terminal emulation either.
But we have another option! Now knowing its IP address, I set up a small wired network to my MacBook Air. Although some terminal programs like Kermit 95 can speak WY-370 over Telnet, using
MacWise
— now
freeware
and runs on Tiger and Power Macs all the way to Tahoe on Apple silicon — I managed to discover that its TeleVideo 925 emulation will
partially
match
FWYCOL
. This was just enough to, with some care, edit
TCP:CONFIG.
and remove all the defaults so that I could manually select the terminal type on Telnet login. I then reset the FTP user credentials in
TCP:FTPUSR.
, uploaded a copy of
ANSI.TDV
from the Eagle 450, and changed the
TDVDEF
line in a test copy of
SYS:AMOS32.INI
to allow it as a terminal type, which at last got me a proper session.
I'm not sure of this system's most recent owner and the seller didn't know either, but there were two interesting domains in its
TCP:HOSTS.
file (identical to
/etc/hosts
) for that IP address. One domain name belongs to someone who appears to have been a recording engineer (!). This domain still exists, but is only partially functional, so I've chosen not to link it here. The other domain name was for a personal genealogy site, now parked, and that site appeared to be what it was currently offering via the Web server on
HTM:
, mapped to PPN [7,77]. However, because the HTML files were not on an extended directory device, I can't tell when the site was created because the old AM file system doesn't preserve modification times:
.log htm:
Transferred from TCP: to HTM:

.type home.htm
<html>
<head>
<META NAME="description" CONTENT="Home page.">
<META NAME="keywords" CONTENT="home,page">
[...]
</table>
<hr>
</body>
</html> 
.dir /full
PUBLIC PPN   1    <00505051717>  000-000-000-000  --------- --:-- --------- --:-- --------- --:--                      47211  DSK0:[7,77]
HOME   HTM   1    <00505051717>  044-112-056-204  --------- --:-- --------- --:-- --------- --:--                      47212
Looking up this domain in the Wayback Machine, it seems to have been active in the early 2000s. Still, not bad assuming it was still serving it then.
I dragged the ailing hulk of the E300, now sans hard disk, back out of climate-controlled storage. By this time it had sat with no power and no clock battery for over eight months.
The plan was to transplant the AM-319 and AM-174-02 as a matched pair from the "secret" E500 into the nicer case of the E300. This was first because I wasn't sure which (if either) board I'd busted, and second to avoid disconnecting and possibly incorrectly reconnecting the X-BUS: besides the fact that a misconnected X-BUS can wreck the system, the X-BUS is connected
differently
on the AM-172 and AM-174s, so it seemed safer just to never separate them in the first place. I wasn't even going to move the SSD and hard disk — since TCP/IP networking was already set up on the E500, I could just upload the site to the E500's hard disk instead. Only the E300's power supply, serial port cards and Tandberg QIC streamer would stay. Once the new transplanted system was working, then I'd see about doing the ZuluSCSI upgrade again.
Before committing to surgery, and leaving its hard disk still out, I reconnected the E300's system board to give it one more chance to start. Checking all my connections thoroughly, I then plugged it into the power strip and turned it on, expecting to see the dreaded 2d code again.
It tried to boot.
Startled, I powered it off, connected the everything console, and turned it back on with the reset button held in to force a self-test. Except for the missing hard disk,
it passed the self-test
— even the SCSI controller tested good.
I decided to push my luck and connect the ZuluSCSI, and this time it
did
throw a 2d. I freaked out again, powered it off, let it sit and then gingerly turned it back on. It still did it. However, when I disconnected the ZuluSCSI, it went back to trying to boot, and a repeated self-test was still clean.
This was clearly new behaviour — beforehand, it wouldn't do anything, not even enter the self-test, let alone attempt booting. Recall that error 2d had
two
mentions in the manual, the second one referencing the primary and secondary boot devices. Since the self-test said the SCSI controller was fine, this made me suspicious that there was something about the ZuluSCSI's configuration the machine didn't like. Knowing some systems can get finicky about sluggish devices immediately after power-up, I reconnected the ZuluSCSI and powered the E300 back on. Code 2d duly appeared, but this time instead of turning it off, I hit the reset button just to see what it would do.
It booted. I checked out the system and the files and jobs I knew should be there, and everything seemed to be operating normally, just as it used to. Here you can see all three panel LEDs lit (power, CPU activity and disk activity) along with the LED for the drive bay. Resetting it again, it booted cleanly a second time. I could find no other defects; it seemed fully functional.
I was delighted it had somehow revived itself in hibernation, but I'm not willing to do much digging into its Lazarus act. The only thing I can think of is that the prolonged de-energised period either completely reset the PLDs, as I hoped would happen, or glitched them enough to force a reload anyway. That's obviously not a theory I'd like to test. In support of said theory, however, although I got the same abnormal front panel code each time, the root cause on each occasion seemed different. Beforehand, it was something about the connection between the system board and the CPU board. Now it appeared to be the SCSI bus.
The other problem is that the boot didn't seem appreciably faster. In fact, the hard disk score from
SI.LIT
had actually dropped to around 10, which was 33%
slower
than its original hard disk.
This particular unit was an old ZuluSCSI, so the next thing to try was a newer one. The ZuluSCSI Blaster supports synchronous transfers up to 18MB/s, and since the 53C710 on the AM-172 and AM-174s supports synchronous SCSI as well, I bought a couple to test. I also copied the disk image to a new, fast SD card to eliminate that as a factor. Here's how the bus looks now (the AM-401 external CD-ROM is turned off):
.scsi
Dispatched SCSI port:

SCSI id  7: (reserved)  SCSI bus host adaptor
SCSI id  6: No device or unable to report
SCSI id  5: No device or unable to report
SCSI id  4: No device or unable to report
SCSI id  3: SCSI-2 (tape)      TANDBERG TDC 4200       =08:01CREATED12119
SCSI id  2: No device or unable to report
SCSI id  1: No device or unable to report
SCSI id  0: SCSI-2 (disk)      ZULUSCSIHARDDRIVE       2.3BZuluSCSI
And the score?
.si dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(114)

               Computer Type: Eagle
              Main Processor: 68030
                Co-Processor: None
                 MMU present: Yes
            Operating System: AMOS 2.3A(484)
          Boot PROM revision: M00
              Number of SSDs: 1
                Total Memory: 16384 K-bytes
     Resident Monitor Memory: 6218 K-bytes

     Computing Index (CX), relative to AM-100:    36.8
     48 bit FP Index (4X), relative to AM-100:    36.3
Floating Point Index (FX), relative to AM-100/L:  5.6
          Disk Index (DX), relative to ST-506:    41.2
Almost three times faster — not bad! But the next run got a little spicy.
.si dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(114)

               Computer Type: Eagle
              Main Processor: 68030
                Co-Processor: None
                 MMU present: Yes
            Operating System: AMOS 2.3A(484)
          Boot PROM revision: M00
              Number of SSDs: 1
                Total Memory: 16384 K-bytes
     Resident Monitor Memory: 6218 K-bytes

     Computing Index (CX), relative to AM-100:    36.9
     48 bit FP Index (4X), relative to AM-100:    36.3
Floating Point Index (FX), relative to AM-100/L:  5.6
          Disk Index (DX), relative to ST-506:    100.4
I wasn't sure how to rationalise why the second run was nearly two and a half times faster (and over
six times
faster than the original hard disk). There's no obvious caching in the Blaster's firmware that I could see, and although the AMOS system-wide disk cache was on, the test is supposed to be unaffected by OS-level caching. On the other hand, when I rebooted AMOS from software, its score went back to 41 and 100 thereafter. More on this phenomenon later.
Termination power was sufficient to power the Blaster. But what the Blaster didn't fix, even with its later firmware, was the 2d code the E300 kept throwing from a cold start. Although booting after a manual reset was still fine,  it refused to start after a power cycle without assistance, which I need it to be able to do if there's a power outage when I'm not around.
The ZuluSCSI has lots of options settable in its
.ini
file, but since the issue appeared to be what the E300 thought was the secondary device and I knew the streamer was connected and working, I had a look at the back boot DIP switches first. The previous setting was #1 and #3 on, which would attempt a boot from the (non-existent) floppy drive first, and then try the SCSI hard disk. This had always worked before, but we have no floppy drive and I'm not likely to find an AM-219 anytime soon, so I tried the other boot position where it attempts a boot from the
streamer
first — again, known good electronics — by switching #4 on. And that worked: now it boots reliably. The conversion is complete.
So, with the E300 resurrected and finally successfully converted to solid state, let's
really
push our luck here ... by doing the same with the others! (I should note I excluded the E100s this time around; I haven't found a special task or physical location for them yet.)
A ZuluSCSI Blaster is a fast SCSI emulator, but it wouldn't be enough to fully challenge the E450's 20MB/s Fast and Wide SCSI-2 controller and Seagate Cheetah ST39204W (a 9GB 10Krpm Ultra160), which collectively notch a baseline
SI.LIT
disk score of 30.9. For this system I bought a ZuluSCSI Wide, which tops out at 34 MB/s read and 15 MB/s write, and which I already use in my
Apple Network Servers
with a similar NCR 53C825A.
Copying the disk image over onto a new fast SD card and firing it up. It also was fine with termination power alone.
.scsi
Dispatched SCSI port:

SCSI id 15: No device or unable to report
SCSI id 14: No device or unable to report
SCSI id 13: No device or unable to report
SCSI id 12: No device or unable to report
SCSI id 11: No device or unable to report
SCSI id 10: No device or unable to report
SCSI id  9: No device or unable to report
SCSI id  8: No device or unable to report
SCSI id  7: (reserved)  SCSI bus host adaptor
SCSI id  6: No device or unable to report
SCSI id  5: No device or unable to report
SCSI id  4: No device or unable to report
SCSI id  3: No device or unable to report
SCSI id  2: SCSI-2 (tape)      HP      C1533A          A907   9
SCSI id  1: No device or unable to report
SCSI id  0: SCSI-2 (disk)      ZULUSCSIHARDDRIVE       2.3WZuluSCSI
Here you can see both the HP C1533A DAT and then the ZuluSCSI Wide.
.si dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(114)

               Computer Type: Eagle
              Main Processor: 68040
                Co-Processor: None
                 MMU present: Yes
            Operating System: AMOS 2.3A(484)-15
          Boot PROM revision: D00
              Number of SSDs: 1
                Total Memory: 73728 K-bytes
     Resident Monitor Memory: 4366 K-bytes

     Computing Index (CX), relative to AM-100:    59.9
     48 bit FP Index (4X), relative to AM-100:    58.2
Floating Point Index (FX), relative to AM-100/L:  7.9
          Disk Index (DX), relative to ST-506:    51.0
.si dsk0:
[...]
          Disk Index (DX), relative to ST-506:    52.2
.
First do note that the CPU is detected as an '040, no doubt because of the MCF5102's heritage as a modified 68040V, and again the erroneous determination that it has an MMU (it does not). Our disk index increases to somewhere around 51, though I don't see the same potentially spurious bump the second time around as we did on the E300, and we're replacing a drive here that was already fairly quick. Still, that pencils out around a 66% increase in performance, so I'll take it.
Now we have this leftover older ZuluSCSI. Surely there's a system we can use it in.
In
the last Alpha Micro article
we booted our AM-1200 desktop system using a BlueSCSI attached to its external 50-pin Centronics-style SASI port, which with some tweaks to the settings file can be made compatible enough for its very old bus. But I'd like to use that device for other things, so we'll put the old ZuluSCSI card — more than fast enough for this thing — inside. To avoid me having to dismantle it every time I want to switch the disk image, I disconnected one of its unused serial ports and threaded a USB cable there.
We'll have to get creative about the insides, though, because the old ST-506 mounting holes won't work for the ZuluSCSI and I don't want to short it out against the brushed metal interior. After copying the disk images and reconstructing the settings, I settled on sticking it in an antistatic bag with holes for power, USB and SASI (there's insufficient termination power to run it off that alone). Hey, you can't see it from the outside. Don't judge me.
With the USB cable, I can now switch disk images and reconfigure the ZuluSCSI from a connected computer, yet not have to take the system apart again unless I need to swap the card. For now I decided to run AMOS 1.4 as its primary operating system with 2.3A as a sidecar on
SUB0:
. It's as fast as the BlueSCSI was, probably because both devices can easily saturate its slow SASI bus:
.scsi
SASI port:

SCSI id 3: No device or unable to report
SCSI id 2: No device or unable to report
SCSI id 1: (disk)      ZULUSCSIHARDDRIVE       2.0 ZuluSCSI
SCSI id 0: (disk)      ZULUSCSIHARDDRIVE       2.0 ZuluSCSI
.log sub0:[1,4]
Transferred from <SYS:> DSK0:[1,4] to SUB0:[1,4]
.si dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(114)

               Computer Type: AM-1000 or AM-1200
              Main Processor: 68000
                Co-Processor: None
                 MMU present: No
            Operating System: AMOS/L 1.4A(189)-2
          Boot PROM revision: Unknown
              Number of SSDs: 1
                Total Memory: 1024 K-bytes
     Resident Monitor Memory: 89 K-bytes

     Computing Index (CX), relative to AM-100:    6.3
     48 bit FP Index (4X), relative to AM-100:    6.3
Floating Point Index (FX), relative to AM-100/L: Not computed. Needs AMOS 2.0
          Disk Index (DX), relative to ST-506:    3.2
.si dsk0:
[...]
          Disk Index (DX), relative to ST-506:    3.2
AMOS 1.4 misdetects its 68010 as a 68000 (AMOS 2.3A detects the CPU correctly), but like the E450, there was no second test bump either.
Now with my three main systems converted to solid state, I decided to stack them and save a bit of space, using the AM-1200 as a crossbar to support the AM-65 and AM-75 terminal heads and the E300 and E450 as its "legs." The E450 and AM-1200 share the AM-65; the E300, as the always-on server, gets the AM-75 all to itself. I suppose I'll find out sooner or later how seismically stable this is.
That left our new arrival, the E500. I converted it to a ZuluSCSI Blaster as well because I was interested to see if the second-run speed bump would occur there also, given it has the same SCSI controller and the same general architecture as the E300. Annoyingly, when I extracted the Seagate Barracuda ST32272N hard disk from the 5.25" bay, one of the posts of the 3.5"-to-5.25" converter was broken and the LED cable hadn't been connected, though it won't fit the Blaster's LED header anyway.
The first order of business was thus to solder some female Dupont jumpers onto the end of the activity LED wires so we could connect it.
Now to mount it. I didn't have any more metal struts from the SGI Indigo^2, and I didn't have any screws that fit the plastic enclosure that would mate with the side rails, so I went with zipties. I said don't judge.
Installed, as good as we can get, with the old LED connector for comparison.
Since the zipties are only in the front, the board will swing down, but this is actually useful because I can easily access the configuration switches when the SCSI cable is unplugged. Like the E300, termination power is enough to run the ZuluSCSI in the E500, so there's no power cable to get in the way.
When the SCSI cable is reattached, its connection to the tape streamer keeps it in raised position.
The rear DIP switches were already correctly set, so the last step was to put its outer metal shell back on (a bit banged up though I managed to bend out a few of the defects) and give it a good scrub. I might consider Retr0brighting it later but simply cleaning it up made it look quite a bit better.
Booting with the
"everything console."
I should point out that the E500 has a slightly later version of AMOS than the E300 and E450 and we get a little more explanation with the bus readout:
.scsi
Dispatched SCSI port:

SCSI id  7: (reserved)  SCSI bus host adaptor
SCSI id  6: SCSI-2 (tape)      TANDBERG TDC 4100       0801=:CREATED12119
            CmdQue Asynchronous
SCSI id  5: No device or unable to report
SCSI id  4: No device or unable to report
SCSI id  3: No device or unable to report
SCSI id  2: No device or unable to report
SCSI id  1: No device or unable to report
SCSI id  0: SCSI-2 (disk)      ZULUSCSIHARDDRIVE       2.3BZuluSCSI
            CmdQue Synchronous: 10.00MB\8
While all three systems support synchronous SCSI, this version of AMOS actually reports it, along with the width (8-bit, because it's only Fast SCSI, not Wide). Now, what about performance?
.si dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(115)-1

               Computer Type: Eagle
              Main Processor: 68040
                Co-Processor: 68882
                 MMU present: Yes
            Operating System: AMOS 2.3A(489)
          Boot PROM revision: Unknown
              Number of SSDs: 1
                Total Memory: 32768 K-bytes
     Resident Monitor Memory: 25249 K-bytes

     Computing Index (CX), relative to AM-100:    83.8
     48 bit FP Index (4X), relative to AM-100:    34.1
Floating Point Index (FX), relative to AM-100/L:  1700.0
          Disk Index (DX), relative to ST-506:    46.3
.si dsk0:
[...]
          Disk Index (DX), relative to ST-506:    180.7
.
The ST32272N we replaced is a 7200rpm drive while the ST310151N in the E300 was only 5400rpm, thus accounting for the E500's better baseline disk score, and the E500's faster CPU probably explains its slightly higher first-run result of 46.3. But the second run is even more lopsided than what we saw with the E300, a massive 180.7.
Since two of the systems were doing it, it was time to dig in a little more. The ZuluSCSI Blaster has a debug mode switch which echoes status and current operation to a connected machine over USB serial at 115200bps, so I hooked up both the E500's serial console and the USB port of the Blaster simultaneously to the MacBook Air to watch what SCSI operations occurred during the benchmark test.
Debug mode obviously substantially impacts SCSI throughput because now the processor in the ZuluSCSI has to emit serial debugging information while it's satisfying requests, but SCSI activity during the first run didn't seem unusual. On the other hand, the activity during the second run was
very
unusual: there wasn't any. In fact, even though the baseline score had sunk down to a dismal 10 or so because of all the debugging data it was emitting, the second run was still a blistering 180.7.
This really sounded like operating system caching, but except for the AM-1200 where I wasn't running it to save memory, the other three systems were running the standard disk cache as virtually any performance Alpha Micro would — and allegedly
SI.LIT
should be unswayed by it. For some reason the E450's cache configuration wasn't locking UFDs (user file directories, i.e., PPNs), but turning that off on the E500 and E300 didn't make a difference, and all three were caching everything else including the MFD (master file directory). However, when I turned off caching altogether at runtime (using the
CACHE.LIT
tool and disabling with
OFF
), though the scores got really low, they were now consistent from run to run.
Do note our observation isn't enough to fully explain the E450, which also runs the OS disk cache, but didn't have a second run bump. If you disable the cache on the E450, although its overall score declines, it still remains consistent from run to run. One possibility is that the driver for its later SCSI controller just isn't as aggressive.
Although the overall issue certainly calls into question how useful
SI.LIT
is as a disk benchmark, despite being likely the only Alpha Micro benchmark tool you can expect most recent systems to come with, the question then becomes
how
comparative disk performance on an Alpha Micro should be measured. Was it still fine for me to continue with my usual practice of leaving the cache on and testing immediately after boot? It's probable that there'd be little in the cache by that point, whatever would be there would likely be similar from system to system (assuming the same version of the operating system), and likelier still that whatever
was
present in the cache wouldn't be very germane to
SI.LIT
. Under my current knowledge of AMOS I think these numbers are still broadly comparable; I just have to keep in mind that the score on subsequent runs is likely to be bogus.
With our Alpha Micro stack now in operation, shown here from the E300's console as it continues serving the world as it did before, let's briefly finish the story of the Eagles. The E100 and E450 became the basis for a number of even smaller systems used as network servers (e.g., the E100NX with few, if any, directly attached terminals) fed by network-connected terminal servers (e.g., E100TX, E450TX) based on the same platform. The single board systems were much cheaper to manufacture, and Alpha Micro discontinued the E300, E500 and E550 in 2000 to introduce the MCF5102-based E250, a cost-reduced E450 in the same way the E100 was a cost-reduced E300, running exactly the same processor at the same speed (Alpha Micro themselves reported a CX score of 59.9, precisely even with our E450 here). The E100 was discontinued shortly afterwards in 2001.
For Alpha Micro, the end of their 68K architecture systems was ultimately tied to the end of the 68K architecture generally. Motorola had never planned to evolve the MCF5102 further as it was always meant as a stopgap, and later ColdFires were not sufficiently suitable nor compatible to run the software legacy AMOS users ran. Although Alpha Micro's Falcon line of PC compatibility cards used them as a CPU starting with the 2002 PCI SuperFalcon (AM-113), it soon became clear PCs were fast enough for software emulation to be a far more effective option. In 2003 Alpha Micro introduced the AM-8000, an AMD Athlon PC running Windows XP Embedded with an on-board SuperFalcon, but here the SuperFalcon was demoted to a coprocessor for handling the SSD and terminal I/O running a reduced "Embedded AMOS" monitor. Everything else was an efficient software emulation, yielding a
SI.LIT
CX score of 816 (!) on dual Athlon 2800+ CPUs. Later AM-113 SuperFalcons were just serial ports and a socket for the SSD; the main system was now more than suitable to service them, and Motorola wasn't making any more 5102 CPUs either. The Eagle 800 that same year ran the same technology in miniature, bringing the great experiment to a close with the discontinuation of the last E250 and E450 systems, and today's systems sold by the reformulated Alpha Microsystems LLC use the same x86-based architecture.
Over their production lifetime, analysis of known serial numbers suggests around ten thousand 68K Eagles were ultimately sold, and now I've got five of them. Rest in peace, Rod. They're still great machines.
