---
title: "Raspberry Pi locks down Pi 5 RAM upgrades in firmware"
url: "https://www.jeffgeerling.com/blog/2026/raspberry-pi-ram-lockdown/"
fetched_at: 2026-09-22T10:00:53.668585+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Raspberry Pi locks down Pi 5 RAM upgrades in firmware

Source: https://www.jeffgeerling.com/blog/2026/raspberry-pi-ram-lockdown/

Raspberry Pi added a feature in their firmware that
restricts users from swapping RAM chips
, sometimes even RAM chips of the same capacity from other Raspberry Pi boards.
Apparently there were people buying cheap 1 or 2 gig Pi 5s, soldering in some cheap and sometimes unreliable 8 gig RAM chips, and
selling them as new 8 gig Pi 5s
.
Now I totally understand where Raspberry Pi's coming from. They don't wanna support Pis being sold like this, because flaky RAM and dodgy resellers are a huge problem. Especially with how profitable can be in the current AI bubble.
But I also totally disagree with the way they're handling the situation.
The firmware update that disabled RAM swaps was actually from late 2024, two years ago. So you can't blame the RAM pricing situation for this.
Raspberry Pi is within their legal rights to lock down their hardware like this, but that doesn't mean we have to like it.
The big problem is there's no easy way to work around this, other than running ancient firmware (
2024-09-10-2712
or older) on the Pi.
This blog post is a lightly edited transcript of today's YouTube video:
Why
I think the most official response we'll get is
this one from PhilE on the Pi Forums
, and I can sense the frustration, especially because users of these modded Pis
are
coming to Raspberry Pi for support. They're not going to call the shop they bought the Pi from when they have problems.
But I guess one thing to answer really quick is whether Raspberry Pi actually has a technical reason for preventing the swaps, or if it's just a conspiracy to get people to pay the piper for official Pi RAM.
And the quick answer is yes, Raspberry Pi does have a point. Memory timings, especially for modern LPDDR chips, are
tricky to get right
, and having a bad solder joint, or a cheap RAM chip that only barely passed validation, means you get weird failure modes.
Not only that, heat and overclocking makes it way worse if you're not using a configuration that's been tested and tuned.
So while yes, I see Raspberry Pi's point here, on a technical level, probably even a legal one. I just don't like it from a hardware hacking level.
The whole ethos with Pi was you can tinker on it. And not being able to tinker down to the chip level feels like a big miss. Not that many people would ever desolder a RAM chip in the first place, but it's the idea that you
can
if you want.
Possible Fix
I remember Raspberry Pi had a solution for this on older Pis (up to the Pi 3 B). They had a
'warranty bit'
.
There was a firmware bit that would switch from 0 to 1 if you intentionally bypassed safety limits in your config.txt, like to overclock the Pi beyond what Raspberry Pi said was safe.
In a similar way, instead of blocking people from legitimately swapping RAM, whether that's to repair a broken board, or someday upgrade from like 2 to 8 gigs, they could implement something similar. Set a one time firmware flag declaring you don't get warranty support, upgrade the RAM, and then it's you on the hook.
The big problem is right now there's no physical way to identify these RAM-swapped Pis. There
is
a way in software, though, as highlighted in
this Geekworm blog post
. Raspberry Pi publishes all the model codes for their Pis so you could verify how much RAM is
supposed
to be on your Pi.
Someone on Hacker News even said Pi could
drill a hole
for the factory-set RAM size, instead of soldering a resistor on here. That might require a little trace re-routing, but at least it would be better than locking users out.
But in the end, it's just another sad loss in hardware ownership, that you can't swap out or upgrade the RAM chips.
