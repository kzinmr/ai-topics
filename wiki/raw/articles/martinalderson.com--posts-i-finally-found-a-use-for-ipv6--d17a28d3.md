---
title: "I Finally Found a Use for IPv6"
url: "https://martinalderson.com/posts/i-finally-found-a-use-for-ipv6/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-29T07:02:04.301028+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# I Finally Found a Use for IPv6

Source: https://martinalderson.com/posts/i-finally-found-a-use-for-ipv6/?utm_source=rss&utm_medium=rss&utm_campaign=feed

IPv6 has been a bit of a conundrum to me. While we've clearly ran out of IPv4 addresses, the penetration of IPv6 on client networks has been incredibly slow, making it unfeasible apart from niche use cases to serve pure IPv6-only. And like it or loathe it CG-NAT has really taken quite a lot of urgency out of the migration - residential ISPs are using it en masse to put tens of thousands of customers behind one IPv4 address.
I haven't came across many places that treat IPv6 as a first class citizen in their web app infrastructure - if anything many places have it entirely firewalled as it's been a pain to configure and support.
However, I have
finally
found an interesting use for it, which I thought I'd share.
The Problem: Running many apps on one server
I've been a huge fan of running bare metal servers for workloads. For very little money you can get a seriously powerful machine that can run dozens of applications at once, serving a surprisingly large amount of traffic. Equally some of the cheaper VPS offerings now come with many CPU cores and 16GB+ of memory - more than enough to run 10+ simpler webapps.
This all works great until you need to access it from the internet and realise you might have (if you are lucky) 5 routable IP addresses - perhaps even only one.
At this point you have a few options. The classic way is to put a reverse proxy on the server, and start doing virtual host routing to various ports internally. While this works, I've never been a huge fan of it - the config gets a bit messy especially with TLS termination and it also means if your reverse proxy fails for whatever reason, all of your apps behind it go down. There are some good options with Docker sidecars, but it doesn't really resolve the single point of failure.
Or you could just get more IPv4 addresses, but they get expensive quickly and are sometimes hard to justify.
Using Cloudflare with IPv6
I'm aware that Cloudflare now becomes a huge single point of failure for this. However, most of these services I proxy through Cloudflare anyway, so it still reduces the risk of having a second level reverse proxy on the machine itself.
While diagnosing a weird LetsEncrypt failure, I realised I did have an entire IPv6 /64 (18.4 quintillion addresses!) routed to the server and it gave me a thought. Could Cloudflare just communicate with the server via IPv6 and have each service listen on an IPv6 address, and expose it to the world via IPv4?
The answer unsurprisingly is yes. All you need to do is add an AAAA (IPv6 version of an A) record to the DNS and it all just works. Cloudflare will handle the translation for users that don't support IPv6. Just make sure port 443 is open on IPv6 in ufw or iptables so traffic isn't firewalled in.
You can use the
::
syntax in IPv6 to mean "fill in with 0s". This makes it easy to do
2a01:4f9:c012:8cf2::1
,
2a01:4f9:c012:8cf2::2
, etc. The great thing about IPv6 is all of the subnet is routed automatically to you - you don't have to add each IPv6 address manually you want to use.
Ephemeral environments
You can take this one step further if you want by using the Cloudflare API as part of your CI/CD process if you are deploying ephemeral environments. Simply choose a random IPv6 address in your /64 (the chance of collision is incredibly low), tell your service to listen on that, and route it with the Cloudflare API.
Drawbacks (guess?)
The (major) drawback of all this is Docker's mediocre (at best) support for IPv6. If it's just for side projects that you're not too worried about security wise, you can just run:
docker run -d --network host yetanothersideproject --bind 2a01:4f9:c012:8cf2::2
and it will all work very smoothly. The downside of this is you don't have network isolation in Docker anymore, so be aware that you are losing quite a lot of the security isolation Docker provides.
The other option I've found is
macvlan
:
You need to create this network first (once only - not per Docker container). This effectively gives each Docker container a virtual NIC with its own MAC address.
docker network create -d macvlan --subnet=2a01:4f9:c012:8cf2::/64 --ipv6 -o parent=eth0 mynet
then run (and cross your fingers):
docker run -d --network mynet --ip6 2a01:4f9:c012:8cf2::2 yetanothersideproject
The problem here though is while it has proper isolation, the container itself won't have IPv4 support for
outgoing
connections. You may get away with this depending on what your server needs to access on the external internet, but I wouldn't recommend it if you want to retain your sanity.
You can get round this by using NAT and giving it an IPv4 address as well:
iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  --subnet=2a01:4f9:c012:8cf2::/64 \
  --ipv6 \
  -o parent=eth0 \
  mynet
It does look like things are slowly getting better, with this
IPv6 only API option
being another stepping stone towards it. Docker 28.0 added
EnableIPv4
as a network option, meaning you can create true IPv6-only networks (behind the
--experimental
flag for now).
Unfortunately I found Docker by far the biggest issue. I really hope they have an easier way to support this workflow. I do want to look at Podman in the future, which apparently has much better support for IPv6. Let me know if you have any thoughts on this!
