---
title: "Go Forth and Search"
url: "https://boyter.org/2015/09/search/"
fetched_at: 2026-05-05T07:02:01.514449+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Go Forth and Search

Source: https://boyter.org/2015/09/search/

Go Forth and Search
2015/09/02
(247 words)
A very fast update. At the request of the excellent
Lars Brinkhoff
via GitHub I have added in the language Forth to be one of the supported languages inside searchcode.
An example search which shows this working would be the following
https://searchcode.com/?q=forth&loc=0&loc2=10000&lan=181
I had to solve a number of interesting problems inside searchcode to support this change. For pragmatic reasons the way searchcode identifies what language any piece of code is written in is to run it though CLOC (Count Lines Of Code). Written in perl it does a reasonably good job of pulling out metadata for any given piece of code. However since my perl ability is poor at best submitting a patch to support forth was not going to be an option.
Instead I ended up adding an additional few checks at the end of the indexing pipeline to identify code that probably should have been categorised as forth and if so change the classification. It has been designed to be extensible so if other languages come up that are not currently identified it should be possible to add them as well.
The only other change of note for searchcode is that I fixed the SSL certificate chain and now you can curl the API again. This was an issue caused by Google throwing its weight around and outlawing SHA1 certificates. When updating to fix this I neglected to fix the chain as well. Oddly browsers worked without issue whereas curl and Python requests broke.
