---
title: "How to crash gdb on OS X"
url: "https://idea.popcount.org/2012-11-13-how-to-crash-gdb-on-os-x"
fetched_at: 2026-05-05T07:01:13.848642+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# How to crash gdb on OS X

Source: https://idea.popcount.org/2012-11-13-how-to-crash-gdb-on-os-x

How to crash gdb on OS X
or how to use gdb on iTunes
13 November 2012
In recent years the
"Apple is evil"
discussion started recurring
more and more often.
In last week's edition
on the YCombinator,
jrockway
mentioned a
very interesting technical quirk
:
[...] I tried to run gdb on iTunes, and gdb segfaulted. I did some
research and found that Apple added extra code to the OS just to
prevent someone from doing exactly that. They spent additional
engineering effort just to lock me out of my own computer. [...]
I won't comment on the evilness, but I can confirm the
gdb
crash:
$
ps
aux
|
grep
iTunes
marek
28880
/
Applications
/
iTunes
.
app
/
Contents
/
MacOS
/
iTunes
$
gdb
-
p
28880
Attaching
to
process
28880.
Segmentation
fault
:
11
Whoo! That's interesting. Fortunately
comex
quickly explained
what's going on: there exists a
PT_DENY_ATTACH
flag to
ptrace
that
explicitly forbids running
ptrace
on that process. iTunes uses exactly
that. Here goes an extract from the manpage
ptrace(2)
:
PT_DENY_ATTACH
    [...] it allows a process that is not currently being
    traced to deny future traces by its parent. [...]
    If the process is currently being traced, it will exit
    with the exit status of ENOTSUP; otherwise, it sets
    a flag that denies future traces.  An attempt by the
    parent to trace a process which has set this flag will
    result in a segmentation violation in the parent.
It's pretty funny. According to OS X crashing parent process is
sometimes a valid and defined behaviour. I wonder if that signal can
be handled and if the kernel code for sending SIGSEGV isn't racy.
mikeash
explained how
to get around this stupid flag - you just need to override
ptrace
syscall before iTunes calls it:
$
gdb
/
Applications
/
iTunes
.
app
/
Contents
/
MacOS
/
iTunes
>
b
ptrace
>
commands
>
return
0
>
cont
>
end
>
r
That's it. Another day, another useless API.
BTW. Charlie Miller have described this hack in his
excellent
2008 Black Hat presentation on OS X
.
