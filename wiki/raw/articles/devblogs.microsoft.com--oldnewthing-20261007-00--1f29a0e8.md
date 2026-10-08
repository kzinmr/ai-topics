---
title: "How can undefined opcodes ud0 and ud1 have parameters? How undefined were they?"
url: "https://devblogs.microsoft.com/oldnewthing/20261007-00/?p=112759/"
fetched_at: 2026-10-08T10:01:35.165283+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How can undefined opcodes ud0 and ud1 have parameters? How undefined were they?

Source: https://devblogs.microsoft.com/oldnewthing/20261007-00/?p=112759/

Gunnar Dalsnes wondered
how
ud0
and
ud1
could have parameters if they were undefined
? “Does it mean they were not completely undefined, just undocumented and not completely implemented?”
The opcodes
ud0
and
ud1
have no definition, but that’s not the same as being architecturally an “undefined instruction”. They live in a purgatory where they were not assigned a meaning, but were also not officially declared to be meaningless.
Originally, these byte sequences went through the instruction decoder and happened to slip through a few cracks before somebody finally noticed, “Wait a second, I don’t know how to execute this.”
You can see this when you look at the instructions that are encoded as
00001111 11111xxx
, as of the Pentium III.
Bits
Bytes
Opcode
Operand 1
Operand 2
Meaning
00001111 11111000
0F F8
PSUBB
mm
mm/m64
Subtract packed bytes
00001111 11111001
0F F9
PSUBW
mm
mm/m64
Subtract packed words
00001111 11111010
0F FA
PSUBD
mm
mm/m64
Subtract packed dwords
00001111 11111011
0F FB
No meaning assigned
00001111 11111100
0F FC
PADDB
mm
mm/m64
Add packed bytes
00001111 11111101
0F FD
PADDW
mm
mm/m64
Add packed words
00001111 11111110
0F FE
PADDD
mm
mm/m64
Add packed dwords
00001111 11111111
0F FF
No meaning assigned
The byte sequences
0F FB
and
0F FF
had yet to be assigned a meaning. You can see how the instruction decoder could take a shortcut and say, “Well, all the instructions in this range, or at least all the ones that I care about, take an mm registers and an mm/m64 operand, so I’ll just save myself some transistors and decode all of them with two parameters (mm, mm/m64).” And then after decoding, it would use bit 3 to decide whether to set up the arithmetic unit for an add or subtract, and it would use bits 0 and 1 to decide how to subdivide the bits into saturating units.
And if you gave it a
0F FF
, it would be only in that last step that the decoder would realize “Oh dear, I don’t know what to do with a bit combination of
11
. I’ll raise an invalid opcode instruction.”
The invalid opcode instruction got raised
after
the operands were parsed.
You can see the trouble that
0F FF
created when those empty slots started to get filled in by the SSE instructions.
Bits
Bytes
Opcode
Operand 1
Operand 2
Meaning
00001111 11111000
0F F8
PSUBB
mm
mm/m64
Subtract packed bytes
00001111 11111001
0F F9
PSUBW
mm
mm/m64
Subtract packed words
00001111 11111010
0F FA
PSUBD
mm
mm/m64
Subtract packed dwords
00001111 11111011
0F FB
PSUBQ
mm
mm/m64
Subtract packed qwords
00001111 11111100
0F FC
PADDB
mm
mm/m64
Add packed bytes
00001111 11111101
0F FD
PADDW
mm
mm/m64
Add packed words
00001111 11111110
0F FE
PADDD
mm
mm/m64
Add packed dwords
00001111 11111111
0F FF
I want to put
PADDQ
here but I can’t
the natural place to put the
PADDQ
instruction is
0F FF
, but people had already been using
0F FF
with the expectation that it raises an illegal instruction exception. Making it a valid instruction would break those programs, so Intel had to move
PADDQ
to the rather awkward location
0F D4
.
Bonus chatter
: Undefined instructions with parameters are actually not uncommon. For example, on AArch64,
there is a range of 65,536 instructions set aside as permanently undefined
, so the
udf
instruction takes a 16-bit immediate to specify which invalid opcode you want. The PDP-10 reserved opcode 000 as a permanently illegal instruction, and it carries a register and a memory address as parameters. (Because
all
PDP-10 instructions carry a register and a memory address as parameters.)
There are also so-called “unofficial opcodes” which are instructions that are not part of the instruction set architecture, but for which people reverse-engineered a consistent behavior and began to rely on it. (The 6502 processor is
well-known in nerd circles for having undergone this type of analysis
.) The
0F FF
is one of these “unofficial opcodes” that was popular enough that Intel felt pressure to maintain backward compatibility with it, even though it was never architecturally documented or supported.
Bonus bonus chatter
: It appears that the mnemonic
ud1
was
introduced by the nasm assembler
:
* Added the following new instructions: SYSENTER, SYSEXIT, FXSAVE,
  FXRSTOR, UD1, UD2 (the latter two are two opcodes that Intel
  guarantee will never be used; one of them is documented as UD2 in
  Intel documentation, the other one just as "Undefined Opcode" --
calling it UD1 seemed to make sense
.)
It seems obvious that
ud1
is also the name that Intel gave internally to that legacy instruction. Otherwise, there would be no need to call the new one
ud2
!
