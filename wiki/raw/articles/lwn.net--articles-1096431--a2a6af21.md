---
title: "Research into file-notification attacks on Linux"
url: "https://lwn.net/Articles/1096431/"
fetched_at: 2026-09-25T10:01:26.128608+00:00
source: "LWN.net"
tags: [blog, raw]
---

# Research into file-notification attacks on Linux

Source: https://lwn.net/Articles/1096431/

Research into file-notification attacks on Linux
[Posted September 24, 2026 by jzb]
Sudheendra Raghav Neela, a member of a group of researchers from
Graz University of Technology
, has
announced
the
release of research into file-notification attacks that would allow spying on
user activity on Android, Linux, macOS, and Windows. The group has published
a paper
with
details on the research as well as a
web site
with demonstrations of the vulnerabilities.
On Linux, an attacker can use
inotifywatch
to
monitor a directory to conduct an inter-keystroke timing attack—even if
they do not have read access to the files within a directory. The group also
discovered a method to conduct a
UI-redress
attack
(or "
clickjacking
" attack) on
KDE 5 and KDE 6 by monitoring
/usr/bin/pkexec
to detect when
Polkit
spawns an authentication
prompt. An attacker could draw a fake password window on top of the real window
to collect a user's credentials.
Both of these flaws are still present today,
though the Linux kernel did partially mitigate the issue with
a
fix
that was included in the 5.10.248, 5.15.198, 6.1.160, 6.6.120, 6.12.65,
and 6.18.3 kernels shipped in January. See the web site for more information and
a mitigation to prevent password-prompt windows from losing focus.
The LWN site is currently under high scraper load, so comment
    display has been suppressed for anonymous users.
    If you are a
        human, you may read the comments by clicking the button below:
Note
: you can avoid this step in the future by logging
        into your LWN account.
