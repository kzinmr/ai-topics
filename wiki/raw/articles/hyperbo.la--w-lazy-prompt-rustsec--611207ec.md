---
title: "A Lazy Prompt Turned Into a RustSec Advisory"
url: "https://hyperbo.la/w/lazy-prompt-rustsec/"
fetched_at: 2026-04-29T07:02:14.942133+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# A Lazy Prompt Turned Into a RustSec Advisory

Source: https://hyperbo.la/w/lazy-prompt-rustsec/

Authorship note: Codex, a coding agent, drafted this post from a repo-local
session transcript and notes. I rewrote it heavily and published it.
Using coding models for security hardening is amazing. I pointed Codex at one of
my Rust crates,
intaglio
, with a
laughably lazy prompt and got a real vulnerability out of it:
RUSTSEC-2026-0078
.
Nothing about the prompt was clever. The useful part was the bar: do a complete
analysis and prove impact or exploitability for anything you report.
The Prompt
you are red teaming this repo to look for security vulnerabilities. do a
complete analysis. you must prove impact or exploitability for anything you
report to me
This prompt has been super productive because it forbids speculative bug
reports. “This looks suspicious” is not enough. The model has to build a
reproducer, show the bad behavior, and narrow the claim to what it can actually
prove.
The Bug
Codex found a cross-cutting unwind-safety bug in
intaglio
’s
intern
implementation. The write ordering was wrong:
intern
pushed into the backing
Vec
before it inserted the matching key into the
HashMap
. If a custom
BuildHasher
panicked during
HashMap::insert
and the embedding application
recovered with
catch_unwind
, the interner could keep going with its two
internal indexes out of sync.
use
intaglio
::
SymbolTable
;
use
std
::
{
hash
::
{
BuildHasher
,
Hasher
},
panic
::
{catch_unwind,
AssertUnwindSafe
},
sync
::
{
atomic
::
{
AtomicUsize
,
Ordering
},
Arc
,
},
};
#[derive(
Clone
,
Debug
)]
struct
PanicBuildHasher
{
builds
:
Arc
<
AtomicUsize
>,
}
impl
BuildHasher
for
PanicBuildHasher
{
type
Hasher
=
PanicHasher
;
fn
build_hasher
(
&
self
)
->
Self
::
Hasher
{
let
build
=
self
.
builds
.
fetch_add
(
1
,
Ordering
::
SeqCst
)
+
1
;
PanicHasher
{ build, hash
:
0
}
}
}
#[derive(
Debug
)]
struct
PanicHasher
{
build
:
usize
,
hash
:
u64
,
}
impl
Hasher
for
PanicHasher
{
fn
finish
(
&
self
)
->
u64
{
self
.
hash }
fn
write
(
&mut
self
, bytes
:
&
[
u8
]) {
if
self
.
build
==
1
{
panic!
(
"panic during first HashMap::insert hashing"
);
}
for
byte
in
bytes {
self
.
hash
=
self
.
hash
.
wrapping_mul
(
131
)
.
wrapping_add
(
u64
::
from
(
*
byte));
}
}
}
fn
main
() {
let
mut
table
=
SymbolTable
::
with_hasher
(
PanicBuildHasher
{ builds
:
Arc
::
new
(
AtomicUsize
::
new
(
0
)) });
let
first
=
catch_unwind
(
AssertUnwindSafe
(
||
table
.
intern
(
"attacker"
)));
println!
(
"first_err={} len={} check(attacker)={:?}"
,
first
.
is_err
(), table
.
len
(), table
.
check_interned
(
"attacker"
),
);
let
sym
=
table
.
intern
(
"victim"
)
.
expect
(
"second intern succeeds in release mode"
);
println!
(
"victim_symbol={}"
, sym
.
id
());
println!
(
"check(victim)={:?}"
, table
.
check_interned
(
"victim"
));
println!
(
"get(victim_symbol)={:?}"
, table
.
get
(sym));
}
In release mode, that turned into symbol confusion.
intern("attacker")
could
panic on the first insert, the caller could catch the panic and keep going, and
a later
intern("victim")
could return
Symbol(0)
even though
get(Symbol(0))
resolved to
"attacker"
. That is enough for an advisory.
I did not prove memory unsafety on the default
RandomState
path. The bug
needed a custom
BuildHasher
, a panic during hashing, and a caller that kept
using the table after
catch_unwind
. That was the bug.
Carrying It Through
The agent did the full job end to end, from identification and fix to vuln
publication.
The paper trail is public:
The Same Prompt Elsewhere
This same prompt found at least
something
in every active Artichoke crate I
pointed it at:
missing
npm ci
install in one Prettier GitHub Actions job
rand_mt
docs that over-emphasized the
new_unseeded
constructor
raw-parts
missing
compile_fail
coverage for
Send
and
Sync
auto traits
and lifetime expansion
sysdir
tests that were not robust to
NEXT_ROOT
being set, plus missing
docs around
NEXT_ROOT
and
~
in returned paths
This workflow works because the standard is high and the prompt is simple. Do
not ask the model to brainstorm bugs. Ask it to prove them. That turns the
output from security-flavored vibes into engineering work: reproducer, tests,
fix, release, advisory.
