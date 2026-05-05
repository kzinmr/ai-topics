---
title: "At Scale You Will Hit Every Performance Issue"
url: "https://boyter.org/2010/08/at-scale-you-will-hit-every-performance-issue/"
fetched_at: 2026-05-05T07:02:08.025967+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# At Scale You Will Hit Every Performance Issue

Source: https://boyter.org/2010/08/at-scale-you-will-hit-every-performance-issue/

I used to think I knew a bit about performance, scalability and how to keep things trucking when you hit large amounts of data. Truth is I know diddly squat on the subject since the most I have ever done is read about how its done. To understand how I came about realising this you need some background.
Essentially what I have been working on and hope to launch soon is a highly vertical search engine that websites can employ on their site and get highly relevant search results. Something like Googles website search, but custom for your website with tight API integration or just a simple “index my website and stick a search box here” sort of thing. While doing this I have learnt more about operating at scale then I would have ever imagined.
So to begin with I had the idea, and all was good. I coded up the initial implementation pretty quickly and had it working pretty well for my initial runs of a couple of hundred pages. The next thing to do was point it at a live website and see how it goes. I seeded the crawler with about 50,000 URLs and set it loose. This is where problems initially began.
The first issue I discovered was in my crawler. I initially set it up to run as one long process which pulled down the list of URLs to crawl. This had the issue that it consumed massive amounts of memory and CPU pretty much all the time. So I made the decision to change it to a short lived process that ran every minute. All was well for a while. It fired up every minute (cron job) and sucked down 20 pages or so. This was fine till the website it was crawling slowed down a bit and it took over 1 minute to pull down the pages. The next process kicked off slowing the site down even more. Within 20 minutes about 15 instances of the crawler were hammering the site and eventually it died under the pressure.
So naturally I needed to think about this again. I added a file lock to ensure only a single instance of the process could run at any one time. Works fine till your crawler dies for some reason without releasing the lock. So I switched to a port bind and everything is hunky dory. Considering the crawler finished I moved on to other issues.
I then did some trial runs against websites crawling and indexing anywhere from 1,000 to 50,000 pages without any problems following the latest changes.
So I fired up the next step. A full index of a website. This involved loading my crawler up with a single seed URL and telling it to harvest links as it goes. The next issue I ran into was problems with the crawler not parsing out crawled websites correctly. Trying to anticipate every form of html content in a page is more difficult then you would think. The thing is when pulling down a page you need to extract the useful information you want to index on and clear out the rest. Since people search on words you need to remove all the other crap. Javascript, CSS, etc… Something I neglected to consider is that you can have in-line styles for CSS. Its one of those things I never encountered on my run of 50,000.
So some quick modifications and I’m getting clean content back.
Everything was fine till I hit the next hurdle. When getting the next batch of URL’s to crawl I do a simple bit of SQL to pull back the URL’s that need to be crawled. IE those which haven’t been hit in a while, those which don’t have issues (IE failed to respond the last 3 times) aren’t marked as deleted or have been asked to be re-crawled. Its a pretty simple bit of SQL. Guess what, all of a sudden it started to slow down. What was taking 1 second at 50,000 URL’s was suddenly taking 4 minutes at 300,000 URL’s. Now partly this was due to me changing the schema as I went, but mostly it was down to poor indexes and pulling back too much data. So some index fixes, a dump of the database and a re-import and the query is down to 1 second again.
So what have I learnt from all of this?
Never assume. Profile profile profile! The cause of a performance issue is never what you expect it to be. My thought it was MySQL insert performance was way off. In fact I wasted a few hours looking into something that wasn’t even an issue. I cant afford to waste time like that.
You will never hit any of the big issues until you actually go to a “live” state. Be prepared to spend time looking at things you wouldn’t have expected to slow down or cause issues.
Unit test your code! Write unit tests to prove a bug exists, then fix it. This saves time in the long run.
