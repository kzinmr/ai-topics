---
title: "LLMs and almost good code"
url: "https://entropicthoughts.com/llms-and-almost-good-code"
fetched_at: 2026-06-09T07:01:22.688795+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# LLMs and almost good code

Source: https://entropicthoughts.com/llms-and-almost-good-code

tl;dr
: My new prior is that top-of-the-line
llm
s working on
easy
tasks
generate code that is maybe 10 % more complicated than necessary. I also think
we accept this complexity too easily, because it comes from code that is
right
here
,
right now
, solving an immediate problem. This may have consequences
for maintenance in the long term.
The background to this discovery was that I needed to do some
crud
plumbing in
a work project. It was a simple change that mostly mirrored existing
functionality. This is a perfect fit for
llm
s, in my experience, so I used a
frontier model to generate the code for it. The change ended up being a total of
just over 200 lines, mostly additions.
The part of the generated code we’ll talk about is a 24-line function that
converts an arbitrary (user-supplied) string to a safe
http
header
value.
1
Encoding it into a safe value is necessary to avoid confusing
mistakes, but also to prevent
http
header injection attacks.
In[1]:
toHeaderValue
::
Text
->
Text
toHeaderValue
raw
=
let
attrChars
=
"!#$&+-.^_`|~"
padHex t
=
if
Text.length t
<
2
then
"0"
<>
t
else
t
    percentEncode c
=
if
(isAscii c
&&
isAlphaNum c)
||
elem c attrChars
then
Text.singleton c
else
Text.concat
          [
"%"
<>
padHex (Text.toUpper (Text.pack (showHex b
""
)))
|
b
<-
ByteString.unpack (encodeUtf8 (Text.singleton c))
          ]
    rfc5987Encode
=
Text.concatMap percentEncode
    isPrintable c
=
c
>=
' '
&&
c
/=
'\DEL'
replacePathSeparator c
=
if
c
==
'/'
||
c
==
'\\'
then
'_'
else
c
    cleaned
=
Text.map replacePathSeparator (Text.filter isPrintable raw)
in
rfc5987Encode cleaned
When looking at this function like this, it obviously seems a bit too
complicated, but recall that this was just 24 lines in a 200-line change. I
confirmed that the underlying idea was correct, and that the generated tests
covered all the edge cases I would want to see covered. It’s not
pretty
code,
but it is proven correct by tests.
More importantly, it is highly local. If anything about this code needs
replacing, it can be replaced without touching anything else. Apprentice-level
programmers worry equally about code quality everywhere; I’ve long wanted to
write an article called “
Don’t worry, it’s local
” where I tell these
programmers that bad code quality is fine, as long as it’s self-contained in a
small location.
2
The reason I haven’t written that article is that I’m
waiting on a bunch of examples the article would need. But I keep forgetting to
collect them, so the total number of examples I have collected so far are zero.
I accepted this code. I needed the implementation to work, and this code
obviously worked. It was
right there
,
right now
. It would have been silly to
not accept it! Accepting it was the easy choice, and certainly not a bad
decision.
However, in a pleasant twist of fate, the
ci
pipeline for this project has a
mandatory statement test coverage check
3
I’m not a huge fan of statement
coverage, but that’s another separate article I’ve put off writing for years.
,
and that check failed for this code. See if you can spot where and why.
I’ll give you a hint: it has to do with the
padHex
function, which takes a
hexadecimal value in the range
0x0
–
0xff
and zero-pads it if it is less than
0x10
.
The data passed into
padHex
has already gone through the
isPrintable
filter,
which removes all bytes lower than
0x20
. Thus no value passed to
padHex
is
ever below
0x10
, and it never ends up padding anything! It is always a no-op.
The statement coverage check warns on the padding branch of
padHex
, because it
is exercised by no test. It is in fact impossible to exercise it in a test.
This was annoying:
On the one hand, we shouldn’t assume
percentEncode
is always called with
characters greater than
0x1f
, even if that happens to be true at the moment.
Such an assumption relies on spooky action at a distance, which – even if it
is local to this function – we want to avoid.
On the other hand, the coverage report is right too: there is something
awkward about this whole construction.
So I stepped in and wrote my own implementation. The implementation that ended
up shipping was closer to this:
In[2]:
toHeaderValue
::
Text
->
Text
toHeaderValue
=
let
retainPrintable
=
Text.filter (
\
c
->
c
>=
' '
&&
c
/=
'\DEL'
)
    replacePathSeparators
=
Text.replace
"/"
"_"
.
Text.replace
"\\"
"_"
--
URL encoding is also legal RFC5987 encoding.
rfc5987Encode
=
decodeUtf8
.
urlEncode
True
.
encodeUtf8
in
rfc5987Encode
.
replacePathSeparators
.
retainPrintable
This is 15
lines of complexity
shorter. That’s around 8 % of the change.
The
llm
did not generate bad code.
4
In some sense, its code is better. The
rfc
5987 encoding is more lax than
url
encoding, so my implementation
technically over-encodes.
It just generated code that was 8 % more complex than
it needed to be. That’s not a disaster today, and when there’s pressure to ship,
it is easy to accept it because it is
right there
,
right now
, and it solves
the problem.
I
accepted and was about to ship code that was 8 % too complex.
It was only by chance I looked into it more deeply and realised the problems
with it.
This experience leaves me with a bunch of questions I don’t have answers to.
What about all the other changes that are also unnecessarily complex, but which
I accept anyway?
What if this was an easy case, and when we sic an
llm
on a more complicated
task, it generates code that is more than 8 % too complex, like 20 %, or 40 %,
or even 3× more complex than it needs to be?
Will we put our foots down when we get code that is so unnecessarily complex?
Or will we accept, because it’s not a disaster today, and it is
right there
,
right now
?
What happens in a year or two, when we continue shipping code that’s
consistently more complex than it needs to be?
On the one hand, this worries me. On the other hand, the obvious
counter-argument is that code-writing robots improve fast enough that in two
years’ time when this becomes a problem, they will know how to deal with it.
Maybe. I’m not convinced.
