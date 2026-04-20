---
title: "Using agents and Wine to move off Windows"
url: "https://1wwzn.mjt.lu/lnk/AUYAAJZ_u8sAAc7fQ14AA-_j058AAYKJInQAoTMkADFx-wBp5jXkibhiNlxtRNuEx5QBNOwcYAAtKWs/6/oOAhGpG22Re0NnP12rwSqQ/aHR0cHM6Ly9tYXJ0aW5hbGRlcnNvbi5jb20vcG9zdHMvdXNpbmctYWdlbnRzLWFuZC13aW5lLXRvLW1vdmUtb2ZmLXdpbmRvd3MvP3V0bV9zb3VyY2U9bmV3c2xldHRlciZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1tb250aGx5"
fetched_at: 2026-04-20T14:23:32.621748+00:00
source_date: 2026-04-20
tags: [newsletter, auto-ingested]
---

# Using agents and Wine to move off Windows

Source: https://1wwzn.mjt.lu/lnk/AUYAAJZ_u8sAAc7fQ14AA-_j058AAYKJInQAoTMkADFx-wBp5jXkibhiNlxtRNuEx5QBNOwcYAAtKWs/6/oOAhGpG22Re0NnP12rwSqQ/aHR0cHM6Ly9tYXJ0aW5hbGRlcnNvbi5jb20vcG9zdHMvdXNpbmctYWdlbnRzLWFuZC13aW5lLXRvLW1vdmUtb2ZmLXdpbmRvd3MvP3V0bV9zb3VyY2U9bmV3c2xldHRlciZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1tb250aGx5

I don't think people have fully internalised how good agents are at reverse engineering code. I had one take a Windows app rated "garbage" for Wine compatibility and get it working on Linux: decompiling DLLs, writing code caves, patching assembly. Equally, they're superb at the kind of sysadmin tasks that make desktop Linux painful.
I've been increasingly unhappy running Windows on my main workstation (I still love Apple hardware for laptops, though). While Windows Subsystem for Linux is pretty excellent, I realised all I was using Windows for was Chrome, Slack and WSL. Plus Windows definitely isn't going in the right direction for my use cases (and I'd argue many people) - with endless bloatware being added in each new release.
While I've got over 20 years Linux experience, I've always struggled to get desktop Linux working very well - despite first installing Red Hat 6.0 many, many years ago. I've always found issues that were painful to resolve, but I had a thought - could an agent fix these for me?
First stop, Fedora
While chatting with an LLM on this plan, it recommended Fedora over Ubuntu at one point. I assumed (probably like many) that Ubuntu was the most polished Linux distribution. I've certainly had no real issues with Ubuntu on the server, but I haven't really used Fedora for many years on the desktop.
Armed with a USB stick, I gave it a go.
First impressions were
very
good. Unlike Ubuntu, it managed fractional font scaling on both my monitors out of the box. All of my hardware was detected and unlike Ubuntu the default packages are nearly all up to date. This is a huge plus - given how badly Ubuntu packages lag latest versions, I have to spend far too long installing random PPAs and binary distributions of many packages. I
believe
this is beginning to improve, but it's just great to be able to
dnf install
a language or tool and have a (mostly) very recent version.
Flatpak also works great, and the GNOME Software app is really nice.
So far, so good. I'd really recommend Fedora for desktop use.
Fixing problems
The first major issue I hit was using my spare iPhone as a webcam. While there are some good solutions, all of the ones I found require an out-of-tree kernel module, which if you use Secure Boot becomes a real pain. This is the
exact
kind of issue where I'd waste far too much time trying to fix manually, and probably at some point give up.
Claude Code, however, guided me through the fairly arcane steps of using
mokutil
and
akmods
to build and sign it. Within a few minutes, webcam working!
The only other issue of note I had the agent fix was multiple Bluetooth devices causing issues. I had Claude Code resolve that by disabling the less important one (though not sure why this doesn't work out of the box) and it even found a way to grab my Bluetooth encryption keys from Windows so everything automatically paired.
In general this worked brilliantly. Even setting up various desktop tweaks (font config, Dash to Panel, etc) was really easy and efficient and saved a tonne of time Googling around to find the best options.
Overall this was
far
quicker than installing and setting up Windows fresh, given Windows requires far more drivers to be downloaded and installed. Linux hardware support for the most part is really excellent these days.
Wine
I did realise that I needed a couple more Windows apps, ideally. All but one worked very quickly with Wine, with Claude Code setting up the various
WINEPREFIX
es and installing the right DLLs.
However, I hit a significant snag trying to get
Airflow
working (it's a really nice app for streaming content to AirPlay and Chromecast devices). Nothing works quite as well as it in my opinion.
This app was rated
"garbage"
for Wine compatibility. This gave me an idea though to see how far I could push Claude Code to fix it. While at first it was hesitant to try and recommended various other alternatives, I insisted it try more.
Incredibly
it managed to get things almost entirely working (and working enough for my needs!). This was an extremely involved (for 99.99% of humans) process.
The first thing it did was build a stub
powrprof.dll
to implement Windows power management APIs the app required. It used the
mingw
cross-compiler to compile a Windows DLL on Linux and load that in. I wasn't even aware you could compile Windows DLLs on Linux like that.
Then came a series of crashes. A socket option level that Wine's Winsock translation didn't handle, Wine's buggy C++ exception handler corrupting vtable pointers, and a Qt call returning null because Wine maps screen coordinates differently to Windows. For each one, Claude Code decompiled the relevant DLLs, worked out what the assembly was doing, and binary-patched them: writing code caves, changing conditional jumps, fixing socket constants at specific file offsets. It was
so
good at this and felt like complete magic watching it work.
This took quite a few rounds, but I could get on with other tasks while it worked, and the agent would let me know to test it again.
A couple of hours later and Airflow was working and streaming to my Chromecast(s). I believe AirPlay was also working but I didn't have a device handy to fully test it. If you're interested in more detail on this I wrote a
gist
of the main steps it did.
Airflow streaming to Chromecast, running in Wine on Fedora
The implications
Firstly, it'd be
awesome
for one of the inference providers (or model creators themselves) to have a go at fixing thousands of Wine apps autonomously in an agent harness. I think it'd be an awesome benchmark in itself of how good an agent/model is
and
would be a great public good.
But the main conclusion I came to is that a lot of the typical "network effects" for software ecosystems are far more fragile than before. It was once a given that these ecosystems had almost impossibly strong network effects. As agents continue to get better and better, it seems to me that reverse engineering and porting apps between platforms is just a matter of tokens.
Finally, I do think it's a shame to see that many open source projects are insisting on a complete ban of any LLM generated code. While I totally appreciate the flood of garbage PRs is taking far too much maintainer time up, I think highly skilled open source developers with agents would allow an enormous amount of improvement in a small space of time. Hopefully this will get more flexible with time.
In my opinion open source absolutely
shines
when you can have an agent work with it. It really in a way fulfils the original vision of open source - that everyone can edit and improve the app or tool in the way they see fit. Agents completely democratise that.
