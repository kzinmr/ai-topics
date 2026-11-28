---
title: "Could we use the CoreApplication Properties to manage the lifetime of an object that refuses to be marshaled?"
url: "https://devblogs.microsoft.com/oldnewthing/20261127-00/?p=112901/"
fetched_at: 2026-11-28T10:00:45.154373+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Could we use the CoreApplication Properties to manage the lifetime of an object that refuses to be marshaled?

Source: https://devblogs.microsoft.com/oldnewthing/20261127-00/?p=112901/

We’ve been looking at why it seems like the
Core­Application.
Properties
frees objects when their source apartment shuts down, and why that is just a mirage.
But this was all in the context of figuring out how to create a fake agile reference to an object that refuses to be marshaled, so let’s see if any of this helps us.
If you have an object that refuses to be marshaled (by implementing
INoMarshal
), then we learned that
the
Ro­Get­Agile­Reference
function cannot create an agile reference to it
. And since the
Core­Application.
Properties
uses
Ro­Get­Agile­Reference
to store non-agile objects, trying to store such an object in the
Core­Application.
Properties
fails with
CO_
E_
NOT_
SUPPORTED
.
So you’re back to square one: You have a non-marshalable object, so how do you create an agile reference to it, while still honoring the promise not to use the object from another apartment?
We can proceed with the same solution: Put the non-marshable object inside a marshalable object, and then use the marshalable wrapper.
The original solution merely carried the marshalable object around and used it to access the non-marshalable object. I guess we could instead store it in the
Core­Application.
Properties
under a newly-generated key, and then remember the key. When it’s time to invoke the delegate, we go back to
Core­Application.
Properties
, look up the key, get the wrapper, and then use it to access the original non-marshalable object. And at destruction, we delete the entry from the
Core­Application.
Properties
.
I mean, I guess you could do that, but it seems like an awful lot of unnecessary work. You have to remember
something
, either the marshalable wrapper or the key to the marshalable wrapper. May as well just remember the marshalable wrapper itself to avoid unnecessary complexity. The
Core­Application.
Properties
is not adding any value.
