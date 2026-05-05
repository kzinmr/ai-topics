---
title: "Addressing - Idea of the day"
url: "https://idea.popcount.org/2019-12-06-addressing"
fetched_at: 2026-05-05T07:01:07.465826+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Addressing - Idea of the day

Source: https://idea.popcount.org/2019-12-06-addressing

Addressing
06 December 2019
Articles from this series:
Creating sockets
on Linux.
Addressing of AF_INET, AF_INET6 and AF_UNIX
sockets.
A freshly created socket isn't very useful. We have to tell it to
either listen for incoming data, or connect to a remote peer. To
achieve anything useful we need to perform a syscall dance, which
involves either
bind()
or
connect()
or both.
Among others,
bind()
and
connect()
syscalls take a socket address
as a parameter. Before going into these syscalls we must discuss what
exactly the address is. Specifically, they take
struct sockaddr
:
struct
sockaddr
{
sa_family_t
sa_family
;
char
sa_data
[
14
];
}
In practice, don't actually use the
struct sockaddr
type. Instead
cast
struct sockaddr_in
,
struct sockaddr_in6
and
struct
sockaddr_un
into it. These structs identify AF_INET, AF_INET6 and
AF_UNIX addresses families respectively.
Sometimes, it is necessary to work with an address, with unknown
address family. For such situations use
struct sockaddr_storage
. On
modern operating systems it's intended to to be large enough to fit
any socket address the system supports
1
.
struct
sockaddr_storage
{
sa_family_t
ss_family
;
// padding, usually 126 bytes
}
Let's talk about the nature of addresses of AF_INET, AF_INET6 and AF_UNIX families.
AF_INET Addresses
In AF_INET the address is encoded as
struct sockaddr_in
:
struct
sockaddr_in
{
sa_family_t
sin_family
;
/* address family: AF_INET */
in_port_t
sin_port
;
/* port in network byte order */
struct
in_addr
sin_addr
;
/* internet address */
};
struct
in_addr
{
uint32_t
s_addr
;
/* address in network byte order */
};
This structure contains, address family - AF_INET, 16 bit port number,
and a 32 bit IP address. Let's focus on the IP address part -
sin_addr
.
In string format, we typically work on IPv4 address in dot-decimal
notation, like "192.0.5.1". Let's start with an easy task - say a user
gave you an address and you want to convert it to
struct in_addr
.
Historically, a typical way to achieve this was to use
inet_aton
. These days it's discouraged - this function is not strict
enough, and accepts addresses in many obscure formats:
char
*
inet_aton
()
# integer
"1"
0.0
.
0.1
"16777217"
1.0
.
0.1
"0100000001"
1.0
.
0.1
octal
"0x1"
0.0
.
0.1
hexadecimal
# mixed dot-decimal
"1.65536"
1.1
.
0.0
octet
.
24
bits
"1.2.256"
1.2
.
1.0
octet
.
octet
.
16
bits
# dot-decimal
"1.2.3.4"
1.2
.
3.4
"1.2.3.071"
1.2
.
3.57
mixed
octal
"1.2.3.0x71"
1.2
.
3.113
mixed
hexadecimal
# trailing whitespace
"1.2.3.4 a"
1.2
.
3.4
"1.2.3.4
\r
a"
1.2
.
3.4
"1.2.3.4
\n
a"
1.2
.
3.4
"1.2.3.4
\t
a"
1.2
.
3.4
"1.2.3.4
\x0b
a"
1.2
.
3.4
"1.2.3.4
\x0b
a"
1.2
.
3.4
"1.2.3.4
\x0c
1"
1.2
.
3.4
# errors
"256.0.0.1"
-
1
overflow
"1.2.3.7
\x85
1"
-
1
non
-
whitespace
trailing
"1.2.3.7
\xa0
1"
-
1
non
-
whitespace
trailing
" 2.3.4.1"
-
1
leading
whitespace
Apart from accepting arcane formatting types, like numeric 32bit
decimal notation like "16777217" meaning "1.0.0.1", it happily parses
addresses with trailing whitespace followed by any gibberish.  A better
alternative is
inet_pton()
, which
only accepts a well known IPv4
dotted-decimal notation
for AF_INET family.
int
inet_pton
(
int
af
,
const
char
*
src
,
void
*
dst
);
With
inet_pton
only the well-formed dot-format addresses are
accepted. All the weird cases result in an error. This is usually the
desired behaviour.
char
*
inet_pton
(
AF_INET
)
"1.2.3.4"
1.2
.
3.4
"1.2.3"
-
1
"0x1"
-
1
"1.2.3.4
\t
a"
-
1
"1.2.3.071"
-
1
You can also use
getaddrinfo()
to convert IP address into
struct
sockaddr *
. It's much more advanced, we'll discuss it later.
Converting from
struct in_addr
to text form can be achieved for example with
inet_ntop
:
inet_ntop
(
int
af
,
const
void
*
src
,
char
*
dst
,
socklen_t
size
);
Where
dst
is a buffer of size INET_ADDRSTRLEN (16) for AF_INET and INET6_ADDRSTRLEN (46) for AF_INET6.
AF_INET6 Addresses
In AF_INET6 the address is encoded in "struct sockaddr_in6":
struct
sockaddr_in6
{
sa_family_t
sin6_family
;
/* AF_INET6 */
in_port_t
sin6_port
;
/* port number */
uint32_t
sin6_flowinfo
;
/* IPv6 flow information */
struct
in6_addr
sin6_addr
;
/* IPv6 address */
uint32_t
sin6_scope_id
;
/* Scope ID (new in 2.4) */
};
struct
in6_addr
{
unsigned
char
s6_addr
[
16
];
/* IPv6 address */
};
Conveniently
inet_pton
is also a correct way to parse IPv6 address
from text format into
struct in6_addr
. IPv6 address is composed of
16 bytes. Typically, the IPv6 address is represented in text as a
group of eight 4-digit (16 bits) hexadecimal numbers separated with a
colon ':'. There are a couple of caveats around parsing, take a look
at these examples:
char
*
inet_pton
(
AF_INET6
)
# eight 4-digit hex groups
'0:1:2:3:4:5:6:7'
0000
:
0001
:
0002
:
0003
:
0004
:
0005
:
0006
:
0007
# :: abbreviates zero groups
'::DEAD:BEEF'
0000
:
0000
:
0000
:
0000
:
0000
:
0000
:
dead
:
beef
'1080::8:800:200C:417A'
1080
:
0000
:
0000
:
0000
:
000
8
:
0800
:
200
c
:
417
a
'FF01::101'
ff01
:
0000
:
0000
:
0000
:
0000
:
0000
:
0000
:
0101
'::1'
0000
:
0000
:
0000
:
0000
:
0000
:
0000
:
0000
:
0001
'::'
0000
:
0000
:
0000
:
0000
:
0000
:
0000
:
0000
:
0000
'::1:20:0:0'
0000
:
0000
:
0000
:
0000
:
0001
:
0020
:
0000
:
0000
# leading zeros are fine (up to 4 characters), and not octal
'0::01:020:0000:0'
0000
:
0000
:
0000
:
0000
:
0001
:
0020
:
0000
:
0000
# IPv4-compatible IPv6 address, must be in correct dotted-decimal format
'0:0:0:0:0:0:1.2.3.4'
0000
:
0000
:
0000
:
0000
:
0000
:
0000
:
0102
:
0304
'::1.2.3.4'
0000
:
0000
:
0000
:
0000
:
0000
:
0000
:
0102
:
0304
# errors
'::FFFF:1.2'
-
1
# Shortcutting embedded IPv4 notation is not allowed
'::0xf'
-
1
# Explicit hexadecimal is not allowed
'::00001'
-
1
# Groups of more than 4 characters are not allowed
'0::1:2::'
-
1
# Multiple zero group are not allowed
There are a number of good practices regarding formatting IPv6
addresses. Most notably
::
should be used to shorten the longest
chain of :0000: blocks, and first one if two chains are equal
size. More recommendations are described in
RFC5952
.
inet_pton
only parses the
struct in6_addr
- IPv6 address part of
struct sockaddr_in6
. That structure has more two more relevant
fields:
sin6_flowinfo
and
sin6_scope_id
. For almost all users
these obscure fields should be kept at zero.
sin6_flowinfo
is going
to be ignored anyway unless you opt-in with a specific setsockopt.
sin6_scope_id
is ignored and taken into account only when target IP
belongs to one of a small number of link-specific IP ranges. We'll
discuss these fields later.
Reserved IP addresses
It's sometimes useful to filter traffic, and deny connections to
reserved IP addresses. For example, if you connect to user-specified
IP, then for security you might want to block target IP of
127.0.0.1. But of course that isn't enough, you need to think about
whole 127.0.0.0/8 subnet. How about ::1? How about ::ffff:127.0.0.1? Don't forget to also
consider 169.254.0.0/16 and fe80:: networks!
Special-purpose IPv4 addresses
Here is a list of prefixes which may come handy when creating
blacklists. The interesting prefixes are described in
RFC6890
,
IANA IPv4 Special-Purpose Address Registry
and
Wiki: Reserved IP addresses
.
IPv4 network
Description
Reference
0.0.0.0/8
"this" network
RFC1122
10.0.0.0/8
"private use"
RFC1918
100.64.0.0/10
"Shared Address Space" for CGNATs
RFC6598
127.0.0.0/8
"loopback"
RFC1122
169.254.0.0/16
"link local"
RFC3927
172.16.0.0/12
"private use"
RFC1918 aka APIPA
192.0.0.0/24
"IETF Protocol Assignments"
RFC6890
192.0.2.0/24
"documentation TEST-NET-1"
RFC5737
192.88.99.0/24
"6to4 Relay Anycast"
RFC3068
192.168.0.0/16
"private use"
RFC1918
198.18.0.0/15
"benchmarking"
RFC2544
198.51.100.0/24
"documentation TEST-NET-2"
RFC5737
203.0.113.0/24
"documentation TEST-NET-3"
RFC5737
224.0.0.0/4
"IPv4 multicast"
RFC5771
240.0.0.0/4
"reserved"
RFC1112
255.255.255.255/32
"limited broadcast"
RFC919
Special-purpose IPv6 addresses
The interesting prefixes are described in
RFC6890
,
IANA IPv6 Global Unicast Address Assignments
and
Wiki: Reserved IP addresses
.
IPv6 network
Description
Reference
::/128
"unspecified address"
RFC4291
::1/128
"loopback address"
RFC4291
::/96
"IPv4 Compatible"
RFC1933
::ffff:0:0/96
"IPv4-mapped Address"
RFC4291
::ffff:0:0:0/96
"IPv4-translated ipv6 address
RFC2765
64:ff9b::/96
"IPv4-IPv6 Translators"
RFC6052
100::/64
"Discard-Only Address Block"
RFC6666
2001::/23
"IETF Protocol Assignments"
RFC2928
2001::/32
"TEREDO"
RFC4380, RFC5991
2001:1::1/128
"Port Control Protocol Anycast"
RFC7723
2001:2::/48
"benchmarking"
RFC5180
2001:3::/32
"AMT"
RFC7450
2001:5::/32
"EID space for LISP"
RFC7954
2001:10::/28
"ORCHID"
RFC4843
2001:20::/28
"ORCHIDv2"
RFC7343
2001:db8::/32
"Documentation"
RFC3849
2002::/16
"6to4"
RFC3056
3ffe::/16
"6bone testing"
RFC3701
5f00::/8
"6bone historical"
RFC3701
fc00::/8
undefined
RFC4193
fd00::/8
"Unique local"
RFC4193
fe80::/10
"link-scoped unicast"
RFC4291
ff00::/8
"IPv6 multicast"
RFC2373
fec0::/10
"site-local"
RFC1884
Using DNS - getaddrinfo
The recommended way to resolve DNS names into IP addresses is
getaddrinfo()
libc function. This function requires some setup, so
for illustration I prepared a couple of scripts. Let's try
"getaddrinfo" on a valid domain "one.one.one.one":
$
./getaddrinfo.py one.one.one.one --type SOCK_STREAM
one.one.one.one  AF_INET   IPPROTO_TCP   1.0.0.1 
one.one.one.one  AF_INET   IPPROTO_TCP   1.1.1.1 
one.one.one.one  AF_INET6  IPPROTO_TCP   2606:4700:4700::1001 
one.one.one.one  AF_INET6  IPPROTO_TCP   2606:4700:4700::1111
The glibc version of
getaddrinfo()
uses a fairly complex
machinery. It uses glibc resolver module and
Name Service
Switch
to perform lookups.
/etc/host.conf
On my Ubuntu host glibc resolver first parses "/etc/host.conf". This file
is obsolete these days, and its "trim" and "reorder" settings affect
only "gethostbyname", "gethostbyname2" and "gethostbyaddr"
functions. The "multi" setting is only read by "ns_files".
Testing these parameters is hard, but can be achieved with
RESOLV_ADD_TRIM_DOMAINS, RESOLV_MULTI and RESOLV_REORDER environment
variables. For example, we can see how the "trim" parameter influences
results of "gethostbyaddr":
$
./gethostbyaddr.py 1.1.1.1
one.one.one.one
[]
[
'1.1.1.1'
]
$ RESOLV_ADD_TRIM_DOMAINS
=
.one ./gethostbyaddr.py 1.1.1.1
one.one.one
[]
[
'1.1.1.1'
]
/etc/resolv.conf
Following reading "/etc/host.conf", glibc pre-loads
"/etc/resolv.conf". This finishes the resolver module
bootstrapping. After this the Name Service Switch kicks in and reads
"/etc/nsswitch.conf".
"nsswitch.conf" on my Ubuntu Bionic contains the following "hosts" section:
bionic$ cat /etc/nsswitch.conf | grep -i hosts
hosts: files mdns4_minimal [NOTFOUND=return] dns myhostname
This reads as:
First, call "files" module which parses "/etc/hosts".
Then call "mdns4_minimal". It's  able to resolve .local domains.
Then try the "dns" module.
Finally, the query goes to "myhostname" module
The NSS is hard to debug - unlike resolver module it doesn't accept
environment variables that can override configuration. We can use a
trick though - we can
call "__nss_configure_lookup" function
,
before program starts. This can be achieved with LD_PRELOAD and this
simple library:
#include <nss.h>
#include <stdlib.h>
static
void
__attribute__
((
constructor
))
preload_nss
(
void
)
{
const
char
*
db
=
getenv
(
"NSS_DB"
);
const
char
*
config
=
getenv
(
"NSS_CONFIG"
);
if
(
db
&&
config
)
__nss_configure_lookup
(
db
,
config
);
}
As an example, let's debug the "myhostname" NSS module:
bionic
$
gcc -fPIC -shared -o libpreload_nss.so preload_nss.c
$ LD_PRELOAD
=
./libpreload_nss.so
\
NSS_DB
=
hosts
\
NSS_CONFIG
=
myhostname
\
./getaddrinfo.py bionic --type SOCK_STREAM
bionic AF_INET  IPPROTO_TCP 192.168.1.148
bionic AF_INET6 IPPROTO_TCP fe80::3c20:d6ec:9876:d951%eth0
In this example, we disabled dns, mdns and even lookups to
/etc/hosts. But still, with "myhostname" module
getaddrinfo()
was
able to resolve my host name "bionic" into assigned interfaces.
/etc/gai.conf
After successful domain resolution, the glibc the resolver module will
open "/etc/gai.conf". Configuration stored there is used to sort the
DNS responses.
RFC3484
describes the sorting requirements. With gai.conf configuration user
may tweak them. Ordering of results has interesting implications for
load balancing. In old days for load balancing web services could rely
on DNS. Returning multiple responses to A or AAAA queries in random
order was enough to guarantee load balancing on the servers. For
example let's see how
apple.com
randomizes the A response order:
$
dig apple.com A +short @dns.google
17.172.224.47
17.142.160.59
17.178.96.59
$
dig apple.com A +short @dns.google
17.142.160.59
17.172.224.47
17.178.96.59
Counter intuitively RFC3484 broke this - it strictly defines the order
in which
getaddrinfo()
results are supposed to be returned. The
glibc code changed over time. For a while around 2008 it was adhering
to RFC3484 and always pre-sorting the returned IP's. This in effect
disabled the DNS round-robin load balancing for many applications. See the
glibc bug report
and
an article by Daniel Stenberg
.
Modern glibc resolver module adheres to the order returned by the DNS
resolver. Most recursive DNS resolvers don't amend the order of the
response - it's usually preserved from the DNS authoritative
response. There are many interesting caveats, as mandated by RFC3484:
Within AAAA, IPv4-mapped-IPv6 takes precedence.
It's followed by addresses glibc believes are from local networks.
Followed by unsorted list of other IP's.
To see it in action you can use our
getaddrinfo
script:
$
./getaddrinfo.py dnslb.popcount.org --type SOCK_STREAM
dnslb.popcount.org  AF_INET     127.0.0.1
dnslb.popcount.org  AF_INET     192.168.1.1
dnslb.popcount.org  AF_INET     198.0.2.1
dnslb.popcount.org  AF_INET     198.0.2.2
dnslb.popcount.org  AF_INET6    ::ffff:192.0.2.1
dnslb.popcount.org  AF_INET6    ::1
dnslb.popcount.org  AF_INET6    fe80::1
dnslb.popcount.org  AF_INET6    2606::1
dnslb.popcount.org  AF_INET6    2606::2
Notice, the 127.0.0.1 and 192.168.1.1 (local subnet in my case) take
precedence. Similarly IPv4-mapped-IPv6 and ::1 are above other AAAA
results. Bear in mind that these intricacies are glibc and
installation-specific. Other libc libraries may have different
caveats. Most importantly some software doesn't use glibc for DNS
resolution. Golang,
browsers (with DoH)
and other software often re-implement DNS resolution functionality,
avoiding glibc. They are often ignoring parts of system configuration
like
/etc/resolv.conf
and
/etc/hosts
.
Without understanding of specific client DNS library it's impossible
to make any assumptions about ordering of IP addresses the client
software is receiving. In practice though, at least in the context of
web browsers, the DNS load balancing works well. As long as the
authoritative DNS server serves IP addresses in randomized order, the
servers load-balance well and receive similar number of requests.
Happy eyeballs
Even though the first IPv6 draft standard was published in 1998, the
protocol is still not fully adopted. In order to facilitate
deployments of dual-stack - IPv4 and IPv6 - systems, many techniques
have been proposed. The engineers try to prioritize IPv6 and give it
better chance on dual systems.
While getting IPv6 to work on servers is relatively straightforward
it's more complex at client side. End hosts may change networks over
time (mobility) and often need to use to networks with broken IPv6
routing.
To work around client problems, a technique called "Happy Eyeballs"
emerged and was ratified as
RFC8305
.  It's used by major
browsers. It is also built
in Apple iOS
operating system. The logic of Happy Eyeballs is roughly:
Launch two DNS queries, AAAA and A.
If A answers first, wait for AAAA answer or at most "Resolution Delay" of usually 50ms.
On AAAA answer, or after the timeout, order the returned addresses.
Ordering should interleave A and AAAA, giving preference to AAAA and hosts with know small RTT.
Begin establishing TCP connections.
Wait "Connection Attempt Delay" - usually between 10 and 250ms - before trying next address.
Don't abort connections in the process of being established - use concurrent connections.
When first connection is successfully established, abort all other connections.
The idea is to establish both IPv6 as well as IPv4 connections, giving
preference to IPv6 and servers closer to the user. By staggering the
connection attempts Happy Eyeballs avoids building network pressure.
Happy Eyeballs algorithm, while suffering
many problems in early implementations
,
had been proved to be successful
in reducing perceived latency for end-users and increasing IPv6 usage.
AF_UNIX Addresses
Thus far we discussed working with AF_INET and AF_INET6 addresses and
how the glibc machinery works for DNS resolution. It's time to discuss
AF_UNIX address family.
Unix sockets address is described by
struct sockaddr_un
:
struct
sockaddr_un
{
sa_family_t
sun_family
;
/* AF_UNIX */
char
sun_path
[
108
];
/* pathname */
};
Depending on the value of
sun_path
, there are three types of UNIX
socket addresses:
Bound to a pathname
Abstract
Unnamed
Bound to a pathname
The most common usage is to bind the UNIX socket to a path. Like:
int
sd
=
socket
(
AF_UNIX
,
SOCK_STREAM
,
0
);
struct
sockaddr_un
unix_addr
=
{
.
sun_family
=
AF_UNIX
,
.
sun_path
=
"/tmp/unix-socket"
,
};
int
r
=
bind
(
sd
,
(
struct
sockaddr
*
)
&
unix_addr
,
SOCKADDR_UN_SIZE
(
&
unix_addr
));
...
This will create a file on disk of special "socket" type. This is best
seen with
ls -F
:
$
ls -F /tmp/unix-socket
/tmp/unix-socket
=
You can confirm this with
stat(2)
syscall which will return
S_IFSOCK
file type. Note, you can't perform normal file operations
on this socket path. The semantics of UNIX sockets bound to pathname
are somewhat arcane. For example, you can't bind to already existing
path - the path must always be
created
by bind. A common practice is
to unconditionally call unlink before calling bind. This may be
dangerous, if untrusted user can influence the path. Consider
privileged daemon receiving "/etc/passwd" as a UNIX domain socket
path. It also creates a race condition when the path is not present
for some amount of time.
A better technique when starting up a server working with UNIX sockets bound to pathname is to:
Verify if the target file is of socket type with
fstatat()
system call.
Create new socket under new name.
Perform atomic
renameat()
operation.
You can inspect all the pathnames used by the system by looking into "/proc/net/unix":
$
cat /proc/net/unix | grep unix-socket
Num               RefCount Protocol Flags    Type St Inode     Path
0000000000000000: 00000002 00000000 00010000 0001 01 146375111 /tmp/unix-socket
Note, that the path reported by "/proc/net/unix" is not updated if the
file is moved, hard-linked or removed. This is just the string passed
at a time of
bind()
syscall, not representing actual disk path.
UNIX sockets bound to pathname have disk presence, and Linux will
verify the permissions. Connecting requires a write permission to the
disk file
2
. If you wish to override the default permission
mask, tune
umask
before calling
bind()
.
Each UNIX socket bound to a pathname has two inodes. First one,
reported by
/proc/net/unix
and tools like
ss
, is the internal
sockfs inode. Second one is the inode used by the socket file on the
disk, as reported by
ls -i
. To my knowledge there is no easy way of
knowing which socket inode the socket file refers to.
Note, that while usual path names are null-terminated, the
sun_path
is only 108 bytes long. Typical
PATH_MAX
is at least 256 bytes. It's
possible to have
sun_path
returned by
getsockname
/
getpeername
lacking the trailing '\x00'. Beware.
UNIX Sockets live in a namespace local to a machine.  If a user has
access to a path of pathname bound UNIX socket, like
"/tmp/unix-socket", then the connect() will succeed. There are a
couple of exceptions though - it won't run over network filesystems
like NFS. From a modern Linux point of view though - sharing a
directory with pathname bound UNIX sockets with Docker container, or
network-namespaced process is totally fine.
Abstract
Then there are Linux-specific abstract UNIX sockets. They aren't
backed by a socket file on disk. The first character of such socket's
sun_path
is '\x00'. It's then followed by any characters. It's
important to note that
sun_path
may contain arbitrary number of
'\x00' bytes, and the length of this field is
not
a part of
sockaddr_un
structure. For abstract sockets you must pass the
appropriate length to
bind
/
connect
syscalls in the
addrlen
parameter.  Basically, in abstract sockets,
sun_path
is not a C
string. For example, this code binds three sockets to two different
abstract names:
struct
sockaddr_un
s_un
=
{
AF_UNIX
}
int
s2
=
socket
(
AF_UNIX
,
SOCK_DGRAM
,
0
);
bind
(
s2
,
&
s_un
,
offsetof
(
struct
sockaddr_un
,
sun_path
)
+
1
);
int
s3
=
socket
(
AF_UNIX
,
SOCK_DGRAM
,
0
);
bind
(
s3
,
&
s_un
,
offsetof
(
struct
sockaddr_un
,
sun_path
)
+
2
);
The created sockets are named '\x00' and '\x00\x00' respectively:
$ cat /proc/net/unix
000000000000: 00000002 00000000 00000000 0002 01 146452179 @
000000000000: 00000002 00000000 00000000 0002 01 146452180 @@
You may have noticed the
SOCKADDR_UN_SIZE
macro used to figure out
the
addrlen
passed to
bind()
. Here's its definition:
#define SOCKADDR_UN_SIZE(sun) \
((sun)->sun_path[0] == '\x00' \
? __builtin_offsetof(struct sockaddr_un, sun_path) + 1 \
+ strnlen(&(sun)->sun_path[1], sizeof((sun)->sun_path)) \
: sizeof(struct sockaddr_un))
The idea is to look at the first byte in
sun_path
. If it's not
'\x00', then it's proper pathname, we can just return
sizeof(struct
sockaddr_un)
. Otherwise, it's an abstract path and we need to craft
proper length. We assume that no sane person would stick '\x00' into
the abstract path name, so we assume following initial zero byte, it
is zero-terminated. This is not strictly correct. As we saw, Linux is
totally capable of handling abstract names like '\x00\x00'. This trick
though, is practical and can simplify the code somewhat - no need to
pass around length explicitly. In fact, this very technique
is used in systemd
.
In order to avoid printing '\x00' character onto the terminal, many
Linux tools substitute the '\x00' characters with '@'. Doing this on
whole string is excessive, but handling first character in manageable
way is important. It's critical to clearly specify if socket is
abstract or bound to a path. If your tool accepts UNIX socket path as
a parameter, remember to allow for abstract names - substitute leading
'@' character with '\x00'.
Abstract sockets are tied to a network namespace. A process from one
netns won't be able to access abstract socket from another network
namespace, even when both run on the same machine.
When should you use UNIX sockets bound to pathnames and when abstract
names? Abstract names automatically disappear when server socket is
closed, but unlike pathname sockets, don't have permissions.
Furthermore, abstract sockets are a non portable Linux extension.
Autobind feature
The example we showed in previous section begs a question - what if we
call
bind()
with empty
sun_path
? In such case Linux will allocate
a 5-character sequential abstract name for us:
struct
sockaddr_un
s_un
=
{
AF_UNIX
};
int
s3
=
socket
(
AF_UNIX
,
SOCK_DGRAM
,
0
);
bind
(
s3
,
(
struct
sockaddr
*
)
&
s_un
,
__builtin_offsetof
(
struct
sockaddr_un
,
sun_path
)
);
int
len
=
sizeof
(
struct
sockaddr_un
);
getsockname
(
s3
,(
struct
sockaddr
*
)
&
s_un
,
&
len
);
if
(
len
>
0
&&
s_un
.
sun_path
[
0
]
==
'\x00'
)
{
s_un
.
sun_path
[
0
]
=
'@'
;
}
On my server this yields:
This behavior is called "autobind feature". Notice: there are only 2^20 unique autobind addresses.
Unnamed
Finally, UNIX sockets created with
sockpair()
syscall don't have
names assigned. The
getsockname
/
getpeername
will indicate
sun_path
is
of zero bytes.
Totally comment
this article on Twitter!
The following people gave valuable feedback on this article:
