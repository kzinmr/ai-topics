---
title: "OpenNMC is an open replacement for expensive APC management cards"
url: "https://www.jeffgeerling.com/blog/2026/opennmc-apc-ups-replacement-card/"
fetched_at: 2026-09-09T10:00:59.986006+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# OpenNMC is an open replacement for expensive APC management cards

Source: https://www.jeffgeerling.com/blog/2026/opennmc-apc-ups-replacement-card/

UPSes are typically the most boring part of your homelab, but they're important. One of their main jobs is to give servers time to shut down safely if the power goes out. Another job is to condition your power so your servers can run smoothly.
To do both of those things
well
, you need a smart interface. And at least with APC, there are tons of older UPSes that use Network Management Cards. The one pictured below is the NMC 2, and I pulled out of my old APC Smart-UPS 2200 XL (pictured above).
It was
discontinued in 2022
, and if I want support, APC wants to sell me their upgraded
NMC
3
, which costs almost $500!
The most annoying part of this is it's all proprietary: the hardware
and
the software. It does have a protocol you can integrate with almost anything, but the firmware on these cards is locked down. And since I've started using
NUT
, or Network UPS Tools, I'd have to use another computer to monitor the UPS anyway.
But not anymore. I'm testing the OpenNMC from
NetCube Systems Austria
. Its firmware is completely open source, meaning you have full ownership of the software that runs on it. It has a built-in NUT server, it's hot-pluggable just like APC's cards, and it even has Wi-Fi if you need that!
The
OpenNMC firmware repo
is already up on GitLab, and the hardware schematics will be released, but I'm not sure under what license. Their GitLab reads:
The schematic, layout, and front panel files are planned to be published once they are cleaned up and tested, with the goal of releasing them as open-source hardware.
I made a quick video about the card and published it on Level 2 Jeff:
And I marked the video 'sponsored' because the prototype I'm testing was sent to me by NetCube Systems Austria. I didn't pay for it, though I had already signed up for the Crowd Supply back when I
spotted the project on Reddit
.
OpenNMC Install
Swapping over to the OpenNMC was easy. With the UPS running, I pulled out the APC NMC 2, and plugged in the OpenNMC. Both are hot-pluggable.
I plugged mine into Ethernet, but it also has Wi-Fi and Bluetooth built-in, if you can't get a network cable to the back of your UPS for some reason.
If I had one complaint about the hardware, I think the LEDs are a little bright. If that bothers you, you probably already have a set of
LightDims
on hand...
For first-time setup, you have to plug into the USB-C serial port on the back, and configure an admin password. After that, you can manage everything through the Web UI.
It's a UPS, so it's not
that
complicated, but you can access all the important stats on the Overview page:
It has a row of buttons to trigger different test modes, run calibration after replacing batteries, or manage the load on the UPS:
And you can allow full management via the built-in NUT server, as well. I tested that with my pre-production firmware and there was one bug preventing some client software from working, but that should be fixed by the time
the Crowd Supply campaign
is live.
I don't know the final expected price (I'll update this post when the campaign is live), but even if it cost exactly the same as APC's own card, that'd be worth it, because you get built-in NUT
and
open source firmware.
