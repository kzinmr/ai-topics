---
title: "BPF: the forgotten bytecode"
url: "https://idea.popcount.org/2014-05-21-bpf-the-forgotten-bytecode"
fetched_at: 2026-05-05T07:01:12.524216+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# BPF: the forgotten bytecode

Source: https://idea.popcount.org/2014-05-21-bpf-the-forgotten-bytecode

BPF: the forgotten bytecode
21 May 2014
This article was originally published on the CloudFlare blog:
Every once in a while I run into an obscure computer technology that
is a hidden gem, which over the years has become mostly
forgotten. This is exactly how I feel about the
tcpdump
tool and its
kernel counterpart the packet filter interface.
For example, say you run:
$
tcpdump -ni eth0 ip and udp and port 53
For most of us this command is pure magic, almost nobody understands
what happens behind the scenes. This is understandable, there is
little need to know how it works: the tool does its job very well,
it's descriptive and very fast.
In this article I'll try to explain how
tcpdump
works and how we use
its spinoffs to help fight the packet floods that hit us every day.
But first, we need a bit of history.
Historical context
Since workstations became interconnected, network administrators had a
need to "see" what is flowing on the wires. The ability to sniff the
network traffic is necessary when things go wrong, even for the most
basic debugging.
For this reason operating systems developed APIs for packet
sniffing. But, as there wasn't any real standard for it every OS had
to invent
a different API
:
Sun’s STREAMS NIT, DEC's Ultrix Packet Filter, SGI’s Snoop and Xerox
Alto had CMU/Stanford Packet Filter. This led to many
complications. The simpler APIs just copied all the packets to the
user space sniffer, which on a busy system resulted in a flood of
useless work. The more complex APIs were able to filter packets before
passing them to userspace, but it was often cumbersome and slow.
All this changed in 1993 when Steven McCanne and
Van Jacobson
published
the paper introducing a better way of filtering packets in the kernel,
they called it
"The BSD Packet Filter" (BPF)
.
Since then
the BPF
has
taken the world by a storm and along with
libpcap
and
tcpdump
become the de-facto standard in network debugging.
Here's
the story told by Steven himself
.
Tcpdump dissected
Tcpdump is composed of three logical parts:
Expression parser: Tcpdump first parses a readable filter
   expression like
ip and udp and port 53
. The result is a short program in
   a special minimal bytecode, the BPF bytecode.
The BPF bytecode (filter program) is attached to the network tap
   interface.
Finally, tcpdump pretty prints filtered packets received from the
   network tap. Pretty printing is far from a simple task, tcpdump
   needs to understand many network protocols to do it.
Expression parser
Given a packet filtering expression, tcpdump produces a short program
in the BPF bytecode. The easiest way to see the parser in action is to
pass a
-d
flag, which will produce a readable assembly-like program:
$ sudo tcpdump -p -ni eth0 -d "ip and udp"
(000) ldh      [12]
(001) jeq      #0x800           jt 2    jf 5
(002) ldb      [23]
(003) jeq      #0x11            jt 4    jf 5
(004) ret      #65535
(005) ret      #0
This program reads like this:
Load a half-word (2 bytes) from the packet at offset 12.
Check if the value is 0x0800, otherwise fail. This checks for the
   IP packet on top of
an Ethernet frame
.
Load byte from a packet at offset 23. That's the "protocol" field 9
   bytes within
an IP frame
.
Check if the value is 0x11, which is the UDP protocol number,
   otherwise fail.
Return success. Packet is matching the rule.
Here you can find
the full documentation of the assembly syntax
.
Less readable compiled bytecode is printed with
-ddd
option:
$ sudo tcpdump -p -ni eth0 -ddd "ip and udp"|tr "\n" ","
6,40 0 0 12,21 0 3 2048,48 0 0 23,21 0 1 17,6 0 0 65535,6 0 0 0,
Kernel API
Tcpdump can open a network tap by requesting a
SOCK_RAW
socket and
after a few magical
setsockopt
calls a filter can be set with
S_ATTACH_FILTER
option:
sock
=
socket
(
PF_PACKET
,
SOCK_RAW
,
htons
(
ETH_P_ALL
))
...
setsockopt
(
sock
,
SOL_SOCKET
,
SO_ATTACH_FILTER
,
...)
From now on the BPF filter will be run against all received packets on
a network interface and only packets matching that filter will be
passed to that network tap file descriptor.
All the gritty details are described in the
Documentation/networking/filter.txt
file. For the best performance one can use
a zero-copy
PACKET_MMAP
/
PACKET_RX_RING
interface
,
though most people should probably stick to the
high level
libpcap
API
.
The BPF bytecode
In essence Tcpdump asks the kernel to execute a BPF program within the
kernel context. This might sound risky, but actually isn't. Before
executing the BPF bytecode kernel ensures that it's safe:
All the jumps are only forward, which guarantees that there aren't
  any loops in the BPF program. Therefore it must terminate.
All instructions, especially memory reads are valid and within range.
The single BPF program has less than 4096 instructions.
All this guarantees that the BPF programs executed within kernel
context will run fast and will never infinitely loop. That means the
BPF programs are not Turing complete, but in practice they are
expressive enough for the job and deal with packet filtering very
well.
The original concepts underlying the BPF were described in a 1993 and
didn't require updates for many years. The Linux implementation on the
other hand is steadily evolving: recently a
new and shiny just-in-time BPF compiler
was introduced, and a few months ago an attempt was made to upgrade
the
BPF assembly to a 64-bit form
.
Not only tcpdump
BPF is an absolutely marvelous and flexible way of filtering
packets. For years it got reused in more places and now Linux uses BPF
filters for:
tcpdump-style packet filtering
"cls_bpf"
classifier for traffic shaping (QoS)
"seccomp-bpf"
syscalls filter to sandbox applications
"xt_bpf" iptables module
How we use it
CloudFlare deals with massive packet floods on a daily basis. It's
very important for us to be able to drop malicious traffic fast, long
before it hits the application.
Unfortunately matching before the application is not easy. Basic
iptables filtering, for example looking just at the source IP, doesn't
work as floods get more sophisticated. The iptables module closest to
our needs is
"xt_u32"
, but
it's hard to understand and somewhat limited. Though it's generally
pretty useful
,
and to make it easier people wrote
rule generators
.
But what works for us best is the "xt_bpf" iptables module by Willem
de Bruijn. With it we can match an iptable rule based on any BPF
expression.
Unfortunately, our BPF bytecode became pretty complex and it can't be
written as a usual tcpdump expression any more. Instead we rely on a
custom crafted BPF bytecode, for example, this is an "xt_bpf" bytecode
that matches a DNS query for
"example.com
":
ld
#20
ldx
4
*
([
0
]
&
0xf
)
add x
    tax

lb_0
:
;
Match
:
076578616
d706c6503636f6d00
'\x07example\x03com\x00'
ld
[
x
+
0
]
jneq
#0x07657861, lb_1
ld
[
x
+
4
]
jneq
#0x6d706c65, lb_1
ld
[
x
+
8
]
jneq
#0x03636f6d, lb_1
ldb
[
x
+
12
]
jneq
#0x00, lb_1
ret
#1
lb_1
:
ret
#0
To compile it we use the tools from the
tools/net
directory:
$
bpf_asm drop_example_com.bpf
14,0 0 0 20,177 0 0 0,12 0 0 0,7 0 0 0,64 0 0 0,21 0 7 124090465,64 0 0 4,21 0 5 1836084325,64 0 0 8,21 0 3 56848237,80 0 0 12,21 0 1 0,6 0 0 1,6 0 0 0
Finally you can apply the rule like so:
iptables -A INPUT \
    -p udp --dport 53 \
    -m bpf --bytecode "14,0 0 0 20,177 0 0 0,12 0 0 0,7 0 0 0,64 0 0 0,21 0 7 124090465,64 0 0 4,21 0 5 1836084325,64 0 0 8,21 0 3 56848237,80 0 0 12,21 0 1 0,6 0 0 1,6 0 0 0," \
    -j DROP
This is a fairly simple rule just looking for a particular bytes in
the packet. The same could be achieved using "u32" or "string"
modules. But "xt_bpf" gives us more flexibility. For example we can
make the rule case insensitive:
...
lb_0:
    ; Match: 076578616d706c6503636f6d00 '\x07example\x03com\x00'
    ld [x + 0]
    or #0x00202020
    jneq #0x07657861, lb_1
    ld [x + 4]
    or #0x20202020
    jneq #0x6d706c65, lb_1
    ld [x + 8]
    or #0x00202020
    jneq #0x03636f6d, lb_1
    ldb [x + 12]
    jneq #0x00, lb_1
    ret #1
...
Or match all the subdomains of
"example.com
":
...
lb_0:
    ; Match: *
    ldb [x + 0]
    add x
    add #1
    tax
    ; Match: 076578616d706c6503636f6d00 '\x07example\x03com\x00'
    ld [x + 0]
    jneq #0x07657861, lb_1
    ld [x + 4]
    jneq #0x6d706c65, lb_1
    ld [x + 8]
    jneq #0x03636f6d, lb_1
    ldb [x + 12]
    jneq #0x00, lb_1
    ret #1
...
These kind of rules are very useful, they allow us to pinpoint the
malicious traffic and drop it early. Just in the last couple of weeks
we dropped 870,213,889,941 packets with few BPF rules. Recently during
a flood we saw 41 billion packets dropped throughout a night due to a
single well placed rule.
Summary
Just as intended by Steven McCanne and Van Jacobson, the BPF is still
very useful and extremely fast. Even without enabling the BPF JIT we
don't see any performance hit of applying complex BPF rules.
I'm sure we'll use more BPF filters in the future to shield ourselves
from malicious traffic and to have more CPU to deal with legitimate
requests.
Does generating BPF assembly sound like fun?
We're hiring talented developers
,
including to our
elite office in London
.
