---
title: "Building a mini Homelab that fits in my carry-on"
url: "https://www.jeffgeerling.com/blog/2026/mini-homelab-network-fits-in-carry-on/"
fetched_at: 2026-08-29T10:01:01.542984+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Building a mini Homelab that fits in my carry-on

Source: https://www.jeffgeerling.com/blog/2026/mini-homelab-network-fits-in-carry-on/

I'm traveling to Chicago for
VCF Midwest
next month. I'll be demoing NTP time history on vintage Macs, with my own GPS-derived NTP service hosted on an Xserve G5, synced via NTP or a strange
AppleTalk timing extension from the 1990s
.
So I built a little 'portable homelab' (pictured above) that supports 1-10 Gbps networking, can run off a small battery for at least an hour, switches between multiple WANs (so I can get my own 5G Internet connection, in case I need it), and gives me 12 wired Ethernet connections.
Is it overkill for this particular scenario?
Absolutely
. Would it look different if Micro Center hadn't sponsored the build as part of their
Columbus OH grand re-opening event
?
You bet
.
That said, it's not far off some of the other networking mini-rack builds I've seen in the
Project MINI RACK Build Showcase
. And I'm happy to have more flexibility when I'm on the road trying to keep
other
weird stuff (like vintage computers) running. It's better to go overkill on the network stack since I don't want to debug
that
alongside the Macs.
Ubiquiti
This is my first experience with UniFi. I've run routers on bare Debian Linux installs, consumer routers with OpenWRT/AsusWRT (my home router is still running that!), and my studio router is currently a mini fanless PC running OPNsense.
I figured it was time to see if the UniFi kool-aid is as good as all the influencers say it is.
First impressions? It's a nice walled garden.
There are plenty of pitfalls to the UniFi's proprietary ecosystem, but if you want to play in their sandbox, it's easy to pick up.
The things I like after messing with this particular Ubiquiti setup:
Everything is local-first, and doesn't need any account tie-in
Optional cloud integration adds on functionality like remote management and easier site-to-site VPN setup
There are no licensing fees for core functionality
Most of the hardware is plug-and-play, and easy to manage in one web UI
There are two sides to every coin, and the big sore point I have is the lack of control over the hardware I bought. I don't see any way to unlock the bootloader, so even though the Gateway is running an Arm SoC, there's no way to load my own OS on it.
Not that I'd want to,
today
... but in 10, 20, or however many years, when Ubiquiti drops support for the Gateway I bought, it looks like it'll go straight to e-waste.
But my main goal was to test if I set up everything from scratch without connecting the Cloud Gateway to the Internet, and never connect any sort of Ubiquiti account to the hardware at all. And I could!
The Build
For a detailed look at this build (and more reasoning behind the components), watch this video:
But here are all the components of the build (I've linked to Micro Center since they were all in stock, but you could purchase direct from Ubiquiti if you're not near a Micro Center):
I used some extra patch cables I had laying around for the Ethernet connections, but did add on an extra DAC cable since the Ubiquiti DACs are either too short or much too long for this particular setup. Here's the DAC I'm using, and it's all getting mounted inside a RackMate TT:
Ubiquiti doesn't make any 10" / mini rack mounting hardware, so most people resort to 3D printing as an upgrade over placing components on rack shelves. It's a hard requirement for my setup, because portability means rigid mounts for everything. I don't want a switch sliding out while I'm lugging the mini rack!
To make the prints as durable and sag-resistant as possible—and also self-extinguishing for a little extra safety—I tried printing them out of
Prusament PETG V0
... that turned out okay with a lot of filament drying and tuning for two of the mounts... but I had failure after failure printing the switch enclosure:
V0 is notoriously stringy, and no matter how I tuned things, it would glob up on the nozzle and eventually start touching the printed part. As it got taller and on one side, only narrowly supported, the glob would knock off part of the print... and then spaghetti was the result. I think I would design this print to have a little more cross-bracing on the long sides, as even my Bambu P1S had trouble with regular ol' PLA on this print!
Anyway, here are links to all the other 3D printed rackmounts:
The Ubiquiti 210W power supply is rather large, and I couldn't find a way to origami it inside the 3U RackMate TT, so I designed a blanking panel that hard-mounts it on the rear, using the wall mount bracket that comes with the power supply.
A mini network rack
With all the 3D prints sorted, everything is hard-mounted and ready for travel. I cut a few blocks of foam to support everything inside during travel, and as long as I unplug the cables and remove the top handles, it fits nicely in my standard carry-on luggage bag:
I brought the rack with me to and from Columbus, OH, and used it along with the 5G Backup stick in lieu of hotel WiFi.
And after spending
far too long debugging why I only got 4G LTE speeds with the U5G-Backup on my AT&T SIM
, I realized the hotel had a wired Ethernet jack with 500 Mbps symmetric bandwidth available!
The hotel's WiFi would only give me 30-40 Mbps, but the wired connection seemed to give me the full connection. So I plugged that into WAN1 on the back of the Cloud Gateway Fiber, and switched to that for primary Internet.
The flexibility of the little setup was working exactly as intended, but I still wanted to see how
true
5G connectivity would perform.
So I tested the
UniFi 5G Max
, which is a more full-featured 5G modem (with dual-SIM, better antennas, a touchscreen status display, etc.), and was getting speeds in excess of 500 Mbps down
inside
the Columbus, OH Micro Center:
When I got back to St. Louis, I did a little more digging on the UniFi 5G modems. Apparently they only work with UniFi's networking, you can't plug one into a generic router and use it as a separate WAN.
That was a bit disappointing, especially for the 5G Max which costs over $400. Since I'd like a redundant 5G connection at the studio (where I run OPNsense, not Ubiquiti), I'm now looking at a
Pepwave 5G Adapter
, since it
looks
like it works with anything.
Conclusion
Before getting into this build, I knew the meme of people buying one UniFi switch or gateway since it meets their needs... then a few years later their entire homelab is laden in
hues of UniFi grey and white
.
I don't blame anyone for going that way; Ubiquiti has a complete ecosystem at this point with anything from physical security, environment monitoring, routing, data storage, etc., and all the equipment I've tried is at least competent.
Personally, I'm not migrating from OPNsense and my hodge-podge studio network. But I will get some use out of the mobile carry-on-sized UniFi mini rack.
Right now it's running on my workbench next to an old Xserve G5 and a TrueTime XL GPS time server, which I'm prepping for VCF Midwest!
