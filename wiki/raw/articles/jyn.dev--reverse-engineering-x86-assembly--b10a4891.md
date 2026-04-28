---
title: "Reverse Engineering x86 assembly"
url: "https://jyn.dev/reverse-engineering-x86-assembly/"
fetched_at: 2026-04-28T07:02:51.903658+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# Reverse Engineering x86 assembly

Source: https://jyn.dev/reverse-engineering-x86-assembly/

Intro
For those of you not familiar with the C toolchain, it goes something like this:
Source -> preprocessed source -> assembly -> object file -> binary
The second step (preprocessed -> assembly) is the hardest to undo.
It removes labels, debug symbols, and turns a high-level control flow into assembly instructions.
However, since you
need
a binary to run a program, if you can undo that step,
you can see what's going on.
GDB Basics
GDB is a debugger. It steps through a compiled program, line by line, and shows you
the changes after every step.
Let's take a simple hello-world program and step through it.
#include
<
stdio.h
>
int
main
(
void
)
{
puts
(
"
Hello, world!
"
)
;
return
0
;
}
Passing
-g
to
gcc
means preserve debug symbols, so we know where we are in the original source code.
Passing
-q
to
gdb
means don't print 10 lines of copyright info.
Note that we have to add a breakpoint in the main function, or it will run without ever stopping.
$
gcc
-
g
hello_world.c
-
o
hello
$
gdb
-
q
hello
Reading
symbols from hello...done.
(
gdb
)
list
1
2
3
int main(void
)
{
4
puts(
"
Hello, world!
"
)
;
5
return 0
;
6
}
7
(
gdb
)
break main
Breakpoint
1 at 0x4004db: file hello_world.c, line 4.
(
gdb
)
run
Starting
program: /home/jyn/hello
Breakpoint
1, main (
)
at
tmp.c:4
4
puts(
"
Hello, world!
"
)
;
(
gdb
)
next
Hello,
world!
5
return 0
;
(
gdb
)
6
}
(
gdb
)
continue
Continuing.
[Inferior
1 (process 28690
)
exited
normally]
You can also show variables as you step through.
(Note that
return 0
is optional in the main function)
#include
<
stdio.h
>
int
main
(
void
)
{
char
*
var
=
"
Hello, world!
"
;
var
=
"
changed my mind
"
;
puts
(
var
)
;
}
$
gcc
-
g
var.c
-
o
var
$
gdb
-
q
var
Reading
symbols from var...done.
(
gdb
)
break main
Breakpoint
1 at 0x4004df: file var.c, line 4.
(
gdb
)
run
Starting
program: /home/jyn/var
Breakpoint
1, main (
)
at
var.c:4
4
char
*
var =
"
Hello, world!
"
;
(
gdb
)
print var
$
1
= 0x0
(
gdb
)
n
5
var =
"
changed my mind
"
;
(
gdb
)
print var
$
2
= 0x4005a0
"
Hello, world!
"
(
gdb
)
n
6
puts(var
)
;
(
gdb
)
print var
$
3
= 0x4005ae
"
changed my mind
"
(
gdb
)
n
changed
my mind
7
}
(
gdb
)
c
Continuing.
[Inferior
1 (process 29542
)
exited
normally]
This post is continued in
Buffer Overflows and Stacks and Assembly, Oh My
.
