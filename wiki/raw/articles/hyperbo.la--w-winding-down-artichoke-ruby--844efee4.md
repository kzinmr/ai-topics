---
title: "Winding Down Artichoke Ruby"
url: "https://hyperbo.la/w/winding-down-artichoke-ruby/"
fetched_at: 2026-04-29T07:02:15.151202+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Winding Down Artichoke Ruby

Source: https://hyperbo.la/w/winding-down-artichoke-ruby/

On November 3, 2025, I archived
Artichoke Ruby
; over the rest
of November 2025, I archived most other repositories in the
@artichoke
GitHub organization.
This was long overdue but something I resisted for a long time, because shutting
it down felt like admitting that the Hacker News commenter was right — that
most alternative Ruby VMs eventually run out of steam
— and I
wasn’t ready to let Artichoke become another data point in that pattern.
Why I Started Artichoke
Artichoke did not start as a grand plan to “fix Ruby.” It started as a toy.
I wanted to build a Rube Goldberg machine: a Monaco editor UI that would let you
write Ruby code, have that Ruby generate SCSS, and then restyle the page
dynamically through a Tokio HTTP server. To do that, I reached for the
mrusty
crate’s bindings to mruby.
Those bindings worked, but they were rough around the edges and occasionally
crashy. (To be fair: they were doing something hard.) One thing led to another,
and instead of building the UI toy, I started strangler-figging mruby —
gradually replacing pieces of it with Rust implementations. Martin Fowler’s
description of the
Strangler Fig pattern
captures the idea well.
That process turned into “oxidizing” mruby.
It was always exploratory. I never believed Artichoke would compete with CRuby,
JRuby, or TruffleRuby. I wanted to see how far I could push it. The original
intent is still captured in the project’s
VISION.md
.
The moment it felt real was when I implemented
Regexp
— something mruby did
not have — and then
talked about it at RubyConf 2019
. Standing
on that stage talking about a Rust-backed Ruby implementation made the
experiment tangible.
What I Built
Over six years, Artichoke became far more real than it had any right to. I’m
proud of several things.
A spec-compliant
String
in pure Rust
Artichoke shipped a fully spec-compliant
String
implementation written 100% in
Rust, built on top of the
bstr
crate. That effort fed back into the Rust
ecosystem, and I’m grateful to have been mentioned in Andrew Gallant’s
announcement post for
bstr
.
Writing
String
forced me to understand Ruby’s encoding semantics, byte vs.
character boundaries, grapheme assumptions, and the subtle ways MRI behaves in
edge cases. It was foundational work.
A modular, capability-oriented VM architecture
Artichoke leaned heavily into Cargo features and crate modularity.
The architecture deliberately separated:
VM-shaped concerns (
artichoke-*
)
Core data structures (
spinoso-*
)
VM internals and glue (
mezzaluna-*
)
Pure utilities (
scolapasta-*
)
This structure is documented in
ARCHITECTURE.md
and influenced by ideas like
matklad’s writing on documenting repository
architecture
.
The goal was loose coupling. You could assemble an interpreter with only the
capabilities you wanted. Native functionality was trait-driven and composable.
Learning why the GIL exists
One of the most instructive arcs in the project was unwinding an early
architectural shortcut: wrapping interpreter state in
Rc<RefCell<_>>
.
PR #442
attempted to destructure the massive
State
struct, but that
early decision had infected the entire codebase. It never compiled as-is and
ultimately spawned dozens of smaller refactors.
PR #670
completed the removal of
Rc<RefCell<_>>
and realigned the
interpreter around explicit
&mut Artichoke
borrowing.
That migration forced nearly every interpreter API to take
&mut self
and
completely reworked the structure of the codebase. The borrow checker made the
mutability boundaries painfully clear.
mruby’s design of passing around an
&mut Interp
reflects where mutability
lives in a dynamic language runtime and where the heap is.
Going through this made it obvious why YARV and CPython converge on something
GIL-shaped: aliasing and shared mutable state in an interpreter are brutally
hard to model otherwise.
Ruby the language is tightly coupled to C and POSIX assumptions. Arrays want to
be contiguous buffers. Attempts to hyper-specialize core structures (like
optimizing empty/one/two-element cases à la Scala maps) feel misaligned with how
MRI models the world. Artichoke ultimately leaned into that reality instead of
fighting it.
The education
Artichoke forced me to learn Rust deeply: unsafe code, FFI boundaries, pointer
lifetimes, trait design, runtime architecture, borrow semantics under stress.
That education alone justified the experiment.
Why I’m Winding It Down
There’s no dramatic reason; I simply haven’t had the time.
As I’ve gotten older, my focus has shifted toward work and family. OpenAI is
demanding in the best possible way, and the opportunity cost of maintaining a
language runtime — even an experimental one — became too high.
There was also a subtle shift in joy. Much of the magic of Artichoke was pushing
myself to learn Rust “by hand.” I achieved that. I now have deep experience in
unsafe Rust, low-level design, and FFI. That foundation makes me effective using
coding agents and modern tooling — but it also means the original spark of “can
I figure this out?” has diminished.
There’s also the reality of compatibility toil. Artichoke’s mspec and ruby/spec
target MRI 2.6.3. Keeping up with upstream Ruby is endless work. Updating spec
versions, reconciling behavioral changes, chasing edge cases — it never ends.
And without a real user base (or a desire to cultivate one), there’s no
compelling reason to shoulder that burden.
I knew it was over when I didn’t start implementing
Hash
— the next core class
to oxidize — for three years after completing
String
.
What Happens Next
Artichoke is archived but not erased. The repositories remain public. The
architecture documents are intact. The code can still be studied, forked, or
embedded. I do not plan to resume active development.
For old updates and project history, tweets are still up at
@artichokeruby
.
If you depend on Artichoke in production, you should plan a migration path to
CRuby or another actively maintained implementation. Artichoke will not receive
compatibility updates, new features, or security patches.
It is complete in the sense that it accomplished what it set out to do.
Thank You
Archiving does not feel like failure. Artichoke served its purpose for me. It
pushed boundaries. It forced growth. It left artifacts that I’m proud of.
And it’s nice not to review monthly Dependabot PRs anymore. 🤖
Thank you to everyone who filed issues, sent patches, asked questions, or just
believed that building a Ruby implementation in Rust was worth trying.
Special thanks to my co-maintainers:
If there’s anything I hope readers take away from this, it’s this: Build things.
Even weird things. Even things that might not last forever. The act of building
changes you.
