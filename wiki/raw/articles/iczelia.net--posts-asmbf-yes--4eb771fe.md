---
title: "Reimplementing GNU yes using asm2bf"
url: "https://iczelia.net/posts/asmbf-yes/"
fetched_at: 2026-05-05T07:01:22.615514+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Reimplementing GNU yes using asm2bf

Source: https://iczelia.net/posts/asmbf-yes/

Introduction
⌗
A few days ago I received a
pull request
with a very simple reimplementation of GNU
yes
in asm2bf:
mov r1, 121
mov r2, 10

@y
    out r1
    out r2
    jmp %y
Its performance seems to oscillate around 800KBps, as evidenced by
bfmake yes.asm && bfi yes.b | pv > /dev/null
, and we’ll try to improve upon it today.
We aim at brainfuck
⌗
First things first, let’s turn the label and the matching unconditional jump into a simple brainfuck loop:
mov r1, 121
mov r2, 10

nav r1
raw .[
    out r1
    out r2
nav r1
raw .]
This change alone speeds the program up to 1.7MiB/s, and makes the code smaller by 173 bytes, bringing it down to 206 bytes!
The next optimisation lies in the way we build the program. Since the label system isn’t used, we can disable it. It won’t bring a performance improvement, but the code size will drop down to 148 bytes.
To make the program a little smaller, we will employ multiplication loops using the
gen_text
macro:
inc r1
nav r1
raw .[
#gen_text("y\n")
nav r1
raw .]
The speed drops down to 400KiB/s, but the program is only 67 bytes now!
If we move
gen_text
out of the loop and somehow preserve whatever it generates, we could accomplish the most optimal program. Let’s do that now:
; step 1: move to the beginning of the tape
nav r1
#emit("<<<")
; step 2: generate `y`.
#emit(gen_constant(string.byte("y")))
; one cell after `y`, generate a newline
raw .>
#emit(gen_constant(10))
; then go back and print these in a loop
raw .<
raw .[
out r1
out r2
raw .<
raw .]
The performance is back at 1.7MiB/s, and we managed to make the output fairly small - it’s 55 bytes:
>++++[<+++++>-]<++++[>+++++<-]>+[-<+>]
++++++++++
<[.>.<]
Fairly good for something that wasn’t handwritten, if you ask me. Either way, asm2bf generates a somewhat inefficient snippet for
y
, so let’s start manual fixes now:
+++++++++++[>+++++++++++<-]>>
++++++++++
<[.>.<]
This change brings us down to 46 bytes, 9 bytes less than the original. Now that we’re done with the assembly part, let’s try running this brainfuck code quickly. Of course,
bfi
isn’t the best choice here, since it’s just an interpreter. Let’s try tritium instead.
tritium yes.b | pv > /dev/null
yields a stable score of around 21MiB/s. Adding the
-a -b -O3
flags seems to speed the program up by 1MiB/s.
Let’s implement some unrolling:
nav r1
#emit("<<<")
#emit(gen_constant(string.byte("y")))
raw .>
#emit(gen_constant(10))
#emit("<[")
; unroll the loop
#for i=1, 10 do
#emit(".>.<")
#end
#emit("]")
tritium -c
appears to generate the following code (with a lot of crap removed):
There’s a significant problem with this approach -
a
and
b
aren’t inlined, and the compiler put them as static variables outside of
main
, meaning that no compiler I’m aware of will optimise these. After we move these into the
main
function, everything starts becoming more reasonable. After compiling with
clang
, we get the final score of 372MiB/s, which I believe can’t be improved much upon. Leaving the loop not unrolled worsens the performance by around 40MiB/s.
The BFVM way.
⌗
Of course, asm2bf’s only target isn’t brainfuck. Albeit targets other languages using brainfuck, BFVM can be used to generate reasonably efficient C code out of asm2bf code.
Let’s use conditional compilation:
#if BFVM == 0 then
    nav r1
    $(
        emit("<<<")
        emit(gen_constant(string.byte("y")))
        emit(">")
        emit(gen_constant(10))
        emit("<[")
    )
    ; unroll the loop
    $(
        for i = 1, 10 do
            emit(".>.<")
        end
        emit("]")
    )
#else
    mov r1, 121
    mov r2, 10

    @y
        out r1
        out r2
        jmp %y
#end
bfmake -c yes.asm && clang -O3 yes.c -o yes && ./yes | pv > /dev/null
yields us the speed of 205MiB/s.
Using the
-j
flag to allocate the tape on the stack and adding the
-flto
switch speeds the resulting code by a few MiB/s, yielding a total of 218MiB/s.
Conclusions
⌗
Even though the program we were working on today was really simple, it proves a few things:
Targetting bfvm is a viable option to get good testing performance, without having to use brainfuck-specific hacks and kludges.
asm2bf is a good language to target for compilers, since parts of the code can be gradually optimised using inline brainfuck and lib-bfm macros, making asm2bf and intermediate step in an iteratively developed, brainfuck-targetting compiler.
