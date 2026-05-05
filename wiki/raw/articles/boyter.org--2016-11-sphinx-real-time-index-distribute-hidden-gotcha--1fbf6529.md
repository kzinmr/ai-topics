---
title: "Sphinx Real Time Index How to Distribute and Hidden Gotcha"
url: "https://boyter.org/2016/11/sphinx-real-time-index-distribute-hidden-gotcha/"
fetched_at: 2026-05-05T07:02:00.414682+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Sphinx Real Time Index How to Distribute and Hidden Gotcha

Source: https://boyter.org/2016/11/sphinx-real-time-index-distribute-hidden-gotcha/

I have been working on real time indexes with Sphinx recently for the next version of searchcode.com and ran into a few things that were either difficult to search for or just not covered anywhere.
The first is how to implement a distributed search using real time indexes. It’s actually done the same way you would normally create an index. Say you had a single server with 4 index shards on it and you wanted to run queries against it. You could use the following,
index rt
{
    type = distributed
    local = rt1
    agent = localhost:9312:rt2
    agent = localhost:9312:rt3
    agent = localhost:9312:rt4
}
You would need to have each one of your indexes defined (only one is added here to keep the example short)
index rt1
{
    type = rt1
    path = /usr/local/sphinx/data/rt1
    rt_field = title
    rt_field = content
    rt_attr_uint = gid
}
Using the above you would be able to search across all of the shards. The trick is knowing that to update you need to update each shard yourself. You cannot pass documents to the distributed index but instead must make a separate update to each shard. Usually I split sphinx shards based on a query like the following,
SELECT cast((select id from table order by 1 desc limit 1)/4 as UNSIGNED)*2, \
         cast((select id from table order by 1 desc limit 1)/4 as UNSIGNED)*3 \
         FROM table limit 1
Where the 4 is the number of shards and the multiplier splits the shards out. It’s performant due to index use. However for RT I suggest a simple modulas operator % against the ID column for each shard as it allows you to continue to scale out to each shard equally.
The second issue I ran into was that when defining the attributes and fields you must define all the fields before the uints. The above examples work fine but the below is incorrect. I couldn’t find this mentioned in the documentation.
index rt
{
    type = rt
    path = /usr/local/sphinx/data/rt
    rt_attr_uint = gid # this should be below the rt_fields
    rt_field = title
    rt_field = content
}
