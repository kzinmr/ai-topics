---
title: "Explore the fediverse, but use block like it's a machine gun in a zombie apocalypse"
url: "https://boyter.org/posts/mastinator-activitypub-breaking-assumptions/"
fetched_at: 2026-05-05T07:01:56.229782+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Explore the fediverse, but use block like it's a machine gun in a zombie apocalypse

Source: https://boyter.org/posts/mastinator-activitypub-breaking-assumptions/

I didn’t really expect to have a post this late in the year but here we go. Lets go through some assumptions that were broken for me recently. Not just my own through perhaps some other peoples assumptions too.
I have been working with ActivityPub for a bit. I want to run my own server, beyond installing some 3rd party. I want to build my own from scratch. However this rapidly exposed some problems with testing ActivityPub.
That is that there are no easy ways to test things. Want to send a post? Well you better be sure you get the JSON format, the endpoints and the signing working as you expect. Want to receive a post? Similar story.
The easiest solution is to spin up an existing compliant solution, hack away on it talking to your custom code, and repeat till you get something working. Then try it again on multiple systems.
So as a result I ended up writing the minimal amount of code to accept a post, so webfinger, inbox and user requests and used that to test things. I then realised that having this running online somewhere would save me a lot of time, as I would not need to fiddle around with ngrok all the time.
A little coding later and I could get it to issue follow requests to 3rd party servers, and then receive those posts. Brilliant. I was close to having enough to implement everything I needed.
However, I also had a thought. If I could generate deterministic public/private keys at runtime, I could do something like mailinator.com and create disposable fediverse accounts. Disposable public anonymous no-login fediverse accounts. I could create ALL the accounts, and accept posts on any of them! A way to follow accounts without being authenticated.
So I registered
mastinator.com
as an homage to mailinator (plus its a purple cow name) , polished off the code, adding in logic to save the posts in memory, such that they expire over time as new posts come in and pushed it live.
As a result
All posts are ephemeral. A server restart, or enough time passing will cause any post to disappear.
Nothing is persisted. It is not an archive, posts exist only in RAM for a brief period of time.
New posts push out old posts over time.
Mastinator cannot and will never send a post. If you get a toot/post/honk from Mastinator it is forged.
Any fediverse account can @ message at mastinator and it will appear in that inboxes timeline
Literally every account already exists. Pick any name and its there.
I then added some accounts to follow… then the show started.
https://mastodon.ar.al/@aral/109585159213960986
It started with the above post by a well known and well followed user Aral. Then all hell broke loose. I did post some responses to try and quell what had by now become a screaming hoard of haters, but that just exposed me to direct abuse.
Not that it bothers me much. I can deal with it, although I will say some of the responses I got were nothing short of horrible. The sort of thing that literally drives people to do bad things. Some out there should be ashamed of themselves.
So I quickly re-evaluated my opinion of the fediverse in general. Or rather parts of it.
I do get it though… I think. I suspect a lot of people have fled other online communities where they were possibly subject to fairly horrible things. If they feel even slightly threatened they are likely to lash out.
As a result I think anyone saying “the community” needs to be very careful in future. Lumping any group as “a community” really does not capture the diversity of opinions and people, especially if you are lumping them all together because they use some piece of technology.
As a result mastinator.com was blocked fairly quickly by a few instances. You can see the commit here
https://github.com/chaossocial/meta/commit/af9abd9043fe20a947f44f00438f9247edfdc50e
So is blocking the solution?
Not really. A quick look at this link
https://fba.ryona.agency/?domain=mastinator.com
shows that some instances have blocked mastinator.com as well (I totally encourage you to do so if you want, although it might be useful if you just block its ability to do follows, as then you can still @ it if you want). However if you look at the list most do not block subdomains. Were I an evil actor I could create a subdomain and be back to following (or indeed messaging were I totally evil) very quickly.
Even blocking subdomains is limited. A new domain is fairly cheap. I certainly am not going to spend money to get around this, but I could see bad faith actors doing so.
Plus I am following the specifications. Were I to actually scrape content I would be unlikely to respond to takedowns, and I would be proxying around to ensure your blocks do not work.
So what to do about this? I have a few possible ideas/solutions in mind, although how viable they are depends on your point of view.
Leave the Federated Systems
Consider if you really need to use a federated discussion system. I suspect a lot of communities who migrated to Mastodon did not really consider the implications of what a federated system means.
They might be better served by an older style web forum. Turn off public access, and have it be invite only. Very safe, lower hosting costs, very good moderation tools built in, and the ability to block forever.
Consider Turning Off Federation
If you really do want the Mastodon system as your place to hang out, perhaps consider turning off all of the federation. Don’t allow any cross server communication.
Switch to allow-lists
Instead of blocking problematic servers, create your own federation by having an approved allow-list shared between those federated servers. Allow new ones only on consensus.
Bigger Icebergs Ahead
In the grand scheme of things, I think that the fediverse has some serious issues coming its way, some technical, some not so much.
The first is that there seems to be this rose tinted glasses approach to federation. People will be nice, and good, think like I do and not abuse the system. Of course the real world does not work like this. I’m no saint, but I was actually interacting with people during this, trying to dispel their concerns and improve things. In short if I were evil I could have just as easily ignored everything, or remained totally hidden.
Bad actors will do none of these things. I would expect them to slurp up every bit of data they can, obscure the fact they are doing it, and then use it for their own purposes, cambridge analytica ring any bells?
The second is that people seem to have a lack of understanding of how this system works. Federation allows cross posting. That’s the point. Based on the conversations I was getting I think there is a massive lack of understanding about how this works. Especially when it comes to posts and follows. People don’t seem to understand that when you post, a copy is made and distributed to every follower you have, and as such that copy is stored on every federated instance.
This lack of understanding applies to edits/deletes and other features of ActivityPub. They are a “should” option inside the specification. Meaning servers can ignore these requests, and as such your delete request does not have to be honoured.
Scale is also a massive issue. Mastodon and other ActivityPub have a massive scaling issue. This was covered by Aral
https://ar.al/2022/11/09/is-the-fediverse-about-to-get-fryed-or-why-every-toot-is-also-a-potential-denial-of-service-attack/
but his take-away is missing things in my opinion.
While people with large followings should probably spin up their own servers so that they foot the bill for distributing posts, as I have shown there are no rate limits when it comes to creating users. The fediverse seems to be working on the assumption that there are external rate limits when it comes to accounts, and that is absolutely not the case.
This is a lot harder to solve, but I think the solution already exists. Perhaps for any interaction that is not requested, so a post to my inbox from another where I wanted to follow them, introduce a small proof of work system. Bitmessage
https://wiki.bitmessage.org/
implemented this and while sadly that has its own issues, you were able to chose your own difficulty and cut down on spam.
Applying this to follow requests, or indeed any other unsolicited request would massively drive the cost of these sort of operations. Indeed the idea itself was proposed by Microsoft to cut down on email spam. I suspect even using the public/private keys that exist within the system to encrypt/decrypt might be enough of a nudge in this direction to increase the spam cost.
Also worth noting, that every added user increases server costs. Want to cost someone a lot of money? Get as many people as you can to follow them. Every follower increases their server load. On a shared instance they are going to slow down the server, and the admins are going to ask for money to maintain it. If they are on their own instance they are going to have to upgrade it to ensure timely communication.
My Takeaway
So as I mentioned I am not doing anything in bad faith here. I started by solving my own problem, realised I could solve other people’s problems, then just followed this to a conclusion. If I had not done this someone else would have.
The difference is that I was happy to do it publicly, took ownership, talked through it, and tried to improve things. Interestingly for some that just isn’t good enough. Nothing short of full capitulation to how they want things to run is enough. This attitude in itself I think is going to hold back everything. Ever wondered why there is no search for the fediverse? Something like that would be extremely useful, especially when it comes to finding people to follow. However parts of the community HATE the idea with fire of a thousand suns and will do anything in their power to tear you down should you build it. I can’t wait for some silicon valley company to come along and do so. Embrace, extend, extinguish could be the death knell of what has been created.
One thing I did observe is that the reach of the fediverse is larger than I thought. So much so I was interviewed over what happened by this following podcast
https://tunes.artemai.art/channels/acrossthefediverse/
The audio is still being cut, but when there might hopefully appease someone? I have my doubts, these days it seems if disagree with someone you have to do so no matter what they say or do.
I think I totally get the uproar over quote re-tweets now. It seems there is a group of people out there who expect people to implement what they think is required for them without considering doing it themselves. Don’t do it? You are spreading hate.
the ethical thing to do is to go take your computer, make sure to pop open every single case, plug them in so you can make sure everything gets nice and fried, then give them all a long, long, long shower.
Thats a direct quote from one of the responses I got BTW, and probably one of the nicer things that… individual wrote.
Anyway tangent aside, expecting others to owe you their time and effort is not cool. I suspect it’s not the technical argument against it, but that people have this mindset going in. I suspect a lot of it comes back to this post
https://boyter.org/posts/the-three-f-s-of-open-source/
with the developers firmly in the third category at this point.
So bringing this back to twitter, while I had an idea that dealing with people on any sort of scale was difficult, I now have new appreciation for not only the people previously running twitter, and some sympathy for Elon Musk.
No matter what you do you are going to piss off a lot of very angry people. Even if you agree 100% with everything these people say you will never be good enough in their eyes. Independent thought seems to be optional.
Anyway this post is long enough. I still like the fediverse. I love the idea of having the ability to run my own instance which was stolen from us with email. I could see it being a good replacement for email, just add encryption using the public/private keys and keep it private.
So yes, I still do say you should check out the fediverse. Just be sure to use that block/mute button like it’s a machine gun in a zombie apocalypse.
