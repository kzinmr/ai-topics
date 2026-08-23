---
title: "Concurrent Servers: Part 8 - Go"
url: "https://eli.thegreenplace.net/2026/concurrent-servers-part-8-go/"
fetched_at: 2026-08-23T10:01:41.404082+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Concurrent Servers: Part 8 - Go

Source: https://eli.thegreenplace.net/2026/concurrent-servers-part-8-go/

This is part 8 in a series of posts on writing concurrent network servers. In
this part, we'll switch to Go and see how it tackles the challenges described
earlier in the series.
All posts in the series:
This post assumes a basic familiarity with the Go programming language.
Sequential state machine server
As before, we'll start with a sequential server for the basic state machine
protocol presented in
part 1
.
This is the main function:
func
main
()
{
port
:=
"9090"
if
len
(
os
.
Args
)
>=
2
{
port
=
os
.
Args
[
1
]
}
log
.
Println
(
"Serving on port"
,
port
)
listener
,
err
:=
net
.
Listen
(
"tcp"
,
":"
+
port
)
if
err
!=
nil
{
log
.
Fatal
(
"Error listening:"
,
err
)
}
defer
listener
.
Close
()
for
{
conn
,
err
:=
listener
.
Accept
()
if
err
!=
nil
{
log
.
Printf
(
"Error accepting connection: %v"
,
err
)
continue
}
log
.
Println
(
"connection received from"
,
conn
.
RemoteAddr
())
if
err
:=
server
.
ServeSerialProtocol
(
conn
);
err
!=
nil
{
log
.
Printf
(
"Error serving %v: %v"
,
conn
.
RemoteAddr
(),
err
)
}
else
{
log
.
Println
(
"peer done"
,
conn
.
RemoteAddr
())
}
}
}
As in the previous parts, the server is "infinite"; it never stops serving new
connections until it's explicitly killed.
This is the function implementing the protocol for a single client; it takes
a
net.Conn
value that represents a socket with a client connected on the
other end:
type
processingState
int
const
(
waitForMsg
processingState
=
iota
inMsg
)
// ServeSerialProtocol serves our serial protocol to a single TCP connection.
func
ServeSerialProtocol
(
conn
net
.
Conn
)
error
{
defer
conn
.
Close
()
if
_
,
err
:=
conn
.
Write
([]
byte
{
'*'
});
err
!=
nil
{
return
err
}
var
state
processingState
=
waitForMsg
buf
:=
make
([]
byte
,
1024
)
for
{
n
,
err
:=
conn
.
Read
(
buf
)
for
_
,
b
:=
range
buf
[:
n
]
{
switch
state
{
case
waitForMsg
:
if
b
==
'^'
{
state
=
inMsg
}
case
inMsg
:
if
b
==
'$'
{
state
=
waitForMsg
}
else
{
var
bb
byte
=
byte
(
b
)
+
1
if
_
,
err
:=
conn
.
Write
([]
byte
{
bb
});
err
!=
nil
{
return
err
}
}
}
}
// Check error after processing the bytes received along with it.
if
err
!=
nil
{
if
errors
.
Is
(
err
,
io
.
EOF
)
||
errors
.
Is
(
err
,
net
.
ErrClosed
)
{
return
nil
}
else
{
return
err
}
}
}
}
One goroutine per client
Rather than directly exposing OS threads, the Go runtime implements its own
M:N scheduling of lightweight
goroutines
on top of OS threads. Using
goroutines in Go is cheap - both in terms of syntax and developer effort, and in
terms of
system resources
.
Here's a version of our serial protocol server that serves clients concurrently
by launching a goroutine for each client. The part of the code that's different
from the previous sample is highlighted:
func
main
()
{
port
:=
"9090"
if
len
(
os
.
Args
)
>=
2
{
port
=
os
.
Args
[
1
]
}
log
.
Println
(
"Serving on port"
,
port
)
listener
,
err
:=
net
.
Listen
(
"tcp"
,
":"
+
port
)
if
err
!=
nil
{
log
.
Fatal
(
"Error listening:"
,
err
)
}
defer
listener
.
Close
()
for
{
conn
,
err
:=
listener
.
Accept
()
if
err
!=
nil
{
log
.
Printf
(
"Error accepting connection: %v"
,
err
)
continue
}
log
.
Println
(
"connection received from"
,
conn
.
RemoteAddr
())
go
func
()
{
if
err
:=
server
.
ServeSerialProtocol
(
conn
);
err
!=
nil
{
log
.
Printf
(
"Error serving %v: %v"
,
conn
.
RemoteAddr
(),
err
)
}
else
{
log
.
Println
(
"peer done"
,
conn
.
RemoteAddr
())
}
}()
}
}
The concurrent modification in this case is particularly simple because the
server is infinite; there's no point waiting for these goroutines to finish
(and hence no need for a
sync.WaitGroup
).
The parameters for
server.ServeSerialProtocol
are lexically captured from
the enclosing scope and its return value is handled by the surrounding closure.
Because goroutines are very cheap, this server is very unlikely to run out
of resources due to launching too many goroutines; in fact, it will probably
run out of something else - like file descriptors for sockets - first. However,
sometimes it's still useful to limit the degree of concurrency - even
in Go, and we'll discuss some approaches to do so in the following sections.
Limiting concurrency with a semaphore
Here are some scenarios in which it makes sense to limit the degree of
concurrency in Go programs, even though goroutines are cheap to launch and
operate:
Tasks may be compute intensive, and the CPU capacity of any server is inherently
limited. If too many concurrent goroutines compete for limited CPUs, they
will all make very little progress. It may make more sense to have fewer tasks
that complete in a reasonable time.
Protecting potentially limited downstream resources, such as concurrent
DB connections or other services. For example, if the server has to send
requests to other services for each task, and these are rate-limited,
concurrency will have to be carefully managed.
Security reasons when work is dictated by clients; malicious clients can
overload and crash a service that's too eager to serve, making it unavailable
for legitimate clients.
Let's switch to the primality testing server from
part 4
for the rest of the
post, because it represents a somewhat more realistic workload.
As a reminder: the server receives numbers, simulates blocking
by sleeping, and returns "prime" or "composite". The unbounded
one-goroutine-per-client version looks
almost identical
to the previous code sample, except that the goroutine invocation calls another
function:
go
func
()
{
if
err
:=
server
.
ServePrimeProtocol
(
conn
);
err
!=
nil
{
log
.
Printf
(
"Error serving %v: %v"
,
conn
.
RemoteAddr
(),
err
)
}
else
{
log
.
Println
(
"peer done"
,
conn
.
RemoteAddr
())
}
}()
Where
ServePrimeProtocol
is :
// ServePrimeProtocol serves our prime protocol to a single TCP connection.
func
ServePrimeProtocol
(
conn
net
.
Conn
)
error
{
defer
conn
.
Close
()
buf
:=
make
([]
byte
,
1024
)
for
{
n
,
readerr
:=
conn
.
Read
(
buf
)
if
n
>
0
{
// Parse the read buffer to an i64
num
,
err
:=
strconv
.
ParseInt
(
strings
.
TrimSpace
(
string
(
buf
[:
n
])),
10
,
64
)
if
err
!=
nil
{
return
err
}
response
:=
"composite"
if
isPrime
(
num
,
true
)
{
response
=
"prime"
}
if
_
,
err
:=
conn
.
Write
([]
byte
(
response
+
"\n"
));
err
!=
nil
{
return
err
}
}
if
readerr
!=
nil
{
if
errors
.
Is
(
readerr
,
io
.
EOF
)
||
errors
.
Is
(
readerr
,
net
.
ErrClosed
)
{
return
nil
}
return
readerr
}
}
}
// isPrime returns true if n is prime, false otherwise. If delay is true, it
// will sleep for n milliseconds before calculating.
func
isPrime
(
n
int64
,
delay
bool
)
bool
{
if
delay
{
time
.
Sleep
(
time
.
Duration
(
n
)
*
time
.
Millisecond
)
}
if
n
<
2
{
return
false
}
if
n
%
2
==
0
{
return
n
==
2
}
for
i
:=
int64
(
3
);
i
*
i
<=
n
;
i
+=
2
{
if
n
%
i
==
0
{
return
false
}
}
return
true
}
The simplest way to limit concurrency in Go is by using a counting semaphore,
implemented with a channel:
func
main
()
{
port
:=
"8070"
if
len
(
os
.
Args
)
>=
2
{
port
=
os
.
Args
[
1
]
}
log
.
Println
(
"Serving on port"
,
port
)
listener
,
err
:=
net
.
Listen
(
"tcp"
,
":"
+
port
)
if
err
!=
nil
{
log
.
Fatal
(
"Error listening:"
,
err
)
}
defer
listener
.
Close
()
maxConcurrency
:=
runtime
.
NumCPU
()
sem
:=
make
(
chan
struct
{},
maxConcurrency
)
for
{
conn
,
err
:=
listener
.
Accept
()
if
err
!=
nil
{
log
.
Printf
(
"Error accepting connection: %v"
,
err
)
continue
}
log
.
Println
(
"connection received from"
,
conn
.
RemoteAddr
())
// Acquire a token from the semaphore to limit concurrency.
sem
<-
struct
{}{}
go
func
()
{
// Return the token when done serving the connection.
defer
func
()
{
<-
sem
}()
if
err
:=
server
.
ServePrimeProtocol
(
conn
);
err
!=
nil
{
log
.
Printf
(
"Error serving %v: %v"
,
conn
.
RemoteAddr
(),
err
)
}
else
{
log
.
Println
(
"peer done"
,
conn
.
RemoteAddr
())
}
}()
}
}
The channel
sem
serves as a semaphore; note that it's a bounded channel
with a maximal size. A token is acquired by sending to the channel, and released
by receiving from the channel. When the channel is full, the send operation
sem <-
struct{}{}
blocks until a token was removed by some other goroutine
.
The type of the channel is
struct{}
which means "empty", or "no data". This
is idiomatic in Go for channels that are used solely for their semantics, not
to send/receive any actual data.
Worker pool
Since launching goroutines is cheap and limiting concurrency is easy as shown
above, the "worker pool" pattern is often unnecessary for scenarios like our
server. Still, it has occasional uses (such as when workers have to maintain
some non-trivial state across tasks) so it's worth discussing it here.
Here's a variant of our primality testing server that uses a worker pool:
func
worker
(
jobs
<-
chan
net
.
Conn
)
{
for
conn
:=
range
jobs
{
if
err
:=
server
.
ServePrimeProtocol
(
conn
);
err
!=
nil
{
log
.
Printf
(
"Error serving %v: %v"
,
conn
.
RemoteAddr
(),
err
)
}
else
{
log
.
Println
(
"peer done"
,
conn
.
RemoteAddr
())
}
}
}
func
main
()
{
port
:=
"8070"
if
len
(
os
.
Args
)
>=
2
{
port
=
os
.
Args
[
1
]
}
log
.
Println
(
"Serving on port"
,
port
)
listener
,
err
:=
net
.
Listen
(
"tcp"
,
":"
+
port
)
if
err
!=
nil
{
log
.
Fatal
(
"Error listening:"
,
err
)
}
defer
listener
.
Close
()
// The channel is unbuffered, so it will block when there are no available
// workers to accept a new connection.
jobs
:=
make
(
chan
net
.
Conn
)
maxConcurrency
:=
runtime
.
NumCPU
()
for
i
:=
0
;
i
<
maxConcurrency
;
i
++
{
go
worker
(
jobs
)
}
for
{
conn
,
err
:=
listener
.
Accept
()
if
err
!=
nil
{
log
.
Printf
(
"Error accepting connection: %v"
,
err
)
continue
}
log
.
Println
(
"connection received from"
,
conn
.
RemoteAddr
())
jobs
<-
conn
}
}
A fixed number of worker goroutines is launched; these goroutines all receive
"jobs" from the same channel. In the
Accept
loop, each client connection
is sent to this channel as a new job and is picked up by the next available
worker. As mentioned before, you would typically see a
sync.WaitGroup
somewhere to ensure clean shutdown of goroutines, but in our case it isn't
necessary because we have a server that never exits.
Async?
Do programmers have to resort to async / event-driven programming in Go? In
my experience, almost never. Go was designed from the bottom up to be
suitable for large-scale concurrency; goroutines are very cheap to create, have a
tiny memory footprint and switching happens very quickly, all in user space.
Measurements I ran
back in 2018
have shown switching times of ~170 ns, as compared to 1-2 microseconds for threads
on Linux.
Moreover, Go already uses event-driven loops like
epoll
underneath for I/O.
Goroutines that wait for I/O like sockets are effectively "parked" and consume
no resources (beyond their small memory footprint); they are woken up by
Go's runtime when their I/O descriptors are ready - this is very similar to how
asynchronous programming works!
That said, some people certainly do try to stretch their resources even more
with direct asynchronous programming in Go when
millions
of streams are
handled concurrently. All I'll say is that this is very rare, and an
overwhelming majority of users never have to do this.
Conclusion
In 2018, I wrote a post named
Go hits the concurrency nail right on the head
,
and after several more years of active coding, I fully stand behind that statement.
Go is extremely powerful and ergonomic for concurrent programs; while other environments
go to great lengths to implement async-await style event loops in libraries,
in Go it's already baked into the core language and runtime. You want
event-driven I/O with very lightweight green threads that can also execute
blocking tasks without worrying about the
function coloring problem
?
Go has you covered.
Code
All the code for this post is available
on GitHub
.
