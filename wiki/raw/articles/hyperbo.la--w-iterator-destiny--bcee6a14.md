---
title: "Ruby Enumerable: Manifest Destiny"
url: "https://hyperbo.la/w/iterator-destiny/"
fetched_at: 2026-04-29T07:02:15.337716+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Ruby Enumerable: Manifest Destiny

Source: https://hyperbo.la/w/iterator-destiny/

ECMAScript 2025 Iterators
continues the manifest destiny of
Ruby
Enumerable
.
Lazy, internal iteration with a rich set of combinators that can be collected
into arbitrary collections in a single allocation are are an immensely powerful
primitive. A universal vocabulary type every language should have.
Rust’s
Iterator
trait is a modern embodiment of this pattern, but
it is not the first. Ruby’s
Enumerable
has existed since at
least Ruby 1.0 (released in 1996).
Ruby’s Enumerable mixin was decades ahead of its time. ECMAScript 2025’s
Iterator type moves JavaScript toward the elegance and composability that Ruby
and Rust developers have long enjoyed, continuing the slow but steady march of
iterator-based programming becoming a universal vocabulary across languages.
Ruby
Here’s what this pattern looks like in Ruby, where it has been refined over
decades.
%w[kiwi apple banana cherry]
.
filter
{ |f| f.
length
>
4
}.
map
.
each_with_index
do
|f, idx|
weight
=
(idx
+
1
)
*
f.
length
[f, weight]
end
.
to_h
# => {"apple" => 5, "banana" => 12, "cherry" => 18}
Rust
Rust’s Iterator trait offers a rich set of combinators with strong type safety
and zero-cost abstractions. Here’s the same transformation, using zip to pair
each filtered element with its index:
let
m
=
[
"kiwi"
,
"apple"
,
"banana"
,
"cherry"
]
.
into_iter
()
.
filter
(
|
f
|
f
.
len
() >
4
)
.
zip
(
1_
usize
..
)
.
map
(
|
(f, idx)
|
{
let
weight
=
idx
*
f
.
len
();
(f, weight)
})
.
collect
::
<
HashMap
<
&
'
static
str
,
usize
>>();
dbg!
(m);
// [src/main.rs:13:5] m = {
//     "cherry": 18,
//     "apple": 5,
//     "banana": 12,
// }
ES2025
JavaScript’s upcoming Iterator type brings lazy, chainable iteration to the
language. While it still lacks built-in combinators like zip and leans on
generator semantics, it’s finally moving toward the ergonomics Ruby and Rust
have long enjoyed:
let
idx
=
1
;
const
m
=
new
Map
(
Iterator.
from
([
"kiwi"
,
"apple"
,
"banana"
,
"cherry"
])
.
filter
((
f
)
=>
f.
length
>
4
)
.
map
((
f
)
=>
{
const
weight
=
idx
++
*
f.
length
;
return
[f, weight];
})
.
toArray
(),
);
console.
log
(m);
// Map(3) {'apple' => 5, 'banana' => 12, 'cherry' => 18}
ECMAScript’s new iterator features bring it closer to the elegance of Ruby and
Rust, but it still has room to grow in terms of composability and built-in
utilities. As more developers embrace iterator-based design, we may finally see
this decades-old idea become truly universal.
