---
title: "Rust's Rules Are Made to Be Broken"
source: "Warp Blog"
url: "https://www.warp.dev/blog/rules-are-made-to-be-broken"
scraped: "2026-05-10T01:28:04.726406+00:00"
lastmod: "2026-04-24T14:39:52.000Z"
type: "sitemap"
---

# Rust's Rules Are Made to Be Broken

**Source**: [https://www.warp.dev/blog/rules-are-made-to-be-broken](https://www.warp.dev/blog/rules-are-made-to-be-broken)

Engineering
Rust's Rules Are Made to Be Broken
Chuck Pierce
March 1, 2022
Brief introduction to several tools in the Rust standard library that let you break the borrow checker's rules: Rc, Arc, RefCell, Mutex, RwLock, and Atomics.
We’ve talked
in the past
about why we chose to build Warp in Rust. Since making that decision, one thing that stands out is how productive we are as a team while still reaping the performance benefits of a systems level language.
A big reason for that productivity is the borrow checker.
By enforcing its rules at compile time, Rust’s
borrow checker
is able to make guarantees about the memory safety of our app, which lets us focus more of our energy on building the future of the terminal and less on chasing down use-after-free bugs.
At the same time, the borrow checker can be a source of frustration. Sometimes, you need to do something that breaks the rules but don’t want to throw the safety out the window.
Fortunately, the Rust standard library provides helpful types to let you do just that: break the rules!
Shared Ownership
+
Reference counting (Rc and Arc)
Unique Borrows
+
RefCell
+
Locking Types (Mutex and RwLock)
+
Atomics
Shared Ownership
The first borrow checker rule we’re going to break is single ownership: By default in Rust, every piece of data has a single owner, and when that owner goes out of scope, the data is cleaned up. This is great for ergonomics as you don’t have to worry about manually allocating and freeing memory!
However, sometimes you don’t want data to have only a single owner. Maybe you want the data to pass through different parts of your program that will each run for different lengths and there’s no way to know how long in total the data needs to exist. Maybe you’re prototyping and don’t yet want to tackle ownership and lifetimes in a more concrete way. Whatever the reason, you really would like to have multiple owners for some data, so that it lasts as long as all of them combined.
Reference counting to the rescue!
Built into the Rust standard library are two types that provide shared ownership of the underlying data:
`Rc`
and
`Arc`
(short for ‘Reference counted’ and ‘Atomically reference counted’, respectively).
Both of these types give shared ownership of the contained data by tracking the number of references and ensuring the data will last as long as there are any active references. They each implement
Clone
and
Drop
: cloning increments the reference count while dropping one decrements it. The data is kept alive as long as there are references and only cleaned up once all of the clones have gone out of scope. For example, this snippet uses
Rc
to share ownership of two pet objects between two owners:
Embed:
https://gist.github.com/charlespierce/27bec09d15f303b99739775f3a2a19c6
Both types incur a small amount of runtime overhead to maintain the reference count. The key difference between them is that
Arc
is thread safe, while
Rc
isn’t.
Arc
uses atomic operations to manage the reference count, which gives it a higher runtime cost but makes it safe to share between threads. If you’re only working in a single thread, then
Rc
is the faster alternative.
The last important fact about
Rc
and
Arc
is that they only allow you to get immutable references to the underlying data.
[2]
Since they fundamentally represent shared data, allowing mutable references would violate Rust’s safety guarantees by allowing for data races and use-after-free errors.
Unique Borrows
“But wait!,” you say, “What if I want to share mutable data between parts of my app?” Luckily, the next borrow checker rule we’re going to break is unique borrows: In order to mutate something, you need to have a unique (also called mutable) reference to the data. The borrow checker enforces that you can only have one mutable reference or any number of immutable references, but never a combination of the two, so you can’t ever mutate data that another part of the program is trying to read at the same time.
This restriction works great most of the time, but we’re here to break the rules! Two cases where you might want to mutate data without having a mutable reference are:
Caching an otherwise immutable calculation (i.e. memoization)
The above shared ownership case with Rc or Arc
For bending the compile-time borrowing rules, the compiler provides several helpful types, each with their own sets of drawbacks. All of them let you safely mutate data behind an immutable reference, using different approaches to make sure that your program is still safe.
[3]
RefCell
First up is
`RefCell`
, which moves the enforcement of unique borrows from compile-time to runtime. Similar to
Rc
,
RefCell
uses reference counting to track how many borrows are active while the program is running. If you ever try to take a mutable reference and another reference at the same time,
RefCell
will immediately panic! So when using
RefCell
, it’s up to you to make sure that your program doesn’t try to read and write the same data at the same time.
Here's an example of using
RefCell
to cache intermediate results for something that is otherwise immutable:
Embed:
https://gist.github.com/charlespierce/e9b38ec0d6696b87b3a6d23334ff9faa
Also, the reference counting in
RefCell
is not thread safe, so it’s not possible to share
RefCell
data between threads. For mutating shared data between threads, we need to turn to our next tool.
Locking Types
The next two types are
`Mutex`
and
`RwLock`
, which both provide ways to access mutable references from an immutable reference in a thread-safe way. They do this by completely blocking the thread until it is safe to access the data. This provides a strong guarantee that the access is safe, but also has a major pitfall: Deadlocks. Deadlocks occur when two threads are blocked waiting for access to data that the other thread is holding. Similar to
RefCell
, it's up to you to make sure the logic of your program doesn't hold onto some data while waiting for access to other data leading to a deadlock.
For example, the following snippet uses a Mutex to increment a counter in parallel in two new threads, then reads the final result from the original thread:
Embed:
https://gist.github.com/charlespierce/87a16e28a98198d0312f8982e1c29623
The key difference between the two types is how they handle different kinds of access. A
Mutex
doesn’t care about whether you are trying to read or write the data, only a single thread can have access at a time. All other threads have to wait until the current consumer gives up their access.
By contrast,
RwLock
follows Rust’s rules: Any number of threads can have read-only access to the underlying data or a single thread can have write access, but no combination. Attempting to obtain write access will block until there are no active readers and vice versa.
The thread safe nature of these locking types makes them some of the most powerful ways to share mutable data, however it comes at potentially significant performance cost: Locking the thread so that no other work can be done until the data is available. If our data is simple enough, the last type we’re going to look at can provide shared access across threads without needing to lock.
Atomics
Atomic types
are available for integer and boolean primitives. These types all provide methods to mutate or read the data as a single operation, so that nothing can happen in between and there is no possibility for data races.
For example, if you want to increment a counter, instead of reading the value, adding one, then writing the value, you would use the
`fetch_add`
method that does all of that in a single block.
Atomics are often used as the building blocks for more complicated thread-safe sharing or one-off initialization. As mentioned above, Arc uses an atomic counter internally to manage the reference counting in a thread-safe way.
\---
The beauty of all of these types is that they provide a way to break the borrow checker rules while still maintaining Rust’s safety guarantees. Understanding which rules each type breaks is the key to knowing which tool you need. If you’re looking for shared ownership without copying, you want the reference counted types. If you’re looking for mutability without Rust’s strict mutable references, reach for interior mutability. And if you need shared mutable state, it’s not uncommon to use a combination of them:
Rc<RefCell<T>>
or
Arc<Mutex<T>>
are combinations for single- and multithreaded shared mutable ownership, respectively.
\---
Footnotes
This cleanup is managed by the
Drop
trait, see the docs for more info.
↩︎
This isn’t strictly true, if there is exactly one reference active, it
is possible
to get a mutable reference out of an Rc or Arc. But in the context of shared data there will be more than one reference active most of the time.
This general approach is called “Interior Mutability”, contrasted with the more standard “Inherited Mutability” which requires a mutable reference to mutate data.
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
