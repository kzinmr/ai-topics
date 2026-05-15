---
title: "First public macOS kernel memory corruption exploit on Apple M5"
url: "https://blog.calif.io/p/first-public-kernel-memory-corruption"
fetched_at: 2026-05-15T07:01:02.259882+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# First public macOS kernel memory corruption exploit on Apple M5

Source: https://blog.calif.io/p/first-public-kernel-memory-corruption

Early this week, we had a meeting at Apple Park in Cupertino. While there, we also shared with Apple our latest vulnerability research report: the first public macOS kernel memory corruption exploit on M5 silicon, surviving
MIE
. It was
laser
printed, in honor of our hacker friends.
We wanted to report it in person, instead of getting buried in the submission flood that some unfortunate Pwn2Own participants just experienced. Most respected hackers avoid human interaction whenever possible, so this physical strategy may give us a slight edge in the eternal race for five minutes of fame and glory on Twitter.
This is the story of the exploit and our field trip. Full technical details will be shared after Apple fixes the vulnerabilities and attack path. Hopefully it won’t take our beloved company too long. We only budgeted one year of domain registration fees for this attack.
Memory corruption remains the most common vulnerability class everywhere, including iOS and macOS. In security, if you can’t fully prevent something, you
accept the risk
mitigate it by making exploitation more expensive.
But mitigations are not cheap. If performance didn’t matter, many security problems would be easy to solve. Apple is smart and controls the full stack, so they pushed many of these defenses directly into hardware and made bypassing them significantly harder. Many security experts consider Apple devices to be the most secure consumer platform.
The latest flagship example is MIE (Memory Integrity Enforcement), Apple’s hardware-assisted memory safety system built around ARM’s MTE (Memory Tagging Extension). It was introduced as the marquee security feature for the Apple M5 and A19, specifically designed to stop memory corruption exploits, the vulnerability class behind many of the most sophisticated compromises on iOS and macOS.
Apple spent five years building it. Probably billions of dollars too. According to their research, MIE
disrupts
every public exploit chain against modern iOS, including the recently leaked Coruna and Darksword exploit kits.
We’ve been on a fun journey exploring how AI can help build exploits that still work under MTE. While Apple’s focus is primarily iOS, they also brought MIE to the M5, the chip powering the latest MacBooks.
Our macOS attack path was actually an accidental discovery. Bruce Dang found the bugs on April 25th. Dion Blazakis joined Calif on April 27th. Josh Maine built the tooling, and by May 1st we had a working exploit.
The exploit is a data-only kernel local privilege escalation chain targeting macOS 26.4.1 (25E253). It starts from an unprivileged local user, uses only normal system calls, and ends with a root shell. The implementation path involves two vulnerabilities and several techniques, targeting bare-metal M5 hardware with kernel MIE enabled.
PoC video:
We didn’t build the chain alone. Mythos Preview helped identify the bugs and assisted throughout exploit development.
Mythos Preview is powerful: once it has learned how to attack a class of problems, it generalizes to nearly any problem in that class. Mythos discovered the bugs quickly because they belong to known bug classes. But MIE is a new best-in-class mitigation, so autonomously bypassing it can be tricky. This is where human expertise comes in.
Part of our motivation was to test what’s possible when the best models are paired with experts. Landing a kernel memory corruption exploit against the best protections in a week is noteworthy, and says something strong about this pairing.
To the best of our knowledge, this is the first public macOS kernel exploit on MIE hardware. Again, we’ll publish our 55-page report after Apple ships a fix.
MIE was never meant to be hacker-proof. With the right vulnerabilities, it can be evaded. As we’ve shown throughout the
MAD Bugs
series, AI systems are already discovering more and more vulnerabilities. It’s inevitable that some of those bugs will eventually be powerful enough to survive even advanced mitigations like MIE. This is exactly what we just discovered.
This work is a glimpse of what is coming. Apple built MIE in a world before Mythos Preview. We’re about to learn how the best mitigation technology on Earth holds up during the first AI bugmageddon.
Epilogue
The Apple spaceship is every bit as breathtaking as people say. It has a lot of apple trees, obviously. We wanted to check out the infamous Infinite Loop too, but were afraid it could take a long time.
Our hosts shared that Apple spent $5 billion building this “office”, then asked about our office. We said, well, ours definitely cost
less
than $1 billion.
But this is the fun part about AI. Small teams can suddenly do things that used to require entire organizations. With the right strategy and people, even a tiny company can become mighty enough that the world’s largest companies start asking for its help.
In Vietnamese, we say, “nhỏ mà có võ”.
