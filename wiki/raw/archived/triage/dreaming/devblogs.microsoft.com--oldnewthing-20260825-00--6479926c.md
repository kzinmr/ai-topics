---
title: "Why didn't the Windows Entertainment Pack just run the MS-DOS version inside an emulator?"
url: "https://devblogs.microsoft.com/oldnewthing/20260825-00/?p=112645"
fetched_at: 2026-08-27T10:01:12.640156+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why didn't the Windows Entertainment Pack just run the MS-DOS version inside an emulator?

Source: https://devblogs.microsoft.com/oldnewthing/20260825-00/?p=112645

I mentioned a little while ago that
Tony Krueger reverse-engineered the MS-DOS verison of Chip’s Challenge and then reimplemented it in Windows
. Somebody asked, “Why did he have to do that? Why not just run the MS-DOS version inside an emulator?”
This is sort of like asking
why they didn’t use the Space Shuttle to rescue the Apollo 13 astronauts
.
The system requirements for the Windows Entertainment Pack
was an 80286 processor or better, Hercules, EGA, or VGA graphics card, a mouse, Windows 3.0, and 1MB of memory. The system requirements for th MS-DOS version of Chip’s Challenge was
512KB of RAM
. So you have to fit all of Windows
and
the emulator into that 1MB of memory. Maybe you’re really parsimonious and you can squeeze Windows into 256KB of memory, and the RAM for the emulated system is 512KB, and 64KB for the emulated video card. That leaves you 192KB of RAM to write your emulator.
The target CPU for Windows 3.0 was the 80286, which does not have support for virtualization. So you’ll have to write an instruction-level CPU emulator. This sounds hard, but that’s probably the easiest part. You also need to emulate all the hardware: The keyboard controller, the timer chip, the interrupt controller, the video card, the hard drive, and whatever other stuff the program needs. The trickiest part is probably emulating the passage of time properly, because games in particular and I/O devices in general are often coded using timing loops, where the code knows that executing a specific number of instructions takes a specific amount of time, so it can, say, issue a command to the PC speaker, perform
exactly
150 cycles of game logic, and then come back to issue the next command to the speaker at exactly the right moment. Or issue an I/O command to the hard drive I/O port to start moving the read head, and then wait exactly 300 cycles, and then issue another I/O command to stop moving the read head, and expect the head to be exactly at a particular track.
And you have to do all this precise timing while co-operatively multitasking against other Windows applications that are running.
Oh, and in 1990, your premium desktop PC was running a 486DX-33. A budget PC would be running an 80286 at around 10 MHz. The
DOSBox emulated CPU equivalency table
says that emulating an 80286 at only 6 MHz would require a Pentium Pro 200 MHz processor. This is a processor that wouldn’t be invented for another five years. The DOSBox project itself didn’t begin until 2000. PC emulation wasn’t really a thing back in 1990. The processors of the day weren’t powerful enough to do it well, and the engineering experience with x86 emulation was not there.
Even if you managed to transport back in time with better hardware and an additional 30 years of software development experience and get the game running inside an MS-DOS emulator, the emulated experience is horrible. After all, you didn’t port the game to Windows. You’re just running it in an emulator. The graphics will be MS-DOS graphics, and they won’t resize when the user resizes the game window. The inputs will be keyboard-based, even though Windows has a mouse. The original MS-DOS version didn’t have a way to save your game. It just gave you a level code once you completed a level, and you can enter that code later to jump back to the level you were on when you quit. Running the program in an emulator means that you can’t add features, like a “High scores” list, or a proper “Save game” function that remembers not just the level you were on but also your total score up to that point.
The Windows version of Chip’s Challenge had to be a port to Windows, not just running the game inside an emulator.
Related reading
:
Running old programs in a virtual machine doesn’t necessarily create a good user experience
.
Bonus chatter
: Why did Tony have to reverse-engineer the MS-DOS version anyway?
My understanding is that the reverse-engineering was primarily focused on figuring out how the puzzle levels were encoded in the data files. The game play itself could be reverse-engineered largely by observation.
Yeah, but that doesn’t answer the question. Why reverse-engineer it? Why not just have the vendor tell you what the format is?
Tony set about porting Chip’s Challenge to Windows
before
the licensing agreement was signed. He was secretly working on the project before the lawyers said it was okay to start. Therefore, he had to rely only on his own wits. And that meant reverse-engineering the file format, because he legally couldn’t yet ask for it.
Related reading
:
Another example of starting a project before the licensing agreement is signed
.
