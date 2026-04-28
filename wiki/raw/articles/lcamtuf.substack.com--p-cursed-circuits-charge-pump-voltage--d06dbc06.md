---
title: "Cursed circuits: charge pump voltage halver"
url: "https://lcamtuf.substack.com/p/cursed-circuits-charge-pump-voltage"
fetched_at: 2026-04-28T07:02:48.799841+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Cursed circuits: charge pump voltage halver

Source: https://lcamtuf.substack.com/p/cursed-circuits-charge-pump-voltage

In the spring of 2023, when this Substack had only a handful of subscribers, I posted a primer on
voltage adjustment in electronic circuits
. The article opened with a brief discussion of linear regulators, and then promptly threw them under the bus in favor of more efficient charge pumps and inductor-based topologies.
The basic charge pump architecture — a voltage doubler — is quite elegant and easy to understand. It’s also far more common than many people suspect: the circuit can be constructed directly on a silicon die, so it shows up inside quite a few digital chips, from modern op-amps to MCUs. If you weren’t a subscriber back in 2023, or if you don’t have a photographic memory for random blog articles, a conceptual diagram of the pump is shown below:
The operation of a rudimentary charge pump.
In the panel on the left, we see a
Cout
capacitor that’s perched on top of the positive rail while a “flying” capacitance
Cf
is charging from the power supply. The charging process produces a voltage that’s internal to the component: we can unplug
Cf
, put it in our pocket, and then hook it up to another circuit to power it for a brief while.
In the second panel (right), we see the second part of the cycle:
Cf
is disconnected from the supply and then hooked up to the terminals of
Cout
. This action transfers some of the charge from
Cf
to
Cout,
up until the voltages across the terminals of the capacitors are equalized. After several of these
roundtrips,
V
AB
should approach
Vsupply
. Of course,
V
BC
is also equal to
Vsupply
; it follows that the voltage between A and C must be the sum of the two, or
2 ·
Vsupply
.
In other words, the circuit is a voltage doubler; the repeated motion of
Cf
ensures that the charge in
Cout
is continually replenished if we connect any load between the points A and C. There will be a bit of voltage ripple, but the amount can be controlled by sizing the capacitors and choosing the operating frequency to match the intended load.
Naturally, practical charge pumps don’t mechanically move a capacitor around. Instead, they use transistors configured as switches to alternately connect
Cf
to to the supply and to the output cap, an architecture that can be sketched the following way:
A more practical outline of a charge pump voltage doubler.
The transistors themselves can be driven by a simple
relaxation oscillator
or by a programmable digital chip.
A similar circuit can be used to produce negative voltages: we do this simply by dangling
Cout
from the negative supply rail instead of perching it on top of the positive one. This modification effectively places the capacitor’s bottom terminal at
-Vsupply.
So far, so good. But this brings us to a more perplexing flavor of the charge pump — the voltage-halving topology shown below:
A mildly cursed “voltage halver”.
What’s that, you might ask — a capacitor-based voltage divider? Well, yes and no. Capacitors
can
be used as voltage dividers for AC signals: they exhibit a
resistance-like effect known as reactance
, so if you have an alternating sinusoidal waveform, you can attenuate it that way. That said, the divider doesn’t really work for DC voltages, because at 0 Hz, the reactance approaches infinity.
To grasp the design, ignore
Cf
and the attached load. Let’s focus just on the pair of series capacitors:
C1
and
C2
. When these two capacitors are first connected to the power supply, they can be analyzed as a single composite capacitance, with some common charging current that will briefly flow through this circuit branch. In particular, if
C1 = C2
, the common current will produce roughly the same charge state for each capacitor, resulting in
V
AB
≈ V
BC
≈ Vsupply / 2.
This sounds like the outcome we’re after, but once the common charging current ceases, there’s nothing to keep the voltages the same.  In particular, if we connect a resistive load across terminals B and C, the bottom capacitor will discharge to 0 V; the reduction in the voltage at point B will also allow the upper capacitor to charge in a way that makes up the difference. A momentary current will flow, but the end state is
V
AB
=
Vsupply
,
V
BC
= 0 V, and
Iout
= 0 A.
This sounds useless, but that’s where the flying capacitor —
Cf
— comes into play. If it’s moved back and forth between
C1
and
C2
, it will charge from the capacitor that sits at a higher voltage and then discharge into the one that’s at a lower voltage; in our example, it will continually replenish the charge in
C2
, allowing a steady current to flow through the load.
The stable equilibrium for this charge transfer process is reached when
V
AB
≈
V
BC
≈
Vsupply
/ 2 — so in contrast to conventional voltage dividers, the output voltage is always at the midpoint between the supply rails, with no dependency on the relative values of
C1
and
C2
. Pretty neat!
👉 For further articles about electronics,
click here
. In particular, you might enjoy:
I write well-researched, original articles about geek culture, electronic circuit design, algorithms, and more. If you like the content, please subscribe.
