---
title: "Programming SUBLEQ"
url: "https://iczelia.net/posts/subleq/"
fetched_at: 2026-05-05T07:01:21.039104+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Programming SUBLEQ

Source: https://iczelia.net/posts/subleq/

Introduction
⌗
Subleq is an one instruction computer where every instruction performs the opeation of subtracting and branching if a value is less or equal than zero. In C-like logic, every instruction in the format of
subleq A, B, C
is equivalent to the following C-like pseudocode:
Synthesising instructions
⌗
Assume a zero register that is always available, i.e.
Z: 0
that is always present at the end of the code. An unconditional branch is as simple as
subleq Z, Z, dest
. Addition (
b += a
) is a bit more complicated and defined as follows, assuming that the missing last argument to
subleq
is the address of the following instruction:
subleq a, Z
subleq Z, b
subleq Z, Z
The first instruction stores
-a
in
Z
, the second instruction computes
b-Z=b-(-a)=b+a
and stores it in
b
. The final instruction restores
Z
back to zero. A move function is thus trivially implemented by clearing
b
first with
subleq b, b
. By abbreviating the encoding to remove the
subleq
instruction and simply storing the operands in memory, we can implement a “Hello, World!” program in Subleq assembly.
Assuming that
p
(the pointer to the current character that is being printed) is stored somewhere in memory, the following assembly code will print it to the standard output. I/O is accomplished using instructions with a negative
b
operand.
?
points to the current address.
a a ?+1
p Z ?+1
Z a ?+1
Z Z ?+1
a:0 -1 ?+1
Then, the pointer is incremented (assuming a
-1
stored in a memory location
m1
):
m1 p ?+1
The final part of the code checks if
p < E
(where
E
is the label placed directly after the end of the literal being printed) and loops:
a a ?+1
E Z ?+1
Z a ?+1
Z Z ?+1
p a -1

Z Z 0
The data of the program is as follows:
p:H Z:0 m1:-1

# "Hello, world!\n" in ASCII
H:72 101 108 108 111 44 32 87 111 114 108 100 33 10
E:E
After assembling this program, the resulting concrete Subleq code is as follows:
12 12 3
36 37 6
37 12 9
37 37 12
0 -1 15
38 36 18
12 12 21
53 37 24
37 12 27
37 37 30
36 12 -1
37 37 0
39 0 -1
72 101 108
108 111 44
32 87 111
114 108 100
33 10 53
An emulator
⌗
The following emulator of a SUBLEQ computer is based on Oleg Mazonka’s subleq executor, assembler and C compiler
. Output is accomplished by instructions with negative
b
operand. To compile Higher Subleq (a C dialect) to Subleq assembly, use the “HSQ -> ASQ” button. Direct translation to Subleq is also possible using the “HSQ -> SQ” button. To run the Subleq code, use the “run sq” button. I/O can be byte-wise (every value is interpreted as an ASCII character) or int-wise (every value is displayed as an integer).
