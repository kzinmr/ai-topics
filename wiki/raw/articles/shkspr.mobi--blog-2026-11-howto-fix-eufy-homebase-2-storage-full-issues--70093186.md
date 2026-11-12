---
title: "HowTo: Fix Eufy HomeBase 2 Storage Full Issues"
url: "https://shkspr.mobi/blog/2026/11/howto-fix-eufy-homebase-2-storage-full-issues/"
fetched_at: 2026-11-12T10:01:10.544220+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# HowTo: Fix Eufy HomeBase 2 Storage Full Issues

Source: https://shkspr.mobi/blog/2026/11/howto-fix-eufy-homebase-2-storage-full-issues/

Quick Fix: Insert a USB memory stick, format it in the app, restart the Eufy HomeBase 2, format the internal memory, restart the hub.
I've had the
eufyCam system for over 6 years
- which is pretty long-life for IoT devices.  The cameras have worked pretty much flawlessly. Four years ago I added their
Video Doorbell
which has been similarly well behaved.
But last night I went to check some security footage, only to be told that the 16GB storage was full. Ordinarily that shouldn't be a problem. Full storage just means that older videos get wiped and new ones replace them. In my case,
all
the old videos were gone.
I could see the cameras and control them, I just couldn't access any old recordings.
There was nothing on there I especially needed (although I'm curious as to when a courier dropped off a "lost" parcel) so I was happy to experiment with fixing the system.
The Eufy forums are full of people having these issues. Anker, the brand that own Eufy are usually fairly customer focused - but I guess they're more interested in getting people to upgrade to a newer hub than fixing the problems with their old kit.
Restarting - no change.
Repairing the storage - didn't fix anything.
Clearing the storage - dire warnings but didn't help.
Formatting - a last resort, but failed.
I found an old 4GB USB-A memory stick and shoved it in the back of the Eufy. The app detected it fairly quickly and said the stick needed to be formatted - so I let it.
Once the stick was formatted, I restarted the hub. Running fix or clean didn't change the situation, so I tried formatting the main memory again. This time it seemed to work. It crawled to 100% and then hung.
I restarted the app and it told me that the storage was unformatted and needed to be formatted again, so I let it.
I restarted the hub and everything sprang to life, no more warnings about full storage.
I'll keep an eye on the storage to make sure it doesn't fill up again.
I'm reluctant to buy a new HomeBase. I like to self-host things, but the promise of commercial kit like this is that it takes the hassle out of ownership. I don't really want to be futzing around formatting memory and deciphering error messages.
If this fails again, I'll have to seriously consider moving my cameras onto something that I can control. At least that way, if it screws up, I'll only have myself to blame.
