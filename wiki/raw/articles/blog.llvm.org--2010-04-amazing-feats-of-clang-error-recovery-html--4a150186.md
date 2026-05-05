---
title: "Amazing feats of Clang Error Recovery"
url: "https://blog.llvm.org/2010/04/amazing-feats-of-clang-error-recovery.html"
fetched_at: 2026-05-05T07:01:44.232991+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Amazing feats of Clang Error Recovery

Source: https://blog.llvm.org/2010/04/amazing-feats-of-clang-error-recovery.html

Amazing feats of Clang Error Recovery
By Chris Lattner
Apr 5, 2010
#C++
,
#Clang
13 minute read
In addition to parsing and generating machine code for your source files when valid, a compiler frontend's job is also to detect invalid code and give you a hint that explains what is wrong so you can fix the problem. The bug could either be straight-up invalid (an error) or could just be something that is legal but looks really dubious (a warning). These errors and warnings are known as compiler 'diagnostics', and Clang aims to go above and beyond the call of duty to provide a really amazing experience.
After the break, we show some examples of areas where Clang tries particularly hard. For other examples, the Clang web page also has
a page on diagnostics
and Doug showed how Clang diagnoses two-phase name lookup issues in
a prior blog post
.
Update
: Other people are starting to compare their favorite compiler. Here's the
OpenVMS Compiler
. Email Chris if you have a comparison you want posted.
Секреты восстановления (Russian Translation)
provided by
Softdroid Recovery
.
Ukrainian Translation
provided by Sandi Wolfe.
Estonian Translation
provided by Johanne Teerink.
German Translation
provided by
Philip Egger.
Spanish Translation
provided by
Laura Mancini
These examples use Apple GCC 4.2 as a comparison on these examples, but this isn't meant to bash (an old version of) GCC. Many compilers have these sorts of issues and we strongly encourage you to try the examples on your favorite compiler to see how it does. The examples all shown are necessarily small (reduced) examples that demonstrate a problem, when you see these in real life, they are often much more convincing :).
One annoying thing about parsing C and C++ is that you have to know what is a typename in order to parse the code. For example "(x)(y)" can be either a cast of the expression "(y)" to type "x" or it could be a call of the "x" function with the "(y)" argument list, depending on whether x is a type or not. Unfortunately, a common mistake is to forget to include a header file, which means that the compiler really has no idea whether something is a type or not, and therefore has to make a strongly educated guess based on context. Here are a couple examples:
$
cat t.m
NSString *P = @"foo";
$
clang t.m
t.m:4:1: error: unknown type name 'NSString'
NSString *P = @"foo";
^
$
gcc t.m
t.m:4: error: expected '=', ',', ';', 'asm' or '__attribute__' before '*' token
and:
$
cat t.c
int foo(int x, pid_t y) {
return x+y;
}
$
clang t.c
t.c:1:16: error: unknown type name 'pid_t'
int foo(int x, pid_t y) {
^
$
gcc t.c
t.c:1: error: expected declaration specifiers or '...' before 'pid_t'
t.c: In function 'foo':
t.c:2: error: 'y' undeclared (first use in this function)
t.c:2: error: (Each undeclared identifier is reported only once
t.c:2: error: for each function it appears in.)
This sort of thing also happens in C if you forget to use 'struct stat' instead of 'stat'. As is a common theme in this post, recovering well by inferring what the programmer meant helps Clang avoid emitting bogus follow-on errors like the three lines GCC emits on line 2.
One of the
more visible
things that Clang includes is a spell checker (also
on reddit
). The spell checker kicks in when you use an identifier that Clang doesn't know: it checks against other close identifiers and suggests what you probably meant. Here are a few examples:
$
cat t.c
#include <inttypes.h>
int64 x;
$
clang t.c
t.c:2:1: error: unknown type name 'int64'; did you mean 'int64_t'?
int64 x;
^~~~~
int64_t
$
gcc t.c
t.c:2: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'x'
another example is:
$
cat t.c
#include <sys/stat.h>
int foo(int x, struct stat *P) {
return P->st_blocksize*2;
}
$
clang t.c
t.c:4:13: error: no member named 'st_blocksize' in 'struct stat'; did you mean 'st_blksize'?
return P->st_blocksize*2;
^~~~~~~~~~~~
st_blksize
$
gcc t.c
t.c: In function ‘foo’:
t.c:4: error: 'struct stat' has no member named 'st_blocksize'
The great thing about the spell checker is that it catches a wide variety of common errors, and it also assists in later recovery. Code that later used 'x', for example, knows that it is declared as an int64_t, so it doesn't lead to other weird follow on errors that don't make any sense. Clang uses the well known
Levenshtein distance function
to compute the best match out of the possible candidates.
Clang tracks the typedefs you write in your code carefully so that it can relate errors to the types you use in your code. This allows it to print out error messages in your terms, not in fully resolved and template instantiated compiler terms. It also uses its range information and caret to show you what you wrote instead of trying to print it back out at you. There are several examples of this on the Clang diagnostics page, but one more example can't hurt:
$
cat t.cc
namespace foo {
struct x { int y; };
}
namespace bar {
typedef int y;
}
void test() {
foo::x a;
bar::y b;
a + b;
}
$
clang t.cc
t.cc:10:5: error: invalid operands to binary expression ('foo::x' and 'bar::y' (aka 'int'))
a + b;
~ ^ ~
$
gcc t.cc
t.cc: In function 'void test()':
t.cc:10: error: no match for 'operator+' in 'a + b'
This shows that clang gives you the source names as you typed them ("foo::x" and "bar::y", respectively) but it also unwraps the y type with "aka" in case the underlying representation is important. Other compilers typically give completely unhelpful information which doesn't really tell you what the problem is. This is a surprisingly concise example from GCC, but it also seems to be missing some critical information (such as why there is no match). Also, if the expression was more than a single "a+b", you can imagine that pretty printing it back at you isn't the most helpful.
One mistake many beginner programmers mistake is that they accidentally define functions instead of objects on the stack. This is due to an ambiguity in the C++ grammar which is resolved in an arbitrary way. This is an unavoidable part of C++, but at least the compiler should help you understand what is going wrong. Here's a trivial example:
$
cat t.cc
#include <vector>
int foo() {
std::vector<std::vector<int> > X();
return X.size();
}
$
clang t.cc
t.cc:5:11: error: base of member reference has function type       'std::vector<std::vector<int> > ()'; perhaps you meant to call this function with '()'?
return X.size();
^
()
$
gcc t.cc
t.cc: In function ‘int foo()’:
t.cc:5: error: request for member ‘size’ in ‘X’, which is of non-class type ‘std::vector<std::vector<int, std::allocator<int> >, std::allocator<std::vector<int, std::allocator<int> > > > ()()’
I run into this thing when I originally declared the vector as taking some arguments (e.g. "10" to specify an initial size) but refactor the code and eliminate that. Of course if you don't remove the parentheses, the code is actually declaring a function, not a variable.
Here you can see that Clang points out fairly clearly that we've gone and declared a function (it even offers to help you call it in case you forgot ()'s). GCC, on the other hand, is both hopelessly confused about what you're doing, but also spews out a big typename that you didn't write (where did std::allocator come from?). It's sad but true that being an experienced C++ programmer really means that you're adept at decyphering the error messages that your compiler spews at you.
If you go on to try the more classical example where this bites people, you can see Clang try even harder:
$
cat t.cc
#include <fstream>
#include <vector>
#include <iterator>
int main() {
std::ifstream ifs("file.txt");
std::vector<char> v(std::istream_iterator<char>(ifs),
std::istream_iterator<char>());
std::vector<char>::const_iterator it = v.begin();
return 0;
}
$
clang t.cc
t.cc:8:23: warning: parentheses were disambiguated as a function declarator
std::vector<char> v(std::istream_iterator<char>(ifs),
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
t.cc:11:45: error: member reference base type 'std::vector<char> (*)(std::istream_iterator<char>, std::istream_iterator<char> (*)())' is not a structure or union
std::vector<char>::const_iterator it = v.begin();
~ ^
$
gcc t.cc
t.cc: In function ‘int main()’:
t.cc:11: error: request for member ‘begin’ in ‘v’, which is of non-class type
‘std::vector<char, std::allocator<char> > ()(std::istream_iterator<char, char, std::char_traits<char>, long int>, std::istream_iterator<char, char, std::char_traits<char>, long int> (*)())’
In this case, Clang's second error isn't particularly great (though it does give much more concise type names), but it gives a really critical warning, telling you that the parens in the example are declaring a function, not being used as parens for an argument.
One error that I frequently make (perhaps due to the wildly inconsistent grammar of C++, or perhaps because I am sloppy and have a short attention span...) is dropping a semicolon. Fortunately these are pretty trivial to fix once you know what is going on, but they can lead to some really confusing error messages from some compilers. This happens even in cases where it is immediately obvious what is going on to a human (if they are paying attention!). For example:
$
cat t.c
struct foo { int x; }
typedef int bar;
$
clang t.c
t.c:1:22: error: expected ';' after struct
struct foo { int x; }
^
;
$
gcc t.c
t.c:3: error: two or more data types in declaration specifiers
Note that GCC emits the error on the thing that
follows the problem
. If the struct was the last thing at the end of a header, this means that you'll end up getting the error message
in a completely different file
than where the problem lies. This problem also compounds itself in C++ (as do many others), for example:
$
cat t2.cc
template<class t>
class a{}
class temp{};
a<temp> b;
class b {
}
$
clang t2.cc
t2.cc:2:10: error: expected ';' after class
class a{}
^
;
t2.cc:8:2: error: expected ';' after class
}
^
;
$
gcc t2.c
t2.cc:4: error: multiple types in one declaration
t2.cc:5: error: non-template type ‘a’ used as a template
t2.cc:5: error: invalid type in declaration before ‘;’ token
t2.cc:8: error: expected unqualified-id at end of input
In addition to emitting the confusing error "multiple types in one declaration", GCC goes on to confuse itself in other ways.
In C++ code, pointers and references often get used fairly interchangeably and it is common to use . where you mean ->. Clang recognizes this common sort of mistake and helps you out:
$
cat t.cc
#include <map>
int bar(std::map<int, float> *X) {
return X.empty();
}
$
clang t.cc
t.cc:4:11: error: member reference type 'std::map<int, float> *' is a pointer; maybe you meant to use '->'?
return X.empty();
~^
->
$
gcc t.cc
t.cc: In function ‘int bar(std::map<int, float, std::less<int>, std::allocator<std::pair<const int, float> > >*)’:
t.cc:4: error: request for member ‘empty’ in ‘X’, which is of non-class type ‘std::map<int, float, std::less<int>, std::allocator<std::pair<const int, float> > >*’
In addition to helpfully informing you that your pointer is a "non-class type", it goes out of its way to spell the full definition of std::map out, which is certainly not helpful.
Perhaps it's just me, but I tend to make this mistake quite a bit, again while in a hurry. The C++ :: operator is used to separate nested name specifiers, but somehow I keep typing : instead. Here is a minimal example that shows the idea:
$
cat t.cc
namespace x {
struct a { };
}
x:a a2;
x::a a3 = a2;
$
clang t.cc
t.cc:5:2: error: unexpected ':' in nested name specifier
x:a a2;
^
::
$
gcc t.cc
t.cc:5: error: function definition does not declare parameters
t.cc:6: error: ‘a2’ was not declared in this scope
In addition to getting the error message right (and suggesting a fixit replacement to "::"), Clang "knows what you mean" so it handles the subsequent uses of a2 correctly. GCC, in contrast, gets confused about what the error is which leads it to emit bogus errors on every use of a2. This can be seen with a slightly elaborated example:
$
cat t2.cc
namespace x {
struct a { };
}
template <typename t>
class foo {
};
foo<x::a> a1;
foo<x:a> a2;
x::a a3 = a2;
$
clang t2.cc
t2.cc:10:6: error: unexpected ':' in nested name specifier
foo<x:a> a2;
^
::
t2.cc:12:6: error: no viable conversion from 'foo<x::a>' to 'x::a'
x::a a3 = a2;
^    ~~
t2.cc:2:10: note: candidate constructor (the implicit copy constructor) not viable: no known conversion from 'foo<x::a>' to 'x::a const' for 1st argument
struct a { };
^
$
gcc t2.cc
t2.cc:10: error: template argument 1 is invalid
t2.cc:10: error: invalid type in declaration before ‘;’ token
t2.cc:12: error: conversion from ‘int’ to non-scalar type ‘x::a’ requested
Here you can see that Clang's second error message is exactly right (and is explained). GCC gives a confusing follow on message about converting an "int" to x::a. Where did "int" come from?
C++ is a power tool that gives you plenty of rope to shoot yourself in the foot as well as mix your multi-paradigmed metaphors. Unfortunately, this power gives you plenty of opportunities to find yourself in a near hopeless situation where you know "something is wrong" but have no idea what the real problem is or how to fix it. Thankfully, Clang tries to be there for you, even in the toughest of times. For example, here's a case involving ambiguous lookup:
$
cat t.cc
struct B1 { void f(); };
struct B2 { void f(double); };
struct I1 : B1 { };
struct I2 : B1 { };
struct D: I1, I2, B2 {
using B1::f;  using B2::f;
void g() {
f();
}
};
$
clang t.cc
t.cc:10:5: error: ambiguous conversion from derived class 'D' to base class 'B1':
struct D -> struct I1 -> struct B1
struct D -> struct I2 -> struct B1
f();
^
$
gcc t.cc
t.cc: In member function ‘void D::g()’:
t.cc:10: error: ‘B1’ is an ambiguous base of ‘D’
In this case, you can see that not only does clang tell you that there is an ambiguity, it tells you
exactly the paths through the inheritance hierarchy that are the problems
. When you're dealing with a non-trivial hierarchy, and all the classes aren't in a single file staring at you, this can be a real life saver.
To be fair, GCC occasionally tries to help out. Unfortunately, when it does so it's not clear if it helps more than it hurts. For example, if you comment out the two using declarations in the example above you get:
$
clang t.cc
t.cc:10:5: error: non-static member 'f' found in multiple base-class subobjects of type 'B1':
struct D -> struct I1 -> struct B1
struct D -> struct I2 -> struct B1
f();
^
t.cc:1:18: note: member found by ambiguous name lookup
struct B1 { void f(); };
^
$
gcc t.cc
t.cc: In member function ‘void D::g()’:
t.cc:10: error: reference to ‘f’ is ambiguous
t.cc:2: error: candidates are: void B2::f(double)
t.cc:1: error:                 void B1::f()
t.cc:1: error:                 void B1::f()
t.cc:10: error: reference to ‘f’ is ambiguous
t.cc:2: error: candidates are: void B2::f(double)
t.cc:1: error:                 void B1::f()
t.cc:1: error:                 void B1::f()
It looks like GCC is trying here, but why is it emitting two errors on line 10 and why is it printing B1::f twice in each? When I get these sort of errors (which is pretty rare, since I don't use multiple inheritance like this often) I really value clarity when unraveling what is going on.
Okay, this may be going a bit far, but how else are you going to fall completely in love with a compiler?
$
cat t.c
void f0() {
<<<<<<< HEAD
int x;
=======
int y;
>>>>>>> whatever
}
$
clang t.c
t.c:2:1: error: version control conflict marker in file
<<<<<<< HEAD
^
$
gcc t.c
t.c: In function ‘f0’:
t.c:2: error: expected expression before ‘<<’ token
t.c:4: error: expected expression before ‘==’ token
t.c:6: error: expected expression before ‘>>’ token
Yep, clang actually detects the merge conflict and parses one side of the conflict. You don't want to get tons of nonsense from your compiler on such a simple error, do you?
Clang: crafted for real programmers who make might make the occasional mistake. Why settle for less?
-Chris
