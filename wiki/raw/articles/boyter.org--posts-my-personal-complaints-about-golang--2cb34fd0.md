---
title: "My Personal Complaints about Programming in Go"
url: "https://boyter.org/posts/my-personal-complaints-about-golang/"
fetched_at: 2026-05-05T07:01:58.856124+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# My Personal Complaints about Programming in Go

Source: https://boyter.org/posts/my-personal-complaints-about-golang/

Go as a language is fairly decent. However because questions about why I have issues with tends to come up often enough on the company slack programming channel (see what I did there?) I figured I would write them down and put it here so I can point people at a link when they ask what my complaints are.
For the record I have been using Go heavily for the last year or so, writing command line applications,
scc
,
lc
and API’s. These include large scale API’s for clients to a
syntax highlighter
that will be used in
https://searchcode.com/
sometime soon.
My criticisms in this are aimed exclusively at Go. I do however have complaints about every language I use. In fact the below quote is extremely applicable.
“There are only two kinds of languages: the ones people complain about and the ones nobody uses.”. - Bjarne Stroustrup,
#1 The lack of functional programming
I am not a functional programming zealot. The first thing that comes to mind when I think of Lisp is a speech impediment.
This is probably my biggest pain point with Go. Going against the crowd I don’t want generics, which I think would just add unnecessary complexity to most Go projects. What I want is some functional methods applied over the in-built slice and map in Go. Both of those types are already magic in the sense that they can hold any type and are generic, which you cannot implement yourself in Go without using interface and then loosing all the safety and speed.
For example consider the below.
Given two slices of strings work out which ones exist in both and put it this into a new slice so we can process it later.
existsBoth
:=
[]
string
{}
for
_
,
first
:=
range
firstSlice
{
for
_
,
second
:=
range
secondSlice
{
if
first
==
second
{
existsBoth
= append(
existsBoth
,
proxy
)
break
}
}
}
The above is one trivial way to solve this in Go. There are other ways to solve the above by using maps, which would reduce the runtime, but lets assume we are slightly memory constrained, or that we don’t have very large slices to process and the additional runtime isn’t worth the complexity it would introduce. Lets compare it to the same logic in Java using streams and functional programming.
var
existsBoth
=
firstList.
stream
()
.
filter
(x
->
secondList.
contains
(x))
.
collect
(Collectors.
toList
());
Now the above does hide the algorithmic complexity of whats happening, but its far simpler to see what its actually doing.
The intent of the code is obvious compared to the Go code it is replicating. What is really neat about it is that adding additional filters is also trivial. To add additional filters to the Go example like the below example we would need to add two more if conditions into the already nested for loops.
var
existsBoth
=
firstList.
stream
()
.
filter
(x
->
secondList.
contains
(x))
.
filter
(x
->
x.
startsWith
(needle))
.
filter
(x
->
x.
length
()
>=
5)
.
collect
(Collectors.
toList
());
There are projects which using
go generate
can achieve some of the above for you, but without nice IDE support its clunky and more of a hassle over pulling out the loop above into its own method.
#2 Channels / Parallel Slice Processing
Go channels are generally pretty neat. While they have some issues where you can block forever, but they aren’t about providing fearless concurrency and with the race detector you can shake out these issues pretty easily. For streaming values where you don’t know how many there are or when the end is, or if your method to process the values is not CPU bound they are an excellent choice.
What they are not so good for is processing slices where you know the size up front and want to process them in parallel.
Multi-threaded programming, theory and practice
Its pretty common in pretty much every other language that when you have a large list or slice you use parallel streams, parallel linq, rayon, multiprocessing or some other syntax to iterate over that list using all available CPU’s. You apply them over your list and get back a list of processed elements. However if there are enough elements or the function you are applying is complex enough it should be done more quickly for multi-core systems.
However in Go its not obvious what you need to do to achieve this.
One possible solution is to spawn a Go routine for each item in your slice. Because of the low overhead of go-routines this is a valid strategy, to a point.
toProcess
:=
[]
int
{
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
}
var
wg
sync
.
WaitGroup
for
i
,
_
:=
range
toProcess
{
wg
.
Add
(
1
)
go
func
(
j
int
) {
toProcess
[
j
] =
someSlowCalculation
(
toProcess
[
j
])
wg
.
Done
()
}(
i
)
}
wg
.
Wait
()
fmt
.
Println
(
toProcess
)
The above will keep the order of the elements in the slice but lets assume this isn’t a requirement in our case.
One problem with the above is adding a waitgroup and having to remember to increment and call done on it. This is additional overhead on the developer. Get it wrong and this program will not produce the right output, either non-deterministically or never finish. In addition if your list is very long you are going to spawn a go-routine for every single one. As I said before this is not an issue itself because Go can do that without issue. What is going to be a problem is that each one of those go-routines is going to fight for a slice of the CPU. As such this is not going to be the most efficient way to perform this task.
What you probably wanted was to spawn a go-routine for each CPU and have them pick over the list processing it in turn. The overhead of additional go-routines is small, but for a very tight loop is not trivial, and when I was working on
scc
it was something I ran into hence it is limited to a go-routine per core. To do this in a Go centric way you need to build a channel, then loop over the elements of your slice and have your functions read from that channel, then another channel which you write to, or update the slice directly. Lets have a look.
toProcess
:=
[]
int
{
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
}
var
input
= make(
chan
int
, len(
toProcess
))
for
i
,
_
:=
range
toProcess
{
input
<-
i
}
close(
input
)
var
wg
sync
.
WaitGroup
for
i
:=
0
;
i
<
runtime
.
NumCPU
();
i
++
{
wg
.
Add
(
1
)
go
func
(
input
chan
int
,
output
[]
int
) {
for
j
:=
range
input
{
toProcess
[
j
] =
someSlowCalculation
(
toProcess
[
j
])
}
wg
.
Done
()
}(
input
,
toProcess
)
}
wg
.
Wait
()
fmt
.
Println
(
toProcess
)
The above creates a channel, and then loops over the slice and puts values in it. Then we spawn a go-routine for each CPU core that our OS reports and process that input channel, then we wait till its all done. It is a lot of code to digest.
Its not even how you should this really because if your slice is very large you probably don’t want to have a channel with a buffer of the same length, so you should actually spawn another go-routine to loop the slice and put those values into the channel and when finished close the channel. I have removed this because it made the code much longer and I want to approximate the basic idea.
Here is roughly the same thing in Java.
var
firstList
=
List.
of
(1,2,3,4,5,6,7,8,9);
firstList
=
firstList.
parallelStream
()
.
map
(
this
::someSlowCalculation)
.
collect
(Collectors.
toList
());
Yes channels and streams are not equivalent. You could replicate more closely the Go logic using a queue which would be closer to a true comparison, but the intent here is not a 1 to 1 comparison. What we wanted was to process a slice/list using all our CPU cores.
This of course is not an issue if
someSlowCalucation
is actually a method which calls out using the network or some other non CPU intensive task. In which case channels and go-routines are brilliant.
This issue ties into #1. If Go had functional methods on top of the slice/map objects adding this functionality would be possible. Its also annoying because if Go had generics someone could write the above as a library like rust’s rayon and everyone would benefit.
Incidentally I believe this is holding Go back from any success in the data science field hence why Python is still king there. Go lacks expressiveness and power in numerical manipulation. The above are reasons why this is so.
#3 Garbage Collector
The Go garbage collector is a very solid piece of engineering. With every release the applications I work on tend to get faster usually due to improvements in it. However prioritizes latency above all requirements. For API’s and UI’s this is a perfectly acceptable choice. It’s also fine for anything with network calls which are going to be the bottleneck as well.
The catch is that Go isn’t any good for UI work (no decent bindings exist that I am aware of) and this choice really hurts you when you want as much throughput as possible. I ran into this as a major issue when working on
scc
which is a command line application which is very CPU bound. It was such a problem I added logic in there to turn off the GC until it hits a threshold. However I could not just disable it because for some things it works on it would quickly run out of memory.
The lack of control over the GC is frustrating at times. You learn to live with it, but there are times where it would be nice to say “Hey this code here, it really just needs to run as fast as possible, so if you could flip into throughput mode for a little while that would be great.”
I think this is becoming less true with the 1.12 release of Go where the GC looks to be improved yet again, however just turning the GC off and on is less control then I would like over it. It is something I should investigate again when I have the time.
#4 Error Handling
I am not the only person with this complaint, but having to write,
value
,
err
:=
someFunc
()
if
err
!=
nil
{
// Do something here
}
err
=
someOtherFunc
(
value
)
if
err
!=
nil
{
// Do something here
}
Is pretty tedious. Go does not even force you to handle the error either which some people suggest. You can explicitly ignore it (does this count as handling it?) with
_
but you can also just ignore it totally. For example I could rewrite the above like,
value
,
_
:=
someFunc
()
someOtherFunc
(
value
)
Now its pretty easy to see I am ignoring something returned from
someFunc
but
someOtherFunc(value)
also can return an error, and I am just totally ignoring it. No handling of this situation at all.
To be honest I don’t know the solution here. I do like the
?
operator in Rust to help avoid this though. V-Lang
https://vlang.io/
looks like it might have some interesting solutions as well.
Another idea would be Optional types and the removal of
nil
, although this is never going to happen in Go even with Go 2.0 as it would break backwards compatibility.
Conclusion
Go is still a pretty decent language. If you told me to write an API, or some task that needs to make a lot of disk/network calls quickly it would still be my first pick. I’m actually at the point where its replacing Python for a lot of my throwaway tasks except data merging were the lack of functional programming is still painful enough to suffer the speed hit.
Things like sensible comparison between strings
stringA == stringB
and compile errors if you try to do the same with slices are really nice things and keep the principle of least surprise unlike Java which I used in the above comparisons.
Yes, the binary sizes could be smaller (some
compile flags and upx
can solve this), I would like it to be faster in some areas, GOPATH wasn’t great but also not as bad as everyone made out, the default unit-tests framework is missing a lot of functionality, mocking is a bit of a pain etc…
Still its one of the more productive languages I have used. I will continue to use it, although I am hopeful that
https://vlang.io/
will eventually be released and solve a lot of my complaints. Either that or Go 2.0, Nim or Rust. So many cool new languages to play around with these days. We developers really are spoiled.
