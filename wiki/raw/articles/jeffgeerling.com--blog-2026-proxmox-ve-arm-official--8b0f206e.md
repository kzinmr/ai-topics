---
title: "Proxmox officially supports Arm, with some caveats"
url: "https://www.jeffgeerling.com/blog/2026/proxmox-ve-arm-official/"
fetched_at: 2026-08-06T10:18:24.041081+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Proxmox officially supports Arm, with some caveats

Source: https://www.jeffgeerling.com/blog/2026/proxmox-ve-arm-official/

Proxmox today announced their
Proxmox Virtual Environment is now available for 64-bit ARM
.
I tested it on my
Ampere Altra Dev Platform
—the same machine on which I've
booted Windows on Arm
the first time, messed with multiple GPUs, and most recently
tested Houdini's native arm64 support
.
Install was easy, as the Ampere Altra uses UEFI / ACPI for its hardware, meaning Proxmox didn't have to tailor its ISO to specific platforms, like you have to do with Raspberry Pis and most SBCs using a Device Tree setup.
I just went into the BIOS, selected my USB stick with the
official Proxmox VE 9.2 for ARM64 ISO
flashed to it, and ran the graphical installer.
I had a little trouble installing Ubuntu 24.04.1 from an arm64 minimal server live CD inside the VM, so I've opened up this issue on the Proxmox forums:
Testing Proxmox VE on Ampere Altra Max (Armv8)
.
Platform Support
Officially, they only support NVIDIA Grace Hopper and Vera server platforms (I'm guessing NVIDIA was interested in bringing up Proxmox support, and helped in some way?).
For other platforms:
Best-effort support on other UEFI-based ARMv9-A or newer hardware (ARMv8-A generally works as well, likewise best-effort)
The host must boot through UEFI and describe its hardware through ACPI
Device-tree-only single-board computers, such as the Raspberry Pi, are not supported
I don't think that precludes this flavor of Proxmox from running on the Raspberry Pi. The forked
Raspberry Pi 5 UEFI
project enables UEFI support (with some limiations) on the Pi 5, and similar projects exist for other popular SBCs, like the
Rockchip RK3588
.
Update
: Mastodon user
@
[email protected]
got it running on Pi 4
already, using
this UEFI firmware from pftf
.
Update 2
: And YouTube user
@_Jonny_ got it working on a Pi 5
, installing things manually on top of Pi OS 13 ("Trixie"), and disabling NetworkManager and cloud-init.
The other main Armv9 platforms I've used are Apple's M-series computers (some older M-series systems may work via Asahi Linux, maybe?), and systems built around the Cix P1 SoC in the
Radxa Orion O6
,
Minisforum MS-R1
, and
Framework AI PC Mainboard
.
Here's a video of the entire install and first look on my Ampere Altra Developer Platform:
Due to time limitations, I've only been able to test on my Ampere Altra Max system. I'd love to hear any of your experiences on other arm64 systems in the comments below!
