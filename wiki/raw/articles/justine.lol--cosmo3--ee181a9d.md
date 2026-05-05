---
title: "Cosmopolitan Third Edition"
url: "https://justine.lol/cosmo3/"
fetched_at: 2026-05-05T07:01:27.337731+00:00
source: "Justine Tunney"
tags: [blog, raw]
---

# Cosmopolitan Third Edition

Source: https://justine.lol/cosmo3/

Oct 31
st
, 2023 @
justine's web page
Updated on Jan 5
th
, 2025
Cosmopolitan Third Edition
Cosmopolitan Honeybadger
After nearly one year of development, I'm pleased to announce our
version
3.0
release of the Cosmopolitan library. The project is an entirely
new animal. For starters, Mozilla sponsored our work as part of
their
MIECO program
.
Google also
awarded
me an open source peer bonus
for my work on Cosmopolitan, which is a
rare honor, and it's nice to see our project listed up there among the
greats, e.g. curl, linux, etc. In terms of this release, we're living up
to the great expectations you've all held for this project in a number
of ways. The first is we invented a new linker that lets you build fat
binaries which can run on these platforms:
AMD64
Linux
MacOS
Windows
FreeBSD
OpenBSD 7.3
NetBSD
ARM64
Linux
MacOS
FreeBSD
Windows (non-native)
It's called
apelink.c
and it's a fine piece of poetry that weaves together the Portable
Executable, ELF, Mach-O, and PKZIP file formats into shell scripts that
run on most PCs and servers without needing to be installed. This is an
idea whose time has come; POSIX
even
changed
their rules
about binary in shell scripts specifically to let us do
it. So we've been using it to create a "Fat Linux Distro" which I've
named the "Cosmos". In the Cosmos, every program is statically linked
and contains a PKZIP central directory where its /usr/share dependencies
are embedded. You can think of it as a coalition of individualistic
executables, where each program can be separated from the whole and run
on other OSes. So far it includes programs like Emacs, Vim, CoreUtils,
Curl, etc.
cosmos-4.0.2.zip
385mb - PE+ELF+MachO+ZIP+SH executables
For AMD64+ARM64 on Linux+Mac+Windows+FreeBSD+NetBSD+OpenBSD
494ecbd87c2f2f622f91066d4fe5d9ffc1aaaa13de02db1714dd84d014ed398f
More specifically, the above zip file contains fat binaries for
bash
,
emacs
,
python
,
zsh
,
lua
,
qjs
,
vim
,
nano
,
ape
,
less
,
grep
,
curl
,
wget
,
tidy
,
zip
,
unzip
,
zstd
,
bzip2
,
sqlite3
,
life
,
cpuid
,
nesemu1
,
make
,
redbean
,
greenbean
,
datasette
,
assimilate
,
ctags
,
pledge
,
verynice
,
find
,
tree
,
awk
,
[
,
b2sum
,
base32
,
base64
,
basename
,
basenc
,
berry
,
brotli
,
cat
,
chcon
,
chgrp
,
chown
,
chroot
,
cksum
,
clang-format
,
comm
,
csplit
,
cut
,
dash
,
date
,
df
,
dir
,
dircolors
,
dirname
,
du
,
echo
,
emacsclient
,
env
,
expand
,
expr
,
factor
,
false
,
fmt
,
fold
,
groups
,
head
,
id
,
install
,
join
,
kill
,
link
,
links
,
ln
,
locate
,
logname
,
ls
,
lz4
,
md5sum
,
mkfifo
,
mknod
,
mktemp
,
mktemper
,
nice
,
ninja
,
nl
,
nohup
,
nproc
,
numfmt
,
od
,
paste
,
pathchk
,
pigz
,
pinky
,
pr
,
printenv
,
printf
,
printimage
,
ptx
,
pwd
,
pypack1
,
readlink
,
realpath
,
rm
,
rmdir
,
rsync
,
runcon
,
script
,
sed
,
seq
,
sha1sum
,
sha224sum
,
sha256sum
,
sha384sum
,
sha512sum
,
shred
,
shuf
,
sleep
,
sort
,
split
,
stat
,
stty
,
sum
,
sync
,
tac
,
tail
,
tar
,
tee
,
test
,
timeout
,
tmux
,
touch
,
tr
,
true
,
truncate
,
tsort
,
tty
,
ttyinfo
,
unbourne
,
unexpand
,
uniq
,
unlink
,
uptime
,
users
,
vdir
,
wall
,
wc
,
who
,
whoami
,
xargs
,
xz
, and
yes
. They can also be downloaded individually
at
https://cosmo.zip/pub/cosmos/bin/
.
This only became possible in the last few months, in part thanks to
Gautham Venkatasubramanian, who spent a few weekends of his PhD studies
modifying
the C language
so it's possible to build conventional software with
Cosmopolitan. Since then it's been out of the frying pan and into the
fire, testing our library to see if it can support some of the most
complex and mature projects in the open source community. Running the
./configure
scripts and
make check
rules of
projects (e.g. GMP) has done so much to help us fix bugs and battle test
new features.
One of the things we're most happy with, is that Cosmo's cross platform
support is now good enough to support Cosmo development. We've
traditionally only compiled code on x86 Linux. Devs using Cosmo would
build their programs on Linux, and then copy the binaries to other OSes.
Focusing on Linux-only helped us gain considerable velocity at the start
of the project; the Cosmopolitan monorepo has two million lines of code.
Today was the first day the whole thing compiled on Apple Silicon and
Microsoft Windows systems, and using Cosmo-built tools.
Windows Improvements
In order to get programs like GNU Make and Emacs to work on Windows, we
implemented
new
libraries for POSIX signals emulation
. Cosmopolitan is now able to
preempt i/o and deliver asynchronous signals on Windows, using
a
SetThreadContext()
trick
I learned from the Go developers. Cosmo does a considerably
better
job
spawning
processes
now too. For example, we wrote
a
brand
new
posix_spawn()
function
that
goes
10x faster
than
the
posix_spawn()
included with Cygwin.
Cosmo's
execve()
can now reparent
subprocesses,
inherit
non-stdio file descriptor
, and
our
read()
function now contains a termios driver
which, for the first time,
lets us
poll()
standard input on consoles. Cosmo binaries
cleanly integrate with WIN32, depending pretty much only on KERNEL32,
and your fat binaries won't have to live on a separate partition like
WSL.
MacOS Improvements
While MacOS may not be the prodigal child of our support vector, this
release brings improvements to MacOS users that are equally important.
For starters, we now have first-class native ARM64
support.
APE
Loader
also now dynamically links the officially blessed Apple
libraries (e.g. libSystem.dylib) on ARM64, so there's less chance that
Apple will break your binaries. We've also
made
semaphores
and
futexes
much better on XNU, thanks to Grand Central Dispatch, and ulock on
AMD64.
Portability and Performance (Pick Two)
The end result is that if you switch your Linux build process to
use
cosmocc
instead of
cc
then the programs
you build, e.g. Bash and Emacs, will just work on the command prompts of
totally different platforms like Windows and MacOS, and when you run
your programs there, it'll
feel
like you're on Linux. However
portability isn't the only selling point. Cosmo Libc will make your
software faster and use less memory too. For example, when I build Emacs
using the cosmocc toolchain, Emacs thinks it's building for Linux. Then,
when I run it on Windows:
It actually goes 2x faster than the native WIN32 port that the Emacs
authors wrote on their own. Cosmo Emacs loads my dotfiles in 1.2 seconds
whereas GNU Emacs on Windows loads them in 2.3 seconds. Many years ago
when I started this project, I had this unproven belief that portability
toil could be abstracted by having a better C library. Now I think this
is all the proof we need that it's not only possible to make software
instantly portable, but actually
better
too. For example, one
of the things you may be wondering is, "these fat binary files are huge,
wouldn't that waste memory?" The answer is no, because Cosmo only pages
into memory the parts of the executable you need. Take for example one
of Linux's greatest hits: the Debian Almquist shell.
$ ls -hal /usr/bin/dash
-rwxr-xr-x 1 root root
107K
Nov 21  2022 /usr/bin/dash
$ ls -hal /opt/cosmos/bin/dash
-rwxr-xr-x 1 jart jart
983K
Oct 15 19:14 /opt/cosmos/bin/dash
Here we see Cosmo's six OS + two architecture fat binary dash is 30%
bigger than the one that comes with Alpine Linux (which only supports
x86-Linux and dynamically links a separate 600kb Musl library). But if I
run them:
$ rusage /usr/bin/dash -c true
took 231µs wall time
ballooned to
688kb
in size
needed 183us cpu (0% kernel)
caused 34 page faults (100% memcpy)

$ rusage /opt/cosmos/bin/dash -c true
took 217µs wall time
ballooned to
544kb
in size
needed 172us cpu (0% kernel)
caused 36 page faults (100% memcpy)
Here we see Cosmo's fat binary version of dash went faster and used less
memory than an x86-Linux-only binary built for Musl Libc. This is due to
(1) the magic of modern memory management, where CPU MMUs lazily load
4096 byte blocks at a time; and (2) how carefully
apelink
plans your executable layout. For example, all that code which is needed
to support Windows (it takes a lot of code to support Windows) gets
linked into its own special section of the binary, far away from what
the MMU will want to page on UNIX systems. The same goes for the
embedded ARM64 build. Since I'm running on AMD64 here, the ARM64 code is
never loaded off disk.
You no longer need to choose between the amalgamation release or the
cosmo monorepo. We now have a third preferred option, which is our
new
cosmocc
command. It works pretty much the same as
the
cc
command you already know. It's distributed as a
self-contained zip file with all the compiler binaries, scripts, tools,
headers, and static libraries you'll need. You can extract it to any
directory you want. In other words, it's path agnostic, and it needn't
be placed on the
$PATH
in order to use it.
cosmocc-4.0.2.zip
422mb - PE+ELF+MachO+ZIP+SH executables
For AMD64+ARM64 on Linux+Mac+Windows+FreeBSD+NetBSD+OpenBSD
85b8c37a406d862e656ad4ec14be9f6ce474c1b436b9615e91a55208aced3f44
Here's an example of how to get started:
mkdir cosmocc
cd cosmocc
wget https://cosmo.zip/pub/cosmocc/cosmocc-4.0.2.zip
unzip cosmocc-4.0.2.zip
printf
'#include <stdio.h>\nint main() { printf("hello world\\n"); }'
>hello.c
bin/cosmocc -o hello hello.c
./hello
Congratulations. You've just created a fat ape binary that'll run on six
OSes and two architectures. If you're a C++ developer, then you can
use
bin/cosmoc++
. If you want to debug your program with
GDB, then the command above also creates the
hello.com.dbg
(x86-64 ELF) and
hello.aarch64.elf
(x86-64 arm64) output
files. You can debug your program using Cosmo's
./hello
--strace
and
./hello --ftrace
flags.
Windows Notes
Since
cosmocc
is a bourne shell script that wraps raw gcc
binaries, Windows users will need a UNIX shell before running the above
commands.
The
cosmos-4.0.2.zip
file at the top of this page contains a bin/ folder. It's recommended
that Windows users extract it to
C:\bin
. Then
install
Terminal
Preview
from the Microsoft Store, and configure it so that it
launches
C:\bin\bash -l
as your shell. You'll naturally
need a good unzip program in order to do this: one that supports
symbolic links (a.k.a. reparse points). You can download the
InfoZIP
unzip
command directly from the cosmo.zip server by
running
curl -o unzip.exe
https://cosmo.zip/pub/cosmos/bin/unzip
in PowerShell.
Building Open Source Software
Assuming you put
cosmocc/bin/
on your
$PATH
,
integrating with GNU Autotools projects becomes easy. The trick here is
to use a
--prefix
that
only
contains software
that's been built by cosmocc. That's because Cosmopolitan Libc uses a
different ABI than your distro.
export
CC=
"cosmocc -I/opt/cosmos/include -L/opt/cosmos/lib"
export
CXX=
"cosmoc++ -I/opt/cosmos/include -L/opt/cosmos/lib"
export
PKG_CONFIG=
"pkg-config --with-path=/opt/cosmos/lib/pkgconfig"
export
INSTALL=
"cosmoinstall"
export
AR=
"cosmoar"
./configure --prefix=/opt/cosmos
make -j
make install
Full Documentation
The full documentation for using cosmocc is in the
cosmocc/README.md
file. It's viewable offline if you run
bin/cosmocc --help
in your terminal. See
also
ahgamut/superconfigure
repository for the largest source of high-quality examples on how to
build open source software using Cosmo. We also have
a
GitHub Wiki and
FAQ
that's open to public editing.
This cosmos release includes the latest version of
the
redbean web server
. This is a fat
single-file forking Lua+SQLite+MbedTLS stack written by the Cosmopolitan
authors originally to showcase the capabilities of the library for
greenfield development. Cosmopolitan is good for more than just building
old GNU code and redbean proves that. It's
the
third most upvoted
hobby
project in Hacker News history. A few weeks ago Berwyn
Hoyt
independently
determined
it to be the fastest Lua web server too!
One of the reasons why redbean is a forking web server is because we
didn't develop our own
POSIX
Threads implementation
until last year. So we put a lot of thought
into writing an example of how you can build a bare minimal threaded web
server that's
even faster
than redbean, and it's called
greenbean. There's a prebuilt fat binary for it in the cosmos.zip
distribution above. Greenbean is
400
lines of liberally commented perfection
. I still can't believe how
good we got its memory usage, thanks to tricks
like
MAP_GROWSDOWN
. On Linux, if I ask greenbean to spawn
over 9,000 persistent worker threads:
$ sudo prlimit --pid=$$ --nofile=18000
$ sudo prlimit --pid=$$ --nproc=18000
$ rusage greenbean 9001
listening on http://127.0.0.1:8080
listening on http://10.10.10.237:8080
greenbean workers=0 connections=0 messages=0 ^C shutting down...
took 7,959,324µs wall time
ballooned to
40,352kb
in size
needed 929,917us cpu (92% kernel)
caused 10,039 page faults (100% memcpy)
54,689 context switches (99% consensual)
Then it somehow only uses 40mb of peak resident memory, and according to
htop, greenbean's virtual memory usage is 76,652kb. That's for 9,001
threads. Like redbean, greenbean is able to handle hundreds of thousands
of requests per second on my Intel Core i9-9900, except (1) greenbean
has better shared memory support, (2) it sets up and tears down
connections faster, and (3) it lets you experience the joy of using Mike
Burrows'
*NSYNC
library,
which is the basis of Cosmopolitan's POSIX synchronization primitives.
If you're not familiar with the man, he's the guy who coded Chubby and
Altavista, a global search engine which was so efficient it only needed
to operate on a single server. But you wouldn't think *NSYNC is as
prolific as it is if you're only going off star count.
My favorite thing about greenbean is how elegantly it reacts to CTRL-C.
When you interrupt greenbean, it'll use the POSIX pthread_cancel() API
to immediately terminate all the worker threads, so that shutdown
happens without delay. Cancelation is one of the trickier concepts for a
C library to get right. It's up there with threads, signals, and fork in
terms of how its ramifications pervade everything. So similar to Musl
Libc, we've put a lot of thought into ensuring that Cosmo does it
correctly. Cosmo avoids cancelation race conditions the same way as Musl
and Cosmo also implements Musl's
PTHREAD_CANCEL_MASKED
extension to the POSIX standard, which has seriously got to be one of
Rich Felker's most brilliant ideas. Read the commentary in greenbean.c
if you want to learn more.
Some of you might view greenbean as just a toy example. In that case, if
you want to see something based on greenbean that is actually running in
production, then pay a visit
to
https://ipv4.games/
whose source
code is
in
net/turfwar/turfwar.c
and
net/turfwar/.init.lua
.
This is a hybrid redbean + greenbean service, where redbean does the
HTTPS frontend, and greenbean does the HTTP backend. Hackers love to
unleash their botnets on the IPv4 Games, and it honestly isn't that hard
to withstand a DDOS with 49,131,669 IPs when your web server can do a
million requests per second. That's for a service where 99% of the
requests are
write requests
. If you want to have fun with this
server, then you're also welcome to check out
our
monitoring metrics
while
you do it.
This cosmos.zip release includes several games you can play which have
been vetted on all our supported platforms. For example you can actually
play Nintendo in the terminal and it'll even work inside the Windows 10
command prompt. Getting poll(stdin) to work in Windows is a messier
problem than even naming or cache invalidation, so it's super sweet that
Cosmopolitan Third Edition is now able to abstract that complexity.
Although in the case of our port of Bisqwit's fabulous NESEMU1 program,
it turned out we didn't need poll() at all! Just calling read() and
letting it be
EINTR
'd by
setitimer()
sixty
times a second to pipe audio did the trick. So playing these games
helped battle test our new signals implementation too.
We may not have GUI support yet, but you can use your mouse in the
terminal. On Windows, your mouse cursor will generate the same ANSI
XTERM style control codes as it does on Linux, MacOS, BSD, etc. Try
running the
life
program that's included in Cosmos. Left
click draws cells. Space runs an iteration of the life game. Right click
can drag the display. You can also ctrl+wheel to zoom the display in and
out. To read the source code to this simple program, check
out
tool/viz/life.c
.
Boulder startup dylibso just announced a few weeks ago that they've
adopted Cosmopolitan for their new
product
Hermit:
Actually Portable Wasm
. Hermit lets you create secure cross-platform
executables for WebAssembly modules. It's worth a try! Cosmopolitan has
a long history of serving the needs of the Wasm community. Our first
major adopter back in early 2021 was actually
the
wasm3 project
which
provides a similarly great solution to running Wasm outside the browser.
I'm happy to see these projects benefiting from the advantages
Cosmopolitan has to offer. Will you be the next adopter? If so, feel
free to reach out to me personally and I'll see what I can do to help
you be
successful:
jtunney@gmail.com
.
You're also invited to
join our
Discord
community.
Funding for Cosmopolitan Third Edition was crowdsourced from Justine
Tunney's
GitHub sponsors
and
Patreon subscribers
, the
backing of
Mozilla's MIECO program
,
and the generous contributions of our
developer community
on
Discord. Your support is what makes projects like Cosmopolitan possible.
Thank you!
