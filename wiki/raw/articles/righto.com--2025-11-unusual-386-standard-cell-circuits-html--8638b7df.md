---
title: "Unusual circuits in the Intel 386's standard cell logic"
url: "http://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html"
fetched_at: 2026-04-30T07:01:06.987639+00:00
source: "righto.com"
tags: [blog, raw]
---

# Unusual circuits in the Intel 386's standard cell logic

Source: http://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html

I've been studying the standard cell circuitry in the Intel 386 processor recently.
The 386, introduced in 1985, was Intel's most complex processor at the time, containing 285,000 transistors.
Intel's existing design techniques couldn't handle this complexity and the chip began to fall behind schedule.
To meet the schedule, the 386 team started using a technique called standard cell logic.
Instead of laying out each transistor manually, the layout process was performed by a computer.
The idea behind standard cell logic is to create standardized circuits (standard cells) for each type of logic element, such
as an inverter, NAND gate, or latch.
You feed your circuit description into software that selects the necessary cells, 
positions these cells into columns, and then routes the wiring between the cells.
This "automatic place and route" process creates the chip layout much faster than manual layout.
However, switching to standard cells was a risky decision since if the software couldn't create a
dense enough layout, the chip couldn't be manufactured.
But in the end, the 386 finished ahead of schedule, an almost unheard-of accomplishment.
1
The 386's standard cell circuitry contains a few circuits that I didn't expect.
In this blog post, I'll take a quick look at some of these circuits:
surprisingly large multiplexers, a transistor that doesn't fit into the standard cell layout,
and inverters that turned out not to be inverters.
(If you want more background on standard cells in the 386, see my earlier post,
"
Reverse engineering standard cell logic in the Intel 386 processor
".)
The photo below shows the 386 die with the automatic-place-and-route regions highlighted; I'm focusing
on the red region in the lower right.
These blocks of logic have cells arranged in rows, giving them a characteristic striped appearance.
The dark stripes are the transistors that make up the logic gates, while the lighter regions between the stripes are the
"routing channels" that hold the wiring that connects the cells.
In comparison,
functional blocks
such as the datapath on the left
and the microcode ROM in the lower right
were designed manually to optimize density and performance, giving them a more solid appearance.
The 386 die with the standard-cell regions highlighted.
As for other features on the chip,
the black circles around the border are bond wire connections that go to the chip's external pins.
The chip has two metal layers, a small number by modern
standards, but a jump from the single metal layer of earlier processors such as the 286.
(Providing two layers of metal made automated routing practical: one layer can hold horizontal wires while the other layer
can hold vertical wires.)
The metal appears white in larger areas, but
purplish where circuitry underneath roughens its surface.
The underlying silicon and the polysilicon wiring are obscured by the metal layers.
The giant multiplexers
The standard cell circuitry that I'm examining (red box above) is part of the control logic that selects registers
while executing an instruction.
You might think that it is easy to select which registers take part in an instruction, but
due to the complexity of the x86 architecture, it is more difficult.
One problem is that a 32-bit register such as EAX can also be treated as the 16-bit register AX,
or two 8-bit registers AH and AL.
A second problem is that some instructions include a "direction" bit that switches the source and
destination registers.
Moreover, sometimes the register is specified by bits in the instruction, but in other cases,
the register is specified by the microcode.
Due to these factors, selecting the registers for an operation is a complicated process with many
cases, using control bits from the instruction, from the microcode, and from other sources.
Three registers need to be selected for an operation—two source registers and a destination register—and there
are about 17 cases that need to be handled.
Registers are specified with 7-bit control signals that select one of the 30 registers and control
which part of the register is accessed.
With three control signals, each 7 bits wide, and about 17 cases for each, you can see that
the register control logic is large and complicated.
(I wrote more about the 386's registers
here
.)
I'm still reverse engineering the register control logic, so I won't go into details.
Instead, I'll discuss how the register control circuit uses multiplexers, implemented with standard cells.
A multiplexer is a circuit that combines multiple
input signals into a single output by selecting one of the inputs.
2
A multiplexer can be implemented with logic gates, for instance, by ANDing each input with the
corresponding control line, and then ORing the results together.
However, the 386 uses a different approach—CMOS switches—that avoids a large AND/OR gate.
Schematic of a CMOS switch.
The schematic above shows how a CMOS switch is constructed from two MOS transistors.
When the two transistors are on, the output is connected to the input, but when the two transistors are
off, the output is isolated.
An NMOS transistor is turned on when its input is high, but a PMOS transistor is turned on when its
input is
low
. Thus, the switch uses two control inputs, one inverted.
The motivation for using two transistors is that an NMOS transistor is better at pulling the output
low, while a PMOS transistor is better at pulling the output high, so combining them yields the best performance.
3
Unlike a logic gate, the CMOS switch has no amplification, so a signal is weakened as it passes through the switch.
As will be seen below, inverters can be used to amplify the signal.
The image below shows how CMOS switches appear under the microscope.
This image is very hard to interpret because the two layers of metal on the 386 are packed together densely, but you
can see that some wires run horizontally and others run vertically.
The bottom layer of metal (called M1) runs vertically in the routing area, as well as providing internal
wiring for a cell.
The top layer of metal (M2) runs horizontally; unlike M1, the M2 wires can cross a cell.
The large circles are vias that connect the M1 and M2 layers, while the small circles are connections
between M1 and polysilicon or M1 and silicon.
The central third of the image is a column of standard cells with two CMOS switches outlined in green.
The cells are bordered by the vertical ground rail and
+5V rail that power the cells. 
The routing areas are on either side of the cells, holding the wiring that connects the cells.
Two CMOS switches, highlighted in green. The lower switch is flipped vertically compared to the upper switch.
Removing the metal layers reveals the underlying silicon with a layer of polysilicon wiring on top.
The doped silicon regions show up as dark outlines.
I've drawn the polysilicon in green; it forms a transistor (brighter green) when it crosses doped silicon.
The metal ground and power lines are shown in blue and red, respectively, with other metal wiring in purple.
The black dots are vias between layers.
Note how metal wiring (purple) and polysilicon wiring (green) are combined to route signals within
the cell.
Although this standard cell is complicated, the important thing is that it only needs to be designed once.
The standard cells for different functions are all designed to have the same width, so the cells can be arranged in
columns, snapped together like Lego bricks.
A diagram showing the silicon for a standard-cell switch. The polysilicon is shown in green. The bottom metal is shown in blue, red, and purple.
To summarize, this switch circuit allows the input to be connected to the output or disconnected, controlled by the select signal.
This switch is more complicated than the earlier schematic because it includes two inverters to amplify
the signal.
The data input and the two select lines are connected to the polysilicon (green); the cell is designed so
these connections can be made on either side.
At the top, the input goes through a standard two-transistor inverter.
The lower left has two transistors, combining the NMOS half of an inverter with the NMOS half of the switch.
A similar circuit on the right combines the PMOS part of an inverter and switch.
However, because PMOS transistors are weaker, this part of the circuit is duplicated.
A multiplexer is constructed by combining multiple switches, one for each input.
Turning on one switch will select the corresponding input.
For instance, a four-to-one multiplexer has four switches, so it can select one of the four inputs.
A four-way multiplexer constructed from CMOS switches and individual transistors.
The schematic above shows a hypothetical multiplexer with four inputs.
One optimization is that if an input is always 0, the PMOS transistor can be omitted. Likewise,
if an input is always 1, the NMOS transistor can be omitted.
One set of select lines is activated at a time to select the corresponding input.
The pink circuit selects 1,
green selects input A, yellow selects input B, and blue selects 0.
The multiplexers in the 386 are similar, but have more inputs.
The diagram below shows how much circuitry is devoted to multiplexers in this block of standard cells.
The green, purple, and red cells correspond to the multiplexers driving the three register control
outputs.
The yellow cells are inverters that generate the inverted control signals for the CMOS switches.
This diagram also shows how the automatic layout of cells results in a layout that appears random.
A block of standard-cell logic with multiplexers highlighted. The metal and polysilicon layers were removed for this photo, revealing the silicon transistors.
The misplaced transistor
The idea of standard-cell logic is that standardized cells are arranged in columns.
The space between the cells is the "routing channel", holding the wiring that links the cells.
The 386 circuitry follows this layout, except for one single transistor, sitting between two columns
of cells.
The "misplaced" transistor, indicated by the arrow. The irregular green regions are oxide that was incompletely removed.
I wrote some software tools to help me analyze the standard cells. Unfortunately, my tools
assumed that all the cells were in columns, so this one wayward transistor caused me considerable inconvenience.
The transistor turns out to be a PMOS transistor, pulling a signal high as part of a multiplexer.
But why is this transistor out of place?
My hypothesis is that the transistor is a bug fix.
Regenerating the cell layout was very costly, taking many hours on an IBM mainframe computer.
Presumably, someone found that they could just stick the necessary transistor into an unused spot in the
routing channel, manually add the necessary wiring, and avoid the delay of regenerating all the cells.
The fake inverter
The simplest CMOS gate is the inverter, with an NMOS transistor to pull the output low and a
PMOS transistor to pull the output high.
The standard cell circuitry that I examined contains over a hundred inverters of various
sizes.
(Performance is improved by using inverters that aren't too small but also aren't
larger than necessary for a particular circuit. Thus, the standard cell library includes inverters of multiple sizes.)
The image below shows a medium-sized standard-cell inverter under the microscope.
For this image, I removed the two metal layers with acid to show the underlying polysilicon
(bright green) and silicon (gray).
The quality of this image is
poor—it is difficult to remove the metal without destroying the polysilicon—but the diagram below
should clarify the circuit.
The inverter has two transistors: a PMOS transistor connected to +5 volts to pull the output high when
the input is 0, and an NMOS transistor connected to ground to pull the output low when the input is 1.
(The PMOS transistor needs to be larger because PMOS transistors don't function as well as NMOS transistors due to
silicon physics.)
An inverter as seen on the die. The corresponding standard cell is shown below.
The polysilicon input line plays a key role: where it crosses the doped silicon, a transistor gate is
formed.
To make the standard cell more flexible, the input to the inverter
can be connected on either the left or the right; in this case, the input
is connected on the right and there is no connection on the left.
The inverter's output can be taken from the polysilicon on the upper left or the right, but in this case, it
is taken from the upper metal layer (not shown).
The power, ground, and output lines are in the lower metal layer, which I have represented by
the thin red, blue, and yellow lines. The black circles are connections between the metal layer and
the underlying silicon.
This inverter appears dozens of times in the circuitry.
However, I came across a few inverters that didn't make sense. The problem was
that the inverter's output was connected to the output of a multiplexer.
Since an inverter is either on or off, its value would clobber the output of the multiplexer.
4
This didn't make any sense.
I double- and triple-checked the wiring to make sure I hadn't messed up.
After more investigation, I found another problem: the input to a "bad" inverter didn't make sense
either. The input consisted of two signals shorted together, which doesn't work.
Finally, I realized what was going on. A "bad inverter" has the exact silicon layout of an inverter,
but it wasn't an inverter: it was independent NMOS and PMOS transistors with separate inputs.
Now it all made sense.
With two inputs, the input signals were independent, not shorted together.
And since the transistors were controlled separately, the NMOS transistor could pull the output
low in some circumstances, the PMOS transistor could pull the output high in other circumstances,
or both transistors could be off, allowing the multiplexer's output to be used undisturbed.
In other words, the "inverter" was just two more cases for the multiplexer.
The "bad" inverter. (Image is flipped vertically for comparison with the previous inverter.)
If you compare the "bad inverter" cell below with the previous cell, they look
almost
the same, but
there are subtle differences.
First, the gates of the two transistors are connected in the real inverter, but disconnected
by a small gap in the transistor pair.
I've indicated this gap in the photo above; it is hard to tell if the gap is real or just an imaging
artifact, so I didn't spot it.
The second difference is that the "fake" inverter has two input connections, one to each transistor,
while the inverter has a single input connection.
Unfortunately, I assumed that the two connections were just a trick to route the signal across
the inverter without requiring an extra wire.
In total, this cell was used 32 times as a real inverter and 9 times
as independent transistors.
Conclusions
Standard cell logic and automatic place and route have a long history before the 386,
back to the early 1970s, so this isn't an Intel invention.
5
Nonetheless, the 386 team deserves the credit for deciding to use this technology at a time when it
was a risky decision.
They needed to develop custom software for their placing and routing needs, so this wasn't a trivial undertaking.
This choice paid off and they completed the 386 ahead of schedule.
The 386 ended up being a huge success for Intel, moving the x86 architecture to 32 bits and defining the dominant computer
architecture for the rest of the 20th century.
If you're interested in standard cell logic, I also wrote about
standard cell logic in an IBM chip
.
I plan to write more about the 386, so 
follow me on
Mastodon
,
Bluesky
,
or RSS for updates.
Thanks to Pat Gelsinger and Roxanne Koester for providing helpful papers.
For more on the 386 and other chips, follow me on
Mastodon (
@
[email protected]
),
Bluesky (
@righto.com
),
or
RSS
.  (I've given up on Twitter.)
If you want to read more about the 386, I've written about the
clock pin
,
prefetch queue
,
die versions
,
packaging
, and
I/O circuits
.
Notes and references
