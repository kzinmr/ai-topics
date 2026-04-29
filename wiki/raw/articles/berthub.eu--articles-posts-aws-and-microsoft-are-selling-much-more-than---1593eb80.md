---
title: "AWS and Microsoft are selling much more than cloud services"
url: "https://berthub.eu/articles/posts/aws-and-microsoft-are-selling-much-more-than-cloud/"
fetched_at: 2026-04-29T07:02:23.349407+00:00
source: "berthub.eu"
tags: [blog, raw]
---

# AWS and Microsoft are selling much more than cloud services

Source: https://berthub.eu/articles/posts/aws-and-microsoft-are-selling-much-more-than-cloud/

Ten, twenty years ago customers over at large corporations would often ask me what hardware they’d need to run my software. As software developers, we’d tend to be rather blasé about such questions: “whatever you have lying around!”. If pressed, we’d say you’d need this much RAM and that much storage.
We thought we were doing our users a tremendous favor by being so flexible. Yet, customers were very much not happy with our responses. They’d press us for endless details on the requirements, even things that were manifestly not relevant.
It took me a while to figure this out. Corporate life is VERY different from open source software developer life. The values are completely different. And an extremely important corporate value is
never getting blamed
. What they desire is that a vendor lays down the requirements, they meet the requirements, and if anything goes wrong, the blame can be assigned 100% to the vendor.
Compare this to someone over at a large corporation selecting hardware based on my “go ahead, pick anything!” advice. They’d be left
holding the bag
if anything disappoints. This is
not
good for you at a corporate place.
So we learned, and the proper way of doing this was to ask what kind of servers/hardware the corporation typically used, and then explicitly bless one of their options. Also, make sure you select some honking hardware so things will come out right. Corporate workers are willing to trade (corporate) money as protection for not getting blamed later on.
Key is, the corporate customer wants to be able to allocate the full blame with you.
It is good to know that governments effectively operate as corporations this way
Photo by
the blowup
on
Unsplash
Time passes
Later, this stopped working, and customers demanded that we’d supply them with complete working solutions. With one big user this ended up in tears. They gave us a few square meters in their data center, and told us to arrange
everything
for a working solution. Including network switch, servers, storage, cabling, rack, racking: the works. They’d supply cooling and power.
As a software person this is no fun, but we had to do it. And it turns out that the customer had 63A power plugs in their DC and we, not being experienced, had missed out on pinning them down on that. So we showed up with a rack with 32A connectivity, and it all didn’t work. We even made a fully certified and fused 63A -> 32A converter, but they wouldn’t have it. So we had to eat the cost of getting them a whole new rack.
The customer was, in a sense, clever that way. They had likely also not realized their power situation was unusual, and they were able to assign the blame entirely to us. Well done.
There is a trade in blame
Large cloud providers will sell you anything and at a scale as large as you want. If your code is slow, it will simply consume more cloud services and rack up a larger bill. But it will work. Compare this to the story above of having to pick a hardware server, and picking one that is too small.
The corporate worker would get blamed for a service simply not working during peak hours
. In the cloud, you’ll not have this problem. It merely gets expensive. But there are ways of dealing with that that do not involve you ruining your career.
This trade in blame is a cloud special. There used to be many of these choices in corporate life, like for example which database to use, when to allow maintenance, what kind of storage fabric to pick. All things that you could end up holding the bag for. But no more.
If you picked AWS for your database, all your problems can be solved by spending more money. If there are security worries, enable the WAF, if there are compliance worries, AWS has them all.
Doing business with AWS or Microsoft is as risk free as any corporate decision will ever be. In the short term, of course. Long term,
there are dangers
Now enter the fledgling European alternative
People who are not AWS or Microsoft are fond of saying “there is no cloud, just other people’s computers”. The idea behind this is that since we also have computers, we are also a cloud provider. Now, this is nonsense
since the big hyperscaler clouds sell services that are definitely not “just servers”
.
However, there is a further way in which this is not true. Large established cloud providers are also supreme blame absorbers. As noted, doing business with them is nearly risk free for almost all corporate workers. Reams of consultants stand ready to defend your choices. Every supplier is on board. It is the go-to choice. Even if AWS suffers a day long failure, EVERYONE experiences that failure, which provides for great cover.
It is the same thing we used to call “no one ever got fired for buying IBM”. Your worst case is that things end up being expensive, and even there the large cloud providers help you: the bills are so complicated it is nearly impossible to assign the blame for excessive costs!
Now, if you as a European independent place try to compete with a US hyperscaler, you have a few things going for you. From a legal/GDPR perspective, but also from a sanctions perspective,
you do look better
. Also, it is entirely possible to offer many things way cheaper and simpler than US hyperscalers.
However, what your 10-100 million euro/year operation can not DREAM of offering is being a risk free choice. Not only is this a matter of heft (you versus trillion dollar shops), you simply do not have the infrastructure to deal with customers making mistakes. Recall how it was a big deal for my small company to deal with a single mis-specced 19" rack. Your smallish place simply can’t provide the 2000 additional CPU cores because the corporation miscalculated the efficiency of its new product.
Additionally, to properly absorb blame as a service provider requires dedicated (sales) staff that can help the poor corporation solve its problems in a way that is legally without risk, but does rake in the cash. This is complicated enough in itself. Absorbing blame as an expensive service.
Now, this is contrary to a lot of the values of European open source/sovereignty idealists. We want to provide the best most efficient most secure services.
But the current large-scale cloud customer worries about very different things. These are not their values. Their values are being successful in large corporations (and who can blame them?).
And when they look at an idealistic European hoster with cloud ambition, almost everything will tickle them the wrong way. We’ll talk about pricing, perhaps with tables listing costs as low as 20 euros/month. There might even be an offer for the first 3 months free!
But nothing screams “you’ll be able to blame us if it goes wrong”. Which is what the actual market is like over at large corporations.
Note that providing “comfort” is about FAR more than blame allocation. It also involves training, certifications that work on the job market, and a whole supporting ecosystem!
So
It is hard enough to compete with the large cloud providers from a technical front. But realize that this is not the only challenge. To compete in this market, you also need to be the place people feel 100% comfortable doing business with. Generating this feeling of comfort is a job in itself.
And if you neglect it, you end up not getting the corporate business.
Which is a shame, since they spend money like water - revenue we are right now missing out on. Also, in terms of “blame game”, what you can now offer is “
not getting us blamed for going out of business after US sanctions
”. This is getting to be an ever more interesting offering!
So do give it a good think - do you want to be a corporate blame absorber & comfort provider? If so, good for you. But if you don’t, you need to be able to survive based on business from very different customers.
Good luck!
Further reading
