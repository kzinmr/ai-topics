---
title: "You can run git on object storage if you re-make packfiles"
url: "https://www.tigrisdata.com/blog/objgit-packfiles/"
fetched_at: 2026-09-17T10:01:20.361233+00:00
source: "xeiaso.net"
tags: [blog, raw]
---

# You can run git on object storage if you re-make packfiles

Source: https://www.tigrisdata.com/blog/objgit-packfiles/

It sure seems that a bunch of companies are trying to ship a git product of some
kind as of late. Wonder why that is.
Either way, I’m building a Git server backed by object storage as an
open-source project
. It sounded simple
enough to start: Git looks like a filesystem, so let’s use a filesystem as a
translation layer on top of object storage to make Git speak object storage.
This model worked…
ok, I guess?
But
it didn’t work for real-world size repositories, so I needed a different
approach. Git stores everything in
Objects
, so why not
store those as objects in Tigris?
Turns out Git packfiles and how they intersected with my (admittedly somewhat
terrible) filesystem shim were the main reason why it was slow. I ended up
having to invent my own packfile format with a columnar store that’s object
storage native. This is the fruit of all of my performance analysis, metrics
annotations, and more
Texas-style distributed systems work
than you can make your k8s cluster shake sticks at.
This approach worked surprisingly well for production-sized repositories, so I’m
sticking with this new Packfile format for now. It seems the least obtrusive
change to make Git Objects feel like object storage Objects, without any client
side changes.
When you make a commit, Git stores the changes you make as objects inside the
.git
(I’ll call this “dotgit” so I don’t have to write as many backticks)
folder.
Imagine Git as two things: a sea of objects and named references to individual
objects. Each object is a
content-addressed
and compressed file. Here’s an example from a tiny git repository:
$ mkdir ~/tmp/gitexample
$ git init && git branch -m main
$ echo "Hello, blog!" >> hello.txt
$ git add .
$ git commit -sm "chore: initial commit"
This produces several objects on the disk like this:
FIG 01
A sea of objects, and a few names into it
.git/objects/
refs/heads/main
│
├── 1c/7a26a901..ec7966
─────▶
commit 1c7a26a
│
│
├── 8e/67afbb2e..857bd3
─────▶
tree 8e67afb
│
│  hello.txt
└── 9c/c9867337..09fe26
─────▶
blob 9cc9867
"Hello, blog!"
the filename is the sha1 of the bytes in the file, so the same
content is always, everywhere, the very same object
If you want to read the contents of an object, it’s compressed, so you have to
use a fairly evil looking python oneliner to scoop out the tasty innards:
$ file .git/objects/**/* | grep -v directory
.git/objects/1c/7a26a901724b4ce766655ac387413fb9ec7966: zlib compressed data
.git/objects/8e/67afbb2ee6bdcbb79061dfdfb93febce857bd3: zlib compressed data
.git/objects/9c/c9867337c2ebae85ba2350f901e0bcc209fe26: zlib compressed data
$ python3 -c "import sys, zlib; sys.stdout.buffer.write(zlib.decompress(sys.stdin.buffer.read()))" < .git/objects/9c/c9867337c2ebae85ba2350f901e0bcc209fe26
blob 13Hello, blog!
As you can see, the objects are just bare files. Let’s look at a Git repository
of the Linux kernel and try to extract out an arbitrary commit. Everything
should just be a billionty bare object files, right? It should be easy to find a
single commit just by looking for the ID on the disk, right?
If only reality were so simple:
$ cd ~/Code/linux.git/
$ tree objects
objects
├── info
└── pack
├── pack-45986f41063f286029742ec12e2c2882b88c5786.idx
├── pack-45986f41063f286029742ec12e2c2882b88c5786.pack
└── pack-45986f41063f286029742ec12e2c2882b88c5786.rev
3 directories, 3 files
Yeah, as I’m sure you guessed just putting everything into their own files won’t
scale to something like the Linux kernel. I’m pretty sure you’d run into inode
limits like everyone did in the era of
fractal
node_modules
folders
.
If you’ve used Node for long enough to remember that, please go get a
colonoscopy. Colon cancer is a real concern that too many people overlook for
too long and takes too many lives too early.
Git works around this by putting objects into
packfiles
, compressed
bundles of objects that store them all in the same file. Here's an example of
the packfile efficiency in my checkout of objgit:
$ git count-objects -v
count: 756
size: 3500
in-pack: 448
packs: 1
size-pack: 321
prune-packable: 0
garbage: 0
size-garbage: 0
If you ever need to “force” git to put bare objects into a packfile, you can run
git gc
:
$ git gc
[omitted for brevity]
$ git count-objects -v
count: 0
size: 0
in-pack: 1203
packs: 2
size-pack: 848
prune-packable: 0
garbage: 0
size-garbage: 0
One of the beautiful things about implementing Git on top of object storage like
I am is that I’m using a platform where the object data is a sea of objects with
named references to points in that sea stored in FoundationDB. This is a kind of
divine recursion that I don’t really know how to describe the beauty of. As
above, so below.
Yo dawg, herd you like objects
​
Here's the object count for a copy of the Linux kernel:
xe@zohar:~/Code/linux.git$ git count-objects -v
count: 0
size: 0
in-pack: 11827138
packs: 1
size-pack: 3876775
prune-packable: 0
garbage: 0
size-garbage: 0
This is eleven million objects, which at a very generous assumption of 10ms per
GetObject call means that fetching each of them takes over an hour to fetch them
all. The truth is there really aren’t 11M objects as individual files on the
disk, they’re bundled into one big happy 3.4Gi packfile. Your typical git repo
ends up accumulating them as it makes sense to break them up. My local copy of
the Tigris blog has 4 packfiles and 290-ish bare objects.
So you’d be thinking, “Oh, if git has packfiles, then why is the rest of this
post a thing?”
Well, like many things in distributed systems it’s complicated. Packfiles are
difficult because they’re designed with local storage and/or mmap in mind. Git
constantly writes packfiles to disk and then re-reads them. Filesystem reads in
that case are 10 nanoseconds
at most
(the filesystem cache helps so much here)
but doing any network roundtrip is 10 milliseconds
at minimum
. It’s at least a
million times slower because of how reality works.
One of the things that
/usr/bin/git
does that makes integrating it into object
storage difficult is the unix-y idiom of writing to a file and then immediately
reading back from that file to calculate the hash. In object storage you can’t
GetObject something that hasn’t finished a PutObject call. I worked around this
previously by writing to the disk and then doing it that way, but the experience
kinda sucked in practice.
Messin' with Packfiles
​
Each packfile has an index that describes what’s in it. Here’s a view of the
index of the packfile made out of that trivial Git repo from earlier uppost:
$ git gc # force objects into a packfile
$ git verify-pack -v .git/objects/pack/pack-3971f5085c23c38be00e517ed0c64ca7df19b746.idx
1c7a26a901724b4ce766655ac387413fb9ec7966 commit 526 366 12
9cc9867337c2ebae85ba2350f901e0bcc209fe26 blob   13 22 378
8e67afbb2ee6bdcbb79061dfdfb93febce857bd3 tree   37 48 400
non delta: 3 objects
.git/objects/pack/pack-3971f5085c23c38be00e517ed0c64ca7df19b746.pack: ok
The commit points to the tree whose file “hello.txt” points to the blob and,
blob’s your uncle, you have a repo. Git uses these binary indices to let it know
where to look and how far it needs to seek into the packfile to know where to go
to get things.
FIG 02
Eleven million objects, one packfile, one index
$ git count-objects -v
.git/objects/pack/
count:            0
└── pack-45986f41..c5786.pack   3.7 GiB
in-pack:   11827138
packs:            1
eleven million loose files would be
size-pack:  3876775
eleven million inodes. so: one file.
.idx
.pack
┌───────────────────────┐
┌──────────────────────────────────────┐
│
0002ff4c..  0x0000c
│
│
███
██
████
█
███████
██
█
████
██████
│
│
0031ab90..  0x0a13f
│
└──────────────────────────────────────┘
│
1c7a26a9..  0x1f3a4
│
│
...
│
└───────────────────────┘
each row's colour is the run of bytes its offset points at, so a
read is a seek to an offset inside one very big file
ALL/03
three rows, three offsets, three runs of bytes
▶ play
The great part is that this works really well when everything is in a
filesystem. Git
mmaps
the packfiles so
that the kernel treats disk contents as memory pages, meaning that trying to
read past what’s “in memory” makes the kernel load it instead of userspace. This
is faster than loading it from the disk directly. It’s a shame this design
doesn’t work in object storage.
If only you could construct Range requests from packfiles
​
At some level this sounds pretty great for object storage, right? You have
offsets into the packfiles and then you can “just” grab out a single object from
a packfile with an
HTTP Range request
right? Objects are placed randomly within packfiles and other attempts at
storing Git in object storage end up having problems here. Tigris is really good
at random access scans, so most of the hard part is figuring out how to grab the
right data out of the bucket.
HTTP Range requests let a client download
part
of a file. The main usecase
they're built for is back in the day of dial-up internet you weren't online all
the time. Your main path to the Internet was the same way you send and received
phone calls. As such, if someone called you while you were online, all your
downloads got interrupted. Range requests let Internet Explorer resume downloads
where they got cut off instead of having to start all the way over.
They've been maintained into the modern era but don't really get much use
outside of galaxy brain format abuse like what I'm doing and online video
streaming.
Well, it’s complicated. The example I gave shows all of the index entries one
after the other, but in the real world processing the index entries one after
the other you know the
decompressed
size of a single object in the packfile,
but not the
compressed
size. This means you don’t have enough information to
construct a HTTP Range request.
FIG 03
One ranged GET, 366 bytes out of the middle of 128 MiB
packs/019a7f3c..bin
┌────────────────────────────────────────────────┐
│
██
│
└───────────────────────────────────
▲
────────────┘
0
│
128 MiB
└── 366 bytes, right here
you know where it starts and how long it is, so ask for
exactly that span and nothing else:
GET /packs/019a7f3c..bin
Range: bytes=100663296-100663661
and that is all the bucket sends back:
206 Partial Content
Content-Range: bytes 100663296-100663661/134217728
┌────┐
│
████
│
366 B on the wire, not 128 MiB
└────┘
This core problem is half the reason why I ended up needing to make my own
object-storage native Git packfile format.
SEND CUE SHEET
​
Way back in the days of physical media, one of the most common formats was the
CD-ROM (Compact Disc Read-Only-Memory, or CD). A CD is a 700Mi container that
stores data in sessions that each contain up to 99 tracks of either audio or
data. CDs were originally invented to store song audio in so that you could
listen to an hour or so of music at a higher quality than analogue cassette
tapes. CDs also let the player skip from track to track so you can go directly
to the song or movement of a larger work that you like.
This is also why you see guides telling you to put legal backups of CD and DVD
media into lossless
.iso
files. An
.iso
file contains one recording session
that may contain data or audio.
FIG 04
A CD cue sheet and an objgit cue sheet solve the same problem
CD AUDIO DISC                                   OBJGIT PACKFILE
──────────────────────────────────────────      ──────────────────────────────────────────
U0008_0000002_0000147.WAV
one big file
objects.bin
one big file
┌──────────┬─────────────┬─────────────────┐    ┌──────────┬─────────────┬─────────────────┐
│ track 01 │  track 02   │       ...       │    │  blob A  │   tree B    │       ...       │
└──────────┴─────────────┴─────────────────┘    └──────────┴─────────────┴─────────────────┘
▲          ▲                                    ▲          ▲
│
00:00
│
00:13
│
@0
│
@142
FILE.cue
plain text, parsed top-down
objects.cue
packed records, fixed width
┌──────────────────────────────────────────┐    ┌──────────────────────────────────────────┐
│ FILE "U0008_0000002_0000147.WAV" WAVE    │    │ HEADER                              16 B │
│                                          │    │   magic  version  rec_size  record_count │
│ TRACK 01 AUDIO                           │    ├──────────────────────────────────────────┤
│ INDEX 01
00:00
│    │ RECORD 0                            58 B │
│ TITLE
"U0008_0000002_0000147_0001"
│    │
hash
3a7f…c21        type blob         │
│                                          │    │   comp zstd            size 311          │
│ TRACK 02 AUDIO                           │    │
bin_offset
0
bin_length
142    │
│ INDEX 01
00:13
│    │
delta_base
0000…0000                   │
│ TITLE
"U0008_0000002_0000147_0002"
│    ├──────────────────────────────────────────┤
└──────────────────────────────────────────┘    │ RECORD 1                            58 B │
└──────────────────────────────────────────┘
to reach track 2 a player parses every
line above it. it already has the disc.
record N sits at 16 + N*58. one seek,
then one ranged GET into objects.bin.
However there’s one catch that kinda ruins this easy way to back up CDs: they
can store
multiple
recording sessions on the same disc. Most of the time this
wasn’t used outside of making piracy on certain late 90’s/early 00’s game
consoles more annoying, but there was
that one Ricoh Encryptease product
that combined
a user-recordable area with a factory printed area so that you could encrypt
files on CDs you share with the decryption software shipping alongside it. This
is about as cursed as it sounds.
The trick of using multiple sessions is how Dreamcast games play as audio CDs
telling you to put it into a Dreamcast or how Xbox 360 games play as DVDs
telling you to put it into an Xbox 360. As an added bonus it means that when you
stick it into a computer it thinks that it’s an audio CD or DVD, which means
that lazy pirates can’t easily scoop out all the game files to their hard
drives.
As a result, there needed to be a way to properly handle this for archival
purposes. The eventual result was creating
cue sheets
to store
alongside the binary blob of data. The
.cue
sheet stores information that the
decoder uses to be able to seek to arbitrary points in the
.bin
file. This
lets you easily extract things like songs or bits of data without having to read
the entire CD image. As an added bonus it handles multiple recording sessions
for you.
Packfiles v2: object storage boogaloo
​
This got me thinking, how would we take all of these lessons into heart and
build a new git packfile format optimized for object storage?
Wait, I know what you’re thinking. You’re thinking that I’m about to make a
Chesterton’s Fence violation
.
Just “rolling my own” format for something as dear and precious as storing the
revision history of a company’s code repositories is probably one of the worst
decisions you can make, right?
Normally, yes, it’s a bad idea to do this. However Git is a
distributed
version control system. When you clone a repository, you clone
all
of the
changes ever made to it on every branch at the same time. This also means that
everyone has a copy of the entire history of that repository, meaning that if
the worst does in fact come to pass and my handrolled format ends up sucking
it’s trivial to recreate all the data. Just push it again.
So what would this format look like?
Well for one the format needs to be Range-request native. You should be able to
scoop any one object out of a packfile without having to download or process
anything but the object you want. Again, Tigris is good at this, so we should
design the format with that usecase directly in mind. The format should also
take advantage of modern compression libraries like
zstd
which are faster and more
data-efficient than zlib. Finally delta objects should be stored as their own
object in the packfile instead of slapped onto the end of the object it’s a
delta of so that you don’t have to read the object and its deltas to read the
object in the first place.
I skipped over this earlier to save time, but Git stores both file revisions
(the entire copy of a file at any given point in time) and the difference
between them as an optimization to make it easier to uncompute the changes made
in commits. At some level this meme is both accurate and wrong:
Objgit's packfile format that probably needs a name
​
The format I came up with is pretty directly inspired from the
.bin
and
.cue
format of CD backup. Objects are stored one after the other in a
.bin
file
that’s normally up to 128Mi (the oddly specific number was chosen because it
looked round to me) and the metadata of what objects are in there are stored
separately in a binary-encoded
.cue
sheet. Together this makes Git repository
storage in Tigris a columnar store.
FIG 05
objects.cue on the wire: one header, then fixed-width records
objects.cue HEADER
16 bytes, once at the top of the file
┌──────────────┬─────────┬──────────┬────────────────────┐
│ magic "OGCU" │ version │ rec_size │ record_count       │
│          4 B │ u16 2 B │ u16  2 B │ u64            8 B │
└──────────────┴─────────┴──────────┴────────────────────┘
0              4         6          8                   16
objects.cue RECORD
58 bytes, repeated record_count times
┌──────────────┬──────┬──────┬────────────┬────────────┬────────┬──────────────┐
│
hash
│ type │ comp │
bin_offset
│
bin_length
│ size   │
delta_base
│
│
sha1  20 B
│ u8 1B│ u8 1B│
u64   8 B
│
u32   4 B
│ u32 4B │
sha1  20 B
│
└──────────────┴──────┴──────┴────────────┴────────────┴────────┴──────────────┘
0              20     21     22           30           34       38            58
identity
hash
,
delta_base
location
bin_offset
,
bin_length
decode
type, comp, size
The big thing I did was store the sizes for both the
compressed
and
uncompressed
forms of objects alongside the offset into the packfile. This
means that you can trivially construct the right HTTP Range requests to scoop
individual objects out of Tigris while the packfile is downloading in the
background.
As an optimization for latency, whenever the Git library requests any object
from a packfile, the entire packfile is downloaded from object storage to a
temporary folder. Anything on the “far end” of the packfile is Range-requested
from Tigris until the downloaded packfile “catches up”. In practice this ends up
meaning that packfiles get downloaded just in time for them to be useful to read
from and there’s overall fairly little latency beyond what’s unavoidable with
the Git library I’m using. If the “scooping objects out of the far end” problem
ends up being an issue in practice I’ll just have it start fetching the most
recent packfiles for a given repository in the background when you start pushing
or pulling.
FIG 06
Racing the beam: four ranged GETs while the container is 2 MiB in
git wants four objects out of packs/019a7f3c..bin
A
B
C
D
▼
▼
▼
▼
┌
────────────────────────────────────────────────
┐
container
│
░░░░░░
█████
░░░░
█████
░░░░░░░░░
█████
░░░░░░
█████
░░░
│
└
────────────────────────────────────────────────
┘
five requests go out at once:
A   16 MiB
│
░░░░░
│
in flight
B   40 MiB
│
░░░░░
│
in flight
C   77 MiB
│
░░░░░
│
in flight
D  107 MiB
│
░░░░░
│
in flight
whole file
│
░░░░░░░░░░░░░░��░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
│
in flight
four ranged GETs race the background download of the whole
file. whatever the download reaches stops needing a GET.
01/07
128 MiB of packfile; git wants A, B, C and D out of it
↺ replay
There’s nothing in the definition of the packfile format that limits packfiles
to 128Mi, I’m just doing that to prevent them from getting too big to download
quickly. In theory if you store a large binary blob (such as 3d models,
perfectly legal backups, etc) into the git repository directly it could result
in a packfile that’s bigger than 128Mi. I plan to solve this by implementing
Git Large File Storage
in the near future.
But for now if you have a workflow that involves storing large binary files in
your git repository and want to use objgit for that: consider a different
architecture.
The funny numbers
​
One of the more surprising things about Git is that basically every interaction
with it is expensive. As such, you can go a long way by benchmarking how long it
takes to push/pull repositories. As such, I decided to compare against a few git
repos that have some interesting properties:
Here are the conditions I ran the tests in:
Item
Value
Started
2026-09-11T12:28:59-04:00
Finished
2026-09-11T13:06:52-04:00
Host
Mac, 16 CPUs
Go
go1.26.5
Git
git version 2.55.0
Bucket
xe-objgit-devel
Build "old"
v1.0.2
Build "fixed"
origin/main
Push tests
​
The big thing I wanted to fix was reducing the number of object storage calls.
Less object storage calls, less latency waiting for them to resolve. It ended up
being ridiculously effective. Object storage call counts sank like a stone.
All charts in this post are at logarithmic scales so they render more cleanly
and the green bars are visible.
FIG 07
S3 requests to push, before and after the format change (log scale)
1
10
100
1,000
10,000
├─────────┼─────────┼─────────┼─────────┤
objgit
old
████████████████████████
231
new
█████████████
18
Xe/x
old
████████████████████████████████████████
9,236
new
███████████████
30
tigris-blog
old
███████████████████████████████████
3,324
new
█████████████████████
136
██
old
git packfiles behind a filesystem shim
██
new
.bin/.cue columnar packfiles
Repo
Build
Wall
S3 requests
PUT
GET
HEAD
LIST
Keys
Bucket bytes
objgit
old
8.7s (8.7s-15.9s)
231
46
47
0
138
42
829.27 KiB
objgit
new
2.2s (1.9s-2.5s)
18 (17-20)
5
10 (9-12)
0
3
4
902.98 KiB
x
old
3m29.4s (3m29.4s-3m40.6s)
9,236 (9,236-9,304)
1,087
2,170
0
5,979 (5,979-6,047)
1,082
54.96 MiB
x
new
14.3s (14.3s-14.7s)
30
6
20
0
4
4
46.38 MiB
tigris-blog
old
2m13.4s (1m29.1s-2m30.5s)
3,324 (2,687-3,417)
515
522
0
2,287 (1,650-2,380)
511
354.67 MiB
tigris-blog
new
26.5s (19.2s-27.4s)
136 (113-146)
9
123 (100-133)
0
4
8
360.75 MiB
The biggest gain was wall clock time for pushing though:
FIG 08
Wall time to push, log scale, speedup on the right
1s
10s
100s
1,000s
├───────────┼───────────┼───────────┤
objgit
old
███████████
8.7s
new
████
2.2s
4.0x
Xe/x
old
████████████████████████████
3m29.4s
new
██████████████
14.3s
14.6x
tigris-blog
old
██████████████████████████
2m13.4s
new
█████████████████
26.5s
5.0x
██
old
git packfiles behind a filesystem shim
██
new
.bin/.cue columnar packfiles
One of the biggest places that objgit used to lag was pushing taking way longer
than it felt like it should. Eliminating the Tigris round trips made pushing way
more responsive.
Clone tests
​
I also wanted to see how the difference affected clone times. There were the
same benefits as with pushing:
FIG 09
S3 requests to clone, before and after the format change (log scale)
1
10
100
1,000
10,000
├─────────┼─────────┼─────────┼─────────┤
objgit
old
█████████████████████████
323
new
████████████
17
Xe/x
old
██████████████████████████████████████
6,428
new
████████████
17
tigris-blog
old
████████████████████████████████████
3,675
new
██████████████████████
158
██
old
git packfiles behind a filesystem shim
██
new
.bin/.cue columnar packfiles
Repo
Build
Wall
S3 requests
GET
HEAD
LIST
Wire bytes
objgit
old
11.8s (11.5s-19.5s)
323
51
0
272
763.63 KiB
objgit
new
2.6s (1.5s-5.7s)
17 (16-17)
13 (12-13)
0
4
767.96 KiB
x
old
3m23.5s (3m23.5s-3m33.6s)
6,428 (6,428-6,780)
1,091
0
5,337 (5,337-5,689)
40.68 MiB (40.68 MiB-40.70 MiB)
x
new
54.4s (54.4s-57.8s)
17 (17-71)
13 (13-67)
0
4
42.22 MiB (42.22 MiB-42.36 MiB)
tigris-blog
old
2m23.6s (2m19.4s-2m50.2s)
3,675 (3,601-4,123)
520
0
3,155 (3,081-3,603)
350.94 MiB (350.93 MiB-351.07 MiB)
tigris-blog
new
1m22s (1m20.8s-1m38.7s)
158 (137-317)
155 (134-314)
0
3
349.04 MiB (348.00 MiB-352.67 MiB)
FIG 10
Wall time to clone, log scale, speedup on the right
1s
10s
100s
1,000s
├───────────┼───────────┼───────────┤
objgit
old
█████████████
11.8s
new
█████
2.6s
4.5x
Xe/x
old
████████████████████████████
3m23.5s
new
██████��███████████████
54.4s
3.7x
tigris-blog
old
██████████████████████████
2m23.6s
new
███████████████████████
1m22.0s
1.8x
██
old
git packfiles behind a filesystem shim
██
new
.bin/.cue columnar packfiles
Oh yeah, the time numbers would probably be better if I tested this on a machine
with ethernet. I did all my testing with my corp laptop on Wi-Fi to specifically
put this in one of the worst conditions it could possibly be in.
Conclusion section
​
I’m still actively working on this. I’m not confident enough to use this for my
own projects yet and I wouldn’t blame you for not wanting to use this yet
either. I still haven’t implemented authentication, authorization, any kind of
API (my long-form
SigV4 auth post
was
actually going to be an objgit post!), or any rate limit beyond what your
machine can physically process. If you were to take this, run it, and then
expose it to the Internet, then anyone that can connect to that server can pull
or push whatever they want. Consider not doing that.
Objgit packfiles also currently accumulate forever, so if you have a bunch of
small pushes then there will be a bunch of small packfiles in the bucket. I’m
toying with designs that would occasionally compact them into bigger packfiles,
but that’s something that can be done later.
At the least though: Git’s packfile format is a great format for the constraints
of storing git repositories in actual filesystems. The moment you put network
roundtrips into the mix it all goes south.
I'm gonna keep working on this and publish reports like this as I learn more. I
hope this was interesting! Stay safe out there.
Read the packfile code before I name the format
objgit stores git repositories directly in Tigris. The .bin/.cue container, the columnar index, and the four-tier read ladder in this post are all in the repo.
