---
title: "Untitled"
url: "https://matduggan.com/you-can-absolutely-have-an-rss-dependent-website-in-2026/"
fetched_at: 2026-04-28T07:02:34.775545+00:00
source: "matduggan.com"
tags: [blog, raw]
---

# Untitled

Source: https://matduggan.com/you-can-absolutely-have-an-rss-dependent-website-in-2026/

I write stuff here. Sometimes the stuff is good. Sometimes it reads like I wrote it at 2 AM after an argument with a YAML file, which is because I did. But one decision I made early on was that I didn't want to offer an email newsletter.
Part of this was simple economics. At one point I did have a Subscribe button up, and enough people clicked it that the cost of actually sending those emails started to resemble a real bill. Sending thousands of emails when you have no ads, no sponsors, and no monetization strategy beyond "I guess people will just... read it?" doesn't make a lot of financial sense.
But the bigger reason — the one I actually care about — is that I didn't want a database full of email addresses sitting under my control if I could possibly avoid it. There's a particular flavor of anxiety that comes with being the custodian of other people's personal data, a low-grade dread not unlike realizing you've been entrusted with someone's elderly cat for two weeks and the cat has a medical condition. I can't lose data I don't have. I never need to lie awake wondering whether some user is reusing their bank password to log into my website just to manage their subscription preferences. The best way I can safeguard user data is by never having any in the first place. It's not a security strategy you'll find in any textbook, but it is airtight.
Now, when I explained this philosophy to people who run similar websites, the reaction was — and I'm being generous here —
warm laughter
. The kind of laughter you get when you ask if an apartment in Copenhagen is under $1,000,000. Email newsletters are the only way to run a site like this, they said. RSS is dead, they said. You might as well be distributing your writing via carrier pigeon or community bulletin board. One person looked at me the way you'd look at someone who just announced they were going to navigate cross-country using only a paper atlas. Not angry. Just sad.
I'm lucky in that I'm not trying to get anyone to pay me to come here. If I were, the math would probably change. I'd be out there A/B testing subject lines and agonizing over open rates like everyone else, slowly losing pieces of my soul in a spreadsheet. But if your question is simply, "Can I make a hobbyist website that actual humans will find and read without an email newsletter?" — the answer is a resounding yes. And I have the logs to prove it.
Stats
All of this is from Nginx access.log.
===========================================
 Traffic Source Breakdown (Current Log)
===========================================

Total Filtered Requests:  49089

  RSS/Feed Traffic:            24750  (50.42%)
  Homepage Traffic:             1534  (3.12%)
  Other Traffic:               22805  (46.46%)
These logs get rotated daily and don't include the majority of requests that hit the Cloudflare cache before they ever reach my server, so the real numbers are higher. But I think they're reasonably representative of the overall shape of things. About half my traffic is readers hitting
/feed
or
/rss
— people who have, of their own free will, pointed an RSS reader at my site and said
yes, tell me when this person has opinions again
. The other half are arriving via a specific link they stumbled across somewhere in the wild.
If we do a deeper dive into that specific RSS traffic, we learn a few interesting things.
The user-agent breakdown shows the usual suspects — the RSS readers you'd expect, the ones that have been around long enough to have their own Wikipedia articles. There are also some abusers in the metrics. I have no idea what "Daily-AI-Morning" is, but whatever it's doing, it's polling my feed with the frantic energy of someone refreshing a package tracking page on delivery day.
The time distribution, though, is pretty good — spread out across the day in a way that suggests real humans checking their feeds at real human intervals, rather than a single bot hammering me every thirty seconds.
My conclusion is this: if you want to run a website that relies primarily on RSS instead of email newsletters, you absolutely can. The list of RSS readers hasn't dramatically changed in a long time, which is actually reassuring — it means the ecosystem is stable, not dead. The people who use RSS
really
use RSS. They're not trend-chasers. They're the type who still have a working bookmark toolbar. They are, in the best possible sense, your people.
Effectively, if you make your site RSS-friendly and you test it in NetNewsWire, you will — slowly, quietly, without a single "SUBSCRIBE FOR MORE" pop-up — build a real audience of people who actually want to read what you write. No email database required. No passwords to leak. No giant confusing subscription system.
