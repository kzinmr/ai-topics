---
title: "Arch Linux on Surface Book 1"
url: "https://jayd.ml/2025/04/15/arch-linux-on-surface.html"
fetched_at: 2026-04-29T07:02:13.542593+00:00
source: "jayd.ml"
tags: [blog, raw]
---

# Arch Linux on Surface Book 1

Source: https://jayd.ml/2025/04/15/arch-linux-on-surface.html

Recently Microsoft told me that my Surface Book 1 was garbage and I should throw
it in the trash. Even though it is old and only a dual core and only has 8 GB
of RAM, I resent being told what to do.
Anyway, this Windows installation had been around since 2017 and had decayed a
lot as Windows tends to do. Plus, this laptop got me through college, and I’m 
not done with it yet, so time to be an anarchist linux hacker I guess.
Why keep using this thing in 2025?
A beautiful 3:2 3000x2000 HighDPI display. Seriously one of my favorite things
about this laptop
When it was new, it had excellent battery life since it has one in the tablet
as well as the base. Since it is old and degraded now, it is simply acceptable
battery life (about 4-5 hours)
I already own it, and don’t use a laptop much
Defiance disorder, M$SFT can’t tell me what to do!!!!1
Debian
Anyway, to Linux it was. I’ve had Debian on machines before, and tried that out
first. I’ve since learned though that “debian stable” means “you’re going to 
deal with the same bugs for 3 years”. I ended up switching it away because:
I couldn’t get sleep to work right (this ended up not being debian’s fault)
I wanted to encrypt the entire disk, including
/boot
I have a bad case of versionitis and want the latest version of everything
all the time
Arch Linux
I’ve heard it said that Arch linux is for a very particular kind of computer
user. I have discovered that I am, in fact, that exact type of user. If there
are good instructions, like the Arch wiki, I have no problem doing it myself. 
And the best instructions I could find for encrypted
/boot
were the arch wiki.
So, after getting it set up and using it for a while, I think it works well 
enough, espcially with the
linux-surface
filling some gaps.
The Good
Arch installed just fine
Feels much lighter weight and snappier than Windows did
KDE looks fantastic on the high DPI display
Battery life is about the same as Windows.
Touchpad feels great to use, guestures work
Touchscreen works
Was able to have a large swapfile (only 8 GB RAM) and get hibernation to work
The Bad
1. No S0ix states
Apparently the Surface Book 1 series has some ACPI weirdness that makes S0ix 
(“modern standby”)
sleep states not work
.
This means when you shut the lid, the battery will drain at about 5% an hour,
which is a problem for me since the usage pattern for this laptop these days is
“once a week at best but it needs to be charged when I need it”.
The workaround was to enable systemd’s suspend-then-hibernate from KDE’s power
applet. There were some issues with a
linux-surface
driver blocking sleep,
see
my other blog post
.
This has worked well enough, I can confidently shut the lid and open it a week
later and I haven’t lost any work. It is pretty slow to resume from sleep though
2. No Dedicated GPU
The
linux-surface
feature matrix
says the
nvidia GPU in the performance base is supported, but after installing the nvidia
linux drivers nothing shows up.
I didn’t really try too hard to get this working since I never found that GPU
very useful anyway.
3. Janky camera support
You
can
get the cameras to work, but you have to fiddle with linux kernel 
modules and run
a loopback script to enable it
. Not great.
4. No power states
Update 07/25/25:
Apparently I just needed to install the
power-profiles-daemon
.
KDE helpfully suggested I install this, and now I have three different power
states (eco, normal, and performance).
In eco it aggressively downclocks to around 400mhz, normal is around 800mhz
and in performance it keeps it at the max non-boost clock speed (and spins up
the fans a bit)
This laptop under Windows has “power states” that let you choose performance vs
battery saver. These aren’t supported in Linux, more ACPI weirdness I suppose.
Whatever power state it defaults to is fine though, the fans rarely spin up
(much less than they did on Windows)
The Ugly
I made it about a week before completely borking my arch install and needing
the rescue ISO.
There was some bug in the KDE crash reporter that would fill up
/tmp
with
a crash dump. While this was happening, I ran
pacman -Syu
, and something
didn’t handle there being 0 free bytes in
/tmp
well (I think
mkinitcpio
), 
and it wouldn’t boot after.
I converted to BTRFS to use snapshots after this debacle.
Also, I still don’t think I’ve set up locales right somehow.
Conclusion
I like it. I think the KDE  folks have done a great job making a sharp, snappy
looking desktop. I get a little more what all the people on hacker news complain
about when they say the Windows desktop is so consistent.
I love having the latest version of everything on Arch. I’ve got most of the 
software I want to work. Hopefully I’ll never have to reinstall or upgrade the
os on this computer ever again.
