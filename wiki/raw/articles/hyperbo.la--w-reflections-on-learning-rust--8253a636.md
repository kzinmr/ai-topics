---
title: "Reflections on Learning Rust By Building Punchtop"
url: "https://hyperbo.la/w/reflections-on-learning-rust/"
fetched_at: 2026-04-29T07:02:15.790849+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Reflections on Learning Rust By Building Punchtop

Source: https://hyperbo.la/w/reflections-on-learning-rust/

Punchtop
is an
audio game
that uses a Chromecast as an audio output device.
I have implemented this game
a few times before
; the rules are simple and I
have a lot of practice implementing my ideal architecture, which makes it a good
candidate for learning new languages and libraries. Punchtop is about 3700 lines
of Rust and JavaScript:
$ (
find
.
-name
'*.rs'
-not
-path
'*target*'
-not
-path
'*proto*'
|
xargs
cat
) \
| wc -l
3104
$ (
find
.
-name
'*.js'
-not
-path
'*target*'
-not
-path
'*node_modules*'
|
xargs
cat
) \
| wc -l
563
For context, my most comfortable languages are Ruby and Python. I also have
written significant amounts of code in Golang, Java, JavaScript, Objective-C,
PHP, and Scala. While I have been meaning to learn Rust
since at least 2014
,
this was my first time sitting down with the language. In this post I’ll reflect
on what I liked, what I didn’t, what I found easy, and what I found hard.
Language
My overall impression of Rust is that it is pleasant to work with once you grok
the memory model. Despite the language being low level, I only had two panics
during development. I felt comfortable in the same way I do when developing
Scala (and that I don’t in Ruby or Golang): if the code compiles, it is likely
to be correct.
Borrow Checker
The borrow checker was a new concept for me. My previous implementation of this
game was an
evented ruby implementation
which was (ahem) cavalier in how it
shared object references. I initially fought with the compiler a lot, but some
practice helped me get into my head when to use references, when to
clone
, and
when to
move
. I tried to read some tutorials on borrowing and none of it
stuck. I had to get comfortable by doing.
Memory Safety
The most practical consequence of Rust’s memory safety is that there is no
null
. Having this baked into the language (and the standard library!) is
liberating. Whole classes of bugs vanish because using
Option
and
Result
is
not only the default, but required.
Clippy
While not part of rustc proper,
Clippy
is a rustup component that
acts as a linter. I found Clippy to be incredibly useful while learning the
language. Its large library of lints helped me to internalize how to write
idiomatic Rust. Early on, I added
#![warn(clippy::all, clippy::pedantic)]
to
my crate.
Clippy helped me write more performant code by suggesting the correct
combinators to use, e.g.
map_or
instead of
map(...).unwrap_or_else(...)
, and
avoiding unnecessary clones by using references when functions did not consume
arguments.
Clippy helped me write more correct code by forcing me to correctly handle
overflow
(this code is gross; it gets much better in
2a8ddbfb
) and safely
convert between
usize
and
u64
.
Clippy Gotchas
Clippy required nightly to analyze all of the crates that Punchtop depended on,
which was initially off-putting. Requiring nightly also interacted poorly with
the
protobuf-codegen-pure
build dependency: the codegen only output
#![allow(clippy)]
in the generated build files, which was
incompatible with
nightly Clippy
. I wrote a
codemod
in
build.rs
to work around this (I wish I
could have found a library that did this for me).
Clippy offers the ability to selectively disable lints by attaching an
#[allow(clippy::...)]
to any code unit. I had to do this in a few places:
generated protobufs
, some
serde enums
, and
rocket route functions
.
Selectively disabling lints was not hard, but it was non-obvious.
The most frustrating part of using Clippy is that it did not force a reanalysis
of all packages in my cargo workspace when invoked multiple times. A (maybe
bad?) habit I learned from rubocop is to incrementally fix lint errors and rerun
the linter to see what I have left. Clippy does not force a re-compile of source
packages in the current workspace requiring contortions like
touch src/main.rs
to get the updated lint errors.
Overall, I found Clippy to be quite excellent and it made my Rust code much
better.
Refactoring
My initial implementation of Punchtop used
rodio
as the audio output device.
Once I added the
Chromecast sink
, the shared API for these two modules evolved
rapidly (especially once the API started to get infected by async). I found that
the rodio implementation was slowing me down too much, so I deleted it. Looking
back, a better solution would have been to add a
#[cfg(...)]
incantation to
disable compilation for the rodio-based module.
Testing
I have
some tests
! which is more than I can normally say about a side project.
I found it much easier to write tests for a few reasons:
Tests are defined inline with the rest of the code in my modules, which
eliminated some context switching and made it easy to write tests as I
implemented functionality.
#[test]
is native to rustc, so I did not have to mess with choosing a unit
test framework and getting it integrated with my project.
I only had to learn two bits of magic to write a test since they are just
regular functions (and even the magic is very straightforward): annotating
test functions with
#[test]
and the
assert_eq!
macro.
Doc tests are amazing
. They made me confident in my documentation and led to a
higher quality README
.
Testing Gotchas
The only non-obvious part of writing tests was wrapping test functions in a
mod test
that is conditionally compiled during test builds with
#[cfg(test)]
. The
Rust book section on testing
has examples that show to do
this, but never specifies
why
to do it. The answer is decreased compilation
time in non-test builds.
Documentation
cargo doc
is excellent. I ran this on an airplane and was able to develop with
no Internet access.
The
stream-util
module I wrote to gracefully drain a futures mpsc channel is
the most well-documented module I have ever written. I added a directive to
fail builds on missing docs
. I modeled the docs on those in
BurntSushi/walkdir
and also ported them over to the README for the crate. Like
I said above, doc tests are amazing.
Documentation Gotchas
Linking to code units in rustdoc was hard to do correctly since there were so
many ways to do it. It took me more than a few attempts to get the resolution
rules internalized.
When porting the rustdoc to the README, I had to manually insert links that
resolved the modules in external crates (mostly tokio) that were pertinent to
using the library.
My biggest frustration with
reading
documentation was using the Rust book(s)
from Google. The books themselves are excellent, but the SEO is terrible. There
are multiple versions linked in Google. The books
know
that I want the most
recent version because they all link to it, but I’d prefer this be handled via a
redirect so Google knows what documentation is current.
Cargo
Cargo is the Yarn equivalent for Rust. It handles managing dependencies,
building your code, and running your code. Cargo is very pleasant to work with.
Pulling in libraries was effortless (even
git dependencies
), as was
running
code in either debug or release configurations
.
Rust 2018 Edition came out early on when developing Punchtop and Cargo made it
easy to upgrade to the latest supported idioms.
One thing I missed from Yarn was an
outdated
command that enumerates libraries
that have available updates. I supported this part of my workflow with the
cargo-outdated
crate which does the job admirably.
Workspaces
As Punchtop grew more complex, I had several trees within
src
that were shaped
like independent libraries. I split my monolithic
punchtop
crate into multiple
crates within a shared cargo workspace.
Moving to a workspace allowed me to consider implementing multiple UI frontends
by reusing the
audio backend
and
stream manipulation
libraries I created.
I also found that splitting libraries out into their own crates made it easier
to reason about the visibility of structs and functions without having to mess
with more exotic visibility modifiers.
Workspaces Gotchas
When I split Punchtop into multiple crates, I missed that I needed to add my
Clippy
!#[warn(...)]
directive to the
lib.rs
of the new crates.
Libraries
Rust has many good libraries. I was able to offload lots of tricky logic to
crates. For example, I do not want to be in the business of
parsing an mp4
to
find out if it is at least 60 seconds long.
tokio
Tokio
is a suite of libraries for writing async code. It is big, but was
mostly easy to use. These are the highlights.
The
tokio
crate is composed of many sub crates, e.g.
tokio-timer
and
tokio-codec
. I initially had a mix of these included in Punchtop and was
confused by the differing version numbers. Ultimately I learned that tokio
recommends
depending on
tokio
in crates with a
main.rs
and the sub crates in crates with a
lib.rs
. I used this newfound
knowledge to
trim 48 dependencies
from the
futures-locks
crate.
tokio-codec
is my favorite part of Tokio.
tokio-codec
enables
reading and
writing frames to a socket
. The cast protocol consists of
u32
-length prefixed
protobuf frames so this was a perfect fit. It was very easy to implement a
stateful decoder
. My encoder consumed a high-level playback command enum and
the decoder produced decoded protobufs which were handled by the
channel
multiplexer
. The separation of concerns made it clear where to check protocol
invariants such as
maximum payload size
.
The one gotcha of
tokio-codec
was the
bytes
crate. I was missing a call to
buf.reserve(len)
, which was the source of one of my panics.
Much has been
written
about the
futures
crate. The two
things I found helped me the most when using it are
impl trait
and
IntoFuture
combined with generics
. I would like to invest more in using
named
Future
s
to clean up the
cast-client
public API.
web_view
The state of writing GUIs in Rust is still developing.
Azul
(based on
WebRender) looks promising but is super alpha. The
Cocoa bindings
used in
Servo require writing lots of unsafe code.
web_view
provides high-level Rust bindings for the cross-platform
webview
single-header C library
. The library allows two-way communication to JS running
in the webview using stringified JSON. I built a
React and Redux app
and a
minimal amount of
MVC glue
to track application state in Rust. The result was
an easy to extend UI. I even integrated the webpack build into the
build
script
for
punchtop-webview
.
log and env_logger
Logging
was super
easy to set up
and achieved good
results by default. The
debug!
and
warn!
macros have obvious meaning and do
not interrupt the flow of the code.
My one complaint is that
RUST_LOG=debug cargo run
dumps all of the verbose
debug logs from
cargo
while your program is being built.
rocket
Rocket
is a
hyper
-based HTTP
framework. Rocket requires nightly, but is very ergonomic to use. It requires
less ceremony than even a Sinatra server
.
The statically-typed
route functions
were pleasant to work with.
I did have to jump through some hoops to use Rocket as an embedded (vs.
application) server, including
launching rocket in a thread
instead of scheduling it on my tokio reactor,
discovering the bind interface
,
and configuring an
unused secret key
.
mp3_duration
mp3_duration
is a single-purpose crate did exactly what I needed it to do
until it panicked on some of my MP3s. Since I was using this crate to filter
items out of a playlist, I
isolated it
using
panic::catch_unwind
and ignored
files it could not parse. I should probably find a panicking sample MP3 and file
a GitHub issue.
serde
Serde
is my favorite of all the crates I used in Punchtop.
I have previous experience with statically-typed JSON libraries in
Jackson
and
json4s
. Serde is by far the easiest JSON
library to work with.
Serde uses Rust macro magic to derive encoders and decoders directly from
structs. The encoder and decoder are configurable with a few other macros. My
two favorites are
remapping rustfmt-compliant struct fields to the native JSON camel case style
and
field-tagged enums
AKA switching deserialization based on a type tag in the JSON. Field-tagged
enums gives you all the benefits of Rust enums when dealing with JSON, most
notably ensuring match arms are exhaustive.
Moving Forward
At this point in the project, I feel reasonably comfortable working with Rust,
but there are still lots of things left to learn. My next goal is to write a
native Cocoa frontend for Punchtop which means either using the
objc
and
cocoa
crates or embedding
cast-client
into a Swift app via FFI. Either way,
I am excited to make more progress.
