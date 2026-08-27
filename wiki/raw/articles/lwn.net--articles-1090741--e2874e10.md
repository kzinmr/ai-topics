---
title: "Armbian 26.8 released"
url: "https://lwn.net/Articles/1090741/"
fetched_at: 2026-08-27T10:01:14.531864+00:00
source: "LWN.net"
tags: [blog, raw]
---

# Armbian 26.8 released

Source: https://lwn.net/Articles/1090741/

Armbian 26.8 released
[Posted August 26, 2026 by jzb]
Version 26.8
of
the
Armbian
distribution for Arm hardware has
been released.
Most releases are a long list of small improvements. This one had three
larger pieces landing at roughly the same time, and all three touch parts of
Armbian that people use directly rather than parts they only read about in
changelogs.
The installer was rewritten. Armbian Imager reached 2.0. And our CI moved out
of the repository it had outgrown into one built for the job. None of these were
planned to coincide; they simply reached the point where postponing them again
would have cost more than doing them.
The installer rewrite is the one I expect people to notice first. It now
ships as an armbian-config module, which means it is unit-tested, the same way
the rest of armbian-config is tested, rather than living as a script that
everyone was slightly afraid to touch. It can target SPI and MTD, treats eMMC
and NVMe as separate flows instead of pretending they are the same thing, can
flash a bootloader on its own, and — this one is overdue — reports when a
bootloader write fails instead of printing "Done." and leaving you to find out
at the next boot.
See the
release notes
for a full list of changes.
