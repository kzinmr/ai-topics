---
title: "How to read error messages"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/errmsg/"
fetched_at: 2026-04-25T12:06:10.119958+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# How to read error messages

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/errmsg/

How to read error messages
[Simon Tatham, 2023-07-06]
Computers give a lot of error messages. They’re often
      misleading, or ambiguous, or difficult to understand. So it’s
      often tempting not to really try: to ignore all
      the
details
mentioned in the error message, and focus
      only on the plain fact that
it’s an error!
But there’s a lot of juice to be squeezed out of error messages
      if you know what to look for. It’s worth learning the skill of
      extracting all the detailed information you can. That gives you a
      head start on debugging problems yourself,
and
a better
      chance of writing a good bug report for somebody else – and
      perhaps even a better chance of deciding which of those things
      to do.
In this article, I’ll try to give an overview of the kind of
      things you can tell from the details of an error message – right
      down to things as trivial as the punctuation.
Disclaimer
: this article is adapted from a
      talk I gave to my colleagues in 2022. So it reads a little more
      like somebody ranting out loud than my usual writings. Also, its
      original target audience was about 30 very specific people. But
      I hope it’s useful to other people too!
Introduction
When a computer prints an error message, what’s it telling you?
Most obviously, it’s saying:
there was an error
. That
        is,
something went wrong
. In other
        words,
whatever I just tried to do didn’t work
.
Just occasionally, that really is the
only
thing that
      the message communicates. One embedded device I
      own
literally
prints a chirpy dialog box saying
      ‘Something went wrong! [OK]’, and that’s all you can ever find
      out about the problem.
But usually a program will at least
try
to tell you
      more detail than that:
It might tell you
what
it was trying to do
        that went wrong.
It will often say something more specific about
what
          happened when it tried
– in other words, not just
        what
didn’t
happen, but what
did
happen
        instead.
Failing that, if the thing it was trying to do involves more
        than one step, it might at least tell you
which
step
        had a problem.
It might mention
who
was trying to do that thing in
        the first place. In a situation involving many cooperating
        programs, your first problem can sometimes be figuring out
        which of them an error came from. So if the failing program
        identifies itself in the error message, that’s a useful clue
        already.
If you’re
especially
lucky, the error message might
        even say something about
why
the program was trying to do
        the thing that went wrong!
Any or all of this information can help narrow down what the
      problem is, and what to do about it. But I’ve often seen people
      – even technically competent ones – apparently
      just
ignore
all the helpful details in the error
      message, and try to solve the problem without them. It’s as if
      they thought that would be an extra challenge. Or as if they
      hadn’t even
noticed
that the error message said
      anything more specific than ‘Something went wrong!’
Try not to do that. It only makes your own life harder. It
      really is worth reading the error message in detail, and
      understanding as much as you can about it.
If you’re trying to solve the problem yourself, this can often
      save you from wasting an hour pursuing a wrong idea of what the
      problem is. For example, by spotting immediately that
      if
that
had been the problem then you’d have expected a
      different error message.
Even if your plan is to report the problem to someone else, it
      can still be worth understanding something about the error
      message, because it gives you hints about what other things you
      should mention in your report. (For example, if the error
      message said ‘no such file’, it’s probably helpful to mention
what
file might be involved, if you can possibly find
      out.)
In particular, if you have a long log file (say, from a CI job)
      containing multiple errors, an understanding of what they mean
      will help you decide whether
this
particular error
      message is the useful one, or whether you should instead look
      further up or down in the log for a more relevant message from
      another subprogram.
Even better, if you can recognise the error as one that
      indicates a
temporary
problem, you may be able to avoid
      having to do anything at all!
Scope and structure
This article is divided into two main sections:
facts
and
advice
. In the facts section, I’ll discuss some
      general principles of what kinds of errors exist, how programs
      typically report them, and what some specific messages mean. In
      the advice section, I’ll apply that knowledge to give some
      recommendations about
what to do
about various kinds of
      message, such as where (or whether) to look for more
      information.
This article will focus mostly on
general-purpose
error messages: the kinds of error that
lots
of
      different programs are likely to have to report. In particular,
      I’ll discuss errors reported by operating systems (both Unix and
      Windows) when a program tries to interact with them to
      manipulate files or directories or processes: ‘I tried to open
      this file, or run that program, and something went wrong.’ I’ll
      also discuss networking errors in particular, because these
      days, more or less
everything
involves networking.
But I won’t go into detail about the error messages generated
      by any
particular program
. Often those can be
      complicated in their own right. In particular, untangling
      complicated
compiler
errors could easily fill a whole
      separate article!
Even for the general error messages I’ll be discussing, I won’t
      have time or space to describe absolutely everything you’ll need
      to know. I only have room here to give a general idea of how
      things are, suggest what kinds of thing to look out for, and
      recommend you start keeping notes of your own. So this article
      won’t teach you all by itself to be an expert
      error-message-ologist. But it might show you how to start
      building up the experience to turn yourself into one.
Facts
In this section I’ll discuss some typical kinds of error
      condition that often happen, and the general conventions for
      reporting them to the user, so you know what general shape of
      message to expect in this kind of situation.
I’ll cover three main categories:
Errors reported by a program from particular operating
        system interactions
Conditions reported by a parent program after a subprogram
        terminates
Kinds of thing that can go wrong with networking in
        particular.
OS error numbers on Unix
When a Unix process interacts with the operating system,
      failures are usually reported using a system of numeric codes.
      These are referred to as
errno
values (after
      the name of the variable that the error code is left in).
Each
errno
value has a symbolic name inside the
      program, always in capitals and beginning with ‘
E
’,
      such as
ENOENT
. There’s a standard system function
      (‘
strerror
’) which translates each one into a short
      phrase intended to be printed to the user. Most simple Unix
      programs will print that string as part of their error messages,
      so it’s worth recognising the common ones and knowing what they
      mean.
There isn’t enough space here to list all
      the
errno
values, but here are some of the most
      important:
ENOENT
, translated as ‘No such file or
        directory’, means that you – or rather, whichever program
        received this error – tried to access a file or directory that
        simply did not exist at all.
EISDIR
, translated as ‘Is a directory’, means
        you tried to do a file-like operation to a directory, such as
        deleting it using
rm
instead
        of
rmdir
, or trying to write data to it.
ENOTDIR
, translated as ‘Not a directory’, means
        the opposite: you tried to do a directory-like operation to a
        file, such as looking up a file inside it, or trying
        to
cd
into it.
EACCES
, translated as ‘Permission denied’,
        means that some file or directory you tried to
        access
exists
, but the Unix permission bits mean
        that
you
are not allowed to access it. Some other
        user on the same system probably can. In particular,
        the
root
user can almost certainly access the
        file.
EPERM
, translated as ‘Operation not permitted’,
        is confusingly similar to
EACCES
, and also means
        that you tried to do something that your particular user id
        doesn’t have permission to do. But
EACCES
is
        about the permissions on files or directories,
        and
EPERM
is about
everything else
: all
        the
other
situations in which ‘you need to
        be
root
to do that’, such as configuring a
        network interface, or killing another user’s process.
Unfortunately, a typical file access operation only reports
      failure in the form of a single code of this type. That doesn’t
      always tell you everything you needed. In particular, if you
      tried to access a file via a path of more than one subdirectory,
      like
foo/bar/baz/quux.txt
, then the error code
      might refer to any of the steps on that path, and nothing will
      tell you which.
ENOENT
might happen because the
      actual file
quux.txt
is missing, or because the
      directory
foo
didn’t exist in the first place, or
      anything in between.
EACCES
might happen because
      you don’t have the right to read
quux.txt
in
      particular – or because you don’t even have the right to look
      inside the containing directory to find out
whether
a
      file of that name exists.
An even more annoying example is that if you’re trying
      to
rename
a file, the error code might refer to the
      source or the destination, and won’t tell you which! For
      example, if ‘
mv foo.txt baz/quux.txt
’ reports ‘No
      such file or directory’, that might mean that the
      file
foo.txt
doesn’t exist to be moved
      anywhere,
or
that the directory
baz
doesn’t exist for you to move it into.
(An even more
confusing
case is that you can
      get
ENOENT
even when you’re trying
      to
create
a file! Your instinct is to think “Of course
      it doesn’t already exist, that’s
why
I’m trying to
      create it.” But
ENOENT
can occur if
      the
directory you’re trying to create it in
doesn’t
      exist.)
So, if you see an error message like this, the first thing to
      be aware of is that it might mean more than one detailed thing.
      If you need to know which step on a directory path is the
      problem, or whether an error referred to the source or
      destination file, you’ll have to poke around
      yourself
after
receiving the error report.
Several error codes in this system have confusing or unclear
      symbolic names, or translations, or both. For example, even the
      ‘ent’ in
ENOENT
isn’t completely obvious. (It’s
      meant to indicate that there was no
entry
in the
      containing directory with the name you specified.)
It’s confusing that
EACCES
goes with the phrase
      ‘Permission denied’ and not ‘Access denied’ – if you know that
      there are things called both
EACCES
and
EPERM
, you might reasonably expect the word
      ‘permission’ in the translation to indicate that the error code
      was
EPERM
! But no,
both
messages use the
      word ‘permission’ or ‘permitted’, and you have to spot the
      difference between the detailed wordings ‘Permission denied’ and
      ‘Operation not permitted’.
Some of these messages and their translations are very vague,
      when they could and should be much more specific. For example,
      if you see
EKEYEXPIRED
/ ‘Key has expired’ when
      trying to access a file, then the ‘key’ in question almost
      certainly refers to a Kerberos ticket – so you’d only expect to
      see it if your organisation is using Kerberos at all.
      It
doesn’t
refer to any kind of key that an application
      program might have been dealing with on purpose, such as an SSH
      key (or a key on the keyboard).
(This is particularly confusing if you get ‘Key has expired’
      when you were
trying
to do something with an SSH key!
      In that situation the SSH key itself is probably fine – or, at
      least, you have no evidence otherwise right now – but your
      Kerberos setup is currently too confused for SSH to find
      it.)
A few
errno
messages are outright misleading. For
      example,
ETXTBSY
/ ‘Text file busy’ has nothing to
      do with what ordinary people think of as a text file. It means
      that an
executable
file was already being run when a
      program tried to write to it, or was in the middle of being
      written when something tried to run it.
(And even that is only
slightly
strange compared to
      the notorious historical message ‘Not a typewriter’, which has
      had nothing to do with typewriters for decades! Linux at least
      has now reworded this as ‘Inappropriate ioctl for device’, which
      is at least
accurate
, though still not especially
      helpful. But its symbolic code is still
ENOTTY
,
      because those are harder to change.)
I won’t try to write a
complete
list of all the
      subtleties of the Unix error code system, or all the situations
      in which one of these errors can occur at a surprising moment.
      That would take too much space, too much time, and I’d surely
      get half of it wrong myself. So all I can say is: be aware in
      general that this kind of confusion
exists
, and as you
      gain experience, build up your own list of things that can catch
      you out. Everyone’s list will be different!
OS error reporting conventions on Unix
When a Unix command-line tool reports an operating system
      error, the message will
ideally
include four pieces of
      information. If you’re lucky, you can hope to see:
the program name (which is useful information if the program
        is one subprocess of a longer shell script)
some kind of object being operated on (e.g. a file, or a
        network host name)
what operation the program was attempting to perform on that
        object
the text translation of the
errno
code,
      indicating in what way that operation did not succeed.
Here are a couple of examples:
$ ls /root
ls: cannot open directory '/root': Permission denied
The program has printed its own name: ‘
ls
’. It
      says what it was trying to operate on: the
      directory
/root
. It says what it was trying to do
      to that directory: open it (in order to start reading a list of
      filenames out of it, which is
ls
’s job). And it
      shows that that operation failed with the
errno
value
EACCES
: the file permission bits on the
      directory
/root
are set so that this user does not
      have the rights to list its contents. (Not surprisingly, because
      it’s the root user’s home directory, and this command was run by
      an unprivileged user.)
$ ssh wibble.example.com
ssh: Could not resolve hostname wibble.example.com: Name or service not known
In this example, the program has printed its name,
      ‘
ssh
’; it’s trying to operate on the network host
      name ‘
wibble.example.com
’; what it’s trying to do
      is to
resolve
that name (which means translating it
      into a numeric IP address that it would then have tried to make
      a connection to). And the error
      translation
is ‘Name or service not known’, which means that hostname
      doesn’t exist at all. (Again, not surprisingly, because I just
      made it up.)
However, you’re not always as lucky as that. Many programs
      forget to print at least one of these pieces of information.
      Sometimes this is pure laziness (the program’s error reporting
      code was written in a hurry, and there isn’t enough internal
      ‘plumbing’ inside the program to get all the right pieces of
      information to the place where the error message is
      constructed). Often it’s because the programmer used a standard
      system library function called
perror
to report the
      error, which prints text of your choice followed by the
      translation of the
errno
value, but makes it
      outright
difficult
to get all three of the other useful
      components into the prefix text.
One thing that you almost
never
find out from this
      type of error message is
why
the program was trying to
      do that operation to that object! In the cases I’ve shown above,
      it’s pretty obvious, but sometimes that can be the biggest
      mystery. I’ll come back to that theme in the advice section.
OS error numbers on Windows
Windows has a similar system to Unix of error numbers with
      symbolic names and text translations. Generally both the names and
      the descriptions are a bit more verbose than Unix.
Here’s a link to MS’s documentation
      of
the
      full list of error codes
. They’re divided into a few
      sub-pages according to their numeric values, so it may help to
      know that most of the common errors relating to processes and
      files are likely to have small numbers and can be found in
      the
0–499
      subpage
. On the other hand, networking errors mostly have
      values just above 10,000, so those are likely to be in
      the
9000–11999
      subpage
.
Here are some typical examples of Windows error codes and their
      translations:
ERROR_FILE_NOT_FOUND
= ‘The system cannot find the file specified.’
ERROR_PATH_NOT_FOUND
= ‘The system cannot find the path specified.’
ERROR_ACCESS_DENIED
= ‘Access is denied.’
ERROR_OPEN_FAILED
= ‘The system cannot open the device or file specified.’
ERROR_DIRECTORY
= ‘The directory name is invalid.’
ERROR_SHARING_VIOLATION
= ‘The process cannot access the file because it is being used by another process.’
Unfortunately, just like the Unix error code system, some of
      the Windows codes are also confusing, or vague, or hard to make
      sense of, or you don’t get the one you’d expect in a particular
      situation. In particular, although Windows has
more
of
      these codes than Unix, and typically puts more words in the
      translations, that doesn’t mean you get more useful information:
      the messages are often surprisingly non-specific, and the same
      code can be reused for things you’d like to be able to tell
      apart.
For example, you get
ERROR_ACCESS_DENIED
if you
      try to read a file you’re not allowed to open – but
      you
also
get it if you attempt a file-like operation on
      a directory. (Unix would have told you the difference,
      with
EACCES
versus
EISDIR
.)
If you attempt a directory-like operation on a file (such as
      trying to
cd
into it),
ERROR_DIRECTORY
seems to be the error code you get. So ‘the directory name is
      invalid’ should be taken to mean ‘there is
something
of
      that name, but it’s not a directory’. If you try
      to
cd
into a directory that doesn’t exist at all,
      you get
ERROR_PATH_NOT_FOUND
.
(On the other hand, this means Windows has separate codes for
      a
file
not existing and a
directory
not
      existing, namely
ERROR_FILE_NOT_FOUND
and
ERROR_PATH_NOT_FOUND
, where Unix
      uses
ENOENT
for both.)
ERROR_OPEN_FAILED
is especially odd. It tells you
      Windows couldn’t open something, but not
why not
. If
      the file wasn’t there, or you didn’t have permission to read it,
      you’d expect a more specific code
      like
ERROR_FILE_NOT_FOUND
or
ERROR_ACCESS_DENIED
. So what kind of
      failure
might
cause
ERROR_OPEN_FAILED
?
      Apparently it can happen when a virus scanner interferes with
      opening the file in some way – but the error is so vague that
      you’d never have guessed that just from the text.
OS error reporting conventions on Windows
Unfortunately, Windows doesn’t have Unix’s strong convention to
      report a few useful pieces of information along with the error
      code. A common behaviour of a Windows command-line tool is
      to
just
print the text translation of the error code,
      without any other information:
C:\Users\User>type wibble.txt
The system cannot find the file specified.
C:\Users\User>reg query HKCU\Software\Nonexistent\Thingy
ERROR: The system was unable to find the specified registry key or value.
This is particularly awkward if a long batch script is running
      lots of subcommands in sequence, because you don’t even get to
      find out which one failed. Suppose your batch file runs, and
      something prints ‘The process cannot access the file because it
      is being used by another process’. Not only do you have no idea
      what file couldn’t be accessed – you don’t even know
      which
process
failed to access
      it!
2
I wish I could give some advice for getting round this problem,
      and actually finding out which program gave an error on Windows.
      But the best I can say is:
be aware
that this is a
      problem, and keep your mind open to the possibility that the
      program giving the error might not be the same one it looks as
      if it is.
Process exit statuses on Unix
When one Unix program runs another, and the child process
      terminates, its parent receives some information about whether
      things went well. It’s useful to know how this works, so you can
      interpret the things the parent program might print
      afterwards.
On Unix, a parent process can find out which of these two
      things happened to a child that has stopped running:
It exited on purpose, returning a
status code
It terminated because it received a particular
signal
.
The status code returned by a terminating program must fit in
      an 8-bit integer; that is, their possible values are between 0
      and 255 inclusive. Status code 0 is invariably used to indicate
      that the program ran successfully. Non-zero status codes
      indicate failure of some kind.
A lot of programs don’t use the whole space of failure codes,
      and simply return 0 for success or 1 for any kind of failure at
      all. On the other hand, some programs will use different nonzero
      values to signal different kinds of failure, but there’s no
      particularly strong convention about how that should work.
One obvious approach would be to use the size of the number to
      indicate the size of the disaster: if 0 means nothing went
      wrong, perhaps 1 might mean something small went wrong, 2 might
      mean a bigger problem, 3 a bigger one still, and so on? I’m
      sure
some
programs do organise their error codes in
      that way. But some do things completely differently. For
      example,
fsck
returns an error status that you have
      to interpret in binary: each of its 8 bits indicates a different
      type of failure, and it can tell you which
combination
of problems occurred!
The second cause of process termination is signals. Just
      like
errno
codes, Unix signals each have a numeric
      value, a symbolic name and a standard text translation.
Unlike
errno
values, signal numbers are quite
      standard between versions of Unix, and also much more likely to
      be visible in log files (see the next section). So it’s useful
      to know how to look them up. In
bash
, at least, the
      command ‘
kill -l
’ will list all the signals and
      their numbers.
Some signals just mean that the program
crashed
: it
      got its internal state confused, and tried to do something so
      badly wrong that the system had no way to continue running it.
      All of the following signals are crashes of one kind of
      another:
SIGSEGV
= ‘Segmentation fault’: the program
      tried to access memory at an address where there wasn’t
      any.
SIGBUS
= ‘Bus error’: the program tried to
      access memory at an address that didn’t even
make sense
in some way.
SIGILL
= ‘Illegal instruction’: the program
      tried to run something that the CPU didn’t recognise as valid
      machine code.
SIGFPE
= ‘Floating point exception’: the
      program tried to divide by zero, or something similar.
If you’re not planning to actually debug the crashing program
      yourself, then the differences between these signals probably
      aren’t very important. But if you report the crash to somebody
      else, it’s worth mentioning
which
of these signals it
      was, in case that’s a useful clue.
(One signal name I’ll call out here for being confusing is
SIGFPE
, which need not refer to
floating
      point
at all. An
integer
division by zero can perfectly well cause that
      signal. In fact, that’s actually
more
likely!)
Other signals indicate that something happened to the process
      from outside. Some examples:
SIGINT
= ‘Interrupt’: usually generated by
      pressing Ctrl-C in the terminal the program was running in.
SIGTERM
= ‘Terminated’: usually generated by
      using the
kill
command in the default way.
SIGKILL
= ‘Killed’: often also generated
      using
kill
, and sometimes by other causes such as
      the system being low on memory.
SIGPIPE
= ‘Broken pipe’: this program was
        writing output to a pipe, and the program at the receiving end
        of the pipe terminated before reading it all.
So if you see any of the first three of those messages in a log
      file, it probably doesn’t mean there’s anything wrong with the
      program that received the signal. If you’re unhappy that someone
      killed your process, you’ll need to hunt down the killer!
(In some situations the killer may be another piece of
      software, of course. CI systems will sometimes run a long job,
      and send it
SIGTERM
or
SIGKILL
if it
      runs for too long. If you’re lucky, the program that sent the
      signal will have left a message somewhere in
its
log
      file confessing to the crime and giving its reasons.)
The last of these signals,
SIGPIPE
, is a bit
      different. That one isn’t sent on purpose by a human. It happens
      when you pipe the output of one program into another, and the
      receiving program dies (for any reason at all) while the sending
      program hasn’t finished writing its output yet. This stops the
      sending program from wasting lots of effort on generating the
      rest of its output that nobody is listening to. So if you see
      ‘Broken pipe’ in a log, you should probably look for why
      the
receiving
process died, because that’s the real
      cause of the problem.
Propagating process exit statuses
Sometimes, when one program runs another, there’s an
      intermediate process in between. For example,
      when
make
runs a compiler, it doesn’t do it directly.
      Instead,
make
runs
sh
, and
that
runs the compiler.
In this situation, the intermediate process will try to pass on
      the exit status of the child. So if the child process exits on
      purpose with a particular status code, the intermediate process
      will exit with the same code, so its parent
make
can find out whether the operation succeeded, in the same way it
      would find it out without the
sh
in the middle.
But what happens if the subprogram terminates due to a
      signal?
As I describe in the previous section, exit statuses and
      signals are completely separate on Unix: you can always tell
      which one happened to a subprocess of yours. So if the
      intermediate process like
sh
wanted the parent to
      receive
exactly
the same notification as if it hadn’t
      been in the way, it would have to do that by deliberately
      killing itself with the same type of signal.
That is
possible
, using the
kill()
system
      call. But it’s not generally considered a good
      idea
,
      and intermediate processes don’t normally do it. Instead, the
      convention is for the intermediate process to terminate with an
      exit status obtained by adding 128 to the signal number.
For example, suppose you see a message along the lines of
      ‘
make: *** [
…
] Error 139
’. This means that a process
      run by
make
has crashed with
SIGSEGV
.
How do we know that? Because:
139 is a bit more than 128, so it’s likely to mean that a subprocess died of a signal, and then an intermediate shell converted the signal into 128 +
signal number
.
So we subtract 128 from the exit status 139, to get the signal number, which is 11.
Now we look that up in
kill -l
, and find that it’s
SIGSEGV
.
Of course, not
all
programs follow the convention that
      exit status 128 +
n
means a subprocess terminated with
      signal
n
. As I mentioned in the previous
      section,
fsck
returns an exit status in which all 8
      bits indicate different failures. So if
fsck
exited
      with status 139, it would mean something entirely different!
Process exit codes on Windows
As usual, things are a bit different on Windows.
On Windows, a process can choose a full
32-bit
exit
      code to return on purpose to its parent. On the other hand, the
      space of deliberate exit codes is shared with the space of
      status values indicating crashes and interrupts. If a process
      terminates for a reason that would generate a signal on Unix,
      then its parent will still just receive a 32-bit exit code, and
      will have to look at the particular code to decide whether it’s
      likely to be a deliberate or involuntary termination.
Similarly to Unix, the
usual
values returned as
      deliberate exit codes on Windows are still normally small
      non-negative integers, with 0 meaning success and nonzero
      meaning an error. Perhaps on Windows there’s
slightly
more of a convention that a larger number means a worse failure.
      (Because
cmd.exe
lets you test exit codes with the
      construction ‘
IF ERRORLEVEL
n
’, and it
      really means that the exit code is
at least
the number
      specified.)
If the process crashes or is interrupted, the return status
      will be taken from MS’s system
      of
NTSTATUS
      codes
. These codes are used for a lot of purposes, many
      having nothing to do with process exit. But among them are some
      values that can be generated when a child process exits. These
      values are typically a bit more than
0xC0000000
.
      Some examples:
0xC0000005
=
STATUS_ACCESS_VIOLATION
is the Windows analogue of
SIGSEGV
, indicating that the process crashed trying to access nonexistent memory
0xC000001D
=
STATUS_ILLEGAL_INSTRUCTION
is the Windows analogue of
SIGILL
, indicating that the process crashed trying to execute invalid machine code
0xC000013A
=
STATUS_CONTROL_C_EXIT
is the Windows analogue of
SIGINT
, indicating that the process was manually interrupted by someone pressing Ctrl-C.
Because these exception codes occupy the same space of numbers
      that a process can return deliberately, an intermediate process
      such as
cmd.exe
can propagate one unchanged to its
      own parent if it wants to
. So there’s no need on Windows for the
      awkward Unix system of adding 128 to the signal number and
      hoping your caller recognises that that’s what happened.
However, in my experience,
cmd.exe
won’t
      propagate
all
of these values unchanged. For example,
      I’ve seen it pass in
STATUS_ACCESS_VIOLATION
when
      its last subprocess returned that, but as far as I can tell, if
      its subprocess exits
      with
STATUS_CONTROL_C_EXIT
,
cmd.exe
discards that status value and returns success to its own
      parent.
Networking errors
Networking is complex. Not just in the general sense of
      ‘difficult to understand’, but in the more specific sense of
      ‘composed of lots of parts’.
A networking system is made of lots of separate components,
      layered on top of each other. So it’s horribly easy to spend ages
      debugging the wrong one, and trying to solve a problem you don’t
      actually have. Therefore, the first task of a networking error
      message is to try to indicate
which
layer has had a
      problem – and the first task of the person reading it is not to
      ignore that information!
As an example, I’ll discuss the stages of setting up an SSH
      connection. (If you’re a web-based person who doesn’t use SSH,
      then sorry about that choice of example. I do realise that HTTP
      is far more widely used than SSH, but it doesn’t make a good
      example for this purpose, because web browsers
      are
exceptionally
bad at reporting the details of
      network errors. I think SSH is one of the most commonly used
      protocols where reading the error messages
      is
useful
.)
When you make an SSH connection in the typical way, the SSH
      client and operating system between them must do all of the
      following things, any of which can fail and give an error
      message:
Find out what numeric IP address the hostname corresponds to
        (usually using DNS)
Try to make a connection to that address and see if any
        reply packet comes back at all …
… and whether the reply says that the server is willing to
        accept a connection on the SSH port
Begin speaking the SSH protocol, and see if the server
        responds in a way that looks like sensible SSH
The server proves it’s the same machine you expected to be
        talking to (‘host key’)
The client proves you’re a user who’s allowed to access that
        server (‘user authentication’)
You try to run some actual command on the server … which may
        fail and give its own error message.
This list looks complete, but one complication is that the very
      first step (‘turn this hostname into a numeric address’)
      typically
also
requres connecting to a server on the
      network – and then again sometimes it doesn’t. So if the whole
      network is down, the evidence of that might be that the DNS step
      fails,
or
that the later connection step fails,
      depending on your particular network setup.
So, what error messages might you see from all of this? In
      rough order:
‘Name or service not known’ or ‘Host does not exist’
The DNS said your hostname doesn’t exist. Maybe look for a
        typo in the hostname, or go back to the person who gave you
        the hostname.
‘Temporary failure in name resolution’
The DNS didn’t deliver a conclusive answer, for some
        reason
.
        Maybe this means the DNS server is down; maybe it’s up, but
        can’t contact some other DNS server it needs; alternatlvely,
        maybe this is your first clue that your entire machine is cut
        off completely from the rest of the network and you can’t
        successfully send network packets
anywhere
.
‘Connection timed out’ or ‘No route to host’
We found the destination machine’s address, but couldn’t get
        any reply from sending even a single packet to it. Maybe this
        means the network is down between you and the destination
        (but, if you’ve got this far, maybe
not
between you
        and the DNS server we talked to already). Or maybe the
        destination machine
itself
is down.
‘Connection refused’
The machine sent a packet back (so it probably
          is
there
), but it isn’t accepting connections to the SSH
          port in particular. Maybe
sshd
is not running on
          the destination machine.
‘Connection refused’ does
not
mean that the server
          is refusing logins to
you in particular
, i.e. that
          your particular user account is unauthorised. This message
          occurs when you haven’t
told
the server who you
          want to log in as, so it can’t possibly base a decision on
          that!
‘Access denied’ or ‘Permission denied, please try again’,
        followed by the client presenting a password prompt again
This probably means that
authentication
failed:
          you tried to prove to the server who you are, and it didn’t
          believe you.
If you’re sure you
have
an account on the server,
          then this is the moment to check your login details are
          right: are you using the right username, the right password,
          and/or the right SSH authentication key?
Alternatively, maybe you
don’t
have an account on
          this server – in which case perhaps this is the moment to
          ask the administrator server nicely if you can have one.
‘Permission denied’ in the style of a Unix command-line
        tool, perhaps mentioning a program name or file path
‘Access
is
denied’ (if the server is Windows, which
        would make this the translation of the system error
        code
ERROR_ACCESS_DENIED
)
This is more likely to mean that you
          successfully
logged in
to the server, but then the
          command you told the server to run (perhaps on
          the
ssh
command line) suffered some kind of a
          failure that had nothing to do with networking – for
          example, maybe you asked the server to access a file that
          your account doesn’t have the right to access.
In other words, this is a failure
          of
authorisation
, as opposed
          to
authentication
: the server knows perfectly
          well
who you are
, but doesn’t believe that person
          is allowed to do the thing you’re attempting.
If you believe you
should
be allowed to do the
          thing, this is the moment to ask the server administrator
          why you can’t.
One other possibility to bear in mind for
most
of
      these problems is that you might simply be connecting to the
      wrong host, or to the wrong
port number
on the same
      host. (Some computers run two separate SSH servers on different
      port numbers, with entirely different sets of valid
      users
.) If you are connecting to entirely the
      wrong place, then you might see
any
of these errors,
      depending on how closely the wrong server resembles the right
      one: the wrong host might not exist, or be down, or not running
      an SSH server, or not believe in your user account – or, even
      more confusingly, it
might
believe in your user account
      but have a different idea of what that account is allowed to
      do.
So, no matter
which
of these steps went wrong, it’s
      worth considering the possibility that the server
      you
actually wanted
is not the one you’re currently
      connecting to! If you’ve entered completely the wrong host name
      or port number, then it doesn’t really matter which step
      the
wrong
server rejected you at. The fix is the same:
      try the right server instead.
I said above that web browsers produce less useful error
      messages than SSH clients. This is true in the early stages of
      connection setup. Firefox, for example, prints exactly the same
      message for both ‘connection refused’ and ‘connection timed
      out’.
But once you’ve got through to a web server, things get a bit
      better, because HTTP itself will deliver some more useful error
      messages that let you tell the difference between types of
      failure:
‘404 Not Found’
This is the HTTP analogue of
ENOENT
: the URL
          you asked for just doesn’t exist at all.
‘403 Forbidden’
The HTTP analogue of
EACCES
: the URL is
          private, and the web server doesn’t have you on the list of
          people who can access it.
But, typically, the web server at least thinks it does have
          some idea of
who
you are. So if you logged in
          before getting this message, this probably
doesn’t
mean your login has failed.
‘401 Unauthorized’
The HTTP analogue of ‘Access denied’ at login time: you
          didn’t successfully convince the web server that you were
          you.
‘302 Found’, or ‘302 Moved Temporarily’, or ‘301 Moved Permanently’
This is
usually
not seen as a final error
          message. When an ordinary browser receives this message, it
          should automatically follow the pointer to some other page
          and return that instead.
But some command-line tools don’t do this in all
          situations. For example, if you’re downloading something
          using
curl
without the
-L
option,
          then it might generate this error as a reason why it can’t
          do what you asked. (The solution may well be to
          add
-L
to your command line and try
          again.)
Advice
Right, I’ve finished talking about what error
      messages
mean
. Now I’ll give some advice about what to
      do when you see one.
Mostly, these will be about investigation: how to convert the
      visible error message into an understanding of what’s
really
gone wrong.
The first step in investigating is to think of some questions
      you want answers to. Some are obvious, like ‘I wonder what file
      it means when it says “file not found?”’. Some might have become
      obvious after you’ve read the previous half of this article,
      like ‘I wonder whether the program that generated this message
      is the same one I think it is?’
Some that perhaps aren’t obvious are:
Do I even
agree
with what the error message is
        telling me?
If I already have an idea of what might be wrong, would I
        expect
that
error message, or a different one?
Do I think the operation that failed
should
have
        even been attempted in the first place? Is the problem that it
        didn’t work, or is the problem that it was tried at all?
If the error message is in a complicated log file: out of
        the whole log, is
this
error message the one that gets
        to the real point of what went wrong? Or is there a more useful
        one somewhere else?
Do I
agree
with what the error message is
      telling me?
If you see an error message making a claim about anything you
      can independently observe, my first piece of advice is
      to
go and look for yourself
, and try to confirm
      the error message’s claim.
In my experience, people often find this counterintuitive. They
      look surprised when I ask it during a pair-debugging session. If
      the computer has just told them some file isn’t there (for
      example), they assume without question that it’s
true
,
      and move straight on to considering how it might have happened,
      or what to do about it.
But I’ve always found it’s worth going and looking for
      yourself.
Mostly
not because the computer is lying.
      (Although that does
occasionally
turn out to be the
      cause, and when it does, it’s good to find out sooner rather than
      later!) But mostly because, in the course of going and looking for
      yourself, it’s surprisingly common to find out something else on
      the way that gives you a clue to
why
the file isn’t there
      (or whatever the problem is).
Here are a few examples.
‘No such file or directory’, with a specific pathname
      mentioned?
Go and look for yourself: tab-complete your way down the
          pathname in the error message, and see whether
you
think that file or directory exists.
For a start, if the pathname involved multiple components
          (like
/usr/lib/foo/bar/baz/quux.txt
), this will
          at least tell you
which
component doesn’t
          exist.
When you get to the directory where the file isn’t (or
          where some containing directory isn’t), look at
          what
is
in that directory. You never know what that
          might turn up. You might find a file spelled very similarly
          to the one you were expecting (aha, so the problem is just a
          typo!) Or you might find that everything in the directory is
          named in upper case rather than lower case (aha, is this
          program being run in a case-sensitive environment for the
          first time?) Or you might simply
recognise
the
          contents of the directory as a set of files you’ve seen
          before, and realise that that is clearly not where you’d
          expect to find the file mentioned in the pathname.
Another possibility is that you’ll find out that the
          file
does
exist, right where you thought it was. In
          that case, if the pathname is relative to the current
          working directory, perhaps the problem is that the program
          that failed wasn’t in the directory you thought it was in?
          And then you know you’re trying to solve a different
          problem: not ‘who deleted my file?’ but ‘why is this program
          running in the wrong directory?’
An even more confusing case is if the error message came
          from a different
computer
– for example, a program
          was run remotely via
ssh
in the middle of a
          script. Then the file might exist
here
, where
          you’re looking, but not
there
where the program was
          running.
In the very worst case, if you find that absolutely
          everything on the whole pathname looks exactly as you expect
          but just that one file is missing … then at least you’ve
          ruled out all those
other
causes of failure, and
          you can focus wholeheartedly on ‘who deleted my file, or
          what happened to the thing that was supposed to have created
          it?’.
Can’t run a program that you thought was on
        your
PATH
?
Go and look for yourself. Print out your
PATH
;
          identify which directory on it you
expected
the thing
          to be in; list that directory to check that it’s there.
You might start by noticing that the directory containing
          the program
isn’t
on your
PATH
, so now
          the question is not ‘where’s my program gone?’ but ‘why was
          my
PATH
not set up the way I expected?’
Or you might find that the program file is present under
          the right name, but isn’t marked as executable – so maybe
          something went wrong with the installation process that put
          it there.
Or (on Unix) you might find that it’s a broken symlink:
          perhaps you symlinked a program into your
bin
directory rather than copying it, and then blew away the
          directory where it
really
lived, without remembering
          that that would cause a problem.
Or – similarly to the previous example – you might
          recognise the contents of the directory as clearly the wrong
          thing. ‘Oh, oops, I added
/opt/program
on
          my
PATH
, but all the binaries live one level
          lower down in
/opt/program/bin
, guess I should
          have used that instead.’
The shell, or a language interpreter, reports a syntax error
        on line
n
of some script file?
Go and look for yourself. Open up the script file in a text
          editor, or just in
less
if that’s easier; have
          a look at the specified location in the file; see what you
          can see.
This is worth doing
even
if you don’t speak the
          language that the script is written in. It’s very easy to
          assume that you won’t be able to make sense of it, and not
          even bother looking. But it’s worth looking anyway, because
          there might very well turn out to be a problem so obvious
          that you don’t
need
to speak the language.
For example, you might be able to recognise that the file
          in question is
completely the wrong kind of thing
.
          Maybe it was supposed to be Python source code but it’s
          English text, or Perl, or binary gibberish, or HTML.
Another possibility is that the file has been truncated for
          some reason, perhaps because a disk filled up, or because a
          download was interrupted. If the program code in the file
          ends half way along a line, or in the middle of a pair of
          brackets or braces, then you might be able to recognise that
          even if you don’t know anything about the language at all.
          You only need to know that it
has
brackets or
          braces (or perhaps infer it from what you can see of the
          code) to guess that perhaps if the file ends in the middle
          of one that isn’t a good thing.
You might even find that the file contains
another
            error message
. For example, perhaps the program that
            generated the source file failed, and wrote its error
            message directly into the output file rather than sending
            it to a separate error channel. (Command-line
            programs
shouldn’t
do that, but sometimes they do
            anyway.)
And so on. If you see any error message that makes a claim you
      can observe directly,
go and look for
      yourself!
Even if you
think
you won’t be able
      to understand what you’re looking at.
You never
      know.
The reason why it’s a bad idea to say ‘I won’t go and look
      because I don’t expect to understand it anyway’ is that that’s
      only what would happen if
everything is working as
      expected
. But you’re investigating an error message, so you
      already know that
something isn’t
doing what you
      expect. And that’s why it’s worth having a quick look in a shell
      script even if you don’t speak shell, or similar:
      what
did
happen might turn out to be
easier
to
      understand than what
should
have happened.
Does my hypothesis predict
that
error
      message?
Sherlock Holmes famously said that it’s easy to reason forwards
      from a cause to likely effects, but harder to reason backwards
      from an effect to its likely causes.
A lot of debugging is based on Holmes’s hard backwards
      reasoning, especially when all you have to go on is a confusing
      error message. But once you’ve formed a theory about what the
      problem is, don’t forget to double-check the
easy
part,
      by asking yourself what effects you’d expect from the cause you
      have in mind. Specifically, ask yourself:
What error message would I
expect
, if that were the
        problem?
And is that, in fact, the same error message as the one I’m
        looking at?
It sounds obvious, but it’s a surprisingly easy step to forget!
      For example, perhaps you already had some possible problem in
      mind before you even ran the program that failed, and when
      it
did
fail, it was easy to assume that it had done it
      in the way you expected – and if it hadn’t, spend half an hour
      looking in the wrong place, when the message telling you
      otherwise was on the screen all along.
Another way this can go wrong is that you form a theory of the
      problem and then find you’re not quite sure
what
error
      message your theory predicts. In that case, one thing you can
      try is to provoke the same error condition on purpose and see
      what error you end up with.
For example, supposing your theory is that a file has the wrong
      permissions, but you can’t remember exactly what error you get
      in that situation. Then you could try using some easy tool
      like
ls
to access a file you
know
has the
      wrong permissions, and compare that error message with the one
      you actually saw.
This technique doesn’t always work. Sometimes your prediction
      of the expected error message will be wrong. Software has bugs,
      and sometimes even its error reporting has bugs; systems are
      complicated, and sometimes you didn’t understand as well as you
      thought.
But you only get better with practice! It’s worth getting into
      the habit of
trying
to predict the errors you expect,
      even if you don’t always get it right. When you get it wrong,
      it’s a learning experience, and you find out more about how
      things really work.
Was the thing that failed even the
      right thing to be trying?
Programs are (mostly) good at reporting
what
they
      tried to do, and what went wrong when they tried it. But they’re
      often less good at reporting
why
.
Of course, sometimes this is obvious, and clearly not the
      problem. If ‘
cat file
’ reports that it failed to
      open
file
, you don’t need it to explain why it
      wanted to.
But sometimes it’s not obvious at all. A program might report
      an error reading some obscure file such
      as
/etc/foo.conf
, and your first question might be
      ‘Why is this program even
trying
to
      read
/etc/foo.conf
, when I didn’t ask it to do
      anything involving a
foo
?’ Or you might find
      yourself looking at a network error, when you didn’t realise
      anything you were doing involved making a network connection. Or
      you might see an error message indicating
EPERM
,
      when you didn’t think you were doing anything that ought to need
      to be root.
If you don’t know why the program was even trying to do the
      failing thing, then one possibility is that it was a mistake to
      try it at all. So, before you start trying to arrange for the
      failing operation
not to fail
, consider whether that’s
      the right direction to be heading in: perhaps what you should be
      doing is arranging for it not to be tried at all.
Beware in particular of the temptation to handle
EPERM
(or any similar ‘you need to be root’
      message) by immediately becoming root and trying the thing
      again, without first thinking about whether it was what you
      actually
wanted
to be doing. If you just try again as
      root
, you risk
      the failure mode ‘You have now tried
extra hard
to do a
      wrong and dangerous thing, and this time, succeeded.’
Pay attention to wording, spelling, and
      even punctuation
Computers critique spelling and punctuation in your code all
      the time. So it seems only fair to return the favour when you’re
      reading their error messages. And it’s actually useful: even
      the
irrelevant
details of an error message can be
      useful clues!
If you’re used to reading text written directly by humans, this
      won’t be second nature. Humans rephrase the same concept in
      different ways all the time – perhaps even on purpose, to avoid
      sounding too repetitive. So you get used to ignoring the
      differences of wording, and focusing on the meaning.
But a computer program has no fear of sounding repetitive, and
      will use a fixed
printf
format string (or
      equivalent) for any given type of error message. So spelling,
      wording and even punctuation can be useful clues, because you
      can reasonably expect them to stay consistent. Even a missing
      comma can be a clue that the error message isn’t the one you
      thought it was!
(On the other hand, you can’t depend on
different
programs all reporting the same error in the same way. If
      they’re all producing the standard translation strings of OS
      error codes, then that part will be consistent, but any part of
      the message made up by the program author can easily differ from
      another program reporting the same type of problem. The
      consistency you can expect is very specific.)
In particular, there are a lot of phrases with similar sense
      but different details, which can indicate wildly different error
      conditions. For example, ‘Connection refused’, ‘Permission
      denied’ and ‘Access denied’ are all English phrases with the
      same basic meaning of ‘I refuse to let you do what you want’ –
      but in the usual contexts of software, they’re all talking
      about
different
things you wanted, so it matters a
      great deal which of them you saw.
An even tinier example is the difference between ‘Access
      denied’, which (for example) an SSH client might print when the
      server refuses your login details, and ‘Access
is
denied’, which is the Windows standard translation
      of
ERROR_ACCESS_DENIED
and indicates either a file
      permissions problem, or treating a directory as a file by
      mistake.
A piece of wording can be a vital clue even of
which
        program
generated the error. For example, I once ran a
        program written in the scripting language Tcl, and it failed
        with a syntax-error message. I didn’t speak Tcl, so if there
        had been a genuine error in the program it would have been
        hard work to figure it out. But I happened to spot that the
        wording of the syntax error looked
very
familiar – in
        fact, suspiciously like a particular error I was used to
        seeing from
bash
… aha! The problem was that the
        Tcl script was being fed to an interpreter for entirely the
        wrong language.
On another occasion, I saw someone get an error dialog box from a
      GUI application, in which the application’s own name was spelled
      without a capital letter. The application was developed by a large
      company, well organised enough that I doubted they would have
      misused their own trademark in that way – and that was enough of a
      clue to track the error down to a third-party plugin rather than
      the application itself.
Finding the useful error message in a log file
Sometimes you don’t just get one error message at a time. You
      get an enormous log file containing messages from lots of
      programs running in a huge script. An example might be a
      software build log, or a log of a test run from a CI system.
If that job as a whole fails, then probably somewhere in the
      log file will be an error message. Or rather,
at least
      one
error message.
In many cases, there will be more than one error message. This
      can happen in a complicated web of interoperating programs for
      lots of reasons. A failure in one program can cause a knock-on
      failure in another; test harness programs will often try to
      helpfully re-summarise errors from other programs; a test suite
      might deliberately continue running after an error to try to
      report as many different useful things as possible; some errors
      aren’t fatal, and a program can carry on running in spite of
      them.
So the next problem is: out of all these error messages, which
      one is the useful one for actually getting to the bottom of what
      went wrong?
Obviously, you’ll need to figure this out if you intend to
      debug the problem yourself. But it’s also a useful thing to do
      if you’re going to report the problem to somebody else.
      You
could
just send your local expert a link to the
      entire log and say ‘please sort this out, kthxbye’, but if
      you’re more polite than that, you’d want to at
      least
try
to pick out the relevant error message, to
      save them some of the effort.
Signposts
Some types of error message report that another program has
      exited with a failure status. In that situation, the other
      program might well have printed an error of its own before
      exiting. So error messages of this type function as ‘signposts’
      in the sense that they point at another error message: they
      don’t indicate the cause of failure by themself, they just tell
      you where to look next.
For example, suppose you see a message such as ‘
*** make:
      [foo] Error 1
’.
make
is a program that runs
      other programs one by one (usually to build a piece of
      software); this error is telling you that it couldn’t build a
      component called
foo
, because it tried to do that
      by running a subprogram of some kind, which exited with status
      1.
As we
discussed earlier
,
      exit status 1 means the subprogram
deliberately
reported failure. And if a program does that, it probably
      printed an error message just beforehand, saying why. So the
      useful message is not ‘Error 1’, but whatever the subprogram
      printed just
before
exiting with status 1. For example,
      it might have printed a message saying a file wasn’t found, or
      that some source code had a syntax error.
(However, if the message had said ‘
*** make: [foo] Error
      139
’, that would have been a different matter: as we
also discussed earlier
, this is
      more likely to mean that the subprogram
crashed
with a
      segmentation fault, in which case it was probably caught by
      surprise and didn’t have time to gasp out a last communication
      at all.)
Another example of an error message that’s usually a signpost
      on the route rather than the final answer is the Python
      exception
subprocess.CalledProcessError
, because
      that too indicates that Python ran another program and expected
      it to succeed, and instead it reported failure.
Typically the full message will look like something along the
      lines of ‘
subprocess.CalledProcessError: Command 'foo'
      returned non-zero exit status 2
’. Again, a small exit
      status like 1 or 2 suggests that the command probably reported
      failure on purpose, so you should look for the message it
      printed before doing so, which will be further up the log
      file,
before
the
subprocess.CalledProcessError
.
It’s easy to mistake the
CalledProcessError
for
      the root cause of the problem, especially because Python
      exceptions come with a large detailed traceback showing exactly
      where in the Python program something went wrong. When the
      problem genuinely is a bug in the Python script, that traceback
      is often exactly what somebody needs to know to fix it. But in
      the particular case of
CalledProcessError
, it’s
      misleading: if you send somebody a problem report consisting of
      just the traceback, they’re likely to be frustrated that you
      left out the
most
important thing, which was
      immediately before the traceback started!
(Of course, this rule doesn’t give the right answer every
      time.
Usually
when a Python script runs a subprogram
      the interesting question is ‘Why didn’t the subprogram succeed?’
      – but just occasionally, as
      we’ve
just discussed
, it’s
      unsurprising that the subprogram failed, and the better question
      is ‘Why was it trying that in the first place?’. And
      for
that
, the traceback might be more likely to
      help.)
Cascade failures
Sometimes, one subprogram of a large job can fail in a way
      that
doesn’t
bring the whole job to a halt – but
      whatever the subprogram was trying to do is not fully done, and
      that can cause other programs to fail later in the job.
In particular, in build and test runs, a lot of the
      interoperating programs will be consuming each other’s output.
      So an error that prevents an output file from being created at
      all, or from being created correctly, can easily lead to the
      consuming program reporting an error message about that file if
      it runs at all. But the real problem is not that the consumer
      got confused by the nonexistent or wrong file – it’s that the
      file was nonexistent or wrong in the first place.
So another skill of finding the most useful error message is to
      identify things that look ‘cascadey’, and treat them as an
      indication to look further up the log file.
For example, errors of the general ‘file not found’ type, such
      as ‘No such file or directory’ or ‘The system cannot find the
      file specified’,
might
indicate that something earlier
      in the same script should have written that file, and might have
      printed a message saying why it didn’t. Not always – it will
      depend on what the file in question is – but it can be worth
      looking.
If your log file is from a software build process, and it
      contains a compile error in a source file
in the build
      directory
rather than in the original source directory,
      that might also be a cascade failure. Source files in the build
      directory are likely to be auto-generated by an earlier build
      step – so the auto-generating tool might have said something
      helpful at the point where it generated this file.
One particularly common case is that a program consuming a file
      reports that it’s unexpectedly
completely empty
. This
      can easily happen by accident, in more than one way.
One way that a file can be accidentally empty is because the
      disk filled up while some earlier program was trying to write
      it
. If you’re
lucky
, there will be an
      earlier error message mentioning that the disk was full –
      although there may not be, because a lot of programs forget to
      check that the
write()
system call (or equivalent)
      succeeded. But even if there’s no error message, it’s worth
      bearing in mind. One clue to a disk-full problem might be
      that
lots
of files in the same run seem to be
      mysteriously empty. In that case, definitely check how much free
      space there is on the disk in question!
Another way for a program to generate an empty file by mistake
      is if it opens the output file
prematurely
, before
      finding out some reason why it can’t generate the data to write
      to it. This in turn can happen for more than one reason. A
      common one is I/O redirection, i.e. running a command of the
      form ‘
command > output_file
’, because the shell
      or command processor handles redirections by creating the output
      file
first
, and then running the subprogram. So if the
      subprogram runs into any kind of problem before writing anything
      to its output, the output file is still
there
, just
      empty.
Another type of premature output-file creation happens in
      Python, if a program uses the
argparse
module to
      process its command line, and in particular
      uses
argparse.FileType
for the option that
      specifies an output file. This will cause
argparse
to actually create and open the output file during parsing of
      the command-line options
. So if the program then discovers a syntax
      error in its input (for example) and exits with an error, it’s
      too late – the output file already exists, without any data in
      it.
Non-fatal errors
In both of the previous subsections, the common theme has been:
      recognise that sometimes an error message indicates that you
      should be looking for a more interesting one earlier in the file.
So an obvious approach is to just look for the
earliest
error message you can find at all! Then it can’t
possibly
be a cascade failure or a re-summarisation of an earlier error
      message.
This often works, but (as usual) not always. One reason it can go
      wrong is that
some error messages are not fatal!
Sometimes a program will print an error message and then keep
      going, because the thing that failed wasn’t very important, or
      because the program already had a good plan for dealing with the
      problem. So if you focus your attention on the earliest error
      message, you might find that it’s
still
not the really
      important one.
One example of this occurs in build tools such
      as
cmake
, which sometimes start off by performing
      tests to see what facilities are available on its build
      machine.
cmake
, for example, might print things like
      this:
-- Looking for strerror_s
-- Looking for strerror_s - not found
-- Looking for setenv
-- Looking for setenv - found
-- Performing Test HAVE_STRUCT_STAT_ST_MTIMESPEC_TV_NSEC
-- Performing Test HAVE_STRUCT_STAT_ST_MTIMESPEC_TV_NSEC - Failed
-- Performing Test HAVE_STRUCT_STAT_ST_MTIM_TV_NSEC
-- Performing Test HAVE_STRUCT_STAT_ST_MTIM_TV_NSEC - Success
The words ‘not found’ and ‘Failed’ in these messages look like
      errors – but they’re perfectly normal. In this snippet (taken from
      the LLVM compiler project),
cmake
is checking the
      system’s build environment for a large range of functions and
      structure fields that aren’t all expected to exist, and if any one
      of them doesn’t exist, it’s OK, the software project has a plan
      for doing without it. (That’s why it bothered to check in the
      first place – to see if its plan would need to be used.)
A completely different example: I used a test suite once that ran
      all its subprograms with a deliberate restriction on the amount of
      memory and CPU they can consume, via the Unix
ulimit
command. This meant that if the program under test went out of
      control, it wouldn’t make too much trouble for everything else on
      the machine. But then we started running the same test suite in a
      container environment in which processes aren’t allowed to
      run
ulimit
to lower their own limits in that way. So
      the log files were suddenly full of errors saying ‘
ulimit:
      Operation not permitted
’. At first nobody noticed, because
      the test harness proceeded without the safety precaution, and the
      tests themselves passed. Later, when the test suite
      actually
failed a test
, the person reading the log file
      connected the dots and thought ‘aha! Error message here, failed
      test there, they must go together’ – but in fact,
      that
ulimit
error had nothing at all to do with the
      test failure.
One way to spot non-fatal errors is to compare your log file
      against a log file from the same job
not
failing, if you
      have one. Any error message you can see in the log that ended up
      reporting success can’t be a fatal one, and then if you see it in
      the failing log, it probably isn’t the real problem. In both of
      the examples above, this technique would have identified the
      errors as non-fatal, without having to know anything
      about
cmake
configuration checks
      or
ulimit
.
Case studies
Here are a few real examples of error messages that are
      confusing, showcasing the use of the advice in this article.
apt
download failure
The first example (with irrelevant details removed) came from
      the
apt
command on an Ubuntu Linux system, when a
      user tried to use it to download a file from the local Ubuntu
      package repository:
E: Failed to fetch http://
long URL
/
filename
.tar.xz  Could not open file
filename
.tar.xz - open (13: Permission denied) [IP:
10.11.12.13
80]
The person who got this error message interpreted it as reporting
      a network error, because of the initial ‘Failed to fetch [URL]’,
      and started trying to debug their network connection. But that
      part of the message is
apt
’s high-level description
      of the overall task that couldn’t be completed. Later in the error
      message, we see a detailed description of what exactly went wrong:
      ‘
open (13: Permission denied)
’. That means that the
      tool attempted the Unix system call
open
, which opens
      an ordinary disk file, and got the
EACCES
error code,
      meaning that Unix file permissions prevented it. (The ‘13’ is the
      numerical value of
EACCES
on Ubuntu.)
In other words, the problem wasn’t the
network
at all.
      The package repository’s web server was functioning perfectly. But
      after
apt
started receiving the file data, it tried
      to create a file on the receiving machine to save the data to,
      and
that
failed with a permissions error.
In fact, the problem was that the user had run the
apt
      source
command, which downloads files into your current
      directory, but their current directory was somewhere
      in
/etc
, where they couldn’t create files. They’d
      forgotten to change directory to somewhere more sensible
      first.
(If the web server really had refused to serve the file, the
      details would have looked less like
      a
Unix
errno
report
and
      more like an
HTTP error code
,
      perhaps 404 or 403 or some such.)
(Also, this is a good illustration of
      the
principle
that you don’t
      always want to respond to a permission error by using more
      authority. The actual failed operation was creating a file
      in
/etc
, which a normal user can’t do, but root
      can. But the user definitely didn’t want to become root and try
      again, because then they would have
succeeded
in
      dropping a Debian package file somewhere
      under
/etc
, where it might confuse some system
      program,
and
where they’d never find it again!)
curl | sh
syntax error
My second example involved a user running a command of the
      form ‘
curl some://url | sh
’, to download and
      immediately run a shell script (which they hoped would install a
      piece of software they wanted to use). This failed,
      because
sh
reported a syntax error.
When this user asked for help, our first suggestion was to run
      the
curl
command on its own, without ‘
|
      sh
’ on the end, so that we could see the actual
      text
curl
was piping into
sh
. The user
      hadn’t tried this, because they didn’t expect to understand it
      anyway, because they didn’t speak
sh
. But this is
      an illustration of the ‘
go and look for
      yourself
’ principle: as soon as we did look at the output
      of
curl
, it turned out that
curl
had
      output an HTML error document in place of a shell script. And
      even if you don’t
understand
shell scripts, you might
      still be able to tell the difference between a shell script and
      a piece of HTML.
Looking at the HTTP error document itself, it contained
      an
HTTP error code
of 302,
      meaning it was a redirection. (The user was downloading the
      shell script via an outdated URL – the website hosting it had
      been reorganised, and the old URL was automatically redirecting
      to a more up-to-date one.) So the answer was that the user
      needed to add the
-L
option to
      the
curl
command line, which makes it follow
      redirections, which it won’t do by default.
But it makes a difference
which
HTTP error it was: if
      it had been 404 rather than 302, then that wouldn’t have helped,
      and instead, we’d have had to check for typos or paste errors in
      the URL, or maybe whether the place they’d got the URL from was
      out of date.
rdiff-backup
startup failure
My final example comes from a backup utility I use
      called
rdiff-backup
, which can back up one computer
      on to another by using SSH to connect to the other machine. When
      SSH fails,
rdiff-backup
tries to print helpful
      user-friendly advice about what to do about it, which sometimes
      goes wrong. For example:
Host key verification failed.
Fatal Error: Truncated header string (problem probably originated remotely)

Couldn't start up the remote connection by executing

    ssh -C
username
@
hostname
rdiff-backup --server

Remember that, under the default settings, rdiff-backup must be
installed in the PATH on the remote system.  See the man page for more
information on this.  This message may also be displayed if the remote
version of rdiff-backup is quite different from the local version (2.0.5).
The final paragraph is large, prominent, and friendly-looking,
      and suggests some plausible things to
      check.
rdiff-backup
needs to be installed on both
      computers for remote backups to work, so
      perhaps
rdiff-backup
isn’t installed correctly on the
      machine we’re connecting to? Or perhaps it is installed, but is
      completely the wrong version? But all of this is guesswork (as you
      can tell from the word ‘may’ and the two different suggestions of
      what
might
be wrong). It’s
rdiff-backup
trying to give helpful advice to the user, not based on hard facts
      about this particular situation, but based on the author’s general
      experience of which things people most often get wrong.
All that
rdiff-backup
really
knows is that
      it ran
ssh
, and the data stream it received
      from
ssh
ended before it had seen anything that
      looked like a greeting from another copy
      of
rdiff-backup
. That’s what it’s reporting in the
      message ‘Truncated header string’.
But in this case, that’s a
cascade
      failure
. Immediately before
that
, we can see the
      real cause of the error: the
ssh
command printed
      ‘Host key verification failed’. When
ssh
prints
      that, it means it gave up on the network connection for security
      reasons before even
trying
to transfer data – so in
      this case the connection was abandoned before even
finding
      out
whether
rdiff-backup
was installed on the
      other system, or whether it was the right version. All of the
      user-friendly advice is completely missing the point, and the
      real error message shows that the problem is totally
      different.
Final advice: don’t trust any of this advice 100%
Everything I’ve said in the advice half of this article is
      unreliable!
All of these suggestions of what to investigate, or how to
      investigate, are good rules of thumb, or good starting points, or
      likely causes of problems. Sometimes they’re not right. If you
      think you know better, and that your case is an unusual one that
      doesn’t conform to my principles, you might be right.
And even if you
don’t
think you know better, there’s
      always the chance that your case is
still
an unusual one,
      and you just haven’t found that out yet.
For example, sometimes programs
report the wrong
        error
, which will cause a serious problem if you’re
        trying to deduce as much as you can from the details of an error
        message!
This can happen intentionally, for security reasons. In this
      article I’ve encouraged you to pay attention to the difference
      between ‘Permission denied’ and ‘No such file or directory’, or
      between 403 and 404 in HTTP, because they mean different things.
      But sometimes they’re deliberately merged: some web servers will
      deliberately return 404 (thing doesn’t exist at all) even when the
      real problem is 403 (it exists but you aren’t allowed to access
      it), in order to avoid leaking information about
what things
      exist
. All I can suggest is to remember which web servers
      can’t be trusted, and treat them with more suspicion.
Reporting the wrong error can also happen by accident. For
      example, on both Unix and Windows, operating system errors are all
      written into the same location – so if another error occurs
      between the real failure and the error message generation, the
      program can print the wrong error code. Another example is in the
      previous section, where a program well-meaningly tried to guess
      how its subprocess had failed, got it wrong, and gave misleading
      advice.
I know it sounds as if I’m saying that you have no hope of
      spotting the right error message. And it’s true that there are no
      rules that are simple
and
reliable.
Ultimately, the most reliable method of decoding error messages
      correctly is to know a lot about the specific programs you’re
      dealing with, and have lots of experience of how they really
      report their errors, which ones are dependable, which ones are
      misleading, and what the confusing ones really mean.
Without that knowledge, you just have to guess – but the rules of
      thumb in this article might make your guesses right more often.
And it’s worth
trying
to interpret error messages in as
      much detail as you can, because that’s a good way to
gain
the detailed experience that makes you an expert. Do your best to
      interpret the error message even if you don’t already know the
      area well; if you get the wrong answer, find out why you were
      wrong, and improve! It’s always tempting to fling the whole thing
      at someone more experienced, to get your immediate problem solved
      faster – but then you don’t learn as much.
Acknowledgments
This article is adapted from material that I originally wrote
      for my employer Arm. I reproduce it as a public article with
      Arm’s kind permission.
With any luck, you should be able to read the footnotes of this
      article in place, by clicking on the superscript footnote number
      or the corresponding numbered tab on the right side of the page.
But just in case the CSS didn’t do the right thing, here’s the
      text of all the footnotes again:
1.
This particular case
      is not
strictly speaking
an
errno
code.
      For historical reasons, the hostname lookup functions report
      errors using their own separate enumeration of error codes,
      which aren’t stored in
errno
or translated using
      the same functions. But the principle is the
      same.
2.
In that situation I
      feel as if Windows shouldn’t be using the definite article! It
      would be more honest for it to print ‘
A
process cannot
      access
a
file’, which at least doesn’t try to give you
      the impression that you ought to know the details
      already …
3.
There’s more than one
      reason why it’s a bad idea to propagate the signal literally.
      One is that it’s inconvenient for the program itself, which
      won’t get a chance to clean up its own state in the normal way,
      and will have to to make a special effort to do it before
      calling
kill()
. Another is that processes dying of
      particular signals have knock-on effects that aren’t wanted in
      this case. For example, if a program terminates due
      to
SIGSEGV
, the OS might write a core dump file, or
      even automatically offer to send a bug report to the developer.
      If the program genuinely crashed, this might be useful – but
      it’s not so useful if the same things happen because the program
      deliberately sent itself
SIGSEGV
.
4.
The fact that exit statuses can be greater than 2
31
, and that this even happens in practice, means that programmers should beware of storing one in an
int
– especially if they have the Unix habit of using a negative value to mean ‘no real value here yet’! This caused a very confusing intermittent bug in early versions of
pterm.exe
.
5.
I’m not convinced that
            Windows reliably reports the difference between permanent and
            temporary DNS failure. I tested it by turning off my own name
            server temporarily and I still got ‘Host does not exist’. Then
            again, the MSDN docs say there are separate error codes, so who
            knows.
6.
In the context where I originally
      gave this talk, many people were users of the
git
hosting system ‘Gerrit’, which typically runs a special SSH
      server on the unusual port number 29418. The server it’s running
      on is likely to also run an
ordinary
SSH server on the
      default port 22, and a common cause of Gerrit login failure is
      to forget to put the special port number in your
git
      clone
command, so that
git
tries to talk to
      the wrong one of those servers. Adding to this confusion, some
      people configure
ssh
to recognise the Gerrit server
      name and
automatically
add the special port number –
      and then when that person sends a sample command line to
      somebody without that configuration tweak, it will cause exactly
      this error …
7.
Also, if you’re using
sudo
in particular, there’s a strong chance of other nasty side
      effects involving leaving files in locations specific
      to
your user id
which are unexpectedly owned by root,
      to create problems later.
sudo kinit
is a
      particular example I’ve seen causing trouble, and any large and
      complicated GUI program is also a bad bet.
8.
In that
      situation it’s probably useful to
also
provide the link
      to the entire log. If you misidentified the relevant message,
      the recipient will need to go back to the full log file and do
      their own analysis. As I said in my much older
      article
How
      To Report Bugs Effectively
, it’s fine to attempt a diagnosis
      in a bug report, but do
also
include all the raw data
      that your reasoning was based on.
9.
Unix is particularly prone to
      generating empty files when the disk fills up, because typically
      Unix filesystem formats have separate limits for the
number
      of files
you can make, and the total
amount of
      data
in those files. And you basically
always
hit the data limit before the file limit. So
      when you try to make a file on a full disk, what happens is that
      you successfully create a new file of zero size, and don’t get
      an error until you actually try to
write
anything to
      it.
10.
At least,
      this happens if you did the obvious thing of
      calling
parser.add_argument
with
type=argparse.FileType("w")
. My personal habit
      in my own Python scripts is to set
type=opener("w")
instead, where
opener
is a wrapper of my own,
      returning a lambda which will call the
FileType
constructor. So I can defer actually opening the output file
      until I’ve got past all the likely causes of error. But this is
      unidiomatic and unusual, and most simple Python programs don’t
      bother.
