---
source_url: https://peec.ai/blog/publish-stats-get-cited-the-tactic-that-put-my-data-all-over-the-web
ingested: 2026-10-22
sha256: ce234d09b1f2cd17
---

What I learned about AI search when I made up 50,000 stats that got cited by ChatGPT...

About 7 months ago, I launched a website with 50,000 statistics. Every one of them was fake.

Google has forgotten the site exists and deindexed the pages, but ChatGPT hasn't. Since the website went live 7 months ago, it has sent more than 10,000 AI sessions its way. And now more than 330 referring domains, including Shopify, Bluehost, and DHL, link to the site. Its made-up numbers have also ended up in an academic paper and in a bank's investment research.

At Peec AI and in the industry, we talk about GEO and SEO every day, and we keep looking for new tactics. I’ve been working on this stats page one for a long time, sharing pieces of it publicly along the way. Of course, it’s experimental, but the results have been hard to ignore. 

Where the idea for publishing fake statistics came from

The impetus to seed a site with statistics came out of long-running research I've been doing on LLMs, relevance engineering, and grounding (credit to the iPullRank team, Dan Petrovic, and Wil Reynolds).

In the course of my work, I noticed a pattern: as more teams write time-sensitive and breaking content with LLMs, those LLMs have to look for (seemingly) reliable data during their research to fill the gaps in their knowledge. Statistics are often exactly what they’re looking for.

Most GEO advice focuses on one moment: getting your brand into the AI answer. This experiment looks at what happens after the answer, when people take that output and use it, putting it into presentations, adding it to a shopping list, and yes, publishing it on their website.

I didn't come up with the idea for this experiment alone. Hat tip to Seer Interactive, who already published 

an eye-opening study

 in August 2025 that got a few thoughts bouncing around in my head. Several months later, those thoughts came together and finally made it to the top of my to-do list. In March 2026, I started working on building the site that would let me test my ideas.

The setup: a website and 50,000 made-up stats, created in one day

Quick context for anyone who wasn’t following along in real time as I ran this experiment:

I bought a brand-new domain, stateglobe.com, and generated 50,000 statistics pages in a single day with GPT-4.1. The site purports to provide stats on SEO, content marketing, social media, e-commerce, and web technology from 200 countries. Except every number was totally invented. I never checked a single one. I pushed them to the site with a basic AI web design template. This cost me around $30. Later, I added 15,000 listicles on top of the statistics. That was about $20 more, so all in all, this is an experiment that came in at the very low price of about $50.

The reaction when I first shared it was wild. When my friend Kevin featured it in 

Growth Memo

, it reached a much bigger audience. I think people responded so enthusiastically to this work because it showed great results while also speaking to the fears people have about what ends up in AI search results.

What happened

Google buried the site almost immediately

When I launched the site, traffic, indexing, and engagement were initially going really well. Using indexer tools, I got almost the entire site indexed within a week, and it started to appear in Google results.

Then two Google updates came out right after launch, and my Google visibility collapsed.

I've been invisible on Google for many months now. Indexed pages bounce between 5 and 20 impressions. At one point, I got curious and created a subdomain to see if I could increase impressions, but it didn't really help.

Other than that, I haven't touched the site. Some pages might even fail to load now and then. I don't know.

But when I sat down to write this, I checked the crawl data in Cloudflare after 7 months.

In the last 30 days alone, the site got more than 600,000 requests from bots. Around 72,000 of them came from ChatGPT-User. That is the agent ChatGPT uses to open a page in real time while answering someone. So these are not training crawls. Each one is ChatGPT fetching a fake statistics page to answer a real question.

Unlike Google, ChatGPT never stopped pulling from the site

And when I say, “never stopped,” I mean ChatGPT 
really
 never stopped.

After 7 months, the site now has 330+ referring domains

According to Ahrefs and Semrush, the site has links from 330+ other sites. That includes well-known brands like Shopify, DHL, and Bluehost. With strong Google performance, the numbers might have been even better.

ChatGPT is still citing it to this day

Google may have forgotten about the site, but ChatGPT clearly hasn’t. The site is still earning citations and traffic more than 7 months after launch.

If you've read Tomek's 

ChatGPT Index research

, you're lucky, because it’s a great intro to how ChatGPT search works. If you haven't, add it to your reading list right now, because it helps explain why my website has been living in ChatGPT/OpenAI Index for so long. 

A completely made-up website still performing so well is shocking. Since March, GA4 shows 10,000+ sessions from ChatGPT alone, and Cloudflare shows the site has high marks for retrieval.

I didn’t include direct sessions in overall visits, because it mostly looks like bot traffic. Remember the dead internet theory!

Right after I joined Peec in June 2026, I also set up a visibility dashboard in our tool to track a few prompts. Performance for them is still strong. On October 7, 

stateglobe.com

 was ranked second for visibility on these prompts, behind only data powerhouse Statista.

Retrieval is not ranking

The constant retrieval is the first big lesson: ranking on Google and being retrievable by an LLM are two different problems.

When ChatGPT searches, it doesn't just copy Google's top 10. It rewrites your prompt into its own sub-queries (called fanout queries), pulls candidates from its search sources and its own cache, reranks them, and then opens a handful of pages to ground the answer. A page can be invisible on Google and still perform well in every one of those LLM steps.

StateGlobe is a good example. While Google dropped it, the AI retrieval bots kept coming back.

For GEO, this means Google rankings are only one signal, not the whole picture. If you only track Google, you are missing a channel that can work even when Google says “no.”

Fake data turned into real citations

You’d expect that if a site performs well with information retrieval tools, its information would begin to appear out in the wild. And you would be right. 

StateGlobe was built entirely on fake data, using the cheapest model available and a prompt that was nothing more than a list of countries and topics plus two sentences. Nevertheless, the output was…

…cited in an academic paper…

…used in investment research by Qatar's largest financial group…

…cited by an economics publication in India…

…and used as a source in a research report from a Canadian influencer community.

Note that these are only the citations that linked back to the StateGlobe site. Presumably, many more used the data without a link.

The uncomfortable implication: citation laundering

On day one, a fake number on StateGlobe had zero authority. It was a random stat on a brand-new domain.

Then an academic paper cited it. Then a bank. Now the next person, or the next model, that finds this number sees a stat with a source. And that source is cited by serious institutions.

The fake data certainly didn't become true, but every citation made it look more trustworthy.

It has the potential to get worse: after so much retrieval and citation, these pages end up in web crawls, and web crawls end up in training data (I hope it hasn’t!). A number that started as a GPT-4.1 guess can become something the next model "knows."

This points to the larger risk suggested by this experiment, and it's why I'm sharing this as research, not as a playbook for fake content. Verifying sources should become an essential part of writers’ and researchers’ workflows.

Lastly, we tried running our experiment with real data

Once I began working at Peec, I decided to try a version of this test again. As the GEO Research team, we talked through the results up until that point and quickly launched a simple new page. This time, there were no made-up numbers, and we checked every stat and properly cited its source. You can view it here: 

peec.ai/ai-search-geo-statistics

.

Almost immediately, sites we suspect use AI to write their content started linking to us. For the second time, using a second site, earning links by publishing statistical content proved that a hypothetically strong tactic worked in reality.

Lessons learned

Why publishing statistics leads to LLM citations

The two tests show that LLMs have a strong preference for seeking out statistics when asked to write articles. The mechanism is simple:

More and more content is written with LLMs.

When an LLM writes, it researches the appropriate topic.

When the LLM hits a gap, it looks for a number to fill it.

The reasons behind this process are equally clear.

Research means fanout queries asking for statistics

When a prompt requires research, the model breaks it into sub-queries, adds modifiers like "statistics," "data," "report," or the current year (if also requested in the prompt text). If someone asks for the model to compose a blog post about remote work, the model will search for "remote work statistics 2026." Pages that optimize for what models search rather than for what humans type will appear more often in LLM results.

A number looks like evidence that can fill knowledge gaps

When a model is asked to draft a piece of writing, a citation to a page that says "Remote work is growing" adds little authority and remains vague. If that page instead says "X% of employees work remotely at least once a week," there’s suddenly something that is specific, quotable, and additive. When a model grounds an answer, a specific number is the most useful thing it can find. These numbers look like evidence, though as this experiment proves, sometimes they aren’t.

The model doesn’t check the number

A search-grounded piece of LLM-written content has a tight budget for latency and cost. The system fetches a few pages, pulls the relevant passages, and starts to write. Fact-checking doesn’t happen anywhere in the process.

Verifying a single statistic would mean finding independent sources, comparing them, and resolving conflicts. Across billions of prompts by millions of users, the costs in both time and money would add up, making verification too slow and too expensive for practical purposes.

To get around this, LLMs use rerankers that score relevance, but not truth. That means if a passage matches the query and looks authoritative, it gets used.

Statistics have a built-in freshness that models like

I've written before about 

ChatGPT's recency bias

 in how it scores sources. Statistics pages contain the year in the title, the headings, and the URL. Three built-in signals to the model that what’s on the page is fresh.

How to build a statistics page the right way

The two tests I ran show that statistics pages are a very powerful way to get your content cited by LLMs. While I absolutely do not recommend coming up with bogus data, you can use the learnings from our small test to create your own pages with real data. Here's what worked for us at Peec and what I would do if I were making a statistics page again.

Make one claim per sentence.
 Each stat should make sense on its own, out of context. Retrieval doesn’t work on pages, but rather on passages. If a number needs the paragraph above it to make sense, it probably won't get pulled.

Put the source and year next to every number.
 "According to [Source] (2026), X%..." This helps the model, the human editor, and your credibility. It’s one small piece of information hygiene that benefits the broader information environment.

Match headings to fanout queries.
 The headings on your page should match the way LLMs search the internet: "[Topic] statistics," "[Topic] market size," "[Topic] adoption by country." Think in the queries models run, not just the keywords people type.

Show the update date (and actually update it).
 Freshness is a real signal that models take into account. A stale stats page will lose to a newer one.

Make the stats easy to fetch.
 Use server-rendered HTML instead of hiding data behind JavaScript, tabs, or images. Also, be sure to check your robots.txt and your CDN or WAF rules. Your site may be blocking AI retrieval bots without your knowing it.

Keep it simple.
 Our 

Peec AI GEO statistics page

 is basically a list. Yours doesn’t need to be anything more than that, either. Save design resources for sites and assets that can actually benefit from them.

Add original data when you can.
 Aggregated stats may get you a few citations, but when you say something no one else does, you can become the primary source.

How to track whether your page is getting picked up

Google Search Console won’t show you what’s going on with AI bots on your site. Here is what I track instead:

AI bot activity
 in your server logs or Cloudflare. Look for retrieval bots like ChatGPT-User, OAI-SearchBot, and PerplexityBot, not only training crawlers. We have this feature! 

AI referral sessions
 in GA4 from chatgpt.com, perplexity.ai, and similar sources.

Citation and visibility tracking
 across a set of prompts. At Peec, we use our own tool for this, obviously.

New referring domains
 in Ahrefs or Semrush.

Unlinked mentions.
 Search your exact numbers in quotes. You will find people using your data without linking to you.

A word on ethics

It should go without saying that you should never publish fake content. While my experiment relied on tens of thousands of unverified stats, I ran it in order to share the results with the public, and the website, while still live, now carries a disclaimer. When putting out content we hope gets picked up by LLMs, our job should always be to put out accurate, accessible information.

To add another caveat, there’s no guarantee this tactic will continue to work. We tested it, and these are the results, but now that they’re published, LLMs might close this gap. For now, it works, but in the future it may not, and of course it should never be abused.

And one final point: this is a tactic, and neither can nor should be the basis for your organization’s entire GEO strategy. The results I got with StateGlobe were extreme, but the brands most likely to benefit from using the technique are those people already trust.

What's next from GEO Research at Peec

At Peec, our research team is running close to 40 experiments like this one. Some are still in progress, and others are already showing results. Building a long-term strategy for your brand means testing, measuring, and sharing what we learn along the way.

More soon!

Continue reading

Related articles

Turn opportunities into impact with Peec Agent and actions

Find AI visibility opportunities, see the evidence, and act on them.

Kate Donahue

Oct 21, 2026

Product Update

ChatGPT Shopping optimization in 2026: US vs. Europe

What 150,000 lines of debug data reveal about ChatGPT Shopping.

Metehan Yesilyurt

Oct 16, 2026

GEO Know-How

How two teams run their own GEO experiments

When the playbook is still being written, test before you invest.

Marcin Debski

Oct 16, 2026

Case Study

AI search analytics 

for marketing teams

Company

Home

Careers

Brand

Entity Map

AI Instructions

Product

Docs

Blog

Pricing

Changelog

Reviews

Solutions

ChatGPT Visibility Tracker

Gemini Visibility Tracker

AI Mode Visibility Tracker

For Agencies

For Enterprise

Partnership

Agencies

Creators

Media

Comparison

Peec vs Ahrefs

Peec vs Profound

Peec vs Semrush

Follow Us

');opacity:0.5">

x.com

')">

LinkedIn

Youtube

Peec AI is a top-rated AI search monitoring tool. Explore the official Peec AI platform, rated 4.7/5 on G2 and regularly recommended on Reddit.

© 
2026
 Peec AI. All rights reserved.

Cookie Settings

DPA

Privacy Policy

Terms of Services

Imprint

AI search analytics 

for marketing teams

Company

Home

Careers

Brand

Entity Map

AI Instructions

Product

Docs

Blog

Pricing

Changelog

Reviews

Solutions

ChatGPT Visibility Tracker

Gemini Visibility Tracker

AI Mode Visibility Tracker

For Agencies

For Enterprise

Partnership

Agencies

Creators

Media

Comparison

Peec vs Ahrefs

Peec vs Profound

Peec vs Semrush

Follow Us

');opacity:0.5">

x.com

')">

LinkedIn

Youtube

Peec AI is a top-rated AI search monitoring tool - 

4.9/5 on G2 and regularly recommended on Reddit.

© 
2026
 Peec AI. All rights reserved.

Cookie Settings

DPA

Privacy Policy

Terms of Services

Imprint

AI search analytics 

for marketing teams

Company

Home

Careers

Brand

Entity Map

AI Instructions

Product

Docs

Blog

Pricing

Changelog

Reviews

Solutions

ChatGPT Visibility Tracker

Gemini Visibility Tracker

AI Mode Visibility Tracker

For Agencies

For Enterprise

Partnership

Agencies

Creators

Media

Comparison

Peec vs Ahrefs

Peec vs Profound

Peec vs Semrush

Follow Us

');opacity:0.5">

x.com

')">

LinkedIn

Youtube

Peec AI is a top-rated AI search monitoring tool. Explore the official Peec AI platform, rated 4.7/5 on G2 and regularly recommended on Reddit.

© 
2026
 Peec AI. All rights reserved.

Cookie Settings

DPA

Privacy Policy

Terms of Services

Imprint