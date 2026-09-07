---
title: "The purpose of DNS is to spread scams"
url: "https://shkspr.mobi/blog/2026/09/the-purpose-of-dns-is-to-spread-scams/"
fetched_at: 2026-09-07T10:01:45.920638+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# The purpose of DNS is to spread scams

Source: https://shkspr.mobi/blog/2026/09/the-purpose-of-dns-is-to-spread-scams/

I imagine everyone here has received an unsolicited message telling them that their tax is overdue and that they urgently need to visit Genuine-Tax-Payment-Website.fart or that a parcel is delayed at customs and you can pay a small sum for its release at Almost-The-Right-Acronym.ak
You know it is a scam. Most people just mark as spam and move on with their day. But a significant number of people don't. They hastily visit the site, tap in their credit card details, give it their mother's maiden name, confirm address, upload a nude selfie, and only then realise that they've been had.
The Internet works at pretty close to the speed of light. You can register a .uk domain and a minute later it's accessible from the other side of the planet. Brilliant for users who want to quickly launch a website. Also brilliant for abusers who want to launch a spam campaign.
By the time enough people have reported the scammers' domain as suspicious, it is too late. In the time it takes for a registrar to disable the domain, or for its name to make its way to the
Safe Browsing List
, a million messages have already been sent and enough people have handed over their details.
We're told that "
the purpose of a system is what it does
". At the moment, the Domain Name System's purpose seems to be a vector for criminals to run scams on people at a terrifyingly high rate.
BIG!
There's a great blog post by Andrew Campling which reports on this startling claim:
The study found that at least 10% of all new gTLD domain names registered during the year had subsequently appeared on security blocklists by the time of analysis. It estimated that, taking account of subsequent blocklisting and associated domains not themselves blocklisted, the share of names registered by malicious actors
may be closer to 20%
.
DNS Abuse and Criminal Infrastructure: Beyond Definitions and Blocklists
(emphasis added)
That links to a presentation by Interisle which contains some rather shocking statistics (
albeit with disputed methodology
). It looks at
generic
Top Level Domains (gTLD) - those are things like .com and .fun rather than country code TLDs (ccTLD) like .uk and .de.
It says 85 million new registrations of gTLDs were made in 2025. Of those 8.5 million were added to blocklists by May 2025. It reckons that a 10% abuse rate is the likely floor for these numbers and it's probably closer to 20%. One in five newly registered domains with a gTLD are scams. That's a bloody crisis.
13 TLDs had more than 50% of their registrations blocklisted.
I can understand why .bid and .loan are popular with scammers. But why .mobi?! What did I ever do to you, eh?
Who are the scammers registering these through?
Ah, our old friends at NameCheap. See
Why do scammers love NameCheap?
If those five registrars had more effective policies, it might significantly dent the scammers' ability to ply their devious wares. Or they might just move on to other registrars.
As the report points out:
suspension rates for blocklisted domains were 7.4% to 16.3%.
The full report is on the Interisle website
.
I don't know.
In the first instance, it might make sense for registrars to do strong Know Your Customer (KYC) checks on anyone buying a domain. But that stops anyone who wants to anonymously register
I-Hate-Nintendo.whatever
without risking the wrath of Intellectual Property lawyers.
Also, criminals have access to stolen money and stolen cards. They can convince a hapless mule to register a domain on the criminals' behalf.
Registrars could ask for an escrow payment. Pay €9 for the domain name put €900 in escrow. If your domain appears on a blocklist within the year, you forfeit the money. Criminals with stolen funds are unlikely to care but it would probably put off lots of people from getting a new domain.
There are various banned words and phrases depending on the TLD. For example,
South Sudan
has a list of political words which they don't want associated with their .ss ccTLD.
But if one gTLD bans a word, a different one might not. A scammer doesn't care if the gTLD is .arse or .elbow - they just want the start of the domain to look legitimate.
Some registrars have strings that they don't allow. In fairness to NameCheap, when I tried to register
dwp-payments-gov-uk.pizza
it told me that domain was banned. It wouldn't let me get any gTLD with that name.
But all it takes is one registrar to be slightly lax and the scammers get through. Increasing the complexity of the rules is also a hell of a burden on smaller registrars.
Besides, it's pretty easy to get a generic enough looking domain and stick the confusing bit on a subdomain. Here are a clutch mentioned in the report:
https://gov.uk-dwpaph.bond/uk/
https://gov.uk-dwpcjh.bond/uk/
https://gov.uk-dwpclc.bond/uk
https://gov.uk-dwpclw.bond/uk
https://gov.uk-dwpclj.bond/uk/
Perhaps there ought to be a delay before a new domain goes live to allow people to object to it? That would give governments, banks, delivery companies, and a dozen more "important" organisations a right to veto any "dodgy" looking domain.
But suppose someone wants to register
gov-uk-stole-my-horse.horse
to protest the government's cruel policy of stealing horses - is that a legitimate use of a domain? What if the Darwin Pensioner Divas - a group of elderly singers - want to take payments for their new album of goth/punk covers, can the DPD delivery company veto
dpd-payments.music
?
Do we want a domain name system where powerful companies control exactly which domains we can register? If I have an idea for a domain on a Friday night do I have to wait until Monday before it can be launched? Are those companies realistically able to parse millions of domains per year and have a low false-positive rate?
All of these things are possible - but all of them come with an impact on legitimate users. To be clear, I don't know what the right answer is.
Lots! It has been a few years since I've been to an ICANN meeting, but even back then the topic of abuse was high on the agenda. They appear to be looking at ways to coordinate abuse reports between various entities, along with some other policies which should hopefully work.
There are two salient points from
one of the discussions held at the recent meeting
If anybody thinks that in our current age of AI and as we move into different kinds of computing, DNS abuse is going to numerically stay steady and we will have a downward effect on that baseline 2027 number. I'm not sure that that's an accurate assumption. I think it's going to be the other thing, which is […] it's going to be easier to abuse the DNS.
And
Abusers are going to abuse because it's just too lucrative, because no matter what we do, they will find the way to make profit off of that, and will try to circumvent everything that we do. That is not a reason not to do it, though.
Quite!
As I said, I don't know the answer to this. What I do know is, much like
Android's app ecosystem being a haven for scammers
, DNS is facing a crisis. When trust in a system goes, only chaos follows.
I don't want to live in a world where I have to show my passport and pay thousands of pounds to register a domain which is only available after being vetted by private interests. But I also don't want to live in a world where scammers have effectively no deterrent from abusing millions of people.
The purpose of a system is what it does. I hope DNS's purpose can become less dangerous while still remaining open.
