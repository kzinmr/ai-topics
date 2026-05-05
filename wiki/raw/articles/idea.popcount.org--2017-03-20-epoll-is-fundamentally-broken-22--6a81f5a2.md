---
title: "Epoll is fundamentally broken 2/2"
url: "https://idea.popcount.org/2017-03-20-epoll-is-fundamentally-broken-22"
fetched_at: 2026-05-05T07:01:10.144794+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Epoll is fundamentally broken 2/2

Source: https://idea.popcount.org/2017-03-20-epoll-is-fundamentally-broken-22

Epoll is fundamentally broken 2/2
I/O multiplexing part #4
20 March 2017
Previous articles in this series:
The history of the Select(2) syscall
Select(2) is fundamentally broken
Epoll(2) is fundamentally broken
In this post we'll discuss the second argument on why the
epoll()
is broken. The problem is best described
in an LWN comment by Foom
:
And epoll certainly has a
HUGE
misdesign in it, that anyone who
actually understood what a file descriptor is should've seen
coming. But if you look back in the history of epoll, you'll see
that it looks like the implementors apparently didn't understand the
difference between file descriptors and file descriptions. :(
epoll
is broken because it mistakes the "file descriptor" with the
underlying kernel object (the "file description"). The issue shows up
when relying on the
close()
semantics to clean up the epoll
subscriptions.
epoll_ctl(EPOLL_CTL_ADD)
doesn't actually register a file
descriptor. Instead it registers a tuple
1
of a file descriptor
and a pointer to underlying kernel object. Most confusingly the
lifetime of an epoll subscription is not tied to the lifetime of a
file descriptor. It's tied to the life of the kernel object.
Due to this implementation quirk calling
close()
on a file
descriptor might or might not trigger epoll unsubscription. If the
close
call removes the last pointer to kernel object and causes the
object to be freed, then it will cause epoll subscription cleanup. But
if there are more pointers to kernel object, more file descriptors, in
any process on the system, then
close
will not cause the epoll
subscription cleanup. It is totally possible to receive events on
previously closed file descriptors.
dup() as example
The simplest way to show the problem is with
dup()
.
Here's the code
:
rfd
,
wfd
=
pipe
()
write
(
wfd
,
"a"
)
# Make the "rfd" readable
epfd
=
epoll_create
()
epoll_ctl
(
efpd
,
EPOLL_CTL_ADD
,
rfd
,
(
EPOLLIN
,
rfd
))
rfd2
=
dup
(
rfd
)
close
(
rfd
)
r
=
epoll_wait
(
epfd
,
-
1
ms
)
# What will happen?
You may think: the
epoll_wait
will block forever, since the only
registered file descriptor "rfd" was closed. But that's not what will
happen. By calling
dup
, we kept the reference to the underlying
"rfd" kernel object, we prevented it from being cleaned up.  The
thing is still subscribed to the epoll.
epoll_wait
will in fact
terminate reporting an event on a dead handle "rfd".
To make matters worse, you need a valid file descriptor handle to
manage subscriptions on "epfd". After we called
close(rfd)
, there is no way to unregister it from epfd!
Neither of these will work:
epoll_ctl
(
efpd
,
EPOLL_CTL_DEL
,
rfd
)
epoll_ctl
(
efpd
,
EPOLL_CTL_DEL
,
rfd2
)
Marc Lehmann phrased
it well:
Thus it is possible to close an fd, and afterwards forever
receive events for it, and you can't do anything about that.
You can't rely on
close
to clean up epoll subscriptions.  If you
ever called
close
in such bad corner case, you can't fix the
"epfd". The only way froward is to trash the old "epfd", create new
one and recreate all the valid subscriptions.
Remember this advice:
You always must always explicitly call
epoll_ctl(EPOLL_CTL_DEL)
before
calling
close()
.
Summary
Explicitly deregistering file descriptors before
close
is nescesary
and works well if you control all the code. In some cases though it
may not be possible - for example when writing an epoll wrapper
library. Sometimes it's impossible to forbid users from calling
close
themselves. For this reason it's
hard to build correct thin
abstraction layers
on top of epoll.
Hopefully this and
the previous
blog
posts on
epoll()
had shedded some light on the dark corners of the
Linux epoll implementation. I can only wonder how closely Microsoft
recreated these quirks in the
Windows Subsystem for Linux
.
Update:
Illumos
has a custom
epoll
implementation as well. In the
man page
they explicitly mention the
close
weirdness and refuse to support
Linux's broken semantics.
