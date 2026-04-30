---
title: "History of PuTTY's development"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/putty-history/"
fetched_at: 2026-04-30T07:00:49.663153+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# History of PuTTY's development

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/putty-history/

History of PuTTY's development
[Simon Tatham, 2020-03-24]
I received email from a software architect asking me if there was a
writeup of the history and gradual development of the PuTTY tool
suite. I wrote and sent a long response, and having done that, it
seemed a shame to waste it. So here it is as a public article too.
The questioner said they were particularly interested in learning
about "successful planning, architecture and roadmap creation." My
response to that was:
I'm flattered that you say that, but I fear you may be overestimating
the amount of all of those things that we actually did! :-)
Most of the evolution of PuTTY, in terms of major features, was driven
either by my own need for the feature, or someone else doing the work
and sending patches. There was very little in the way of long-term
planning.
Off the top of my head, here are some points of history that I can
remember:
Summer 1996
: I started writing my own Windows GUI Telnet client with
built-in terminal emulator. I had been using things like Win95 Telnet
and DOS Kermit to talk to various login servers and chat systems, and
I'd got tired of the poor terminal emulation in each of them, and the
inconsistencies between them whenever I switched from one to another. My
original plan – as a student who hadn't learned pessimism yet – was to
take the existing code bases of Unix Telnet and
xterm
, glue them
together back to back, and port them to Windows. But I quickly realised
that it would be faster to write one from scratch than to make that plan
work. So I did that instead.
The result was a program I unimaginatively named 'STel' ('Simon's
Telnet'). It had the advantage of some early testing in DEC, because my
dad worked there: DEC application software tends to use a lot of dark
corners of the VT100ish escape sequence system, so it makes a pretty
rigorous test.
At this stage, STel was very much in the category of 'scratching my own
itch' software: I'd written it because
I
wanted to use it, and its
feature set was exactly the features I'd found a need for myself. I let
friends have copies of it on request, but I hadn't distributed it
publicly.
Summer 1998
: people were getting the memo about network security being a
good idea, and systems I used were starting to switch over to SSH. I
converted STel into a multi-protocol client with a switchable backend
system, implemented an SSH-1 backend, and renamed it 'PuTTY'.
Early 1999
: I put it up on a web page for the first time. No
installer, no manual, not even a zip file; just a
single
putty.exe
you could download and run, and a web
page that mostly consisted of apologies for all the features
it
didn't
have.
Mid-1999
: a contributor sent an
scp
implementation
to go with the terminal login client, and
pscp.exe
was
born.
Late 2000
: my employer (Arm) was looking for a way to run CVS over SSH
on Windows. Their IT department found PuTTY, noticed that it was written
by an Arm employee, and talked my manager into letting me spend a few
weeks of work time on adding the necessary features. (I guess that
worked out cheaper than a lot of ssh.com licences!) That burst of
development gave rise to Plink, Pageant and PuTTYgen, and also added
SSH-2 support, which was starting to become necessary around then.
Early 2001
: a contributor sent us an implementation of X11 forwarding,
for benefit of people running a Windows X server (such as Exceed, or
Cygwin's one). I remember that the implementation was not done at all
the way I expected: instead of being integrated into the SSH code, it
was a separate module sitting alongside the SSH code, with more or less
peer-to-peer communication between them (function calls back and forth).
I don't even know whether the architecture
I'd
imagined would have
worked: I never got round to trying it. I just knew I'd never have
thought to do it the way our contributor did. But it worked at the time,
and that design choice has survived unchanged until now and been copied
in several other places, so it turned out to be a pretty good idea.
Mid-2001
: another contributor sent us TCP port forwarding, by
essentially using the same design as X forwarding and modifying the
details.
Also in mid-2001
: Unicode support was contributed, together with a
conversion layer so that you could configure what character set you
expected the server to send.
Early 2002
: finally got round to writing a manual!
Late 2002
: I'd now been using my own personal terminal emulator for long
enough that I started to get picky about
other
terminals not behaving
quite like it. I was tired of having to go back to
xterm
when I sat down
at a Linux machine. What I wanted was a Linux terminal program that used
the PuTTY terminal emulator.
So I took a full month off work, and spent a lot of it porting various
parts of the PuTTY code to Linux. I ported the terminal emulator, and
turned it into a program called
pterm
. I ported the network code, so
that I could test it under Valgrind, which I expected to deliver
stability benefits on the Windows version of the code. And I ported the
complicated control-layout system for the configuration dialog, because
I was developing a cross-platform internal API for that anyway (for the
benefit of a Classic MacOS port that was never finished) and Linux made
a good test case.
Having got all three of those major pieces, it only took another
couple of hundred lines of code to glue them all together into a Linux
version of the full PuTTY application. I immediately decided I
preferred that to OpenSSH because it didn't have that awkward in-band
'
~
' interface for delivering commands to the SSH client:
in GUI PuTTY, every keystroke typed in the window is sent to the
server, and if you want to talk to the client itself (to reconfigure
forwarding or whatever) then you can do that through the GUI menus.
I think that was more or less the point at which things stabilised a
little. By that time we had a full SSH client implementation including
agent, key generator, file transfer and GUI and CLI login tools, with
mostly the same feature set as OpenSSH of its time, but also running on
both Linux and Windows. My own major goals were achieved: I could use
software that behaved exactly the way I liked it, no matter which kind
of machine I happened to have sat down at.
For quite a few years, development was more in the realm of bug fixes,
minor features, keeping pace with evolving standards (e.g. implementing
new SSH protocol elements such as ciphers), and general polishing. I
don't remember implementing any major features of my own for some time,
although a few largish things were contributed by other people, notably:
IPv6 networking support (2005)
Arabic and other bidirectional text support in the terminal (also 2005)
Kerberos authentication in SSH (2011)
elliptic-curve cryptography (2017).
Perhaps one exception to that general trend was the addition of serial
port support in 2007, which is quite unusual in that I wrote it myself
even though I had no use for it personally. (I think even now I've only
used PuTTY to talk to a serial port once or twice.) But a lot of people
were asking for it, and it was tricky enough (restructuring of Windows
event loops to deal with things other than network sockets) that I
decided I'd better do it myself if it was going to be done at all. The
restructuring I had to do for that feature also permitted local proxy
command support, which in particular allows you to run PuTTY with a
Plink proxy to go via a secondary SSH connection to a 'jump host'.
To my personal way of thinking, the next
big
feature I worked on was
connection sharing, implemented in 2015. That needed a much larger
restructuring of the code: I worked on it out-of-tree for about six
months before it was ready to push without destabilising everything. My
main motivation was that I was using the proxy-command support at work
to connect through a particularly strange proxy that never connected me
to the same host twice (centralised dispatch service on a large cluster
of machines), and so I needed a reliable way to open a second terminal
window on whatever machine I'd got through to the first time.
The only other really big piece of work I can think of was even more
recent, in 2019: I refactored the SSH code so as to implement a server
alongside the client. But that's not really a user-facing feature,
because the server is not security-hardened, performance-optimised, or
tied into standard authentication systems. It's just a development tool,
for testing the client against.
So, if you're after general themes about architecture and roadmap ... I
think most of the time I never really had a forward-looking roadmap for
PuTTY development. I just did a
lot
of dogfooding, in varied
circumstances: I've been using my own SSH client and terminal emulator,
as close to exclusively as possible, ever since they were written, and
whenever I come across a need for a feature myself, I write it, even if
it's huge. But I don't plan across decades: I rarely know what feature
I'll find a need for next year! At most, I sometimes have medium-length
plans that drive me to spend 6 months or a year working towards a
particular goal, but the goal was generally some specific feature that I
was ultimately going to want to use myself.
And another common theme is that other people were doing the same. A lot
of the early feature work was contributed by other people, who liked my
code as far as it went and were willing to put their own effort into
adding the one extra feature they felt it was missing.
More or less the only exception to that general theme was the serial
port support, which – as I mention above – I wrote myself, but the
motivation came from other people. That may have something to do with
why it's never really had much love: for example, other serial terminal
programs support serial-port-friendly in-band file transfer protocols
such as Kermit or Zmodem, but we've never added anything like that (in
spite of a few requests). Probably if I had been a heavy user of the
serial backend myself, I'd have got round to it by now. As it is, people
have occasionally sent patches that graft in someone else's Zmodem code
with a small glue layer, but we're generally reluctant to accept that
kind of patch, because usually the other code's licence is less
permissive than the one we want to publish the result under.
