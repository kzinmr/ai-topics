---
title: "Cursed circuits #6: reverse avalanche oscillator"
url: "https://lcamtuf.substack.com/p/cursed-circuits-6-reverse-avalanche"
fetched_at: 2026-07-09T07:01:30.864484+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Cursed circuits #6: reverse avalanche oscillator

Source: https://lcamtuf.substack.com/p/cursed-circuits-6-reverse-avalanche

Last year, I published an article titled
“It’s hard to build an oscillator”
:
The title alluded to the fact that there’s no shortage of oscillator circuits on the internet, but many of them use unusual parts, need weird supply voltages, or don’t work well (if at all).
But sometimes,
bad
rises to an art form. Here’s probably the most puzzling bad oscillator you can assemble today with the parts you have at hand:
Reverse avalanche oscillator. Other small NPN transistors should also work.
At first blush,
nothing here makes sense
. The transistor is upside down and its base terminal is not connected. And yet, the circuit works: hook it to a supply of about 14-20 V and watch the LED blink.
If you connect an oscilloscope to the terminals of the capacitor, you’ll see that the cap is repeatedly charging to about 10 V, then rapidly dumping some of the charge, all the way down to 9.1 V:
Capacitor charge state with a 14 V supply (5.8 Hz oscillation). By author.
It’s no mystery that the capacitor must be charging via the 1 kΩ resistor from the positive supply rail. It’s also clear that the energy is dumped into the LED via the upside-down NPN transistor. But why?
To answer this, you’ll need a basic grasp of semiconductor junctions. If you’re rusty on how they work, this earlier article should jog your memory:
As a quick recap, a conventional diode consists of a
p-n
junction formed from two distinct types of semiconducting materials. At the boundary between these materials forms a non-conductive region known as the depletion layer. In forward bias — when a small positive voltage is applied to the
p
-side in relation to the
n
-side — the depletion layer is disrupted and charge carriers can cross.
In reverse bias, in contrast, the depletion region remains notionally impassable. That said, if the applied reverse voltage is high enough, the electrostatic field grows so strong that it can accelerate charges with sufficient force to knock electrons in the depletion region into the conduction band in an avalanche-like effect. This makes the junction conductive again:
Breakdown in a 1N4148 diode. By author.
An NPN transistor, as the name implies, is an
n-p-n
semiconductor structure that resembles two conjoined diodes. No matter whether we make the collector terminal or the emitter terminal more positive, one of these diodes is always reverse-biased; it follows that in the circuit we’re looking at, conduction should not occur.
At the same time, the reverse-biased junction that’s standing in the way is susceptible to avalanche breakdown if we supply a sufficiently high voltage. If the transistor is oriented the usual way — if the collector is more positive — the breakdown voltage for 2N2222 is around 50 V. But if we connect the component the other way around, the emitter-collector threshold is only a bit over 8 V. This is because the emitter area is doped more heavily (
n++)
. The depletion region formed in a heavily-doped semiconductor is thinner and easier to disrupt, so the emitter-side
n++-p
junction is an easier fight.
But that’s not all: this circuit won’t oscillate with an ordinary reverse-biased diode. There’s a point on the diode V-I curve where the charging current admitted through the 1 kΩ resistor matches the discharge current flowing through the diode, so the circuit would simply settle at that voltage.
The essence of what makes our circuit different is the following V-I plot painstakingly obtained for a reverse-biased NPN transistor with a floating base:
V-I plot for 2N2222 at I
B
= 0. Dashed line: what we’d expect of a diode.
The
n++-p-n
structure remains non-conductive until we reach about 8.2 V. But as soon as the “hump” is cleared, the conduction path begins to open up more in response to the current we’re pushing through. With 5 mA flowing through the junction, we need about 8 V to sustain the process; at 40 mA, we only need 7 V.
This curve rules out the possibility of a stable equilibrium for the circuit. The capacitor charges until it reaches the “hump”; at that point, some small discharge current starts flowing through the transistor, but the resistor, which lets through 10 mA, still more than makes up for the loss. The capacitor is decisively pushed into “dip” where the current skyrockets while allowing the voltage to taper off. But eventually, the capacitor voltage is too low to sustain the current, and because of the shape of the curve, that voltage is
even less able
to sustain lower currents. The transistor cuts off.
Some old-timers may recall that there’s another component that behaves the same way: the neon lamp. The lamp requires a higher starting (“striking”) voltage to ionize the gas, but once plasma is formed, you don’t need nearly as much. Neon lamps are uncommon today, but you can build a nearly-identical oscillator with one.
To be clear, everything about this oscillator is terrible! It requires a fairly high supply voltage, it’s inefficient, it requires a beefy capacitor, and it has awful duty cycle and frequency stability. But it’s a good reminder that semiconductors are complicated beasts: the circuit is using the part of the V-I curve that isn’t even shown in most books.
Some other articles in the series:
I write about electronics,
the foundations of mathematics
,
the history of technology
, and other geek interests. If you like it, please subscribe.
