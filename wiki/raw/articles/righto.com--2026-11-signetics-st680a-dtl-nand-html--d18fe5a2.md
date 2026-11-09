---
title: "Reverse engineering a vintage diode-transistor logic chip"
url: "http://www.righto.com/2026/11/signetics-st680a-dtl-nand.html"
fetched_at: 2026-11-09T10:11:02.413287+00:00
source: "righto.com"
tags: [blog, raw]
---

# Reverse engineering a vintage diode-transistor logic chip

Source: http://www.righto.com/2026/11/signetics-st680a-dtl-nand.html

Going through a collection of old parts, CuriousMarc encountered some ICs that he couldn't
identify.
He opened up one of these ICs, and I studied it under the microscope.
After some reverse engineering, I determined that it was a logic chip that implemented four NAND gates
using old-fashioned diode-transistor logic (DTL).
1
The chip turned out to be the ST680A, a member of the Signetics 600 series of chips from 1965.
In this article, I discuss the circuitry in this chip and how diode-transistor logic works.
The die of the ST680A under the microscope.
Integrated circuits can be packaged in many ways. One of the most popular is the
plastic DIP (Dual In-line Package), a black rectangle of epoxy with two rows of metal
pins.
This type of package was
invented
by Signetics: "Introduced in late 1965, the 600 series was the first integrated circuit family to be offered in a solid, plastic, dual in-line package (DIP)."
Earlier integrated circuits were packaged in round metal cans or in small flat-packs.
In 1965, engineers at Fairchild invented the DIP, which had two
rows of pins on 0.1" spacing.
Unlike the surface-mounted flat-pack, the DIP had pins that were inserted into holes, making
manual or automated assembly quick and easy.
Because the pins of a DIP were on a regular grid, rather than the circular pattern of a metal
can, circuit board design and manufacturing were also easier
(
details
).
The first DIP chips had ceramic packages.
The plastic DIP, introduced by Signetics, was much cheaper and became very popular.
An advertisement for the Signetics 600 series. From
Electronics
, March 21, 1966.
The plastic DIP is less popular with me, however, because it is harder to open.
With a ceramic package, I can simply tap it with a chisel and pop it open, but
that doesn't work with epoxy packages.
An epoxy package can be dissolved with nitric or sulfuric acid, but I try to avoid dangerous acids.
Instead, CuriousMarc used
Antoine's hot air
decapping method.
Unfortunately, the hot air technique doesn't always work. In this case, tiny bits of epoxy
were stuck to the die, obscuring the circuitry.
I used a few drops of boiling sulfuric acid to clean the die.
(I'm okay with sulfuric
acid in tiny quantities.)
The die on its metal frame.
The photo above shows the silicon die
on its metal frame, the lead frame.
The golden blobs are where
the bond wires were attached to the die.
You can see the doped silicon regions that form diodes and bipolar NPN transistors,
as well as 16 resistors in the center, forming serpentine paths.
Most chips have a passivation layer—a thin layer of silicon dioxide—over the chip.
Inconveniently, this old chip didn't have a passivation layer, so the acid also stripped off
the metal layer. (A few remnants are visible in the upper left.)
Without the metal layer, I had to guess at how the components were connected to
form logic gates.
The die has very faint color differences where the silicon was protected by the metal,
so that helped.
Eventually, I came up with the diagram below, showing how the metal
layer was probably configured.
This wiring reveals that the chip implements four DTL NAND gates, which I'll describe
in more detail below.
One puzzle was that the chip has two unused diodes, indicated with question marks below.
The metal layer for a quad NAND chip. I desaturated the image to make the labels clearer.
Transistors, diodes, and resistors
In this section, I'll explain how the patterns in the image correspond to components
of the circuit.
The silicon die is doped with various impurities to form regions with different
electrical characteristics.
These regions appear red or green under the microscope due to thin-film effects.
As a result, 
the chip's transistors, diodes, and resistors are visible.
The chip is made from bipolar NPN transistors, which have a completely different
construction from the MOS transistors in modern ICs.
In an NPN transistor, the current from the collector to the emitter is controlled
by the current through the base.
The collector is a large region of N-type silicon, silicon that is doped with
atoms such as phosphorus or arsenic. 
Since these elements have one more valence electron than silicon, they give the
silicon more negative charge carriers, so it is called N for negative.
The N-type silicon happens to appear reddish.
On top of the collector, the base is a thin region of P-type silicon, which appears green.
This silicon has been doped with atoms such as boron or gallium, which have 
one fewer valence electron than silicon. The missing electrons form "holes", which
act as positive charge carriers.
Finally, the emitter is N-type silicon, on top of the base layer.
These layers work together through semiconductor magic, amplifying the base current.
Two NPN transistors on the chip. The second transistor is a larger output transistor.
The chip's output transistors are slightly larger so they can sink more current.
In the transistor on the right above, note that the collector contact wraps around three sides of
the transistor. 
The emitter is also larger, with an L-shaped contact.
According to the datasheet, each output transistor can sink 2.5 mA of current.
The chip uses many diodes since it is diode-transistor logic. 
The structure of a diode is similar to a transistor, but without the emitter.
In a diode, current flows from the cathode (P-type silicon) to the anode (N-type).
A diode and a resistor on the chip.
The chip uses 16 resistors, located in the middle of the die.
A resistor is constructed from a long, thin region of doped silicon.
Since silicon has moderately high resistance, a long strip of silicon acts
as a resistor.
Most of the resistors have a serpentine layout to fit a long resistor into a smaller area.
These resistors consist of P-type silicon (green) in a "tub" of N-type silicon (red).
The tub is connected to the positive voltage supply; since current doesn't flow from
N-type silicon to P-type silicon, this isolates the resistors from each other.
Operation of a DTL gate
Logic gates can be created in many ways.
The earliest integrated circuits (such as the ones in the Apollo Guidance Computer)
used Resistor-Transistor Logic (RTL), where logic gates were constructed from resistors
and transistors.
In March 1962, Signetics announced the first family of commercial Diode-Transistor Logic
(DTL) integrated circuits (
details
).
By using diodes on the inputs instead of resistors, DTL provided better performance than
RTL. 
However, DTL soon became overshadowed by TTL (Transistor-Transistor Logic), which
was faster and used less power. (If you built digital circuits a few decades ago, you're
probably familiar with the popular 7400 series of TTL chips.)
The diagram below shows how the DTL NAND gate works.
If both inputs are high, the current from the first resistor flows through the
base of the first transistor, turning it on.
The transistor amplifies this current, passing a much larger current from the
transistor's collector to the transistor's emitter.
This current goes through the base of the second transistor, which turns on the
second transistor.
The second transistor passes an even larger current from the output pin to ground,
pulling the output pin low.
The DTL NAND gate with both inputs high. The schematic is from the datasheet.
This circuit is considerably more complicated than the DTL gate on
Wikipedia
.
But if one of the input pins is pulled low, the current from the resistor goes through
the diode instead of the transistor.
The first transistor turns off, and without a base current, the second transistor turns off.
The third resistor pulls the output high.
Thus, the output is low only if both inputs are high: a NAND gate.
The DTL NAND gate with an input low.
I'll point out a few features of this circuit.
The diodes on the inputs ensure that one input doesn't affect the other input.
The diode in the middle raises the voltage on the first transistor's emitter, so it
requires more voltage to turn on, reducing the sensitivity to noise.
The output uses a resistor to pull the output high; more advanced circuits use another
transistor.
When the output is low, the third resistor is still "trying" to pull the output high,
which is wasting power.
Moreover, the resistor limits the output current, so the high output is fairly weak.
In some DTL families, you can get gates with different values for the output resistor,
so you can select the tradeoff between wasting power and having an output that is too weak.
If you've used TTL integrated circuits from the 1970s, you know that chips usually have power
and ground on diagonal pins: ground on pin 7 and power on pin 14.
(Putting power and ground diagonally opposite both helps die layout and circuit board layout.)
Much to my surprise, I found that the Signetics chips predate this standard and have
ground on pin 1 and power on pin 8: still diagonal, but the wrong diagonal!
The diagram below shows how the four NAND gates are wired in the chip.
Pinout of the 680A quad NAND gate. From the
databook
.
Three chips from one die
When I examined the die under the microscope, I figured out the circuit, but I was puzzled
by two extra diodes, as if two NAND gates had a third input that wasn't used.
The explanation is that Signetics used the same silicon layout for at least three different
chips, applying a different metal layer for different functionality.
This saved money since it's much cheaper to produce a single optical mask for the metal layer
than a complete set of new masks.
Signetics sold semi-custom ICs to customers, using an approach called variFEBS (Variable
Functional Electronics Blocks). This approach used a custom metal layer on top of
fixed silicon, providing custom circuits without the cost of a full mask set.
These circuits didn't sell well, but Signetics used the same approach for standard ICs.
Pinout of the 670A triple NAND gate and the 616A quad NAND gate. All three chips have some similarities, such as using pins 2 and 14 as outputs. From the
databook
.
One IC with the same silicon as the quad NAND gate is the 670A chip, which
has three NAND gates, each with three inputs (above left).
The diagram below shows how the silicon can be wired to provide this functionality.
The hypothesized metal layer for the 670A triple-NAND gate.
The layout for the triple chip above is a bit tricky because the top gate has inputs on
both sides of the power (Vcc) pin.
This creates a layout problem because the power and ground metal runs vertically to the
resistors, blocking metal wiring from one side to the other.
The solution is a "crossunder", a region of silicon that allows a signal to pass under
the metal layer, connecting the inputs on the left to the rest of the circuitry on the right.
This crossunder is visible near the top of the chip.
Another chip with the same layout is the 616A dual NAND gate, with five inputs on each gate.
Since this chip has 10 inputs in total (compared to 8 on the quad gate), this chip
uses the two "extra" diodes that I spotted.
If that isn't enough inputs, each NAND gate has an expansion input; by connecting external
diodes to the expansion input, the gate can be made as large as desired.
The hypothesized metal layer for the 616A dual-NAND chip.
Some history
The history of Signetics is closely tied to Fairchild.
The story of Fairchild's founding is well known: in 1957, eight
engineers—the Traitorous Eight—left Shockley Semiconductor and created
Fairchild Semiconductor.
Hundreds of companies (the "Fairchildren") were started by engineers who left
Fairchild.
Signetics was one of those companies, formed in 1961 and
said
to be the first company to exclusively design and manufacture integrated circuits.
2
Signetics announced its first product in 1962, a NAND gate that cost $125 (over $1000 in
current dollars).
3
Not surprisingly, sales were weak.
Signetics soon ran short of money, so in 1962, Corning Glass invested $1.7 million for 51%
ownership of Signetics.
Corning Glass may seem like a strange investor, but Corning was more of a high-tech
company than you'd expect, making components such as resistors and
glass capacitors
, and later creating fiber optics.
Moreover, in the early 1960s, integrated circuits were the hot area (much like AI now),
and everyone wanted to get involved.
In 1963, the Department of Defense pushed for contractors to use integrated circuits
in new products.
Riding this wave, Signetics became the leading producer of integrated circuits.
4
However, Fairchild soon introduced a series of DTL chips that competed with Signetics. The
Fairchild 930 series was faster than the Signetics chips and less than half the price,
so Fairchild took much of the market from Signetics and dominated the IC market.
Signetics also produced analog integrated circuits.
Signetics is probably best known for creating the
555 timer chip
in 1970, said to be
the world's most popular IC, with billions sold.
5
Signetics was acquired by Philips in 1975, and then Philips Semiconductors was spun
off as NXP (Next exPerience) in 2006. NXP is currently the #10 semiconductor manufacturer
worldwide, so the heritage of Signetics lives on.
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
Thanks to CuriousMarc for providing the IC and thanks to TubeTime for finding the databook.
AI statement: Despite the presence of the em dash, no AI was used in the writing of this article (
details
).
Notes and references
