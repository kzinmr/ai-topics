---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2014/07/feedback-loop/"
fetched_at: 2026-05-05T07:02:03.133985+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2014/07/feedback-loop/

About a month ago searchcode.com managed to sit on the front page of Hacker News (HN) for most of a day and produced a lot of useful feedback for me to act on. You can read the full details here
searchcode: A source code search engine
Between the HN feedback, some I received via tweets and from republished articles I got a list of things I needed to work on.
The first and main change requested was over the way searchcode was matching results. It was by default looking for exact matches. Hence if you searched for something like “mongodb find” it would look for that exact text. It was requested by quite a few people to change this. The expectation was that the matching would work like Githubs. This has now taken effect. A sample search that came up is included below with the new logic,
https://searchcode.com/?q=MongoDBObject+find+lang%3AScala
vs
https://github.com/searchq=MongoDBObject+find+language%3Ascala&type=Code&ref=searchresults
I believe the results are more in line with the expectation.
The second thing requested was that I point at the new Google endpoints for GWT and Android. This has been done and the code is currently sitting in the queue ready to be indexed. I expect this to take place in the next few days. In addition I have pulled in a lot of new repositories from Github and Bitbucket using their API’s. The number of projects now being indexed is well over 5 million and growing every day.
The last request came from the user chdir on HN. I hope they won’t mind but I have included their request below,
“I use sourcegraph occasionally and mostly rely on Gihub search. I wish the search has all those advanced refinement options that grep & Sublime Text search has. Some examples would be to use regex, search a word within a scope of lines, search within search results etc. Additionally, it’s very useful to be able to sort the search results by stars/forks. Sometimes I just want to see how popular projects have implemented a certain feature. A keyword based search isn’t enough for that.
I guess these features are very expensive & slow to implement but it would be super useful if it can be achieved. Source code search is for geeks so it is probably fair to say that a truly advanced & complex interface won’t turn away users.”
The above is actually one of the more difficult requests. However its suggestions are on my radar of things to do. To start with I have rolled out an experimental feature which displays matching results. One of the issues with codesearch is that being good developers there is a lot of duplicate code used in various projects. Since when you search for something like “jquery mobile” you don’t want to see the same file repeated thousands of times you need to work out the duplicate content and filter it out.
Sometimes however you want to see those results. Its a piece of functionality that existed in Google Code search which I had wanted implemented for a long time. Well it is now here. The duplicates are worked out using a few methods, matching MD5 hashes, file-name and a new hash I developed myself which converges the more similar the files are. Similar to simhash this new has however does not require any post calculation operations to determine if two files are a match. More details of this will come in a later post after I iron out all the kinks.
Anyway you can now see this functionality. Try searching for “
jquery mobile
” and look next to the title. You can see something along the lines of “Show 76 matches”
Clicking the link will expand out the matching files for this result. Each of the matching results shows the filename project and the location in the project. All of course are click-able and link to the duplicate file.
Lastly you can also do the same on the code page itself. Just click “Show 5 matches” on the top right of the result page to see a list of the matching files.
There is more to come in the next few weeks which I am excited about but for the moment I would love to get feedback on the above.
