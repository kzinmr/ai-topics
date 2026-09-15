---
title: "Could rogue agent swarms take over the entire internet in the next six months?"
url: "https://garymarcus.substack.com/p/could-rogue-agent-swarms-take-over"
fetched_at: 2026-09-13T10:01:14.199391+00:00
source: "garymarcus.substack.com"
tags: [blog, raw]
---

# Could rogue agent swarms take over the entire internet in the next six months?

Source: https://garymarcus.substack.com/p/could-rogue-agent-swarms-take-over

Could rogue agent swarms take over the entire internet in the next six months? Dario Amodei seems to think so.
Or at least Axios thinks he thinks so, based on Amodei’s new essay.
Dario Amodei warned in an essay that swarms of rogue AI agents could take over the internet in as little as six months from now.
BREAKING: Anthropic CEO calls for immediate slowdown in AI development
https://t.co/4rvLlmLFHN
2:41 PM · Sep 12, 2026
·
257K Views
75 Replies
·
261 Reposts
·
1.03K Likes
We think that’s (a) a vague claim, and (b) pretty implausible as best we can understand it. But in fairness also not exactly what Dario said. Let’s unpack it all.
First, taking down (or taking over) the internet altogether is really, really hard.  Gizmodo had
a great article
about this back in 2019 gathering many perspectives, and mostly arguing no. Some samples of the comments from people they interviewed:
and
What about Dario himself, and has anything changed?
Amodei’s new essay starts with hype-farming. He starts off talking about curing most major diseases in the next 5–10 years and creating a world of abundance. Obviously, with no specifics, because specifics would kill the vibes. As one of us (Gary) wrote recently, curing major disease is completely implausible; the abundance stuff doesn’t seem too likely, either. Here’s what he wrote on the vulnerability of the internet.
“Taking over the entire internet” is, once again, immense in scope yet so vague it hurts.
Taking over how? To do what? To claim the “entire” internet is vulnerable is all but nonsensical, because that’s just not how the internet works. It is true that some companies, for example, Cloudflare, Google, and AWS, have an outsized impact on the internet, so when they go down, many apps go down at the same time.  Despite this centralization, it seems highly unlikely they could all be taken down at once.
Even if all three were down (or “taken over”, whatever that means), the internet as a whole would continue, though obviously impaired. And it’s worth noting that all three of those companies have much more professional security than the average website. A report on Mythos by the British agency AISI said that Mythos could “autonomously compromise [only] small, weakly defended vulnerable systems”. Even with continued advances we are not at all sure that any of those big three could be taken down or controlled for a prolonged period of time (other than through government force).
Then there is the question of motive.
Why
would anyone do this? What’s the goal of taking down (or taking over) the entire internet? If it were fully down, sites would be down for attackers too.
And people forget that attackers have goals and budgets of their own. How does taking out the entire internet make them money? Who would be footing the bill for this? We are talking about many many millions of dollars. You may be able to steal resources from some of the victims, but probably not on the scale required.
And how exactly would the attack
agents
coordinate at that point? Seems kind of absurd when you look at the details. We get the sense that Amodei has not really thought this through.
§
Botnets, which Amodei referenced, are most often used for denial-of-service attacks and to send spam and phishing emails. They are made up of compromised machines operating on other people’s networks. But in this case, the botnet would be comprised of actual AI bots (we doubt he means sending more fake bank logins or ads for Viagra). So what does he think would actually happen? And where would these bots be running? If each of them demands its very own giant frontier model to cause mayhem, it’s pretty unclear how that happens without extreme negligence on the part of the labs themselves.
We also wonder: is Amodei saying Frontier AI will take over the internet? As far as we know, no one has frontier AI but Anthropic and OpenAI so it’s almost like he’s saying “maybe we will REALLY mess up”; if they do we really ought to shut them down for sheer negligence. They really should be able to guard against their own software being abused in this way, or they shouldn’t make it available.
§
All that said, we don’t think Amodei’s concerns should be dismissed entirely, even if we do think they should be taken with a large shaker of salt.
First, his announcement should serve as a reminder that, for decades, many companies have been getting away without putting an appropriate amount of emphasis on cybersecurity. Google, AWS, and Cloudflare are hardened, but many sites are not.  This leaves quite a bit of low-hanging fruit begging to be picked. A lot of individual sites will be attacked, even if the internet itself is very unlikely to crumble.
Second, things could change. Right now, doing anything like what Amodei envisions is likely to be insanely expensive, and probably could only be done on the cloud, to the extent that it could be done at all. One would hope that the cloud providers, and the LLM model providers that run on top, would have enough good sense to have enough monitoring in place to keep this kind of large-scale attack from happening, especially post the Hugging Face incident. In the worst case, if it’s all running in a giant data center that we can identify, maybe we can shut it down.  But as models get optimized and local hardware improves, more and more devious things will be feasible
without
going out to giant data centers. So we should absolutely still keep an eye on all this.
For now, we don’t find Dario’s claim particularly plausible. The six month part is silly.
But it’s all still more reason to restrict any AI that cannot be closely monitored, and more reason to ask why we are allowing all these hard-to-control agents out onto the internet in the first place.
Share
Gary Marcus,
Professor Emeritus at NYU, and Founder of Geometric Intelligence (acquired by Uber) has warned repeatedly about the risk of agents to cybersecurity, and is author of six books including
Taming Silicon Valley.
Nathan Hamiel
, Senior Director of Research at Kudelski Security, focusing on emerging and disruptive technologies and their intersection with information security, and writes the blog Perilous.tech. At Black Hat, he serves as the AI, ML, and Data Science track lead.
Zach Korman
, CEO and co-founder of
Embroidery
, an AI agent monitoring and detection platform; he is well-known for his work in the application of AI to cybersecurity.
