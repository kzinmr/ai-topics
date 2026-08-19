---
title: "And then the men with guns tell you to do it anyway"
url: "https://shkspr.mobi/blog/2026/08/and-then-the-men-with-guns-tell-you-to-do-it-anyway/"
fetched_at: 2026-08-18T10:03:45.058480+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# And then the men with guns tell you to do it anyway

Source: https://shkspr.mobi/blog/2026/08/and-then-the-men-with-guns-tell-you-to-do-it-anyway/

In early February 2011
Egypt was in the middle of a political revolution
. One morning, everyone's phones suddenly pinged with an alert.
The Armed Forces asks Egypt's honest and loyal men to confront the traitors and criminals and protect our people and honour and our precious Egypt.
A
series of messages arrived
all ostensibly from the network provider Vodafone. All pro-regime and all with the undercurrent of violence.
Why did Vodafone send these messages?  Earlier in the week,
all Internet access was cut off
now phones were blasting propaganda to the masses.
After the network went down, Vodafone issued a statement saying:
It has been clear to us that there were no legal or practical options open to Vodafone, or any of the mobile operators in Egypt, but to comply with the demands of the authorities.
Do you have to follow orders? Do you have to obey the law even when it is unjust? Should multinational corporations instruct local executives to be loyal to their parent company or the rulers of the country they live in?
After the messages came in - including promises that "
The Armed Forces cares for your safety and well being and will not resort to using force against this great nation
" - Vodafone Global, safely ensconced in the UK, put out another statement:
Under the emergency powers provisions of the Telecoms Act, the Egyptian authorities can instruct the mobile networks of Mobinil, Etisalat and Vodafone to send messages to the people of Egypt. They have used this since the start of the protests. These messages are not scripted by any of the mobile network operators and we do not have the ability to respond to the authorities on their content.
Vodafone Group has protested to the authorities that the current situation regarding these messages is unacceptable. We have made clear that all messages should be transparent and clearly attributable to the originator.
Statements - Vodafone Egypt
A few years later I was at a networking event chatting to a guy. We'd both previously worked for Vodafone. Me in the UK, he in Egypt. I asked him about the incident - he talked about how they built the SMS infrastructure, what they did to secure it, how they prevented spam, and how one day armed men arrived.
I suspect most of us have seen a movie where some flunky in an office refuses the baddies demands to open the safe, and then gets shot in the head. Perhaps you think that's a noble death? He lived with honour and refused to yield! But, in every movie I've seen, the guy's subordinate opens the safe anyway and gets to live.
But we're technologists, right? We can build fail safes and cryptographic proofs and
simply build infrastructure that can't be abused
.
And then the men with guns come and tell you what to do.
I've written before about
Civic Hygiene
- it's the idea that we should be mindful of the ways that our technologies could be misused. The term was coined back in 2010 by the technologist Bruice Schneier
It's bad civic hygiene to build technologies that could someday be used to facilitate a police state.
But what do we mean by that?
We don't want backdoors in security products - lest hackers break in or evil governments get elected. But we want a way to access our beloved ones' data after they die. It's important that we know that photos haven't been manipulated by propagandists and saboteurs. But we want to send funny memes about that politician we don't like. We don't want police stalking ex girlfriends' cars - but we want dangerous drivers prosecuted.
We want to be alerted about imminent threats, but don't want Governments to use that power for ill.
Way back in the early 2020s, I had a minor role in the UK Government's adoption of
Common Alerting Protocol
the technology which powers cell-broadcast emergency alerts.
Even back then, one of the discussions was around whether the utility of being able to send an unavoidable push notification was worth the risk that someone would send an inappropriate message. Fresh in everyone's minds was the
false alarm saying missiles were heading to Hawaii
.
Too many safeguards means that a genuine alert doesn't get sent in time. Too few safeguards and you can blame "
Human Error
" for any mistakes.
I don't know which safeguards are in place for the UK's system -
and most details are exempt from Freedom of Information requests
. But it is both easy and fun to speculate on how such a system might be designed.
The Government generates an alert. It specifies where and when the alert should be sent. It sends that message to the network operators via a secure and private channel. Perhaps they also do some out-of-band verification like having the network operator call a pre-determined phone number to check the message's validity.
At which point, the operator can choose to send the message or not.
Or can they?
In August 2026, the UK government instructed network operators to send this message:
Did the networks
have
to send that message? If they thought it wasn't serious enough, could they have refused? As far as I can tell, the law only talks about the fact that operators can disregard "spam" laws in order to send a mass message:
A relevant public communications provider (P) may, for the purpose of providing an emergency alert service, disregard the restrictions on the processing of data relating to users or subscribers set out in paragraph (2) if the conditions set out in paragraph (3) are met.
[…]
(3) The conditions are—
(a)P is notified by a relevant public authority that—
(i)an emergency within the meaning of section 1(1) of the Civil Contingencies Act 2004 has occurred, is occurring or is about to occur;
Statutory Instrument 2015 No. 355
I'm no expert, but I can't see anything in
the spectrum licence
nor in the
Wireless Telegraphy Act
which
compels
operators to process these messages.
The usual British way is to ask people to play nicely and threaten them with regulation if they don't.
Could the networks have refused to send the message about wildfires - or indeed any other message? If your least favourite politician gets their hands on the emergency alert system and tries to abuse it, would you want the networks to stand up to them?
What if the network refuses to send the message because they're worried alerting people about a hurricane will lower the company's profits?
What if armed thugs are sent in and the choice is send the message or die?
I don't know what the answer is here. I think most people agree that it is broadly sensible to have a way to alert the population of emergencies. There's no mass media any more, we're not all listening to a single radio channel, or reading newspapers, or even on the same social media platforms. Sometimes there are emergencies and the Government has a duty to alert people to them.
How would you design a system that simultaneously achieved all these goals:
Rapid sending of messages
Careful checking of the content of messages
Ability to quickly target a specific geographic area
Inability to mistakenly send a test message
Requiring strong proof that the message is authentic before sending
Resilient enough to work after significant damage to infrastructure
That networks have the ability to vet and ignore
That networks are compelled to send
Which can only be used for good
And cannot be used for evil.
In truth,
having experienced fire-starters
, I'm not bothered about the contents of this latest message from the UK Government. Given the overstretched fire service and the imminent threat across most of the country, my personal opinion is that it is proportionate.
But it is easy to see why some people feel this might open the gateway to messages which, at best, are irrelevant and, at worst, are similar to the insidious propaganda which appeared on the phones of Egyptians:
To every mother-father-sister-brother, to every honest citizen. Preserve this country as the nation is forever.
Perhaps you can think of a way to design an alerting system which cannot be abused - but I can't.
