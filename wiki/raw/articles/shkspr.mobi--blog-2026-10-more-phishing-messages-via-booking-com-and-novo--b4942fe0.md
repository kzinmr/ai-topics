---
title: "More phishing messages via Booking.com and Novotel"
url: "https://shkspr.mobi/blog/2026/10/more-phishing-messages-via-booking-com-and-novotel/"
fetched_at: 2026-10-24T10:00:50.909251+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# More phishing messages via Booking.com and Novotel

Source: https://shkspr.mobi/blog/2026/10/more-phishing-messages-via-booking-com-and-novotel/

A few days ago I booked a Novotel hotel on Booking.com - two days later I received these phishing messages via WhatsApp. Both knew my exact name, phone number, location of stay, and date of stay.
Luckily, both were fairly inept. Let's take a quick look at them.
The first came from a Portuguese business account.
Obviously the name doesn't match that of the large chain hotel I booked with. The domain name doesn't look anything like what I'd expect from either Booking.com or Novotel. They note this isn't an emergency - presumably to bypass the warnings that you shouldn't act on any message trying to convey a sense of urgency. The "Cancel" button on the bottom makes this look more genuine though.
The second one is slightly different.
This is from a much more generic business account, albeit a UK-based one. The date is formatted differently. There's no cancel button. But the wording is identical.
So are these both from the
same
scammer?
The domains were both registered on the same day - the 21st of October - within hours of each other. They're both protected by CloudFlare, but were registered at two different registrars - one Chinese and one Japanese. Lots of scammers use CloudFlare (who seem to relish in being the protectors of all sorts of unsavoury characters). A smart scammer would register their domains on multiple registrars to avoid all of them getting banned at once. So that's a bit inconclusive.
Looking at the source code for the pages, they appear to be identical.
That means one of two things:
There is one incompetent scammer who doesn't keep a record of which messages they've sent to which victims.
There are multiple scammers who are all using the same "off the shelf" phishing kit.
But how did my data leak in the first place?
The first place to look, as always, is within. My Booking.com account uses a strong and unique password. It has a unique email address tied to it. I have MFA via an authenticator app. I regularly use the "Sign out of other sessions" options in the Booking.com app.
My email is similarly secure. And, frankly, if scammers were in there then they could do a lot more damage than sending me a phishing link!
That leaves either Booking.com, Novotel, or one of their systems.
It's fair to say this is a
persistent
problem with Booking.com - they were
breached in 2023
and these sorts of phishing attacks
happen regularly
.
Although I couldn't find any record of Accor (the owners of Novotel) being breached, it's fair to say
other hotels suffer from this problem
. It seems depressingly easy to con or bribe a worker into allowing scammers access into a booking system.
This sort of "
reservation hijacking
" is now depressingly common.
There's a slight twist in the tale. A few moments after I made the original reservation, I received this message directly from the hotel via the Booking.com messaging system:
I can only assume that Novotel are aware of the persistent problem they're facing and this is their attempt to deflect blame.
So I called the hotel (using the number on their website) and they confirmed my reservation. When I mentioned the phishing messages the hotel were very quick to tell me they were a scam, that I shouldn't click any links, and to delete them right away. I did ask if they'd suffered a data breach but, understandably, they don't tell receptionists that.
I've reported the problem to both Accor and Booking.com - we'll see who comes up with the most convincing explanation.
As it happens, a few days ago, the
European Commission announced it was investigating Booking.com
:
The Commission will also investigate whether the provider of Booking.com has diligently assessed and addressed the risks that phishing scams pose to consumers.
In particular, the investigation will focus on risks related to the way reservation and guest data is shared with accommodation providers, and the design and functioning of Booking.com's messaging service.
The Commission will also examine whether the company has put in place sufficient safeguards to prevent data from being misused to carry out phishing and solicit fraudulent payments.
Stay safe out there!
