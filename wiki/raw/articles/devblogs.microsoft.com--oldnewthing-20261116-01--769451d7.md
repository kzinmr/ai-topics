---
title: "How can I ask a second program to show a dialog box as if it were shown by my first program?"
url: "https://devblogs.microsoft.com/oldnewthing/20261116-01/?p=112863/"
fetched_at: 2026-11-17T10:00:44.386018+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How can I ask a second program to show a dialog box as if it were shown by my first program?

Source: https://devblogs.microsoft.com/oldnewthing/20261116-01/?p=112863/

Suppose you have two programs, one a GUI program and another a program that runs in the background. The GUI program asks the background program to do some work, and then the background program realizes that it needs to display a dialog box. How do you get that dialog box to appear as if it were shown by the GUI program?
If you have the background program simply try to show a dialog box with no owner, then that dialog box has no relationship to the GUI program’s main window, which means that there is no requirement that the dialog box appear in front of the GUI program’s main window. If the GUI program didn’t disable its main window, then you have the situation where both windows (the GUI program main window and the dialog box) can be clicked on and interacted with. But if the GUI program
did
disable its main window, the fact that the main window can end up in front of the dialog box from the background program means that the user can’t see the dialog box that is preventing them from making progress.
The GUI program should include its window handle as part of the call into the background program, so that the background program can use that window handle as the owner for the dialog box. If the dialog box is modal, this also disables the GUI program’s window, and if the user tries to click on the GUI program’s window, the window manager will instead put focus on the dialog box (and blink its title bar).
Note that a cross-thread owner/owned relationship implicitly attaches the two threads’ input queues, which means that
both threads need to to remain responsive to window messages in order for things to work properly
until the attachment is implicitly broken when the dialog box is destroyed.
That’s the ideal situation, but maybe you aren’t in the ideal situation.
For example, maybe the GUI program is written in a framework that doesn’t give you access to the window handle.
You could have the GUI program call
Allow­Set­Foreground­Window()
with the process ID of the background program, so that the background program can call
Set­Foreground­Window()
on its dialog box and try to bring it to foreground.
Now, if the GUI program didn’t have foreground, then
it can’t give away a permission that it doesn’t itself possess
, and the call to
Set­Foreground­Window
will fail.
There’s not much more you can do at this point. The system doesn’t want to let random programs steal focus, and since there was no coordination with the window that
has
focus, you look like a random program as far as the system is concerned.
But really, the solution is to fix the design.
You’ve already separated the problem into a GUI process and a background process, so honor that separation: Don’t make the background process try to do UI. UI is the job of the GUI process.
If the background process wants to display UI, it can ask the GUI process to do it, and then the GUI process can send back the dialog box result. One way to do this would be to have the background process return an error code like “UI required” and information about what UI it needs. The GUI process can then display the UI, gather the answer, and then call the background process again. Another way to do it is to have the background process call back into the GUI process when it needs UI, and the GUI process displays the UI, gathers the answer, and returns it to the background process. There are pros and cons to both of these designs, so you can choose the one that works best for you.
