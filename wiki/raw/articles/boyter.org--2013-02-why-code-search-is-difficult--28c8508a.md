---
title: "Why Code Search is Difficult"
url: "https://boyter.org/2013/02/why-code-search-is-difficult/"
fetched_at: 2026-05-05T07:02:04.993423+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Why Code Search is Difficult

Source: https://boyter.org/2013/02/why-code-search-is-difficult/

I was chatting with a colleague the other day and he was asking me why code search is a difficult problem. After all its not quite as dynamic as the web so it should be easier to index.
In truth its a mixed bag. Some things like like crawling are easy, others such as indexing are much harder then you would think. I thought I would write down why this is.
Thankfully crawling is one of the things that you really don’t have to put any work into. Once you have a list of sources (repo locations) you can use source control download for you. Just clone/checkout the code to disk and you are done. The only exception to this is getting the list of projects, you can crawl website (not advisable) but emailing the website owners usually gives you a hook into their data. The best thing about crawling this way is that refreshing your data is easy, just update your source or checkout/clone it again.
Indexing is where things get difficult. The first problem is knowing how to split terms. Most index engines are designed to work with words, and when it comes to words its fairly easy to determine what is considered at term by looking at spaces. In code this is far more difficult. This is best illustrated with an example. Take the following search term,
i++
and then consider the following code snippets which should all match,
for(i=0; i++; i&lt;100) {
for(i=0;i++;i&lt;100) {
spliti++;
How do you split them into terms? By spaces results in the following,
for(i=0;
i++;
i&lt;100)
{
for(i=0;i++;i&lt;100)
{
spliti++;
Using a naive split via spaces you will notice that none of the above actually match. Hence a search for i++ on the above will result in no matches. There are a few ways to get around this but suffice to say its not as straight forward as just applying Lucene/Sphinx/Solr over the data.
Compare the above search on the 3 large code search engines
searchcode
,
github
and
ohloh
.
Other issues to consider is that most indexers will not index special characters such as !@#$%^&*()_+[]>< These are desirable searches when looking for source code. Once you realise someone might want to search for
List
you realise just how difficult splitting the text and indexing characters can be.
One other issue that comes to mind is that because of the above problems your index is going to be absolutely massive. searchcode’s index on disk is actually 3x the size of the data its searching over. This isn’t a huge problem (disk space is cheap) but means you hit scaling issues far sooner then you would indexing normal text.
None of the above are insurmountable problems, but certainly something to keep in mind if you think indexing is straight forward.
