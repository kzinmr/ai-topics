---
title: "Static Web Hosting on the Intel N150: FreeBSD, SmartOS, NetBSD, OpenBSD and Linux Compared"
url: "https://it-notes.dragas.net/2025/11/19/static-web-hosting-intel-n150-freebsd-smartos-netbsd-openbsd-linux/"
fetched_at: 2026-04-28T07:02:49.482249+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Static Web Hosting on the Intel N150: FreeBSD, SmartOS, NetBSD, OpenBSD and Linux Compared

Source: https://it-notes.dragas.net/2025/11/19/static-web-hosting-intel-n150-freebsd-smartos-netbsd-openbsd-linux/

Update
: This post has been updated to include
Docker
benchmarks and a comparison of container overhead versus FreeBSD Jails and illumos Zones.
Note
: Some operating systems (FreeBSD and Linux) support kernel TLS (kTLS) and the related SSL_sendfile path in nginx, which can improve HTTPS performance for static files. Since this feature is not available on all the systems included in the comparison (for example NetBSD, OpenBSD and illumos), the benchmarks were run with a common baseline configuration that does not rely on kTLS. The goal is to compare the systems under similar conditions rather than to measure OS specific optimizations.
I often get very specific infrastructure requests from clients. Most of the time it is some form of hosting. My job is usually to suggest and implement the setup that fits their goals, skills and long term plans.
If there are competent technicians on the other side, and they are willing to learn or already comfortable with Unix style systems, my first choices are usually one of the BSDs or an illumos distribution. If they need a control panel, or they already have a lot of experience with a particular stack that will clearly help them, I will happily use Linux and it usually delivers solid, reliable results.
Every now and then someone asks the question I like the least:
“But how does it
perform
compared to X or Y?”
I have never been a big fan of benchmarks. At best they capture a very specific workload on a very specific setup. They are almost never a perfect reflection of what will happen in the real world.
For example, I discovered that idle bhyve VMs seem to use fewer resources when the host is illumos than when the host is FreeBSD. It looks strange at first sight, but the illumos people are clearly working very hard on this, and the result is a very capable and efficient platform.
Despite my skepticism, from time to time I enjoy running some comparative tests. I already did it with
Proxmox KVM versus FreeBSD bhyve
, and I also
compared Jails, Zones, bhyve and KVM
on the same Intel N150 box. That led to the FreeBSD vs SmartOS article where I focused on CPU and memory performance on this small mini PC.
This time I wanted to do something simpler, but also closer to what I see every day:
static web hosting.
Instead of synthetic CPU or I/O tests, I wanted to measure how different operating systems behave when they serve a small static site with nginx, both over HTTP and HTTPS.
This is
not
meant to be a super rigorous benchmark. I used the default nginx packages, almost default configuration, and did not tune any OS specific kernel settings. In my experience, careful tuning of kernel and network parameters can easily move numbers by several tens of percentage points. The problem is that very few people actually spend time chasing such optimizations. Much more often, once a limit is reached, someone yells “we need mooooar powaaaar” while the real fix would be to tune the existing stack a bit.
So the question I want to answer here is more modest and more practical:
With default nginx and a small static site, how much does the choice of host OS really matter on this Intel N150 mini PC?
Spoiler
: less than people think, at least for plain HTTP. Things get more interesting once TLS enters the picture.
Disclaimer
These benchmarks are a snapshot of my specific hardware, network and configuration. They are useful to compare
relative
behavior on this setup. They are not a universal ranking of operating systems. Different CPUs, NICs, crypto extensions, kernel versions or nginx builds can completely change the picture.
Test setup
The hardware is the same Intel N150 mini PC I used in my previous tests: a small, low power box that still has enough cores to be interesting for lab and small production workloads.
On it, I installed several operating systems and environments, always on the bare metal, not nested inside each other. On each OS I installed nginx from the official packages.
Software under test
On the host:
SmartOS
, with:
- a Debian 12 LX zone
- an Alpine Linux 3.22 LX zone
- a native SmartOS zone
FreeBSD
14.3-RELEASE:
- nginx running inside a native jail
OpenBSD
7.8:
- nginx on the host
NetBSD
10.1:
- nginx on the host
Debian
13.2:
- nginx on the host
Alpine Linux
3.22:
- nginx on the host
- Docker: Debian 13 container running on the Alpine host (ports mapped)
I also tried to include
DragonFlyBSD
, but the NIC in this box is not supported. Using a different NIC just for one OS would have made the comparison meaningless, so I excluded it.
nginx configuration
In all environments:
nginx was installed from the system packages
worker_processes
was set to
auto
the web root contained the same static content
The important part is that I used
exactly the same
nginx.conf
file for all operating systems and all combinations in this article
. I copied the same configuration file verbatim to every host, jail and zone. The only changes were the IP address and file paths where needed, for example for the TLS certificate and key.
The static content was a default build of the example site generated by
BSSG
, my Bash static site generator
. The web root was the same logical structure on every OS and container type.
There is no OS specific tuning in the configuration and no kernel level tweaks. This is very close to a “package install plus minimal config” situation.
TLS configuration
For HTTPS I used a very simple configuration, identical on every host.
Self signed certificate created with:
openssl req -x509 -newkey rsa:4096 -nodes -keyout server.key -out server.crt -days 365 -subj "/CN=localhost"
Example nginx
server
block for HTTPS (simplified):
server {  
listen 443 ssl http2;  
listen [::]:443 ssl http2;  

server_name _;  

ssl_certificate /etc/nginx/ssl/server.crt;  
ssl_certificate_key /etc/nginx/ssl/server.key;  

root /var/www/html;  
index index.html index.htm;  

location / {  
try_files $uri $uri/ =404;  
}  
}
The HTTP virtual host is also the same everywhere, with the root pointing to the BSSG example site.
Load generator
The tests were run from my workstation on the same LAN:
client host: a mini PC machine connected at 2.5 Gbit/s
switch: 2.5 Gbit/s
test tool:
wrk
For each target host I ran:
wrk -t4 -c50 -d10s http://IP
wrk -t4 -c10 -d10s http://IP
wrk -t4 -c50 -d10s https://IP
wrk -t4 -c10 -d10s https://IP
Each scenario was executed multiple times to reduce noise; the numbers below are medians (or very close to them) from the runs.
The contenders
To keep things readable, I will refer to each setup as follows:
SmartOS Debian LX
→ SmartOS host, Debian 12 LX zone
SmartOS Alpine LX
→ SmartOS host, Alpine 3.22 LX zone
SmartOS Native
→ SmartOS host, native zone
FreeBSD Jail
→ FreeBSD 14.3-RELEASE, nginx in a jail
OpenBSD Host
→ OpenBSD 7.8, nginx on the host
NetBSD Host
→ NetBSD 10.1, nginx on the host
Debian Host
→ Debian 13.2, nginx on the host
Alpine Host
→ Alpine 3.22, nginx on the host
Docker Container
→ Alpine host, Debian 13 Docker container
Everything uses the same nginx configuration file and the same static site.
Static HTTP results
Let us start with plain HTTP, since this removes TLS from the picture and focuses on the kernel, network stack and nginx itself.
HTTP, 4 threads, 50 concurrent connections
Approximate median
wrk
results:
Environment
HTTP 50 connections
SmartOS Debian LX
~46.2 k
SmartOS Alpine LX
~49.2 k
SmartOS Native
~63.7 k
FreeBSD Jail
~63.9 k
OpenBSD Host
~64.1 k
NetBSD Host
~64.0 k
Debian Host
~63.8 k
Alpine Host
~63.9 k
Docker Container
~63.7 k
Two things stand out:
All the native or jail/container setups on the hosts that are not LX zones cluster around 63 to 64k requests per second.
The two SmartOS LX zones sit slightly lower, in the 46 to 49k range, which is still very respectable for this hardware.
In other words, as long as you are on the host or in something very close to it (FreeBSD jail, SmartOS native zone, NetBSD, OpenBSD, Linux on bare metal), static HTTP on nginx will happily max out around 64k requests per second with this small Intel N150 CPU.
The Debian and Alpine LX zones on SmartOS are a bit slower, but not dramatically so. They still deliver close to 50k requests per second and, in a real world scenario, you would probably saturate the network or the client long before hitting those numbers.
HTTP, 4 threads, 10 concurrent connections
With fewer concurrent connections, absolute throughput drops, but the relative picture is similar:
SmartOS Native around 44k
NetBSD and Alpine Host around 34 to 35k
FreeBSD, Debian, OpenBSD around 31 to 33k
The Docker Container sits slightly lower at ~30.2k req/s, showing a small overhead from the networking layer
The SmartOS LX zones sit slightly below, around 35 to 37k req/s
The important conclusion is simple:
For plain HTTP static hosting, once nginx is installed and correctly configured, the choice between these operating systems makes very little difference on this hardware. Zones and jails add negligible overhead, LX zones add a small one.
If you are only serving static content over HTTP, your choice of OS should be driven by other factors: ecosystem, tooling, update strategy, your own expertise and preference.
Static HTTPS results
TLS is where things start to diverge more clearly and where CPU utilization becomes interesting.
HTTPS, 4 threads, 50 concurrent connections
Approximate medians:
Environment
HTTPS 50 connections
CPU notes at 50 HTTPS connections
SmartOS Debian LX
~51.4 k
CPU saturated
SmartOS Alpine LX
~40.4 k
CPU saturated
SmartOS Native
~52.8 k
CPU saturated
FreeBSD Jail
~62.9 k
around 60% CPU idle
OpenBSD Host
~39.7 k
CPU saturated
NetBSD Host
~40.4 k
CPU saturated
Debian Host
~62.8 k
about 20% CPU idle
Alpine Host
~62.4 k
small idle headroom, around 7% idle
Docker Container
~62.7 k
CPU saturated
These numbers tell a more nuanced story.
FreeBSD, Debian and Alpine on bare metal form a “fast TLS” group.
All three sit around 62 to 63k requests per second with 50 concurrent HTTPS connections.
FreeBSD does this while using significantly less CPU.
During the HTTPS tests with 50 connections, the FreeBSD host still had around 60% CPU idle. It is the platform that handled TLS load most comfortably in terms of CPU headroom.
Debian and Alpine are close in throughput, but push the CPU harder.
Debian still had some idle time left, Alpine even less. In practice, all three are excellent here, but FreeBSD gives you more room before you hit the wall.
SmartOS, NetBSD and OpenBSD form a “good but heavier” TLS group.
Their HTTPS throughput is in the 40 to 52k req/s range and they reach full CPU usage at 50 concurrent connections. OpenBSD and NetBSD stabilize around 39 to 40k req/s. SmartOS native and the Debian LX zone manage slightly better (around 51 to 53k) but still with the CPU pegged.
HTTPS, 4 threads, 10 concurrent connections
With lower concurrency:
FreeBSD, Debian and Alpine still sit in roughly the 29 to 31k req/s range
SmartOS Native and LX zones are in the mid to high 30k range
The Docker Container drops slightly to ~27.8k req/s
NetBSD and OpenBSD sit around 26 to 27k req/s
The relative pattern is the same: for this TLS workload, FreeBSD and modern Linux distributions on bare metal appear to make better use of the cryptographic capabilities of the CPU, delivering higher throughput or more headroom or both.
What TLS seems to highlight
The HTTPS tests point to something that is not about nginx itself, but about the TLS stack and how well it can exploit the hardware.
On this Intel N150, my feeling is:
FreeBSD, with the userland and crypto stack I am running, is very efficient at TLS here. It delivers the highest throughput while keeping plenty of CPU in reserve.
Debian and Alpine, with their recent kernels and libraries, are also strong performers, close to FreeBSD in throughput, but with less idle CPU.
NetBSD, OpenBSD and SmartOS (native and LX) are still perfectly capable of serving a lot of HTTPS traffic, but they have to work harder to keep up and they hit 100% CPU much earlier.
This matches what I see in day to day operations: TLS performance is often less about “nginx vs something else” and more about the combination of:
the TLS library version and configuration
how well the OS uses the CPU crypto instructions
kernel level details in the network and crypto paths
I suspect the differences here are mostly due to how each system combines its TLS stack (OpenSSL, LibreSSL and friends), its kernel and its hardware acceleration support. It would take a deeper dive into profiling and configuration knobs to attribute the gaps precisely.
In any case, on this specific mini PC, if I had to pick a platform to handle a large amount of HTTPS static traffic, FreeBSD, Debian and Alpine would be my first candidates, in that order.
Zones, jails, containers and Docker: overhead in practice
Another interesting part of the story is the overhead introduced by different isolation technologies.
From these tests and the
previous virtualization article on the same N150 machine
, the picture is consistent:
FreeBSD jails behave almost like bare metal and are significantly more efficient than Docker.
For both HTTP and HTTPS, running nginx in a jail on FreeBSD 14.3-RELEASE produces numbers practically identical to native hosts.
The contrast with Docker is striking: while the Docker container required 100% CPU to reach peak for the HTTP and HTTPS throughput,
the FreeBSD jail delivered the same speed with ~60% of the CPU sitting idle
. In terms of performance cost per request, Jails are drastically cheaper.
SmartOS native zones are also very close to the metal.
Static HTTP performance reaches the same 64k req/s region and HTTPS is only slightly behind the "fast TLS" group, although with higher CPU usage.
SmartOS LX zones introduce a noticeable but modest overhead.
Both Debian and Alpine LX zones on SmartOS perform slightly worse than the native zone or FreeBSD jails. For static HTTP they are still very fast. For HTTPS the Debian LX zone remains competitive but costs more CPU, while the Alpine LX zone is slower.
Docker on Linux performs efficiently but eats the margins.
I ran an additional test using a Debian 13 Docker container running on the Alpine Linux host. At peak load (50 connections), the throughput was impressive and virtually identical to bare metal: ~63.7k req/s for HTTP and ~62.7k req/s for HTTPS. However, there is a clear cost. First, while the bare metal host maintained a small CPU buffer (~7% idle) during the HTTPS test, Docker
saturated the CPU to 100%
. Second, at lower concurrency (10 connections), the overhead became visible. The Docker container scored ~30.2k req/s for HTTP and ~27.8k req/s for HTTPS, slightly trailing the ~31-34k and ~29-31k range of the bare metal counterparts. The abstraction layers (NAT, bridging, namespaces) are extremely efficient, but they are not completely free.
This leads to a clear conclusion on efficiency:
FreeBSD Jails provide the highest throughput with the lowest CPU cost.
LX zones and Docker containers can match the speed (or come close), but they burn significantly more CPU cycles to do so.
What this means for real workloads
It is easy to get lost in tables and percentages, so let us go back to the initial question.
A client wants static hosting.
Does the choice between FreeBSD, SmartOS, NetBSD or Linux matter in terms of performance?
For
plain HTTP
on this hardware, with nginx and the same configuration:
Not really.
All the native hosts and FreeBSD jails deliver roughly the same maximum throughput, in the 63 to 64k req/s range. SmartOS LX zones are slightly slower but still strong.
For
HTTPS
:
Yes, it starts to matter a bit more.
FreeBSD stands out for how relaxed the CPU is under high TLS load.
Debian and Alpine are very close in throughput, with more CPU used but still with some headroom.
SmartOS, NetBSD and OpenBSD can still push a lot of HTTPS traffic, but they reach 100% CPU earlier and stabilize at lower request rates.
Does this mean you should always choose FreeBSD or Debian or Alpine for static HTTPS hosting?
Not necessarily.
In real deployments, the bottleneck is rarely the TLS performance of a single node serving a small static site. Network throughput, storage, logging, reverse proxies, CDNs and application layers all play a role.
However, knowing that FreeBSD and current Linux distributions can squeeze more out of a small CPU under TLS is useful when you are:
sizing hardware for small VPS nodes that must serve many HTTPS requests
planning to consolidate multiple services on a low power box
deciding whether you can afford to keep some CPU aside for other tasks (cache, background jobs, monitoring, and so on)
As always, the right answer depends on the complete picture: your skills, your tooling, your backups, your monitoring, the rest of your stack, and your tolerance for troubleshooting when things go sideways.
Final thoughts
From these small tests, my main takeaways are:
Static HTTP is basically solved on all these platforms.
On a modest Intel N150, every system tested can push around 64k static HTTP requests per second with nginx set to almost default settings. For many use cases, that is already more than enough.
TLS performance is where the OS and crypto stack start to matter.
FreeBSD, Debian and Alpine squeeze more HTTPS requests out of the N150, and FreeBSD in particular does it with a surprising amount of idle CPU left. NetBSD, OpenBSD and SmartOS need more CPU to reach similar speeds and stabilize at lower throughput once the CPU is saturated.
Jails and native zones are essentially free, LX zones cost a bit more.
FreeBSD jails and SmartOS native zones show very little overhead for this workload. SmartOS LX zones are still perfectly usable, but if you are chasing every last request per second you will see the cost of the translation layer.
Benchmarks are only part of the story.
If your team knows OpenBSD inside out and has tooling, scripts and workflows built around it, you might happily accept using more CPU on TLS in exchange for security features, simplicity and familiarity. The same goes for NetBSD or SmartOS in environments where their specific strengths shine.
I will not choose an operating system for a client just because a benchmark looks nicer. These numbers are one of the many inputs I consider. What matters most is always the combination of reliability, security, maintainability and the human beings who will have to operate the
system at three in the morning when something goes wrong.
Still, it is nice to know that if you put a tiny Intel N150 in front of a static site and you pick FreeBSD or a modern Linux distribution for HTTPS, you are giving that little CPU a fair chance to shine.
