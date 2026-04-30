---
title: "The Pentium contains a complicated circuit to multiply by three"
url: "http://www.righto.com/2025/03/pentium-multiplier-adder-reverse-engineered.html"
fetched_at: 2026-04-30T07:01:08.478353+00:00
source: "righto.com"
tags: [blog, raw]
---

# The Pentium contains a complicated circuit to multiply by three

Source: http://www.righto.com/2025/03/pentium-multiplier-adder-reverse-engineered.html

In 1993, Intel released the high-performance Pentium processor, the start of the long-running Pentium line.
I've been examining the Pentium's circuitry in detail and I came across a circuit to multiply by three, a complex circuit with thousands of
transistors. Why does the Pentium have a circuit to multiply specifically by three? Why is it so complicated? In this article, I examine
this multiplier—which I'll call the ×3 circuit—and explain its purpose and how it is implemented.
It turns out that this multiplier is a small part of the Pentium's floating-point multiplier circuit. In particular, the Pentium multiplies two
64-bit numbers using base-8 multiplication, which is faster than binary multiplication.
1
However, multiplying by 3 needs to be handled as a special case.
Moreover, since the rest of the multiplication process can't start until the multiplication by 3 finishes, this circuit must be very fast.
If you've studied digital design, you may have heard of techniques such as carry lookahead, Kogge-Stone addition, and carry-select addition.
I'll explain how the ×3 circuit combines all these techniques to maximize performance.
The photo below shows the Pentium's thumbnail-sized silicon die under a microscope.
I've labeled the main functional blocks.
In the center is the integer execution unit that performs most instructions. On the left, the code and data caches improve memory performance. The floating point
unit, in the lower right, performs floating point operations.
Almost half of the floating point unit is occupied by the multiplier, which uses an array of adders to rapidly multiply two 64-bit numbers.
The focus of this article is the ×3 circuit, highlighted in yellow near the top of the multiplier.
As you can see, the ×3 circuit takes up a nontrivial amount of the Pentium die, especially considering that its task seems simple.
This die photo of the Pentium shows the location of the multiplier.
Why does the Pentium use base-8 to multiply numbers?
Multiplying two numbers in binary is conceptually straightforward.
You can think of binary multiplication as similar to grade-school long multiplication, but with binary numbers instead of decimal numbers.
The example below shows how 5×6 is computed in binary: the three terms are added to produce the result.
Conveniently, each term is either the multiplicand (101 in this case) or 0, shifted appropriately, so computing the terms is easy.
101
    ×110
     ―――
     000
i.e. 0×101
101
i.e. 1×101
+101
i.e. 1×101
―――――
   11110
Unfortunately, this straightforward multiplication approach is slow. With the three-bit numbers above, there are three terms to add.
But if you multiply two 64-bit numbers, you have 64 terms to add, requiring a lot of time and/or circuitry.
The Pentium uses a more complicated approach, computing multiplication in base 8.
The idea is to consider the multiplier in groups of three bits, so instead of multiplying by 0 or 1 in each step, you multiply by a number from 0 to 7.
Each term that gets added is still in binary, but the number of terms is reduced by a factor of three.
Thus, instead of adding 64 terms, you add 22 terms, providing a substantial reduction in
the circuitry required.
(I'll describe the full details of the Pentium multiplier in a future article.
2
)
The downside to radix-8 multiplication is that multiplying by a number from 0 to 7 is much more complicated than multiplying by 0 or 1, which is almost trivial.
Fortunately, there are some shortcuts.
Note that multiplying by 2 is the same as shifting the number to the left by 1 bit position, which is very easy in hardware—you wire each bit one position to the left.
Similarly, to multiply by 4, shift the multiplicand two bit positions to the left.
Multiplying by 7 seems inconvenient, but there is a trick, known as Booth's multiplication algorithm.
Instead of multiplying by 7, you add 8 times the number and subtract the number, ending up with 7 times the number.
You might think this requires two steps, but the trick is to multiply by one more in the (base-8) digit to the left, so you get the factor of 8 without an additional step.
(A base-10 analogy is that if you want to multiply by 19, you can multiply by 20 and subtract the multiplicand.)
Thus, you can get the ×7 by subtracting.
Similarly, for a ×6 term, you can subtract a ×2 multiple and add ×8 in the next digit.
Thus, the only difficult multiple is ×3.
(What about ×5? If you can compute ×3, you can subtract that from ×8 to get ×5.)
To summarize, the Pentium's radix-8 Booth's algorithm is a fast way to multiply, but it requires a special circuit to produce the ×3 multiple
of the multiplicand.
Implementing a fast ×3 circuit with carry lookahead
Multiplying a number by three is straightforward in binary: add the number to itself, shifted to the left one position.
(As mentioned above, shifting to the left is the same as multiplying by two and is easy in hardware.)
Unfortunately, using a simple adder is too slow.
The problem with addition is that carries make addition slow.
Consider calculating 99999+1 by hand.
You'll start with 9+1=10, then carry the one, generating another carry, which generates another carry, and so forth, until you go through all the digits.
Computer addition has the same problem:
If you're adding two numbers, the low-order bits can generate a carry that then propagates through all the bits.
An adder that works this way—known as a ripple carry adder—will be slow because the carry has to ripple through
all the bits.
As a result, CPUs use special circuits to make addition faster.
One solution is the carry-lookahead adder. In this adder, all the carry bits are computed in parallel, before computing
the sums. Then, the sum bits can be computed in parallel, using the carry bits.
As a result, the addition can be completed quickly, without waiting for the carries to ripple through
the entire sum.
It may seem impossible to compute the carries without computing the sum first, but there's a way to do it.
For each bit position, you determine signals called "carry generate" and "carry propagate".
These signals can then be used to determine all the carries in parallel.
The
generate
signal indicates that the position generates a carry. For instance, if you add binary
1xx
and
1xx
(where
x
is an arbitrary bit), a carry will be generated from the top bit,
regardless of the unspecified bits.
On the other hand, adding
0xx
and
0xx
will never generate a carry.
Thus, the
generate
signal is produced for the first case but not the second.
But what about
1xx
plus
0xx
? We might get a carry, for instance,
111+001
, but we might not,
for instance,
101+001
. In this "maybe" case, we set the
carry propagate
signal, indicating that a carry into the
position will get propagated out of the position. For example, if there is a carry out of
the middle position,
1xx+0xx
will have a carry from the top bit. But if there is no carry out of the middle position, then
there will not be a carry from the top bit. In other words, the
propagate
signal indicates that a carry into the top bit will be propagated out of the top
bit.
To summarize, adding
1+1
will generate a carry. Adding
0+1
or
1+0
will propagate a
carry.
Thus, the
generate
signal is formed at each position by
G
n
= A
n
·B
n
, where
A
and
B
are the inputs.
The
propagate
signal is
P
n
= A
n
+B
n
,
the logical-OR of the inputs.
3
Now that the
propagate
and
generate
signals are defined, some moderately complex logic
4
can compute the carry
C
n
into
each bit position.
The important thing is that all the carry bits can be computed in parallel, without waiting for the carry to ripple through each bit position.
Once each carry is computed, the sum bits can be computed in parallel:
S
n
= A
n
⊕ B
n
⊕ C
n
. In other words, the two input bits and the computed carry are combined with exclusive-or.
Thus, the entire sum can be computed in parallel by using carry lookahead.
However, there are complications.
Implementing carry lookahead with a parallel prefix adder
The carry bits can be generated directly from the
G
and
P
signals.
However, the straightforward approach requires too much hardware as the number of bits increases.
Moreover, this approach needs gates with many inputs, which are slow for electrical reasons.
For these reasons, the Pentium uses two techniques to keep the hardware requirements for carry lookahead tractable.
First, it uses a "parallel prefix adder" algorithm for carry lookahead across 8-bit chunks.
7
Second, it uses a two-level hierarchical approach for carry lookahead: the upper carry-lookahead circuit handles eight 8-bit chunks, using
the same 8-bit algorithm.
5
The photo below shows the complete ×3 circuit;
you can see that the circuitry is divided into blocks of 8 bits.
(Although I'm calling this a 64-bit circuit, it really produces a 69-bit output: there are 5 "extra" bits on the left to avoid overflow and to provide additional bits for rounding.)
The full ×3 adder circuit under a microscope.
The idea of the parallel-prefix adder is to
produce the
propagate
and
generate
signals across ranges of bits, not just single bits as before.
For instance, the
propagate
signal
P
32
indicates that a carry in to bit 2 would be propagated out of bit 3,
(This would happen with
10xx+01xx
, for example.)
And
G
30
indicates that bits 3 to 0 generate a carry out of bit 3.
(This would happen with
1011+0111
, for example.)
Using some mathematical tricks,
6
you can take the
P
and
G
values for two smaller ranges and merge them into
the
P
and
G
values for the combined range.
For instance, you can start with the
P
and
G
values for bits 0 and 1, and produce
P
10
and
G
10
, the
propagate
and
generate
signals describing two bits.
These could be merged with
P
32
and
G
32
to produce
P
30
and
G
30
,
indicating if a carry is propagated across bits 3-0 or generated by bits 3-0.
Note that
G
n0
tells us if a carry is generated into bit
n+1
from all the lower bits, which is the
C
n+1
carry value that we
need to compute the final sum.
This merging process is more efficient than the "brute force" implementation of the carry-lookahead logic since
logic subexpressions can be reused.
There are many different ways that you can combine the
P
and
G
terms to generate the necessary terms.
8
The Pentium uses an approach called
Kogge-Stone
that attempts to minimize the total delay while keeping the amount of circuitry reasonable.
The diagram below is the standard diagram that illustrates how a
Kogge-Stone adder works.
It's rather abstract, but I'll try to explain it.
The diagram shows how the
P
and
G
signals are merged to produce each output at the bottom. 
Each square box at the top generates the
P
and
G
signals for that bit.
Each line corresponds to both the
P
and the
G
signal.
Each diamond combines two ranges of
P
and
G
signals to generate new
P
and
G
signals for the combined
range.
Thus, the signals cover wider ranges of bits as they progress downward, ending with the
G
n0
outputs that indicate carries.
A diagram of an 8-bit Kogge-Stone adder highlighting the carry out of bit 6 (green) and out of bit 2 (purple). Modification of the diagram by Robey Pointer,
Wikimedia Commons
.
I've labeled a few of the intermediate signals so you can get an idea of how it works. Circuit "A" combines
P
7
and
G
7
with
P
6
and
G
6
to produce the signals describing two bits:
P
76
and
G
76
.
Similarly, circuit "B" combines
P
76
and
G
76
with
P
54
and
G
54
to produce the signals describing four bits:
P
74
and
G
74
.
Finally, circuit "C" produces the final outputs for bit 7:
P
70
and
G
70
.
Note that most of the intermediate results are used twice, reducing the amount of circuitry.
Moreover, there are at most three levels of combination circuitry, reducing the delay compared to a deeper network.
The key point is the
P
and
G
values are computed in parallel so the carry bits can all be computed in parallel,
without waiting for the carry to ripple through all the bits.
(If this explanation doesn't make sense, see my discussion of the Kogge-Stone adder
in the
Pentium's division circuit
for a different—but maybe still confusing—explanation.)
Recursive Kogge-Stone lookahead
The Kogge-Stone approach can be extended to 64 bits, but the amount of circuitry and wiring becomes overwhelming.
Instead, the Pentium uses a recursive, hierarchical approach with two levels of Kogge-Stone lookahead.
The lower layer uses eight Kogge-Stone adders as described above, supporting 64 bits in total.
The upper layer uses a single eight-bit Kogge-Stone lookahead circuit, treating each of the lower chunks as a single bit.
That is, a lower chunk has a propagate signal
P
indicating that a carry into the chunk will be propagated out, as well as a generate signal
G
indicating that the chunk generates a carry.
The upper Kogge-Stone circuit combines these chunked signals to determine if carries will be generated or propagated by groups of chunks.
9
To summarize, each of the eight lower lookahead circuits computes the carries within an 8-bit chunk.
The upper lookahead circuit computes the carries into and out of each 8-bit chunk.
In combination, the circuits rapidly provide all the carries needed to compute the 64-bit sum.
The carry-select adder
Suppose you're on a game show: "What is 553 + 246 +
c
? In 10 seconds, I'll tell you if
c
is 0 or 1 and whoever gives the answer first wins $1000."
Obviously, you shouldn't just sit around until you get
c
. You should do the two sums now, so you can hit the buzzer as soon as
c
is announced.
This is the concept behind the carry-select adder: perform two additions—with a carry-in and without--and then supply the correct answer as soon as the
carry is available.
The carry-select adder requires additional hardware—two adders along with a multiplexer to select the result—but it overlaps the time to compute
the sum with the time to compute the carry.
In effect, the addition and the carry lookahead operations are performed in parallel, with the multiplexer combining the results from each.
The Pentium uses a carry-select adder for each 8-bit chunk in the ×3 circuit. The carry from the second-level carry-lookahead selects which sum should be produced for the chunk.
Thus, the time to compute the carry is overlapped with the time to compute the sum.
Putting the adder pieces together
The image below zooms in on an 8-bit chunk of the ×3 multiplier, implementing an 8-bit adder.
Eight input lines are at the top (along with some unrelated wires). Note that each
input line splits with a signal going to the adder on the left and a signal going to the right.
This is what causes the adder to multiply by 3: it adds the input and the input shifted one bit to the left, i.e. multiplied by two.
The top part of the adder has eight circuits to produce the
propagate
and
generate
signals.
These signals go into the 8-bit Kogge-Stone lookahead circuit. Although most of the adder consists of a circuit block repeated eight times, the
Kogge-Stone circuitry appears chaotic. 
This is because each bit of the Kogge-Stone circuit is different—higher bits are more complicated to compute than lower bits.
One 8-bit block of the ×3 circuit.
The lower half of the circuit block contains an 8-bit carry-select adder. This circuit produces two sums, with multiplexers selecting the correct sum
based on the carry into the block.
Note that the carry-select adder blocks are narrower than the other circuitry.
10
This makes room for a Kogge-Stone block on the left. The second level Kogge-Stone circuitry is split up; the 8-bit carry-lookahead circuitry has one bit
implemented in each block of the adder, and produces the carry-in signal for that adder block.
In other words, the image above includes 1/8 of the second-level Kogge-Stone circuit.
Finally, eight driver circuits amplify the output bits before they are sent to the rest of the floating-point multiplier.
The block diagram below shows the pieces are combined to form the ×3 multiplier.
The multiplier has eight 8-bit adder blocks (green boxes, corresponding to the image above).
Each block computes eight bits of the total sum.
Each block provides
P
70
and
G
70
signals to the second-level lookahead, which determines if each block receives a carry in.
The key point to this architecture is that everything is computed in parallel, making the addition fast.
A block diagram of the multiplier.
In the diagram above, the first 8-bit block is expanded to show its contents. The 8-bit lookahead circuit generates the
P
and
G
signals that determine the
internal carry signals.
The carry-select adder contains two 8-bit adders that use the carry lookahead values.
As described earlier, one adder assumes that the block's carry-in is 1 and the second assumes the carry-in is 0. When the real carry in value is
provided by the second-level lookahead circuit, the multiplexer selects the correct sum.
The photo below shows how the complete multiplier is constructed from 8-bit blocks.
The multiplier produces a 69-bit output; there are 5 "extra" bits on the left.
Note that the second-level Kogge-Stone blocks are larger on the right than the left since the lookahead circuitry is more complex for higher-order bits.
The full adder circuit. This is the same image as before, but hopefully it makes more sense at this point.
Going back to the full ×3 circuit above, you can see that the 
8 bits on the right have significantly simpler circuitry.
Because there is no carry-in to this block, the carry-select circuitry can be omitted.
The block's internal carries, generated by the Kogge-Stone lookahead circuitry, are added using exclusive-NOR gates.
The diagram below shows the implementation of an XNOR gate, using inverters and a multiplexer.
The XNOR circuit
I'll now describe one of the multiplier's circuits at the transistor level, in particular an XNOR gate.
It's interesting to look at XNOR because XNOR (like XOR) is a tricky gate to implement and different processors use very different approaches. 
For instance, the Intel 386 implements XOR from AND-NOR gates (
details
) while the
Z-80 uses pass transistors (
details
).
The Pentium, on the other hand, uses a multiplexer.
An exclusive-NOR gate with the components labeled. This is a focus-stacked image.
The diagram above shows one of the XNOR gates in the adder's low bits.
11
The gate is constructed from four inverters and a pass-transistor multiplexer.
Input B selects one of the multiplexer's two inputs: input A or input A inverted. The result is the XNOR function.
(Inverter 1 buffers the input, inverter 5 buffers the output, and inverter 4 provides the complemented B signal to drive the multiplexer.)
For the photo, I removed the top two metal layers from the chip, leaving the bottom metal layer, called M1. 
The doped silicon regions are barely visible beneath the metal.
When a polysilicon line crosses doped silicon, it forms the gate of a transistor.
This CMOS circuit has NMOS transistors at the top and PMOS transistors at the bottom.
Each inverter consists of two transistors, while the multiplexer consists of four transistors.
The BiCMOS output drivers
The outputs from the ×3 circuit require high current.
In particular, each signal from the ×3 circuit can drive up to 22 terms in the floating-point multiplier.
Moreover, the destination circuits
can be a significant distance from the ×3 circuit due to the size of the multiplier.
Since the ×3 signals are connected to many transistor gates through long wires, the capacitance is high, requiring high current to change the
signals quickly.
The Pentium is constructed with a somewhat unusual process called BiCMOS, which combines bipolar transistors and CMOS on the same chip.
The Pentium extensively uses BiCMOS circuits since they reduced signal delays by up to 35%.
Intel also used BiCMOS for the Pentium Pro, Pentium II, Pentium III, and Xeon processors.
However, as chip voltages dropped, the benefit from bipolar transistors dropped too and BiCMOS was eventually abandoned.
The schematic below shows a simplified BiCMOS driver that inverts its input.
A 0 input turns on the upper inverter, providing current into the bipolar (NPN) transistor's base.
This turns on the transistor, causing it to pull the output high strongly and rapidly.
A 1 input, on the other hand, will stop the current flow through the NPN transistor's base, turning it off.
At the same time, the lower inverter will pull the output low. (The NPN transistor can only pull the output high.)
Note the asymmetrical construction of the inverters. Since the upper inverter must provide a large current into the NPN transistor's base, it is designed to produce a strong (high-current)
positive output and a weak low output.
The lower inverter, on the other hand, is responsible for pulling the output low. Thus, it is constructed to produce a strong low output, while the
high output can be weak.
The basic circuit for a BiCMOS driver.
The driver of the ×3 circuit goes one step further: it uses a BiCMOS driver to drive a second BiCMOS driver.
The motivation is that the high-current inverters have fairly large transistor gates, so they need to be driven with high current (but not as much as they produce, so there isn't an infinite regress).
12
The schematic below shows the BiCMOS driver circuit that the ×3 multiplier uses.
Note the large, box-like appearance of the NPN transistors, very different from the regular MOS transistors.
Each box contains two NPN transistors sharing collectors: a larger transistor on the left and a smaller one on the right.
You might expect these transistors to work together, but the contiguous transistors are part of two
separate circuits.
Instead, the small NPN transistor to the left and the large NPN transistor to the right are part of the same circuit.
One of the output driver circuits, showing the polysilicon and silicon.
The inverters are constructed as standard CMOS circuits with PMOS transistors to pull the output high and NMOS transistors to pull the output low.
The inverters are carefully structured to provide asymmetrical current, making them more interesting than typical inverters.
Two pullup transistors have a long gate, making these transistors unusually weak.
Other parts of the inverters have multiple transistors in parallel, providing more current.
Moreover, the inverters have unusual layouts, with the NMOS and PMOS transistors widely separated to make the layout more efficient.
For more on BiCMOS in the Pentium, see my article on
interesting BiCMOS circuits in the Pentium
.
Conclusions
Hardware support for computer multiplication has a long history going back to the 1950s.
13
Early microprocessors, though, had very limited capabilities, so microprocessors such as the 6502 didn't have hardware support for multiplication;
users had to implement multiplication in software through shifts and adds.
As hardware advanced, processors provided multiplication instructions but they were still slow.
For example, the Intel 8086 processor (1978) implemented multiplication in microcode, performing a slow shift-and-add loop internally.
Processors became exponentially more powerful over time, as described by Moore's Law, allowing later processors to include dedicated multiplication hardware.
The 386 processor (1985) included a
multiply unit
, but it was still slow, taking up to 41 clock cycles for a multiplication instruction.
By the time of the Pentium (1993), microprocessors contained millions of transistors, opening up new possibilities for design.
With a seemingly unlimited number of transistors, chip architects could look at complicated new approaches to squeeze more performance out of a system.
This ×3 multiplier contains roughly 9000 transistors, a bit more than an entire Z80 microprocessor (1976).
Keep in mind that the ×3 multiplier is a small part of the floating-point multiplier, which is part of the floating-point unit in the
Pentium.
Thus, this small piece of a feature is more complicated than an entire microprocessor from 17 years earlier, illustrating
the incredible growth in processor complexity.
I plan to write more about the implementation of the Pentium, so
follow me on Bluesky (
@righto.com
) or
RSS
for updates. (I'm no longer on Twitter.)
The
Pentium Navajo rug
inspired me to examine the Pentium in more detail.
Footnotes and references
