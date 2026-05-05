---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2012/06/codesearch-api/"
fetched_at: 2026-05-05T07:02:05.469911+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2012/06/codesearch-api/

Happy to announce that the CodeSearch API is now alive and kicking for those who wish to use it. The details are included below.
Example calls,
JSON
http://searchco.de/api/codesearch_I/?q=%23define
http://searchco.de/api/codesearch_I/?q=IO::pipe
http://searchco.de/api/codesearch_I/?q=goto%20lang:perl
http://searchco.de/api/codesearch_I/?q=test%20lang:perl&p=1
JSONP
http://searchco.de/api/jsonp
_codesearch_I/?q=%23define&callback=CALLBACK
http://searchco.de/api/jsonp
_codesearch_I/?q=IO::pipe&callback=CALLBACK
http://searchco.de/api/jsonp
_codesearch_I/?q=goto%20lang:perl&callback=CALLBACK
http://searchco.de/api/jsonp
_codesearch_I/?q=test%20lang:perl&p=1&callback=CALLBACK
Parameters are,
q = query
p = page
The return results are pretty self explanatory, except that they include a modeltype which indicates what sort of match it was, the types being
exactmatch, closematch, regexexact, regexclose
They allow you to highlight lines. Exact match means you entered a non regex IE not wrapped in / and there are exact matches. Close match means it couldn’t find anything exact and reverted to a loose match. Same with regexexact and regexclose except the first uses an exact regex match.
The other important part is the below,
Page = The page is just the page you are on.
Total = total number of results. You are limited to browsing 1000 though (just like Google)
Query = the exact query passed in
Matchterm = what we match on IE ignoring the lang: and ext: syntax
Regex = if its a regex search this is the regex used to match
Generalregex = loose matching regex for close matches
Nextpage = if there is a next page will have the id of the next page
Previouspage = if there is a previous page IE not on 0 will point at the previous page
Cs = Used internally, but just indicates its a code search
“page”: 0,
“total”: “1000”,
“query”: “/test/ lang:perl”,
“matchterm”: “/test/”,
“generalregex”: “/test/i”,
“regex”: “/test/”,
“nextpage”: 1,
“previouspage”: null,
“cs”: true
That should be enough to get you started. There are examples of how to call this in the DuckDuckGo spice project. If you do use this I would love to get a link so I can display it here, and a link back would be nice.
