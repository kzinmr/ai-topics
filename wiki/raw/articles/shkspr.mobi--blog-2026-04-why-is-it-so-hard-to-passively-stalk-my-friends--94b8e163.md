---
title: "Why is it so hard to passively stalk my friends’ locations?"
url: "https://shkspr.mobi/blog/2026/04/why-is-it-so-hard-to-passively-stalk-my-friends-locations/"
fetched_at: 2026-04-30T07:01:01.006675+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Why is it so hard to passively stalk my friends’ locations?

Source: https://shkspr.mobi/blog/2026/04/why-is-it-so-hard-to-passively-stalk-my-friends-locations/

I feel terribly guilty when I visit a new city, post photos of my travels, only to have a friend say "Hey! Why didn't you let me know you were in my neck of the woods?"
Similarly, if I bump into an old acquaintance at a conference, we both tend to say "If only I'd known you were here, we could have had dinner together last night!"
I do enjoy the serendipity of events like FOSDEM - randomly seeing a mate and expressing the joy of spontaneity. But I also like arranging to meet up in advance.
At the moment, my strategy is sending a blast on social media saying "I'm visiting [this city] next week, anyone fancy a beer and a natter?" I've met friends all over Europe, Australia, and New Zealand that way.
It mostly works
.  But I can't help feeling it is inefficient and prone to missing connections.
I even wrote my own code to auto-post FourSquare checkins to my other social media sites.
Here are my ideal scenarios. Imagine something built in to Signal / WhatsApp / Whatever app you already use.
I tell my app that I'm going to Barcelona from 14th - 19th February and am happy to meet any of my friends.
✨Background Magic✨
My friend Alice has also planned a trip to Barcelona around those dates. She gets a ping saying that one of her friends is going to be in the same city. Does she want to know more?
So far, so
Dopplr
.
My friend Bob lives just outside of Barcelona. He's set his "willing to travel" settings to be about 30 minutes, so also receives a ping.
I don't know that either of them have seen the notification until they decide they want to meet.
I step off the train in Manchester, England England.  Perhaps the app notices I'm away from home, or maybe I press the "Anyone Around?" button.
On a map I can see friends who have shared their rough location. I decide to message Chuck to see if he's free for a chat.
Dave notices my location is now within his preferred travel distance. He gives me a ring.
A bit like how FourSquare used to be - but with less precision.
The above is very much the "happy path". It doesn't look at any of the knotty problems or grapple with the UI that would be needed to make this work.  But we know the technology for sharing location is viable - so what are the social issues that make this so difficult?
"Oh, fuck, Edgar's location says he's in town. Can we pretend to be out of the country?"
Alternatively, "Huh, I know at least a dozen people who live in Skegness. Why aren't any of them responding to me?"
Social pressure and awkwardness are hard problems. No one wants to use the app that makes you feel like a friendless loser.
Do you
want
your friends knowing your every movement? I'm sure some people do, but most probably don't. It's possible to sketch out some vague controls:
Only send a notification if I push this button.
Don't send alerts if I am within this radius of my home / work.
Fuzz my location to the city / state / country level.
Is it a risk to let people know vaguely where you are? Is meeting up with (semi-) strangers from the Internet a smart life choice? Is having an app stalk you across the globe giving too much data to advertisers?
Does that creep from work abuse the system to keep popping up whenever you're out with friends?
I said the technology exists for this, and that was sort of true. Every device has GPS & an Internet connection. Storing a log of friends and sending them a message is a solved problem.
But is it solved in a decentralised and privacy preserving way?
No one wants to give all this power to one company. Google will build it and kill it. Facebook will sell your secrets to dropshippers. A funky start-up will be acquhired by Apple & restricted to iOS devices.
My location is fuzzed to an acceptable degree of imprecision and then sent… where? To all my friends directly? To a central server? Can
k
-anonymity
help?
Is this a separate app? Everyone seemed to leave FourSquare after they buggered around with it. Perhaps it is just a feature in existing apps?
Messaging apps like Signal, Telegram, and WhatsApp allow you to share your location with one or more friends.
To me, it feels a bit weird to manually send a dropped pin to some / all of my contact. It also doesn't let you share "tomorrow I will be in…"
Using "Stories" is the common way to share an update with all contacts - but none of them let you automatically share your location in a story.
FourSquare's Swarm app allows you to check in to a "neighbourhood". But there's no obvious way of saying "London" or "Manchester" - and I'm not sure how close to an area you need to be to get an alert that your friend is there.
I don't want to build this. Trying to get everyone I know to adopt a new app isn't going to happen. With the fragmentation of messaging and the lack of interoperability, this is likely to remain an unsolved problem for some time.
So here's my strategy.
Get back in to using FourSquare. Most of my friends seemed to stop using it back in 2017 when it was split into Swarm. But a few are still on there.
Manually post a story on Mastodon, BlueSky, Facebook, WhatsApp, Signal, and Telegram saying "Visiting Hamburg next week. Anyone want a beer?"
Hope that something better comes along.
