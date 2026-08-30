---
title: "Can Self-Hosting Be Simple?"
url: "https://feed.tedium.co/link/15204/17432610/self-hosting-third-place-strategy"
fetched_at: 2026-08-27T10:01:15.972959+00:00
source: "tedium.co"
tags: [blog, raw]
---

# Can Self-Hosting Be Simple?

Source: https://feed.tedium.co/link/15204/17432610/self-hosting-third-place-strategy

Hey all, I’m working on a new newsletter dedicated to mini-PCs that I’m planning on launching soon, but I wanted to kind of give a sneak peek of what I’m thinking. If tiny computers are your thing, sign up here!
Earlier this year,
I wrote a big thing about where self-hosting was going
, and looked at a number of emerging software tools. One comment I heard as I went deep into all the competing tools is that some folks just kind of wanted a template to work with. Less magnifying glass, more 30,000-foot view.
This time, I’m going to keep it simple. Like last time, I’m doing this with the support of a review unit, the
Acemagic K1
. This particular unit is more of a modest player in the modern computing landscape, essentially an embedded AMD processor retrofitted in a mini-PC context. At the moment, this unit sells for $349 ($319 with coupon) on Amazon in its 16GB/256GB configuration. (There are faster processors with
this form factor
, generally hitting below the $500 mark.) Unlike the Kamrui machine I reviewed in the last piece, this isn’t overpowered for its use case. It’s good enough to do Plex and run a Syncthing server. That’s really all the average person needs.
I ran the installer on Windows, and it worked fine, and it handled my dock, even though the device does not support USB4, leaving it out of the Thunderbolt conversation. (My Dell Thunderbolt dock has a built-in chip to downstep to USB 3.2. I bought it cheap on eBay—best purchase in a while.) But if you buy this machine, be aware that it’s not a screamer. The Ryzen R2544 embedded chip outpaces Intel’s N150 processor, a common low-end chip in mini PCs, but you’re not buying this to game. You’re buying this because you need a device to drop somewhere, and you aren’t going to look at it more than a couple times.
(One general note on Plex, Jellyfin, and similar video-hosting tools: While this will certainly work, you likely want Intel or even a Mac Mini for that use case, because
video encoding is a weak spot for AMD
. But not every mini PC has to be a Plex machine or game console.)
That’s not much SSD space, nor is it maxing out your RAM, but it is enough to do some pretty basic self-hosting stuff. With that in mind, we’re not going to reinvent the wheel here. I’m going to recommend about half a dozen tools that can be hosted by just about anyone, that hit broad use cases, and that actually make sense for a low-end computer with 256 gigs of storage.
The tools in question:
Immich
,
a very good Google Photos alternative
Linkwarden
,
a link management tool akin to the late, lamented Pocket
Vaultwarden
,
a password management platform based on Bitwarden
Syncthing
,
a file-syncing platform that’s akin to a locally hosted Dropbox
CryptPad
,
an encrypted office suite that’s hopefully less annoying to install than NextCloud
Hermes Agent
,
because I refuse to put OpenClaw on this thing but realize folks are probably curious about this
These all cover various common self-hosting use cases, none of which require video or Steam. In the case of all of these you can technically host everything in your own little bubble, though in the case of Hermes you’re realistically going to be plugging it into an external LLM.
The idea with this is that I’ll set it up once, I’ll occasionally update it, and it will just do its thing, syncing data and offering a home for old photos and a backup repository for secure data.
Look, this ain’t gonna win any land-speed awards. But mini PCs don’t have to.
Not blazing fast, but perfectly useful
Some notes about the machine: It is not a beast; it’s perfectly cromulent. Per my Geekbench test in Windows, it got a score of just 900 in single core and 3000 in multi-core. (It slightly bested those numbers in Linux.) That’s actually on the low end of performance for this chip. But it’s still a little faster than a Raspberry Pi 5 or an N150, though not by much. More notably, it’s also slower than an AMD Ryzen 3 4300U, which on paper, it should be faster than, as it has a higher TDP (45W vs. 15W), more threads, and a higher clock speed. But with the processor capped at 28W in the machine, it makes the device run a little more modestly. Alas.
Why does it underperform? Simply: the RAM is both on the slower DDR4 standard and there's only one chip of it in the machine. (You generally want two separate RAM chips for dual-channel memory.) To put another way: This is a solvable problem if you’re able to upgrade it.
How hard is that upgrade? Well, it’s very much possible, with a couple of notes. First, the screwholes, hiding under the rubber feet, are recessed in a way that a relatively standard iFixit screwdriver can’t easily fit inside, which made it harder to open than it needed to be. And second, the expandability is on the top of the board, not the bottom, which means you need to take the machine completely apart. (It’s not locked down like Fort Knox or anything, or even that complex a box, but that does complicate a simple upgrade.)
But the nice thing about mini PCs is that, once they’re set up it’s set-and-forget. And at a time when buying a computer costs more than ever, a device that hits around $300 still feels perfectly reasonable.
Dockge doesn’t promise anything more than a simple way to manage Docker compose scripts. It does the job admirably … but you still have to set up Docker first.
A normie distro, a normie self-hosting strategy
My first steps for this process involved installing the most normie of Linux distros,
Linux Mint
. (I specifically installed it so it automatically logs in, which is important for this use case.)
My goal: To set up the machine with a bunch of Docker containers, then set it up so those containers could be accessed on
Tailscale
and nothing else. Tailscale is available on basically every device you can think of, and you can
even enable ssh
for it. Once that’s set up, you can ssh in from another machine on your “tailnet” and do all your work on it, with the mini PC completely headless. But on those rare occasions you
do
need to hop into a GUI, you have Mint right there.
So, after doing some prep work in a virtual machine, including building out the docker-compose files I would be using, I copied those files from the VM to the live machine using scp. Big time saver, and one Tailscale makes particularly painless.
In terms of the Docker install, which has a couple modest bugaboos, I more or less
followed the install process for Ubuntu
. But instead of restarting the machine, something I obviously wanted to avoid given that I was in the terminal, I
followed the post-installation process
.
In the past when writing about these apps, I’ve at times courted disaster (see the
nightmare
I had to manage with Cal.com a few years ago). This time, however, it was relatively smooth sailing, thanks to a tool called
dockge
. It’s not packed with bells and whistles like
Cosmos
or as in-depth as
Portainer
, but it is simple and just kind of works. It makes launching a new container as easy as copying a bunch of docker-compose scripts and .env variables directly into a page on a Tailscale-provisioned website.
While a bit rougher around the edges, CryptPad is a promising, privacy-respecting choice of office suite if you’re allergic to the complex setup of NextCloud.
Some of my tools, like Syncthing and Immich, just worked. Others still required me to hit the terminal, particularly CryptPad, which presumes a two-URL setup to secure the stuff you’re working on. But given the hell that a NextCloud install can often be, it’s actually easier to set up than that mess of wires. I got Hermes working, complete with API wiring to DeepSeek and Xiaomi’s MiMo, and it did the job without taxing the device.
Yes, there were hiccups. CryptPad and Hermes-WebUI occasionally stuttered as I attempted to solve my https issues, with CryptPad in one case seemingly losing its data. (It might have been user error, to be fair.) The process of installing Docker containers is always full of bugaboos, and Tailscale adds a few.
I had to build custom scripts to get https to load over Tailscale, for example. They work, but point to a gap in Tailscale’s feature set; it should be smart enough to know that a Docker container is usually shared with https and account for that in its serving strategy. But instead, you’re having to reinvent the wheel every time you add a node to your tailnet, which feels counterproductive.
Your data needs a third place, too
You likely have friends and loved ones with nearby homes. Maybe you have an office. This computer could live in those places, and buy you some peace of mind. Because stuff happens. Your power goes out, and so does your homelab. But even if your normal sync machine is out of service, you can still save your data somewhere, just in case. With that in mind, I’m having this little box live offsite, because it’s just practical advice.
I installed this with Linux Mint and RustDesk because you never know when you’re gonna have to load up GParted. Maybe you can just randomly make a USB drive show up in your remote computer by thinking about it.
Could I take this build further? Very much so. I’m only sharing select data with this machine because, I don’t know if you heard, but SSDs are expensive these days. On top of everything else, I was able to get the remote-access tool
RustDesk
working on this device as well. There was a bit of setup involved, much of it more complex than a normal person might be willing to do, but I’m now able to hop into Mint and handle settings the graphical way if I so choose. Plus, there’s always the possibility of running the machine completely through a VPN. (Mullvad and Tailscale actually offer a service for this exact purpose, so you don’t have to choose
or
build a hacky solution.)
So how’d the Acemagic machine hold up to all this? Not bad! I didn’t see it choking at anything I threw at it. I was even able to get RustDesk to stream YouTube videos through it at 30fps, with completely synced audio.
It didn’t get hot or loud, either. A mini PC I’ve had for about five years frequently spins up and makes loud fan noises. I barely even noticed the Acemagic. It’s not high-end. It’s wrapped in cheap gray-and-black plastic. But it does the job, even if I have a sinking feeling that, in normal times, we’d never see a consumer device hit with this weird embedded processor.
This specific solution with the Acemagic machine is perfect for this kind of use case. It’s not a high-end machine—it’s light, and it’s got a pretty basic, barebones plastic design. But it doesn’t get hot. Plus, I have a feeling that if this was normal times we would see a better processor under the hood. But it’s more than capable enough with the right use case.
This is a step above a Raspberry Pi—and honestly, with all the price increases in the single-board computing world, it costs about as much as one. Things ain’t cheap out there, but you can still make a weekend project out of something like this.
