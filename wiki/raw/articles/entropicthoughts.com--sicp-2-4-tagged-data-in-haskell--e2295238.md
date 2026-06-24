---
title: "Tagged data in Haskell (SICP 2.4.2)"
url: "https://entropicthoughts.com/sicp-2-4-tagged-data-in-haskell"
fetched_at: 2026-06-24T07:01:01.246254+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Tagged data in Haskell (SICP 2.4.2)

Source: https://entropicthoughts.com/sicp-2-4-tagged-data-in-haskell

Complex numbers can be stored in their rectangular form, where there’s a real
and an imaginary part. They can also be stored in polar form, where there’s a
magnitude and an angle. The authors ask us to imagine that two people have been
working on a library for mathematics, but ended up choosing different ways to
store complex numbers. How can they write their code so that they don’t have to
agree on one way to store the data?
Abelson and Sussman propose a
tagged
representation, where the data of the
complex numbers are paired with a tag, which indicates to the implementation
what representation is being used. They suggest the following functions to
attach a tag, as well as inspect tagged data.
As a last reminder, this is Haskell code, but written in Lisp style to mimic the
solution in
sicp
as closely as possible.
In[1]:
-- | Tag a value as having a particular representation.
attach_tag
tag contents
=
(cons tag contents)
-- | Extract the type tag from a tagged value.
type_tag
datum
=
(if_ (is_pair datum)
       (car datum)
       (error
"Bad tagged datum"
))
-- | Extract the value from a tagged value.
contents
datum
=
(if_ (is_pair datum)
       (cdr datum)
       (error
"Bad tagged datum"
))
This code uses
cons
in the Lisp sense, i.e. it creates a pair of two values,
with a left hand side, known as the
car
of the pair, and a right hand side,
known as the
cdr
of the pair.
With these, we can check if a complex number is stored in its rectangular or
polar representation by inspecting its tag.
In[2]:
is_rectangular
z
=
(eq (type_tag z) (quote
"rectangular"
))
is_polar
z
=
(eq (type_tag z) (quote
"polar"
))
To create a complex number in either rectangular or polar form, we create a cons
cell with the coordinates, and tag that cell with the appropriate symbol.
In[3]:
make_rectangular
re im
=
(attach_tag (quote
"rectangular"
) (cons re im))
make_polar
r a
=
(attach_tag (quote
"polar"
) (cons r a))
If we have the rectangular coordinates for a complex number, we can extract the
real and imaginary part easily, too. These functions assume we have peeled off
the tag, and that the data is in the correct format.
In[4]:
real_part_rectangular
z
=
(car z)
imag_part_rectangular
z
=
(cdr z)
Similarly, we can easily extract the polar coordinates from a complex number
stored in its polar form. These implementations are the same as the above,
because these functions are supposed to be run after we have verified the tag is
correct, and the tag has been peeled off.
In[5]:
magnitude_polar
z
=
(car z)
angle_polar
z
=
(cdr z)
If we want to extract polar coordinates from a complex number stored in
rectangular form, or vice versa, we’ll have to do some trigonometry.
In[6]:
magnitude_rectangular
z
=
(sqrt_ (add_ (square_ (real_part_rectangular z))
               (square_ (imag_part_rectangular z))))
angle_rectangular
z
=
(atan_ (imag_part_rectangular z)
          (real_part_rectangular z))
real_part_polar
z
=
(mul_ (magnitude_polar z) (cos_ (angle_polar z)))
imag_part_polar
z
=
(mul_ (magnitude_polar z) (sin_ (angle_polar z)))
These functions also assume a particular representation, with the tag peeled
off. But, now that we have all of the above, we can write our first
generic
functions, i.e. those that can work on either representation. They’ll do this by
inspecting the tag and then performing the right operation depending on what
representation is indicated by the tag.
These generic functions will extract the respective coordinates for complex
numbers regardless of their underlying representation, by dispatching on the
type tag.
In[7]:
real_part
z
=
(if_ (is_rectangular z)
       (real_part_rectangular (contents z))
       (if_ (is_polar z)
            (real_part_polar (contents z))
            (error
"Unknown type"
)))
imag_part
z
=
(if_ (is_rectangular z)
       (imag_part_rectangular (contents z))
       (if_ (is_polar z)
            (imag_part_polar (contents z))
            (error
"Unknown type"
)))
magnitude
z
=
(if_ (is_rectangular z)
       (magnitude_rectangular (contents z))
       (if_ (is_polar z)
            (magnitude_polar (contents z))
            (error
"Unknown type"
)))
angle
z
=
(if_ (is_rectangular z)
       (angle_rectangular (contents z))
       (if_ (is_polar z)
            (angle_polar (contents z))
            (error
"Unknown type"
)))
Given these, the two people no longer have to agree on how they should store
complex numbers. Each can choose their own representation, and then they can
write generic maths functions over complex numbers, like these.
In[8]:
add_complex
za zb
=
(make_rectangular
    (add_ (real_part za) (real_part zb))
    (add_ (imag_part za) (imag_part zb)))
mul_complex
za zb
=
(make_polar
    (mul_ (magnitude za) (magnitude zb))
    (add_ (angle za) (angle zb)))
These functions are written to exploit that addition of complex numbers is
easier in rectangular form, but multiplication is easier in polar form. It
doesn’t matter how
za
and
zb
are stored, because we get the appropriate
coordinates out of them either way.
This is the solution in
sicp
, and we did it in Haskell. But now I got curious
if we could leverage the strengths of Haskell to make the code more clear.
