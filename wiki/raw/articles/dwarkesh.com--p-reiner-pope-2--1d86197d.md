---
title: "Reiner Pope - Chip design from the bottom up"
url: "https://www.dwarkesh.com/p/reiner-pope-2"
fetched_at: 2026-05-23T07:01:05.785719+00:00
source: "dwarkesh.com"
tags: [blog, raw]
---

# Reiner Pope - Chip design from the bottom up

Source: https://www.dwarkesh.com/p/reiner-pope-2

New blackboard lecture with Reiner Pope: how do chips actually work - starting with basic logic gates, and working up to why GPUs, TPUs, FPGAs, and the human brain each look the way they do.
Reiner
is CEO of
MatX
, a new chip startup (full disclosure - I’m an angel investor). He was previously at Google, where he worked on
software
efficiency
, compilers, and TPU architecture.
Watch this one on
YouTube
so you can see the chalkboard.
Crusoe
was one of only five GPU clouds that made the gold tier in SemiAnalysis’ most recent ClusterMAX report. Gold-tier providers like Crusoe delivered 5-15% lower TCO than silver-tier clouds, even with identical GPU pricing. This is because optimizations like early fault detection and rapid node replacement don’t necessarily show up in the sticker price, but still matter a ton in the real world. Learn more at
crusoe.ai/dwarkesh
Cursor
is where I do most of my work—from reading research papers to visualizing technical concepts to coding up internal tools for the podcast. Most recently, I used it to build two different review interfaces for my essay contest, one that anonymizes submissions for scoring and another that lets me see applicants’ essays next to their resumes and websites. Whatever you’re working on, you should try doing it in Cursor. Get started at
cursor.com/dwarkesh
Jane Street
let me ask Ron Minsky and Dan Pontecorvo, two senior Jane Streeters, a bunch of questions about how they use AI. We discussed everything from the types of models they’re training to how they think about the future of trading to why they’re more bullish than ever on hiring technical talent. You can watch the full conversation and learn more about their open positions at
janestreet.com/dwarkesh
00:00:00 – Building a multiply-accumulate from logic gates
00:16:31 – Muxes and the cost of data movement
00:26:10 – How systolic arrays work
00:39:11 – Clock cycles and pipeline registers
00:51:51 – FPGAs vs ASICs
01:03:25 – Cache vs scratchpad
01:07:27 – Why CPU cores are much bigger than GPU cores
01:12:00 – Brains vs chips
01:15:33 – A GPU is just a bunch of tiny TPUs
Dwarkesh Patel
I’m back with
Reiner Pope
, CEO of
MatX
, a new AI chip company.
Last time
we were talking about what happens inside a data center. Now I want to understand what happens inside an AI chip. How does a chip actually work? Full disclosure, by the way: I am an angel investor in MatX. So hopefully you have designed a good chip.
Reiner Pope
Hope so. I’ll start with the smallest fundamental unit of
chip design
, and we’ll build up to what an actual production chip is and what its components are. At the very bottom level of a chip, the primitives we work with are
logic gates
, very simple things like AND, OR, and NOT. These are connected together by wires that have to be laid out physically as metal traces on a chip.
The main function that AI chips want to compute is the
multiplication of matrices
. Inside that, the fundamental primitive is a
multiply-accumulate
of pairs of numbers. We’re going to demonstrate what that calculation looks like by hand, and then infer what a circuit would look like for that.
It’ll be easiest if I do a multiply-accumulate of a four-bit number with another four-bit number. The clearest primitive is actually multiply-accumulate. So there’s a multiply of these two terms, and then we’re going to add in an eight-bit number.
Dwarkesh Patel
Can I ask a clarifying question? Why is this the natural primitive for whatever computation happens inside a computer?
Reiner Pope
There are a few reasons. It’s a little bit more efficient, but the reason it’s natural for AI chips is that if you look at what’s happening during a matrix multiply… What is a matrix multiply in short? There’s a for-loop over
i
, over
j
, and over
k,
of output [
i
,
k
] += input [
i
,
j
] x other input [
j
,
k
]. A multiply-accumulate happens at every single step of a matrix multiply.
The other observation is that the precision will almost always be higher in the accumulation step than in the multiplication step. This is specific to AI chips. You’re multiplying low-precision numbers, and then when you accumulate, errors accumulate quickly, so you need more precision there. This is why we’ve chosen to do a four-bit multiplication and an eight-bit addition.
Dwarkesh Patel
Let me make sure I understood that. There are two ways to understand that. One is that the value will be larger than the inputs. The other is that if it was a floating-point number it would be… Maybe that part is less intuitive to me. But maybe it’s the same principle?
Reiner Pope
It really is the same principle. The separate principle is that as you’re summing up this number, you’re summing up a whole bunch of numbers, so you’ve got a lot of rounding errors accumulating. Whereas in this case, there’s only one multiplication in the chain, so there aren’t a lot of rounding errors accumulating in the multiplication.
Dwarkesh Patel
Why are you summing up a whole bunch of numbers? There’s just two numbers there.
Reiner Pope
This summation is repeated
j
many times.
Dwarkesh Patel
Any errors accumulate. I see.
Reiner Pope
So how would we perform this calculation by hand? As a human, we would probably separate it into two, but we can do it all in one using long multiplication.
For the multiplication term first, we’re going to multiply this four-bit number by every single bit position in the other four-bit number. We write that out. First, 1001 multiplied by this bit position. That is the number itself. Then shifted across by one, we’re multiplying by 0. That gives us an all-0 number. Shifted across one more to multiply by this one, we get 1001. Finally, for this last bit position, we get an all-0 number again.
This gives us a bunch of terms that we have to add for the multiplication. While we’re doing that summation, we might as well add in the actual accumulator term as well. So we just copy that directly across. So this is the sum. It’s a five-way sum that we want to compute.
What logic gates did it take us to get to this intermediate step? We needed to produce all 16 of these partial products. How do I produce one of these partial products? Let’s take this number 1, for example here. We produce it by multiplying this number by this one over here. We can produce that with an
AND gate
. This number is 1 if both this bit is 1 and this bit is 1. If either of them is 0, then the multiplication of 0 times anything is 0. To produce all of this, we ended up consuming 16 AND gates. In the general case, if I were doing a
p
bit multiply times a
q
bit multiply, this will be
p
times
q
many ANDs.
Finally, I sum them. Most of the work is going to happen in the summing. Let me describe the other logic gate that we use here. AND is almost the simplest logic gate that exists on a chip. It’s almost the smallest. At the other extreme, the very largest logic gate you’ll typically use is something called a
full adder
.
Coming from software, you might think that a full adder adds 32-bit numbers together. In this case, it just adds three single-bit numbers together, so you can think of it as adding 0, 1, and 1 together. When I add these together, the result can be 0, 1, 2, or 3, so I can express that in binary using just two bits. As input, it has three bits. As output, it has two bits. The number 2 in binary is 10. This is also known as a 3→2 compressor because it takes three bits of input and produces two bits of output.
Dwarkesh Patel
Just to make sure I understood: the two inputs are an X and a Y value and then some carry that came in…
Reiner Pope
The three inputs are all bits in the same bit position, like three bits in a column here. The two outputs, I’ve drawn them vertically here and horizontally here to match this vertical versus horizontal layout. This expresses that things in the same column are in the same bit position, whereas things in adjacent columns are different. This is a carry out, whereas this was the sum.
Dwarkesh Patel
So if the inputs in the full adder were, say, 101, then the output would be 10. If it were 111, it’d be 11. If it were 000, it’d be 00. If it were 010, it’d still be 01. Got it.
Reiner Pope
Yeah. It’s essentially just counting the number of things and expressing that in binary. This circuit captures what we as humans naturally do when we’re summing along a column.
I’ll show one iteration of using the full adder to sum. The way I sum here is going to be a little unnatural for humans. We would sum along the column and then remember the carry, but instead of remembering the carry, we’ll explicitly write it out. We proceed from the rightmost column toward the left. On the rightmost column, we sum the 1 and the 1, and that produces a zero here and a carry of one. We’ve used this full adder circuit on this pair of bits and produced a pair of bits as output.
Now we can do the same thing with this column. We have a column of four numbers, so we’ll take the first three of them, run a full adder on them, and that gives us a 0 and a 0 as output. The sum of these is 00. That’s the full adder applied to all these bits. As I’ve used up bits, I’ll cross them out to indicate that I’ve handled them.
Let’s keep going a little bit more. I take these three numbers, I add them, and that gives me a 1 and a 0. I’ve dealt with these three numbers. Now I take these three numbers and add them, and that gives me a 1 and a 0, and I’ve dealt with these numbers.
The way to view this is that I have this whole grid of numbers that need to be added. I’m going to keep applying full adders to all the bits here, constantly removing three numbers from a column and writing out two numbers as output. Keep going over and over again until I eventually get just one single number coming out.
This approach is called a
Dadda multiplier
. This is the standard for how you do area-efficient multipliers using full adders. Let’s try to quantify the circuit size of this so we have a sense of how big things are and can compare them later.
How many full adders did I use? How many numbers did I start with? I have the 16 partial products, which is a product of all of these terms with all of these terms, plus the eight terms that I’m adding here. I started off with 24 bits. Eventually I produced eight bits on the output. In every step, I was crossing off three numbers and writing two numbers out as a result.
Every single use of a full adder eliminates one of the bits here. So how many full adders? It must be 24 minus 8, so there were 16 full adders in this circuit. This is true in the general case as well. There will be
p
times
q
many full adders in this circuit.
Dwarkesh Patel
Let me make sure I understand the logic of that. The input bits, 24, is
p
x
q
, plus
p
+
q
. The output bits are just
p
+
q
. So
p
x
q
plus
p
+
q
, minus
p
+
q
equals
p
x
q
.
Reiner Pope
That’s right. I think this explains, or at least hints at, the second reason we chose to do a multiply-accumulate. The first reason is that it’s what shows up in matrix multiplication. The second is that it gave us this very slick, simple
p
x
q
, very simple algebra.
We’ve described this whole procedure. Every single atomic step that I took here becomes a logic gate, and then the wires are connected together. When I had these three inputs that I used to produce these two outputs, if I think of mapping this to a physical device, there would be a wire connecting all three of these things together into a logic gate that produced this output.
This is the main primitive, at different bit widths, that’s inside an AI chip. We’re going to build up from here to how you would use it to run all the other operations you might want.
Dwarkesh Patel
This might be the wrong time to ask, but whenever Nvidia reports that this chip can do X many
FP4
or half as many
FP8
, it seems to imply those circuits are fungible, that there’s not a dedicated FP4 versus FP8. But the way you’re mapping it out here, it seems like if it has to be mapped out in the logic, you would need a dedicated FP4 multiply-accumulate and then a dedicated FP8 accumulate. Can you “funge” them?
Reiner Pope
As drawn, they’re not particularly fungible. This is actually one of the main choices you have to make when designing a chip: how much of FP4 and how much of FP8 do I have? Sometimes I’ll make that consideration from the point of view of the customer requirement. Another angle is to equalize the power budget between FP4 and FP8.
Dwarkesh Patel
When they report those numbers and it just happens to be the case that it does 2x as many FP4 as FP8, they’re just choosing to give equivalent
die
areas to all the floating points, and as a result it ends up being…?
Reiner Pope
Why is the ratio exactly 2x? Part of it is that surely it won’t be exactly equivalent to die area. There’s a data movement reason. We’ll maybe come back to this when we look at how it goes into and out of memories. There’s something really nice from a software level about the fact that I can pack two four-bit numbers into the same storage as an eight-bit number. When I store that to memory, the sizing of the buses that I wire out within the chip makes that work out really nicely.
Dwarkesh Patel
Come to think of it, it’s not just 2x. The amount of area it takes sounds like it’s quadratic with the bit length. That’s why smaller precision is even more favorable than you might think.
Reiner Pope
This is a really big reason. In fact, Nvidia made a change. Historically, up until
B100
or
B200
, every time you halved the bit precision, you doubled the
FLOP
count. For the reason you said, because of this quadratic scaling, that ratio is actually slightly wrong. You should get an even bigger speedup than you might otherwise think. Nvidia’s product specs have started acknowledging that in
B300
and beyond, where the FP4 is three times faster than the FP8.
Dwarkesh Patel
Though it should be 4x.
Reiner Pope
Yeah. What I’ve shown here is the simplest case of integer multiply. When you’re dealing with floating point, as you do in FP4 and FP8, there’s this other term, the exponent, that complicates the calculation.
What can we see already from this? I think the big observation you’ve made is that there’s this quadratic scaling with bit width, which is very effective and is the single reason low-precision arithmetic has worked so well for
neural nets
. The other thing we’re going to do now is compare the area spent on the multiplication itself with all the circuitry around it.
Reiner Pope
We’ll walk back in time a little bit and see how
GPUs
prior to
Tensor Cores
worked, which is in fact the same way
CPUs
worked. Where do we stick this multiply-accumulate unit? Generically, I’ll describe a
CUDA
core or a CPU. You’ll have some
register file
which stores some number of entries, maybe eight entries of, in this case, 4-bit numbers, but typically 32-bit numbers.
Inside the CUDA core, I’ll have some register file of some depth, and then I’ll have my multiply-accumulate circuit. What it’s going to do is take three arbitrary registers from this register file, perform the multiply-accumulate, and then write back to the register file. It’s going to write to this one, but it was able to read from this one, this one, and another random one. It will take three inputs like this.
This is the core data path of many processors. Most processors look like this. You’ve got some set of registers, and then you’ve got some set of logic units, or
ALUs
. We want to analyze the cost of the data movement from the register file to the ALU and back.
Ultimately, there’s going to be some circuit that says, “Well, I don’t always have to select this guy. I might select any of the registers at any point in time.” The first question is: how can I build a circuit? The circuit I’m going to look for is a
mux
. In this case, it’s going to have eight inputs, one from each entry of the register file, and it’s going to have one output, which is actually producing this output.
What is the cost of this thing? All we have to build it out of is AND and
OR
. How do we build it? We do the dumbest thing possible. We form a mask. When we want to read the third entry, we’re going to AND every single entry with either 1 or 0 based on whether that’s what we want to read, and then we’re going to OR all of them together.
Dwarkesh Patel
Just to make sure I understand the basics. What the mux is doing is just selecting an input?
Reiner Pope
Just selecting, invisible to software. You say “I want input number three,” and that means there’s a mux here.
So what is the cost of this mux? An
n
-input mux operating on
p
bits. I have
n
rows. That’s just eight rows, and each row is
p
bits wide. I have to AND every single bit, so I get
n
x
p
many AND gates. For every single input I have to decide whether I’m going to
mask it out
or not. Then I’m going to OR them all together.
There’s going to be
n
– 1 times
p
many OR gates. I’ve got all of these different things, almost all of them are 0s, but I need to collapse them from my eight options down into one option. Every step, I need to OR one row into an existing row.
Dwarkesh Patel
It’s actually funny that you don’t think at the level of hardware. You just think, “Oh, I’ll just select element three,” and something as simple as that is in and of itself quite a complicated circuit.
Reiner Pope
This is the first step of all of the hidden data movement costs that show up. We’re just going to compare. I have to pay this cost. I’ve got one mux here, and in fact I have two more copies of that for each of the three inputs to my multiply-accumulate operation. I have this cost, which is 3 x
n
x
p
AND gates over here, compared to
p
x
q
gates in the actual circuit that is doing the thing I care about.
If we plug in actual numbers, with
n
being eight, I get 24 x
p
gates just in the data movement, compared to—if
q
is four—4 x
p
gates just in the multiply-adder.
Dwarkesh Patel
Where is the three coming from?
Reiner Pope
Three different inputs here. What I’m hinting at is that all of this work, which scales as the size of the register file—and this is a very small register file—all of this work just moving the data from the register file to the logic unit is many, many times more expensive than the logic unit.
Dwarkesh Patel
It may be helpful to just see what a mux looks like, maybe a two-bit or a four-bit mux.
Reiner Pope
We’ll do a two-way mux. We’ve got two different numbers, we’ve got these two inputs. These are the inputs that are being selected between, and the selector can either be “I want this one” or “I want the other one.” This is a
one-hot
encoding.
This is what we start with. Let’s focus on this case. This is the actual input we got, and we want to produce this guy as the result. Very laboriously, we AND this bit with all of these. That produces ANDing this bit with this row. Likewise, we AND this bit with this row. That produces all 0s. There are four ANDs here.
Finally, we OR these two together, and this gives a 1. We OR these two together, this gives a 1. We OR these two together, it gives a 0. We OR these two together and it gives a 1. Those are the four ORs. This actually ends up looking a little bit like addition. We did exactly the same set of ANDs. We’ve ANDed all of these things together, but then instead of collapsing it by using full adder circuits, we just get a very simple collapsing with OR gates.
Dwarkesh Patel
But that doesn’t look like
n
times
p
.
Reiner Pope
This was with
n
=2 inputs. In the general case, we will have
n
rows, and we’ll have
p
bits per row. That gives us the
n
times
p
many AND gates. In this circuit I’ve described, almost all of the cost, seven-eighths of the cost, is in reading and writing the register file, and only a tiny fraction of the cost is in the logic unit itself.
This is the problem to solve. This essentially was the state of play prior to the
Volta generation
of Nvidia GPUs. This kind of thing is what was inside the CUDA cores. This problem statement is what motivated the introduction of Tensor Cores, which are more generically called
systolic arrays
.
Think about how we’re going to solve this problem. We’re spending almost all of our circuit area on something that we really don’t care about and is hidden to the software programmer, and the thing that we actually care about is not much of the area. Make this one bigger somehow while keeping this at the same size. That’s the goal.
Reiner Pope
The evolution was that we had baked this much into hardware at this stage. This single line is a multiply-accumulate, and this single thing was baked into hardware. The idea of a systolic array is to go two levels of loops up and bake this entire loop out here into hardware. The idea is that if we have a much bigger granularity fixed-function piece of logic, maybe the taxes we pay on the input and output are much smaller.
Dwarkesh Patel
Interesting. It sounds like you’re suggesting that if you go up one step in the matrix multiply loop, you can tilt the balance more towards compute than communication.
Reiner Pope
That’s right. There are two effects we’re going to take advantage of here. One is that we can do more stuff per every trip through our register file. The other is that in some of this loop, we can take advantage of certain things staying fixed.
Visually, we’re going to look at this matrix multiplication. This portion of the loop corresponds to a
matrix-vector multiplication
. We’ll take a matrix and multiply it by a vector. How do we do this? Every column gets multiplied by the vector and then summed. We’re going to sum along columns.
This 0 and 3 gets multiplied by the 3 and 7 and gets summed, and then the 1 and 2 gets multiplied by the 3 and 7 and gets summed. There is a multiply-accumulate associated with every single one of these entries in the matrix. We’ll draw out these four multiply-accumulates.
Dwarkesh Patel
Just to make sure I understand why there are four multiply-accumulates: each entry in the column that corresponds to the output vector is a
dot product
, and in this case it will be two multiplications and then the addition of those two multiplications. You’re accumulating...
Reiner Pope
Really there’s only one addition per dot product, but we like to start with zero.
Dwarkesh Patel
But it includes the initialization of zero.
Reiner Pope
Yeah. We want to have quadratically more compute. We have
x
times
y
as much compute as we had before. But we want to aim for having only
x
times as much communication. The intention is to get this advantage term going as
y
.
We’ve laid down the multiplications. We want to bring in a vector of size two, and that is already in line with our columns target. That’s fine. However, we need to manage the communication of this matrix, which exceeds our budget of
x
.
The idea is that in an AI context, this matrix is going to stay fixed for a long period of time. We’ve got some register files sitting over here.  The amount of stuff coming out of this register file… this is the term that we want to go as
x
, in some sense. We don’t want to bring this full matrix in from the register file every cycle, because that would cost too much in terms of wiring from the register file.
Our key trick is that this matrix can be stored locally to the systolic array. We’ll store these numbers 0, 1, 2, and 3 in a gate called a register that physically stores these numbers, and we’re going to reuse these numbers over and over again for a large number of different vectors.
Dwarkesh Patel
The optimization here is that the nature of matrix multiplication is that you can store this square quadratic thing directly where the logic is happening, which has an extra dimension compared to the inputs that you keep swapping in and out.
Reiner Pope
That’s right.
Dwarkesh Patel
This is the nature of what a matrix multiplication is. You do a lot of multiplication to get one value out. A dot product is the result of a lot of multiplications. So that optimization means you can stuff a lot of multiplication in before you get some value out of it.
Reiner Pope
That’s right. Just to complete the picture of concretely how that looks: I swapped the 3 and the 2 here. Just like this 0 and 3 is going to multiply by the 3 and the 7, we’re going to form a dot product along columns here. We’re going to feed a 3 and a 7 in here. This feeds into this multiplication and also feeds into this multiplication. Likewise, the 3 feeds into here and also into here. Then we’re going to sum along here. Starting at the top of a column, we feed in 0s, and then coming out the bottom we get results.
Visually, there’s a dot product performed along columns in a matrix, and that maps exactly to what is done spatially in the systolic array. This is one dot product summed vertically, and this is a second dot product also summed vertically.
What is the data that needs to go into and out of the register file? We have
x
amount of data coming out on the output, and we also have
x
amount of data coming from the input. With respect to the input and output vectors at least, we’ve met our goal of having only
x
as much data going in and out of the register file.
This leaves open the question: I said the weight matrix is stored locally in the systolic array, so how did it get there in the first place? At some point, you need to boot your chip and populate this data, so where did that come from?
The trick is that we just do it very slowly. We very slowly trickle-feed it into the systolic array. The simplest strategy is that we run this daisy chain: feed a number in here, and on the next clock cycle it will move down to the next entry of the systolic array. We can do that in every column in parallel, this is also going to come from here, and that gives us another factor of approximately
x
units of bandwidth coming in.
Dwarkesh Patel
Would you mind repeating that sentence one more time?
Reiner Pope
We know that we’re going to be bringing numbers only rarely into the matrix. We just want to come up with any construction at all such that the amount of wiring that crosses the boundary of the systolic array is bounded to
x
and not go as
xy
.
A particularly simple strategy is that we bring a number into the top row of the systolic array in one clock cycle. Then, for
y
consecutive clock cycles, we bring in the top row every time and shift all the other rows down by one. This keeps the wiring that needs to come from this expensive register file only down to a factor of
x
rather than
xy
.
Dwarkesh Patel
I see. There are two questions in terms of communication: communication time and communication bandwidth. You’re saying that since we’re only going to be loading this in once, let’s minimize bandwidth, because bandwidth equals die area. We load it in slowly over smaller lanes because we’re just going to keep this value in there for a while.
Reiner Pope
Exactly.
Dwarkesh Patel
It’s interesting to me that when we were talking last time about inference across many chips, the big high-level thing we’re trying to optimize for is increasing the amount of compute per memory bandwidth, that is to say, per communication. Here also, we’re trying to increase the amount of actual multiplies or additions relative to transporting information from registers to the logic. In both cases, you’re trying to maximize compute relative to communication.
Reiner Pope
This shows up all the way up and down the stack. This is close to the bottom, to the gates. There’s a version that’s maybe even closer to the gates in the precision of the number format that you choose to use. We saw that same effect. There’s a squared versus linear term going on both purely in the precision of the ALU, but also in the size of the matrix.
This unit is the next bigger unit. We had the multiplication circuit, and on top of that we have a pretty large systolic array. I drew it as 2x2, but older
TPUs
were described as 128x128 of this circuit shown here. This ends up being the most efficient known circuit for implementing a matrix multiply.
Dwarkesh Patel
We’ve talked about how it seems obvious that you should try to maximize compute relative to communication. What are non-obvious trade-offs that keep you up at night, about whether you should do X or Y and it’s not obvious what the answer is?
Reiner Pope
Most of the decisions in chip design are sizing decisions. Already in what we’ve drawn so far… AI chips all have this circuit in them. They have a systolic array, and somewhere near it a register file providing inputs and outputs.
Even within this scope, the sizing questions you have are: how big should I make my systolic array, and how big should I make the register file? These two questions are coupled. One way to think of it is to set a budget for what percentage of chip area you want to spend on data movement. Maybe I say that I want this to be 10% and the systolic array to be 90%.
Then I can size my register file. Bigger register files are more flexible. They allow me to get more application-level performance out, but they take away from the area spent on the systolic array.
Dwarkesh Patel
Where does the
clock cycle
of a chip come in? What determines what that is? And what is a clock cycle of a chip?
Reiner Pope
At baseline, it’s worth observing that chips are incredibly
parallel
. You’ve got 100 billion transistors in a chip. A key thing you need to do whenever you have massive parallelism is synchronize between the different parallel units.
In software, typically you have these very expensive synchronization methods like a
mutex
. One thread will finish what it’s doing, grab a lock stored somewhere in memory, and notify the other thread that it’s done. On chips, we take a very different approach. Every nanosecond or so, all circuitry in the chip will pause for a moment and synchronize. That is the clock cycle. The entire chip typically goes in lockstep to the next operation in one fell swoop.
What this looks like in circuitry is that the clock is mediated by registers, which are these storage devices we’ve drawn elsewhere. The way to think of it is: I have some storage holding a bit, which might be 0 or 1. Then I have some cloud of logic, which maybe is this systolic array or multiplier. I have a bunch of inputs feeding into this cloud of logic, and eventually there’s going to be some output register that it writes to.
There is a global clock signal driving all these registers. At a certain instance in time, when the clock strikes, whatever value happens to be on that wire at that instant is what gets stored.
The challenge is that I would like to have my clock speed run as fast as possible. If I run at two gigahertz, I get twice as many operations done per second as if I run at one gigahertz. But what that ends up meaning is that I’m very sensitive to the delay through this cloud of logic, because any computation happening in there needs to finish before the next clock cycle hits. A major point of optimization on any chip is to make this delay as short as possible.
Dwarkesh Patel
Interesting. The constraint here seems to be that if you add too much logic, you might risk missing the clock cycle. But if you don’t add enough, you’re leaving potential compute on the table. Is there ever a situation where you take a probabilistic chance that a computation finishes, or is it strictly that it either finishes by the clock cycle or it doesn’t?
Reiner Pope
In standard chip design, you margin it such that there is a probability, but it’s many standard deviations out. For all intents and purposes, it is a reliable part and will always meet the clock.
There are some weird exceptions, like
clock domain crossings
where you go from one clock to another. Then you actually do have to reason about this probability. But in the main path, you margin it such that you’ll get there 25% of the clock cycle in advance, making it very unlikely that it misses.
Dwarkesh Patel
Where the clocks synchronize, where the registers are, is this something you determine as a chip designer? Or is it an artifact where you want a certain sequence of logic, and the software you use to convert your
Verilog
into what you send to
TSMC
just determines that to make it work, you have to put a register here, here, and here, making sure no single step makes the whole chip’s clock cycle longer than it has to be?
Reiner Pope
Inserting them is actually a huge part of the work of designing a chip. It’s done by a combination of manual and automatic methods.
To show the very dumb version of what you can do here, you can take this logic and split it in half. Instead of just one cloud of logic, I can have two smaller clouds of logic that do the same thing, but split them up by a register. If you split it in the middle, you can hit twice the clock frequency. That’s great, you get twice the performance, but at the cost of an extra register, which means more storage.
Dwarkesh Patel
Stepping back, why do we need to synchronize the whole chip? If you imagine playing
Factorio
or something, there’s no global clock cycle. Things are just done when they’re done. There’s iron on the plate, and you can take it if you want.
Reiner Pope
Taking that analogy, the thing you need to be mindful of is if I have two different paths through some logic. Say I have to do computation
f
here and computation
g
here, and they’re going to meet for computation
h
.
There’s going to be manufacturing variance. In some chips
f
will take a little longer; in some chips
g
will take a little longer. If I have a signal propagating through, and the results from
f
and
g
have to meet up at
h
, what can go wrong is that
f
gets there early and it meets the previous value of
g
, or the next value of
g
.
Dwarkesh Patel
Ah. And
h
needs to know when to start, when the next iteration has…
Reiner Pope
Exactly.
Dwarkesh Patel
This explains why different chips made at the same process node, the same TSMC technology, can have different clock cycles. Two chips made at
3 nm
might have different clock cycles based on whether they were able to optimize to ensure no single critical path is so long that it slows down the whole chip’s clock cycle.
Reiner Pope
That’s right. This optimization I showed here is called
pipeline register insertion
. We’ve inserted a register in the middle of the pipeline. This is a pure trade-off between clock speed and area. That is the easy case. There is a harder case too. I drew out a pipeline of logic, but in other cases you may have some calculation which actually feeds back in on itself. It runs some function
f
and then writes back to itself. For example, this might be an addition where you’re adding a number every clock cycle. This little circuit essentially sums all the numbers presented on different clock cycles.
The challenge is, if this plus takes too long, what can I do? If I try to put a pipeline register right in the middle of it, it changes the computation that’s done. Instead of forming a running sum of everything that comes in, I will actually have two different running sums. I’ll end up with a running sum of the even numbers and a running sum of the odd numbers. This constraint—where I have a loop in my logic, which all chips have somewhere—is the hardest thing to address and sets the clock cycle.
Dwarkesh Patel
I don’t understand why it would be a problem to have that. I’m not even sure what it would mean to have a register there. Is it a sort of atomic operation?
Reiner Pope
Well, plus is not really atomic.
Dwarkesh Patel
As you just demonstrated.
Reiner Pope
It took a whole lot of work to do a summation. You can take the early parts of that work, stick a register in the middle, and then take the late parts of that work.
Dwarkesh Patel
Okay. TSMC offers a
PDK
which specifies the primitives of logic they can grant you in the chip. It’s up to them to determine that no primitive is bigger than the clock cycle they’re hoping a process node targets. But other than that, can’t you just take all the primitives from TSMC and keep adding registers between them as much as needed until you get to your desired clock cycle?
Reiner Pope
As a logic designer, the chip architect sets the clock cycle. For example, the primitives you get from TSMC are on the order of AND gates or full adders. It depends a lot on voltage and which library you choose, but generally you can have about 10, 20, or 30 of these sequentially in a clock cycle. These primitives are very fast, maybe 10 picoseconds.
As a logic designer, in principle, if you just had a register and an AND gate in a loop, you could get an insanely fast clock speed, more than four, five, or six gigahertz. But if you take this really simple circuit and look at the area you’re spending here… This is called one gate equivalent in size, so unit of one in area. This thing is maybe a unit of eight in area.
Again, almost all your cost becomes synchronization or communication cost compared to the actual logic. This would be a case where you’ve gone too far. You’ve made your clock speed really fast at the cost of spending almost all of your area on pipeline registers.
Dwarkesh Patel
Interesting. So you’re hinting at a dynamic where you can have a really fast clock speed but you’re not getting that much work done. You can have low latency but low throughput.
Reiner Pope
It hurts your throughput, in fact, because the throughput of your chip is the product of how much you get done per clock cycle—which is based on area efficiency—times how many clocks you get per second.
Dwarkesh Patel
This is actually so similar to the thing we were discussing last time about batch size, where if you have a low batch size, any one user can receive their next token really fast, but the total number of tokens processed in, say, an hour will be lower than it could otherwise be.
Reiner Pope
Exactly. You get less parallelism out if you drive your clock speed up really high.
Dwarkesh Patel
I remember talking to an
FPGA
engineer at
Jane Street
, Clark, who helped me prep for the previous interview we did together. He was explaining why they use FPGAs. I imagine that for high-frequency trading, throughput is less important than latency, so having very specific control over the clock cycle in a deterministic way is the most important thing. Maybe it’d be interesting to talk about why you can’t just achieve that with an
ASIC
, or why you might use an FPGA to have deterministic clock cycles for
high-frequency trading
.
Reiner Pope
Let’s consider the business case for an FPGA versus an ASIC. FPGAs and ASICs use largely the same conceptual model. You have a series of gates built from small primitives—ANDs,
ORs
,
XORs
—connected together with wires running in a fixed clock cycle. Anything you can express in an FPGA you can express in an ASIC too. It will be about an order of magnitude cheaper and have better energy efficiency on an ASIC than an FPGA.
The trade-off is that the first FPGA costs you $10,000, whereas the first ASIC you make costs $30 million because it requires an entire
tape-out
. The business use case for an FPGA is when you want something that has very
deterministic latency
, fast runtime, and high parallelism, but you are going to change the workload frequently, maybe every month. You don’t want to pay that tape-out cost every time.
How does an FPGA actually emulate the ASIC programming model in a fixed piece of hardware? At its core, it has the two components we just talked about. It has registers as storage devices, and it has
lookup tables
(LUTs) which provide all of the gates.
Then there’s a third component. We have a swarm of these registers and LUTs, and they are connected by a big set of muxes. In front of every single one of these, we have a mux which selects an input from everywhere else. We have a whole bunch of different options feeding into all of these things.
What this allows is essentially that when I program my FPGA, I can take all of these components and superimpose a particular wiring which goes through this LUT, feed it into another LUT, send it to this register, and then feed it into another LUT, or something like that.
What I’ve drawn in orange is how you… FPGA means Field-Programmable Gate Array. The orange is what has been programmed in the field, whereas the white is all the wires that must exist in the FPGA in order to actually make the device in the first place.
Dwarkesh Patel
What does it mean to be programmed in the field?
Reiner Pope
Programmed in the field means the device is being deployed in a data center. It’s sitting out in the world, and then you can come and program it.
Dwarkesh Patel
Ah, not field as in like electric field. Field as in like out there in the world, ok.
If I look at how the field programming comes out of the first lookup table and goes into a second one, how does that work?
Reiner Pope
Where are the wires that make that happen? I got a little bit lazy in drawing all of these. Every single device here has a mux sitting in front of it, which can select from all of the nearby circuits that are available. The actual configuration of the FPGA amounts to the mux control. In this mux, we have the data inputs, and we have the control that selects.
There’s a little storage device sitting next to every single one of these muxes saying, “This is where you’re going to source your input from.” Programming it consists of configuring every single one of these muxes.
Dwarkesh Patel
That makes sense. What is happening inside of the lookup table?
Reiner Pope
The lookup table is also going to have a little bit of control telling it what to do. Its purpose is to configurably take the role of an AND gate, OR gate, XOR, or any of those different things. There are many ways you could consider doing that. The way it’s done in traditional FPGAs… A lookup table has four bits of input and one bit of output. How many different functions are there from four bits to one bit? There are 16 different functions.
You can tabulate this as 16 different numbers. You’ve got a table of 0111001, 16 entries. This table is stored in this blue configuration bit. It views these four bits as binary, looks up the relevant row of the table, and emits that bit. This is essentially a truth-table view of lookup tables.
Dwarkesh Patel
Okay, so if you think about an AND gate, OR gate,
NOR gate
, XOR gate, these all take as input…
Reiner Pope
Those are two-input functions. Sometimes we have a three-input function, like a three-way XOR, or a four-way XOR.
Dwarkesh Patel
In this case, does it just depend on how big it is?
Reiner Pope
The typical size for LUTs is four inputs. It’s sort of just a sweet spot. There’s another compute vs. communication trade-off here. If it has too few inputs, you need to use more LUTs.
Dwarkesh Patel
Basically the lookup table is a
truth table
. With a truth table, you can program in any gate you want. So instead of a lookup table, you can just think of it as a programmable gate.
Reiner Pope
That’s right. One of the things you can do here is you can see where the rule of thumb that an FPGA is an order of magnitude more expensive than an ASIC comes from. You count how many gates would be inside this lookup table.
We can view this lookup table essentially as one of these muxes. It has to select between 16 different values, so it’s a mux with
n
=16 options and
p
=1 bits. As we saw earlier, this circuit costs
n
times
p
many gates. So it costs
np
, which is 16, AND gates, and also 16 ORs.
Dwarkesh Patel
This circuit being the mux?
Reiner Pope
Exactly, the mux.
Dwarkesh Patel
The mux that goes into the lookup table?
Reiner Pope
The lookup table itself you can think of as being a big mux that selects from all 16 rows down to one output. That’s the lookup table.
Dwarkesh Patel
But the way you’ve drawn it here, there’s a mux and then a lookup table.
Reiner Pope
It’s muxes all the way down. There is a second mux that is inside here. This mux is this mux.
Dwarkesh Patel
And the other mux is just saying…
Reiner Pope
where it came from in this mess of gates.
Dwarkesh Patel
Right, and the second mux is, “Okay, now you have one value, but that value is still a four-bit value.”
Reiner Pope
Yeah, I’ve selected four bits from the soup. Then I use those four bits to select which entry in the lookup table I’m going to use.
Dwarkesh Patel
Suppose in the first mux you’re pulling from eight nearby registers as input. That’s a total of 32 bits going in. Out of that, four bits come out. Those four bits go into the second mux, which is inside the lookup table.
Reiner Pope
In this case, these registers are single-bit registers. If there are eight nearby registers and lookup tables, then I have eight bits total coming in nearby. I select from eight down to four different values. There are actually four different muxes, a little mux associated with each of these input bits. Each of them is selecting one out of eight.
Dwarkesh Patel
Where are those eight coming from?
Reiner Pope
Nearby registers and other LUTs.
Dwarkesh Patel
Each register is one bit.
Reiner Pope
Yes.
Dwarkesh Patel
I guess AMD or whoever makes these FPGAs still has to be opinionated about which registers are connected to which registers. You can program in the actual gates, but they add a wire in the connect… the communication topology, right?
Reiner Pope
You get flexibility at a local grain. There’s a nearby neighborhood you can select from, but for more coarse, long-distance connections, they form an opinion on that.
Dwarkesh Patel
And the reason it’s 10x slower is why?
Reiner Pope
If you look at the cost of building this lookup table, it’s 32 gates. It can give me the equivalent of—what’s an interesting thing I can do here—a four-way AND gate. A four-way AND means AND, AND, and then an AND of an AND. This is a circuit I could implement in an ASIC directly using three AND gates. Using a LUT, I can also implement it, but it’s going to take 32 gates instead of three.
Dwarkesh Patel
So the overhead is really coming from the fact that there’s a more concise way to describe a truth table than listing out every single possible combination of inputs, which is just to write out the gate.
Reiner Pope
Yes, to place down the polysilicon and the wires and so on.
Dwarkesh Patel
Interesting. One important point you made to me is that the reason they prefer FPGAs to CPUs is that they get deterministic clock cycles. They know when a packet will come in and go out. Why isn’t that a guarantee in CPUs?
Reiner Pope
You can actually design a CPU that has deterministic latency as well. In fact, the processors inside a lot of AI chips also have deterministic latency.
Groq
has advertised this. TPUs have that in the core as well.
The challenge is getting deterministic latency and high speed at the same time. Non-deterministic latency comes from specific design choices in a CPU. It’s actually possible to remove those design choices and make a CPU with deterministic latency, but those are not very attractive in the market, so people don’t make those CPUs anymore.
In some sense, deterministic latency is a simpler starting point, and some chip designers have added things in to make it non-deterministic. To take a concrete example, probably the most important source of non-determinism on a CPU is the
CPU cache
itself.
In a CPU, you have the
CPU die
itself, and then
DDR memory
off on the side. You have a cache system inside that remembers recent accesses to DDR and stores them. When I’m running through my CPU instructions, every time I have an instruction that accesses memory, it first checks if the data was stored in the cache. If not, it fetches it from DDR.
This is a huge optimization. The cache is two orders of magnitude faster than the DDR. If you never used the cache, basically all programs would run a hundred times slower. The presence of a cache is absolutely necessary for a CPU to run at a reasonable speed.
But whether or not you get a cache hit depends on the ambient environment of the CPU: what other programs are running, what has run recently, and what the random number generator inside the cache system is doing. That is a big source of non-determinism in the runtime of a CPU.
That is the memory system for a CPU. The big thing you can do differently is, instead of having the hardware say, “I’m going to read memory” and then the hardware decides whether or not it comes from the cache, you can bake this decision into software, a different design philosophy.
You see this in TPUs, for example. I’ll draw the same diagram, but I’ll call it a scratchpad. The main difference is… This would be a TPU, and you have
HBM
in this case rather than DDR, but it’s still an off-chip memory. Instead of the software saying “first access memory” and letting the hardware decide, you have one kind of instruction that goes to the scratchpad and a totally different kind of instruction that goes to HBM.
This style is generically known as
scratchpad
instead of cache. The key distinction is that you have one kind of instruction that says “read or write scratchpad,” and a totally different instruction that says “read or write HBM.”
Dwarkesh Patel
So scratchpad being the cache.
Reiner Pope
Yeah, this thing here is the scratchpad.
Dwarkesh Patel
Stepping way back: people say computers have the “
von Neumann architecture
”, where there’s this serial processing of information. Maybe it’s just because we’ve been talking about parallel accelerators, but the FPGA is super parallel. The AI accelerators, the TPUs, are super parallel. Even CPUs are super parallel if you think about all the cores they have. In what sense is modern hardware actually the von Neumann architecture? Is that actually a fair way to describe modern hardware?
Reiner Pope
I think it’s a fair way to describe CPUs. The amount of parallelism you get on a CPU is about 100 cores times maybe 16-way vector units, so about 1,000-way parallelism on a CPU.
Dwarkesh Patel
One question: there is a die being used for the CPU, and if there are fewer
threads
, just as a matter of transistor voltages switching on and off, is it that there’s literally one control flow—a small part of the die—where voltages are switching on and off?
How do you actually occupy the die area of a CPU…
Reiner Pope
If there are so few cores, what are you spending all of the die on?
Dwarkesh Patel
Yeah, what is happening there?
Reiner Pope
The cores are just much bigger and more complicated. We should compare a CPU core, which takes up one one-hundredth of the die, to a LUT. A LUT is only 16 gates. It’s clear why there are so many more LUTs in an FPGA than cores in a CPU.
But why are there more CUDA cores, for example, than CPU cores? What’s the difference between a CPU and a GPU? Inside the CPU, one big use of the area is the cache. Very little is actually the ALUs. Mostly it’s these register files rather than the logic units. Both of those have equivalents in a GPU, so that’s not a big difference.
But the thing that does not have an equivalent in a GPU is the
branch predictor
. There is a whole big area in the CPU which is just a bunch of predictors saying when the next
branch
will be and where the branch target is. Stripping a lot of that out, as well as making these register files tighter, drives a lot of the GPU gains over the CPU.
Dwarkesh Patel
What is the purpose of the branch predictor? To execute both branches at once, or what does it do?
Reiner Pope
The issue is that when I’ve got a series of instructions, if I have a branch, the actual step of processing an instruction takes a really long time. It takes maybe five nanoseconds.
The time to notice that I’ve got a branch, evaluate whether the
Boolean
is true, update the program counter to the new target, and then read from the instruction memory could take five nanoseconds to finish. So in reality, this may finish somewhere down here. I want to run a clock speed that is much faster than what five nanoseconds allows. Five nanoseconds is a 200 MHz clock speed. I would like to run at one or two gigahertz.
So I need to run other instructions while the branch is being evaluated. I just want to keep running the instructions that happen after me. But that might have been wrong. If the branch ended up being taken, then I need to know that instead of evaluating these instructions, I actually need to jump to wherever the target is and run those instructions instead. The purpose of the branch predictor is to predict, five cycles earlier, that a branch is going to happen, before you even get to that instruction.
Dwarkesh Patel
If I think about how the brain works versus what you’re describing here, at a high level the differences might be that while you can do structured sparsity in these accelerators and save yourself some area that you would have otherwise had to dedicate to gates, in the brain there’s unstructured sparsity. Any neuron can connect to any other neuron, and not in ways where they have the column aligned.
Then there’s the fact that memory and compute are co-located. Although I guess you could say in a way the memory and compute are co-located on these dies too.
Reiner Pope
This is exactly the co-location, in some sense, of the memory and compute.
Dwarkesh Patel
So maybe that isn’t a big difference. Another big difference is that the clock cycle on the brain is much slower than on computers. Partly that’s to preserve energy, because the faster the clock cycle, the bigger the voltage needs to be in order for the signal to settle and to identify what state a transistor is in.
Reiner Pope
That’s right.
Dwarkesh Patel
I don’t know if you have any commentary on what the brain might be doing versus how these chips work.
Reiner Pope
Let’s take the clock speed one first. The clock speed is quite high on a chip because that drives higher throughput. When we compare a GPU running some workload, it’s running batch size 1,000. Whereas the brain is not running batch size 1,000, there’s only one of me.
You could imagine saying, “Take a GPU and instead of running at a gigahertz, run it at a megahertz,” and that would start to look a little more like the equivalent things you’re talking about in the brain. But in the way silicon works, that does not give you a 1,000x advantage in energy efficiency.
What it ends up looking like is you just run this circuit once to stabilization, and then it will sit idle for a long period of time. It doesn’t consume a lot of energy while it’s sitting idle because most of the energy is consumed in toggling bits from zero to one and back.
Let’s talk about the energy consumption of a circuit like this. The way to think of a bit being stored is that you’ve deposited some charge in a capacitor sitting somewhere in the chip implicitly. It becomes charged when the bit becomes a one, and then it becomes discharged when it next goes to a zero.
That cycle of charging the capacitor and then dumping that charge out to ground is where the energy is consumed. This is called the dynamic or switching power, and it’s most of the energy consumption of a chip. There is some other energy consumption just coming from the fact that insulators aren’t perfect, but we’ll discard that. Most of the energy consumption comes from toggling from zero to one and back to zero.
If you run a chip much slower and you only clock it once every thousand clock cycles, you will have 1,000 times fewer transitions. It will be about 1,000 times less energy consumption. But it’s not a substantial advantage in energy efficiency.
Dwarkesh Patel
Okay, so you described how a TPU works at a high level. What is the difference at a high level between how a GPU and a TPU work?
Reiner Pope
There is a high-level organization principle that is different, and then inside the cores things are different. Looking at the high level, we’ll take a GPU and a TPU and see what the top-level block structure looks like.
If you think of this as the whole chip in each case, the organization of the GPU is mostly a bunch of almost-identical units, which are the
SMs
. They’ve got an
L2 memory
in the middle, and then a bunch more of these SMs on the bottom. So there is a fairly regular grid of cores.
If we look at a TPU in comparison, you end up with much coarser-grained units of logic. You end up with just a few matrix units, which are the big systolic arrays. In the middle you’ve got some vector unit, and then you’ve got your matrix units at the bottom. These matrix units with a vector unit in the middle make up the whole TPU chip.
You can think of scaling this thing down into a really tiny unit with a smaller matrix unit and a smaller vector unit, and that is sort of what an SM is. From a very high-level point of view, the GPU has a lot of tiny TPUs tiled across the whole chip.
Dwarkesh Patel
Oh, interesting. You’re suggesting the tensor core within a streaming SM is analogous to an
MXU
?
Reiner Pope
Yeah, it’s all very similar.
Dwarkesh Patel
I see. If you had more lack of structure, having a bunch of tiny TPUs makes a lot of sense. Whereas if you just have huge matrix multiplications, you might want to avoid the cost of having individual SMs with their own registers and warp schedulers. Why not just make a huge thing and amortize those costs across the whole thing?
Reiner Pope
This shows up in how large you can grow things. We’ve seen this theme, especially with the systolic array, where a larger systolic array amortizes the register file costs better.
This design allows you to have larger systolic arrays, whereas the GPU design constrains you to having small units of everything. There is a trade-off, however. Because of this coarse-grained separation of things, you need to move a lot of data from the vector unit to the matrix units, through just two lines of perimeter here.
If you look at the equivalent thing in a GPU, you’ve got vector units everywhere, and you can move data through many different lines. The amount of data you can move between a vector unit and a matrix unit is actually much higher in a GPU than in a TPU. Instead of having to move all the data through just two lines, you’re moving it through 16 lines of wiring in a GPU.
Dwarkesh Patel
Right. But also you might have to move across less area.
Reiner Pope
Which is an energy saving as well. So if you can operate entirely within an SM, the data movement is much smaller. But the moment you want to operate across SMs, it becomes more complicated and expensive.
Dwarkesh Patel
So you don’t have to comment, but one might expect that a thing MatX might try to do is get the GPU-like smaller structure of systolic arrays surrounded by
SRAM
, but at the same time make it so that the things you need in an SM to support the CUDA architecture—which take a bunch of space—you might discard.
Reiner Pope
We’ve talked publicly about something we call a
splittable systolic array
, which in some sense you can think of as big systolic arrays that can be small systolic arrays too.
Dwarkesh Patel
Cool. Okay, I think that’s a good note to close on. Reiner, thank you so much.
Reiner Pope
Thanks, Dwarkesh.
