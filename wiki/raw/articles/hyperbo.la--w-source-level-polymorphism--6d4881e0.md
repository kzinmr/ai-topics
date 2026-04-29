---
title: "Source-level Polymorphism in Rust"
url: "https://hyperbo.la/w/source-level-polymorphism/"
fetched_at: 2026-04-29T07:02:15.568441+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Source-level Polymorphism in Rust

Source: https://hyperbo.la/w/source-level-polymorphism/

Artichoke Ruby
is a Ruby
implemented in Rust
. As Artichoke
strangles
its
mruby
core, I’ve been capturing core data
structures from the VM into Rust code.
Artichoke is a Cargo workspace and uses separate crates for implementing the
data structures that back Ruby Core APIs.
Splitting core data structures into their own crates helps me ensure they are
high quality. For example, crates
fail CI if they have missing documentation
.
Using a separate crate for each data structure also makes it easier to have
multiple implementations of the API.
Multiple Implementations
Having multiple implementations of core data structures allows Artichoke to be
built with different use cases in mind. For example, Artichoke distributes a
ruby
CLI frontend that should allow users to interact with the host system;
but Artichoke also aims to support embedding use cases which may wish to limit
the ways the interpreter may interact with the host system.
VISION.md
expounds
on
Artichoke’s design and goals
.
Array
spinoso-array
is the crate that implements the contiguous buffer type that
backs
Ruby
Array
. Using conditional compilation with
cargo features
,
spinoso-array
by default exposes two concrete buffer types:
Array
, which is backed by a Rust
Vec
, and
SmallArray
, which is backed by a
SmallVec
.
spinoso-array
does not have a trait that unifies these two types to ensure
they can be used interchangeably. Instead, these structs implement the exact
same API. Flipping between implementations is as simple as changing an import:
use
spinoso_array
::
Array
as
SpinosoArray
;
// or
use
spinoso_array
::
SmallArray
as
SpinosoArray
;
ENV
Another data structure that implements the multiple backend pattern is
Artichoke’s access to environment variables.
spinoso-env
implements multiple
types that expose an identical API for accessing the environment:
System
is a wrapper around
std::env
and gives Ruby
code access to the platform environment variables via native APIs.
Memory
is a wrapper around a
HashMap
, which allows
Ruby code to have a functional
ENV
in environments where mutable
access to the host system’s environment is undesirable (if embedding Artichoke
in another application) or unavailable (if building for e.g. the
wasm32-unknown-unknown
target).
The Artichoke VM is
configurable at compile-time
to select the
ENV
backend:
[
features
]
# Enable resolving environment variables with the `ENV` core object.
core-env = [
"spinoso-env"
]
# Enable resolving environment variables with the `ENV` core object using native
# OS APIs. This feature replaces the in-memory backend with `std::env`.
core-env-system = [
"core-env"
,
"spinoso-env/system-env"
]
The code that wires up the environment backend indirects the concrete type with
a
conditionally-compiled type alias
and requires no
other code changes:
#[cfg(not(feature
=
"core-env-system"
))]
type
Backend
=
spinoso_env
::
Memory
;
#[cfg(feature
=
"core-env-system"
)]
type
Backend
=
spinoso_env
::
System
;
Polymorphism
Source-compatible data structure implementations have the following nice
properties:
Traits don’t need to be in scope to use data structure APIs.
No reliance on trait objects.
No monomorphization or generics.
Conditional compilation is lightweight.
