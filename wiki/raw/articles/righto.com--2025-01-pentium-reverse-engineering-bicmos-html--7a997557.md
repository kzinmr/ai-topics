---
title: "Interesting BiCMOS circuits in the Pentium, reverse-engineered"
url: "http://www.righto.com/2025/01/pentium-reverse-engineering-bicmos.html"
fetched_at: 2026-05-01T07:01:17.576812+00:00
source: "righto.com"
tags: [blog, raw]
---

# Interesting BiCMOS circuits in the Pentium, reverse-engineered

Source: http://www.righto.com/2025/01/pentium-reverse-engineering-bicmos.html

Intel released the powerful Pentium processor in 1993, establishing a long-running brand of processors.
Earlier, I
wrote
about the
ROM in the Pentium's floating point unit that holds constants such as π.
In this post, I'll look at some interesting circuits associated with this ROM.
In particular, the circuitry is implemented in BiCMOS, a process that combines bipolar transistors with
standard CMOS logic.
The photo below shows the Pentium's thumbnail-sized silicon die under a microscope.
I've labeled the main functional blocks; the floating point unit is in the lower right with the
constant ROM highlighted at the bottom.
The various parts of the floating point unit form horizontal stripes.
Data buses run vertically through the
floating point unit, moving values around the unit.
Die photo of the Intel Pentium processor with the floating point constant ROM highlighted in red. Click this image (or any other) for a larger version.
The diagram below shows how the circuitry in this post forms part of the Pentium.
Zooming in to the bottom of the chip shows the constant ROM, holding 86-bit words:
at the left,  the exponent section provides 18 bits. At the right, the wider significand section provides 68 bits.
Below that, the diagram zooms in on the subject of this article: one of the 86 identical multiplexer/driver circuits that provides the output from the ROM.
As you can see, this circuit is a microscopic speck in the chip.
Zooming in on the constant ROM's driver circuits at the top of the ROM.
The layers
In this section, I'll show how the Pentium is constructed from layers.
The bottom layer of the chip consists of transistors fabricated on the silicon die.
Regions of silicon are doped with impurities to change the electrical properties; these regions appear
pinkish in the photo below, compared to the grayish undoped silicon.
Thin polysilicon wiring is formed on top of the silicon. Where a polysilicon line crosses doped silicon, a transistor is
formed; the polysilicon creates the transistor's gate.
Most of these transistors are NMOS and PMOS transistors, but there is a bipolar transistor near the upper right,
the large box-like structure.
The dark circles are contacts, regions where the metal layer above is connected to the polysilicon or silicon to
wire the circuits together.
The polysilicon and silicon layers form the Pentium's transistors. This photo shows part of the complete circuit.
The Pentium has three layers of metal wiring. The photo below shows the bottom layer, called M1. 
For the most part, this layer of metal connects the transistors into various circuits, providing wiring over
a short distance.
The photos in this section show the same region of the chip, so you can match up features between the photos.
For instance, the contacts below (black circles) match the black circles above, showing how this metal
layer connects to the silicon and polysilicon circuits.
You can see some of the silicon and polysilicon in this image, but most of it is hidden by the metal.
The Pentium's M1 metal layer is the bottom metal layer.
The M2 metal layer (below) sits above the M1 wiring. 
In this part of the chip, the M2 wires are horizontal.
The thicker lines are power and ground.
(Because they are thicker, they have lower resistance and can provide the
necessary current to the underlying circuitry.)
The thinner lines are control signals.
The floating point unit is structured so functional blocks are horizontal, while data is transmitted vertically.
Thus, a horizontal wire can supply a control signal to all the bits in a functional block.
The Pentium's M2 layer.
The M3 layer is the top metal layer in the Pentium. It is thicker, so it is better suited for the chip's main
power and ground lines as well as long-distance bus wiring.
In the photo below, the wide line on the left provides power, while the wide line on the right provides ground.
The power and ground are distributed through wiring in the M2 and M1 layers until they are connected to the
underlying transistors.
At the top of the photo, vertical bus lines are visible; these extend for long distances through the floating
point unit.
Notice the slightly longer line, fourth from the right. This line provides one bit of data from the ROM, provided
by the circuitry described below.
The dot near the bottom is a via, connecting this line to a short wire in M2, connected to a wire in M1,
connected to the silicon of the output transistors.
The Pentium's M3 metal layer. Lower layers are visible, but blurry due to the insulating oxide layers.
The circuits for the ROM's output
The simplified schematic below shows the circuit that I reverse-engineered.
This circuit is repeated 86 times, once for each bit in the ROM's word.
You might expect the ROM to provide a single 86-bit word. However, to make the layout work better, the
ROM provides eight words in parallel. Thus, the circuitry must select one of the eight words with a multiplexer.
In particular, each of the 86 circuits has an 8-to-1 multiplexer to select one bit out of the eight.
This bit is then stored in a latch.
Finally, a high-current driver amplifies the signal so it can be sent through a bus, traveling to a destination halfway across the floating
point unit.
A high-level schematic of the circuit.
I'll provide a quick review of MOS transistors before I explain the circuitry in detail.
CMOS circuitry uses two types of transistors—PMOS and NMOS—which are similar but also opposites.
A PMOS transistor is turned on by a
low
signal on the gate, while an NMOS transistor is turned on by a
high
signal on the gate; the PMOS symbol has an inversion bubble on the gate.
A PMOS transistor works best when pulling its output
high
, while an NMOS transistor works best when pulling
its output
low
.
CMOS circuitry normally uses the two types of MOS transistors in a Complementary fashion to implement logic gates, working together.
What makes the circuits below interesting is that they often use NMOS and PMOS transistors independently.
The symbol for a PMOS transistor and an NMOS transistor.
The detailed schematic below shows the circuitry at the transistor and inverter level.
I'll go through each of the components in the remainder of this post.
A detailed schematic of the circuit. Click for a larger version.
The ROM is constructed as a grid: at each grid point, the ROM can have a transistor for a 0 bit, or no transistor
for a 1 bit. Thus, the data is represented by the transistor pattern.
The ROM holds 304 constants so there are 304 potential transistors associated with each bit
of the output word.
These transistors are organized in a 38×8 grid. To select a word from the ROM, a select line activates
one group of eight potential transistors.
Each transistor is connected to ground, so the transistor (if present) will pull the associated line low, for a 0 bit.
Note that the ROM itself consists of only NMOS transistors, making it half the size of a truly CMOS implementation.
For more information on the structure and contents of the ROM, see my
earlier article
.
The ROM grid and multiplexer.
A ROM transistor can pull a line low for a 0 bit, but how does the line get pulled high for a 1 bit?
This is accomplished by a precharge transistor on each line. Before a read from the ROM, the precharge
transistors are all activated, pulling the lines high.
If a ROM transistor is present on the line, the line will next be pulled low, but otherwise it will remain high
due to the capacitance on the line.
Next, the multiplexer above selects one of the 8 lines, depending on which word is being accessed.
The multiplexer consists of eight transistors. One transistor is activated by a select line, allowing the ROM's
signal to pass through. The other seven transistors are in the off state, blocking those ROM signals.
Thus, the multiplexer selects one of the 8 bits from the ROM.
The circuit below is the "keeper."
As explained above, each ROM line is charged high before reading the ROM. However, this charge can fade away.
The job of the keeper is to keep the multiplexer's output high until it is pulled low.
This is implemented by an inverter connected to a PMOS transistor.
If the signal on the line is high, the PMOS transistor will turn on, pulling the line high.
(Note that a PMOS transistor is turned on by a low signal, thus the inverter.)
If the ROM pulls the line low, the transistor will turn off and stop pulling the line high.
This transistor is very weak, so it is easily overpowered by the signal from the ROM.
The transistor on the left ensures that the line is high at the start of the cycle.
The keeper circuit.
The diagram below shows the transistors for the keeper. The two transistors on the left implement a standard
CMOS inverter. 
On the right, note the weak transistor that holds the line high.
You might notice that the weak transistor looks larger and wonder why that makes the transistor weak rather than
strong.
The explanation is that the transistor is large in the "wrong" dimension.
The current capacity of an MOS transistor is proportional to the width/length ratio of its gate.
(Width is usually the long dimension and length is usually the skinny dimension.)
The weak transistor's length is much larger than the other transistors, so the W/L ratio is smaller and the transistor is weaker.
(You can think of the transistor's gate as a bridge between its two sides. A wide bridge with many lanes lets
lots of traffic through. However, a long, single-lane bridge will slow down the traffic.)
The silicon implementation of the keeper.
Next, we come to the latch, which remembers the value read from the ROM.
This latch will read its input when the load signal is high. When the load signal
goes low, the latch will hold its value.
Conceptually, the latch is implemented with the circuit below.
A multiplexer selects the lower input when the load signal is active, passing the latch input through to the (inverted) output.
But when the load signal goes low, the multiplexer will select the top input, which is feedback of the value in the latch.
This signal will cycle through the inverters and the multiplexer, holding the value until a new value is loaded.
The inverters are required because the multiplexer itself doesn't provide any amplification; the signal would
rapidly die out if not amplified by the inverters.
The implementation of the latch.
The multiplexer is implemented with two CMOS switches, one to select each multiplexer input.
Each switch is a pair of PMOS and NMOS transistors
that turn on together, allowing a signal to pass through. (See the bottom two transistors below.)
1
The upper circuit is trickier. Conceptually, it is an inverter feeding into the multiplexer's CMOS
switch. However, the order is switched so the switch feeds into the inverter. The result is not-exactly-a-switch
and not-exactly-an-inverter, but the result is the same.
You can also view it as an inverter with power and ground that gets cut off when not selected.
I suspect this implementation uses slightly less power than the straightforward implementation.
The detailed schematic of the latch.
The most unusual circuit is the BiCMOS driver.
By adding a few extra processing steps to the regular CMOS manufacturing process, bipolar (NPN and PNP) transistors can be created.
The Pentium extensively used BiCMOS circuits since they reduced signal delays by up to 35%.
Intel also used BiCMOS for the Pentium Pro, Pentium II, Pentium III, and Xeon processors.
However, as chip voltages dropped, the benefit from bipolar transistors dropped too and BiCMOS was eventually abandoned.
The BiCMOS driver circuit.
In the Pentium, BiCMOS drivers are used when signals must travel a long distance across the chip.
(In this case, the ROM output travels about halfway up the floating point unit.)
These long wires have a lot of capacitance so a high-current driver circuit is needed and the NPN transistor
provides extra "oomph."
The diagram below shows how the driver is implemented. The NPN transistor is the large boxy structure in the
upper right. 
When the base (B) is pulled high, current flows from the collector (C), pulling the emitter (E) high and thus
rapidly pulling the output high.
The remainder of the circuit consists of three inverters, each composed of PMOS and NMOS transistors.
When a polysilicon line crosses doped silicon, it creates a transistor gate, so each crossing corresponds to
a transistor. 
The inverters use multiple transistors in parallel to provide more current; the transistor sources and/or drains overlap
to make the circuitry more compact.
This diagram shows the silicon and polysilicon for the driver circuit.
One interesting thing about this circuit is that each inverter is carefully designed to provide the desired current,
with a different current for a high output versus a low output.
The first inverter (purple boxes) has two PMOS transistors and two NMOS transistors, so it is a regular inverter,
balanced for high and low outputs. (This inverter is conceptually part of the latch.)
The second inverter (yellow boxes) has three large PMOS transistors and one smaller NMOS transistor, so it has
more ability to pull the output high than low.
This transistor turns on the NPN transistor by providing a high signal to the base, so it needs more current
in the high state.
The third inverter (green boxes) has one weak PMOS transistor and seven NMOS transistors, so it can pull its
output low strongly, but can barely pull its output high. 
This transistor pulls the ROM output line low, so it needs enough current to drive the entire bus line.
But this transistor doesn't need to pull the output high—that's the job of the NPN transistor—so the PMOS transistor can be weak.
The construction of the weak transistor is similar to the keeper's weak transistor; its gate length is much larger than the other
transistors, so it provides less current.
Conclusions
The diagram below shows how the functional blocks are arranged in the complete circuit, from the ROM at the bottom to the
output at the top.
The floating point unit is constructed with a constant width for each bit—38.5 µm—so the circuitry is
designed to fit into this width.
The layout of this circuitry was hand-optimized to fit as tightly as possible, 
In comparison, much of the Pentium's circuitry was arranged by software using a
standard-cell approach
, which is
much easier to design but not as dense. Since each bit in the floating point unit is repeated many times, hand-optimization
paid off here.
The silicon and polysilicon of the circuit, showing the functional blocks.
This circuit contains 47 transistors. Since it is duplicated once for each bit, it has 4042 transistors in total,
a tiny fraction of the Pentium's 3.1 million transistors.
In comparison, the MOS 6502 processor has about 3500-4500 transistors, depending on how you count.
In other words, the circuit to select a word from the Pentium's ROM is about as complex as the entire 6502 processor.
This illustrates the dramatic growth in processor complexity described by Moore's law.
I plan to write more about the Pentium so follow me on Bluesky (
@righto.com
) or
RSS
for updates. (I'm no longer on Twitter.)
You might enjoy reading about the
Pentium Navajo rug
.
Notes
