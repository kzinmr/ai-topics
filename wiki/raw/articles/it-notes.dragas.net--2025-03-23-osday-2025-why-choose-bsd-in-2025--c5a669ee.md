---
title: "OSDay 2025 - Why Choose to Use the BSDs in 2025"
url: "https://it-notes.dragas.net/2025/03/23/osday-2025-why-choose-bsd-in-2025/"
fetched_at: 2026-04-29T07:02:11.281065+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# OSDay 2025 - Why Choose to Use the BSDs in 2025

Source: https://it-notes.dragas.net/2025/03/23/osday-2025-why-choose-bsd-in-2025/

This is the text underlying my presentation at
OSDay 2025
, held on 21 March 2025 in Florence, Italy. There was limited time, so I couldn't go into much detail and had to keep things more general and structured than usual. You can watch
the video of my talk on YouTube
.
The slides can be downloaded
here
Happy reading!
OSDay Florence - 21 March 2025 -
Why Choose to Use the BSDs in 2025
"I'm Stefano Marinelli,
I solve problems
."
I'm the founder and Barista of the
BSD Cafe
, a community of *BSD enthusiasts.
I work in my company, called
Prodottoinrete
- a container of ideas and solutions.
I'm passionate about technology and computing, and I've made my passion my profession. Every morning, when I sit in front of the computer, a new world opens up for me to explore.
I've been a Linux user since 1996, before I turned 17. Back then, I used Fidonet and would read about alternative operating systems. I experimented with Linux distributions from CDs, and by 1997, Linux became my everyday system. It was only in 2002 that I began exploring BSD systems, largely thanks to FreeBSD's fantastic handbook.
The relationship we had with Open Source 20-30 years ago was fundamentally different than today. Back then, embracing Open Source meant thinking differently. It meant embracing freedom. We chose Linux and the BSDs when Windows and commercial Unix systems dominated the market. Not because they were simple or free (as in free beer), but for freedom from impositions - both technological and ideological.
I solve problems.
And to solve problems effectively, we need to recognize when the landscape has changed.
The reality today is that while we won that war - Open Source is everywhere - we're facing a new challenge. The "mainstream" Open Source world is creating monocultures. The focus has shifted from technologies to specific tools. We're seeing innovation for novelty's sake, not problem-solving.
This shift has profound implications. In a world dominated by cyber threats, where everything is connected and we completely depend on technology, the value of stability has been lost. By stability, I don't just mean that a system doesn't crash. I mean continuity over time, upgradeability, and system visibility.
Instead, the industry seems obsessed with the hype cycle. "New" is prioritized over secure and stable. The mantra has become: - "It will be fixed in the next version" - "We need automatic restarts when it crashes" - "Do we need software that crashes less? We have systemd and Kubernetes to restart crashed workloads!" - "We need moooarrr powaaaaaaar!!!!"
Let me give you a concrete example. A program written in Rust should be memory safe - that's one of the main selling points of the language. But if that program uses unsafe functions and segfaults, what advantage does it offer over a mature C implementation? Stability matters more than the implementation language.
I solve problems.
And creating a monoculture does not solve problems - it creates new ones.
Yes, Linux, Docker, and Kubernetes are better than closed source solutions. But when everyone uses the same tools, freedom dies. We use them because "everyone does" rather than because they're the best tool for our specific needs.
If we had only used what everyone else used, we wouldn't have Linux or the BSDs today. There would be no LibreOffice, no Nextcloud. We'd just have Windows variations and expensive Unix systems. We'd be bound by licenses and vendors, stuck with closed solutions.
This is where the BSDs offer a compelling alternative: "Be free and evaluate alternatives. Always."
For those who don't know, the original BSD started in the 1970s (before Linux was conceived). Minix was created as an educational OS because it was believed that BSD, mature and professional, would be the Open Source OS that would dominate the market. A legal case stalled development and scared adopters, but in 1993, NetBSD and FreeBSD emerged. OpenBSD forked from NetBSD later, then DragonflyBSD from FreeBSD.
As Linus Torvalds said in 1993, "If 386BSD had been available when I started on Linux, Linux would probably never had happened."
What makes the BSDs special is their philosophy: - Kernel and userland developed by same teams - Consistency in tools and updates - Excellent documentation - especially OpenBSD, where insufficient docs are considered a bug - Man pages contain virtually everything - Evolution, not Revolution
Let me briefly introduce the main BSD variants that I work with daily:
FreeBSD
is a generalist system. It focuses on stability and performance - with HardenedBSD as a security-enhanced fork. It has native ZFS, Boot Environments, and complete separation between OS and packages. It's had container support via jails since 2000 - which predates Linux cgroups by a decade! It offers bhyve virtualization (more efficient than KVM). OPNsense and pfSense are based on FreeBSD, as pf is a powerful firewall. It's used by Netflix for streaming video delivery and forms the foundation for PlayStation consoles. MacOS and iOS also contain some FreeBSD code.
OpenBSD
focuses on security and code correctness. Its code is constantly audited and simplified - less is more. The team believes "The more complex the code, the less maintainable." It has security mechanisms like pledge() and unveil(). OpenSSH (and many other nice things) originated and are developed here. Development is driven by team priorities, not user requests. It's ideal for routers, firewalls, and security-critical systems.
NetBSD
lives by the motto "Of course it runs NetBSD!" Its focus is on correctness, portability, and proper implementation. It supports 50+ architectures. Development centers on compatibility, which necessitates code quality. It must function on decades-old hardware. It's ideal for systems that require stability without the need for continuous updates, like embedded devices.
I solve problems.
And in my experience, the BSDs have consistently proven to be excellent problem-solvers. Here are some real-world benefits I've experienced:
Better stability and security
Simplified administration - upgrades won't destroy your system
Less vulnerability to common attacks
- "We don't need this patch, you're running OpenBSD and it's been fixed 20 years ago"
Network interfaces maintain consistent names - ix0 will remain ix0, not renaming from enx3e3300c9e14e to enp10s0f0np0
FreeBSD shows lower system load compared to Linux
FreeBSD handles I/O pressure better -
on the same hardware, I've seen 70% time reduction
FreeBSD delivers improved end-user experience/responsiveness
NetBSD provides the comfort of "Don't worry - your platform will be supported for the foreseeable future"
So why choose BSD in 2025? I believe there are several compelling reasons:
Security in an increasingly hostile environment
Stability in a world obsessed with novelty
Performance without unnecessary complexity
Freedom from the mainstream monoculture
Systems designed with coherent philosophy
Don't be afraid to try BSD systems - despite the Beastie mascot, they don't hurt and you'll appreciate them!
See you at
BSD Cafe
!
