---
title: "Another day another interview…"
url: "https://boyter.org/2014/04/day-interview/"
fetched_at: 2026-05-05T07:02:03.588759+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Another day another interview…

Source: https://boyter.org/2014/04/day-interview/

Another day another interview. I actually have been getting some good results from them so far. In particular the last two I have been on. I will discuss them briefly.
The first had an interesting coding test. Rather then asking me to solve Fizzbuzz or implement a depth first algorithm over a binary tree (seriously, I have been programming for 10 years and never needed to do that. I can, but its something I did in uni and not really applicable to anything I have done since then). It was to implement a simple REST service.
You created your service, hosted it online (heroku was suggested as its free) passed in the URL to a form, submitted and it hit your service looking for error codes and correct responses/output to input. Since you got to implement it in any language you want I went with Python/Django and produced the following code.
def
parse_json
(self, data):
filtered
=
self
.
filter_drm(data[
'payload'
])
filtered
=
self
.
filter_episode_count(filtered)
return
self
.
format_return(filtered)
def
filter_drm
(self, data):
if
data
is
None
or
data
==
[]:
return
[]
result
=
[x
for
x
in
data
if
'drm'
in
x
and
x[
'drm'
]
==
True
]
return
result
def
filter_episode_count
(self, data, count
=
0
):
if
data
is
None
or
data
==
[]:
return
[]
result
=
[x
for
x
in
data
if
'episodeCount'
in
x
and
x[
'episodeCount'
]
&
gt; count]
return
result
def
format_return
(self, data):
if
data
is
None
or
data
==
[]:
return
{
"response"
: []}
result
=
[{
"image"
: x[
'image'
][
'showImage'
],
"slug"
: x[
'slug'
],
"title"
: x[
'title'
]}
for
x
in
data
if
'image'
in
x
and
'slug'
in
x
and
'title'
in
x]
return
{
"response"
: result}
Essentially its the code from the model I created. It takes in some JSON data, filters it by the field DRM and Episode count, then returns a subset of the data in it. The corresponding view is very simple, with just some JSON parsing (with error checks) and then calling the above code. I did throw in quite a few unit tests though to ensure it was all working correctly.
Thankfully, after writing the logic, some basic testing (curl to fake a response) it all looked OK to me. I uploaded on heroku (never used it before and it took most of the time) and submitted the form. First go everything worked correctly passing all of the requirements listed which made me rather happy.
As for the second interview, it raised a good question which highlights the fact while I know how to write a closure and lambda I cannot actually say what they are. It also highlighted I really need to get better at Javascript since while I am pretty comfortable with it on the front end for backend processes such as node.js I am an absolute notice.
For the first, I was right about a lambda, which is just an anonymous function. As for the second part a closure is a function which closes over the environment allowing it to access variables not in its function list. An example would be,
def
function1
(h):
def
function2
():
return
h
return
function2()
In the above function2 closes over function1 allowing it to access the the variables in function1’s environment such as h.
The other thing that threw me was implementing a SQL like join in a nice way. See the thing is I have been spoilt by C# which makes this very simple using LINQ. You literally join the two lists in the same way SQL would and it just works. Not only that the implementation is really easy to read.
I came up with the following which is ugly for two reasons,
its not very functional
it has very bad  O(N^2) runtime performance.
var
csv1
=
[
{
'name'
:
'one'
},
{
'name'
:
'two'
}
];
var
csv2
=
[
{
'name'
:
'one'
,
'address'
:
'123 test street'
},
{
'name'
:
'one'
,
'address'
:
'456 other road'
},
{
'name'
:
'two'
,
'address'
:
'987 fake street'
},
];
function
joinem
(
csv1
,
csv2
) {
var
ret
=
[];
$
.
each
(
csv1
,
function
(
index
,
value
) {
$
.
each
(
csv2
,
function
(
index2
,
value2
) {
if
(
value
.
name
==
value2
.
name
) {
ret
.
push
(
value2
);
}
});
});
return
ret
;
}
var
res1
=
joinem
(
csv1
,
csv2
);
Assuming I get some more time later I want to come back to this. I am certain there is a nice way to do this in Javascript using underscore.js or something similar which is just as expressive as the LINQ version.
