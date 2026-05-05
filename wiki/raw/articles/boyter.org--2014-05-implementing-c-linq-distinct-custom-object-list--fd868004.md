---
title: "Implementing C# Linq Distinct on Custom Object List"
url: "https://boyter.org/2014/05/implementing-c-linq-distinct-custom-object-list/"
fetched_at: 2026-05-05T07:02:03.510604+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Implementing C# Linq Distinct on Custom Object List

Source: https://boyter.org/2014/05/implementing-c-linq-distinct-custom-object-list/

Implementing C# Linq Distinct on Custom Object List
2014/05/07
(145 words)
Ever wanted to implement a distinct over a custom object list in C# before? You quickly discover that it fails to work. Sadly there is a lack of decent documentation about this and a lot of FUD. Since I lost a bit of time hopefully this blog post can be picked up as the answer.
Thankfully its not as difficult as you would image. Assuming you have a simple custom object which contains an Id, and you want to use that Id to get a distinct list all you need to do is add the following to the object.
public
override bool
Equals
(object obj)
{
return
this
.
Id
==
((CustomObject)obj).
Id
;
}
public
override
int
GetHashCode
()
{
return
this
.
Id
.
GetHashCode
();
}
You need both due to the way that Linq works. I suspect under the hood its using a hash to work out whats the same hence GetHashCode.
