---
title: "Rebound Project | Ben E. C. Boyter"
url: "https://boyter.org/2015/01/rebound-project/"
fetched_at: 2026-05-05T07:02:02.953218+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Rebound Project | Ben E. C. Boyter

Source: https://boyter.org/2015/01/rebound-project/

As I mentioned in the previous entry I had started work on a new project I called portfold. Built and released without fanfare I have quietly killed it before even the month is out. Why? I realise now that it was a rebound project similar to a rebound relationship. I had been getting a little down on searchcode.com and wanted to branch out to some new technology. Once done though the itch was scratched and now I am back to working on searchcode again.
There have been a few long standing issues with searchcode that I have finally tracked down and fixed. Quickly I am going to outline what each was and what I did about it.
The first issue was that if you filtered down the results using the right hand controls that they would be lost the moment you paged through the results. I cannot remember why I didn’t implement this the first time thought I suspect it was due to issues with the code dealing with non existant filters which I had since fixed.
Another issue was that when paging thorough results sometimes searchcode would report a page where none existed or when you paged through only had a few results rather then the 20 that should be there. This one took a long time to track down. The root cause turned out to be a slight difference between how code is indexed vs searched. When searchcode indexes it performs various splitting operations over the code to ensure that a search for
api.duckduck.com
will find results with that exact term. It also splits it so a search for
api duckduck go
will also work. This process works when performing a search as well, however its not the same logic due to one being done in sphinxes index pipeline and the other in Python logic. The result is that I neglected to implement the split on the singe . in the search logic. Very annoying to say the least. I had been getting bug reports for a while about it and had built a very large bug report on it. One of the main issues with it was being unable to replicate it on my local machine. This is due to the size of the data which has outgrown the ability for a single machine to deal with.
One other annoying issue was the parsers for source code had a nasty habit of crashing the instance they were running on which required a reboot to resolve. I run these on the smallest possible digital ocean instances. Turns out that by default these do not have any swap space, which ended up causing the issue. Thankfully adding swap space is relatively easy and they have now been running for days without issue. I have since queued up another million or so projects to index and should be searchable soon.
The last issue and one I am still addressing is performance. I was a little disturbed by how long it was taking for even cached results to return. A bit of poking around concluded that all of the ajax request to get the similar results where flooding the available gunicorn workers I had on the backend. This needed to be rectified. The first step was to setup nginx to read cached results directly from memcached and avoid hitting the backend at all. The second was to increase the number of workers slightly. The result is that the page does load a lot faster for the average request now with less load on the server.
In addition to the above fixes I have also added a new piece of functionality. You can now filter by user/repo name. This works in a similar manner to the existing repo filter however you need to supply the username first and delimit with a forward slash. An example would be a search for
select repo:boyter/batf
All in all I am happy with progress so far. The current plan is to focus on upgrading the API such that everything is exposed for those who wish to build on it. This will include public API’s for the following, getting a code result, finding related results, advanced filters, and pretty much everything required to in theory create a clone of searchcode. In addition I want to expand the index as much as possible by pulling in bitbucket and more of githumb. As always any feedback is greatly appreciated and I do try to implement requests.
