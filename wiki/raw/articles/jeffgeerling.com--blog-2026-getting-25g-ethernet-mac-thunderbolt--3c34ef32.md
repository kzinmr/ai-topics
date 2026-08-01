---
title: "Getting 25 Gbps Thunderbolt Ethernet on my Mac Studio"
url: "https://www.jeffgeerling.com/blog/2026/getting-25g-ethernet-mac-thunderbolt/"
fetched_at: 2026-08-01T10:13:01.364391+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Getting 25 Gbps Thunderbolt Ethernet on my Mac Studio

Source: https://www.jeffgeerling.com/blog/2026/getting-25g-ethernet-mac-thunderbolt/

I've been using the built-in 10 Gigabit Ethernet on my Mac Studio for a few years. It works fine: I can edit 4K video straight off my NAS over the network, and run backups at around 1 GB/sec.
But... I want
more
. I upgraded my rack and my NAS to 25 GbE a couple years ago, and wanted to upgrade my main workstation, too.
I looked up 25G networking options for the Mac, and they're all
crazy
expensive:
The problem is Macs all require Thunderbolt adapters; you can't just plug an inexpensive(ish) PCIe card into a Mac (RIP Mac Pro).
I stopped looking until I saw
this blog post
. Christian Kohlschütter found a
cheap 25G Thunderbolt adapter
that uses a server-pulled OCP 2 NIC with a little Thunderbolt 3 adapter board. And it works on any computer with Thunderbolt.
Back in January, it was only $160, which was insta-buy territory for me. Since that time, the Amazon listing jumped to
$299
, which still might be good compared to the Sonnet... but you might have to go digging through some Chinese sites to find a non-marked-up version now.
This blog post is a companion to the following YouTube video:
First Test - Two Problems to Solve
Once I had pulled some new fiber to my desk (where I only had Cat6A cabling before), I tested the bandwidth using
iperf3
between my Mac and my NAS. That's when I ran into two problems:
The version of
iperf3
I was running on the NAS was too old. Without multi-threading, it maxed out at 15 Gbps.
The 25G NIC enclosure was getting
hot
. Painful to the touch.
I could solve the first problem easily: I compiled the latest version of
iperf3
. That got me to 20 gigabits, since more than one CPU core could hand the transfers on my NAS. As Christian mentioned in his blog post, 20 Gpbs single direction and 25 Gbps bidirectional is about the limit for the Thunderbolt 3 chipset being used (even if you plug into a Thunderbolt 5 port).
But the second problem was more tricky.
The burning-hot enclosure wasn't thermally bonded to the OCP 2 network card, meaning the NIC chips were
cooking
.
They had tiny heatsinks on them, but OCP 2 NICs are meant to be inside servers with high pressure fans, not in a little passively-cooled enclosure.
It was acting like a little oven.
Fixing the NIC's cooling problem
Christian mentioned he slapped a couple giant heatsinks on the enclosure. That brought the chip down to a temperature that wouldn't cause NIC dropouts, but it was still getting pretty hot.
I wanted to make sure things were stable, and that meant active cooling.
My first idea was to stick on
these low-profile heatsinks
and set
this speed-controlled USB fan
in front. I had to remove the enclosure's barely-ventilated front plate to get more airflow inside, but the back plate also created a ton of resistance.
It would still get hot, and the fan was just loud enough to be distracting, even on its lowest setting.
A Prusa rep had reached out around this time asking if I had any use for their new
Prusament PLA in Noctua Brown and Beige
... and I decided to switch tracks once they offered to send a spool of each. I purchased a
Noctua NF-A8 80mm 5V fan
, and an
NA-FC1 Speed Controller
to silence it.
I designed a
fan duct for the 25G Thunderbolt NIC enclosure
, and printed it in Noctua beige PLA.
Then I printed this
airflow-optimized 80mm fan grill
, and screwed that on the front of the 80mm fan.
I was able to use the screws from the 25G NIC enclosure (I removed the front plate entirely), and the fan screws and extra cable that came with the Noctua 80mm fan, to secure everything together.
I chose to splice the braided fan extension cable Noctua includes, and taped it down inside the enclosure with kapton tape for some strain relief.
I soldered the cut end of the fan cable into these through-holes on the Thunderbolt-to-OCP adapter PCB to get the needed 5V power (well, 4.8V, but it's close enough):
The fan only used about 0.5W of power, so I don't think it'll cause any brownout conditions on the NIC itself (which uses 4-5W total at idle).
After final assembly, this is what it looks like:
I plugged it in, re-tested with
iperf3
, and checked the temperature. It was sitting at less than 36°C after 10 minutes, with the fan on low. And this being a Noctua fan, I couldn't hear it at all under the desk.
How does 25 Gbps perform on the Mac?
Like earlier, it maxes out around 20-25 Gbps, because of the slower Thunderbolt 3 connection.
Testing Samba file copies between my NAS and my Mac, I got around 1.4 GB/sec read, and 1 GB/sec write
.
That's only marginally better than the built-in 10G Ethernet. It's an improvement, sure... but was all the work pulling fiber, designing a fan cowling, paying $200 for all the parts, and assembling everything worth it?
Maybe. At least I got this blog post out of it.
