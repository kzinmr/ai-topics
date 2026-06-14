---
title: "The adder at the heart of Intel's 8087 floating-point chip"
url: "http://www.righto.com/2026/06/intel-8087-adder-reverse-engineered.html"
fetched_at: 2026-06-14T07:00:54.586786+00:00
source: "righto.com"
tags: [blog, raw]
---

# The adder at the heart of Intel's 8087 floating-point chip

Source: http://www.righto.com/2026/06/intel-8087-adder-reverse-engineered.html

In 1980, Intel released the Intel 8087 floating-point coprocessor, a chip that could make math up to 100 times faster.
As well as arithmetic and square roots, the 8087 computed
transcendental functions including tangent, exponentiation, and logarithms.
But it all depended on a 69-bit adder:
"The arithmetic heart of the floating-point
execution unit is centered about a nanomachine comprised of the adder and its related registers, shifters and control circuitry,"
as
the patent
describes it.
In this article, I explain the circuitry of this adder.
The photo below shows the 8087 die under a microscope.
Around the edges of the die, hair-thin bond wires connect the chip to its 40 external pins.
The complex patterns on the die are formed by its metal wiring, as well as the polysilicon and silicon underneath.
At the top of the chip, the Bus Interface Unit connects to the rest of the system: coordinating with the main 8086 processor and 
memory.
The chip's instructions are defined by the large microcode ROM in the middle.
Die of the Intel 8087 floating-point unit chip, with relevant functional blocks labeled. The die is 5mm×6mm.  Click for a larger image.
The bottom half of the die is the "datapath", the circuitry that performs calculations; it is split into the exponent datapath,
which handles the exponent of a floating-point number, and the fraction datapath, which handles the fractional part (or significand).
The adder (red) sits in the middle of the fraction datapath; to perform addition on the exponent, the exponent must be copied over to
the fraction datapath.
Structure of the adder
Building a binary adder is easy; the hard part is making it fast.
The key problem is how to handle the carries from a bit position to the next.
Each carry potentially depends on all the lower carries, but you don't want
to wait as a carry ripples through the logic for all 69 bits.
(It's similar to doing 999999+1 with long addition: you need to carry the one, carry the one, ...)
The 8087's adder speeds up performance by breaking addition into 4-bit blocks, using two techniques to make computation inside each
block fast. The carry needs to ripple from block to block, but this reduces the number of carry steps by a factor of four.
Simplified diagram of a four-bit block in the 8087's adder.
The diagram above shows the structure of one 4-bit block, with the carry generation circuits abstraced out for now.
The adder takes two inputs: one (
F
) is from the chip's fraction bus, a bus that connects the components of the fraction datapath.
The second input (
B
) comes from a register called the B register.
Each bit of the sum is produced by XORing a
F
input, a
B
input, and the carry into that bit position.
1
For reasons that will be explained below, the intermediate value (
F XOR B
) is called "propagate". 
The carry-out from each block is tied to the carry-in of the next block.
But what happens inside the carry circuits?
In 1959, researchers at the University of Manchester developed a fast carry technique for a computer called Atlas.
This technique, named the Manchester carry chain,
computes the carry values by setting up switches in parallel and then letting the
carry quickly propagate through the wires, controlled by the switches.
Although the carry still needs to travel from bit to bit, it travels at the speed of a signal in a wire, not slowed by logic gates.
2
The Manchester carry chain is built around the concepts of Generate, Propagate, and Delete (also known as Kill), which arise when
adding two bits and a carry.
If you add
1+1
, a carry-out is
generated
, whether there is a carry-in or not.
In contrast, if you add
0+0
, there is no carry-out, regardless of the carry-in; any carry-in is
deleted
.
The interesting case is if you add
0+1
: a carry-out results only if there is a carry-in; that is, the carry-in is
propagated
to the carry-out.
In logic terms,
the generate signal is the AND of the two input bits, the delete signal is the NOR, and the propagate signal is the XOR.
The important thing is that these signals can be computed for all bit positions in parallel, in constant time.
The idea behind the Manchester carry chain. Note that the low bit is on the left, so the carry flows left to right.
The Manchester carry chain is constructed as above, with the switches at each bit set according to the Generate/Propagate/Delete values.
Once the switches are set, the carry status quickly flows through the circuit, producing the carry value at each position without any
logic delays. If the propagate switch is closed, the previous carry passes through. But if the generate or delete switch is closed,
the carry is set or cleared, respectively.
Once the carry values are available, the final sum can be computed in parallel with XORs.
The 8087 uses an optimized circuit for the Manchester carry chain, combining the Generate and Delete cases.
One stage of the adder's carry chain is shown below.
For the propagate case, the carry-in
Cin
passes through the top switch, propagated to the carry out
Cout
.
For the generate and delete cases, the bottom switch is closed, passing the input bit
F
.
The trick is that the generate case corresponds to
1+1
, so
F
is 1, resulting in
Cout
getting set.
The delete case corresponds to
0+0
, so
F
is 0, and
Cout
is cleared.
(Note that both inputs,
F
and
B
, are the same in these cases, so using
F
instead of
B
is arbitrary.)
One stage of the Manchester carry chain.
The middle of the diagram shows how the switches correspond to a multiplexer (mux) selecting the top signal
Cin
if
prop
is set, or
the bottom signal
F
if
prop
is clear.
The right side of the diagram shows the physical implementation with two NMOS transistors.
These transistors function as switches (pass transistors), controlled by the
prop
signals on the gate.
The problem is that pass transistors aren't perfect switches, but lose a bit of voltage at
 each step.
To fix this, the carry chain is broken into blocks of four bits (as shown earlier) and each block produces a "fresh" carry.
This refresh is done by a "carry-skip" circuit, which can skip the carry processing inside the block.
Specifically, the carry-skip mechanism checks if all positions inside the block are Propagate.
In this case, the carry-out will have the same value as the carry-in (since the carry-in propagates through all the bit positions of the block).
The carry-skip circuit detects this case and produces a carry-out signal matching the carry-in.
Putting this all together,
the schematic below shows the adder circuitry for a typical block of four bits.
The four multiplexers form the Manchester carry chain, while the NOR gate detects the carry-skip case.
Reverse-engineered schematic for a 4-bit block of the adder.
To optimize performance, there is a complication for electrical reasons.
3
The 8087 uses NMOS transistors, which are much faster to pull a signal low than to pull a signal high.
To improve performance, the carry lines are precharged to 5V at the start of an addition, and then the circuitry pulls the lines
low if needed.
In order to start in the no-carry state, the carry lines are all negated, so the initial 5V state corresponds to no carry, and the ground
state corresponds to a carry.
The last multiplexer in the block has four inputs instead of two
4
. The third input pulls the (inverted) carry line low for the carry skip
case.
5
The fourth input is the
precharge
signal; it puts 5V on the carry line to precharge it. (A control circuit activates the precharge signal
at the start of an addition cycle.) Note that this only precharges one of the carry lines;
to precharge the rest, the propagate signal is forced high during precharge.
Reverse-engineered schematic for the propagate circuit. This shows an arbitrary bit
n
.
The circuit to generate the
propagate
signal (above) is
conceptually the XOR of the two inputs, but there are (of course) complications.
When the
precharge
signal is high,
propagate
is forced high, tying all the carry lines together so the precharge can
propagate to all of them.
The second feature is that the
B
inputs can be blocked by the
forceZero
signal, so the value 0 is added instead of the
B
value.
To summarize, the adder is divided into blocks of four bits. Each block uses a Manchester carry chain and a carry-skip circuit to
optimize the performance.
Even with these optimizations, though, the large number of blocks requires the 8087 to take two clock cycles to complete an addition.
The adder in silicon
The image below shows how the circuitry for a block of four bits appears on the die.
These blocks are stacked vertically to create the complete adder as seen in the earlier die photo.
In this image, the metal layer is visible as white lines, mostly obscuring the circuitry underneath.
The 8087 has a single metal layer, which constrains the layout. Note that metal wiring is tightly packed, occupying almost the complete
area.
The thick vertical metal trace at the left is ground, while the thick metal trace at the right is power, supplying the adder circuitry.
The horizontal traces provide wiring inside the adder block, as well as allowing the fraction bus to pass across the adder.
The vertical lines on either side are control signals for the adder (
precharge
and
forceZero
) as well as connections to
circuitry at the bottom of the chip.
A block of four bits in the adder.
The photo below shows the 
silicon and polysilicon circuitry underneath the metal layer.
(To take this photo, I dissolved the metal layer with acid.)
The thin lines are polysilicon wiring, while the pinkish areas that appear raised are doped silicon.
A transistor is formed when polysilicon crosses doped silicon.
The circuitry is complex and irregular, connected by the horizontal metal wires above.
The white circuits are contacts between the silicon and the metal wiring, while the white squares are contacts between the polysilicon
and metal.
Roughly speaking, if you divide the circuitry above into quarters, each quarter adds one bit.
The carry-skip circuitry is in the middle.
A block of four bits in the adder with the metal layer removed.
The left and the right sides of the image don't have any transistors, just polysilicon lines that pass under the vertical metal wiring.
Many of these polysilicon lines are widened to reduce their resistance and thus tune performance.
The silicon in these regions is "wasted", just providing a channel for the vertical wiring.
The size of the adder
Although the 8087 nominally has 64-bit values for the fraction (significand),
the adder is slightly larger:
it takes 69 bits as input and generates 70 output bits.
One reason is that the 8087 uses three extra low-order bits for rounding, called Guard,
Round, and Sticky. These bits ensure that a value is always rounded in the right direction.
Handling of the rounding bits is fairly complicated, with multiple modes, but from the adder's perspective they are just three
input bits.
6
As will be explained below, the value from the B register can be doubled, requiring one more bit.
Finally, the fraction bus and the B value can be negated. (This is used for subtraction, among other things.)
A negative value is represented in two's complement, requiring one more bit.
In total, the inputs to the adder are 69 bits wide.
When adding two large numbers, the result can require one additional bit.
Thus, the output of the adder is 70 bits wide.
The Sum Shifter (explained below) can shift the output two bits to the right, cutting the result down to 68 bits.
This is still one bit larger than 64 bits with 3 rounding bits; the "extra" bit is supported by a few special-purpose
registers, such as the
tmpC
register
7
and the Skip Shifter.
The surrounding circuitry
The inputs and outputs of the adder are tied to some special registers and circuits. I'll leave a detailed explanation of
this circuitry to another post, but I'll provide a brief description here.
8
The adder has two inputs: one input is from the fraction bus and the other input is from the B register.
The adder's output is stored in the Sum Register.
To make multiplication faster, the 8087 uses
radix-4 Booth multiplication
,
which multiplies by two bits at a time. 
The multiplier is stored in the Skip Shifter, a register that allows two bits to be shifted out at a time.
Based on these bits, one of the values
2B
,
B
,
0
, or
-B
is added.
(The
-B
path is also used for subtraction.)
The adder's output is shifted right two bits by the Sum Shifter (not to be confused with the Skip Shifter) and stored in the Sum Register.
The adder and associated registers. Based on
the patent
.
Division is implemented by repeated subtraction, addition, and shifting. The bits of the result are accumulated in the quotient register.
The implementation of square root is similar to the pencil-and-paper long square root, except in binary.
The skip shifter provides two bits from the left, which are appended to the right side of the adder input. A subtract or add takes
place, similar to division, and the square root is formed in the B register.
Multiplication, division, and square root require multiple steps to process all the bits.
For performance, this looping is implemented in hardware, not in microcode.
These instructions require a lot of microcode to prepare the arguments, handle exponents, handle special cases, and store the results,
but the inner loop is hardware.
Conclusions
The
8087 patent
expresses the importance of the adder: "Ultimately, all arithmetical operations are reduced at one point to a binary addition."
Thus, the performance of the adder is vital to the performance of the 8087.
There are faster ways to add, such as the
Kogge-Stone adder in the Pentium
, but these approaches require much more hardware, too much for the constrained transistor count of the 8087.
The 8087 balanced complexity against performance, using the Manchester carry chain with a carry-skip adder.
I plan to write more about the 8087;
for updates, follow me on
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
Thanks to the members of the "Opcode Collective" for their hard work, especially Smartest Blob and Gloriouscow.
AI statement: I didn't use AI to write this article; the em-dashes are natural (
details
).
Notes and references
