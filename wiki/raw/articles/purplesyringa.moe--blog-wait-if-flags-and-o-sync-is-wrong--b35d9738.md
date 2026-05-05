---
title: "Wait, if (flags & O_SYNC) is wrong?"
url: "https://purplesyringa.moe/blog/./wait-if-flags-and-o_sync_is-wrong/"
fetched_at: 2026-05-05T07:02:08.588754+00:00
source: "Alisa Sireneva (PurpleSyringa)"
tags: [blog, raw]
---

# Wait, if (flags & O_SYNC) is wrong?

Source: https://purplesyringa.moe/blog/./wait-if-flags-and-o_sync_is-wrong/

Wait, if (flags & O_SYNC) is wrong?
April 23, 2026
I needed to convert
file status flags
between operating systems yesterday. They are the values you pass as the second argument to
open
–
O_NONBLOCK
,
O_NOATIME
,
O_SYNC
,
O_DSYNC
, and so on:
int
open
(
const
char
*path,
int
flags,  )
;
So naturally I wrote it like this:
int
dst_flags =
0
;
if
(src_flags & SRC_O_NONBLOCK) dst_flags |= DST_O_NONBLOCK;
if
(src_flags & SRC_O_NOATIME) dst_flags |= DST_O_NOATIME;
if
(src_flags & SRC_O_SYNC) dst_flags |= DST_O_SYNC;
if
(src_flags & SRC_O_DSYNC) dst_flags |= DST_O_DSYNC;
...
It turns out this code has a subtle bug.
Man pages
Here’s what
Linux man pages
say:
The argument
flags
must include one of the following access modes:
O_RDONLY
,
O_WRONLY
, or
O_RDWR
. These request opening the file read-only, write-only, or read/write, respectively.
In addition, zero or more file creation flags and file status flags can be bitwise ORed in
flags
.
So I can’t do
if (src_flags & SRC_O_RDWR)
, because
O_RDWR
is not a bit flag and may be a bit field instead. For example, Linux uses a 2-bit field for the access mode, assigning
O_RDONLY
to
0
, so
if (src_flags & O_RDONLY)
would never trigger:
#
define
O_ACCMODE      0003
#
define
O_RDONLY         00
#
define
O_WRONLY         01
#
define
O_RDWR           02
…but the other flags should be fine – they can be bitwise ORed after all.
History
Except, it turns out, that’s not actually true. I was interested to see how compilers handled this kind of bit permutation, but what I found after looking at the disassembly was
not
pure bit permutation. It turns out that, if you look at
bits/fcntl-linux.h
, you’ll find that
O_SYNC
is defined as having
two
bits (that’s octal, in hex it’d be
0x101000
):
#
ifndef
O_SYNC
#
define
O_SYNC        04010000
#
endif
So
why
does it do that and what do the individual bits mean? We can find the answer
in Linux headers
:
#
ifndef
O_DSYNC
#
define
O_DSYNC     00010000
#
endif
...
#
ifndef
O_SYNC
#
define
__O_SYNC    04000000
#
define
O_SYNC      (__O_SYNC|O_DSYNC)
#
endif
Let me make it clearer.
O_SYNC
and
O_DSYNC
are two flags controlling data integrity:
O_DSYNC
makes
write
wait until file contents are flushed to disk.
O_SYNC
makes
write
wait until file contents
and metadata
are flushed to disk.
So
O_SYNC
is a semantic superset of
O_DSYNC
.
On old Linux,
O_SYNC
was
00010000
. Old Linux didn’t flush metadata on
O_SYNC
, and didn’t have
O_DSYNC
. So new Linux reused that constant for
O_DSYNC
, to ensure that programs compiled for old Linux exhibited the same behavior on new Linux.
To ensure that programs compiled with new Linux headers
worked on old Linux
as best as they could, the new
O_SYNC
value needed to contain the old
O_SYNC
value as a submask. So
O_SYNC
had to become
00010000
(new
O_DSYNC
) plus something else for disambiguation. The new bit
__O_SYNC
took that role.
When the kernel checks the flags, it
almost always uses
one of the following patterns:
To flush file contents:
if (flags & O_DSYNC)
or
if (flags & O_SYNC)
interchangeably.
To flush metadata:
if (flags & __O_SYNC)
.
Bug
So when you write
if (flags & O_SYNC)
, you aren’t testing whether the caller wrote
O_SYNC
– this will match both
O_SYNC
and
O_DSYNC
. On Linux,
if
(flags & O_SYNC) flags |= O_SYNC;
…is not a no-op, and will turn on the more costly metadata flushing even if only contents flushing was requested. Furthermore, if code like this is used not only to
create
file descriptors, but also to
validate
their mode, this can be a correctness issue.
The right way to map flags is:
if
((src_flags & SRC_O_SYNC) == SRC_O_SYNC) dst_flags |= DST_O_SYNC;
People rarely need to parse file status flags by hand, but when they do, this mistake is common. For example, here’s
WasmEdge reporting pure-
O_DSYNC
fds as
O_SYNC
:
if
(FdFlags & O_SYNC) {
  FdStat.fs_flags |= __WASI_FDFLAGS_RSYNC | __WASI_FDFLAGS_SYNC;
}
And same for
WAVM
:
if
(fdFlags & O_SYNC)
{
#
ifdef
O_RSYNC
outInfo.flags.syncLevel = fdFlags & O_RSYNC
                                  ? VFDSync::contentsAndMetadataAfterWriteAndBeforeRead
                                  : VFDSync::contentsAndMetadataAfterWrite;
#
else
outInfo.flags.syncLevel = VFDSync::contentsAndMetadataAfterWrite;
#
endif
}
Here’s
YouTube’s Cobalt miswrapping
fcntl
:
if
(flags & MUSL_O_SYNC) {
  platform_flags |= O_SYNC;
}
Maybe you can find more bugs in popular programs.
O_RSYNC
Bonus bug!
POSIX defines
the
O_RSYNC
flag, which requests file contents or metadata (depending on whether it’s used together with
O_DSYNC
or
O_SYNC
) to be additionally flushed before each read. Linux doesn’t implement these semantics – instead, it aliases
O_RSYNC
to
O_SYNC
.
This is bonkers, because
O_RSYNC
alone is supposed to be a no-op. In fact, since POSIX says this is an
optional
flag, Linux could simply not
#define
it, and POSIX-compliant programs with
#ifdef O_RSYNC
would keep working. But whatever.
Since
O_SYNC = O_RSYNC
, even
if ((flags & O_RSYNC) == O_RSYNC) ...
can both overpromise (if you assume this indicates the kernel flushes on reads, when it doesn’t) and overdeliver (if the target OS supports true
O_RSYNC
, this may map
O_SYNC
to the more expensive
O_SYNC | O_RSYNC
).
For example, here’s
Ceph always interpreting
O_SYNC
as
O_SYNC | O_RSYNC
:
int64_t
Client::_read(Fh *f,
int64_t
offset,
uint64_t
size, bufferlist *bl,
                      Context *onfinish,
bool
read_for_write)
{
  ...
if
(f->flags & O_RSYNC) {
      _flush_range(in, offset, size);
    }
I believe both WasmEdge and WAVM are also in the wrong here by promising
O_RSYNC
on Linux, but it’s unclear if this can be solved without OS-level support.
Bonus bonus
Added later today:
It turns out that
O_TMPFILE
is
also
not a single bit – it’s a mask containing
O_DIRECTORY
, so
if (flags & O_TMPFILE)
erroneously catches
O_DIRECTORY
. This is a rarer mistake, but people still make it. Here’s one in
libvips
:
if
(
#
ifdef
O_TMPFILE
!(flags & O_TMPFILE) &&
#
endif
g_file_test(filename, G_FILE_TEST_IS_DIR)) {
    errno = EISDIR;
return
-1
;
  }
It deliberately validates that the opened file is not a directory, but accidentally allows opening a directory if
O_DIRECTORY
is set. This is probably not intended.
And it seems like the Linux kernel itself
committed this bug
two weeks ago in CIFS, erroneously trying to remove directories opened with
O_DIRECTORY
on close:
if
(oflags & O_TMPFILE)
    opts |= CREATE_DELETE_ON_CLOSE;
Uh-oh! I think I should
report this
.
Conclusion
My advice.
For
O_SYNC
:
(flags & O_SYNC) == O_SYNC
is cross-platform and does the right thing. Same for
O_TMPFILE
.
For
O_RSYNC
: honestly, YOLO it. Its semantics differ across many operating systems, with Linux not supporting
O_RSYNC
and instead enabling
O_SYNC
,
NetBSD
only implementing
O_RSYNC | O_SYNC
, but not
O_RSYNC | O_DSYNC
, and other OSes doing who knows what. There’s no telling what
O_RSYNC
will look like if Linux implements it, so you can’t really prepare for that.
