---
title: "Billions of lines of code"
url: "https://boyter.org/2012/07/billions-of-lines-of-code/"
fetched_at: 2026-05-05T07:02:05.392226+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Billions of lines of code

Source: https://boyter.org/2012/07/billions-of-lines-of-code/

Billions of lines of code
2012/07/16
(267 words)
Recently I fired off the spiders to pull in an additional 30,000 projects I was aware of and then added them to the index. The result being searchcode now has 3.8 billion lines of code indexed. The exact count being 3,863,756,553 lines. Of course the reason this is most exciting for me is that koders.com which is the default code search (now that Google Code search has been retired) has 3.3 billion lines of code index according to their website. Of course, searchcode does index anything considered “textual” data so there is a lot of non-code results in the index so the counts are probably fairly close in terms of what’s relevant. In short though, for a single person operation running on a single server I think its pretty impressive.
In other news I have cleaned the index of “compiled” code. Essentially any result with extremely long lines has been stripped. An example of this would be minified JavaScript libraries such as jQuery which made searching rather painful sometimes. With the cleaned index things like “
jQuery
” produces reasonable results.
What’s next? I am starting to play with blending of results. There seems to be a lot of people expecting to search “mysql_query” and get both the API documentation and code examples together which makes sense. I am also looking to integrate my own web results for selected websites with Bing turning off, but how soon this gets rolled out depends on how well I can get the results to turn out. In short come back and check now and then as exciting things are in the pipeline.
