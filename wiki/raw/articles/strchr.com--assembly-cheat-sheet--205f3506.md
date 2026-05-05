---
title: "Win32 Assembly Cheat Sheet"
url: "http://www.strchr.com/assembly_cheat_sheet"
fetched_at: 2026-05-05T07:01:16.062731+00:00
source: "Peter Kankowski (strchr)"
tags: [blog, raw]
---

# Win32 Assembly Cheat Sheet

Source: http://www.strchr.com/assembly_cheat_sheet

The cheat sheet is intended for 32-bit Windows programming with
FASM
. One A4 page contains almost all general-purpose x86 instructions (except FPU, MMX and SSE instructions).
What is included
You will find various kinds of moves (MOV, CMOV, XCHG), arithmetical (ADD, SUB, MUL, DIV) and logical (AND, OR, XOR, NOT) instructions here. Several charts illustrate shifts (SHL/SHR, ROL/ROR, RCL/RCR) and stack frames. Code samples for typical high-level language constructs (if conditions, while and for loops, switches, function calls) are shown. Also included are quick references for RDTSC and CPUID instructions, description of string operations such as REP MOVSB, some code patterns for branchless conditions, a list of registers that should be saved in functions, and a lot of other useful stuff.
The idea
is to put all reference information about x86 assembly language on the one page. Some rarely-used instructions such as LDS, BOUNDS or AAA are skipped.
Notation
The cheat sheet use common notation for operands:
reg
means register,
[mem]
means memory location, and
imm
is an immediate operand. Also,
x, y,
and
z
denote the first, the second, and the third operand. Instruction mnemonics are written in capital letters to make them easier to find when you are skipping through the cheat sheet.
Example
For example, let's look at multiplication and division section. There are instructions for signed (IMUL) and unsigned (MUL) multiplication. Both instructions take one operand, which may be register (
reg
) or memory (
[mem]
). There are three possible cases:
If operand size is one byte, MUL or IMUL multiplies it by
al
and stores the result in
ax
If operand size is a word, MUL or IMUL multiplies it by
ax
and stores the high-order word of the result in
dx
and the low-order word in
ax
.
If operand size is a double word, MUL or IMUL multiplies it by
eax
and stores the high-order dword in
edx
and the low-order dword in
eax
.
There are also two-operand and three-operand forms of IMUL shown on the figure above.
Other features of assembly language are described in a similar way.
Download
The cheat sheet is designed for A4 page size; if you print it on US Letter paper, you will get large margins. You can print the cheat sheet and put it on your table to look for some instructions when you forget them.
Download Win32 Assembly Cheat Sheet (PNG picture, 713 Kb)
Serbo-Croatian translation
of this article by
WHG Team.
