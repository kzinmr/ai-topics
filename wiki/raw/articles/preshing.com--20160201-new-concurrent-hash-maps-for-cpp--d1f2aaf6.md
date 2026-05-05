---
title: "New Concurrent Hash Maps for C++"
url: "https://preshing.com/20160201/new-concurrent-hash-maps-for-cpp"
fetched_at: 2026-05-05T07:01:04.111247+00:00
source: "Preshing"
tags: [blog, raw]
---

# New Concurrent Hash Maps for C++

Source: https://preshing.com/20160201/new-concurrent-hash-maps-for-cpp

A
map
is a data structure that maps a collection of keys to a collection of values. It’s a common concept in computer programming. You typically manipulate maps using functions such as
find
,
insert
and
erase
.
A
concurrent map
is one that lets you call some of those functions
concurrently
– even in combinations where the map is modified. If it lets you call
insert
from multiple threads, with no mutual exclusion, it’s a concurrent map. If it lets you call
insert
while another thread is calling
find
, with no mutual exclusion, it’s a concurrent map. Other combinations might be allowed, too. Traditional maps, such as
std::map
and
std::unordered_map
, don’t allow that.
Today I’m releasing
Junction
, a C++ library that contains several new concurrent maps. It’s BSD-licensed, so you can use the source code freely in any project, for any purpose.
On my Core i7-5930K, Junction’s two fastest maps outperform all other concurrent maps.
They come in three flavors:
Junction’s
Linear
map is similar to the
simple lock-free hash table
I published a while ago, except that it also supports resizing, deleting entries, and templated key/value types. It was inspired by Cliff Click’s
non-blocking hash map
in Java, but has a few differences.
Junction’s
Leapfrog
map is similar to Linear, except that it uses a probing strategy loosely based on
hopscotch hashing
. This strategy improves lookup efficiency when the table is densely populated. Leapfrog scales better than Linear because it modifies shared state far less frequently.
Junction’s
Grampa
map is similar to Leapfrog, except that at high populations, the map gets split into a set of smaller, fixed-size Leapfrog tables. Whenever one of those tables overflows, it gets split into two new tables instead of resizing the entire map.
Junction aims to support as many platforms as possible. So far, it’s been tested on Windows, Ubuntu, OS X and iOS. Its main dependencies are CMake and a companion library called
Turf
. Turf is an abstraction layer over POSIX, Win32, Mach, Linux, Boost, C++11, and possibly other platform APIs. You configure Turf to use the API you want.
Using Junction Maps
Instantiate one of the class templates using integer or raw pointer types.
typedef
junction::ConcurrentMap_Grampa<turf::u64, Foo*> ConcurrentMap;
ConcurrentMap myMap;
Each map exposes functions such as
get
,
assign
,
exchange
and
erase
. These functions are all atomic with respect to each other, so you can call them from any thread at any time. They also provide
release and consume semantics
implicitly, so you can safely pass non-atomic information between threads.
myMap.assign(
14
,
new
Foo);
Foo* foo = myMap.get(
14
);
foo = myMap.exchange(
14
,
new
Foo);
delete
foo;
foo = myMap.erase(
14
);
delete
foo;
Out of all possible keys, a
null
key must be reserved, and out of all possible values,
null
and
redirect
values must be reserved. The defaults are 0 and 1. You can override those defaults by passing custom
KeyTraits
and
ValueTraits
parameters to the template.
Safe Memory Reclamation
All Junction maps rely on a form of safe memory reclamation known as QSBR, or
quiescent state-based memory reclamation
. QSBR could be described as a primitive garbage collector.
If it seems odd to perform garbage collection in C++, keep in mind that scalable concurrent maps are already prevalent in Java, an entirely garbage-collected language. That’s no coincidence. Garbage collection allows you to sidestep locks, especially during read operations, which greatly improves scalability. Not even a read-write lock is necessary. You can certainly write a concurrent map in C++ without garbage collection, but I doubt it will scale as well as a Junction map.
To make QSBR work, each thread must periodically call
junction::DefaultQSBR.update
at a moment when that thread is
quiescent
– that is, not in the middle of an operation that uses the map. In a game engine, you could call it between iterations of the main loop.
Dynamically Allocated Values
Junction maps use QSBR internally, but you must still manage object lifetimes yourself. The maps don’t currently support smart pointers.
If you’re storing dynamically allocated objects, you’ll often want to check for existing entries in the table before inserting a new one. There are a couple of ways to do that. One way is to create objects optimistically, then detect racing inserts using
exchangeValue
.
ConcurrentMap::Mutator mutator = myMap.insertOrFind(
14
);
Foo* value = mutator.getValue();
if
(!value) {
    value =
new
Foo;
    Foo* oldValue = mutator.exchangeValue(value);
if
(oldValue)
        junction::DefaultQSBR.enqueue(&Foo::destroy, oldValue);
}
The above code uses a
Mutator
, which is like a pointer to a single entry in the map. First,
insertOrFind
creates an entry if one doesn’t already exist. Then, if two threads race to insert the same key, the second thread will garbage-collect the object created by the first.
Another way is to prevent such collisions entirely using double-checked locking. This approach guarantees that only one object will ever be created for a given key.
Foo* value = myMap.get(
14
);
if
(!value) {
    turf::LockGuard<turf::Mutex> lock(someMutex);
    ConcurrentMap::Mutator mutator = myMap.insertOrFind(
14
);
    value = mutator.getValue();
if
(!value) {
        value =
new
Foo;
        mutator.assignValue(value);
    }
}
Development Status
You should consider this alpha software. All of the code is experimental. I spent a lot of effort to get it right, and it passes all the tests I’ve thrown at it, but you never know – bugs might still lurk under the surface. That’s part of the reason why I’m releasing the code for free. Readers of this blog have proven quite good at finding obscure bugs. I hope you’ll subject Junction to your harshest scrutiny.
[Update Dec. 30, 2017: Almost two years after this was published,
the first bug
has been spotted and fixed.]
If you’d like to contribute to the project in other ways, here are a few suggestions:
Porting Turf to additional platforms
Further optimization
Searching the repository for
FIXME
comments
Identifying missing functionality that would be useful
To leave feedback, simply post a comment below,
open an issue
on GitHub, or use my direct
contact form
.
