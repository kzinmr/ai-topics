---
title: "Media Server Journey"
url: "https://laplab.me/posts/media-server-journey/"
fetched_at: 2026-05-05T07:01:23.684163+00:00
source: "Nikita Lapkov (laplab)"
tags: [blog, raw]
---

# Media Server Journey

Source: https://laplab.me/posts/media-server-journey/

I manage my legally obtained content using a media server. Over the years, both hardware and software on the server went through a bunch of transformations which I find interesting.
In order to not look at ads on my Samsung TV, I view all of my content through NVIDIA Shield. It is connected to the TV through HDMI and has a working implementation of HDMI eARC that my TV responds to. Because of that, whether NVIDIA Shield turns on or turns off, TV follows suit, which is very convenient.
My initial setup involved simply connecting HDD to NVIDIA Shield and using Kodi app to view media from it. This served me well for half a year, but constantly unplugging the HDD to add more media grew tedious quickly.
I tried connecting to Samba server on NVIDIA Shield, but for some reason that didn’t work with my Mac. At the very end of transferring a file from the Mac to the Shield, I would get an non-descriptive error. NVIDIA Shield is quite an underpowered device and I didn’t want to add more load to it anyway. So I decided to look into NAS setups.
My home router is FRITZ!Box and it has a NAS built-in. This could work, but I never tried it. Somehow I doubt that a NAS implementation as an added feature in a consumer router is any good, but maybe I’m wrong.
Update:
Turns out, a friend of a friend uses this feature and claims it works very well. They didn’t have any issues using it with Mac too.
I had previous experience of running “always-on” software on Raspberry Pi, which is why I immediately decided not to do it again. Instead, I opted to buy Intel NUC. It provided a no frills familiar x86 Ubuntu environment which is all I ever needed. I re-used external HDD from my Shield setup and connected it to Intel NUC through USB.
Unsurprisingly, USB turned out to be a terrible medium for connecting drives in the long term. It is very easy to accidentally disconnect the drive by slightly changing the angle of the cable. However, I found a quiet place where the server had almost no vibrations and this setup worked well for 1.5 years. At some point, I added a second HDD, also connected through USB, to extend storage. It worked fine. However, I still needed to restart the server and adjust the cables occasionally. I was also running out of USB 3.0 ports.
Since I’m a software engineer, I decided to solve the problem by introducing 10 more. I briefly considered buying or building a NAS with internal HDDs. However, at some point I had a brainwave — I already own a very capable and underused “server” — my gaming PC.
My PC runs Windows, so I needed some way to run Ubuntu. Using WSL felt like cheating, so I decided to run a proper Virtual Machine using Hyper-V. It sucked. Hyper-V itself is surprisingly good, but the networking situation is abysmal. If (and that’s a big “if”) I understand this correctly, for both the VM and the host machine to use the same network card, they need to share a virtual switch. My router didn’t like this at all and constantly assigned new IPs both to the VM and the host machine. This is very annoying in streaming because the VM’s IP can change in the middle of the film, which caused Plex to disconnect. I tried all angles I could think of and I don’t know how to solve this. My router relies on MAC addresses for static IP assignments and virtual switch messes up VM’s and host’s MAC addresses,
I think
. In any case, this was a no-go.
At some point during experiments with Hyper-V, my external HDDs died. ZFS scrubbing would just hang and the HDDs would stop spinning. I’m not sure what exactly happened, but I wanted to switch to internal HDD anyway, so it was fitting. In total, HDDs served for roughly two years, which funnily enough is exactly their guarantee period. I think they performed well, given the fact that I used them quite extensively.
With Hyper-V networking problem unresolved, I switched to the boring solution of just running WSL2. Turns out, it has a bunch of very annoying quirks like not supporting ZFS or iptables. I need ZFS because I like ZFS. I need iptables because I wasn’t able to run Docker without it. So for the first time in my life, I compiled a custom kernel. All the hard work was already done by
a friendly stranger on the internet
, I just enabled a bunch of additional compile flags to have iptables. With the custom kernel, WSL2 runs pretty well. The networking part does, at least. You can configure WSL2 to use the same IP as the host machine and it doesn’t make my router’s brain hurt. No more Plex stream pauses because of that.
Unfortunately, Plex started to suddenly die because WSL2 shuts down itself if it’s not “used”. The criteria for “used” seems to be “has an open terminal to WSL on the host machine”. I’m sure there is a more elegant way to keep WSL2 running in the background, but this works for now.
You also need to make sure the internal hard drive is mounted to WSL every time before the startup. This is easy to do with a PowerShell script, but still annoying.
A nice bonus of using WSL2 is that Linux and Windows can share the GPU. This is very handy for hardware transcoding in Plex and is pretty easy to configure. Having “Plex Media Server” in the list of GPU processes from “nvidia-smi” executed in Windows feelt like magic.
Switching to the gaming PC meant that I need to keep it turned on 24/7. The PC definitely draws more power than Intel NUC, but I was curious how much more. Unfortunately, the idea to measure this came to me only after I fully migrated to the PC, so I don’t have any measurements for Intel NUC. Here are some for the PC, though:
Display
WSL*
Activity
Power usage
Cost per hour
Off
Off
Idle
60W
1 pence
On
Off
Idle
60W**
1 pence
Off
On
Idle
63-65W
2 pence
Off
On
Watching Plex without GPU transcoding
64-65W
2 pence
Off
On
Watching Plex with GPU transcoding
140W
3 pence
*
WSL is running with all containers I use for my media server.
**
For some reason, I observed spikes to 100W every two seconds.
Assuming that the server is running 24/7 and I watch content probably under 2 hours per day (let’s say everything is GPU transcoded), the total electricity cost is about £15.5 per month. Still cheaper than Netflix Premium!
In the end, would I recommend running a media server on a VM on Windows? Lol. Does it work relatively well in my conditions and brings me joy? It does, yes.
