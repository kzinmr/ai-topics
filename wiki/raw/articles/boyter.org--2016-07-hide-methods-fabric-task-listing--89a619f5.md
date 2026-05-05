---
title: "How to Hide Methods From Fabric Task Listing"
url: "https://boyter.org/2016/07/hide-methods-fabric-task-listing/"
fetched_at: 2026-05-05T07:02:01.023369+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# How to Hide Methods From Fabric Task Listing

Source: https://boyter.org/2016/07/hide-methods-fabric-task-listing/

How to Hide Methods From Fabric Task Listing
2016/07/21
(73 words)
Occasionally you may want to hide a method from appearing inside the fabric listing of available tasks. Usually its some sort of helper method you have created that is shared by multiple tasks. So how to hide it? Simply prefix with _
For example,
def
_apt_get
(packages):
'''Makes installing packages easier'''
sudo(
'apt-get update'
)
sudo(
'apt-get -y --force-yes install
%s
'
%
packages)
When listing the fabric tasks this method will no longer appear in the results.
