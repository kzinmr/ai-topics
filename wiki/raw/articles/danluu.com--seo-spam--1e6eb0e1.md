---
title: "How bad are search results? Let's compare Google, Bing, Marginalia, Kagi, Mwmbl, and ChatGPT"
url: "https://danluu.com/seo-spam/"
fetched_at: 2026-05-05T07:01:29.126277+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# How bad are search results? Let's compare Google, Bing, Marginalia, Kagi, Mwmbl, and ChatGPT

Source: https://danluu.com/seo-spam/

In
The birth & death of search engine optimization
, Xe suggests
Here's a fun experiment to try. Take an open source project such as
yt-dlp
and try to find it from a very generic term like "youtube downloader". You won't be able to find it because of all of the content farms that try to rank at the top for that term. Even though
yt-dlp
is probably actually what you want for a tool to download video from YouTube.
More generally, most tech folks I'm connected to seem to think that Google search results are significantly worse than they were ten years ago (
Mastodon poll
,
Twitter poll
,
Threads poll
). However, there's a sizable group of vocal folks who claim that search results are still great. E.g., a bluesky thought leader who gets high engagement says:
i think the rending of garments about how even google search is terrible now is pretty overblown
I suspect what's going on here is that some people have gotten so used working around bad software that they don't even know they're doing it, reflexively doing the modern equivalent of
hitting ctrl+s all the time in editors, or ctrl+a; ctrl+c when composing anything in a text box
. Every adept user of the modern web has a bag of tricks they use to get decent results from queries. From having watched quite a few users interact with computers, that doesn't appear to be normal, even among people who are quite competent in various technical fields, e.g., mechanical engineering. However, it could be that people who are complaining about bad search result quality are
just hopping on the "everything sucks" bandwagon and making totally unsubstantiated comments
about search quality.
Since it's fairly easy to try out straightforward, naive, queries, let's try some queries. We'll look at three kinds of queries with five search engines plus ChatGPT and we'll turn off our ad blocker to get
the non-expert browsing experience
. I once had a computer get owned from browsing to a website with a shady ad, so I hope that doesn't happen here (in that case, I was lucky that I could tell that it happened because the malware was doing so much stuff to my computer that it was impossible to not notice).
One kind of query is a selected set of representative queries a friend of mine used to set up her new computer. My friend is a highly competent engineer outside of tech and wanted help learning "how to use computers", so I watched her try to set up a computer and pointed out holes in her mental model of how to interact with websites and software.
The second kind of query is queries for the kinds of things I wanted to know in high school where I couldn't find the answer because everyone I asked (teachers, etc.) gave me obviously incorrect answers and I didn't know how to find the right answer. I was able to get the right answer from various textbooks once I got to college and had access to university libraries, but the questions are simple enough that there's no particular reason a high school student shouldn't be able to understand the answers; it's just an issue of finding the answer, so we'll take a look at how easy these answers are to find. The third kind of query is a local query for information I happened to want to get as I was writing this post.
In grading the queries, there's going to be some subjectivity here because, for example, it's not objectively clear if it's better to have moderately relevant results with no scams or very
relevant results mixed interspersed with scams that try to install badware or trick you into giving up your credit card info to pay for something you shouldn't pay for
. For the purposes of this post, I'm considering scams to be fairly bad, so in that specific example, I'd rate the moderately relevant results above the very relevant results that have scams mixed in. As with my
other
posts
that
have some kind of subjective ranking, there's both a short summary as well as a detailed description of results, so you can rank services yourself, if you like.
In the table below, each column is a query and each row is a search engine or ChatGPT. Results are rated (from worst to best) Terrible, Very Bad, Bad, Ok, Good, and Great, with worse results being more red and better results being more blue.
The queries are:
download youtube videos
ad blocker
download firefox
Why do wider tires have better grip?
Why do they keep making cpu transistors smaller?
vancouver snow forecast winter 2023
YouTube
Adblock
Firefox
Tire
CPU
Snow
Marginalia
Ok
Good
Ok
Bad
Bad
Bad
ChatGPT
V. Bad
Great
Good
V. Bad
V. Bad
Bad
Mwmbl
Bad
Bad
Bad
Bad
Bad
Bad
Kagi
Bad
V. Bad
Great
Terrible
Bad
Terrible
Google
Terrible
V. Bad
Bad
Bad
Bad
Terrible
Bing
Terrible
Terrible
Great
Terrible
Ok
Terrible
Marginalia does relatively well by sometimes providing decent but not great answers and then providing no answers or very obviously irrelevant answers to the questions it can't answer, with a relatively low rate of scams, lower than any other search engine (although, for these queries, ChatGPT returns zero scams and Marginalia returns some).
Interestingly, Mwmbl lets users directly edit search result rankings. I did this for one query, which would score "Great" if it was scored after my edit, but
it's easy to do well on a benchmark when you optimize specifically for the benchmark
, so Mwmbl's scores are without my edits to the ranking criteria.
One thing I found interesting about the Google results was that, in addition to Google's noted propensity to return recent results, there was a strong propensity to return recent youtube videos. This caused us to get videos that seem quite useless for anybody, except perhaps the maker of the video, who appears to be attempting to get ad revenue from the video. For example, when searching for "ad blocker", one of the youtube results was a video where the person rambles for 93 seconds about how you should use an ad blocker and then googles "ad blocker extension". They then click on the first result and incorrectly say that "it's officially from Google", i.e., the ad blocker is either made by Google or has some kind of official Google seal of approval, because it's the first result. They then ramble for another 40 seconds as they install the ad blocker. After it's installed, they incorrectly state "this is basically one of the most effective ad blocker [sic] on Google Chrome". The video has 14k views. For reference, Steve Yegge spent a year making high-effort videos and his most viewed video has 8k views, with a typical view count below 2k. This person who's gaming the algorithm by making low quality videos on topics they know nothing about, who's part of the cottage industry of people making videos taking advantage of Google's algorithm prioritizing recent content regardless of quality, is dominating Steve Yegge's videos because they've found search terms that you can rank for if you put anything up. We'll discuss other Google quirks in more detail below.
ChatGPT does its usual thing and impressively outperforms its more traditional competitors in one case, does an ok job in another case, refuses to really answer the question in another case, and "hallucinates" nonsense for a number of queries (as usual for ChatGPT, random perturbations can significantly change the results). It's common to criticize ChatGPT for its hallucinations and, while I don't think that's unfair,
as we noted in this 2015, pre-LLM post on AI
, I find this general class of criticism to be overrated in that humans and traditional computer systems make the exact same mistakes.
In this case, search engines return various kinds of hallucinated results. In the snow forecast example, we got deliberately fabricated results, one intended to drive ad revenue through shady ads on a fake forecast site, and another intended to trick the user into thinking that the forecast indicates a cold, snowy, winter (the opposite of the actual forecast), seemingly in order to get the user to sign up for unnecessary snow removal services. Other deliberately fabricated results include a site that's intended to look like an objective review site that's actually a fake site designed to funnel you into installing a specific ad blocker, where the ad blocker they funnel you to appears to be a scammy one that tries to get you to pay for ad blocking and doesn't let you unsubscribe, a fake "organic" blog post trying to get you to install a chrome extension that exposes all of your shopping to some service (in many cases, it's not possible to tell if a blog post is a fake or shill post, but in this case, they hosted the fake blog post on the domain for the product and, although it's designed to look like there's an entire blog on the topic, there isn't — it's just this one fake blog post), etc.
There were also many results which don't appear to be deliberately fraudulent and are just run-of-the-mill SEO garbage designed to farm ad clicks. These seem to mostly be pre-LLM sites, so they don't read quite like ChatGPT hallucinations, but they're not fundamentally different. Sometimes the goal of these sites is to get users to click on ads that actually scam the user, and sometimes the goal appears to be to generate clicks to non-scam ads. Search engines also returned many seemingly non-deliberate human hallucinations, where people confidently stated incorrect answers in places where user content is highlighted, like quora, reddit, and stack exchange.
On these queries, even ignoring anything that looks like LLM-generated text, I'd rate the major search engines (Google and Bing) as somewhat worse than ChatGPT in terms of returning various kinds of hallucinated or hallucination-adjacent results. While I don't think concerns about LLM hallucinations are illegitimate,
the traditional ecosystem has the problem that the system highly incentivizes putting whatever is most profitable for the software supply chain in front of the user
which is, in general, quite different from the best result.
For example, if your app store allows "you might also like" recommendations, the most valuable ad slot for apps about gambling addiction management will be gambling apps. Allowing gambling ads on an addiction management app is too blatantly user-hostile for any company deliberately allow today, but of course companies that make gambling apps will try to game the system to break through the filtering and
they sometimes succeed
. And for web search, I just tried this again on the web and one of the two major search engines returned, as a top result, ad-laden SEO blogspam for addiction management. At the top of the page is a multi-part ad, with the top two links being "GAMES THAT PAY REAL MONEY" and "GAMES THAT PAY REAL CASH". In general, I was getting localized results (lots of .ca domains since I'm in Canada), so you may get somewhat different results if you try this yourself.
Similarly, if the best result is a good, free, ad blocker like ublock origin, the top ad slot is worth a lot more to a company that makes an ad blocker designed to trick you into paying for a lower quality ad blocker with a nearly-uncancellable subscription, so the scam ad blocker is going to outbid the free ad blocker for the top ad slots. These kinds of companies also have a lot more resources to spend on direct SEO, as well as indirect SEO activities like marketing so, unless search engines mount a more effective effort to combat the profit motive, the top results will go to paid ad blockers even though the paid ad blockers are generally significantly worse for users than free ad blockers. If you talk to people who work on ranking, a lot of the biggest ranking signals are derived from clicks and engagement, but
this will only drive users to the best results when users are sophisticated enough to know what the best results are, which they generally aren't
. Human raters also rate page quality, but this has the exact same problem.
Many Google employees have told me that ads are actually good because they inform the user about options the user wouldn't have otherwise known about, but anyone who tries browsing without an ad blocker will see ads that are various kinds of misleading, ads that try to trick or entrap the user in various ways, by pretending to be a window, or advertising "GAMES THAT PAY REAL CASH" at the top of a page on battling gambling addiction, which has managed to SEO itself to a high ranking on gambling addiction searches. In principle, these problems could be mitigated with enough resources, but we can observe that trillion dollar companies have chosen not to invest enough resources combating SEO, spam, etc., that these kinds of scam ads are rarely seen. Instead, a number of top results are actually ads that direct you to scams.
In their original Page Rank paper, Sergei Brin and Larry Page noted that ad-based search is inherently not incentive aligned with providing good results:
Currently, the predominant business model for commercial search engines is advertising. The goals of the advertising business model do not always correspond to providing quality search to users. For example, in our prototype search engine one of the top results for cellular phone is "The Effect of Cellular Phone Use Upon Driver Attention", a study which explains in great detail the distractions and
risk associated with conversing on a cell phone while driving. This search result came up first because of its high importance as judged by the PageRank algorithm, an approximation of citation importance on the web [Page, 98]. It is clear that a search engine which was taking money for showing cellular phone
ads would have difficulty justifying the page that our system returned to its paying advertisers. For this type of reason and historical experience with other media [Bagdikian 83], we expect that advertising funded search engines will be inherently biased towards the advertisers and away from the needs of the Consumers.
Since it is very difficult even for experts to evaluate search engines, search engine bias is particularly insidious. A good example was OpenText, which was reported to be selling companies the right to be listed at the top of the search results for particular queries [Marchiori 97]. This type of bias is much more insidious than advertising, because it is not clear who "deserves" to be there, and who is willing to pay money to be listed. This business model resulted in an uproar, and OpenText has ceased to be a viable search engine. But less blatant bias are likely to be tolerated by the market. ... This type of bias is very difficult to detect but could still have a significant effect on the market. Furthermore, advertising income often provides an incentive to provide poor quality search results. For example, we noticed a major search engine would not return a large airline’s homepage when the airline’s name was given as a query. It so happened that the airline had placed an expensive ad, linked to the query that was its name. A better search engine would not have required this ad, and possibly resulted in the loss of the revenue from the airline to the search engine. In general, it could be argued from the consumer point of view that the better the search engine is, the fewer advertisements will be needed for the consumer to find what they want. This of course erodes the advertising supported business model of the existing search engines ... we believe the issue of advertising causes enough mixed incentives that it is crucial to have a competitive search engine that is transparent and in the academic realm.
Of course, Google is now dominated by ads and, despite specifically calling out the insidiousness of user conflating real results with paid results,
both Google and Bing have made ads look more and more like real search results
, to the point that most users usually won't know that they're clicking on ads and not real search results. By the way, this propensity for users to think that everything is an "organic" search result is the reason that, in this post, results are ordered by the order the appear on the page, so if four ads appear above the first organic result, the four ads will be rank 1-4 and the organic result will be ranked 5. I've heard Google employees say that AMP didn't impact search ranking because it "only" controlled what results went into the "carousel" that appeared above search results, as if inserting a carousel and then a bunch of ads above results, pushing results down below the fold, has no impact on how the user interacts with results. It's also common to see search engines ransoming the top slot for companies, so that companies that don't buy the ad for their own name end up with searches for that company putting their competitors at the top, which is also said to not impact search result ranking, a technically correct claim that's basically meaningless to the median user.
When I tried running the query from the paper, "cellular phone" (no quotes) and, the top result was a Google Store link to buy Google's own Pixel 7, with the rest of the top results being various Android phones sold on Amazon. That's followed by the Wikipedia page for Mobile Phone, and then a series of commercial results all trying to sell you phones or SEO-spam trying to get you to click on ads or buy phones via their links (the next 7 results were commercial, with the next result after that being an ad-laden SEO blogspam page for the definition of  a cell phone with ads of cell phones on it, followed by 3 more commercial results, followed by another ad-laden definition of a phone). The commercial links seem very low quality, e.g., the top link below the carousel after wikipedia is Best Buy's Canadian mobile phone page. The first two products there are an ad slots for eufy's version of the AirTag. The next result is for a monthly financed iPhone that's tied to Rogers, the next for a monthly financed Samsung phone that's tied to TELUS, then we have Samsung's AirTag, an monthly financed iPhone tied to Freedom Mobile, a monthly financed iPhone tied to Freedom mobile in a different color, a monthly financed iPhone tied to Rogers, a screen protector for the iPhone 13, another Samsung AirTag product, an unlocked iPhone 12, a Samsung wall charger, etc.; it's an extremely low quality result with products that people shouldn't be buying (and, based on the number of reviews, aren't buying — the modal number of reviews of the top products is 0 and the median is 1 or 2 even though there are plenty of things people do actually buy from Best Buy Canada and plenty of products that have lots of reviews). The other commercial results that show up are also generally extremely low quality results. The result that Sergei and Larry suggested was a great top result, "The Effect of Cellular Phone Use Upon Driver Attention", is nowhere to be seen, buried beneath an avalanche of commercial results. On the other side of things, Google has also gotten into the action by buying ads that trick users,
such as  paying for an installer to try to trick users into installing Chrome over Firefox
.
Anyway, after looking at the results of our test queries, some questions that come to mind are:
How is Marginalia, a search engine built by a single person, so good?
Can Marginalia or another small search engine displace Google for mainstream users?
Can a collection of small search engines provide better results than Google?
Will Mwmbl's user-curation approach work?
Would a search engine like 1996-Metacrawler, which aggregates results from multiple search engines, ChatGPT, Bard, etc., significantly outperform Google?
The first question could easily be its own post and this post is already 17000 words, so maybe we'll examine it another time. We've previously noted that
some
individuals
can
be very productive, but of course the details vary in each case.
On the second question,
we looked at a similar question in 2016
, both the general version, "I could reproduce this billion dollar company in a weekend", as well as specific comments about how open source software would make it trivial to surpass Google any day now, such as
Nowadays, most any technology you need is indeed available in OSS and in state of the art. Allow me to plug meta64.com (my own company) as an example. I am using Lucene to index large numbers of news articles, and provide search into them, by searching a Lucene index generated by simple scraping of RSS-crawled content. I would claim that the Lucene technology is near optimal, and this search approach I'm using is nearly identical to what a Google would need to employ. The only true technology advantage Google has is in the sheer number of servers they can put online, which is prohibitively expensive for us small guys. But from a software standpoint, Google will be overtaken by technologies like mine over the next 10 years I predict.
and
Scaling things is always a challenge but as long as Lucene keeps getting better and better there is going to be a point where Google's advantage becomes irrelevant and we can cluster Lucene nodes and distribute search related computations on top and then use something like Hadoop to implement our own open source ranking algorithms. We're not there yet but technology only gets better over time and the choices we as developers make also matter. Even though Amazon and Google look like unbeatable giants now don't discount what incremental improvements can accomplish over a long stretch of time and in technology it's not even that long a stretch. It wasn't very long ago when Windows was the reigning champion. Where is Windows now?
In that 2016 post, we saw that people who thought that open source solutions were set to surpass Google any day now appeared to have no idea how many hard problems must be solved to make a mainstream competitor to Google, including real-time indexing of rapidly-updated sites, like Twitter, newspapers, etc., as well as table-stakes level NLP, which is extremely non-trivial. Since 2016, these problems have gotten significantly harder as there's more real-time content to index and users expect much better NLP. The number of things people expect out of their search engine has increased as well, making the problem harder still, so it still appears to be quite difficult to displace Google as a mainstream search engine for, say, a billion users.
On the other hand, if you want to make a useful search engine for a small number of users, that seems easier than ever because Google returns worse results than it used to for many queries. In our test queries, we saw a number of queries where many or most top results were filled with SEO garbage, a problem that was significantly worse than it was a decade ago, even before the rise of LLMs and that continues to get worse. I typically use search engines in a way that doesn't run into this, but when I look at what "normal" users query or if I try naive queries myself, as I did in this post, most results are quite poor, which didn't used to be true.
Another place Google now falls over for me is when finding non-popular pages. I often find that, when I want to find a web page and I correctly remember the contents of the page, even if I do an exact string search, Google won't return the page. Either the page isn't indexed, or the page is effectively not indexed because it lives in some slow corner of the index that doesn't return in time. In order to find the page, I have to remember some text in a page that links to the page (often many clicks removed from the actual page, not just one, so I'm really remembering a page that links to a page that links to a page that links to a page that links to a page and then using archive.org to traverse the links that are now dead), search for that, and then manually navigate the link graph to get to the page. This basically never happened when I searched for something in 2005 and rarely happened in 2015, but this now happens a large fraction of the time I'm looking for something. Even in 2015, Google wasn't actually comprehensive. Just for example, Google search didn't index every tweet. But, at the time, I found Google search better at searching for tweets than Twitter search and I basically never ran across a tweet I wanted to find that wasn't indexed by Google. But now, most of the tweets I want to find aren't returned by Google search, even when I search for "[exact string from tweet] site:twitter.com". In the original Page Rank paper, Sergei and Larry said "Because humans can only type or speak a finite amount, and as computers continue improving, text indexing will scale even better than it does now." (and that, while machines can generate an effectively infinite amount of content, just indexing human-generated content seems very useful). Pre-LLM, Google certainly had the resources to index every tweet as well as every human generated utterance on every public website, but they seem to have chosen to devote their resources elsewhere and, relative to its size, the public web appears less indexed than ever, or at least less indexed than it's been since the very early days of web search.
Back when Google returned decent results for simple queries and indexed almost any public page I'd want to find, it would've been very difficult for an independent search engine to return results that I find better than Google's. Marginalia in 2016 would've been nothing more than a curiosity for me since Google would give good-enough results for basically anything where Marginalia returns decent results, and Google would give me the correct result in queries for every obscure page I searched for, something that would be extremely difficult for a small engine. But now that Google effectively doesn't index many pages I want to search for, the relatively small indices that independent search engines have doesn't make them non-starters for me and some of them return less SEO garbage than Google, making them better for my use since I generally don't care about real-time results, don't need fancy NLP (and find that much of it actually makes search results worse for me), don't need shopping integrated into my search results, rarely need image search with understanding of images, etc.
On the question of whether or not a collection of small search engines can provide better results than Google for a lot of users, I don't think this is much of a question because the answer has been a resounding "yes" for years. However, many people don't believe this is so. For example, a Google TLM replied to the bluesky thought leader at the top of this post with
Somebody tried argue that if the search space were more competitive, with lots of little providers instead of like three big ones, then somehow it would be *more* resistant to ML-based SEO abuse.
And... look, if *google* can't currently keep up with it, how will Little Mr. 5% Market Share do it?
presumably referring to arguments like
Hillel Wayne's "Algorithm Monocultures"
, to which our bluesky thought leader replied
like 95% of the time, when someone claims that some small, independent company can do something hard better than the market leader can, it’s just cope. economies of scale work pretty well!
In the past,
we looked at some examples where the market leader provides a poor product and various other players, often tiny, provide better products
and in a future post, we'll look at how economies of scale and diseconomies of scale interact in various areas for tech but, for this post, suffice it to say that it's clear that despite the common "econ 101"
cocktail party idea
that economies of scale should be the dominant factor for search quality, that doesn't appear to be the case when we look at actual results.
On the question of whether or not Mwmbl's user-curated results can work, I would guess no, or at least not without a lot more moderation. Just browsing to Mwmbl shows the last edit to ranking was by user "betest", who added some kind of blogspam as the top entry for "RSS". It appears to be possible to revert the change, but there's no easily findable way to report the change or the user as spammy.
On the question of whether or not something like Metacrawler, which aggregated results from multiple search engines,  would produce superior results today, that's arguably irrelevant since it would either be impossible to legally run as a commercial service or require prohibitive licensing fees, but it seems plausible that, from a technical standpoint, a modern metacrawler would be fairly good today. Metacrawler quickly became irrelevant because Google returned significantly better results than you would get by aggregating results from other search engines, but it doesn't seem like that's the case today.
Going back to the debate between folks like Xe, who believe that straightforward search queries are inundated with crap, and our thought leader, who believes that "the rending of garments about how even google search is terrible now is pretty overblown", it appears that Xe is correct. Although Google doesn't publicly provide the ability to see what was historically returned for queries, many people remember when straightforward queries generally returned good results. One of the reasons Google took off so quickly in the 90s, even among expert users of AltaVista, who'd become very adept at adding all sorts of qualifiers to queries to get good results, was that you didn't have to do that with Google. But we've now come full circle and we need to add qualifiers, restrict our search to specific sites, etc., to get good results from Google on what used to be simple queries. If anything, we've gone well past full circle since the contortions we need to get good results are a lot more involved than they were in the AltaVista days.
If you're looking for work, Freshpaint is hiring a recruiter, Software Engineers, and a Support Engineer. I'm in an investor in the company, so you should take this with the usual grain of salt, but if you're looking to join a fast growing early-stage startup, they seem to have found product-market fit and have been growing extremely quickly (revenue-wise).
Thanks to Laurence Tratt, Heath Borders, Justin Blank, Brian Swetland, Viktor Lofgren (who, BTW, I didn't know before writing this post — I only reached out to him to discuss the Marginalia search results after running the queries), Misha Yagudin, @hpincket@fosstodon.org, Jeremey Kun, and Yossi Kreinin for comments/corrections/discussion
Appendix: Other search engines
DuckDuckGo: in the past, when I've compared DDG to Bing while using an ad blocker, the results have been very similar. I also tried DDG here and, removing the Bing ads, the results aren't as similar as they used to be, but they were still similar enough that it didn't seem worth listing DDG results. I use DDG as my default search engine and I think, like Google, it works fine if you know how to query but, for the kinds of naive queries in this post, it doesn't fare particularly well.
wiby.me: Like Marginalia, this is another search engine made for finding relatively obscure results. I tried four of the above queries on wiby and the results were interesting, in that they were really different than what I got from any other search engine, but wiby didn't return relevant results for the queries I tried.
searchmysite.net: Somewhat relevant results for some queries, but not as relevant as Marginalia. Many fewer scams and ad-laden pages than Google, Bing, and Kagi.
indieweb-search.jamesg.blog: seemed to be having an outage. "Your request could not be processed due to a server error." for every query.
Teclis: The search box is still there, but any query results in "Teclis.com is closed due to bot abuse. Teclis results are still available through Kagi's search results, explicitly through the 'Non-commercial Web' lens and also as an API.". A note on the front page reads "Teclis results are disabled on the site due to insane amount of bot traffic (99.9% traffic were bots)."
Appendix: queries that return good results
I think that most programmers are likely to be able to get good results to every query, except perhaps the tire width vs. grip query, so here's how I found an ok answer to the tire query:
I tried a youtube search, since
a lot of the best car-related content is now youtube
. A youtube video whose title claims to answer the question (the video doesn't actually answer the question) has a comment recommending Carroll Smith's book "Tune To Win". The comment claims that chapter 1 explains why wider tires have more grip, but I couldn't find an explanation anywhere in the book. Chapter 1 does note that race cars typically run wider tires than passenger cars and that passenger cars are moving towards having wider tires and it make some comments about slip angle that give a sketch of an intuitive reason for why you'd end up with better cornering with a wider contact patch, but I couldn't find a comment that explains differences in braking. Also, the book notes that the primary reason for the wider contact patch is that it (indirectly) allows for more less heat buildup, which then lets you design tires that operate over a narrower temperature range, which allows for softer rubber. That may be true, but it doesn't explain much of the observed behavior one might wonder about.
Tune to Win recommends Kummer's The Unified Theory of Tire and Rubber Friction and Hays and Brooke's (actually Browne, but Smith incorrectly says Brooke) The Physics of Tire Traction. Neither of these really explained what's happening either, but looking for similar books turned up
Milliken and Millken's Race Car Vehicle Dynamics
, which also didn't really explain why but seemed closer to having an explanation. Looking for books similar to Race Car Vehicle Dynamics turned up Guiggiani's The Science of Vehicle Dynamics, which did get at how to think about and model a number of related factors. The last chapter of Guiggiani's book refers to something called the "brush model" (of tires) and searching for "brush model tire width" turned up a reference to Pacejka's Tire and Vehicle Dynamics, which does start to explain why wider tires have better grip and what kind of modeling of tire and vehicle dynamics you need to do to explain easily observed tire behavior.
As we've noted, people have different tricks for getting good results so, if you have a better way of getting a good result here, I'd be interested in hearing about it. But note that, basically every time I have a post that notes that something doesn't work, the most common suggestion will be to do something that's commonly suggested that doesn't work, even though the post explicitly notes that the commonly suggested thing doesn't work. For example, the most common comment I receive about
this post on filesystem correctness
is that you can get around all of this stuff by doing the rename trick, even though the post explicitly notes that this doesn't work, explains why it doesn't work, and references a paper which discusses why it doesn't work. A few years later,
I gave an expanded talk on the subject
, where I noted that people kept suggesting this thing that doesn't work and the most common comment I get on the talk is that you don't need to bother with all of this stuff because you can just do the rename trick (and no, ext4 having
auto_da_alloc
doesn't mean that this works since you can only do it if you check that you're on a compatible filesystem which automatically replaces the incorrect code with correct code, at which point it's simpler to just write the correct code). If you have a suggestion for the reason wider tires have better grip or for a search which turns up an explanation, please consider making sure that the explanation is not
one of the standard incorrect explanations noted in this post and that the explanation can account for all of the behavior that one must be able to account for if one is explaining this phenomenon
.
On how to get good results for other queries, since this post is already 17000 words, I'll leave that for a future post on how expert vs. non-expert computer users interact with computers.
Appendix: summary of query results
For each question, answers are ordered from best to worst, with the metric being my subjective impression of how good the result is. These queries were mostly run in November 2023, although a couple were run in mid-December. When I'm running queries, I very rarely write natural language queries myself. However, normal users often write natural language queries, so I arbitrarily did the "Tire" and "Snow" queries as natural queries. Continuing with the theme of running simple, naive, queries, we used the free version of ChatGPT for this post, which means the queries were run through ChatGPT 3.5. Ideally, we'd run the full matrix of queries using keyword and natural language queries for each query, run a lot more queries, etc., but this post is already 17000 words (converting to pages of a standard length book, that would be something like 70 pages), so running the full matrix of queries with a few more queries would pretty quickly turn this into a book-length post. For work and for certain kinds of data analysis, I'll sometimes do projects that are that comprehensive or more comprehensive, but here, we can't cover anything resembling a comprehensive set of queries and the best we can do is to just try a handful of queries that seem representative and use our judgment to decide if this matches the kind of behavior we and other people generally see, so I don't think it's worth doing something like 4x the work to cover marginally more ground.
For the search engines, all queries were run in a fresh incognito window with cleared cookies, with the exception of Kagi, which doesn't allow logged-out searches. For Kagi, the queries were done with a fresh account with no custom personalization or filters, although they were done in sequence with the same account, so it's possible some kind of personalized ranking was applied to the later queries based on the clicks in the earlier queries. These queries were done in Vancouver, BC, which seems to have applied some kind of localized ranking on some search engines.
download youtube videos
Ideally, the top hit would be
yt-dlp
or a thin, graphical, wrapper around
yt-dlp
. Links to
youtube-dl
or other less frequently updated projects would also be ok.
Great results (
yt-dlp
as a top hit, maybe with
youtube-dl
in there somewhere, and no scams): none
Good results (
youtube-dl
as a top hit, maybe with
yt-dlp
in there somewhere, and no scams): none
Ok results (
youtube-dl
as a top hit, maybe with
yt-dlp
in there somewhere, and fewer scams than other search engines):
Marginalia: Top link is for
youtube-dl
. Most links aren't relevant. Many fewer scams than the big search engines
Bad results (has some useful links, but also links to a lot of scams)
Mwmbl: Some links to bad sites and scams, but fewer than the big search engines. Also has one indirect link to
youtube-dl
in the top 10 and one for a GUI for
youtube-dl
Kagi: Mostly links to scammy sites but does have, a couple pages down, a web.archive.org link to the 2010 version of
youtube-dl
Very bad results (fails to return any kind of useful result)
ChatGPT: basically refuses to answer the question, although you can probably prompt engineer your way to an answer if you don't just naively ask the question you want answered
Terrible results (fails to return any kind of useful result and is full of scams:
Google: Mostly links to sites that try to scam you or charge you for a worse version of free software. Some links to ad-laden listicles which don't have good suggestions. Zero links to good results. Also links to various youtube videos that are the youtube equivalent of blogspam.
Bing: Mostly links to sites that try to scam you or charge you for a worse version of free software. Some links to ad-laden listicles which don't have good suggestions. Arguably zero links to good results (although one could make a case that result #10 is an ok result despite seeming to be malware).
ad blocker
Ideally, the top link would be to ublock origin. Failing that, having any link to ublock origin would be good
Great results (ublock origin is top result, no scams):
ChatGPT: First suggestion is ublock origin
Good results (ublock origin is high up, but not the top result; results above ublock origin are either obviously not ad blockers or basically work without payment even if they're not as good as ublock origin; no links that directly try to scam you): none
Ok results (ublock origin is in there somewhere, fewer scams than other search engines with not many scams)
Marginalia: 3rd and 4th results gets you to ublock origin and 8th result is ublock origin. Nothing that appears to try to scam you directly and "only" one link to some kind of SEO ad farm scam (which is much better than the major search engines)
Bad results (no links to ublock origin and mostly links to things that paywall good features or ad blockers that deliberately let ads through by default):
Mwmbl: Lots of irrelevant links and some links to ghostery. One scam link, so fewer scams than commercial search engines
Very bad results (exclusively or almost exclusively link to ad blockers that paywall good features or, by default, deliberately let through ads)
Google: lots of links to ad blockers that "participate in the Acceptable Ads program, where publishers agree to ensure their ads meet certain criteria" (not mentioned in the text, but explained elsewhere if you look into it, so that the main revenue source for companies that do this is advertisers paying the "ad blocker" company to not block their ads, making the "ad blocker" not only not an ad blocker, but very much not incentive aligned with users. Some links to things that appear to be scams. Zero links to ublock origin. Also links to various youtube videos that are the youtube equivalent of blogspam.
Kagi: similar to Google, but with more scams, though fewer than Bing
Terrible results (exclusively or almost exclusively link to ad blockers that paywall good features or, by default, deliberately let through ads and has a significant number of scams):
Bing: similar to Google, but with more scams and without youtube videospam
download Firefox
Ideally, we'd get links to download firefox with no fake or scam links
Great results (links to download firefox; no scams):
Bing: links to download Firefox
Mwmbl: links to download firefox
Kagi: links to download firefox
Good:
ChatGPT: this is a bit funny to categorize, since these are technically incorrect instructions, but a human should easily be able to decode the instructions and download firefox
Ok results (some kind of indirect links to download firefox; no scams):
Marginalia: indirect links to download Firefox instructions to get to a firefox download
Bad results (links to download firefox, with scams):
Google: top links are all legitimate, but the #7 result is a scam that tries to get you to install badware and the #10 result is an ad that appears to be some kind of scam that wants your credit card info.
Why do wider tires have better grip?
Ideally, would link to an explanation that clearly explains why and doesn't have an incomplete explanation that can't explain a lot of commonly observed behavior
Great / Good / Ok results: none
Bad results (no results or a very small number of obviously incorrect results):
Mwmbl: one obviously incorrect result and no other results
Marginalia: two obviously incorrect results and no other results
Very bad results: (a very small number of semi-plausible incorrect results)
ChatGPT: standard ChatGPT "hallucination" that's probably plausible to a lot of people (it sounds like a lot of incorrect internet comments on the topic, but better written)
Terrible results (lots of semi-plausible incorrect results, often on ad farms):
Google / Bing / Kagi: incorrect ad-laden results with the usual rate of scammy ads
Why do they keep making cpu transistors smaller?
Ideally, would link to an explanation that clearly explains why. The best explanations I've seen are in
VLSI
textbooks, but I've also seen very good explanations in lecture notes and slides
Great results (links to a very good explanation, no scams): none
Good results (links to an ok explanation, no scams): none
Ok results (links to something you can then search on further and get a good explanation if you're good at searching and doesn't rank bad or misleading explanations above the ok explanation):
Bing: top set of links had a partial answer that could easily be turned into links to correct answers via more searching. Also had a lot of irrelevant answers and ad-laden SEO'd garbage
Bad results (no results or a small number of obviously irrelevant results or lots of semi-plausible wrong results with an ok result somewhere):
Marginalia: no answers
Mwmbl: one obviously irrelevant answer
Google: 5th link has the right keywords to maybe find the right answer with further searches. Most links have misleading or incorrect partial answers. Lots of links to Quora, which don't answer the question. Also lots of links to other bad SEO'd answers
Kagi: 10th link has a fairly direct path to getting the correct answer, if you scroll down far enough on the 10th link. Other links aren't good.
Very bad results:
ChatGPT: doesn't really answer the question. Asking ChatGPT to explain its answers further causes it "hallucinate" incorrect reasons.
vancouver snow forecast winter 2023
I'm not sure what the ideal answer is, but a pretty good one would be to Environment Canada's snow forecast, predicting significantly below normal snow (and above normal temperatures)
Great results (links to Environment Canada winter 2023 multi-month snow forecast as top result or something equivalently good): none
Good results: none
Ok results (links to some kind of semi-plausible winter snow forecast that isn't just made-up garbage to drive ad clicks): none
Bad results (no results or obviously irrelevant results):
Marginalia: no results
ChatGPT: incorrect results, but when I accidentally prepended my question with "User\n", then it returned a link to the right website (but in a way that would make it quite difficult to navigate to a decent result), so perhaps a slightly different prompt would pseudo-randomly cause a ok result here?
Mwmbl: a bunch of obviously irrelevant results
Very bad results: none
Terrible results (links to deliberately faked forecast results):
Bing: mostly irrelevant results. The top seemingly-relevant result is the 5th link, but it appears to be some kind of scam site that fabricates fake weather forecasts and makes money by serving ads on the heavily SEO'd site
Kagi: top 4 results are from the scam forecast site that's Bing's 5th link
Google: mostly irrelevant results and the #1 result is a fake answer from a local snow removal company that projects significant snow and cold weather in an attempt to get you to unnecessarily buy snow removal service for the year. Other results are SEO'd garbage that's full of ads
Appendix: detailed query results
Download youtube videos
For our first query, we'll search "download youtube videos" (Xe's suggested search term, "youtube downloader" returns very similar results). The ideal result is
yt-dlp
or a thin, free, wrapper around
yt-dlp
.
yt-dlp
is a fork of
youtube-dlc
, which is a now defunct fork of
youtube-dl
, which seems to have very few updates nowadays.. A link to one of these older downloaders also seems ok if they still work.
Google
Some youtube downloader site. Has lots of assurances that the website and the tool are safe because they've been checked by "Norton SafeWeb". Interacting with the site at all prompts you to install a browser extension and enable notifications. Trying to download any video gives you a full page pop-over for extension installation for something called CyberShield. There appears to be no way to dismiss the popover without clicking on something to try to install it. After going through the links but then choosing not to install CyberShield, no video downloads. Googling "cybershield chrome extension" returns a knowledge card with "Cyber Shield is a browser extension that claims to be a popup blocker but instead displays advertisements in the browser. When installed, this extension will open new tabs in the browser that display advertisements trying to sell software, push fake software updates, and tech support scams.", so CyberShield appears to be badware.
Some youtube downloader site. Interacting with the site causes a pop-up prompting you to download their browser extension. Putting a video URL in causes a pop-up to some scam site but does also cause the video to download, so it seems to be possible to download youtube videos here if you're careful not to engage with the scams the site tries to trick you into interacting with
PC Magazine listicle on ways to download videos from youtube. Top recommendations are paying for youtube downloads, VLC (which they note didn't work when they tried it), some $15/yr software, some $26/yr software, "FlixGrab", then a warning about how the downloader websites are often scammy and they don't recommend any downloader website. The article has more than one ad per suggestion.
Some youtube downloader site with shady pop-overs that try to trick you into clicking on ads before you even interact with the page
Some youtube downloader site with pop-ups that try to trick you into clicking on scam ads
Some youtube downloader site with pop-ups that try to trick you into clicking on scam ads, e.g., "Samantha 24, vancouver | I want sex, write to WhatsApp | Close / Continue". Clicking anything (any button, or anywhere else on the site tries to get you to install something called "Adblock Ultimate"
ZDNet ZDnet listicle. First suggestion is clipware, which apparently bundles a bunch of malware/adware/junkware with the installer:
https://www.reddit.com/r/software/comments/w9o1by/warning_about_clipgrab/
. The listicle is full of ads and has an autoplay video
[YouTube video] Over 2 minutes of ads followed by a video on how to buy youtube premium (2M views on video)
[YouTube video] Video that starts off by asking users to watch the whole video (some monetization thing?). The video tries to funnel you to some kind of software to download videos that costs money
[YouTube video] PC Magazine video saying that you probably don't "have to" download videos since you can use the share button, and then suggests reading their story (the one in result #3) on how to download videos
Some youtube downloader site with scam ads. Interacting with the site at all tries to get you to install "Adblock Ultimate"
Some youtube downloader site with pop-ups that try to trick you into clicking on scam ads
Some youtube downloader site with scam ads
Out of 10 "normal" results, we have 9 that, in one way or another, try to get you to install badware or are linked to some other kind of ad scam. One page doesn't do this, but it also doesn't suggest the good, free, option for downloading youtube videos and instead suggests a number of paid solutions. We also had three youtube videos, all of which seem to be the video equivalent of SEO blogspam. Interestingly, we didn't get a lot of ads from Google itself
despite that happening the last time I tried turning off my ad blocker to do some Google test queries
.
Bing
Some youtube downloader site. This is google (2), which has ads for scam sites
[EXPLORE FURTHER ... "Recommended to you based on what's popular"] Some youtube download site, not one we saw from google. Site has multiple pulsing ads and bills itself as "50% off" for Christmas (this search was done in mid-November). Trying to download any video pulls up a fake progress bar with a "too slow? Try [our program] link". After a while, a link to download the video appears, but it's a trick, and when you click it, it tries to install "oWebster Search extension". Googling "oWebster Search extension" indicates that it's badware that hijacks your browser to show ads. Two of the top three hits are how to install the extension and the rest of the top hits are how to remove this badware. Many of the removal links are themselves scams that install other badware. After not installing this badware, clicking the download link again results in a pop-over that tries to get you to install the site's software. If you dismiss the pop-over and click the download link again, you just get the pop-over link again, so this site appears to be a pure scam that doesn't let you download videos
[EXPLORE FURTHER]. Interacting with the site pops up fake ads with photos of attractive women who allegedly want to chat with you. Clicking the video download button tries to get you to install a
copycat ad blocker
that
displays extra pop-over ads
. The site does seem to actually give you a video download, though
[EXPLORE FURTHER] Same as (3)
[EXPLORE FURTHER] Same as Google (1) (that NortonSafeWeb youtube downloader site that tries to scam you)
[EXPLORE FURTHER] A site that converts videos to MP4. I didn't check to see if the site works or is just a scam as the site doesn't even claim to let you download youtube videos
Google (1), again. That NortonSafeWeb youtube downloader site that tries to scam you.
[EXPLORE FURTHER] A link to youtube.com (the main page)
[EXPLORE FURTHER] Some youtube downloader site with a popover that tries to trick you into clicking on an ad. Closing that reveals 12 more ads. There's a scam ad that's made to look like a youtube downloader button. If you scroll past that, there's a text box and a button for trying to download a youtube video. Entering a valid URL results in an error saying there's no video that URL.
Gigantic card that actually has a download button. The download button is fake and just takes you to the site. The site loudly proclaims that the software is not adware, spyware, etc.. Quite a few internet commenters note that their antivirus software tags this software as malware. A lot of comments also indicate that the software doesn't work very well but sometimes works. The site for the software has a an embedded youtube video, which displays "This video has been removed for violating YouTube's Terms of Service". Oddly, the download links for mac and Linux are not for this software and in fact don't download anything at all and are installation instructions for
youtube-dl
; perhaps this makes sense if the windows version is actually malware. The windows download button takes you to a page that lets you download a windows executable. There's also a link to some kind of ad-laden page that tries to trick you into clicking on ads that look like normal buttons
PC magazine listicle
An ad for some youtube downloader program that claims "345,764,132 downloads today"; searching the name of this product on reddit seems to indicate that it's malware
Ad for some kind of paid downloader software
That's the end of the first page.
Like Google, no good results and a lot of scams and software that may not be a scam but is some kind of lightweight skin around an open source project that charges you instead of letting you use the software for free.
Marginalia
12-year old answer suggesting youtube-dl, which links to a URL which has been taken down and replaced with "Due to a ruling of the Hamburg Regional Court, access to this website is blocked."
Some SEO'd article, like you see on normal search engines
Leawo YouTube Downloader (I don't know what this is, but a quick search at least doesn't make it immediately obvious that this is some kind of badware, unlike the Google and Bing results)
Some SEO'd listicle, like you see on normal search engines
Bug report for some random software
Some random blogger's recommendation for "4K Video Downloader". A quick search seems to indicate that this isn't a scam or badware, but it does lock some features behind a paywall, and is therefore worse than
yt-dlp
or some free wrapper around
yt-dlp
A blog post on how to install and use
yt-dlp
. The blogpost notes that it used to be about
youtube-dl
, but has been updated to
yt-dlp
.
More software that charges you for something you can get for free, although searching for this software on reddit turns up cracks for it
A listicle with bizarrely outdated recommendations, like RealPlayer. The entire blog seems to be full of garbage-quality listicles.
A script to download youtube videos for something called "keyboard maestro", which seems useful if you already use that software, but seems like a poor solution to this problem if you don't already use this software.
The best results by a large margin. The first link doesn't work, but you can easily get to
youtube-dl
from the first link. I certainly wouldn't try Leawo YouTube Downloader, but at least it's not so scammy that searching for the name of the project mostly returns results about how the project is some kind of badware or a scam, which is better than we got from Google or Bing. And we do get a recommendation with
yt-dlp
, with instructions in the results that's just a blog post from someone who wants to help people who are trying to download youtube videos.
Kagi
1. That NortonSafeWeb youtube downloader site. Interacting with the site at all prompts you to install a browser extension and enable notifications. Trying to download any video gives you a full page pop-over for extension installation for something called CyberShield. There appears to be no way to dismiss the popover without clicking on something to try to install it
2. Another link to that NortonSafeWeb youtube downloader site. For some reason, this one is tagged with "Dec 20, 2003", apparently indicating that the site is from Dec 20th 2003, although that's quite wrong.
3. Some youtube downloader site. Selecting any video to download pushes you to a site with scam ads.
4. Some youtube downloader site. Interacting with the site at all pops up multiple ads that link to scams and the page wants to enable notifications. A pop-up then appears on top of the ads that says "Ad removed" with a link for details. This is a scam link to another ad.
5. Another link to the above site
6-7. Under a subsection titled "Interesting Finds", there are links to two github repos. One is for transcribing youtube videos to text and the other is for using Google Takeout to backup photos from google photos or your own youtube channel
8. Some youtube downloader site.
9-13. Under a subsection titled "Blast from the Past", 4 irrelevant links and a link to youtube-dl's github page, but the 2010 version at archive.org
14. SEO blogspam for youtube help. Has a link that's allegedly for a "Greasemonkey script for downloading YouTube videos", but the link just goes to a page with scammy ads
15. Some software that charges you $5/mo to download videos from youtube
Mwmbl
Some youtube video downloader site, but one that no other search engine returned. There's a huge ad panel that displays "503 NA - Service Deprecating". The download link does nothing except for pop up some other ad panes that then disappear, leaving just the 503 "ad".
$20 software for downloading youtube videos
2016 blog post on how to install and use
youtube-dl
. Sidebar has two low quality ads which don't appear to be scams and the main body has two ads interspersed, making this extremely low on ads compared to analogous results we've seen from large search engines
Some youtube video download site. Has a giant banner claiming that it's "the only YouTube Downloader that is 100% ad-free and contains no popups.", which is probably not true, but the site does seem to be ad free and not have pop-ups. Download link seems to actually work.
Youtube video on how to install and use
youtube-dlg
(a GUI wrapper for
youtube-dl
) on Linux (this query was run from a Mac).
Link to what was a 2007 blogpost on how to download youtube videos, which automatically forwards to a 2020 ad-laden SEO blogspam listicle with bad suggestions. Article has two autoplay videos. Archive.org shows that the 2007 blog post had some reasonable options in it for the time, so this wasn't always a bad result.
A blog post on a major site that's actually a sponsored post trying to get you to a particular video downloader. Searching for comments on this on reddit indicate that users view the app as a waste of money that doesn't work. The site is also full of scammy and misleading ads for other products. E.g., I tried clicking on an ad that purports to save you money on "products". It loaded a fake "checking your computer" animation that supposedly checked my computer for compatibility with the extension and then another fake checking animation, after which I got a message saying that my computer is compatible and I'm eligible to save money. All I have to do is install this extension. Closing that window opens a new tab that reads "Hold up! Do you actually not want automated savings at checkout" with the options "Yes, Get Coupons" and "No, Don't Save". Clicking "No, Don't Save" is actually an ad that takes you back to a link that tries to get you to install a chrome extension.
That "Norton Safe Web" youtube downloader site, except that the link is wrong and is to the version of the site that purports to download instagram videos instead of the one that purports to download youtube videos.
Link to Google help explaining how you can download youtube videos that you personally uploaded
SEO blogspam. It immediately has a pop-over to get you to subscribe to their newsletter. Closing that gives you another pop-over with the options "Subscribe" and "later". Clicking "later" does actually dismiss the 2nd pop-over. After closing the pop-overs, the article has instructions on how to install some software for windows. Searching for reviews of the software returns comments like "This is a PUP/PUA that can download unwanted applications to your pc or even malicious applications."
Basically the same as Google or Bing.
ChatGPT
Since ChatGPT expects more conversational queries, we'll use the prompt "How can I download youtube videos?"
The first attempt, on a Monday at 10:38am PT  returned "Our systems are a bit busy at the moment, please take a break and try again soon.". The second attempt returned an answer saying that one should not download videos without paying for YouTube Premium, but if you want to, you can use third-party apps and websites.  Following up with the question "What are the best third-party apps and websites?" returned another warning that you shouldn't use third-party apps and websites, followed by the
ironic-for-GPT warning,
I don't endorse or provide information on specific third-party apps or websites for downloading YouTube videos. It's essential to use caution and adhere to legal and ethical guidelines when it comes to online content.
ad blocker
For our next query, we'll try "ad blocker". We'd like to get
ublock origin
. Failing that, an ad blocker that, by default, blocks ads. Failing that, something that isn't a scam and also doesn't inject extra ads or its own ads. Although what's best may change at any given moment, comparisons I've seen that don't stack the deck have
often seemed to show that ublock origin has the best or among the best performance
, and ublock origin is free and blocks ads.
Google
"AdBlock — best ad blocker". Below the fold, notes "AdBlock participates in the Acceptable Ads program, so unobtrusive ads are not blocked", so this doesn't block all ads.
Adblock Plus | The world's #1 free ad blocker. Pages notes "Acceptable Ads are allowed by default to support websites", so this also does not block all ads by default
AdBlock. Page notes that " Since 2015, we have participated in the Acceptable Ads program, where publishers agree to ensure their ads meet certain criteria. Ads that are deemed non-intrusive are shown by default to AdBlock users", so this doesn't block all ads
"Adblock Plus - free ad blocker", same as (2), doesn't block all ads
"AdGuard — World's most advanced adblocker!" Page tries to sell you on some kind of paid software, "AdGuard for Mac". Searching for AdGuard turns up a post
from this person looking for an ad blocker that blocks ads injected by AdGuard
. It seems that you can download it for free, but then, if you don't subscribe, they give you more ads?
"AdBlock Pro" on safari store; has in-app purchases. It looks like you have to pay to unlock features like blocking videos
[YouTube] "How youtube is handling the adblock backlash". 30 second video with 15 second ad before the video. Video has no actual content
[YoutTube] "My thoughts on the youtube adblocker drama"
[YouTube] "How to Block Ads online in Google Chrome for FREE [2023]"; first comment on video is "your video doesnt [sic] tell how to stop Youtube adds [sic]". In the video, a person rambles for a bit and then googles
ad blocker extension
and then clicks the first link (same as our first link), saying, "If I can go ahead and go to my first website right here, so it's basically officially from Google .... [after installing, as a payment screen pops up asking you to pay $30 or a monthly or annual fee]"
"AdBlock for Mobile" on the App Store. It's rated 3.2* on the iOS store. Lots of reviews indicate that it doesn't really work
MalwareBytes ad blocker. A quick search indicates that it doesn't block all ads (unclear if that's deliberate or due to bugs)
"Block ads in Chrome | AdGuard ad blocker", same as (5)
[ad] NordVPN
[ad] "#1 Best Free Ad Blocker (2024) - 100% Free Ad Blocker." Immediately seems scammy in that it has a fake year (this query was run in mid-November 2023). This is for something called TOTAL Ad Block.
Searching for TOTAL Ad Block turns up results indicating that it's a scammy app that doesn't let you unsubscribe and basically tries to steal your money
15 [ad] 100% Free & Easy Download - Automatic Ad Blocker. Actually for Avast browser and not an ad blocker.
A quick search show that this browser has a history of being less secure than just running chromium
and that
it collects an unusually large amount of information from users
.
No links to ublock origin. Some links to scams, though not nearly as many as when trying to get a youtube downloader. Lots of links to ad blockers that deliberately only block some ads by default.
Bing
1. [ad] "Automatic Ad Blocker | 100% Free & Easy Download". [link is actually to avast secure browser, so an entire browser and not an ad blocker; from a quick search, this appears to be a wrapper around chromium that [has a history of being less secure than just running chromium](https://palant.info/2020/01/13/pwning-avast-secure-browser-for-fun-and-profit/) [which collects an unusually large amount of information from users](https://palant.info/2019/10/28/avast-online-security-and-avast-secure-browser-are-spying-on-you/)].
2. [ad]  "#1 Best Free Ad Blocker (2023) | 100% Free Ad Blocker". Has a pop-over nag window when you mouse over to the URL bar asking you to install it instead of navigating away. Something called TOTAL ad block. Apparently tries to get to sign up for a subscription [and then makes it very difficult to unsubscribe](https://www.reddit.com/r/Adblock/comments/1412m7l/total_adblock_peoples_experiencesopinions/) (apparently, you can't cancel without a phone call, and when you call and tell them to cancel, they still won't do it unless you threaten to issue a chargeback or block the payment from the bank)
3. [ad] "Best Ad Blocker (2023) | 100% Free Ad Blocker". Seems to be a fake review site that reviews various ad blockers; ublock origin is listed as #5 with 3.5 stars. TOTAL ad block is listed as #1 with 5 stars, is the only 5 stars ad blocker, has a banner that shows that it's the "#1 Free Ad Blocker", is award winning, etc.
If you then click the link to ublock origin, it takes you to a page that "shows" that ublock origin has 0 stars on trustpilot. There are multiple big buttons that say "click to start blocking ads" that try to get you to install TOTAL ad block. In the bottom right, in what looks like an ad slot, there's an image that says "visit site" for ublock origin. The link doesn't take you to ublock origin and instead takes you a site for [the fake ublock origin](https://www.reddit.com/r/ublock/comments/32mos6/ublock_vs_ublock_origin/).
4. [ad] "AVG Free Antivirus 2023 | 100% Free, Secure Download". This at least doesn't pretend to be an ad blocker of any kind.
5. [Explore content from adblockplus.org] A link to the adblock plus blog.
6. [Explore content from adblockplus.org] A link to a list of adblock plus features.
7. "Adblock Plus | The world's #1 free ad blocker".
8-13. Sublinks to various pages on the Adblock Plus site.
We're now three screens down from the result, so the equivalent of the above google results is just a bunch of ads and then links to one website. The note that something is an ad is much more subtle than I've seen on any other site. Given
what we know about when users confuse ads with organic search results
, it's likely that most users don't realize that the top results are ads and think that the links to scam ad blockers or the fake review site that tries to funnel you into installing a scam ad blocker are organic search results.
Marginalia
"Is ad-blocker software permissible?" from judaism.stackexchange.com
Blogspam for Ghosterty. Ghostery's pricing page notes that you have to pay for "No Private Sponsored Links", so it seems like some features are behind a pay wall. Wikipedia says "Since July 2018, with version 8.2, Ghostery shows advertisements of its own to users", but it seems like this might be opt-in?
https://shouldiblockads.com/
. Explains why you might want to block ads. First recommendation is ublock origin
"What’s the best ad blocker for you? - Firefox Add-ons Blog". First recommendation is ublock origin. Also provides what appears to be accurate information about other ad blockers.
Blog post that's a personal account of why someone installed an ad blocker.
Opera (browser).
Blog post, anti-anti-adblocker polemic.
ublock origin.
Fairphone forum discussion on whether or not one should install an ad blocker.
SEO site blogspam (as in, the site is an SEO optimization site and this is blogspam designed to generate backlinks and funnel traffic to the site).
Probably the best result we've seen so far, in that the third and fourth results suggest ublock origin and the first result is very clearly not an ad blocker. It's unfortunate that the second result is blogspam for Ghostery, but this is still better than we see from Google and Bing.
Mwmbl
A bitly link to a "thinkpiece" on ad blocking from a VC thought leader.
A link to cryptojackingtest, which forwards to Opera (the browser).
A link to ghostery.
Another link to ghostery.
A link to something called 1blocker, which appears to be a paid ad blocker. Searching for reviews turns up comments like "I did 1blocker free trial and forgot to cancel so it signed me up for annual for $20 [sic]" (but comments indicate that the ad blocker does work).
Blogspam for Ad Guard. There's a banner ad offering 40% off this ad blocker.
An extremely ad-laden site that appears to be in the search results because it contains the text "ad blocker detected" if you use an ad blocker (I don't see this text on loading the page, but it's in the page preview on Mwmbl). The first page is literally just ads with a "read more" button. Clicking "read more" takes you to a different page that's full of ads that also has the cartoon, which is the "content".
Another site that appears to be in the search results because it contains the text "ad blocker detected".
Malwarebytes ad blocker, which doesn't appear to work.
HN comments for article on youtube ad blocker crackdown. Scrolling to the 41st comment returns a recommendation for ublock origin.
Mwmbl lets users suggest results, so I tried signing up to add ublock origin. Gmail put the sign-up email into my spam folder. After adding ublock origin to the search results, it's now the #1 result for "ad blocker" when I search logged out, from an incognito window and all other results are pushed down by one. As mentioned above, the score for Mwmbl is from before I edited the search results and not after.
Kagi
1. "Adblock Plus | The world's #1 free ad blocker".
2-11. Sublinks to other pages on the Adblock Plus website.
12. "AdBlock — best ad blocker".
13. "Adblock Plus - free ad blocker".
14. "YouTube’s Ad Blocker Crackdown", a blog post that quotes and links to discussions of people talking about the titular topic.
15-18. Under a section titled "Interesting Finds", three articles about youtube's crackdown on ad blockers. One has a full page pop-over trying to get you to install TOTAL Adblock with "Close" and "Open" buttons. The "Close" button does nothing and clicking any link or the open button takes to a page advertising TOTAL adblock. There appears to be no way to dismiss the ad and read the actual article without doing something like going to developer tools and deleting the ad elements. The fourth article is titled "The FBI now recommends using an ad blocker when searching the web" and 100% of the above the fold content is the header plus a giant ad. Scrolling down, there are a lot more ads.
19. "AdBlock".
20. Another link from the Adblock site, "Ad Blocker for Chrome - Download and Install AdBlock for Chrome Now!".
21-25. Under a section titled "Blast from the Past", optimal.com ad blocker, a medium article on how to subvert adblock, a blog post from a Mozillan titled "Why Ad Blockers Work" that's a response to Ars Technica's "Why Ad Blocking is devastating to the sites you love", "Why You Need a Network-Wide Ad-Blocker (Part 1)", and "A Popular Ad Blocker Also Helps the Ad Industry", subtitled "Millions of people use the tool Ghostery to block online tracking technology—some may not realize that it feeds data to the ad industry."
Similar quality to Google and Bing. Maybe halfway in between in terms of the number of links to scams.
ChatGPT
Here, we tried the prompt.
How do I install the best ad blocker?
First suggestion is ublock origin. Second suggestion is adblock plus. This seems like the best result by a significant margin.
download firefox
Google
1-6. Links to download firefox.
7. Blogspam for firefox download with ads trying to trick you into installing badware.
8-9. Links to download firefox.
10 [ad] Some kind of shady site that claims to have firefox downloads, but where the downloads take you to other sites that try to get you to sign up for an account where they ask for personal information and your credit card number. Also pops up pop-over with window that does the above if you try to actually download firefox. At least one of the sites is some kind of gambling site, so this site might make money off of referring people to gambling sites?
Mostly good links, but 2 out of the top 10 links are scams. And
we didn't have a repeat of this situation I saw in 2017, where Google paid to get ranked above Firefox in a search for Firefox
. For search queries where almost every search engine returns a lot of scams, I might rate having 2 out of the top 10 links be scams as "Ok" or perhaps even better but, here, where most search engines return no fake or scam links, I'm rating this as "Bad". You could make a case for "Ok" or "Good" here by saying that the vast majority of users will click one of the top links and never get as far as the 7th link, but I think that if Google is confident enough that's the case that they view it as unproblematic that the 7th and 10th links are scams, they should just only serve up the top links.
Bing
1-12. Links to download firefox or closely related links.
13. [ad] Avast browser.
That's the entire first page. Seems pretty good. Nothing that looks like a scam.
Marginalia
1. "Is it better to download Firefox from the website or use the package manager?" on the UNIX stackexchange
2-9. Various links related to firefox, but not firefox downloads
10. "Internet Download Accelerator online help"
Definitely worse than Bing, since none of the links are to download Firefox. Depending on how highly you rate users not getting scammed vs. having the exact right link, this might be better or worse than Google. In this post, this scams are relatively highly weighted, so Marginalia ranks above Google here.
Mwmbl
1-7. Links to download firefox.
8. A link to a tumblr that has nothing to do with firefox. The title of the tumblr is "Love yourself, download firefox" (that's the title of the entire blog, not a particular blog post).
9. Link to download firefox nightly.
10. Extremely shady link that allegedly downloads firefox. Attempting to download the shady firefox pops up an ad that tries to trick you downloading Opera. I did not run either the Opera or Firefox binaries to see if they're legitimate.
kagi.com
1-3. Links to download firefox.
4-5. Under a heading titled "Interesting finds", a 404'd link to a tweet titled "What happens if you try to download and install Firefox on Windows" [which used to note that downloading Firefox on windows results in an OS-level pop-up that recommends Edge instead "to protect your pc"](https://web.archive.org/web/20220403104257/https://twitter.com/plexus/status/1510568329303445507) and some extremely ad-laden article (though, to its credit, the ads don't seem to be scam ads).
6. Link to download firefox.
7-10. 3 links to download very old versions of firefox, and a blog post about some kind of collaboration between firefox and ebay.
11. Mozilla homepage.
12. Link to download firefox.
Maybe halfway in between Bing and Marginalia. No scams, but a lot of irrelevant links. Unlike some of the larger search engines, these links are almost all to download the wrong version of firefox, e.g., I'm on a Mac and almost all of the links are for windows downloads.
ChatGPT
The prompt "How do I download firefox?" returned technically incorrect instructions on how to download firefox. The instructions did start with going to the correct site, at which point I think users are likely to be able to download firefox by looking at the site and ignoring the instructions. Seems vaguely similar to marginalia, in that you can get to a download by clicking some links, but it's not exactly the right result. However, I think users are almost certain to find the correct steps and only likely with Marginalia, so ChatGPT is rated more highly than Marginalia for this query.
Why do wider tires have better grip?
Any explanation that's correct must, a minimum, be consistent with the following:
Assuming a baseline of a moderately wide tire for the wheel size.
Scaling both of these to make both wider than the OEM tire (but still running a setup that fits in the car without serious modifications) generally gives better dry braking and better lap times.
In wet conditions, wider setups often have better braking distances (though this depends a lot on the specific setup) and better lap times, but also aquaplane at lower speeds.
Just increasing the wheel width and using the same tire generally gives you better lap times, within reason.
Just increasing the tire width and leaving wheel width fixed generally results in worse lap times.
Why tire pressure changes have the impact that they do (I'm not going to define terms in these bullets; if this text doesn't make sense to you, that's ok).
At small slip angles, increasing tire pressure results in increased lateral force.
In general, lowering tire pressure increases effective friction coefficient (within reason a semi-reasonable range).
This is one that has a lot of standard incorrect or incomplete answers, including:
Wider tires give you more grip because you get more surface area.
Wider tires don't, at reasonable tire pressure, give you significantly more surface area.
Wider tires actually don't give you more grip because friction is surface area times a constant and surface area is mediated by air pressure.
It's easily empirically observed that wider tires do, in fact, give you better handling and braking.
Wider tires let you use a softer compound, so the real reason wider tires give you more grip is via the softer compound.
This could be part of an explanation, but I've generally seen this cited as the only explanation. However, wider tires give you more grip independent of having a softer compound. You can even observe this with the same tire by mounting the exact same tire on a wider wheel (within reason).
The shape of the contact patch when the tire is wider gives you better lateral grip due to [some mumbo jumbo], e.g., "tire load sensitivity" or "dynamic load".
Ok, perhaps, but what's the mechanism that gives wider tires more grip when braking? And also, please explain the mumbo jumbo. For my goal of understanding why this happens, if you just use some word but don't explain the mechanism, this isn't fundamentally different than saying that wider tires have better grip due to magic.
When there's some kind of explanation of the mumbo jumbo, there will often be an explanation that only applies to aspect of increased grip, e.g., the explanation will really only apply to lateral grip and not explain why braking distances are decreased.
Google
1. A "knowledge card" that says "Bigger tires provide a wider contact area that optimizes their performance and traction.", which explains nothing. On clicking the link, it's SEO blogspam with many [incorrect statements, such as "Are wider tires better for snow traction? Or are narrow tires more reliable in the winter months? The simple answer is narrow tires!](https://mastodon.social/@danluu/111441790762754806) Tires with a smaller section width provide more grip in winter conditions. They place higher surface pressure against the road they are being driven on, enabling its snow and ice traction"
2. [Question dropdown] "do wider tires give you more grip?", which correctly says "On a dry road, wider tires will offer more grip than narrow ones, but the risk of aquaplaning will be higher with wide tires.". On clicking the link, there's no explanation of why, let alone an answer to the question we're asking
3. [Question dropdown] "Do bigger tires give you better traction?", which says "What Difference Does The Wheel Size Make? Larger wheels offer better traction, and because they have more rubber on the tire, this also means a better grip on the road", which has a nonsensical explanation of why. On clicking the link, the link appears to be talking about wheel diameter and is not only wrong, but actually answering the wrong question.
4. [Question dropdown] "Why do wider tires have more grip physics?", which then has some of the standard incorrect explanations.
5. "Do wider wheels improve handling?", which says "Wider wheels and wider tires will also lower your steering friction coefficient". On clicking the link, there's no explanation of why nor is there an answer to the question we're asking.
6. "What are the disadvantages of wider tires?", which says "Harder Handling & Steering". On clicking the link, there are multiple incorrect statements and no explanation of why.
7. "Would wider tires increase friction?", which says "Force can be stated as Pressure X Area. For a wide tire, the area is large but the force per unit area is small and vice versa. The force of friction is therefore the same whether the tire is wide or not.". Can't load the page due to a 502 error and the page isn't in archive.org, but this seems fine since the page appears to be wrong
8. "What is the advantage of 20 inch wheels over 18 inch wheels?" Answers a different question. On clicking the link, it's low quality SEO blogspam.
9. "Why do race cars have wide tires?", which says "Wider tires provide more resistance to slippery spots or grit on the road. Race tracks have gravel, dust, rubber beads and oil on them in spots that limit traction. By covering a larger width, the tires can handle small problems like that better. Wider tires have improved wear characteristics.". Perhaps technically correct, but fundamentally not the answer and highly misleading at best.
10-49. Other question dropdowns that are wrong. Usually both wrong and answering the wrong question, but sometimes giving a wrong answer to the right question and sometimes giving the right answer to the wrong question. I am just now realizing that clicking question dropdowns give you more question dropdowns.
50. "Why do wider tires get more grip? : r/cars". The person asks the question I'm asking, concluding with "This feels like a really dumb question because wider tires=more grip just seems intuitive, but I don't know the answer.". The top answer is total nonsense "The smaller surface area has more pressure but the same normal force as a larger surface area. If you distribute the same load across more area, each square inch of tire will have less force it's responsible for holding, and thus is less likely to be overcome by the force from the engine". The #2 answer is a classic reddit answer, "Yeah, take your science bs and throw it out the window.". The #3 answer has a vaguely plausible sounding answer to why wider tires have better lateral grip, but it's still misleading. Like many of the answers, the answer emphasizes how wider tires give you better lateral grip and has a lengthy explanation for why this should be the case, but wider tires also give you shorter braking distances and the provided explanation cannot explain why wider tires have shorter braking distances so must be missing a significant part of the puzzle. Anyway, none of the rest of the answers really even attempt to explain why
51-54. Other reddit answers bunched with this one, which also don't answer the question, although one of them links to https://www.brachengineering.com/content/publications/Wheel-Slip-Model-2006-Brach-Engineering.pdf, which has some good content, though it doesn't answer the question.
55. SEO blogspam for someone's youtube video; video doesn't answer the question.
56. Extremely ad-laden site with popovers that try to trick you into clicking on ads, etc.; has text I've seen on other pages that's been copied over to make an SEO ad farm (and the text has answers that are incorrect)
Bing
1. Knowledge card which incorrectly states "Larger contact patch with the ground."
2-4. Carousel where none of the links answer the question correctly. (3) from bing is (50) from google search results. (2) isn't wrong, but also doesn't answer the question. (3) is SEO blogspam for someone else's youtube video (same link as google.com 55). The video does not answer the question. (3) and (4) are literally the same link and also don't answer the question
5. "This is why wider tires equals more grip". SEO blogspam for someone else's youtube video. The youtube video does not answer the question.
6-10. [EXPLORE FURTHER] results. (6) is blatantly wrong, (7) is the same link as (3) and (4), (8) is (2), SEO blogspam for someone else's youtube video and the video doesn't answer the question, (9) is s SEO blogspam for someone else's youtube video and the video doesn't answer the question, (10) is generic SEO blogspam with lots of incorrect information
11. Same link as (2) and (8), still SEO blogspam for someone else's youtube video and the video doesn't answer the question
12-13 [EXPLORE FURTHER] results. (12) is some kind of SEO ad farm that tries to get you to make "fake" ad clicks (there are full screen popovers that, if you click them, cause you to click through some kind of ad to some normal site, giving revenue to whoever set up the ad farm). (13) is the website of the person who made one of the two videos that's a common target for SEO blogspam on this topic. It doesn't answer the question, but at least we have the actual source here.
From skimming further, many of the other links are the same links as above. No link appears to answer the question.
Marginalia
Original query returns zero results. Removing the question mark returns one single result, which is the same as (3) and (4) from bing.
Mwmbl
NYT article titled "Why Women Pay Higher Interest". This is the only returned result.
Removing the question mark returns an article about bike tires titled "Fat Tires During the Winter: What You Need to Know"
Kagi
A knowledge card that incorrectly reads "wider tire has a greater contact patch with the ground, so can provide traction."
(50) from google
Reddit question with many incorrect answers
Reddit question with many incorrect answers. Top answer is "The same reason that pressing your hand on the desk and sliding it takes more effort than doing the same with a finger. More rubber on the road = more friction".
(3) and (4) from bing
Youtube video titled "Do wider tyres give you more grip?". Clicking the video gives you 1:30 in ads before the video plays. The video is good, but it answers the question in the title of the video and not the question being asked of why this is the case. The first ad appears to be an ad revenue scam. The first link actually takes you to a second link, where any click takes you through some ad's referral link to a product.
"This is why wider tires equals more grip". SEO blogspam for (6)
SEO blogspam for another youtube video
SEO blogspam for (6)
Quora answer where top answer doesn't answer the question and I can't read all of the answers because I'm not logged in or aren't a premium member or something.
Google (56), stolen text from other sites and a site that has popovers that try to trick you into clicking ads
Pre-chat GPT nonsense text and a page that's full of ads. Unusually, the few ads that I clicked on seemed to be normal ads and not scams.
Blogspam for ad farm that has pop-overs that try to get you to install badware.
Page with ChatGPT-sounding nonsense. Has a "Last updated" timestamp that's sever-side generated to match the exact moment you navigated to the page. Page tries to trick you into clicking on ads with full-page popover. Ads don't seem to be scams, as far as I can tell.
Page which incorrectly states "In summary, a wider tire does not give better traction, it is the same traction similar to a more narrow tire.". Has some ads that get you to try to install badware.
ChatGPT
Provides a list of "hallucinated" reasons. The list of reasons has better grammar than most web search results, but still incorrect. It's not surprising that ChatGPT can't answer this question, since it often falls over on questions that are both easier to reason about and where the training data will contain many copies of the correct answer, e.g.,
Joss Fong noted that, when her niece asked ChatGPT about gravity
, the response was nonsense: "... That's why a feather floats down slowly but a rock drops quickly — the Earth is pulling them both, but the rock gets pulled harder because it's heavier."
Overall, no search engine gives correct answers. Marginalia seems to be the best here in that it gives only a couple of links to wrong answers and no links to scams.
Why do they keep making cpu transistors smaller?
I had this question when I was in high school and my AP physics teacher explained to me that it was because making the transistors smaller allowed the CPU to be smaller, which let you make the whole computer smaller. Even at age 14, I could see that this was an absurd answer, not really different than today's ChatGPT hallucinations — at the time, computers tended to be much larger than they are now, and full of huge amounts of empty space, with the CPU taking up basically no space relative to the amount of space in the box and, on top of that, CPUs were actually getting bigger and not smaller as computers were getting smaller. I asked some other people and didn't really get an answer. This was also relatively early on the life of the public web and I wasn't able to find an answer other than something like "smaller transistors are faster" or "smaller = less capacitance". But why are they faster? And what makes them have less capacitance? Specifically, what about the geometry causes that to scale so that transistors get faster? It's not, in general, obvious that things should get faster if you shrink them, e.g., if you naively linearly shrink a wire, it doesn't appear that it should get faster at all because the cross sectional area is reduced quadratically, increasing resistance per distance quadratically. But length is also reduced linearly, so total resistance is increased linearly. And then capacitance also decreases linearly, so it all cancels out. Anyway, for transistors, it turns out the same kind of straightforward scaling logic shows that they speed up (at back then, transistors were large enough and wire delay was relatively small enough that you got extremely large increases in performance for shrinking transistor). You could explain this to a high school student who's taken physics in a few minutes if
you had the right explanation
, but I couldn't find an answer to this question until I read a VLSI textbook.
There's now enough content on the web that there must be multiple good explanations out there. Just to check, I used non-naive search terms to find some good results. Let's look at what happens when you use the naive search from above, though.
Google
1. A knowledge card that reads "Smaller transistors can do more calculations without overheating, which makes them more power efficient.", which isn't exactly wrong but also isn't what I'd consider an answer of why. The article is interesting, but is about another topic and doesn't explain why.
2. [Question dropdown], "Why are transistors getting smaller?". Site has an immediate ad pop-over on opening. Site doesn't really answer the question, saying "Since the first integrated circuit was built in the 1950s, silicon transistors have shrunk following Moore’s law, helping pack more of these devices onto microchips to boost their computing power."
3. [Question dropdown] "Why do transistors need to be small?". Answer is "The capacitance between two conductors is a function of their physical size: smaller dimensions mean smaller capacitances. And because smaller capacitances mean higher speed as well as lower power, smaller transistors can be run at higher clock frequencies and dissipate less heat while doing so", which isn't wrong, but the site doesn't explain the scaling that made things faster as transistors got smaller. The page mostly seems concerned about discrete components and note that "In general, passive components like resistors, capacitors and inductors don’t become much better when you make them smaller: in many ways, they become worse. Miniaturizing these components is therefore done mainly just to be able to squeeze them into a smaller volume, and thereby saving PCB space.", so it's really answering a different question
4. [Question dropdown], "Why microchips are getting smaller?". SEO blogspam that doesn't answer the question other than saying stuff like "smaller is faster"
5. [Question dropdown], "Why are microprocessors getting smaller?". Link is to stackexchange. The top answer is that yield is better and cost goes down when chips are smaller, which I consider a non-answer, in that it's also extremely expensive to make things smaller, so what explains why the cost reduction is there? And, also, even if the cost didn't go down, companies would still want smaller transistors for performance reasons, so this misses a major reason and arguably the main reason.
#2 answer actually sort of explains it, "The reason for this is that as the transistor gate gets smaller, threshold voltage and gate capacitance (required drive current) gets lower.", but is both missing parts of the explanation and doesn't provide the nice, intuitive, physical explanation for why this is the case. Other answers are non-answers like "The CORE reason why CPUs keep getting smaller is simply that, in computing, smaller is more powerful:". It's possible to get to a real explanation by searching for these terms
6. "Why are CPU and GPU manufacturers trying to make ...". Top answer is the non-answer of "Smaller transistors are faster and use less power. Small is good." and since it's quora and I'm not a subscriber, the other answers are obscured by a screen that suggests I start a free trial to "access this answer and support the author as a Quora+ subscriber".
7-10. sub-links to other quora answers. Since I'm not a subscriber, by screen real estate, most of the content is ads. None of the content I could read answered the question.
Bing
1. Knowledge card with multiple parts. First parts have some mumbo jumbo, but the last part contains a partial answer. If you click on the last part of the answer, it takes you to a stack exchange question that has more detail on the partial answer. There's enough information in the partial answer to do a search and then find a more complete explanation.
2-4. [people also ask] some answers that are sort of related, but don't directly answer the question
5. Stack exchange answer for a different question.
7-10 [explore further] answers to totally unrelated questions, except for 10, which is extremely ad-laden blogspam to a related question that has a bunch of semi-related text with many ads interspersed between the text.
Kagi
1. "Why does it take multiple years to develop smaller transistors for CPUs and GPUs?", on r/askscience. Some ok comments, but they answer a different question.
2-5. Other reddit links that don't answer the question. Some of them are people asking this question, but the answers are wrong. Some of the links answer different questions and have quite good answers to those questions.
6. Stackexchange question that has incorrect and misleading answers.
7. Stackexchange question, but a different question.
8. Quora question. The answers I can read without being a member don't really answer the question.
9. Quora question. The answers I can read without being a member don't really answer the question.
10. Metafilter question from 2006. The first answers are fundamentally wrong, but one of the later answers links to the wikipedia page on MOSFET. Unfortunately, the link is to the now-removed anchor #MOSFET_scaling. There's still a scaling section which has a poor explanation. There's also a link to the page on Dennard Scaling, which is technically correct but has a very poor explanation. However, someone could search for more information using these terms and get correct information.
Marginalia
No results
Mwmbl
A link to a Vox article titled "Why do artists keep making holiday albums?". This is the only result.
ChatGPT
Has non-answers like "increase performance". Asking ChatGPT to expand on this, with "Please explain the increased performance." results in more non-answers as well as fairly misleading answers, such as
Shorter Interconnects: Smaller transistors result in shorter distances between them. Shorter interconnects lead to lower resistance and capacitance, reducing the time it takes for signals to travel between transistors. Faster signal propagation enhances the overall speed and efficiency of the integrated circuit ... The reduced time it takes for signals to travel between transistors, combined with lower power consumption, allows for higher clock frequencies
I could see this seeming plausible to someone with no knowledge of electrical engineering, but this isn't too different from ChatGPT's explanation of gravity, "... That's why a feather floats down slowly but a rock drops quickly — the Earth is pulling them both, but the rock gets pulled harder because it's heavier."
vancouver snow forecast winter 2023
Good result: Environment Canada's snow forecast, predicting significantly below normal snow (and above normal temperatures)
Google
Knowledge card from a local snow removal company, incorrectly stating "The forecast for the 2023/2024 season suggests that we can expect another winter marked by ample snowfall and temperatures hovering both slightly above and below the freezing mark. Be prepared ahead of time.". On opening the page, we see that the next sentence is "Have Alblaster [the name of the company] ready to handle your snow removal and salting. We have a proactive approach to winter weather so that you, your staff and your customers need not concern yourself with the approaching storms." and the goal of the link is to get you to buy snow removal services regardless of their necessity by writing a fake forecast.
[question dropdown] "What is the winter prediction for Vancouver 2023?", incorrectly saying that it will be "quite snowy".
[question dropdown] "What kind of winter is predicted for 2023 Canada?" Links to a forecast of Ontario's winter, so not only wrong province, but the wrong coast, and also not actually an answer to the question in the dropdown.
[question dropdown] "What is the winter prediction for B.C. in 2023 2024?" Predicts that B.C. will have a wet and mild winter, which isn't wrong, but doesn't really answer the question.
[question dropdown] "What is the prediction for 2023 2024 winter?" Has a prediction for U.S. weather
Blogspam article that has a lot of pointless text with ads all over. Text is contradictory in various ways and doesn't answer the question. Has huge pop-over ad that covers top half the page
Another blogspam article from the same source. Lots of ads; doesn't answer the question
Ad-laden article that answers some related questions, but not this question
Extremely ad-laden article that's almost unreadable due to the number of ads. Talks a lot about El Nino. Eventually notes that we should see below-normal snow in B.C. due to El Nino, but B.C. is almost 100M km² and the forecast is not the same for all of B.C., so you could maybe hope that the comment about B.C. here applies to Vancouver, but this link only lets you guess at the answer
Very ad-laden article, but does have a map which has map that's labeled "winter precipitation" which appears to be about snow and not rain. Map seems quite different from Environment Canada's map, but it does show reduced "winter precipitation" over Vancouver, so you might conclude the right thing from this map.
Bing
1-4. [news carousel] Extremely ad laden articles that don't answer the question. Multiple articles are well over half ads by page area.
5. Some kind of page that appears to have the answer, expect that the data seems to be totally fabricated? There's a graph with day-by-day probability of "winter storm". From when I did the search, there's about an average of about a 50% daily chance of a "snow storm" going forward for the next 2 weeks. Forecasts that don't seem fake have it at 1% or less daily. Page appears to be some kind of SEO'd fake forecast that makes money on ads?
6-8. [more links from same site] Various ad laden pages. One is a "contact us" page where the main "contact us" pane is actually a trick to get you to click on an ad for some kind of monthly payment service that looks like a scam
9-14 [Explore 6 related pages ... recommended to you based on what's popular] Only one link is relevant. That link has a "farmer's almanac" forecast that's fairly different from Environment Canada's forecast. The farmer's almanaic page mainly seems to be an ad to get you to buy farmer's almanic stuff, although it also has conventional ads
Kagi
1. Same SEO'd fake forecast as Bing (5)
2-4. More results from scam weather site
5-7. [News] Irrelevant results
8. Spam article from same site as Google (6)
9-13. More SEO spam from the same site
14. Same fake forecast as Google (1)
15. Page is incorrectly tagged is being from "Dec 25, 2009" (it's a recent page) and doesn't contain relevant results
Marginalia
No results.
Mwmbl
1. Ad-laden news article from 2022 about a power outage. Has an autoplay video ad and many other ads as well.
2. 2021 article about how the snow forecast for Philadelphia was incorrect. Article has a slow-loading full-page pop-over that shows up after a few seconds and is full of ads.
3. 2016 article on when the Ohio river last froze over.
4. Some local news site from Oregon with a Feb 2023 article on the snow forecast at the time. Site has an autoplay video ad and is full of other ads. Clicking one of the random ads ("Amazon Hates When You Do Ths, But They Can't Stop You (It's Genius)" results in the ad trying to get you to install a chrome extension. The ad attempts to resemble an organic blog post on a site that's just trying to get you to save money, but if you try to navigate away from the "blog post", you get a full page popover that tries to trick you into installing the chrome extension. Going to the base URL reveals that the entire site is actually a site that's trying to trick users into installing this chrome extension. This is the last result.
ChatGPT
"What is the snow forecast for Vancouver in winter of 2023?"
Doesn't answer questions, recommends using a website, app, or weather service.
Asking "Could you please direct me to a weather website, app, or weather service that has the forecast?" causes ChatGPT to return random weather websites that don't have a seasonal snow forecast.
I retried a few times. One time, I accidentally pasted in the entire ChatGPT question, which meant that my question was prepened with "User\n". That time, ChatGPT suggested "the Canadian Meteorological Centre, Environment Canada, or other reputable weather websites". The top response when asking for the correct website was "Environment Canada Weather", which at least has a reasonable seeming seasonal snow forecast somewhere on the website. The other links were still to sites that aren't relevant.
Appendix: Google "knowledge card" results
In general, I've found Google knowledge card results to be quite poor,
both for specific questions
with
easily findable answers
as well as for silly questions like "when was running invented" which, for years, infamously returned "1748. Running was invented by Thomas Running when he tried to walk twice at the same time" (which was pulled from a Quora answer).
I had a doc where I was collecting every single knowledge card I saw to tabulate the fraction that were correct. I don't know that I'll ever turn that into a post, so here are some "random" queries with their knowledge card result (and, if anyone is curious, most knowledge card results I saw when I was tracking this were incorrect).
"oc2 gemini length" (looking for the length of a kind of canoe, an oc2, called a gemini)
20″ (this was the length of a baby mentioned in an article that also mentioned the length of the boat, which is 24'7"
"busy beaver number"
"Feedly revenue"
"$5.2M/yr", via a link to a site which appears to just completely fabricate revenue and profit estimates for private companies
"What airlines fly direct from JFK airport to BLI airport?"
"Alaska Airlines - (AS) with 30 direct flights between New York and Bellingham monthly; Delta Air Lines - (DL) with 30 direct flights between JFK and BLI monthly". This sounded plausible, but when I looked this up, this was incorrect. The page it links to has a bunch of text that like "How many morning flights are there from JFK to BLI? Alaska Airlines - (AS) lists, on average, 1 flights departing before 12:00pm, where the first departure from JFK is at 09:30AM and the last departure before noon is at 09:30AM", seemingly with the goal of generating a knowledge card for questions like this. It doesn't really matter that the answers are fabricated since the goal of the site seems to be to get traffic or visibility via knowledge cards
"Air Canada Vancouver Newark"
At the time I did this search, this showed a knowledge card indicating that AC 7082 was going to depart the next day at 11:50am, but no such flight had existed for months and there was certainly not an AC 7082 flight about to depart the next day
"TYR Hurricane Category 5 neoprene thickness"
1.5mm (this is incorrect)
"Intel number of engineers"
(604) 742-3501 (I was looking for the number of engineers that Intel employed, not a phone number, and even if I was looking for a phone number for Intel engineers, I don't think this is it).
"boston up118s dimensions"
"5826298 x 5826899 x 582697 in" (this is a piano and, no, it is not 92 miles long)
"number of competitive checkers players"
"fraser river current speed"
"97 to 129 kilometers per hour (60 to 80 mph)" (this is incorrect)
"futura c-4 surfski weight"
"39 pounds" (this is actually the weight of a different surfski; the article this comes from just happens to also mention the futura c-4)
Appendix: FAQ
As already noted, the most common responses I get are generally things that are explicitly covered in the post, so I won't recover those here. However, any time I write a post that looks at anything, I also get a slew of comments like and, indeed, that was one of the first comments I got on this post.
This isn't a peer-reviewed study, it's crap
As I noted in
this other post
,
There's nothing magic about academic papers. I have my name on a few publications, including one that won best paper award at the top conference in its field. My median blog post is more rigorous than my median paper or, for that matter, the median paper that I read.
When I write a paper, I have to deal with co-authors who push for putting in false or misleading material that makes the paper look good and my ability to push back against this has been fairly limited. On my blog, I don't have to deal with that and I can write up results that are accurate (to the best of my ability) even if it makes the result look less interesting or less likely to win an award.
The same thing applies here and, in fact, I have a best paper award in this field (information retrieval, or IR, colloquially called search). I don't find IR papers particularly rigorous. I did push very hard to make
my top-conference best-paper-award-wining paper
more rigorous and, while I won some of those fights, I lost others, and that paper has a number of issues that I wouldn't let pass in a blog post. I suspect that people who make comments like this mostly don't read papers and, to the extent they do, don't understand them.
Another common response is
Your table is wrong. I tried these queries on Kagi and got Good results for the queries [but phrase much more strongly]
I'm not sure why people feel so strongly about Kagi but, all of these kinds of responses so far have come from Kagi users. No one has gotten good results for the tire, transistor, or snow queries (note, again, that this is not a query looking for a daily forecast, as clearly implied by the "winter 2023" in the query), nor are the results for the other queries very good if you don't have an ad blocker. I suppose it's possible that the next person who tells me this actually has good results, but that seems fairly unlikely given the zero percent correctness rate so far.
For example, one user claimed that the results were all good, but they pinned GitHub results and only ran the queries for which you'd get a good result on GitHub. This is actually worse than you get if you use Google or Bing and write good queries since you'll get noise in your results when GitHub is the wrong place to search. Of course you make a similar claim that Bing is amazing is you write non-naive queries, so it's curious that so many Kagi users are angrily writing me about this and no Google or Bing users. Kagi appears to have tapped into the same vein that Tesla and Apple have managed to tap into, where users become incensed that someone is criticizing something they love and then
write nonsensical defenses of their favorite product
, which bodes well for Kagi. I've gotten comments like this from not just one Kagi user, but many.
