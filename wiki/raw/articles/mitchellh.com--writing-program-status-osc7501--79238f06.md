---
title: "A Terminal Protocol for Program Status (OSC 7501)"
url: "https://mitchellh.com/writing/program-status-osc7501"
fetched_at: 2026-10-07T10:01:26.915882+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# A Terminal Protocol for Program Status (OSC 7501)

Source: https://mitchellh.com/writing/program-status-osc7501

I wrote a specification for a new terminal escape sequence:
OSC 7501, the Program Status Protocol
.
It lets any program tell the terminal what it's doing: idle, working,
waiting on the user, finished, or failed, and why.
For example, here is how
Terraform
could indicate that it is blocked waiting for user input, with the
message "Apply 3 to add, 1 to change, 0 to destroy?" (base64-encoded). A terminal (or any
other tool running Terraform) could show this information however it feels
appropriate: a notification, an inbox, a status icon, etc.
ESC ] 7501 ; state=blocked:kind=permission:app=terraform:msg=QXBwbHkgMyB0byBhZGQsIDEgdG8gY2hhbmdlLCAwIHRvIGRlc3Ryb3k/ ESC \
This post covers why I think this protocol needs to exist, why the
existing approaches aren't good enough (especially for coding agents),
and how the protocol works.
This is a completely generic, terminal-native specification and protocol.
It emerged from my work on
Superlogical
and
Ghostty
but
the specification
has no product-specific
functionality or language. It is designed as an idiomatic, well-formed
specification that any terminal developer will find familiar.
The Problem
Long-running work is common in terminals: builds, deployments, package
upgrades, data processing, and, more and more today, coding agents. These programs
alternate between working on their own, waiting on the user, and finishing.
Meanwhile, users usually go off and do something else and want to know
when the work finishes or needs them.
Aspects of this problem have been solved in various ways going back decades.
For example, some terminals monitor the active foreground process and have
features to notify when it changes. Or, they wait for some time period of
"quiet" (for various definitions) output. The specification
also
lists the reasons why existing sequences aren't enough
.
Ultimately, I felt there wasn't a cohesive, interaction-agnostic, generic
solution to this problem that conveyed progress, blocking, completion,
and trees of tasks. And it wasn't possible to cobble together pre-existing
sequences to achieve it robustly, either.
Singling Out "Agentic Inboxes"
Don't care about AI, LLMs, etc.? Skip this section.
The problem
is generic and applies in a compelling way without bringing in
AI. It's particularly nasty with AI so I want to call it out, but if you
don't care about any of that, just skip this.
It's now increasingly common for people to run many long-running agents
for any number of reasons: background research, issue monitoring, bug fixing,
large features, etc. Each one works for a while and then stops to ask for
permission, ask a question, or report it's done.
From this, a new category of tool has emerged that I'll simply call
the
agentic inbox
: a single view across every running agent showing
which are working, which are done, and which are waiting on you.
Herdr
,
cmux
, and
Agent Deck
are a few examples
of
hundreds
.
Without a dedicated protocol, they solve the agent status problem in
two ways: heuristics and non-terminal APIs.
Heuristics
The first approach is to guess by reading the screen or the window title
and matching it against known patterns.
Herdr is a good example because it does this well and documents it
openly. Its
detection manifests
are TOML rules that classify an agent as idle, working, or blocked. Here is
the first of 16 rules
for Claude Code:
[[
rules
]]
id
=
"
osc_title_working
"
state
=
"
working
"
priority
=
1100
region
=
"
osc_title
"
visible_working
=
true
# Braille covers <= 2.1.227; half-circles are the 2.1.228 busy spinner.
regex
=
[
'
^[\x{2800}-\x{28FF}\x{25D0}-\x{25D3}]
'
]
Claude Code is considered "working" if its window title starts with a
Braille spinner character or, as of version 2.1.228, a half-circle one.
The
history of that file
shows ten changes in three months for just Claude Code.
This isn't a criticism of Herdr.
Its maintainers are doing the best
possible job with the tools available. But it demonstrates well the
benefit
a unified protocol
would have.
Non-Terminal APIs
The second approach is to have the program report its own state through
an inbox-specific, out-of-band API such as
Herdr's socket API
or
cmux notify
. This is better
than heuristics in some ways, because the program that actually knows its state is the
one reporting it. But every program has to integrate with every inbox
separately, and a local socket doesn't work over SSH or from within a
container without extra bridging. The pty already works across all of this.
The Program Status Protocol
OSC 7501
is a terminal native answer to this problem. The program
reports its own state directly via the pty that it always has, using a
format that is safe to send everywhere (well-behaved terminals ignore
unknown OSCs).
The body of the sequence is a
list of
key=value
pairs
separated by
:
.
The only required key is
state
, which is one of:
state
Meaning
idle
At rest, waiting for the user's next instruction.
working
Running. May include a
progress
percentage.
done
Finished. The result is ready and the user hasn't seen it yet.
blocked
Can't continue until the user does something.
kind
says what (
permission
,
question
, or
auth
) and
msg
says why.
error
Failed and stopped.
Optional keys
include
app
, a stable
machine-readable program name like
cargo
or
claude-code
, and
msg
,
a single human-readable line encoded as base64.
Programs that run several things at once can report multiple records
using
hierarchical ids
. A
deploy tool
can be
working
at the root while
us-east
pushes an image at 40% and
eu-west
is
blocked
waiting for
approval to deploy to production. Both are true at the same time, and
the terminal decides what to show. A
clear
state removes records.
Here's a
complete integration
for a shell script to wrap
rsync
to participate in this protocol:
status
()
{
printf
'
\e]7501;state=%s:msg=%s\e\\
'
"
$1
"
"
$(
printf
'
%s
'
"
$2
"
|
base64
|
tr
-d
'
\n
'
)
"
}
status
working
"
Syncing photos
"
rsync
-a
~/Photos
backup:/photos
&&
status
done
"
Photos synced
"
||
status
error
"
rsync failed
"
Trivial to script with plain old POSIX
sh
.
No SDK, no sockets, no environment variables, no JSON.
No bias towards specific GUI presentations. No bias to any specific
workload (like AI). A well-formed, generic foundation to build functionality
above that anyone and everyone can participate with.
The
full spec
covers the rest:
record lifetime
,
feature detection
,
terminfo
,
size limits
,
and
security
. It's short. I wrote it all by hand. Please read it.
Implement It
I wrote
this specification
based on my experience maintaining a terminal
emulator for many years now. It is written in a way that is easy for
application developers to emit, and easy for terminal emulators to consume
and parse.
I've already implemented this protocol twice. We have one implementation
in
libghostty
and
I have a parallel implementation in
Rex
.
I've also implemented it as a proof-of-concept in Terraform, Claude Code,
Codex, and Homebrew via either plugins or forks. In each case, the
implementation was no more than a dozen lines.
I've been in contact with the maintainers of many popular terminal programs
and emulators and they've helped review and shape the specification.
But if you have any more feedback, I'm happy to hear it.
If you've implemented the specification
please let me know via
email (mail icon in the footer) and I'll add you to the list of tools
that implement this. Thank you.
I'd like us all to stop guessing what programs are doing by reading
their screens or process trees. The program already knows. Let's give it
a way to tell us!
