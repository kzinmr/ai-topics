---
title: "Taxis and hash functions"
url: "https://www.johndcook.com/blog/2026/11/16/taxis-and-hash-functions/"
fetched_at: 2026-11-17T10:00:44.400086+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Taxis and hash functions

Source: https://www.johndcook.com/blog/2026/11/16/taxis-and-hash-functions/

In 2014 New York City released dump of trip and fare logs from NYC taxis in the previous year. In an attempt to protect privacy, the taxi license numbers and medallion numbers were hashed using the MD5 hash function.
If you’re familiar with secure has functions, your first reaction might be that the problem with the scenario above is that NYC used a hash function that had been shown to be broken a decade earlier. But that was not the problem.
MD5 was considered broken in 2004 because someone showed how to create a hash collision, not because one can calculate a preimage. It’s easy to create two messages that have the same MD5 hash value. However, if you have a message
m
with hash MD5(
m
) =
h
, it is still not practical to infer
m
from
h
in general. However, if you know that your message
m
comes from a fairly small set, such as the set of all NYC taxi license numbers, you can hash them all and see which one hashes to
h
. This would be true for a more secure hash function like SHA-256 just as much as for MD5.
The root of the problem was that the hash function was known. If the city had used a keyed hash, this would have prevented anyone from simply hashing all the license and medallion numbers. If they had chosen a random number and concatenated it to each value before hashing, this would have prevented an attacker from creating a lookup table, even using MD5. There may have been other privacy problems with the data, but this particular line of attack would have been blocked.
Related posts
