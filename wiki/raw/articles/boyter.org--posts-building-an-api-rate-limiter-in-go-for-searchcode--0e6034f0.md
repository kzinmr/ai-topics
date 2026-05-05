---
title: "Building a API rate limiter in Go for searchcode"
url: "https://boyter.org/posts/building-an-api-rate-limiter-in-go-for-searchcode/"
fetched_at: 2026-05-05T07:01:57.843482+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Building a API rate limiter in Go for searchcode

Source: https://boyter.org/posts/building-an-api-rate-limiter-in-go-for-searchcode/

So regular readers of this site might know that I run
https://searchcode.com
which I recently converted over to Go. While I had always run searchcode cheaply I never wanted to implement rate limits and instead operate as Bill and Ted by being “Excellent to each other”. Sadly the internet is not from the Bill and Ted universe and due to some level of abuse against the API I have been forced to implement a rate limiter.
Specifically there was some joker who was smashing the API with 100’s of requests a second (by themselves) which was not a huge issue in terms of load on the system generally but felt unfair. Some other IP’s appeared to be hitting it hard, but generally it was just this one individual who I wanted to restrict. Note I said restrict and not ban. I don’t ever want to have to ban as that just turns into an arms race which I will loose because in the race between arms and armor, arms always wins.
While I could have just restricted that single IP (or blocked them) I decided to put the effort in and create a general purpose rate limiter. One that solves the immediate problem but should also help with future ones.
Generally a simple rate limiter is a fairly easy thing to implement, especially if you do it by IP address. There are techniques that you can use to mitigate distributed abuses against search API’s but the simplest thing is a simple IP limit. The easiest way to do this in Go is by using a wrapper which is a
http.HandlerFunc
with an expiring map.
func
GetIP
(
r
*
http
.
Request
)
string
{
forwarded
:=
r
.
Header
.
Get
(
"X-FORWARDED-FOR"
)
if
forwarded
!=
""
{
return
forwarded
}
return
r
.
RemoteAddr
}
var
_ipMap
=
map
[
string
]
int64
{}
// used for checking IP spamming
var_ipMapMutex
sync
.
Mutex
func
IpRestrictorHandler
(
next
http
.
HandlerFunc
)
http
.
HandlerFunc
{
return
func
(
w
http
.
ResponseWriter
,
r
*
http
.
Request
) {
ip
:=
GetIP
(
r
)
_ipMapMutex
.
Lock
()
result
,
ok
:=
_ipMap
[
ip
]
if
ok
{
// continue to ban up-to a certain level beyond which they just have to wait a long time before the limit goes back down
if
result
<
RATE_BAN_LIMIT
{
result
++
_ipMap
[
ip
] =
result
}
_ipMapMutex
.
Unlock
()
if
result
>=
RATE_LIMIT
{
w
.
WriteHeader
(
http
.
StatusTooManyRequests
)
w
.
Header
().
Set
(
"Content-Type"
,
jsonContentType
)
_
,
_
=
fmt
.
Fprint
(
w
,
"{}"
)
return
}
}
else
{
_ipMap
[
ip
] =
1
_ipMapMutex
.
Unlock
()
}
next
.
ServeHTTP
(
w
,
r
)
}
}
// SNIP to router implementation using github.com/gorilla/mux
router
.
Handle
(
"/api/"
,
IpRestrictorHandler
(
app
.
ApiCodeView
)).
Methods
(
"GET"
,
"OPTIONS"
)
The above is close to the wrapper that searchcode.com actually uses. It gets the users IP address then checks if it exists in a map. If it does not it adds the IP to the map with an initial count of 1. If the IP already exists it increments the count up to to a certain limit held by RATE_BAN_LIMIT. If the count is over the ban threshold of RATE_LIMIT then the user is returned a HTTP 429 Too Many Requests response with an empty JSON value.
Note that the above is designed to punish checks against the API to see if the IP is still restricted as the increment always happens up to a controllable limit. You can make the filter less punitive by not incrementing once the IP is getting 429 responses, but the idea is to encourage exponential back-off against the system. That is if you ever get 429 you should back off for longer and longer periods till you are able to run again.
You can increase the RATE_BAN_LIMIT as required to provide longer lockouts of those that abuse the system.
The only thing left to do is to reduce the counts every now and then. That is reduce the API counts so that the limits reduce. To do so I create a simple go-routine that runs constantly in the background decrementing the count and then sleeping.
go
func
() {
for
{
time
.
Sleep
(
common
.
RATE_LIMIT_WINDOW_SECONDS
*
time
.
Second
)
// space out runs to avoid spinning all the time
keys
:=
[]
string
{}
// Get all of the keys
_ipMapMutex
.
Lock
()
for
k
:=
range_ipMap
{
keys
= append(
keys
,
k
)
}
_ipMapMutex
.
Unlock
()
for
_
,
k
:=
range
keys
{
_ipMapMutex
.
Lock
()
v
,
ok
:=
_ipMap
[
k
]
if
ok
{
v
=
v
-
common
.
RATE_LIMIT_DECREMENT
if
v
<=
0
{
delete(
_ipMap
,
k
)
}
else
{
_ipMap
[
k
] =
v
}
}
_ipMapMutex
.
Unlock
()
}
}
}()
The above sleeps for a fixed period of time set by RATE_LIMIT_WINDOW_SECONDS. In the case of searchcode.com it’s 60 seconds. It pulls all of the keys out of the map, then loops through each key. It decrements the count of each one by a configurable amount RATE_LIMIT_DECREMENT. If the value ever is less than 0 removes that entry from the map.
I actually have RATE_LIMIT_DECREMENT set to a lower value than RATE_LIMIT for searchcode. This gives a slight “soft limit” where you can use more than your budget at for a small period of time.
The reason for all the bizarre locking is to avoid locking the map as much as possible since contention to the map actually slows down HTTP requests to searchcode as everything runs through the wrapper code. I am not super happy with this implementation, but since it runs in under 1ms every 60 seconds it’s not worth investigating for any improvements yet as the time taken per time budget is so minimal.
So the above is about as simple as it gets. To deal with say multiple searches of the same term against the API from distributed IP’s you could replace the IP map with search term map, and assuming someone is spamming the same search term over and over it should help control that. Thankfully I have not needed to implement this yet.
The results?
Well the below is a dump of the map in memory a few seconds after a fresh deployment (which resets the map removing the restrictions, but thats not a huge issue in practice). The obscured portion is IP address. The annoying thing about the whole system is that now I need to IP address which frankly I never wanted to store (solves some privacy issues) but whatever. You can clearly see the first one is that individual I mentioned who apparently has still not gotten the message to please stop the hammering.
"ipCount": {
    "x.x.x.x": 1706,
    "x.x.x.x": 1,
    "x.x.x.x": 19,
    "x.x.x.x": 1,
    "x.x.x.x": 1,
    "x.x.x.x": 1,
    "x.x.x.x": 1,
    "x.x.x.x": 2,
    "x.x.x.x": 1,
    "x.x.x.x": 3,
    "x.x.x.x": 1,
    "x.x.x.x": 5
}
I do keep an eye on the above while its running to ensure the map never fills up and thankfully the most entries I have ever seen was a few hundred at times and generally its cleared out except for a single IP address every time the decrement works. Probably not the most memory efficient thing around but does not appear to have triggered any additional GC pauses. In addition the load average on the search servers has gone down very slightly.
So is this a perfect implementation? No. However it works well enough and there is scope to improve it at a later date if required. Assuming I need to expand on the code I will but in this case it achieved my simple goal of restricting a certain abuse of the system. Some ideas I have to improve it would be moving the map into redis to ensure it persists between API deployments, but this comes at the cost of latency and/or complexity if I keep the check in a in process map and sync it across. Of course redis already supports rate limiting patterns itself if you need it
https://redislabs.com/redis-best-practices/basic-rate-limiting/
There is also the option to use an existing library such as tollbooth for this
https://github.com/didip/tollbooth
however generally I would rather not pull in another dependency when a reasonable implementation is only 30 or so lines of code.
By the way, if you were planning on using searchcode’s API and now are getting throttled, get in contact with me. We can hammer out a commercial agreement and I can ensure you get your own special rate limit applied.
