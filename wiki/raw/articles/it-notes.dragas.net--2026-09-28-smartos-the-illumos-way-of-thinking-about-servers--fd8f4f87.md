---
title: "SmartOS: The illumos Way of Thinking About Servers"
url: "https://it-notes.dragas.net/2026/09/28/smartos-the-illumos-way-of-thinking-about-servers/"
fetched_at: 2026-09-28T10:02:14.977118+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# SmartOS: The illumos Way of Thinking About Servers

Source: https://it-notes.dragas.net/2026/09/28/smartos-the-illumos-way-of-thinking-about-servers/

As I often say, I like simplicity and predictability. My servers are generally built around that principle: the server itself (physical or virtual) is just a coordinator of containers. When it's based on FreeBSD, those containers take the form of jails and VMs. In case of disaster, restoring is simple, and
I talked about it at EuroBSDCon 2026 in Brussels
.
But there's another operating system that I appreciate and have been using for quite some time, and it's perfect for this purpose:
illumos
.
Born as a fork of OpenSolaris, it incorporates everything the brilliant minds at Sun designed and built. Many of those minds still work on illumos (and its distributions) today, making it a modern and extremely mature operating system.
ZFS was born at Sun, and illumos is the proof: it's not just its file system, everything is designed around it, with a level of integration that goes beyond even FreeBSD's. There are also technologies like Crossbow (network virtualization), DTrace, very advanced resource controls and, above all, something very dear to me: zones. Inspired by FreeBSD jails, zones strictly separate all the components and create secure and isolated compartments. There's also good support for LX (Linux) zones, so it can run software compiled for Linux inside them. I'll come back to this in detail later. On top of that, it supports virtualization with both bhyve and KVM, giving the (practically unique, in the open source world) possibility of using both the efficiency of bhyve and the broad compatibility of KVM. SMF, five years older than systemd, is extremely powerful, even if not particularly intuitive for those who don't know it.
As you can guess, there are many similarities between illumos and the BSDs, and it's no coincidence: the licenses and the minds are compatible, and so is the philosophy, and there's a lot of exchange of ideas, code and solutions. bhyve, born on FreeBSD, performs excellently on illumos and, in some areas, has even surpassed the FreeBSD implementation. Tests I ran myself about a year ago showed that a nearly idle VM still used some (little) host CPU on FreeBSD, while it used zero (ZERO!) on illumos.
illumos has several distributions. Among them there's
OpenIndiana
, general purpose and comparable to Linux distributions, and
Tribblix
, which "blends a retro style with modern components", developed and maintained by
Peter Tribble
with constancy and regularity. Then there's
OmniOS
, a traditional server distribution, and
SmartOS
, the one I use the most and the one this post is mainly about.
SmartOS, in fact, was born for servers. Its concept is simple and powerful: the hardware (or the VM) is a pure "hypervisor" of zones or VMs. VMs themselves run inside dedicated zones, one per VM, so even in case of a VM escape, you still end up inside a zone, so there's another layer. This "onion" approach increases security. LX zones are considered very important in SmartOS, so they get the best possible support. Today it's possible to run complete Debian zones because, unlike FreeBSD jails (but this is changing), they can run systemd too. I've given clients entire Debian systems in LX zones and they never noticed the difference. Also, unlike jails, a zone only sees the resources assigned to it: while a FreeBSD jail will still see all the host's RAM (and gets blocked when it exceeds the assigned RAM), illumos zones (native or LX) will only see the assigned resources as their limit. An Alpine LX zone on illumos with 512 MB of RAM assigned will show, with the
free
command, only 512 MB total.
SmartOS is also designed as a live, mostly read-only operating system. It's normally booted from external media, although it can also boot directly from the ZFS pool. Upgrading is simply... booting a new platform image. On first boot, it will ask to create a ZFS pool to store configurations, logs and zones, but the whole OS is immutable. This increases both security and reliability. It can also be installed but, in practice, the approach doesn't change: a ZFS dataset will be created on the local pool and used to boot and to read the OS files. For a traditional installation, other distributions are a better fit.
In this post I'll show a basic SmartOS installation (on a physical host or a VM) and the creation of a couple of services. The goal is to show some of its peculiarities and hopefully spark some curiosity about this fantastic OS (and about our
illumos.cafe
).
The first thing to do is download the SmartOS ISO (or USB image, depending on how you'll boot it). On average there's a release every two weeks, with its changelog (only if there's something to release - nobody here ships updates just to shout that there's been an update). So go to
https://docs.smartos.org/download-smartos/
and:
Download the ISO if you're booting from a CD-ROM (physical or virtual)
Download the USB image if you're booting from it or from a USB stick. This USB image only contains the read-only OS, so you'll need another disk for the ZFS pool.
Once booted, the first question will be the IP address of the "admin" interface. SmartOS normally expects to live in a datacenter, with one interface dedicated to administration and another one to workloads. In this example we'll use the same one, assuming we're on a LAN. It will then ask for the DNS servers and the NTP server, and complete the network setup. Next it will propose a disk for the ZFS pool - careful, make sure it's the right disk, because it will wipe everything. At that point it will ask whether you want to boot from a pool (like that one) or keep booting from the device you just booted from. When possible, I keep booting from a separate device. When my SmartOS runs in a bhyve VM on FreeBSD, I have a config like this:
loader="uefi"
cpu="8"
memory="16G"
network0_type="virtio-net"
network0_switch="public"
disk0_type="nvme"
disk0_name="smartos.img"
disk1_type="nvme"
disk1_name="disk0.img"
[...]
That is, one disk for SmartOS (the downloaded "USB image") and one for the zones pool. Upgrading SmartOS means downloading a new image from the website, replacing
smartos.img
and rebooting the VM. Profit.
Next it will ask whether we want to install pkgsrc, NetBSD's package manager which, yes, is native here too. It's not strictly needed on the hypervisor itself, but I usually install it anyway. Then it will ask for the root password and the system hostname. Yes, the root password: no sudo, etc. The idea is that, in theory, root should only log in from the dedicated interface and only to manage the hypervisor. Because, remember, workloads aren't supposed to run on the "base" SmartOS, but inside zones.
The installation will be very fast because it's basically the creation of a ZFS pool, some swap space, a few small configuration files and, if requested, pkgsrc. You can then reboot and the system will start.
SmartOS doesn't boot fast. It's a server OS, it's not expected to reboot often, but it performs all the necessary checks.
illumos isn't merely Unix-like. It is Unix by lineage, derived directly from Unix, although it isn't UNIX-certified. And some commands aren't even remotely comparable to the Linux or BSD ones. That's one of the reasons why, in the late '90s and early 2000s, I looked sideways at the Sun SPARCstations at university: I didn't know the commands and considered them "weird". It took me years to understand their power.
There's no
top
, there's
prstat
.
prstat -Z 1
, for example, will also show the per-zone load, very useful to understand what's going on.
SmartOS provides native tools to list, download and install ready-made disk images (for zones or VMs), and to create, start and access the console of zones and VMs - and the commands are the same for both. So whether it's a zone or a VM, there isn't much difference. There's also a web UI, which can help (at least partially) with creating and managing zones and VMs, easy to install following the instructions on its page:
https://docs.smartos.org/web-interface/
The goal of SmartOS is to provide, in the "global zone" (the hypervisor itself), only the tools to manage the host and to create more zones. Everything should go into zones. Even a simple DHCP server. A concrete example, which gives an idea of how everything is supposed to work, is this one:
https://docs.smartos.org/nat-using-etherstubs/
With
imgadm avail
, for example, you can see all the disk images available on the servers. They're divided into
zone-dataset
(native illumos zones),
lx-dataset
(LX, that is Linux, zones) and
zvol
(actual VMs). For example, I want to see all the ready-made Alpine Linux images:
[root@sos01 ~]# imgadm avail|grep alpine
f48e3bf4-6d02-11e5-9a1f-53a8ab833767  alpine-3                        20151007      linux    lx-dataset    2015-10-07
96bb1fac-c87d-11e5-b5bf-ff4703459205  alpine-3                        20160201      linux    lx-dataset    2016-02-01
712f1436-0311-11e6-b4d4-139262136691  alpine-3                        20160415      linux    lx-dataset    2016-04-15
d8830f1e-3680-11e6-be72-2ba188e02d31  alpine-3                        20160620      linux    lx-dataset    2016-06-20
77bc3f50-8f4c-11e6-90b6-f7b69b9dcf20  alpine-3                        20161011      linux    lx-dataset    2016-10-11
e7b557c2-b2a8-11e6-b2c1-7f681aa61371  alpine-3                        20161125      linux    lx-dataset    2016-11-25
0c8b0b40-c0ce-11e6-81ce-f74ad6815a5d  alpine-3                        20161213      linux    lx-dataset    2016-12-13
4d3ed29a-c851-11e6-b5a9-639aada4a9c8  alpine-3                        20161222      linux    lx-dataset    2016-12-22
212c8962-ec06-11e6-8cee-5b0a09ebef00  alpine-3                        20170206      linux    lx-dataset    2017-02-06
19aa3328-0025-11e7-a19a-c39077bfd4cf  alpine-3                        20170303      linux    lx-dataset    2017-03-03
b5d89e30-128d-4ea4-824f-8e36fd7e3703  alpine-3                        20230721      linux    lx-dataset    2023-07-21
029a1752-71c8-4d30-a2aa-dcdc4ee32008  alpine-3                        20231121      linux    lx-dataset    2023-11-21
632a25ad-15dc-42f0-a23b-743b37f62cbb  alpine-3                        20240726      linux    lx-dataset    2024-07-26
0b7d45d9-be8c-439f-9a24-bd6223199c2b  alpine-3                        20250120      linux    lx-dataset    2025-01-20
c38b1b62-6d89-41f1-bd1d-5342b2d783d7  alpine-3.21.3                   20250407      linux    lx-dataset    2025-04-07
2ab26a8c-616b-4b2f-9a30-b121c044c278  alpine-3.23-nocloud             20260311      linux    zvol          2026-03-26
95766d4b-a225-4755-b630-1eae6b34b447  alpine-3.23-nocloud             20260501      linux    zvol          2026-05-01
The latest Alpine Linux LX image available is 3.21 - it's possible to create custom ones, but that's outside the scope of this guide.
First, let's use
imgadm
to import the image we need, using its UUID:
imgadm import c38b1b62-6d89-41f1-bd1d-5342b2d783d7
In a short time, the image will be installed and will populate its dataset.
I usually keep configurations in a dedicated dataset. It's not necessary, but it's useful to find them later, remember what I did and, if needed, create similar zones.
I won't cover IPv6 in this example, since its setup depends heavily on the host, the network topology, and the addressing model provided by the upstream network.
To keep things simple and reproducible, I'll stick to a basic IPv4 setup with the zone behind the existing NAT on the LAN. IPv6 can certainly be added, but it deserves to be treated separately rather than squeezed into an example whose purpose is simply to show the fundamentals.
zfs create zones/jsons
cd /zones/jsons
In that directory, create a file called
lx_alpine.json
:
{
  "brand": "lx",
  "resolvers": [
    "8.8.8.8",
    "8.8.4.4"
  ],
  "kernel_version": "5.10.0",
  "ram": 1024,
  "alias": "alpine01",
  "customer_metadata": {
  },
  "nics": [
    {
      "nic_tag": "admin",
      "ips": [
        "192.168.1.2/24"
      ],
      "gateway": "192.168.1.1"
    }
  ],
  "image_uuid": "c38b1b62-6d89-41f1-bd1d-5342b2d783d7",
  "quota": 10
}
Network settings will obviously vary, but here I've basically created an Alpine Linux LX zone with 1 GB of RAM assigned and a 10 GB disk quota. The
image_uuid
matches the one we downloaded with
imgadm
- just run
imgadm list
to see all the images on the system.
The command to create the zone is:
vmadm create -f lx_alpine.json
The system will create an LX zone based on the downloaded Alpine 3.21 image.
To access the zone, once it's ready (check with
vmadm list
), use the
zlogin
command. Careful:
zlogin
doesn't want the alias but the zone name, which is a UUID. But it supports tab completion, so just type
zlogin alp
and press tab - it will first complete to
alpine01
and then, at the second tab, replace it with the correct UUID of the zone.
Once inside, you can update packages, install software, etc. Just one caveat: Alpine Linux changed some things with apk 3.x (so from 3.23 on) and it seems that, without IPv6, updates can cause problems. The workaround that worked for me was adding a line like
151.101.66.132 dl-cdn.alpinelinux.org
to
/etc/hosts
(it's a CDN address, so it may change over time) and, at that point, you can move directly to Alpine 3.24, the latest currently available.
Commands like
top
,
free
,
df
, etc. will work and return the assigned values, almost as if it were a VM.
In this example I used Alpine, but many distributions are available and supported.
But LX zones are a compatibility layer. SmartOS also has native zones, usually created from the base images, and we can easily add one:
imgadm avail | grep base | tail
85d0f826-0131-11ed-973d-2bfeef68011c  base-64-lts                     21.4.1        smartos  zone-dataset  2022-07-11
93bdf06a-01ef-11ed-81ff-bf0efad842c7  base-64-lts                     20.4.1        smartos  zone-dataset  2022-07-12
e44ed3e0-910b-11ed-a5d4-00151714048c  base-64-lts                     22.4.0        smartos  zone-dataset  2023-01-10
e6b8e342-c19d-11ed-b9d1-00151714048c  base-64-trunk                   20230313      smartos  zone-dataset  2023-03-13
0b13305e-4fe1-11ee-b322-00151714048c  base-64-trunk                   20230910      smartos  zone-dataset  2023-09-10
db382b98-822e-11ee-992e-00151714048c  base-64-trunk                   20231113      smartos  zone-dataset  2023-11-13
8adac45a-aca7-11ee-b53e-00151714048c  base-64-lts                     23.4.0        smartos  zone-dataset  2024-01-06
8925400d-ff66-441e-ab5c-340505636ff8  base-64-trunk                   20240116      smartos  zone-dataset  2024-01-16
2f1dc911-6401-4fa4-8e9d-67ea2e39c271  base-64-lts                     24.4.1        smartos  zone-dataset  2025-01-06
b933df4b-b8f4-4bef-ad1e-236a20304496  base-64-lts                     25.4.0        smartos  zone-dataset  2026-01-09
So:
imgadm import b933df4b-b8f4-4bef-ad1e-236a20304496
That's the latest one, 25.4.0. Then we need a proper JSON for native zones (the brand is
joyent
, a legacy of the company that created SmartOS). Let's make one for nginx, for example -
nginx.json
:
{
  "brand": "joyent",
  "image_uuid": "b933df4b-b8f4-4bef-ad1e-236a20304496",
  "ram": 512,
  "hostname": "nginx",
  "resolvers": [
    "9.9.9.9",
    "1.1.1.1"
  ],
  "alias": "nginx",
  "nics": [
    {
      "nic_tag": "admin",
      "ips": [
        "192.168.1.254/24"
      ],
      "gateway": "192.168.1.1"
    }
  ],
  "customer_metadata": {
  },
  "quota": 5
}
Then:
vmadm create -f nginx.json
Once the zone is ready, just use
zlogin
as usual. Once inside, we can install nginx (and useful packages like certbot, etc., if needed) with pkgin (
pkgin search certbot
will show the exact package names):
pkgin in nginx py314-certbot-nginx
At the end, the banner will tell us how to start nginx at zone boot:
/usr/sbin/svcadm enable -r svc:/pkgsrc/nginx:default
At this point we'll have two zones - one native, one with Alpine Linux - ready to run our workloads. The same principle can be used to create VMs, with both bhyve and KVM, but that will be the topic of a future article.
