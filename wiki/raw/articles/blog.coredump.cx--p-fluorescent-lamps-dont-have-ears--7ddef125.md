---
title: "Fluorescent lamps (don’t) have ears"
url: "https://blog.coredump.cx/p/fluorescent-lamps-dont-have-ears"
fetched_at: 2026-09-01T10:00:43.870743+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Fluorescent lamps (don’t) have ears

Source: https://blog.coredump.cx/p/fluorescent-lamps-dont-have-ears

I never mentioned it publicly, but early in my career, I did a part-time stint in
technical surveillance countermeasures
(TSCM) — a fancy term for sweeping office environments in search of electronic bugs and other unauthorized spy gear. In practice, the job entailed getting several certifications, hauling around a bunch of costly suitcases, and above all, spending some time with ex-spooks, listening to stories that would make James Bond blush.
The discipline is rather hush-hush, so you never know what’s real. One of the more striking claims I remember from the training was that fluorescent lamps could be used to passively eavesdrop on conversations in the room. This makes some sense: the tubes are filled with glowing gas. A sound wave propagating through this medium could theoretically produce subtle luminosity fluctuations that could be picked from afar.
To be clear, long-distance optical audio pickup is real: if you shine a laser at a pane of glass or other reflective surface, sound-induced vibrations can be picked up by measuring the angle of the reflected beam; in favorable conditions, this supposedly works at distances in excess of 100 m (330 ft). Far less practically, a
Black Hat presentation in 2020
demonstrated the ability to passively recover audio by placing a beefy speaker 1 cm away from a dangling lightbulb, and then observing the motion of the lightbulb via a telescope from about 25 m (80 ft).
But is the claim about fluorescent lamps true? At first blush, it sounds physically plausible. But when you think about it, the gas in the tube is kept at about 1/200th of atmospheric pressure. It’s nearly vacuum — hardly a good medium for sound waves. Worse, the glowing gas emits UV, which needs to be converted to visible light using an opaque phosphor layer that covers the inside of the tube and exhibits strong afterglow. Wouldn’t that mask any momentary, localized changes in luminosity?…
After two short decades, I couldn’t take it anymore and decided to test the claim. My initial plan was to tape a photodiode directly to the tube, connect the sensor into a low-noise amplifier, and then view the resulting waveform on an oscilloscope. But then, I settled for a simpler approach: I placed the lamp next to a high-intensity sound source — a 200 W audio system hooked up to a signal generator and cranked all the way up — and then took a series of high-speed, up-close photos with a shutter of 1/8000 s. I figured that if such powerful sound waves don’t produce visible artifacts in any of the captured 14-bit images, the odds of the scheme working in a more realistic scenario were minimal, even if we used more precise measurement gear.
But first, I needed to power the tube. Traditional fluorescent lamps rely on thermionic emission to get going: there’s a pair of terminals on each end that connects to an internal heater coil. Once the coil is heated to a glow, it becomes easier for thermally-excited electrons to dart off into the void in response to an externally-applied electromotive force. In this respect, the device is similar to a vacuum tube.
A conceptual sketch of a fluorescent lamp.
For the 9” tube I purchased, the heater needed a current of about 200 mA at 16 V. I opted for DC operation to minimize AC-induced flicker, so it was sufficient to heat just the negative side. With that done, the terminals on each end would be shorted and a voltage of roughly 70-80 V would be applied across the tube. The voltage causes plasma to form; from that point on, the current must be capped to about 180 mA at ~35 V.
Here’s a quick video showing the process of manually starting the lamp:
I’ll spare you the dozens of fast-shutter photos I’ve taken while playing back different audio frequencies: they show nothing at all. These non-results are summarized more concisely in the following video of a wide-frequency audio sweep:
I really wanted to believe the claim. Maybe someone else can still “prove” it; pump the volume up even higher, use a larger tube, take absurdly precise measurements. But in terms of a practical attack, I think the myth is busted. Sorry, Mr. Bond?
