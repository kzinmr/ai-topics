---
title: "How to install FreeBSD on providers that don't support it with mfsBSD"
url: "https://it-notes.dragas.net/2025/07/02/install_freebsd_providers_mfsbsd/"
fetched_at: 2026-04-29T07:02:10.891462+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# How to install FreeBSD on providers that don't support it with mfsBSD

Source: https://it-notes.dragas.net/2025/07/02/install_freebsd_providers_mfsbsd/

FreeBSD is an extremely powerful operating system. The ability to isolate services in jails and, thanks to ZFS, the simplicity with which you can create snapshots (both local and remote) make it a perfect system for increasing peace of mind, especially when running many workloads.
Many providers, blinded by the success and large numbers achieved by Linux distributions, have decided to no longer support FreeBSD in their installers. While understandable (they might not have staff experienced with systems other than Linux), this can cause problems for those who want to try using something different. And yes,
it makes perfect sense, even just to avoid IT monocultures
, which are extremely harmful even in the medium term.
There's an extremely powerful tool that, in my opinion, deserves much more attention than it gets. The tool is called
mfsBSD
. Using the author's words: "This is a set of scripts that generates a bootable image (and/or ISO file), that creates a working minimal installation of FreeBSD (mfsBSD) or Linux (mfslinux). It is completely loaded into memory."
mfsBSD works intelligently: it can be launched both via UEFI and via "traditional" boot since it has both boot modes enabled. It gets an IP address via DHCP (an operation that works with most providers) and opens an SSH server (with a preset password - so it's advisable to connect immediately and change it, to prevent someone else from doing it for you).
This means that mfsBSD can be used both when you have a console available and, in many cases, without a console, since you'll just need to connect via SSH and start with the traditional installation.
To install FreeBSD using mfsBSD, you just need to follow some very simple steps: all providers, in fact, offer the ability to boot in Linux "rescue mode", generally based on a sufficiently recent version. Set your server (whether physical or VPS, it doesn't matter) in rescue mode and reboot. Once active, connect via SSH (or open a console) to the server in rescue mode.
Now it's sufficient to download the mfsBSD image (for example, from here:
https://mfsbsd.vx.sk/files/images/
- in my case, I usually choose the normal image, which at the time of writing this post is https://mfsbsd.vx.sk/files/images/14/amd64/mfsbsd-14.2-RELEASE-amd64.img). At this point, it needs to be written with
dd
directly to the server's disk (or, if in doubt, disks). For example:
dd if=mfsbsd-14.2-RELEASE-amd64.img of=/dev/sda bs=5M conv=sync
In this case I wrote "sda", but if you had one or more NVMe drives, the correct device would be
/dev/nvme0n1
for the first disk,
/dev/nvme1n1
for the second, etc.
Reboot. If you have a console, you'll see mfsBSD boot up, enable the SSH server, and position itself at the login. Otherwise, ping the server's IP until it starts responding. At that point, it's sufficient to connect via SSH as the root user.
The root password is
mfsroot
As the first thing, change the root password with the
passwd
command
. This is to prevent someone from entering and compromising the machine during the installation time.
Now launch the
bsdinstall
command and proceed with the normal FreeBSD installation (also setting up mirrors, RAID, etc., if desired), keeping in mind that mfsBSD is running in RAM, so you can overwrite the disk it was installed on without problems.
After the reboot, you'll have your FreeBSD system installed and running.
