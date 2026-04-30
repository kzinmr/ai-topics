---
title: "A tricky Commodore PET repair: tracking down 6 1/2 bad chips"
url: "http://www.righto.com/2025/04/commodore-pet-repair.html"
fetched_at: 2026-04-30T07:01:08.192671+00:00
source: "righto.com"
tags: [blog, raw]
---

# A tricky Commodore PET repair: tracking down 6 1/2 bad chips

Source: http://www.righto.com/2025/04/commodore-pet-repair.html

mult3
In 1977, Commodore released the PET computer, a quirky home computer that combined the processor,
a tiny keyboard, a cassette drive for storage, and a trapezoidal screen in a metal unit.
The Commodore PET, the Apple II, and Radio Shack's TRS-80 started the home computer market with ready-to-run computers,
systems that were called in retrospect the
1977 Trinity
.
I did much of my early programming on the PET, so when someone offered me a non-working PET a few years
ago, I took it for nostalgic reasons.
You'd think that a home computer would be easy to repair, but it turned out to be a challenge.
The chips in early PETs are notorious for failures and, sure enough, we found multiple bad chips.
Moreover, these RAM and ROM chips were special designs that are mostly unobtainable now.
In this post, I'll summarize how we repaired the system, in case it helps anyone else.
When I first powered up the computer, I was greeted with a display full of random characters.
This was actually reassuring since it showed that most of the computer was working: not just the monitor,
but the video RAM, character ROM, system clock, and power supply were all operational.
The Commodore PET started up, but the screen was full of garbage.
With an oscilloscope, I examined signals on the system bus and found that the clock, address, and data lines were full of activity,
so the 6502 CPU seemed to be operating.
However, some of the data lines had three voltage levels, as shown below.
This was clearly not good, and suggested that a chip on the bus was messing up the data signals.
The scope shows three voltage levels on the data bus.
Some helpful sites online
7
suggested that if a PET gets stuck before clearing the screen, the most likely cause is
a failure of a system ROM chip.
Fortunately, Marc has a
Retro Chip Tester
, a cool device designed to
test vintage ICs: not just 7400-series logic, but vintage RAMs and ROMs.
Moreover, the tester knows the correct ROM contents for a ton of old computers, so it can tell if a PET ROM has
the right contents.
The Retro Chip Tester showed that two of the PET's seven ROM chips had failed.
These chips are MOS Technologies MPS6540, a 2K×8 ROM with a weird design that is incompatible with standard ROMs.
Fortunately, several people make adapter boards that let you substitute a standard 2716 EPROM, so I ordered
two adapter boards, assembled them, and Marc programmed the 2716 EPROMs from online data files.
The 2716 EPROM requires a bit more voltage to program than Marc's programmer supported, but the chips seemed to
have the right contents (foreshadowing).
The PET opened, showing the motherboard.
The PET's case swings open with an arm at the left to hold it open like a car hood.
The first two rows of chips at the front of the motherboard are the RAM chips.
Behind the RAM are the seven ROM chips; two have been
replaced by the ROM adapter boards.
The 6502 processor is the large black chip behind the ROMs, toward the right.
With the adapter boards in place, I powered on the PET with great expectations of success, but it failed in precisely
the same way as before, failing to clear the garbage off the screen.
Marc decided it was time to use his Agilent 1670G logic analyzer to find out what was going on;
(Dating back to 1999, this logic analyzer is modern by Marc's standards.)
He wired up the logic analyzer to the 6502 chip, as shown below, so we could track the address bus, data bus,
and the read/write signal.
Meanwhile, I disassembled the ROM contents using Ghidra, so I could interpret the logic analyzer against the assembly code.
(
Ghidra
is a program for reverse-engineering software that was developed by the NSA, strangely enough.)
Marc wired up the logic analyzer to the 6502 chip.
The logic analyzer provided a trace of every memory access from the 6502 processor, showing what it was executing.
Everything went well for a while after the system was turned on:
the processor
jumped to the reset vector location, did a bit of initialization, tested the memory, but then everything went haywire.
I noticed that the memory test failed on the first byte.
Then the software tried to get more storage by garbage collecting the BASIC program and variables.
Since there wasn't any storage at all, this didn't go well and the system hung before reaching the code that
clears the screen.
We tested the memory chips, using the Retro Chip Tester again, and found three bad chips.
Like the ROM chips, the RAM chips are unusual: MOS Technology
6550
static RAM chip, 1K×4.
By removing the bad chips and shuffling the good chips around, we reduced the 8K PET to a 6K PET.
This time, the system booted, although there was a mysterious 2×2 checkerboard symbol near the middle of the screen (foreshadowing).
I typed in a simple program to print "HELLO", but the results were very strange: four floating-point numbers, followed
by a hang.
This program didn't work the way I expected.
This behavior was very puzzling.
I could successfully enter a program into the computer, which exercises a lot of the system code.
(It's not like a terminal, where echoing text is trivial; the PET does a lot of processing behind the scenes to parse
a BASIC program as it is entered.)
However, the output of the program was completely wrong, printing floating-point numbers instead of a string.
We also encountered an intermittent problem that after turning the computer on,
the boot message would be complete gibberish, as shown below.
Instead of the "*** COMMODORE BASIC ***" banner, random characters and graphics would appear.
The garbled boot message.
How could the computer be operating well for the most part, yet also completely wrong?
We went back to the logic analyzer to find out.
I figured that the gibberish boot message would probably be the easiest thing to track down, since that happens
early in the boot process. 
Looking at the code, I discovered that after the software tests the memory, it converts the memory size to an ASCII string using a moderately complicated
algorithm.
1
Then it writes the system boot message and the memory size to the screen.
The PET uses a subroutine to write text to the screen.
A pointer to the text message is held in memory locations 0071 and 0072.
The assembly code below stores the pointer (in the X and Y registers) into these memory locations.
(This Ghidra output
shows the address, the instruction bytes, and the symbolic assembler instructions.)
d5ae 86 71   STX 71
d5b0 84 72   STY 72           
d5b2 60      RTS
For the code above, you'd expect the processor to read the instruction bytes 86 and 71, and then write to address 0071.
Next it should read the bytes 84 and 72 and write to address 0072.
However, the logic analyzer output below showed that something slightly different happened.
The processor fetched instruction bytes 86 and 71 from addresses D5AE and D5AF,
then wrote 00 to address 0071, as expected.
Next, it fetched instruction bytes 84 and 72 as expected, but wrote 01 to address 007A, not 0072!
step   address byte  read/write'
112235   D5AE   86      1
112236   D5AF   71      1
112237   0071   00      0
112238   D5B0   84      1
112239   D5B1   72      1
112240
007A
01      0
This was a smoking gun. The processor had messed up and there was a one-bit error in the address.
Maybe the 6502 processor issued a bad signal or maybe something else was causing problems on the bus.
The consequence of this error was that the string pointer referenced random memory rather than the desired boot
message, so random characters were written to the screen.
Next, I investigated why the screen had a mysterious checkerboard character.
I wrote a program to scan the logic analyzer output to extract all the writes to screen memory.
Most of the screen operations made sense—clearing the screen at startup and then writing the boot message—but I found one
unexpected write to the screen.
In the assembly code below, the Y register should be written to zero-page address 5e, and the X register should
be written to the address 66, some locations used by the BASIC interpreter.
d3c8 84 5e   STY 5e
d3ca 86 66   STX 66
However, the logic analyzer output below showed a problem.
The first line should fetch the opcode 84 from address d3c8, but the processor received the opcode 8c from the ROM,
the instruction to write to a 16-bit address.
The result was that instead of writing to a zero-page address, the 6502 fetched another byte to write to a 16-bit
address.
Specifically, it grabbed the STX instruction (86) and used that as part of the address, writing FF (a checkerboard character) to screen memory at
865E
2
instead of to the BASIC data structure at 005E.
Moreover, the STX instruction wasn't executed, since it was consumed as an address.
Thus, not only did a stray character get written to the screen, but data structures in memory didn't get updated.
It's not surprising that the BASIC interpreter went out of control when it tried to run the program.
step   address byte read/write'
186600   D3C8
8C
1
186601   D3C9
5E
1
186602   D3CA
86
1
186603
865E
FF      0
We concluded that a ROM was providing the wrong byte (8C) at address D3C8.
This ROM turned out to be one of our replacements; the under-powered EPROM programmer had resulted in a flaky byte.
Marc re-programmed the EPROM with a more powerful programmer.
The system booted, but with much less RAM than expected.
It turned out that
another
RAM chip had failed.
Finally, we got the PET to run. I typed in a simple program to generate an animated graphical pattern, a program
I remembered from when I was about 13
3
, and generated this output:
Finally, the PET worked and displayed some graphics. Imagine this pattern constantly changing.
In retrospect, I should have tested all the RAM and ROM chips at the start, and we probably could have found the faults
without the logic analyzer.
However, the logic analyzer gave me an excuse to learn more about Ghidra and the PET's assembly code, so it
all worked out in the end.
4
The bad chips sitting on top of the keyboard.
In the end, the PET had 6 bad chips: two ROMs and four RAMs.
The 6502 processor itself turned out to be fine.
5
The photo below shows the 6 bad chips on top of the PET's tiny keyboard.
On the top of each key, you can see the quirky graphical character set known as PETSCII.
6
As for the title, I'm counting the badly-programmed ROM as half a bad chip since
the chip itself wasn't bad but it was functioning erratically.
CuriousMarc created a video of the PET restoration, if you want more:
VIDEO
Follow me on Bluesky (
@righto.com
) or
RSS
for updates. (I'm no longer on Twitter.)
Thanks to Mike Naberezny for providing the PET.
Thanks to
TubeTime
, Mike Stewart, and especially
CuriousMarc
for help with the repairs.
Some useful PET troubleshooting links are in the footnotes.
7
Footnotes and references
