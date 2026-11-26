---
title: "Why did it seem that the entries in the CoreApplication Properties expired when the source application shut down?"
url: "https://devblogs.microsoft.com/oldnewthing/20261125-00/?p=112895/"
fetched_at: 2026-11-26T10:00:51.374888+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why did it seem that the entries in the CoreApplication Properties expired when the source application shut down?

Source: https://devblogs.microsoft.com/oldnewthing/20261125-00/?p=112895/

Last time, we confirmed that
entries in the
Core­Application.
Properties
are not tied to the lifetime of the apartment that added them
. But Luca claimed that they did. Where did this claim come from?
While it’s true that the entries don’t expire, the
objects
might expire.
If the object you put into the
Core­Application.
Properties
are not agile, then they must be used in the apartment that created them, and therefore when that apartment shuts down, the objects become unusable.
When you put a non-agile object in the
Core­Application.
Properties
, it says, “Oh no, this object is not agile. I need to create an agile wrapper for it, and put the
wrapper
in the
Properties
collection.” It has to do this because the
Properties
is a global object that can be used from any thread, so it’s possible to retrieve the object from a thread different from the one that the non-agile object belongs to.
When you retrieve the object from the
Properties
, the
Core­Application
unwraps the agile wrapper, and if you aren’t on the same thread that the wrapped object belongs to, then the COM infrastructure will create a proxy for the wrapped object. When you call methods on the proxy, the COM infrastructure switches to the object’s original thread, calls the method, and then takes the results back to the calling thread, possibly creating proxies for them if those results are themselves non-agile.
This agile wrapper is nothing special. It’s the standard agile wrapper created by
Ro­Get­Agile­Reference
function.
Here are some of the more common libraries for implementing COM objects and whether their objects are agile.
Library
Object agility
C#
Agile
C++/WinRT default
Agile
C++/WinRT +
non_agile
Non-agile
WRL default
Agile
WRL +
__WRL_CONFIGURATION_LEGACY__
Non-agile
C++/CX default
Agile
C++/CX +
[MarshalingBehavior(Standard)]
Non-agile
Handwritten
Agile if you aggregate the
free-threaded marshaler
My guess is that Luca implemented a COM object by hand, since the other libraries require you to opt out of agility explicitly, in which case the lack of agility probably would have been called out.
Okay, so now we understand how Luca came to the conclusion that entries in the
Core­Application.
Properties
are auto-removed when the source apartment shuts down: The tests were done with non-agile objects. What they observed was the
value
expiring, not the entry.
Next time, we’ll look some more at what happens when you put non-agile objects in the
Core­Application.
Properties
.
