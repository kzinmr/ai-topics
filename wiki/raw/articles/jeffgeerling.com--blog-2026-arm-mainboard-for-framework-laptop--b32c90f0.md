---
title: "An Arm Mainboard for the Framework Laptop"
url: "https://www.jeffgeerling.com/blog/2026/arm-mainboard-for-framework-laptop/"
fetched_at: 2026-04-29T07:02:13.674045+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# An Arm Mainboard for the Framework Laptop

Source: https://www.jeffgeerling.com/blog/2026/arm-mainboard-for-framework-laptop/

Using the repair-friendly Framework 13 laptop chassis, I've tested the low-end x86 option (a
Ryzen AI 5 340 Mainboard
), the fastest RISC-V option (
DC-ROMA II
), and today I'm publishing results from the only Arm Mainboard, the
MetaComputing AI PC
, which has a 12-core Arm SoC and up to 32 GB of soldered-on RAM.
My Framework 13 has run on x86, RISC-V, and now Arm, making it something of a 'Ship of Theseus'.
The AI PC Mainboard uses Cix's P1 SoC, an odd duck in the Arm world. There are 12 CPU cores, but they're structured in a way that necessitates disabling four of them to run Windows 11—and yes, this board
should
be able to do that.
I have a video going over my experience swapping out the Framework 13's guts and testing everything (including setting up FEX and playing some x86 games through Steam):
If you'd rather read than watch a video, scroll on!
Hardware
The AI PC Mainboard features the Cix P1 CP8180, a chip that's also found in Radxa's
Orion O6
,
Minisforum's MS-R1
, and the
Orange Pi 6 Plus
.
RAM chips are soldered to the mainboard (16GB of LPDDR5 in the review sample I was provided), and all the typical I/O for a Framework Mainboard is present (a M.2 NVMe slot, a WiFi module slot, display, keyboard, sound, and battery connections, and four USB-C ports for high-speed peripherals, power input, and display out).
It was easy to swap out mainboards so I could test this build in a chassis. And my first question was whether this mainboard fixes the major drawback of the Cix P1 chip: idle power consumption.
And it does... a little. Compared to the other Cix P1 systems I've tested:
But we're still far from ideal—here's a comparison to the MacBook Neo, and Framework's lowest-spec AMD Mainboard (which is also faster and about as efficient as the Cix CPU in heavy workloads):
Software
MetaComputing currently provides an 'official' Ubuntu 25.04 ISO you can flash to an NVMe drive to boot with full hardware support, but this laptop has a full BIOS, with UEFI support.
However
, not all distros are supported yet... I didn't test any other distros yet, but
Windows for Arm at least partially installed
, which is a good start.
But running their official Linux build, I was able to run Vulkan and OpenGL on the chip's Arm Mali G720 Immortalis iGPU. I had some trouble with
vkmark
, but
GravityMark scored 7,627
, comparable to the graphics in Apple's A14 SoC, and a little faster than Intel's low-end graphics in chips like the N150.
Geekbench scores
are right in line with the other Cix P1 systems I've tested, though
High Performance Linpack scores
are not. I'm not sure if it's the slightly slower memory, or what, but this system scored about half as well as the MS-R1 and Orion O6 when running the memory-intensive FP64 HPL benchmark.
But rather than compare the chip against itself, let's put the numbers in context, using Geekbench, as it's a good proxy for general perceived performance for smaller systems:
Apple Silicon takes the cake in single core performance, but the Cix chip having 12 cores almost makes up for that. Having a
fan
also helps with sustained loads—the Framework Mainboard just about ties the MacBook Neo when running HPL, since the Neo starts throttling after a minute or two of sustained load.
But when comparing this mainboard to the one closest in price (taking RAM into account) made by Framework themselves—the
Ryzen AI 5 340
—it falls both in single and multi-core performance. Add in the compatibility issues with Arm Linux and Windows for Arm which currently exist, and it really limits the potential to grow beyond the niche of Arm devs who might be interested in the AI PC Mainboard.
Fex for Steam Games on Arm
Your browser does not support the video tag.
Just to see whether this system would be useful for Steam games in its current form, I followed Ubuntu's
guide for running Steam games on arm64 with FEX
, which worked without a hitch. I had also tried installing
box86/box64
for comparison, but ran into some problems.
Steam ran without issue (albeit a little slow), and I could download games like Doom Eternal at 500+ Mbps. But when it came to gameplay, the games were quite choppy—even older, simpler games like Horizon Chase Turbo at the lowest resolution settings (see embed above).
Portal 2 ran, but stuttered quite a bit (to the point of being unplayable), and I couldn't get either Obduction or Doom Eternal to launch, possibly due to memory requirements (the 16 GB of RAM is shared between the system and the iGPU).
Conclusion
You can find all my test data and any further updates in the
MetaComputing AI PC issue
in my SBC Reviews project.
And you can buy the MetaComputing AI PC Mainboard (either standalone, or as part of a Framework 13 build) direct from MetaComputing:
AI PC Arm Mainboard
.
In the end, I think this Mainboard has a lot more potential at the launch price of $550. Unfortunately, with the DRAM crisis, the price is pushed a little above the 'maybe I'll pick one up and tinker with it' range, and thus I can only recommend the AI PC Mainboard to Arm enthusiasts.
For everyone else looking for the best value low-end Arm laptop: get a MacBook Neo.
