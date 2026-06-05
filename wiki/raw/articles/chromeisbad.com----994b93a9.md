---
title: "Chrome is Bad"
url: "https://chromeisbad.com/"
fetched_at: 2026-06-05T07:01:41.931795+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Chrome is Bad

Source: https://chromeisbad.com/

Short story: Google Chrome installs an updater called Keystone on your computer, which is
bizarrely correlated
to massive unexplained CPU usage in WindowServer (a system process)
[1]
, and
made my whole computer slow
even when Chrome wasn't running
. Deleting Chrome and Keystone made my computer
way, way faster, all the time
.
Click here for instructions
.
Long story: I noticed my brand new 16" MacBook Pro started acting sluggishly doing even trivial things like scrolling. Activity Monitor showed *nothing* from Google using the CPU, but
WindowServer
was taking ~80%, which is abnormally high (it should use <10% normally).
Doing all the normal things (quitting apps, logging out other users, restarting, zapping PRAM/SMC, etc) did nothing, then I remembered I had installed Chrome a while back to test a website.
I deleted Chrome, and noticed Keystone while deleting some of Chrome's other preferences and caches. I deleted everything from Google I could find, restarted the computer, and it was like night-and-day.
Everything was instantly and noticeably faster, and WindowServer CPU was well under 10% again.
Then something else hit me, my family had been complaining about the sluggish performance of a 2015 iMac since practically the day we bought it. I had tried everything I could think of – it had a Fusion drive and the symptoms were consistent with a failing SSD – but drive diagnostics always turned up nothing. We even went as far as to completely wipe and set up the computer fresh multiple times.
Yeah, I realize this sounds like a freakin' infomercial, but it worked so well I spent a whole $5 on a domain name and set up this website even if it makes me sound like a raving nut.
OK that's weird, how do you delete Chrome and Keystone?
(Update 12/15/2020, the good people at Google on the Chromium team are taking this seriously, if you're technically inclined and can contribute samples please see
this thread
– direct link to the
crbug 1158402
.)
Go to your
/Applications
folder and drag
Chrome
to the Trash.
In the
Finder
click the
Go
menu (at the top of the screen), then click "
Go to Folder...
".
Type in
/Library
and hit enter.
Check the following folders:
LaunchAgents
,
LaunchDaemons
,
Application Support
,
Caches
,
Preferences
.
Delete all the
Google
folders, and anything else that starts with
com.google...
and
com.google.keystone...
Go to "
Go to Folder...
" again.
Type in
~/Library
and hit enter.
(Note the "~")
Check the following folders:
LaunchAgents
,
Application Support
,
Caches
,
Preferences
.
Delete all the
Google
folders, and anything else that starts with
com.google...
and
com.google.keystone...
Empty the Trash, and restart your computer.
Now what browser should I use?
Safari
is good and it's already on your Mac. It's fast and efficient. If you want something WebKit-based with more features,
Orion
might be a good fit. If you need a Chromium-based browser, try
Brave
,
Opera
, or
Vivaldi
.
(Brave and Vivaldi both use an open source library called
Sparkle
for updates which makes an issue like this impossible.)
What's the deal with Keystone anyway?
Wired first
reported on Keystone in 2009
, when Google put it into Google Earth. It has a long history of crashing Macs by doing bizarre things that shouldn't be necessary for auto-update software to function.
To all the good people at Google who work on Chrome: something is going on between the code you're writing and what is happening on people's computers. I hope you can track it down and give us an honest postmortem.
Update 12/15/2020:
Collected anecdotes:
https://twitter.com/lorenb/timelines/1338892756752732169
FAQ
Just restarting probably fixed it.
No, the issue persists across restarts, no indexing/applications running, etc, and is otherwise completely unexplained. Nothing obvious appears in Activity Monitor, and many people have meticulously tried to troubleshoot to no avail (obviously including restarting), and the only thing that
immediately and conclusively
addressed the issue was removing Chrome & Keystone.
It’s the observer effect.
Sure, Activity Monitor activity itself uses CPU, so just looking for the issue might show slightly elevated WindowServer activity. That is not what is happening here. The magnitude of the issue is enormous, WindowServer CPU thrashing dwarfs whatever Activity Monitor itself is doing
(no, using 'top' doesn't make an appreciable difference)
. For many people actually measuring the difference quantitatively is irrelevant (though helpful) since it’s so immediately obvious what the problem was through vastly improved responsiveness, battery usage, fan noise, etc.
This is a placebo!
The issue isn't subtle, and the improvement is immediate, obvious, and testable. Please see above.
Hiding from Activity Monitor?! Inconceivable!
(The original version of this page implied that keystone itself was hiding from Activity Monitor, my bad for the imprecise langauge.)
Correct, the
keystone/updater process itself
doesn’t hide itself from Activity Monitor, it briefly shows up and disappears on schedule. That is not the issue. It is causing something else on the system to consume massive CPU that leaves no indication that Chrome/Keystone are in fact the culprits.
Sure, the spectrum of plausible theories here varies, anywhere from an exploit trampolining through keystone, then code injecting WindowServer (unlikely, and insane if true... my gut says this issue is old, but still happens post-hardening) to Google abusing system apis (more likely) to a bug in the OS that Google didn’t rigorously test against (very possible).
I wouldn't ascribe this to malice on Google's part.
I agree, I personally believe the Chrome engineers and PMs who claim not to know about the issue. That said, Google took on the responsibility of architecting an updater in a brittle and dangerous way when better / simpler alternatives existed. Good engineering would make a problem like this
structurally impossible
.
If not malice, hubris, disparaging skepticism (“works on my machine”), apathy, and poor organizational prioritization would explain it.
You didn’t prove anything.
True.
(12/18/2020: The original version of this page was written in haste but uncovered a real and systemic issue, that — had it affected someone else — may have been written off completely.)
This is going to be like proving whether smoking causes cancer. But whatever it is absolutely trashed my computers (along with
many others
), and was fixed decisively after deleting Chrome & Keystone when nothing else worked.
On some level, the burden of proof lies with Google to explain their architectual decisions since there is no technical reason for Chrome/keystone to run a persistent daemon even for people who don't use Chrome often, just to facilitate auto-updating (which, for browsers, is a good idea) when better solutions exist.
