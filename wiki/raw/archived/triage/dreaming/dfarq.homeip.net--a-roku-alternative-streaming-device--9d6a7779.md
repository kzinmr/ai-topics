---
title: "A Roku alternative streaming device"
url: "https://dfarq.homeip.net/a-roku-alternative-streaming-device/?utm_source=rss&utm_medium=rss&utm_campaign=a-roku-alternative-streaming-device"
fetched_at: 2026-08-30T10:01:00.930238+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# A Roku alternative streaming device

Source: https://dfarq.homeip.net/a-roku-alternative-streaming-device/?utm_source=rss&utm_medium=rss&utm_campaign=a-roku-alternative-streaming-device

The privacy, or lack thereof, around streaming media has been bothering me lately. I’m sure some people would ask what took me so long. And I’m sure others would say I am overreacting. But it is a problem not very many people have talked about, and even fewer have tried to solve and then talk about. For me, the tipping point was the acquisition of Roku, a company I have long admired, by Fox, a broadcasting company. A media company, Fox or otherwise, tracking what I watch and injecting ads is way too
Max Headroom
for me, which led me to seek a Roku alternative.
The Roku problem
I like to turn machines like this
Dell Optiplex 3040 micro
into streaming devices. They take up about as much space as a Roku and have lots of advantages.
Roku was a solution to a problem for me. Besides being a cool product with a couple of ex-
Amiga
engineers on its design team, it was a streaming hardware platform controlled by a relatively small company. With it off the board, all of my possible off-the-shelf alternatives are controlled by a big tech company. Roku went from being a solution to another problem. Hence my need for a true Roku alternative.
In theory I could get an Amazon or Google TV device and load LineageOS on it, which is a de-Googled build of Android. In practice, the models Lineage supports are discontinued, and although I can find old models online, I can’t usually tell from the listings which model it is, so maybe it’s supported, maybe it’s not. So I can take a chance on random old models. Or I buy current models and wait, but I wouldn’t know how long I would have to wait.
A build exists for the Raspberry Pi, which sounded like a good option. The 2 GB model of the Raspberry Pi Model B would be ideal for this application, if you can find one.
Then I found a build of
LineageOS TV for x86
, which runs on ordinary PCs. And that gave me an idea.
Turn a PC into a Roku alternative
No, I don’t want a bulky desktop or worse yet, a minitower next to my TVs. Not long term. That’s fine to prove the concept, if you have a spare desktop laying around. But for anything more than a temporary setup, I’d want something smaller.
But small form factor PCs do exist. They are somewhere in between streaming box and a game console in size and have regular PC hardware inside. You’ve probably seen them in doctors’ offices.
They cost a lot more than a Roku, if you buy new. But I don’t buy new ones. The
Dell Optiplex 3040 Micro
is old enough that it doesn’t support Windows 11, but it has an HDMI output. They’re relatively plentiful because corporations are retiring them, and demand is higher for the newer units that can run Windows 11. I can get an Optiplex 3040 Micro for around $60-$70, comparable to a Raspberry Pi Model B once I get an enclosure, storage, and power supply. Look for one with wireless networking built in. I haven’t had any luck getting USB wireless solutions working.
I go with Dell specifically because the 3040 and newer models have HDMI. Similar HP and Lenovo models have Displayport, which you can adapt to HDMI, but that’s extra expense.
And then I can load LineageOS on it, load a Jellyfin client on it to stream my locally hosted media, and disappear. I can be like one of those Blanks in
Max Headroom
. I can load a repository like F-Droid and load open source clients that allow some limited streaming. And for someone who wants to disappear less completely, you can load regular Android TV apps on it and still have a greater degree of privacy than you would using stock Android TV.
Sound good? Here’s the build process I came up with.
LineageOS TV x86-64 on a mini PC
I acquired three Dell Optiplex 3040 micro PCs to experiment with. They’re about seven inches wide, seven inches deep, and only an inch tall. And they don’t really look out of place next to a TV.
I loaded
LineageOS TV x86-64
on them. It’s alpha so it’s a little glitchy but hey, Rokus can be a little glitchy sometimes too. The important thing is, Jellyfin runs better on my $50 PC running an alpha operating system than it does on the Roku. That’s a win, and will only get better. It boots in about a minute, every Jellyfin client I tried loads almost immediately, and was smoother once it was up and running than it is on the Roku.
To control the one that didn’t have wireless or bluetooth, I bought a
$12 USB remote
that works OK for playback but doesn’t really have all the buttons you need to set up the device. A USB game controller is likely to work as well or better, so if you have one laying around to try, try that first.
For the units that had wireless and Bluetooth, I loaded an open source app called
Bluetooth Remote
on our Android phones. Use that app specifically, because the idea is to have privacy. It has all the buttons you need to navigate around Android TV, and therefore LineageOS, comfortably.
I have had trouble getting audio working over HDMI. If you do too, you may want to attach some speakers, because the speaker in an Optiplex Micro is very wimpy.
Creative Labs Pebble speakers
are an inexpensive, compact choice that draw power over USB.
The build process
I downloaded the ISO, then wrote the ISO to a 4-gig USB stick using
Rufus
. Then I downloaded APKs for a Jellyfin client called
Wholphin
and a nice launcher called
Projectivy
. I also downloaded the APK for
f-droid
, an alternative app store that only hosts free, OSS mobile apps. I saved the APKs onto the same USB stick containing LineageOS. There was plenty of room. It’s entirely possible to load some or all of the Google infrastructure onto it so it acts like any other Android TV, but I just want an operating system, a launcher, and a Jellyfin client. I didn’t need any of the Google stuff for that. If you want to use commercial streaming services, you may need to load the Google apps/Play services.
I cabled up the Dell, including connecting a USB keyboard and mouse, plugged in the USB stick, mashed the F12 key after power up, and selected the option to boot off USB. And then I selected the option to install Lineage.
The installer asks for some options. It warns not to pick all of them at once and for good reason. Some of them contradict each other and result in a system that won’t run. The main thing you need is the codecs. Go ahead and pick all of them. I also checked the box for all of the battery options, and the audio option to use Celodon.
Once I got past that, taking the defaults worked fine.
When it boots, LineageOS may get stuck trying to detect Bluetooth devices. Use your USB keyboard to break out of it. Hitting space worked for me. I’ve also seen suggestions to hit TAB, F2, and/or ESC. You can then pair Bluetooth devices by navigating to Settings > Remotes & Accessories.
Once I booted, I opened up the files app. I clicked the hamburger menu in the top left, found my USB stick, then located the APKs. I opened the APK for Projectiviy and answered yes when I had to give permissions. Then I repeated for Wholphin and F-Droid.
The tricky part is getting Projectivy as the default launcher. To do that, run Projectivy, run through its setup, then go to Settings > Projectivy Settings > General > Launcher. There you can select Projectivy.
This is a good time to put the device on your wifi. That option is in the top right.
Then I launched Wholphin, pointed it at my local Jellyfin server, and the result was a nice overall UX that rivals Roku, lets me watch content I host locally on my own Jellyfin server, and doesn’t send out any telemetry about what I’m doing, profile me, or serve me ads. More on Jellyfin later.
How’s it run?
I’ve tried this combination on i3 6100T and i5 6500t processors with 4 or 8 GB of RAM and whatever sub-128GB SSDs I had laying around. It runs smoothly, and now that I have a build process down, it takes me less than 30 minutes to spin one up. Honestly, 8 GB feels more future proof, but 4 GB is fine, and with even DDR3 RAM prices being high right now, I’m happy to run some of them with 4 GB. When prices come back down, I can always come back and upgrade the memory and/or processors.
And that’s another nice thing about this solution. Unlike a Roku, I can come back and upgrade later, swapping in more storage, more RAM, or a faster processor. I don’t have to buy a whole new unit when it goes obsolete. I give up some ease of use, but I gain back control. Since I’m very comfortable swapping parts around, this is a solution that works for me.
The content problem
The other problem is that these days, purchase doesn’t mean ownership. The content industry no longer abides by the rule that a deal is a deal.
In 2009, there was a big uproar when Amazon deleted books off Kindles that customers had paid for. The reason, they said, was the books violated someone else’s copyrights. I’m old enough to remember a time when the remedy for that was to give the money to the rightful owner. Not delete the content. Amazon promised not to do it again.
Instead it set a precedent. Amazon repeated the behavior randomly starting in 2024 with video content.
Another example that’s not as notorious as it should be is when Sony announced in 2023 that it would be deleting all of the Discovery content its customers had paid for. And it only gave 27 days notice.
Maybe you get a refund, maybe you don’t.
So when you buy content, you’re really only renting it for an indefinite period of time, unless you secure a digital copy of it that you can host on a computer inside your own network, not in something someone else controls. So, if you buy digital content online, always always always ensure you get an actual file you can store someplace. Or buy physical media and then rip the media to a file you can store someplace.
Also, a great deal of content goes into the public domain
every January
. Yes, we’re talking content that’s either 95 or 100 years old. But maybe that’s not that bad. I don’t know about anyone else, but experiencing some of the Roaring Twenties for myself seems pretty good right about now.
Breaking free with a self-hosted server
For a self-hosted server, I recommend
Jellyfin
. It’s not terribly hard to set up and can host video, audio, and books. Its user experience is similar to commercial streaming services, with the exception of providing recommendations. Since it’s not actively building a profile on you, it’s not as good at guessing what else you’ll like. I think the trade-off is worth it.
You’re on your own for content, but even if you limit yourself to public domain content and never buy anything again, there’s a lot of excellent content available free. You can also rip physical media you already bought and paid for. It’s fair use, the rightsholders get paid, but they can’t change their mind later.
If building a Jellyfin server seems like a bit much for you, you can
download a prebuilt image
that you just load on any x86-64 PC. It runs on Linux, so there’s no licensing involved, and it includes not just Jellyfin, but enough infrastructure to make it easy to copy content onto it from a Windows PC over the network.
All trademarks are the property of their respective owners. Keeping track of who owns what this week is a full time job and I already have one of those. I’m sure you understand.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
