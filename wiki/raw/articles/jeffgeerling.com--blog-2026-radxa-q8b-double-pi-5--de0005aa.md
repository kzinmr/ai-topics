---
title: "Radxa's Q8B has 2x the performance and expansion of the Pi 5"
url: "https://www.jeffgeerling.com/blog/2026/radxa-q8b-double-pi-5/"
fetched_at: 2026-10-10T10:00:52.621011+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Radxa's Q8B has 2x the performance and expansion of the Pi 5

Source: https://www.jeffgeerling.com/blog/2026/radxa-q8b-double-pi-5/

There was a time I'd look at a board like the
Radxa Dragon Q8B
(at left, above) and be like, "there's no way I'd spend $209 on an SBC with 8 gigs of RAM". But we're in 2026, and seeing the 8 gig Raspberry Pi 5 going for almost the same amount, I figured I'd give it a shot.
On
paper
, the Q8B beats the Pi 5 in pretty much every way. A lot of that is thanks to this Snapdragon 8cx Gen 3 chip, which is the same chip
I tested on Microsoft's Windows Dev Kit 2023
.
It has twice the CPU cores, a way faster GPU, a built in NPU, a newer process node for better efficiency, way more PCI Express lanes to play with, multiple built-in M.2 slots, dual 2.5G networking...
I mean, I could go on, and yes it's a slightly larger board. But once we're in the $200 price range, we're talking the realm of mini PCs. But instead of Intel or AMD, Qualcomm promises better efficiency.
And the Windows Dev Kit only ran Windows officially, but this board
should
be able to run any arm64 flavor of Linux, too (including Radxa's own OS). This strange love-child between Qualcomm and Radxa might prove to be the start of an interesting new era in SBCs. No longer is it mainly Broadcom, Rockchip, and Allwinner. Qualcomm might be finally breaking into the hobbyist market, though it's not without hiccups.
This blog post is a condensed version of the information in the video above; I left out some of the experiential aspects of using the Q8B in this blog post, since they're more easily conveyed on YouTube. But please continue reading for more notes on performance and usability, compared to the Raspberry Pi 5.
Getting Started - Choosing an OS
The first hiccup is selecting an operating system to run. Like other Radxa boards, instead of just pointing you to one download, the
System Installation Guide
is more like a choose-your-own-adventure. And you get to decide what storage medium you'll use (some require different techniques), whether to use the link in the Wiki or one on a GitHub release page, and whether to run Debian or two flavors of official Ubuntu-derived OSes.
And that's before I tried installing a generic arm64 OS via USB. I've detailed that process in my
Dragon Q8B benchmark issue
, and spoiler: I still haven't been able to boot a generic arm64 ISO to install to NVMe storage. Follow
this thread on the Radxa Community forum
for more.
I'm not saying all this to harp on Radxa. They're certainly a lot better than some
other
SBC vendors. But I keep saying this, year after year. One reason I stick with Raspberry Pi when I need to get a project done is—despite weaker hardware and fewer options—
it's easy to get started
. And I don't have to spend time in the forums just to figure out the best way to turn it on.
Usage
Overall, at least running Radxa OS, the board feels like an N150 mini PC, maybe even a bit faster. Firefox is the default browser, and YouTube plays back in 4K just fine, and the UI is snappy (which I can't always say for Pi 5-era SBCs).
There are two 2.5 Gbps Ethernet ports, an M.2 2230 slot on the topside for WiFi, dual M.2 2280 slots on the bottom for NVMe or other expansion, a PCIe FPC like on the Raspberry Pi 5, full GPIO, and even another PCIe flat connector on the bottom that doesn't seem to be documented in the Wiki.
I haven't gotten in a ton of testing with the I/O on this board, but if Qualcomm doesn't run into the same PCIe compatibility quirks as other arm64 platforms, you could do a
lot
with this board.
I was about to run
apt upgrade
so I'd be on the latest versions of everything for benchmarks, but I'm glad I kept reading through the
Getting Started Guide
.
Apparently
you're not supposed to use apt to upgrade things on here. You're supposed to use Radxa's 'Rsetup' tool. I have to ding Radxa on this: If you're maintaining a custom distro, the least you can do is make sure things like system updates work using the standard tools (in this case
apt upgrade
).
If that doesn't work, and it breaks someone's install... that just shouldn't happen. Rsetup is useful for hardware configuration, but I hate that in 2026 we still have custom tools for standard operations like this—at least using Radxa OS.
Performance
Besides some odd behavior with network download speeds (and not always, but in some instances like downloading Geekbench or some video files), the performance of this board was excellent, especially compared to SBCs in the same class as the Pi 5.
Just looking at Geekbench, it's not the best benchmark in the world, but it's good for a relative comparison. The Q8B's not quite double the speed of the Pi 5, but it's a major improvement. Radxa's slightly cheaper Q6A holds up well with
its
8 cores, but the Q8B
really
trounces these two in multicore.
It's more than twice as fast as the Pi. It's not quite like an Apple M1, but to have this type of performance on a tiny SBC is huge.
HPL, which really crushes the CPU and RAM, is also showing a huge jump from Pi 5 performance.
And even using more power, the overall efficiency is better. It's not quite as good as the more efficiency-focused ARM SoCs, but it's pretty good.
But idle power was interesting. I noticed Radxa has this thing set in performance mode by default, so it'll always be burning a little more power when it's doing nothing.
I don't know if it's for stability, to juice benchmark numbers, or what, but that is something I noticed. The chip also pulls 20+W under full load, so having a 65W power adapter is important, especially if you have NVMe, WiFi cards, that sort of stuff.
And of course this thing's 2.5 gig port blows away the 1 gig network that was standard on most of the previous generation SBCs.
3D performance was also way better, but we
are
talking about a chip that's built for this stuff. The Pi's SoC just doesn't have the same grunt.
Memory speed's also up, which helps a lot if you're doing something like running a local LLM or doing image processing.
But the overall picture is that for around the same price, you're getting a lot more performance. And Qualcomm
seems
committed to Linux support, in a way that Rockchip never was. They've actually put some resources into it, and it seems like Radxa's taking advantage of that.
For
all
my benchmark data and more comparisons, visit my
SBC Reviews website
.
Conclusion
There's one big problem, though:
getting
a Q8B. It doesn't matter how good it is if you can't buy one. Here in the US, they're in short supply. I bought mine from ARACE, but I ordered it in June, and it showed up in September.
A three month lead time isn't great if you're building something important with your SBC. With Raspberry Pi, at least, I can drive 10 minutes to Micro Center and pick one up right now. Or I could order one from PiShop and have it here in a week or two. At least... some models.
It seems like SBCs might be nearing shortage-level supplies again, if
this PiShop page
is any indication.
It's a tough time for the SBC market. I said it before,
the SBC hobby is dying
. And if it's not prices that'll put you off, it's just... getting them in the first place.
I really hope we can get past this, like we just barely did with the component shortages. But what will things be like on the other side? Your guess is as good as mine.
