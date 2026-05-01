---
title: "6o6 v1.1: Faster 6502-on-6502 virtualization for a C64/Apple II Apple-1 emulator"
url: "https://oldvcr.blogspot.com/2026/03/6o6-v11-faster-6502-on-6502.html"
fetched_at: 2026-05-01T07:01:26.163848+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# 6o6 v1.1: Faster 6502-on-6502 virtualization for a C64/Apple II Apple-1 emulator

Source: https://oldvcr.blogspot.com/2026/03/6o6-v11-faster-6502-on-6502.html

I'm doing periodic updates on some of my long-term projects, one of them being 6o6, a fully virtualized NMOS 6502 CPU core that
runs
on a 6502 written in 6502 assembly language. 6o6 implements a completely abstracted memory model and a fully controlled execution environment, but by using the host's ALU and providing a primitive means of instruction fusion it can be faster than a naïve interpreter. This library was something I wrote over two decades earlier for
my KIM-1 emulator project
for the Commodore 64, and relatively recently
I open-sourced and discussed it in detail
. It runs on just about any 6502-based system with sufficient memory.
For this update I made some efficiency improvements to addressing modes, trimmed an instruction out of the hot path, provided an option for even more control of the 6502 interrupt flag and implemented a faster lane for direct stores to 6502 zero page (as well as the usual custodial and documentation updates). And, of course, any complex library needs a suite of examples, and of course, any update to a complex library demands new examples to play with too.
So, given that this year is
Apple's 50th anniversary
(and, as it happens, my own 50th year of existence personally), what better way to show off a 6502-on-6502 virtualization library than with an Apple-1 emulator ... that runs on the Commodore 64 or Apple II? Now yea, verily, this is hardly the first such example and several others have done something of the sort, but I submit that 6o6 makes our take on it here unique, and as a bit of fun we'll discuss the Apple-1's hardware and look at all that prior 8-bit emulator art for comparison (for the C64 and Apple II and even more exotic systems like the SAM Coupé).
Let's get the technical notes out of the way first and then we'll get to the rogues' gallery. In broad strokes, 6o6 provides a virtual machine on your 6502 computer that itself implements a full NMOS 6502 software core (documented instructions only), written in 6502 assembly language. You provide a harness, which is the VM's sole access to guest memory, and a kernel, which acts as a hypervisor. The kernel calls the VM repeatedly, which uses the harness as an interface to access guest memory and executes one (or, if "extra helpings" instruction fusion is on, several) guest instruction(s) from it, returning to the kernel. The kernel then examines the guest processor state and acts upon or modifies it as appropriate, then calls the VM again to run more instructions, and so on. Because the VM only accesses guest memory strictly via the harness, the harness thus becomes a highly flexible virtual memory manager: it alone maps virtual addresses to physical addresses, so it can page things in and out, synthesize address space on the fly and/or throw exceptions and faults back to the kernel. One of our examples runs a guest (with EhBASIC) on a Commodore 64 or 128 entirely from a geoRAM paged RAM expansion, managed by the harness; no part of the guest memory is actually on the computer itself.
You can read about 6o6's development in more detail
.
Although the changes here introduce minor functional improvements with how 6o6 handles IRQs (and by extension
BRK
s, which the 6502 treats as a software interrupt), this update is primarily a performance one. 6o6 is tightly bound to
the
xa65
cross-assembler
's macro system, which it uses to inline large sections of code relating to memory access. Although this certainly bloats the VM, the macros also make it substantially faster because overhead from subroutine calls and returns can be avoided in the hot path. The most profitable of these macros are the memory access ones, where every fetch from RAM — because even reading an instruction requires a fetch — can be inlined (you define these too as they are considered part of the harness). There is a special path for instructions that access the 6502 zero page, and new in this release is a fast path for zero page stores as well as loads. Zero page is specially optimized because its physical location in memory can be precomputed and thus reduce the complexity needed to resolve a virtual address. The memory access macros are all optional but are strongly advised as the VM runs rather slower without them.
Another class of macros, executed literally on every single guest instruction, are the address mode resolvers. These also call into the harness, using (and inlining) the same memory access macros when available, and after any arguments are fetched do all the math for indexing as required. The addressing mode resolvers are also inlined, so they also need to be quick, and "upon further review" several of the zero page addressing modes were setting up the virtual address results inefficiently: the zero page fast path now makes the work they used to do completely unnecessary, so they were trimmed and combined with shaving an opcode out of instruction dispatch for further savings, a section of code that also must literally run on every single guest instruction.
I'm proud of the efficiency gains 6o6 has made over the years I've iterated on it such that big wins are now understandably harder to come by, but these improvements are still measurable. 6o6 is stress-tested in multiple configurations using Klaus Dorman's well-known and community-accepted
6502 validation suite
to prove full adherence to the instruction set, after which a count of instructions (as a proxy for relative execution time) is computed. A native 6502 must execute 30,646,178 instructions to pass this suite, which we count using a test framework based on
lib6502
. In its fastest configuration, with all optimizations enabled and maximum inlining, 6o6 1.0 executed and passed the suite in 1,602,516,769 instructions. This necessarily includes the veneer harness and kernel used to run the test suite, a average ratio of 52.3 host instructions per guest instruction. 6o6 1.1 can now execute and pass the suite in 1,561,780,659 instructions using the same harness and kernel. Although 2.6% fewer instructions doesn't seem like a big deal, remember that a small percentage of a big number can still be a big number: the improvements bring the average down to 51.0 host instructions per guest instruction, and the processor now requires over 40 million instructions
fewer
to qualify. The delta increases further for code that does more reading than writing generally, or a lot of zero page activity specifically, since more of those accesses (including stores) can now be moved to a fast path.
This calls for a celebration, and as such, it is known that all celebrations must have at least one gratuitous stunt. I'm a nerd and this is mine. Some of you will have seen some of these pictures previously from when I was at the 2019 Vintage Computer Festival West.
The Apple-1 needs no introduction and I'm not going to get into the history much in this particular piece, but it is, of course, the nascent Apple Computer Company's first product ever in 1976. Only around two hundred were made and perhaps half of those survive. They were originally intended to use the Motorola 6800 CPU, but it was too expensive, and Steve Wozniak, its designer, developed the system around the new, dramatically cheaper and bus-compatible (surprise!) MOS Technology 6502 instead. Selling for the allegedly totally innocent price of $666.66 [about $3850 in 2026 dollars], all of the units were hand-assembled by Woz, Steve Jobs, and/or their small crew of assistants, and the system was sold until mid-1977 when it was replaced by the much expanded Apple II. Units shipped with 4K of RAM and a complete system could be assembled from the board, a case, an ASCII keyboard and a composite display — no teletype required. Common upgrades included a practically essential cassette adapter (the Apple Cassette Interface card) and an additional 4K of RAM added to the onboard sockets; up to a full 64K was possible through an expansion slot, modulo I/O and ROMs. The small internal ROM monitor (WOZMON) could be supplemented by other languages loaded into RAM, most commonly Wozniak's Integer BASIC. Remaining examples now go for eye-watering amounts of money, even broken or incomplete systems, especially because units sent back to Apple for trade-in value were destroyed.
Today, the Apple-1 Owner's Club is here to remind you that you don't have an Apple-1, and neither do I. Still, its historicity is such that for a system very few of us will ever touch, let alone have in our own homes, the Apple-1 has a lot of people interested in it. The attraction is enhanced by hardware so simple to grok that it makes a popular target for emulator authors and replica builders, almost all of whom (myself included) haven't ever touched a real one either.
The Apple-1's basic operation can be trivially simulated with a 6502 core and some sort of terminal, which is actually a reasonable basic summary of the system architecture, since it was constructed around a terminal design Woz had built in 1974 out of a keyboard from Sears (remember when Sears sold keyboards? um, remember Sears?) and an off-the-shelf television set. The video display is entirely 40x24 text and centred on seven one-kilobit Signetics 2504 shift registers, six of which hold the character	bits for each screen location and the seventh where the cursor is at (a binary-one in its current location). Four of these shift registers have one 74157/74LS157 quad selector/multiplexor and the remaining two have another, while the cursor shift register is supervised by a 74175/74LS175 quad flip-flop. The process of drawing the screen breaks it down into 24 rows. For each row, 40 bits from each main kilobit shift register are clocked into a smaller Signetics 2519 6x40 shift register used as a line buffer (and cycled back into the kilobit registers). This smaller shift register is repeatedly cycled to draw each line of each character, using the bits to index glyph lines stored in a Signetics 2513 character generator. Those lines are fed into an even smaller eight-bit 74166 shift register and clocked out as dots to the screen.
A new character can only replace another if the cursor is in the row currently being drawn
and
at the point where that character would be displayed. This means any one single character can only be added to the screen each frame (60.05fps), and
only
one character. When this happens, if the character is in the printable range, a write signal to the 74157s causes the character's code bits to be both propagated and loaded into the shift registers, and the cursor moves one bit forward. A "busy bit" can be read by the 6502 to know when the video hardware is ready to accept another character. (If you write to the hardware anyway, the result is officially undefined, though reportedly unhelpful. Ken Shirriff's
shift register analysis
is instructive.)
To turn the new character from 7-bit ASCII (the upper eighth bit is used for the "busy bit" to indicate when the terminal is ready to accept a character) into the 6-bit index of the desired character glyph, one of the bits must be converted. The shift registers only take input from bits 1 (0), 2, 3, 4, 5 and 7 (64). Bits 1-5 are passed through unchanged (to the 2513's A4-A8 inputs via the 2519's I1-I5/O1-O5 lines), but the 2513's A9 input is set to the
inverse
of bit 7 by the NOR gate at C10 via the 2519's I6/O6 lines. You can see the sequence emitted from this Perl program.
% perl -e 'for($i=32;$i<128;$i++){$j = $i & 95; $j |= ($j&64)?0:32; $j &=63; printf(" %02x ",$j);}'
 20  21  22  23  24  25  26  27  28  29  2a  2b  2c  2d  2e  2f  30  31  32  33 
 34  35  36  37  38  39  3a  3b  3c  3d  3e  3f  00  01  02  03  04  05  06  07 
 08  09  0a  0b  0c  0d  0e  0f  10  11  12  13  14  15  16  17  18  19  1a  1b 
 1c  1d  1e  1f  00  01  02  03  04  05  06  07  08  09  0a  0b  0c  0d  0e  0f 
 10  11  12  13  14  15  16  17  18  19  1a  1b  1c  1d  1e  1f
For most control characters, they are considered
not
printable, so nothing happens and they are never inserted into the shift registers (but the per-frame penalty is still paid). These characters are filtered out by the logic chips in positions C5-C9, C12 and D12, which also incorporate whether the cursor is present at that position. Only the carriage return is checked for specifically, by the C6 74LS10 NAND and C5 74LS27 NOR gates, and used to move the cursor to the next line. When the cursor moves off the bottom edge of the screen, a row of blanks pushes the top line out of the main shift registers and the cursor resets. All of this happens in hardware and independently of the 6502. Clearing the screen is even done manually with a button to signal the two 74157/74LS157 quad selector/multiplexers' strobe lines, making them zero the bits to and from their shift registers — the CPU itself is unaware of that process too. Since all the bits in the kilobit shift registers end up clear, bit 5 gets set in the 2519 and no others, which is the space glyph.
Because of this design, there is no CPU-accessible video memory and thus no way at all for the CPU to know what's on the display. For I/O the onboard Motorola 6820 PIA provides single locations to emit to the display and read a character from the keyboard (and control registers for each), and that's it. Any program accepting user input must maintain its own command line buffer, which WOZMON and Integer BASIC both do. Otherwise, there are no graphics modes, no colour, and not even reverse or flashing video, with the only thing flashing at all being a small "@" cursor — which is also independently maintained by the hardware, using a 555 wired into the 2519 to cycle it on and off. And how do we know the cursor is an @? The presence of the cursor bit at the current position suppresses the write signal and thus the bits entering the kilobit shift registers, making them zero for that single character position, while the 555's output (gated by an AND gate to make sure the cursor is present) becomes the other input to the same NOR gate at C10. If the 555 has turned the cursor on, the NOR gate emits a zero to the 2519's I6 line and thus to the 2513, and no bits set yields the @ glyph. Otherwise, the NOR gate emits a one to the same line, and as we already know, that becomes a space glyph. The cursor never goes backwards, so it never needs to restore any character.
The situation is only slightly complicated by a small jumper area in the middle of the board used to configure the machine's memory map. You can see it in this photo, or zoom in on the
Wikipedia picture of the mainboard
. Each of the 16 points (0-F) linked to a corresponding 4K region of the 6502's addressing space. The upper four bits of the address bus were decoded by a 74154/74LS154 to those 16 outputs; your jumper then went between those outputs and whatever your enable pin or circuitry was attached to. The board had seven hardwired lines for this, R, S and T (user configurable, exposed on the expansion slot and unconnected from the factory), W and X which were connected by solder jumpers to $1000 and $0000 respectively, Y which was connected by a solder jumper to $F000, and Z which was connected by a small wire to $D000. On the other end W and X went to the chip select lines for whichever 4K banks of RAM were present, Y went to one of the chip enable lines on the WOZMON ROM and Z went to one of the chip select lines on the PIA.
The idea was that you could rewire these to whatever was on the included breadboard section of the computer or in the expansion slot, but most software assumed the PIA would be at $D000 and without low RAM and high ROM the system wasn't too useful, so X, Y and Z weren't often changed. On the other hand, a frequent modification was to cut the W jumper and run a new wire from W to $E000, which moved the upper 4K of RAM to just under the ROM region. Integer BASIC, for example, was commonly loaded to that location, and because the change made RAM no longer contiguous, there was less risk of a BASIC program (in the low 4K) inadvertently corrupting it.
You should expect for a machine with little comprehensive documentation lots of people know about but a rather tiny minority have actually used that there would be ...
varying ideas
about its user experience, as it were. I'd like to emphatically insist this is
not
an indictment or criticism of any of the authors below, just an observation on what I consider an interesting subniche around an exceedingly rare piece of history. Nor is this an exhaustive exposé on all the ways you can emulate an Apple-1; that includes the assorted hardware replicas, some of which can go for pretty stupid money themselves, but are really just emulators to me of a different sort graced by the heady smell of solder.
Still, we'll need
something
to compare against, and a useful test vector for comparison is this one, which comes right out of the Apple-1 manual written by Apple co-founder Ronald Wayne. We'll use it on our various candidate implementations (including my own) to compare their behaviour. As our benchmark, since I sadly have no Apple-1 at Floodgap — I look forward to your offers — MAME has a very competent Apple-1 driver which first originated in a early version of MESS (somewhere between 0.2 and at least 0.37) before their merger. Unlike the likely majority of the other programs we'll discuss in this article, including mine, the MESS/MAME driver looks to have been revised by people either with access to or at least excellent understanding of the actual hardware, first an initial version I can't credit, then some updates by Rodney Hester, then a
substantial revision
credited to Colin Howell who improved
the video emulation
and later added cassette support. (Current versions of MAME use a complete rewrite by R. Belmont that nevertheless maintains the correctness of the earlier releases.)
On the other hand, the major historical Apple-1 emulators (the actual hardware being practical unobtanium) derived their operation almost entirely from the described behaviour in the manual. Thus, we would expect any good emulation to support some semblance of this sequence, and
most
Apple-1 emulators at least attempt to run it as written. The devil's of course in the details of what
isn't
described in the manual, such as how the monitor reacts when characters are typed, which glyphs precisely are displayed, and even what the cursor looks like, all of which we previously labouriously derived from the schematic.
This is how a session looks in modern MAME. Up at the top, after the backslash being used as a prompt (printed on reset or pressing ESCAPE), we entered the code in hexadecimal, then printed the contents of those memory locations for verification, then after deliberately backspacing over a line — the underscores, which after completely obliterating what we typed internally makes the monitor move to the next line — we started the program running. You'll notice that there is no way to move the virtual carriage back, so the characters couldn't actually be deleted from the screen when we backed up. You'll also notice no address was specified to run ("R") from. In this case, the fact it works at all is due to a remarkable coincidence: with no argument given, the execution starts from the last address accessed (tracked in a zero page variable called
XAML
), which in this case is $000a because it was the last memory location we displayed, which contains $00 because we put it there as part of the final instruction, which is the
BRK
opcode, so the 6502 pulls the IRQ vector at $fffe from WOZMON, which is ... $0000, and the program duly runs from there.
The program trivially disassembles to
LDA #0:BACK TAX:JSR $FFEF:INX:TXA:JMP BACK
. I'm assuming the use of the X register is just to make increments more straightforward, since the routine at $ffef will display the character in the accumulator once the video hardware has indicated it's "ready" to accept it. When you start it, the accumulator A begins at zero. The first thirteen (0-12) characters are control characters and never actually enter the shift registers. However, printable and unprintable characters alike have the same approximate sixtieth of a second acceptance rate per frame regardless of their ultimate disposition, so there ends up being a brief but noticeable pause where nothing appears. Only when we get to character value 13 do we move to the next line, then again ignore the next eighteen (14-31) characters which are also unprintable (another brief pause),
then
get into the printable range. Characters 32 to 95 appear with the character shapes you'd expect and at the same rate, though characters 96 to 127 are also printable, just repeats of 64 to 95. After that, because the high bit is never passed to the video hardware, codes 128 to 255 appear (or not) exactly the same as codes 0 to 127, and then X (and then A) overflows to zero. The routine runs forever in this fashion, scrolling the screen as needed, until stopped. Halting the program is usually accomplished with the reset key, which is a non-destructive restart, and puts us back in WOZMON.
All of that occurred with a very simple 6502 machine language program calling a simple routine in the monitor which simply twiddles two locations on the PIA, but running the 6502 code is actually the easy (or at least best defined) part, because the obvious thing to do is run 6502 code on ... a 6502 directly, which would run at native speed and completely authentically. The main problem here is there's no MMU or hardware virtualization on a vanilla 6502 CPU (you see where I'm going with this), so you can't prevent it from reading or writing where it thinks the PIAs are, or WOZROM, or anything else like, say, your support code, because the memory map almost certainly won't match. Still, it's a great hack to try and people certainly tried it, though to make it work requires breaking some rules, so the interesting part is which rules and how.
The earliest example I can find of an Apple-1 on any 8-bit computer is appropriately enough
for the Apple II
, written by Mark Stock, and
dates to 2006
. Mark appears to indeed have based his emulator on the manual,  so some gaps shouldn't be surprising: for example, it uses a block cursor, since most people would have supposed that's what it had, and it moves the carriage back with deletions since most people would have supposed that's how it worked. Later patches were offered to adjust. Although the files are not on the Wayback Machine, at least one version
is on Asimov
. This emulator displays text on the Apple II high-res screen so that the whole of $0000-$3fff can be used by the emulated Apple-1, including zero page and stack, and then also loads a patched version of WOZMON into $ff00 on the language card RAM so that calls to it work too and gives us proper 6502 high memory vectors at the same time.
The reason for patching WOZMON is the PIAs, which is how this emulator "breaks the rules." Although the PIA's address range at $d000 is available in this configuration, the Apple II has no routine interrupts where a service routine could regularly pick up or deposit values, and even if there were, the potential for race conditions should be glaringly obvious. Instead, the patches turn PIA loads and stores into calls into its support routines: an
STA $D012
which would write a character to the screen would become
JSR $805B
, including in the routine at $ffef, and an
LDA $D011
which would read a character from the keyboard would become
JSR $8070
. If your program wasn't using WOZMON, then you'd need to patch it yourself to do these things. Mark did a version of Lunar Lander as an example.
Here's our test vector output. The stock Apple II doesn't have free-running timers either, so it isn't possible to slow down the video output to the Apple-1 framerate, nor does the cursor blink (and since we're on the hi-res screen, you can't cheat with flashing characters). The Apple DELETE key isn't mapped to anything and just emits a nonsense character, but underscore (i.e., SHIFT-minus) is treated as delete. Both the delete moveback and the extra linefeeds were corrected with later patches, though the wrong bits on the 96-127 character range were not.
If anything, the top speed of this emulator is slightly
too
fast. The Apple-1 6502 ran at a nominal rate of 1.0227
27
MHz, divided down by fourteen from the single 14.318
18
MHz (1260/88) crystal also used for video generation, but RAM refresh imposes a four of every 65 cycles' penalty for an effective throughput of 0.9598MHz. On the Apple II, the system runs at the full /14 speed except for every 65th cycle which is lengthened by two ticks of the same master crystal, yielding an average speed of 1.020484MHz.
Understandably and unavoidably you can hose the emulator (and, for that matter, WOZMON) by overwriting its code, and on a system with an NMOS 6502, jam opcodes like $02 will still cause the system to hang up until it's reset. However, one interesting thing is that on an Apple II+ (NMOS from the factory), CONTROL-RESET becomes like pressing the Apple-1's Reset button and the behaviour actually matches. This doesn't work on the IIe and up, where it's just CONTROL-RESET and you exit to BASIC (but you can
CALL 32768
to get back in, and $02 is a two-byte no-op on CMOS 65C02s anyway).
Simon Owen's Apple-1 emulator appears to be the next in line, as I can't find another one predating his first version in 2007, but he didn't do it on a 6502 — he did it on a Z80, or the SAM Coupé to be precise, arguably the most advanced system of the classic ZX Spectrum family. Simon explained to me that his emulator was written to model the emulation in Pom1, written by Verhille Arnaud, an early Apple-1 emulator which seems to have had its first public release in 2000. Since Pom1 was written in Java, you can still run it, and
some versions of it
are preserved on the Wayback Machine. The last release I can find is 0.70.
Pom1 itself seems to have taken cues from what I believe is the earliest Apple-1 emulator on
any
platform, written for the Macintosh. This is Sim6502, originally developed in 1997 by Achim Breidenbach, and is still downloadable from a veritable Garden of Macintosh sites or
the Wayback Machine
. The readme accompanying it suggests Breidenbach also wrote it based on the description of the system in the manual, though he made some different choices: among others Sim6502 advances the cursor on control characters (effectively rendering them as blanks) and doesn't show the second repeated set of characters from 96 to 127 except as blanks too, because without looking at the schematic the bit conversion wouldn't have been obvious. Although it does try to correctly model the character output rate, its 6502 emulation also has some notable deficiencies, such as lacking decimal mode entirely (documented in the readme) and failing to run the IRQ vector via
BRK
with
R
(you need to kick off our example with an explicit
0R
, or else it gets treated like a soft reset). Reportedly Breidenbach was working on a later version that addressed some of these gaps but I can't seem to find any evidence it was released.
Despite a better 6502 emulator and video improvements, Pom1 nevertheless mirrored some of Sim6502's idiosyncracies in its own emulation core like the block cursor, though these varied from version to version. For example, 0.62 had a working delete key that moved the carriage back, but required you to have the caps lock down. By contrast, 0.70 correctly only does capital letters, but its delete key just advances the cursor and is not recognized by WOZMON as delete (you're supposed to press SHIFT-MINUS to get the underscore instead). The later version also incorporates the same or similar monitor that intercepts the
BRK
our test sequence executes, which 0.62 didn't. Both versions also don't suppress control characters when emitted to the PIA's output port, which again render as blanks, though it does properly render the 96-127 range. (Many of these issues were subsequently fixed, including in the
native SDL-based version
maintained by John Corrado. Appropriately enough, Mark Stock later ported
SDL Pom1 to Mac OS X
.)
Simon's release is based on the earlier Pom1, e.g., block cursor, Delete actually deletes, control characters advance the cursor. The current version also shows lowercase in the 96-127 range for our test vector, and likewise implements the same or similar monitor to Pom1 0.70 that traps
BRK
. But Simon's emulator is particularly notable because it must implement its 6502 core in Z80 assembly language — because it's running on a Z80. Since it doesn't run Apple-1 programs on-processor, it needs no adjustments to run anything, and is similarly immune to many catastrophic faults. For example, if you try running a jam opcode, this emulator just ignores it.
It also includes not only Integer BASIC, but also Applesoft BASIC, and programs seem to work there as well. Simon is working on improvements to the emulator core to bring it up to the standard in MAME/MESS, but you can
play with it now
or in the
SimCoupe emulator
. It's open source, too.
Of course, running the code effectively under an interpreter does impose an obvious speed penalty.  The SAM Coupé has a 6MHz Z80 and as such Simon estimates its 6502 emulator runs at about 20% of the speed of a real Apple-1, though the emulator's overall performance is at or near native speed when printing because of the ~60Hz limit.
Fast-forward a few years, and with the more accurate MAME driver the extremely narrow subniche of 8-bit Apple-1 emulators got more accurate too — though now different rules needed breaking.
People might be surprised to know you could simulate the Apple II, or at least some portion of Applesoft BASIC,
on the Commodore 64
(monstrosities like the Spartan Mimic notwithstanding, though I'd still love to play with one), and I seem to recall at least a couple others in that vein. But in 2013, Alexei Eeben decided to do it for the Apple-1, incorporating his own monitor program C'mon for the VIC-20 which he cross-ported, dubbing it
Green Delicious
.
Green Delicious also runs native, directly on the Commodore 64's 6510 CPU, which to anyone with a knowledge of the C64's architecture should immediately highlight a big problem: the 6510 reserves the lowest two locations of RAM ($0000 and $0001) for its on-chip I/O port. That means if we even try to
type in
our sample vector ...
... it will crash, and crash hard, as soon as it stores the first byte or two. Any program that expects to use or start there will simply not work.
Thus we need to run our test from another location, say $0300, and from there it works as expected and shows the right character set at the correct approximate speed. IMHO Green Delicious is without a doubt one of the prettiest Apple-1 emulators on any platform, not just 8-bit, from its pixel correct output (you can change the colour with F3 if you don't like green) to the flashing rainbow Apple logo (you can restore the classic @ with F5). In fact, the only minor flaw I could find in its appearance is that the cursor blink rate is a bit off — the 555 has a period of about half a second, two-thirds of which is the on-phase.
Green Delicious uses its own variation of patching to handle PIA access, and its pre-patched internal version of WOZMON also has a live IRQ vector which it uses for housekeeping tasks. (This vector doesn't appear to handle
BRK
instructions, though, which will also make it crash.) Unlike our earlier Apple II-based emulator, however, Green Delicious' built-in loader will patch your binary
on the fly
, and log what got patched to memory where so you can see what what it did. Surprisingly, this automatic patcher works for a lot of binaries without modification.
BASIC programs run fine, and since the interpreter runs at or faster than a real Apple-1, they run at a ripping speed. Indeed, this is Green Delicious' strongest turf. On the other hand, if you try to run native code it's also rather easy — even unintentionally — to crash the emulator and invariably the 64 itself, and after a couple hard stops with a real 64 and a real 1541 disk drive you're going to have a real conniption waiting for it to reload again.
So let's go back to Simon's idea from the SAM Coupé of running the Apple-1's 6502 code in emulation, but this time we'll use a virtualization library for the 6502 itself that reuses the 6502's own ALU for speed and correctness on guest code, yet completely isolates memory and maintains full control of the guest processor state at all times. Hmm, I wonder where we could find such a library?? Think think think! ...
VA1, for Virtual Apple-1, will run on the Commodore 64 or an Apple II+ or better with at least 48K; here we're running it on an emulated Commodore SX-64. To handle the screen we use a custom character set based on the Signetics' font shapes and set the screen to 24-row mode, starting everything on the second line so scrolling "just works."
The Commodore version
LOAD
s and
RUN
s like a BASIC program and enters WOZMON immediately. You can tell we're now isolated from the main CPU because we can store our test program right at $0000 ...
... and run it, and not only does it not crash, it runs successfully and identically to MAME. Since the C64's jiffy clock (maintained by the Timer A interrupt) is roughly the same speed as the Apple-1's video hardware, we sync to it to clock characters out and flash the cursor at the right time. This is the same basic idea
we used in Oblast
except there we also intentionally overdrove Timer A to speed up the game.
The cursor is maintained by checking the jiffy clock on every cycle of the virtual machine and changing the character code appropriately. We simply use the Kernal's character out routine here which effectively maintains its own, merely disabled, cursor on each screen's logical line. We use this position to draw our own, removing it if we are going to a new line or about to scroll the screen, and for a little extra paranoia ensure that every logical screen line in the Kernal's screen editor map corresponds exactly to the same physical screen line.
VA1 has key equivalents for the Apple-1's special functions like other emulators. The ESCAPE key is sent with F1 and you can use INST/DEL to delete (or press the backarrow for an underscore, which is the same ASCII value). For resetting the guest Apple-1, the Commodore 64 version uses the RESTORE key; I somehow found it appropriate to generate an NMI on the host computer to generate a reset signal on the guest. Just tap it and the virtual machine will safely dump you back into WOZMON with memory intact.
6o6 can throw exceptions and VA1 will handle them. Here, if you run an illegal instruction (undocumented NMOS instructions are intentionally not supported, sorry) like a jam opcode, the 64 won't crash. Instead, 6o6 throws an illegal instruction exception, VA1 prints a message (you know it's coming from the emulator because it appears instantaneously), and puts you right back into WOZMON pointing to the offending address. For that matter, you can't overwrite WOZMON from inside the emulator either. Note that  because VA1's harness synthesizes a full 64K guest address space and 6o6 hypercalls are disabled, the only exception you'd get on a practical basis would indeed be an illegal instruction.
VA1 is 109 blocks long and intentionally uncompressed so that you can overwrite it in place with anything you load from disk. It provides an 8K RAM system; by default it comes with Integer BASIC in the high 4K RAM at virtual address $E000 and
Hamurabi
[sic] loaded into the low 4K RAM at virtual address $0000. If you type
E2B3R
to warm-start Integer BASIC and then type
RUN
, the game starts.
Running BASIC programs is admittedly where the processor emulation drags noticeably. Simon's claim of 20% native for his SAM Coupe 6502 emulator is based on a processor that clock-for-clock (6MHz versus 1.0227
27
MHz [NTSC] or 0.98524861
1
MHz [PAL], but Z80 instructions on average take more clock cycles) is about two or three times faster than the C64's and has more registers, and is running a purpose-written emulator instead of the more generalized one here. While the harness and kernel in VA1 are very thin, they do add a non-trivial cost, and when no display output is being generated VA1 is probably around twenty to thirty times slower than a real Apple-1 depending on the instruction mix. When emitting characters, however, both emulators run roughly at full speed because now the video hardware becomes the rate-limiting factor.
Because VA1 is uncompressed, you can hit RUN/STOP-RESTORE (not just RESTORE) and load something over it, then re-
RUN
the program. You can even load it
before
you run it. The low 4K bank at virtual address $0000 is located at physical address $1000, and the high 4K bank at virtual address $E000 is at physical address $2000. Here, we'll load an assembly language version of Lunar Lander (files ending in
.sa
have a Commodore-style starting address for your convenience) to virtual address $0300 (physical address $1300), return to VA1 by running it, ...
... and with
300R
you can play an unmodified copy of Lunar Lander at a speed indistinguishable from a real Apple-1. (I think.) I decided to do it this way instead of building in a formal interface because firstly I'm lazy, and secondly it makes a better demonstration example if there isn't a lot of additional code. If you want an artistic Apple-1 emulator on your Commodore 64 with more glitz, you should just run Green Delicious.
But you
can't
run Green Delicious on an Apple II, whereas you
can
run VA1. It runs as a binary program with
BRUN
.
As with Mark Stock's earlier Apple-1-on-an-Apple-II emulator, and because the stock Apple II lacks a free-running clock, this emulator does not limit text output to 60.05Hz either. As for the blinking cursor, that's just because I chose a blinking @ for the cursor as generated by the Apple II's video hardware, since once again there's no clock source to sync it to. Either way, on the Apple II as well we are able to enter our test program ...
... and run it. The Delete key, if you have one, also maps to the underscore or you can just hit SHIFT-minus as usual. With the right cursor key (not used by the Apple-1), you can perform a non-destructive reset of the guest Apple-1, like hitting RESTORE in the C64 version. If you have an up key on your keyboard, that will clear the screen (or press CONTROL-K). The Apple II version also uses the built-in ROM routines to print and scroll the screen, and uses similar code to the C64 version to position its own cursor.
The CPU core is otherwise exactly the same and throws the same exceptions, and fails safe in the same way.
You also have the same Hamurabi program loaded into the low 4K ...
... and you can overwrite VA1's memory with your own programs from disk here too. Hit CONTROL-RESET and the binaries on the provided disk image can simply be
BLOAD
ed in place. The Apple II version has the same emulated memory layout, with the low 4K ($0000) at physical address $1000 and the high 4K ($E000) at physical address $2000. We load Lunar Lander, then warm start the emulator with
CALL 2051
...
... and then run it with
300R
. More software is available from
Apple1Software.com
, though you will need to encode the correct starting address within VA1 (for the binary or
PRG
file) on both platforms.
Lastly, here it is running on a
real
Commodore SX-64, providing as much, if not more, portability as the original Apple-1 (though it's a bit heavier). If someone wants to port this to Atari 8-bit, which would be well within its capabilities, toss a pull request my way and I'll have a look.
So happy birthday, Apple. While working on the upgrades to 6o6, I started thinking about future ways to continue to reduce the impact of memory abstraction on the core, since there aren't many more ways to make the processor emulation itself quicker. For the next release of 6o6, I would like to create a fast path for stack pushes and pulls — this wasn't a major need for the Incredible KIMplement because there wasn't a great deal of memory in the KIM-1 for storing subroutines (let alone calling them), but larger programs certainly make use of them, and may do so frequently. This can probably be done with a new set of macros, so it shouldn't be technically complex.
But the other thing I'd like to consider is some sort of dynamic pagetable, effectively a declarative harness. Since the pagetable would already have the deferenced physical location of a virtual page in it, the VM could just go fetch it, and a flag value could tell the VM when the harness needs to be directly consulted instead — at which point the harness still handles the load/store operation as it does now, but it could also make any adjustments and fix up the pagetable on demand, or even throw an exception. (Hey, we just reinvented the page fault!) I need to do some more thinking about this and ideally how to implement it without wrecking the current API, but it could substantially simplify memory access for the typical case, so I think it'd be worth it. Watch for these and other changes in the future.
In the meantime, you can look at the changes for v1.1 in the
6o6 Github project
or download updated demonstration disk images and programs for the C64 and Apple II from
the Releases tab
, which includes VA1. 6o6 is released under the Floodgap Free Software License.
Additionally, the Incredible KIMplement — the original KIM-1 emulator on the Commodore 64 for which 6o6 was originally written — is also updated to the new processor core, plus changes to the build system for better future maintainability. You can get that from
the KIMplement page
, or browse
the source code on Github
. It too is released under the Floodgap Free Software License.
