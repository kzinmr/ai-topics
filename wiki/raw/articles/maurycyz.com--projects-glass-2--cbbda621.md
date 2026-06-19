---
title: "Glassblowing #2: Making a tungsten lamp and (bad) vacuum diode"
url: "https://maurycyz.com/projects/glass/2/"
fetched_at: 2026-06-19T07:00:57.259961+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Glassblowing #2: Making a tungsten lamp and (bad) vacuum diode

Source: https://maurycyz.com/projects/glass/2/

Glassblowing #2: Making a tungsten lamp and (bad) vacuum diode
2026-06-18
Now that I have a way to run electrodes through
glass
, it's time to do something with that.
An old school lightbulb is rather simple: just a thin wire that gets hot enough to glow.
However, to produce anything approaching white light, the wire must get to around 2500 C.
While conductors like tungsten or graphite can survive those temperatures, they all burn on contact with air.
To prevent this, I'll be sealing my lamp in glass under vacuum: no air, no problem.
I lied.
Some ceramics start conducting once heated, and being oxides, are completely unaffected by oxygen.
Open air "Nernst lamps" did enjoy brief popularity in the 1890-1900s, but because of the added complexity of preheating the filament,
they were replaced by filament lamps once vacuum pumps became good enough for commercial production.
To start, I bent some some 0.3mm diameter tungsten wire into a "U" shape, and twisted a length of very fine 0.012 mm tungsten wire onto the free ends.
I cut one side of the lead frame shorter so that the filament would sit diagonally:
allowing it to be reasonably long without looping it around which could result in a short.
To make the bulb, I partially inserted the lead frame into a glass tube, heated the end with an oxy-propane torch and pinched the glass onto the wires:
Once one end was sealed, I connected the other to a rotary vane vacuum pump, and pumped it down while lightly heating the tube to remove moisture.
After a few minutes, I headed the middle of the tube to sale the bulb, and pulled off the excess tubing.
After the glass cooled, I cut the middle of the wire "U" to separate the leads:
Glowing at 4 volts
The finished lamp glows nicely between 200 and 400 mA (3-6 V and 0.5-2.5 W):
I didn't stretch the filament tight enough and it ended up touching the glass, which creates a dim spot.
The glass is borosilicate, so I'm not too worried about cracking, but it's still not ideal.
I've tested the bulb up to 10 volts
(~7 W), which is bright to light up a whole room,
and the creates white light instead of the orange-ish color seen at low power —
but it also gets very hot and won't last very long.
In addition to color, the filament's temperature also affects the bulb's efficiency:
a low temperature filament emits the vast majority of it's light in the infrared.
A hot filament emits more visible light per watt, but tungsten evaporates faster leading to early failure.
This tradeoff between lifespan and color/efficiency is why most light bulbs have rather short lifespans...
or at least they did until we stopped using filaments.
As an experiment
, I ran a length of wire through a hole in the glass tube before evacuating it:
When making seals like this, first melt a capillary tube (~1 mm) onto the tungsten wire before sealing it.
This ensures good contact to the metal and protects the wire from the torch flame.
The idea was to observe thermionic emission:
when the filament is white hot, the atom's have enough kinetic energy to knock electrons into the vacuum.
If the cold electrode is at a positive voltage, these electrons allow a small current to flow.
If it's negative, the free electrons are repelled and nothing happens.
While a diode isn't terribly exciting, it's the basis of more interesting devices like triodes, X-ray tubes and CRTs.
... and it's terrible
: only conducting 1 uA with 700 V of bias between the filament and anode.
Reverse biased, it conducts around 50 nA, mostly from the photoelectric effect.
I suspect this is the result of two problems.
Tungsten wire contains trapped gasses, which are released when it's heated.
To avoid ruining the vacuum, the filament should be run while pumping down the tube, which I forgot to do.
Second, the anode area is really small: Its ~6 mm of 0.3 mm wire, several centimeters away from the filament.
Most emitted electrons will miss the anode and create a negative charge on the glass, which impedes current flow.
Real vacuum diodes surrounding the filament in a metal tube, but I didn't do that because I wanted it to work as a light bulb.
Just for fun
, here's a photograph of my spool of filament wire, lit by the bulb made using it:
Related
:
