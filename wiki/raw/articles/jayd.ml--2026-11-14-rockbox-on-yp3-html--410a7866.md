---
title: "Porting Rockbox to an undocumented $9 Aliexpress ‘YP3’ MP3 Player with LLMs"
url: "https://jayd.ml/2026/11/14/rockbox-on-yp3.html"
fetched_at: 2026-11-22T10:01:11.461941+00:00
source: "jayd.ml"
tags: [blog, raw]
---

# Porting Rockbox to an undocumented $9 Aliexpress ‘YP3’ MP3 Player with LLMs

Source: https://jayd.ml/2026/11/14/rockbox-on-yp3.html

Rockbox
is a wonderful old custom firmware project for
a variety of MP3 players and iPods. Flashing rockbox to my
Sansa E200
was a seminal moment for me: computers were everywhere, and if they didn’t do
cool things, it was because no one had bothered to program them to do so. Looking
back, that played no small part in my choice of career.
It seems like in 2026 there aren’t any cheap MP3 players that Rockbox supports 
though. Reverse engineering an embedded platform like this is one of the hardest
things I can think of, and I had decided to pay the big bucks for one of those
delicious subsidized token plans to try and push it as hard as I could, and
I did have a dirt cheap $9 Aliexpress MP3 player lying around.
TL;DR: it ported Rockbox to a 512 KiB player, I was barely involved. 
Then, I had it build a re-usable toolkit/set of skills for future ports based on
what worked from the first attempt approach, and Claude was able to get Rockbox 
running on another MP3 player (TS47) in 4 hours.
VIDEO
I made a quick website for the project:
https://rockslop.jayd.ml
Here is the porting toolkit:
auto-rockbox
Enter: The YP3
This is an unbranded player, sold under a variety of fake consonant soup brands
on Amazon as well as Aliexpress. You can order them wholesale from Alibaba for
less than $7 or so each.
It calls itself a
yp3_2.0.43
in the “About” menu as.
This appears to be a listing for a YP3
- the original is gone. I paid $9.71 for mine, shipped.
NOTE: Before you run off and buy one, I have another rockbox port that is probably
a week or two out, it is booting and stable, just needs more acceptance testing.
This device is extremely similar but has 4 MiB PSRAM, so it has fewer compromises
This was $20 on sale
I also have a stack of other random MP3 players I intend to repeat this with
See the project website:
https://rockslop.jayd.ml
Special thanks
If anyone gets credit for this rockbox port, it’s
ilyakurdyukov
- they figured out how to get it into ROM Download
mode (Down + USB), and wrote a utility to dump / write flash. Then I could be
a little slop kiddie and not have to use a soldering iron.
See
the YP3 page
on the project
website for more info.
The good:
It costs $9. If it breaks buy another one.
USB-C and Blueooth!
There is a physical reset button, device is easily recoverable
Unbrickable (if you keep stock bootloader): holding down and resetting brings
you into a DFU USB download mode.
Someone already figured out how to flash and interact with ROM DFU
That ROM DFU mode lets you poke flash and RAM.
The bad
SoC:
Complete mystery meat Chinese “Smartlink SL6801” / Jointbees. Does
not exist online
2x Cortext-M4 r0p1 cpuID
0x410fc241
192 MHz (stock does not vary CPU freq). Has an FPU
Capable of Execute In Place (XIP) from flash, but no cache at all. Slow as dirt.
When XIP-ing code, cpu1 always waits behind cpu0 and can stall indefinitely
if cpu0 is continuously fetching instructions from flash. Very easy to deadlock
SRAM
512 KiB plus about ~30 KiB for packets for the bluetooth radio.
2 MB Flash ROM
128x160 full color LCD (RGB565)
Only 5 buttons - a dpad with a center press (center press is power & wired to 
PMU)
Bluetooth (with an undocumented stack)
It has 512KiB of SRAM, and the smallest existing Rockbox target was 2 MiB, I was
already scrolling Aliexpress for another one, but the LLM said “trust me bro I 
can make it happen” and I decided to try its luck.
The ugly
While the hardware is cheap but functional, stock OS is painful to use
It regularly crashes and watchdogs when in USB transfer mode
Where the port ended up
YP3 running Rockbox
After about a week it was booting a build of Rockbox on a crash diet - every
single buffer had been cut to the bone, but it could start and play audio. 
Tuning, bug fixing, etc took another month or so.
I am not aware of anything that isn’t working hardware wise.
The main feature you lose is concurrency while playing music and plugins. Codecs
and plugins are already loaded and swapped around at runtime with normal Rockbox,
but on this player there is one shared 128 KiB arena for both, so starting a 
plugin stops music playback.
Other cuts include:
No voice
Only English is supported
DSP:
No pitch/speed control, surround, crossfade
Cuesheets
album art
Theme backdrop pictures
No dircache, so folders are read straight from SD card
Large folders are truncated by default at 256 (configurable from 32 to 512)
Playlists are capped at 400
Codecs: WMA Pro, Musepack (MPC), RealAudio (Cook), and the chiptune formats 
SID, NSF, VGM, KSS, HES, SGC, ASAP. WavPack (16-bit), (24-bit/96 kHz)
What made it, somehow:
MP3 (up to 320 kbps), AAC/M4A (AAC+ too, HE-AAC v2 plays in mono),
WMA, Opus (up to ~192 kbps), Ogg Vorbis, FLAC (stereo, up to 24-bit/96 kHz), 
ALAC, WAV, AIFF, AU, TTA, APE, Speex, MOD, SPC, AY, GBS, A52/AC3, ATRAC3, 
Shorten, ADX, VOX, SMAF.
The database.
The database has a new variant that is disk only and has synchronous, blocking
updates (ie the player shows a loading screen and stops music when it refreshes
and doesn’t refresh in background). I think it also cut the “songs by letter”
menu.
The database requests memory for its menus at runtime, and depending on the
size of your theme it can refuse to open the menus.
Themes, without backgrounds. load and work, although heavy themes can cause the
database to stop opening (handled gracefully with a warning)
Bluetooth
Overnight Claude reverse engineered the bluetooth stack and wrote a bluetooth 
HAL for Rockbox. I asked it before I went to bed and it was working in the
morning.
No binary blobs are shipped: the bt stack is burned into chip ROM (not flash),
and the YP3 bluetooth driver calls into the stack.
A note on codecs
Most of the codecs run from SRAM as normal. MP3, AAC, WMA, Vorbis and Opus, 
however, wouldn’t fit in our arena nicely, so they run from flash.
But, our XIP flash is dirt slow, so lots of very careful profiling was done to 
move hot code loops back into SRAM. This kind of profiling had to be done
all over Rockbox to get hot loops into SRAM - font rendering, alpha blending,
scrolling, etc. This is where most of the “weeks of polishing” went.
Battery Life
Largely comparable to stock. I hooked the player up to the PC’s line in or
fake bluetooth sink and set it to repeat Daft Punks
Random Access Memories
. A 
script on the PC detected when it cut out.
Stock:
21.29 hours wired, 20.07 on Bluetooth
Rockbox:
20.07 hours wired, 19.3 on Bluetooth
There was some variation in the battery voltage at start, and this was just
one run, so expect some variation.
Battery life is surprisingly impressive on this player,
Approach
I’m one of those software guys, I can’t solder or find UART pads to save my life.
This was an entirely software only port; I haven’t ever opened mine up.
I hooked up ghidra-mcp and let it start pulling the firmware apart. It figured
out how to inject tasks into the running RTOS (FreeRTOS) in bootloader mode. 
This allowed it to probe the hardware and even write drivers before attempting a
Rockbox boot.
To be clear: this is
100% vibecoded
. I have only glanced at some of the code 
it wrote. I contributed my approach to development and testing, was the PM and 
QA person, and the agent’s little meat robot to reboot it when it crashed or 
wander around my house with headphones on while it tuned the bluetooth radio.
I haven’t doneC and firmware development for years.
Cleanroom
Initially I let the same agent do the reverse engineering as implementation.
Later I had it go through and rip out anything that wasn’t a hardware fact (ie
a register) and re-did the drivers with a cleanroom setup. One dirty agent with
Ghidra, one referee agent in between to make sure nothing leaks, and the implementation
agent. Subsequent ports used a variation of this setup from the beginning
The most work I have done personally on this project is writing this blog post.
Robotic eyes and ears
Webcam pointed at the screen, so the model could see what the player was
doing and to work on the LCD drivers.
Webcam mic for bringing up the speaker
(had to yell at Claude when it decided to start playing tones at 2 AM)
Headphone jack plugged into Line In on my PC (finally, I used it!!)
This allowed it to test and tune audio output.
Bluetooth adapter. I plugged in a bluetooth adapter and gave it full reign
for testing. It used Google’s
Bumble
python
bluetooth stack to have the PC pretend to be headphones
Claude kept picking “We Will Rock You” as a test track. I choose to believe this
is evidence of a subtle sense of humor when working on a Rockbox port
Opus 5.5 »»»> Sol
This port was started with Codex/Sol 5.6. It was making progress, but was incredibly
risk averse and slow. It took it 5 days or so and dozens of manual resets on my
part until it felt ready to flash something and boot it.
I should have told it how to figure out how to arm the watchdog and reboot into
download mode itself sooner. Codex got it to showing the rockbox logo with buggy
drivers stubbed out, but had clearly lost its mind in the meantime. I hadn’t 
been paying attention too closely, but as it had spun around it had:
Created 55 GB of files in 2,567 dirs. 3.87 million files total
443 one off tool scripts, 384 documents written
an incredibly paranoid flasher that would check each block as it was written 
and took 15 minutes to write 2 MiB
This flashing script - and many other tool scripts - would check the sha256
of the
documentation files they depended on
to ensure nothing had changed.
It’s kind of beautiful in its own insane way: this seems to be an attempt to
work around multiple agents and memory limits. Madness though
An MCP server with tons of ceremony and tools around flashing things, running 
tests, etc
Claude immediately threw that garbage away and wrote like a few python scripts
to use instead. Auto mode in claude code helped too.
The subsequent TS17 port went from me plugging it in to a usable alpha build
in about 4 hours with Opus 5.5 (there was little to re-use from the YP3 other 
than scripts and skills).
Bidirectional Rockbox Dev Shell
This is one of the most valuable things it did. Rockbox has an existing one-way USB 
serial driver for logs. I had that extended to have dozens of little commands to
drive the player, everything from injecting keypresses to taking screenshots to 
debugging the bluetooth radio.
This was critical for completely hands off development - I had it build a torture
test suite in Python that would monkey-test the player for hours, pressing
buttons at random. Many bugs were found doing this - including some in Rockbox
upstream. At this point the player has hundreds of hours of bench testing under
Rockbox - I could just leave it running and Claude would patiently watch the
test logs for new failures to diagnose and fix.
An agent can reboot to recovery, flash firmware, reboot into Rockbox, run tests,
see what is on the screen, hear what it is doing, completely on its own. Most of
the development of this project happened while I was asleep.
Audio Tuning
For audio (and battery endurance testing) Claude had me set up a 3.5 mm splitter 
with one end going into the PC’s Line In and the other going into real 
headphones to provide an actual load.
Then I had it build a test suite and file that plays a variety of sweeps and 
test tones. I used an Apple lightning adapter to use as the ground truth for this
setup, then used it to compare audio levels and frequency response.
My PC’s sound card is not high sensitivity equipment, but this is enough of a 
sanity check for me.
More charts that I don’t understand</summary>
</details>
The Hardest Parts
There were two tricky things to work out that Claude struggled to fix. 
The exact power off sequence took quite a few tries, probably because it was the 
only thing I had to be there to test, it couldn’t just work on it for hours 
overnight.
The other crazy bug was that the FM radio sounded terrible. You
could tune to a station, but the sound was distorted and clipped. Claude spent
forever trying to figure out why, but eventually I noticed that the frequency
it was tuned to did not match the station identifier over the air.
It turns out the tuner had been set up with a slightly wrong clock source, so it
was ~4 MhZ off. It just so happened to work out that when I tuned it to my test
station, it could kind of lock on to another one, but sounded terrible.
Other New Features
Plugin Psychosis
I told Claude to port as many games as it could to Rockbox.
This release adds
THREE HUNDRED AND FIFTY SEVEN
new plugins. That is not a 
typo: 357. Most of these are ports, a few are originals. Given the quantity here
I haven’t done enough QA here.
Originals
RockGPT
This is going to get its own blog post because it is deeply amusing. A ~1 million
param model running on your MP3 player. Almost coherent, fine tuned to be aloof
and dismissive of humanity. Weights are streamed from SD card. Crazy
RockTrack
A little tracker/chiptune editor for Rockbox. I haven’t had a ton of time to 
test this one. Probably needs ergonomic improvements.
Video Player
Rockbox’s existing mpegplayer didn’t fit on the YP3 and I didn’t want to hack
it up too much, so I had Claude write a new one, with a nicer pixel art UI,
MKV support. AVI, MKV, MP4; MPEG-1/2, MJPEG.
Ports
There are too many to list.
Here is the full set of ports
Anarch - FOSS DOOM clone
Celeste Classic - Platformer Maddy Thorson, Noel Berry
MicroCity City builder, jhhoward
Prizm Racing, Racing, duarteapcoelho
Rockcraft Minecraft-style block sandbox, port of Blocks-TI-84 by The Science Elf, MIT
Terrario, Terraria-like KBD2
Jet Island, 3D island demo CubeCoders
Rock88, 3D rendered Film player demo JetExamples
Bulk Ports
We got to stupid plugin numbers by writing compat shims/libraries for several 
popular open source players:
Misc Features
Themes
I had it port some themes from the Rockbox website to work on this screensize, 
add a bluetooth status icon, and it generated 5 original themes: Ukiyo (my 
favorite), Asterism, Chaldani, Lavenia, Cyanotype.
Note: This is a WIP screenshot, there have been bug fixes & some of these got
cut because of unclear licensing.
Note that heavy themes can cause some issues, so I would suggest sticking with
lightweight ones.
Fin
Well, reverse engineering a completely undocumented chipset was one of the 
hardest things I could think of to do, and Claude can ace it. I’m planning on
porting Rockbox to a bunch of other cheap MP3 players.
THEY ALL SHALL RUN ROCKBOX!
Appendix: Identifying a YP3
There are lots of clones that look like each other. The YP3 specifically:
Only has 5 buttons - dpad and center
no power, volume
symbols molded into buttons, not printed on them in white
Has a reset pinhole on the
right
Speaker on
top
rear
USB on bottom right, headphone jack on left
SD card on the left
I think they’re all black
Also, these screens are made of cheese, you’ll want a screen protector.
