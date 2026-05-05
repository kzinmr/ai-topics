---
title: "Simple Go Cache | Ben E. C. Boyter"
url: "https://boyter.org/posts/simple-go-cache/"
fetched_at: 2026-05-05T07:01:54.641027+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Simple Go Cache | Ben E. C. Boyter

Source: https://boyter.org/posts/simple-go-cache/

Happy new year!
I am in the middle of converting searchcode.com over to SQLite, which is a far more interesting future post, and as a result had to rewrite some of the core service logic. The previously implemented code had grown over time so I decided to start fresh. Of course the catch of this is introducing regressions, which I did by stripping out some of the caching logic I had implemented.
I have wanted to make a generic cache for Go for a while as none of the existing ones I had found fit my requirements, which are as follows,
Have the ability to set a hard limit on the max items, but also allow “infinite” growth
Have the ability to age out items over time
Have the ability to keep items forever unless the max cap is found
Configurable expiration algorithm LRU/LFU and others over time
Support concrete types (In other words use Go generics)
Configurable random eviction policy, to trade off time for accuracy and vice versa
Specific to one concrete type per cache
With the above in mind what I really wanted was Go map, with the expiration. I am fully aware that multiple excellent cache solutions for Go exist, with searchcode using github.com/coocood/freecache as a generic cache but for specific items I more or less wanted some functions over a fancy map.
The result I cleaned up and have released
https://github.com/boyter/simplecache
Usage is fairly simple. Create a new cache after importing github/boyter/simplecache similar to the below and set the type you want to cache, which in this case is a string. Then get/set/delete as normal.
sc
:=
simplecache
.
New
[
string
]()
v
,
ok
:=
sc
.
Get
(
"key-1"
)
if
ok
{
fmt
.
Println
(
v
)
// prints "some value"
}
v
,
ok
=
sc
.
Get
(
"key-99"
)
if
ok
{
fmt
.
Println
(
v
)
// not run "key-99" was never added
}
sc
.
Delete
(
"key-1"
)
// removes the item
sc
.
Clear
()
// clear the whole cache
You can also configure the cache to meet your own requirements. The default values as of now are 100,000 items, no age expiration, LFU as the expiration algorithm, with 5 samples taken.
All of which are configurable. For example, lets assume you want to limit to 1,000 items.
mI
:=
1_000
sc
:=
simplecache
.
New
[
string
](
simplecache
.
Option
{
MaxItems
:
&
mI
,
})
How about 1,000 items and a max age of 10 minutes,
mI
:=
1_000
oMA
:=
time
.
Minute
*
10
sc
:=
simplecache
.
New
[
string
](
simplecache
.
Option
{
MaxItems
:
&
mI
,
MaxAge
:
&
oMA
,
})
Lastly how about setting all the possible options.
oMi
:=
1000
oEp
:=
simplecache
.
LRU
oEs
:=
5
oMA
:=
time
.
Second
*
60
sc
:=
simplecache
.
New
[
string
](
simplecache
.
Option
{
MaxItems
:
&
oMi
,
// max number of items the cache will hold, evicting on Set, nil for no limit
EvictionPolicy
:
&
oEp
,
// Which eviction policy should be applied LRU or LFU
EvictionSamples
:
&
oEs
,
// How many random samples to take from the items to find the best to expire
MaxAge
:
&
oMA
,
// Max age an item can live on Get when past this will be deleted, nil for no expiry
})
So I yeeted it into searchcode.com’s beta and running the normal tests the profile shows all is well again. Happy days and I can get back to working on the SQLite migration.
