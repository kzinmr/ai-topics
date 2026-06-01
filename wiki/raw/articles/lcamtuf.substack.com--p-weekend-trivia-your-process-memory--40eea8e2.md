---
title: "Weekend trivia: your process' memory is a file"
url: "https://lcamtuf.substack.com/p/weekend-trivia-your-process-memory"
fetched_at: 2026-06-01T07:14:09.675017+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Weekend trivia: your process' memory is a file

Source: https://lcamtuf.substack.com/p/weekend-trivia-your-process-memory

Some folks say that the design philosophy of Unix is that “everything is a file”. If you’re familiar with Unix-like platforms, you probably know that they don’t quite live up to the hype. It’s true that these systems allow convenient access to hardware through file-like objects in directories such as
/sys
or
/dev
. At the same time, there’s plenty of OS functionality that isn’t exposed via files; for example, you can’t connect to a remote webserver without using a dedicated system call.
This is something people would probably have liked to do! A popular shell called
bash
comes with a workaround: it special-cases certain file paths, letting you construct the following shell monstrosity:
That said, the
/dev/tcp/<server>/<port>
trick works only for the files opened by the shell itself. If you pass such a path to any other program, you won’t get the expected result:
If you complain about this inconsistency, you might get told that not everything is a file; instead, “everything is a
file
descriptor
”. That is, you might need to do something special to initiate a TCP/IP connection, but once this is done, the returned connection identifier has file-like semantics and can be passed to standard file APIs such as
read(…)
and
write(…)
.
But then, not everything is actually a file descriptor! Some parts of the OS use separate namespaces and APIs; a good example are process identifiers (PIDs). You can peek at process metadata via a pseudo-filesystem called
/proc
, but at a glance, the data doesn’t seem particularly interesting. It’s the stuff you see in the output of
ps
or
top
:
You can’t call
read(…)
on a process identifier. Both PIDs and file descriptors are just integers, but they use the same numbers to reference unrelated things. To be fair, recent Linux kernels have a special system call that lets you convert a PID into a
limited-use file descriptor
, but today, there’s little you can do with that.
But wait, there’s more! If you ever snooped around the
/proc/<pid>/
directory on Linux, you might have noticed a mysterious file that seemingly can’t be read:
To get anything out of that “file”, you need to
lseek(…)
to a specific offset before calling
read(…)
or
write(…)
; alternatively, you can pass the offset when calling
pread(…)
or
pwrite(…)
. If you follow that procedure, you can then seamlessly fetch or modify the memory of the target program in real time.
Here’s how it works in practice — a program that performs self-surgery by accessing the file-based interface (
demo link
):
When I first discovered this API some 25 years ago, I found it to be remarkably elegant. The standard Unix debugging interface,
ptrace(…)
, supports a pair of better-known
PTRACE_PEEKDATA
and
PTRACE_POKEDATA
methods, but
ptrace(…)
is incredibly janky; in contrast,
/proc/<pid>/mem
is beautiful in its simplicity.
Anyway — in 2002, my fascination with this API prompted me to write a program called
memfetch
; the utility allowed you to grab a non-destructive “screenshot” of the memory of any process of your choice, be it to satiate curiosity, to work around anti-debugging features, or to recover data from a non-responsive app. This weekend, I dug it up and overhauled the code to work on modern 64-bit systems. You can download the source
here
.
Some readers might find it amusing that in the early 2000s, Linux 2.2 allowed you to call
mmap(…)
on the resulting
/proc/<pid>/mem
file descriptor, mirroring the memory of the target process to your address space. This was too good to be true: the initial version of
memfetch
would sometimes crash or hang the entire system due to page tables getting out of sync. Soon after, the entire
mmap(…)
logic was yanked out.
Correction:
thanks to Jann Horn who pointed me to pidfds and spotted a mistake related to PTRACE_ATTACH. I initially stated it’s necessary for accessing the file, but it isn’t.
If you are a software engineer, you might also enjoy:
I write original articles about electronics, math, and other stuff. If you like what you see, please subscribe.
