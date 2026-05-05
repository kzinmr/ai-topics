---
title: "Sphinx and searchcode"
url: "https://boyter.org/2014/06/sphinx-searchcode/"
fetched_at: 2026-05-05T07:02:03.230195+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Sphinx and searchcode

Source: https://boyter.org/2014/06/sphinx-searchcode/

There is a rather nice blog post on the Sphinx Search blog about how searchcode uses sphinx. Since I wrote it I thought I would include a slight edited for clarity version below. You can read the
original here
.
I make it no secret that the indexer that powers
searchcode
is
Sphinx Search
which for those who do not know is a stand alone indexing and searching engine similar to Solr.
Since
searchcode’s
inception in 2010, Sphinx has powered the search functionality and provides the raw searching and faceting functionality across 19 billion lines of source code. Each document has over 6 facets and there are over 40 million documents in the index at any time. Sphinx serves over 500,000 queries a month from this with the average query returning in less than a second.
searchcode
is an unusual beast in that while it doesn’t index as many documents as other large installations, it indexes a lot more data. This is due to the average document size being larger and the way source code is delimited. The result of these requirements is that the index when built is approximately 3 to 4 times larger than the data being indexed. The special transformation’s required are accomplished with a thin wrapper on top of Sphinx which modifies the text processing pipeline. This is applied when Sphinx is indexing and running queries. The resulting index is over 800 gigabytes in size on disk and when preloaded consumes over 25 gigabytes of RAM.
This is all served by a single i7 Quad Core server with 32 gigabytes of RAM. The index is distributed and split into 4 parts allowing all queries to run over network agents and scale out seamlessly. Because of the size of the index and how long this takes each part is only indexed every week and a small delta index is used to provide recent updates.
Every query run on
searchcode
runs multiple times as a method of improving results and avoiding cache rot. The first query run uses the sphinx ranking mode BM25 and and subsequent queries use SPH04. BM25 uses a little less CPU then SPH04 and hence new queries use it as return time to the user is important. All subsequent queries run as a offline asynchronous task which does some further processing and updates the cache so the next time the query is run the results are more accurate. Commonly ran queries are added the the asynchronous queue after the indexes have been rotated to provide fresh search results at all times.
searchcode
is currently very CPU bound and given the resources could improve search times 4x with very little effort simply by moving each of the the Sphinx indexes to individual machines.
searchcode
updates to the latest stable version of Sphinx for every release. This has happened for every version from 0.9.8 all the way to 2.1.8 which is currently being used. There has never been a single issue with each upgrade and each upgrade has overcome an issue that was previously encountered. This stability is one of the main reasons for having chosen Sphinx initially.
The only issues encountered with Sphinx to date where some limits on the number of facets which has been resolved with the latest versions. Any other issue has been due to configuration issues which were quickly resolved.
In short Sphinx is an awesome project. It has seamless backwards compatibility, scales up to massive loads and still returns results quickly and accurately. Having since worked with Solr and Xapian, I would still choose Sphinx as searchcode’s indexing solution. I consider Sphinx as Nginx of the indexing world. It may not have every feature possible but its extremely fast and capable and the features it does have work for 99% of solutions.
