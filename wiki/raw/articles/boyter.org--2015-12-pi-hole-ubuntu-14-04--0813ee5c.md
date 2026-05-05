---
title: "Pi-Hole for Ubuntu 14.04"
url: "https://boyter.org/2015/12/pi-hole-ubuntu-14-04/"
fetched_at: 2026-05-05T07:02:01.385722+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Pi-Hole for Ubuntu 14.04

Source: https://boyter.org/2015/12/pi-hole-ubuntu-14-04/

Pi-Hole for Ubuntu 14.04
2015/12/26
(305 words)
Because of the fact that I personally work for an ad supported company and that searchcode.com is currently supported via third party advertising I tend to keep an eye on the state of ad blockers on the web.
Most people probably know about adblockplus and other browser extensions however there are other ways to block ad’s on ones network. One that I had previously read about was setting up your own Bind9 server on a server and adding custom rules to block them at a DNS level. Other the last week I had been playing around with this but since I am not a bind expert I was unable to get it working in a satisfactory way.
However the following article about
blocking all ads using a Raspberry Pi
appeared on my radar. I don’t have a Raspberry Pi, but I did have an old netbook (Asus Eee 1000HA) lying around that I was trying to find some use for. I had previously set it up with Ubuntu 14.04 and had it running under the house running OwnCloud as a test. I thought it might be a good candidate for this sort of thing.
The install was pretty easy and as simple as following the guide on
http://pi-hole.net/
It says that you need to be using Raspbian but works perfectly for me. Thankfully I have a reasonably good router (
D7000 which I can highly recommend
) and once the setup was done I pointed its DNS at the new server and sat back for things to start working. It did. Flawlessly.
I think the advertising industry is in for a rude shock. When these devices are as cheap as this and as simple to install its only a matter of time before they become a built in to the router itself or a plug and play.
