---
title: "Improving the Index"
url: "https://boyter.org/2012/02/improving-the-index/"
fetched_at: 2026-05-05T07:02:05.737317+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Improving the Index

Source: https://boyter.org/2012/02/improving-the-index/

The last couple of weeks I have been spending improving the index based on feedback about duplicate results. When indexing source code you will find a lot of duplicate libraries and copied code all over the place. Usually when searching for something like jQuery you don’t want to see thousands of results of the same file. However when searching for method calls you do want to see results which call the method in a similar way as you may be looking for examples of how to use it.
This makes trimming out duplicate content harder then it seems initially. You can’t just throw out any results that look similar as they may actually be what you are searching for in the latter case.
Initially searchco.de was stripping out duplicates based on a hash of the files contents. This was particularly effective in stripping out copied files and libraries such as jQuery. Where it did fall down however was any file slightly modified such as with an additional newline, or a new version with a few bug fixes. With bug fixes and slight modifications occurring all over the place you end up with a lot of duplicate content. As the amount of code indexed increased this became more and more of an issue to the point that some searches had pages of useless results as each result was 99% the same file.
The example presented to me was a search for
glGetFragDataLocation
. The file glop.cpp would be repeated over and over again in multiple variations of what was fundamentally the same thing. At the time I was working on a solution to the issue but it was very nice to get a concrete example.
There are two methods of removing duplicate content in a search. The first is to pre-process it (like the hash that was already in use) and the second is to do it at runtime. The former cuts down on processing time, while the latter is a little more flexible as you can tweak your algorithm on the fly and code around edge cases. The recommendation of Anna Patterson of Cuil fame is to
sort out duplicate content at runtime
.
My personal experience in this sort of thing however is going for a hybrid approach. Pre-processing has advantages such as less overhead when serving results and since I don’t have infinite resources its useful to cut down the amount of work required at runtime where possible.
The long and short of this is that you should notice search results for queries to return gradually better and better results from this point. The hash checking still remains (cheap and fast) but I have expanded this to include duplicate content checks for results. This is done through a combination of a backend process running checks over content identifying and marking content as being a duplicate and checks when serving up the results to identify which results should be stripped out. Have a spin and let me know how it works out for you.
