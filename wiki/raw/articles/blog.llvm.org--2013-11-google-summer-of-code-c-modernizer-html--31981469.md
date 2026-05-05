---
title: "Google Summer of Code: C++ Modernizer Improvements"
url: "https://blog.llvm.org/2013/11/google-summer-of-code-c-modernizer.html"
fetched_at: 2026-05-05T07:01:43.056285+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Google Summer of Code: C++ Modernizer Improvements

Source: https://blog.llvm.org/2013/11/google-summer-of-code-c-modernizer.html

This article presents the improvements made to the tool in the last few months, which include my work from this summer for GSoC. For a complete overview of the tool and how to install it, please visit the documentation:
. For a demonstration of the tool you can take a look at the Going Native 2013 talk given by Chandler Carruth:
. clang-modernize is featured starting at ~33min.
A major improvement since the last version is the ability to transform every file that composes a translation unit not only the main source file. This means headers also get transformed if they need to be which makes the modernizer more useful.
To avoid changing files that shouldn’t be changed, e.g. system headers or headers for third-party libraries, there are a few options to control which files should be transformed:
Since the last article in April, the Add-Override Transform has been improved to handle user-defined macros. Some projects, like LLVM, use a macro that expands to the ‘override’ specifier for backward compatibility with non-C++11-compliant compilers. clang-modernize can detect those macros and use them instead of the ‘override’ identifier.
.
Before
After
#define LLVM_OVERRIDE override
struct
A {
virtual
void
foo();
};
struct
B
:
A {
virtual
void
foo();
};
#define LLVM_OVERRIDE override
struct
A {
virtual
void
foo();
};
struct
B
:
A {
virtual
void
foo()
LLVM_OVERRIDE
;
};
Improvement to Use-Nullptr
This transform has also been improved to handle user-defined macros that behave like NULL. The user specifies which macros can be replaced by nullptr by using the command line switch
-user-null-macros=<string>
.
Example:
clang-modernize
-user-null-macros=MY_NULL
bar.cpp
Before
After
#define MY_NULL 0
void
bar
() {
int
*
p
=
MY_NULL;
}
#define MY_NULL 0
void
bar
() {
int
*
p
=
nullptr
;
}
New Transform: Replace Auto-Ptr
This transform was a result of GSoC work. The transform replaces uses of
std::auto_ptr
by
std::unique_ptr
. It also inserts calls to
std::move()
when needed.
Before
After
#include <memory>
void
steal
(std
::
auto_ptr
<
int
>
x);
void
foo
(
int
i) {
std
::
auto_ptr
<
int
>
p(
new
int
(i));
steal(p);
}
#include <memory>
void
steal
(std
::
unique_ptr
<
int
>
x);
void
foo
(
int
i) {
std
::
unique_ptr
<
int
>
p(
new
int
(i));
steal(
std
::
move(
p
)
);
}
New Transform: Pass-By-Value
Also a product of GSoC this transform makes use of move semantics added in C++11 to avoid a copy for functions that accept types that have move constructors by const reference. By changing to pass-by-value semantics, a copy can be avoided if an rvalue argument is provided. For lvalue arguments, the number of copies remains unchanged.
The transform is currently limited to constructor parameters that are copied into class fields.
Example:
clang-modernize pass-by-value.cpp
Before
After
#include <string>
class
A
{
public:
A(
const
std
::
string &Copied,
const
std
::
string
&
ReadOnly)
:
Copied(Copied),
ReadOnly(ReadOnly) {}
private:
std
::
string Copied;
const
std
::
string
&
ReadOnly;
};
#include <string>
#include <utility>
class
A
{
public:
A(
std
::
string
Copied,
const
std
::
string
&
ReadOnly)
:
Copied(
std
::
move(
Copied
)
),
ReadOnly(ReadOnly) {}
private:
std
::
string Copied;
const
std
::
string
&
ReadOnly;
};
std::move()
is a library function declared in
<utility>
. If need be, this header is added by clang-modernize.
There is a lot of room for improvement in this transform. Other situations that are safe to transform likely exist. Contributions are most welcomed in this area!
Usability Improvements
We also worked hard on improving the overall usability of the modernizer. Invoking the modernizer now requires fewer arguments since most of the time the arguments can be inferred.
If no compilation database or flags are provided, -std=c++11 is assumed.
All transforms are enabled by default.
Files don’t need to be explicitly listed if a compilation database is provided. The modernizer will get files from the compilation database. Use -include to choose which ones.
Two new features were also added.
Automatically reformat code affected by transforms using
LibFormat
.
A new command line switch to choose transforms to apply based on compiler support.
Reformatting Transformed Code
LibFormat
is the library used behind the scenes by
clang-format
, a tool to format C, C++ and Obj-C code.
clang-modernize
uses this library as well to reformat transformed code. When enabled with -format, the default style is LLVM. The -style option can control the style in a way identical to clang-format.
Example:
format.cpp
#include <iostream>
#include <vector>
void
f
(
const
std
::
vector
<
int
>
&
my_container) {
for
(std
::
vector
<
int
>::
const_iterator I
=
my_container.begin(),
E
=
my_container.end();
I
!=
E;
++
I) {
std
::
cout
<<
*
I
<<
std
::
endl;
}
}
Without reformatting
$ clang-modernize -use-auto format.cpp
#include <iostream>
#include <vector>
void
f
(
const
std
::
vector
<
int
>
&
my_container) {
for
(
auto
I
=
my_container.begin(),
E
=
my_container.end();
I
!=
E;
++
I) {
std
::
cout
<<
*
I
<<
std
::
endl;
}
}
With reformatting
$ clang-modernize -format -style=LLVM -use-auto format.cpp
#include <iostream>
#include <vector>
void
f
(
const
std
::
vector
<
int
>
&
my_container) {
for
(
auto
I
=
my_container.begin(), E
=
my_container.end(); I
!=
E;
++
I) {
std
::
cout
<<
*
I
<<
std
::
endl;
}
}
For more information about this option, take a look at the documentation:
Formatting Command Line Options
.
Choosing Transforms based on Compiler Support
Another useful command-line switch is:
-for-compilers
. This option enables all transforms the given compilers support.
As an example, imagine that your project dropped a dependency to a “legacy” version of a compiler. You can automagically modernize your code to the new minimum versions of the compilers you want to support:
To support Clang >= 3.1, GCC >= 4.6 and MSVC 11:
clang-modernize -format -for-compilers=clang-3.1,gcc-4.6,msvc-11 foo.cpp
For more information about this option and to see which transforms are available for each compilers, please read
the documentation
.
What’s next?
The ability to transform many translation units in parallel will arrive very soon. Think of
clang-modernize -j
as in make and ninja. Modernization of large code bases will become much faster as a result.
More transforms are coming down the pipe as well as improvements to existing transforms such as the pass-by-value transform.
We will continue fixing bugs and adding new features. Our backlog is publically available:
https://cpp11-migrate.atlassian.net/secure/RapidBoard.jspa?rapidView=1&view=planning
Get involved!
Interested by the tool? Found a bug? Have an idea of a transform that can be useful to others? The project is Open Source and contributions are most welcomed!
The modernizer has its own bug and project tracker. If you want to file or fix a bug just go to:
https://cpp11-migrate.atlassian.net
A few other addresses to keep in mind:
Final word
Finally I want to thank my mentor Edwin Vane and his team at Intel, Tareq Siraj and Ariel Bernal, for the great support they provided me. Also thanks to the LLVM community and Google Summer of Code team for giving me this opportunity to work on the C++ Modernizer this summer.
-- Guillaume Papin
