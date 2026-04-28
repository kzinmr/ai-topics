---
title: "Refurb weekend: Silicon Graphics Indigo² IMPACT 10000"
url: "https://oldvcr.blogspot.com/2025/09/refurb-weekend-silicon-graphics-indigo.html"
fetched_at: 2026-04-28T07:02:04.932270+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Refurb weekend: Silicon Graphics Indigo² IMPACT 10000

Source: https://oldvcr.blogspot.com/2025/09/refurb-weekend-silicon-graphics-indigo.html

It's one of my periodic downsizing cycles, which means checking the hardware inventory (and, intermittently, discovering things that were
not
on the hardware inventory) and deciding if I want to use it, store it or junk it. And so we come to this machine, which has been sitting in the lab as a practical objet d'art when I picked it up from a fellow collector for the cost of take-it-away almost exactly a decade ago.
This beautiful purple slab is the Silicon Graphics Indigo² (though, unlike its earlier namesake, not actually indigo
coloured
) with the upper-tier MIPS R10000 CPU and IMPACT graphics. My recollection was that it worked at the time, but I couldn't remember if it booted, and of course that was no guarantee that it could still power on. If this machine is to stay working and in the collection, we're gonna need a Refurb Weekend.
Counting this sucker, there are three SGI systems presently in the house. (I had a chance many years ago to land one of SGI's early 68K IRIS machines, I think an IRIS 3110, but I was still in a small apartment back then and hadn't the space. I've always regretted turning that one down.) The "big" one is a 900MHz R16000 SGI Fuel (codenamed "Asterix") with 4GB of RAM and a V12 DCD graphics card; the line was first introduced in 2002 and is best described as a single-node Origin 3000. This particular machine has a penchant for chewing up timekeeper batteries and power supplies, and true to form it's recently devoured another set (probably capacitors in the PSU's case), so
a future Refurb Weekend
will involve converting it to ATX. The Fuel certainly has its detractors, mostly Tezro owners, but I've already hit my quota for big, hot and loud RISC workstations with my trusty Power Mac Quad G5 (the Raptor Talos II is rather more tractable). The Fuel, by contrast, is reasonably quiet and for me powerful enough, I love the bright red tower case, and its more commodity PC-like design might seem chintzier but I find it also makes it easier to work on.
The other one you've met and is my personal favourite: the pizzabox SGI Indy (codenamed "Guinness"), introduced in 1993. This Indy's most recent appearance was as
the Hyper-G server
for the RDI PrecisionBook laptop, which was running the Hyper-G Harmony client. The Indy was the first SGI workstation I ever personally touched. I don't have the original IndyCam grab anymore, just this cropped picture, but here I am photographed using one of the Indys as an undergraduate at the Salk Institute circa 1995-ish:
Ostensibly they were there for X-ray crystallography rendering but they also played a lot of
sgidoom
. It didn't help my envy that the lower-end Indys were almost kinda
vaguely
affordable for a college student, criminal sidehustles or unsavoury loan terms notwithstanding. Though I never did buy one in college, this Indy I picked up later came with the Indybag to tote it in.
The SGI Indy makes a good segue into the Indigo2 — as I'll render it for the remainder of this article — because they have many similarities in their architecture since the Indy is in large part descended from it. In fact, the lowest-binned Indigo 2 systems, with a hardware IP ("Inhouse Processor") identifier of IP22, look the same as the Indy (IP24) to system software which also reports it out as an IP22. The Indy's more limited processor and graphics options, undoubtedly for purposes of market distinction, led to the common joke that the Indy was "an Indigo without the 'go'." While this Indy has 24-bit XL 2-D graphics and a 150MHz R4400SC (i.e., with L2 cache), a processor second only to the higher-tiered R4400s and R5000, all but the most anaemic contemporary configurations of the Indigo2 would have outclassed it.
The first Indigo 2 systems, in a teal case which also wasn't indigo, emerged in January 1993 and made up the IP22 family based on R4000-series CPUs, maxxing out in 1995 with the 250MHz R4400SC sporting 2MB of L2 cache. The launch configuration with a 100MHz R4000 would set you back about $35,000, an eye-watering $78,000+ in 2025 dollars. Initially the IP22 family shipped with Extreme graphics (codenamed "Ultra"), a three-card 24-bit 2D/3D rendering system that was roughly a doubled-up Elan ("Express" graphics) from the original Indigo with twice the Geometry Engines and Raster Engines (eight GE7 and two RE3.1 units respectively). Because the teal Indigo2s have only four card slots, the Extreme graphics board set ended up occupying most of them. Each slot has an EISA connector but only three of them also have GIO64 connectors for SGI's high-speed bus interconnect, and two of those are actually shared.
In mid-1993 additional lower-tier options were offered: "Newport" graphics, sold as the XL for speedy 2-D graphics but no 3-D, and two options both called XZ for cheaper 3-D, one identical to the Indigo Elan (four GEs, one RE) and one with half the GEs (two). The advantage of these lower-tier options, besides cost, was getting some card slots back if you didn't need Extreme-level acceleration. The four-GE XZ and the XL were also sold for the Indy, which came out around the same time, along with an even cheaper 8-bit-depth XL card for entry-level Indys.
The Indigo2 jumped a processor generation in October 1994 when SGI announced the POWER Indigo². This family (IP26) incorporated the R8000 from the high-end POWER Onyx, which was the first MIPS IV processor (the R4000 was the first MIPS III) and explicitly designed around floating point performance such that its codename was "TFP" for "Tremendous Floating-Point." Despite the moniker, however, the R8010 FPU was in fact a separate chip decoupled from the main CPU with a queue allowing for limited out-of-order execution of mixed FP and integer instructions. The R8000 itself was strictly in-order yet a superscalar design issuing up to four instructions per cycle on a five-stage integer pipeline (although also highly pipelined the R4000 and R4400 are merely scalar CPUs; by contrast the R4600 mostly did away with pipelining its FPU, which made a relatively weak core even worse). The main R8000 CPU has conventional on-die L1 caches plus external L2 cache. Interestingly, the L2 cache is all but obligatory because it ends up shared with the R8010 which uses it as
L1
. These are serviced by two separate identical "tag RAMs" containing the cache tags, and the external cache has its own five-stage pipeline.
The entire amalgamation made for a complex chipset to design, taking years of development time, and to the chagrin of MIPS management its release date slipped from 1993 when it might even have been a plausible Indigo2 launch configuration. By this point SGI had acquired MIPS Computer Systems as its subsidiary MIPS Technologies, Inc. (MTI) and made the R8000's completion an engineering priority. It was just as expensive to fabricate — Toshiba produced the R8000 and R8010 at 0.7μm, totaling over 3.4 million transistors between the two — and after the POWER Onyx launched in July 1994 the 75MHz POWER Indigo2 finally emerged in October for a cool $46,000 (over $105,000 in 2025 simoleons) with 2MB L2 cache, XZ graphics, 64MB of RAM, a 2GB SCSI disk, monitor, keyboard and mouse. Compare that to the 200MHz R4400SC configuration introduced at the same time with 24-bit XL graphics, 32MB of RAM, 1GB disk, monitor, keyboard and mouse for "just" $24,500 — you paid a lot for
the special little front case badge
these rather rare systems sported. And if you had to ask how much a POWER Onyx was, well, you couldn't afford it.
Meanwhile, the GE7 Geometry Engine's transform performance started to become a liability as CPUs increased in speed and could compute them faster, and the presently available Indigo 2 options lacked any support for hardware texture mapping. Indeed, texel-capable SGI graphics hardware had existed for at least several years, first on SGI's earlier Crimson systems using PowerVision VGX graphics, but it had yet to be deployed in any workstation. As a new faster graphics option for the Indigo2 SGI started with the GE10 from the Onyx's RealityEngine² and cranked up the new GE11 to 960,000 MFLOPs (compare to the eight GE7s in the Extreme that
together
produced about 256,000), and paired it with a new faster RE4 raster engine. For the upper-binned configurations, they also added a texture engine option with its own RAM ("TRAM"), and the highest of the three configurations had an extra GE11, RE4 and pixel processor for blending, depth and dithering. SGI called this new architecture IMPACT.
SGI made the case purple (still not indigo) for the IMPACT family, putting a special silver "IMPACT" badge on the front as shown in this 1995 ad I joined by hand from two magazine page scans. It was also somewhat internally different: to accommodate IMPACT graphics' greater power and bus demands, SGI reversed the four card slots' loadout so that there were only three EISA card connectors but
four
GIO64 ones (though still only two logical slots), and added individual supplemental power connectors to each. These in turn were backed by a beefier 385W power supply. A variation called "IMPACT Ready" had all the system upgrades but no IMPACT card, which could be bought separately and added later (the original graphics options would still mostly work).
Although the first Indigo2 IMPACTs were announced in July 1995, a conspicuous absence among them was an R8000 configuration: the systems weren't offered with one. While SGI had drivers for it internally, the company had quietly concluded the R8K was an engineering dead-end. Its design made it difficult to evolve and it ultimately topped out at just 90MHz (and the Indigo2 only had the 75MHz part); on top of that, it ran hot and power-hungry, pulling 13W at 75MHz while the R4400 could pull as little as eight watts at 200MHz, and Toshiba couldn't seem to make it any cheaper. Similarly, although it generally achieved the floating point dominance it was designed to, its integer performance improvements proved more modest and it was difficult for programmers to squeeze out optimum throughput.
SGI instead put MTI on finishing the processor generation after it. As far back as 1991 MIPS Computer Systems had been developing specifications for a "next-generation" RISC part which it grandiosely called the R10000 and planned to release in 1994. Codenamed "T5," MIPS prevailed upon its usual partners to contribute to its development, eventually receiving a reported $150 million in investments. The R10000's development was somewhat slowed by the R8000, causing SGI/MTI to fund Quantum Effect Design's R5000 in the meantime for their low end hardware (our
Cobalt RaQ 2
uses a later derivative, and an R5000 option was offered for the Indy, though never for the Indigo2). Although announced in July 1995 in 175MHz and 195MHz speeds, significant production problems delayed its release until March 1996 for SGI's high-end servers and the NEC-fabbed ones had to be recalled in July because of unexpected shutdowns.
During the estimated $10 million recall for the faulty R10Ks, SGI finally introduced the chip (presumably fixed) to the Indigo2 IMPACT line as the IP28 at both the 175MHz and 195MHz speeds. (I'll talk more about the R10K when we get to the CPU module.) These last and mightiest IMPACT systems got their own silver badge that read "IMPACT 10000" — which brings us to our system today.
This machine here is actually the last variant of the IMPACT 10Ks, with Solid IMPACT graphics. Recall I mentioned three bins for IMPACT. As introduced initially SGI produced a High IMPACT R10000 system for $43,000 ($88,500 in 2025 dollars) which was the middle tier with texture mapping, and a Maximum IMPACT system for $55,000 ($113,300) with texture mapping and the extra rendering hardware. Solid IMPACT systems lack texture mapping and, as the lowest tier, were introduced shortly afterwards as a cheaper option (around $34,000 or in 2025 $70,000). Finally, an even less expensive variation called Killer IMPACT was also offered, which was nothing more than Solid IMPACT paired with the lesser 175MHz R10K and thus arguably unworthy of the name. There weren't many of these as the later Octane and O2 systems were more popular by then, but this is actually one of them that has been secondarily upgraded, and I'll show you that in a minute.
I should also mention that this thing weighs a ton (or more accurately a bit over 40 pounds) and was a real adventure dragging it out to the staging area.
There were a couple other minor variations on the Indigo2 that we won't talk further about here, though I mention them for reference. Like the Challenge S, which was a modified headless Indy used as a cheaper rackmount, there was a headless teal Challenge M with no graphics option (though one can be installed, making it a regular Indigo2). This variation was rebadged by Control Data Corporation and Siemens Nixdorf but is the same machine otherwise. The case was also used for the Challenge M Vault, an overgrown SCSI enclosure that added another 5.25" bay and two 3.5" bays, and repurposed the expansion card cage for four more 3.5" drives. Obviously the Vault isn't actually a workstation and I've never seen one myself.
Gratuitous shots of the case badges. SGI certainly made some physically striking systems. The "10000" on the case badge got a little banged-up prior to my acquisition but the whole setup still looks awfully cool.
The rear didn't clean up particularly well, but it's still instructive. There is only one card in the slots, the Solid IMPACT card itself, because pretty much everything else essential is on-board. It has a 13W3 video port, though this type of port never got a standardized pinout and only video cables and converters wired for SGI graphics will work properly with it (naturally I have some in stock). We'll have more to say about video output later on. The DE-9 next to it is for an active-shutter 3-D stereo viewer, which excites me as a 3-D enthusiast, though sadly I don't have anything that works with it right now.
Below that on either side are the external 50-pin SCSI port and the audio connectors for microphone, line in, line out, headphones, and serial digital stereo. This is what used to be called IEC958 and is now called IEC 60958, better known nowadays in its consumer-grade form as S/PDIF. The connection here transmits and receives AES3 (AES/BDU) stereo PCM audio over an unbalanced line at sampling rates up to 48kHz. All the jacks are 1/8" (3.5mm) TRS.
The other ports are two PS/2 ports for keyboard and mouse (a regular PC keyboard and mouse will do), two MiniDIN-8 serial ports (classic Mac serial port cables work), the AUI Ethernet connector and 25-pin IEEE-1284 parallel port, and at the base a 10BaseT Ethernet port. The AUI and 10bT connectors are the same NIC, and if both are connected then only the 10bT port is active. Additional NICs could be installed in the EISA slots with appropriate drivers. The manual cautions you not to "throw the mouse at co-workers."
This unit appears to have been upgraded aftermarket: the model number CMNB007AF175 corresponds to the 175MHz variant, and a 175MHz R10K plus Solid IMPACT graphics would be a Killer IMPACT system. However, it's actually got a 195MHz CPU module and I'll prove that when we bring the machine up. Machines that SGI upgraded or refurbished in-house have additional stickers on the Indigo² plate and the model number plate, though this one has neither, so it must have been added after the fact.
The copper coverplate is a bit of a mystery, but may have been intended for a ISDN port or something similar like the Indy's and was simply never populated on this board.
Finally, the power supply. These don't have a great reputation but are not trivially replaceable by an AT or ATX substitute, and it was one of the two components I was most expecting to have failed. It's possible to
replace their capacitors
if necessary but doing so involves several caps on the high-voltage side, which could be risky or dangerous depending on your skill set. (Mine sucks.)
To get to the other component I was pretty sure
had
failed, we need to get to the logic board now. The front door opens down, or it would if one of the hinges weren't broken, to reveal a 5.25" bay occupied by a(n apparent) CD-ROM caddy-fed drive and then a black 3.5" bay.  Next to the 5.25" bay is the master power button and a smaller reset button. At the top are two clips which we pull down.
These clips enable removing the entire front bezel, revealing not only the 5.25" bay but actually
two
hard disks. They are all on their own benighted little custom sleds that we'll have to do battle with later. For now, we slide their restraining clips to the left and pull the sleds from the system.
The hard disks and the optical drive do not appear to have been factory-issue either. (Note from the future: they weren't.) Notice the alignment prongs and the oversized rear connector which carries not only the SCSI bus, but also SCSI ID and power lines. SGI offered a DAT option which went in the top 3.5" bay, and there were also SCSI 3.5" floppy and QIC 5.25" options.
We then turn it horizontal and remove the feetsies, or what SGI staidly calls "workstation stands." These were 3D printed by someone on Nekochan (RIP) and while the colour doesn't quite match, they're reasonably robust and look a lot better than the scuffed-up O.G. ones you might pay a mint for on eBay. I got them a while ago when I still had immediate plans for this thing and they've been with it ever since. The feetsies are important because the side slats' vents must remain unobstructed when vertical, especially if you have one of the bigger video options.
With the bezel off and everything out, we can just undo its moorings and lift the top case up, which rotates back on little clips in the rear until it comes off. Keep that in the back of your head for when we reassemble it.
The naked chassis. You can see the card cage and riser (and cooling fan), the drive bays connected by a big stiff ribbon, the power supply, and (peeping out in the top middle section) a small portion of the logic board.
This was all very dusty, so the canned air came out at this point to clear away the bunnies and debris.
To expose more of the logic board we'll need to remove the 5.25" tray first. This is secured by two captive screws in front.
It then simply slides back out of its retaining clips and can be flipped over to the side (it isn't necessary to remove the flat connecting cable).
With the tray out of the way we now see the main CPU module and RAM SIMM slots. Let's talk a little more about the R10K.
The R10000 was MTI's first out-of-order core. The chip has a seven-stage pipeline and fetches four instructions every cycle from the I-cache for decoding. These (except for NOPs and jumps) in turn feed three instruction queues for integer, FP and address operations, each of which can accept up to four instructions themselves, which dispatch reordered operations to two integer (add/shift/move or multiply/divide), two FP (add or multiply/move) and one load/store execution unit. Up to 32 instructions can be in-flight. Each execution unit maintains its own multi-stage pipeline, except for high-latency division and square root units that hang off the FP multiplier, with integer instructions having the lowest latency. The address queue is uniquely a circular FIFO so that instruction order is preserved for tracking dependencies and maintaining sequential-memory consistency. Instruction reordering is assisted by 64-register rename files for both GPRs and FPRs, alongside a separate condition file recording in parallel if the result was non-zero so that conditional move instructions need only test a single bit instead of the whole register.
The R10K implements a 64-entry translation lookaside buffer and is also capable of speculative execution, predicting branches using a 512-entry history table and saving state in a four-entry branch stack. Unusually for such a design, it does not predict branch
targets
, relying on its out-of-order core to do useful work during the additional cycle required to compute them (a problem with branch-heavy code that could not be easily parallelized). It carried 32K of L1 instruction cache and two interleaved 16K L1 data caches, plus supporting L2 cache (called the "data streaming cache") anywhere from 512K to 16MB, and could be set up for "glueless" SMP out of the box with up to three other CPUs — or, with custom hardware, potentially hundreds. The CPU implements the Avalanche bus, a muxed 64-bit bus which directly interfaces with the L2, apparently unrelated to an earlier experimental bus for the PA-7100. In theory SGI Avalanche could run at CPU speed, but in practice its overhead limited it to 100MHz in uniprocessor configurations and 80MHz under SMP, or around 540 MB/s. While this was reportedly enough to keep a 4-CPU system fed, it paled in comparison to wider non-multiplexed buses like the PowerPC 620 which could maintain roughly twice the bandwidth.
Although the first iteration was intended to run up to 200MHz, poor yields caused problems above 180MHz and it was introduced at the slightly slower maximum speed of 195MHz as shown here. Despite being a third source for the R4400 IDT chose not to produce the R10000, so it was fabricated by NEC and Toshiba on a 350nm process with 6.8 million transistors and a die area of 298 square millimetres. NEC-fabbed units initially drew so much power that they caused unexpected system shutdowns and forced SGI into that very expensive recall I mentioned earlier. The R10K eventually reached 250MHz in 1997 with a process shrink to 250nm, though this wasn't ever offered for the Indigo2.
The R10000 turned out to be a far more significant microarchitectural landmark than SGI had intended. We'll come back to this when we finish the story at the end.
The chip speed is confirmed by the part number, a PMT5 030-0966-004 indicating an R10000 (technically an R10000SC) with 1MB of L2 cache. This chip runs rather hot as the huge heatsink and active cooling fan would indicate.
The part I was pretty sure was dead is (surprise surprise) a Dallas DS1286 timekeeper chip (top left/northwest corner). Dallas timekeepers have built-in batteries and last a fairly long time, but eventually crap out and are notoriously not intended to be user-refurbished. Despite the name they do other things as well such as provide a watchdog timer and a small amount of battery-backed "NVRAM."
The death of a timekeeper in an SGI has various effects depending on the machine. In most cases this just affects the clock, as is the case with my battery-munching Fuel, though at least in the Fuel's case the battery is external and can be replaced. However, in machines like the Indy, things like the on-board Ethernet MAC address are kept there as well and the network hardware won't function until the chip is refurbished and reprogrammed. It should be noted that the "NVRAM" in these things is nowhere near large enough to maintain the PROM environment variables; that is stored elsewhere.
Because this machine is related to the Indy I decided better safe than sorry (note from the future: it fortunately appears at least the IP28 Indigo2 doesn't keep the MAC address or any other vital system data in the DS1286 either). Unfortunately we can't just remove it because the riser card for the slots is in the way, so we'll need to get that free. At this point I removed the stiff blue power supply connector from the riser card, which also grants easier access to the 72-pin SIMM RAM slots.
RAM is installed in three groups of four identical SIMMs each. The spec is parity FPM — EDO reportedly doesn't work — 60ns or faster. This machine came with only the default 64MB of RAM (as four 16MB SIMMs), which isn't great, so I found someone selling a four-pack of 32MB SIMMs of the same spec with the plan to order it if we get this machine to power up.
Officially the IP26 and IP28 boards only accept up to 640MB of RAM, limited to eight 64MB SIMMs because of heat concerns. It turns out this isn't actually a problem with most SIMMs and virtually any IP28 can accept 768MB (all 64MB SIMMs) just fine. The little IP22 is limited to 32MB SIMMs, however, and thus 384MB of RAM. The situation is more complicated with the IP26 as the R8000 CPU card encroaches on some of the RAM slots, necessitating "low profile" SIMMs, and there is also some question over SGI's insistence that installing any 64MB SIMM will require at least one bank to consist of all 32MB SIMMs.
It is possible, at some expense, to cram 1GB of RAM into an IP28 using 128MB "32x36" parity SIMMs. The memory controller is hard-limited to 1GB, however, so you could only populate two of the banks this way to yield 1024MB from eight 128MB SIMMs. Here's a
more thorough explanation
.
To get the riser card up we'll need to take the Solid IMPACT card out. This is a single card, so it's a little bit less of a hassle than the stacked multicard graphics options. The card cage has a door which you can simply pull down on to open.
The Solid IMPACT card connects only to the GIO64 bus and the supplemental power connector (the EISA connector for that slot is open). Those huge heat sinks again should say something about how much work this card ends up doing.
The card is identified as an 030-0786-004.
Although I don't know for sure which is which, my guess is that the two chips labeled SGI/ISD 099-9028-001 ("V101 REVA") are the twin PP1 pixel processors that handle blending, depth and dithering, since they're next to the video output, and the chip labeled ADV7162KS170 is the single HQ3 command processor. The larger square of the two heat sinks would then most likely be for the GE11 Geometry Engine (because it has the most gates of any of the chips) and the smaller rectangular one for the RE4 Raster Engine and the SDRAM framebuffer.
The cards are securely held not only by the card edge and the usual screw in the slot, but also by this retention pin which slots down in front of the card edge by the door.
The video card can now be pulled out (there are handy loops if you like) and set aside.
Now to pull up the riser card. This is secured in several places, so we'll start with the screw in the back.
Unfortunately this screw was pretty badly stripped. I'm not sure if someone had tried to do some other upgrade on this machine and mucked it up, but either way no screwdriver could turn it, so I grabbed a pair of pliers and cranked it off.
I also don't know who J. R. Vala is, but if you wanted his attention, this is the riser card for you.
Next we undo a little brass-coloured screw at the bottom which secures the riser card to the logic board.
Now we can pull the riser card up out of its connectors (but gently so as not to bend anything).
We don't need to yank it up all the way to get the timekeeper out, but if you did want to remove it, you'll want to remove the twisted black-and-yellow cable as well as the stiff flat blue cable.
Now we can grab that chip, which is conveniently socketed.
Expecting I would have to do this at some point, I had already pre-purchased
a repair board for the DS1286
that you could simply wrap the needed pins around to provide a proper battery holder. However, it should have been a tip-off to me that the repair board has a crystal on it, because the DS1286 has a crystal too. (I am not complaining: I bought a replacement
DS1386 module for my Indy
from the same seller and that has worked very well.)
There seem to be some DS1286s that
lack the crystal and battery
, which would actually make them more like a DS1284. Those chips (and the DS1284 generally) can be very easily converted with this board. However, as you can see here, the DS1286 in this machine already has those pins yanked back. Undoubtedly it was made out of a DS1284 with the battery and crystal epoxied onto the top in a similar fashion.
Because it was shot anyway I got out the Dremel and decided to see how far I could shave it down. Unfortunately the entire top chamber is epoxy; you can't just cut into it or dig out chunks.
I did grind down to the battery and what I thought was the crystal, but in the end all I ended up doing at that point was just making a mess, nor did I find any obvious metal portions I could solder the conversion board to. But it was only $10, so live and learn.
I dithered over buying a DS1284 to retrofit but the problem with buying ICs on eBay is getting re-marked crap or chips that are absolutely fraudulent. However, while looking at chips from dodgy international sellers I ran across an individual producing
a small board for the Tektronix TDS524A digital scope
, which also uses the DS1286. This board has a little replaceable coin cell on it plus a DS1284Q and crystal. More to the point it also has pads on top, so an alternative battery pack can be fitted.
Although it is twice as big as the original DS1284 (in area, anyway), it still fits.
Before installing it I soldered a 2AA battery holder to the battery pads so that when the lithium battery it came with craps out eventually, I can just put in lithium AAs (don't put alkaline in this, they'll leak) and not have to go through this whole disassembly again.
Sheathing it with electrical tape to ensure the upper pins and the battery pack won't short, it fits neatly in the socket.
At this point we should now make sure we can power on the system, so I put back down the riser card (leaving out the stripped rear screw) and reinstalled the video card and retention pin.
Although the machine will bring up a console on the serial ports, I also wanted to know if the video card is working, so I got out an SGI-wired 13W3 to VGA converter and connected one of my utility LCD panels. I then plugged it into the wall, crossed my fingers and pressed the power button.
To my delight the machine did indeed power up and make its little happy jingle chord! However, nothing appeared on the screen and the Indigo2's LED stayed amber, suggesting the video card was unhappy about something.
The "something" in this case was probably the monitor. One thing that 13W3-based video cards
do
have in common is that they're all sync-on-green, which is to say that the horizontal and vertical sync signals are mixed in with the green channel. Many monitors nowadays, including this particular ViewSonic LCD panel, don't understand sync-on-green anymore and won't be able to sync. Conversely, as an unusual case, I have a NEC multisync CRT monitor that does sync to such a signal, but still displays the green anyway, giving it the wrong colour.
There is a more definitive solution for this problem and we will address it later on, but fortunately it turned out my INOGENI USB VGA capture box
does
understand sync-on-green, and the PROM monitor display rate is 60Hz which the INOGENI will accept. For the time being, the M1 MacBook Air and VLC can thus serve as the monitor (and we can also take screen grabs).
With the Mac connected I reset the Indigo2, and this time the SGI's LED turned back to green and we got a picture. The picture said the machine was unbootable, though we already knew that because we pulled the drives out. I powered it off and plugged in a PS/2 keyboard and mouse. Normally you shouldn't operate the machine with the case off because it can't run its airflow normally, but there is sufficient ventilation here even though you can certainly feel the heat from the CPU module.
I then secured the battery holder to the metal back of the riser card with some Velcro. It fit perfectly.
With the battery holder in place and the timekeeper now working again, I installed the hard disks and the optical drive, and powered it on with the capture box connected. Now that I knew the machine was working, I went ahead and ordered the extra RAM, but we have other tasks to complete in the meantime. Let's switch to the screen grabs, which have been cropped and corrected for aspect ratio.
One of the things that made SGI MIPS (and its early PC hardware, but more on that later) interesting was the graphical boot PROMs. These are based on the Advanced RISC Compouting (ARC) specification modified for SGI's usage ("ARCS"). ARC came out of the Advanced Computing Environment (ACE) consortium originally founded by Compaq, Microsoft, MIPS (pre-acquisition), DEC and SCO in 1991, later joined by SGI, Control Data Corporation, Prime Computer, Zenith and others. Notably absent were Sun Microsystems, Hewlett-Packard and IBM, who never participated — nor Intel.
At this time in the industry RISC was believed to be the future — but so was Windows NT, or what was then referred to as OS/2 3.0 or "Portable OS/2," due to its planned wide portability and the existing software it supported. ACE concentrated on 32-bit x86 using conventional BIOS (due to Compaq's influence) and near-future RISC workstations using ARC; they identified two platforms, namely SCO UNIX and the future Windows NT, that would run on both. MIPS was heavily touted as the architecture for these workstations, both from SGI and MIPS' presence, and the absence of anyone else more powerful to say otherwise.
Within a year, however, ACE rapidly degenerated into squabble and collapsed: market appetite for the alternative ARC workstation didn't develop as planned, and SGI buying MIPS was the last straw for some participants who saw the purchase as SGI trying to corner the architecture. DEC, which was already working on what would become Alpha anyway, de-emphasized its MIPS offerings as a result and eventually got out of the business altogether. Intel, for its part, accelerated development on Pentium in response and made non-x86 alternatives comparatively even less desirable. Although ARC foundered, and no computer was ever fully compliant with its specification, it maintained a long-standing legacy presence in Windows NT which still specified it for boot devices until Windows Vista. Likewise, the RISC systems that
could
boot Windows NT generally used an ARC console to do so, even ones that weren't MIPS-based like various Alpha-based workstations in the form of AlphaBIOS, and some RS/6000s.
No SGI MIPS hardware ever booted NT natively, though through the influence of ACE where MIPS was supposed to reign supreme these boot PROMs implement ARC too, at least in their own fashion. But what makes them most outstanding to modern users is that they have a full mouse-based GUI congruent with IRIX and the ability to do some basic tasks built-in.
Messages appear as well-rendered dialogue boxes, sometimes extracted from console output and highlighted to the user. If you clicked the Stop For Maintenance button (or pressed Escape) you would enter the main menu right here before starting the OS.
Other output appeared in a text window where additional detail was required. However, our disks still don't boot and the message doesn't tell us why, so we proceed to the PROM menu.
The System Maintenance menu has six options accessible by button clicks or the numbers 1-6. Using the keyboard is particularly handy when your mouse doesn't work or if, as in our circumstance, you're struggling with screen lag due to the capture box. The most immediately useful is the Command Monitor, so we press 5.
This pops up in a new window. (That also means there was no password on the PROM. If one was set, and we don't know what it is, removing a jumper on the board under the CPU card will allow you to reset it.)
We first list our
hinv
, the hardware inventory, using the
-v
option for verbose output. This reports we have an IP28, 64MB of RAM, a 195MHz R10K and Solid IMPACT graphics, as expected. The Iris Audio Processor is the standard onboard audio codec used in many SGI-MIPS systems.
The environment (
printenv
) didn't look too interesting other than its apparently residual IP address, but the MAC address did appear and seemed valid, so we shouldn't need to worry about that like we would with an Indy. Nevertheless, just in case anything was corrupted, I did a
resetenv
at this point to force defaults.
With the default environment I tried to boot again, and this time got a marginally more useful message:
Boot file not found on device: scsi(0)disk(1)rdisk(0)partition(8)/sash
. This is an ARC path and should be fairly self-explanatory (basically SCSI bus 0, i.e., the internal bus, ID 1, LUN 0, partition 8). This partition is where the standalone shell should be found to bring up the IRIX kernel but it's not finding it.
hinv -t
will show you the device tree. Most of it makes sense, but when we get to the internal SCSI bus (starting with
adapter SCSI WD33C93B key 0
, a Western Digital Fast SCSI-2 controller) it gets very weird. Note as background that the controller in SGI hardware has ID 0 (not 7 like, say, Macintoshes), so connected devices start at ID 1. One of the hard disks is indeed at ID 1 — and then the other one is sprayed over every other ID.
I also didn't see the optical drive anywhere in that list. Given that one of the hard disks got an ID despite the other one going nuts, this device should have gotten one also. Nevertheless, I decided to grab one of my caddies, stick an IRIX Tools CD in it and see if I could bring up a miniroot. This disc in particular is known good and readable by the Indy. The drive accepted the caddy and seemed to be fine with the disc ...
... but trying to bring up the miniroot from it (using the PROM menu install option) showed no bootable devices.
I shut down the system and pulled out all the devices again, then had a look at the optical drive specifically. The sleds carry power, SCSI and SCSI ID lines. It looked like it was hooked up correctly but it was strange to see a La Cie sticker on it. That sounded like a Mac drive which had been repurposed.
Extracting it from the sled, the drive revealed itself as a Sony CDU948S. I noticed that there was no parity jumper, and indeed the manual seems to indicate that parity can't even be enabled on this drive, which would make it unbootable. I imagine the prior owner simply went with what he had available. We'll replace that now.
On the shelf I had some old Toshiba XM-5401B SCSI CD-ROMs which I had purchased for another project long since forgotten. These are highly compatible and will generally boot just about anything, assuming they're working, which the first one wasn't (wouldn't eject its tray without a lot of force). I tried the second one.
While you don't need to connect the SCSI ID cable and can assign IDs manually, it's easier to let the machine do it. On this drive the SCSI ID cable goes on in this orientation. I installed the new old CD-ROM drive alone and booted the system back into the command monitor.
hinv -t
shows the drive, on ID 1, and no more drives-all-over-the-place nonsense. This also means the SCSI controller wasn't likely at fault.
And the installer option sees it too, and will offer to boot from it, but, uh ...
... um, the CD's already in there ...
... so both drives are bad.
The only other internal SCSI CD-ROM I had at hand was a Nakamichi CD changer, but that seemed like a waste, so I scrounged around in the server room for alternatives. In the stack of parts for the Fuel I found a spare factory-issue SCSI DVD-ROM (Toshiba SD-M1711). I knew this was bootable in the Fuel, so it probably would also be bootable here.
I got it the ID cable upside down the first time, but the second time it went on cleanly and got assigned an ID.
In the Command Monitor it showed as ID 6 and was recognized as a CD-ROM. To make sure of what I was dealing with, I ran
hinv
this time with
-t -p
to give me ARC paths, showing the full ARC path for the device would be
scsi(0)cdrom(6)
— there is shorthand for this, I promise. I then tried to bring up the standalone shell from the tools CD with
boot -f scsi(0)cdrom(6)partition(8)/sash64
and this time it worked! The Sony drive went on the parts shelf for another system to use some other time.
That took care of the optical drive, so I next looked at the IBM drive that had been spamming the SCSI bus (the one in the top bay).
The problem was obvious: the ID cable wasn't connected, so my best guess is the hard disk thought it was ID 0 and promptly clashed with the controller. In fact, the cable wasn't anywhere near long enough to have even reached the drive's ID pins — which also meant it couldn't possibly have been bootable either. I ejected its tray and turned my attention to the second drive.
With the drive installed by itself, it comes up once again as ID 1, so I put the DVD-ROM back in and decided to try system recovery to see what might be on it.
The optical drive is recognised and we insert the CD.
And, immediately, the PROM starts copying the installation tools to disk. This is notable: that means the hard disk has something the PROM recognizes as a swap partition, where the miniroot lives during system recovery operations.
The crash recovery kernel successfully starts within the console and asks for the machine's hostname. As it happens I've already picked a name for the Indigo2, and it is ...
purplehaze
. Catchy, no?
This is what I meant by the PROM monitor intercepting certain strings on the console. Because I reset the environment way back when, it now has a
192.168.1.2/24
address which the kernel treats as unconfigured. This is a string the kernel simply emits, but as the PROM monitor services the console, it sees it arrive and promotes it to a dialogue box instead.
There isn't really anything to restore from, so I forced it into a shell at this point.
The fuller
hinv
available from an IRIX shell prompt shows everything we expect it to, and the miniroot's
/dev
shows that the remaining hard disk has partitions at 0, 1, 6, 7 and 15. This might suggest the disk was formatted XFS at some point, since 0 would be the root, 1 would be swap, 6 would be
/usr
, 7 would be the whole thing minus the partition volume header in 8, and 15 would be the XFS log. I didn't see a partition 10, but that could be an artifact of how the disk was imported by crash recovery. However, there was no partition 8 for the standalone shell and other tools at all.
The miniroot also didn't want to mount partition 0 as either XFS or EFS. There is a small chance this was due to an incompatible way the partition filesystem was made, but the Tools version here is 6.5.9 and should be recent enough to understand XFS version 2 directories. The most likely conclusion is that the disk was partitioned but no filesystems were actually created, which means this machine was never actually bootable when I received it.
That's no problem — we'll just start fresh. And, since we're going to have to install IRIX from scratch anyway, let's do it on solid state.
There are only two sleds, and since the second drive we were using could actually be installed and enumerated (just not mounted), I decided to take the sled from the first drive that had no working ID cable. We'll then replace it with a ZuluSCSI.
The particular ZuluSCSI I selected has a bottom plastic carrier that I attached the sled to.
Unfortunately the clip on these things is spring-loaded and said spring is not secured particularly well, which ended up getting loose while I tried to adjust the sled's position in the drive bay. This required taking the carrier off again to rethread it.
Leftover was a couple of prop bars which I didn't need to mount the ZuluSCSI, so those will be put in the junk drawer in case they're useful for something else.
To cable it, however, we'll need an extension: the sled's connector is meant for a hard disk extending all the way back and can't be pulled further without damaging it.
Happily, I found a little SCSI extender of the right size in the box of tricks and a Molex-to-Berg power connector. The last step was to create a big 18GB empty image on the 32GB SD card as our IRIX volume (something like
dd if=/dev/zero of=HD1.img bs=1024 count=18874368
will do). We can't install the SCSI ID cable on the ZuluSCSI, but we know that the emulated disk can come up safely as device 1, so we'll tag the disk image as such.
With the ZuluSCSI's sled installed in the top bay, we obligingly see the lights of both the DVD-ROM and the ZuluSCSI flash as we power on the system ...
... and both devices are visible in the device tree in
hinv -t -p
.
If we were still working with the second partitioned disk we could simply start the installer at this point, but the disk image on the ZuluSCSI isn't partitioned yet. This requires manually bringing up the
fx
partitioner from the CD. To save my fingers I used the ARC shorthand for the device paths: instead of
scsi(0)cdrom(6)partition(8)
we can just say
dksc(0,6,8)
, and likewise for
scsi(0)cdrom(6)partition(7)
, making the boot command from the Command Monitor
boot -f dksc(0,6,8)/sash64 dksc(0,6,7)/stand/fx.64 --x
(the
--x
option starts expert mode). The partitioner duly starts from disc.
We accept the defaults, which would be
dksc(0,1,0)
for the image on the ZuluSCSI.
fx
immediately determines the image is unpartitioned and sets up a default configuration.
We'll then label the disk. We really just need it to create the
sgiinfo
portion (used for administrative purposes) but no harm in having it do the rest again. This is almost instantaneous.
From the label menu don't forget to sync it to disk to ensure the new disk label is written, which I almost did (!), after which you can exit.
Back in the PROM menu, we'll proceed with the IRIX installer.
IRIX, the primary Unix for SGI-MIPS, originated on their first MIPS systems, the SGI IRIS 4D (thus the name, derived from "IRIS UNIX," and not actually an acronym). Prior 68K systems ran "GL2," based on UniSoft's port of UNIX System V; IRIX is a true Unix as well, likewise descended originally from UNIX System V, though it wasn't actually badged as IRIX until 3.0 in 1988 which corresponded to SVR3 with components from 4.3BSD. This "first" release implemented a distinctive window manager called 4Sight designed to resemble their prior "multiple exposure" (
mex
) interface. Unfortunately for SGI 4Sight was implemented with Sun NeWS and NeWS lost to X11, so IRIX 4.0 switched to X11R4 and the similar Motif-based 4Dwm window manager, which ultimately became IRIX's most lasting visual signature. When people talk about using IRIX, most of the time they're really talking about 4Dwm, a notable contrast against other proprietary Unices which largely used the
HP VUE-derived
CDE.
IRIX 6.0 made the jump to 64-bit, and 6.5 was the last major version, based on SVR4 and released in 1998. SGI cut off support for earlier machines like the Indy and this Indigo2 at 6.5.22, which is the version we will install, and subsequently locked versions up to 6.5.30 behind a support contract requirement. 6.5.30 was the last official release of IRIX in August 2006, which still supports later machines like the Fuel, and thus the Fuel system here runs that instead. SGI has never ported IRIX to any other platform nor made IRIX open source, nor is the company's current incarnation likely to ever do so, though some portions of source code were officially made available such as the XFS file system (which yours truly uses for the boot volume in my Fedora Linux Raptor POWER9). Various clone window managers exist today that try to recapture the style and substance of 4Dwm on modern hardware, but they end up falling in the uncanny valley in various ways, and in the end there's still nothing like the original.
It is certainly possible to run other operating systems on SGI-MIPS, notably
NetBSD
up to IP32 and
hacked versions
of the
former OpenBSD port
, but I like IRIX too much to do that.
We now have a valid swap partition on the ZuluSCSI image, so we can actually start the installation miniroot this time.
Despite the new timekeeper our clock is a
little
off and we'll correct that from the NTP server when we get networking up, but we don't have a filesystem yet on the image, which the installer will now offer to create. (This step is what I suspect didn't happen with the second hard disk.)
Again, this is very fast on the ZuluSCSI, and we go right into the installer from there.
From-scratch IRIX installations of later versions involve a lot of disk swapping and overlays. This article is long enough already without me trying to do a comprehensive IRIX installation guide, and it would be fruitless anyway because there are so many permutations. However,
this install guide
is pretty good for most intents and purposes. There are also various means of doing the installation from a network server, but I don't have this set up, and I try not to do so many IRIX installs that it would become worth it to do so.
Here we'll load up the install sets ...
... marvel at the cutting-edge included applications like Java 1.4, Acrobat Reader 4.05b and Netscape Navigator 4.8a ...
... and, after resolving the inevitable conflicts between packages, finally start the installation. I did this all manually with CDs. In the future I might try just loading them all as ISOs on the ZuluSCSI as well.
A number of disc swaps later, we are "finished" ...
... except for having to re-quickstart all the ELF files that were just installed. Since this leaves us with a nice clean install of IRIX I could potentially use later, I powered the system off and backed up the disk image.
The new sticks of RAM had arrived, so I pulled the 5.25" tray one last time to install them.
This brings us to 192MB, but for some unexplained reason the system then put up the solid amber LED again when I tried to reboot. I got out a serial cable this time.
System Maintenance Menu

1) Start System
2) Install System Software
3) Run Diagnostics
4) Recover System
5) Enter Command Monitor

Option? 5
Command Monitor.  Type "exit" to return to the menu.
>> hinv
                   System: IP28
                Processor: 195 Mhz R10000, with FPU
     Primary I-cache size: 32 Kbytes
     Primary D-cache size: 32 Kbytes
     Secondary cache size: 1024 Kbytes
              Memory size: 192 Mbytes
                SCSI Disk: scsi(0)disk(1)
               SCSI CDROM: scsi(0)cdrom(6)
                    Audio: Iris Audio Processor: version A2 revision 1.1.0
For some horrible reason the Solid IMPACT card was suddenly not being seen. I decided to see what the diagnostics would say about that, since it was obviously just working and I hadn't messed with the graphics card or the riser. This can run from the new install of IRIX; we don't need the CD.
>> exit


System Maintenance Menu

1) Start System
2) Install System Software
3) Run Diagnostics
4) Recover System
5) Enter Command Monitor

Option? 3


                         Starting diagnostic program...

                       Press <Esc> to return to the menu.

              Checking for Distribution CD-ROM on scsi(0)cdrom(6).
dks0d6s8: Device not ready: Medium not present
dks0d6s8: drive is not ready

             Distribution CD-ROM not found.  Booting installed IDE.
SGI Version 6.5 IP28 IDE field  Oct  6, 2003

                   System: IP28
                Processor: 195 Mhz R10000, with FPU
     Primary I-cache size: 32 Kbytes
     Primary D-cache size: 32 Kbytes
     Secondary cache size: 1024 Kbytes
              Memory size: 192 Mbytes
                 Graphics: Solid Impact
                SCSI Disk: scsi(0)disk(1)
               SCSI CDROM: scsi(0)cdrom(6)
 
Testing Impact graphics.
Notice that when the diagnostics program started, it
did
see the board, and could drive it for testing.
The full diagnostics check took about a half hour to run, but in the end everything seemed fine ...
TEST RESULTS: 
CPU tests completed. 
FPU tests completed. 
Audio tests completed. 
SCSI tests completed. 
Impact graphics board tests completed. 
Diagnostics completed - press <Enter> to continue
... so I'm not sure what happened there. The system rebooted uneventfully and showed a proper green LED this time, though on the maiden boot of the operating system it switched to a non-60Hz mode the INOGENI didn't like and required me to hook up the Hall scan converter. These next few images are a bit fuzzy as a result. Sorry about that.
Yes, yes, we'll eventually fix the clock. Yes, yes, we'll eventually plug in the network.
Four default logins are created,
root
(duh),
demos
,
guest
and
EZsetup
. None of these have a password yet. Don't put this on an unprotected network exposed to the outside world, please.
I don't really need the easy setup, but for demonstration purposes here it is.
EZsetup's post-install wizard features four steps to greatness: security, networking (because nothing says security like networking), creating a non-root account, and customizing your work environment, which mostly means dumbing down 4Dwm and setting up Netscape.
Security, in this case, means creating passwords and setting permissions. This machine will spend the rest of its days with me only ever on the hardwired non-routable internal network, but this step is certinaly better than nothing for those of you who may not have the locked-down playground I have here for such machines.
After you've accomplished these trivial token tasks, you can quit, though the account remains available.
On our next boot the refresh rate issue sorted itself out and we come to the nice clean 4Dwm desktop of our new user account. I have more applications to install, but before we do that, we need to put its top case back on and find it a better place of lurkage than under that table.
Shutting IRIX down.
The top cover is reinstalled by fitting these rear plastic tabs into slots in the metal back panel and rotating it back down into position.
And, of course, they're old plastic, so they immediately tried to separate and snap off from the upper lid when I inserted them. Light-set high quality cyanoacrylate time.
Despite this, the top cover still wouldn't come all the way down onto its clips — it was getting stuck on the ZuluSCSI's plastic carrier, which needed to be pushed back a little. Of course, the minute I did that, the plastic clip on the drive sled snapped.
I got it glued back together but it had snapped at the very thinnest section, naturally, and the spring chose this moment to come loose again at the same time. After some screaming and infuriated reassembly the sled's clip was good for exactly one insertion before it snapped again in the same place, but only one insertion was required; the new position of the carrier allowed the top case to finally come down fully and lock. I'll deal with that if I ever have to take it out again, which comfortably should be never.
I also put back the second drive after disconnecting its power. I don't really have anywhere else to keep the sled and at least that drive is formatted and wired up, so it might as well stay there.
With the front bezel back on, we have a green LED and a clean boot into the system maintenance menu. It's time to assign it a home.
I found a nice cleared-out area where it could sit vertically next to
homer
,
the HP 9000/350 rack in the server room
, and dragged it on back.
As we won't be using the MacBook as its display anymore, we'll need to do something about the sync-on-green. Such boxes are not very common nowadays, but Software Integrators still sells brand-new active sync converters (
model #7053
) that filter out the sync signal from the green channel and turn it into composite sync which most monitors will recognize. I use one of them with my Indy and I keep a couple more in stock (not affiliated, just satisfied). They aren't cheap and they're active components that require their own power supply, but these boxes are probably the least expensive ones you'll find and they're still manufactured.
With the network up, files are obtained, and serious
sgidoom
and Mozilla 1.7 business ensues.
I was pleased to note that despite not having an external LED light to connect to, the internal activity LED of the ZuluSCSI can be easily seen through the bezel apertures with the front door down.
Shutting down. Now that I know the new RAM works, I think I'll fill up the other bank with an additional 128MB, plus I'm toying with tracking down a 10/100 Ethernet card for the EISA slots. It's stereo-capable, so I should figure out how that works, and of course if a High IMPACT or Max IMPACT card turns up at a decent price, I'd be a
Fuel
fool not to buy it. It's hotter and louder than the Indy, but it's a lot more powerful, and shouldn't everyone have a big purple time and money sink in their hobby? Plus, I got a powerful classic SGI system for free, and now that it's fully operational I really ought to make the most of it.
With our refurb complete, let's finish the story. The R10000 was only intended to be SGI's next processor architecture, but it ended up being their last. Originally, MIPS' market strategy was to create high-end chips and then shrink them, which it did successfully for the R3000 and R4000. However, that strategy fell apart with the R8000, and in the R10000 era MTI instead decided on tiered chips for multiple market points by continuing to iterate on earlier designs. This even progressed to the point that MTI planned on making a midrange "D2" follow-on to the R5000, which wasn't even their design, and a separate high-end "H1" chip codenamed the "Beast."
The revised strategy might have worked except that MTI didn't have enough design resources for multiple microarchitectures. So SGI went back to the old strategy: big powerful cores that could be scaled down.
In May 1997 SGI announced their new MIPS roadmap (here reproduced from
Microprocessor Report
May 12, 1997), starting with an enhancement of the R10K called the R12000. It would be built on the current 250nm process size, enlarge the number of instructions in flight to 48 from 32 and add a new pipeline stage, implement a new branch target address cache with 32 entries a la contemporary PowerPC, and expand the branch history table to 2048 entries from 512 (compensating for the longer pipeline's larger mispredict penalty) while doubling the size of the way-prediction table to better support large L2 caches. SGI expected the R12000 to hit 300MHz or better and would only need about ten percent more die space.
The "Beast" H1 remained in SGI's plans, now scheduled for 1999 at 250nm and 2000 at 180nm, to be followed by an even higher-performance "H2" core codenamed "Alien" somewhere around 2001. Along the way SGI-MTI gamely predicted a six-fold increase in integer performance from the 350nm R10K to the terminal H2. Although Alien was too far in the future to be definite, Beast had some lofty and specific goals; it was to be a MIPS V CPU with MDMX SIMD extensions, implementing a 256-bit cache bus and 256-bit main memory bus at speeds of 200MHz or higher. Alien, on the other hand, was intended for large NUMA multiprocessing systems and correspondingly with even higher bandwidth, by no means coincidentally similar to Cray that SGI had just bought out.
Industry analysts didn't find R12K particularly compelling against expected future competitors and expected Beast would provide a stronger punch. However, after about a year's worth of work — which was only three months after the roadmap announcement — SGI abruptly canned Beast to the market's general surprise, claiming that R12K would be more scalable than anticipated and they would redirect engineers to Alien instead. More ominous to customers was SGI's quieter simultaneous announcement of "Intel-based" Windows NT systems to emerge in 1998, which SGI called the "Visual PC" initiative. Indeed, in 1998 SGI shut down Alien development as well, something that had been all but openly expected, and spun off MTI as a separate company in March to focus on MIPS in the embedded market. The "Visual PC" emerged in August 1999 as the SGI Visual Workstation running Windows NT 4. The first two machines in the series were not fully standard Pentium II and III PCs; they maintained custom graphical boot PROMs and used SGI's bespoke Cobalt graphics, requiring a custom HAL for NT 4 and Windows 2000. Architecturally these early VWs were similar to the SGI O2, while later units were essentially commodity PC hardware with Nvidia Quadro GPUs.
As Itanium started looming over the market, SGI too lost its corporate mind and jumped on the IA-64 bandwagon. Meanwhile, despite vague noises about porting IRIX to x86 (or possibly even Itanic) or providing an emulation layer, the existing MIPS install base proved simply too large to ignore, and SGI did not want to lose existing customers with large ecosystem investments to other vendors — especially since the roadmap for Itanium was far from certain. For this legacy market SGI retained some of the MIPS engineers to continue refining the R10K core and produced new hardware around it. The R12000 finally started shipping in February 1999 initially at speeds up to 300MHz, fabbed by NEC and Toshiba at 250nm and reducing the 7.15 million transistor die to 229mm², though delays and the Osborne effect limited its availability until May. From the R12K to the R14000 and R16000 (codenamed "N0"), each generation had a corresponding "A" subtype with boosted clock speeds, but other than die and process shrinks few other microarchitectural improvements were made. In general these late CPUs were clocked relatively low to reduce heat and power usage. The last, mightiest and rarest R16000A, fabbed by NEC at 110nm in 2004, topped out at 1.0GHz and was only produced for specific customers in limited quantities. None of these chips ever made the jump to MIPS V.
SGI did consider two more chips in the series, though the company was increasingly in the weeds by this point and neither was produced. The best known of these was the R18000 (codenamed "N1"), which SGI presented an early version of in 2001. Specifically intended for SGI's ccNUMA servers, its core was recognizably based on the R10K but each FP unit now had independent multiply, add, divide and square root capability as well as multiply-add, and the core also got an additional load/store unit. A new "SysTF" bus used twin DDR links, one a large non-multiplexed 128-bit read path plus a smaller 64-bit multiplexed write and address path, as well as preserving Avalanche ("SysAD") compatibility. Up to 1MB of L2 cache was on chip, and up to 64MB of external L3 cache (with cache tags on-die) was supported. It was to be fabbed by NEC on a 130nm process in nine layers of copper, and planned for around 2004.
In 2002 SGI suggested N1 could be fabbed at 110nm and run up to 800MHz, but also mentioned an "N2" to appear in 2005 which was widely believed to be a future R20000. SGI promised speeds of 1GHz or more and up to 8 gigaflops of FP performance per core, though the company provided little other information. Both chips were quietly cancelled.
On the graphics side, the terminal VPro ("Odyssey" and "InfinitePerformance") architecture could at best only tread water: it had some very advanced lighting and colour features, but suffered from inordinately weak memory bandwidth and poor texture mapping performance, and was expensive to produce on top of that. SGI abandoned it for Nvidia GPUs which, despite some being badged as VPro cards, were not compatible with legacy MIPS. The MIPS server line offically came to an end with the Intel Itanium 2 (McKinley) Altix in January 2003, SGI's first Itanic systems, running Windows NT and Linux; the workstations were subsequently succeeded by the McKinley-based Prism in April 2005 using the same architecture and ATI FireGL GPUs. They were poorly priced and poorly performing, another nail in the coffin of Itanium, and consequently failed to restore SGI to its former glory. All MIPS product lines were finally terminated in December 2006.
I have some more machines to work on and disposition, by the way. You'll be seeing those soon.
