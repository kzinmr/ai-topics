---
title: "The two kinds of error"
url: "https://evanhahn.com/the-two-kinds-of-error/"
fetched_at: 2026-04-29T07:02:20.020276+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# The two kinds of error

Source: https://evanhahn.com/the-two-kinds-of-error/

In short: in my mind, errors are divided into two categories. Expected errors (think “user entered invalid data”), which are part of normal operation, aren’t the developer’s fault, and should be handled. Unexpected errors (think “null pointer exception”) are the developer’s fault, likely indicate a bug, and are allowed to crash.
Error handling is an important, but often neglected, part of programming and user experience.
Over the years, I’ve developed an opinion about the two types of error in software. This is primarily informed by a career in web and application development, but I hope these learnings are widely applicable.
In my mind, errors are divided into two categories:
expected
and
unexpected
.
Expected errors
Expected errors happen during normal operation. Examples:
Validation errors when the user enters invalid data. You can’t control what the user types!
Network errors when the user’s network fails. It’s not your fault if the user turns their Internet off or has a slow connection!
Permission errors when your program isn’t allowed to do something. You can’t magically read forbidden files, fix a user’s password, or steal webcam privileges!
The developer hasn’t made a mistake when these happen, and there’s often little they can do to prevent it. The existence of these errors is not a bug (though failing to handle them can be). These aren’t the programmer’s fault.
Expected errors are recoverable. This might mean logging a warning, showing a message to the user, or using a fallback.
Expected errors should not
throw
,
raise
, or
panic
. Instead, they should return an error result. This works differently in every language, but is often a
Result
type, a union of
null
and the success value, or an error code. This pattern pushes you toward handling the error, which you should if you want to make your software reliable.
Expected errors should use
WARN
or
INFO
log messages because this isn’t a problem to solve. You may want to set up an alert if you start getting
lots
of warnings.
Unexpected errors
Unexpected errors should never happen. If they do, you’ve got a bug! Examples:
Assertion errors. For example, a function
must
be called with a non-empty string, and someone violated the contract if they didn’t.
Logic errors. If Thing A depends on Thing B, but Thing B isn’t properly initialized, that’s unexpected. Null pointer exceptions are also typically a surprise.
Invalid data errors. You can usually assume your database will give back valid data. If it doesn’t, you’ve probably got a bug somewhere.
You should generally not try to recover these errors. It’s okay to explode—crash,
panic
, and
throw
.
To get even more radical: I often think unexpected errors should
completely crash the program
. It’s disruptive in the short term, but I find crashes make software feel
more
reliable in the long run. You’re more likely to hear about these problems from annoyed users—if not your own testing.
Unexpected errors should use
ERROR
or
FATAL
log messages because they indicate a real problem. At best, they indicate an incorrect assumption. At worst, there’s a serious bug somewhere.
Drawing the line
The line between “expected” and “unexpected” depends on the task.
At one extreme: if you’re making a prototype or quick script, I reckon
all
errors are unexpected. You might decide not to handle problems with the network, filesystem, or user input. Who cares? This is just a little script or idea.
At the other extreme: if you’re coding for a space probe on a 50-year mission, almost
all
errors are expected,
including catastrophic hardware failures
.
Most programs lie somewhere in between, and you have to decide which errors are unexpected. For example, are memory allocation errors expected in your program? It depends.
In my experience, if you want to make your stuff more reliable, you’ll trend toward expecting more and more errors. Lots can go wrong on a normal day! For example, my team recently had to deal with a memory allocation error, even though we’re writing a Node.js app.
Some programming languages, like Rust and Zig, classify many errors as expected. Others, like JavaScript and Python, classify them as unexpected. For example, when you parse JSON in Go, the compiler makes you handle the error; not so in Ruby. I tend to prefer stricter compilers for production software and looser languages for scripts and prototypes, in part because of their philosophy about errors. (The Rustaceans among you probably notice that this whole post is very similar to
Rust’s error philosophy
.)
To be clear: this is just what
I
think. I’ve found it useful to categorize errors this way. If you think about errors differently, (1)
I’d love to hear it
(2) I’m glad you’re thinking about error handling in software.
See a response to this post,
“The three kinds of error”
.
