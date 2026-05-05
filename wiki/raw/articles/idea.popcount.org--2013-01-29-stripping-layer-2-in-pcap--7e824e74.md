---
title: "Stripping layer 2 in pcap"
url: "https://idea.popcount.org/2013-01-29-stripping-layer-2-in-pcap"
fetched_at: 2026-05-05T07:01:13.333057+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Stripping layer 2 in pcap

Source: https://idea.popcount.org/2013-01-29-stripping-layer-2-in-pcap

Stripping layer 2 in pcap
29 January 2013
Say you want to sniff TCP/IP packets on your network. That's pretty
easy, right? Use
libpcap
, receive packets from the network interface
and we're done. But before you can extract the IP header from a
received packet you need to strip
layer 2
header.
It's not that easy.
Libpcap
tries to help only a bit - it is
possible to get the data link type of the network interface. But this
is useless without the knowledge of how to extract IP from given data
link type.
Most software use hardcoded offsets for the most common data link
types. Here's the relevant code in few popular programs:
Hardcoded offsets:
Data Link
p0f v3
nmap
hping
libnids
DLT_RAW
0
0
0
0
DLT_NULL
4
4
4
4
DLT_LOOP
8
4
4
-
DLT_PPP
4
4† or 8‡ else 24
4
4
DLT_PPP_BSDOS
-
4† or 8‡ else 24
24
-
DLT_PPP_SERIAL
8
4† or 8‡ else 24
4
4
DLT_PPP_ETHER
8
4† or 8‡ else 24
-
-
DLT_EN10MB
14
14
14
14 or 18 if VLAN
DLT_LINUX_SLL
16
16
16
16
DLT_PFLOG
28
-
-
-
DLT_IEEE802_11
32
-
14
24-32
DLT_IEEE802
-
22
14
22
DLT_MIAMI
-
16
-
-
DLT_SLIP
-
16† else 24
16
0
DLT_SLIP_BSDOS
-
16† else 24
16
-
DLT_FDDI
-
21
13
21
DLT_ENC
-
12
-
-
DLT_IPNET
-
24
-
-
DLT_ATM_RFC1483
-
-
8
-
DLT_CIP
-
-
8
-
DLT_ATM_CLIP
-
-
8
-
DLT_C_HDLC
-
-
4
-
DLT_LANE8023
-
-
16
-
Those programs are in agreement only about:
Data Link
offset
DLT_RAW
0
DLT_NULL
4
DLT_EN10MB
14
DLT_LINUX_SLL
16
Additionally it may be important to remove 802.1Q VLAN header from
DLT_EN10MB, for example
libnids
has the following code:
case
DLT_EN10MB
:
if
(
hdr
->
caplen
<
14
)
return
;
/* Only handle IP and 802.1Q VLAN tagged packets */
if
(
data
[
12
]
==
8
&&
data
[
13
]
==
0
)
{
/* Regular ethernet */
nids_linkoffset
=
14
;
}
else
if
(
data
[
12
]
==
0x81
&&
data
[
13
]
==
0
)
{
/* Skip 802.1Q VLAN and priority information */
nids_linkoffset
=
18
;
}
else
/* non-ip frame */
return
;
break
;
Furthermore, decoding of DLT_IEEE802_11 in
libnids
contains pretty
complex logic.
Opposite strategy is chosen by
p0f
- it tries to guess the offset of
IPv4 or IPv6 headers if the data link type is unrecognized.
Finally, here's the official tcpdump/libpcap documentation:
