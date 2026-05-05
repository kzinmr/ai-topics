---
title: "Sloc Cloc and Code Revisited - A focus on accuracy"
url: "https://boyter.org/posts/sloc-cloc-code-revisited/"
fetched_at: 2026-05-05T07:01:59.284656+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Sloc Cloc and Code Revisited - A focus on accuracy

Source: https://boyter.org/posts/sloc-cloc-code-revisited/

Update 2019-03-13
This is now part of a series of blog posts about
scc
Sloc Cloc and Code which has now been optimised to be the fastest code counter for almost every workload. Read more about it at the following links.
Two things prompted me to start looking at my code counter
scc
again. The first being the release of Go 1.11. New releases of compilers, libraries and tool-chains have a wonderful habit of making things go faster without you having to do anything other than recompile. In addition they often provide new methods which assist with this and are worth exploring.
The other was that the author of
tokei
released a new update v8.0.0 and included a comparison to
scc
on the project page
https://github.com/Aaronepower/tokei/blob/master/COMPARISON.md
I had been tracking the improvements in
tokei
,
loc
and
polyglot
over the last few weeks. However what really surprised me was the accuracy issues pointed out, particularly the fact that
scc
version 1.7.0 was misreporting the number of lines.
Denial: Step one of software debugging
I tried testing it out on the example provided by
tokei
in the comparison page
https://github.com/Aaronepower/tokei/blob/master/COMPARISON.md
-------------------------------------------------------------------------------
Language                 Files     Lines     Code  Comments   Blanks Complexity
-------------------------------------------------------------------------------
Rust                         1        33       28         1        4          5
-------------------------------------------------------------------------------
Total                        1        33       28         1        4          5
-------------------------------------------------------------------------------
Wow. It really does misreport the number of lines. There should be 39 there.
This disturbed me quite a lot. In fact I had even written tests in
scc
to ensure I got the number of lines correct. For example this one,
content
:=
""
for
i
:=
0
;
i
<
5000
;
i
++
{
content
+=
"a\n"
fileJob
.
Lines
=
0
fileJob
.
Content
= []byte(
content
)
CountStats
(
&
fileJob
)
if
fileJob
.
Lines
!=
int64(
i
+
1
) {
t
.
Errorf
(
"Expected %d got %d"
,
i
+
1
,
fileJob
.
Lines
)
}
}
That should never happen.
Bargaining/Self-Blame: Stage two of software debugging
Time to go code spelunking. Since I wrote
scc
and its a fairly small code-base I had a feeling it was an issue to do with the skip ahead logic. When
scc
finds a matching condition it keeps the offset around so it can jump ahead. The idea being we skip bytes we have looked at where possible if we know they matched a condition which changed the state. However if there was an error in this logic its possible it would jump over any newlines \n which are used to determine to total count.
The offending code in mind was this one.
// If we checked ahead on bytes we are able to jump ahead and save some time reprocessing
// the same values again
index
+=
offsetJump
Just commenting out this and I got
scc
to report the correct number of lines. Ouch. Turns out I made a boo-boo. That was rather stupid of me.
I Still issues with the rest of the stats but was happy with progress. I then turned my attention to the
tokei
test suite and the simpler examples it had to verify correct output. The author of
tokei
suggested just using the test suite from
tokei
https://www.reddit.com/r/rust/comments/99e4tq/reading_files_quickly_in_rust/
so it seemed like a good idea. Also how could I be so stupid as to introduce this bug from day one and not notice it?
Anger: Stage three of software debugging
I turned my attention to this example from the tokei code-base written in Java.
/*23 lines 16 code 4 comments 3 blanks*/
/*
- Simple test class
*/
public
class
Test
{
int
j
=
0;
// Not counted
public
static
void
main
(String
[]
args)
{
Foo f
=
new
Foo();
f.
bar
();
}
}
class
Foo
{
public
void
bar
()
{
System.
out
.
println
(
"FooBar"
);
//Not counted
}
}
Getting the stats from our now correct
scc
(for lines counts anyway).
-------------------------------------------------------------------------------
Language                 Files     Lines     Code  Comments   Blanks Complexity
-------------------------------------------------------------------------------
Java                         1        23       18         2        3          0
-------------------------------------------------------------------------------
Total                        1        23       18         2        3          0
-------------------------------------------------------------------------------
Well thats not brilliant. The only thing
scc
got right was the number of files and the number of lines. Maybe if I tweak it a little bit I can resolve this issue and everything else will go away? In any case how in the heck could I never have noticed this. I knew that the edge cases are a bitch to deal with, but still…
Depression: Stage four of software debugging
Looking into it the issues still appeared to be related to the end of line comments. When I first implemented
scc
I set a special state at the end of closing multi-line comments. This would allow it to fall back into the code state when it hit a newline. However the result of this is that I introduced a bug. When there was a multi-line comment the last line of the multi-line would be counted as code. I never caught it because when I checked all my projects I don’t use multi-line comments most of the time.
In reality what should I should have done (which seems obvious in hindsight) is never process whitespace characters, unless they are a
\n
newline which resets the state and counts whatever state the application is is. When I realized this I was rather depressed that it took me so long to work this out.
Acceptance: Stage five of software debugging
A quick change to resolve the above, never process whitespace characters and all of a sudden everything was working as it should.
-------------------------------------------------------------------------------
Language                 Files     Lines     Code  Comments   Blanks Complexity
-------------------------------------------------------------------------------
Java                         1        23       16         4        3          0
-------------------------------------------------------------------------------
Total                        1        23       16         4        3          0
-------------------------------------------------------------------------------
In fact running over the
tokei
samples everything worked (with on exception covered later). So I had a look again at the torture test posted.
$ scc
-------------------------------------------------------------------------------
Language                 Files     Lines     Code  Comments   Blanks Complexity
-------------------------------------------------------------------------------
Rust                         1        38       29         5        4          5
-------------------------------------------------------------------------------
Total                        1        38       29         5        4          5
-------------------------------------------------------------------------------
A much better result. However it still is not accurate, nor matching
tokei
which produces, (BTW I am not a fan of the new full width result
tokei
now produces and made it hard to get the below close to the above in terms of matching width).
$ tokei
--------------------------------------------------------------------------------
Language             Files        Lines         Code     Comments       Blanks
--------------------------------------------------------------------------------
Rust                     1           38           32            2            4
--------------------------------------------------------------------------------
Total                    1           38           32            2            4
--------------------------------------------------------------------------------
What’s the difference? One thing when looking at the source that caught my eye was the following,
let
this_does_not
=
/*a /* nested */ comment "*/
Nested comments? In fact I remember looking into this when I first wrote
scc
. I was wondering about nested multi-line comments which turned out to be a compile error in Java, hence while I toyed with getting it working figured that was not a brilliant idea and explicitly made it work without them.
So the reason for the difference is that
tokei
has some sort of stack for dealing with nested comments so it know when to finish with them. I didn’t even know was a thing.
Playing around with Rust and it turns out that it DOES support nested comments. My first thought was that this implementation is a bad idea. For example if you write the following
/*/**/
that is going to break
tokei
as everything will be a comment. Trying it out happens to be a compiler error… so it is not a case worth worrying about. If however you did happen to half implement a nested comment you get the following (I added it to the first line),
-------------------------------------------------------------------------------
Language            Files        Lines         Code     Comments       Blanks
-------------------------------------------------------------------------------
Rust                    1           38            0           34            4
-------------------------------------------------------------------------------
Total                   1           38            0           34            4
-------------------------------------------------------------------------------
Clearly the above is wrong, but then again so is the code as it will not compile. I have no idea if other languages will allow the above state. Also if you are reading this and know why you would even want nested comments please let me know. I cannot think of a good reason to implement them other than its a neat trick to put into your language.
Side note, this is why it is a good idea to at least toy around with other languages. If gives you greater perspective. Before I started my Rust journey I would have insisted that no mainstream language supports nested multi-line comments. Always be learning.
Acceptance: Stage five of software debugging
Well knowing what is wrong is the second step to fixing it, with the first being knowing something is wrong. Clearly I underestimated how devious language designers can be.
To fix this isn’t a huge issue. Just need to keep a stack of the multi-line comment opens, and check when in comments for another one. Sadly during this process I noticed that
scc
was missing quite a few edge cases. Thankfully the
tokei
stress test is pretty brutal and allowed me to identify them all and resolve them.
After much tweaking and fiddling with the logic.
$ tokei
--------------------------------------------------------------------------------
Language             Files        Lines         Code     Comments       Blanks
--------------------------------------------------------------------------------
Rust                     1           38           32            2            4
--------------------------------------------------------------------------------
Total                    1           38           32            2            4
--------------------------------------------------------------------------------

$ scc
-------------------------------------------------------------------------------
Language                 Files     Lines     Code  Comments   Blanks Complexity
-------------------------------------------------------------------------------
Rust                         1        38       32         2        4          5
-------------------------------------------------------------------------------
Total                        1        38       32         2        4          5
-------------------------------------------------------------------------------
Excellent.
However what price has
tokei
paid for this logic. For example is it intelligent enough to know that Java does not support nested multi-line comments? Turns out it is. Also turns out that nested multi-line comments are more common across languages than I expected, Lisp, Rust, Lean, Jai, Idris, Scheme, Swift, Julia and Kotlin all support them. As such I added in the same checks to ensure that
scc
is as accurate as
tokei
, unless of course there are differences in the languages.json file that both use.
I tried then running across the full suite of tokei tests,
$ scc -c -co -s name tests
-------------------------------------------------------------------------------
Language                     Files       Lines      Code    Comments     Blanks
-------------------------------------------------------------------------------
C++                              1          15         7           4          4
C++ Header                       1          21        11           5          5
CMake                            1          25        16           3          6
Cogent                           1           7         2           2          3
Crystal                          1          20        14           2          4
D                                1           8         2           5          1
Dockerfile                       1          16         6           3          7
Emacs Dev Env                    1          16         6           7          3
Emacs Lisp                       1          21        11           6          4
F#                               1          13         4           5          4
F*                               1          10         3           4          3
HTML                             1          27        15           8          4
Java                             1          23        16           4          3
MSBuild                          1          12        10           1          1
Makefile                         1          24        11           5          8
Meson                            1          12         6           2          4
Module-Definition                1          17         9           6          2
Org                              1          13         7           2          4
QML                              1          20        11           5          4
Rakefile                         1          10         4           2          4
Ruby                             1          20         9           8          3
Rust                             1          39        32           2          5
SRecode Template                 1          37        23           2         12
Scheme                           1          26        14           4          8
Scons                            1          10         3           3          4
Ur/Web                           2          17         9           5          3
Ur/Web Project                   1           3         1           1          1
VHDL                             1          30        20           4          6
Visual Basic                     1           7         4           2          1
Xtend                            1          23        13           4          6
-------------------------------------------------------------------------------
Total                           31         542       299         116        127
-------------------------------------------------------------------------------
$ tokei tests
--------------------------------------------------------------------------------
Language             Files        Lines         Code     Comments       Blanks
--------------------------------------------------------------------------------
 CMake                    1           25           16            3            6
 Cogent                   1            7            2            2            3
 C++                      1           15            7            4            4
 C++ Header               1           21           11            5            5
 Crystal                  1           20           14            2            4
 D                        1            8            5            1            2
 Dockerfile               1           16            6            3            7
 Emacs Lisp               1           21           11            6            4
 Emacs Dev Env            1           16            6            7            3
 F#                       1           13            5            4            4
 F*                       1           10            3            4            3
 HTML                     1           27           15            8            4
 Java                     1           23           16            4            3
 Makefile                 1           24           11            5            8
 Meson                    1           12            6            2            4
 Module-Definition        1           17            9            6            2
 MSBuild                  1           12           10            1            1
 Org                      1           13            7            2            4
 QML                      1           20           11            5            4
 Rakefile                 1           10            4            2            4
 Ruby                     1           20            9            8            3
 Rust                     1           39           32            2            5
 SRecode Template         1           37           23            2           12
 Scheme                   1           26           14            4            8
 Scons                    1           10            3            3            4
 Ur/Web                   2           17            9            5            3
 Ur/Web Project           1            3            1            1            1
 VHDL                     1           30           20            4            6
 Visual Basic             1            7            4            2            1
 Xtend                    1           23           13            4            6
--------------------------------------------------------------------------------
Total                   31          542          303          111          128
--------------------------------------------------------------------------------
The differences in the stats are down to how the language D works. I have a bug tracked for this
https://github.com/boyter/scc/issues/27
to be resolved at some point in the future. Annoying but not worrying enough at this point to spend too much time on it.
With what appears to be most of the bugs ironed out time to look at performance again. With the changes that were made there are bound to be some wins, and with the new tools in Go I can hopefully spot some other issues. However that is a subject for another blog post.
For the moment if you want the newer more accurate
scc
you can build from source or get the binaries for Windows/Linux/macOS
https://github.com/boyter/scc/
