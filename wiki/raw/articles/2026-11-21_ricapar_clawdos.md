---
title: "ClawDOS - An AI coding agent for DOS (IBM PC 5160 / 8088)"
source: http://ricapar.net/ClawDOS/
date: 2026-11-21
type: article
sha256: 89495f1a9c876a99bf2110da547c8c6fb104dd9101548bf8f6dd34e2601598d5
---

> HN discussion: https://news.ycombinator.com/item?id=50586292 (84 pts)

ClawDOS | An AI chat and coding harness for DOS, on a real IBM PC 5160 (8088 at 4.77 MHz) 

 Ricapar/ ClawDOS 

 ClawDOS 

 ClawDOS

 An AI coding agent for DOS. 

 It runs on an IBM PC XT: an 8088 at 4.77 MHz, 640K of RAM, a CGA card.

 A (real) human’s note: 

 Backstory: The IBM PC was my first computer. Rather, it was my parents’ first personal computer that I got to use at a very early age.

 It was already obsolete by the time I was old enough to use it, but at 5 years old it was a magical device that I could make do different things depending on what I typed.

 I learned how to type and use DOS so that I could launch some early “Learn the Alphabet” games that my mom had bought me. I learned some elementary-level use of BASIC, but at the time that didn’t progress much further than making some number guessing games and other small projects.

 From there, many years passed but I still have some of the original parts of that PC. I have a collection of vintage machines that mean something to me, with my fully maxed-out IBM PC 5160 being the centerpiece of my collection. It still has a working 20 MB hard drive, but that’s disconnected in favor of a PicoMEM that lets me emulate a hard drive off of an SD card, making experimentation and play much easier.

 Old, meet new. New, meet old: I love intersections of old and new technology. What better way to cross the two than building an AI coding agent to run on DOS on original hardware?

 And of course, what better to build it than an AI coding agent?

 I (read: Claude) built this for my own entertainment. I wanted to see how far I could push an AI coding agent to build something given out of the (modern) norm of constraints. Also, can that something it built then build other somethings? 100% of this repo is written by Claude, with the exception of the text within this box.

 As explained in more detail below, the harness runs on the native OS and hardware and relies on a “bridge” PC in order to handle TLS, which would’ve been more than what an 8088 could handle.

 Type CLAWDOS at the C:\> prompt and talk to Claude. It reads and edits the
files on your disk, writes programs, compiles them with Turbo C, runs them and
looks at what they draw on the screen. It keeps notes between conversations and
picks up where it left off.

 The whole harness runs on the PC. HARNESS.EXE is a 176 KB DOS program that
speaks the Claude Messages API itself: it writes the requests, parses the
streamed reply, runs the tools and keeps every conversation on its own disk.
The 8088 does everything but TLS.

 See it work

 Every screen below comes from a 5160 at 4.77 MHz, emulated in 86Box. The
conversations are with the live API.

 From a sentence to a running program

 One message: “Write PRIMES.C: print the primes below 100. Compile it with
Turbo C and run it.” ClawDOS reads its guide to the compilers on this machine,
writes the source, then compiles, links and runs it in a single tool call. The
answer is on the screen 64 seconds after Enter, 26 of them spent compiling,
linking and running.

 The compiler gets the machine to itself. For a build, ClawDOS saves its state
and leaves memory, Turbo C runs with about 450K free, and the harness comes
back on the same conversation with the program’s output in hand.

 WarGames, written on the XT

 ClawDOS wrote this tribute to the 1983 film on the PC itself: a vector world
map, missiles arcing over the pole, a tic-tac-toe endgame, and a score for the
PC speaker or an AdLib card. Five files of Turbo C, 15 KB of source, a
 WG.EXE under 10 KB.

 Here it is running on the real 5160, filmed off its IBM monitor:

 ▶ Watch the WarGames demo on YouTube 

 It remembers

 Start a new conversation and “your WarGames demo” is all it needs. ClawDOS
opens the note it saved in C:\MEMORY , finds the latest build, and recalls
the palette trick the war scene plays on the CGA.

 It sees the screen

 That Run call asked for a screenshot 25 seconds in. A timer-interrupt hook
copies the CGA’s video memory at that moment, the 8088 encodes it as a PNG, and
the picture goes to Claude with the tool result. This is the file the PC made,
320x200 in four colours, 16 KB:

 And this is what Claude made of it:

 An agent at work

 Asked to make the demo exit on its own, ClawDOS goes looking. It searches the
sources for the keyboard wait, reads the file, says what it found and edits one
line. Each tool call shows in the transcript with its result, and between them
Claude says what it is about to do.

 It plays

 Text art in sixteen colours, straight into the transcript, and music on the PC
speaker in GW-BASIC’s PLAY language.

 The harness

 A chat screen built for the CGA. Replies stream onto the screen as they
arrive, word-wrapped at 80 columns in code page 437. Writes are timed to the
retrace, so there is no snow. The transcript scrolls in hardware through the
CRTC start address, with PgUp and PgDn to go back. The spinner and its seconds
run from the timer interrupt and keep moving while the PC is busy.

 Eighteen tools. Claude works on the machine through these:

 Tools 
 What they do 

 sysinfo , dir , read , search 
 Look at the system, list directories, read files as text or hex, find text across files 

 write , edit , delete , mkdir , rename 
 Create and change files; edit replaces one piece of a file in place 

 run 
 Run DOS programs and batch files and read back what they printed, up to twelve commands in a call, with a screenshot on request 

 peek , poke , port 
 Read and write memory and I/O ports 

 play , textart 
 PC speaker music and coloured CP437 art 

 memory_list , memory_read , memory_write 
 Its own notes, kept in C:\MEMORY 

 A development kit on the disk. Two assemblers (TINYASM and WASM),
Bruce’s C, GW-BASIC and the lDebug debugger, plus Turbo C 2.0, installed from
your own floppy images in external/ . All of them are proven on the 8088, and
ClawDOS knows how to drive each one.

 Memories and skills. Memories are what ClawDOS learns on your PC: what you
built together, what worked, what you like. Skills are guides that ship with
it, such as the dev tools and CGA demo effects. Both are plain text files on
the disk, listed in every conversation’s system prompt and read when they fit
the task. F4 browses the memories:

 Safe mode. On by default. Anything that changes a file, memory or a port
asks Allow ...? (y/n) first. F3 turns it off.

 Conversations that last. Every chat is a file on the disk in the API’s own
message format. F6 lists them, Enter reopens one, and your next message
carries it on. A chat cut off by the power switch reopens too.

 Any model, mid-conversation. /model lists the providers in
 CLAWDOS.CFG and switches between them and their models without losing the
conversation. F5 sets how hard Claude thinks, from low to max. Any host that
speaks the Messages API works.

 Easy on a slow link. The system prompt and tools are cached by the API.
After a conversation’s first request the PC uploads only what is new, so a tool
result goes up in about 500 bytes. A dropped connection or an overloaded API
is retried, and the turn carries on.

 A flight recorder. CLAWDOS.LOG has a line for every round: time to first
token, upload size and time, tokens in and out, cache reads.

 api anthropic claude-opus-5-5 round=1 ttft=2750 total=4015 up=165 len=1784 stop=tool_use in=2 out=221 cr=5543 cw=739 th=cont
relaunch: program 61.5 s, CLAWDOS away 82.3 s

 Under the hood

 flowchart LR
 subgraph DOS["IBM PC XT (8088, 640K, CGA)"]
 direction TB
 subgraph APP["HARNESS.EXE"]
 direction TB
 UI["Chat screen"]
 LOOP["Agent loop<br/>Messages API requests, SSE and JSON,<br/>history on disk"]
 TOOLS["Tools<br/>files, search, DOS programs, screenshots,<br/>memory and ports, speaker"]
 end
 NET["mTCP + packet driver"]
 APP <--> NET
 end

 TUNNEL["TLS tunnel<br/>copies bytes"]
 API["Claude Messages API"]

 NET <-->|"plain HTTP"| TUNNEL
 TUNNEL <-->|"HTTPS"| API

 Machine 
 IBM PC XT 5160: 8088 at 4.77 MHz, 640K, CGA. A PicoMEM card supplies the disk (an image on microSD), WiFi as an NE2000, EMS and a battery clock 

 Code 
 13,000 lines of C and C++, built with Open Watcom for the 8086 instruction set 

 Programs 
 HARNESS.EXE , 176 KB, the whole harness. CLAWDOS.EXE , 29 KB, the launcher you type 

 System 
 FreeDOS 1.4 with mTCP for TCP/IP 

 API 
 The Claude Messages API, streamed: tool use, images, prompt caching, message threads 

 TLS 
 A tunnel on another machine, tunnel/tunnel.py , socat or stunnel . It copies bytes between a plain port and api.anthropic.com:443 . It can also hold the API key, so the key never touches the PC’s disk 

 Memory 
 A program ClawDOS runs gets 200K beside the harness, or 450K when the harness steps out 

 Tests 
 31 boot tests in DOSBox-X against a mock API, unit tests that run on DOS, and runs on 86Box’s 8088 

 docs/API.md has exactly what ClawDOS sends and what it expects back.

 Run it

 You need a Mac or a Windows PC with Python 3, and an Anthropic API key. On
Windows the command is python .

 python3 scripts/setup-tools.py # fetch the compilers, FreeDOS, mTCP and the emulators
echo ANTHROPIC_API_KEY=sk-ant-... > .env
python3 scripts/build.py # build/CLAWDOS.IMG, a bootable disk
python3 tunnel/tunnel.py # the TLS tunnel, on port 8443
python3 scripts/run86box.py # boot an IBM PC XT

 At the C:\> prompt, type CLAWDOS .

 No key? python3 tunnel/mockapi.py plays the API offline: type
 CLAWDOS 10.0.2.2:18023 and send !help .

 On a real PC: build with the address of the machine running the tunnel
( python3 scripts/build.py --tunnel 192.168.1.10:8443 ), copy CLAWDOS.IMG to
the PicoMEM’s microSD card, pick it as the hard disk in the PicoMEM’s menu,
boot, and type CLAWDOS . Later builds update the card’s image in place and
keep its memories and chats
( python3 scripts/build.py --update /path/to/CLAWDOS.IMG ).

 At the keyboard

 Key 

 Enter 
 Send 

 Esc 
 Stop a reply, or clear the input 

 Up / Down 
 Recall earlier messages 

 PgUp / PgDn 
 Scroll back 

 F1 
 Help 

 F2 
 New chat 

 F3 
 Safe mode on or off 

 F4 
 Memories 

 F5 
 Effort: low, medium, high, xhigh, max 

 F6 
 Earlier chats 

 F10 
 Quit 

 /model , /chats , /memories , /new and /quit work from the input box.
 CLAWDOS -m "..." sends a message from the command line and -c NAME reopens
a chat.

 More

 docs/MANUAL.md 
 Setup in full, real hardware, the image updater, other providers, every setting 

 docs/API.md 
 What ClawDOS sends to the API and expects back 

 docs/ROADMAP.md 
 The plan, the benchmark and the memory map 

 Path 
 What 

 src/harness/ 
 HARNESS.EXE: the chat screen, the turn, the tools 

 src/clawdos/ 
 CLAWDOS.EXE, the launcher 

 lib/ 
 The pieces: screen, console, network and HTTP, the API request writer and stream parser, JSON, history, the tool executors, screenshots and the PNG encoder 

 tunnel/ 
 The TLS tunnel and the mock Messages API 

 image/ 
 What goes on the disk: the manifest, the system prompt, the tool schemas, the skills, the tests 

 scripts/ 
 Build, disk image tools, the emulator runners and test harnesses 

 tests/unit/ 
 DOSUNIT.EXE, the unit tests that run on DOS 

 License

 ClawDOS is free software under the GNU General Public License, version 3 or (at your option)
any later version: see LICENSE . HARNESS.EXE links mTCP, which is GPLv3. The FreeDOS
boot sector in src/boot/freedos is vendored unmodified under its own GPLv2-or-later license
(its COPYING ). Disk images you build hold other people’s software (FreeDOS, mTCP, and Turbo C
from your own floppies): don’t redistribute an image with Turbo C on it.

 ClawDOS stands on mTCP , FreeDOS ,
 Open Watcom , the
 PicoMEM , 86Box and
 DOSBox-X .

 This site is open source. Improve this page .
