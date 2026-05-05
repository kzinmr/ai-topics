---
title: "How Elasticsearch Stores Documents"
url: "https://boyter.org/posts/how-elastic-search-stores-documents/"
fetched_at: 2026-05-05T07:01:58.106314+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# How Elasticsearch Stores Documents

Source: https://boyter.org/posts/how-elastic-search-stores-documents/

Developer? Need to know how to use Elasticsearch? Want to know how to get working with it quickly? This is the book for you!
Buy now using Leanpub
It is useful to understand is how elasticsearch stores documents. Documents that are indexed need to go into an index and have a type. Indexes can contain one or more types. This may sound limiting but you can search over all indexes or all types within an index or just one type within an index if you require.
Consider it logically like the below. You can search at any part of the tree which will search across all children, or pull back a specific document if you know the key.
ElasticSearch
├── Index1
│   ├── Type1
│   │   └── Document1
│   ├── Type2
│   │   └── Document2
│   │   └── Document3
│   │   └── Document4
│   ├── Type3
│   │   └── Document5
├── Index2
│   ├── Type1
│   │   └── Document6
│   ├── Type4
│   │   └── Document7
The confusing thing however is that documents stored in elasticsearch don’t actually need to have the same structure. You can index both of the documents,
{
"title"
:
"The Matrix"
,
"year"
:
1999
}
and
{
"fact"
:
"Originally intended on becoming an Olympic hockey player for Canada."
,
"type"
:
"Actor"
,
"person"
: {
"name"
:
"Keanu Reeves"
,
"DOB"
:
"1964-09-02"
,
"Citizenship"
:
"Canadian"
}
}
Into the same index of the same type and everything will work. However it will be problematic as a consumer as you will need to guess what type the documents coming out of elasticsearch are. It will be especially annoying when it comes to adding facets and other fancy queries on top of your search.
Rule of thumb. Use an index per project and type per each unique thing you want to search against.
For the purposes of your project, you probably want a single index and then one or multiple types. Have your index named something like what your project is called. As for the types for each “thing” you want to search across E.G.
ticket
,
document
,
metadata record
and define a type for each one.
To store a document in elasticsearch under an index and type you POST to the endpoint with the JSON you want to create.
For the above you could POST our Keanu document to the index
film
and the type
actor
to the endpoint
http://localhost:9200/film/actor
with the type as
application/json
. The result of this should be similar to the below,
{
"_index"
:
"film"
,
"_type"
:
"actor"
,
"_id"
:
"xeB3nGcB5wabZ-h5JSJW"
,
"_version"
:
1
,
"result"
:
"created"
,
"_shards"
: {
"total"
:
2
,
"successful"
:
1
,
"failed"
:
0
},
"_seq_no"
:
0
,
"_primary_term"
:
1
}
The above indicates that the document was added to the index film with the type actor and that elasticsearch has generated the unique ID for this document as being
xeB3nGcB5wabZ-h5JSJW
.
Don’t use elasticsearch as a primary data store. Use another document store for persistence and populate elasticsearch using it. Having a fast rebuild process is a good idea and using a highly durable data-store for your data such as S3 is an excellent backup solution.
It is worth-while writing a robust way of populating elasticsearch from your documents before doing anything else. This allows you to delete and rebuild the index at will allowing for rapid iteration. It also ensures that you have a way to rebuild everything should your elasticsearch cluster die or have issues. For a smallish cluster of 6 nodes with 4 CPU’s each you should be able to index over 1 million documents in under an hour.
If you want to use a custom id and not an elasticsearch generated one post to
http://localhost:9200/film/actor/id
where id is the id you want to use. Keep in mind that if that id already exists you will replace the existing document with your new one
