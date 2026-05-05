---
title: "Creating sockets"
url: "https://idea.popcount.org/2019-11-06-creating-sockets"
fetched_at: 2026-05-05T07:01:07.348821+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Creating sockets

Source: https://idea.popcount.org/2019-11-06-creating-sockets

Creating sockets
06 November 2019
Articles from this series:
Creating sockets
on Linux.
Addressing of AF_INET, AF_INET6 and AF_UNIX
sockets.
Our journey into the Linux networking API starts with the common
socket()
syscall:
int
socket
(
int
domain
,
int
type
,
int
protocol
);
It takes three arguments:
domain
specifies an address family. Most commonly used are IPv4, IPv6 and Unix sockets - AF_INET, AF_INET6 and AF_UNIX families. Linux supports more families, notably AF_PACKET, AF_NETLINK, AF_ALG and AF_VSOCK are sometimes handy.
type
specifies communication semantics. Most common are streaming SOCK_STREAM, usually TCP and  datagram SOCK_DGRAM, usually UDP. Unix sockets also support sequenced datagrams - SOCK_SEQPACKET.
protocol
specifies a concrete protocol type - this is where we can explicitly request TCP, UDP protocols. This field can be left blank to allow the operating system to choose the default.
AF_INET and AF_INET6
Linux supports a myriad of address families and protocols, but most of
them are rarely used. To communicate in the public internet, it's
necessary to use AF_INET and AF_INET6 - the Internet IPv4 and IPv6
address families. Most often we use them with with TCP and UDP
protocols
1
.
The usual way to create internet IPv4 sockets is:
int
fd
=
socket
(
AF_INET
,
SOCK_STREAM
,
0
);
// IPv4, TCP
int
fd
=
socket
(
AF_INET
,
SOCK_DGRAM
,
0
);
// IPv4, UDP
And IPv6:
int
fd
=
socket
(
AF_INET6
,
SOCK_STREAM
,
0
);
// IPv6, TCP
int
fd
=
socket
(
AF_INET6
,
SOCK_DGRAM
,
0
);
// IPv6, UDP
In Linux IPv4 and IPv6 networks stacks are interacting in complex
ways. For example, you can create an AF_INET6 socket on IPv4-mapped
addresses - like ::ffff:127.0.0.1. Then you could downgrade such
AF_INET6 socket onto AF_INET with IPV6_ADDRFORM socket option. We'll
discuss these things later, but for now note: IPv4 and IPv6
networking stacks on Linux are entangled.
AF_UNIX
While AF_INET/AF_INET6 address families route packets over the
network, AF_UNIX address family only works within local machine. With
AF_UNIX it's possible to transmit data between processes on the same
machine much faster, without spending CPU on things like IP firewall
and routing table. The behavior or AF_UNIX + SOCK_STREAM sockets is
comparable to TCP, and AF_UNIX + SOCK_DGRAM to UDP. UNIX socket have
advantages - they don't need to allocate internet addresses and ports,
don't reorder packets are reliable and much faster. Example setup:
int
fd
=
socket
(
AF_UNIX
,
SOCK_STREAM
,
0
);
int
fd
=
socket
(
AF_UNIX
,
SOCK_DGRAM
,
0
);
int
fd
=
socket
(
AF_UNIX
,
SOCK_SEQPACKET
,
0
);
SOCK_SEQPACKET is an underrated communication paradigm. It's
connection-oriented and reliable like TCP, but is able to preserve
record/message boundaries like UDP
2
. Such semantics are very
programmer-friendly and useful in practice.
When to choose AF_UNIX over AF_INET?
If you are exchanging data between two processes on the same Linux
host, you should use AF_UNIX. It's faster, supports the common Unix
filesystem permissions model, and don't have the annoying limitations
of TCP/IP - like a  need to allocate port numbers.
Why allocating TCP port numbers is such a big deal? TCP/IP ports are a
limited resource. It's not uncommon to run out of them! In past I
discussed a war story
when a bug in one program can lead to the system running out of port
numbers for localhost connections, therefore hampering all
applications on a machine.
Similarly - using large number of short-lived connections is also
risky. In such case it's possible to end up with many sockets locked in TIME-WAIT
state, preventing new connections from being established. See the
2nd TCP Puzzle
for an example of this behavior.
The advice is - when possible, prefer AF_UNIX over AF_INET. There is
almost no disadvantage of using AF_UNIX. Except maybe one -
debugability. It's way easier to just run
tcpdump
and see Internet
packets flowing by. Fortunately there is a workaround. The solution is
is to pipe the data from UNIX socket to INET socket and back with the
help of
socat
tool. For example:
ln real.sock real.sock~
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CONNECT:real.sock~
socat UNIX-LISTEN:fake.sock,fork TCP-CONNECT:127.0.0.1:6000
mv fake.sock real.sock
This reads as:
Create a hard-link of our debugged socket and name it
real.sock~
.
Accept connections on 127.0.0.1:6000 and forward them to
real.sock~
with
socat
.
Accept connections on
fake.sock
and forward them to 127.0.0.1:6000.
Atomically replace
real.sock
with
fake.sock
.
After this sequence of instructions all the data will pass over loopback, and it is possible to debug it with usual
tcpdump
. To revert the probe, just run:
ln -f real.sock~ real.sock
This will overwrite our mocked
real.sock
back with the real one. Remember to wait for the old connections to die off before killing
socat
instances. This trick will work for SOCK_STREAM and SOCK_DGRAM, but not for SOCK_SEQPACKET, and of course requires a Unix socket that is bound to a pathname (ie: not abstract or unnamed Unix sockets).
The
type
argument to
socket()
syscall is most often SOCK_STREAM, SOCK_DGRAM or SOCK_SEQPACKET. There is one more caveat about this field - you can squeeze two flags there: SOCK_NONBLOCK and SOCK_CLOEXEC flags.
SOCK_NONBLOCK
SOCK_NONBLOCK flag can be used to avoid having to call
fcntl()
twice to set socket as non-blocking. The code:
int
fd
=
socket
(
AF_INET
,
SOCK_STREAM
|
SOCK_NONBLOCK
,
0
);
if
(
fd
<
0
)
{
return
errno
;
}
Is equivalent to:
int
fd
=
socket
(
AF_INET
,
SOCK_STREAM
,
0
);
if
(
fd
<
0
)
{
return
errno
;
}
int
flags
=
fcntl
(
fd
,
F_GETFL
);
if
(
flags
==
-
1
)
{
return
errno
;
}
int
r
=
fcntl
(
fd
,
F_SETFL
,
flags
|
O_NONBLOCK
);
if
(
r
==
-
1
)
{
return
errno
;
}
Using SOCK_NONBLOCK is an easy win, and can save quite a few lines of code.
SOCK_CLOEXEC
Second flag that can be passed in the
type
field is SOCK_CLOEXEC. It looks like this:
int
fd
=
socket
(
AF_INET
,
SOCK_STREAM
|
SOCK_CLOEXEC
,
0
);
This is roughly equivalent to setting FD_CLOEXEC with
fcntl()
:
r
=
fcntl
(
fd
,
F_SETFD
,
FD_CLOEXEC
)
The semantics of CLOEXEC are pretty simple - this flag ensures that
when the program calls
exec()
the file descriptor will be closed
before starting the desired program. Passing a socket to a child
program may be problematic. To illustrate this, consider the program:
int
fd
=
socket
(
AF_INET
,
SOCK_STREAM
,
0
);
...
int
r
=
connect
(
fd
,
(
struct
sockaddr
*
)
&
sa
,
sizeof
(
sa
));
...
if
(
fork
()
==
0
)
{
system
(
"sleep 100"
);
exit
(
0
);
}
close
(
fd
);
Here, even though we called
close()
the socket will not in fact
shutdown. The socket will remain active for 100 seconds, wasting resources, until the
child process exits and closes the last remaining reference to the
socket.
The FD_CLOEXEC and SOCK_CLOEXEC subtly differ. Consider
a sequence of
socket()
and
fcntl()
calls like this:
int
fd
=
socket
(
AF_INET
,
SOCK_STREAM
,
0
);
...
...
// What if another thread calls fork()?
...
r
=
fcntl
(
fd
,
F_SETFD
,
FD_CLOEXEC
)
This code is racy. It's possible that a thread, doing some other work in
background, might call
fork()
in the least appropriate moment - just
between the socket and fcntl calls! This would, again, lead to a socket
leaking to the child process
3
.
For completeness, on Linux it's also possible to set CLOEXEC flag with
unstandardized
ioctl()
:
int
r
=
ioctl
(
fd
,
FIOCLEX
);
Use
FIONCLEX
to clear the flag.
socket() errors
The
socket()
syscall returns a new file descriptor or an error.
EMFILE
is returned when per-process fd limit is reached. You can inspect the default value with
$ ulimit -n
. Alternatively call
getrlimit(RLIMIT_NOFILE)
within the process to see the current limit. To fix the problem, the process must release some file descriptors. Some ancient Unix programs anticipated hitting this limit. To keep on functioning even in such error case, they kept a dummy file descriptor to some irrelevant file, like
/dev/null
. Before running into critical section, like saving state to disk, the dummy fd would be closed, the critical section run, and dummy file re-opened. With this trick the program could be confident that it won't see EMFILE in the critical section and reduced the risk of loosing important state.
ENFILE
is raised on hitting the global file descriptor limit or
memory limit. Inspect the global limit with
$ cat
/proc/sys/fs/file-max
or
sysctl fs.file-max
. Generally speaking,
fixing this error is a job for system administrator - if the memory allows,
she should consider bumping the global limit.
Then there is
EPERM
error which is raised when user doesn't have permissions to open sockets. Practically speaking this is a concern for AF_PACKET/SOCK_RAW sockets. To open these you need to be root or have CAP_NET_RAW capability.
Testing programs for handling of these errors is hard. On Linux we can try injecting fake error return codes - injecting faults. On Linux there are numerous ways to inject faults to aid testing, but perhaps the easiest one is to use injection facility of
strace
tool. This is how to make every 10th
socket()
syscall to fail with EMFILE:
$
strace
\
-e
trace
=
none
\
-e
inject
=
socket:error
=
EMFILE:when
=
10+10
\
./program.py
Read the
man page of modern
strace
for detailed description of the rich fault injection facilities.
Retrieving socket type
Sometimes a process is given a file descriptor, without any prior
knowledge. For example an fd can be inherited from a parent process,
or retrieved via SCM_RIGHTS Unix socket.
Given such a file descriptor, we might want to query kernel to learn its properties. First, it's easy to recover address family, type and protocol:
int
r
;
socklen_t
r_sz
=
sizeof
(
r
);
getsockopt
(
SOL_SOCKET
,
SO_DOMAIN
,
&
r
,
&
r_sz
);
getsockopt
(
SOL_SOCKET
,
SO_TYPE
,
&
r
,
&
r_sz
);
getsockopt
(
SOL_SOCKET
,
SO_PROTOCOL
,
&
r
,
&
r_sz
);
With this information we should know if socket is TCP or UDP. But it doesn't tell us on which stage of lifetime the socket is:
newly created socket descriptor
listening (TCP), unconnected (UDP)
established (TCP), connected (UDP)
Linux doesn't allow us to read this status easily. Instead we have to
look a series of clues to recover the socket lifetime information. There are three most important clues:
Does
getsockname()
return local port equal zero?
Does
getpeername()
return with ENOTCONN error?
The value of
getsockopt(SO_ACCEPTCONN)
syscall.
This is how these clues look on listening/unconnected sockets:
lport
getpeername
()
SO_ACCEPTCONN
socket
(
AF_INET
,
STREAM
)
0
ENOTCONN
0
bind
()
57329
ENOTCONN
0
listen
()
57329
ENOTCONN
1
socket
(
AF_INET
,
DGRAM
)
0
ENOTCONN
0
bind
()
35918
ENOTCONN
0
The established/connected sockets:
lport
getpeername
()
SO_ACCEPTCONN
socket
(
AF_INET
,
STREAM
)
0
ENOTCONN
0
bind
()
49245
ENOTCONN
0
connect
()
49245
ok
0
socket
(
AF_INET
,
DGRAM
)
0
ENOTCONN
0
bind
()
35918
ENOTCONN
0
connect
()
35918
ok
0
But in practice running all these tests may be an overkill. Often, just calling
listen()
on an unconnected TCP socket is sufficient to get socket to a predictable state.  The error codes indicate the socket status: ENOTSOCK means it's not a socket and EOPNOTSUPP means it's not unconnected TCP.
Socket activation
Sometimes it's worthwhile to ask an intermediary to establish sockets for us. This is most useful when:
A socket with specific port number is needed, and we want to make sure it's allocated early in the life of the system, to avoid port number clashes.
A privileged socket is needed.  That can be a raw socket needed to perform
ping
or
traceroute
, or more often just a normal TCP Listen socket bound to a privileged port.
In such situations it's recommended to pass-down the privileged socket from the parent process - most commonly systemd. Systemd supports this as a "socket activation" feature.  Systemd will set LISTEN_FDS environment variable, explaining how many file descriptors belongs were passed down with socket activation (counting from fd number 3 and up). Then it
will set LISTEN_FDNAMES and LISTEN_PID
.
Example of a systemd socket configuration:
$
cat /etc/systemd/system/socket-port-80.socket
[
Unit
]
Description
=
Port 80/TCP
[
Socket
]
Service
=
daemon.service
ListenStream
=
0.0.0.0:80
FileDescriptorName
=
socket-port-80
[
Install
]
WantedBy
=
sockets.target
An an example daemon service using such a socket:
$
cat /etc/systemd/system/daemon.servie
[
Unit
]
Description
=
Important Network Daemon
Requires
=
socket-port-80.socket
After
=
network.target
[
Service
]
User
=
nobody
Group
=
nobody
ExecStart
=
/daemon
Restart
=
on-failure
RestartSec
=
15
Sockets
=
socket-port-80.socket
[
Install
]
WantedBy
=
default.target
On startup, the daemon needs to recognize the inherited sockets. Systemd provides LISTEN_PID, LISTEN_FDS and LISTEN_FDNAMES env variables. Here is an example code that could be used to pick up the passed descriptors:
listenfds
=
int
(
os
.
environ
.
get
(
'LISTEN_FDS'
,
'0'
))
fdnames
=
os
.
environ
.
get
(
'LISTEN_FDNAMES'
,
''
)
.
split
(
':'
)
if
len
(
fdnames
)
!=
listenfds
:
return
"LISTEN_FDS doesn't match LISTEN_FDNAMES"
SOCKETS
=
[]
for
fd
,
fdname
in
zip
(
range
(
3
,
listenfds
+
3
),
fdnames
):
# In python we need socket object to call getsockopt
tmp_sd
=
socket
.
fromfd
(
fd
,
0
,
0
,
0
)
try
:
domain
=
tmp_sd
.
getsockopt
(
SOL_SOCKET
,
SO_DOMAIN
)
type
=
tmp_sd
.
getsockopt
(
SOL_SOCKET
,
SO_TYPE
)
protocol
=
tmp_sd
.
getsockopt
(
SOL_SOCKET
,
SO_PROTOCOL
)
except
OSError
:
# not a socket
pass
else
:
sd
=
socket
.
socket
(
domain
,
type
,
protocol
,
fileno
=
fd
)
SOCKETS
.
append
(
(
fdname
,
sd
)
)
# tmp_sd is a dup, we must close it
tmp_sd
.
close
()
return
SOCKETS
This socket activation code will only work with systemd - it relies on LISTEN_FDNAMES environment variable. Sometimes we need to work with other implementations of socket activation. A slightly more generic method to achieve socket activation, is just to traverse file descriptor numbers in ascending order, looking for sockets passed down from a parent.
In such case we just need to make an assumption on when to stop our search for valid file descriptors, or specifically: after how large gap in file descriptor numbers we stop?
MAXCONTIGOUSFDGAP
=
32
gap
=
0
SOCKETS
=
{}
for
fd
in
itertools
.
count
(
3
):
# In python we need socket object to call getsockopt
# this dup()s the fd.
try
:
tmp_sd
=
socket
.
fromfd
(
fd
,
0
,
0
,
0
)
except
OSError
as
e
:
if
e
.
errno
==
errno
.
EBADF
:
gap
+=
1
if
gap
>
MAXCONTIGOUSFDGAP
:
break
continue
else
:
raise
e
gap
=
0
try
:
# This can trigger EBADF
domain
=
tmp_sd
.
getsockopt
(
SOL_SOCKET
,
SO_DOMAIN
)
sock_type
=
tmp_sd
.
getsockopt
(
SOL_SOCKET
,
SO_TYPE
)
protocol
=
tmp_sd
.
getsockopt
(
SOL_SOCKET
,
SO_PROTOCOL
)
except
OSError
as
e
:
# not a socket
pass
else
:
SOCKETS
[
fd
]
=
socket
(
domain
,
sock_type
,
protocol
,
fd
)
tmp_sd
.
close
()
This solution stops iterating over file descriptors when a gap of defined size is found. Yet another technique could use
/proc/self/fd
directory to iterate over only valid file descriptor numbers.
Dissolving the socket association
From the application point of view, file descriptors end their life when application calls
close()
. Depending on the protocol the socket itself may linger in the background for a while. There is a myriad toggles available for different protocols, from
setsockopt(SO_LINGER)
, to
shutdown()
. We'll discuss these options later.
However, there is one obscure way to recycle a socket descriptor without really closing it. Some protocols allow calling
connect(AF_UNSPEC)
on a connected socket, which will "dissolve the socket association" - reset the socket state, and bring it back to pristine state, like just after calling
socket()
. Beware though, some obscure socket flags may not be cleaned correctly. Here is an example code of this trick:
int
sd
=
socket
(
AF_INET
,
SOCK_STREAM
,
0
);
...
int
r
=
connect
(
sd
,
(
struct
sockaddr
*
)
&
sa
,
sizeof
(
sa
));
...
struct
sockaddr
su
=
{
.
sa_family
=
AF_UNSPEC
,
};
r
=
connect
(
sd
,
(
struct
sockaddr
*
)
&
su
,
sizeof
(
su
));
if
(
r
<
0
)
{
error
(
-
1
,
errno
,
"connect(AF_UNSPEC)"
);
}
...
r
=
connect
(
sd
,
(
struct
sockaddr
*
)
&
sa
,
sizeof
(
sa
));
...
This AF_UNSPEC socket dissolve trick is totally ugly, but it can save us a syscall. Instead of calling
close()
and then
socket()
, we can do a single
connect(AF_UNSPEC)
only. The big issue is it's not obvious which internal socket fields are reset and which are preserved.
socketpair()
There is one final way to create sockets which specific to UNIX address family. We can create a pair of sockets with
the
socketpair()
syscall
. For example:
int
sv
[
2
];
int
r
=
socketpair
(
AF_UNIX
,
SOCK_STREAM
,
0
,
sv
);
This creates
sv[0]
and
sv[1]
UNIX sockets, connected to each other. This syscall works for all UNIX domain socket types.  The created sockets are special - both are "connected" from the start. Their getsockaddr/getpeeraddr functions return a special value - not even empty address family string, but a lack of thereof. This is called "unnamed" UNIX sockets. More about this in UNIX sockets addressing section.
Totally comment
this article on Twitter!
