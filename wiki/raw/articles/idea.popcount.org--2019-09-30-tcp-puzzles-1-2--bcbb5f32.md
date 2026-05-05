---
title: "TCP Puzzles 1-2 - Idea of the day"
url: "https://idea.popcount.org/2019-09-30-tcp-puzzles-1-2"
fetched_at: 2026-05-05T07:01:07.175625+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# TCP Puzzles 1-2 - Idea of the day

Source: https://idea.popcount.org/2019-09-30-tcp-puzzles-1-2

TCP Puzzles 1-2
30 September 2019
Recently I've been spending more time looking into Linux TCP
implementation, trying to better understand some corner cases.
Here are two TCP puzzles. Using obvious, almost trivial, Python
snippets, we can show really important design choices made deep in the
networking stack. All we need is a bit of time... and courage to go into the Linux internals!
1. Write buffer vs POLLOUT
Imagine a TCP server and a client connected to it. The server has
plenty of data available. It wants to send it to the client as fast as
possible. One option is to stuff what we have into a large TCP write
buffer. Consider the following two programs.
(1A) Running
send()
until it fails:
c
.
setblocking
(
False
)
while
True
:
try
:
c
.
send
(
b
"A"
*
16384
)
except
io
.
BlockingIOError
:
break
c
.
setblocking
(
True
)
(1B) Running
send()
as long as
poll(POLLOUT)
is happy:
c
.
setblocking
(
False
)
while
True
:
poll
=
select
.
poll
()
poll
.
register
(
c
,
select
.
POLLOUT
)
e
=
poll
.
poll
(
0
)
if
not
e
:
break
c
.
send
(
b
"A"
*
16384
)
c
.
setblocking
(
True
)
Their behavior differs. Can you explain how?
2. TIME-WAIT symmetry
I always found closing TCP sockets to be a mysterious and convoluted process. There are a
number of Linux-specific low level toggles, like "tcp_tw_reuse"
sysctl. To remove some of the mystery, we can illustrate what it does. Here are two, almost identical, programs which behave differently.
(2A) This program works fine - it creates infinite number of short lived connection to 127.0.0.1. It will loop forever:
os
.
system
(
'sysctl net.ipv4.tcp_max_tw_buckets=65535'
)
os
.
system
(
'sysctl net.ipv4.tcp_tw_reuse=0'
)
port
=
1234
s
=
socket
.
socket
(
socket
.
AF_INET
,
socket
.
SOCK_STREAM
,
0
)
s
.
bind
((
'127.0.0.1'
,
port
))
s
.
listen
(
16
)
for
i
in
itertools
.
count
():
if
i
%
10000
==
0
:
print
(
"."
)
c
=
socket
.
socket
(
socket
.
AF_INET
,
socket
.
SOCK_STREAM
,
0
)
c
.
connect
((
'127.0.0.1'
,
port
))
sc
,
_
=
s
.
accept
()
sc
.
close
()
c
.
close
()
(2B) While this program, doing the same thing, will quickly hang:
os
.
system
(
'sysctl net.ipv4.tcp_max_tw_buckets=65535'
)
os
.
system
(
'sysctl net.ipv4.tcp_tw_reuse=0'
)
port
=
1234
s
=
socket
.
socket
(
socket
.
AF_INET
,
socket
.
SOCK_STREAM
,
0
)
s
.
bind
((
'127.0.0.1'
,
port
))
s
.
listen
(
16
)
for
i
in
itertools
.
count
():
if
i
%
10000
==
0
:
print
(
"."
)
c
=
socket
.
socket
(
socket
.
AF_INET
,
socket
.
SOCK_STREAM
,
0
)
c
.
connect
((
'127.0.0.1'
,
port
))
sc
,
_
=
s
.
accept
()
c
.
close
()
sc
.
close
()
# Notice: reordered close()!
Can you explain why reordering
close()
statements made such a big
difference? Why the latter program hangs, as opposed to exiting with
an error? Will the latter program work fine if we set
tcp_tw_reuse=1
, why?
The
tcp_max_tw_buckets
is set to 64k on my Ubuntu, but some systems
ship with different values. Funnily enough even with
tcp_tw_reuse=0
the
tcp_max_tw_buckets
value is important. At 2000 the latter script
works, at 50k it slows down at first and then eventually stops
behaving, at 64k the script properly breaks.
See
this Twitter thread for the answers
.
