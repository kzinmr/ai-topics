---
title: "How to sleep a million years"
url: "https://idea.popcount.org/2013-07-19-how-to-sleep-a-million-years"
fetched_at: 2026-05-05T07:01:12.906832+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# How to sleep a million years

Source: https://idea.popcount.org/2013-07-19-how-to-sleep-a-million-years

How to sleep million years
19 July 2013
Let me assure you, the
"fluxcapacitor"
project is very interesting. Unfortunately, I find it very difficult
to describe what it does. For this project I completely fail the
elevator pitch
.
I won't attempt to describe it, instead I'll try present it in action.
Prerequisites
First, you need to compile the fluxcapacitor (FC), it's supposed to be
simple:
$
sudo aptitude install git gcc make
$
git clone https://github.com/majek/fluxcapacitor.git
$
cd
fluxcapacitor
$
make
If you're lucky you should have FC up and running:
$
.
/
fluxcapacitor
--
help
Usage:
fluxcapacitor
[
options
]
[
--
command
[
arguments
...
]
...
]
Introduction
Fluxcapacitor runs any program in an special environment which has
different view on passing time than the rest of the operating
system. From a point of view of a program everything is normal, but if
you observe it from outside you'll see it run "faster". You can say
fluxcapacitor speeds up the flow of time for the program. For example:
$
time
sleep
12
real
0
m12
.003
s
$
time
.
/
fluxcapacitor
--
sleep
12
real
0
m0
.057
s
Both times
sleep
thinks 12 seconds had passed. But in the second
case the observer would disagree - it only took a few milliseconds to
finish.
Sleep
isn't able to realize that.
Notice the
time
command was run
outside
fluxcapacitor
environment. If you run it inside, it will surely report 12 seconds:
$
.
/
fluxcapacitor
--
bash
-
c
"time sleep 12"
real
0
m12
.016
s
Let's make the example more extreme:
$
.
/
fluxcapacitor
--
bash
-
c
"sleep 315360000; date"
Sat
Jul
15
11
:
36
:
23
BST
2023
We briefly went to the year 2023.
How to sleep a million years
You can try sleeping for any time you wish. Unfortunately my operating
system (bash?) can't express dates after the year 2550:
$
./fluxcapacitor --idleness
=
0 -- bash -c
\
'for i in `seq 1 100`; do sleep 315360000; date; done'
Sat Jul 15 11:38:25 BST 2023
Tue Jul 12 11:38:25 BST 2033
Fri Jul 10 11:38:25 BST 2043
...
Sun Apr 28 11:38:26 BST 2543
Wed Apr 25 11:38:26 BST 2553
Tue Oct  3 12:03:52 BST 1978
Fri Sep 30 12:03:52 BST 1988
...
Fluxcapacitor is very powerful, let's jump to more sophisticated
examples.
Speeding up sleep sort
In 2011 someone on 4chan invented the
"sleep sort" algorithm
:
#!/bin/bash
function
f
()
{
sleep
"$1"
echo
-n
"$1 "
}
while
[
-n
"$1"
]
do
f
"$1"
&
shift
done
wait
echo
It sorts numbers by spawning many processes and waiting approriate
number of seconds. For example:
$
time
.
/
sleepsort
.
sh
5
3
6
3
6
3
1
4
7
1
3
3
3
4
5
6
6
7
real
0
m7
.012
s
Although this was intended as a joke, with fluxcapacitor you can run it
in a fraction of a second:
$
time
.
/
fluxcapacitor
--
.
/
sleepsort
.
sh
5
3
6
3
6
3
1
4
7
1
3
3
3
4
5
6
6
7
real
0
m0
.056
s
For the curious: the complexity of sleep sort on
fluxcapacitor is
O(n^2)
.
Advanced usage
Sleep sort forked many processes and fluxcapacitor is able to guard
any number of OS processes or threads. You can spawn many commands by
delimiting the command line with two dashes
--
:
$
time
./fluxcapacitor
\
-- bash -c
"sleep 60; date"
\
-- bash -c
"sleep 120; date"
Wed Jul 17 13:14:01 BST 2013
Wed Jul 17 13:15:01 BST 2013
real    0m0.179s
With many processes things get really interesting.
Memcached expiration
Let's try to use do something more
complicated.
Memcached
, a
caching daemon, can expire an item after a timeout. Let's try to test it
using fluxcapacitor. We need to run two processes within FC:
"server" - the memcached deamon:
/
tmp
/
memcached
-
1.4.15
/
memcached
-
p
1121
"client" - a simple bash script. It will set the key with
   appropriate expiry timeout, check if it's there, wait some time and
   check for the key again. Finally we need to kill the memcached
   daemon. The code:
# 1) set key foo with timeout of 60 seconds
echo
-
e
"set foo 0 60 2
\r\n
aa"
|
nc
localhost
1121
# 2) is foo still there? (it should)
echo
"get foo"
|
nc
localhost
1121
# 3) wait for 70 seconds
sleep
70
# 4) is foo still there? (it shouldn't)
echo
"get foo"
|
nc
localhost
1121
# 5) cleanup, don't need memcached anymore
killall
memcached
It would be better to write a proper script for the "client" part, but
we can also run it inline as a parameter to
bash -c
. Here it goes:
$
time
.
/
fluxcapacitor
--
/
tmp
/
memcached
-
1.4.15
/
memcached
-
p
1121
--
bash
-
c
'
echo
-
e
"set foo 0 60 2
\r\n
aa"
|
nc
localhost
1121
;
echo
"get foo"
|
nc
localhost
1121
;
sleep
70
;
echo
"get foo"
|
nc
localhost
1121
;
killall
memcached
'
STORED
VALUE
foo
0
2
aa
END
END
real
0
m0
.521
s
Memcached behaves as it should. The test takes about 500ms, instead of
70 seconds it would take without the FC.
You may want to pass
--idleness=5ms
option to FC to make it go
fast. Without this option the test takes about 4 seconds.
In fact, fluxcapacitor is intended for similar scenarios - to make
network protocol tests run faster. It's especially useful when
mocking a time library is not an option - just like in our memcached
example.
Redis expiration
Let's repeat the same test with redis. Again, we need:
"server" - a redis deamon
/
tmp
/
redis
-
2.6.14
/
src
/
redis
-
server
--
port
7379
"client" - as previously:
# 1) set key foo with expiry time of 60 seconds and check it
echo
-
en
"SET foo aa EX 60
\r\n
GET foo
\r\n
"
|
nc
localhost
7379
# 2) wait 70 seconds
sleep
70
# 3) is foo still there? (it shouldn't)
echo
-
en
"GET foo
\r\n
"
|
nc
localhost
7379
# 4) cleanup
killall
redis
-
server
To run it:
.
/
fluxcapacitor
--
idleness
=
1
ms
--
/
tmp
/
redis
-
2.6.14
/
src
/
redis
-
server
--
port
7379
--
bash
-
c
'
echo
-
en
"SET foo aa EX 60
\r\n
GET foo
\r\n
"
|
nc
localhost
7379
;
sleep
70
;
echo
-
en
"GET foo
\r\n
"
|
nc
localhost
7379
;
killall
redis
-
server
'
+
OK
$
2
aa
$
-
1
real
0
m1
.109
s
Wrapper scripts
I wouldn't recommend stacking very long parameters to fluxcapacitor
for any serious application. Instead, you should create a wrapper
script that spawns all the processes you need. This is a python script to run the redis
test (derived from
a fluxcapacitor example
):
#!/usr/bin/env python
import
os
,
time
,
signal
,
socket
server_pid
=
os
.
fork
()
if
server_pid
==
0
:
os
.
execv
(
"/tmp/redis-2.6.14/src/redis-server"
,
[
'redis-server'
,
'--port'
,
'7379'
])
os
.
_exit
(
0
)
else
:
time
.
sleep
(
1
)
s
=
socket
.
socket
()
s
.
connect
((
'127.0.0.1'
,
7379
))
s
.
send
(
'SET foo aa EX 60
\r\n
'
)
assert
s
.
recv
(
1024
)
==
'+OK
\r\n
'
s
.
send
(
'GET foo
\r\n
'
)
assert
s
.
recv
(
1024
)
==
'$2
\r\n
aa
\r\n
'
time
.
sleep
(
70
)
s
.
send
(
'GET foo
\r\n
'
)
assert
s
.
recv
(
1024
)
==
'$-1
\r\n
'
os
.
kill
(
server_pid
,
signal
.
SIGINT
)
Run it as usual:
$
.
/
fluxcapacitor
--
idleness
=
1
ms
--
.
/
run_redis_test
.
py
Final note
Fluxcapacitor is really good at speeding up client/server or protocol
tests.
Actually fluxcapacitor was originally created to speed up the
sockjs-protocol
test
suite. It wasn't possible to mock up a time library - we needed to run
the tests against any sockjs http server, whether it's in
erlang
,
node.js
or
python
. It turns out the
only way to run timeout-related tests in a reasonable time is to use
fluxcapacitor.
You might ask how fluxcapacitor works. In short - it uses
ptrace
to
catch syscalls like
clock_gettime
or
gettimeofday
and overwrite
the kernel response with a fake time. Additionally it short-circuits
syscalls that can block for a timeout like
select
or
poll
. For technical details
see the
README
.
