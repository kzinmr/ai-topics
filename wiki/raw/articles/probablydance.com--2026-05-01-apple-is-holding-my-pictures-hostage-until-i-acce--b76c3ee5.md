---
title: "Apple is Holding my Pictures Hostage Until I Accept Their New Terms of Service"
url: "https://probablydance.com/2026/05/01/apple-is-holding-my-pictures-hostage-until-i-accept-their-new-terms-of-service/"
fetched_at: 2026-05-05T07:01:25.359630+00:00
source: "Malte Skarupke (Probably Dance)"
tags: [blog, raw]
---

# Apple is Holding my Pictures Hostage Until I Accept Their New Terms of Service

Source: https://probablydance.com/2026/05/01/apple-is-holding-my-pictures-hostage-until-i-accept-their-new-terms-of-service/

It started off a few months ago, when my iPad suddenly couldn’t play videos any more that it had recorded. It would show the first frame, but hitting the play button wouldn’t do anything. I googled around but couldn’t find anything. I had recently installed an update, so I figured I’ll just wait for the next update to fix things.
VIDEO
But the next update didn’t fix things, and it turns out the reason is actually a little dystopian: Apple has deleted my local copies of my videos and will only give them back if I sign their new terms of service.
You may have noticed that the preview pictures in the video above are often blurry. Soon after this, the pictures on my iPad also started looking oddly blurry. Eventually we noticed a little info icon next to the pictures that, when tapped, says “Unable to Load Photo. An error occured while loading a higher quality version of this photo.”
What is it talking about? Why would the thumbnail load but the full picture doesn’t? But at least this is a message I can google for. I need to change the “iCloud -> Photos” settings to “Download and Keep Originals.”
I never paid for Apple’s iCloud service so I am a little surprised that not only were my pictures uploaded, the local copy was deleted. Here is a picture of the storage in my iPad:
See that yellow bar for “Photos”? It’s almost not there because my local photos were almost all deleted.
This scared me. I knew I should have backed these up… Google said I should go to the “iCloud” settings but those are grayed out, untappable:
Since I never paid for iCloud, this is not too surprising, but what do I do now? I start by installing updates. That doesn’t help, but eventually I find the right spot:
So I agreed to the new terms of service. And as soon as I do, my videos are back. I immediately turn on the setting to keep a local copy of all my photos and videos.
Are they Allowed to Do this?
I obviously didn’t read the new terms of service before accepting them. They’re long. I asked Claude if they say anything about holding my pictures hostage, but there is no clear sentence saying they can withhold the content when they update their terms of service. They only say that they can
change the terms of service with 30 days notice (Section I.E, “Changing the Service”)
terminate my service if I violate the agreement (Section VII.B, “Termination by Apple”)
ban me if my use of the service “intentionally or unintentionally threatens Apple’s ability to provide the Service” (Section I.C, “Limitations on Use”)
take “steps” they believe are “reasonably necessary or appropriate” to enforce compliance with any part of the agreement. (Section V.E, “Access to Account and Content”)
may remove the service “for indefinite periods of time”, or cancel the service “in accordance with the terms of this agreement” (Section IX, “DISCLAIMER OF WARRANTIES; LIMITATION OF LIABILITY”)
Number 1 happened, they didn’t do number 2 or number 3 here. Number 4 might apply superficially, because they want to force me to sign the new agreement, but I didn’t break any terms of the version of the agreement that I actually agreed to. But maybe none of that actually matters because number 5 says they are free to not provide the service anyway. But on the other hand “in accordance with the terms of the agreement” should mean that they’re limited by the previous terms (though I’m not a lawyer).
So neither Claude nor me sees anything here that says they can block access to my videos until I sign the new terms of service. In particular the “Access to Account or Content” section is really weak, which makes me think they’re not allowed to block me from my own videos.
In theory.
In practice I signed the new agreement like everyone else, because what’s supposed to happen if they do something that they’re not allowed to do according to their own agreement? That’s just how this works. The agreement limits me, not them.
So What Evil Thing Happened Here?
It’s hard to say which act exactly led to this dystopian setting where a company can make a copy of your picture, delete the originals, put a new agreement in front of you, and force you to agree to it in order to get your pictures back. But what exactly is the evil thing? Every individual step was not so bad:
They upload the pictures to iCloud even though I didn’t sign up.
They always give you 5GB for free so might as well use them to have a backup of your photos. That’s probably a good thing to do, because people (like me) are irresponsible and don’t do backups on their own.
They delete local pictures by default.
This is probably very useful for people who have lots of online storage, more than they have space on their iPad.
They don’t allow you to use iCloud if you don’t agree to the new Terms of Service.
What else are you supposed to do? According to their own agreement they probably have to still provide access to the pictures, but that seems hard.
Repeatedly force you to agree to new Terms of Service that are too long for any sane person to read
South Park did an episode about this, but the new terms of service are probably not bad and they probably made changes for a reason.
Ship a locked down device where you can’t run arbitrary software and regularly have to install updates and which automatically does weird things like the above.
Yeah there’s definitely a bit of “Stallman was right” here. In particular I probably would have done backups already if I could run my normal backup software on there. But that’s a terminal app and I don’t think I can ssh onto an iPad.
I don’t know. None of these are really evil. I can see good people doing these things for not bad reasons. And nothing really bad happened here. I just had to tap “I Agree” to some agreement that I didn’t read. But it sure doesn’t feel good. I thought you’d at least get a warning before buying the device: “This device may delete your pictures. We’ll make a copy and promise to give them back as long as you agree to all future terms of service.”
Also what’s the lesson for me personally, if I want to not be evil? Which of the above things should I refuse to do? Every individual step isn’t so bad. I guess you have to notice the patterns, notice when other people think what you’re doing is bad (FSF, South Park), and then actually take that seriously, not just dismiss it…
And what should Apple do? Obviously they should allow access to the pictures and videos even if I haven’t signed the new agreement. That small step would move them from “dystopian” back into good territory. But I do notice that they have already walked into a part of the good territory where it’s very narrow and small missteps move you into bad areas…
Will this change my behavior in any way? I already don’t buy most apple products, precisely for the “walled garden” reason. I have this iPad and that’s it. I’ll try to not buy more.
