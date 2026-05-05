---
title: "Old Desktop to Linux - Wayland is still not ready"
url: "https://boyter.org/posts/upgrading-my-old-desktop-linux/"
fetched_at: 2026-05-05T07:01:54.229684+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Old Desktop to Linux - Wayland is still not ready

Source: https://boyter.org/posts/upgrading-my-old-desktop-linux/

Back in August 2021 during the covid madness I updated my rather aged desktop to have new CPU, GPU, PSU and fans. The goal being to make it quieter and get more life out of the system. I also kept it running Windows at the time, since I already have a stable Windows 10 install on it. However it is now 2025 and we are getting close to the end of life time for it in October. I never had any major issues with Windows up till 10. However Microsoft’s increasingly hostile approach to the hardware I paid for can no longer be overlooked. Similiar to how I cancelled netflix recently, I am not paying in order to watch ad’s. Coupled with the invasion of privacy of not allowing local accounts it was time to swich back to some flavour of Linux.
I had been preparing for this switch for a few years now, ensuring that any hardware I bought would have drivers, and ensuring things like my mouse and keyboard had dongles to avoid the pain of bluetooth. The only catch was which flavour to install. My only real requirements for it are that I want it to run a fairly recent kernel, and be reasonably stable. I ruled out Arch since I didnt feel like setting everything up from scratch. I also ruled out Ubuntu since I don’t like the direction its going with snap. Mint was my next contender, but I do want something with slightly more frequent updates.
The choice was made to use Fedora. I have never used Fedora itself, as the last system similar I used was Red Hat back in 2001. I have fond memories of having to recompile my own kernal in order to get my wireless 802.11b wireless card working on it, but while at university stuck with Windows XP before moving back to using Ubuntu around 2005 or so.
Installing was fairly simple using Fedora Workstation. Everything worked out of the box, which was not suprising considering how old the machine is, Intel 4790k from 2014, and my attempts to only buy linux compatible hardware. GPU drivers worked flawlessly and I was even able to get Steam running with Proton and have some games work. A big step up from where I last remember Linux being, where the goal was to get tuxracer to render at more than 5 fps.
However its also where problems began. I started getting random crashes. Nothing predictable, but almost always within 4 hours of of a reboot. The crashes were so hard that they locked the system, although if I SSH’ed into the machine I could see through htop that the load average was increasing, without any CPU usage. I put up with this for about a day, with some investigation and eventually noticed in the logs that it looked like Gnome was crashing.
I had always used Gnome, since 2001 (or perhaps earlier) and despite having a fondness for Fluxbox at the time still installed Gnome just to get all the tools it provided. With Fedora having a new flavour however that was KDE based perhaps it was time to try that. So I reinstalled, and was up and running with KDE. Sadly the crashes persisted.
At this point I was beginning to suspect it was something else causing the issue. Looking around suggested that perhaps wayland was the issue. So I logged out and restarted into an X11 session. The same session that I am writing this blog post using.
I had hoped that after 16 years wayland would be working out of the box these days, but it seems to not be the case. While I like the idea of it, I also find it fairly comforting to be running my display through software that is about as old as I am.
Anyway if you do flip over to linux and notice random crashes using an AMD GPU, consider testing an X11 session over Wayland.
Regardless, everything seems stable now and I am loving being back in the linux world. Actually makes me want to upgrade this system, although I suspect I am about to get another few years out of it, especially with how snappy it feels all of a sudden. Its also nice to be running a system that respects my right as the user to control the system the way I want.
