---
title: "Who Knows Regex | Ben E. C. Boyter"
url: "https://boyter.org/2012/05/who-knows-regex/"
fetched_at: 2026-05-05T07:02:05.607408+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Who Knows Regex | Ben E. C. Boyter

Source: https://boyter.org/2012/05/who-knows-regex/

Who Knows Regex
2012/05/13
(269 words)
Apparently not many. I have been monitoring how the search has been used since I rolled out code search and noticed that most people are just typing in search terms and not regex search terms. Of course this means some results are not what people are expecting.
I have thus changed the way searches work. It now does an exact match of whatever it is you are looking for UNLESS you wrap your search term in / in which case it will default to a regex search. Take for example the following,
[cb]at
vs
/[cb]at/
The first will search for the exact term “[cb]at” whereas /[cb]at/ will expand out to search for terms cat OR bat anywhere in the file.
The change is slight, but should make things more accessible for most people since it is obvious through what I have been seeing that people just expect to type into a box and get results back. The only other change is that I have disabled the “Google” instant inspired search for any code search IE when the checkbox is checked. The reason being it fired off so many requests and my megre hardware was unable to cope. I think it actually works better now, but I can always turn it back on later should hardware increases permit.
Finally I had a look at the backend and it looks like there are over 2.5 billion lines of code indexed now. I do have plans to pull all sorts of interesting stats out of the code and display it on the front page but that’s a subject for another blog post.
