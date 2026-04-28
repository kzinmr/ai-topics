---
title: "Someone at BrowserStack is Leaking Users’ Email Address"
url: "https://shkspr.mobi/blog/2026/04/someone-at-browserstack-is-leaking-users-email-address/"
fetched_at: 2026-04-28T07:01:48.826084+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Someone at BrowserStack is Leaking Users’ Email Address

Source: https://shkspr.mobi/blog/2026/04/someone-at-browserstack-is-leaking-users-email-address/

Like all good nerds, I generate a unique email address for every service I sign up to. This has several advantages - it allows me to see if a message is legitimately from a service, if a service is hacked the hackers can't go credential stuffing, and I instantly know who leaked my address.
A few weeks ago I signed up for
BrowserStack
as I wanted to join their Open Source programme. I had a few emails back-and-forth with their support team and finally got set up.
A couple of days later I received an email to that email address from someone other than BrowserStack. After a brief discussion, the emailer told me they got my details from Apollo.io.
Naturally, I reached out to Apollo to ask them where they got my details from.
They replied:
Your email address was derived using our proprietary algorithm that leverages publicly accessible information combined with typical corporate email structures (e.g., firstname.lastname@companydomain.com).
Wow! A
proprietary
algorithm, eh? I wonder how much AI it takes to work out "firstname.lastname"????
Obviously, their response was inaccurate. There's no way their magical if-else statement could have derived the specific email I'd used with BrowserStack. I called them out on their bullshit and they replied with:
Your email address came from BrowserStack (browserstack.com) one of our customers who participates in our customer contributor network by sharing their business contacts with the Apollo platform.
The date of collection is 2026-02-25.
So I emailed BrowserStack a simple "Hey guys, what the fuck?"
I love their cheery little "No spam, we promise!"
Despite multiple attempts to contact them, BrowserStack never replied.
Given that this email address was only used with one company, I think there are a few likely possibilities for how Apollo got it.
BrowserStack routinely sell or give away their users' data.
A third-party service used by BrowserStack siphons off information to send to others.
An employee or contractor at BrowserStack is exfiltrating user data and transferring it elsewhere.
There are other, more nefarious, explanations - but I consider that to be unlikely. I suspect it is just the normalisation of the shabby trade in personal information undertaken by entities with no respect for privacy.
But, it turns out, it gets worse. My next blog post reveals how Apollo got my phone number from from a
very
big company.
Be seeing you 👌
