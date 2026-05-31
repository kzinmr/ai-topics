---
title: "Ahoy, DECmate II! the little PDP-8 that could"
url: "https://oldvcr.blogspot.com/2026/05/ahoy-decmate-ii-little-pdp-8-that-could.html"
fetched_at: 2026-05-31T07:01:06.355651+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Ahoy, DECmate II! the little PDP-8 that could

Source: https://oldvcr.blogspot.com/2026/05/ahoy-decmate-ii-little-pdp-8-that-could.html

In 1982, as we mentioned at length with our history of
the DEC Professional
, Digital Equipment Corporation attempted to keep their PDP-11 minicomputer market-relevant by turning the venerable architecture into a largely incompatible desktop microcomputer. But that wasn't the only PDP-series mini it happened to, and it wasn't even the first: the PDP-8 actually got the shrink-ray treatment several years before, and not content to merely make it into a smaller general purpose computer, DEC turned it into a word processor.
Thus emerged the DECmates, descended from the 1977 DECstation VT78; arguably the zenith of the line was this one, the DECmate II, which rolled off the assembly line in 1982 simultaneously with the first DEC Professional models and the DEC Rainbow. Advertised aggressively to offices new to computers, take the two floppy disk drives built-in, add a printer, monitor and keyboard, and right away you had a simple office system for basic needs. With a Z80 or an 8086 processor card, you could turn it into an overgrown CP/M machine or a rather limited MS-DOS one. You could stick two more floppy drives in it. You could even add a hard disk or a graphics card, as long as you didn't consider what more powerful system you could have gotten instead for that money.
Now, that's a lot of word processing. But under the hood it's still at least PDP-8
adjacent
, even considering its oddities and incompatibilities, and you can make it do many of the things a full-size Eight can. We'll take this basic unit, convert the floppy drives to solid state, tap the video output, and put it through its paces. After all, if we have
a PDP-11 on our desk
, we should really have a PDP-8 too.
Naturally the story starts with the PDP-8 itself, officially the seventh member of Digital's Programmed Data Processor family (the PDP-2 was never built). The PDP-8 is a 12-bit system that traces its lineage back to the 1961 LINC ("Laboratory INstrument Computer") developed initially at MIT's Lincoln Laboratory and manufactured by Digital and others. Also a 12-bit design, the 2048-word LINC was a capable and even beloved machine due to its flexibility and ease of interfacing, and it is generally considered the first effective "minicomputer" — not necessarily in size, mind you, but rather as a simpler architecture and reduced instruction set as opposed to larger systems. It was nevertheless fully comparable with them, and DEC systems architect Gordon Bell and designer Alan Kotok (later co-founder of the W3C) developed a simplified specification based upon it aimed at smaller market applications where the 18-bit PDP-1 and PDP-4 would have been unattractively priced. This became the 1963 PDP-5, its logic principally designed by engineer Edson de Castro (later the founder of
Data General
). It started at $27,000 [in 2026 dollars about $282,000], a surprisingly low cost for the era, and about a thousand were sold.
Castro expanded the PDP-5 further, mindful to retain the easy interfacing that made it popular, but at the same time making it faster and cheaper through parsimonious design and various architectural and microcode improvements. He was also able to make it smaller: built out of diode-transistor logic on closely packed flip-chip modules, it was now merely the size of a small refrigerator. DEC introduced it as the PDP-8 minicomputer in March 1965, as shown here in its original form at the Computer History Museum, for an even lower price at "just" $18,500 [$190,000]. It provided 4096 words of magnetic core memory and ran at a cycle time of 1.5us, yielding an effective clock speed of 667kHz. These initial models were later nicknamed the "Straight-8" and became the best selling computer model to that time, with nearly 1,500 rolling out to customers.
The PDP-8 went through a rapid stepwise process of evolution, making it even cheaper and more capable, in addition to the side-branch LINC-8 and PDP-12 which specifically supported LINC instructions for those customers. These improvements arguably culminated in the 1970 PDP-8/E, a versatile system supporting up to 32kW of RAM that a year and a half and a price cut later became the first computer to sell for under $5,000 [$4,995, or in 2026 dollars around $52,000]. Although ostensibly a consolidated re-design of the TTL-based 1968 PDP-8/I, its stronger I/O capabilities using the new OMNIBUS and a wide variety of peripheral and system options nevertheless enabled it to scale from small installations up to very large ones, in a variety of settings (this particular unit assisted monitoring during neurosurgery at Massachusetts General Hospital). DEC offered several operating system choices as well, ranging from the simple PS/8 executive and its descendant operating system OS/8 to the multiuser TSS/8 supporting up to 16 users.
By the mid-1970s, however, the PDP-8 was finally showing its age. The 1974 $1835 PDP-8/A had reduced it to a single board and expanded total memory even more, supporting both classic core memory and new semiconductor RAM, but although it found use as a lower-end option for office tasks (such as the 1975 DEC Datasystem 310) and basic CNC automation, compared to newer systems its architectural idiosyncrasies were increasingly seen as a liability. Exceeding the fundamental 4kW addressing limit required grafted-on registers, only addresses in the current 128-word page or the zeroth one could be accessed without indirection, the small basic instruction set made excessive use of "magic" locations and sometimes needed cumbersome code sequences for simple tasks (e.g., logical-OR), and its subroutine call storing the return address in the subroutine's first word inhibited efficient recursion — or running from ROMs. While Digital intended to keep selling Eights as long as there were buyers, at the time the corporation saw little profit in evolving the platform further.
In the meantime, few (if any) patents and copyrights had persisted on the PDP-8 instruction set or its major design features, to some degree because the LINC from which it was descended was government-funded and in the public domain, and combined with its simplicity and enduring popularity it became an attractive target for clones. A couple even appeared during the architecture's commercial lifetime — somewhat to Digital's annoyance — such as the Digital Computer Controls DCC-112, introduced in 1970 as a faster clone of the PDP-8/I. Even as DEC tried to wind down the line, its residual presence nevertheless remained sizeable, and other clones like the 1974 Fabri-Tek MP12 emerged to service the market. Despite Fabri-Tek billing the core unit as a "microprocessor," the main CPU module was still all discrete TTL.
But the first commercial microprocessor implementation of the PDP-8 didn't come from DEC either — in fact, for a period of time DEC under co-founder Ken Olsen actively repulsed internal attempts to do so. As we talked about before with
the DEC Professional
, the emergence of the microcomputer became an existential crisis to minicomputer makers, including DEC but also HP, Data General, TI, IBM and others, and many attempted to compete by shrinking down their current offerings (such as TI turning the 990 into the TMS9900, DG with the ill-starred microNOVA, and the HP 2100 as the Binary Processor Chip). An DEC skunkworks project did the same to develop what was intended as the PDP-8/B in 1973, but management was sceptical of the investment required and it was cancelled. Shortly afterwards, in 1974, developers squeezed a reduced PDP-8/A logic board into a VT50 terminal and demonstrated it as one of two potential personal computer products to Olsen. To their disappointment (including a young David Ahl), he vetoed them also on the advice of management concerned it would cut into existing product lines, making the infamous observation that no one would want a computer in their home. (Olsen would repeatedly attempt to clarify this statement, even doubling down on it in 1977, citing the size and inconvenience of then-contemporary computer systems.)
The installed base of PDP-8s was still significant, however, and upstart semiconductor company Intersil saw an opportunity of their own. Intersil was founded in Cupertino by Swiss physicist Jean Hoerni in 1967, one of transistor co-designer William Shockley's "traitorous eight" who left Shockley Semiconductor to form Fairchild in 1957. At Fairchild Hoerni patented the planar process of semiconductor production in 1959, still an elemental concept even today in modern photolithography, then going on to found Amelco, later Teledyne, in 1961 and consult for the new Union Carbide Electronics in 1964 before establishing Intersil. Intersil became an early pioneer in low-power CMOS through their work in watch timekeeper chips, where power saving was critical, and were able to fabricate full CMOS designs years before many competitors.
Intersil's 1975 development of a pure CMOS PDP-8 CPU was completed independently of DEC, intending not only to create a microprocessor of their own but also one with a presumably guaranteed market: the well-known instruction set would enable it to run much existing software, but could run up to 4MHz (from an 8MHz crystal), and its fully static CMOS design and uncomplicated power requirements would position it for embedded applications as well as categorical computer hardware. Among its features included moving the Extended Arithmetic Element (EAE) option on-chip for multiplication and division, which included the component MQ (multiplier/quotient) register usable as an accumulator adjunct. Intersil sampled and sold the IM6100 openly, seeing its first use in Pacific Cyber/Metrix's long-lived PCM-12 computer line (another PDP-8 clone), but nevertheless offered it to DEC as well in the fall of 1976. Harris Semiconductor came on as a second source (we last saw Harris as part of the Navy TAC-4 deployment that brought forth the
SAIC Galaxy
) and produced it as the HM-6100.
DEC management was reportedly surprised to learn of the IM6100's existence but found its implementation (based on the PDP-8/E) sufficient, and Olsen permitted what DEC called the "CMOS-8" to ship in the 1977 DECstation VT78, a trial low-end machine for small office settings where the PDP-8/A was still sold. Derived in part from the DEC 310W (a reduced office-oriented version of the DEC Datasystem 310 with a specialized terminal) and not unlike the prior prototype Olsen had summarily scuttled, Gordon Bell noted the "goals for this terminal were to drastically reduce costs": chip count was kept as low as practicable, it ran at only 2.2MHz, its low-binned and unexpandable 16kW of RAM yielded weaker benchmarks than every single previous PDP-8 system except the notoriously slow PDP-8/S, and the keyboard and CRT were integrated with the logic board into a single chassis derived from the VT52. A small exterior pedestal housed a dual RX01 8" floppy drive for storage on which the computer could sit; later units shipped with upgraded RX02 drives. Colour-coded keys such as a distinctive GOLD key used for system commands and functions were added to help non-technical users.
DEC offered two distinct families of the VT78. One version, the $7,995 [$43,000] standard model, ran OS/78 on floppy, an updated version of the original OS/8. Unfortunately, hardware-level compatibility was not a design goal — in fairness it wasn't advertised as such — and some PDP-8 software simply wouldn't work. Ports allowed the connection of printers, tape readers and additional serial links. The second version, the WS78 or Word Station 78, was oriented as an entry-level dedicated word processing unit. It shipped with a high-quality printer and a port of WPS-8, DEC's new PDP-8 word processing package, for $13,990 [$76,000]; optional ROMs to support it as a network client with a PDP-11 WPS-11M server were additionally available. (DEC made other Word Station variations based on the PDP-8/A as well up to the 2-user DEC Word System 202, all of which were also compatible with WPS-8. For that matter, DEC sold a PDP-8/A DECstation
88
too.)
Although the VT78 was not a major commercial priority for DEC, nor were they considered market leaders, they nevertheless sold well enough for Digital management to consider a successor. Intersil offered the IM6100 in two additional variants, the faster but more power-hungry 6100A and the slower though more power-efficient 6100C, but DEC regarded the IM6100 as a dead end because the chip lacked memory management hardware and required much discrete logic to support the VT78's 16kW of RAM. DEC contracted instead with Harris to develop a more flexible single-chip solution, though because Harris only had second source rights to Intersil's design, Harris ended up creating a completely new gate-array version incorporating DEC's requested enhancements yet even more small but significant behavioural differences. As before, these additional differences were of little consequence to DEC which never envisioned the DECmates as full PDP-8 successors, yet such incompatibilities were to become notorious nonetheless. This new CPU was the HD-6120.
In July 1981 DEC trialed the HD-6120 for their next microcomputer PDP-8 product, christened the original DECmate, or VT278. In the same way that the VT78 was an IM6100 system crammed in a VT52, the DECmate VT278 was an HD-6120 system crammed in a VT100. The early HD-6120 ran at 5MHz from a 10MHz crystal and among its other enhancements supported up to 32kW of main memory and another 32kW range as "control panel" memory, intended as the system's supervisor and activated by periodic interrupts or special "panel request" instructions. The DECmate VT278 had 32kW of main memory and 4kW of control panel RAM, part of which served as the display buffer, with the remainder of the control panel address space given to ROMs and memory mapped I/O. The control panel range was used for device emulation in software and to drive the main terminal display, but the CPU wasn't quite up to the task of simultaneously running user programs and servicing system devices, yielding sometimes janky screen updates.
For storage the DECmate VT278 was offered with its own RX02 dual disk drive pedestal, on which it perched somewhat perilously, and later up to four optional RL02 hard disks using an RL278 controller. If you installed a DP278A or DP278B dual serial port option, you got an overgrown, quirky and expensive VT100-compatible terminal that operated entirely from ROM, the only DECmate where this was possible. The VT278 supported WPS-8, COS-310 (DEC's Commercial Operating System, effectively a runtime for DIBOL programs), a modified version of P?S/8, and OS/78 and later the "enhanced" OS/278, which were hopped-up versions of OS/8 with the older command interface disabled. We'll look at this near the end. The VT278 started at $6,795 [$23,700].
Barely a month after, the emergence of the IBM PC 5150 in August and its rapid sales sent a shockwave through the industry, causing Olsen to abruptly reconsider his negative opinion of the personal computer segment. Quickly promising a new low-end machine based on the PDP-8, in November Olsen also told investors to expect a "DEC personal computer" (his words), insisting "we are not planning to go after the home computer market" but that the planned system would be "equivalent" to the IBM PC. In early 1982 he further elucidated that there would indeed be an updated DECmate, plus two new lower-cost "16-bit" systems. This highest tier was the
DEC Professional
, originally dubbed the DEC XT 100 (not to be confused with the IBM PC/XT), and based on DEC's chip version of the PDP-11. As the DEC XT was to become DEC's personal computer flagship, the corporation's new Small Systems Group (SSG) made its industrial design the template for the entire rollout. Despite wildly different internals, each planned system would use similar or identical cases, the same monitors, the same floppy drives, the same 103-key keyboard and mostly the same cables.
DEC unveiled the line in May 1982: two DEC Professional models (the DEC Pro 325 and DEC Pro 350), the DOS and CP/M-compatible DEC Rainbow 100 aimed directly at the IBM PC, carrying software-switchable Z80 and Intel 8088 CPUs, and bringing up the rear as promised, a new DECmate — the DECmate II. No longer an all-in-one, the DECmate II finally looked the part of an 1980's office computer with a separated keyboard, monitor and main unit, but despite the more premium appearance was intended as a cheaper alternative to the DECmate while running much of the same software. Moreover, DEC uncharacteristically priced the DECmate II to sell, launching it at "only" $3740 [$13,000] with bundled monochrome VR201 monitor, specialized LK201 keyboard and built-in RX50 5.25" dual floppy disk drive.
As with the VT78 and DECmate VT278, DEC continued to heavily market the DECmate II for small business applications and ran ads in non-computer industry journals, such as this one targeted at law offices. Although DEC rapidly ran into early supply problems with the Pros and the Rainbow, and Pro-specific software in particular was non-existent for months, the DECmate II internally was only a modest upgrade over the original DECmate and ran largely the same packages, enabling it to be produced and usefully ship in numbers when the other DEC desktops could not.
This is my only DECmate II, the basic model with just an internal RX50 dual floppy drive in the standard BA25 case, and one of the few remnants I still have of a large DEC haul from Pasadena in 2013. We had no idea how in over our heads we were until we arrived and most of it we couldn't rescue, but my high-end
DEC Professional 380
systems came from that day and so did this DECmate, along with several keyboards and monitors for each. If you compare the DECmate II with a Rainbow or a Pro, you will note that their profile, form factor, colour scheme and general appearance are deliberately almost identical. All of them use some basic variation of this case, though the Pros are a couple inches longer.
Front power switch and badge. The pop-out panel to the right is an option bay. All DECmate IIs can support a second RX50 dual drive in this bay, or you can install an RX78 controller card for dual 8" RX01 or RX02 drives, or an MFM controller card for an internal hard disk option, though this sometimes required an upgraded power supply.
The RX50 5.25" dual disk drive is going to be a major part of this entry, and we'll be talking about it in detail because it has a rather unusual form factor. Its two drive slots are stacked and share a common motor, and while each drive has its own head and counter-rotating spindle, the carriage and stepper moving those heads is also common to both drives. These heads are both in the centre of the drive, so RX50 disks are single-sided and have their write surfaces face the central head carriage — meaning data is written on the
back
of the floppy — and thus disks inserted into the lower drive must be inserted
upside down
.
To aid the user, the drive was given two red stripes, one for each disk slot, and matching arrows placed on DEC-issue RX50 media. The stripes are offset so that the drive stripe matches the arrow on each side of the floppy when properly inserted, reminding you which side should be on top.
RX50 sectors are 8-bit (we'll get to the exact disk format later), but because the DECmates are 12-bit, the controller can also perform disk access directly in 12-bit mode for faster operation. However, changing the bit width does not change the disk's storage density, and 12-bit mode is stored effectively as 16-bit with four bits wasted, cutting capacity in half.
Little is seen on the back of the unit as there were no official openings for option cards, though some users ran cabling out the back for larger or hotter hard disks.
The rear badge gives the official model designation of this DECmate II as PC278-A, making it a relatively early unit; revisions to PC278-A3 are documented. The serial number of WF38116
indicates
it was manufactured in Westfield, MA.
Other than the power socket, there are only three ports on the back and a small aperture above them. Like the DEC Pro, there are two serial ports, though only the large DB-25 is officially labeled as RS-232. DEC's DF01 acoustic coupler modem and DF02 and DF03 direct-connect modems attached to this port, though pretty much any serial connection to any RS-232 device will do. However, the DE-9 ("DB-9") port is also a serial port, just used for a printer, and unlike the DEC Pro or later DECmates both ports can run up to 9600bps. A BCC05 cable will enable this port to be used as a serial port as well, no null modem required.
With the standard VR201 monitor, which we'll get to shortly and even disassemble later, the DA-15 video port is used to connect and power the monitor, which in turn connects and powers the keyboard. The monitor connects with a BCC02 cable, but this is just a straight-thru female-to-female DA-15, the same port used for classic Mac monitors and old-school PC joysticks. Because this cable carries 12 volts, I once again make the stern warning to never connect the monitor with the system power on, or a short could fry your keyboard. The display is strictly text, effectively an integrated DEC terminal of its own; although there was a graphics board option that can display 768x240 bitmap graphics, even in colour with a VR241 head, these boards aren't often encountered and not much supported them.
The small aperture marked TEST is for testing the Auxiliary Processor Unit. I don't have an APU in this system, but the APU was an expansion card containing a Z80 and its own 64K of RAM allowing the DECmate II to run CP/M 2.2. In this configuration the 6120 is demoted to I/O and handles the disks and display, much as the Commodore 128's main 8502 CPU did while the Z80 ran CP/M Plus. WPS-8 is aware of this card and requires it as a coprocessor board for footnotes and spellcheck. Later DEC made available the much rarer Extension Processor Unit, or XPU, which contains a Z80
and
an 8086, and either 256K or 512K of RAM though the Z80 is still limited to 64K. The XPU can boot not only CP/M (not CP/M-86) but also MS-DOS 2.11. This makes it similar to a Rainbow, and it will run some Rainbow software, though like the Rainbow there are many compatibility issues with it due to the non-standard disk format and the differing I/O. That said, it was also rather faster in practice than even some '286 systems because the 6120 could take the load off the 8086. Both cards are much more useful with a hard disk.
Speaking of the VR201 monitor, here it is. It's cute. Even though it's monochrome it came in colours like the iMac, but the colour variations are the display phosphor: the VR201-A, the one here, has a white phosphor, the VR201-B has a green phosphor and the VR201-C an amber phosphor. The VR201 works with Pros (using the same BCC02 cable) and the Rainbow as well, and later DEC terminals like the VT240.
The controls and connectors are all on the back of the monitor: the other end of the DA-15 for power, keyboard and video; and then the keyboard connector (a 4P4C "RJ11"), plus wheels for brightness and contrast. This is the monitor we will initially use, a page-white VR201-A. It was manufactured December 27, 1983 in Hong Kong (both from the serial number #HK39094 and the label).
The cuteness factor is enhanced by the swing-out carrying handle, which unlike Spindlerplastic has held up very well and you can totally carry the monitor with it. There are also mounting points for the stand, which I don't have, and a spring-loaded height adjust which is not too useful without the stand either.
But what I
do
have, on both monitors, are "cataracts." Although this flash picture is intended to emphasize them, this is legitimately what they look like; my original VR201-B that I got from the DEC haul is in worse shape, but the VR201-A I picked up later has some too. The phenomenon is due to degeneration of the glue sealing the CRT to the front monitor glass, and while all CRT monitors constructed in that fashion are theoretically subject to it, DEC displays seem afflicted to an unusual degree probably because of the specific adhesive used. The cataracts are merely ugly and being external to the CRT don't actually affect its operation, but cleaning up the damage
is not trivial
and necessarily requires working near the high-voltage tube.
The green VR201-B is also a bit flaky, probably due to bad solder joins, and in worse physical shape. Still, we'll have a use for it, and we'll come back to that later. For now we'll plug in the VR201-A.
And into the VR201-A we will plug our keyboard. I don't have the official DECmate II keyboard, designated LK201-A-1, but any compatible one like a generic LK201 or (this one) the LK401 will work. These keyboards likewise work with the Pros and Rainbow.
The primary difference is that the official keyboard had a customizeable legend with specifically marked keys such as Set-Up and GOLD, and overlaid on the numeric keypad were additional word processing function keys. However, all of these keys can be generated on this LK401; they're just not marked as such.
This keyboard was manufactured in Mexico, though the HJ serial number doesn't appear in the DEC factory codes list (DEC's Mexican office was in Mexico City).
That's it for the peripherals. Let's have a look inside the computer itself.
Pulling the two clasps on the underside allows the top to simply lift off. Like the Pro and Rainbow, the DECmate II is an exceptionally sturdy unit, some of the best built systems of that era. The internal chassis is metal, not plastic, and this one is nearly pristine except for some scuffs I later found under the floppy drive. Plastic guide rails position the RX50 and whatever you choose to put in the option bay. The 220W H7842A power supply surrounds them, also sheathed in metal. The spare Molex power connector will power many MFM hard disks, though some required an upgraded supply.
Again like the DEC Professional, the DECmate II's logic board lives in a tray on the underside secured by thumbscrews. However, the DECmate's "thumbscrews" are more like thumb
wheels
, and I don't think this one had been opened before, so they were in rather tight. I had to get out a flat-head screwdriver to turn them which is hard to do without damaging the plastic.
After that, we unplug the power supply cable ...
... and pull the tray out.
Like our
old Alpha Micros
the EPROMs on this board had lost their window stickers, so I quickly put a couple new ones on and cleaned off some of the dust.
Here is the entire logic board, with the rear ports oriented at the top/north side of this photograph, and the power supply and floppy connectors at the top right/northeast corner. Again similar to the Pro, option boards stretch over the top of the logic board. They connect to the brown connectors at the bottom/south end and are stabilized on the black posts sticking up.
The main brains of the machine are in these seven large DIPs. The CPU itself is the bottommost one, labeled D1-6120-9 with a date code of 52nd week 1982. The HD-6120 implements all of the features of the original IM6100. In addition, it puts the extended memory registers from the PDP-8/E on-die for 32kW of standard address space, supports the second "control panel" ("CP") 32kW range we saw in the original DECmate, provides vectored interrupts, and expands the instruction set with two stack pointers which greatly facilitate subroutine calls in particular, adding them as pseudo-IO instructions. The original HD-6120 in the first DECmate was limited to 5.1MHz; this later revision can run at 8MHz and faster.
The other chips, from top (north) to bottom (south), are an NEC D7201C multiprotocol dual serial chip, two Harris D3-6402-9 UARTs (second sources of the Intersil IM6402) from 29th week 1982, and three Harris D1-6121-9 I/O controllers ("IOC" but sometimes seen as "PIE," for Programmed Interface Elements) from 44th week 1982. These chips permit full control of up to five 12-bit I/O ports (thus five devices each), providing the CPU with programmable address decoding, priority-vectored interrupt control, and I/O port handshaking. The HD-6120, when it receives an IOT family instruction, sequences it to one of the 6121s which in turn communicates with the CPU through three control lines specifying data direction, accumulator handling and whether the next instruction should be skipped. A device might include the keyboard input or output (separate devices), or the serial port input or output (also separate devices), the real time clock, and so on. The IOCs/PIEs in the DECmate line were the source of even more incompatibilities themselves which we'll come back to when we talk about OS/278 near the end. The original DECmate has only two instead of three but is subject to the same behaviour.
The main ROMs for the machine are the three socketed 2716 EPROMs. Together these three chips would provide six kilobytes, or in this case 4096 12-bit words. One EPROM holds the low eight bits for the first 2kW half, the second holds the low eight bits for the second 2kW half, and the third holds the upper four bits for each half.
How these ROMs actually bring up the system is an abject lesson in the PDP-8's architectural irregularities. When the machine is first turned on, the ROMs completely occupy the processor's 4kW address space. Recall that it is difficult to call subroutines in read-only memory because the subroutine jump instruction expects to store its return address as the callee's first word, and the DECmate II's internal code is more complex than the DECmate's (more presently), so for expediency the DECmate II startup code copies itself to control panel (CP) RAM. The 6120's extended memory registers are set up so that ROM is accessed directly and CP RAM is accessed indirectly. The ROM repeatedly tests the lowest address of CP RAM until it is available, and upon success uses an unrolled loop to copy a twenty-word stage-one loader into the lowest 128 words (page) of CP RAM. This earliest code relies entirely on hard-coded addresses because at this point there is no directly-accessible RAM
at all
for indirection or counting. The execution register then directs a jump into the copied loader in RAM, which twiddles the extended registers to copy the remaining 4kW (field) of ROM minus one page into the highest CP RAM field and jumps to that, after which the EPROMs are banked out completely and never accessed again until reset. Among other critical low-level tasks, the ROM contains code for setting up the 6121s, testing the system and memory, displaying basic status messages on-screen, handling interrupts, and reading sectors from the disk drive. However, it is also not the entirety of the machine's supervisor-level code. We'll get to that a little later.
The main RAM for the system is here, twelve (ten visible) Hitachi 21-18470-02 chips. These appear to be identical to Hitachi 4864 DRAMs, which is itself the Hitachi version of the 64Kbit 4164 DRAM, so twelve 64Kbit chips equals our 64 12-bit kW of RAM, 32kW for main memory and 32kW for the control panel. Also present is a Western Digital FD1793A, the floppy drive controller for the factory-standard RX50, which works two jobs (not unlike my current employment) handling each drive head. The FDC is supervised by the Intel 8751 ("C8751-8 (B-1)") below it, an Intel 8051-family microcontroller with 4K of EPROM and 128 bytes of RAM.
Three crystals are visible here. The 16MHz crystal is divided down to 8MHz by both the C8751-8 here and the HD-6120, though this is divided again to 4MHz while the HD-6120 is performing I/O operations. The 15.741MHz clock under (south) of it is for the 80-column display, and the 22.856MHz clock to the left (west) is for the 132-column display.
The display hardware sequenced by those oscillators is on the other side of the board. The centre of the built-in video hardware, such as it is, is the Standard Microsystems Corporation CRT9007 Video Processor and Controller ("VPAC"). In this view the VPAC is the ceramic DIP left (west) of the system EPROMs. DEC refers to it as the CRTC in its own documentation.
To a first approximation, the VPAC implements many of the functions of a standard VT100 terminal on a single chip, and the data sheet even bills it as "VT100 Compatible." In theory it can generate up to a 240x256 character display with up to 32 scanlines per character row, emitting a fully synchronised display directly to an attached monitor, though most monitors probably couldn't tolerate such a signal. The VPAC is fully autonomous, reminiscent of chips like the Motorola 6847 VDG, and does its own fetches from memory to obtain character data and draw the display. In the DECmate II, the VPAC is used to generate either an 80x24 or 132x24 character display, selected based on the clock signal fed to it. Two 4kW fields in CP RAM are used as screen memory; on each screen row the VPAC briefly halts the CPU and retrieves the next row's data via DMA ("data break" in DEC parlance). The VPAC also handles drawing the cursor. In the original DECmate some of the CP range was used for memory mapped I/O for its own display, but here all 32kW of the CP range contains RAM, so the VPAC's registers are instead manipulated through the processor's IOT instructions.
In most applications the VPAC is often paired with one or two row buffers to reduce memory contention — here two SMC CRT9006-135 single row buffers — and an SMC CRT8002 Video Display Attributes Controller ("VDAC") for character generation and decoration. The DECmate II instead performs the analogous role with an arguably cheaper combination of discrete logic and software (again to be explained when we actually boot something on the machine). Glyphs for the base character set are stored in the 2764 EPROM shown here, including graphics and line-drawing characters, with user-defined characters loadable by panel request into the TMM2016 (2K) RAM below/south of it and banked in and out as necessary. Video memory is laid out as a set of rows with a table indexing 16-bit row addresses (spread over adjacent words). The two upper bits of the row address are used to encode row-specific features such as double font width and height, while the upper four bits of each word in a row are used for blink, underscore, bold and reverse video attributes. Double-size characters are drawn in hardware by the VPAC. Although the VPAC supports horizontal scrolling and page flipping, the DECmate II's system software doesn't.
The other piece here is a 5.0688MHz crystal, which is divided down in various ratios to equal the serial port rates for the keyboard (4800bps) and serial and printer ports (up to 9600bps).
The DECmate II also came with a reasonable amount of documentation. I had the presence of mind to grab some of the boxed software during the rescue, and this one turned out to be a full accessory kit containing two manuals (an installation guide and the owner's manual) and a small box of disks ("System Test Diskette" BL-T345B-MA ©1983, and "System Overview" BL-P333B-BA ©1982-83). The box also contained a small folder with sticker labels for the RX50 drives and warranty card stubs, though the computer serial number they wrote down (#WF0006516) does not match this machine. The warranty card stubs were for three Infocom games (Zork Trilogy V1.0 PC200, Deadline V27 PC200, Planetfall V26 PC200), Daisy Aids DM (DECmate) as a basic charting package, and two WPS-8 components (DMII/WPS Package Kit and DMII/WPS DECspell). Since they had DECspell, their system must also have had an APU installed. Like Commodore, DEC rebadged several Infocom titles for the Rainbow and DECmate II; there was also a DECmate II port of Microsoft Multiplan as well, which we last encountered with the
Convergent WorkSlate
.
Unfortunately I don't have those disks, but we do have these two, so let's try booting them starting with the System Overview.
When you turn the system on initially, the "DECmate II" message will appear if all is well with POST, after which the system ROM-in-RAM waits for a disk in the top drive 0/A. Upon insertion the DECmate II checks track 1 sector 1 for a valid RX50 bootstrap block and track 0 sector 3 for the keyboard translation table. These must be present and validated to continue. It then reads track 0 sectors 7 to 10 and if valid, uses them to install an optional character set. This is intended for language-specific support. Following that, it finally loads the entirety of tracks 78 and 79 directly into CP RAM as 12-bit words. This is the remainder of the machine's supervisor code — or as DEC christened it, the "slushware."
The concept of "slushware" was new for the DECmate II: the original DECmate had its system ROM in the CP addressing space, but DEC decided it would be more flexible, not much slower, and above all rather cheaper to just load that code from floppy. In fact, slushware code directly descends from the DECmate PC278 ROMs — the name from being less permanent than
firm
ware, ergo,
slush
ware — and is for the most part upwardly compatible such that the majority of original DECmate software packages will run. It provides applications with an interface to the keyboard (key inputs, plus outputs to its LEDs and settings), access to video memory, VT52 and VT100-compatible escape sequences and terminal emulation, character set configuration and selection, access to the rear serial ports, the built-in setup applet, and sector-level disk access.
The main program is then started from the boot block (track 1 sector 1). In some cases it might load additional code into CP RAM, straining the concept of "almost firmware" since the slushware explicitly supports exchanging and rewriting both main and CP memory, including its own regions. Slushware also exists on DECmate II and later systems equipped with a hard disk, where it necessarily occupies different locations and is used to launch the hard disk-specific Master Menu.
The boot doesn't get far before running into a problem. Although the VPAC display is strictly character-oriented, it can still display various graphics. This flashing disk icon does not mean the system is loading, like, say,
the DesignWare chirp
— it means there's a disk error.
The RX50 has a very characteristic sound when it loads, with a clicky motor unlike any other floppy disk drive, and you can hear it in this video trying very hard. But the DECmate II's ROMs never say die; they'll just keep trying until they get something.
And at least initially, they do get something: a modest, though nicely animated, title screen. Move over, Apple Presents Apple; this is DECmate Presents DECmate.
Unfortunately, we can only get a little ways into the demonstration and tutorial ...
... before the system comes to a screeching halt. This is the DECmate II equivalent of a system error, complete with a full 6120 register dump, though the DECmate II was also the first of the line that could in some sense recover and even continue. On the DECmate VT278 and the VT78, you had no choice but to hard-reset.
In this case the floppy disk appears to be corrupt enough or the disk drive defective enough (or the system shot enough?) that continuing didn't work, but we
can
get into the slushware setup menu, where you can see the terminal and serial port settings. You can also boot another disk directly from here. Unlike typical serial terminals, because entering this menu might be unexpected by whatever the foreground program is, there is no key combination or button to press to immediately jump to it; the program has to
let
you do so and/or poop its pants first.
Since we got that error, trying the System Test disk seems the next logical step. We press Remove and are asked to switch floppies ...
... so we do, and press Do after we do so.
No flashing disk error this time.
The System Test disk is the nucleus of potentially an entire suite of self-tests and can also be used to format an attached hard disk. You'll note, however, that there is no option to format a
floppy
disk, and that's because DEC explicitly didn't allow it for the DECmate II. In fact, they didn't even allow it for the DEC Professionals either, roiling the user base who rebelled when forced to buy preformatted RX50 media from DEC or one of their overpriced tame vendors. Officially only later versions of CP/M and MS-DOS for the Rainbow could do this, and some users ended up buying Rainbows expressly for that purpose. We'll run the system test and see what's what with the hardware. Since this requires two floppies to test both drives, I put the System Overview disk into the second drive (remember, it goes upside down into the bottom slot).
The system board fortunately checks out, but the drives don't, and a thorough grinding with a 5.25" cleaning diskette didn't make a difference either. However, the test program is strictly pass-fail, much like my college grade point average, and there isn't enough detail to say if the floppy disk or the disk drive (or both) is to blame.
For a more thorough test, which will hopefully generate a disk image as a useful side effect that we can verify, let's pull out the RX50 and try driving it manually with a
Greaseweazle controller
. The drive uses a regular 34-pin Shugart floppy connector to the logic board, so we just pull the power connector and disconnect the floppy interface from the top, then depress the front lock tab and slide it out.
Unfortunately the DECmate's own floppy cable will not connect to a Greaseweazle; it has a key pin. Since we're already considering a solid state floppy emulator, let's just take the cable out entirely. It is secured to the chassis by a metal tab here, back by the main power supply cable ...
... and here, on top of the power supply itself where the Molex power connectors exit. We slide the lugs off the tabs and this will then free the cable fully.
Next, the drive itself. There are two ways you can connect an RX50 directly to a Greaseweazle. The simplest is to use a standard twisted PC floppy cable, but plug the
twisted
end in (as you face the unit, pin 1 is on the left), which also gives you the most length. I set it up this way initially for testing purposes.
In this configuration only the lower drive is active, which the Greaseweazle will see as drive A, so you'll need to insert any floppies upside down as usual. However, should you need both drives active, you can connect a straight-thru floppy cable just like the DECmate II's (or the first part of a PC twisted cable before the twist, if you don't mind it being shorter), after which the top drive will also be available to the Greaseweazle as drive B. Yes, this is different from how the DECmate itself enumerates the drives, but we can cope with complexity, no?
A quick speed check before we begin to verify the drive responds and the interface is operating.
% gw rpm
Rate: 300.629 rpm ; Period: 199.581 ms
% gw rpm --drive b
Rate: 300.682 rpm ; Period: 199.577 ms
Now to attempt some reads. I threw together a quick little
diskdef
to make this process easier:
% cat rx50.diskdef 
disk rx50
    cyls = 80
    heads = 1
    tracks * ibm.mfm
        secs = 10
        bps = 512
        rate = 250
    end
end
Here we have defined the RX50 format as a single-sided MFM floppy with 80 tracks, 10 sectors per track, 512 bytes per sector and a data rate of 250kHz (i.e., double density). This will generate a 400K image file.
Unfortunately both disks had multiple bad sectors. Some were more readable on several tries, and the lower drive was more consistent, but other sectors seemed completely blown. As the error pattern was generally the same between both drives, I concluded the floppy disks themselves were most likely shot. Here's the best read of the test disk:
% gw read --diskdefs=rx50.diskdef --format=rx50 testdisk.img
Reading c=0-79:h=0 revs=2
Format rx50
T0.0: IBM MFM (10/10 sectors) from Raw Flux (86384 flux in 399.75ms)
T1.0: IBM MFM (10/10 sectors) from Raw Flux (82693 flux in 399.88ms)
T2.0: IBM MFM (10/10 sectors) from Raw Flux (82438 flux in 399.84ms)
T3.0: IBM MFM (10/10 sectors) from Raw Flux (82965 flux in 399.76ms)
T4.0: IBM MFM (10/10 sectors) from Raw Flux (85809 flux in 399.95ms)
T5.0: IBM MFM (10/10 sectors) from Raw Flux (84448 flux in 399.71ms)
T6.0: IBM MFM (10/10 sectors) from Raw Flux (88619 flux in 399.84ms)
T7.0: IBM MFM (10/10 sectors) from Raw Flux (86363 flux in 399.69ms)
T8.0: IBM MFM (10/10 sectors) from Raw Flux (84200 flux in 399.89ms)
T9.0: IBM MFM (10/10 sectors) from Raw Flux (92215 flux in 399.70ms)
T10.0: IBM MFM (10/10 sectors) from Raw Flux (86482 flux in 399.78ms)
[...]
T57.0: IBM MFM (10/10 sectors) from Raw Flux (83216 flux in 399.91ms)
Unknown mark f9
T58.0: IBM MFM (8/10 sectors) from Raw Flux (82429 flux in 399.87ms)
Unknown mark f9
Unknown mark f9
T58.0: IBM MFM (8/10 sectors) from Raw Flux (206025 flux in 999.57ms) (Retry #1.1)
Unknown mark f9
T58.0: IBM MFM (8/10 sectors) from Raw Flux (329623 flux in 1599.24ms) (Retry #1.2)
Unknown mark f9
Unknown mark f9
T58.0: IBM MFM (8/10 sectors) from Raw Flux (453221 flux in 2198.79ms) (Retry #1.3)
T58.0: Giving up: 2 sectors missing
T59.0: IBM MFM (10/10 sectors) from Raw Flux (82857 flux in 399.90ms)
T60.0: IBM MFM (10/10 sectors) from Raw Flux (85518 flux in 399.76ms)
[...]
T75.0: IBM MFM (0/10 sectors) from Raw Flux (76092 flux in 399.78ms)
Unknown mark f6
Unknown mark f6
Unknown mark f4
Unknown mark f6
Unknown mark eb
Unknown mark f6
T75.0: IBM MFM (0/10 sectors) from Raw Flux (190208 flux in 999.17ms) (Retry #1.1)
Unknown mark f6
T75.0: IBM MFM (3/10 sectors) from Raw Flux (304343 flux in 1598.66ms) (Retry #1.2)
Unknown mark f6
T75.0: IBM MFM (8/10 sectors) from Raw Flux (418481 flux in 2198.17ms) (Retry #1.3)
T75.0: Giving up: 2 sectors missing
T76.0: IBM MFM (6/10 sectors) from Raw Flux (76119 flux in 399.80ms)
Unknown mark f6
T76.0: IBM MFM (10/10 sectors) from Raw Flux (190253 flux in 999.07ms) (Retry #1.1)
T77.0: IBM MFM (10/10 sectors) from Raw Flux (76081 flux in 399.76ms)
T78.0: IBM MFM (10/10 sectors) from Raw Flux (79042 flux in 399.74ms)
T79.0: IBM MFM (10/10 sectors) from Raw Flux (74392 flux in 399.82ms)
Cyl-> 0         1         2         3         4         5         6         7         
H. S: 01234567890123456789012345678901234567890123456789012345678901234567890123456789
0. 0: ...............................................X......................XXXXXX....
0. 1: ..........................................................X...........XXXXX.....
0. 2: ......................................................................XX.XX.....
0. 3: ..........................................................X...........XXXXX.....
0. 4: ......................................................................XX.XX.....
0. 5: ......................................................................XX.XX.....
0. 6: ......................................................................XX.XX.....
0. 7: ......................................................................XX.XX.....
0. 8: ......................................................................XXXXXX....
0. 9: ..........................................X...........................XXXXX.....
Found 749 sectors of 800 (93%)
% ls -l testrx50.img 
-rw-r--r--  1 censored staff  409600 Apr 21 09:58 testdisk.img
You can see several of the tracks from 70 on up were kaput, but most of the rest of the disk was fine, and tracks 0, 1, 78 and 79 in particular were clean. As this particular disk only has basic system tests on it, it doesn't appear we ever encountered those bad tracks during our usage. On the other hand, here's the best read of the overview disk:
% gw read --diskdefs=rx50.diskdef --format=rx50 overview.img
Reading c=0-79:h=0 revs=2
Format rx50
T0.0: IBM MFM (10/10 sectors) from Raw Flux (86508 flux in 399.82ms)
T1.0: IBM MFM (9/10 sectors) from Raw Flux (83769 flux in 399.91ms)
[...]
Cyl-> 0         1         2         3         4         5         6         7         
H. S: 01234567890123456789012345678901234567890123456789012345678901234567890123456789
0. 0: ................................................................................
0. 1: ...X............................................................................
0. 2: .X..............................................................................
0. 3: ...X............................................................................
0. 4: ................................................................................
0. 5: ................................................................................
0. 6: ...X............................................................................
0. 7: .......................................................................X........
0. 8: ...X............................................................................
0. 9: .......................................................................X........
Found 793 sectors of 800 (99%)
% ls -l overview.img
-rw-r--r--  1 censored staff  409600 Apr 21 09:51 overview.img
While only a few sectors read bad, those errors early on in tracks 1 and particularly 3 likely corrupted part of the main program, which in turn almost certainly triggered the program halt we saw.
Before conceding defeat, though, I wanted to compare the sectors that were readable with any other sector dumps of these disks to see if they were an unusual version or not. There are a few archives of DECmate-compatible software such as
ibiblio
. The ibilio disk images are in
Teledisk
format, which we could potentially use to remaster our floppies, but here we simply want to turn these Teledisk images into sector dumps as well so that we can compare and/or splice.
wteledsk
can do that: it will display the metadata in the Teledisk image first, then extract out the sector data. I tried it on ibiblio's version of the system test desk.
% wteledsk testdisk/TESTDISK.TD0 -oTESTDISK.IMG

BL-HV86A-MV                     075591
DM SYSTEM TEST DISKETTE V4.5

    COPR (c) 1986 DIGITAL EQUIP. CORP.





created June 01, 1994  17:10:41
string len 0x70  start variable 0x86 = 0x70 with 8 NULs
file length 0x35a88 = 219784


Normal EOF on track 79 #sectors in track record = 0xff
final file position 0x35a88  => this is EOF
parsed 80 logical tracks, 800 sectors with data 
 found 0 skipped sectors and 0 repeated (ignored)

max data sectors/track  10
The metadata and copyright date suggests this is a somewhat later disk from the DECmate II's successor model, unimaginatively called the DECmate III (or possibly the III+), which I'll talk about at the end when we finish the story. This disk is a bit differently organized and wouldn't be a good source for our missing sectors. However, the Internet Archive has
an image of our exact disk
in both
ImageDisk format
and as a 400K raw sector dump. It also has
the same version of the Overview
and some other
training software
examples. We could easily remaster our floppies with those, and it is possible to use a PC 5.25" with certain software packages to do so. (Or even format them — just don't tell DEC.)
But, now that we know we have exact images of our otherwise iffy disks, and there are more disks to be had out there that we can play with, I think it's time to bring on the Goteks.
I cobbled together this franken-solid-state-RX50 out of a new-style rotary encoder Gotek floppy emulator and an old button-based one I still had on the shelf. Since I figured I would be primarily using the second drive only as a data disk, I decided I'd use the older unit to just flip between a couple scratch volumes. Both have
FlashFloppy firmware
.
Because of the RX50's unusual construction and common motor-stepper assembly, whether you can successfully swap a pair of Goteks for an RX50 in any arbitrary DEC machine appears to depend greatly on the system's firmware. The DECmate II is atypical in that it usually works fine. This Gotek sandwich was originally intended for my DEC Professional 380, but the POST sequence would complain about it every time, and I've yet to get it working. On the other hand, there are people using them (apparently with different DEC Pro floppy controller cards) where they operate with no difficulty. One theory is that the more recalcitrant systems assume that both drives step in sync, as they would on a real RX50, and there is at least one attempt at
modified FlashFloppy firmware
to duplicate that behaviour. Even later DECmate III systems can be troublesome.
Since the, uh, superstructure will all be hidden inside the case anyway, I built it out of two 3.5"-to-5.25" bay converters and stuck little rubber standoffs between then to act as spacers, then taped it all together.
The floppy cable is an ordinary 34-pin PC floppy cable with a twist, with the top drive connected after the twist and jumpered to MO (no S0 or S1 jumper). The bottom drive is connected first before the twist. A Y-cable for power completes the connections.
The whole assembly fits nearly perfectly where the RX50 did, though we'll install it in a proper sled once we've verified compatibility.
The last things to do are to load some sample disk images and configure the FlashFloppy firmware for the interface connection. I put an image of the System Test disk on the top unit's USB stick and a blank RX50 image on the bottom's, then changed the following in
FF.CFG
on each unit's stick:
interface = shugart
host = dec
pin02 = low
pin34 = rdy
I also added a
ejected-on-startup = yes
for convenience to the top drive's configuration but that's personal preference, and powered everything up to read the settings in.
Of course, it helps if you plug the Gotek sandwich into the computer's floppy interface as well, or you'll get an error code 32 when you try to start (the brief concomitant moment of panic is just a bonus). The DECmate II ROMs are not as nice as the DEC Pros about telling you where the problem is.
It's booting!
We reach the menu successfully, not substantially faster but certainly no slower, to start the System Test again. Notice the track numbers counting up on the second drive during that test.
Full pass — both Gotek units test "OK" to the DECmate II.
To install it more securely, we will next take the sled off the RX50 and mount it on the Gotek sandwich. The four screws on the underside hold the sled on.
However, these screws are a bit too big to fit the smaller mounting holes on the 5.25" bay converter, so I put the screws in the RX50 (in case I decide to put it in something else or use it as a second set of drives) and used a smaller set from my bag of tricks.
This will now slide neatly along the rails, though the length of the sandwich does not quite match the RX50, so it won't be flush with the case opening. I dithered over how to fix this and eventually put a clip on the back of the sled. This ended up scratching the bottom surface under the sandwich, which I'm not quite happy about, but ...
... from the outside it looks nice and neat. I find the two-tone look kind of fun, actually. Remember that faceplates for the hard disks of this era were usually black as well, so this isn't a shocking computer fashion statement.
As a final test, I downloaded the raw image of the System Overview from the Internet Archive as linked above and put it on the top drive's stick.
It boots great.
I think it's time for a proper tour of the system using some additional disk images from the ibilio archive, but before we do, I'm also a bit tired of taking fisheye pictures of the monitor screen. The signal sent to the VR201 monitor is actually just high quality monochrome composite video, at least in 80 column mode, and some DEC users without a monitor of their own have fashioned dongle connectors that split up the DA-15 in the back into video, power and keyboard lines. But we have an iffy monitor here that has all the necessary ports already. Let's just add a composite jack to it, and this modified monitor will also work for monochrome grabs from our DEC Pro 380 in the future (and maybe a Rainbow if I decide to hunt one down).
The VR201 is quite easy to disassemble. (The usual warning when working on vintage monitors: CRTs contain high voltage and can maintain a dangerous charge for some period after use. Do not attempt if you are uncomfortable or unskilled with working around potentially energized glass tubes of this sort.) First, to get it out of the way, on the underside of the monitor press in the spring-loaded height adjust slide and pull the height pole all the way out from the monitor.
Next, with a spudger or carefully with a flathead screwdriver, pop this button cover off the back.
Under the button cover is a single Phillips-head screw. Remove that and you can slide the entire rear plastic shell off.
The circuit bar and CRT both sit in a metal cage. Here I have oriented the monitor so it's sitting on the circuit board side, but the circuit board is actually on
top
of the monitor, so this view is looking at the underside. We don't need to disturb the CRT for what we're going to do, but if you want to
discharge the CRT for safety
, this view shows where to find the suction cup anode.
The usual CRT adjustment pots are behind the tube.
What we'll do is solder a composite jack directly to the video input lines as a tap. This will necessarily bleed off some of the signal to the monitor when the jack is connected, but we don't really care about that for this purpose (if you did care, you'd probably want to pre-amplify the video signal a bit). We'll access the underside of the monitor's DA-15 by undoing these two top screws and folding back the Tyvek non-conductive shield.
Using the
BCC02 cable pinout
, you can see multiple lines fused together into a single ground and two others into a single +12V, and the rest for keyboard, video and colour lines, which are irrelevant here. On this hand-routed PCB the power and ground conglomerations are obvious from their fatter traces. To avoid the risk of causing a short near the +12V power lines on the DA-15 connector itself, I decided to only attach ground there and looked for another solder point with continuity to pin 12, the monochrome video input. I found a nice strong signal on the "highlighted" junction up and to the right (northeast) of the rightmost/easternmost screw in this picture, about 4/5ths of the way to the right.
I put the signal line on that point, then soldered the ground to the big ground junction on the port.
With the cable attached, I grabbed another of the same size and took the plastic shell out to the workshop to cut a hole for it. We'll route it out through the ventilation slots.
Buffing the hole with the Dremel to clean it up a little.
To accommodate the new cable I removed the rear plate over the ports and thumbwheels, then routed the cable down, around and out the hole.
These captures were done directly from our hacked-in composite output. Although it cuts off the rightmost column and a rasterline or two at the bottom, which might indicate the signal isn't
quite
standard, this isn't noticeable most of the time and the image quality is very good. However, I forgot to plug the keyboard in before I turned it on (so error 16). We'll fix that and then drive around the block.
Ready to start. One more check of the System Test.
And it's good.
Back into the startup menu to start our first package. We'll spend a little time with WPS-8, which is nearly the whole reason the DECmate series existed. The version we'll use here is a 1987 release from the DECmate III era to give you the full breadth of what was possible.
DEC's Word Processing System was a comprehensive solution, evolving from a basic terminal-based word processor on the VT78 into (by this period) a remote-enabled, multiuser document management package. WPS-8 is the PDP-8 standalone version which scaled from single user to concurrent terminals in the WPS-8/MTS variant; it was the first iteration of the WPS family, developed by a team at Digital (including Dan Bricklin, later to co-create VisiCalc) for the DEC Datasystem 310W based on the 8/A, and then quickly ported to the VT78/WS78 and DECmates. Although dedicated word processing systems from companies like NBI and Lexitron were already on the market, WPS-8 was the first such package written for a general purpose computer. A parallel system called WPS-11M ran as a task under RSX-11M on PDP-11 servers for document storage and tracking, and WPS-11M could send code to VT78/WS78 systems with specific ROMs so they could edit and upload documents from the local machine. This functionality was moved into software for the DECmates.
Regardless of how good it was at creating the office of the future, however, it isn't so good at accepting the
dates
of the future. We'll just fudge that. Date and time are shown in the top right corner nearly everywhere except, oddly, when editing a document.
The menu system uses short one or two letter commands and sprawls over multiple pages. It starts with the basics, create, print and filesystem. Notice the default drive: on a dual-drive system it prefers to keep the system disk in one drive and your data disk in the other ("drive 1"). We'll set that up in a moment.
Additional optional packages included list processing support, which is basically DEC's take on form letters and mail merge, and a companion sort package that can rearrange list documents by field.
The character transmission package replaced the VT78's WPS-11M downloadable client functionality, becoming regular software loaded from floppy into the DECmate. It could use a directly attached serial port or a modem connection to the remote PDP-11 to send and access documents.
Disk management tools to backup floppies and system diskettes were also provided. There was no copy protection on the system diskette and DEC even encouraged you to make copies of it. You could store documents on the system disk as well, which was useful on a single drive system, but is rather less necessary with an RX50. However, the disk initialization options here only erase the disk to set up the proper storage structures for WPS-8: they don't low-level format it, and DEC was careful to call out the difference in the documentation. Only 8" disks could be formatted by WPS-8. For the RX50, you still had to buy your pre-formatted 5.25" floppies from DEC at mildly confiscatory rates, or use your appropriately configured Rainbow, or find one of the unofficial "Clandestine Disk Formatters" that could do so on the hardware itself. You then initialized that pre-formatted floppy here.
As it turns out, we don't have that problem anyway because we have a clean blank RX50 image loaded in the second drive. This will become the lower Gotek's disk image #0.
The process is not fast, though the Gotek greatly speeds it up; while the manual says to expect about three minutes to complete the process, we readied our virtual WPS-8 document disk from start to finish in just over 90 seconds. The Gold MENU key referenced here is PF1 followed by M on the LK401, but you can also just press F9. On the official DECmate II keyboard the Gold key was indeed indicated by a gold plastic keycap that was otherwise blank.
Some of the other WPS-8 menu shortcuts.
Let's create a simple document of our own by using the C option.
One notable thing about WPS-8, especially for the era, is that its document naming rules were very free given it was intended for relatively non-technical users. Document names could be up to 71 characters long, in mixed case, permitting spaces, numbers and most symbols except for angle brackets. The only notable restrictions were that a filename could not start with {, [, or a number, or start or end with spaces (though all of those characters were legal otherwise), and you shouldn't name a file something that completely contains the name of another file (like
Monthly
vs
Monthly newsletter
) or you might make the file inaccessible by that name. We'll talk about why these restrictions exist when we get to the disk index. Here we will write a short and pointed letter to Kenneth Olsen.
Intended for non-proportional dot matrix and daisywheel printers, the display is as WYSIWYG as you'll get on a terminal, with a small "ruler" indicating left and right character margins. Word wrap respects these margins, and adjusting them would automatically reflow the document accordingly, repaginating it as necessary (widow and orphan adjustment could be optionally enabled). This ruler could also be used to mark tab stops and justification points for more advanced formatting, and could be saved to the system disk for regular reuse. A top status bar tracks your cursor's page, line, and character position. The DECmates could show bold and underlined text. Combinations with the Gold key are used to mark text, to set attributes, to move by word, sentence or paragraph, or to cut and paste.
When you were done, Gold MENU would bring you to this options screen. The math option was for the optional Math package, allowing live calculations in the document, sort of a proto-spreadsheet not unlike the
Canon Cat
. You could also adjust the page layout, print, do search and replace, reference a library document for prewritten text, or define "user keys" for storing a sequence of keys as a macro. Library documents and user keys, along with text shortcut abbreviations, could also be saved on a system disk.
We'll pick the F option to file the document, which will save it to our virtual data disk in the lower Gotek.
The disk directory can be seen from the menu's "index" option. (Again, apologies for the last column being cut off.) This is stored as a phantom document on the disk called the
<Index Document>
. Each document has a number and the index document is always document 1, created as part of the initialization process and automatically maintained by the system as documents are created or deleted. It contains a mapping of filenames to document numbers for loading a file by name, though you can also use a document number directly, which is why you can't start a filename with a number. When retrieving a file by name the system searches for the first match in the file, which will accept partial matches, so if you had file
Monthly newsletter
as document 2 and
Monthly
as document 3, loading
Monthly
would actually retrieve document 2 (which is why you shouldn't name files substrings of other filenames).
You can edit the index document like any other document and this is in fact the easiest way to do things like renaming, but you'll notice that there are angle brackets in that file to indicate the file number (which is why you can't use angle brackets in a filename, and they are also used as metacharacters in things like abbreviation definitions). It is possible and supported to create an index document that refers to documents scattered across multiple disks (a "master index").
Finally, the program prefers you to explicitly finish before you power off or leave the system. This not only ensures everything is written out and files are closed, but also clears the paste buffer (in case you're just leaving for lunch and don't want someone snarfing your deleted text).
If WPS-8 was too big (or expensive) for you, DEC later offered a cut-down glass typewriter program called TYPEasy as a poor substitute.
TYPEasy has substantially fewer options and is primarily oriented to spewing text you type, either directly or (more helpfully) line by line, straight to an attached line printer. This is even less functional than the typewriter motif in Commodore's
Magic Desk
, which at least could keep lines in memory.
In fact, you really can't do anything useful with it at all if you don't have a printer connected, and we don't. TYPEasy doesn't seem to have been very popular and there's  little out there about it.
So, now that we have a working copy of it on the Gotek, we should revisit the System Overview next. This is actually a very extensive program and we'll just show a little bit for flavour. There were other interactive computer-based instruction disks for the DECmate, including ones specifically for WPS-8 and its optional packages.
The Overview and other CBI titles had detailed, stepwise instructions to a degree that might seem excessive to us nerds but was probably appreciated by office users at the time, and makes regular use of the keyboard's special keys.
Main menu. It is mercifully possible for advanced or partially trained users to skip ahead to an arbitrary topic.
However, some of what this disk has (and this is the disk we have, specifically for the DECmate II) seems to be inaccurate. This is legitimately where the Set-up key is on the official DECmate II keyboard (i.e., F3), but programs will not generally let you enter it on demand.
It nevertheless presents a reasonably accurate facsimile of the user experience, including the slushware setup screen, which we just "inverted." If you press the wrong key, the program will not let you continue until you press the correct one.
Units have a summary at the end for reinforcement. A unit number in the upper right corner allows you to monitor your progress through the lessons.
Simple graphics and animation turn up in various places, such as this rendering of a 5.25" floppy.
When you exit, the program lets you boot something else. Let's do something fun.
Drumroll please!
At least a couple games disks were produced for the DECmate family. This is the first volume, with an animated text title screen.
I'm not going to go through all of these here on both disks, but we'll show a couple for a taste.
The disks also have a "word from your sponsor," soliciting additional programs and encouraging membership in DECUS, the Digital Equipment Corporation Users Society. However, that required talking to your local salesdroid and you know how I hate talking to salesdroids.
On this first disk the games are generally simple text-based programs which were (near as I can tell) all or largely written in BASIC, and many likely originated from Digital's own
101 BASIC Computer Games
, edited by David Ahl (later to found
Creative Computing
). For example, here is the venerable
Hamurabi
. Compared to the version I have on
6o6's Apple-1 emulator
, this version is a bit more florid with the text, but uses the same general algorithm as most other spins on Hamurabi and can be "won" (to the extent the game can be) using the same sorts of strategies. Since it's BASIC, you can break out of it and most of these games by pressing Control-C, which will return you to the menu.
Defuse puts you in bomb squad mode with your trusty bomb tracker in a suspiciously large governmental building that on paper resembles a Borg cube.
The game ends up requiring more trigonometry than I was comfortable with, and I decided to take a forced retirement off the 100th floor to see what it would do. Turns out wind resistance is also futile.
And what collection of BASIC games would be complete without
Star Trek
?
This spin is a modified version of the reworked Super Star Trek version and plays very similarly to other SSTs of the time.
The second games disk gets a slightly different "digital" logo splash.
It also has a more elabourate volcano animation, though one annoyance is I couldn't seem to skip it. However, the "word from our sponsor" screen is the same.
This disk skews more towards fancier arcade-style games and has a blingier menu (again, sorry for the right column getting cut off). They have the distinct feel of early IBM PC games played on the text screen, and likely because no one custom character set would have sufficed for them all and/or disk space considerations, everything is depicted in the stock text and line-drawing character sets. As before I lack sufficient space to show them all here, but we'll do the highlights.
Did it ever bother you that between all that hard, hard word processing hardness you couldn't just sit back and play Pac-Man on your coffee break? Exceptional Business Solutions, an exceptionally ironic business name for a game title (unrelated to the 2006 company with the same name of indeterminate irony), has you covered with DECmaze. Not DEC
mate
, DEC
maze
. Exceptional Business Solutions was a Culver City, California-based outfit that developed DEC-specific software; this iteration of the name closed up shop in 1993. You will see them again at the end.
DECmaze is the DECmate's Chex Quest, a Pac-Man ripoff slavishly devoted to platform sales. Your task, in the words of the instruction screen, is to "[g]uide DEC through the perils of the small business computer world. ... Capture all the sales while outmaneuvering the competition. ... Additional 1000 points for capturing the computer market (get all the dots)." The diamonds give you the "Advantage" (eat your competition). The hapless phantasms roaming the maze are APL, IBM, TRS and WNG, and they certainly do not violate any trademarks. At all.
DECbert is another arcade ripoff, this time of course of Q*bert, though this version is more of a puzzler than an arcade game (no Coily or Ugg, you provide the @!#?꩜). There are no enemies and no time limit. You basically play until you're tired of it.
You are scored not only on changing the "colour" (shade of grey) of the squares, but also on the number of moves you
wasted
jumping to a square that was already the right colour. On higher levels where you have to change it multiple times, this not only penalizes you but can significantly retard your progress.
And of course if we have Pac-Man and Q*bert, then we must have Space Invad ... I mean, Space Demons, which is completely unrelated to any other arcade game of any sort ever made.
Ever.
Thanks for the encouragement ...
... and the disclaimer.
This games disk also "includes"
(Colossal Cave) Adventure
. In reality, it's merely a launcher; the game occupies an entire RX50 disk of its own. This particular spin has a rather interesting history, hailing from Don Woods' variation of William Crowther's PDP-10 original, then ported to RT-11 (on PDP-11 systems) by Bob Supnik and that version ported to the PDP-8 by Dick Murphy, both at DEC.
It also has its own, and also slightly different, Digital splash screen.
The particularly interesting part is that DECmate Adventure exposes its OS/8 underpinnings (or some later vintage, to be explored a little later) directly to the user: you manually save and resume your game as memory dumps, making it a good segue into OS/278 which I'll talk about after this one.
We'll start a new adventure and prepare the disk for saving, though we won't play enough of the game here to be worth doing so.
The setup process clears some files (with an ominous pair of wild cards) for space, plus some other tasks which are not shown onscreen. This is actually a script. We'll come back to this too.
After it finishes you get dumped into the command line. The } shows that the higher-level command interpreter CCL is active (the "Concise Command Language"). The
R GMU
command pulls a saved executable image from the main disk and starts it (in this case
GMU.SV
), bringing you back to the menu where you can "Start your ADVENTURE" [sic].
Otherwise this is a relatively straightforward port.
You can get to the } prompt by telling the game interpreter to
SUSPEND
, though there's not much else you can do from there other than manage the game state, resume it, or quit. Still, the fact it responds to the
DIR
command at all proves the entire executive is indeed present:
DIR
is internally converted by CCL into the lower-level Keyboard MONitor command
R DIRECT.SV
followed by command decoder input
TTY:<DSK:/E=2
(expressing that both the TTY and
DSK:
disk device are being used and a default option
/E=2
). KMON will faithfully try to load it, though there is no
DIRECT.SV
on the disk, so the CCL command won't work.
We do
R GMU
again, but this time we pick the third option to boot a new diskette (or return to the Master Menu on a hard disk-equipped system). Let's move on to our last stop, OS/278.
DECmates that didn't primarily run WPS-8 or COS-310 (or CP/M or MS-DOS, if you had an APU or XPU) almost certainly ran OS/278 in some form — sometimes undetected, as we'll demonstrate — and that makes it a good conclusion to our brief software tour. For that matter, it's where
I
spend most of my time on this system as well. It descends originally from OS/8, the primary development environment for classic PDP-8 systems first introduced in 1971 that gradually displaced most of its predecessors (including the "Programming System/8" [PS/8] from which it itself evolved). Here's
a good resource
on classic OS/8.
OS/8 presented a simple, single-tasking command line operating system with a minimum resident portion in memory, making the most of the PDP-8's limited addressing space, alongside a flat file system oriented to the device level that worked on DECtapes all the way up to hard disks. Its space and memory requirements were considered modest, and it can boot very quickly even from floppy or exceptionally fast from a hard drive since the kernel (what DEC called the "OS/8 Executive") was quite small, even by the standards of the time. OS/8 was most often used for creating and building software, like its ancestor PS/8 was, though it could also be used as a general-purpose operating system for other tasks. During the development of the VT78/WS78, OS/8 was forked at V3D and rebadged as OS/78; while mainline OS/8 continued along its own development, OS/78 subsequently dropped various aspects of backwards compatibility such as support for Omnibus, which was irrelevant to the word processor line, and added compatibility for changes in the DECmate family. There were well-known bugs in these early versions. Many were resolved by OS/78 V4, which was rebadged as OS/278 for the DECmate VT278; version 2.0 is what we're demonstrating here, which of course also runs on the DECmate II.
As mentioned earlier, backward compatibility with earlier PDP-8 hardware was not a development priority for the DECmates, and any level of it that existed was to some degree accidental. In fairness DEC never billed them as such (certainly not to the extent they later touted the DEC Professional as a "desktop PDP-11"), though the gaps rankled certain users anyway, and OS/78 and OS/278 cannot serve as practical substitutes for OS/8 because a non-trivial amount of PDP-8 software will not run on the later versions. Part of this was software changes, dropping support for irrelevant hardware features of the larger PDP-8 systems, but also deliberately locking out lower-level components. In addition, the device handler interface changed in OS/278 specifically, causing older device handlers to fail to the point where the same program might not run from floppy but would from a hard disk, and OS/278 2.0 did not maintain compatibility with other older system components either. However, there were also hardware changes that were especially more acute with the DECmates: the 6120 CPU handled instructions for interrupts and certain I/O operations differently, and aspects of the 6121 IOC/PIE chips caused altered flags particularly on the console which older programs didn't expect. DEC's documentation on these points was terse, the general opinion being that if you were running an OS/8 derivative on a DECmate, then you were skilled enough to deal with those sorts of irregularities.
Like we saw in Adventure, the standard prompt is }, indicating the Concise Command Language (CCL). A lengthy readme came on the disk, so we'll enter
type notes.tx
to read it. This version of OS/278 can accept lowercase input. The OS/8 filename convention is 6.2.
The executive in OS/8 and derivatives has four main components. The
Keyboard MONitor
is the lowest-level interface, with a permanently resident portion consuming only 128 words each in fields 0 and 1, and the rest loaded or swapped as needed. This stub is the only persistent portion of the executive and makes it possible to run OS/8 in as little as 8kW. KMON accepts basic commands for specifying devices, and loading, executing, debugging and saving memory images. To load these files, a request goes to various
user service routines
(USRs) that open and close files, start execution, and so on, analogous to system calls, which will activate
device handlers
to fulfill the request. If a program is to be executed, the devices and files it needs are specified at runtime and parsed by the
Command Decoder
. All of these pieces are swapped in and out of main memory as required.
The CCL, on the other hand, is a separate program. Its sole purpose is to turn commands into KMON and CD equivalents, patterned after TOPS-10, and in OS/78 its use became obligatory likely as Digital's way of standardizing their command line interface between systems. A badly-kept-secret setting, to be even more badly kept shortly, allowed OS/78 users to still drive KMON directly but was removed in OS/278, much to the displeasure of OS/8 power users.
The lengthy multipage text file here is the core documentation for OS/278 on floppy. There was never an official printed manual for it, though much of the OS/78 manual suffices. This readme also makes reference to two other disks containing BASIC, Fortran and the hard ("Winchester") disk installer, but I have so far only found this first floppy image, which fortunately has most of the operating system.
On our RX50 DECmate II we can access the individual drives directly as
RX50:
and
RX51:
. We can list the files on the top drive where the system disk is loaded with
dir rx50:
, which as we mentioned earlier is internally a KMON command of
R DIRECT
and a CD argument of
TTY:<RX50:/E=2
.
These are the files on the system disk. I'll talk briefly about them in a moment.
There isn't much space left on this disk and I don't want to run the risk of messing up its contents. To make a data disk, in a separate session I copied the OS/278 image to the lower Gotek's USB stick as image #1 and deleted all the files on it with
delete rx51:*.*
.
dir rx51:
now shows a clean empty directory with 711 free blocks. The image still has the system heads on it, an untracked segment at the beginning with the bootstrap, monitor and overlays, but this is more than enough space for my purposes. In this brief demo I'm not going to do more with the blank image other than to note its presence, but in
a future article
we'll be doing some programming on it.
The system pseudodevice
SYS:
points to the boot drive, which in this case is the top RX50 slot, and thus has the same directory. The other important pseudodevice is
DSK:
, which is the "working" device and by default points to
SYS:
(something like
ASSIGN RX51 DSK
will change that).
The majority have the extension
.SV
, a saved "core image" of an executable, but there are also a couple
.TX
text files and one
.HL
help database. A particular saved image can be used for multiple commands; the major ones are
FOTP.SV
(File Oriented Transfer Program, handling copies, renaming, deletion, etc.), and
PIP.SV
(Peripheral Interchange Program, used for disk-wide maintenance; the CP/M utility of the same name incorporates aspects of both). We also talked about
DIRECT.SV
, but you can also see the
PAL8.SV
assembler, the
EDIT.SV
and
TECO.SV
editors,
WPFLOP.SV
for interchange with WPS-8 disks, the DECmate-specific utility
SETUP.SV
to enter the slushware setup screen and/or boot another disk, and three versions of Kermit with different baud rates. As usual, the provided disk format utility
FORMAT.SV
doesn't work for RX50 disks. The latest files on this floppy date to July 1984.
I mentioned a backdoor of sorts in the original OS/78 (
SET SYS OS8
) that would let you issue direct KMON commands, which are more baroque but can be more expressive. However, this setting doesn't work on OS/278 and despite appearing to succeed enables nothing. In fact, if you do issue it, it then proceeds to punish you by printing an error message on every command afterwards until you revert it (
SET SYS OS278
).
Even users that didn't know they were running OS/278 were often invisibly running OS/278. For example, the System Test disk ... is OS/278. (The
.PA
extension would normally indicate a PAL assembler file, but these are actually just text screens. I am not sure of many of the extensions as used here.)
And so is the System Overview. The presence of
BASIC.OV
suggests it was written in compiled BASIC.
And, in the "no surprise by now" category, so are our game disks, though they don't like being loaded from the second drive. (I'm using the long-form
RUN
command instead of
R
to run a core image since these are not on
SYS:
.) I suspect they want their
.OV
overlays installed on
SYS:
, which they would be if we booted from the disk directly. Some of these game programs date back to the late 1970s.
We can also look back at our Adventure disk and as suspected we can see that it is, in some form, also an OS/8-derived format. The
.BI
batch script that cleaned up the saved image on our game disk is shown, with a structured look very appropriate to DEC of that era.
However, these game binaries also don't like running from this version of OS/278 directly, or being on the second drive, or who knows. There might also be a format problem specific to this disk: the uniform May 1, 1977 dates are instantly suspicious as that's around when Don Woods would have written his version on the PDP-
10
. Trying to run them gave some weird error messages, and then the system itself got wacky, and then my OS/278 boot disk wouldn't, and I finally had to replace the image on the USB stick with a fresh one. Keep backups of your disk images; the DECmate generally expects to write to them and a wrong step might make it write something you don't want.
Situations like that are a good reminder to the modern retro spelunker that OS/8 and friends can be an alien environment for the uninitiated. Fortunately, there is a decent amount of basic online help.
HELP
all by itself brings up this command list.
Not all of the commands work, unfortunately: there is no BASIC because I don't have that disk. But we should be able to work the assembler.
Fortunately, the assembler does have basic online help of its own and is explained with
HELP PAL
. This is where we will be doing our future work. For now, this gives you an idea of what you could do, and how (IMHO) OS/278 makes the DECmate II feel most like a "real computer."
* * *
Let's finish our story of the DECmates before we conclude. The DECmate II was the only machine in any way successful from the DEC Small Systems Group; the incompatibilities of the Rainbow with DOS programs and the first-generation DEC Professionals with PDP-11 packages, plus the lack of promised Pro-specific software, rapidly led not only to their own demise but also that of division VP Andrew Knowles in September 1983, the sixth VP to leave Digital in just two years. Even though the DECmate II didn't sell in large numbers either, it still succeeded where its siblings failed because it was relatively inexpensive, avoided the supply problems of the other systems, had readily available application software, and didn't get advertised as something it wasn't.
Despite this, the DEC Personal Computer Group, the inheritor of the SSG, tried again with reworked versions of all three. In April 1984 DEC introduced an updated Rainbow 100B with improved compatibility and more memory, and in September 1984 rolled out the substantially more powerful DEC Professional 380. A month after that, the DECmate family got its own new member.
The DECmate III was introduced in October 1984 as an evolutionary, cost-reduced version of the II and at least initially positioned merely as a lower-priced alternative. "Professionals might select the DECmate II, while clerical staff would use the lower priced, text-intensive DECmate III," James Gallagher, DEC's DECmate manager, said at the production demonstration to
Computerworld
. With the exception of the APU, DEC had noticed that the DECmate II's expansion capability went largely unused and thus cut it to a single expansion slot, shrinking the main board and at the same time consolidating a significant portion of its discrete logic into custom gate arrays. It used the same 8MHz 6120 and had the same 64kW of RAM (while early announcements indicated 96kW, released systems have only the same twelve 64Kbit DRAMs), although like the DEC Pro the printer port was also capped at 4800bps. Later versions of slushware were required for these minor hardware changes, but OS/278, WPS-8 and COS-310 were still supported.
The III's single expansion slot could accept one of the later II graphics cards or its own revised Z80 APU, since WPS-8 benefited from it, though not a hard disk and only one option at a time. An internal "Scholar" modem option plugged into its own separate connector. Although a III with the Z80 APU could still run CP/M, the XPU was
not
supported and thus neither was MS-DOS. The base system with standard RX50 dual disk drive and VR201 monitor started at $2695 [$8675 in 2026 dollars].
Contrary to the original intention, however, sales of the DECmate II were starting to wane by the time the DECmate III became available in early 1985, and the older machine was too expensive to continue producing. Correspondingly, the II was sold at a substantial discount from May 1985 until stocks were exhausted in 1986. To make up for the lack of a hard disk-capable DECmate, DEC subsequently incorporated the DECmate II's controller onto the DECmate III logic board and included an 20MB ST-225 drive, though they also removed its internal modem connector and replaced the dual RX50 with a single (Teac) RX33, making it practically impossible to install CP/M. This was sold as the DECmate III+ for $5145 [$15,400] alongside the standard III.
Still, no DECmate ever achieved the sales goals DEC management was hoping for, and while Ken Olsen was adamant the company should not compete in the cutthroat home computer segment, the personal computer line wasn't making much headway against IBM's business desktops either. Indeed, Digital's bread-and-butter was still big iron in the back room, which in those days meant VAXen and late-model PDP-11s, and for customers who didn't want a full computer on every desktop their ALL-IN-1 package had delivered a well-regarded office automation suite with messaging, word processing and time management to any connected terminal since 1977. Continuing to produce pint-sized PDPs for an indifferent market seemed like a sucker's game when an off-the-shelf PC could do the same job — as long as it also helped DEC sell more VAXes.
Publicly, at least, the new concept ironically started with the Rainbow, DEC's already existing not-quite-a-PC. "Anybody can make an IBM PC-compatible machine," Olsen declared, probably handing his beer to somebody, and in March 1985 DEC announced the end of production of the Rainbow 100 to be replaced with the new Rainbow 190. For $6495 [$19,500] you got the same basic hardware with a 10MB hard disk, 640K of RAM, MS-DOS 2.11 ... and WPS-Plus, a port of WPS directly to MS-DOS advertised as fully compatible with WPS-8 and WPS-11M. Remember Exceptional Business Solutions and Pac-Man on your DECmate? WPS-Plus was their work, and the 190 even came with the same Gold Key keyboard that the DECmates did. An optional DECnet networking expansion and the Rainbow Office Workstation suite were also announced for the entire series, integrating the Rainbows tightly to your local VAX with ALL-IN-1, yet still being able to run MS-DOS software (well, to the extent any Rainbow was able to). Digital even announced such an ALL-IN-1 oriented package for the DEC Professional.
As it happened, by then approximately nobody wanted a new Rainbow that was roughly an old Rainbow, and suspiciously to observers, DEC didn't seem too serious about producing it either. "It appears that the 190 was announced primarily to counterract [sic] media reports that the Rainbow had been scuttled by DEC," commented editor Caroline Mack in the December DECUS PC SIG newsletter, and contributor Brian Orr added it was obvious "that the Rainbow 190 was also a hyped system that was announced to keep DEC in the PC news." Only a small number of 190s were actually made.
In February 1986, a leaked internal memo emerged from Digital's Personal Computing Engineering Group dated January 1985 that mentioned a Rainbow successor, with "a goal of having the first units in the July 1985 time frame." Codenamed the PCXX, the alleged machine was built IBM PC/AT-compatible from the ground up, with an 80286 CPU and ISA slots, and correspondingly had nothing directly in common with its ancestor. DECnet was built-in and for the first time on any DEC computer it could run standard MS-DOS. Industry interest forced DEC to admit that such a system was indeed in development, but delayed, in large part due to problems developing the VAX server piece for supporting the PCXX as a client; over 250 people from various divisions had been pulled into the project by February 1986. The deadlines were still slipping, and the admission exposed the Rainbow 190 as nothing more than a bid to buy time, but by then the PCXX had also picked up a new name: the VAXmate.
The VAXmate finally hit the market in September 1986 starting at $4045 [$12,100]. It had an 8MHz '286, 1MB of RAM, a 14" monochrome display, a single RX33 5.25" floppy and built-in Thinnet for DECnet connections. A '287 FPU, an additional 2MB RAM card or an internal modem were all options, as well as a hard disk expansion chassis installed under the CPU box that added a 20MB hard disk and two ISA slots. Notable for the time, DEC included a 3-button hockey puck mouse. The custom video controller could generate 16 shades of grey, with up to a 640x400 or 800x252 4-shade graphics mode or a 320x200 16-shade graphics mode, plus the usual 80x25 and 40x25 text modes. Its unique LK250 keyboard resembled the LK201 and provided both DEC and IBM-style function keys, including a Gold key for WPS-Plus (which was available and prominently marketed for the new machine), but used the same 6-pin SDL plug as early Model M keyboards. DEC claimed it was the first microcomputer designed for networking because of the built-in Ethernet, and while other factory-networked systems certainly existed prior, I agree it is one of the earliest desktop machines to include standard Ethernet of any kind.
The VAXmate initially ran MS-DOS 3.1 and a custom version of Microsoft Windows 1.0 bundled for an additional $250 [$750]. But the real secret sauce was VAXmate/VMS Services, which DEC also released in versions for the Rainbows and the IBM PC family, that could share files with a VAX/VMS server or act as a VT220 or VT240 terminal. DEC sold a single seat basic install for $650 all the way up to a top-end $19,500 site license. For the back end DEC announced a turn-key MicroVAX II system with 5MB of RAM, Ethernet, 16 ports and a 30-seat ALL-IN-1 plus WPS wordprocessing starting at $81,160 [$243,000]. In March 1987 DEC offered an additional VAXmate configuration intended for desktop publishing bundled with WPS-Plus, Aldus Pagemaker and Microsoft Chart all running under Windows for $6670 [$20,500], or the VAX Departmental Publishing Solution with an ALL-IN-1 backend, file storage services and the DECpage batch formatter starting at $41,161 [$124,000].
In the end, however, the VAXmate failed to supersede the DECmates and in some respects fared worse. Industry observers pronounced the machine a disappointment despite its technical achievements because it was simply priced too high for a 286. In March 1988 DEC slashed the price to $3495, or threw in a VAXmate with a VAX purchase for just $3195, or if you bought more than 25, $2995 — and the network client software now came included. The inevitable lack of response caused DEC to reluctantly can the VAXmate in 1989 and partner with Tandy to rebadge their popular PC line as DECstations instead — and you could even trade in that old Rainbow — though that's another story for another day.
And what of the DECmates the VAXmate was supposed to replace? The resilient WPS-8 user base turned out to have no interest in giving up what worked, and unable to ignore that market completely, DEC ended up keeping the DECmate IIIs on the sales list until 1990 when the product line was finally terminated.
The DECmate II is widely considered the DECmates' peak and in my personal estimation is the best example of the line, though it is also fair to observe, as some have, that the DECmates are barely PDP-8s in any technical sense. Still, they're closer than people think and their pedigree is legit, and while they don't have the hardware flexibility of the canonical systems, the software still gives you enough flavour to entice you back to the originals. There are various
simh
-based reconstructions of the PDP-8 and some you can even run on
miniature replica front panels
, but for me the DECmates have a more convenient form factor and the irreplaceable heft of being true historical artifacts. With the Goteks on board this is now a quieter system with tons of things to play with, and
in a future article
we'll talk more about the instruction set and write some programs.
Digital wasn't finished trying to make workstation versions of their servers, by the way, but we'll talk about another miniature midrange we have in the Floodgap lab
later on as well
. In the meantime, please excuse me so I can finish banging out that pointed letter to Kenneth Olsen.
