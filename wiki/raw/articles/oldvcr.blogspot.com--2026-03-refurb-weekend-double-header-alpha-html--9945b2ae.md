---
title: "Refurb weekend double header: Alpha Micro AM-1000E and AM-1200"
url: "https://oldvcr.blogspot.com/2026/03/refurb-weekend-double-header-alpha.html"
fetched_at: 2026-05-01T07:01:26.409395+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Refurb weekend double header: Alpha Micro AM-1000E and AM-1200

Source: https://oldvcr.blogspot.com/2026/03/refurb-weekend-double-header-alpha.html

I've mentioned previously
my great affection for Alpha Microsystems hardware, which are rather obscure computers nowadays, but back in the 1980s and 1990s were fairly sophisticated 68000-based multiuser systems that turned up in all kinds of vertical markets. For example, my first Alpha Micro (an Eagle 300) came from a party supplies store, my Eagle 450 was in a 9-1-1 emergency dispatch centre, and I've seen or heard of them running in medical and veterinary offices, churches, and even funeral homes. In fact, I know for a fact many of these blue-collar computers are still out there quietly doing their jobs in back offices and small businesses to this day. They're probably most technically notable for AMOS, their highly efficient real-memory preemptively multitasked operating system, and the fact they are (as far as I can tell) the only 68K-based machines to effectively run
little
-endian.
Sadly my beloved Eagle 300 appears to have suffered a system board fault and will not complete the power-on sequence, so the ColdFire-based Eagle 450 has temporarily taken over server duties for it on
ampm.floodgap.com
. Fortunately I have a source identified for E300 replacement hardware and one or both of these systems might turn up in
a future article
. Until then, in our continuing household computer inventory, we have two, count 'em, two additional and earlier Alpha Micro machines we need to disposition as well: a 1982 Alpha Micro 1000 (specifically the AM-1000E, originally sold with a 30MB hard disk) and its bigger brother, a 1987 Alpha Micro 1200 (as a AM-1200XP, with additional serial ports and a 70MB disk).
The AM-1000 family were probably the most widespread Alpha Micros, at least to the extent any Alpha Micro ever
was
widespread, and their flexible form factor meant I knew nearly as many people who used them as desktop workstations as who used them as office servers. Neither one is booting, and if they're junk they're too big together to stay in the house. If we can get them back into AMOS, we'll find them something to do. If we can't, we'll recover the space and send them to storage. In this Refurb Weekend we'll tear them apart, find some surprises, dig a couple more out from storage for comparison, and even throw one of their hard disks into the freezer and actually get data off it ...
... but first, a little history, and then a funny story that should be past the statute of limitations about how I broke into the church database as a teenager. And, yeah, it involves an Alpha Micro.
In the 1960s, while juggling his spare time as a rock guitarist, Dick Wilcox was working for the Newport-Mesa School District in suburban Orange county, California, which had its own DEC PDP-8/I running TSS/8 at Costa Mesa High School and a KA10 PDP-10 in the district office (these pictures of the actual hardware, which I upscaled and retouched by hand, are from a Computer History Museum collection originally taken for publicity purposes by Digital Equipment Corporation). Around the same time, as a consultant for Caltech (where our
DEC Professional 380
came from, a "desktop" PDP-11) he developed a small real-time operating system for their new PDP-11, which his contract permitted him to take with him.
Across town in Santa Ana, Alvin Phillips was fed up with upper management at Rockwell and quit his job as manager of its autonetics division to start his own semiconductor company in April 1970, which he named General Digital. General Digital's first product wasn't a chip: it was a chip
tester
, the Spartan 770, designed by John Glade. It could perform functional and parametric testing up to 5MHz, using 40 data channels each with 1Kbit of pattern RAM, all driven by an on-board custom control computer instead of a general-purpose minicomputer. The control computer could be programmed manually using a thumbwheel console, or using punched cards or tape. Phillips estimated this would allow them to sell the machine for less than $100,000 [about $835,000 in 2026 dollars].
General Digital was able to attract enough interest in the Spartan, as well as new semiconductor business, that within a year they moved to a new 35,000-square foot production facility boasting (in a 1971 ad) "capacity to turn out a half-million chips per month" in Newport Beach — near, as it happens, where Wilcox was working. It also attracted the attention of previously existing local company
Digital General
, who was already producing their own semiconductor test equipment, and who promptly sent several cease-and-desist letters to Phillips. As Digital General would almost certainly prevail in any threatened litigation, Phillips economized with the inevitable name change — since he had already spent a fair amount of money on machined plastic letters for the company's flagpole sign, he simply had the G, A and L replaced with W, S and T, and then rearranged the set to spell its new name in July 1971: Western Digital. The company went all in on the new name, adopting a Wild West advertising theme that even included a bikini-clad model in boots wearing a ten gallon hat, lasso and sidearm, and not much else.
While WD's semiconductor product range was expanding into various other ICs, notably RAM and calculators, the Spartan line remained a strong seller. However, although its custom control computer enabled Western Digital to sell the basic test rig relatively inexpensively, it was also insufficient for some customers who wanted to run more sophisticated tests. By 1972 the Spartan 770 came in six ("Six-Shooter") discrete configurations ranging in cost from the $49,700 single station "Bit-Rider" memory tester to the $180,800 "Ranch-Master" engineering characterization test system [approximately $380,000 to $1.39 million in 2026 dollars]. The two upper tier systems came with their own preconfigured PDP-11/20 minicomputer which WD purchased from DEC and provided to buyers. Dick Wilcox subsequently joined the company as manager of software, bringing his real-time operating system with him, and those systems ran Wilcox's timesharing kernel with the addition of multiuser support.
The arrangement was profitable for both companies, and on the strength of this corporate relationship DEC approached WD in 1974 with a new project. While the early generation PDP-11s were fast and capable for the time, they were expensive, hot, bulky and difficult to architecturally expand owing largely to their construction out of discrete logic, even the slightly later microcoded units. DEC wanted to contract WD to develop an LSI (i.e., large scale integration, in the tens-of-thousands of transistors per chip) processor architecture cheap enough that DEC could make new low-end PDP-11s out of it in large numbers. The two companies negotiated an arrangement where WD would keep the rights to the resulting design and could market it separately to licensees, DEC included, and DEC would pay WD roughly $6.3 million for the work [about $42.4 million in 2026 dollars].
Phillips put engineers on the initiative immediately and the first LSI-11 CPU was unveiled for the DEC PDP-11/03 announced in February 1975, with full production starting in March. The core design, called the MCP-1600 by Western Digital, was in fact a CPU optimized for running
microcode
rather than any fixed instruction set; the microcode, in turn, determined the particular instruction set it understood. MCP-1600 systems came as a constellation of at least three chips on an 18-bit internal bus: the 1611 RALU (data or register ALU) chip with the ALU, execution path and 26 8-bit registers that in LSI-11 systems were paired into the PDP-11 16-bit registers, the 1621 control chip handling instruction dispatch, microinstruction scheduling, external system bus and interrupts, and then at least one 1631 MICROM high-speed 512 word ROM (words were 22-bit) with the control store. The basic LSI-11 system shipped two of these ROMs, with a third for the extended and floating-point instruction sets, along with a separate writeable control store as an upgrade option for developing custom instructions. The chips were fabricated by WD on a 7μm NMOS process as 40-pin DIPs and ran up to 3.3MHz.
Fulfilling DEC's desire, the LSI-11 PDP-11/03 and its descendents were substantially less costly to manufacture and significantly smaller, and despite being what longtime DEC engineer Bob Supnik sardonically referred to as "the slowest PDP-11 ever produced" ended up selling in some of the largest quantities of any minicomputer to that point. (As far as DEC was concerned, the resulting market segmentation was a beneficial consequence: if you wanted a
fast
PDP-11, they'd happily sell you one of the big ones.) Their unspectacular performance was due to being in effect an 8-bit architecture emulating a 16-bit one: the basic cycle time was a respectable 350ns for a nominal clock speed of 2.857MHz, and the control chip's "programmable translation array" (a collection of four on-chip PLAs) greatly reduced macroinstruction overhead, but main memory access times were impaired by the double-pumped data bus and a worst-case instruction could take tens of microseconds to execute.
Wilcox believed he could do better. Fellow engineer Rich Notari refined the microcode ROMs by reworking the instruction set and adding additional ones such as block move instructions; after several iterations they had a five-chip version that was competitive (though not compatible) with mid-range PDP-11 systems, yet being derived from the less expensive LSI-11 meant it was cheaper too. Simultaneously Wilcox had continued to enhance his kernel, now using a PDP-11/40 in his back bedroom, into a highly complete operating system with development tools, its own compiled BASIC dialect and a wide array of system calls operated through a command line interface resembling TOPS-10 to which he was already accustomed.
In 1976, however, Western Digital's fortunes took a nosedive as their other core lines plummeted, especially with the bankruptcy of Bowmar, one of their major calculator customers. Alvin Phillips was ejected during Chapter 11 reorganization in October and WD's shrinking fabrication capacity forced DEC to become their own second source for the chipset, reducing their buy and stressing the ailing WD further. In an attempt to raise cash, WD's interim management decided to re-release the MCP-1600 with Notari's microcode as a separate product in October 1976, dubbed the WD-16. Although it attracted little industry interest, possibly due to concerns over WD's future, Wilcox still believed in its potential and in January 1977 established Alpha-Micro Technology with himself, Notari, and investor Bob Hitchcock in Tustin to capitalize upon it. Making an arrangement with WD to buy and sell the chips on their own, Wilcox and Notari also lured John Glade and fellow engineer John French to join them in developing the new architecture.
The company's first product was to be the SIXTEEN/8, nicknamed "Sweet 16" and later dubbed the CM-16, which replaced the 8080 CPU in an Altair or IMSAI 8080 enclosure with a set of two extra-height S-100 cards carrying WD-16 chips. These cards were so tall that they extended nearly twice as high above the modified IMSAI 8080 the set was demonstrated in, here shown from
Kilobaud
April 1977 with Wilcox at the console. Notionally 2MHz for bus compatibility, it could be clocked up to 3.3MHz "with some modifications." The SIXTEEN/8 ran Wilcox's fully-fledged operating system monitor provided on floppy disk and the card was to be sold for somewhere between $1000 and $1300 [from about $5400 to $7000 in 2026 dollars] plus floppy media cost.
Dr Dobbs Journal
editor Jim Warren, evaluating the prototype at the Homebrew Computer Club, called it "a magnitude more potent than any other system I have seen" and approved of its speed and capability. Within months Alpha-Micro Technology was renamed to Alpha Microsystems (not to be confused with the later, unrelated Alpha-Micro Technology in Fontana, California) and the cardset was renamed to the AM-100.
Being one of the earliest multitasking microcomputer systems, when introduced in August 1977 at $1495 [about $8100 in 2026 dollars] the new machine sold well by the standards of the day and sales soon broadened from initial direct hobbyist purchases to more corporate sales via resellers and dealers. Thus began the tradition of Alpha Micro's dominance in certain vertical markets, where value-added resellers sold turnkey packages with the main computer, terminals and customized software ready to run. In February 1979 Alpha Micro upgraded the architecture with the AM-100T (later the AM-100/T), providing a full 16-bit data bus through a modification of the S-100 bus and increasing the clock speed from 2MHz to its full 3.3MHz. Meanwhile, AMOS — the now-matured form of Wilcox's original operating system monitor — could support as many as 22 simultaneous users running multiple simultaneous tasks limited only by memory, with a text editor originally described by Wilcox himself as "a limited version of the very popular TECO program" plus support for a macro assembler, an ISAM database, and the included AlphaBASIC dialect which compiled to a bespoke P-code. By the middle of 1981 over 5,000 systems were reportedly in use.
Simultaneously, however, the architecture was approaching a dead end because the WD-16's unusual design couldn't be flogged to go much faster nor expanded a great deal further. Internally Alpha Micro selected the Motorola 68000 as their next CPU based on its strong support, 16-bit compatibility, solid performance and minicomputer-like architecture, but this posed a quandry with the existing userbase because the WD-16 and the original AMOS ran little-endian, while the 68K is categorically big-endian (and running WD-16 binaries in emulation would have been impractical in any case). Alpha Micro's system designers came up with an alternative. Since the native word size of the WD-16 was a 16-bit integer short, Alpha Micro simply chose to flip address lines so that all 16-bit quantities (including CPU opcodes) were stored the same way as the WD-16 in memory — i.e., little-endian — but still seen as big-endian to the CPU. This scheme yielded the only case I know of a little-endian 68000 system, allowing pre-compiled AlphaBASIC P-code binaries and most other data files to be used all but unchanged on the new architecture; certain macroassembler features were added at the same time to make the transition smoother for native code. AlphaBASIC and its runtime (as well as the rest of AMOS) then could be rewritten native for the 68000, and since most then-extant third-party software had been written in AlphaBASIC and shipped as P-code, it could run unchanged yet several times faster. (This byteswap was only needed for shorts; 32-bit integer longs are still emitted big-endian, but with each 16-bit half stored little, thus effectively "middle endian" by modern standards. This is also the same way the PDP-11 stores shorts and longs in memory, and given Wilcox's history with DEC hardware it was almost certainly not a coincidence.)
Alpha Micro ended up reinventing nearly their entire product line around the 68000, and introduced the new models in the summer of 1982.
For the original S-100 systems, the AM-100/L, their final S-100 CPU card, was introduced at the National Computer Conference in June with an 8MHz 68000. This is my AM-100/L and an AM-710 memory board (128K with single-bit error correction). For current customers, with the new 68K-based AMOS and a change in CPU cards, the /L gave current S-100 owners an upgrade path to the new faster architecture yet kept most of their existing hardware options and many applications.
For new customers, the AM-100/L was shipped in several stock "minicomputer"-esque configurations (initially the AM-1042 and AM-1062, and later the AM-1042E, AM-1072, AM-1082 and AM-1092) intended for large deployments, supporting up to 8MB of RAM and 68 serial ports. These machines used similar backplanes as the earlier WD-16 S-100 systems and integrated the functions of their two-digit LED AM-960 front panel, but alongside a conventional tape streamer option also provided a new backup feature standard — VHS tape. Up to 100MB could be stored on a standard VHS video casette recorder, and an I/O connector allowed specially fitted VCRs to be computer-controlled. The machine could even boot from a VHS tape for emergency restoration.
Parenthetically, the VCR backup system was popular enough to be eventually exported as a standalone product for PCs and even the Macintosh, sold as Videotrax. Since this blog is even
called
Old VCR, it's a fascinating technology we should definitely look at
in a future article
.
But the bigger news was the
smaller
system family introduced at the same time: the all-in-one, desktop-ready AM-1000. Unlike the larger S-100 systems, requiring sometimes multiple cardboxes for devices and disks, the AM-1000 could sit on a desk yet carried enough serial ports to still support other users. It came with the same 8MHz 68000, 128K of RAM (initially expandable to 384K, later several megabytes or more), three serial ports and the VCR interface, plus your choice of up to two 800K 5.25" floppy drives and a Winchester hard disk (at that time ST-506 connected by SASI). With an AM-1003 board, you got a Z-80 with its own 64K RAM and CP/M 2.2 compatibility, plus four more serial ports and a parallel port; later upgrades allowed up to eight more ports. The entire system started at "just" $10,000 [about $34,500 in 2026 dollars].
At that price the AM-1000 wasn't going to be
a
Commodore 64, but it rapidly became
Alpha Micro's
C64: amid record company profits after the 68K systems started shipping in July 1982, by early 1984 the AM-1000 family represented thirty percent of Alpha Micro sales. From a 1982 installed base of 7,000 the company reported over 20,000 systems in October 1984, and most of them were AM-1000s.
These were credible sales numbers for multi-user systems and on their strength the company might have slowly continued to gain marketshare, but several missteps started to impair their finances at the same time market trends were changing. With the advent of the IBM PC, the "small" AM-1000 family's unusual capability as a light office server didn't make much sense to small buyers who might just want a PC or two and didn't need the multiuser features. Plus, while AMOS was considered a strength by its userbase and had many devoted fans, it was unfamiliar to higher-end markets which increasingly preferred a Unix option.
Alpha Micro attempted to counter these perceived weaknesses in two ways. The first was their own line of PCs, some equipped with ISA co-processor boards that could run AMOS (basically AM-1000s on a card), serve other users, and exchange files between the DOS and AMOS partitions. The second was UNIMOS, their own licensed version of AT&T System V UNIX, and the 1984 AM-1100E, its intended target, originating as a a hopped-up AM-1000 with a 10MHz 68010, 1MB of RAM and extra memory management hardware (never needed for AMOS, something I'll talk about shortly). The problem in both cases was they were neither cheap enough nor distinctive enough to entice new customers that weren't already in Alpha Micro's orbit (the base AM-1100E system started at $15,585 [$48,700 in 2026 dollars], a thoroughly unattractive price), and the customers that already were overwhelmingly preferred AMOS.
UNIMOS' failure in particular badly damaged the company, first from the price of the Unix license itself and its associated royalties, a substantial sum for a company of Alpha Micro's size, and second when expected sales failed to materialize. The company also had to contend with a 1984 lawsuit from Digital Equipment Corporation over AMOS' similarities to TOPS-10 and RSTS/E, an ultimately unsuccessful legal action but not without cost. In the meantime, Alpha Micro cut prices and introduced the VMEbus to the line with two new tower midrange systems, the 1985 10MHz 68010 AM-1500 and that same year their first fully 32-bit machine, the AM-2000 with a 16MHz 68020. The weakened company subsequently found itself the unwilling target of a September 1986 hostile takeover from a local Orange county competitor less than half its size; this buyout was deflected by Wilcox and Hitchcock, who still held a quarter of the company but had been forced out of the top executive slots, when they agreed to instead sell out to terminal and computer maker TeleVideo — who walked away from the deal in November anyway. In December 1986 Alpha Micro, in an attempt to revive their best-selling product, reworked hardware from the doomed AM-1100E into the AM-1200, a continued refinement of the AM-1000 architecture at a lower cost yet with more upgrade options. The 1MB RAM AM-1200B base model, with 20MB hard disk and an 8MHz 68000, now started at $8300 [$23,200] and came with a bundled AM-62 terminal and 5-user AMOS license, a much more economical option.
Still, it wasn't like the company wasn't notching
any
significant wins. One of the vertical markets Alpha Micro practically ruled for years was professional legal services, and the Nevada criminal court system migrated in 1984 to multiple AM-1072, AM-1092 and AM-1000E machines and 150 AM-60 user terminals through Alpha Micro and their local Carson City dealer Jimwest, a contract worth about $500,000 [$1.56 million]. Alpha Micro also had a strong presence in medical and dental practices as well as non-profits and houses of worship — a good fit for the Salvation Army, a church first and foremost but with its own strong presence in social services, whose 13-state Western Territory region of the United States contracted with VAR Alpha Base Systems in 1985 to buy nearly 90 systems for individual corps (churches) and headquarters. Initially these were AM-1000X systems with 512K of RAM and some number of AM-62 terminals; the contract continued into at least the mid-1990s with subsequent installations, particularly for larger premises, based on the AM-2000 or later. The Salvation Army's use of Alpha Micro systems was quite sophisticated for the time. I was told by someone who worked on it that they developed a means for turning
U.S. Census TIGER files
into raw street map data to route trucks for donation pickup, and even had touch screen terminals to aid workers sorting clothing donations.
That leads to my funny, hopefully non-prosecutable, story, which also suffices as a bit of introduction to the operating system. As I've mentioned in
prior entries
I grew up in San Diego, California, and in the late 1980s we started attending the Salvation Army as parishioners, first in
El Cajon
and and then the Citadel Corps, which in those days was in the Gaslamp Quarter (now the
Centre City Corps
). I played in the band, too, just not very well. In 1993 the San Diego Citadel Corps moved to a new, much larger property in Clairemont on Balboa Avenue (old
CA 274
) and we began attending there. California is of course part of the Salvation Army Western Territory — THQ is still in Rancho Palos Verdes — and so the new Citadel got its own Alpha Micro installation, a couple printers and five or six AM-62 terminals in various offices as memory serves, with the show run by an AM-2000 in the back. I dimly remember RJ-45 jacks in the offices for the serial connections, probably plain old Category 1 wiring at that time, but I also clearly recall it had a VCR for automated backups, plus a modem and its own phone line so it could communicate with the main system downtown.
Security in AMOS is best described as token, largely because it was only ever designed for relatively small numbers of simultaneous users who were expected to behave themselves, and though additional privilege levels were added in later versions they were never very strong. Another reason was cultural practice: if you get to the AMOS dot prompt on any random Alpha Micro system, odds are you can rapidly gain operator privileges (based on octal project-programmer numbers, again another DEC-ism) because most VARs never put a password on [1,2] (the superuser, usually aliased to
OPR:
) or for that matter [1,4] (where system files are stored, usually aliased to
SYS:
). AMOS is also a strict real-memory operating system, which is to say there's no MMU, and programs were expected to be fully position-independent and run wherever the monitor ended up loading them. This makes it fast, but also makes it possible for jobs to stomp on other jobs, and it was not uncommon for busy systems to crash on a regular basis. More nefarious tricks were possible: the hacker magazine P/HUN noticed (June 27, 1989) that you could nab operator even on a system that
did
have a password by patching where your current PPN was in RAM, something like
WORD(WORD(1072)+20)=258
in AlphaBASIC — 258 is, of course, $0102, i.e., [1,2] — a hole that was later closed, probably through obfuscation, but intrinsically could never be fully avoided. In fact, going to 68K supervisor mode is even an unauthenticated "ordinary" system call, something we're going to use later in this article. On the other hand, the vast majority of AM systems were independent standalones like this one that could only be accessed on premises, so if anything went hinky, in many cases it wouldn't take you long to find the culprit. (Foreshadowing.)
As such, the primary means of security on a running installation was not to let users actually
get
to a dot prompt, thus moving privilege enforcement into the front-end turnkey application — whatever that was — instead of the operating system monitor. Alpha Micro themselves even provided AlphaMENU as a generic front-end system. In this case, the Salvation Army ran Alpha Base Systems' church management and accounting suite, which I believe was also written primarily in AlphaBASIC with various extensions. I don't remember how I talked the Captain (pastor) into letting me on the system, but he did, though upon logging on you were immediately and unconditionally launched into the application suite. After rapidly exhausting the entertainment potential of word processing, spreadsheets and fundraising campaigns, I decided the front-end was in my way and started looking for a means to break out of it. I should mention at this point that I only knew the system was an Alpha Micro; I didn't know anything about AMOS otherwise.
AM terminals (which are actually modified Wyse terminals) have a Cancel key. This would normally interrupt a running program and such front ends generally disabled it while you were within them, though they necessarily had to re-enable it to run certain utilities as subprocesses. It turns out that Alpha Base's front end had a race condition in at least one of the menu options where, if you hit Cancel before the menu could restart, the program would stop and you'd get a dot prompt. As I say, I didn't know AMOS, but I immediately knew a command line when I saw one. Since
TYPE
and
DIR
in AMOS do the same things as
TYPE
and
DIR
in MS-DOS and I think the account was already logged into
SYS:
, I was able to read some sample script files from which I learned that
LOG
was the command to change an account, and from there I learned about
OPR:
, and there was no password on it, of course, and that was the end of the game. Through trial and error and the limited online help I learned more AMOS commands, wrote some games of my own to play in AlphaBASIC, and even discovered how to dial out through the modem and connect to the terminal server at UC San Diego where I was an undergrad at the time. That meant that on Sundays, when we spent most of the day at the corps, I could connect to my shell account at the university, read my E-mail, and waste time MUDding during the downtime between services. (In my defense, even though the 619 area code was a lot larger in those days, it would only have been a local call from Clairemont to La Jolla.)
As I recall I ended up putting a password on the PPN I stored these things in once I figured out how, something I should have realized would almost certainly be noticed, and a couple Sundays later the system administrator — herself also a parishioner, and who was well aware of my interest in computers — accosted me after church. "Cameron," she said, "don't deny it — I
know
you did it. You tell me how and I'll let you keep the access." Indeed, there was no need to explain what "it" was. I showed her the race condition and she also made me undo the password protection, but she was impressed by what I'd figured out and was as good as her word: I got a login that
did
have system access once I promised I would not abuse it, because she informed me in no uncertain terms that she would know, and I kept that login until I started attending a different church a few years later. I don't know when THQ eventually scrapped the Alpha Micro systems, though there were already some standalone office PCs appearing even then, and to the best of my knowledge no remnant of the deployment remains today. As for the Balboa Avenue site, it was an expensive property to maintain in an expensive real estate market, and in 2022 the Citadel Corps ended up moving to its current location on Health Center Drive with the old complex now occupied by another church.
So, when annoying salesdroids can't or won't understand why I don't want remote access I don't fully control to anything that matters (my alarm system, my car, etc.), this is the story I tell them, and this is also why I wanted to have an Alpha Micro of my own because it was the first system I technically hacked into (even if largely by accident). The first such system I ever owned personally was the Alpha Micro Eagle 300 I mentioned at the beginning, a much more modern system we'll revisit when we tie the history up at the end, and which longtime readers of the blog
have met before
. It was a chance find on eBay from its prior life as a point-of-sale system in a party supply store and I learned a lot from it. Along the way I picked up a couple more Eagle systems including a couple Eagle 100s and the Eagle 450 which is my primary system at the moment, and intermittently various AM-1000s and AM-1200s. Some of these I found homes for and a few I kept.
Admittedly the "desktop" form factor was mostly by comparison: they still take up a couple square feet on a desk and weigh 20-25 pounds, though you can easily plunk the terminal head and other peripherals on top of their sturdy steel cases. These two particular machines which I still had in my possession were not booting, which unfortunately will be the case for most such units you'll find nowadays. Most were sold with ST-506 drives with special Alpha Micro-specific conversion boards to make them look like old-school SASI (Shugart Associates System Interface, the ancestor of SCSI, which is a largely compatible superset). The drives AM favoured in these machines were not highly reliable over time — compare with, say, the one in my
DEC Professional 380
— and tended to readily fail with highly stressful tasks such as sitting around and merely existing (the relatively poor airflow inside the case can't have helped).
When the main drive dies on these and other similar models, the system PROM will display a "b" in the LED status and then just sit there, implying the computer had completed basic POST but has not yet found a device with an operating system. Since the drive is kaput, it will never get past this point. If you find one of these machines on eBay, ask the seller if the "b" appears and then goes away — only if it does is it actually booting from something.
This is also a good picture of the front panel. Besides the two-digit LED status, which is programmable, there are separate LEDs for "power," "run" and "parity" (renamed to "memory" on the 1200), and the AM-1200 also adds a "disk" access light for SASI activity. The "power" light is self-explanatory. The "run" light is wired to the CPU status output lines such that if this LED ever extinguishes, the processor has halted (or never started); on these systems using their original processors, the run LED should be pretty much lit continuously. Finally, the "parity" light indicates a memory error, if enabled by the operating system. We'll come back to this very soon.
Let's start with the AM-1000. This is a slightly later 1983 AM-1000E variant which as originally shipped from Irvine came with 256K of RAM and a 30MB disk.
However, our first clue that this unit was heavily upgraded is when we look at the back. Original
original
AM-1000s have a black enamel rear panel, which I'll show you in a moment, with subsequent units like this one shipping with brushed metal. The three 25-pin RS-232 serial ports are on the top left, with the VCR interface to the right of them, but on the lower right this unit also has a third-party Piiceon SR1000-16PB upgrade card providing
sixteen
more. These are RJ-45 jacks using Alpha Micro's serial pinout. A few things have also been
removed
: there should be a perforated metal stiffener along the top which has been taken out (the open black windows), and there is no plate over the external SASI interface (the Centronics-style port on the lower right), suggesting this unit was attached to one or more external drives at some point from which it was then separated. I'll show you what both of these would have looked like later on the AM-1200.
The serial ports are conveniently labeled with how they would be referenced in the system initialization file. This machine is also labeled with its Software Security Device (SSD) serial number for easy reference, a five-digit code you would provide to a VAR selling you licensed software, who would validate the serial number and then give you back a PIC (Product Installation Code). This PIC is keyed to the SSD and encodes your license conditions (typically maximum users, enabled features, etc.); the operating system also has a PIC which enforces maximum user caps (i.e., serial ports that may be active) and certain other premium features. The SSD was introduced with the AM-100/L and appeared on all subsequent systems, and because only Alpha Micro issued them, every SSD is unique to a specific machine and centrally registered. The SSD serial number can't be used to derive the SSD key value (or at least not that I know of), which only Alpha Micro kept internally, and vendors wanting to PIC-code their software had to go through Alpha Micro to do it. If the system needs to be moved to another logic board, the SSD can be removed and installed on the new board so that the same software will still work. On these early systems the SSD was typically a PAL20X10 in a socket with the markings scratched off; later SSDs were PLCCs. As their security fuses are invariably blown, cloning them requires at minimum a decap, and there was (allegedly) a cottage industry among some VARs that did just that.
However, I'm not sure if that label's SSD serial number is accurate, because next to the Dymo-labeled SSD serial number is the
factory
rear label. On the factory label this machine's serial number matches (I1244) but not the SSD serial, which appears to have been originally different. The model number is given as AM1000-17, referring to its particular board iteration, and "revision C03." Again, remember this for comparison later with the AM-1200. Fortunately most of the software we care about nowadays (the core OS, AlphaTCP, etc.) no longer requires a PIC.
These early Alpha Micros also have a "system change history" on the underside where the factory loadout was printed and a diligent owner was supposed to annotate any subsequent changes or upgrades. In my experience this was rarely done with any consistency, and there is indeed no mention of the SSD change or the serial port option card, though this machine apparently did have at least one post-market upgrade to its hard disk.
The next step is to run the self-test. This can be done with the status LEDs alone but it's nicer with a terminal, though the AM-1000 has the old self-test ROMs which only communicate at 300bps. Here we'll use my spare colour AM-75, which is a modified Wyse WY-370. Its configuration screens, accessible by pressing Ctrl-Shift-Cancel, use simple text pulldown menus. We set the new baud rate and wire the terminal into the first serial port ("AM1000-0").
To start the self-test, we hold down the reset button as we turn it on. After some garbage, we get the test starting, so looks like the electronics are okay. The system displays both text output to the terminal as well as codes to the status LEDs.
The real surprise is that this machine has not 256K of memory, not 512K of memory, not 1MB of memory, not 4MB of memory, but
eight megabytes
of memory, a whopping amount for such a system and not achievable with any combination of Alpha Micro memory boards. However, it completely fails to detect a hard disk ("Winchester controller not detected"), as well as the floppy drive and tape streamer, which aren't installed.
I tried to capture the serial port output, but ...
=====================
| AM-1000 Self-Test |
=====================

TESTING MEMORY ..
MEMORY TEST passed
 8192K bytes detected


=====================
| AM-1000 Self-Test |
=====================

TESTING MEMORY ..
.. it did not like being connected to the MacBook or the iBook G4 and (on the LEDs) repeatedly complained the serial port was bad, after which it then failed to emit any additional information to it despite working just fine to the AM-75. It's possible the PL-2303 dongle unsettled it (though note from the future: it was perfectly fine using this dongle as a console terminal).
Given the bad hard disk and that unexpectedly huge amount of RAM, we really need to crack it open now even if only to see what this thing is actually packing.
Because some of the rear screws were already removed during whatever upgrades took place, all we need to do for this particular unit is remove the upper shell.
And immediately we see an even more substantial upgrade sitting right in the middle: an Interlink Systems Dimension-030 upgrade board with a real, honest-to-goodness 68030 CPU. It is replacing a very large DIP in the middle which is obviously where the 68000 used to be. This would have been a non-trivial upgrade to install since the 68000 was soldered on many units, and you can see it also requires its own power supply which it pulls from one of the drive Molex connectors. While there is RAM on the main logic board, it is not used by the accelerator, which has its own SIMMs. Much of the board is in fact discrete logic which is primarily part of the VCR interface.
A second CPU is visible at the bottom, an NEC D780C-1, which is a 4MHz Z80 clone handling I/O and (I believe) the VCR circuitry. This CPU, like most of the other clock sources on the board, is clocked by the 16MHz oscillator next to it, which would have been divided by two for the 68000 and four for the D780C-1. Two 4.9152MHz crystals in the top right are used for the serial ports as they can be divided down to standard bitrates. These seem to drive the three Hitachi HD46850s next to them, one for each of the three standard serial ports, which are clones of the Motorola MC6850 ACIA. The only other visible clock source is a 14.31818MHz (1260/88) crystal at XY1 near the patent sticker on the top left, which any video nerd will recognize is divided by four to yield 3.58MHz (315/88), the standard NTSC colourburst frequency (obviously for the VCR). There is a jumper for the video standard near the green case ground wire.
A moderate amount of board rework and some bodge wires are also immediately apparent. One notable area for this is U196 up near the top right, which is ordinarily a small PROM. This PROM has to be removed and/or replaced for memory upgrades, which is what was done here and new wires routed to a point under the CPU upgrade card. Another notable chip is U156 on the bottom right, which is the SSD. The serial on top of it doesn't match any of the external codes either, but it's socketed and the right kind of chip, the only chip on the board with a plausible SSD serial number stamped on it, and — consistent with a security device they don't want people messing with — the only chip where its factory markings have largely been scrubbed off.
The 68030 CPU is the spiky silver heatsinked chip in the centre. There is no external cache visible, just two slots for SIMMs, both of which appear to be 4MB and parity. (Stay tuned on that.) For that matter, there's no oscillator on the board either, so barring some non-obvious clock doubling circuit it is most likely clocked at the same 8MHz as the 68000 it replaced. A jumper (J1-J2) controls whether it has 1-2MB of memory or 4-16MB. The rest of the upgrade board is glue logic and a bunch of GALs.
The 1991 copyright date (and 1992 chip dates), compared with the 1985-6 chip dates for the rest of the logic board, tells you how long this machine was in service doing its job. (Note from the future: it will get a few years longer when we finish tallying up the upgrades and remnants on the hard disk.) It must have been a very important job to its owners to justify these upgrades, too, as this particular board was a low-volume item and definitely not cheap. Indeed, it is the first one I've ever seen myself.
The CPU board has its own run LED, and it obligingly turns on when I turn on the power. Obviously it must work to some degree or the self-test wouldn't have run, since the CPU must run it.
Other landmarks on the board include the (super dead) 3.6V NiCd General Electric DataSentry rechargeable clock-calendar battery which has clearly seen better days, next to the power supply connector ...
... and the logic side of the Piiceon serial board ("Intelligent 16 Port"). This has its own Z80, another third-party version (Mostek MK3880N-4) rated for 4MHz and running from the 3.6864MHz oscillator next to it. It has its own EPROM and 8K of RAM and drives eight Signetics SCN2681 (SCN2681AC1N40) DUARTs, also rated for 4MHz and also clocked by the same 3.6864MHz source. These are clones of the Motorola MC68681 with each DUART handling (wait for it) two ports. The latest chip dates on this board are 18th week 1989, so it looks like it got the serial port upgrade first, then the CPU upgrade, presumably because it was servicing a lot more users at that point.
But we haven't gotten to the hard disk yet, so we need to get the logic board up. The logic board is in a tray that can swing up, so we undo its moorings from the rear plate ...
... after which we can just lift it up and back.
From left to right, the bottom of the case has the power supply, an empty peripheral bay (the 5.25" floppy or tape streamer option would go here), and finally our recalcitrant hard disk. There was a dual floppy variant which had another floppy drive in place of the hard disk, but I can't imagine that particular loadout was at all popular.
The back end of the Piiceon port card is also here, connected to the controller board above by a ribbon cable (the one marked with red, not the blue port, which is the external SASI). This side shows the back of the RJ-45 connectors and a whole mess of Motorola MC1488 quad-line RS-232 drivers and MC1489 line receivers that handle the level conversion for the DUARTs.
And finally the hard disk itself. AM-1000s initially came with ST-506 drives carrying onboard Xebec controllers that make them look like SASI, but later ones came with SCSI-1 drives, which because SCSI-1 is a strict (enough) superset will work with SASI. This particular SCSI drive is a Maxtor, which is why it failed, because all Maxtor drives suck. The vendor kindly wrote the installation date on the drive (January 11, 1994), extending our system's minimum service lifetime to no less than eight years in the field — we'll get a better idea of its exact operational period later. It is officially a 3600rpm, 207MB formatted, SCSI-1 piece of crap.
Unfortunately, if the Piiceon card or the Dimension-030 board require any drivers, they'll be on that piece of crap, so we need to get it to spin up somehow. (I don't have the budget nor the inclination to send it to a data recovery specialist.) We take out its mounting screws on the bottom ...
... and fish it out.
The drive electronics look superficially okay, but hooking it up to power caused it to power up, seize and then immediately power down, as if the spindle couldn't turn. A couple (gentle) taps did not make it any more willing to start up, and I don't have a clean room dust-free enough to make me willing to expose the platters.
There is, of course, one other old wives' fix for what appears to be a terminal case of stiction, and that's to go stick it in the freezer for a couple hours. The theory behind this otherwise barbaric notion is that if the head is stuck, freezing everything will shrink the metal components enough for the head to hopefully clear the platter(s) and let it spin up again. This hasn't worked for me before — coincidentally with a half-height 7200rpm Maxtor that committed suicide in my Power Mac 7300 and took most of my files with it — and it definitely isn't a good idea with modern spinning rust where the tolerances are far smaller. However, this is a drive old enough where it
might
work, and the risk of condensation is reduced because Floodgap HQ is in dry Southern California (and the Santa Ana winds make it even drier), so in the immortal words of General MacArthur, why not. I stuck it in a sealed bag with some silica gel packets and left it to congeal.
In the meantime I went to the "hot" storage unit where I keep spares and partially working systems and dragged out the other pair of AM-1000 and AM-1200 systems. These two were already known not to work properly but I wanted to see what I could get off them to restore the others. You can distinguish the AM-1200 I just grabbed from the one I'm trying to restore because the busted one has a more worn-down front badge.
The AM-1000 here is one of the first generation units with the black enamel back plate. This is the AM-1000-07 configuration (three onboard serial ports and a four-port extension), but these earliest systems have no back label. I find the black backplates nicer looking than the later ones. No, I don't know what it did at Ontario Hydro, a Canadian crown corporation which at one time was one of the largest electric power generating companies in the country. It was broken into five successor entities by an Act of the Legislative Assembly of Ontario in 1999 and presumably this machine had been long since decommissioned by then.
Inside, even this machine has been upgraded somewhat, just not to the extent the AM-1000E was. The 68000 is socketed in this machine. U196 has been removed and a large AM-706 memory board fitted on top. Labouriously counting the TMS4164 8K RAM chips, there are seventy-two, and knowing that some are reserved for parity this is most likely a 512K board. There are pads for at least thirty-six more, which would be 768K.
I say "most likely" because this machine does not pass power-on tests. Notice that the run light has gone out. If I try to bring it up in self-test, it hangs on the very first code 81, which is during the memory check. With this many individual RAMs on board it is almost certainly choking on bad RAM, and such a fault would take a very long time to smoke out and fix. I put it and the spare AM-1200 aside for the moment and turned to the AM-1200 we're going to restore.
The AM-1200 generally comes across a bit more upscale than the AM-1000. It has its own nice badge, plus a recessed reset button and a disk activity light, plus the same LEDs as the AM-1000. This particular system also has the optional 5.25" floppy installed using a different front bezel. The floppy disk was some sort of accounting software and I think it was just a random disk that someone jammed in there as
a head protector
.
This unit has the perforated horizontal stiffener on the top shell that the AM-1000 had since lost, and it also still has a plate over the external SASI interface, so it probably wasn't connected to any other hard disks. There is an asset tag for "UNIVEX" which could be one of several companies but one short and embarrassingly cursory Google search later I couldn't find one with a matching historical logo (if you recognize it, post in the comments).
There were three main factory variations of the AM-1200, the base AM-1200B (the bundle) with the built-in five serial ports, 1MB of RAM and 20MB hard disk, and then two thirteen-port versions, the AM-1200E and then the AM-1200XP with 35MB and 70MB disks respectively. Thus, this one must be at least a 1200E because the eight-port expansion card is present. A tape streamer or 5.25" floppy could be added as options to any of the three variants, as was done here. Also note the VCR jacks, the "remote" for connecting to a computer-controlled VCR, and DIP switches for selecting the boot order (here down-up-up-down, indicating VCR, followed by floppy, followed by hard disk).
To the left of these is a coax port labeled LINK I/O. This is for AlphaNET, technically 10Base2 based on IEEE 803.2a, which uses a custom protocol for file sharing and running remote jobs between Alpha Micro systems and suitably equipped PCs. Despite being Thinnet in principle, this port was never used for AlphaTCP; systems running TCP/IP like my Eagles either use SLIP or "real" Ethernet (10BaseT or AUI).
However, one unexpected thing is how the rear sticker identifies the model: as part of the AM-
1000
family. Yes, as far as Alpha Micro was concerned, AM-1200s were just refined AM-1000s (here an AM-1000-63, revision A05).
You will have noticed that this unit mostly has "DB-9" (DE-9) ports, but these aren't wired like standard PC COM ports. I find it most convenient to use modular connectors for these. On the DE-9 side, wire (8P8C colours)
    Blue (RJ-45 1) to DE-9 1,
    Orange (RJ-45 2) to DE-9 8,
    Black (3) to 3,
    Red (4) to 5,
    Green (5) to 2,
    Yellow (6) to 9,
    Brown (7) to 7, and
    White (8) to 4. This yields a modular connection equivalent to an Alpha Micro "RJ-45" serial port like we saw on the Piiceon card. Run an "RJ-45" 8P8C cable to your other end, which in my case is usually a real RS-232 DB-25. That wiring schedule is Blue (RJ-45 1) to DB-25 1,
Orange (RJ-45 2) to DB-25 20,
Black (3) to 3,
Red (4) to 5,
Green (5) to 2,
Yellow (6) to 8,
Brown (7) to 7, and
White (8) to 4. If you just have a 9-pin serial port, any straight-thru converter will serve.
And here is the system change history, which as is typical has never actually been changed. The drive size appears to be the 70MB variant, so this would be the top-spec AM-1200XP. Let's get it open.
This has nicer case screws than the AM-1000E did.
Because it still has the perforated stiffener on the top case, we need to also undo a second set of screws (the top ones on the rear) to remove the lid.
Immediately on opening it, I noticed two EPROMs whose windows were exposed. Now, a momentary flash of indirect sun certainly won't erase them right away, but since we're going to have the lid off let's get some stickers on those.
That's better.
The main logic board. Although it is ostensibly a member of the same series as the AM-1000, you can see it is a rather different board layout, in large part due to some significant logic consolidation and also the loss of the side area where the option board connected. We still have our three ACIAs for the first three serial ports, though these are actual MC6850Ps this time, but the two additional ports on the AM-1200 are serviced by a different Zilog "Z80 SIO/2" dual-channel serial controller.
There are at least seven clock sources on this board. In addition to the 14.31818MHz (VCR), twin 4.9152MHz (serial port) and 16MHz (main CPU) crystals we saw on the AM-1000, a second 16MHz crystal is at the top near the LINK I/O coax port, plus 200kHz and 3.6864MHz crystals near a large black custom gate array.
If that speed sounds familiar, that's because it was the same clock speed as the Z80 in the Piiceon serial port card, and indeed we have another NEC D780C-1 clone Z80 chip here. We also have the same big bunch of MC1488/MC1489 level shifting logic, but the DUARTs in this machine are actual Motorola MC68681s. Effectively this is the same as the Piiceon card but half the ports and completely merged into the logic board, so we don't need the option card area. Notice the bank of jumpers for selecting RS-422 or RS-232 on each port. The big black gate array ("LIA0995 ALPHAMICRO ICC0000100") appears to have replaced much of the discrete logic chips used for the VCR interface, freeing up more board space.
These earlier AM-1200s have a regular 8MHz 68000, same as the AM-1000 series. Later on they were trivially upgraded with the same 10MHz 68010 used in the AM-1100E (more on that later). This board also has the same 3.6V GE DataSentry rechargeable clock-calendar battery, and the SSD is located next to it, the same sort of PAL (also fabbed by MMI) that we saw in the AM-1000E. One of the stickers that apparently came off our EPROMs came to rest here.
In the last picture you may have noticed a giant gap for a second oversize DIP at location U107 next to the 68000 CPU at U106. There is a jumper next to the CPU saying MMUON, indicating that massive DIP footprint is almost certainly for a Motorola 68451. This is the MMU the AM-1100E used for UNIMOS, and while the AM-1200 doesn't have this chip because AMOS doesn't need an MMU, as a descendant design both the location it would have existed in and the jumper to control it persisted. The MC68451 was a legacy segment-based MMU and not particularly performant, and its deficiencies likely also contributed to UNIMOS's collective woe.
The AM-1200 has updated self-test ROMs. Although they are kicked off the same way (hold in the reset button while powering on) like any other 68K Alpha Micro, these ROMs autosense the baud rate of any connected terminal: the status LEDs display "5b" (for "Sb", "sense baud") and will emit to the first serial port it can detect the space bar on. However, port zero didn't do anything and the computer timed out waiting for it. Port one responded, fortunately, after which the AM-1200 gave a complete readout. In this photograph you can see the status LED showing the current test stage.
19200 baud detected


====================
| System Self-Test |
====================

System configuration:
 Processor - 68000
 Memory detected - 1024K bytes
 Number of serial ports - 11
 VCR interface
 Floppy interface
 Multi-communications ports

Verify the proper configuration was detected ..

TESTING MEMORY ..
MEMORY TEST passed - 1024K bytes

TIMER TEST passed

SERIAL PORT TEST
 !"#$%&'()*+,-./0123456789:;<=>
 ?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]
 Port # 0 passed
 Port # 1 passed
 Port # 2 passed
Testing Expansion Ports
8 serial ports tested
 Port # 5 passed
 Port # 6 passed
 Port # 7 passed
 Port # 8 passed
 Port # 9 passed
 Port # 10 passed
 Port # 11 passed
 Port # 12 passed

VCR TEST
 Ram test passed
 Remote not detected, write/read test being bypassed

FLOPPY DRIVE TEST
 Ram test passed
 Seek/Read test ?Disk error: 0C 65 3E 01 00

MULTI-COMMUNICATIONS PORTS TEST
 Restore CPU passed
 Peripheral I/O test passed
 Counter/Timer test passed
 Serial I/O output
 Parallel port output - No printer connection detected


====================
| System Self-Test |
====================

System configuration:
 Processor - 68000
[...]
There should be 13 ports and all eight option ports are detected, so it looks like two of the five logic board ports are dead — though strangely it says that port 0 is okay even though it wouldn't respond on it. The fact those two aren't displayed at all suggests their control chip did not respond when polled for, because if the chip was found but failed the loopback or interrupt test, it would be counted as present yet the fault would be shown. Unfortunately, neither the Z80 SIO/2 chip nor the MC6850s are socketed, so figuring this out would be tricky and we have plenty of ports for a single user anyway.
The disk error indicates a problem when seeking to track zero. While that could be due to this particular floppy diskette, the drive activity LED stayed lit abnormally long despite being past that particular test stage.
Finally, the hard disk doesn't appear at all, so that's shot too. Let's open it up.
As before, we undo the screws mooring the flip-up logic board from the rear plate.
At first we won't be able to lift the logic board up completely because of the ribbon cables going to the option ports.
We'll disconnect those from the logic board ...
... and now the logic board can flip all the way back on its hinge. The 5.25" floppy is driven by an AM-220 controller board, functionally equivalent to the AM-210 S-100 floppy controller card, with a Western Digital (heh) WD2791 floppy drive controller and 2K of RAM (the NEC D4016C 6116 clone). Although there are 50-pin solder pads for the tape streamer and 8" floppy options, these are unpopulated. The floppy drive mechanism itself is a Panasonic/Matsushita JU-475-2AEG, an off-the-shelf device used in many machines and not too hard to find used. While this drive will write high-density data up to 1.6MB, the controller card only supports single or double density, and the disk format utility will not work with later versions of AMOS. We'll revisit this later.
This hard disk is mounted differently than the one in the AM-1000.
Instead, we unscrew a set on top inside the case ...
... and extract the drive and its bracket that way.
This is likely the system's original drive, an ST-506 Fujitsu with an on-drive Xebec controller appearing as SASI to the logic board, which I've separated to show you.
The controller board is a Xebec 104766. Alpha Micro had a relatively long relationship with Xebec who provided the earlier 1410 and 1410A controller chips as special items, making AM drives with those chips particularly vexing should the electronics fail, especially in the AM-1000 where its very small boot PROMs may be specific to the particular Xebec controller in use. In this case, this drive's board is driven by yet another Z80 (a real Zilog one this time) with its own 2K of RAM (a real 6116 this time), an Intel 8237A DMA controller and four custom Xebec chips. These particular custom chips hail from 1986 based on their date codes, just shortly before Xebec got knifed in the back by IBM in 1987 who switched to their own disk controller chips for the PS/2. Overly dependent on these sales, the loss of IBM's business sent Xebec spiraling into bankruptcy and the company dissolved in 1989.
And the hard drive's electronics. Since this is a Fujitsu drive, most of the chips are theirs. The really dusty larger DIP at the upper left is a Fujitsu MBL8031AH, a second-source Intel 8031, which is a ROM-less version of our old friend the Intel 8051 microcontroller. The EPROM for this chip is likely the 2764 with the gold foil over its window. The MBL8031 and MBL8051 are much quicker than the original 8051, running many instructions in just one or two cycles compared to the 8051 which could take up to a dozen.
Hooking it up to a good power supply, the drive doesn't spin at all, so there's no point keeping it inside.
At 3.086kg (about 6.8 pounds), extracting the drive makes this now a rather svelter desktop system.
Speaking of hard disks, our sucktastic Maxtor should be icier than a South Pole sunbather by now. I hooked it up to a ZuluSCSI set to initiator mode to see if we could get any sort of image out of it, applied power and ... the drive spun up! And kept spinning! Still, the LED flash pattern from the ZuluSCSI and the Maxtor's activity light suggested it was having to make many retries on a lot of sectors. This was not unexpected. Nevertheless, it was successfully running and it looked like
something
could be read periodically, so I left the ZuluSCSI to grind away at it.
Meanwhile, our next attempt will be to boot them "clean" from completely new disk images. This is harder than it sounds with these machines because Alpha Micro rarely sold install media as an item, expecting users would make their own bootable backups for recovery purposes. Additionally, there are two particular complications with this process specific to AMOS. The first is the system initialization file, defining terminals and devices, which is invariably specific to the system it ran on — if we try to use a copy of another system's bootable image, even assuming there were no PIC-controlled software packages on the original system, the file may invoke drivers for now non-existent hardware and prevent the boot from succeeding on the new one. The second is that the number of users (which is to say, the number of serial ports which may be active) is also PIC-coded since at least AMOS 1.3, so we would be officially restricted to a single console terminal. This is because if there were a PIC present on the image, it would almost certainly not match the SSD, which as far as the operating system is concerned is the same situation as no PIC being present at all. Even if we actually
did
have install media, we still wouldn't be able to get around this because we don't have a PIC to give the installer.
However, if we have an image file from some other system in a SCSI emulator device, we at least have a way around the first problem: because the initialization file is just text, we can monkeypatch it for the new system by editing the image file's sectors in a hex editor. We won't be able to work around any limits on the operating system in that fashion, but we should be able to get it to a dot prompt. AlphaBASIC and the M68 assembler aren't PIC-coded, so we can still write and run programs this way.
Since the Maxtor image would likely not have enough good sectors to boot and the Fujitsu was totally shot, I had to turn to another user who had successfully imaged his own system to a ZuluSCSI, so many thanks to fellow Alpha Micro hacker Tom who provided the AMOS images we're going to modify here. I consider this acceptable since owning AMOS-capable hardware grants you a express license to run it on at least a single serial port, which the operating system supports without any PIC. I'll even show you the license text as proof momentarily.
I started with his AMOS 1.3 image. The first thing we have to patch is the initial
TRMDEF
line in the system configuration file that defines the console, or we may not get any output on the serial port at all. On most systems this line usually appears very near the beginning after a
:T
line to turn on output and a
JOBS
line to define the maximum number of jobs on the system (e.g.,
JOBS 8
). The console
TRMDEF
line looks something like
TRMDEF TRM1,AM1000=0:9600,AM62,100,100,100
, which defines
TRM1
(could be any valid name) as port 0 on an interface
AM1000.IDV
at 9600bps using AM-62 terminal emulation and buffers of 100 bytes each for line entry, input and output. These are admittedly small but they are a typical size on many systems, as increasing this bloats the size of the resident monitor and having many terminals with large buffers could consume a lot of RAM. Since we're going to run this on the AM-1000 first, we need to make sure we're using the
AM1000
driver on the right port; for the AM-1200, it would be (reasonably)
AM1200
. This one weird line may appear multiple times in the disk image depending on how many revisions were made to the initialization file, so it is most prudent to change any and all occurrences that may look like part of it.
After editing I moved the image to an microSD card and marked it as SCSI ID 0 (named to
HD00.hda
). Since card access is necessary until we get this all running, I put the card in a BlueSCSI with a Centronics-style 50-pin SCSI port that I could just plug into the external SASI. Unfortunately, even after a firmware update, the BlueSCSI would repeatedly flash its blue activity light like something was being queried but nothing would start.
I then added a configuration file to the SD card. This was to
bluescsi.ini
but would also work for, say,
zuluscsi.ini
.
[SCSI]
Quirks = 4   # Xebec
EnableUnitAttention = 1
EnableSCSI2 = 0
EnableParity = 0
This turns on Xebec quirks to make it act more like the Xebec controller board, enables the ATN line on power on or media swap, and disables both SCSI-2 and parity. I won't guarantee all of these are necessary and some reflect my personal preference, but they're what worked for me because — after a very long delay presumably from testing all 8MB of RAM — the system started! ...
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
         ?           ?
???????  ?  ???????  ???????  ???????   ?????????  ?  ???????  ???????  ???????
      ?  ?  ?     ?  ?     ?        ?   ?   ?   ?  ?  ?        ?        ?     ?
???????  ?  ?     ?  ?     ?  ???????   ?   ?   ?  ?  ?        ?        ?     ?
?     ?  ?  ?     ?  ?     ?  ?     ?   ?       ?  ?  ?        ?        ?     ?
???????  ?  ???????  ?     ?  ???????   ?       ?  ?  ???????  ?        ???????
            ?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



     IMPORTANT:  READ BEFORE USING THE AMOS SOFTWARE CONTAINED HEREIN.  THE
     USE  OF  AMOS  IS  GOVERNED  BY  THE  FOLLOWING  LICENSE.  USING  AMOS
     INDICATES  PURCHASER'S AGREEMENT TO ABIDE BY THE LICENSE. IF PURCHASER
     DOES NOT AGREE TO ITS TERMS, PURCHASER MAY CALL (714) 641-7698  (USA),
     0753-821922 (UK), OR 32-2-660 5093 (BELGIUM), WITH ANY QUESTIONS.





          AMOS SOFTWARE LICENSE AGREEMENT FOR ALPHA MICRO CPU SYSTEMS

     Alpha  Microsystems grants to the Purchaser of an Alpha Micro system a
     non-exclusive license to use the AMOS Software on one Alpha Micro  CPU
     system,  with no more than   8 serial IO ports, at a single  location,
     for the sole purpose of operating AMOS for  its  own  internal  needs.
     Any  adaptations  of  AMOS by Purchaser for its internal needs may not
     be  transferred  without  the   prior   written   consent   of   Alpha
     Microsystems.

     Purchaser agrees to maintain AMOS in confidence and not  to  transmit,
     lease  or  transfer  AMOS  or  any  portion thereof to any third party
     except with the same  Alpha  Micro  CPU  system.   This  agreement  is
     binding on all users and transferees of AMOS.

     AMOS  is  copyrighted  and is the sole and exclusive property of Alpha
     Microsystems.  Further,  it  is  an  unpublished  work  that  contains
     proprietary confidential information and trade secrets.

     Copyright (C) 1977, 1986, Alpha Microsystems
     All rights reserved
     
.;
.VER
              -- AMOS/L Version 1.3D(165)-1 Up and Running --           
.PARITY
... and immediately hung up on the
PARITY
command. Notice also the license, as promised, so if you find an AM system you want to boot, there you go. I very much doubt those phone numbers are valid, by the way.
The
PARITY
command has nothing to do with SCSI parity — it enables parity checking on the RAM. This should almost always be enabled as most systems shipped with parity RAM and the SIMMs in the Dimension board indeed looked like they were parity. My first thought was that the RAM might be defective, so I got a couple more parity SIMMs to try. Unfortunately these were double-sided and only one of them fit, and even then it didn't fix the problem.
Fortunately this command is not (strictly speaking) necessary to use the system. I put the old RAM back in for the time being, edited the image again to comment that statement out, and tried bringing the system back up.
.VER
              -- AMOS/L Version 1.3D(165)-1 Up and Running --           
.;ARITY
.;
.DEVTBL DSK1,DSK2,DSK3,DSK4,DSK5,DSK6,DSK7,DSK8,DSK9,DSK10,DSK11,DSK12,DSK13
.DEVTBL TRM,RES,MEM
.;
.BITMAP DSK,2834,0,1,2,3,4,5,6,7,8,9,10,11,12,13
.;
.ERSATZ ERSATZ.INI
.MSGINI 10K
.;
.SYSTEM SYSMSG.USA
.SYSTEM TRM.DVR[1,6]
.SYSTEM CMDLIN.SYS
.SYSTEM SCNWLD.SYS
.SYSTEM DCACHE.SYS/N/M/U 100k
.SYSTEM
.;
.MEMORY 0
.
We're in! AMOS/L refers to the original version of AMOS for 68000 CPUs, starting naturally with the AM-100/L, which then evolved into a full 32-bit version as AMOS/32 starting with the AM-2000. These early systems here can run either but the later true 32-bit systems must run AMOS/32. By the end of AMOS' development on the original hardware, the /L and /32 versions had been gracefully merged together, though this was not the case for the early 1.x versions we'll be using here.
What these lines did is define devices for each of the partitions on this disk image (Tom's image had 14, which is not at all unusual for large disks: my Eagle 450 has
274
), plus the terminal and memory, then the size of the block allocation map ("bitmap") for each of the partitions, then aliases for various PPNs (which AMOS calls ersatzes), then allocates 10K for the Inter-Task Communication System (something like System V shared memory if you squint), and loads various system extensions and messages after that. One of these extensions is a disk cache which I ended up removing because it's probably of little benefit with a drive this fast, but you can also load executables into system memory so that users don't have to load the executables into whatever memory slice you grant them. These executables, which usually end in
.LIT
, must be marked as "re-entrant" and "re-useable," which is to say they are sharing-safe because one executable image can be shared between multiple users and re-run in place without having to reload it. Notice the last
SYSTEM
line by itself, which appears to do nothing, but is needed to tell the monitor that nothing else will be loaded into it.
The final line relates to memory usage: AMOS allows you to set limits on any job, but an explicit argument of zero says the job may have as much RAM as it wants, which is probably desirable for the system console. Incidentally, it is absolutely possible to have insufficient memory to run
MEMORY
(considered harmful).
.systat
Status of AMOS/L Version 1.3D(165)-1 on Saturday, January 15, 1955 03:55:55 PM

TOM     TRM1    DSK0:1,4        00070070 RN  SYSTAT  8157724 bytes at    702744
5 jobs allocated on system, 1 jobs in use (1 logged in)
Total memory on system is 8192K bytes
System uptime is 57357:719:58

DSK0    41915 Blocks free       DSK1      Not mounted           
DSK2      Not mounted           DSK3      Not mounted           
DSK4      Not mounted           DSK5      Not mounted           
DSK6      Not mounted           DSK7      Not mounted           
DSK8      Not mounted           DSK9      Not mounted           
DSK10     Not mounted           DSK11     Not mounted           
DSK12     Not mounted           DSK13     Not mounted           

17 devices on system, total of 41915 blocks free
The
SYSTAT
command shows, reasonably, the status of the system. Our clock is a hair off and consequently we have an absolutely stupendous uptime figure, probably a math overflow, but it otherwise works and we can see all of our partitions (unmounted) plus the system disk (always
DSK0:
). Now that the system is up, we can modify
a copy of
the initialization file to our taste directly from the running system with
VUE
, AMOS's built-in visual editor. However, I should caution you that VUE only works well with an Alpha Micro terminal, or if you load an equivalent definition (
such as
terminfo
) as I've done with a couple of my machines here. Otherwise, you may have some luck with the TeleVideo 925 driver (
DSK0:TVI925.TDV[1,6]
), if it exists, which is close enough to VT100 to work sort of. Although the Alpha Micro Users Society and others distributed additional terminal driver code, VT100 and ANSI drivers were not a standard part of AMOS until later.
The reason I said you should only modify
a copy of
the initialization file is because if you do it wrong, you can make these earlier system unbootable. Here you might be able to recover by hacking the image file, but it's still not a good practice. Copy it first with
LOG SYS:
and
COPY TEST.INI=AMOSL.INI
and then edit
TEST.INI
. When you're ready, a utility called
MONTST
will allow you to try out the new file with something like, after a
LOG OPR:
so you have the right permissions,
MONTST AMOSL,TEST.INI
(
TEST.INI
must still be in
SYS:
, which is [1,4]). If the boot succeeds, you can swap the new file in. If it doesn't, you can hit the panel reset and go back to the old one.
With that working, the next version to try was 1.4. This got a little weird because messing around with a second job ended up zeroing out the version number (yes, literally "AMOS 0.0"). I decided to edit that out and reboot. Ignore the garbage here from the non-AM terminal type.
System booting - please wait . . . 

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
         ?           ?
???????  ?  ???????  ???????  ???????   ?????????  ?  ???????  ???????  ???????
      ?  ?  ?     ?  ?     ?        ?   ?   ?   ?  ?  ?        ?        ?     ?
???????  ?  ?     ?  ?     ?  ???????   ?   ?   ?  ?  ?        ?        ?     ?
?     ?  ?  ?     ?  ?     ?  ?     ?   ?       ?  ?  ?        ?        ?     ?
???????  ?  ???????  ?     ?  ???????   ?       ?  ?  ???????  ?        ???????
            ?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



     IMPORTANT:  READ BEFORE USING THE AMOS SOFTWARE CONTAINED HEREIN.  THE
     USE  OF  AMOS  IS  GOVERNED  BY  THE  FOLLOWING  LICENSE.  USING  AMOS
     INDICATES  PURCHASER'S AGREEMENT TO ABIDE BY THE LICENSE. IF PURCHASER
     DOES NOT AGREE TO ITS TERMS, PURCHASER MAY CALL (714) 641-7698  (USA),
     0628-822120 (UK), OR 32-2-660 5093 (BELGIUM), WITH ANY QUESTIONS.





          AMOS SOFTWARE LICENSE AGREEMENT FOR ALPHA MICRO CPU SYSTEMS

     Alpha  Microsystems grants to the Purchaser of an Alpha Micro system a
     non-exclusive license to use the AMOS Software on one Alpha Micro  CPU
     system,  with  no  limit  on   serial IO ports, at a single  location,
     for the sole purpose of operating AMOS for  its  own  internal  needs.
     Any  adaptations  of  AMOS by Purchaser for its internal needs may not
     be  transferred  without  the   prior   written   consent   of   Alpha
     Microsystems.

     Purchaser agrees to maintain AMOS in confidence and not  to  transmit,
     lease  or  transfer  AMOS  or  any  portion thereof to any third party
     except with the same  Alpha  Micro  CPU  system.   This  agreement  is
     binding on all users and transferees of AMOS.

     AMOS  is  copyrighted  and is the sole and exclusive property of Alpha
     Microsystems.  Further,  it  is  an  unpublished  work  that  contains
     proprietary confidential information and trade secrets.

     Copyright ~.} 1977, 1988, Alpha Microsystems
     All rights reserved

@1.;
.VER
             -- AMOS/32 Version 1.4(189)-1 Up and Running --           
.;ARITY
.;
.DEVTBL DSK1,DSK2,DSK3,DSK4,DSK5,DSK6,DSK7,DSK8,DSK9,DSK10,DSK11,DSK12,DSK13
.DEVTBL TRM,RES,MEM
.DEVTBL /VCR0
.DEVTBL /STR0
.;
.BITMAP DSK,,0,1,2,3,4,5,6,7,8,9,10,11,12,13
.;
.ERSATZ ERSATZ.INI
.MSGINI 10K
.;
.SYSTEM SYSMSG.USA
.SYSTEM TRM.DVR[1,6]
.SYSTEM VCR.DVR[1,6]
.SYSTEM STR.DVR[1,6]
.SYSTEM CMDLIN.SYS
.SYSTEM SCNWLD.SYS
.;SYSTEM DCACHE.SYS/N/M/U 400k
.RELIEF /300
Copyright 1985,1986 Software Designs, Spokane, WA 992090 
.SYSTEM
.;
.MOUNT DSK1:
.MOUNT DSK2:
.MOUNT DSK3:
.MOUNT DSK4:
.MOUNT DSK5:
.MOUNT DSK6:
.MOUNT DSK7:
.MOUNT DSK8:
.MOUNT DSK9:
.MOUNT DSK10:
.MOUNT DSK11:
.MOUNT DSK12:
.MOUNT DSK13:
.;
.MEMORY 0
.systat
Status of AMOS/32 Version 1.4(189)-1 on Saturday, January 15, 1955 03:00:00 PM

MASTER TRM1                       DSK0:1,4       RN  SYSTAT      7884466  bytes
5 jobs allocated on system, 1 jobs in use (1 logged in)
Total memory on system is 8M bytes
System uptime is 19085:855:50

DSK0    31170 Blocks free       DSK1    22870 Blocks free       
DSK2    22682 Blocks free       DSK3    20625 Blocks free       
DSK4     4149 Blocks free       DSK5    42200 Blocks free       
DSK6    60848 Blocks free       DSK7    64102 Blocks free       
DSK8    64102 Blocks free       DSK9    64102 Blocks free       
DSK10    64102 Blocks free      DSK11    64102 Blocks free      
DSK12    64102 Blocks free      DSK13    64102 Blocks free      

19 devices on system, total of 653258 blocks free
The image was actually an AMOS/32 build, but otherwise with the initial glitch ironed out it too worked just fine.
1.4 is the last release of the original AMOS 1.x. At this point I decided to go for the brass ring and try 2.3A, the last version of AMOS for these classic machines and the version my Eagles run. This also should have support for the Dimension board since it substantially postdates it. However, I could not get 2.3A to start at all on this 1000, showing only an error "12" on the status LEDs indicating it couldn't find the initialization file. This may relate to the age of the system PROMs in it.
As a hack suggested by Tom, I set up what AMOS calls a "subsystem driver," or what you might call "mounting more than one SCSI device at once."
The idea with this is, with the subsystem driver loaded, you now have both
DSKn:
devices representing partitions on SCSI device 0, and (with
DEVTBL
and
BITMAP
lines added as appropriate)
SUBn:
devices for partitions on SCSI device 1. I renamed the 2.3A image to
HD10.hda
and brought up both devices. That much worked and I was able to list files on the subsystem device, so since
MONTST
necessarily boots a new monitor, I next fed it the 2.3A monitor on
SUB0:
. That not only
didn't
work, it spewed garbage repeatedly to the console and made a shrill beeping racket until I switched everything off.
Let's see if the AM-1200 can do better.
The AM-1200 still had its interface plate on, so of course that had to come off first.
After that the BlueSCSI can simply plug into its SASI port as well. As 1.3D is right on the cusp of AM-1200 support I decided to start with the 1.4 image. Unfortunately, I could not get any console output with
AM1200=0
or
AM1200=1
, suggesting two bad ports exactly as the self-test said.
Finally I moved the console to
AM1200=2
. That started up, but the boot froze.
.;
.VER
               -- AMOS/32 Version 1.4(189)-1 Up and Running --         
.;ARITY
.;
.DEVTBL DSK1,DSK2,DSK3,DSK4,DSK5,DSK6,DSK7,DSK8,DSK9,DSK10,DSK11,DSK12,DSK13
.DEVTBL TRM,RES,MEM
.DEVTBL /VCR0
.DEVTBL /STR0
.;
.BITMAP DSK,,0,1,2,3,4,5,6,7,8,9,10,11,12,13
.;
.ERSATZ ERSATZ.INI
.MSGINI 10K
.;
.SYSTEM SYSMSG.USA
.SYSTEM TRM.DVR[1,6]
.SYSTEM VCR.DVR[1,6]
.SYSTEM STR.DVR[1,6]
.SYSTEM CMDLIN.SYS
.SYSTEM SCNWLD.SYS
.;SYSTEM DCACHE.SYS/N/M/U 400k
.RELIEF /300
Copyright 1985,1986 Software Designs, Spokane, WA 992090
RELIEF
is a command history utility and isn't essential either. In the hex editor I ended the image to turn on parity and comment out
RELIEF
, and the AM-1200 now started too. And that's why you never edit the system initialization file directly, because if you make an error such that you can't edit the file, your system becomes unbootable! (You can recover with a backup "warm start" tape, assuming you have one, but only starting with the later Eagles was there a firmware solution.)
The 2.3A image will also start with similar edits to its own initialization file. I've abbreviated the license text since you're probably familiar with it by now.
AMOS  is  copyrighted  and is the sole and exclusive property of Alpha
     Microsystems.  Further,  it  is  an  unpublished  work  that  contains
     proprietary confidential information and trade secrets.

     Copyright © 1977, 1998, Alpha Microsystems - All rights reserved
     The IPL Monitor is AMOSL.INI
     The IPL Initialization file is AMOSL.INI

       ****05-25-2000** AMOS Released MONITOR  **05-25-2000****

.XY=24
.VER
               -- AMOS Version 2.3A(488)-1 Up and Running --          
.PARITY
.;
.DEL TRMDEF
TRMDEF.LIT
.;
.LOAD DEVTBL
.;DEVTBL DSK
.DEVTBL TRM,RES,MEM
.DEVTBL /VCR0
.;DEVTBL /FLP0
.DEL DEVTBL
DEVTBL.LIT
.;
.LOAD BITMAP
.BITMAP DSK
.;
.ERSATZ ERSATZ.INI
.QUEUE  500
.MSGINI 10K
.;
.LOAD SYSTEM
.SYSTEM DCACHE.SYS/N 200K
.SYSTEM TRM.DVR[1,6]
.SYSTEM VCR.DVR[1,6]
.;SYSTEM STR.DVR[1,6]
.SYSTEM SYSMSG.USA
.SYSTEM SYS:AMSORT.SYS
.SYSTEM CMDLIN.SYS
.SYSTEM QFLOCK.SYS
.SYSTEM SCNWLD.SYS
.SYSTEM
.DEL SYSTEM
SYSTEM.LIT
.;
.MOUNT DSK:
.;
.SET DSKERR
.LOG SYSTEM SERVICE
Already logged in under DSK0:[1,4]
Ersatz name is SYS:
.MEMORY 0
.
I'll need to add a
BITMAP
to get the other
DSKn:
partitions working and mounted, but this is enough to get started. Notice that this version hails from May 2000 — nearly 14 years after the AM-1200 was announced. Not bad for backwards compatibility! Also note the use of a user name
SYSTEM SERVICE
, which is another way to specify a PPN in later versions, and is usually attached to [1,4] (
DEMO
is usually attached to [1,2]).
Because AMOS is a real-memory operating system, as I pointed out before, its system variables are visible and can be read (and, if you're adventurous or stupid, modified). This is most easily done from AlphaBASIC, which is included with every version of AMOS. For illustration and curiosity purposes we'll compare the values of the
system word
, which is always a 32-bit long at location 1024 ($0400), starting with 1.4. Do note that the reported version of AlphaBASIC does not in general correspond to the operating system version.
On the AM-1000, BASIC is slow to start because of the added RAM (it checks how much space it has every time it starts, and we've already told it with
MEMORY 0
that there's no limit, so it ends up walking nearly all 8MB).
.basic
AlphaBASIC Version 1.3(238)

READY
print byte(1024),byte(1025),byte(1026),byte(1027)
 48            0             5             4 
print word(1024),word(1026)
 48            1029 
bye
.
This is a value of $00300405, stored long in memory as $30000504, though AlphaBASIC only supports byte and 16-bit short ("word") access. Officially, the meaning of the bits is thus:
The value is hex, so we have bits set for programmer's toolbox routines, 8-bit character sets and language definition tables, as well as indicating we are running on an AM-1000 and the final
SYSTEM
command has been issued. There are bits for the 68020 and 68030, but 1.4 doesn't detect the Dimension's CPU as such.
Unsurprisingly, the AM-1200 reports exactly the same value, because it's a member of the AM-1000 family.
.basic
AlphaBASIC Version 1.3(238)

READY
print word(1024),word(1026)
 48            1029
On 2.3A, however, the system word is a little different:
.ver
               -- AMOS Version 2.3A(488)-1 Up and Running --          
.basic
AlphaBASIC Version 1.4(309)-3

READY
print word(1024),word(1026)
 49            17413
This is a value of $00314405, adding bits for extended format directories (something the old PROMs in this AM-1000 likely do not support) and the software interrupt system. These are features that don't exist in 1.x.
On my big Eagle 450 on 2.3A, running a slightly older version, we get a different value still:
.ver
              -- AMOS Version 2.3A(484)-15 Up and Running --           
.basic
AlphaBASIC Version 1.4(309)-2

READY
print word(1024),word(1026)
 20529         58369 
bye 
.
This is a value of $5031e401, the highest bit of which does not appear in Alpha Micro's table. I surmise bit $4000000 likely indicates a ColdFire since $2000000 indicates a 68060 (and the MCF5102 looks like a 68040 to user code, so it also gets bit $10000000). After that, we have the same values as the AM-1200 in 2.3A, plus adding the bits for 68020 and 68030 instruction support and removing the bit for the AM-1000.
By this time the ZuluSCSI had probed the Almighty Maxtor of Suck for nearly 24 hours. I figured this boded poorly for the quality of the resulting disk image, so I stopped it at this point, though it turned out that almost all of the sectors had been addressed anyway. I started paging through the log file.
[10719ms] SCSI ID 0 capacity 415436 sectors x 512 bytes
[10719ms] Drive total size is 202 MiB
[10719ms] SCSI Version 1
[10719ms] [SCSI0]
[10720ms]   Vendor = "MAXTOR  "
[10720ms]   Product = "LXT-213S        "
[10720ms]   Version = "4.57"
[10721ms]   Type = 0
[10805ms] Preallocating image file
[10825ms] Starting to copy drive data to HD00_imaged.hda
[10986ms] SCSI read succeeded, sectors done: 256 / 415436 speed 824 kB/s - 0%
[11136ms] scsiHostRead: received 10752 bytes, expected 32768
[11136ms] Read failed at byte 0
[11141ms] SCSI read from sector 256 was incomplete: expected 131072 got 32768 bytes
[11141ms] Failed to transfer 256 sectors starting at 256
[11142ms] Retrying.. 1/5
[11686ms] scsiHostRead: received 10752 bytes, expected 32768
[11686ms] Read failed at byte 0
[11691ms] SCSI read from sector 256 was incomplete: expected 131072 got 32768 bytes
[11692ms] Failed to transfer 256 sectors starting at 256
[11692ms] Retrying.. 2/5
[12092ms] Multiple failures, retrying sector-by-sector
[12114ms] SCSI read succeeded, sectors done: 257 / 415436 speed 28 kB/s - 0%
[12117ms] SCSI read succeeded, sectors done: 258 / 415436 speed 256 kB/s - 0%
That was a reasonably encouraging start considering the hard disk was practically a doorstop, but soon I started seeing a whole bunch of
[15772ms] Failed to transfer 1 sectors starting at 278
[15773ms] Retry limit exceeded, skipping one sector
[...]
[18690ms] Failed to transfer 1 sectors starting at 279
[18690ms] Retry limit exceeded, skipping one sector
[...]
[21607ms] Failed to transfer 1 sectors starting at 280
[21608ms] Retry limit exceeded, skipping one sector
and only somewhere around a third of the sectors turned out to be recoverable. But hey, let's hear it for freezing cantankerous old hard disks. We wouldn't have gotten even this much without it.
You can learn a lot about a hard disk by running
strings
on a disk image of it (here's
another example
of disk image spelunking) — like, for example, who owned it last.
Key Curriculum Project, founded in Berkeley, CA, ... well, actually, there's a company history in the disk image dated 1984 which appears to be part of a business plan, so I'll just let them tell it: "Key Curriculum Project is a family-owned educational publishing
company that has been in business since 1971.  It is the self-publishing
effort of two brothers [Steven and Peter Rasmussen].  They founded the company in order to maintain
control over their work. [...] A year and a half ago [i.e., 1982], Key Curriculum Project acquired an educational
software company, for which one of the brothers had already written
several programs.  In that year and a half, EduSoft, as the new
division is known, increased its offerings from twelve programs for
Apple, Atari, and TRS-80 to seventeen programs.  New programs are
currently being designed for future release. [...] One of Key's worktext series is very
innovative and has particular appeal in small private schools where
there is a good deal of student-teacher contact.  The rest of Key's
series work very well in secondary public schools.  They are designed
with minimal student-teacher contact in mind and stress basic skills
as opposed to experimental learning. [...] [EduSoft] programs are designed for
various grade level [sic], with some of the programs designed particularly
for the teacher.  Some of the new EduSoft products are designed and
being designed with a much broader market in mind.  That market is the
home market. [...] Print and disk duplication houses are used for the printing
and duplicating of the books, documetation and disks.  Consequently,
Key and EduSoft moved 400,000 books and 5000 disks with a total staff
of five full-timers and one part-timer." One of their example workbooks is shown above.
EduSoft achieved modest success with in-class software but little in the home market, where companies like
Springboard Software
and
DesignWare
were more dominant. On the other hand, Key had lasting impact with
The Geometer's Sketchpad
, a spinoff of the National Science Foundation-funded Visual Geometry Project at Swarthmore College. Under the direction of faculty Eugene Klotz and Doris Schattschneider, the program became focused on interactive ways to explore Euclidean geometry. As proofs-of-concept using videotape were insufficiently hands-on, Klotz approached one of his former students, Nicholas Jackiw, to develop a software implementation. Klotz had in mind a concept he called "Sketchpad" where students could type in coordinates and then pan over figures without having to have substantial art ability. Jackiw, a Macintosh user, found this un-Mac-like and instead delivered his own take on the idea where a user could draw a figure with the mouse, picking points in any order, and then drag any of its sides and vertices dynamically which moves other sides and vertices as required. Klotz was delighted with Jackiw's innovations and the concept underwent several years of refinement until Steven Rasmussen, fascinated by the concept, picked up the product for commercial distribution; the first release was in 1991. Key later spun off KCP Technologies, also helmed by Steven Rasmussen, which maintained and ported the product to Windows. McGraw-Hill bought Key in 2012 and continued to publish their core written curricula, supporting
TGS
officially until 2019. A free modernized
beta test
is available for Windows and macOS (the screenshot is from my M1 Air running Tahoe).
At Key, this machine seemed to be primarily used for typical Alpha Micro tasks in the typical Alpha Micro office environment: letters and accounting. For example, there were lots of contracts and letters, some product blurbs and sales information, and even a few detailed internal office procedures. Some examples for flavour (proprietary or personal information censored):
THIS AGREEMENT made as of day _____ of _______________, 19___, between
_________________________________________________, hereinafter called
"Consultant," and KEY CURRICULUM PROJECT, INC., Berkeley, California,
hereinafter called "KEY."
After carefully evaluating [redacted], we have decided
that we cannot market it successfully.  
We think that you have a clever idea, however, the user
interface needs work.  The programming is functional but
not of the polished nature being demanded by the ever
more sophisticated educational computer community.
You should realize that your use of lower case prevents
the program from being used on an Apple II+.  You should
use a high resolution character generator to create 
nic [sic] looking upper and lower case text.
Enclosed you will find all copies of the program and 
documentation that you submitted to us.  We have not 
retained any copies of the program or documentation.
Thank you for allowing EduSoft to evaluate your program.
We wish you every success in marketing it elsewhere.
Sincerely,
Steven Rasmussen
Editor
TRS-80 (48K Model III or 4)     $49.95
            TEACH IT!
    LESSON AUTHORING SYSTEM
Create customized courseware easily
and professionally with this powerful 
Lesson Authoring System. No programming 
knowledge is needed. Just follow the 
on-screen instructions to input your 
lessons into TEACH IT!'s flexible format. 
Once you've created a customized unit, 
TEACH IT! will present it to your 
students.  As students progress, TEACH 
IT! gives students immediate feedback 
and records their progress for your review.
/y 65
/X 70
/FLAG US _
/UNDERSCORE BS
/br              
/C EDUSOFT RELEASES MAGIC PIANO MUSIC LEARNING SYSTEM
/C _Powerful New Creative Tool for Learning Music_
/apr 5 1
EduSoft, publisher of educational software, announces the release of the
Magic Piano Music Learning System.  The package includes three new programs:
the Magic Piano, a music creativity tool, and two related skill building
programs, the Rhythm Game and the Melody Game.
"The Magic Piano is unlike any other music software currently available,"
states EduSoft Editor Steven Rasmussen.  "While other programs are
difficult to use or presuppose some knowledge of music, total beginners
can play the Magic Piano in minutes.  This unique teaching program
introduces the formal aspects of music through informal creative play.  
The Magic Piano combines the excitement of construction set programs with 
the best features of drill and practice software.  The skill building 
components of the package support and enhance the creative process."
The Magic Piano transforms the Apple keys into piano keys.  As users play
songs on the keyboard, the program instantly scores and displays the
song on the screen.  Compositions can be played back, edited, stored, or
printed with a few simple keystrokes.
[...]
The Magic Piano Music Learning System is currently available for the Apple
II/II+/IIe/IIc family of computers and costs $49.95.
For more information write to EduSoft, P.O. Box [redacted], Berkeley, CA  94702.
Or, call toll-free 1-800-[redacted].  In CA, AK and HI call 415-[redacted].
In these Key To Decimal booklets, you will learn to work with decimal
numbers.  Decimal numbers are an extension of the Hindu-Arabic number 
system, the number system that we use today.  
The number system we use today seems perfectly natural.  It's based on
the number 10, the number of fingers on our two hands.  All number
systems however have not been base ten systems.
Based on correspondence on the hard disk, Key started with an AM-100/T. One of the most significant applications it ran was the PMIS suite from VORT Corporation, then based out of Palo Alto. PMIS nowadays would be considered a primitive early example of customer relationship management software, which for this era mostly meant mail merge and mass mailings. A significant amount of sales and shipping data was also tracked on this machine. I also found a simple blackjack game and Dravac's Game of Wizard (turn-based conquest strategy game) because even educational vendors need to relax sometime.
Paging through some more came up with the main system initialization file from 1994, consistent with the handwritten date on the hard disk. No later one was easily apparent.
; RBF - 05/03/88 - decrease JOBS 21 to JOBS 10, add job BKGRND for CRT610
; RBF - 05/03/88 - change TRMDEF TVNEW to SOROC to enable control-V in VUE
; SMW - 08/30/89 - CHANGE FOR AM1000
; MLW - 10/10/89 - Change Term Definitions (3,4,6) to support MACS
; MLW - 09/27/90 - Add Jobs 12-13, Modify 11-13 to Macs    
; MLW - 10/04/90 - MODIFY JOB 4 TO AM
; MLW - 02/26/91 - Modify Job 10 from AM to Mac
; A.C.S. 03/27/91- Added 2 cables for new Mac jobs
; MLW - 04/18/91 - Modify JOB2 to greater mem
; MLW - 05/15/91 - Modify old Televideo terminals to Wyse 50 mode.
; MLW - 05/16/91 - Modify JOB14 to Wyse 50 mode (TVI925)
; RBF - 10/18/91 - Change TRMnn to real people names !!!
; MLW - 01/02/92 - Change TRM14 to Mac (Scott!)
; Interlink - 02/16/92 - Install Dimension-030 and SuperDisk
; MLW - 04/16/92 - Change JOB4 to Mac (Cherlondia)
; MLW - 08/24/92 - Terminal maintenance
; MLW - 09/09/92 - Change JOB9 back to TVI925
; MLW - 12/16/92 - Change Job3 to Mac!
; MLW - 01/18/93 - Change Job9 to Mac/change names for Jobs4/5/6
; MLW - 02/05/93 - Change Monica/Denee/John to new names
; MLW - 02/08/93 - Modify to move ICACHE statement to bottom of TRMDEF section
; MLW - 02/17/93 - Mofify .INI to move 2 jobs to MAC
; MLW - 09/07/93 - Modify .INI for new space layout
; MLW - 02/22/94 - Modify .INI to increase Monte memory allocation
; MLW - 1994/08/01 - Modify .INI to current names
; MLW - 1994/08/06 - Modify .INI for modem (RBF)
; A.M.S.O. 8-9-94  -MOVED MODEM FROM PIIC.#11 TO AM1000 PORT 1 -
; PIICEON PORT BAD HAD TO DISCONNECT PRINTER #3 TO FREE PORT J.B.
JOBS 25
;PARITY; removed to stop status 9 crashes (RBF,3/17/93,Hunt's suggestion)
TURBO ON
JOBALC JOB1,JOB2,JOB3,JOB4,JOB5,JOB6,JOB7,JOB8,JOB9
JOBALC JOB10,JOB11,JOB12,JOB13
JOBALC JOB14    ;                      
JOBALC JOB15    ;               
JOBALC BKGRND
JOBALC SPOOL,SPOOL2,SPOOL3,SPOOL4
There's a few interesting things here. It appears they upgraded directly from the S-100 AM-100/T (if they got it in 1988, it may have been second-hand) to this AM-1000 on August 30th, 1989, and they also had a number of Macintoshes in this office that required terminal changes. Other strings show they exchanged data with a custom AlphaBASIC program that could convert files like Microsoft Word 5.1 documents. The dates also demonstrate the system was in operation at least as long as the date on the Maxtor, and seems to have been exceptionally well-maintained by experts (several names I know from Alpha Micro history appear in other places such as Arjun Khalsa and Bob Fowler). A regular backup job kept a detailed log. The last unambiguous date I can find is
1994-OCT-10 12:31:26 BEGIN CUSTRK REPORTING
1994-OCT-10 06:25:58 END CUSTRK REPORTING
1994-OCT-10 06:25:59 BEGIN STREAMER CERTIFICATION
If there was anything more recent, it went down on the bad sector ship. That means this specific system operated from 1989 to at least 1994, running software and data files generated years earlier. This longevity in service was exactly Alpha Micro's value proposition.
Continuing through the initialization file, this system got its '030 upgrade on February 16, 1992 and it looks like Interlink themselves did the install. It doesn't say when the Piiceon card was added but it does say at least one of its ports went bad, and the various entries with specific port numbers suggest the machine did (as we earlier hypothesized) get the serial card upgrade first.
But the most interesting part is that they
also
had to comment out the
PARITY
line to get it to start. A front panel LED code of 9 is indeed a parity failure. The immediate next line is a command
TURBO ON
that sounds suspiciously like what you would need to get the accelerator card fully running.
What about a driver for the Piiceon? For that we turn to the list of terminals immediately following.
TRMDEF COMPUT,  AM1000=0:9600,  soroc,200,200,200
XY=0
TRMDEF MMCYN,   PI16IF=0:19200, VT100,190,190,40 
TRMDEF TONY,    PI16IF=1:19200,  VT100,190,190,40 
TRMDEF DIANNE,  PI16IF=2:19200, VT100,190,190,40
TRMDEF STACIE,  PI16IF=3:19200, VT100,190,190,40
TRMDEF OE,      PI16IF=4:19200, VT100,190,190,40
TRMDEF JEFF,    PI16IF=5:19200, VT100,190,190,40  
TRMDEF KATE,    PI16IF=6:19200, VT100,190,190,40
;TRMDEF MODEM,  PI16IF=11:2400, SOROC,190,190,40 ;BAD PORT
TRMDEF MONICA,  PI16IF=12:19200,VT100,190,190,40
TRMDEF DENEE,   PI16IF=13:19200,VT100,190,190,40
TRMDEF JAY,     PI16IF=14:19200,VT100,190,190,40
TRMDEF SCOTT,   PI16IF=15:19200,VT100,190,190,40
TRMDEF ADAMC,   PI16IF=16:19200,VT100,190,190,40
TRMDEF JILL,    PI16IF=17:19200,VT100,190,190,40
TRMDEF NEC,     PI16IF=7:9600,  TELTYP,200,200,200
TRMDEF TI810,   AM1000=2:9600,  TELTYP,200,200,200
TRMDEF TI810A,  PI16IF=10:9600, TELTYP,200,200,200
TRMDEF MODEM,   AM1000=1:2400,  SOROC,200,200,200
TRMDEF DUMMY,   PSEUDO,         NULL,200,200,200
TRMDEF DUMMY2,  PSEUDO,         NULL,50,50,50
ICACHE DSK0: 2050K 7777777/50%
The console was a Soroc of some sort, another Orange county company then based out of Anaheim, which Alpha Micro used and sold as terminals until they started rebadging Wyses under their own name. However, most of the users — and this looks like Key eventually became a
very
busy office — were apparently on Macintoshes using a VT100 driver (likely from AMUS) loaded secondarily onto the system. These users must have been connected to the Piiceon since their high port numbers could not have been directly on the AM-167 logic board, and there are no other port drivers (
PSEUDO
is a trivial internal driver used for simple links such as serial printers).
Thus, based on the command lines we saw in the initialization file, we're looking for
TURBO.LIT
and
PI16IF.IDV
. Looking further through the image, we can find their hash totals and locations, apparently on
DSK2:[44,1]
.
002a2cc0  20 34 36 30 2d 32 31 33  2d 35 33 31 2d 35 37 31  | 460-213-531-571|
002a2cd0  20 20 0d 0a 44 53 4b 32  3a 54 55 52 42 4f 2e 4c  |  ..DSK2:TURBO.L|
002a2ce0  49 54 5b 34 34 2c 31 5d  20 20 20 20 20 20 20 20  |IT[44,1]        |
002a2cf0  20 20 20 20 20 20 20 20  20 20 31 2e 30 28 39 29  |          1.0(9)|
002a2d00  20 20 20 20 20 20 20 20  20 20 20 20 34 35 36 2d  |            456-|
002a2d10  31 33 31 2d 34 36 33 2d  37 36 33 20 20 0d 0a 44  |131-463-763  ..D|
002a2d20  53 4b 32 3a 54 55 52 42  4f 2e 4f 4c 44 5b 34 34  |SK2:TURBO.OLD[44|
002a2d30  2c 31 5d 20 20 20 20 20  20 20 20 20 20 20 20 20  |,1]             |
002a2d40  20 20 20 20 20 31 2e 30  28 38 29 20 20 20 20 20  |     1.0(8)     |

002a2800  37 15 20 20 20 20 20 20  20 20 20 20 20 30 35 35  |7.           055|
002a2810  2d 37 33 30 2d 36 34 37  2d 36 34 35 20 20 0d 0a  |-730-647-645  ..|
002a2820  44 53 4b 32 3a 50 49 31  36 49 46 2e 49 44 56 5b  |DSK2:PI16IF.IDV[|
002a2830  34 34 2c 31 5d 20 20 20  20 20 20 20 20 20 20 20  |44,1]           |
002a2840  20 20 20 20 20 20 32 2e  30 28 31 30 35 29 20 20  |      2.0(105)  |
002a2850  20 20 20 20 20 20 20 20  34 33 37 2d 37 30 35 2d  |        437-705-|
002a2860  34 30 36 2d 30 34 33 20  20 0d 0a 44 53 4b 32 3a  |406-043  ..DSK2:|
002a2870  50 49 31 36 49 46 2e 4d  36 38 5b 34 34 2c 31 5d  |PI16IF.M68[44,1]|
002a2880  20 20 20 20 20 20 20 20  20 20 20 20 20 20 20 20  |                |
Impressively, the Piiceon driver appeared to even have source code. It might be a chore to actually find their sectors and walk them, though, so I decided to look first on my Eagle 450 since Alpha Micros have a way of accumulating historical cruft.
.dir /h/v sys:turbo.lit
TURBO  LIT 6     456-131-463-763   1.0(9)           DSK0:[1,4]

.dir /h/v dvr:pi16if.idv
PI16IF IDV 3     001-710-531-515   2.0(106)         DSK0:[1,6]
There they are! The hashes don't match because they are slightly later versions,
but the files are there,
and very close in version number! I first tried running it directly on the Eagle 450, which was a little dumb on my part because if anything was going to unsettle the system it would be something like this. Fortunately, although it seemed to detect there was compatible hardware, it didn't try to change anything.
.turbo /h
%Error: TURBO must be run before final SYSTEM
Usage:  TURBO ON, OFF
Pulling the file from the 450 and looking at it,
% strings turbo.lit 
$g8.
Usage:  TURBO ON, OFF
        ~{N
CPU Turbo is 
CPU type not supported by this command
[...]
Note: Run 'TURBO OFF' before MONTST
[...]
Dimension-030 routines installed
Copyright 1991 by InterLink Systems, Inc.
%Error: TURBO must be run before final SYSTEM
?Not running Dimension-030!
A quick and dirty cross-disassembly (swapping the shorts back to big-endian, naturally) shows that it patches the operating system to twiddle the 68020-and-later Cache Control Register. The relevant code looks like this, heavily using Alpha Micro's A-line operating system traps to do common tasks.
0000006e : 4a38 fe06      TST      $0000fe06
00000072 : 7e09           MOVEQ    #$09,D7
00000074 : 4e7b 7002      MOVEC    D7,CACR
00000078 : 600a           BRA      $00000084
0000007a : 4a38 fe03      TST      $0000fe03
0000007e : 7e08           MOVEQ    #$08,D7
00000080 : 4e7b 7002      MOVEC    D7,CACR
00000084 : a00c           TYPE

00000086 : 43 50 55 20 54 75 72 62 6f 20 69 73 20 00         CPU Turbo is .  

00000094 : 4e7a 7002      MOVEC    CACR,D7
00000098 : 0807 0000      BTST     #0,D7
0000009c : 6708           BEQ      $000000a6
0000009e : a00c           TYPE

000000a0 : 4f 4e 00 00                                       ON..            

000000a4 : 6006           BRA      $000000ac
000000a6 : a00c           TYPE

000000a8 : 4f 46 46 00                                       OFF.            

000000ac : a010           CRLF
000000ae : a012           EXIT
I'm not sure what the
TST
s are doing, but the rest of it turns on or off the instruction cache with the EI bit (bit 0) and clears it with the CI bit (bit 3). While the driver accesses the CACR in multiple places, it only ever addresses those two bits — the data cache doesn't seem to be used at all. It also does a substantial amount of patching in low memory, copying specific portions of itself into what look like regions of the operating system monitor. It is not clear to me what these patches do either.
In any event, this is surely our CPU driver. Unfortunately, with only one terminal on the AM-1000 and its small buffers, transferring binary files to it is a pain because the terminal driver keeps interfering with Kermit, so we'll have to escape and encode it by some other means. Although it should be possible to write something to convert, say, a Motorola S-record, I decided to just send over raw binary pseudo-ops for the M68 macroassembler and have it build the file as a binary directly. This results in an obviously long-winded file that's bigger than it needs to be, but we only have to do this once and we can slowly squirt it into VUE with an intercharacter delay. Here is a simple Perl script to do that.
#!/usr/bin/perl -s

$/ = \2; $offs = 0;
$lf = ($lf) ? "\r\n" : "\r";
print STDOUT "\tradix 10$lf";
while(<>) {
        $w = unpack("H*", $_);
        die("unexpected odd byte at $offs: $w\n") if (length($w) != 4);
        $k = hex(substr($w, 2, 2) . substr($w, 0, 2));
        print STDOUT "\tword $k$lf";
}

print STDOUT "$lf\tend$lf$lf";
This generates the file you'll upload, flipping the words back to big-endian for purposes of assembly. Since we're uploading this into a text editor, our line endings must be carriage returns, just like typing on an Alpha Micro terminal.
For the transfer, I chose an intercharacter delay of 10ms which seemed like a good safety margin. You can adjust this depending on your system speed and buffer size. I did the transfer on the AM-1200 in AMOS 2.3A so that way I could "upload" it to the AM-1000 by mounting the 2.3A image as a subsystem and copying the resulting file to AMOS 1.4. You can do these next steps in any PPN, but I was in
MAC:
(sometimes a/k/a
M68:
) where most such assembly language programs go, typically [7,7].
% picocom -b19200 /dev/cu.usbserial-10 --send-cmd="ascii-xfr -snv -c10"
[...]
.vue turbo.m68
AlphaVUE 3.1(531)-2
DSK0:TURBO.M68 does not exist, do you wish it created? Y
Loading DSK0:TURBO.M68
Press ESCAPE at this point (you may or may not have a coherent screen due to your terminal type) and you will be in the editor. Now upload the file (in
picocom
, Ctrl-A followed by Ctrl-S).
[...]
*** file: turbo.m68
$ ascii-xfr -snv -c10 turbo.m68
ASCII upload of "turbo.m68"
Line delay: 0 ms, character delay 10 ms
[...]
7 1ne 014347 0
7 17(e7)n7*d7+
14.1 Kbytes transferred at 83 CPS... Done.

*** exit status: 0 ***
You'll see output, which may be garbage, for each line, but at the end you should see roughly the number of lines in the converted file. Now press ESC again and type (blindly?)
finish
to you'll go back to the dot prompt. Let's assemble it.
.m68 turbo.m68

== Alpha Microsystems Macro Assembler Version 2.0(187) ==

Processing TURBO.M68

Phase 1:   Work area: 479208 bytes, 4 used
Phase 2:   Object file finished
Phase 4:   Program  file finished
           [Program size = 2866. bytes]
.dir /h/v turbo.lit
TURBO  LIT 6     456-131-463-763   1.0(9)           DSK0:[7,7]
.turbo
?Not running Dimension-030!
An F2 turned up on the status LED, but this seems to be expected behaviour on a pre-030 CPU. I remounted the 2.3A volume as SUB: from the AM-1000 and copied it over.
.log
Logged into -> <SYS:> DSK0:[1,4]
.copy turbo.lit=sub0:turbo.lit[7,7]
SUB0:TURBO.LIT[7,7] to TURBO.LIT
Total of 1 file transferred
.dir sys:turbo.lit /h/v
TURBO  LIT 6     456-131-463-763   1.0(9)           DSK0:[1,4]
But even simply running this reconstituted
TURBO.LIT
from the command line, which hashes the same as the working executable on the AM-1200 and should merely exit since we are fully booted, causes the AM-1000 to lock up hard. It's possible the patches it tried to install wrecked the monitor image.
We do at least know how it works and what it seems to support, though, so as an alternative we'll try our own simpler driver that twiddles with the CACR bits ourselves. Since the OS knows nothing about the D-cache and the driver apparently doesn't even support it, we'll also solely enable the I-cache and clear it and see what happens.
First, a baseline measurement on the AM-1200, which will be closest for this purpose to an unmodified AM-1000. AMOS 1.4 doesn't have
SI.LIT
, Alpha Micro's standard benchmarking utility, so when we get to the AM-1000 we'll run it from the subsystem image. As another point of comparison we'll also execute a simple-minded delay loop in BASIC as AlphaBASIC of this vintage will not treat such a loop as dead code. Here's the AM-1200 on 1.4:
.basic
AlphaBASIC Version 1.3(238)

READY
10 for i=0 to 10000:next
run
COMPILING
Compile time was 0.02 seconds, elapsed time was 0 seconds

CPU time was 2.60 seconds, elapsed time was 3 seconds

READY
run

CPU time was 2.60 seconds, elapsed time was 3 seconds

READY
bye
.
And now on 2.3A, running the
SI
benchmark beforehand.
.ver
               -- AMOS Version 2.3A(488)-1 Up and Running --                  
.si dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(114)

               Computer Type: AM-1000 or AM-1200
              Main Processor: 68000
                Co-Processor: None
                 MMU present: No
            Operating System: AMOS 2.3A(488)-1
          Boot PROM revision: Unknown
              Number of SSDs: 1
                Total Memory: 1024 K-bytes
     Resident Monitor Memory: 369 K-bytes

     Computing Index (CX), relative to AM-100:    4.6
     48 bit FP Index (4X), relative to AM-100:    4.6
Floating Point Index (FX), relative to AM-100/L:  1.0
          Disk Index (DX), relative to ST-506:    3.0
.basic
AlphaBASIC Version 1.4(309)-3

READY
print word(1024),word(1026)
 49            17413 
10 for i=0 to 10000:next
run
COMPILING
Compile time was 0.01 seconds, elapsed time was 0 seconds

CPU time was 1.72 seconds, elapsed time was 1 seconds

READY
run

CPU time was 1.72 seconds, elapsed time was 2 seconds

READY
bye
This version of BASIC is definitely quicker on the AM-1200 (the change in the system word is due to AMOS 2.3A implementing the new software interrupt system), so we'll want to make absolutely sure we only compare apples with apples. Fortunately, we can run this version of AlphaBASIC on the AM-1000 from the subsystem device also. Here's the AM-1000's baseline results, booted without messing with the CACR:
.basic
AlphaBASIC Version 1.3(238)

READY
10 for i=0 to 10000:next
run
COMPILING
Compile time was 0.01 seconds, elapsed time was 0 seconds

CPU time was 1.50 seconds, elapsed time was 0 seconds

READY
run

CPU time was 1.50 seconds, elapsed time was 0 seconds

READY
bye
.sub0:si.lit[1,4] dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(114)

               Computer Type: AM-1000 or AM-1200
              Main Processor: 68000
                Co-Processor: None
                 MMU present: Yes
            Operating System: AMOS/L 1.4A(189)-2
          Boot PROM revision: Unknown
              Number of SSDs: 1
                Total Memory: 8192 K-bytes
     Resident Monitor Memory: 89 K-bytes

     Computing Index (CX), relative to AM-100:    7.5
     48 bit FP Index (4X), relative to AM-100:    7.4
Floating Point Index (FX), relative to AM-100/L: Not computed. Needs AMOS 2.0
          Disk Index (DX), relative to ST-506:    3.1
.sub0:basic.lit[1,4]
AlphaBASIC Version 1.4(309)-3

READY
print word(1024),word(1026)
 48            1029 
10 for i=0 to 10000:next
run
COMPILING
Compile time was 0 seconds, elapsed time was 0 seconds

CPU time was 1.60 seconds, elapsed time was 0 seconds

READY
run

CPU time was 1.59 seconds, elapsed time was 0 seconds

READY
bye
Notice that the 68030 MMU is detected, and the result on the newer BASIC was in fact slightly slower.
Being careful to compare only our run results on AlphaBASIC under AMOS 1.4, the AM-1200, clocked also at 8MHz, took 73% longer. That's actually pretty impressive because, with no caches on, nearly all the gain with the 68030 card is microarchitectural (32-bit ALU in the '030 versus 16-bit in the '000, fewer clocks required for many instructions, etc.).
However, this gain is almost completely erased with the faster AlphaBASIC in AMOS 2.3A, which narrows the speed gap to just eight percent. On the other hand, the testable CPU benchmarks at baseline are 63% faster on the AM-1000 generally, so I'm suspecting the AMOS 2.3A BASIC may have other confounders involved.
Now let's write our assembler code, this time on the AM-1000 directly.
.log m68:
Transferred from <SYS:> DSK0:[1,4] to <M68:> DSK0:[2,3]
.type cacr.m68

        search sys
        search syssym
        search trm

        phdr -1,,

        supvr
        lword ^H4e7a1002
        dcvt 0,ot$trm
        type <... >
        bset #0,d1
        bset #3,d1
        lword ^H4e7b1002
        nop
        lword ^H4e7a1002
        dcvt 0,ot$trm
        crlf
        lsts #^H2000
        exit

        end
This code first emits a header saying it is neither reentrant nor reusable, since it monkeys with CPU registers. It jumps to supervisor mode using the official Alpha Micro A-line system call, then reads the current value of the CACR (we need to write this instruction out manually since M68 of this vintage doesn't understand it), displays it using two more utility traps, turns on all the bits we need, stores it into the CACR (also written out longhand), pauses (
TURBO.LIT
does this, so I inserted one just in case it was significant) and reads the CACR back for confirmation. We must set supervisor mode to mess with the CACR or we will trap into the monitor. At the end we jump back to user mode (the
LSTS
macro assembles exactly to
MOVE.W ,SR
) and exit to the dot prompt.
.m68 cacr.m68

== Alpha Microsystems Macro Assembler Version 2.0(178) ==

Processing CACR.M68

Phase 1:   Searching DSK0:SYS.UNV[7,7]
           Searching DSK0:SYSSYM.UNV[7,7]
           Searching DSK0:TRM.UNV[7,7]
[...]
Phase 4:   Program  file finished
           [Program size = 62. bytes]
.cacr
0... 1
Well, it didn't crash this time! And that's the bit we expect to see set after a successful store (the cache clear bit does not persist). Does it make a difference?
.basic
AlphaBASIC Version 1.3(238)

READY
10 for i=0 to 10000:next
run
COMPILING
Compile time was 0.01 seconds, elapsed time was 0 seconds

CPU time was 1.51 seconds, elapsed time was 0 seconds

READY
run

CPU time was 1.50 seconds, elapsed time was 0 seconds

READY
bye
.cacr
1... 1
Nope, and the bits were still set when we left, so it wasn't like they got turned off. What about
SI
and the later AlphaBASIC?
.sub0:si.lit[1,4] dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(114)

               Computer Type: AM-1000 or AM-1200
              Main Processor: 68000
                Co-Processor: None
                 MMU present: Yes
            Operating System: AMOS/L 1.4A(189)-2
          Boot PROM revision: Unknown
              Number of SSDs: 1
                Total Memory: 8192 K-bytes
     Resident Monitor Memory: 89 K-bytes

     Computing Index (CX), relative to AM-100:    7.5
     48 bit FP Index (4X), relative to AM-100:    7.5
Floating Point Index (FX), relative to AM-100/L: Not computed. Needs AMOS 2.0
          Disk Index (DX), relative to ST-506:    3.1
.sub0:basic.lit[1,4]
AlphaBASIC Version 1.4(309)-3

READY
print word(1024),word(1026)
 48            1029 
10 for i=0 to 10000:next
run
COMPILING
Compile time was 0 seconds, elapsed time was 0 seconds

CPU time was 1.60 seconds, elapsed time was 0 seconds

READY
run

CPU time was 1.59 seconds, elapsed time was 0 seconds

READY
bye
I tried adding another
bset #4,d1
to see if adding the burst enable bit made any difference, and it didn't crash and duly reported the bit was set, but it didn't make any difference either.
This seems to be as good as we can get for the AM-1000's upgrade card. We already know it's defective because it can't enable its own memory parity, so perhaps there is something wrong with the cache interface as well. Worse still for the AM-1000, the AM-1200 isn't out of the race yet: we've got an upgrade for
it
.
That upgrade turned out to be in our
second
AM-1200, as we'll find when we get the lid off.
This particular unit is rather worse for wear, not just the front badge, but also a bent back panel which suggests it was really thrown around at one point. Even steel won't be impervious to a couple of good bangs.
Our machine here is still part of the AM-1000 family, but now a rather later AM-1000-71 revision A00 with a correspondingly later serial number.
The logic board is still broadly similar to the prior unit, though consistent with its poor treatment there's a bit of oxidation on the logic board tray. Fortunately it isn't bent like the rear is.
Still, there are several important changes. The first is that the 68000 CPU has been replaced with a 68010 CPU (remember, the AM-1200 was descended from the doomed AM-1100E, which used the '010). The 68010 was in general a drop-in replacement right down to the pinout, with the only notable compatibility change being to make
MOVE SR
supervisor-mode only so that the upper supervisor bits were not visible to user code. Being an uncommon instruction to begin with, most programs were unaffected, and programs that were could either trap to an operating system library or be patched to use a new
MOVE CCR
instruction that didn't expose the naughty parts. These and other related changes, particularly its ability to restart instructions, made it much more amenable to virtual memory and timesharing than the original 68000. Its other benefit was a trivial 6-byte, two-instruction loop cache that could greatly accelerate certain tight loops by as much as fifty percent. Amiga and Atari ST users adopted the chip nearly immediately, tolerating the few applications that would crash (patches were later available), and even fewer AMOS applications of significance were affected by the change because most of them were in AlphaBASIC.
The other big change with the 68010 AM-1200 was a 10MHz clock (off a 20MHz crystal instead of 16MHz), 25% faster than the 68000 in previous AM-1200s and the stock AM-1000. The 68000 had only just come out with a 10MHz part in 1981, but Alpha Micro was already using the 10MHz 68010 in the AM-1500 and AM-1100E, and it seems the only reason early generation AM-1200s had the same 8MHz 68000s in them was cost.
Otherwise, the only other major change was the video ASIC being replaced by a Motorola-fabbed PLCC carrying a later designation number ("ICC0000200"), suggesting some refinements. The NEC D780C-1 has also been replaced by a real Zilog Z80 but that wouldn't have been otherwise noticeable.
I'd love to power this unit up, but when I tried to I remembered why it was in storage in the first place: it did not, in fact, power up. The fan turned on but there was no activity at all from the logic board or the front panel.
In the grotty dirty bottom of the case were two more things that didn't work: a Micropolis SASI hard disk, and the likely culprit, the power supply. I have not personally had good luck with Micropolis drives of this era but others are more complimentary, and the general consensus is that they beat the MTBF in an era where the MTBF was often pretty crummy. I think the best that can be said is it's not a Maxtor.
I got no voltage at all (there should be at least +12V and +5V) on the Molex power connectors, so the next thing to do is disconnect the board and move it to the working AM-1200's power supply to see if we get a pulse. Although the connector from the power supply is keyed, take care to note how the red stripes on the other ribbon cables are oriented — those connectors are
not
keyed, and while it is unlikely you'd blow something up misconnecting those (this is not true of Eagles, however), putting the connectors in upside down obviously won't work.
After that, the whole tray can simply be pulled back and up and lifted out from the hinges, and we will swap it with the known working board.
Here's a high level comparison on the boards, by the way. The old board has the circular stickers on the EPROM windows. Notice how little has physically changed between revisions.
Plugged in to the known-good power supply, this second board powers right up. Let's run the self-test. I got output right away on port 0.
====================
| System Self-Test |
====================

System configuration:
 Processor - 68010
 Memory detected - 1024K bytes
 Number of serial ports - 11
 VCR interface
 Multi-communications ports

Verify the proper configuration was detected ..

TESTING MEMORY ..
MEMORY TEST passed - 1024K bytes

TIMER TEST passed

SERIAL PORT TEST
 !"#$%&'()*+,-./0123456789:;<=>
 ?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]
 Port # 0 passed
 Port # 1 passed
 Port # 2 passed
Testing Expansion Ports
8 serial ports tested
 Port # 5 passed
 Port # 6 passed
 Port # 7 passed
 Port # 8 passed
 Port # 9 passed
 Port # 10 passed
 Port # 11 passed
 Port # 12 passed

VCR TEST
 Ram test passed
 Remote not detected, write/read test being bypassed

MULTI-COMMUNICATIONS PORTS TEST
 Restore CPU passed
 Peripheral I/O test passed
 Counter/Timer test passed
 Serial I/O output
 Parallel port output - No printer connection detected


====================
| System Self-Test |
====================

System configuration:
[...]
As with the other system, two serial ports are bad, but notably the floppy interface wasn't detected even though I made sure to plug it in.
I confirmed voltage on the +12V and +5V lines, and made sure the floppy mechanism was connected to good power and the controller ribbon was in the right way. I did not find a jumper or other means of enabling it. For that matter, switching the SSDs didn't make any difference either, though support for a floppy disk drive shouldn't be controlled by that.
I did test the Micropolis hard disk, and with good power it does spin up and appears to respond, but it still wouldn't boot and I couldn't read anything from it. As stiction didn't appear to be the problem with this drive, throwing it in the freezer as well didn't strike me as useful.
Now to try booting the machine from the BlueSCSI. Despite the same test readout, the port assignments in the same image of AMOS 2.3A required moving the console definition because port 0 would work but not port 1. Also, although using the machine is definitely faster with the 68010, is this just because of the clock speed? Indeed, we would expect a 25% increase from running at 10MHz alone, so the real question is whether we see anything more.
.si dsk0:
   SI--AMOS System Information, (C) Copyright 1990, Alpha Microsystems Inc.
                               Version 3.0(114)

               Computer Type: AM-1000 or AM-1200
              Main Processor: 68010
                Co-Processor: None
                 MMU present: No
            Operating System: AMOS 2.3A(488)-1
          Boot PROM revision: Unknown
              Number of SSDs: 1
                Total Memory: 1024 K-bytes
     Resident Monitor Memory: 369 K-bytes

     Computing Index (CX), relative to AM-100:    5.7
     48 bit FP Index (4X), relative to AM-100:    5.7
Floating Point Index (FX), relative to AM-100/L:  1.2
          Disk Index (DX), relative to ST-506:    3.4
The new CPU is detected, but both scores of 5.7 vs. 4.6 and 1.2 vs. 1.0 pretty much scale to the clock difference. This benchmark, at least, doesn't have anything that would obviously benefit from the '010 loop cache or its other minor improvements.
I looked to see if the busted power supply was at all repairable, but when I dug it out I saw at least one immediate serious problem: one of the transformers had literally fractured. I doubt that's the only thing that's wrong with it either. This machine had been really mistreated at some point.
Still, even with the same number of bad ports and no working floppy interface (clearly a logic board problem though I'm not exactly sure where), the board swap has made this machine fast(er) enough that I decided to keep the '010 board in it. This particular floppy interface is also not well-supported in 2.3A in any case, which this machine will be running most of the time, so in my view it's no big loss. I gave it a "new" rear "badge" with the correct serial and SSD numbers, marked the working ports, and cleaned up the exterior.
In the end I determined the AM-1200 will be staying and the AM-1000E will go to temperature-controlled storage for another day (and the mashed AM-1200 will be stripped). Although the AM-1000E is demonstrably faster, the 10MHz 68010 in the AM-1200XP has narrowed the gap and I remain not at all confident that the '030 accelerator board is working properly. Plus, its extra (and, for these early versions of AMOS, largely wasted) RAM makes it much slower to start up cold. By contrast, modulo the board defects, the AM-1200 is otherwise in working-well-enough order and boots any version of AMOS I can throw at it. I'm trying to track down the Alpha Micro User's Society issue (
AMUS.LOG
, December 1992) that talked about the Dimension upgrade board and perhaps I'll take another crack at it later.
As usual, let's conclude by finishing the Alpha Micro story. By the time the AM-1200 arrived in December 1986, the company had suffered three years of losses in the wake of UNIMOS' death rattle (cancelled in 1987), the DEC lawsuit and the two failed 1986 mergers. The AM-1200 rollout didn't reverse the company's fortunes either; AMUS called it "bungled" because the inventory of AM-1000s ran out before the new systems arrived, and dealers were incensed when AM-1000 configurations they had promised to customers were not available for the 1200. Bob Hitchcock eventually reasserted control of the corporation, but it was not until Alpha Micro jumped to the 68030 in December 1987 with the 20MHz AM-3000, capable of servicing up to 300 users in its largest $245,000 [$684,000 in 2026 dollars] configuration, that the company was briefly able to turn a profit again. Unfortunately even this glimmer of hope started fading as the company became almost totally reliant on its AMOS line, for which there was shrinking market demand and relatively little development cash.
Subsequently, Dick Wilcox retired from Alpha Micro in 1990 and Hitchcock's personal health problems caused him to sell his own stock in 1991. New management once more attempted to diversify the company away from the legacy systems and yet again bet on the wrong horse by trying to migrate to the Motorola 88000. This was to be the linchpin of Alpha Micro's second attempted Unix system, planned to run SVR3 and SVR4 with an AlphaBASIC compatibility layer, and the subject of a three year, $4.2 million [$9.8 million] agreement that fall. However, Motorola soon abandoned the 88K processor for the PowerPC AIM alliance and the arrangement never yielded any shipping hardware. The company also continued expanding its presence in vertical market software and launched various side ventures like AlphaConnect for websites and AlphaServ.com, but none of these initiatives were particularly successful, nor were they market leaders.
The next big leap in Alpha Micro systems came with the first Eagle class computer in 1994, retrospectively named the Eagle 300 (officially the AM-3500 series). These were based around a more modern system design with faster SCSI and a greater emphasis on networking with many Eagles shipping Ethernet ports standard, driven by AlphaTCP, an AMOS port of SpiderTCP (and enough pieces of SpiderStreams to support it). SpiderTCP was of course best known at that time as the TCP/IP stack in O.G. Windows NT 3.1. Roadrunner upgrade boards for virtually every post-S-100 system even allowed the AM-1000s to join the party, and gave the Eagles an upgrade path to the 68040 and later the 68060. Subsequent systems like our local Eagle 450 run the ColdFire MCF5102, a first-generation "bridge" CPU that looks like a 68040 to application software (not a coincidence, as the chip originally started life as the 68040VL).
The systems were well-received by the user base, though that market was a lot smaller by then, and so were their profit margins. Predictably, continued losses back in the C-suite forced piecemeal divestment of much of their vertical market software operations and its corporate ownership bounced between multiple erstwhile parent companies in the late 1990s and early 2000s. The company eventually landed at Alpha Micro reseller Birmingham Data Systems, whose California subsidiary renamed itself to Alpha Microsystems in 2002.
In the meantime, Alpha Micro had long produced ISA and PCI compatibility boards for PCs that could run AMOS using their on-board 68K or ColdFire processor, and in 2003 the revised Alpha Micro went one step further by completely emulating AMOS under Microsoft Windows. These machines still shipped a ColdFire-on-a-PCI card, but in this architecture the PCI card's CPU ran a minimal embedded version of AMOS, demoted to I/O for servicing its on-board serial ports and SSD — everything else ran on the main x86 CPU using a Power Macintosh-like 68K emulator and a native version of AlphaBASIC. Later, when Motorola/Freescale stopped producing the MCF5102, the PCI card's CPU was dispensed with completely, leaving only serial ports and the SSD. Even this became unnecessary when Alpha Micro developed the Cardinal, basically the SSD in a USB dongle.
In 2019 a private consortium bought the intellectual property and trademarks, creating a new Alpha Microsystems LLC, after which the former California entity was dissolved. I had the pleasure of speaking to one of the company's principals the other night for a couple hours by phone, an individual who had himself used Alpha Micros since 1979. Their newest planned machine, the AM-770, is intended to use a virtual software Cardinal SSD, completely eliminating the last vestige of legacy AM hardware yet still able to run virtually any Alpha Micro application. They sell today to users who need to expand or revamp their older back office Alpha Micro, where these new units — essentially high-end PCs with AMOS and the AMPC emulation system preloaded — can substitute seamlessly in the job their old hardware had previously performed, in some cases for decades.
It's a fitting happy ending for a warhorse poor man's minicomputer architecture that, if only in a virtual sense, still lives on today. Plus, now you know why I like them so much. Call it my penance.
