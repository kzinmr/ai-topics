---
title: "How will a Athlon 64 PC with 512 of ram hold up as a home server?"
url: "https://boyter.org/2009/01/athlon-64-pc-512-ram-hold-home-server/"
fetched_at: 2026-05-05T07:02:08.506974+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# How will a Athlon 64 PC with 512 of ram hold up as a home server?

Source: https://boyter.org/2009/01/athlon-64-pc-512-ram-hold-home-server/

This post was taken from a
Mahalo Answers Question
I answered.  I thought rather then risk Mahalo going away (since Jason Calacanis has said hes working on something else) I thought I would copy it here.
Question
How will a Athlon 64 PC with 512 of ram hold up as a home server. Whats the best setup… read details. I want to setup a drag and drop file server as well as a voip server like teamspeak. Also have a low user website. What OS should I use and how do I make it also a web server.
Answer
Short answer very well. None of what you want to do which as written above, file sharing/server, low end webserver, teamspeak server is going to really tax that machine to much. For OS, just go with whatever you are most comfortable with unless you want to learn new things. If you are most familiar with Windows then you will have far less frustration in using that for your server then getting a crash course in Linux or BSD.
Long answer. Generally file servers work better with more RAM, which they can use as a buffer between the HDD and the network. I had a file server with 128 meg of RAM and when I upped it to 512 meg you could notice the difference when copying large amounts of large files. Honestly though unless you are working with video files or doing large copies frequently it wont make a noticeable difference.
For teamspeak the server requirements are a low end Pentium or Pentium 2 and 128 RAM. So no issues there. Even if you are using some other program I suspect that you will saturate your internet long before your VOIP is throttled by CPU and/or RAM.
For a webserver what you have there will also be fine even if it is running a dynamic site using WordPress etc… so long as you don’t make the front page of digg or slashdot and then once again your bandwidth will give out before your server crashes. If your website does become popular you can always outsource or get a beefier server.
Finally choice of OS. Mainly this should come down to your preference, experience and needs. For webserver generally you will want Apache or IIS. Apache is Windows and Linux, IIS is Windows only.
Apache. You will find more guides on the net using Linux (usually Ubuntu). Here are two I found in 5 mins using google and walk through the whole process.
http://nettuts.com/articles/news/how-to-setup-a-dedicated-web-server-for-free/
http://www.howtoforge.com/perfect-server-ubuntu8.04-lts
If you are going to go Windows option and want apache, Xampp will get you running very quickly and can be secure if you add passwords etc…
http://www.apachefriends.org/en/index.html
IIS… I am not a guru of IIS, hopefully someone can come along and answer this for you. I have used it in the past and never had any real issues with it though.
BTW To have you website have a nice domain name you will either need a static IP (which means your IP address stays the same) or will need to set up Dynamic DDNS. IF you want a static IP ring your ISP they should be able to sort it out for you, but make sure you check their home server policy because some might not allow home servers.
For DDNS, read the following and use the links at the bottom or do some google searches. There are many DDNS providers, each of which I find do a similar job, so just pick one that gives you the name you want.
http://en.wikipedia.org/wiki/Dynamic_DNS
Otherwise best of luck with this. It is usually a lot of work, but very rewarding once you host your own website. :)
