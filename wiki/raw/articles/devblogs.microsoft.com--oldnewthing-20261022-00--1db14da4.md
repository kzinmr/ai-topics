---
title: "Why didn't we use Co­Register­Initialize­Spy to clean up the unmarshalable delegate?"
url: "https://devblogs.microsoft.com/oldnewthing/20261022-00/?p=112791/"
fetched_at: 2026-10-24T10:00:50.208549+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why didn't we use Co­Register­Initialize­Spy to clean up the unmarshalable delegate?

Source: https://devblogs.microsoft.com/oldnewthing/20261022-00/?p=112791/

Another suggestion from Luca Bacci on
creating a fake agile wrapper that is technically agile but is not useful outside its home apartment
was to
use the
IInitialize­Spy
interface
.
Some of the thing that made The
Ro­Register­For­Apartment­Shutdown
unsuitable also apply to
Co­Register­Initialize­Spy
. For example, you are required to revoke the spy from the same thread that registered it, which means that we have to remember the original thread so we can somehow get back to executing code on it.
Another problem is explicitly noted in the documentation for
Co­Revoke­Initialize­Spy
:
It is unpredictable whether a call to
Co­Revoke­Initialize­Spy
from within an IInitialize­Spy method call will have an effect during the current top-level (non-nested) call to Co­InitializeEx or Co­Uninitialize.
This is the same problem we had with
Ro­Unregister­For­Apartment­Shutdown
function, in the case where the original object’s destruction in turn triggers an attempt to revoke an initialize spy: It revokes the spy, thinking that this will stop the callbacks, but in fact, the callback might still happen.
It also suffers from the same implementation issue regarding the number of initialize spies: Registration is
O
(1), but unregistration is
O
(
n
) because it does a linear search through a linked list. The assumption is that initialize spies are rarely unregistered before they are triggered.
But there’s an even bigger problem that makes this completely unsuitable for using an initialize spy to clean up an object at apartment shutdown, and maybe you noticed it in the earlier discussion.
Initialize spies are registered on a
per-thread
basis, not per-apartment.
If the original object is in the multi-threaded apartment, then it’s wrong to give up the object once the original thread uninitializes COM, because it might still be kept alive by another thread.
Also, a thread may change apartments over time. For example, if you are not in the neutral apartment and you call into an object that
is
in the neutral apartment, then there is no thread switch. COM merely removes your thread temporarily from whatever apartment it is in and puts the thread into the neutral apartment for the duration of the call.
Now, if the thread had previously belonged to a single-threaded apartment, and somebody makes a call into an object on that single-threaded apartment, COM may temporarily remove that thread from the neutral apartment and put it back into the original single-threaded apartment for the duration of that call.
A thread may move between apartments during its lifetime, but the
IInitialize­Spy
is tied to the thread, not to the apartment.
This means that if the non-marshalable object happens to live in, say, the neutral apartment, you would be given that object in the neutral apartment, and you would register your
IInitialize­Spy
against the
thread
that is currently running. When that thread uninitializes COM as a single-threaded apartment, your
Pre­Uninitialize
would be running in that dying single-threaded apartment, but it can’t clean up the object because the object is in the neutral apartment, not the single-threaded apartment.
So yeah,
IInitialize­Spy
doesn’t really help.
