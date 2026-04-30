---
title: "Unfortunately, the ICEBlock app is activism theater"
url: "https://micahflee.com/unfortunately-the-iceblock-app-is-activism-theater/"
fetched_at: 2026-04-30T07:01:56.998045+00:00
source: "micahflee.com"
tags: [blog, raw]
---

# Unfortunately, the ICEBlock app is activism theater

Source: https://micahflee.com/unfortunately-the-iceblock-app-is-activism-theater/

At this summer's HOPE conference, Joshua Aaron spoke about
ICEBlock
, his iPhone app that allows users to anonymously report ICE sightings within a 5 mile radius, and to get notifications when others report ICE sightings near them. You can see the full talk, and the lively/infuriating Q&A,
here
, starting at 6:12:10.
Thanks to repression from the highest levels of the Trump administration, his app has gone viral and garnered over a million downloads from the App Store. Karoline Leavitt
called it
"an incitement of further violence against our ICE officers." Tom Homan
said
, "DOJ needs to look at this and see if they're crossing that line." Kristi Noem
called the app
"obstruction of justice." Pam Bondi
announced
"we are looking at it, we are looking at him, and he better watch out, because that's not a protected speech." (Notifying people about ICE sightings is protected speech, no matter what the fascist Attorney General says.) Joshua and his family have been receiving threats.
But unfortunately, despite the app’s goal of protecting people from ICE, its viral success, and the state repression against it, ICEBlock has serious issues:
Most importantly, it wasn’t developed with input from people who actually defend immigrants from deportation. As a result, it doesn’t provide people with what they need to stay safe.
Because ICE sightings in the app aren’t verified in any way, it's likely that most reports in the app aren't actually ICE, even if they’re posted by people who mean well – as I describe below, the vast majority of ICE reports are false positives.
And judging by the App Store reviews, it’s clear that not everyone means well. One review says: “This is a great app for safety information. Unfortunately MAGA is now posting false information on there and making racist comments in the comment section.”
Joshua makes strong claims about the security and privacy of his app without backing any of them up with technical details. Many of his claims are false. He also chose to target only iOS, and not Android, because of a
misunderstanding
about how Android push notifications work. And even worse, during the Q&A, he made it clear that he didn't understand terms like “warrant canary,” "reverse engineering," or “security through obscurity,” which doesn't inspire confidence.
Privacy promises without the evidence
When I first heard about ICEBlock, I liked the idea, but I – and others in various group chats I'm part of – were skeptical.
Joshua promises that ICE reports are "completely anonymous," that the app doesn't store any personal data, and that it's "impossible to trace reports back to individual users." These are bold claims that he hasn't backed up with evidence. Unlike reputable privacy tools, ICEBlock isn't open source (in the talk, he explicitly rejected the idea of open sourcing it or allowing the security community to help him improve it), and Joshua hasn't published a threat model or technical documentation explaining how his app keeps these promises.
My friend Cooper Quintin, a security researcher at EFF, was also skeptical of ICEBlock, and so he
reverse engineered it
, and spoke to 404 Media about
his findings
. He largely confirmed Joshua's claims:
The TL;DR is that I didn't find anything suspicious, the app doesn't talk to any third parties, and it doesn't send your location to the developer. Neither your phone ID or iCloud account are associated with the requests the app sends to the apple cloud servers to run. (2/11)
—
Exploit Code Not People (@cooperq.com)
2025-07-15T18:52:15.697Z
This is great, and it's the reason that (despite his hostility towards transparency) I really do think that Joshua means well.
Even if we can trust that Joshua isn't collecting data himself, it's difficult to discern what Apple would be able to hand over if it got subpoenaed for data related to his app. The website simply says it's "completely anonymous," without any caveats.
But ignoring the lack of transparency, there's an even larger problem.
ICEBlock spreads unverified information, making it useless for defending immigrants
Local immigrant defense groups around the country have been defending people from deportation for the last decade or more. In a training with
NorCal Resist
, I learned that when people post (and repost) unverified reports of ICE sightings on social media,
it does more harm than good
.
Millions of people are living in a state of fear. From my experience working with NorCal Resist,
most ICE sightings that people hear about aren't real, even when the person reporting it believes that they are.
It's common for someone to see a bunch of dudes in uniforms, or sketchy looking vans, and assume it's ICE, when it's actually something else. If I had to guess, I'd say about 98% of reports are false positives.
False reports encourage panic, which doesn't help anyone.
Meanwhile, what people actually need are
legal observers
– people to document the behavior of federal agents, and provide this evidence to their lawyers. They also need help with connecting families of kidnapped people with information and lawyers, and they need communities coming out to defend their neighbors.
When I asked Joshua about this during the Q&A of his talk, he didn't answer the question. Here's my question and his non-answers:
Joshua's non-answer to my question about false positives and user research
Specifically, I asked:
With my local group, they put a whole lot of energy into verifying every single report before spreading information about it. My question is, how do you know that ICEBlock isn't just full of false positives? And have you done any user research, or worked with local immigration groups to figure out how reliable this is, how much it's actually helping people versus causing panic?
In an attempt to answer the question about user research, Joshua said, "No, we do not do any user data or metrics." He misunderstood the question, apparently thinking that I meant collecting data from users rather than talking to humans who know more than he does and incorporating their feedback into the design of the app.
He then explained what ICEBlock does to prevent
malicious
people from making false reports — including falsely claiming that it's "not possible" to make tons of simultaneous fake reports (more on this below).
ICEBlock doesn't verify anything, and instead
only
spreads unverified rumors. To be fair, verification is a
very hard problem
. In my local group, we have
announcement-only Signal groups
full of volunteers who physically verify every single ICE sighting that's reported to our rapid response hotline. The vast majority of reports are false positives. There might be several reports a day, but actual ICE or CBP activity is much more rare. I've personally gone to check out maybe 10 to 15 different ICE sightings, only one of which turned out to be actual immigration enforcement (though by the time I got to the location, ICE had already left the area). None of these false reports were malicious: they were simply scared people who saw a bunch of vehicles and people in uniforms and reported an ICE sighting, when it was actually something else.
Another person in the audience asked a similar question:
I'm wondering, I think someone asked earlier, if in the design of ICEBlock, or even now, are you currently working with immigrant communities to figure out what resources they need?
Another question about if Joshua has engaged with community groups
His answer was that ICEBlock has been translated into many different languages. And that the community organizers he's spoken with told him that ICEBlock doesn't meet their needs. So, he decided to not worry about their feedback and do his own thing instead.
If you want to support people who are actually protecting immigrants from deportation, please
donate to NorCal Resist
or your local community rapid response networks.
What's GPS spoofing?
When Joshua explained the safeguards against abuse in the app, he claimed that it's "not possible" to make 100 fake reports in a single morning, in part because you can only make reports within a 5 mile radius of your location. But apparently, Joshua has never heard of GPS spoofing.
Even though I'm sitting at my house in California right now, here's a screenshot I just took of the ICEBlock app from the Eiffel Tower in Paris. While I won't go into details of the masterful hacking skills that this took, I'll give you a hint: it's the same technique kids use to cheat at Pokemon Go.
Screenshot of ICEBlock app, with GPS location spoofed to make it think I'm in Paris
Make ICEBlock open source? "Absolutely not."
Someone asked whether Joshua would be interested in collaborating with the hacker community on ICEBlock, so they could provide him with advice and help him with feature development.
Joshua rejected the idea, saying that he believes that he'd need to completely trust anyone he collaborated with. "Believe me when I say I would love help. I'm supporting over a million users myself. There's not some giant company behind this," he said. "But it's really really hard for me to put my trust in somebody, and share the source code, and share the access to this."
Joshua explaining that he's building ICEBlock all on his own because he can't trust outside contributors
This is, of course, not how secure software development works. The most widely trusted security and privacy tools that exist, like Signal and Tor, are open source, and they accept peer review and code contributions from the public.
The thing that makes this perfectly reasonable and safe is
code review
. If Joshua published the ICEBlock source code, experts in the hacker community could add features or fix bugs for him, and make pull requests with their changes. He could then carefully review the changes before merging them into his codebase. He could reject whatever changes he wants. You don't actually need to trust – or even know the identity of – hackers who help you develop software. This is a solved a problem, and Joshua seems utterly unaware of it.
My friend Jen Helsby, the CTO of Freedom of the Press Foundation and a SecureDrop developer, explicitly asked if he would be open to making ICEBlock open source. Here's the clip:
Joshua will not release ICEBlock as open source because he doesn't believe in reverse engineering and thinks keeping the implementation details of his app obscure makes it more secure
Jen asked:
There's a lot of secure software, that probably people in this room work on, that is developed in the open, and that is used primarily by at-risk users, including things like Tor, Signal, SecureDrop. That's great, because it makes it easy for folks to contribute. Maybe you don't want that, I understand that can be hard. But it also makes it easier for people to audit and gain assurance that the app is doing what you claim without having to have, you know, EFF reverse engineer it. Would you be open to making the app open source?
His answer: "Absolutely not."
Why? "I don't want anybody from the government to have their hooks in how I'm doing what I'm doing. Once you go open source, everybody has access to it. So I'm just going to keep the codebase private at this time."
He also claimed that the government can't learn everything about how an app works by reverse engineering it, which isn't true.
I agree with Jen. His answers are very concerning.
What's security through obscurity?
Another person asked specifically how concealing the details of how the app works from the government is distinguishable from security through obscurity, Joshua agreed that security through obscurity is terrible... and denied that he's doing it?
Joshua falsely claiming he doesn't do security through obscurity
In case you're not aware of this term, the first sentence of the Wikipedia
article
on security through obscurity has a concise definition:
In security engineering,
security through obscurity
is the practice of concealing the details or mechanisms of a system to enhance its security.
NIST's
General Guide to Server Security
lists "Open Design" as a core security principle, saying that, "System security should not depend on the secrecy of the implementation or its components."
Minutes before this, Joshua had just finishing explaining that he definitely won't open source his app because, "I don't want anybody from the government to have their hooks in how I'm doing what I'm doing."
He's implying that his code includes some "secret sauce" that, if it were made public, would make the app less secure, so he can't risk letting anyone discover how it works. This is the
definition
of security through obscurity.
My server is "HIGHLY secure," he says to a room full of hackers
Throughout the Q&A, Joshua kept referencing the security of his server. At one point, he even said that he built it himself and it's "
HIGHLY
secure." He also assured the audience, "Trust me when I tell you, I think about
EVERYTHING
to the Nth degree."
It took about 20 minutes of digging around to discover that the server that hosts the iceblock.app website is running on Linode and also hosts the websites of several of Joshua's other projects, going back decades. This includes a website for his IT consulting business, his band, etc. If any one of those old websites gets hacked, it's possible that the hacker could more easily access ICEBlock data that's stored on the same server.
Without providing more details, I also discovered that his server is running outdated software with known vulnerabilities.
What's a warrant canary?
At one point, a lawyer asked some excellent legal questions:
I'm curious if ICEBlock either currently or has intentions to implement something like a warrant canary or other method. And more generally, whether you have received anything like search warrants, or All Writs Act requests, or anything else. Things like more intrusive means of obtaining information from ICEBlock. Things like requests for live interception, which would be authorized under a search warrant. And if you have a response plan in place already for those.
A lawyer asking Joshua about warrant canaries and data requests
If you're not familiar with
warrant canaries
, these are basically public notices that say, "I've never been forced to give up user data." If the notice ever gets taken down, the public can infer that the service was in fact forced to hand over user data.
Joshua said, "No on the warrant canary, because it would probably require some sort of user data to do that." He seemed to think that a warrant canary would be a new feature in the app (that's uh, not what a warrant canary is), and he completely ignored the legal questions, instead opting to talk about why it's important to keep the app design simple.
When the lawyer asked again what he would do if the government tried to compel him to spy on his users, Joshua simply said, "I'd just tell them to go fuck themselves." It's a good answer, but it's also naive. Government requests can include gag orders, preventing him from telling anyone that he has received them, and punishment for disobeying them can include threats of jail time. It's good to plan ahead. Luckily, he has EFF and ACLU offering him legal support, in case he ever actually has to face something like this.
It's not too late
Despite everything, I do think that Joshua's heart is in the right place and that he genuinely wants to help people. He's sticking his neck out to fight fascism, and the far right is harassing him and his family for it.
This is why I, and several other hackers who attended his HOPE talk, spent so much time and energy (both during his talk and in the days after it) trying to encourage him to open things up so that ICEBlock, and its million-strong userbase, might yet become a helpful tool in defending immigrants against Trump's fascist plans. He has rejected our offers.
It's possible for him to turn things around, but sadly, I'm not holding my breath.
Sign up for micahflee
Hi, I'm Micah. I'm a coder, a journalist, and I help people stay private and secure.
No spam. Unsubscribe anytime.
