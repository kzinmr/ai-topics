---
title: "Cloud Network Traffic Within the Same Region Can Be Very Expensive"
url: "https://databasearchitects.blogspot.com/2022/04/cloud-network-traffic-within-same.html"
fetched_at: 2026-05-05T07:01:28.639968+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Cloud Network Traffic Within the Same Region Can Be Very Expensive

Source: https://databasearchitects.blogspot.com/2022/04/cloud-network-traffic-within-same.html

Everyone knows that the major cloud vendors try to make it easy to get data in, and hard to get it out. What is less known is that high egress cost also applies to outbound traffic within the same region.
Let's look at AWS specifically. In AWS, EC2 outbound traffic is only free within the same availability zone (AZ). Moving data from one AZ to another in the same region is actually quite expensive:
"
IPv4: Data transferred “in“ to and “out“ from Amazon EC2 [...] across Availability Zones in the same AWS Region is charged at $0.01/GB in each direction."
source
This means that transferring 1TB costs $0.01/GB * 1000GB * 2 = $20. For comparison: most inter-region transfers cost $0.02 per GB, but only for outgoing traffic. Thus, remarkably, transferring 1TB from Ohio to Tokyo will cost the same as transferring it within Ohio from
us-east-2a
to
us-east-2b
. Two
c5n.18xlarge
instances communicating with each other at full 100 Gbit speed can theoretically incur network costs of $1,800 per hour (or $1,296,000 per month).
Interestingly, S3 can be used to bypass the high traffic cost when moving data between different AZs in the same region because
"Data transferred directly between Amazon S3 [...] in the same AWS Region is free."
source
Let's see if we can exploit this. Consider again our example where we want to transfer 1TB from
us-east-2a
to
us-east-2b
. Instead of two EC2 instances talking directly, we could use an S3 Standard bucket in
us-east-2
. We first PUT the data into it from
us-east-2a
, then GET the data from that bucket using
us-east-2b
instances, and finally delete all objects. If we split our data into 1,000 1GB chunks, we need to pay for only 1,000 PUT and 1,000 GET S3 requests, which would be less than $0.01. Storage cost is also low: assuming a transfer rate of 1GB/s, the data would have to be stored in S3 for less than an hour, which costs about $0.03 (and could be reduced via pipelining). Thus, in total we can transfer 1TB through S3 for less than $0.05 instead of $20.
To summarize, inter-AZ traffic cost within the same region is unreasonably expensive. It seems unlikely that these prices have any resemblance to internal AWS cost -- as is reflected by the fact that AWS services such as S3 allow bypassing this cost.
