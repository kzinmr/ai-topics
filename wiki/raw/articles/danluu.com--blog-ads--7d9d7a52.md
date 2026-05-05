---
title: "Blog monetization"
url: "https://danluu.com/blog-ads/"
fetched_at: 2026-05-05T07:01:33.932163+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Blog monetization

Source: https://danluu.com/blog-ads/

Does it make sense for me to run ads on my blog? I've been thinking about this lately, since Carbon Ads contacted me about putting an ad up. What are the pros and cons? This isn't a rhetorical question. I'm genuinely
interested in what you think
.
Pros
Money
Hey, who couldn't use more money? And it's basically free money. Well, except for the all of the downsides.
Data
There's lots of studies on the impact of ads on site usage and behavior. But as with any sort of benchmarking, it's not really clear how or if that generalizes to other sites if you don't have a deep understanding of the domain, and I have almost no understanding of the domain. If I run some ads and do some A/B testing I'll get to see what the effect is on my site, which would be neat.
Cons
Money
It's not enough money to make a living off of, and it's never going to be. When Carbon contacted me, they asked me how much traffic I got in the past 30 days. At the time, Google Analytics showed 118k sessions, 94k users, 143k page views. Cloudflare tends to show about 20% higher traffic since 20% of people block Google Analytics, but those 20% plus more probably block ads, so the "real" numbers aren't helpful here. I told them that, but I also told them that those numbers were pretty unusual and that I'd expect to average much less traffic.
How much money is that worth? I don't know if the CPM (cost per thousand impressions) numbers they gave me are confidential, so I'll just use a current standard figure of $1 CPM. If my traffic continued at that rate, that would be $143/month, or $1,700/year. Ok, that's not too bad.
But let's look at the traffic since I started this blog. I didn't add analytics until after a post of mine got passed around on HN and reddit, so this isn't all of my traffic, but it's close.
For one thing, the 143k hits over a 30-day period seems like a fluke. I've never had a calendar month with that much traffic. I just happen to have a traffic distribution which turned up a bunch of traffic over a specific 30-day period.
Also, if I stop blogging, as I did from April to October, my traffic level drops to pretty much zero. And even if I keep blogging, it's not really clear what my “natural” traffic level is. Is the level before I paused my blogging the normal level or the level after? Either way, $143/month seems like a good guess for an upper bound. I might exceed that, but I doubt it.
For a hard upper bound, let's look at one of the most widely read programming blogs, Coding Horror. Jeff Atwood is nice enough to make his traffic stats available. Thanks Jeff!
He got 1.7M hits in his best month, and 1.25M wouldn't be a bad month for him, even when he was blogging regularly. With today's CPM rates, that's $1.7k/month at his peak and $1.25k/month for a normal month.
But Jeff Atwood blogs about general interest programming topics, like
Markdown
and
Ruby
and I blog about obscure stuff, like
why Intel might want to add new instructions to speed up non-volatile storage
with the occasional
literature review
for variety. There's no way I can get as much traffic as someone who blogs about more general interest topics; I'd be surprised if I could even get within a factor of 2, so $600/month seems like a hard and probably unreachable upper bound for sustainable income.
That's not bad. After taxes, that would have approximately covered my rent when I lived in Austin, and could have covered rent + utilities and other expenses if I'd had a roommate. But the wildly optimistic success rate is that you barely cover rent when the programming job market is hot enough that mid-level positions at big companies pay out total compensation that's 8x-9x the median income in the U.S. That's not good.
Worse yet, this is getting worse over time. CPM is down something like 5x since the 90s, and continues to decline. Meanwhile, the percentage of people using ad blockers continues to increase.
Premium ads can get well over an order of magnitude higher CPM and
sponsorships can fetch an ever better return
, so the picture might not be quite as bleak as I'm making it out to be. But to get premium ads you need to appeal to specific advertisers. What advertisers are interested in an audience that's mostly programmers with an interest in low-level shenanigans? I don't know, and I doubt it's worth the effort to find out unless I can get to Jeff Atwood levels of traffic, which I find unlikely.
A Tangent on Alexa Rankings
What's up with Alexa? Why do so many people use it as a gold standard? In theory, it's supposed to show how popular a site was over the past three months. According to Alexa, Coding Horror is ranked at 22k and I'm at 162k. My understanding is that traffic is more than linear in rank so you'd expect Coding Horror to have substantially more than 7x the traffic that I do. But if you compare Jeff's stats to mine over the past three months (Oct 21 - Jan 21), statcounter claims he's had 78k hits compared to my 298k hits. Even if you assume that traffic is merely linear in Alexa rank, that's a 28x difference in relative traffic between the direct measurement and Alexa's estimate.
I'm not claiming that my blog is more popular in any meaningful sense -- if Jeff posted as often as I did in the past three months, I'm sure he'd have at least 10x more traffic than me. But given that Jeff now spends most of his time on non-blogging activities and that his traffic is at the level it's at when he rarely blogs, the Alexa ranks for our sites seem way off.
Moreover, the Alexa sub-metrics are inconsistent and nonsensical. Take this graph on the relative proportion of users who use this site from home, school, or work.
It's below average in every category, which should be impossible for a relative ranking like this. But even mathematical impossibility doesn't stop Alexa!
Traffic
Ads reduce traffic. How much depends both on the site and the ads. I might do a literature review some other time, but for now I'm just going to link to this single result by
Daniel G. Goldstein, Siddharth Suri, R. Preston McAfee, Matthew Ekstrand-Abueg, and Fernando Diaz
that attempts to quantify the cost.
My point isn't that some specific study applies to adding a single ad to my site, but that it's well known that adding ads reduces traffic and has some effect on long-term user behavior, which has some cost.
It's relatively easy to quantify the cost if you're looking at something like the study above, which compares “annoying” ads to “good” ads to see what the cost of the “annoying” ads are. It's harder to quantify for a personal blog where the baseline benefit is non-monetary.
What do I get out of this blog, anyway? The main benefits I can see are that I've met and regularly correspond with some great people I wouldn't have otherwise met, that I often get good feedback on my ideas, and that every once in a while someone pings me about a job that sounds interesting because they saw a relevant post of mine.
I doubt I can effectively estimate the amount of traffic I'll lose, and even if I could, I doubt I could figure out the relationship between that and the value I get out of blogging. My gut says that the value is “a lot” and that the monetary payoff is probably “not a lot”, but it's not clear what that means at the margin.
Incentives
People are influenced by money, even when they don't notice it. I'm people. I might do something to get more revenue, even though the dollar amount is small and I wouldn't consciously spend a lot of effort of optimizing things to get an extra $5/month.
What would that mean here? Maybe I'd write more blog posts? When I experimented with blurting out blog posts more frequently, with less editing, I got uniformly positive feedback, so maybe being incentivized to write more wouldn't be so bad. But I always worry about unconscious bias and I wonder what other effects running ads might have on me.
Privacy
Ad networks can track people through ads. My impression is that people are mostly concerned with really big companies that have enough information that they could deanonymize people if they were so inclined, like Google and Facebook, but some people are probably also concerned about smaller ad networks like Carbon. Just as an aside, I'm curious if companies that attempt to do lots of tracking, like Tapad and MediaMath actually have more data on people than better known companies like Yahoo and eBay. I doubt that kind of data is publicly available, though.
Paypal
This is specific to Carbon, but they pay out through PayPal, which is notorious for freezing funds for six months if you get enough money that you'd actually want the money, and for pseudo-randomly
draining your bank account due to clerical errors
. I've managed to avoid hooking my PayPal account up to my bank account so far, but I'll have to either do that or get money out through an intermediary if I end up making enough money that I want to withdraw it.
Conclusion
Is running ads worth it? I don't know. If I had to guess, I'd say no. I'm going to try it anyway because I'm curious what the data looks like, and I'm not going to get to see any data if I don't try something, but it's not like that data will tell me whether or not it was worth it.
At best, I'll be able to see a difference in click-through rates on my blog with and without ads. This blog mostly spreads through word of mouth, so what I really want to see is the difference in the rate at which the blog gets shared with other people, but I don't see a good way to do that. I could try globally enabling or disabling ads for months at a time, but the variance between months is so high that I don't know that I'd get good data out of that even if I did it for years.
Thanks to Anja Boskovic for comments/corrections/discussion.
Update
After running an ads for a while, it looks like about 40% of my traffic uses an ad blocker (whereas about 17% of my traffic blocks Google Analytics). I'm not sure if I should be surprised that the number is so high or that it's so low. On the one hand, 40% is a lot! On the other hand, despite complaints that ad blockers slow down browsers, my experience has been that web pages load a lot faster when I'm blocking ads using the right ad blocker and I don't see any reason not to use an blocker. I'd expect that most of my traffic comes from programmers, who all know that ad blocking is possible.
There's the argument that ad blocking is piracy and/or stealing, but I've never heard a convincing case made. If anything, I think that some of the people who make that argument step over the line, as when ars technica blocked people who used ad blockers, and then backed off and merely exhorted people to disable ad blocking for their site. I think most people would agree that directly exhorting people to click on ads and commit click fraud is unethical; asking people to disable ad blocking is a difference in degree, not in kind. People who use ad blockers are much less likely to click on ads, so having them disable ad blockers to generate impressions that are unlikely to convert strikes me as pretty similar to having people who aren't interested in the product generate clicks.
Anyway, I ended up removing this ad after they failed to send a payment after the first payment. AdSense is rumored to wait until just before payment before cutting people off, to get as many impressions as possible for free, but AdSense at least notifies you about it. Carbon just stopped paying without saying anything, while still running the ad. I could probably ask someone at Carbon or BuySellAds about it, but considering how little the ad is worth, it's not really worth the hassle of doing that.
Update 2
It's been almost two years since I said that I'd never get enough traffic for blogging to be able to cover my living expenses. It turns out that's not true! My reasoning was that I mostly tend to blog about low-level technical topics, which can't possibly generate enough traffic to generate "real" ad revenue. That reason is still as valid as ever, but my blogging is now approximately half low-level technical stuff, and half general-interest topics for programmers.
Here's a graph of my traffic for the past 30 days (as of October 25th, 2016). Since this is Cloudflare's graph of requests, this would wildly overestimate traffic for most sites, because each image and CSS file is one request. However, since the vast majority of my traffic goes to pages with no external CSS and no images, this is pretty close to my actual level of traffic. 15% of the requests are images, and 10% is RSS (which I won't count because the rate of RSS hits is hard to correlation to the rate of actual people reading). But that means that 75% of the traffic appears to be "real", which puts the traffic into this site at roughly 2.3M hits per month. At a typical $1 ad CPM, that's $2.3k/month, which could cover my share of household expenses.
Additionally, when I look at blogs that really try to monetize their traffic, they tend to monetize at a much better rate. For example,
Slate Star Codex charges $1250 for 6 months of ads and appears to be running 8 ads
, for a total of $20k/yr. The author claims to get "10,000 to 20,000 impressions per day", or roughly 450k hits per month. I get about 5x that much traffic. If we scale that linearly, that might be $100k/yr instead of $20k/yr. One thing that I find interesting is that the ads on Slate Star Codex don't get blocked by my ad blocker. It seems like that's because the author isn't part of some giant advertising program, and ad blockers don't go out of their way to block every set of single-site custom ads out there. I'm using Slate Star Codex as an example because I think it's not super ad optimized because I doubt I would optimize my ads much if I ran ads.
This is getting to the point where it seems a bit unreasonable not to run ads (I doubt the non-direct value I get out of this blog can consistently exceed $100k/yr). I probably "should" run ads, but I don't think the revenue I get from something like AdSense or Carbon is really worth it, and it seems like a hassle to run my own ad program the way Slate Star Codex does. It seems totally irrational to leave $90k/yr on the table because "it seems like a hassle", but here we are. I went back and added affiliate code to all of my Amazon links, but if I'm estimating Amazon's payouts correctly, that will amount to less than $100/month.
I don't think it's necessarily more irrational than behavior I see from other people -- I regularly talk to people who leave $200k/yr or more on the table by working for startups instead of large companies, and that seems like a reasonable preference to me. They make "enough" money and like things the way they are. What's wrong with that? So why can't not running ads be a reasonable preference? It still feels pretty unreasonable to me, though! A few people have suggested crowdfunding, but the top earning programmers have at least an order of magnitude more exposure than I do and make an order of magnitude less than I could on ads (folks like Casey Muratori, ESR, and eevee are pulling in around $1000/month).
Update 3
I'm now trying
donations via Patreon
. I suspect this won't work, but I'd be happy to be wrong!
