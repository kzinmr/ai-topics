---
title: "Creating a fake agile wrapper that is technically agile but is not useful outside its home apartment, part 1"
url: "https://devblogs.microsoft.com/oldnewthing/20260803-00/?p=112582"
fetched_at: 2026-08-04T10:18:16.112707+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Creating a fake agile wrapper that is technically agile but is not useful outside its home apartment, part 1

Source: https://devblogs.microsoft.com/oldnewthing/20260803-00/?p=112582

Last time,
we considered what it means when the context callback fails
, which prevents us from releasing the object in its original context. We noted that the problem is that when the original apartment tears down, we lose our chance to release the object.
What we want is something between a strong reference and a weak reference. We want a reference that is strong, but which releases its reference to the destination when the originating apartment tears down.
Is there such a thing?
It turns out that there is.
What we can do is register the object in the global interface table (historically known as the GIT, unrelated to the source control system). The usual reason for doing this is to allow the object to be accessed from another apartment by redeeming the registration cookie. We have no intention of accessing the object from another apartment, but we do this to take advantage of a feature of the GIT: References in the GIT are automatically released when the object’s apartment shuts down. The registration cookie remains valid, but if you try to redeem it, you are told that the server is no longer available.
So the idea here to register the original delegate in the GIT and save it in the agile wrapper. The agile wrapper then unregisters the delegate on destruction. We never redeem the registration cookie. The purpose of registering the delegate was not to access it from another apartment, but just to auto-release it when the original apartment tears down.
So let’s try it.
Next time.
