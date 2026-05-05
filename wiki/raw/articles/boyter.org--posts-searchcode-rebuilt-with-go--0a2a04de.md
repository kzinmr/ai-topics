---
title: "searchcode Rebuilt with Go"
url: "https://boyter.org/posts/searchcode-rebuilt-with-go/"
fetched_at: 2026-05-05T07:01:57.893133+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# searchcode Rebuilt with Go

Source: https://boyter.org/posts/searchcode-rebuilt-with-go/

So as of about 12 hours a new version of
https://searchcode.com/
has been rolled out. It marks the biggest update to the site in over 4 years since I moved over to version 3 which you can read about
https://boyter.org/2016/07/searchcode-com-architecture-migration-3-0/
The reason for it was that searchcode has always been something I kept running as a showpiece. It’s something that I can point to publicly and say “I did that”. The idea being to ensure I remain employable. Recently though I was becoming ashamed of its look, performance and instability. I briefly considered selling it and had some interested parties although I think with COVID-19 rampaging that feel by the wayside.
The previous version of searchcode.com was written in Python using Django. In hindsight that was probably a mistake. I chose Django because iconfinder.com was written using it and I wanted to get more experience with Python. While that probably did get things moving more quickly at first it became messy pretty quickly. Reasons for this include,
The Django admin pages could not deal with size of the tables in searchcode.com
Because the admin pages didn’t work I lost one of the main benefits of Django
Deploying Python web applications is a major PITA. Having to configure gunicorn and such was annoying
Python while pushing all the happy parts in my brain is not suited to large applications (3rd time this has bitten me)
Python performance was a bit of an issue, and one I kept running into given how the site works
The code got very ugly as I was hacking around the way Django worked
Probably the biggest impediment to me actually upgrading was styling. I am not a designer, and while I can do html/css to a reasonable level when required I am at heart a back-end engineer. When the following MVP style-sheet popped up on hacker news
https://andybrewer.github.io/mvp/
I quickly threw together a simple homepage (which is what you see at searchcode.com now) which looked alright and then just followed through with the rest of the site.
With the styling done I turned to the actual back-end.
Interestingly searchcode server is written Java. I chose Java for it at the time because Java is a pretty good language, works almost everywhere, has fantastic tooling and most importantly has lucene. This allowed me to build the indexing engine into it. About one year ago I started modifying it to support multiple backend indexes. The idea being I could use one shared code-base between the two different tools.
It ended in failure. I had made decisions inside searchcode server that did not translate well to searchcode. In addition one of the main issues with Java is the syntax highlighting. There is no decent library that exists in the java world today which you can put in some code and get back highlighted HTML syntax. Believe me I tried. You can use Pygments with Jython but it turns out to be too slow for a lot of inputs. In the end I implemented a small binary
https://github.com/boyter/searchcode-server-highlighter
in Go which uses Chroma to highlight. My plan was to spin that up in the back-end and pass back code to highlight.
Probably however the failure was due to having too large a scope. I was trying to upgrade the site, modify the backend, modify the data store, convert across across the crawlers/parsers and it was just too much. I ended up not continuing a while back and had been working on some other side projects.
Those side projects just happened to be very useful when it comes to dealing with code. Sloc Cloc and Code being one and another being a command line code search tool.
I realised after playing around with them that I could probably bring together all of this code I had just written with the HTML/CSS using MVP and I could bang out a copy of searchcode very quickly. Especially if I cut scope to only upgrade the front-end and search and worry about the indexing later.
Several weeks later and it is here. A few changes were made though.
I am now using redis as the cache coupled with a “level 1” cache in memory (github.com/allegro/bigcache). The level 1 cache saves on a network request, and as know the fastest network request is the one you don’t take. If an item is missed from level 1 cache it looks to level 2. If found in level to it sticks the item into level one to save the next request. If an item is missing from both it hits the back-end then puts it into redis and the level one cache. I have never really used redis in anger before. I remember reading about its memory model back in 2016 and since it was susceptible memory fragmentation decided I would stick with memcached. This however has improved recently and as such I decided I would give it a try. As such I have the following config values set.
maxmemory 8000mb
maxmemory-policy allkeys-lfu
LFU seems like it might work better for searchcode rather than LRU but I have no metrics to back that up. Looking at the stats out of it its memory fragmentation ratio is set to 1.0 which so it appears there are no issues there at least. I may try changing it around in a week or so and observe the difference on hit ratios.
A few other changes made in the interest of performance include that indexing and display (by default) is limited to the first 50kb of the file. I guess a final point of notice is that I blew away and rebuilt the indexing machines using Ubuntu 18.04 as an upgrade 16.04.
Anyway I did try to keep everything working for those using the API’s and ensure that all inbound links work. As always if you do run into issues please let me know @boyter
