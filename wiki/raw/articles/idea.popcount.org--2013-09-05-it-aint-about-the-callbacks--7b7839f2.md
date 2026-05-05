---
title: "It ain't about the callbacks..."
url: "https://idea.popcount.org/2013-09-05-it-aint-about-the-callbacks"
fetched_at: 2026-05-05T07:01:12.799917+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# It ain't about the callbacks...

Source: https://idea.popcount.org/2013-09-05-it-aint-about-the-callbacks

It ain't about the callbacks...
05 September 2013
... it's about the flow control
Programmers tend to be very opinionated about programming with
callbacks
.
It's just a programming style, not a big deal usually, but it becomes
an issue when a platform forces you to use
only
the callback
style. I'm talking about you, JavaScript.
In my opinion people forget an important point in the discussion about
callbacks.
The problem is: different programming styles
1
encourage different
solutions, and not all solutions are equally good. In particular
forcing people to use callbacks encourages
bad
solutions to common
problems. Most annoyingly it makes it very easy to forget about data
flow control.
Let me start with an example of a broken Node.js API.
Yup, it's an Echo server again
Here's a naive
echo server
in node.js:
var
net
=
require
(
'net'
);
var
server
=
net
.
createServer
();
server
.
on
(
'connection'
,
function
(
c
)
{
c
.
on
(
'data'
,
function
(
data
)
{
c
.
write
(
data
);
});
});
server
.
listen
(
10007
)
There are two things wrong in this code:
It's impossible to slow down the pace of accepting new incoming
   client connections.
A noisy client will be able to crash our server, as
c.write
is
   non-blocking and will buffer an infinite amount of data in memory (this
   can be partially solved with a node.js Stream API, more on that
   later).
1) The implicit
accept
The first problem: we can't slow down the pace of accepting new
connections. The
accept(2)
syscall is being implicitly handled by
node.
As far as I know there isn't a way around it. It's caused by the
design of the non-blocking API that doesn't support flow-control. You
can't tell the server "don't accept any more client connections,
please!"
An astute reader may notice the
server.maxConnections
property
. But
this is not the same - it causes client sockets to be
closed
when
the limit is reached. I don't want clients to get actively rejected, I
don't want to
accept
them in the first place!
In my ideal programming environment the
accept
would be
blocking. I'd have a main coroutine for a server looking like this:
while
true
:
if
can_serve_more_clients
()
:
client
=
server
.
accept
()
deal_with_the_client
(
client
)
else:
block_until_can_serve_more_clients
()
To work around this problem node.js could add a new method to "pause"
the
net.Server
for a while. But this is a bad design as well.  Let's
explain this using our second illustration - the design of node.js
Streams.
2) Streams suffer a race condition
Node.js Streams
are a common API that support basic flow control for common data
sources that can
read
and/or
write
. In our code the
client
socket is a valid node.js Stream and using Streams API our code gets
even simpler:
var
net
=
require
(
'net'
);
var
server
=
net
.
createServer
();
server
.
on
(
'connection'
,
function
(
c
)
{
c
.
pipe
(
c
);
});
server
.
listen
(
10007
)
The
pipe
command forwards all data received on the
data
event to
the
write
method.
This code doesn't suffer from the described problem - now a single
client won't be able to crash node with out-of-memory. It works as
follows: on the
data
event bytes are passed to the
write
method.
The
write
method can return
false
,
meaning "please stop writing for now". The stream understands this and
calls the
pause
method on the reader. On the
drain
event the
reader
resumes
.
As a result the stream will stop reading from
c
if data can't be
written to
c
. Clever, right?
First, I believe most node.js programmers (including myself) don't
understand Streams and just don't implement the Stream interfaces
correctly.
But even if Streams were properly implemented everywhere the API
suffers a race condition: it's possible to get plenty of data before
the writer reacts and stops the reader. The stream needs to actively
inform the reader when something happens to the writer. It's like a
line of people passing bricks - when the last person says: "no more
bricks please!" everybody in the line will have their hands full!  The
longer the queue the more bricks will get "buffered".
Particularly in node using Streams it's possible to receive plenty
of data before the back pressure kicks in.
var
net
=
require
(
'net'
);
var
server
=
net
.
createServer
();
server
.
on
(
'connection'
,
function
(
c
)
{
c
.
pipe
(
c
);
c
.
on
(
'data'
,
function
(
d
)
{
console
.
log
(
'received'
,
d
.
length
);
});
c
.
on
(
'drain'
,
function
(
d
)
{
console
.
log
(
'it\'s okay to receive'
);
});
var
p
=
c
.
push
;
c
.
push
=
function
(
chunk
)
{
var
r
=
p
.
apply
(
c
,
[
chunk
]
);
if
(
r
==
false
)
console
.
log
(
'stop receiving now!'
);
return
r
;
}
});
server
.
listen
(
10007
);
When you run this code and start a noisy client that floods the server
with plenty of data, you'll see:
it's okay to receive
received 65536
stop receiving!
received 65536
Once again: we received a chunk of data
after
we told the server to
stop receiving. In the real world the problem is even more serious:
there is usually a significant delay between the reader and the
writer, so even more data will get buffered.
Let's try to make it more concrete: imagine a web server that needs to
speak to Redis, SQL database and read a local file before crafting an
HTTP response. Then, the writer may notice the network connection is
slow and react accordingly: tell the reader to stop receiving new
requests from the client. But in the meantime the time has passed and
your server could have already received thousands of HTTP requests
from the evil client. The race condition in the Stream API is serious
due to the fact that the delay between receiving an evil request and
noticing that evil client doesn't read can be significant.
In our code the only solution to this problem is to deliver exactly
one data chunk and wait for a confirmation before receiving another
one. Using the bricks analogy: the last person would shout "please
give me a new brick" when it dealt with the last one, thus
guaranteeing that no matter how many hands are in the line, at most
one brick will be processed at a time.
This damages the throughput but guarantees we won't run out of memory
even in case of an evil client.
Push and pull
In programming, the code can be written in one of two ways:
It can "pull" the data from the source.
It can "push" the data to the destination.
Synchronous code usually does the first thing, callbacks do the
second. Neither is better or worse, but in the "pull" model it's much
easier to reason about the flow control. On the other hand in a badly
written "push" code a fast producer (or a slow consumer) can overwhelm
the program.
Synchronous code embeds the flow control in its structure. It's much
harder to express the data flow control using callbacks
2
.
Finally, please don't get me wrong. Although this rant is focused
around node.js it's not limited to it. It's generally hard to think
about end-to-end flow control in callback based environments. It's
impossible to design good callback based API's when you don't have
tools to deal with data flow control.
