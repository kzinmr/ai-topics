---
title: "Why Writing a Web Crawler isn't Easy"
url: "https://boyter.org/2010/08/why-writing-a-web-crawler-isnt-easy/"
fetched_at: 2026-05-05T07:02:08.217060+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Why Writing a Web Crawler isn't Easy

Source: https://boyter.org/2010/08/why-writing-a-web-crawler-isnt-easy/

The below is just a few things to keep in mind if you are writing a crawler or considering writing one.
The first is to assume that all of the links you have are broken to begin with. When I write this I dont mean assume that the link goes nowhere, but that the URL itself is actually wrong. Even when you seed your own list (like I did) you can still get some bad URL’s in there.
Assume all websites are slow. If you assume that the website is a lot slower then yours and that it can take pages seconds to render then you are on the right track. Not assuming this means you might spawn more threads or processes to crawl then the website can respond to. Not only does this mean you get a lot of connection errors you can effectivly kill the site though an unintentional DOS attack.
Assume you have more bandwidth. This might seem to be the wrong assumption, because odd’s are if you are writing your own crawler you don’t have as much bandwidth as Google, Yahoo or Bing. That is probably true, but as a technical person you probably will have more bandwidth then most people. Better to be safe, assume you have more bandwidth and throttle back before killing a site with your uber crawler.
When running a process ensure you have some form of mutex, file lock or socket bind to prevent other instances running concurrently. This also seems probably counter intuitive but trust me it isn’t. If you don’t lock down the process, and then add it into your crontab or some other scheduler you may end up in the situation where your first process is still running (because the sites you are crawling are stressed) and the second process kicks off. This slows the site down more, causing more processes to overlap, slowing the site more etc… This ends only when someones code crashes, and on most websites which are database heavy odds are it will be them. Lock your process down initially and then spawn out a specific number of threads or processes. This way you can accuratly say “No more then 100 pages from this site will be crawled per minute”.
Dont assume timeouts will save you. Adding timeouts to connections will not save you from having to consider and implement all of the above. You can still kill a website pretty quickly by getting thousands of connections all waiting on something in their stack (database, cache, presenter etc..) to catch up.
You will not find bugs in your crawler until you have crawled a large amount of pages and by then it will be too late. It took several runs of 50,000 pages til I ironed out most of the bugs in my VERY simple crawler and make it stable.
Be patient. It takes a long time to get the crawler up, working correctly and behaving in a predictable manner. You will make mistakes and bring websites to their knees. You will crawl in an endless loop some form of spam capture site. You will have bugs that only occur after hitting 100,000 pages and you cannot replicate.
So what should you do? Looking back I should have taken the following approch. Model your crawler as you would a highly secure server. Remove network connectivity. Remove all moving parts. Lock it down. Lock it down so tightly it cannot do anything. Think. What do I need to remove to get it working? How can I remove the restriction in the most restrictive way possible. By thinking backwards you can be dammed sure you arent going to encounter problems later on.
