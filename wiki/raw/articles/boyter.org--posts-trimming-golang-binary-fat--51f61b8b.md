---
title: "Trimming the fat from a Golang binary"
url: "https://boyter.org/posts/trimming-golang-binary-fat/"
fetched_at: 2026-05-05T07:01:59.013974+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Trimming the fat from a Golang binary

Source: https://boyter.org/posts/trimming-golang-binary-fat/

I have recently started work again on
searchcode server
with the continued plan to upgrade
searchcode
to use the same code-base.
One big issue with this which I recently tweeted about was that Java has a decent well documented fast library for just about everything, with the exception of a good syntax highlighter like Pygments
http://pygments.org/
or Chroma
https://github.com/alecthomas/chroma
It is however possible to use Pygments in Java using Jython
http://pygments.org/docs/java/
which was very appealing to me as Pygments is the current highlighter used by searchcode.com
However in my tests it was too slow to be usable, in particular Lisp programs caused it to take 10’s of seconds to render, which is totally unacceptable for my performance requirements.
I briefly considered writing my own implementation but quickly discarded this idea due to the amount of effort it would entail. As such I decided I would package in either a HTTP or command line implementation of a highlighter. I quickly discarded the idea of a command line as it could mean potentially hundreds of forking processes on
searchcode
and settled on using Go and Chroma served over HTTP.
A quick check showed that the problematic files when run through Chroma were processed in ~100ms which was a massive improvement over Pygments in Java which solved that performance issue so there were no issues using it like this.
Go is a pretty nice language. However the binary files it produces since they include everything are rather fat. My simple syntax highlighter
https://github.com/boyter/searchcode-server-highlighter
server was ~13 MB when built with the usual
go build
command. However it is possible to slim down Go binary if you want.
Since I potentially need to package up-to 3 binaries with searchcode-server its pretty important to shrink this size down.
Starting with the standard
go build
as a default position.
$ go build

# bboyter @ SurfaceBook2 in ~/Go/src/github.com/boyter/searchcode-server-highlighter on git:master x [12:04:06]

$ ls -lh searchcode-server-highlighter*
-rwxrwxrwx 1 bboyter bboyter  13M Jan  7 12:04 searchcode-server-highlighter
The first trick is to set ldflags. If you build with the flags
-s -w
you can strip out the debug information.
$ go build -ldflags="-s -w"

# bboyter @ SurfaceBook2 in ~/Go/src/github.com/boyter/searchcode-server-highlighter on git:master x [12:06:17]

$ ls -lh searchcode-server-highlighter*
-rwxrwxrwx 1 bboyter bboyter 9.5M Jan  7 12:06 searchcode-server-highlighter
~4 MB of savings just with that single flag. Of course it makes debugging harder, but thats not usually an issue in production, or in my case where I want to ship the binary with another application.
The next trick is to use
upx
which is a binary packer
https://upx.github.io/
which compresses your binary. This comes with the trade off of requiring your application to be decompressed every time it is run, so its not the best idea for command line tools which need to start quickly such as
ls
,
ripgrep
,
scc
etc…
However in my case its going to be a long running background process, so who cares.
$ go build -ldflags="-s -w" && upx searchcode-server-highlighter
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2013
UPX 3.91        Markus Oberhumer, Laszlo Molnar & John Reiser   Sep 30th 2013

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   9904128 ->   3376604   34.09%  linux/ElfAMD   searchcode-server-highlighter

Packed 1 file.

# bboyter @ SurfaceBook2 in ~/Go/src/github.com/boyter/searchcode-server-highlighter on git:master x [12:12:36]

$ ls -lh searchcode-server-highlighter*
-rwxrwxrwx 1 bboyter bboyter 3.3M Jan  7 12:12 searchcode-server-highlighter
Bingo Boom-Shaka-Laka and suddenly a binary that was 13 MB is size is now closer to 3 MB and a far better option for packaging with an existing application.
Its also possible to do this with your Windows builds and since the initial binary was smaller to begin with on windows the resulting compressed binary is even smaller.
$ ls -lh searchcode-server-highlighter.exe*
-rwxrwxrwx 1 bboyter bboyter 2.9M Jan  7 08:42 searchcode-server-highlighter.exe
Will anyone notice this for
searchcode
? Honestly probably not, but its nice to try and at least save some disk space and download time where possible.
BTW I am not the only person to have written about this
https://blog.filippo.io/shrink-your-go-binaries-with-this-one-weird-trick/
but its more here for my personal reference than anything else.
