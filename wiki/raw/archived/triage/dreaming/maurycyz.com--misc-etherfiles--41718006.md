---
title: "Technical note: transfer files over an ethernet patch cable"
url: "https://maurycyz.com/misc/etherfiles/"
fetched_at: 2026-08-30T10:01:00.900267+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Technical note: transfer files over an ethernet patch cable

Source: https://maurycyz.com/misc/etherfiles/

Technical note: transfer files over an ethernet patch cable
2026-08-29
It's possible to just connect two computers together with Ethernet and do a bit of IP configuration:
# On
sender
...
ip address add
dev
eth0
fd42:dead:beef::1/48
ip link
set dev
eth0
up
# On
receiver
...
ip address add
dev
eth0
fd42:dead:beef::2/48
ip link
set dev
eth0
up
After a few seconds, pings should work:
# On
receiver
...
/ #
ping
fd42:dead:beef::1
64 bytes from fd42:dead:beef::1: icmp_seq=1 ttl=64 time=0.649 ms
64 bytes from fd42:dead:beef::1: icmp_seq=2 ttl=64 time=0.376 ms
64 bytes from fd42:dead:beef::1: icmp_seq=3 ttl=64 time=0.414 ms
64 bytes from fd42:dead:beef::1: icmp_seq=4 ttl=64 time=0.340 ms
... and so should this:
# On
receiver
...
socat
- TCP6-LISTEN:
1234
|
dd
status
=
progress
>
big_file.tar.gz
# On
sender
...
socat
- 'TCP6-CONNECT:
[fd42:dead:beef::2]
:
1234
'
<
big_file.tar.gz
These commands assume you are using Linux, but this trick works everywhere.
A nothing-special patch cable and ethernet jack should have no problem hitting ~900 Mbits/second, which is 6.7 GB per minute.
Fancy network cards will allow speeds orders of magnitude faster, but it's already much faster than USB flash or cloud storage.
Other options
... for transferring a file larger than 10 GB or so between two machines a few meters apart.
Cloud storage
: upload it to a server and download it from the other machine.
In most cases, this will be glacially slow, both because of slow internet connections and cloud providers throttling traffic.
Worse, the file has to be transferred over the network twice which doubles the time it takes.
Also, it can be expensive unless you already have a suitable server.
Direct TCP
over LAN is better, but WiFi is still quite slow and with random dropouts:
those multi-gigabit speed claims are dubious at best and certainly won't be reached in a typical home networking environment (walls, interference, long distances, etc)
However, if your house is wired for gigabit Ethernet, this can work great.
Removable storage
is quite slow unless you are willing to spend a lot of money.
Even if you do, it's often limited by the cable:
USB theoretically supports high speeds... with a (near mythical) perfect cable and pristine connectors.
I have only single cable and peripheral pair that actually reaches gigabit speeds, which has an MSRP of ~2300$.
(and that only works if plugged into the right USB port at the right angle)
Also, it has the same problem as cloud storage, having to copy data on and off the drive effectively halves the speed.
Unlike Ethernet, directly connecting two computers together won't work because USB is based around a host/device distinction.
Really
, Ethernet is the only common connection that can reliably reach gigabit speeds between two random devices using inexpensive cables.
It's also truly differential (with transformers!) which makes it resistant to RFI and ground level shifts.
I think it's underappreciated for non-internet applications and doesn't even need a local network:
point to point wiring is perfectly fine.
It also doesn't need a TCP/IP stack:
raw link-layer frames are perfectly fine even on a switched LAN.
This makes for a very simple way to move data to and from a microcontroller.
Related
:
