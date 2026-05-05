---
title: "AWS Abusing Search Engine Gets Abused"
url: "https://boyter.org/posts/aws-abusing-search-engine-gets-abused/"
fetched_at: 2026-05-05T07:01:56.790288+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# AWS Abusing Search Engine Gets Abused

Source: https://boyter.org/posts/aws-abusing-search-engine-gets-abused/

Some time ago I wrote about building an Australian search engine by abusing how AWS Lambdas work. You can view it at
bonzamate.com.au
, and read the
post about it here
.
Recently I noticed that Bonzamate.com.au was in turn being abused by a series of bots repeatedly making queries against it.
Now normally I don’t worry about bots. There is little you can do to stamp them out entirely, and its always nice to see someone trying to exploit the things you work on. However should the bots either result in degraded service or in this case increased personal costs to me I will actively try to work against them.
See the thing about bonzamate is that it costs nothing, so long as nobody is using it. When it is running queries they are usually fairly inexpensive and generally slider under the free AWS tier.
I was reviewing my costs and noticed that the number of lambda invokes had skyrocketed.
The above shows from when I turned off the service, then back on once I had some limiting in place. That many invokes of Lambda if left unchecked would result in fairly expensive cost to me of many hundreds of dollars. Looking deeper into this showed the cause.
In short automated scanners looking for websites to exploit, or spam.
By default bonzamate has a
rate limiter
in place. Its based on code I lifted from searchcode.com. You can use it, but rapid fire queries will eventually land you in the sin bin and every response will return with the slightly snarky response,
{"url":"<https://en.wikipedia.org/wiki/Exponential_backoff"}>
This however was only applying to pure requests. What was needed is to also factor in the query itself, since the query allows a better determination of what could be spam. The result was a new
isSpam
function with looks at any query passed in. Based on the type of queries we are looking at it does not need to be too smart. As such it considers the following,
Looking for spam words such as yabb, powered by, cgi-bin, traceback, .php, guestbook
Counting how many terms are in the query
Counting how long the query is
How much of the query is non english text
With the above all adding to a score which is returned, I can then determine if the query looks spammy. This is further broken down into something being obviously spam, or something that looks spammy.
In the former case the ip address that called this is instantly assigned a high value which results in the rate limit being applied instantly for an hour or so. The latter allows the query to run, but ensures they need wait a minute or so.
I also changed the limiter to be more punitive. If you keep making queries when limited it keeps adding to the cooldown value. The final step was to persist the list of spammy ip’s and their cooldowns so restarting the service does not allow them a free pass.
With that implemented all of the spam is now gone.
All of the above 400 responses are 429 responses.
Some bots clearly don’t respect those 429 responses. In fact here are is sample, that despite getting 429 responses over the last week have then continued to make hundreds of thousands of queries. Hopefully at some point the bot operators realise something is wrong and do something about it.
"196.196.194.123": 635414,
"196.196.194.86": 623684,
"196.196.194.95": 614114,
"196.196.195.55": 644328,
"196.196.197.22": 651979,
"196.196.198.213": 631779,
"196.196.198.67": 640054,
"196.196.198.78": 639051,
"196.196.198.95": 641331,
"196.196.220.21": 619319,
"196.196.222.79": 636529,
"196.196.31.191": 635040,
"196.196.31.246": 640176,
"196.196.31.92": 619990,
In fact its actually fun watching them continue to hit the service. You can see IP’s being blocked in real time by watching the logs, as well as see the queries that caused their spam status to be accounted for.
Is this the end of fighting spam? Probably not. However it solves my immediate problem, and allowed me to work on some UI and various other improvements for bonzamate. More on that to come.
