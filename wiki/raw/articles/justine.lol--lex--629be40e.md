---
title: "Weird Lexical Syntax"
url: "https://justine.lol/lex/"
fetched_at: 2026-05-05T07:01:27.282930+00:00
source: "Justine Tunney"
tags: [blog, raw]
---

# Weird Lexical Syntax

Source: https://justine.lol/lex/

Oct 31
st
, 2024 @
justine's web page
Weird Lexical Syntax
I just learned 42 programming languages this month to build a new syntax
highlighter for
llamafile
. I
feel like I'm up to my eyeballs in programming languages right now. Now
that it's halloween, I thought I'd share some of the spookiest most
surprising syntax I've seen.
The languages I decided to support are Ada, Assembly, BASIC, C, C#, C++,
COBOL, CSS, D, FORTH, FORTRAN, Go, Haskell, HTML, Java, JavaScript,
Julia, JSON, Kotlin, ld, LISP, Lua, m4, Make, Markdown, MATLAB, Pascal,
Perl, PHP, Python, R, Ruby, Rust, Scala, Shell, SQL, Swift, Tcl, TeX,
TXT, TypeScript, and Zig. That crosses off pretty much everything on
the
TIOBE Index
except
Scratch
,
which can't be highlighted, since it uses blocks instead of text.
How To Code a Syntax Highlighter
It's really not difficult to implement a syntax highlighter. You could
probably write one over the course of a job interview. My favorite tools
for doing this have been C++ and
GNU gperf
. The hardest
problem here is avoiding the need to do a bunch of string comparisons to
determine if something is a keyword or not. Most developers would just
use a hash table, but gperf lets you create a perfect hash table. For
example:
%{
#include <string.h>
%}
%pic
%compare-strncmp
%language
=ANSI-C
%readonly-tables
%define
lookup-function-name
is_keyword_java_constant
%%
true
false
null
gperf was originally invented for gcc and it's a great way to squeeze
out every last drop of performance. If you run the
gperf
command on the above code above, it'll
generate this .c file
. You'll
notice its hash function only needs to consider a single character to
get a collision free lookup. That's what makes it perfect, and perfect
means better performance. I'm not sure who wants to be able to syntax
highlight C at 35 MB per second, but I am now able to do so, even though
I've defined
about
4,000 keywords
for the language. Thanks to gperf, those keywords
don't slow things down.
The rest just boils down to finite state machines. You don't really need
flex, bison, or ragel to build a basic syntax highlighter. You simply
need a
for
loop and a
switch
statement. At
least for my use case, where I've really only been focusing on strings,
comments, and keywords. If I wanted to highlight things like C function
names, well, then I'd probably need to do actual parsing. But focusing
on the essentials, we're only really doing lexing at most. See
highlight_ada.cpp
as an example.
Demo
All the research you're about to read about on this page, went into
making one thing, which is llamafile's new syntax highlighter. This is
probably the strongest advantage that llamafile has over ollama these
days, since ollama doesn't do syntax highlighting at all. Here's a demo
of it running on Windows 10, using the
Meta
LLaMA 3.2 3B Instruct
model. Please note, these llamafiles will run
on MacOS, Linux, FreeBSD, and NetBSD too.
[screencast of the Mozilla/Llama-3.2-3B-Instruct-llamafile LLM being
   used to generate code in various programming languages (FORTRAN,
   Rust, C++, Perl) for printing the first 100 prime numbers]
The new highlighter and chatbot interface has made llamafile so pleasant
for me to use, combined with the fact that open weights models
like
gemma
27b it
have gotten so good, that it's become increasingly rare that
I'll feel tempted to use Claude these days.
Examples of Surprising Lexical Syntax
So while writing this highlighter, let's talk about the kinds of lexical
syntax that surprised me.
C
The C programming language, despite claiming to be simple, actually has
some of the weirdest lexical elements of any language. For starters, we
have trigraphs, which were probably invented to help Europeans use C
when using keyboards that didn't
include
#
,
[
,
\
,
^
,
{
,
|
,
}
,
and
~
. You can replace those characters
with
??=
,
??(
,
??/
,
??)
,
??'
,
??<
,
??!
,
??>
,
and
??-
. Intuitive, right? That means, for example, the
following is perfectly valid C code.
int
main
(
int
argc,
char
* argv
??(??)
)
??<
printf(
"hello world\n"
);
??>
That is, at least until trigraphs were removed in the C23 standard.
However compilers will be supporting this syntax forever for legacy
software, so a good syntax highlighter ought to too. But just because
trigraphs are officially dead, doesn't mean the standards committees
haven't thought up other weird syntax to replace it. Consider universal
characters:
int
\uFEB2
= 1;
This feature is useful for anyone who wants, for example, variable names
with arabic characters while still keeping the source code pure ASCII.
I'm not sure why anyone would use it. I was hoping I could abuse this to
say:
int
main
(
int
argc,
char
* argv
\u005b\u005d
)
\u007b
printf(
"hello world\n"
);
\u007d
But alas, GCC raises an error if universal characters aren't used on the
specific UNICODE planes that've been blessed by the standards committee.
This next one is one of my favorites. Did you know that a single line
comment in C can span multiple lines if you use backslash at the end of
the line?
//hi\
there
Most other languages don't support this. Even languages that allow
backslash escapes in their source code (e.g. Perl, Ruby, and Shell)
don't have this particular feature from C. The ones that do support this
too, as far as I can tell, are Tcl and GNU Make. Tools for syntax
highlighting oftentimes get this wrong, like Emacs and Pygments.
Although Vim seems to always be right about backslash.
Here's another good one that Emacs gets wrong: the null preprocessor
directive. One of the first things you notice when reading the v6 source
code, is that most of the .c files start like this:
#
/*
 * foo library -- bar
 */
Allegedly this was to work around quirks, but it's still valid code to
this day. It can even serve a meaningful purpose, such as hiding
comments from
cc -C -E
:
#
/*
   * this comment will always be removed by the preprocessor
   * even if you pass -C which asks comments be preserved
   */
Haskell
Every C programmers knows you can't embed a multi-line comment in a
multi-line comment. For example:
/*
 hello
 /* again */
nope nope nope
*/
However with Haskell, you can. They finally fixed the bug. Although they
did adopt a different syntax.
-- Test nested comments within code blocks
let
result3 =
{- This comment contains
                   {- a nested comment -}
               -}
10 - 5
D
You'd think the D language would have been the first to fix C's
recursive comment bug. What D did instead, was adopt both forms of C
comment syntax as-is:
// hello
/*
 hello
 /* again */
nope nope nope
*/
While introducing a third syntax, for comment recursion.
/+
 + D stands for dead
 + for /+ what is dead may never die +/
 + but rises again, harder and stronger
 +/
Of all the languages, I thought D did the best job
documenting its lexical
syntax
. It's formal and it laid out all the gory details I needed to
know, like its hex strings and heredoc strings.
"str\"str"
plain
`str"\str`
plain
r
"str\str"
plain
q
"/str/
warn/"
plain
q
"<str>
warn>"
plain
q
"(str"(str)"str)"
plain
q
"[str"[str]"str]"
plain
q
"eos
hello
eos"
plain
q
"eos
!warn
warn
eos"
plain
q
"eos
warn
eos
warn
eos"
plain
x
"dead beef"
plain
x
"dead
w
a
rn
"
plain
Tcl
The thing that surprised me most about Tcl, is that identifiers can have
quotes in them. For example, this program will print
a"b
:
puts
a"b
You can even have quote in your variable names, however you'll only be
able to reference it if you use the
${a"b}
notation, rather
than
$a"b
.
set
a"b
doge
puts
${
a"b
}
JavaScript
JavaScript has a builtin lexical syntax for regular expressions. However
it's easy to lex it wrong if you aren't paying attention. Consider the
following:
var
foo =
/[/]/
g;
When I first wrote my lexer, I would simply scan for the closing slash,
and assume that any slashes inside the regex would be escaped. That
turned out to be wrong when I highlighted some minified code. If a slash
is inside the square quotes for a character set, then that slash doesn't
need to be escaped!
Now onto the even weirder.
There's some invisible UNICODE characters called the LINE SEPARATOR
(u2028) and PARAGRAPH SEPARATOR (u2029). I don't know what the use case
is for these codepoints, but the ECMAScript
standard
defines
them as line terminators
, which effectively makes them the same
thing as
\n
. Since these
are
Trojan Source
characters,
I configure my Emacs to render them as ↵ and ¶. However most software
hasn't been written to be aware of these characters, and will oftentimes
render them as question marks. Also as far as I know, no other language
except D does this. I was able to use that to my advantage for
SectorLISP, since it let me create C + JavaScript polyglots.
javascript syntax highlighting
//¶
`
... C only code goes here ...
//`
That's how I'd insert C code into JavaScript files.
c syntax highlighting
//¶`
#if
0
//`
... JavaScript only code goes here ...
//¶`
#endif
//`
And that's how I'd insert JavaScript into my C source code. An example
of a piece of production code where I did this
is
lisp.js
which is what powers
my
SectorLISP blog post
. It both runs in
the browser, and you can compile it with GCC and run it locally too.
llamafile is able to correctly syntax highlight this stuff, but I've yet
to find another syntax highlighter that does too. Not that it matters,
since I doubt an LLM would ever print this. But it sure is fun to think
about these corner cases.
Shell
We're all familiar with the heredoc syntax of shell scripts, e.g.
cat <<EOF
this is kind of
a multi-line
string
EOF
The above syntax allows you to put
$foo
in your heredoc
string, although there's a quoted syntax which disables variable
substitution.
cat <<
'END'
this won't print the contents of $var
END
If you ever want to confuse your coworkers, then one great way to abuse
this syntax is by replacing the heredoc marker with an empty string, in
which case the heredoc will end on the next empty line. For example,
this program will print "hello" and "world" on two lines:
cat <<
''
hello
echo
world
It's also possible in languages that support heredocs (Shell, Ruby, and
Perl) to have multiple heredocs on the same line.
cat /dev/fd/3 3<< E1 /dev/fd/4 4<< E2
foo
E1
bar
E2
Another thing to look out for with shell, is it's like Tcl in the sense
that special characters like #, which you might think would always begin
a comment, can actually be valid code depending on the context. For
example, inside a variable reference, # can be used to strip a prefix.
The following program will print "there".
x
=hi-there
echo
${
x
#hi-}
String Interpolation
Did you know that, from a syntax highlighting standpoint, a Kotlin
string can begin with " but end with the { character? That's the way
it's string interpolation syntax works. Many languages let you embed
variable name references in strings, but TypeScript, Swift, Kotlin, and
Scala take string interpolation to the furthest extreme of encouraging
actual code being embedded inside strings.
val
s2 =
"${
s1.replace(
"is"
,
"was"
)
}, but now is $
a
"
So to highlight a string with Kotlin, Scala, and TypeScript, one must
count curly brackets and maintain a stack of parser states. With
TypeScript, this is relatively trivial, and only requires a couple
states to be added to your finite state machine. However with Kotlin and
Scala it gets real hairy, since they support both double quote and
triple quote syntax, and either one of them can have interpolated
values. So that ended up being about 13 independent states the FSM needs
for string lexing alone. Swift also supports triple quotes for its
"\(var)"
interpolated syntax, however that only needed 10
states to support.
Swift
Swift has its own unique approach to the problem of embedding strings
inside a string. It allows "double quote", """triple quote""", and
/regex/ strings to all be surrounded with an arbitrary number of #hash#
marks, which must be mirrored on each side. This makes it possible to
write code like the following:
let
threeMoreDoubleQuotationMarks =
#"""
Here are three more double quotes: """
"""#
let
threeMoreDoubleQuotationMarks =
##"""
Here are three more double quotes: #"""#
"""##
C#
C# supports Python's triple quote multi-line string syntax, but with an
interesting twist that's unique to this language. The way C# solves the
"embed a string inside a string" problem, is they let you do quadruple
quoted strings, or even quintuple quoted strings if you want. However
many quotes you put on the lefthand side, that's what'll be used to
terminate the string at the other end.
Console.WriteLine(
""
);
Console.WriteLine(
"\""
);
Console.WriteLine(
""""""
);
Console.WriteLine(
""""""
);
Console.WriteLine(
""" yo "" hi """
);
Console.WriteLine(
"""" yo """ hi """"
);
Console.WriteLine(
""""First
                  """100 Prime"""
                  Numbers:
                  """"
);
This is the way if you ask me, because it's actually simpler for a
finite state machine to decode. With classic Python triple quoted
strings, you need extra rules, to ensure it's either one double-quote
character, or exactly three. By letting it be an arbitrary number,
there's fewer rules to validate. So you end up with a more powerful
expressive language that's simpler to implement. This is the kind of
genius we've come to expect from Microsoft.
What will they think of next?
FORTH
Normally when code is simpler for a computer to decode, it's more
difficult for a human to understand, and FORTH is proof of that. FORTH
is probably the simplest language there is, because it tokenizes
everything on whitespace boundaries. Even the syntax for starting a
string is a token. For example:
c" hello world"
Would mean the same thing as saying
"hello world"
in every
other language.
FORTRAN and COBOL
One of the use cases I envision for llamafile is that it can help the
banking system not collapse once all the FORTRAN and COBOL programmers
retire. Let's say you've just been hired to maintain a secretive
mainframe full of confidential information written in the COmmon
Business-Oriented Language. Thanks to llamafile, you can ask an
air-gapped AI you control,
like
Gemma
27b
, to write your COBOL and FORTRAN code for you. It can't print
punch cards, but it can highlight punch card syntax. Here's what FORTRAN
code looks like, properly syntax highlighted:
*
*     Quick return if possible.
*
IF
((M
.EQ.
0)
.OR.
(N
.EQ.
0)
.OR.
+
(((ALPHA
.EQ.
ZERO)
.OR.
(K
.EQ.
0))
.AND.
(BETA
.EQ.
ONE)))
RETURN
*
*     And if alpha.eq.zero.
*
IF
(ALPHA
.EQ.
ZERO)
THEN
IF
(BETA
.EQ.
ZERO)
THEN
DO
20
J = 1,N
DO
10
I = 1,M
                      C(I,J) = ZERO
10
CONTINUE
20
CONTINUE
ELSE
DO
40
J = 1,N
DO
30
I = 1,M
                      C(I,J) = BETA*C(I,J)
30
CONTINUE
40
CONTINUE
END IF
RETURN
END IF
FORTRAN has the following fixed column rules.
Putting *, c, or C in column 1 will make the line a comment
Putting non-space in column 6 lets you extend a line past 80 characters
Labels are created by putting digits in columns 1-5
Now here's some properly syntax highlighted COBOL code.
000100
*Hello World in COBOL
000200
IDENTIFICATION DIVISION
.
000300
PROGRAM-ID
. HELLO-WORLD.
000400
000500
PROCEDURE DIVISION
.
000600
DISPLAY
'Hello, world!'
.
000700
STOP RUN
.
With COBOL, the rules are:
Putting * in column 7 makes the line a comment
Putting - in column 7 lets you extend a line past 80 characters
Line numbers go in columns 1-6.
Zig
Zig has its own unique solution for multi-line strings, which are
prefixed with two backslashes.
const
copyright =
\\ Copyright (c) 2024, Zig Incorporated
    \\ All rights reserved.
;
What I like about this syntax, is it eliminates that need we've always
had for calling
textwrap.dedent()
with Python's triple
quoted strings. The tradeoff is that the semicolon is ugly. This is a
string syntax that really ought to be considered by one of the languages
that don't need semicolons, e.g. Go, Scala, Python, etc.
Lua
Lua has a very unique multi-line string syntax, and it uses an approach
similar to C# and Swift when it comes to solving the "embed a string
inside a string" problem. It works by using double square brackets, and
it lets you put an arbitrary number of equal signs inbetween them.
-- this is a comment
[[hi [=[]=] ]]
there
[[hi [=[]=] ]]
there
[==[hi [=[]=] ]==]
hello
[==[hi  ]=]==]
hello
[==[hi  ]===]==]
hello
[====[hi  ]===]====]
hello
What's really interesting is that it lets you do this with comments too.
--[[
comment #1
]]
print
(
"hello"
)
--[==[
comment [[#2]]
]==]
print
(
"world"
)
Assembly
One of the most challenging languages to syntax highlight is assembly,
due to the fragmentation of all its various dialects. I've sought to
build something with llamafile that does a reasonably good job with
AT&T, nasm, etc. syntax. Here's nasm syntax:
section
.data
message
db
'Hello, world!'
, 0xa
; The message string, ending with a newline
section
.text
global
_start
_start
:
; Write the message to stdout
mov
rax, 1
; System call number for write
mov
rdi, 1
; File descriptor for stdout
mov
rsi, message
; Address of the message string
mov
rdx, 13
; Length of the message
syscall
; Exit the program
mov
rax, 60
; System call number for exit
xor
rdi, rdi
; Exit code 0
syscall
And here's AT&T syntax:
/ syscall
.globl
_syscall,csv,cret,cerror
_syscall
:
jsr
r5,csv
mov
r5,r2
add
$04
,r2
mov
$9f
,r3
mov
(r2)+,r0
bic
$!0377
,r0
bis
$sys
,r0
mov
r0,(r3)+
mov
(r2)+,r0
mov
(r2)+,r1
mov
(r2)+,(r3)+
mov
(r2)+,(r3)+
mov
(r2)+,(r3)+
mov
(r2)+,(r3)+
mov
(r2)+,(r3)+
sys
0; 9f
bec
1
f
jmp
cerror
1
:
jmp
cret
.data
9
:	.=.+12.
And here's GNU syntax:
/ setjmp() for x86-64
// this is a comment too
; so is this
# this too!
! hello sparc
setjmp
:
lea
8(
%rsp
),
%rax
mov
%rax
,(
%rdi
)
mov
%rbx
,8(
%rdi
)
mov
%rbp
,16(
%rdi
)
mov
%r12
,24(
%rdi
)
mov
%r13
,32(
%rdi
)
mov
%r14
,40(
%rdi
)
mov
%r15
,48(
%rdi
)
mov
(
%rsp
),
%rax
mov
%rax
,56(
%rdi
)
xor
%eax
,
%eax
ret
With keywords I've found the simplest thing is to just treat the
first identifier on the line (that isn't followed by a colon) as a
keyword. That tends to make most of the assembly I've tried look pretty
reasonable.
The comment syntax is real hairy. I really like the original UNIX
comments which only needed a single slash. GNU as still supports those
to this date, but only if they're at the beginning of the line (UNIX
could originally put them anywhere, since
as
didn't have
the ability to do arithmetic back then). Clang doesn't support fixed
comments at all, so they're sadly not practical anymore to use in open
source code.
But this story gets even better. Another weird thing about the original
UNIX assembler is that it didn't use a closing quote on character
literals. So where we'd say
'x'
to get 0x78 for x, in the
original UNIX source code, you'd say
'x
. This is another
thing GNU as continues to support, but sadly not LLVM. In any case,
since a lot of code exists that uses this syntax, any good syntax
highlighter needs to support it.
The GNU assembler allows identifiers to be quoted, so you can put pretty
much any character in a symbol.
Finally, it's not enough to just highlight assembly when highlighting
assembly. The assembler is usually used in conjunction with either the C
preprocessor, or m4. Trust me, lots of open source code does this.
Therefore lines starting with
dnl
,
m4_dnl
,
or
C
should be taken as comments too.
Ada
Ada is a remarkably simple language to lex, but there's one thing I
haven't quite wrapped my head around yet, which is its use of the single
quotation mark. Ada can have character literals like C,
e.g.
'x'
. But single quote can also be used to reference
attributes, e.g.
Foo'Size
. Single quote even lets you embed
expressions and call functions. For example, the program:
with
Ada.Text_IO;
procedure
main
is
S : String := Character'(
')'
)'Image;
begin
Ada.Text_IO.Put_Line(
"The value of S is: "
& S);
end
main;
Will print out:
The value of S is: ')'
Because we're declaring a character, giving it a value, and then sending
it through the
Image
function, which converts it to
a
String
representation.
BASIC
Let's talk about the Beginner's All-purpose Symbolic Instruction Code.
While digging through the repos I've git cloned, I came across this old
Commodore BASIC program that broke many of my assumptions about syntax
highlighting.
10
rem cbm basic v2 example
20
rem comment with keywords: for, data
30
dim
a$(20)
35
rem the typical space efficient form of leaving spaces out:
40
fort=0to15:poke646,t:
print
"{revers on}     "
;:
next
50
geta$:ifa$=
chr
$(0):
goto
40
55
rem it is legal to omit the closing " on line end
60
print
"{white}"
:
print
"bye...
70
end
We'll notice that this particular BASIC implementation didn't require a
closing quote on strings, variable names have these weird sigils, and
keywords like
goto
are lexed eagerly out of identifiers.
Visual BASIC also has this weird date literal syntax:
Dim
v
As
Variant
' Declare a Variant
v =
#1/1/2024#
' Hold a date
That's tricky to lex, because VB even has preprocessor directives.
#If DEBUG Then
<WebMethod()>
Public Function
SomeFunction
()
As
String
#Else
<WebMethod(CacheDuration:=86400)>
Public
Function
SomeFunction
()
As
String
#End If
Perl
One of the trickier languages to highlight is Perl. It exists in the
spiritual gulf between shells and programming languages, and inherits
the complexity of both. Perl isn't as popular today as it once was, but
its influence continues to be prolific. Perl made regular expressions a
first class citizen of the language, and the way regex works in Perl has
since been adopted by many other programming languages, such as Python.
However the regex lexical syntax itself continues to be somewhat unique.
For example, in Perl, you can replace text similar to sed as follows:
my
$
string
=
"HELLO, World!"
;
$
string
=~ s
/hello/Perl/
i;
print $
string
;
# Output: Perl, World!
Like sed, Perl also allows you to replace the slashes with an arbitrary
punctuation character, since that makes it easier for you to put slashes
inside your regex.
$
string
=~ s
!hello!Perl!
i;
What you might not have known, is that it's possible to do this with
mirrored characters as well, in which case you need to insert an
additional character:
$
string
=~ s
{hello}{Perl}
i;
However
s///
isn't the only weird thing that needs to be
highlighted like a string. Perl has a wide variety of other magic
prefixes.
/case sensitive match/
/case insensitive match/
i
y
/abc/xyz/
e
s
!hi!there!
m
!hi!
i
m
;hi;
i
qr
!hi!
u
qw
!hi!
h
qq
!hi!
h
qx
!hi!
h
m
-hi-
s
-hi-there-
g
s
"hi"there"
g
s
@hi@there@
yo
s
{hi}{there}
g
One thing that makes this tricky to highlight, is you need to take
context into consideration, so you don't accidentally think
that
y/x/y/
is a division formula. Thankfully, Perl makes
this relatively easy, because variables can always be counted upon to
have sigils, which are usually
$
for
scalars,
@
for arrays, and
%
for hashes.
my
$
greeting
=
"Hello, world!"
;
# Array: A list of names
my
@
names
= (
"Alice"
,
"Bob"
,
"Charlie"
);
# Hash: A dictionary of ages
my
%
ages
= (
"Alice"
=> 30,
"Bob"
=> 25,
"Charlie"
=> 35);
# Print the greeting
print
"$greeting\n"
;
# Print each name from the array
foreach my
$
name
(@
names
) {
    print
"$name\n"
;
}
This helps us avoid the need for parsing the language grammar.
Perl also has this goofy convention for writing man pages in your source
code. Basically, any =word at the start of the line will get it going,
and
=cut
will finish it.
#!/usr/bin/perl
=pod

=head1 NAME

my_silly_script - A Perl script demonstrating =cut syntax

=head1 SYNOPSIS

 my_silly_script [OPTIONS]

=head1 DESCRIPTION

This script does absolutely nothing useful, but it showcases
the quirky =cut syntax for POD documentation in Perl.

=head1 OPTIONS

There are no options.

=head1 AUTHOR

Your Name <your.email@example.com>

=head1 COPYRIGHT

Copyright (c) 2023 Your Name. All rights reserved.

=cut
print
"Hello, world!\n"
;
Ruby
Of all the languages, I've saved the best for last, which is Ruby. Now
here's a language whose syntax evades all attempts at understanding.
Ruby is the union of all earlier languages, and it's not even formally
documented. Their manual has a section
on
Ruby syntax
, but it's very light on details. Whenever I try to test
my syntax highlighting, by concatenating all the .rb files on my hard
drive, there's always another file that finds some way to break it.
def
`(command)
return
"just testing a backquote override"
end
Since ruby supports backquote syntax like
var
=
`echo hello`
, I'm not exactly sure how
to tell that the backquote above isn't meant to be highlighted as a
string. Another example is this:
when
/\.*\.h/
options[
:includes
] <<arg;
true
when
/--(\w+)=\"?(.*)\"?/
options[
$1
.to_sym] =
$2
;
true
Ruby has a
<<
operator, and it also supports heredocs
(just like Perl and Shell). So I'm not exactly sure how to tell that the
code above isn't a heredoc. Yes that code actually exists in the wild.
Even Emacs gets this wrong. Out of all 42 languages I've evaluated,
that's probably the biggest shocker so far. It might be the case that
Ruby isn't possible to lex without parsing. Even with parsing, I'm still
not sure how it's possible to make sense of that.
But wait, it gets even better. This is actually valid Ruby code:
puts
"This is #{<<HERE.strip} evil"
incredibly
HERE
Yup.
Complexity of Supported Languages
If I were to rank the complexity of programming languages by how many
lines of code each one takes to syntax highlight, then FORTH would be
the simplest language, and Ruby would be the most complicated.
125
highlight_forth.cpp
266
highlight_lua.cpp
132
highlight_m4.cpp
282
highlight_csharp.cpp
149
highlight_ada.cpp
282
highlight_rust.cpp
160
highlight_lisp.cpp
297
highlight_python.cpp
163
highlight_test.cpp
300
highlight_java.cpp
166
highlight_matlab.cpp
321
highlight_haskell.cpp
186
highlight_cobol.cpp
335
highlight_markdown.cpp
199
highlight_basic.cpp
337
highlight_js.cpp
200
highlight_fortran.cpp
340
highlight_html.cpp
211
highlight_sql.cpp
371
highlight_typescript.cpp
216
highlight_tcl.cpp
387
highlight_kotlin.cpp
218
highlight_tex.cpp
387
highlight_scala.cpp
219
highlight.cpp
447
highlight_asm.cpp
220
highlight_go.cpp
449
highlight_c.cpp
225
highlight_css.cpp
455
highlight_swift.cpp
225
highlight_pascal.cpp
521
highlight_d.cpp
230
highlight_zig.cpp
570
highlight_shell.cpp
235
highlight_make.cpp
583
highlight_perl.cpp
239
highlight_ld.cpp
1042
highlight_ruby.cpp
263
highlight_r.cpp
llamafile
is a
Mozilla
project who
sponsors me to work on it. My work on open source is also made possible
by my
GitHub sponsors
and
Patreon subscribers
.
Thank you for giving me the opportunity to serve you all these last four
years. Since you've read this far, I'd like to invite you to join both
the
Mozilla AI Discord
and
the
Redbean Discord
servers
where you can chat with me and other people who love these projects.
