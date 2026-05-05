---
title: "Rust streams and timeouts gotcha"
url: "https://laplab.me/posts/rust-streams-gotcha/"
fetched_at: 2026-05-05T07:01:23.963185+00:00
source: "Nikita Lapkov (laplab)"
tags: [blog, raw]
---

# Rust streams and timeouts gotcha

Source: https://laplab.me/posts/rust-streams-gotcha/

Imagine we have a list of paths to Parquet files on R2. We need to fetch Parquet footer of each file. However, we don’t know in advance whether we will need footers of all files and we want to avoid fetching extra.
Rust has a streams abstraction. It is kind of like an iterator, but with async operations permitted. Like iterators, streams are lazy - they don’t do anything unless explicitly polled. This sounds like it ticks all the boxes, so lets try to implement it:
use
futures::stream::{
self
, StreamExt};
let
footers = stream::iter(parquet_paths).map(|path|
async
move
{
// TODO: Perform some validation, return errors as needed.
fetch_parquet_footer(path).
await
});
while
let
Some
(footer) = footers.next().
await
{
// TODO: Process footer.
}
This works! We fetch only the footers we need and the code is pretty clean. We can even add
StreamExt::buffered(n)
to make fetching happen in parallel at the expense of some over-fetching at the end (if you don’t consume all items).
When I deployed this at work, we started seeing random timeouts from R2 in the logs. We weren’t quite sure what caused this until my colleague noticed the subtle bug. Our app has many async tasks running, all joined like this:
tokio::
select!
{
_ = task1() => {
...
}
_ = task2() => {
...
}
...
}
Sometimes one of these tasks will take a particularly long time before getting to the next
.await
and releasing the control to the runtime. This made the following execution order possible:
Open connection to R2, wait for R2 to return the bytes of the object. This point is
.await
ed
Switch to running another task and take just long enough to exceed the R2 timeout
Return to the first task and observe the timeout
There are a couple of ways to fix this problem. The quick fix is to to spawn every fetch like this:
let
footers = stream::iter(parquet_paths).map(|path|
async
move
{
// TODO: Perform some validation, return errors as needed.
tokio::spawn(fetch_parquet_footer(path)).
await
});
You can also spawn a task that fetches the footers:
tokio::
select!
{
_ = tokio::spawn(task1()) => {
...
}
_ = task2() => {
...
}
...
}
Once you destructure the bug, its pretty clear and easy to fix. Still, I found this combination of streams, their futures, timeouts and cooperative multitasking pretty fun!
Update:
Even with the two solutions above, there is still a problem of the original blocking task. This is the task that blocked the runtime just long enough for the timeout to fire. I assumed that since Tokio uses work-stealing executor, its going to just steal the task fetching data from R2 to another thread. As
pointed out
by
@mikedorf
on lobsters, that’s not always the case! So the better solution is to offload blocking work to
spawn_blocking()
, as
suggested
by
@kornel
.
