---
title: "Orange FTTH and IPv6 - part two"
url: "https://idea.popcount.org/2023-04-01-orange-ftth-and-ipv6---part-two"
fetched_at: 2026-05-05T07:01:05.825399+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Orange FTTH and IPv6 - part two

Source: https://idea.popcount.org/2023-04-01-orange-ftth-and-ipv6---part-two

Orange FTTH and IPv6 - part two
01 April 2023
Three years ago I published a guide on how to configure a custom Linux
router to work with Orange FTTH setup:
The most important part was getting IPv6 working, since it wasn't
possible with the "Funbox" router supplied by the carrier.
This seem to have been fixed. In past when using "Funbox", and when
setting the PPPoE username suffix to "/ipv6" to enable IPv6, the
suffix was automatically dropped every ~24h, and reverted to
IPv4-only. Today as far as I understand it's totally doable to have a
solid IPv6 session with generic "Funbox".
This is a good news, you can just keep on using the generic "Funbox"
if you want and enjoy both IPv4 and IPv6. There might still be some
niche reasons to use your own router, like what I am doing. Read on to
understand the details.
If you, like me, are still trying to avoid "Funbox", then you should
know that the solution I suggested - using to use the "two PPPoE
sessions" - stopped working. When second PPPoE session is started, the
first one drops. In pracice IPv4 stops working when IPv6 session gets
engaged.
However, classic "Funbox" router
is
able to sustain both IPv4 and
IPv6 connectivity. How does it do that?
It does differentl setup - it uses IPIP / Ds-Lite tunneling
over
IPv6 PPPoE session.
It took me a while but I was able to replicate this setup on my small
Debian router.
First, we need the PPPoE IPv6 session. This is pretty much the same as
in
my previous blog post
.
Single PPPoE v6 session
Verify if the ppp config for IPv6 is sensible
/etc/ppp/peers/neostradaipv6
. Probably half of the options are not
needed:
plugin
rp
-
pppoe
.
so
eth1
.35
user
"xxx@neostrada.pl/ipv6"
ifname
ppp1
noauth
hide
-
password
persist
maxfail
0
holdoff
5
lcp
-
echo
-
interval
10
lcp
-
echo
-
failure
3
noaccomp
default
-
asyncmap
mtu
1540
mru
1540
+
ipv6
debug
ipv6cp
-
accept
-
remote
ipcp
-
accept
-
remote
nodeflate
noccp
noproxyarp
My
/etc/network/interfaces
:
auto
ppp1
iface
ppp1
inet
ppp
post
-
up
for
i
in
`
seq
30
`
;
do
ip
l
show
ppp1
&&
break
;
sleep
1
;
done
provider
neostradaipv6
post
-
up
tc
qdisc
add
dev
ppp1
root
fq_codel
request_prefix
1
acceept_ra
2
post
-
up
sysctl
-
w
net
.
ipv6
.
conf
.
ppp1
.
accept_ra
=
2
post
-
up
sysctl
-
w
net
.
ipv6
.
conf
.
all
.
use_tempaddr
=
0
post
-
up
sysctl
-
w
net
.
ipv6
.
conf
.
default
.
use_tempaddr
=
0
post
-
up
/
etc
/
settunnel
.
sh
allow
-
ppp1
eth1
allow
-
ppp1
eth1
.35
Notice, at this point I disabled the IPv4 PPPoE session
ppp0
. Make
sure
ppp0
IPv4 session is not started.
(consult the old blog post for wide-dhcpv6-client config)
At this point you should have a stable IPv6 session. Getting IPv4
is harder and requires IPIP tunnel.
IPv4 IPIP tunnel
To get the IPIP DS-Lite tunnel working we first need... a tunnel! Here's the setup in nutshell:
ip
l
add
name
ipip6
type
ip6tnl
\
local
<
local
>
\
remote
<
aftr
-name
>
\
mode
ipip6
encaplimit
none
ip
l
set
ipip6
up
ip
r
add
0.0.0.0
/
0
dev
ipip6
ip
l
set
ipip6
mtu
1500
It was "fun" to get there - the
encaplimit none
option is basically
undocumented.
You could add these commands to startup and be done, however that
would require knowing the local IPv6 address and remote tunnel
AFTR-NAME.
While local IPv6 can be scraped easily with some
ip -6 route get
incantation, it's not so easy with the AFTR-NAME.
It turns out this thing is shared between the provider with the router
using DHCPv6 options.  This is how it looks on the wire:
IP6
(
flowlabel
0xb70d8
,
hlim
1
,
next
-
header
UDP
(
17
)
payload
length
:
154
)
fe80
::
xx
.546
>
ff02
::
1
:
2.547
:
[
udp
sum
ok
]
dhcp6
rebind
(
xid
=
6273
b8
(
client
-
ID
hwaddr
/
time
type
1
time
715299037
000000002
ebc
)
(
elapsed
-
time
0
)
(
vendor
-
class
)
(
IA_PD
IAID
:
1
T1
:
0
T2
:
0
(
IA_PD
-
prefix
2
a01
:::
1
::/
56
pltime
:
86400
vltime
:
86400
))
(
reconfigure
-
accept
)
(
option
-
request
AFTR
-
Name
opt_82
opt_83
))
IP6
(
class
0xc0
,
hlim
64
,
next
-
header
UDP
(
17
)
payload
length
:
130
)
fe80
::
xx
.547
>
fe80
::
xx
.546
:
[
udp
sum
ok
]
dhcp6
reply
(
xid
=
6273
b8
(
client
-
ID
hwaddr
/
time
type
1
time
715299037
000000002
ebc
)
(
server
-
ID
vid
000005
8338303
a61
)
(
IA_PD
IAID
:
1
T1
:
43200
T2
:
69120
(
IA_PD
-
prefix
2
a01
:::
1
::/
56
pltime
:
86400
vltime
:
86400
))
(
AFTR
-
Name
war01f
.
cgn
.
tpnet
.
pl
))
Notice: the response has "AFTR-Name war01f.cgn.tpnet.pl" indicating
what is the DS-Lite IPv4-in-IPv6 tunnel endpoint.
We might do it the right way - make our DHCPv6 client to query the
Orange server with appropriate request and receive not only IPv6
address, lease but also the AFTR-NAME. This is insanely complicated
though.
wide-dhcpv6-client doesn't support this option, and doesn't support
   non-standard dhcp request options.
isc-dhcp-client had million options, was super complicated to set up and now is discontinued.
dhcpcd and Dibbler also didn't get my love for some reasons.
Basically there is no dhcpv6 client implementation that could do this.
What is the solution then? Keep the ususal wide-dhcpv6-client, which
is simple and works, allow it to just run, and later, after IPv6 is
working just forge/spoof another DHCPv6 request. To do this it's
needed to query appropriate DHCPv6 optcode=64 option. Put this script
in the script
/root/dhcp6.py
:
import
socket
from
scapy.layers
import
inet6
from
scapy.layers.inet
import
UDP
from
scapy.layers.dhcp6
import
*
from
scapy.config
import
conf
import
scapy.volatile
from
scapy.sendrecv
import
sniff
import
signal
import
sys
iface
=
sys
.
argv
[
1
]
if
len
(
sys
.
argv
)
>
1
else
'ppp1'
srcip
=
conf
.
route6
.
route
(
"ff02::1:2"
,
dev
=
iface
)[
1
]
m
=
DHCP6_Solicit
(
trid
=
scapy
.
volatile
.
RandInt
())
/
DHCP6OptClientId
(
duid
=
b
'00'
)
/
DHCP6OptOptReq
()
/
DHCP6OptElapsedTime
()
/
DHCP6OptIA_NA
()
p
=
inet6
.
IPv6
(
src
=
srcip
,
dst
=
'ff02::1:2'
)
/
UDP
(
sport
=
546
,
dport
=
547
)
/
m
s
=
socket
.
socket
(
socket
.
AF_PACKET
,
socket
.
SOCK_DGRAM
,
0xdd86
)
s
.
bind
((
iface
,
0
))
s
.
send
(
p
.
build
())
signal
.
alarm
(
5
)
while
True
:
p
=
s
.
recv
(
4096
)
p
=
IPv6
(
p
)
if
UDP
not
in
p
:
continue
if
p
[
UDP
]
.
sport
==
547
and
p
[
UDP
]
.
dport
==
546
:
break
aftr
=
p
[
DHCP6OptUnknown
]
if
aftr
.
optcode
==
64
:
s
=
[]
d
=
aftr
.
data
while
d
:
l
,
=
struct
.
unpack_from
(
'B'
,
d
)
s
.
append
(
d
[
1
:
l
+
1
])
d
=
d
[
l
+
1
:]
dns
=
b
'.'
.
join
((
s
[:
-
1
]))
dns_two
=
s
[
0
]
+
b
'.1540.'
+
b
'.'
.
join
((
s
[
1
:
-
1
]))
print
(
dns
.
decode
())
print
(
dns_two
.
decode
())
Of course you need either:
apt
install
python3
-
scapy
apt
install
python
-
scapy
This is what I get:
# python3 /root/dhcp6.py
war01f
.
cgn
.
tpnet
.
pl
war01f
.1540
.
cgn
.
tpnet
.
pl
Don't ask me why adding the
1540
part into the url is needed. But it
is.
Ok, we have all the pieces. Here's the plan:
Set up iptables/masquerade to prevent leaking our IPv4 network to
   the IPv4 CGNAT AFTR gateway. This can be done in
/etc/rc.local
On IPv6 interface setup, setup the IPv4 tunnel (it's going over IPv6 remember).
The firewall addition to
/etc/rc.local
:
IFIP4
=
ipip6
iptables -t nat -A POSTROUTING -o
$IFIP4
-j MASQUERADE
iptables -A FORWARD -i br0 -o
$IFIP4
-j ACCEPT
iptables -A FORWARD -i
$IFIP4
-o br0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -P FORWARD DROP
To create the tunnel add a script like
/etc/settunnel.sh
:
#!/bin/bash
[
"$IFACE"
=
"ppp1"
]
||
exit
0
[
"$ADDRFAM"
=
"inet"
]
||
exit
0

func
()
{
sleep 5
    ip l del ipip6
SRCIP
=
`
ip -6 -o route get 2606:4700:4700::1111 | sed -n
's/.*src \([0-9.:a-fA-F]\+\).*/\1/p'
`
DSTDNS
=
`
python3 /root/dhcp6.py ppp1 |tail -n1
`
DSTIP
=
`
dig +short AAAA
$DSTDNS
`
echo
"ip l add name ipip6 type ip6tnl local $SRCIP remote $DSTIP mode ipip6 encaplimit none"
ip l add name ipip6
type
ip6tnl
local
$SRCIP
remote
$DSTIP
mode ipip6 encaplimit none

    ip l
set
ipip6 mtu 1500
    ip l
set
ipip6 up
    ip r add 0.0.0.0/0 dev ipip6
}
func &
Notice, it runs in the background after IPv6 setup. I found it most
stable like that.
You also need to make sure this script is run from
/etc/network/interfaces
, like:
...
iface
ppp1
inet
ppp
...
post
-
up
/
etc
/
settunnel
.
sh
That's it.
Fixing MTU
Oh, one more thing, the MTU. On my WAN interface, the MTU contains as
follows for IPv6 traffic:
Which means that to get 1500 IPv6 MTU, we need to have:
eth1 MTU 1512
eth1.35 MTU 1508
ppp1 MTU 1500
For IPv4 however we're doing:
VLAN
/
PPPoE
/
IPv6
/
IPv4
This requires bigger MTU:
eth1 MTU 1552
eth1.35 MTU 1548
ppp1 MTU 1540
ipip6 MTU 1500
Fine, so the ppp1 device must establish at least 1540 MTU. There is a
problem though. Normal ppp daemons has hardcoded max MTU at 1508. To
bump it we need to recompile the pppd. Good luck!
apt
-
get
install
debuild
devscripts
apt
-
get
build
-
dep
ppp
apt
-
get
source
ppp
Change this
ppp-2.4.7/pppd/plugins/rp-pppoe/pppoe.h
/* There are other fixed-size buffers preventing
this from being increased to 16110. The buffer
sizes would need to be properly de-coupled from
the default MRU. For now, getting up to 1500 is
enough. */
#define ETH_JUMBO_LEN 1508
to this
#define ETH_JUMBO_LEN 1600
then
cd
ppp
-
2.4.7
/
debuild
-
b
-
uc
-
us
and you should have your patched ppp package!
Miscellaneous
There exists
poff
command to end ppp sessions
