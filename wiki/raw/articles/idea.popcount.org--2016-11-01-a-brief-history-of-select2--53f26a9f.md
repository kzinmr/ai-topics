---
title: "A brief history of select(2)"
url: "https://idea.popcount.org/2016-11-01-a-brief-history-of-select2"
fetched_at: 2026-05-05T07:01:10.679708+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# A brief history of select(2)

Source: https://idea.popcount.org/2016-11-01-a-brief-history-of-select2

A brief history of select(2)
I/O multiplexing part #1
01 November 2016
Recently I've been thinking about the multiplexing in Linux, namely
the
epoll(7)
syscall. I was curious if
epoll
is better or worse than the
iocp
or
kqueue
. I was wondering if there was
a benefit in batching
epoll_ctl
calls
. But
let's step back for a while, before we start a serious discussion we
need to get some context. Most importantly - is file descriptor
multiplexing an aberration or a gentle extension to the Unix design
philosophy's?
To answer these question we must first discuss the
epoll
predecessor: the
select(2)
syscall. It's a good excuse to do some Unix archaeology!
In mid-1960's
time sharing
was still a
recent invention. Compared to a previous paradigm - batch-processing -
time sharing was truly revolutionary. It greatly reduced the time
wasted between writing a program and getting its
result. Batch-processing meant hours and hours of waiting often to
only see a program error. See this film to better understand the
problems of 1960's programmers:
"The trials and tribulations of batch processing"
.
VIDEO
Early Unix
Then in 1970 the first versions of
Unix
were developed. It's
important to emphasize that Unix wasn't created in a void - it tried
to fix the batch-processing problems. The intention was to make a
better, multi-user, time-sharing environment to speed up most common
tasks. The "common tasks" were mostly: executing
programs requiring heavy CPU computations and heavy disk access.
These days when a program was executed, it could "stall" (block) only on a couple of things
1
:
wait for CPU
wait for disk I/O
wait for user input (waiting for a shell command) or console (printing data too fast)
Take a look at
the Linux process states
. The
above "stalls" are represented as:
R
,
D
,
S
process states.
Processes in early Unix couldn't do much more really. There was a
pipe(2)
and later a named pipe abstractions, but that's about it.
Let's take a closer look at the
pipe(2)
2
. A colleague of mine
@dwragg
found this gem:
"UNIX Time-Sharing System: A Retrospective"
by Ritchie from 1978. Here's a relevant snippet on the page 1966 (page 20 in the PDF):
There is no general inter-process message facility, nor even a
limited communication scheme such as semaphores. It turns out that
the pipe mechanism mentioned above is sufficient to implement
whatever communication is needed between closely related,
cooperating processes. [...] Pipes are not,
however, of any use in communicating with daemon processes intended
to serve several users.
Here, Ritchie seem to have confirmed that synchronous
pipe
sufficed
as the basic inter-process communication facility.
It might well have been sufficient! In
3BSD
the processes were limited to
maximum of 20 file descriptors
.
Each user was limited to
20 concurrent processes
. These
systems were really rudimentary. There just wasn't a need for
IPC or complex I/O.
For example, in early Unix'es there was no idea of file descriptor multiplexing. A
good example is the
cu(1)
Call Unix
command. The man page says:
When a connection is made to the remote system, cu forks into two
processes. One reads from the port and writes to the terminal, while
the other reads from the terminal and writes to the port.
This makes sense. All of the I/O was blocking. The only way to
read
and
write
at the same time was to use two processes.
As a side note, if you are a Golang programmer, this may sound
familiar. In Golang
read
and
write
calls usually block so you are forced
to use two coroutines when you want to read and write at the same time.
The TCP/IP is born
This all changed in 1983 with the release of 4.2BSD. This revision
introduced an early implementation of a TCP/IP stack and most importantly
- the
BSD Sockets API
.
Although today we take the BSD sockets API for granted, it wasn't
obvious it was the right API.
STREAMS
were a
competing API design on
System V Revision 3
.
With the BSD Sockets API came the
select()
syscall. But why was it
necessary?
I always thought that the "proper" Unix way to write network servers
in was to create one worker process for each
connection. In case of TCP/IP servers, this meant the accept-and-fork
model:
sd
=
bind
();
while
(
1
)
{
cd
=
accept
(
sd
);
if
(
fork
()
==
0
)
{
close
(
sd
);
// Worker code goes here. Do the work for `cd` socket.
exit
(
0
);
}
// Get back to `accept` loop. Don't leak the `cd`.
close
(
cd
);
}
While this model may be sufficient for writing basic network services
3
,
it's not enough for non-trivial programs.
Terminal multiplexing
Around 1983,
Rob Pike
was developing
Blit
, a
fancy graphical terminal for
Research Unix 8th Edition
. Best
to see it in action:
VIDEO
Here's the
Blit research paper
for the curious.
Blit clearly did terminal multiplexing. It allowed users to interact with
multiple virtual consoles over a single physical serial link.
I asked Mr. Pike about the history of
select
:
Accept-and-fork, as you call it, makes it impossible for multiple
clients to share state on the server. It's not just about networking
either; one influence was the work with the Blit.
While running two synchronous processes to power
cu
was sufficient,
it wasn't enough to power Blit. Blit did require some kind of socket
multiplexing facility to work smoothly.
I would speculate that there was an theoretical alternative. One might
try to extend the
cu
model and hack together a file descriptor
multiplexer by spawning multiple processes blocking on I/O and having
them synchronized on some kind of IPC.
Unfortunately no decent IPC mechanisms existed for
BSD.
System V
IPC
was released in January 1983, but nothing comparable was implemented
on BSD. I went through the
4.2BSD man pages
and couldn't find any kind of real IPC
4
.
With lack of any serious IPC mechanisms, it seems likely that Blit
simply needed
select
to be able to do the console multiplexing.
Back to sockets
I contacted
Kirk McKusick
about the history of
select
. He replied:
Select was introduced to allow applications to multiplex their I/O.
Consider a simple application like a remote login. It has
descriptors for reading from and writing to the terminal and a
descriptor for the (bidirectional) socket. It needs to read from the
terminal keyboard and write those characters to the socket. It also
needs to read from the socket and write to the terminal. Reading
from a descriptor that has nothing queued causes the application to
block until data arrives.  The application does not know whether to
read from the terminal or the socket and if it guesses wrong will
incorrectly block. So select was added to let it find out which
descriptor had data ready to read.  If neither, select blocks until
data arrives on one descriptor and then awakens telling which
descriptor has data to read.
[...] Non-blocking was added at the same time as select. But using
non-blocking when reading descriptors does not work well. Do you go
into an infinite loop trying to read each of your input descriptors?
If not, do you pause after each pass and if so for how long to
remain responsive to input?  Select is just far more efficient.
Select also lets you create a single inetd daemon rather than having to
have a separate daemon for every service.
Here we are. Mr. McKusick confirms that non-blocking I/O simply didn't
exist before
select
. Furthermore, he cites the
cu
terminal use
case - it would be hard to write a
telnet
client without I/O
multiplexing. Finally, he mentions
inetd
, which although introduced
later in 4.3BSD, would have been impossible without
select
.
Recap
Having to run two processes to get
cu
working was a hack. With
lack of any serious IPC it was impossible to emulate socket
multiplexing in Blit without
select
.
Furthermore
select
was needed to implement
inetd
. On architecture
level
select
is needed to implement stateful servers which allow some
state sharing between client connections.
Here's another snippet from the
"UNIX Time-Sharing System: A Retrospective"
page 1966:
[In UNIX] input and output ordinarily appear to be synchronous;
programs wait until their I/O is completed. [...] There remain
special applications in which one desires to initiate I/O on several
streams and delay until the operation is complete on only one of
them. When the number of streams is small, it is possible to
simulate this usage with several processes.  However, the writers of
a UNIX ncp ("network control program") interface to the Arpanet feel
that genuinely asynchronous I/O would improve their implementation
significantly.
Early Unix systems were pretty basic and
select
was simply not needed. It's not that blocking I/O model in C was
deemed the best programming paradigm for everyone. This model made
sense because all you could do were simple operations on files.
This all was changed with the advent of network. Network application
required things like
inetd
, stateful servers and terminal emulators
like
telnet
. These things would be hard to implement had the OS not
allowed socket multiplexing.
Conclusion
In this discussion I was afraid to phrase the core question. Were Unix
processes intended to be
CSP-style
processes? Are file descriptors a CSP-derived "channels"? Is
select
equivalent to
ALT
statement?
I think: no. Even if there are design similarities, they are
accidental. The file-descriptor abstractions were developed well
before the original CSP paper.
It seems that an operating socket API's evolved totally disconnected
from the userspace CSP-alike programming paradigms. It's a pity
though. It would be interesting to see an operating system coherent
with the programming paradigms of the user land programs.
Let me leave you with a couple of vaguely related links:
Ever wondered why
select
uses a bit mask to pass file descriptor list to kernel? Because 4.2BSD allowed only
20 file descriptors per program
.
History of Actors
programming model
Channel I/O
STREAMS
and
Solaris Guide
and
"A Stream Input-Output System"
by Ritchie.
mpx
and
mpxio
or
mpxcall
- an early IPC / file desciptor multiplexing API. I think these were introduced in 1979
Version 7 Unix
: "Multiplexed files: 
A feature that did not survive long was a second way (besides pipes) to do inter-process communication: multiplexed files. A process could create a special type of file with the mpx system call; other processes could then open this file to get a "channel", denoted by a file descriptor, which could be used to communicate with the process that created the multiplexed file. Mpx files were considered experimental, not enabled in the default kernel, and disappeared from later versions, which offered sockets (BSD) or CB UNIX's IPC facilities (System V) instead (although mpx files were still present in 4.1BSD)."
Update:
Mr. Pike clarified a bit of early history:
Greg Chessons mpx was in v7 unix by the late 1970s, well before 1983
and BSD. Sockets were just one attempt in a crowded environment. The
predecessor to the Blit used Greg's mpx. I think the very earliest
Blit stuff did too, but by the time the movie was made v8 had
happened and Dennis Ritchie gave me streams and select (but no sockets!).
Select and sockets were roughly the same time but not necessarily
two parts of one thing.
The last statement is telling.
select
came at the same time as
sockets, but it wasn't implemented purely for networking. It seems that
all of multiplexing, sockets and IPC came at about the same time,
without a coherent grand design.
A number of people helped with this article: Rob Pike, Kirk McKusick, Ólafur Guðmundsson, Martin J. Levy, David Wragg and Tony Garnock-Jones. Thanks!
Update:
In
a twitter exchange
Clifford Heath noted that there was nonblocking I/O on TTY devices
before 1983.
There was nonblocking I/O before 1983. The University of Melbourne
CS dept paused in 1980/1 to play Hack, and I used it for Pacman.
I wonder how it worked. What ioctl's did it use and what were the
semantics. Perhaps
read()
was nonblocking?
Upate:
Paul Ruizendaal followed up this blog post with some more
investigation into early history. His findings are documented in
The History of Unix
mailing list:
Continue reading about
Select() being fundamentally broken →
