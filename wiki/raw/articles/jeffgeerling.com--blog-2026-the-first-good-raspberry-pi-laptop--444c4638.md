---
title: "The first good Raspberry Pi Laptop"
url: "https://www.jeffgeerling.com/blog/2026/the-first-good-raspberry-pi-laptop/"
fetched_at: 2026-04-29T07:02:14.120426+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# The first good Raspberry Pi Laptop

Source: https://www.jeffgeerling.com/blog/2026/the-first-good-raspberry-pi-laptop/

Ever since the
Raspberry Pi Compute Module 5
was introduced, I wondered why nobody built a decent laptop chassis around it.
You could swap out a low spec CM5 for a higher spec, and get an instant computer upgrade. Or, assuming a CM6 comes out someday in the same form factor, the laptop chassis could get an entirely new life with that upgrade.
Think
Framework Mainboard
, but even easier to swap out!
Well, Argon40 just launched the
ONE UP
(pictured above), a laptop that can be bought one of two ways:
Shell: $400 version (bring your own CM5 and storage)
Core: $550 version (includes 8GB CM5, and NVMe SSD)
They originally launched the laptop via
Kickstarter
, and have been shipping the laptop to backers as of early 2026.
I just received my Argon ONE UP a couple weeks ago, and I bought the Shell version, since I already had a spare CM5 and an NVMe SSD.
And I'm lucky I already had them, because just this week,
Raspberry Pi announced another price increase
in response to component cost inflation.
Despite the Pi not being built for laptop use, the ONE UP is pretty good.
But it's launching at about the worst possible time in Raspberry Pi's history.
As of early 2026, to reproduce my entire setup would cost around $600:
If it were a
killer laptop
, it could be worth it—after all, MacBooks start at $999, and Chromebooks are... well... you can get a Chromebook starting around $200-300 (so half the cost). But running Linux on those is annoying.
Maybe this can win for a cheap Linux laptop?
Well... maybe not, when
the competition
has a faster Intel N150, costs $400, and ships tomorrow.
Or for around the same price as my setup, you could upgrade to a
name-brand Lenovo
with an 8-core AMD CPU.
That doesn't mean this laptop is useless; like other Pi gear, it could serve a niche. But as a general laptop, right now the value is just not there.
Taking all that into account, let's dive in.
Video
This blog post is the companion to this YouTube video. If you don't like watching videos, please scroll right past, and carry on reading!
Hardware
The first thing I did was remove the bottom cover, to see what's under the hood. There's a pretty large and mostly empty mainboard, in contrast to other laptops. That's because the actual computery bits are all crammed onto the Compute Module.
There's a small fan that blows air directly past the CM5 out the rear hinge, and the rest of the space is dominated by a large 55.21 Wh / 4780 mAh battery. The battery is held on with four screws, so should be easy enough to replace.
The CM5 and NVMe storage are accessible just removing a little heatsink plate, and the entire structure is aluminum. Honestly, this laptop feels more premium than the
Framework 13 I tore down
a few months ago.
There are more ports on here than my MacBook Air. On the right side:
Kensington lock
USB 3.0 (Type-A)
USB 2.0 (Type-A)
microSD (only works with Lite Compute Modules, without eMMC)
3.5mm Headphone
And on the left side:
USB-C PD input (45W power adapter recommended)
Full-size HDMI 2.0
USB 3.0 (Type-A)
2x USB-C GPIO (these ports are weird)
A GPIO breakout adapter plugs into the last two USB-C ports on the left side. But the little pamphlet that comes with the laptop says they have PD Power
and
Data. The last port even offers DisplayPort and OTG according to the pamphlet, but Argon40 just clarified in a Kickstarter update that the pamphlet is wrong. These ports
only
support their GPIO breakout, not any of the other modes.
Yay for more abuse of the USB-C port standard 🤦‍♂️
The more annoying thing is I've had to figure out a lot of this through my own testing. The
Argon40 forum
has some hefty requirements for new users before allowing them to post new topics. And even then, there's not yet a category or tag for the ONE UP, so people are forced to post about the laptop in other parts of the forum.
Worse yet, there's no Wiki pages for the ONE UP, and the only official documentation page links to the
same incorrect quick start guide
that's included with the laptop!
So far the best support has come through the ONE UP's
Kickstarter page
; Argon40 is posting updates and infrequently responds to backer comments.
But seriously, why is it these smaller companies are failing at product support. Give me a usable forum! I mean, at least they don't point you at a random Discord :P
I tested all the ports, and was able to extend my monitor using HDMI, but was not able to use a USB-C display on the USB-C port marked on the Quick Start Guide as having DisplayPort out.
I also tested a USB flash drive on all the USB ports, and it worked on all the Type-A ports, but on none of the Type-C ports.
Speakers
There are also two decent-sized speakers on either side of the battery.
Cheaper laptops often skimp on sound. The ONE UP's speakers aren't MacBook-level quality, but they're certainly as good as other mid-tier laptop speakers. I could get over 80 dBa out of them with no distortion, from a foot away.
They lack bass, but the stereo image is decent.
Display
The 14" IPS LCD display is 1920x1200 at 60 hertz. The colors and image are great, though it's a tad bit dim at 250 nits.
Just above the display is an HD webcam, with a tiny privacy shutter.
Keyboard and Trackpad
The keyboard is as nice to type on as my Air. The chassis is rigid and the keys have enough travel for a comfortable typing experience.
The trackpad is good, but not great. The left click area on the bottom left always gives a loud click sound... but sometimes that doesn't register as an actual click. The right click area is a tiny 1x1 centimeter spot on the bottom right.
Tap to click works reliably, tracking and scrolling is good, and a two finger tap to right click works well too.
Bottom line: If you like to
push
to click, this isn't the trackpad for you. Otherwise, it's fine.
The power button lights up when it's on, and you can hold it down for 10 seconds to force a shutdown.
Setup Notes
In the 'Shell' version I bought, it comes with a tiny screwdriver and a little baggie with 8 small screws. I used four of them to secure the CM5 in place, but I noticed there was no thermal pad.
I had to fish a 1mm pad out of my 'small bag of unused thermal pads' to place between the CM5 and the bottom heatsink cover. I'm guessing one was supposed to be included. Not sure what happened there.
With that in place, the CM5 idled around 35°C, and maxed out below 50°C when running
stress-ng
for 10+ minutes. The thermals are well-controlled and the fan is pretty quiet when it is spinning at all.
The software experience
Raspberry Pis, and Raspberry Pi OS, are
not
built for laptop use. Basic things like trackpad settings, battery configuration, and even
sleep
aren't supported. Other Linux distros may fare better, but can't solve the problem of the Pi not supporting any sleep modes.
Argon40 has a Python script you can run that displays battery life in an icon on the desktop, but that's mostly a hack. The community's
working on a proper battery driver for Linux
, but really Argon40 should've had that going day one.
Their script also reacts to closing the lid, and turns off the screen immediately—it can even be configured to
shut down the Pi
after 5 minutes (can't see that going wrong, ever...).
But in general, the Pi will stay running at around 3.3W even if the screen is off, from the lid being closed or if you turn on 'Screen Blanking'. With the screen
on
, the laptop idles at 8W. And with the CPU going full-tilt, it uses 12.5W.
Other power stats: (I used a
45W Anker Nano II GaN adapter
, measured by
Thirdreality Smart Outlet
):
Battery charged, computer off: 0.4W
Battery charged, computer idle: 7.9W
Battery charged, computer maxed out: 12.5W
Battery charged, computer idle, screen blank: 3.3W
Battery discharged, charging max, computer off: 33.5W
Battery discharged, charging max, computer idle: 40.6W
Battery discharged, charging max, computer maxed out: 44.9W
Based on the battery's 55 watt-hour capacity, if you turn off the display and quickly stash the laptop, you get a maximum of 17 hours of standby power. Good enough for one day, but it's better to shut it down when you're not using it.
To see how long the battery goes while using it, I played a 1080p copy of
Big Buck Bunny
in VLC on a loop. I had the screen on full brightness, and speakers at about 25%.
I wasn't expecting much, and the same test on a modern MacBook will go for a lot longer, but coming in at 7 hours and 34 minutes was a decent result. That's right in line with their 6-8 hour battery life claim.
Even without sleep, the CM5 isn't the
worst
idea in a laptop. It's better than the RISC-V ESWIN chip I tested in the DC ROMA II that burned 25W at idle!
Real-world use
To put it through its paces in the real world, I also took a
prototype
model of this laptop that Argon40 sent to me
last year
to Open Sauce, in California.
I published a separate video featuring the laptop's use on that trip:
Hacking Meshtastic with a Raspberry Pi and GNU Radio
.
I used the laptop with my HackRF SDR to scan radio frequencies. I was trying to decode Meshtastic messages using GNURadio, and I was also monitoring airplane traffic on the ONE UP.
It worked great for all that, though the CM5 is a little limited for some things compared to a even a used laptop. Like you could
buy an old M1 MacBook Air for $400 bucks
, and that thing would probably beat this in every aspect, and still give you that quiet, cool Arm-powered laptop experience.
Conclusion
If the price is right, this laptop could be useful. I already
had
a spare CM5, so it's nice to use it for quick project testing around the studio.
Another use I have is for a small class I teach. I've been using Chromebooks to program microcontrollers to teach electronics, but dealing with Chrome OS is rough.
It's much nicer to run Linux and something like Thonny directly, without playing inside Google's walled garden. And this does that. The trouble is, a cheap used Windows laptop gets that done too, and usually for a lot less.
The ONE UP is a good laptop. Not perfect, but serviceable. But because of where the world of computing is right now, with RAM prices where they are... it's just not a good deal.
I think if we ever end up in a sane world again, that'll change. Especially if there's ever a newer, faster CM6. The ONE UP is like a different take on the Framework, but it achieves the same right to repair goal: the laptop doesn't have to go in the dumpster every few years if you wanna upgrade.
But the value is just not there right now, so I can't really recommend the ONE UP.
For all my test data, and any future updates, check out the
Argon ONE UP CM5 Laptop
issue on my Pi PCIe project website.
