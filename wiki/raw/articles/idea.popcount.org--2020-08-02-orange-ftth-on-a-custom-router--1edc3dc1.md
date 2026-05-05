---
title: "Orange FTTH on a custom router"
url: "https://idea.popcount.org/2020-08-02-orange-ftth-on-a-custom-router"
fetched_at: 2026-05-05T07:01:05.942349+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Orange FTTH on a custom router

Source: https://idea.popcount.org/2020-08-02-orange-ftth-on-a-custom-router

Orange FTTH on a custom router
02 August 2020
Don't actually throw away FunBox. Not only it belongs to the carrier, but also you're not supposed to throw electrical equipment into mixed trash.
Here in Poland, Orange has a decent
FTTH
offer - less than
$16 for 300Mbit down, 50Mbit up. People reversed it over the years,
most impressively Pierre Kim in 2016:
Recently, it has been possible to replace the router the provider gives, called
"FunBox 3.0", with a custom one. There are couple of reasons for that:
My understanding it's impossible to get a stable IPv6 on FunBox 3.
FunBox is proprietary and evil.
For majority of Orane customers FunBox, made by Sagemcom, is more than
sufficient. It has all the standard bells and whistles, TV and VOIP
integration. Don't replace it unless you really need to.
But if you are a hobbyist like myself, and care about decent IPv6,
then maybe there is a case for replacing it. Most people seem to use
Mikrotik
[1]
, to replace FunBox but I decided to use a vanilla Debian
router.
First step is to call the call centre and ask for a technician to
install ONT. After repeating "I want ONT" enough, they eventually give
up and send a technitian.
When the technican comes in remember to ask for
PPPoE
password
. Generally this is impossible to extract from FunBox, but in
past there were reports this data can be retrieved from
rejestracja.orange.pl
. I don't know
if it works. I asked the technitian.
My FTB (Fiber Terminal Box) and Huawei HG8010Hv3 ONT (Optical Network Terminal)
Before we start verify you have:
the ONT box that terminates the fibre
FunBox, just in case
your ppp username, like
xxxxxxx@neostrada.pl
your ppp password, in my case 8 characters
Now we can do the real work.
IPv4 only
On my Debian 10 Buster I have two network interfaces.
eth1
which is
WAN connected to ONT, and
br0
which is lan.
My
/etc/network/interfaces
:
auto br0
iface br0 inet static
  bridge_ports ... # custom bridge config
  address 192.168.2.1
  netmask 255.255.255.0

auto eth1
iface eth1 inet manual
  mtu 1600

auto eth1.35
iface eth1.35 inet manual
  vlan-raw-device eth1
  mtu 1508

auto ppp0
iface ppp0 inet ppp
  pre-up /sbin/ip link set dev eth1.35 up
  provider neostrada
Notice, we configured vlan 35. Orange
sets following vlans
: 35 for internet, 839 for TV multicast, 838 for VOD unicast. I also noticed some noise on vlans 1314, 2014, 2114, but I'm confident this is a due to a bug or misconfiguration of my Huawei ONT.
Now, time for the ppp config. The configs are arcane, but this will
not deter us.
Best docs I found are here
. My
/etc/ppp/peers/neostrada
file:
plugin rp-pppoe.so eth1.35
user "xxxxxxx@neostrada.pl"
ifname ppp0
noauth
hide-password
persist
maxfail 0
holdoff 5
lcp-echo-interval 10
lcp-echo-failure 3
noaccomp
default-asyncmap
noipdefault
defaultroute
# usepeerdns
# debug
Followed by
/etc/ppp/chap-secrets
holding, well, secrets:
xxxxxxx@neostrada.pl * xxxxxxxx *
According to
internet forums
, the user name could be prepended with
no prefix: ports 25, 135, 137, 138, 139, 445 firewalled off
podstawowy-
: ports 135, 137, 138, 139, 445
bez_ochrony-
: no firewall done by provier
There is also
/ipv6
suffix, more on this later.
Next step is firewall. I prefer good old raw iptables in
/etc/rc.local
:
sysctl -w net.ipv4.ip_forward
=
1
iptables -t nat -A POSTROUTING -o ppp+ -j MASQUERADE
iptables -A FORWARD -i br0 -o ppp+ -j ACCEPT
iptables -A FORWARD -i ppp+ -o br0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -P FORWARD DROP
Remember to make
chmod +x /etc/rc.local
otherwise the file won't be loaded.
The last step is setting up local dhcp server for my lan.
dnsmasq
seems like the simplest chice
/etc/dnsmasq.d/lan
:
no-resolv
interface=br0
bind-interfaces
dhcp-option=3,0.0.0.0
dhcp-option=6,1.1.1.1
dhcp-range=192.168.2.2,192.168.2.255,48h
This is it. To bring the ppp session up and dwon you can use the
pon
and
poff
tools:
$
pon neostrada
$
poff neostrada
Useful for debugging but it's not using the debian network/interfaces
infrastructure. Better way:
$
ifup ppp0
$
ifdown ppp0
You can observe logs are in
/var/log/syslog
. If you enabled
debug
in
ppp/peers
config you can take a look at
/var/log/debug
.
Setting up ipv6 is more fun, but let's leave that for later.
IPv6 - two solutions
It turns out that if you open a PPPoE session with
/ipv6
suffix in
username, as suggested by docs, then the PPP session is, well, only
IPv6. There is no IPv4 address given, no IPv4 routing, etc. To get
IPv4 working the right way is to use v4-in-v6 tunneling to a local
Orange CGN (Carrier Grade Nat) router using
ds-lite
tunnel.
This creates couple of problems.
First, the CG Nat setup requires the router to ship packets, to the
CGN router. Packets that belong to your local network. In other words:
if your local printer has IP of 192.168.2.111 then the packet sent to
CGNAT will have source IP of 192.168.2.111. This basically extends the
local network to CGNAT router, which is not nice.
The alternative is to do double-NAT - one on your local router, one on
CGNAT layer, but this has the usual double-NAT issues.
My understanding is that in this setup it's impossible to get a public
IPv4 address. No chances for exposing public v4 ports! Another issue
is MTU. Tunneling v4 over v6 over PPPoE has obvious MTU implications,
and would require some further tuning to get to 1500 IPv4 frames.
A second option is to create two PPPoE sessions. One v4 without and
one v6 with the
/ipv6
suffix in
username.
Forum report from March 2019
indicates this setup works for 5 days, until some Orange automation
detects it and blocks the PPPoE sessions. This needs confirmation, but
getting public IPv4 address, avoiding CGNAT and avoiding double-NAT is
probably worth the extra trouble and potential instabilty.
Two PPPoE sessions
The second solution - two use PPPoE sessions, one for IPv6 and one for IPv4, is relatively easy to set up. First, you need to add a second ppp config. My
/etc/ppp/peers/neostradaipv6
file:
plugin rp-pppoe.so eth1.35
user "xxxxxxx@neostrada.pl/ipv6"
ifname ppp1
noauth
hide-password
persist
maxfail 0
holdoff 5
lcp-echo-interval 10
lcp-echo-failure 3
noaccomp
default-asyncmap
+ipv6
ipv6cp-accept-local
# debug
Changes to
/etc/network/interfaces
:
auto ppp1
iface ppp1 inet ppp
    pre-up /sbin/ip link set dev eth1 up
    provider neostradaipv6
Most importantly, we need to add a DHCPv6 client on that link. I used
wide-dhcpv6
. The
/etc/wide-dhcpv6/dhcp6c.conf
config:
profile default
{
  information-only;
  request domain-name-servers;
  request domain-name;
  script "/etc/wide-dhcpv6/dhcp6c-script";
};
interface ppp1 {
    send ia-pd 0;
    send rapid-commit;
};

id-assoc pd 0 {
    prefix-interface br0 {
        sla-len 0;
        sla-id 1;
        ifid 1;
    };
};
Then we need to tell the daemon to listen on our new
ppp1
interface, this is done in
/etc/default/wide-dhcpv6-client
:
Once the IPv6 prefix delegation is working, we need to give IPv6 to
our local clients on
br0
. Again, this is where
dnsmasq
comes
in. Adding these two lines to our
lan
config works:
enable-ra
dhcp-range = ::,constructor:br0,   ra-stateless, ra-names, 12h
The next step is to glue these things together. I think restarting
wide-dhcpv6
and
dnsmasq
is needed for them to pick up
ppp1
presence after the interface is brought up. I did this via ppp ip-up script
/etc/ppp/ipv6-up.d/enablev6
:
#!/bin/bash
sysctl -w net.ipv6.conf.
$PPP_IFACE
.accept_ra
=
2
systemctl restart wide-dhcpv6-client
systemctl restart dnsmasq
Remember to
chmod +x
it.
The last step is traffic forwarding. This time, since we are in V6
world. we don't need MASQUERADE / NAT, but we still want connection
tracking to allow only outbound connections to go through our router. New lines in
rc.local
:
sysctl -w net.ipv6.conf.all.forwarding=1
ip6tables -A FORWARD -i ppp+ -o br0 -m state --state RELATED,ESTABLISHED -j ACCEPT
ip6tables -A FORWARD -i br0 -o ppp+ -j ACCEPT
ip6tables -P FORWARD DROP
One PPPoE v6 session
The setup done by FunBox is to establish one IPv6 session, and achieve
IPv4 via ds-lite tunnel.
To be continued...
