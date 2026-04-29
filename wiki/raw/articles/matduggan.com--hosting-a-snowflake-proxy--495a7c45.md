---
title: "Untitled"
url: "https://matduggan.com/hosting-a-snowflake-proxy/"
fetched_at: 2026-04-29T07:01:54.041370+00:00
source: "matduggan.com"
tags: [blog, raw]
---

# Untitled

Source: https://matduggan.com/hosting-a-snowflake-proxy/

In the nightmarish world of 2026 it can be difficult to know how to help at all. There are too many horrors happening to quickly to know where one can inject even a small amount of assistance. However I wanted to quickly post about something I did that was easy, low impact and hopefully helps a tiny fraction of a fraction of a percent of people.
Snowflake
So I was browsing Mastodon when someone posted a link asking for people to host Snowflake proxies. Snowflake is a lightweight proxy best explained by David Fifield below.
So, in summary, Snowflake is a censorship circumvention system, and what that means is, it's a way of enabling network communication between two endpoints despite the presence of some adversary in the middle, a censor in the middle, who's interfering with the communication. Now, that's kind of an abstract, scientifically useful definition of censorship, but this model is, of course, motivated by real-world considerations, actual censorship people encounter in practice. It's security and privacy, but it's also tied up with human rights and freedom of expression, and that's why we do this work. There are a lot of networks in the world—I won't belabor the point—but there are a lot of networks where, you want to read some news, you want to use some app, you want to participate in some discussion group, and you can't. Or you cannot easily, because there's a censor preventing you from doing so. And to give you an idea of the types of things we see in practice, a censor can do stuff like block IP addresses, it can inject RST packets to tear down TCP connections, it can give you false answers to DNS queries, and these are all very commonly seen in practice.
So there are a lot of different circumvention systems, using a variety of different techniques, what is Snowflake's angle? In a nutshell, Snowflake uses a large network of very lightweight, temporary proxies, which we call snowflakes, and they communicate using WebRTC protocols. So when I say "temporary proxies," what I mean by that is that these proxies are allowed to appear and disappear at any time. So the pool is, kind of, constantly changing, and you don't depend on these proxies to be reliable. And WebRTC is a suite of protocols that are often used for real-time communication on the web. So: audio, video, text chat, online games, a lot of these things use WebRTC.
Now we're we're equipped to answer the following two questions. And if you are accustomed, if you're used to censorship research, these answers to these two questions will tell you most of what you need to know to understand what Snowflake is doing. And you'll also understand why these are the two critical questions to ask. If you're not so familiar with this research field, I hope to give you a little bit of familiarity with why these are important questions through the course of this talk. The first questions is: How does Snowflake resist address-based blocking? Well, the answer there is the pool of temporary proxies. It's large, and by "large" you should think, about 100 thousand, and it's not always the same 100 thousand, which is important. Making proxies very easy to run is part of achieving this large proxy pool. The second question is: How does Snowflake resist content-based blocking? Well, that's WebRTC. Rather than transmit client traffic in the clear, we wrap it in an encrypted WebRTC container.
Now, our team started the Snowflake project in order to innovate in the circumvention space, to explore a different combination of parameters and see how well it works. It turns out, it works quite well. But this is more than a research prototype. This has been in serious deployment for three or more years. We serve actual users on an ongoing basis. We have to care about operations, and things like that. It is a built-in circumvention option in Tor Browser, so in Tor Browser you can just choose "Snowflake" from the menu and you'll be using Snowflake. And at any given time we're serving an average of a few tens of thousands of users.
Effectively it is a lightweight and easy to run way to bypass censorship that doesn't require running a VPN and involves almost zero technical knowledge. It's quite the design and one that I kept shaking my head thinking "man I never would have thought of this in a mission years" as I read more about how it works.
So I have a box sitting on an internet connection where I'm lucky enough to have plenty of excess capacity. I figured "why not share it". I thought I'd post the process here in case people were curious but were worried about how much bandwidth it might use or how many resources.
Running Snowflake
Setting it up on a Debian box took like 5 minutes.
Get the package from here:
https://packages.debian.org/sid/snowflake-proxy
with:
sudo apt install snowflake-proxy
Make sure it is enabled and running
● snowflake-proxy.service - snowflake-proxy
     Loaded: loaded (/usr/lib/systemd/system/snowflake-proxy.service; enabled; preset: enabled)
     Active: active (running) since Thu 2026-03-05 14:40:10 UTC; 2 weeks 4 days ago
 Invocation: 06bacb9a1d164c73a02eaf1873d483d2
       Docs: man:snowflake-proxy
             https://snowflake.torproject.org/
   Main PID: 386999 (snowflake-proxy)
      Tasks: 8 (limit: 4459)
     Memory: 715.6M (peak: 817.3M)
        CPU: 8h 32min 11.845s
     CGroup: /system.slice/snowflake-proxy.service
             └─386999 /usr/bin/snowflake-proxy
That's it.
So this has been running for two weeks and in that two weeks I've served up the following amount of traffic:
Upload: 91.81 GB
Download: 7.87 GB
Total: 99.68 GB
CPU usage is quite low, Memory is slightly higher than I would have thought but that's likely a function of running for so long. Remember you can modify the systemd service file to limit memory if you are interested in running this yourself but are concerned about crossing a gig of memory.
[Service]
MemoryMax=512M
All in all I haven't noticed I'm running this at all. Obviously its great to run the browser extension to increase the pool of IP addresses and keep them from becoming static and blockable, but if you have a dedicated box with a large amount of bandwidth and are looking for a quick 20 minute project to help out people trying to deal with internet censorship, this seems like a good one to me.
