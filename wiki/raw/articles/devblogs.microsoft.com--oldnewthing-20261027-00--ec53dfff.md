---
title: "Why don't we run the taskbar and Task Manager at high priority, so they can remain responsive?"
url: "https://devblogs.microsoft.com/oldnewthing/20261027-00/?p=112800/"
fetched_at: 2026-10-28T10:01:26.449981+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why don't we run the taskbar and Task Manager at high priority, so they can remain responsive?

Source: https://devblogs.microsoft.com/oldnewthing/20261027-00/?p=112800/

If a system becomes CPU-starved, all processes begin to suffer. This includes the taskbar and Task Manager, even though they are often the tools you want to use to stop whatever it is that’s making your system suffer. Why can’t we run the taskbar and Task Manager at high priority?
The catch with running anything at high priority is that unless you have been very careful to avoid it, you will eventually run into a shared resource that you will have to wait for, and you are now stuck. Your priority checkout pass gets you to the front of the line, but if the person at the register has a large shopping cart full of groceries, you just have to wait until they are done before you get your chance.
Even if the code that protects the shared resource is careful to avoid priority inversion by transferring the priority of the waiter to the thread that owns the resource, you are still stuck waiting, and that owning thread might be doing something that takes a long time, like, say, accessing a file over the network.
For UI code, this problem is particularly acute because you will eventually have to call into the UI system, and now you’re duking it out with all the other UI threads in the system.
The problem is that it’s hard to fix a runaway system from within that same system. The tools which you can use to try to fix the system may already have been compromised. And it’s definitely hard to fix a runaway system if your tools have to share critical resources with the thing that is out of control.
Windows already gives preferential treatment to the program that is in focus
, so if you can get focus onto the taskbar or Task Manager, you are doing about as well as you can. But that preferential treatment takes you only so far if those preferred threads find themselves blocked on things that are controlled by non-preferred threads.
