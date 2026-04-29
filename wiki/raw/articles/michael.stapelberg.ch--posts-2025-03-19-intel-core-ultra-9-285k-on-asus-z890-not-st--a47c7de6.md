---
title: "Intel 9 285K on ASUS Z890: not stable! (2025)"
url: "https://michael.stapelberg.ch/posts/2025-03-19-intel-core-ultra-9-285k-on-asus-z890-not-stable/"
fetched_at: 2026-04-29T07:01:14.042347+00:00
source: "michael.stapelberg.ch"
tags: [blog, raw]
---

# Intel 9 285K on ASUS Z890: not stable! (2025)

Source: https://michael.stapelberg.ch/posts/2025-03-19-intel-core-ultra-9-285k-on-asus-z890-not-stable/

Table of contents
Update (2025-05-15):
Turns out the CPU was faulty! See
My 2025 high-end
Linux PC
for a new article on
this build, now with a working CPU.
Update (2025-09-07):
The replacement CPU also died and I have given up on
Intel. See
Bye Intel, hi AMD!
for
more details on the AMD 9950X3D.
In January I ordered the components for a new PC and expected that I would
publish a successor to my
2022 high-end Linux PC
🐧
article. Instead, I am now sitting on
a PC which regularly encounters crashes of the worst-to-debug kind, so I am
publishing this article as a warning for others in case you wanted to buy the
same hardware.
Components
Which components did I pick for this build? Here’s the full list:
Total: ≈1800 CHF, excluding the Graphics Card I re-used from a previous build.
…and the next couple of sections go into detail on how I selected these components.
Case
I have been a fan of Fractal cases for a couple of generations. In particular, I
realized that the “Compact” series offers plenty of space even for large
graphics cards and CPU coolers, so that’s now my go-to case: the Fractal Define
7 Compact (Black Solid).
I really like building components into the case and working with the case. There
are no sharp edges, the mechanisms are a pleasure to use and the
cable-management is well thought-out.
The only thing that wasn’t top-notch is that Fractal ships the case screws in
sealed plastic packages that you need to cut open. I would have wished for a
re-sealable plastic baggie so that one can keep the unused screws instead of
losing them.
Power Supply
I wanted to keep my options open regarding upgrading to an nVidia 50xx series
graphics card at a later point. Those models have a TGP (“Total Graphics Power”)
of 575 watts, so I needed a power supply that delivers enough power for the
whole system even at peak power usage in all dimensions.
I ended up selecting the Corsair RM850x, which
reviews favoribly (“leader in
the 850W gold
category”)
and was available at my electronics store of choice.
This was a good choice: the PSU indeed runs quiet, and I really like the power
cables (e.g. the GPU cable) that they include: they are very flexible, which
makes them easy to cable-manage.
SSD disk
I have been avoiding PCIe 5 SSDs so far because they consume a lot more power
compared to PCIe 4 SSDs. While bulk streaming data transfer rates are higher on
PCIe 5 SSDs, random transfers are not significantly faster. Most of my compute
workload are random transfers, not large bulk transfers.
The power draw situation with PCIe 5 SSDs seems to be getting better lately,
with the Phison E31T being the first controller that implements power saving. A
disk that uses the E31T controller is the Corsair Force Series MP700
Elite. Unfortunately, said disk was unavailable when I ordered.
Instead, I picked the Samsung 990 Pro with 4 TB. I made good experiences with
the Samsung Pro series over the years (never had one die or degrade
performance), and my previous 2 TB disk is starting to fill up, so the extra
storage space is appreciated.
Mainboard
One annoying realization is that most mainboard vendors seem to have moved to
2.5 GbE (= 2.5 Gbit/s ethernet) onboard network cards. I would have been
perfectly happy to play it safe and buy another Intel I225 1 GbE network card,
as long as it
just works
with Linux.
In the 2.5 GbE space, the main players seem to be Realtek and Intel. Most
mainboard vendors opted for Realtek as far as I could see.
Linux includes the
r8169
driver for Realtek network cards, but you need a
recent-enough Linux version (6.13+) that includes commit “
r8169: add support
for
RTL8125D
”,
accompanied by a recent-enough linux-firmware package. Even then, there is some
concern around stability and ASPM support. See for example
this ServerFault
post
by someone working on the
r8169
driver.
Despite the Intel 1 GbE options being well-supported at this point, Intel’s 2.5
GbE options might not fare any better than the Realtek ones: I found
reports of
instability with Intel’s 2.5 GbE network
cards
.
Aside from the network cards, I decided to stick to the ASUS prime series of
mainboards, as I made good experiences with those in my past few builds. Here
are a couple of thoughts on the ASUS PRIME Z890-P mainboard I went with:
I like the quick-release PCIe mechanism: ASUS understood that people had
trouble unlocking large graphics cards from their PCIe slot, so they added a
lever-like mechanism that is easily reachable. In my couple of usages, this
worked pretty well!
I wrote about
slow boot times with my 2022 PC
build
that were caused by
time-consuming memory training. On this ASUS board, I noticed that they blink
the Power LED to signal that memory training is in progress. Very nice! It
hadn’t occurred to me previously that the various phases of the boot could be
signaled by different Power LED blinking patterns :)
The downside of this feature is: While the machine is in suspend-to-RAM, the
Power LED also blinks! This is annoying, so I might just disconnect the
Power LED entirely.
The UEFI firmware includes what they call a Q-Dashboard: An overview of what
is installed/connected in which slot. Quite nice:
CPU fan
I am a long-time fan of Noctua’s products: This company makes silent fans with
great cooling capacity that work reliably! For many years, I have swapped out
every of my PC’s fans with Noctua fans, and it was always an upgrade. Highly
recommended.
Hence, it is no question that I picked the latest and greatest Noctua CPU cooler
for this build: the Noctua NH-D15 G2. There are a couple of things to pay
attention to with this cooler:
I decided to configure it with one fan instead of two fans: Using only one fan
will be the quietest setup, yet still have plenty of cooling capacity for this
setup.
There are 3 different versions that differ in how their base plate is
shaped. Noctua recommends: “For LGA1851, we generally recommend the regular
standard version with medium base convexity”
(
https://noctua.at/en/intel-lga1851-all-you-need-to-know
)
The height of this cooler is 168 mm. This fits well into the Fractal Define 7
Compact Black.
CPU
Probably the point that raises most questions about this build is why I selected
an Intel CPU over an AMD CPU. The primary reason is that Intel CPUs are so much
better at power saving!
Let me explain: Most benchmarks online are for gamers and hence measure a usage
curve that goes “start game, run PC at 100% resources for hours”. Of course,
when you never let the machine idle, you would care about
power efficiency
:
how much power do you need to use to achive the desired result?
My use-case is software development, not gaming. My usage curve oscillates
between “barely any usage because Michael is reading text” to “complete this
compilation as quickly as possible with all the power available”. For me, I need
both absolute power consumption at idle, and absolute performance to be
best-of-class.
AMD’s CPUs offer great performance (the recently released
Ryzen 9 9950X3D is
even faster
than the
Intel 9 285K), and have great
power efficiency
, but poor
power consumption
at idle: With ≈35W of idle power draw, Zen 5 CPUs consume ≈3x as much power as
Intel CPUs!
Intel’s CPUs offer great performance (like AMD), but excellent power consumption
at idle.
Therefore, I can’t in good conscience buy an AMD CPU, but if you want a fast
gaming-only PC or run an always-loaded HPC cluster with those CPUs, definitely
go ahead :)
Graphics card
I don’t necessarily recommend any particular nVidia graphics card, but I have
had to stick to nVidia cards because they are the only option that work with my
picky
Dell UP3218K monitor
.
From time to time, I try out different graphics cards. Recently, I got myself an
AMD Radeon RX 9070 because I read that it works well with open source drivers.
While the Radeon RX 9070 works with my monitor (great!), it seems to consume 45W
in idle, which is much higher than my nVidia cards, which idle at ≈ 20W. This is
unacceptable to me: Aside from high power costs and wasting precious resources,
the high power draw also means that my room will be hotter in summer and the
fans need to spin faster and therefore louder.
Maybe I’ll write a separate article about the Radeon RX 9070.
Installation
UEFI setup
On the internet, I read that there was some issue related to the Power Limits
that mainboards come with by default. Therefore, I did a
UEFI firmware
update
first thing after getting the mainboard. I upgraded to version 1404 (2025/01/10)
using the provided ZIP file (
PRIME-Z890-P-ASUS-1404.zip
) on an MS-DOS
FAT-formatted USB stick with the EZ Flash tool in the UEFI firmware
interface. Tip: do not extract the ZIP file, otherwise the EZ Flash tool cannot
update the Intel ME firmware. Just put the ZIP file onto the USB disk as-is.
I verified that with this UEFI version, the
Power Limit 1 (PL1)
is 250W, and
ICCMAX=347A
, which are exactly the values that Intel recommends. Great!
I also enabled XMP and verified that memtest86 reported no errors.
Software setup: early adopter pains
To copy over the data from the old disk to the new disk, I wanted to boot a live
linux distribution (specifically,
grml.org
) and follow my
usual procedure: boot with the old disk and the new (empty) disk, then use
dd
to copy the data. It’s nice and simple, hard to screw up.
Unfortunately, while grml 2024.12 technically does boot up, there are two big
problems:
There is no network connectivity because the kernel and linux-firmware
versions are too old.
I could not get Xorg to work at all. Not with the Intel integrated GPU, nor
with the nVidia dedicated GPU. Not with
nomodeset
or any of the other
options in the grml menu. This wasn’t merely a convenience problem: I needed
to use
gparted
(the graphical version) for its partition moving/resizing
support.
Ultimately, it was easier to upgrade my old PC to Linux 6.13 and linux-firmware
20250109, then put in the new disk and copy over the installation.
Stability issues
At this point (early February), I switched to this new machine as my main PC.
Unfortunately, I could never get it to run stable! This journal shows you some
of the issues I faced and what I tried to troubleshoot them.
Xorg dying after resume-from-suspend
One of the first issues I encountered with this system was that after resuming
from suspend-to-RAM, I was greeted with a login window instead of my X11
session. The logs say:
(EE) NVIDIA(GPU-0): Failed to acquire modesetting permission.
(EE) Fatal server error:
(EE) EnterVT failed for screen 0
(EE) 
(EE) 
(EE) Please also check the log file at "/var/log/Xorg.0.log" for additional information.
(EE) 
(WW) NVIDIA(0): Failed to set the display configuration
(WW) NVIDIA(0):  - Setting a mode on head 0 failed: Insufficient permissions
(WW) NVIDIA(0):  - Setting a mode on head 1 failed: Insufficient permissions
(WW) NVIDIA(0):  - Setting a mode on head 2 failed: Insufficient permissions
(WW) NVIDIA(0):  - Setting a mode on head 3 failed: Insufficient permissions
(EE) Server terminated with error (1). Closing log file.
I couldn’t find any good tips online for this error message, so I figured I’d
wait and see how frequently this happens before investigating further.
Feb 18: xHCI host controller dying
On Feb 18th, after resume-from-suspend, none of my USB peripherals would work
anymore! This affected
all USB ports
of the machine and could not be fixed,
not even by a reboot, until I fully killed power to the machine! In the kernel
log, I saw the following messages:
xhci_hcd 0000:80:14.0: xHCI host not responding to stop endpoint command
xhci_hcd 0000:80:14.0: xHCI host controller not responding, assume dead
xhci_hcd 0000:80:14.0: HC died; cleaning up
Feb 24: xHCI host controller dying
The HC dying issue happened again when I was writing an SD card in my USB card
reader:
xhci_hcd 0000:80:14.0: HC died; cleaning up
Feb 24: → UEFI update, disable XMPP
To try and fix the host controller dying issue, I updated the UEFI firmware to
version
1601
and disabled the XMPP RAM profile.
Feb 26: → switch back from GeForce 4070 Ti to 3060 Ti
To rule out any GPU-specific issues, I decided to switch back from the Inno3D
GeForce RTX4070 Ti to my older MSI GeForce RTX 3060 Ti.
Feb 28: PC dying on suspend-to-RAM
On Feb 28th, my PC did not resume from suspend-to-RAM. It would not even react
to a ping, I had to hard-reset the machine. When checking the syslog afterwards,
there are no entries.
I checked my power monitoring and saw that the machine consumed 50W (well above
idle power, and far above suspend-to-RAM power) throughout the entire
night. Hence, I suspect that the suspend-to-RAM did not work correctly and the
machine never actually suspended.
Mar 4th: PC dying when running django tests
On March 4th, I was running the test suite for a medium-sized Django project (=
100% CPU usage) when I encountered a really hard crash: The machine stopped
working entirely, meaning all peripherals like keyboard and mouse stopped
responding, and the machine even did not respond to a network ping anymore.
At this point, I had enough and switched back to my 2022 PC.
Conclusion
What use is a computer that doesn’t work? My hierarchy of needs contains
stability as the foundation, then speed and convenience. This machine exhausted
my tolerance for frustration with its frequent crashes.
Manawyrm
actually warned me about the ASUS board
:
ASUS boards are a typical gamble as always – they fired their firmware
engineers about 10 years ago, so you might get a nightmare of ACPI
troubleshooting hell now (or it’ll just work). ASRock is worth a look as a
replacement if that happens. Electronics are usually solid, though…
I didn’t expect that this PC would crash so hard, though. Like, if it couldn’t
suspend/resume that would be one thing (a dealbreaker, but somewhat expected and
understandable, probably fixable), but a machine that runs into a hard-lockup
when compiling/testing software? No thanks.
I will buy a different mainboard to see if that helps, likely the ASRock Z890
Pro-A. If you have any recommendations for a Z890 mainboard that actually works
reliably, please let me know!
Update 2025-04-17:
I have received the ASRock Z890 Pro-A, but the machine
shows exactly the same symptoms! I also swapped the power supply, which also did
not help. Running Prime95 crashed almost immediately. At this point, I have to
assume the CPU itself is defective and have started an RMA. I will post another
update once (if?) I get a replaced CPU.
Update 2025-05-11:
The CPU was faulty indeed! See
My 2025 high-end Linux
PC
for a new article on this
build, now with a working CPU.
Did you like this
    post?
Subscribe to this
      blog’s RSS feed
to not miss any new posts!
I run a blog since 2005, spreading knowledge and experience for over 20 years! :)
If you want to support my work, you
    can
buy me a coffee
.
Thank you for your support! ❤️
