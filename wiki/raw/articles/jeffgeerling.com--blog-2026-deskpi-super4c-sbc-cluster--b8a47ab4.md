---
title: "SBC Clusters are a terrible value, but they're fun anyway"
url: "https://www.jeffgeerling.com/blog/2026/deskpi-super4c-sbc-cluster/"
fetched_at: 2026-05-02T07:00:43.145184+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# SBC Clusters are a terrible value, but they're fun anyway

Source: https://www.jeffgeerling.com/blog/2026/deskpi-super4c-sbc-cluster/

Pictured above is the new
DeskPi Super4C
installed in an 8U mini rack. The Super4C is a 4-node Raspberry Pi CM5 cluster board that solves two pain points I had with the older
Super6C
.
I was testing this board around the same time I helped kick off the
SBCC 2026
, the Single Board Cluster Competition for students. A dozen or so university teams squared off to run the best mini HPC cluster with a budget of $6,000, and a couple days to benchmark
six HPC workloads
.
I decided to populate the Super4C DeskPi sent me to test with four 16GB CM5s I got
last year
, back when they were $125 each. They're about
$300
today, after the
latest round of price increases
.
I made a video reviewing the Super4C and a new mini rack from Waveshare, the
HomeRack
, and I posted it on YouTube:
In that rack build, I also tested Waveshare's
HomeRack Pi 7" Touch Panel mount
, as well as a
Tripp-Lite mini UPS
that slots nicely into the bottom. If you're interested in the hardware, go watch the video.
The Goldilocks Cluster
The main thing I wanted to point out in this blog post are the two annoyances DeskPi fixed in the Super4C—which I think they fixed by reducing the number of Compute Modules from 6 to 4 (thus gaining valuable board space):
Remote Management
: There's now an ESP32 you can access over WiFi (or, soon, Ethernet) for 'lights out' management of the cluster—at least for power control and monitoring
.
Redundant Ethernet and Power
: This board has two Ethernet connections to each CM5 slot (one 2.5 Gbps NIC off the USB 3.0 bus, and one 1 Gbps connection through the CM5's own Broadcom NIC). It also has dual 19V DC barrel jack power inputs, and will switch between them to whichever one has the higher voltage.
The video has more detail about other board features, but I mention that it's kind of a 'Goldilocks' board for the SBC Cluster enthusiast; it has just enough features to solve the pain points I had with the Super6C, but not so much complexity the price is pushed beyond a hobbyist's budget.
I don't recommend a cluster like this for
value
. The reason you'd buy something like this is for HPC tinkering, on a tiny scale, at your desk, without a bunch of power-hungry used mini PCs or old servers heating up your room.
It could also be useful in some other niche use cases:
A multi-camera / multi-node vision processing system, with one or two cameras per CM5 (up to 8 cameras total, with an AI accelerator for each Pi)
A tiny 4-computer board that has an HDMI display on each node
A small build farm for Arm projects or CI
A tiny redundant edge cluster for lightweight applications
If you just want to build a little homelab, though, and you don't care about learning networking or multi-node deployment/coordination: buy a mini PC. You can get a decent one nowadays for $500-600 with 32 GB of RAM, even with inflated memory pricing.
As it is, a minimum cluster build with four Pi CM5s with eMMC and 2 GB of RAM will cost nearly $600. And the cluster as pictured above is closer to $1,400! Like I said, it's not about value, versus a single beefy machine.
The Competition
It's fun to see how this cluster running on four CM5s with a total of 16 A76 CPU cores and 64 GB of LPDDR5 RAM compares to the SBCC student clusters.
Here's how it stacks up running HPL:
Not a bad showing, overall! In my kickoff speech, I told the students I suspected the team with a cluster of Orange Pi 5 Max boards would have a good shot at the title—and running HPL at least, they were second!
Looking at efficiency, my Super4C cluster was also in the middle of the pack:
The other cluster (PlumJuice) that's neck-in-neck is also running on Raspberry Pi 5s (9 of them), so it's nice to see that consistency in efficiency from cluster to cluster.
The outlier in
both
cases was a cluster of four
Minisforum X1 Pro-370
mini PCs—with their boards ripped out of them so they were more in the spirit of 'Single Board' computers :)
Here's a look at all the specs for the clusters in the top of the HPL results:
The NTHU team's AMD nodes were underclocked for better efficiency (AMD and Intel seem to push default clocks way beyond what's necessary, I guess to one-up each other), and they also
compiled HPL with ROCm against the iGPU
for a bit of a speedup, too.
You can call that cheating, since most people don't look at Minisforum PCs and think "SBC", but I call it a creative interpretation of the rules.
Besides, the NTHU team
didn't
win the overall competition. Team Kent Ridge did, with a cluster of 16 Orange Pi 5 Max's.
I wish the SBCC existed back when I was in college. Since it didn't, I'm glad I can at least
Cosplay as a Sysadmin
and build my own little clusters to compare today.
These cluster projects don't make sense anymore if you just need to run a homelab. But they're quite fun if you want to learn HPC with a cluster that sits on your desk.
