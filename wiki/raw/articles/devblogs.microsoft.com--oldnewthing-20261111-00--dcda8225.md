---
title: "I didn't write a program with emoji, but I did use a control character"
url: "https://devblogs.microsoft.com/oldnewthing/20261111-00/?p=112848/"
fetched_at: 2026-11-12T10:01:09.800782+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# I didn't write a program with emoji, but I did use a control character

Source: https://devblogs.microsoft.com/oldnewthing/20261111-00/?p=112848/

Adventures in PC Emulation
recently wrote about
Executable Emoji
: Writing an MS-DOS program using machine code represented solely by Unicode emoji characters.
This reminded me that back in the day I did something similar, but much less impressive: I wrote a
reboot.com
program that could be generated from the command line via
echo
.
echo
Alt
+
Num2
,
Num0
,
Num5
Ctrl
+
Y
>reboot.com
The
Alt
+
Num2
,
Num0
,
Num5
means to press and hold the
Alt
while sequentially pressing and releasing
Num2
,
Num0
,
Num5
on the numeric keypad, and then releasing the
Alt
key. In the IBM PC 437 code page, this comes out looking like
═
, which is character 205, or hex
0xCD
.
The byte
0xCD
is the machine code for the
int
instruction, for issuing a software interrupt. And
Ctrl
+
Y
generates character 25, or hex
0x19
, which completes the instruction:
int 19h
.
Interrupt 19h was a sort-of not-very-good “reboot the system” interrupt. You can read about all the problems it has in
Ralph Brown’s Interrupt List
.
This interrupt reboots the system without clearing memory or restoring interrupt vectors. Because interrupt vectors are preserved, this interrupt usually causes a system hang if any TSRs have hooked vectors from 00h through 1Ch, particularly INT 08.
Since this was not a very good way of rebooting the system, it was mostly just a parlor trick.
But at least I did it.
