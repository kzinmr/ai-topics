---
title: "1,000 Data Breaches Later, the Disclosure Lag is Worse Than Ever"
url: "https://www.troyhunt.com/1000-data-breaches-later-the-disclosure-lag-is-worse-than-ever/"
fetched_at: 2026-06-02T07:05:04.636070+00:00
source: "troyhunt.com"
tags: [blog, raw]
---

# 1,000 Data Breaches Later, the Disclosure Lag is Worse Than Ever

Source: https://www.troyhunt.com/1000-data-breaches-later-the-disclosure-lag-is-worse-than-ever/

Today, I loaded the 1,000th data breach into
Have I Been Pwned
. Reflecting on that milestone number, I pondered how to mark the occasion in writing, and what immediately came to mind was a very simple question: why is it still needed? Especially considering the emergence of privacy regulations such as GDPR and CCPA in the 12 and a half years since I started HIBP, what possible purpose does it still serve? The title kinda gives the answer away, and the big number we hit today coincided with another pattern that makes everything worse: increasingly long lag times for disclosure.
This is all going to be anecdotal, and as far as I know, there are no hard numbers for me to cite, but the evidence is everywhere. Here's what I mean:
That was the 24th of April, five days after
news of the incident had broken
. Given ShinyHunters' MO, Carnival would have known about the breach many days before they ratcheted up extortion pressure by announcing the impending leak on their website. The subsequent leak on the 24th was very public: an announcement was posted to the group's dark-web site, the data itself was published to their
clear-web
site, and industry commentary followed:
Per that last post, the data was then reposted to all sorts of other places: hacking forums, Telegram channels, and who knows how many other, more private locations. The point is that it spread quickly, extensively, and, without any shadow of a doubt, Carnival were aware of this.
They then told people about it on the 27th... of May
. According to
their press release that same day
, this was 43 days after learning about the incident. For more than 6 weeks, data breach victims whose names, dates of birth, email addresses, loyalty program details and, of course, their association with Carnival leaked to the public en masse had absolutely no idea of their exposure. And if they asked Carnival about it? Well:
So, why the delay?
Last week's press coverage
may give some insight:
thorough and time-consuming analysis of the impacted data
Often, the reason I hear for disclosure lag is "we needed to fully assess the scope of exposed data before notifying people". The issue I have with this position is that it implies that even an early heads-up can't happen until there's a very comprehensive understanding of the impact. There are many things that take time to establish after a data breach: the jurisdiction each individual sits in, the precise data that was exposed about them and additional information that may be buried in terabytes of exfiltrated data in all sorts of different formats. But pulling out email addresses and sending early notification is
very
easy - I've literally done it a thousand times now.
This isn't just a Carnival issue; in fact, it was off the back of this next one only a few days later that I was prompted to write this post:
FFS. 45 days. Even worse than Carnival. And like Carnival,
very
broadly distributed and easily accessible by the masses, including HIBP:
I have a working theory that the disclosure lag is worsening in part due to the proliferation of class actions
immediately
following a breach. In my live stream last weekend, I did a quick search for the DentaQuest breach:
Three of the first four results are all for class actions related to the breach, and there are two more class action results a little further down the page.
I've been raising concerns about the adverse impact of class actions for many years now
, and it's worse than I've ever seen. By a big margin, too.
It's not just me observing how the behaviour of these orgs appears to be influenced by how lawyers will respond, either. Have a read of this post from
Roby Joyce
(check out his bio if you don't already know why he's worth paying attention to) after he learned about his exposure in the ZenBusiness breach via HIBP:
What especially caught my eye was this sentence:
That is not a customer-protection posture. That is a litigation posture.
This isn't about prioritising the customer, it's about protecting the organisation. I don't think most people understand that organisational accountability really lies with their shareholders, first and foremost. All the pleasantries around "customers are our number one priority" and "we take security seriously" are all secondary to shareholder happiness, and minimising the chances of getting their arses sued into oblivion is a big part of that.
Rob's quoted comment above came immediately after the response he received from ZenBusiness after asking them about the incident:
If we determine that an incident resulted in the exposure of your protected PII, we will provide notice as legally required
Which brings me to the next problem as it relates to disclosure lag: it may be infinite. By which I mean you may
never
be told. Ever. GDPR allows it. CCPA allows it. Whatever your local privacy regulation acronym is also allows it. A couple of years ago, I wrote about
the data breach disclosure conundrum
, where I explained how privacy regs have very specific carve-outs around the circumstances under which data breach victims must be notified. For example:
If the breach is likely to result in a
high risk of adversely affecting individuals’ rights and freedoms
, you must also inform those individuals without undue delay.
That's in the UK, here's our carve-out in Australia:
Under the Notifiable Data Breaches scheme, an organisation or agency that must comply with Australian privacy law has to tell you if a data breach is
likely to cause you serious harm
You see the loophole, right? As far as I know, ZenBusiness still hasn't contacted any individual victims. And like Carnival and Zara, their data is all over the place. Same with Charter, which was in the press last week, where
they were quoted as saying the following
:
No sensitive personal information (PI) or customer proprietary network information (CPNI) data was exfiltrated by the threat actor as a result of recent activity
I'm not aware of any disclosure they've made to individuals, but to use Rob's term, that sentence reads like legal posturing to me. It's technically correct, of course: there are very clear definitions for sensitive PII, for example, under
California's CCPA
:
a specific subset of personal information that includes certain government identifiers (such as social security numbers); an account log-in, financial account, debit card, or credit card number with any required security code, password, or credentials allowing access to an account; precise geolocation; contents of mail, email, and text messages; genetic data; biometric information processed to identify a consumer; information concerning a consumer’s health, sex life, or sexual orientation; or information about racial or ethnic origin, religious or philosophical beliefs, or union membership.
GDPR has a similar definition for "
special categories of personal data
":
personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, and the processing of genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health or data concerning a natural person’s sex life or sexual orientation
In other words, none of this applies to any of the ShinyHunters breaches in the examples I've been providing above.
I've been in many meetings with breached companies over the years where they're obviously aiming to skirt around disclosure obligations. Clearly, these obligations aren't
legal
ones, but I will argue they're
social
ones. We expect to be notified when our data is leaked, and we believe organisations should be required to inform us. Therein lies the gap.
I'll finish by recognising that every organisation I've referred to here, and indeed every one I've loaded into HIBP, has been the victim of a criminal act. I'm especially sympathetic to those who've been the target of an aggressive extortion campaign, and I know it's been an absolute nightmare for the folks in those companies who've been left to clean up the mess. However... here we are. Clearly, their goals are misaligned with ours regarding breach disclosure, and that's why, 1,000 breaches later, HIBP still exists.
