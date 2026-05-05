---
title: "Quora answer about writing a search engine"
url: "https://boyter.org/2013/12/quora-answer-writing-search-engine/"
fetched_at: 2026-05-05T07:02:04.310808+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Quora answer about writing a search engine

Source: https://boyter.org/2013/12/quora-answer-writing-search-engine/

The following I posted on Quora in response to the question
“I am planning to make a small scale search engine on my local system, but I don’t know from where to start?”
. It’s a reasonable answer so like my
Mahalo
one I thought I would make a copy for myself.
I agree with Wolf Garbe and that you are better off in your case starting with existing technologies, have a look at
http://yacy.net/
and SphinxSearch as well. However if you are doing this to learn and not just deliver a product I can provide a few links for you.
For your specific questions,
How do I use hashing for efficient search operation ?
You are talking about having an inverted index I suspect. Have a look at the articles above which discuss the inverted index. Keep in mind you have options here. Such as inverted index or a full inverted index. The latter is useful if you want to do thinks like proximity searches and the like. For hashing itself,
Which hashing algorithm is best for uniqueness and speed?
Be careful when using hashes with URL’s. While the square root of the number
We Worship MD5, the GOD of HASH of URL’s is still a lot bigger then the current
web size if you do get a collision you are going to get pages about Britney Spears
when you were expecting pages about Bugzilla. Look into using bloom filters to avoid
these issues (assuming you get to sufficient scale).
How I will manage the data and ?
Up-to you. For small scale I would just use whatever database you are most familiar with. Any SQL database will scale up to hundreds of millions of records without too many issues.
How my searching algorithm would work ?
This is up-to you as well. You are the one in control here. Assuming you want to get something up and running as soon as possible I would do the following.
Write a simple crawler and start crawling. (for url; get url; find urls;) is about
all you need. For seeding use wikipedia’s data dump, the alexa top lists or dmoz
data.
Build a simple inverted index indexer and index as you go. Limit your index to small portions of text (title, meta tags etc..) for the moment till you get the kinks
ironed out. If your indexer is not using 100% of the CPU rethink your approach as it is wrong.
Build a simple ranker (just rank numbers of words in documents for the moment). DO NOT DO PAGE RANK! This step will save you a lot of time while getting everything else working.
Build it by default to be an OR engine (this saves you writing a query parser or
working out how to intersect two 10 million document lists quickly).
Be sure to use a stemmer from the following Stemming Algorithm. Implement a fairly large amount of stop words and ignore anything less then 3 characters in length.
The above should be enough to occupy you for several weeks at least.
Here is a link to a collection of articles on how to start building a search engine.
Want to write a search engine? Have some links
I have copied the article below, but the above link I tend to update from time to
time as I find new articles.
PHP Search Engine – Yioop!
This one is fairly fresh and talks about building and running a general purpose
search engine in PHP.
About Us – Gigablast
This has been defunct for a long time now but is written by Matt Wells (Gigablast and Procog) and gives a small amount of insight into the issues and problems he worked through while writing Gigablast.
Why Writing Your Own Search Engine Is Hard
This is probably the most famous of all search engine articles with the exception of the original Google paper. Written by Anna Patterson (Cuil) it really explores the basics of how to get a search engine up and running from crawler to indexer to
serving results.
A Conversation with Matt Wells
A fairly interesting interview with Matt Wells (Gigablast and Procog) which goes into some details of problems you will encounter running your own search engine.
Building a Search Engine
This has a few articles written about creating a search engine from scratch. It
appears to have been on hold for years but some of the content is worth reading. If nothing else its another view of someone starting down the search engine route.
blekko | spam free search
Blekko’s engineering blog is usually interesting and covers all sorts of
material applicable to search engines.
http://www.boyter.org/201
3/01/co…
This is a shameless plug but I will even suggest my own small implementation. Its essentially a walk though a write of a search engine in PHP. I implemented it and it worked quite well with 1 million pages serving up reasonable results. It actually covers everything you want, Crawling, Indexing, Storing, Ranking with articles explaining why I did certain things and full source code here Phindex
The Anatomy of a Search Engine
The granddaddy of search papers. Its very old but outlines how the original version of Google was designed and written.
open-source-search-engine
Gigablast mentioned above has since become an Open source project hosted on Github. Personally I am still yet to look through the source code but you can find how to run it on the developer page and administration page.
High Scalability – High Scalability – DuckDuckGo Architecture – 1 Million Deep Searches a Day and Growing
High Scalability – High Scalability – The Anatomy of Search Technology: blekko’s NoSQL database
High Scalability – High Scalability – Challenges from large scale computing at Google
High Scalability – High Scalability – Google’s Colossus Makes Search Real-time by Dumping MapReduce
High Scalability – High Scalability – The Three Ages of Google – Batch, Warehouse, Instant
The above are fairly interesting. The blekko one is the most technical. If you only have time to read one go with the blekko one.
Another thing you might want to consider is looking through the source of existing
indexing engines like Solr and Sphinx. I am personally running through the initial
version of the Sphinx engine and will one day write a blog about how it works.
Here are a few other links (disclaimer I wrote all of those) showing how to implement the vector space model (a good thing to start with as it does ranking for you)
Vector Space Search Model Explained
Building a Vector Space Indexing Engine in Python
GoLang Vector Space Implementation
C# Vector Space Implementation
and here is a much better article which explains the math behind it,
Page on La2600
For snippet extraction I have another article here,
Building a Search Result Extract Generator in PHP
For crawling here is another one,
Why Writing a Web Crawler isn’t Easy
Lastly if you do go about and write your own search engine please write blog posts or articles about it. Its quite hard to find this sort of information, especially from the big boys (Google, Bing, Yandex, Yahoo) and I would love to see more articles about it.
