---
title: "NixOS is making me less afraid"
url: "https://entropicthoughts.com/nixos-is-making-me-less-afraid"
fetched_at: 2026-10-21T10:00:52.374204+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# NixOS is making me less afraid

Source: https://entropicthoughts.com/nixos-is-making-me-less-afraid

Something funny happened a little while ago: I read about FreshRSS, and it
sounded nice, so I
installed it on a server and started using it
. That would
not have happened a year ago, but then again, a year ago I didn’t have any NixOS
servers.
For the past few years, my
rss
feeds have lived locally on my phone only.
There was a good idea behind that
1
I can mostly take time to read when I’m
away from my computer anyway.
, but it never quite worked in practice. For one,
many things are easier to read on a larger screen. But it was also brittle to
trust a phone app to manage the read/unread status of thousands of articles
across a hundred feeds.
2
In particular, when I switched to a different phone
I could migrate all feeds to it, but the read/unread status was lost along the
way.
What I really wanted was a server-side feed aggregator. This is software
that runs on a server, manages
rss
feeds, and then I can read the
rss
feeds
either through a web interface, or through client applications. I’ve wanted that
for a while, but I’ve never taken the step, because it would be yet another side
project to maintain the deployment of.
But now, with some NixOS experience, adding a working FreshRSS configuration
(including backups) took 9 lines of Nix code
3
Plus a dozen more lines for the
nginx reverse proxy configuration. It got a little complicated because I wanted
to
proxy_pass
from a specific location block which required rewriting cookie
paths. But that’s a me problem, not a NixOS problem.
. That installation has
just hands-off worked for the past few months. If or when that server breaks, I
can spin up a new one running the exact same configuration, probably in
something like 15 minutes. When we can do something like that, there is
literally no reason to not just try the new software.
Contrast this against how FreshRSS is installed outside of NixOS. Then we’d
download and extract an archive to the right location;
configure permissions according to instructions;
install nginx and
php-fpm
with necessary extra dependencies to the server;
configure
php-fpm
pools and make nginx pass requests through to
php-fpm
;
set up Let’s Encrypt certificates;
set up backups; and
hopefully remember how to do all the above if something breaks and we need to
reinstall FreshRSS on a new or upgraded server later.
Of course, the FreshRSS project provides a container image which would shorten
the process a little bit. It purports to set up Apache with mod_php and
configure them the right way. Then we’d only need to configure backups, create a
systemd service that runs the container, and manage nginx as a
tls
terminating
reverse proxy in front of that, because the container image reasonably does not
come with
tls
support. This is still stuff to remember, and there’s also no
guarantee the same thing works six months down the line when reinstalling,
unless we wrote down which exact container image we downloaded.
4
It does not
help to build the container image from source, because two builds from the same
Dockerfile separated by time can result in rather different container images.
I have mentioned before how much I dislike maintaining side projects. That
includes my own code, but also self-hosted services developed by someone else.
I’m okay with a few minutes of maintenance here and there, but having to
schedule hours of uninterrupted work to upgrade something, or spending
any
amount of time at all on emergency maintenance, really kills my desire to work
with computers.
You’d think someone of my disposition would be deep into configuration
management, container orchestration, or both, but no. I have made honest
attempts with CFEngine, Ansible, podman, and k3s but none of them improved my
installation/configuration/deployment experience significantly over (a)
carefully writing things down, and sometimes (b) turning those careful notes
into a shell script performing a sequence of
ssh
commands.
5
Yes, this is
essentially reinventing Ansible – but less brittle. It won’t break the next time
someone glances sideways at
pip
.
The drawback of the shell script is that it
often ends up relying on assumptions that become invalid with time, or when it
is used in a different environment. A NixOS configuration reads a lot like the
careful instructions to myself, except they’re executable and they produce the
same result every time.
