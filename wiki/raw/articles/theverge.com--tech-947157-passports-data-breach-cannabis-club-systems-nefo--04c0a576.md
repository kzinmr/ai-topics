---
title: "Nearly a million passports and photo IDs were left unprotected on the public internet"
url: "https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal?view_token=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjdjV0Y5TTBuM0ciLCJwIjoiL3RlY2gvOTQ3MTU3L3Bhc3Nwb3J0cy1kYXRhLWJyZWFjaC1jYW5uYWJpcy1jbHViLXN5c3RlbXMtbmVmb3MtcHVmZnBhbCIsImV4cCI6MTc4MzA5NDY0NiwiaWF0IjoxNzgyNjYyNjQ2fQ.7SjX6B8AAGhzsdrtD5asJWBwzQvTDUD31hWte7K1oec"
fetched_at: 2026-06-29T07:00:45.463012+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Nearly a million passports and photo IDs were left unprotected on the public internet

Source: https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal?view_token=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjdjV0Y5TTBuM0ciLCJwIjoiL3RlY2gvOTQ3MTU3L3Bhc3Nwb3J0cy1kYXRhLWJyZWFjaC1jYW5uYWJpcy1jbHViLXN5c3RlbXMtbmVmb3MtcHVmZnBhbCIsImV4cCI6MTc4MzA5NDY0NiwiaWF0IjoxNzgyNjYyNjQ2fQ.7SjX6B8AAGhzsdrtD5asJWBwzQvTDUD31hWte7K1oec

Typing a few letters and numbers into my web browser, I find myself gaping at the identity documents of complete strangers. The passport of a young woman from Germany. The passport of a man from Spain with glasses resting on his head. The front and back of another man’s driver’s license, a stereotypically goofy expression on his face.
They were all sitting unprotected at public URLs, with no password or access control of any sort. If I sent you a link, you could have looked at someone’s passport.
“We have to do something about it as fast as possible, because people will find this and resell it. It will do damage,” Sammy Azdoufal told me in May.
Azdoufal is the security researcher who used Claude Code to help discover that
every DJI Romo robot vacuum cleaner
and
a million baby monitors and security cameras
were embarrassingly easy to hack. This time, he says he discovered over 985,000 photo IDs sitting on the public internet for any half-decent hacker to steal.
If you’ve visited a cannabis club in Spain, Azdoufal says, chances are your photo ID was among them — and possibly your phone number, address, your favorite strains of cannabis, and how much you consumed each month while there. Azdoufal says celebrities are in the database, too, and visitors from all over the world, including 30,000 from the United States. “They have famous people,” says Azdoufal. “People who don’t want everyone to know they smoke weed.”
Here’s a rough summary of the user base that Azdoufal’s automated tool was able to see and the names of some of the clubs:
It’s not the clubs that didn’t protect these identity documents. An Irish company called Cannabis Club Systems (CCS), formally Nefos Solutions, develops and provides the software these clubs use for sales, accounting, and admissions, including a verification system where receptionists upload your IDs and selfies to Nefos’ cloud.
Traditionally, you’d need to provide a photo ID every time you wanted to get into a club. But with the verification system, the receptionist can pull up your stored identity documents and check if your face matches. There’s also an optional app called PuffPal that lets clubs scan a QR code for faster entry.
But when Azdoufal decompiled that PuffPal app,
he explains in his report
, he discovered that Nefos had no meaningful level of security. He discovered a secret key for the Stripe payments platform sitting inside the app in plain text. He discovered he could pull up any member’s profile just by changing one number. If those profiles included their phone number, home address, passport, and weed preferences, he now had access to them too.
And then, he discovered that those passports, drivers licenses, and photo IDs were stored at public URLs as simple as this: https://ccsnubev2.com/v8/images/_{club}/ID/{user_id}-front.jpg
Those clubs were uploading 5,000 new photo IDs with these insecure URLs every day, Azdoufal tells me.
He also found an admin portal accessible via the public internet — and that the cannabis clubs had a trivial level of security on their own accounts, using passwords that could theoretically be cracked in minutes with a modern GPU. Private chat messages between clubs and members through the PuffPal app were also vulnerable.
The good news: Roughly a month after we reached out to Nefos, the company seems to finally be taking meaningful action. The company says it’s shutting down its entire PuffPal system and vulnerable APIs until they can be fixed — in Azdoufal’s latest tests on June 10th, passport images and personal data seem to be secure. Nefos has also informed local authorities and says it will take responsibility to make fixes, pay fines, and tell users what happened.
In a phone interview, Nefos cofounder Andreas Nilsen tells
The Verge
that he’s in touch with Ireland’s Data Protection Commission (DPC) about the data breach — a fact that DPC spokesperson Evan O’Leary confirmed to us by email. “We have to communicate to everyone that was potentially exposed,” Nilsen tells me, saying he hopes the DPC can show his company how to do that properly. Nilsen claims there’s currently no evidence that any outsider accessed the data other than Azdoufal.
But it took far too long for Nefos to take the threat seriously. It took five days and the threat of a story before the company replied to us, long after Azdoufal reached out. Then, Nefos began by papering over the holes instead of risking business.
I was prepared to write this story at the beginning of June, after Azdoufal told me Nefos had finally locked down the passport images. But on June 4th, I surprised Azdoufal by showing him that his very own passport was online once again, without any protection.
That’s because Nefos had not yet stopped cannabis clubs from using the PuffPal app, and clubs were complaining the locked-down images weren’t showing up the way they used to — so Nefos simply unlocked the images again. While Nilsen claims the images were locked down “70 percent of the time” since Azdoufal and I got in touch, it’s pretty clear that Nefos made a decision to prioritize its customers instead of the threat.
On June 9th, Azdoufal discovered that even though Nefos had locked down the passport images and photo IDs with tokens,
everything else
in the user profiles was still easily accessible: passport numbers, phone numbers, email addresses, home addresses, everything.
All a hacker had to do was type “curl -X POST https://ccsnubev2.com/v8/api/userProfile.php -d “user_id=[NUMBER]&[CLUB NAME]=test&language=en” into a command line, and the servers would freely give up a ream of personal information. After we brought this to Nefos’ attention, that hole, too, has been closed.
But how could the company be so careless? “I don’t want to put the blame on others because at the end of the day it resides with us,” Nilsen says. But he does point the finger
at 9Series
, an outsourcing firm he claims was responsible for developing the PuffPal app and creating all the vulnerable APIs it used to pull unprotected data from Nefos’ user database. (9Series did not have a response by publish time.)
Now that PuffPal is down, Nefos is emailing every club to let them know their members won’t be able to use those QR codes for entry — but they can still pull up IDs from Nefos’ servers after scanning a member’s RFID card or typing in their phone number, among other examples.
Nilsen claims his company will not simply relaunch unsecured PuffPal if the clubs ask. “We’re going to tell them we can’t,” he says. “We will make sure, after this debacle, that this is verified by an independent security researcher and guarantee that this is 100 percent secure.” He says Nefos is parting ways with 9Series and hopes to have a new app within a few months.
Nilsen says he’s aware that
under EU law
, his company legally had to disclose the breach within 72 hours or pay significant fines, something the company didn’t do
.
“I’m sure we’ll get whatever kind of penalty there is,” Nilsen says.
Just last month, a website called the UK Visa Portal
similarly exposed at least 100,000 passports
to anyone who could guess a URL. Let’s hope this is a wakeup call.
Follow topics and authors
from this story to see more like this in your personalized homepage feed and to receive email updates.
Sean Hollister
Report
Security
Tech
