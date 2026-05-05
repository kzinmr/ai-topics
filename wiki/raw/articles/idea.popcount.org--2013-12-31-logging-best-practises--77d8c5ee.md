---
title: "Logging best practices"
url: "https://idea.popcount.org/2013-12-31-logging-best-practises"
fetched_at: 2026-05-05T07:01:12.567269+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Logging best practices

Source: https://idea.popcount.org/2013-12-31-logging-best-practises

Logging best practices
31 December 2013
Every serious program has some kind of logging infrastructure.
Sometimes it's trivial (
stderr
); sometimes it's sophisticated and
highly configurable.
Unfortunately, many programs use logging inconsistently. The logging
infrastructure is usually grown organically and not thought
through. Many programs repeat the same mistakes with regard to
logging.
Let's take some time to talk about logging in larger systems.
Before we start it's necessary to recognise that logging serves many
different purposes. Generally speaking, I think log messages fit into
distinct categories, each useful on a different occasion:
Critical errors
describing why the system wasn't able to
start. They are useful for the system administrator trying to get the
program to run.
Debug messages
used mostly post mortem to discover why something
went wrong. They are used by developers to understand what happened to a
system on a higher level. Users are often asked to share these logs
but rarely have enough knowledge to understand what they say.
Access logs
related to end-user actions; for example
HTTP requests in an HTTP server. Useful for statistics and to debug
end-to-end system behaviour.
1) Critical failures are special
Errors of the first type are critical errors describing why the system wasn't able
to start. In my opinion these messages are a special case. They are
often produced before a proper logging system started; for example when
configuration can't be parsed. I think these messages require
separate treatment.
The Linux kernel is a good example. It can print all logs on the console
before the system is properly configured. If the kernel fails to start a
system administrator is able to quickly debug it.
2) Don't produce too many logs
It's often useful to have a verbosity setting for debug
messages - though I think it shouldn't be overcomplicated. Three
verbosity settings are in my opinon enough:
"Quiet" mode, useful when the server is running in batch mode.
"Default", that prints logs most useful for normal users.
"Debug" mode, with verbose logs for debugging.
In my opinion even the "debug" should be readable. These logs are
going to be read by a human and it's counterproductive to produce
megabytes of verbose logs that nobody can digest. Furthermore, useless
debug statements spoil the code without creating any value.
Let's look at the Linux kernel again. Kernel programmers avoid logging
too much -
dmesg
usually contains only the most important
information. To log more than that is treated as a potential
denial of service attack vector
.
3) Don't mix debug and access logs
I believe that access logs are fundamentally different from debug messages
and should be dealt with separately. Access logs, as opposed to debug
messages, are mostly used for statistics and represent a well-defined
and valid system behaviour.
In practice the distinction is not that simple. Ideally debug logs
should be only about a meaningful state changes in the full
system. Things like start, stop, configuration reload, credential
changes or disk errors, completely unrelated to end-user activity. Web
servers are a good example. They treat access logs separately from
whole-program debug messages. A configuration file allows the user to specify
access log granularity per vhost.
This time, the Linux kernel is a bad example. By design it doesn't have an
"access log" equivalent. Unfortunately, it's possible to bend the rules
and get it log end-user activity in
dmesg
. For example one can get
iptables
to do logging by using
-j LOG
like this:
iptables
-
A
INPUT
-
p
tcp
--
dport
22
--
syn
\
-
j
LOG
--
log
-
prefix
"iptables: "
As a result the "access" logs produced by iptables are mixed with
potentially crucial debug messages in
dmesg
. Without a special rule
in
syslogd.conf
, the
/var/log/kern.log
file becomes a mess.
4) Rate-limit debug logs
Related to the previous point: I think it's best to avoid producing
debug messages that contain user requests or are derived from them.
As mentioned above, the Linux kernel by default avoids logging
end-user actions and keeps
dmesg
clean. But it's not always easy to
distinguish what is an "end-user" action and what is not. For example,
receiving a network packet clearly shouldn't be logged in
dmesg
, but
how about the action of mounting a CD?  For this reason Linux kernel
has a special
printk_ratelimited
function. It's used to log a thing,
but if it happens too often the kernel is free to skip it and avoid
overwhelming the syslog.
5) Heighten your hygiene
When software matures and the code stabilises, logging statements can
age. I've seen this many times - recent parts of the code produce
reasonable debugging logs while old code has some really weird
verbose stuff that nobody understands and everybody is afraid to
remove. My advice: be bold, remove stupid logs and make a constant
effort to keep all logging levels consistent and sensible.
Let me use Linux as an example again. Its logging is generally in
good shape, but in my opinion it could be simplified. I really don't
understand the difference between "EMERGENCY", "ALERT" and "CRITICAL";
or "DEBUG" and "INFO" error levels.  But all of these seem to be
used:
linux
$
for
type
in _DEFA _DEBUG _INFO _WARN _NOTI _ERR _CRIT _ALER _EMER;
do
echo
-en
"$type\t"
; find . -name
\*
c -a -type f| xargs cat|egrep
"\sprintk"
|grep KERN
$type
|wc -l;
done
_EMERG   266
_ALERT   287
_CRIT    397
_ERR     10697
_WARNING 4811
_NOTICE  822
_INFO    6706
_DEBUG   4478
Summary
The main message is simple: don't be a slave of your logging
system. Tweak it, refactor it, maybe even rewrite it. Most importantly:
think it through. In the end it's a part of the code you ship.
