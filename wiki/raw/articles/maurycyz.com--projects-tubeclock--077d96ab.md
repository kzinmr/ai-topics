---
title: "Building a clock from salvaged Vacuum Fluorescent Displays"
url: "https://maurycyz.com/projects/tubeclock/"
fetched_at: 2026-05-15T07:01:01.878098+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Building a clock from salvaged Vacuum Fluorescent Displays

Source: https://maurycyz.com/projects/tubeclock/

Building a clock from salvaged Vacuum Fluorescent Displays
2026-05-14
(
Electronics
)
When was disassembling an old calculator (as you do) I found these cool VFD tubes:
Normally, a whole display is built into a single flat package, which doesn't look particularly interesting.
These ones have the individual digits inside a standard vacuum-tube housing, which gives them a cool nixie-esque look.
Because vacuum tubes are rather archaic components
, they deserve some introduction.
The simplest tube has two electrodes: A filament and anode plate.
Similar to an old-school lightbulb, the filament is a tungsten wire that heats up when a current passes through it.
On a microscopic scale, heat is vibration of atoms —
which knocks some (negatively charged) electrons out of the wire and into the surrounding space.
If the plate has a positive voltage, it attracts some free electrons which allows a current to flow.
If the plate is negative, the electrons are repelled and the tube doesn't conduct.
This diode configuration is useful for power supplies,
but most tubes added a wire mesh or "grid" between the other electrodes.
The grid shields the electric field of the plate, so the electrons near the filament only feel the grid's voltage.
However, because the grid has a very small area, most of the electrons it attracts fly through one of the holes to arrive at the plate.
As a result, a triode tube conducts plate to filament when both the grid and plate have a positive voltage:
similar to an n-channel MOSFET.
A Vacuum Fluorescent Display is just a triode
but with the
anode plate coated in rare-earth oxide (similar to what's found in CRTs) which glows when stuck by electrons in the tube.
In my displays, each tube contains a single grid, but the anode is broken up into seven isolated segments which can be used to form digits.
The grid allows a clever trick:
segment lines can be shared between digits as long as only a one tube is on at a time.
A single tube is supplied with a positive grid voltage, allowing it to light up,
while all the other tubes have a negative grid voltage forcing them to stay dark regardless of the segment voltage.
By quickly cycling between the digits,
the control electronics can create the illusion that the whole display is on...
but saving a lot of wires:
a six digit display with a total of 42 segments only needs 13 signal lines.
I couldn't find a datasheet for my displays
, so I had to determine the pinout experimentally:
Find the heater. It should be a pair of pins with a few ohms of resistance
Run 25 - 50 mA through it. The filament should start glowing
very dimly
. If it's bright, there's to much current.
Apply +12 volts (relative to the heater) to pairs of the remaining pins until a segment lights up: One of those pins is the grid
Moving the one of the +12 wires to a different pin, while keeping the other one connected as is.
If the display goes out, the pin you disconnected was the grid.
If a different segment is on: The pin that stayed connected is the grid.
Now, connect twelve volts to the grid and use apply +12 to the remaining pins to map out the segments.
If you try this, be very careful to not connect 12 volts across the filament.
Doing this will likely destroy the tube!
Also, on step #4, only the second outcome is guaranteed accurate if some pins are
not connected internally. It may be a good idea to try again but moving the other wire
to be sure.
With that done, I moved on to finding good operating conditions for the display
:
Increasing the filament current or/and the plate voltage will make the tube brighter...
but don't get the current to where the filament is visibly glowing:
That will make it hard to read and reduce the tube's life.
Borrowing some math from light bulbs, the expected filament lifespan is (roughly) inversely proportional
to current to the 6th power, so it's not a good idea to push it.
You'll often hear stories about that light bulb that's been running for 100 years, but it's no secret how they did it:
the bulb is running at 6% of it's rated power!
(Ok, a lot of that loss is from aging, but the original filament resistance was a lot higher than a modern bulb.
That made it run less current, at the cost of being even more inefficient and having a very red cast)
The plate voltage can be adjusted more freely, and is mostly a matter of personal preference.
However, too much will fade the phosphors faster, and again, there's a non-linear relation:
a higher voltage will cause more electrons to flow, but those electrons will also have a higher energy and do more damage.
Mine were happy
at 25 mA of heater and a voltage between 10 - 24 volts.
I settled on 12 volts, which worked well for a desk clock while not being annoying at night.
(keeping in mind that multiplexed tubes appear a lot dimmer than when driven individually)
While 12 volts is much lower than what's used for nixie tubes
, it's still to high for a microcontroller.
Since they don't draw much current, I stepped up the signals using a MOSFET and pull up resistor:
Vector version
When the MOSFET is on, these drivers dissipate a good 0.14 W as heat, which comes out to ~1.5 W (peak) for the whole device...
but it's still less then a typical smoke detector burns in it's power supply, so it's acceptable for a mains-powered device.
The heater drive resistors also dissipate a half a watt, so they do get quite warm.
Historically, tube filaments were run from a dedicated 1 to 3 turn transformer winding, but such multi-voltage transformers are hard to find nowadays.
On the microcontroller's end
, it's all very standard clock stuff:
the same as driving any other multiplexed seven-segment display.
I wrote a 480 Hz timer interrupt to cycle the active digit and assert the correct segments.
The results in an effective refresh rate of 120 Hz, so it's a
gaming clock
.
While a microcontroller's internal oscillator is fine for most applications,
it's not good enough for a clock:
A 1% error would cause it to drift by 7 hours each month...
To avoid this, timekeeping is done by a second timer interrupt run from a 32.768 kHz quartz crystal,
which should keep the drift to within a few minutes per year.
Crystal loading capacitors are not optional:
A few picofarads might seem trivial, but without them, it can struggle to oscillate or run at the wrong frequency.
The neon lamp is a visually consistent separator, but isn't currently wired up to anything.
These need around 100 volts, so it would take some doing to make it work.
... and the same clock after making it a wooden box
:
Because I'm not very good at woodworking, I made it by gluing together a bunch of scrap wood into a block
and using a CNC mill to cut a clock-shaped pocket and round the edges.
I kept the back open
out of laziness
to provide easy access to the buttons and for cooling.
There was a bit of workholding drama half way through, but it's nothing that couldn't be fixed with some wood filler and sanding.
Related
:
