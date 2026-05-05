---
title: "If you succeed, you will fail"
url: "https://boyter.org/posts/if-you-succeed-you-will-fail/"
fetched_at: 2026-05-05T07:01:56.774805+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# If you succeed, you will fail

Source: https://boyter.org/posts/if-you-succeed-you-will-fail/

If you succeed, you will fail.
Something said at a client engagement I was at some time ago. I figure enough time has passed that it is worth sharing this story.
One of the early engagements was to deliver for a very large company an iOS Application powered by a RESTful API. This was problematic due to what is common for every large organisation, a collection of older legacy backends. Some with their own API’s, and bizzare authentication processes. Part of the deliverable was also working with push notifications for things like billing updates, documenting the systems (since few people knew how everything worked) and load testing.
Delivering the API… looking back had some pain points, but nothing exceptional. After 6 months of development, we had built out a full AWS environment, including deployment pipelines for all infrastructure, the API, with tests, monitoring and such. The authentication process was particularly bizarre in the way it worked. It was what I would expect OAuth to work like, if you faxed the details of it a few times before handing over the final copy to someone to implement. It worked, but was bespoke.
Early on we had discussed performance. The company insisted that they were going to advertise the app pretty heavily and with their expected customer base that tens of thousands of customers would login and use the application within a few days. Further prodding, with estimates based on existing load and such we settled on a target of about 100 RPS.
For the portions that we were in control of this was easy. We have built out using AWS API-GW with Lambda. So we got 300 concurrent lambdas per endpoint by default. Since most requests were processed in 100ms or so we could comfortably deliver over 1,000 RPS without actually having to do anything.
Where we needed to talk to backend systems was a different story however. SAP was the system driving the business and it had most of the integration we had to work with. The lead developer for the system was a fairly nasty piece of work. He was not the most incompetent person I had ever worked with, in fact far from it. But he is certainly one of the most hostile.
There were multiple ways to query his system, and getting straight answers as to the most efficient way to do so was met with “well you could do that”. In short he was actively trying to sabotage the project, even pointing out his system offered an API already, so why build another? Ignoring of course that we integrated with multiple systems, and were managing things like push notifications.
Anyway once we added load tests for anything that depended on SAP it became apparent that the downstream systems could deliver something like 25-50 RPS depending on what we were querying for. Optimisation of the calls had already been done at this point, with his insistence as to things being slow met with “Well its processing a lot of data” and “We don’t have AWS so we cannot be lazy and have to optimise properly”.
We need to halt the release till this is resolved.
Pointing out that this was going to be problematic eventually resulted in an upgrade of the SAP systems. At which point they could perform over 100 RPS and everyone was happy.
However there is always a bottleneck. You just remove one to uncover another.
However, remember that oddly implemented authentication system? Because of quirks with how it was implemented it meant when tokens to it expired, they expired at once for every user. Also with the release coming there was going to be a huge amount of requests to start. When this was load tested it became apparent it could only sustain about 5 RPS.
This became a huge issue, especially once we started load testing against staging which was the closest environment to production. Whenever we load tested, not only would staging go down for hours once it had tipped over, production would soon follow. This resulted in a lot of massive conference calls with myself and a few others running an automated script to fire the requests, while an army of op’s and developers would monitor systems to work out the problem.
Turned out that at some point someone had configured the production network systems to fall over to staging in the event of a failure. However they had also configured the reverse. This took a few weeks to discover why however. Now this would probably be fine were it limited to the app, but it actually ended up taking down the production web application at the same time. The best part? We weren’t even load testing in a distributed way. In fact most of our “load” tests were run on a single EC2 instance, or even local laptop over WiFi. We realised that we could probably take down the system, on prem or remotely using a raspberry pi and a ADSL2+ connection.
Even more alarming was that when this was done it would take down the web portal application used by customers around the country.
We need to halt the release till this is resolved.
Having already heard this, clearly it fell on deaf ears. After all, they already upgraded… So why do it again?
The release date was fixed, and going ahead no matter what. No amount of discussion or push back could change their mind. It was then someone (I don’t even know if it was me) pointed out in a meeting that, if as many people as they want or expect use the system on the release, it’s going to be a success in terms of users, and then an epic fail when the system falls over.
If you succeed, you will fail.
We ended up trying to cover our company by sending out an email listing the problems, what the likely result was and asking for their acceptance of this outcome. Which I think we got.
Sadly it did happen just as expected. There was a large party celebrating the launch, and while many were eating cupcakes and drinking sparkling wine to celebrate, I and my colleagues were watching the production system crash and burn. Eventually we had to severely limit the login using API-GW before calling it a day and going home.
I think the worst thing was knowing that a new authentication system was just weeks away. Which would have ensured this would not happen.
Several weeks later we were out. Considering we had delivered I was not too upset by this, although I do wish it had been the success that we all wanted to be.
I learnt a few things from this. The first is, some companies or organisations within them need failure in order to progress. Warnings, no matter how prophetic, are seen as being unhelpful and negative. Blind optimism up till the failure is their modus operandi. Fall back on blaming the process when failure comes around and avoid ever pointing fingers or owning it.
I also learnt to only become as involved and care as much as the customer. If they aren’t willing to go that extra mile then why should I?
Am I a bitter person because of this experience? Not really. I still have enthusiasm for projects and helping out. But I am far wiser as to when I care as much as I did this time.
