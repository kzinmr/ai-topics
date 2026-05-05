---
title: "Bind before connect"
url: "https://idea.popcount.org/2014-04-03-bind-before-connect"
fetched_at: 2026-05-05T07:01:12.350532+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Bind before connect

Source: https://idea.popcount.org/2014-04-03-bind-before-connect

Bind before connect
03 April 2014
A TCP/IP connection is identified by a four element tuple: {source IP,
source port, destination IP, destination port}. To establish a TCP/IP
connection only a destination IP and port number are needed, the
operating system automatically selects source IP and port. This
article explains how the Linux kernel does the source port allocation.
Ephemeral port range
To establish a connection
BSD API
requires two
steps: first you need to create a socket, then call
connect()
on
it. Here's some code in Python:
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
)
s
.
connect
((
"www.google.com"
,
80
))
When a connection is made the operating system needs to select an
unused source port number. Linux selects a port from an
ephemeral port range
,
which by default is a set to range from 32768 to 61000:
$
cat /proc/sys/net/ipv4/ip_local_port_range
32768   61000
On Linux the ephemeral port range is a global resource
1
, it's not a
specific setting local to an IP address.
Let's dig into details on how exactly a source port is selected. The
main work is done in the
__inet_hash_connect
function.
Here's an excerpt (with many lines of code removed for simplicity):
static
u32
hint
;
inet_get_local_port_range
(
net
,
&
low
,
&
high
);
remaining
=
(
high
-
low
)
+
1
;
for
(
i
=
1
;
i
<=
remaining
;
i
++
)
{
port
=
low
+
(
i
+
hint
)
%
remaining
;
head
=
&
hinfo
->
bhash
[
inet_bhashfn
(
net
,
port
,
hinfo
->
bhash_size
)];
inet_bind_bucket_for_each
(
tb
,
&
head
->
chain
)
{
if
(
net_eq
(
ib_net
(
tb
),
net
)
&&
tb
->
port
==
port
)
{
if
(
tb
->
fastreuse
>=
0
||
tb
->
fastreuseport
>=
0
)
goto
next_port
;
if
(
!
check_established
(
death_row
,
sk
,
port
,
&
tw
))
goto
ok
;
goto
next_port
;
}
}
tb
=
inet_bind_bucket_create
(
hinfo
->
bind_bucket_cachep
,
net
,
head
,
port
);
goto
ok
;
next_port:
}
[...]
ok:
hint
+=
i
;
In translation: we start with a
hint
port number
2
and increase it
until we find a source port that is either:
Completely unused.
Used by some connections but it's ok for it to be reused: it
    passes the
check_established
check.
By default there are 28232 ports in the ephemeral range, so the first
condition could be matched at most that number of times. If you have
more than 28k connections Linux will need to find a port that passes
check_established
check. It's okay to reuse a port if no connection already exists
between the same source and destination endpoints.
With multiple destination addresses it's possible to have pretty much
unlimited
3
number of connections. But establishing more than 28k
concurrent connections to a single {destination IP, destination port}
pair will fail.
What if you really want to establish more than 28k connections to a
single destination? There are a couple of tweaks you can make:
Increase the
ip_local_port_range
pool. Setting it to maximum
    range will allow 64511 concurrent connections (65535-1024).
Set
tcp_tw_reuse
sysctl
to
enable reusing of TIME_WAIT sockets
.
Do
not
set
tcp_tw_recycle
. It will cause SYN's to be dropped
    for users behind a NAT.
If you really want to establish even more than 64k connections to a
single destination address you'll have to use more than one source IP
address.
Bind before connect
It is possible to ask the kernel to select a specific source IP and
port by calling
bind()
before calling
connect()
:
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
)
# Let the source address be 192.168.1.21:1234
s
.
bind
((
"192.168.1.21"
,
1234
))
s
.
connect
((
"www.google.com"
,
80
))
This trick is often called, wait for it..., "bind before
connect". Specifying port number
0
means that the kernel should do a
port allocation for us:
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
)
s
.
bind
((
"192.168.1.21"
,
0
))
s
.
connect
((
"www.google.com"
,
80
))
This method is fairly well known, but there's a catch.
Bind
is
usually called for listening sockets so the kernel needs to make sure
that the source address is not shared with anyone else. It's a
problem. When using this techique in this form it's impossible to
establish more than 64k (ephemeral port range) outgoing connections in
total. After that the attempt to call
bind()
will fail with an
EADDRINUSE
error - all the source ports will be busy.
To work around this we need to understand two flags that affect the
kernel port allocation behaviour:
SO_REUSEADDR
and
SO_REUSEPORT
.
SO_REUSEADDR
SO_REUSEADDR
is mentioned in only two man pages:
Man
ip(7)
:
A TCP local socket address that has been bound is unavailable for
  some time after closing, unless the SO_REUSEADDR flag has been set.
  Care should be taken when using this flag as it makes TCP less
  reliable.
Man
socket(7)
:
SO_REUSEADDR: Indicates that the rules used in validating addresses
  supplied in a bind(2) call should allow reuse of local addresses.
  For AF_INET sockets this means that a socket may bind, except when
  there is an active listening socket bound to the address.  When the
  listening socket is bound to INADDR_ANY with a specific port then it
  is not possible to bind to this port for any local address.
  Argument is an integer boolean flag.
Don't worry if it sounds confusing, here's how I understand it:
By setting
SO_REUSEADDR
user informs the kernel of an intention to
share the bound port with anyone else, but only if it doesn't cause a
conflict on the protocol layer. There are at least three situations
when this flag is useful:
Normally after binding to a port and stopping a server it's
   neccesary to wait for a socket to time out before another server
   can bind to the same port. With
SO_REUSEADDR
set it's possible
   to rebind immediately, even if the socket is in a
TIME_WAIT
state.
When one server binds to
INADDR_ANY
, say
0.0.0.0:1234
, it's
   impossible to have another server binding to a specific address
   like
192.168.1.21:1234
. With
SO_REUSEADDR
flag this behaviour
   is allowed.
When using the bind before connect trick only a single connection
   can use a single outgoing source port. With this flag, it's
   possible for many connections to reuse the same source port, given
   that they connect to different destination addresses.
SO_REUSEPORT
SO_REUSEPORT
is poorly documented. It was introduced for UDP
multicast sockets. Initially, only a single server was able to use a
particular port to listen to a multicast group. This flag allowed
different sockets to bind to exactly the same IP and port, and receive
datagrams for
selected multicast groups
.
More generally speaking, setting
SO_REUSEPORT
infroms a kernel of an
intention to share a particular bound port between many processes, but
only for a single user. For multicast datagrams are distributed based
on multicast groups, for usual
UDP
datagrams are distributed in
round-robin way. For a long time this flag wasn't available for
TCP
sockets, but recently Google submitted patches that fix it and
distribute incoming connections
in round-robin way between listening sockets
.
The best explanation of these flags I found
in this stackoverflow answer
.
Port allocation
With
0
passed to
bind
the kernel does a source port allocation:
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
)
s
.
bind
((
"192.168.1.21"
,
0
))
This type of port allocation works differently than when using
straight
connect()
. I won't paste
the kernel code
here, it's rather brutal. Basically, the kernel doesn't use
hint
variable as previously, instead it selects a random port from the
ephemeral range and
increases it until it finds a conflict-free port
.
What is
a "conflict-free" very much depends on the
SO_REUSEADDR
and
SO_REUSEPORT
flags
.
Although supported by the code, setting
SO_REUSEPORT
and asking
kernel to allocate a port number makes little sense. I doubt it's used
by anyone (prove me wrong!).
On the other hand
SO_REUSEADDR
is very handy. Usage example:
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
)
s
.
setsockopt
(
socket
.
SOL_SOCKET
,
socket
.
SO_REUSEADDR
,
1
)
s
.
bind
((
"192.168.1.21"
,
0
))
s
.
connect
((
"www.google.com"
,
80
))
In this case the kernel will find a port that doesn't directly
conflict with other socket but, as opposed to the lack of
SO_REUSEADDR
setting, ports in
TIME_WAIT
and used by already
established connections may be reused. Therefore by setting
SO_REUSEADDR
flag it is possible to have more than 64k (ephemeral
port range) outgoing connections from a single selected IP to multiple
destinations.
But there's another catch: when we call
bind()
the kernel knows only
the source address we're asking for. We'll inform the kernel of a
destination address only when we call
connect()
later. This may lead
to problems as kernel may reuse source port already used by another
connection possibly to the same desitnation we want to use. In such
case
connect()
will fail with
EADDRNOTAVAIL
error. Here's a code
handling this situation:
for
i
in
range
(
RETRIES
):
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
)
s
.
setsockopt
(
socket
.
SOL_SOCKET
,
socket
.
SO_REUSEADDR
,
1
)
s
.
bind
((
"192.168.1.21"
,
0
))
try
:
s
.
connect
((
"www.google.com"
,
80
))
break
except
socket
.
error
,
e
:
if
e
.
errno
!=
errno
.
EADDRNOTAVAIL
:
raise
else
:
raise
Exception
(
"Failed to find an unused source port"
)
If you want to establish more than 64k (ephemeral port range)
connections to a single destination, you need to use all the tricks:
Tweak kernel parameters to increase ephemeral port range.
Manually specify many source IP addresses by using bind before
   connect.
Set
SO_REUSEADDR
flag on outging connections.
Check
bind()
for
EADDRINUSE
errors, in case we run out of
   available ports.
Check
connect()
for
EADDRNOTAVAIL
errors in case there is a
   connection conflict and retry if neccesary.
Don't mix
Unfortunately, connections established with normal
connect
and with
bind before connect don't mix well. Outgoing ports used by one
technique can't be reused by another. If you establish 64k connections
using
connect
,
bind
will fail with
EADDRINUSE
. And the other way
around: when thousands of connections are using bind before connect
straight
connect
might fail with
EADDRNOTAVAIL
.
Summary
To wrap it up:
If you can, just use straight
connect()
, the kernel does a good
   job at allocating source ports.
If you need to select a source IP manually, for whatever reason,
   normally you'll be limited to one outgoing connection for one
   ephemeral port: destination address is not taken into
   account. This limits number of outgoing connections considerably.
Therefore if you need to specify a source IP consider setting
SO_REUSEADDR
flag to enable address reuse. This will increase
   number of possible connections, but you will need to handle
   possible
connect()
EADDRNOTAVAIL
errors.
When calling
bind()
consider selecting other IP addresses than the
   default outgoing IP address for your network. Filling ephemeral
   range on the default outgoing IP may cause problems with
   applications that use normal
connect()
.
Comments
From: Maciej Żenczykowski

(a) on Linux SO_REUSEPORT is meant to be used *purely*
for load balancing multiple incoming UDP packets or
incoming TCP connection requests across multiple sockets
belonging to the same app.  ie. it's a work around for
machines with a lot of cpus, handling heavy load, where
a single listening socket becomes a bottleneck because of
cross-thread contention on the in-kernel socket
lock (and state).

(b) set IP_BIND_ADDRESS_NO_PORT socket option for
tcp sockets before binding to a specific source ip
with port 0 if you're going to use the socket for
connect() rather then listen() this allows the kernel
to delay allocating the source port until connect()
time at which point it is much cheaper
