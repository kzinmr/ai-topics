---
title: "Inside a 1980s filter chip that uses switched capacitors"
url: "http://www.righto.com/2026/10/ML10-switched-capacitor-filter.html"
fetched_at: 2026-10-11T10:01:12.180230+00:00
source: "righto.com"
tags: [blog, raw]
---

# Inside a 1980s filter chip that uses switched capacitors

Source: http://www.righto.com/2026/10/ML10-switched-capacitor-filter.html

Sometimes it's easier to identify an IC with a microscope.
While sorting a box of old ICs, CuriousMarc came across some Harris ICs labeled "F1-10-5",
a mysterious part number that didn't show up in any databooks.
Since unidentifiable ICs are useless, he gave me one to analyze.
Conveniently, it was in a ceramic package, so I could open it up with a quick tap from a chisel.
Under the microscope, the chip's most striking feature was a grid of square capacitors. 
With all those capacitors, I guessed that it was a switched-capacitor filter.
The die provided another clue: the part number HF-10. With this information, we quickly
found that the chip was Harris's version of the standard MF10 switched-capacitor filter chip.
1
The Harris integrated circuit, labeled F1-10-5 (or maybe FI-10-5), with a 1985 date code. Photo courtesy of CuriousMarc.
Switched-capacitor filters were a popular way to implement analog filters in the 1980s.
Rapidly switching capacitors in and out of a circuit
enabled the construction of single-chip filters
that were easy to use and performed well.
The MF10, introduced by National Semiconductor in 1981, provides two flexible filters on a chip; each filter
acts as a low-pass filter, band-pass filter, or a high-pass filter.
The filter's characteristics are simple to control with a few external resistors.
The Harris HF-10 die under the microscope with the main functional blocks labeled. (Click for a larger image.)
Since I had the chip under the microscope, I took the opportunity to analyze it more closely.
The white lines are the metal wiring that connects the chip's circuitry. Under the metal
layer are two layers of polysilicon (reddish) and the underlying silicon (gray).
The top and bottom halves of the chip are mostly mirror images, corresponding to the
chip's two filters.
The distinctive reddish squares in the middle of the chip are 72 tiny capacitors,
constructed from polysilicon.
Above the capacitors, CMOS switches turn on and off at the clock frequency,
switching capacitors in and out of the circuit.
Each filter uses three operational  amplifiers (op amps), outlined in red.
At the right are the three outputs from the three op amps: high pass, band pass, and low pass.
The control circuitry is on the left: clock level shifting, clock shaping, frequency ratio
handling, startup circuitry, and current sinks to provide fixed currents to other parts of
the chip.
Around the edges of the silicon die, 20 hair-thin bond wires
connect the die to its 20 external pins.
The die has some interesting chip art: a Harris logo and an outline of Florida; Harris
was headquartered in Melbourne, Florida.
The initials on the die are presumably the engineers who designed the chip.
Some interesting images from the die.
Switched capacitor circuits
The filter is based on switched-capacitor circuits.
A switched capacitor can replace a resistor in certain circuits, as shown below.
The switches are controlled by a clock signal; the switches alternately close in clock phase 1 and phase 2 (ϕ1 and ϕ2).
In phase 1, the capacitor is charged to the input voltage. In phase 2, the capacitor
passes charge to the output.
By rapidly toggling the switches, charge is (almost) steadily passed to the output.
The larger the capacitance, the more charge that is passed through. Likewise, a higher
frequency passes more charge. 
It can be shown that the circuit matches a resistor with resistance of 1/(fC):
a higher capacitance and frequency correspond to lower resistance.
A switched capacitor can replace a resistor.
Why would you replace a simple resistor with this complicated switching circuit?
In an integrated circuit, resistors are inaccurate and inconveniently large, especially
high-value resistors.
Replacing a large resistor with a small capacitor saves space on the die.
Moreover, it is easy to generate an extremely accurate clock frequency with an inexpensive quartz crystal,
making the filter's frequency highly accurate.
Finally, the equivalent resistance can be changed simply by changing the clock frequency,
making it easy to tune or sweep the filter.
On-chip capacitors are fairly inaccurate, with the capacitance typically varying by 20%
from chip to chip due to variations in manufacturing conditions.
However, this isn't a problem in the MF10 because the circuitry was designed to depend
on the
ratio
between capacitances, which is stable.
Specifically, the MF10 uses 72 identical square capacitors, which will have almost
identical capacitances. 
Careful examination shows that some of the capacitors are separate, while others are connected in groups of 8 to form larger capacitors.
2
This yields a highly accurate ratio of 8:1 between the grouped capacitors and the individual
capacitors, even though the absolute capacitance will vary from chip to chip.
Each capacitor is constructed from two layers of polysilicon,
3
forming the plates of the capacitor,
separated by a thin layer of insulating oxide that acts as the dielectric.
I estimate that each capacitor square is 5 picofarads.
The grid of capacitors in the MF10. I've added yellow lines to show how the capacitors are grouped. The switches are above and below the capacitors.
This chip uses one more trick with switched capacitors: it inverts the voltage while
acting as a resistor.
In the switched-capacitor circuit below, there are four switches.
The capacitor charges to the input voltage during phase 1, the same as before.
But duing phase 2, note that the top plate of the capacitor is grounded, while the output
comes from the bottom plate.
If the capacitor was charged to, say, 1 volt, the top plate is 1 volt above the bottom plate.
So if the top plate is grounded, then the bottom plate must be at -1 V.
(This is the same idea as a
charge pump
.)
This circuit turns out to yield a more accurate filter because some parasitic capacitances
cancel out.
By using four switches, the switched capacitor can invert the voltage.
The op-amp integrator
The heart of most analog circuits is the operational amplifier, or op-amp.
An op-amp takes two inputs and amplifies the difference by many orders of magnitude.
Normally, an op-amp is configured with negative feedback, which forces the two inputs
to be essentially the same.
Op-amps are useful not only for amplification, but for filtering, buffering, summing, and
other tasks.
A basic op-amp integrator.
The filter chip uses op-amps as integrators, to integrate an input voltage over time.
The circuit above shows a simple op-amp integrator.
The input voltage produces a current that flows through the resistor and charges the capacitor, so the
capacitor holds the integral of the input voltage over time.
You might expect that the left side of the capacitor would become positive as it charges.
However, the op-amp's feedback forces both inputs to ground, so instead the right
side of the capacitor becomes negative. Thus, the output is the negative integral.
4
The MF10 chip uses the circuit above, except the resistor is replaced with a switched
capacitor. The capacitor across the op-amp is not switched, but consists of either 8 or 16
capacitors from the capacitor grid.
The CMOS switches
The CMOS switch is the technology that makes the switched-capacitor filter possible.
A CMOS switch has a fairly low resistance (maybe tens of ohms) when closed and an enormously
high resistance (hundreds of megohms) when open. This high resistance ensures that the
charge doesn't leak out of the capacitors.
A CMOS switch is constructed by combining an NMOS transistor and a PMOS transistor.
The NMOS transistor and PMOS transistor are opposites.
An NMOS transistor is good at pulling the output low, while a PMOS transistor is good
at pulling the output high, so in combination they provide an effective switch.
An NMOS transistor is turned on by a high voltage on the gate, while a PMOS transistor
is turned on by a low voltage on the gate. Thus, a CMOS switch requires two control signals
of opposite polarity, which is a minor inconvenience.
A CMOS switch.
The diagram above shows how a switch is implemented with an NMOS transistor and a PMOS
transistor in parallel. When the control line is high, and the inverted control line is low,
both transistors turn on, providing a path through the switch circuit. When the control line is low
(and the inverted line high), the transistors turn off, opening the switch.
The chip uses CMOS switches in pairs, with one switch on and the other off.
This forms the equivalent of a toggle switch that connects either A or B to the output.
This circuit is simply two CMOS switches, with separate control lines for each switch,
as shown below.
In the MF10, the switch toggles at the clock frequency.
During one clock phase, the switch is connected to A, while the switch is connected to B
during the other clock phase.
The schematic on the right, below, is the same circuit, but reorganized to match the
layout on the die.
A double-throw CMOS switch.
The photo below shows a CMOS switch on the die, constructed from two PMOS transistors and
two NMOS transistors.
The four control lines run horizontally in polysilicon, forming a transistor gate where they
cross doped silicon.
The upper PMOS and NMOS transistors are driven by the clock phase 1 (Φ1) signals, while the
lower transistors are driven by the phase 2 signals.
CMOS switches on the die. The metal layer was removed to show the transistors.
One problem with switched-capacitor filters is that the clock can generate switching noise
that appears in the chip's outputs. The MF10 uses several techniques to reduce clock noise.
Each set of transistors is surrounded by two isolation rings: one positive and one negative. These block noise from
traveling through the silicon substrate.
Note that the rings have opposite polarity for the NMOS transistors and the PMOS transistors.
The light tan region in the photo above is a second layer of polysilicon. This polysilicon is
connected to ground, providing a shield layer over the switching circuits.
For the photo above, I removed the metal layer with acid
5
to make the transistors more visible.
The photo below shows the original die, with the metal layer connecting the transistors.
The small black circles are connections between the metal layer and silicon or polysilicon.
The same CMOS switches, showing the metal layer.
Putting it together: the state variable filter
There are many ways of creating a filter.
The MF10 chip uses a technique called the state variable filter,
invented
in 1967.
This circuit acts as three filters, with high-pass, band-pass, and low-pass outputs.
Moreover, the circuit is flexible since the frequency, the gain, and the filter quality (Q)
can be varied independently.
It uses three op-amps: one to sum signals and two for integration.
By changing how the values are summed, the characteristics of the filters can be changed.
The diagram below shows a simplified representation of a state variable filter.
The mathematics behind a state variable filter is complicated, so I won't get into it.
In short, the signal, the integral, and the double integral form the three state variables
that define the state of the system.
The block diagram below shows how the filter is represented in the MF10 datasheet.
6
The diagram is similar to the diagram above, with three op-amps.
However, the summing circuitry has been separated out.
Moreover, the feedback paths are not shown explictly.
Instead, resistors are connected between the chip's external pins (squares) to configure
the filter as desired.
The mode switch at the top allows the low-pass feedback to be controlled by an external pin
(S
A/B
).
Block diagram of one of the filter sections. Adapted from
the datasheet
.
The schematic below is my reverse-engineered schematic of the filter, as implemented on the chip.
It closely matches the block diagram, but fills in the details.
In the block diagram, the summing circuit (circle) adds one signal and subtracts two signals.
This summing circuit is implemented with the three switched capacitors on the left,
which act as summing resistors.
Note that one switch is grounded during phase 1, while the others are grounded during phase 2;
switching the polarity implements addition versus subtraction.
The top sum input is either feedback from the low-pass output or ground, selected by an
input pin. 
A CMOS switch is used here, but the switch is static, not clocked, so it doesn't use protection rings and shielding like the other switches.
My reverse-engineered schematic of one of the filters. Click this image (or any other) for a larger version.
The integrators have switched capacitors on the inputs, acting as resistors.
The integration capacitor is either 8 or 16 "squares" of capacitance, selected by a ratio selection pin.
This controls the ratio between the clock frequency and the filter frequency,
either 50:1 or 100:1.
7
Although the integration capacitors are attached to a CMOS switch, the switch is static, so
the capacitors act as regular capacitors, not switched capacitors.
The op-amps
The op-amps are fairly standard CMOS op-amps, built from about 35 transistors.
(You might get a lower count if you try counting the transistors below, since some of the blocks are multiple transistors.)
The op-amp transistors are much larger than the CMOS switch transistors (very bottom, center).
On the die, each op-amp is split into two parts: the differential amplifier on the
left and an additional amplification stage on the right. A large capacitor (pinkish) sits between
the halves. My first thought was that this was the integration capacitor, but it is
just a frequency compensation capacitor, common in many op-amps to stabilize the output.
The op-amps also have large transistors next to the output pins;
these transistors are functionally part of the op-amps, but
located next to the pins to minimize resistance.
One of the chip's op-amps. I removed the metal layer to make the transistors visible.
One unusual feature of the op-amps is a low-power mode.
Pulling a particular IC pin low causes the chip to stop filtering and enter a low-power mode,
reducing power consumption by 70%.
This is implemented by shutting down the "current mirror" circuits that provide fixed
currents to the op-amps and other parts of the chip.
The non-overlapping clock generator
The MF10 chip is driven by external clock signals, one for each filter,
with the frequency of the filter proportional to the clock frequency.
The photo of the CMOS switches earlier showed that the clock drives four control lines for the switches.
You might think that two control lines would be sufficient: the clock and the inverted clock.
The problem is that it is very important to avoid having both switches closed at the same time,
even for
a moment, as that will short the inputs and corrupt the signals.
Instead, the two switches have separate control lines that enforce a small gap
between when one switch opens and the other one closes.
This is implemented with the circuit below that
takes an input clock signal and produces the four outputs that drive the switches.
The circuit to generate non-overlapping clock signals. There is a delay between when gate A or B turns on and when the corresponding output changes.
The idea behind the circuit is that a phase is blocked from going high until after the other
phase goes low, with a pair of inverters providing additional delay.
In more detail, suppose the input clock drops from high to low.
Gate A will turn off, causing the phase 1 output (ϕ1) to drop after a few gate delays
(A delay). Gate B can't turn on until ϕ1 goes low. After additional gate delays, ϕ2
goes high.
The behavior is similar when the input clock goes high. Gate B turns off, causing
ϕ2 to go low after a delay. This allows gate A to turn on, turning on ϕ1 after more delay.
To summarize, after a phase is turned off, there is a delay before the other phase turns on,
so the two phases never overlap.
The clock-shaping circuitry is implemented with CMOS logic gates.
The photo above shows this circuitry under the microscope, with the metal layer removed.
The rectangular blocks are doped silicon that forms transistors.
The darker regions on the left are NMOS transistors and the lighter regions on the right
are PMOS transistors. A CMOS gate consists of NMOS and PMOS transistors working together.
The PMOS transistors are larger because PMOS transistors are slightly less efficient than
NMOS transistors.
The dark circles are contacts between the silicon and the metal layer on top.
The copper-colored lines are not metal but a special type of silicon called polysilicon.
When a polysilicon line crosses doped silicon, it forms the gate of a transistor. 
The pinks and greens are due to thin-film interference from a thin layer of oxide that
didn't completely dissolve; the silicon is actually gray.
The ternary input
A weird feature of the chip is the input pin that selects the ratio between the
input clock and the filter frequency.
In effect, this is a digital input with
three
values.
Tying the pin to the high supply voltage selects a 50:1 ratio. Tying the pin to the
midpoint between the supply voltages selects
a 100:1 ratio.
Pulling the pin to the low supply voltage stops the filter and puts the chip into a low-power
mode.
8
To handle the three-level input, the input goes through two separate buffers, one that
transitions at a lower voltage and one that transitions at a higher voltage.
Thus, the two buffers separate the middle signal level.
Each buffer consists of a special inverter feeding into a regular inverter.
Before explaining the special inverters, I'll review how a regular CMOS inverter works.
A CMOS inverter is constructed from a PMOS transistor and an NMOS transistor. When the input
is high, the NMOS transistor turns on and pulls the output to ground. When the input is low,
the PMOS transistor turns on and pulls the output high. Thus, the input signal is inverted.
A CMOS inverter is constructed from a PMOS transistor and an NMOS transistor.
In the die photo, you can see the four PMOS transistors (light gray) and four NMOS transistors
(darker), forming four inverters.
When a polysilicon line (copper-colored) crosses a doped silicon region, it forms the gate
of a transistor.
For this picture, I dissolved the metal layer in acid so the transistors are visible.
The metal layer connected the transistors to complete the wiring of the inverters: it connects the two "out1" contacts to "in2" and connects the two "out2"
contacts to the rest of the chip. For the second buffer, "out3" connects to "in4" and so forth.
The four inverters that handle the ternary input. I flipped the image to make the orientation better.
In this circuit, the length of the transistor gates is varied to make the inverters
activate at different voltage levels.
Six of the transistor gates are normal (orange arrows); the PMOS gates are wider
(in the vertical direction) than the NMOS gates
because PMOS transistors are inherently weaker.
However, two of the transistor gates are unusually long (horizontal direction, red), making the transistors weak since the current must travel a longer distance.
The inverter on the left has a weak PMOS transistor. If the input is high or low, the
inverter will operate normally. But if the input is in the middle, both transistors will
partially turn on. Since the PMOS transistor is very weak, the NMOS transistor will "win", pulling
the output low.
Thus, the leftmost
inverter treats a medium-level input as a 1, outputting a 0.
The third inverter is the opposite; the NMOS transistor has a long, winding gate, so it
is weak. In this case, a medium-level input will partially turn on both transistors, but
the PMOS transistor will "win", pulling the output high.
To summarize, the two inverters have opposite behavior for a middle-level signal, allowing
the three input levels to be distinguished.
Since the output from a special inverter may be weak, the output goes to a normal inverter
to amplify the signal.
Conclusions
Like most semiconductor companies, Harris has a complicated history.
Harris started way back in 1895 as a printing press company.
Harris moved into high technology in the 1950s and 1960s, acquiring various radio and electronics companies.
In particular, Harris entered the IC business in 1967, when it acquired
Radiation, Inc.
,
renaming it Harris Semiconductor a few years later. (We've encountered some
Radiation modules in Apollo systems, but I haven't written about them yet.)
Harris got out of the semiconductor business in 1999, spinning off Intersil, which was
later acquired by the Japanese semiconductor firm Renesas.
In 2019, Harris merged with L3 Technologies to
become L3Harris, the eighth-largest defense contractor in the US.
As for switched-capacitor filters, they have lost popularity as filtering is now more
easily done in the digital domain.
Texas Instruments acquired National Semiconductor (and the MF10) in 2011;
TI's
website
shows the MF10 as active but expensive and out of stock, so it's probably
no longer being manufactured.
State variable filters are still
used in the synthesizer world
both because of their
flexibility and because they provide low-pass, band-pass, and high-pass filters in one unit.
For more, follow me on
Bluesky (
@righto.com
),
Mastodon (
@
[email protected]
),
or
RSS
.
Thanks to CuriousMarc for providing the IC.
AI statement: Despite the presence of the em dash, no AI was used in the writing of this article (
details
).
Notes and references
