---
title: "One hundred million little queries"
url: "https://boyter.org/posts/one-hundred-million-little-queries/"
fetched_at: 2026-05-05T07:01:55.080939+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# One hundred million little queries

Source: https://boyter.org/posts/one-hundred-million-little-queries/

I recently X’ed/Tweeted about how my searchcode.com since Nov 2022 using its custom index
https://boyter.org/posts/how-i-built-my-own-index-for-searchcode/
had processed over 50 million queries with a rolling average time around 80ms to process them.
That was a low-ball estimate though. I actually checked and its actually just over 100,000,000 queries. Which I find astonishing considering its running though a index I wrote.
However that number excludes all of the attempted queries. As you may expect any public search engine, especially one with a public unauthenticated API is pretty constantly hammered by bots. So what about those?
I had previously written about
how I rate limit searchcode
, with the usual reddit response of “Just use tollbooth”. However as I wrote then, writing a rate limiter isn’t that difficult, offers me a great deal of control and is fun to write. The reason I work on searchcode is to solve interesting problems, not just ship a product. If you never write anything yourself how do you ever expect to grow and learn?
The limiter mentioned there has expanded a bit since and now offers the following benefits
Identifies problematic queries and instantly penalizes the IP
Has a slight bust limit for the first minute
Punishes known repeated bad actors punitively
Auto adjusts limits based on current system load
Prioritizes HTML users over API
Prioritizes self preservation over everything else
Special treatment for certain IP’s based on negotiation with yours truly
Has an upper limit of punishment that works out to be months of delay
Note while it prioritizes HTML users, don’t think that scrapers have a free pass. They run through the same rules. However it does mean if you are prepared to scrape the HTML in theory your queries will be prioritized over the JSON ones in terms of who goes first. However if you are staying in the limits, you may as well just use the API and avoid having to write HTML parsers.
As such its hard for me to actually say what the rate limits are since they vary based on outside influence but they are fairly generous. Even so there are a lot of IP’s that well frankly aren’t getting the message, despite searchcode responding with a HTTP 429 StatusTooManyRequests, a Retry-After header and a slightly snarky JSON response of
{"url":"https://en.wikipedia.org/wiki/Exponential_backoff"}
So what happens if we estimate how many queries we would have responded with if we did allow these jokers through?
There is an upper limit on the time searchcode allocates IP’s to gaol with 6000+ IP’s that are currently blocked. Some are seriously blocked too, with for example 108.181.22.197 having its count value set to 100,000,000 which is the upper limit allocated in the system.
Distilling this down to a number is hard, but good news I keep track of that too! So with 100,000,000 legitimate queries, throw in the blocked queries and searchcode is looking at having processed over 500,000,000 queries since I replaced the index with my own. Say it has half a billion and that is an impressive number.
Anyway I was going to link to a github gist here containing all of the problematic IP’s I have been dealing with but apparently thats an invalid request and I have been requested to not do so again. So I shall link it below and pray my poor server does not get hard linked as spam list source. If you do need the list please take a copy.
badip.txt
Probably no need to do anything with this list, but if you own one of the IP’s listed there you might want to go check for rogue processes and/or fix your code.
