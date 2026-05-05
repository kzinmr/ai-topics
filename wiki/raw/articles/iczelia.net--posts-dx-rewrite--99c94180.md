---
title: "Domain eXtensions for Dyalog APL"
url: "https://iczelia.net/posts/dx-rewrite/"
fetched_at: 2026-05-05T07:01:23.217446+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Domain eXtensions for Dyalog APL

Source: https://iczelia.net/posts/dx-rewrite/

I took a few attempts at writing APL interpreters. Initially, I settled on making a library implementing the APL dialect that would suit me, and then move onto implementing it in C or C++.
My first attempt contained a few mostly useless additional primitives and used a fairly unusual input method (string argument; could probably be made a
bit
better with a REPL). It featured a bunch of things I liked from J (
1-⍨ => <:
,
1+ => >:
) and a bunch of things that I missed from other languages (like format strings, filter operator, n-th satisfying, value mapping -
'a' 2 'b' 4 ⍈ 'abab'
returning
2 4 2 4
, etc…).
After noticing how divorced from usefulness this implementation was, I decided to start a new project and pick a different approach. This time, the library would be a standard APL dop that queries the character representation of said dfn, performs replacements on the tokenised version and then executes it in a custom namespace which contains all the required definitions.
Having established that, I moved into the implementation. Around then I didn’t know that
60⌶
exists (an I-beam service for tokenising APL code), so I rolled my very own, partially broken and small APL lexer and implemented a bunch of new builtin functionalities.
Finally, around the time of writing this blog post, I wanted to rework my library. So here it comes.
Project goals
⌗
I decided to sketch a few goals that I’d like to accomplish while putting this project to life:
More concise and reasonable programs
Common functionality shouldn’t be hidden behind a long and complex sequence of APL primitives (
{⍵[⍋⍵]}
should totally be a single glyph)
The domain of many primitives should be extended to make programming a bit more straightforward
The library should be easy to use and integrate into existing programs
It should be easy to add new primitives to it
… and here’s a bunch of things that I decided to not care about:
Performance. Since this is a proof of concept and not an actual C or C++ implementation, performance isn’t a concern.
Uniqueness. I should borrow from other APL extensions to make my own dialect even better.
Starting the implementation
⌗
I start the implementation with sketching an APL lexer that is capable of performing replacements to make our custom tokens work and execute the resulting code. Let’s start by defining a few testing primitives:
Our primitives table is structured this way:
┌────────┬─────────┐
│┌─┬────┐│┌─┬─────┐│
││~│_Neg│││√│_Root││
│└─┴────┘│└─┴─────┘│
└────────┴─────────┘
We want to extract the corresponding primitive tokens to then perform replacements, which is accomplished using this short snippet:
We modify our source code accordingly:
Now, it would be nice to actually query the code we’re going to execute. I used
⎕CR
to query the character representation of a
dfn
. Not so fast, though:
It seemed like
⎕CR
doesn’t work with the dop left/right operand (although
⎕NC
seems to?), so we’re making a workaround by creating a temporary variable:
The character representation is a matrix, since we can query for character representation for multiline
dfn
s:
… so we turn it into a vector of lines using grade down and tokenise each element of it:
There are a few concerns though. We can’t directly evaluate the result of
⎕cr
, because input to
⍎
has to be a string. We can work around this by adding statement separators after the end of each line (excluding the last line, otherwise the value will be discarded). This, of course, requires stripping line comments. So we do that now.
This expression is pretty tangled, so let me explain it:
⊃⊃⌽⍵
takes the first character of the last token in a line.
We check if this token is a comment character (
'⍝'=
).
The comparison will either return 0 or 1.
To drop the last element of a vector, we use
¯1↓vec
If we negate the result of this comparison, i.e.
-'⍝'=⊃⊃⌽⍵
, we get ¯1 if the last token should be stripped, and 0 if it shouldn’t.
To avoid having to type out parenthesis, we use
⍵↓⍨-'⍝'=⊃⊃⌽⍵
instead of
(-'⍝'=⊃⊃⌽⍵)↓⍵
.
To avoid
⋄⋄
being present in the code and to simplify matters in the future, we filter out empty lines by checking if their length is zero:
{⍵/⍨{0≠≢⍵}¨⍵}
. Finally, we want to pass this input to the replacement function, which modifies the code line by line. To sum up, we worked out this much so far:
Where
t3
is our translation function and
r
is (ideally) the preprocessed code. Let’s implement
t3
now.
Since we receive a tokenised line, we iterate over each of the tokens to check if the first character
of the said token is present in our keys vector and pick the index at which this is the case.
For example, inside
t3
:
The next obvious step is juxtaposing the code against the matches:
,⍥⊂¨⍨
is a fairly complex construct, so let’s untangle it. First, we enclose both sides (
⊂
), then we catenate them (
,
) -
,⍥⊂
. We do that for each element, but we want our table correspondence vector to go first, so we commute this operation, giving
,⍥⊂¨⍨
. For the test case above, this code returns:
If the length of the translation vector part is zero (not a custom token), we use the second element of this tuple to produce output, so we write it as
{0=≢⊃⍵:⊃⌽⍵⋄⍵}
(ignoring the translation case for now). Example output:
Let’s handle the translation case now. We take the index in the table by picking first tuple element, then we get the element under this index, and pick the second tuple element of this (remember: our translation tuple is a vector of tuples where first element represents the index in translation table and the second element represents the token, meanwhile the translation table is a vector of tuples where the first element is the token and the second element is the function name inside our namespace). We implement this:
For the evaluated code to be valid, every line needs to end with a statement separator, and tokens should have a space between each other (to not merge for example identifiers with numbers). The implementation is rather simple:
Finally, we figure out the arity of our function. If
2=⎕NC'⍺'
, then we were called dyadically. We use a guard to switch between the dyadic and monadic version:
Full source code:
Custom primitives
⌗
Currently our extension is a bit empty and useless. Let’s provide some common functionality to it. We will import
dfns
since the
pco
function (among others) will be useful later on.
Let’s define a few features from J that I missed all along:
Reverse compose, better rounding, matrix multiplication and generating identity matrices might be useful:
I also decided to borrow Adam Brudzewsky’s range function and translate the tradfn alternant from the dfns workspace into a more sane and modern version:
The fibonacci builtin will stick along:
Of course, I’m fixing the sorting problems too:
I also decided to include glyphs for iterating a function infinitely and taking the inverse of it (sometimes useful when we use APL as a calculator):
The other extension is fairly niche, but it looks handy. We add a primitive to take the middle of a vector, dyadically:
… so, for example:
The
,⍥⊂
idiom I tried to explain earlier is fairly common in APL code, so we define a separate pair function for this (
{⍺⍵}
). Since we’re at it, the pair function is only dyadic, so some functionality could be packed into the monadic invocation of it. I decided to turn the pair function into a constant function:
We also include Euler’s totient as a builtin. Filter from
xapl
shares the same fate:
Finally, we add monadic/dyadic variants to existing primitives. Monadic equality will now check if all elements of a vector are equal, and monadic NAND/NOR will generate a prefix/suffix array:
Down tack will now default to base-10 and it’ll be a tiny bit saner:
Improvements
⌗
I compiled a list of potential improvements while skimming through the code:
Better matching system for the replacements.
Skim through my old/someone’s else APL code to see if there are any more annoying idioms missing in APL.
Each left / each right operator borrowed from K.
Power (
⍣
) with immediate results.
Syntax extensions (= implement something else besides just primitives).
RIDE
⌗
While I was working on DX, I noticed that the RIDE editor UX is far from perfect. Also, I wanted to add my primitives to the language bar. On my personal fork of RIDE, I decided to
add a Fix button and remove the Fix menu option on right-click
. In the next commit,
I added language bar support for RIDE
:
Summary
⌗
I think that
dx
is a fairly nice project. I worked on the rewrite for around 4 hours. All in all, I consider it time well spent.
I will be trying to incorporate some improvements to DX listed above when I have some more time on my hands. For now, though, that’s all I’ve prepared for this article. ’til the next time :).
