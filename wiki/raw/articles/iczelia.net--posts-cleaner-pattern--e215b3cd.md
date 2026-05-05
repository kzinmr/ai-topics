---
title: "The Cleaner pattern - how to free native handles in Java 9?"
url: "https://iczelia.net/posts/cleaner-pattern/"
fetched_at: 2026-05-05T07:01:21.747217+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# The Cleaner pattern - how to free native handles in Java 9?

Source: https://iczelia.net/posts/cleaner-pattern/

Why not finalizers?
⌗
Until Java 9, the only reliable way to write wrappers over native objects that do not leak memory was to use the
finalize
method. The idea was quite simple: the
finalize
method was called by the garbage collector on an object when there are no more references to the object. A subclass of
Object
could override the finalize method to perform various kinds of cleanup. While this idea looks good in theory (in fact, it had initially looked so good that it made its way into Java 1.0 and stayed there for decades), it has many severe flaws. To name a few:
Finalization introduces unpredictable latency - the delay between the moment an object becomes unreachable and the moment its finalizer is called is arbitrary and unpredictable. To add, the garbage collector provides no guarantee that any finalizer will ever be called.
Finalization may invoke unpredictable behavior - the finalizer implementation may take any action. In particular, it can save a reference to the object being finalized, thereby resurrecting the object and making it reachable once again.
Finalization is always enabled - it is not possible to opt out of finalization (or, conversely, to opt into it). A class with a finalizer enables finalization for every instance of the class, whether needed or not. Finalization of an object cannot be cancelled, even if it is no longer necessary for that object, incurring a performance penalty.
Finalization invokes implementation-defined behaviour - finalizers run on unspecified threads, in a completely arbitrary order. Neither threading nor ordering can be controlled in any way.
Finalization is notoriously hard to make use of correctly - many cases of alleged finalization bugs “found” over the years are actually caused by incorrect use of finalizers.
,
.
These flaws have many crushing real-life consequences.
Security impacts - if a class has a finalizer, every new instance of that class is eligible for finalization as soon as its constructor begins to execute. If the constructor throws an exception then the new instance is not destroyed, even though it might not be completely initialized. The new instance remains eligible for finalization and its finalizer can perform arbitrary actions on the object, including resurrecting it for later use. Furthermore, it is not possible to fix this problem by just not implementing
finalize
- a subclass might implement it and gain access to improperly constructed objects.
Performance impacts - the presence of finalizers imposes a performance penalty - the garbage collectors must perform extra work when objects are created, before and after finalizing them. For example, a 7-11x slowdown when adding finalization to a class has previously been observed
. Finalization might also lead to increased pause times and/or increased data structure overhead. Some classes provide an explicit method to release resources (e.g. as in
AutoCloseable
), as well as a finalizer, just to be safe. If the user forgets to call close then the finalizer can release the resource. However, since finalizers do not support cancellation, the performance penalty is always paid, even for unnecessary finalizers for already-released resources.
Recognising these issues, two solutions have been conjectured to hopefully replace finalizers. The first one is the try-with-resources statement, which is a language-level construct that allows the user to automatically release resources when they are no longer needed. The second one is the Cleaner class, which is a new Java 9 API that allows the user to register a callback to be invoked when an object becomes unreachable. The Cleaner class is a part of the
java.lang.ref
package, which contains classes and interfaces for working with references.
In this blog post, I would like to focus on the Cleaner class, since it has proven itself to be very useful to me. The new Java 9 interface avoids some drawbacks of finalizers:
No unsafe behaviour - cleaning actions cannot access the object, so object resurrection is impossible.
Opt-in, can’t leave the class in an improperly constructed state - a constructor can register a cleaning action for a new object after the object has been fully initialized by the constructor. This means that a cleaning action never processes a partially initialized object. In addition, a program can cancel an object’s cleaning action so that the GC no longer needs to schedule the action.
How to use the Cleaner class?
⌗
To start using the Cleaner class, it is necessary to acquire an instance of it. Because every Cleaner starts a daemon thread, we want to minimise the amount of Cleaners we instantiate, so the best choice would be the singleton pattern:
The main class could be implemented following this template:
There are a few important things to point out. The
CleanerRunnable
class must be static. This is because the
Cleaner
class holds a strong reference to the
Runnable
object we pass it, so if the
Runnable
object is not constructed from a static class, it will keep a reference to the enclosing object, which is not what we want - this way, the object will never be garbage collected! Alongside the cleaner, you should also implement
AutoCloseable
(although for the API simplicity you may choose not to). The
close
method should cancel and then execute the cleaning action, so that the object is not cleaned twice:
