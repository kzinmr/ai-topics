---
title: "Data-directed programming in Haskell (SICP 2.4.3)"
url: "https://entropicthoughts.com/sicp-2-4-data-directed-programming-in-haskell"
fetched_at: 2026-07-01T07:00:53.717833+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Data-directed programming in Haskell (SICP 2.4.3)

Source: https://entropicthoughts.com/sicp-2-4-data-directed-programming-in-haskell

Complex numbers can be stored in their rectangular form, with a real
and an imaginary part. They can also be stored in polar form, where there’s a
magnitude and an angle. Whichever way a complex number is stored, we would like
to be able to query it for all of these four quantities:
The real coordinate in the rectangular form of the complex number.
The imaginary coordinate in the rectangular form.
The magnitude in the polar form.
The angle in the polar form.
Last time we implemented these on top of a
tagged
value. To return one of the
four coordinates above, a function would introspect the tag to figure out how to
satisfy the caller for the representation involved. This works, but any time we
want to add a new representation, we have to change all four existing
operations.
To get around that problem, Abelson and Sussman suggest a data-directed approach
instead. We won’t start at the lowest level of Lisp like in the previous
article, but jump in around halfway, when we are using compiler-recognised
tuples and strings for tagging our types. That means we are starting from this code:
In[1]:
attach_tag
tag contents
=
(tag, contents)
type_tag
(tag,
_
)
=
tag
contents
(
_
, value)
=
value
is_rectangular
z
=
type_tag z
==
"rectangular"
is_polar
z
=
type_tag z
==
"polar"
make_rectangular
re im
=
(attach_tag
"rectangular"
(re, im))
make_polar
r a
=
(attach_tag
"polar"
(r, a))
In the book, the authors use two magical functions
get
and
put
to store and
retrieve operations from an implicitly declared table of operations. Here’s what
those two functions look like in our Haskell code:
In[2]:
put
op tag fn
=
State.modify (Map.insert (op, tag) fn)
get
op tag
=
State.gets (Map.lookup (op, tag))
We will use them to install operations for the rectangular representation, just
like in the Lisp code in
sicp
.
In[3]:
install_rectangular
=
let
real_part (re,
_
)
=
re
    imag_part (
_
, im)
=
im
    magnitude (re, im)
=
sqrt (re
^
2
+
im
^
2)
    angle (re, im)
=
atan2 im re
in
do
put
"real_part"
"rectangular"
real_part
    put
"imag_part"
"rectangular"
imag_part
    put
"magnitude"
"rectangular"
magnitude
    put
"angle"
"rectangular"
angle
We do the same for the polar representation.
In[4]:
install_polar
=
let
real_part (r, a)
=
r
*
cos a
    imag_part (r, a)
=
r
*
sin a
    magnitude (r,
_
)
=
r
    angle (
_
, a)
=
a
in
do
put
"real_part"
"polar"
real_part
    put
"imag_part"
"polar"
imag_part
    put
"magnitude"
"polar"
magnitude
    put
"angle"
"polar"
angle
We re-implement the
apply_generic
function from
sicp
to pick the right
operation from this table.
In[5]:
apply_generic
op arg
=
do
value
<-
get op (type_tag arg)
  pure
$
case
value
of
Just
fn
->
fn (contents arg)
Nothing
->
error
"No method for these types."
This operation can be used to implement the generic coordinate extraction functions.
In[6]:
real_part
z
=
apply_generic
"real_part"
z
imag_part
z
=
apply_generic
"imag_part"
z
magnitude
z
=
apply_generic
"magnitude"
z
angle
z
=
apply_generic
"angle"
z
Then, because we are writing this in Haskell, the complex number arithmetic is
going to look a little clumsy. Don’t worry, we’ll fix that soon.
In[7]:
add_complex
za zb
=
do
za_re
<-
real_part za
  za_im
<-
imag_part za
  zb_re
<-
real_part zb
  zb_im
<-
imag_part zb
  pure
$
make_rectangular (za_re
+
zb_re) (za_im
+
zb_im)
mul_complex
za zb
=
do
za_r
<-
magnitude za
  za_a
<-
angle za
  zb_r
<-
magnitude zb
  zb_a
<-
angle zb
  pure
$
make_polar (za_r
*
zb_r) (za_a
+
zb_a)
To run a computation with this, we have to run it as a stateful computation,
where we first install the operations, and then perform the computations. It
might look like this.
In[8]:
main
=
flip State.evalStateT Map.empty
$
do
install_rectangular
  install_polar
  zc
<-
add_complex (make_polar 4 0.3) (make_rectangular 3 2)
  s
<-
show_complex zc
  liftIO (putStrLn s)
Great! We can do what Lisp can do.
