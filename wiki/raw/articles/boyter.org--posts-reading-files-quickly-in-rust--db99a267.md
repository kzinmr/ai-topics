---
title: "Reading files quickly in Rust"
url: "https://boyter.org/posts/reading-files-quickly-in-rust/"
fetched_at: 2026-05-05T07:01:59.325856+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Reading files quickly in Rust

Source: https://boyter.org/posts/reading-files-quickly-in-rust/

I have been wanting to learn Rust for a while now. I did play with it some time back
https://boyter.org/2017/09/working-rust/
for solving some of the project Euler problems and was reasonably impressed with how it turned out. However as I had no practical use for it at the time I ended up investing more time in Go.
Go as it turns out is a pretty decent language, and somewhat akin to Python in terms of getting things done. There is usually one obvious way to solve any problem. I was even very happy with the performance I was getting out of it. As such I took on building the fastest version of a count lines of code program I could using Go
scc
which you can read about at
sloc cloc and code
.
However with the latest release of 1.27 of Rust (SIMD support) the code counters written in Rust were suddenly a lot faster in Linux. In fact it meant that the fastest one
tokei
was suddenly faster than my
scc
for almost all tests. In addition a new project
polyglot
written in a language I have never heard of
ATS
popped up which is also now faster than my Go program for any repository when running on a machine with less than 8 cores.
I looked a little further into
scc
to determine if I could improve the performance at all and came away unconvinced. There was little opportunity as far as I could see to make it run faster. It still holds the performance crown on Windows however.
During this process I tried running it compared to
tokei
on a 32 core machine with 50 copies of the linux kernel. In this test
tokei
showed an interesting characteristic. It started by using only a few of the cores then after a brief period maxed out all of them. By contrast
scc
started by maxing out every core it could from the moment it started. This suggests that
tokei
started by walking the file system, then processing every file once that process was done. By contrast I had designed
scc
to walk the file system and process each file as it went by chaining Go streams. This suggests that as one might expect for tight loops which code counting is Rust is not just faster than Go but considerably faster.
I played around with how
scc
worked internally and I couldn’t come up with any way to speed it up. Does not mean its not possible, but I doubt I have enough skill to do so.
Seeing as I wanted to learn Rust anyway it seemed like a good idea to attempt to port
scc
into Rust, and learn if
scc
would have been faster if so.
Please note that I going to continue to use Go for the foreseeable future. Its certainly a very easy language to get started with, has a fast feedback loop and generally I don’t write much code that needs such a level performance. When you are working with HTTP endpoints whats a few milliseconds between friends.
So on to learning Rust. To start with I wanted to see how to write a simple Rust program that walks the file tree, loads each file into memory, loops each byte in the file checking if any are null which indicates the file is binary, and end the loop saying so. Otherwise continue counting every byte. I was not going to do this with any parallel code as I wanted to see how fast Rust was compared to Go on the core loop.
This would be the very least amount required in order to start porting
scc
across.
Knowing already how to do so in Go I wrote a simple program using the fastest file walker I know in it. My goal was to a Rust version to run at the same speed.
package
main
import
(
"fmt"
"github.com/karrick/godirwalk"
"io/ioutil"
)
func
main
() {
godirwalk
.
Walk
(
"./"
,
&
godirwalk
.
Options
{
Unsorted
:
true
,
Callback
:
func
(
osPathname
string
,
info
*
godirwalk
.
Dirent
)
error
{
if
!
info
.
IsDir
() {
content
,
err
:=
ioutil
.
ReadFile
(
osPathname
)
bytesCount
:=
0
if
err
==
nil
{
for
index
:=
0
;
index
< len(
content
);
index
++
{
if
content
[
index
]
==
0
{
fmt
.
Println
(
fmt
.
Sprintf
(
"./%s bytes=%d binary file"
,
osPathname
,
bytesCount
))
break
}
bytesCount
++
}
fmt
.
Println
(
fmt
.
Sprintf
(
"./%s bytes=%d"
,
osPathname
,
bytesCount
))
}
}
return
nil
},
ErrorCallback
:
func
(
osPathname
string
,
err
error
)
godirwalk
.
ErrorAction
{
return
godirwalk
.
SkipNode
},
})
}
My first attempt to do the above in Rust I used the WalkDir crate used in ripgrep and as with the Go version didn’t bother with any error checking.
extern
crate
walkdir;
use
walkdir::WalkDir;
use
std::fs::File;
use
std::io::Read;
fn
main
() {
let
nul
=
0
;
let
mut
bytes_count:
i32
;
for
entry
in
WalkDir::new(
"./"
).into_iter().filter_map(
|
e
|
e.ok()) {
if
entry.file_type().is_file() {
let
mut
file
=
File::open(entry.path().display().to_string()).unwrap();
bytes_count
=
0
;
for
b
in
file.bytes().into_iter() {
if
b.unwrap()
==
nul {
println!
(
"
{}
bytes=
{}
binary file"
, entry.path().display().to_string(), bytes_count);
break
}
bytes_count
+=
1
;
}
println!
(
"
{}
bytes=
{}
"
, entry.path().display().to_string(), bytes_count)
}
}
}
I then compiled rust in release mode
cargo build --release
and to ensure they both produced the same output tried them both on the same directory with 172 files.
# bboyter @ SurfaceBook2 in ~/Projects/rust on git:master x [15:36:35]

$ ./go | sort | uniq | sha256sum
0fcf9a1b41ef48053f1f2264c8ecc5076aff4d914d23ec82204e84fa22d6ea57  -

# bboyter @ SurfaceBook2 in ~/Projects/rust on git:master x [15:38:11]

$ ./rust | sort | uniq | sha256sum
0fcf9a1b41ef48053f1f2264c8ecc5076aff4d914d23ec82204e84fa22d6ea57  -
With the above confirming they both produced the same results I went and did a quick benchmark,
$ hyperfine './go' && hyperfine './rust'
Benchmark #1: ./go
  Time (mean ± σ):      29.1 ms ±   2.4 ms    [User: 4.0 ms, System: 25.4 ms]
  Range (min … max):    24.4 ms …  34.8 ms

Benchmark #1: ./rust
  Time (mean ± σ):     103.7 ms ±   2.2 ms    [User: 9.4 ms, System: 96.2 ms]
  Range (min … max):    99.3 ms … 108.5 ms
Clearly I have done something wrong here. It seems at odd that Go would be so much faster in this case. Looking again at the Rust docs its possible to read the file into a Vector from the start. Since the Go code actually reads the whole file into memory this seemed like a likely candidate as to the difference.
In fact what is actually happening in the above Rust is that it is performing a syscall to fetch every byte. Changing it to be in line with the Go version is not too hard.
extern
crate
walkdir;
use
walkdir::WalkDir;
use
std::fs::File;
use
std::io::Read;
fn
main
() {
let
nul
=
0
;
let
mut
bytes_count:
i32
;
for
entry
in
WalkDir::new(
"./"
).into_iter().filter_map(
|
e
|
e.ok()) {
if
entry.file_type().is_file() {
let
mut
file
=
File::open(entry.path().display().to_string()).unwrap();
bytes_count
=
0
;
let
mut
s: Vec
<
u8
>
=
Vec::with_capacity(file.metadata().unwrap().len()
as
usize
);
file.read_to_end(
&
mut
s).unwrap();
for
b
in
s.into_iter() {
if
b
==
nul {
println!
(
"
{}
bytes=
{}
binary file"
, entry.path().display().to_string(), bytes_count);
break
}
bytes_count
+=
1
;
}
println!
(
"
{}
bytes=
{}
"
, entry.path().display().to_string(), bytes_count)
}
}
}
And the benchmark after another release compile.
Benchmark #1: ./go
  Time (mean ± σ):      28.6 ms ±   2.9 ms    [User: 3.8 ms, System: 28.5 ms]
  Range (min … max):    24.3 ms …  39.4 ms

Benchmark #1: ./rust
  Time (mean ± σ):      45.0 ms ±   3.4 ms    [User: 1.7 ms, System: 41.4 ms]
  Range (min … max):    40.2 ms …  56.0 ms
Thats a bit more like it. Seems like Rust is one of these languages that has a few ways to do things and if you do it the wrong way performance can suffer. It is better, but still not great though.
Just to be sure my laptop was not influsing the result I created a Digital Ocean instance and tried it out on a copy of the linux kernel.
root@ubuntu-c-16-sgp1-01:~/linux# hyperfine './go' && hyperfine './rust'
Benchmark #1: ./go
  Time (mean ± σ):      1.131 s ±  0.022 s    [User: 708.5 ms, System: 534.7 ms]
  Range (min … max):    1.116 s …  1.190 s

Benchmark #1: ./rust
  Time (mean ± σ):      2.222 s ±  0.016 s    [User: 1.639 s, System: 0.578 s]
  Range (min … max):    2.198 s …  2.255 s
Seems it was not a case of just my laptop being silly. Wondering if perhaps the first version was faster on linux I copied that up and ran it. It took even longer.
Not sure what was wrong I turned to the Rust subreddit
https://www.reddit.com/r/rust/comments/98japr/newbie_to_rust_question_about_reading_files_from/
A few decent responses there I managed to modify my code to the below. The changes are to set up the buffer Vector outside the core loop and clear it and reload each run. It also removes the to_string calls (which made almost no difference).
extern
crate
walkdir;
use
walkdir::WalkDir;
use
std::fs::File;
use
std::io::Read;
use
std::io;
fn
main
() -> Result
<
(), io::Error
>
{
let
nul :
u8
=
0
;
let
mut
bytes_count:
i32
;
let
mut
buffer
=
Vec::new();
for
entry
in
WalkDir::new(
"./"
).into_iter().filter_map(
|
e
|
e.ok()) {
if
!
entry.file_type().is_file() {
continue
}
let
path
=
entry.path();
let
mut
file
=
File::open(path)
?
;
bytes_count
=
0
;
buffer.clear();
file.read_to_end(
&
mut
buffer)
?
;
for
b
in
buffer.iter() {
if
b
==
&
nul {
println!
(
"
{}
bytes=
{}
binary file"
, path.display(), bytes_count);
break
}
bytes_count
+=
1
;
}
println!
(
"
{}
bytes=
{}
"
, path.display(), bytes_count)
}
Ok(())
}
With the following runtime.
Benchmark #1: ./go
  Time (mean ± σ):      51.8 ms ±   4.0 ms    [User: 7.8 ms, System: 50.2 ms]
  Range (min … max):    46.8 ms …  66.2 ms

Benchmark #1: ./rust
  Time (mean ± σ):      57.0 ms ±   3.7 ms    [User: 2.2 ms, System: 52.8 ms]
  Range (min … max):    51.7 ms …  68.0 ms
Which is much closer to what I was expecting. Incidentally this introduced me to the
?
operator
in Rust. Trying it out on a much larger repository, which is a fresh checkout of the Linux kernel.
Benchmark #1: ./go
  Time (mean ± σ):      1.661 s ±  0.046 s    [User: 1.069 s, System: 0.658 s]
  Range (min … max):    1.563 s …  1.722 s

Benchmark #1: ./rust
  Time (mean ± σ):      2.076 s ±  0.029 s    [User: 1.534 s, System: 0.531 s]
  Range (min … max):    2.034 s …  2.131 s
Which is better than before but still not as good as I had hoped. Its not a blocking issue in my goal of porting
scc
though.
Anyway what I have discovered so far is that Go seems to take reasonable defaults. Rust gives you more power, but also allows you to shoot yourself in the foot easily. If you ask to iterate the bytes of a file thats what it will do. Such an operation is not supported in the Go base libraries. That said Rust does push the happy parts of my brain in a way that Python does.
Its a start towards what I hope will be a faster version of
scc
and failing that a start on my goal of learning enough Rust to be productive.
