---
title: "complected and orthogonal persistence"
url: "https://jyn.dev/complected-and-orthogonal-persistence/"
fetched_at: 2026-04-28T07:02:50.790297+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# complected and orthogonal persistence

Source: https://jyn.dev/complected-and-orthogonal-persistence/

Everything Not Saved Will Be Lost
—Ancient Nintendo Proverb
persistence is hard
say that you are writing an editor. you don't want to lose people's work so you implement an "autobackup" feature, so that people can restore their unsaved changes if the program or whole computer crashes.
implementing this is hard
! the way i would do it is to serialize the data structures using something like
bincode
and then write them to an SQLite database so that i get crash-consistency. there are other approaches with different tradeoffs.
languages with persistence
this
1983 paper
asks: why are we spending so much time rewriting this in applications, instead of doing it once in the runtime? it then introduces a language called "PS-algol", which supports exactly this through a library. note that arbitrary data types in the language are supported without the need for writing user code.
it turns out that this idea is already being used in production. not in that form—people don’t use Algol anymore—but the idea is the same. M (better known as
MUMPS
),
Bank Python
, and the
IBM i
are still used in healthcare, financial, and insurance systems, and they work exactly like this. here is a snippet of M that persists some data to a database:
SET
^table(
"
column
"
,
"
primary key
"
)=
"
value
"
and here is some Bank Python that does the same:
db
[
"
/my_table
"
]
=
Table
(
[
(
"
etf
"
,
str
)
,
(
"
shares
"
,
float
)
]
,
[
"
SPY
"
,
1200
.
0
]
)
and finally some COBOL:
IDENTIFICATION DIVISION
.
PROGRAM-ID
.
FILES
.
ENVIRONMENT DIVISION
.
INPUT-OUTPUT SECTION
.
FILE-CONTROL
.
SELECT
TRANSACTIONS
ASSIGN
TO
'
transactions.txt
'
ORGANIZATION
IS
SEQUENTIAL
.
DATA DIVISION
.
FILE SECTION
.
FD
TRANSACTIONS
.
01
TRANSACTION-STRUCT
.
02
UID
PIC 9(5).
02
DESC
PIC X(25).
WORKING-STORAGE SECTION
.
01
TRANSACTION-RECORD
.
02
UID
PIC 9(5)
VALUE
12345
.
02
DESC
PIC X(25)
VALUE
'
TEST TRANSACTION
'
.
PROCEDURE DIVISION
.
OPEN
OUTPUT
TRANSACTIONS
WRITE
TRANSACTION-STRUCT
FROM
TRANSACTION-RECORD
CLOSE
TRANSACTIONS
STOP RUN
.
note how in all of these, the syntax for persisting the data to disk is essentially the same as persisting it to memory (in MUMPS, persisting to memory is exactly the same, except you would write
SET table
instead of
SET ^table
).
if you don't require the runtime to support all datatypes, there are frameworks for doing this as a library.
protobuf
and
flatbuffer
both autogenerate the code for a restricted set of data types, so that you only have to write the code invoking it.
orthogonal persistence
the thing these languages and frameworks have in common is that the persistence is part of the program source code; either you have to choose a language that already has this support, or you have to do extensive modifications to the source code to persist the data at the right points. i will call this kind of persistence
complected persistence
because they tie together the business logic and persistence logic (see
Simple Made Easy
by Rich Hickey for the history of the word "complect").
there is also
orthogonal persistence
.
"orthogonal persistence"
means your program's state is saved automatically without special work from you the programmer. in particular, the serialization is managed by the OS, database, or language runtime. as a result, you don't have to care about persistence, only about implementing business logic; the two concerns are
orthogonal
.
orthogonal persistence is more common than you might think. some examples:
hibernation
(suspend to disk). first invented in 1992 for the Compaq
LTE Lite
. Windows has this on by default since Windows 8 (2012). MacOS has had it on by default since OS X 10.4 (2005).
virtualized hibernation in hypervisors like VirtualBox and VMWare (usually labeled "Save the machine state" or something similar)
how far can we take this?
these forms of orthogonal persistence work on the whole OS state. you could imagine a version that works on individual processes: swap the process to disk, restore it later. the kernel kinda already does this when it does scheduling. you can replicate it in userspace with
telefork
, which even lets you spawn a process onto another machine.
but the rest of the OS moves on while the process is suspended: the files it accesses may have changed, the processes it was talking to over a socket may have exited. what we want is to snapshot the process state: whatever files on disk stay on disk, whatever processes it was talking to continue running. this allows you to rewind and replay the process, as if the whole thing were running in a database transaction.
what do we need in order to do that?
a filesystem that supports atomic accesses, snapshots, and transaction restarts, such as
ZFS
.
a runtime that supports detailed tracking and replay of syscalls, such as
rr
. this works by intercepting syscalls with
ptrace()
, among other mechanisms, and does not require any modifications to the program executable or source code.
a sandbox that prevents talking to processes that weren’t running when the target process was spawned (unless those processes are also in the sandbox and tracked with this mechanism), such as
bubblewrap
.
effectively, we are turning syscalls into
capabilities
, where the capabilities we give out are “exactly the syscalls the process made last time it spawned”.
note how this is possible to do today, with existing technology and kernel APIs! this doesn’t require building an OS from scratch, nor rewriting all code to be in a language with tracked effects or a capability system. instead, by working at the syscall interface between the program and the kernel, we can build a highly general system that applies to all the programs you already use.
“but why?”
note that this involves 3 different levels of tracking, which we can think of in terms of progressive enhancement:
features you can get just by recording and replaying the whole process ("tracking between processes")
features you can get by replaying from a specific point in the process ("tracking within a process")
features you can only get with source code changes, by allowing the process to choose where it should be restored to ("tracking that needs source code changes")
the editor example i gave at the beginning refers to 3; but you can get really quite a lot of things just with 1 (tracked record/replay and transactional semantics). for example, here are some tools that would be easy to build on top:
needs tracking between processes
collaborative terminals, where you can “split” your terminal and hand a sandboxed environment of
your personal computer
to a colleague so they can help you debug an issue. this is more general than OCI containers because you don't need to spend time creating a dockerfile that reproduces the problem. this is more general than
rr pack
because you can edit the program source to add printfs, or change the input you pass to it at runtime.
“save/undo for your terminal”, where you don’t need to add a
--no-preserve-root
flag to
rm
, because the underlying filesystem can just restore a snapshot. this generalizes to any command—for example, you can build an arbitrary
git undo
command that works even if installed after the data is lost, which is
not possible today
. note that this can undo by-process, not just by point-in-time, so it is strictly more general than FS snapshots.
query which files on disk were modified the last time you ran a command. for example you could ask “where did this
curl | sh
command install its files?”. the closest we have to this today is
dpkg --listfiles
, which only works for changes done by the package manager.
needs tracking within a process
needs source code changes
“save/undo for your program”, where editors and games can take advantage of cheap snapshots to use the operating system's restore mechanism instead of building their own.
this is not an exhaustive list, just the first things on the top of my head after a couple days of thinking about it. what makes this orthogonal persistence system so useful is that all these tools are near-trivial to build on top: most of them could be done in shell scripts or a short python script, instead of needing a team of developers and a year.
isn’t this horribly slow?
not inherently. “turning your file system into a database“ is only as slow as submitting the query is—and that can be quite fast when the database runs locally instead of over the network; see
sled
for an example of such a DB that has had performance tuning. rr boasts
less than a 20% slowdown
. bubblewrap uses the kernel’s native namespacing and to my knowledge imposes no overhead.
now, the final system needs to be designed with performance in mind and then carefully optimized but, you know. that's doable.
does this work across versions of my program?
kinda. there are two possible ways to implement intra-process persistence (i.e. "everything other than disk writes").
take a snapshot of the memory, registers, and kernel state (e.g. file descriptors). this is how
telefork
works. this only works with a single version of the executable; any change, even LTO without changing source code, will break it.
replay all syscalls done by the process. this will work across versions, as long as the program makes the same syscalls in the same order.
1 is cheap if you don't have much memory usage compared to CPU time.
2 is cheap if you don't have much CPU time compared to memory usage.
only 2 allows you to modify the binary between saving and restoring.
it's possible to do both for the same process, just expensive.
summary
persisting program state is hard and basically requires implementing a database
persistence that does not require action from the program is called “orthogonal persistence”
it is possible to build orthogonal persistence for individual processes with tools that exist today, with only moderate slowdowns depending on how granular you want to be
there are multiple possible ways to implement this system, with different perf/generality tradeoffs
such a system unlocks many kinds of tools by making them orders of magnitude easier to build
many of the ideas in this post were developed in collaboration with edef. if you want to see them built, consider
sponsoring her
so she has time to work on them.
bibliography
Dan Luu, "Files are hard"
Ty Overby, Zoey Riordan, Victor Koenders,
bincode
Atkinson, M.P., Bailey, P.J., Chisholm, K.J., Cockshott, W.P. & Morrison, R. “PS-algol: A
Language for Persistent Programming”. In Proc. 10th Australian National Computer
Conference, Melbourne, Australia (1983) pp 70-79.
Cal Paterson, "An oral history of Bank Python"
Hugo Landau, "IBM i: An Unofficial Introduction"
Google LLC, "Protocol Buffers"
Google LLC, "FlatBuffers Docs"
Rich Hickey, "Simple Made Easy"
Tristan Hume, "Teleforking a process onto a different computer!"
Robert O’Callahan et al., "RR"
Simon McVittie et al., "bubblewrap"
Chip Morningstar and F. Randall Farmer, "What Are Capabilities?"
Robert O'Callahan, "rr Trace Portability"
Free Software Foundation, Inc., "GNU Coreutils"
Waleed Khan, "git undo: We can do better"
Marcin Kulik, "Record and share your terminal sessions, the simple way."
Jade Lovelace, "The postmodern build system"
Salsa developrs, "About salsa"
The Rust Project contributors, "Incremental compilation in detail"
Tyler Neely, "sled - it's all downhill from here!!!"
edef
The PostgreSQL Global Development Group, "Reliability and the Write-Ahead Log: Write-Ahead Logging (WAL)"
Yvan Scher, "7 cobol examples with explanations."
Robert N. M. Watson et al., "CTSRD – Rethinking the hardware-software interface for security"
WebAssembly Working Group, "WebAssembly"
Rob Pike, "Systems Software Research is Irrelevant"
System Calls Manual, "ptrace(2)"
dpkg suite, "dpkg(1)"
Wikipedia, "MUMPS"
Wikipedia, "orthogonal persistence"
Wikipedia, "IBM i"
Wikipedia, "ZFS"
Wikipedia, "Orthogonality"
Wikipedia, "Hibernation (computing)"
Wikipedia, "Compaq LTE Lite"
