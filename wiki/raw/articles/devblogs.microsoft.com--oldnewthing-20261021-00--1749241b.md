---
title: "Why didn't we use Ro­Register­For­Apartment­Shutdown to clean up the unmarshalable delegate?"
url: "https://devblogs.microsoft.com/oldnewthing/20261021-00/?p=112786/"
fetched_at: 2026-10-22T10:01:03.806024+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why didn't we use Ro­Register­For­Apartment­Shutdown to clean up the unmarshalable delegate?

Source: https://devblogs.microsoft.com/oldnewthing/20261021-00/?p=112786/

In my attempt to
create a fake agile wrapper that is technically agile but is not useful outside its home apartment
,
Luca Bacci suggested, among other things
, using the
Ro­Register­For­Apartment­Shutdown
function.
The
Ro­Register­For­Apartment­Shutdown
function is nice, but it doesn’t suit our needs.
One problem is that the object registered for apartment shutdown must be agile. (If you pass a non-agile object, the call fails.) That means that our wrapper must be agile. If we put the non-marshalable non-agile object inside our wrapper, we now have an agile object (the wrapper) that holds a non-agile object (the original object) as a member, which creates the risk that the wrapper will run down in the wrong apartment. The normal way of fixing that is to use
Ro­Get­Agile­Reference
to create an agile wrapper around the non-agile object, and store that agile wrapper in our container object.
This puts us back where we started: We are trying to implement that agile wrapper!
Even if we got past that problem, we have another problem: At apartment shutdown, COM calls the wrapper object’s
UnInitialize
method, and there’s a warning on the using the
Ro­Unregister­For­Apartment­Shutdown
function:
Warning
: Don’t call the
Ro­Unregister­For­Apartment­Shutdown
function from the
OnUninitialize
callback.
But wait, what if the destructor of the object we are wrapping wants to call
Ro­Unregister­For­Apartment­Shutdown
? It might happen indirectly because it has its own reference to another object, that in turn tries to call
Ro­Unregister­For­Apartment­Shutdown
.
For example, it might hold another fake agile wrapper whose
UnInitialize
method has already been called! (We can work around that in our agile wrapper by nulling out the non-agile pointer so we don’t double-release, but maybe there’s some other object that uses
Ro­Unregister­For­Apartment­Shutdown
that is less resilient to this scenario.)
Another requirement of
Ro­Unregister­For­Apartment­Shutdown
is that it must be called from the same apartment that registered. This doesn’t quite put us back where we started, but it makes things more complicated because the whole point of the exercise is to find a way to release the object without having to try to switch to the apartment. I guess what we could do is use
IContext­Callback
to try to switch back to the apartment to release the original object and unregister the apartment shutdown callback. If the apartment switch fails, then we assume it’s because the apartment has already run down, so we assume that the
IApartment­Shutdown::
On­Uninitialize
method was called, and it released the object for us. (Of course, that still creates the problem that we are cleaning up inside the
On­Uninitialize
callback, which meas that nobody else can unregister their apartment shutdown callback.)
The last note on this is that the implementation is written on the assumption that there are not a lot of apartment shutdown callbacks. Registration is
O
(1), but unregistration is
O
(
n
) because it does a linear search through all of the apartment’s registered shutdown callbacks to find the one being unregistered. By comparison, the Global Interface Table is designed on the assumption that it will have to manage a lot of objects, so it can look up its cookies in
O
(1) time. The proposed alternate design would register and unregister a lot of apartment shutdown callbacks, so it’s pushing the apartment shutdown callback list into a usage pattern it wasn’t optimized for.
