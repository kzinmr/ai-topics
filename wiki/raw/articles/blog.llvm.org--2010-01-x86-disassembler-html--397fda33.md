---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2010/01/x86-disassembler.html"
fetched_at: 2026-05-05T07:01:44.337337+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2010/01/x86-disassembler.html

The x86 Disassembler
Disassemblers make binary analysis work. With a reliable disassembler, you can solve high-level problems like tracing back through a program's call stack or analyzing sample-based profiles to low-level problems like figuring out how your compiler unrolled a tight floating-point loop or what advantages declaring a variable const actually had at the other end of the optimization chain. A reliable disassembler, which takes sequences of bytes and prints human-readable instruction mnemonics, is a crucial part of any development platform. You're about to go on a whirlwind tour of the LLVM disassembler: why one should exist, what's great about this one, and how you can use it.
The case for an LLVM-based disassembler
Disassemblers are all over the place. A disassembler you may well be familiar with is the disassembler from GNU gdb (
source
). In fact, any debugger needs one: Sun mdb has a disassembler too (
source
). Some specialized applications like Dtrace need disassemblers as well (
source
). So because this is well-traveled ground, there are several common properties you should expect from a disassembler:
A large library can contain hundreds of thousands of instructions, so disassembly must be
fast
.
A disassembler with a large memory footprint can steal memory and cache from analysis algorithms that need them more, so its code and data should be
compact
.
Because disassemblers are used in a variety of applications, they should provide information about instructions in a
generic
, preferably even architecture-independent form.
For the benefit of future code maintainers, disassemblers should be as
table-driven
as possible.
Enter the LLVM MC architecture. In MC, instructions are represented using the architecture-independent
MCInst
class (
include/llvm/MC/MCInst.h
). The translation between MC instructions and machine code is specified by pre-existing
TableGen
tables (
lib/Target/X86/X86.td
for x86 platforms). Writing a disassembler inside the MC framework makes sense because it solves the generality and table-driven problems naturally, but we still need to solve two problems: speed and compactness.
Quick Testdrive of the Disassembler
The llvm-mc tool provides a simple command line wrapper around the disassembler that we primarily use for testing (e.g.
test/MC/Disassembler/simple-tests.txt
).  It reads a text file containing input bytes and prints out the instructions that correspond to those bytes.  For example, here's a simple transcript of using it:
$ echo '1 2' | llvm-mc -disassemble -triple=x86_64-apple-darwin9
addl %eax, (%rdx)
$ echo '0x0f 0x1 0x9' | llvm-mc -disassemble -triple=x86_64-apple-darwin9
sidt (%rcx)
$ echo '0x0f 0xa2' | llvm-mc -disassemble -triple=x86_64-apple-darwin9
cpuid
$ echo '0xd9 0xff' | llvm-mc -disassemble -triple=i386-apple-darwin9
fcos
Design of the decode process
Fast disassemblers can be classified into two categories, depending on the instruction format. On platforms with fixed-length instructions, it is possible to pull out all bits of the instruction at once and filter based on arbitrary ranges of those bits. In contrast, platforms with variable-length instructions require that the instruction be parsed byte by byte. In this article, I will discuss the variable-length case, and in particular the case of x86, which includes the
i386
and
x86_64
targets.
The structure of an x86 instruction is determined by several important factors, each of which is of vital importance when decoding:
The
context
of the instruction determines the meaning of the instruction and the size of its operands. The context includes the address and operand sizes of the instruction, as well as the presence (and position!) of prefixes such as the
REX.w
prefix on
x86_64
targets and the
f3
prefix on architectures with SSE.
The
opcode
of the instruction is of varying size, and determines what operands are required. Opcodes come in four different types: one-byte opcodes of the form
xx
, two-byte opcodes of the form
0f
xx
, three-byte opcodes of the form
0f
38
xx
, and three-byte opcodes of the form
0f
3a
xx
.
The
addressing bytes
of the instruction determine the addressing mode of the instruction's memory operand (there is only one memory operand possible with a selectable mode). The addressing bytes include the ModR/M (Modifier - Register/Memory) byte and the SIB (Scale - Index - Base) byte.
Other prefixes?
Mandatory prefix?
REX prefix?
0f
[
38
/
3a
]?
Opcode
ModR/M byte?
SIB byte?
Table 1:
Portions of an instruction relevant to decode
You can read more about the meaning of all of these bytes in Chapter 2 of the Intel instruction manual, volume 2A (
large PDF
). The x86 disassembler is structured around hierarchical tables that assume a 5-phase decode process. You can follow along with this discussion by looking at
lib/Target/X86/Disassembler/X86DisassemblerDecoderCommon.h
, and the steps below are colored consistently with the data they access in Table 1.
Phase 1
Record all prefixes but do not use them. Determine the type of the opcode, and obtain a
ContextDecision
on that basis:
ONEBYTE_SYM
,
TWOBYTE_SYM
,
THREEBYTE38_SYM
, and
THREEBYTE3A_SYM
.
Phase 2
Develop a context mask based on the prefixes that are present and the machine architecture being decoded for. Look up this mask in a lookup table (
CONTEXTS_SYM
) to get a context ID. Consult the
ContextDecision
to find the
OpcodeDecision
that corresponds to the context. As the comments in the header point out, the many possible contexts are boiled down to
IC_max
distinct context IDs that actually matter when decoding. This saves a lot of space.
Phase 3
Read the opcode and use it to consult the
OpcodeDecision
to find the right
ModRMDecision
.
Phase 4
The ModR/M byte not only specifies the addressing mode, but also sometimes serves to identify the specific instruction intended. For example, extended opcodes and escape opcodes (often seen in SSE) use the Reg/Opcode field in the ModR/M byte as part of the opcode. You can see these oddities in Chapters A.4 and A.5 of the Intel instruction manual, volume 2B (
large PDF
). Given the value of the ModR/M byte, look up the LLVM opcode for the decoded instruction in the
ModRMDecision
.
Phase 5
If the ModR/M byte indicates that an SIB byte is needed, read the SIB byte. This phase occurs as operands are read.
Once these five steps have been performed, the disassembler consumes the operands, whose forms are now completely specified.
Using the disassemblers in real code
If you want to use a disassembler in your own code, then
tools/llvm-mc/Disassembler.cpp
is a good example of how to use one. You can instantiate a disassembler given a Target using the following code:
llvm
::
OwningPtr
<
const
llvm
::
MCDisassembler
>
disassembler
(
target
.
createMCDisassembler
());
This disassembler works with
MemoryObject
s (
include/llvm/Support/MemoryObject.h
), and you will need to subclass
MemoryObject
to perform the proper reading functions. A very
simple
MemoryObject
subclass might look like this:
class
BufferMemoryObject
:
public
llvm
::
MemoryObject
{
private
:
const
uint8_t
*
Bytes
;
uint64_t
Length
;
public
:
BufferMemoryObject
(
const
uint8_t
*
bytes
,
uint64_t
length
) :
Bytes
(
bytes
),
Length
(
length
) {
}
uint64_t
getBase
()
const
{
return
0
; }
uint64_t
getExtent
()
const
{
return
Length
; }
int
readByte
(
uint64_t
addr
,
uint8_t
*
byte
)
const
{
if
(
addr
>
getExtent
())
return
-1
;
*
byte
=
Bytes
[
addr
];
return
0
;
}
};
Given a
BufferMemoryObject
, all you have to do to extract
MCInst
objects is to call the
getInstruction
method of the disassembler you got earlier:
llvm
::
MCInst
Inst
;
uint64_t
Size
;
disassembler
->
getInstruction
(
Inst
,
Size
,
BufferMObj
,
0
,
llvm
::
nulls
()));
The last argument is an optional diagnostic stream, and the
0
indicates that the disassembler should start from address 0 in the buffer.
Where to look for more documentation
For general information on how the disassembler's decode tables are generated from
lib/Target/X86/X86.td
, visit
utils/TableGen/DisassemblerEmitter.cpp
, which provides an overview of the TableGen side of the code. If you're interested in the gory, bit-for-bit details of how the disassembler dissects the various instruction bytes, you can go straight to
lib/Target/X86/Disassembler/X86Disassembler.h
, which describes the decode process in more detail and gives a guide to the implementation files.
