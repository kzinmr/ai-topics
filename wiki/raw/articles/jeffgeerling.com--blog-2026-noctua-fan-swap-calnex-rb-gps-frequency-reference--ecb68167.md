---
title: "Noctua Fan Swap on a Calnex Rb/GPS Frequency Reference"
url: "https://www.jeffgeerling.com/blog/2026/noctua-fan-swap-calnex-rb-gps-frequency-reference/"
fetched_at: 2026-10-28T10:01:25.555979+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Noctua Fan Swap on a Calnex Rb/GPS Frequency Reference

Source: https://www.jeffgeerling.com/blog/2026/noctua-fan-swap-calnex-rb-gps-frequency-reference/

Since this will be the
only
source of this process on the Internet
, I figured I'd document a quick fan swap I did on a piece of test/reference equipment I'm running in my
Atomic Clock Tower
.
I took my Torx T10 screwdriver and popped off the top cover. The screws required some force to loosen, as they were all secured with Loctite.
The inside is simple and serviceable. There's a
SpectraTime GRClok-1500
, with an integrated timing-grade GPS module, and a stabilized 10 MHz output
.
The Calnex PCB seems to divide a 1 PPS signal from that output for the front panel connection, and provides power to the unit.
The cooling solution is a bit funky:
There's a very poke-y stabby aluminum heatsink
screwed down to a large heat spreader, to which the GRClok is attached. Everything inside is screwed down but is easy enough to remove, despite some sticky thermal interface material.
The problem
I
had with the Frequency Reference is noise: I want to use it near my desk, and to have a stable output, it needs to run practically 24x7. The warm-up period for any clock-based device is measured in hours, sometimes days. And the noise from the original Delta EFB0412HHD fan was unbearable. Not loud, but annoying.
Since it's a 12V fan, and I'm running in an already-air-conditioned environment, I wasn't worried about reducing the static pressure a bit. So I installed a
Noctua NF-A4x20 FLX
, using the stabby OmniJoin cable connectors Noctua provides for custom fan installs. The fan connector on Calnex's PCB was a strange square 4-pin arrangement, and I didn't have ends that would stick into that tiny connector.
So I just snipped the cable, stripped the ends, put the stabby connectors inline, and installed the Noctua fan. I didn't torque down the fan screws too tightly, though, just enough that the Noctua fan’s rubber bumpers were snug to the case.
I should mention, since the heatsink was in the way, and I didn't want my fingers to turn into a bloody mess, I removed it by flipping over the unit, and removing four screws that were holding it down:
This picture was taken after removing the bottom cover (with captive screws holding down rubber feet), and may I just take a second to admire Calnex's choice to use the
exact same
screw head for every part of the internals: a trusty Torx T10?
It is quite rare to take apart a device these days and
not
have to pull out multiple bits from an iFixit toolkit, or have multiple exotic screwdrivers at the ready.
This device seems like it was built by engineers and not optimized
too
much for space and cost. And I guess it wouldn't be, since it's not exactly cheap (they don't publish a price for the unit online). But I wish more devices were designed for this ease of serviceability.
Anyway, I got the thing put back together, plugged it in on top of my Clock Tower (if they redesigned the chassis, everything would fit nicely inside 2U of mini rack space...), and got its reference output into my PPS Signal Analyzer, ready for the next few years of clock building!
And yes, it's not locked yet in this photo. It takes 20-30 minutes to acquire a rubidium timing lock and GNSS sync.
