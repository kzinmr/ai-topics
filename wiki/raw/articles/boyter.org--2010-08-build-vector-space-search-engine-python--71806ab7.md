---
title: "Building a Vector Space Indexing Engine in Python"
url: "https://boyter.org/2010/08/build-vector-space-search-engine-python/"
fetched_at: 2026-05-05T07:02:07.777220+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Building a Vector Space Indexing Engine in Python

Source: https://boyter.org/2010/08/build-vector-space-search-engine-python/

Ever wanted to code a search engine from scratch? Well actually its a pretty simple thing to do. Here is an example indexer I coded up in less then an hour using Python.
The first thing we need to do is have a way to take our documents we want to search on and turn them into an concordance. A concordance for those not in the know is a count of every word that occurs in a document.
def
concordance
(document):
if
type(document)
!=
str:
raise
ValueError
(
'Supplied Argument should be of type string'
)
con
=
{}
for
word
in
document
.
split(
' '
):
if
con
.
has_key(word):
con[word]
=
con[word]
+
1
else
:
con[word]
=
1
return
con
The above method simply allows us to pass in a clean text document and get back a concordance of the words in that document.
The only other thing we need is a vector space. A vector space for those not in the know is a way of calculating the distances between two points. Essentially it works the same way calculating the 3rd side of a triangle. Except that instead of 2 planes (x and y) or even 3 planes (x,y,z) you can have as many planes as you want. The actual idea takes a while to understand but you can read about it here,
Vector Space Search Engine Theory
(PDF).
Thankfully I already have implemented the algorithm in my
Decoding CAPTCHA’s
post and can just copy paste it from there. I have modified it a little bit to avoid divide by zero issues, check types and to add the above concordance method in since it really does belong together.
class
VectorCompare
:
def
magnitude
(self,concordance):
if
type(concordance)
!=
dict:
raise
ValueError
(
'Supplied Argument should be of type dict'
)
total
=
0
for
word,count
in
concordance
.
iteritems():
total
+=
count
**
2
return
math
.
sqrt(total)
def
relation
(self,concordance1, concordance2):
if
type(concordance1)
!=
dict:
raise
ValueError
(
'Supplied Argument 1 should be of type dict'
)
if
type(concordance2)
!=
dict:
raise
ValueError
(
'Supplied Argument 2 should be of type dict'
)
relevance
=
0
topvalue
=
0
for
word, count
in
concordance1
.
iteritems():
if
concordance2
.
has_key(word):
topvalue
+=
count
*
concordance2[word]
if
(self
.
magnitude(concordance1)
*
self
.
magnitude(concordance2))
!=
0
:
return
topvalue
/
(self
.
magnitude(concordance1)
*
self
.
magnitude(concordance2))
else
:
return
0
def
concordance
(self,document):
if
type(document)
!=
str:
raise
ValueError
(
'Supplied Argument should be of type string'
)
con
=
{}
for
word
in
document
.
split(
' '
):
if
con
.
has_key(word):
con[word]
=
con[word]
+
1
else
:
con[word]
=
1
return
con
To use it you just supply two concordances (one the document and the other the query) and it returns a number from 0 to 1 of how related they are. The higher the number the more relevant the search terms are to the document.
So now all we need do, is take every document, build a concordance for it, then compare each one to our search terms, sort the results by the number returned and we are set. The documents I decided to use are the titles and first paragraph of the last 7 blogs I have posted here.
v
=
VectorCompare()
documents
=
{
0
:
'''At Scale You Will Hit Every Performance Issue I used to think I knew a bit about performance scalability and how to keep things trucking when you hit large amounts of data Truth is I know diddly squat on the subject since the most I have ever done is read about how its done To understand how I came about realising this you need some background'''
,
1
:
'''Richard Stallman to visit Australia Im not usually one to promote events and the like unless I feel there is a genuine benefit to be had by attending but this is one stands out Richard M Stallman the guru of Free Software is coming Down Under to hold a talk You can read about him here Open Source Celebrity to visit Australia'''
,
2
:
'''MySQL Backups Done Easily One thing that comes up a lot on sites like Stackoverflow and the like is how to backup MySQL databases The first answer is usually use mysqldump This is all fine and good till you start to want to dump multiple databases You can do this all in one like using the all databases option however this makes restoring a single database an issue since you have to parse out the parts you want which can be a pain'''
,
3
:
'''Why You Shouldnt roll your own CAPTCHA At a TechEd I attended a few years ago I was watching a presentation about Security presented by Rocky Heckman read his blog its quite good In it he was talking about security algorithms The part that really stuck with me went like this'''
,
4
:
'''The Great Benefit of Test Driven Development Nobody Talks About The feeling of productivity because you are writing lots of code Think about that for a moment Ask any developer who wants to develop why they became a developer One of the first things that comes up is I enjoy writing code This is one of the things that I personally enjoy doing Writing code any code especially when its solving my current problem makes me feel productive It makes me feel like Im getting somewhere Its empowering'''
,
5
:
'''Setting up GIT to use a Subversion SVN style workflow Moving from Subversion SVN to GIT can be a little confusing at first I think the biggest thing I noticed was that GIT doesnt have a specific workflow you have to pick your own Personally I wanted to stick to my Subversion like work-flow with a central server which all my machines would pull and push too Since it took a while to set up I thought I would throw up a blog post on how to do it'''
,
6
:
'''Why CAPTCHA Never Use Numbers 0 1 5 7 Interestingly this sort of question pops up a lot in my referring search term stats Why CAPTCHAs never use the numbers 0 1 5 7 Its a relativity simple question with a reasonably simple answer Its because each of the above numbers are easy to confuse with a letter See the below'''
,
}
index
=
{
0
:v
.
concordance(documents[
0
]
.
lower()),
1
:v
.
concordance(documents[
1
]
.
lower()),
2
:v
.
concordance(documents[
2
]
.
lower()),
3
:v
.
concordance(documents[
3
]
.
lower()),
4
:v
.
concordance(documents[
4
]
.
lower()),
5
:v
.
concordance(documents[
5
]
.
lower()),
6
:v
.
concordance(documents[
6
]
.
lower()),
}
searchterm
=
raw_input(
'Enter Search Term: '
)
matches
=
[]
for
i
in
range(len(index)):
relation
=
v
.
relation(v
.
concordance(searchterm
.
lower()),index[i])
if
relation
!=
0
:
matches
.
append((relation,documents[i][:
100
]))
matches
.
sort(reverse
=
True
)
for
i
in
matches:
print i[
0
],i[
1
]
Now running it and trying some searches.
Enter Search Term: captcha
0.124034734589 Why You Shouldnt roll your own CAPTCHA At a TechEd I attended a few years ago I was watching a prese
0.0957826285221 Why CAPTCHA Never Use Numbers
0
1
5
7
Interestingly this sort of question pops up a lot in my referr
Enter Search Term: mysql stallman
0.140028008403 Richard Stallman to visit Australia Im not usually one to promote events and the like unless I feel
0.110096376513 MySQL Backups Done Easily One thing that comes up a lot on siteslike Stackoverflow and the like is
Results are not too bad I think! Now there are some problems with this technique. Firstly it doesn’t support boolean searches which can be an issue, although most people tend to just type some terms. Secondly it has problems with larger documents. The way the vector space works is biased towards smaller documents since they are closer to the search term space. You can get around this by breaking larger documents up into smaller ones though. The final and biggest issue though is that it is pretty CPU intensive. I have tested a search like this with 50,000 documents and it was OK but you wouldn’t want to go much further then that. It is a pretty naive implementation though. With some caching and checking which documents are worth comparing you could take this up to millions of documents.
I remember reading somewhere (no source sorry) that Altavista and some of the other early search engines used a technique similar to the above for calculating rankings, so it seems the idea really can be taken to a large scale.
By now I am sure someone is thinking, “Hang on, if its that simple then why is it so hard to make the next Google?”. Well the answer is that its pretty easy to index 10,000 to 100,000,000 pages it gets considerably more difficult to index 1,000,000,000+ pages. You have to shard out to multiple computers and the margin for error is pretty low. You can read this post
Why Writing a Search Engine is Hard written by Anna Patterson
(one of the co-founders of
Cuil
) which explains the problem nicely.
A few people have expressed difficulty getting the above to run. To do so just copy it all into a single file and run it.
