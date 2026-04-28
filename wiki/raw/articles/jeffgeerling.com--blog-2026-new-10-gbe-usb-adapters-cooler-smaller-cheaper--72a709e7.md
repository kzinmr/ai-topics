---
title: "New 10 GbE USB adapters are cooler, smaller, cheaper"
url: "https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/"
fetched_at: 2026-04-28T07:02:52.797981+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# New 10 GbE USB adapters are cooler, smaller, cheaper

Source: https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/

For years, the best way to get 10 gigabit networking on laptops was to buy an expensive, large, and hot 10 GbE Thunderbolt adapter. With new RTL8159-based 10G USB 3.2 adapters coming onto the market, the bulky adapters might be a thing of the past. Just look at the size of the thing in comparison to my Thunderbolt adapters:
2.5G
and even
5G USB adapters
have been out for a while, but sometimes you need more bandwidth.
The 10G adapter I'm testing is
this $80 model from WisdPi
. That's double the price of most 5G/2.5G adapters, but less than half what I paid for my Thunderbolt 10G adapters.
If you
need
10 gigs, this might be the best option, if you use RJ45 and not SFP+. If you
don't
need 10 gigs, a 2.5 or 5 Gbps adapter is still the best value.
Also, you might not even
get
10 Gbps with these new adapters, depending on your computer. I'll summarize why after the video:
USB is
fast
frustrating
I tested this adapter on four computers:
Framework 13 with AMD Ryzen AI 5 340 (includes USB 4 / USB 3.2 Gen 2)
MacBook Neo (USB 3.1 and USB 2.0)
M4 MacBook Air (USB 4 / USB 3.1 Gen 2)
Desktop with AMD Ryzen 7900x with B650 motherboard (USB 3.2 Gen 2x2)
Getting those specific USB port specs is a bit of a chore (some websites don't even tell you if it's '3.2 Gen 2' or '3.0', and Windows itself only says "USB 3.0" when you plug in a USB 3.2 Gen 2x2 device like the 10 Gbps NIC!)
I was only able to get
full
10 Gbps speed (minus a little overhead) on the AMD Desktop, which has a single USB 3.2 Gen 2x2 port good for 20 Gbps of throughput. The other machines got around 6-7 Gbps:
The Macs have the same per-port bandwidth (USB 3.1 Gen 2x1, for 10 Gbps), but the performance is consistently worse than the Framework.
On the Macs, the adapter was correctly identified when I plugged it in, and worked straightaway, with no extra driver installation. The 'Hardware' tab in the Network settings incorrectly reported a connection speed of
2500Base-T
.
On Windows, the adapter was recognized when plugged in, but wouldn't connect to the network until I installed the latest Realtek driver, downloaded from their website.
Bidirectional bandwidth testing offered an interesting contrast; the Macs both handled traffic symmetrically, while the Framework was wildly disparate. The desktop PC gave a full 9.5 Gbps down, and around 5 Gbps up.
The main takeaway is this adapter only reaches its full potential if you have a USB 3.2 Gen 2 2x2 20 Gbps port.
And considering the mess of USB naming over the past decade—and the fact Microsoft reports
all
USB 3.x connections as "3.0" in their Device Settings pane, good luck figuring out your own computer's support without glancing at spec sheets!
A few computers I've seen actually label the USB port speed (e.g. '10' or '20'), but that seems fairly rare. Most manufacturers seem to follow Apple in eschewing labeling entirely!
At least Apple has the negotiated port speed visible in the 'System Information' app—I couldn't find that detail anywhere on Windows.
5G and 2.5G a better value?
With reduced speed due to inadequate USB port bandwidth, would a 2.5 Gbps or 5 Gbps adapter be a better value?
Testing the
WisdPi 5 Gbps adapter
pictured above on my M4 Air, it got 4.6 Gbps. The
10 Gbps adapter
is 1.4x faster, but for more than 2x the price ($30 vs $80).
I think, if you already
have
a 10 Gbps network, you use RJ45 and not SFP+ connections, and you want a more compact adapter (compared to the bulky, hot Thunderbolt adapters), it's a good deal. But if you
need
that full 10 Gbps or SFP+ support, Thunderbolt adapters are still the best if you have Thunderbolt ports that don't support USB 3.2 Gen 2 2x2.
If you don't need 10 Gbps, though, stick to 2.5 or 5 Gbps adapters—they are still the best value right now.
Thermals and Power Draw
I also checked thermals and power draw—though my tests are not comprehensive. Measuring the absolute power draw is difficult because my USB-C power measurement devices downgrade the connection speed to USB 2, which means I'm not testing at full performance.
At the slower USB 2 speed, the adapter uses about 0.86 Watts of power.
And it doesn't get that hot, which was surprising. All my Aquantia-based 10 gig adapters turn into little ovens. That's why they're so big: the enclosures are giant heatsinks.
But the WisdPi only got up to 42.5°C after running a bidirectional iperf3 test for a few minutes.
That's warm, but not so hot that I'd burn myself touching it like I have with other 10 gig adapters.
Conclusion
If $80 is too rich, this isn't the only option that uses the new chip; AliExpress is
littered with alternatives
. And you can get it on PCI Express cards, which bypasses the USB port requirement on desktop PCs.
In the midst of all the price inflation in personal computing, it's nice to find a new device that's cheaper, faster, and (depending on your USB port) better.
