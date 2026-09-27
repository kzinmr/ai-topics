---
title: "GDB 18.1 released"
url: "https://lwn.net/Articles/1096897/"
fetched_at: 2026-09-27T10:01:14.342677+00:00
source: "LWN.net"
tags: [blog, raw]
---

# GDB 18.1 released

Source: https://lwn.net/Articles/1096897/

Version 18.1 of the GDB interactive debugger has been released.  Changes
include new commands to manipulate the environment of the subprocess, the
ability to save the command history to a file, support for a couple of new
targets, several Python API additions, and more.  See
the
NEWS file
for the complete list.
From
:
Andrew Burgess via Gdb-announce <gdb-announce-AT-sourceware.org>
To
:
gdb-announce-AT-sourceware.org, info-gnu-AT-gnu.org
Subject
:
GDB 18.1 released!
Date
:
Fri, 25 Sep 2026 16:52:55 +0100
Message-ID
:
<6ab698d7.84bf0792.34ed8d.a212@mx.google.com>
Archive-link
:
Article
GDB 18.1 released!

Release 18.1 of GDB, the GNU Debugger, is now available.  GDB is
a source-level debugger for Ada, C, C++, Fortran, Go, Rust, and many
other languages.  GDB can target (i.e., debug programs running on)
more than a dozen different processor architectures, and GDB itself
can run on most popular GNU/Linux, Unix and Microsoft Windows variants.
GDB is free (libre) software.

You can download GDB from the GNU HTTPS server in the directory:
https://ftp.gnu.org/gnu/gdb/?C=M;O=D
The vital stats:

  Size   sha256sum                                                         Name
  22MiB  cd9fc3fe2b47743840e42c1592d3d87f8302eb18639c0b8b4ba0898002e2348f  gdb-18.1.tar.xz
  37MiB  fb83623deb238cab91ad17f8a906e2da26d0b4620fb1da43c20a274252e51082  gdb-18.1.tar.gz

There is a web page for GDB at:
https://www.gnu.org/software/gdb/
That page includes information about GDB mailing lists (an announcement
mailing list, developers discussion lists, etc.), details on how to
access GDB's source repository, locations for development snapshots,
preformatted documentation, and links to related information around
the net.  We will put errata notes and host-specific tips for this release
on-line as any problems come up.  All mailing lists archives are also
browsable via the web.

GDB 18.1 includes the following changes and enhancements:

 * Major improvements to the Windows native target:

   ** Non-stop mode is now supported (requires Windows 10 or later).

   ** Scheduler-locking ("set scheduler-locking on") now works.

   ** Native Thread Local Storage (TLS) variables are now supported.

   ** On the Windows Terminal console, GDB now supports true-color
      24-bit colors, and, when the output codepage is 65001, emoji
      styling and UTF-8 text in general (the host charset is then set
      to UTF-8 automatically).

   ** File names are now consistently shown with forward slashes,
      instead of a mix of slash styles, e.g. "C:/proj/src/main.c"
      instead of "C:/proj/src\main.c".  This affects all interpreters
      (CLI, TUI, GDB/MI, DAP) and everywhere GDB shows a file or
      directory name.

 * GDB now adds all type symbols to the .gdb_index section, fixing
   cases where GDB could fail to find a type when relying on the
   index.  Existing indexes should be regenerated.

 * Improved handling of inferior arguments:

   ** "set args", "run", "start" and "starti" now accept arguments
      containing a newline character, within a quoted argument.

   ** New --no-escape-args command line option for GDB, an alternative
      to --args that does not escape special shell characters within
      the arguments.  gdbserver accepts a --no-escape-args flag with
      the same effect on the inferior arguments.

   ** When connecting to a remote server that supports the new
      qExecAndArgs packet, GDB copies the argument string from the
      server into its own 'args' setting, so that the arguments are
      visible with "show args" and reused by subsequent runs.

 * When connected to an extended-remote target, GDB can now set the
   'remote exec-file' automatically, using the current executable, if
   the remote was not started with an executable and the user did not
   set one explicitly.

 * The add-inferior, clone-inferior and MI -add-inferior commands now
   warn and create the new inferior without a connection when the
   current connection cannot be shared (e.g. core files, or the
   Windows native target).  Sharing these previously tended to crash
   GDB.

 * "info locals" now shows a "shadowed" annotation and location
   information for variables that shadow, or are shadowed by, others.

 * Support for the Floating Point Mode Register (FPMR) on AArch64.

 * GDB now supports libipt v2.2 events originating from Event Tracing
   ("set record btrace pt event-tracing on") on a FRED-enabled system,
   and from Trigger Tracing.

 * GDB now supports arbitrary (non-standard) baud rates for serial
   connections on systems whose libc accepts them through
   cfsetispeed/cfsetospeed, such as glibc 2.42 and later, and GNU Hurd.

 * "info inferiors" now shows the core file loaded in an inferior, if
   any.

 * New "essential" help command class, listing what we believe is
   close to a minimal set of commands for a new GDB user.

 * New commands:

   ** "set/show/unset local-environment", analogs of the "environment"
      commands, affecting the environment of subprocesses started by
      GDB itself, such as those started by "shell" and "pipe".

   ** "save history", "save skip" and "save user", to save the command
      history, the current skips, and the user-defined commands to a
      file.

   ** "info proc environ", to print the initial environment variables
      of a process (Linux only).

   ** "set/show progress-bars enabled", to disable the progress bars
      GDB shows for long operations, such as while debuginfod
      downloads content.

   ** "delete skip", "enable skip" and "disable skip", new aliases for
      "skip delete", "skip enable" and "skip disable".

   ** "set/show debug gnu-ifunc" and "set/show debug ctf".

 * New targets:

   ** GNU/Linux/MicroBlaze (gdbserver)  microblazeel-*linux*

   ** AArch64 MinGW                     aarch64-*-mingw*

 * Python API enhancements:

   ** New gdb.Corefile class, representing a loaded core file, with
      the new Inferior.corefile attribute, plus the new
      gdb.CorefileMappedFile and gdb.CorefileMappedFileRegion types
      describing the files mapped when the core file was created.

   ** New gdb.Style class, gdb.StyleParameterSet class, and
      gdb.INTENSITY_* constants, for representing styles and creating
      custom "set/show style NAME ..." parameters.  gdb.write() takes
      a new optional 'style' argument.

   ** New gdb.events.selected_context event registry, emitting a
      SelectedContextEvent whenever the user changes the selected
      inferior, thread or frame.

   ** New gdb.events.corefile_changed event registry, emitting a
      CorefileChangedEvent whenever the core file of an inferior
      changes.

   ** New gdb.Symtab.source_lines method, returning the source lines
      of the file associated with a symtab.

   ** The Architecture.disassemble method accepts a new 'styling'
      argument, to get ANSI escape sequences in the assembly strings.

   ** New gdb.Block.ranges attribute, listing the ranges of a block.

 * Debugger Adapter Protocol changes:

   ** Unhandled Ada exceptions can now be caught using the "unhandled"
      exception filter.

   ** The launch and attach requests accept a new adaSourceCharset
      parameter, and the attach request accepts a new coreFile
      parameter.

   ** Constants are now returned in scopes.

 * Remote protocol changes:

   ** New qExecAndArgs packet, returning the executable file name and
      argument string the server was started with.

   ** New single-inf-arg qSupported feature, letting GDB send the
      inferior arguments as a single string in the vRun packet.

 * Incompatible changes:

   ** Support for the stabs and mdebug debug information formats, and
      for the dbx binary file format, has been removed.

   ** Support for the Common Trace Format (CTF) has been removed:
      trace information is now saved exclusively in GDB's own "tfile"
      format, the "target ctf" command is gone, and "tsave" and MI
      "-trace-save" no longer accept the "-ctf" flag.  The
      --with-babeltrace configure option has been removed as well.

   ** Support for .gdb_index sections older than version 7 has been removed.

   ** Support for DWP (DWARF Package File) version 1 has been removed.

   ** The format of execution records saved by "record save" has
      changed; previous formats are no longer supported.

   ** Guile 2.2 is now the minimum supported Guile version, and the
      deprecated memory port buffer size procedures have been
      removed; use 'setvbuf' instead.

   ** The "maint check psymtabs", "maint info psymtabs" and "maint
      print psymbols" commands have been removed, as GDB no longer
      uses partial symbol tables internally.

   ** "maintenance info program-spaces" no longer displays the core
      file name; use "info inferiors" instead.

   ** GDB no longer supports AIX 7.1; the minimum supported version is
      now AIX 7.2 TL5, and only DWARF debug information is supported
      on AIX going forward.

   ** The s390 32-bit target (s390-*) is deprecated and planned for
      removal in a future release, along with the elf32-s390 target
      format.  configure now errors out for this target, which can be
      overridden with --enable-obsolete.  The s390 64-bit target
      (s390x-*) remains supported.

For a complete list and more details on each item, please see the gdb/NEWS
file, available at:
https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;...
-- 
Andrew Burgess
