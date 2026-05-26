---
title: "A hypothetical redesign of System.Diagnostics.Process to avoid confusion over properties that are valid only when you are the one who called Start"
url: "https://devblogs.microsoft.com/oldnewthing/20260525-00/?p=112351"
fetched_at: 2026-05-26T07:14:42.770687+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# A hypothetical redesign of System.Diagnostics.Process to avoid confusion over properties that are valid only when you are the one who called Start

Source: https://devblogs.microsoft.com/oldnewthing/20260525-00/?p=112351

Some time ago, I noted that
the
Process.
Standard­Output
property is an attractive nuisance
because it is valid only on
Process
objects that you called
Start
on. You can’t just grab any old
Process
object and try to access its standard handles.
Others in the comments had their ideas on how to remove the confusion. Here’s mine. The principle is that the properties and methods of the
Process
object should be valid for all instances of the
Process
class. If a property or method is valid only conditionally, then either move it to a place that is accessible only if the condition is met, or get rid of it entirely if it adds no value.
The standard handles are the three properties that make sense only for
Process
objects that were created by the static
Start
method. There are also four methods related to those standard handles, as well as two events. Move them all to a new class, call it
Process­Start­Result
:
class ProcessStartResult
{
    public Process Process { get; }
    public System.IO.StreamWriter StandardInput { get; }
    public System.IO.StreamWriter StandardOutput { get; }
    public System.IO.StreamWriter StandardError { get; }

    public void BeginOutputReadLine();
    public void CancelOutputReadLine();
    public event DataReceivedEventHandler? OutputDataReceived;

    public void BeginErrorReadLine();
    public void CancelErrorReadLine();
    public event DataReceivedEventHandler? ErrorDataReceived;
}
Change the signature of all the overloads of the
Start
method so that they return a
Process­Start­Result
instead of a
Process
. Now it is impossible to do anything with the standard handles from a process you didn’t start: If you didn’t start the process, then you don’t have a
Process­Start­Result
. This removes the confusion that existed in the original attempt to have a process read from its own standard output.
This follows
a principle I wrote about earlier
: To force the developer to do things in a certain order, make the second step dependent on something produced by the first step. In this case, we want to force the developer to call
Start
before they use the standard handles, so we put the members related to the standard handles on a thing that you can obtain only by calling
Start
.
Next, remove the
Start­Info
property entirely. It serves two purposes:
Prior to calling the
Start
method, it provides a convenient pre-made
Process­Start­Info
.
After calling the
Start
method, it holds a copy of the parameters that you passed to the
Start
method.
The first purpose is just to cover for people who are too lazy to write the
new
keyword. So don’t be lazy. Write
new Process­Start­Info()
.
The second purpose doesn’t tell you anything you don’t already know, since you are the one who passed the parameters to the
Start
method in the first place. If they are so important to you, you can save them yourself.
Removing the
Start­Info
avoids confusion over whether the properties in it describe the process you want to start, or whether they describe a process that has already started. (And often, it describes neither!)
I think that takes care of the largest source of confusion over the proper use of the
Process
class.
