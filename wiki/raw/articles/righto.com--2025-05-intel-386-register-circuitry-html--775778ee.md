---
title: "The absurdly complicated circuitry for the 386 processor's registers"
url: "http://www.righto.com/2025/05/intel-386-register-circuitry.html"
fetched_at: 2026-04-28T07:01:55.243212+00:00
source: "righto.com"
tags: [blog, raw]
---

# The absurdly complicated circuitry for the 386 processor's registers

Source: http://www.righto.com/2025/05/intel-386-register-circuitry.html

The groundbreaking Intel 386 processor (1985) was the first 32-bit processor in the x86 architecture.
Like most processors, the 386 contains numerous registers; registers are a key part of a processor because
they provide storage that is much faster than main memory.
The register set of the 386 includes general-purpose registers, index registers, and segment selectors, as well
as registers with special functions for memory management and operating system implementation.
In this blog post, I look at the silicon die of the 386 and explain how the processor implements its main registers.
It turns out that the circuitry that implements the 386's registers is much more complicated than one would expect.
For the 30 registers that I examine, instead of using a standard circuit, the 386 uses
six
different circuits,
each one optimized for the particular characteristics of the register.
For some registers, Intel squeezes register cells together to double the storage capacity.
Other registers support accesses of 8, 16, or 32 bits at a time.
Much of the register file is "triple-ported", allowing two registers to be read simultaneously while a value is written
to a third register.
Finally, I was surprised to find that registers don't store bits in order: the lower 16 bits of each register are interleaved, while the upper 16 bits are stored linearly.
The photo below shows the 386's shiny fingernail-sized silicon die under a special metallurgical microscope.
I've labeled the main functional blocks. 
For this post, the Data Unit in the lower left quadrant of the chip is the relevant component.
It consists of the 32-bit arithmetic logic unit (ALU) along
with the processor's main register bank (highlighted in red at the bottom).
The circuitry, called the datapath, can be viewed as the heart of the processor.
This die photo of the 386 shows the location of the registers. Click this image (or any other) for a larger version.
The datapath is built with a regular structure: each register or ALU functional unit is a horizontal stripe of circuitry,
forming the horizontal bands visible in the image.
For the most part, this circuitry consists of a carefully optimized circuit copied 32 times, once for each bit of the processor.
Each circuit for one bit is exactly the same width—60 µm—so the functional blocks can be stacked together like microscopic
LEGO bricks.
To link these circuits, 
metal bus lines run vertically through the datapath in groups of 32, allowing data to flow up and down through the blocks.
Meanwhile, control lines run horizontally, enabling ALU operations or register reads and writes; the irregular circuitry
on the right side of the Data Unit produces the signals for these control lines, activating the appropriate control
lines for each instruction.
The datapath is highly structured to maximize performance while minimizing its area on the die.
Below, I'll look at how the registers are implemented according to this structure.
The 386's registers
A processor's registers are one of the most visible features of the processor architecture.
The 386 processor contains 16 registers for use by application programmers, a small number by modern standards,
but large enough for the time.
The diagram below shows the eight 32-bit general-purpose registers.
At the top are four registers called EAX, EBX, ECX, and EDX.
Although these registers are 32-bit registers, they can also be treated as 16 or 8-bit registers for backward
compatibility with earlier processors.
For instance, the lower half of EAX can be accessed as the 16-bit register AX, while the bottom byte of EAX can
be accessed as the 8-bit register AL.
Moreover, bits 15-8 can also be accessed as an 8-bit register called AH.
In other words, there are four different ways to access the EAX register, and similarly for the other three registers.
As will be seen, these features complicate the implementation of the register set.
The bottom half of the diagram shows that the 32-bit EBP, ESI, EDI, and ESP registers can also be treated as 16-bit registers BP, SI, DI, and SP. Unlike the previous registers,
these ones cannot be treated as 8-bit registers.
The 386 also has six segment registers that define the 
start of memory segments; these are 16-bit registers.
The 16 application registers are rounded out by the status flags and instruction pointer (EIP);
they are viewed as 32-bit registers, but their implementation is more complicated.
The 386 also has numerous registers for operating system programming, but I won't discuss them here, since they
are likely in other parts of the chip.
1
Finally, the 386 has numerous temporary registers that are not visible to the programmer but are used by the microcode
to perform complex instructions.
The 6T and 8T static RAM cells
The 386's registers are implemented with static RAM cells, a circuit that can hold one bit.
These cells are arranged into a grid to provide multiple registers.
Static RAM can be contrasted with the dynamic RAM that computers use for their main memory:
dynamic RAM holds each bit in a tiny capacitor, while static RAM uses a faster but larger and more complicated circuit.
Since main memory holds gigabytes of data, it uses dynamic RAM to provide dense and inexpensive storage.
But the tradeoffs are different for registers: the storage capacity is small, but speed is of the essence.
Thus, registers use the static RAM circuit that I'll explain below.
The concept behind a static RAM cell is to connect two inverters into a loop.
If an inverter has a "0" as input, it will output a "1", and vice versa.
Thus, the inverter loop will be stable,
with one inverter on and one inverter off, and each inverter supporting the other.
Depending on which inverter is on, the circuit stores a 0 or a 1, as shown below.
Thus, the pair of inverters provides one bit of memory.
Two inverters in a loop can store a 0 or a 1.
To be useful, however, the inverter loop needs a way to store a bit into it, as well as a way to read out the stored bit.
To write a new value into the circuit, two signals are fed in, forcing the inverters to the desired new values.
One inverter receives the new bit value, while the other inverter receives the complemented bit value.
This may seem like a brute-force way to update the bit, but it works.
The trick is that the inverters in the cell are small and weak, while the input signals are higher current,
able to overpower the inverters.
2
These signals are fed in through wiring called "bitlines"; the bitlines can also be used to read the value
stored in the cell.
By adding two pass transistors to the circuit, the cell can be read and written.
To control access to the register, 
the bitlines are connected to the inverters through pass transistors, which act as switches to
control access to the inverter loop.
3
When the pass transistors are on, the
signals on the write lines can pass through to the inverters. But when the pass transistors are off, the
inverters are isolated from the write lines.
The pass transistors are turned on by a control signal, called a "wordline" since it controls access to a word
of storage in the register.
Since each inverter is constructed from two transistors, the circuit above consists of six transistors—thus this circuit is called a "6T" cell.
The 6T cell uses the same bitlines for reading and writing, so you can't read and write to registers simultaneously.
But adding two transistors creates an "8T" circuit that lets you read from one register
and write to another register at the same time. (In technical terms, the register file is two-ported.)
In the 8T schematic below, the two additional transistors (G and H) are used for reading.
Transistor G buffers the cell's value; it turns on if the inverter output is high, pulling the read output bitline low.
4
Transistor H is a pass transistor that blocks this signal until a read is performed on this register;
it is controlled by a read wordline.
Note that there are two bitlines for writing (as before) along with one bitline for reading.
Schematic of a storage cell. Each transistor is labeled with a letter.
To construct registers (or memory), a grid is constructed from these cells.
Each row corresponds to a register, while each column corresponds to a bit position.
The horizontal lines are the wordlines, selecting which word to access, while the
vertical lines are the bitlines, passing bits in or out of the registers.
For a write, the vertical bitlines provide the 32 bits (along with their complements).
For a read, the vertical bitlines receive the 32 bits from the register.
A wordline is activated to read or write the selected register.
To summarize: each row is a register, data flows vertically, and control signals flow horizontally.
Static memory cells (8T) organized into a grid.
Six register circuits in the 386
The die photo below zooms in on the register circuitry in the lower left corner of the 386 processor.
You can see the arrangement of storage cells into a grid, but note that the pattern changes from row to row.
This circuitry implements 30 registers: 22 of the registers hold 32 bits, while the bottom ones are 16-bit registers.
By studying the die, I determined that there are six different register circuits,
which I've arbitrarily labeled (
a
) to (
f
).
In this section, I'll describe these six types of registers.
The 386's main register bank, at the bottom of the datapath.  The numbers show how many bits of the register can be accessed.
I'll start at the bottom with the simplest circuit: eight 16-bit registers that I'm calling type (
f
).
You can see a "notch" on the left side of the register file
because these registers are half the width of the other registers (16 bits versus 32 bits).
These registers are implemented with the 8T circuit described earlier, making them dual ported:
one register can be read while another register is written.
As described earlier, three vertical bus lines pass through each bit: one bitline for reading and two bitlines
(with opposite polarity)
for writing.
Each register has two control lines (wordlines): one to select a register for reading and another to select a register for writing.
The photo below shows how four cells of type (
f
) are implemented on the chip.
In this image, the chip's two metal layers have been removed along with most of the polysilicon wiring, showing the underlying silicon.
The dark outlines indicate regions of doped silicon, while the stripes across the doped region correspond to transistor
gates. 
I've labeled each transistor with a letter corresponding to the earlier schematic.
Observe that the layout of the bottom half is a mirrored copy of the upper half, saving a bit of space.
The left and right sides are approximately mirrored; the irregular shape allows separate read and wite wordlines 
to control the left and right halves without colliding.
Four memory cells of type (
f
), separated by dotted lines. The small irregular squares are remnants of polysilicon
that weren't fully removed.
The 386's register file and datapath are designed with 60 µm of width assigned to each bit.
However, the register circuit above is unusual:
the image above is 60 µm wide but there are two register cells side-by-side.
That is, the circuit crams
two
bits in 60 µm of width, rather than one.
Thus, this dense layout implements two registers per row (with interleaved bits), providing twice the density of the other register circuits.
If you're curious to know how the transistors above are connected,
the schematic below shows how the physical arrangement of the transistors above corresponds to two of the 8T memory cells
described earlier.
Since the 386 has two overlapping layers of metal, it is very hard to interpret a die photo with the metal layers.
But see my
earlier article
if you want these photos.
Schematic of two static cells in the 386, labeled "R" and "L" for "right" and "left". The schematic approximately matches the physical layout.
Above the type (
f
) registers are 10 registers of type (
e
), occupying five rows of cells.
These registers are the same 8T implementation as before, but these registers are 32 bits wide instead of 16.
Thus, the register takes up the full width of the datapath, unlike the previous registers.
As before, the double-density circuit implements two registers per row.
The silicon layout is identical (apart from being 32 bits wide instead of 16), so I'm not including a photo.
Above those registers are four (
d
) registers, which are more complex.
They are triple-ported registers, so one register can be written while two other registers are read.
(This is useful for ALU operations, for instance, since two values can be added and the result written back
at the same time.)
To support reading a second register, another vertical bus line is added for each bit.
Each cell has two more transistors to connect the cell to the new bitline.
Another wordline controls the additional read path.
Since each cell has two more transistors, there are 10 transistors in total and the circuit is called 10T.
Four cells of type (
d
). The striped green regions are the remnants of oxide layers that weren't completely removed, and can be ignored.
The diagram above shows four memory cells of type (
d
).
Each of these cells takes the full 60 µm of width, unlike the previous double-density cells.
The cells are mirrored horizontally and vertically;
this increases the density slightly since power lines can be shared between cells.
I've labeled the transistors
A
through
H
as before, as well as the two additional transistors
I
and
J
for the
second read line.
The circuit is the same as before, except for the two additional transistors, but
the silicon layout is significantly different.
Each of the (
d
) registers has five control lines. Two control lines select a register for reading, connecting the register
to one of the two vertical read buses.
The three write lines allow parts of the register to be written independently: the top 16 bits, the next 8 bits, or the
bottom 8 bits.
This is required by the x86 architecture, where a 32-bit register such as EAX can also be accessed as the 16-bit AX register,
the 8-bit AH register, or the 8-bit AL register.
Note that reading part of a register doesn't require separate control lines: the register provides all 32 bits and
the reading circuit can ignore the bits it doesn't want.
Proceeding upward, the three (
c
) registers have a similar 10T implementation.
These registers, however, do not support partial writes so all 32 bits must be written at once.
As a result, these registers only require three control lines (two for reads and one for writes).
With fewer control lines, the cells can be fit into less vertical space, so the layout is slightly more compact than
the previous type (
d
) cells. The diagram below shows four type (
c
) rows above two type (
d
) rows.
Although the cells have the same ten transistors, they have been shifted around somewhat.
Four rows of type (
c
) above two cells of type (
d
).
Next are the four (
b
) registers, which support 16-bit writes and 32-bit writes (but not 8-bit writes).
Thus, these registers have four control lines (two for reads and two for writes).
The cells take slightly more vertical space than the (
c
) cells due to the additional control line, but the layout is
almost identical.
Finally, the (
a
) register at the top has an unusual feature: it can receive a copy of the value in the register just
below it.
This value is copied directly between the registers, without using the read or write buses.
This register has 3 control lines: one for read, one for write, and one for copying.
A cell of type (
a
), which can copy the value in the cell of type (
b
) below.
The diagram above shows a cell of type (
a
) above a cell of type (
b
).
The cell of type (
a
) is based on the standard 8T circuit,
but with six additional transistors to copy the value of the cell below.
Specifically, two inverters buffer the output from cell (
b
), one inverter for each side of the cell.
These inverters are implemented with transistors I1 through I4.
5
Two transistors, S1 and S2, act as a pass-transistor switches between these inverters and the memory cell.
When activated by the control line, the switch transistors allow the inverters to overwrite the memory cell with
the contents of the cell below.
Note that cell (
a
) takes considerably more vertical space because of the extra transistors.
Speculation on the physical layout of the registers
I haven't determined the mapping between the 386's registers and the 30 physical registers, but I can speculate.
First, the 386 has four registers that can be accessed as 8, 16, or 32-bit registers: EAX, EBX, ECX, and EDX.
These must map onto the (
d
) registers, which support these access patterns.
The four index registers (ESP, EBP, ESI, and EDI) can be used as 32-bit registers or 16-bit registers,
matching the four (
b
) registers with the same properties.
Which one of these registers can be copied to the type (
a
) register?
Maybe the stack pointer (ESP) is copied as part of interrupt handling.
The register file has eight 16-bit registers, type (
f
).
Since there are six 16-bit segment registers in the 386, I suspect the 16-bit registers are the segment registers and two additional registers.
The
LOADALL
instruction gives some clues, suggesting that the two additional 16-bit registers are
LDT (Local Descriptor Table register) and TR (Task Register).
Moreover,
LOADALL
handles 10 temporary registers, matching the 10 registers of type (
e
) near the bottom
of the register file.
The three 32-bit registers of type (
c
) may be the
CR0 control register and the DR6 and DR7 debug registers.
The six 16-bit segment registers in the 386.
In this article, I'm only looking at the main register file in the datapath.
The 386 presumably has other registers scattered around
the chip for various purposes.
For instance, the Segment Descriptor Cache contains multiple registers similar to type (
e
), probably holding cache entries.
The processor status flags and the instruction pointer (EIP) may not be implemented as discrete registers.
6
To the right of the register file, a complicated block of circuitry uses seven-bit values to select registers.
Two values select the registers (or constants) to read, while a third value selects the register to write.
I'm currently analyzing this circuitry, which should provide more insight into how the physical registers
are assigned.
The shuffle network
There's one additional complication in the register layout.
As mentioned earlier, the bottom 16 bits of the main registers can be treated as two 8-bit registers.
7
For example, the 8-bit AH and AL registers form the bottom 16 bits of the EAX register.
I explained earlier how the registers use multiple write control lines to allow these different parts of the register
to be updated separately.
However, there is also a layout problem.
To see the problem, suppose you perform an 8-bit ALU operation on the AH register, which is bits 15-8 of the EAX register.
These bits must be shifted down to positions 7-0 so they can take part in the ALU operation, and then must be shifted
back to positions 15-8 when stored into AH.
On the other hand, if you perform an ALU operation on AL (bits 7-0 of EAX), the bits are already in position and
don't need to be shifted.
To support the shifting required for 8-bit register operations, the 386's register file physically interleaves the bits of the two lower bytes (but not the high bytes).
As a result, bit 0 of AL is next to bit 0 of AH in the register file, and so forth.
This allows multiplexers to easily select bits from AH or AL as needed.
In other words, each bit of AH and AL is in almost the correct physical position, so an 8-bit shift is not required.
(If the bits were in order, each multiplexer would need to be connected to bits that are separated by eight positions,
requiring inconvenient wiring.)
8
The shuffle network above the register file interleaves the bottom 16 bits.
The photo above shows the shuffle network.
Each bit has three bus lines associated with it: two for reads and one for writes, and these all get shuffled.
On the left, the lines for the 16 bits pass straight through.
On the right, though, the two bytes are interleaved.
This shuffle network is located below the ALU and above the register file, so data words are shuffled when stored in the
register file and then unshuffled when read from the register file.
9
In the photo, the lines on the left aren't quite straight.
The reason is that the circuitry above is narrower than the circuitry below.
For the most part, each functional block in the datapath is constructed with the same width (60 µm) for each bit.
This makes the layout simpler since functional blocks can be stacked on top of each other and the vertical bus wiring
can pass straight through.
However, the circuitry above the registers (for the barrel shifter) is about 10% narrower (54.5 µm), so the wiring
needs to squeeze in and then expand back out.
10
There's a tradeoff of requiring more space for this wiring versus the space saved by making the barrel shifter
narrower and Intel must have considered the tradeoff worthwhile.
(My hypothesis is that since the shuffle network required additional wiring to shuffle the bits, it didn't take up
more space to squeeze the wiring together at the same time.)
Conclusions
If you look in a book on processor design, you'll find a description of how registers can be created from static memory cells.
However, the 386 illustrates that the implementation in a real processor is considerably more complicated.
Instead of using one circuit, Intel used six different circuits for the registers in the 386.
The 386's register circuitry also shows the curse of backward compatibility.
The x86 architecture supports 8-bit register accesses for
compatibility with processors dating back to 1971.
This compatibility requires additional circuitry such as the shuffle network and interleaved registers.
Looking at the circuitry of x86 processors makes me appreciate some of the advantages of RISC processors,
which avoid much of the ad hoc circuitry of x86 processors.
If you want more information about how the 386's memory cells were implemented, I wrote a
lower-level article
earlier.
I plan to write more about the 386, so
follow me on Bluesky (
@righto.com
) or
RSS
for updates.
Footnotes and references
