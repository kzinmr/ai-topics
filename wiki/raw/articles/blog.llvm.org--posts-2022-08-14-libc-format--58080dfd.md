---
title: "Text formatting in C++ using libc++"
url: "https://blog.llvm.org/posts/2022-08-14-libc++-format/"
fetched_at: 2026-05-05T07:01:37.168813+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Text formatting in C++ using libc++

Source: https://blog.llvm.org/posts/2022-08-14-libc++-format/

Text formatting in C++ using libc++
Historically formatting text in C++, using the standard library, has been
unpleasant. It is possible to get nice output with the stream operators, but it
is very verbose due to the stream manipulators. The other option is using
printf
, which is convenient but only supports a limited number of types and
is not extendable. A non-standard option is using the
{fmt}
library. This article provides a
short introduction to the parts of this library that were standardized in C++20
as
std::format
, as well as the current implementation status in LLVM 15.
What is
std::format
std::format
is a text formatting library using format strings similar to
Python’s
format
and extensible for user defined types.
#include
<format>
#include
<iostream>
int
main
() {
std
::
cout
<<
std
::
format(
"Hello {} in C++{}"
,
"std::format"
,
20
);
}
Writes the following output:
Hello std::format in C++20
The
{}
indicates a replacement field like
%
in
printf
. With
std::format
the argument types are known, so it is not required to specify
them in the replacement field.
The desired output format and the positional argument to use for each
replacement field can also be specified.
(For brevity, the following examples omit the required includes.)
Writes the first positional argument using different bases, a prefix, and
zero padding to 8 columns.
int
main
() {
std
::
cout
<<
std
::
format(
"{0:#08b}, {0:#08o}, {0:08}, {0:#08x}"
,
16
);
}
0b010000, 00000020, 00000016, 0x000010
It is possible to use an upper case prefix and hexadecimal digits.
int
main
() {
std
::
cout
<<
std
::
format(
"{0:#08B}, {0:#08o}, {0:08}, {0:#08X}"
,
15
);
}
0B001111, 00000017, 00000015, 0X00000F
The alignment and fill character can be specified.
int
main
() {
std
::
cout
<<
std
::
format(
"{:#<8} {:*>8} {:-^5}"
,
"Hello"
,
"world"
,
'!'
);
}
Hello### ***world --!--
When printing tables it is nice to be able to specify the alignment and width
of the columns. However, formatting Unicode text can be especially tricky,
since not every
char
(or
wchar_t
) is one “character”.
For example the letter Á, can be written in two ways:
LATIN CAPITAL LETTER A WITH ACUTE
LATIN CAPITAL LETTER A + COMBINING ACUTE ACCENT
This combining of multiple “characters” is used in several scripts and in
emojis. (This “combined multiple characters” is known as
extended grapheme clusters
in
Unicode.) The library has implemented these rules so it will count both forms
of Á as using one column in the output.
Another issue with text formatting is that not all every “character” has the
same column width. Based on the “character” the column width is estimated to be
one or two columns.
Below is an example taken from the
paper
that
introduced the width estimation algorithm in
std::format
:
struct
input
{
const
char
*
text;
const
char
*
info;
};
int
main
() {
input inputs[]
=
{
{
"Text"
,
"Description"
},
{
"-----"
,
"------------------------------------------------------------------------"
"--------------"
},
{
"
\x41
"
,
"U+0041 { LATIN CAPITAL LETTER A }"
},
{
"
\xC3\x81
"
,
"U+00C1 { LATIN CAPITAL LETTER A WITH ACUTE }"
},
{
"
\x41\xCC\x81
"
,
"U+0041 U+0301 { LATIN CAPITAL LETTER A } { COMBINING ACUTE ACCENT }"
},
{
"
\xc4\xb2
"
,
"U+0132 { LATIN CAPITAL LIGATURE IJ }"
},
// Ĳ
{
"
\xce\x94
"
,
"U+0394 { GREEK CAPITAL LETTER DELTA }"
},
// Δ
{
"
\xd0\xa9
"
,
"U+0429 { CYRILLIC CAPITAL LETTER SHCHA }"
},
// Щ
{
"
\xd7\x90
"
,
"U+05D0 { HEBREW LETTER ALEF }"
},
// א
{
"
\xd8\xb4
"
,
"U+0634 { ARABIC LETTER SHEEN }"
},
// ش
{
"
\xe3\x80\x89
"
,
"U+3009 { RIGHT-POINTING ANGLE BRACKET }"
},
// 〉
{
"
\xe7\x95\x8c
"
,
"U+754C { CJK Unified Ideograph-754C }"
},
// 界
{
"
\xf0\x9f\xa6\x84
"
,
"U+1F921 { UNICORN FACE }"
},
// 🦄
{
"
\xf0\x9f\x91\xa8\xe2\x80\x8d\xf0\x9f\x91\xa9\xe2\x80\x8d
"
"
\xf0\x9f\x91\xa7\xe2\x80\x8d\xf0\x9f\x91\xa6
"
,
"U+1F468 U+200D U+1F469 U+200D U+1F467 U+200D U+1F466 "
"{ Family: Man, Woman, Girl, Boy } "
}
// 👨‍👩‍👧‍👦
};
for
(
auto
input: inputs) {
std
::
cout
<<
std
::
format(
"{:>5} | {}
\n
"
, input.text, input.info);
}
}
(Note the column width is intended to look good on a terminal. The author has
observed differences in quality of the output depending on the browser used.)
Text | Description
----- | --------------------------------------------------------------------------------------
    A | U+0041 { LATIN CAPITAL LETTER A }
    Á | U+00C1 { LATIN CAPITAL LETTER A WITH ACUTE }
    Á | U+0041 U+0301 { LATIN CAPITAL LETTER A } { COMBINING ACUTE ACCENT }
    Ĳ | U+0132 { LATIN CAPITAL LIGATURE IJ }
    Δ | U+0394 { GREEK CAPITAL LETTER DELTA }
    Щ | U+0429 { CYRILLIC CAPITAL LETTER SHCHA }
    א | U+05D0 { HEBREW LETTER ALEF }
    ش | U+0634 { ARABIC LETTER SHEEN }
   〉 | U+3009 { RIGHT-POINTING ANGLE BRACKET }
   界 | U+754C { CJK Unified Ideograph-754C }
   🦄 | U+1F921 { UNICORN FACE }
   👨‍👩‍👧‍👦 | U+1F468 U+200D U+1F469 U+200D U+1F467 U+200D U+1F466 { Family: Man, Woman, Girl, Boy }
Attempting to format a value as the wrong type (e.g. formatting a string as a
number) will result in a compilation error, instead of a runtime error with
printf
. Most of the major compilers provide a warning to try to detect
incorrect format specifiers in
printf
, but this is not part of the
specification, and in particular embedded compilers often don’t provide that
warning. In contrast,
std::format
is
specified
to produce a compilation
error, which is implemented in the library itself using C++20
consteval
functions.
int
main
() {
std
::
cout
<<
std
::
format(
"{0:#08B}, {0:#08o}, {0:08}, {0:#08X}"
,
"15"
);
}
The compiler output starts with this error, followed by a lot of not too useful messages.
error: call to consteval function 'std::basic_format_string<char, const char (&)[3]>::basic_format_string<char[37]>' is not a constant expression
  std::cout << std::format("{0:#08B}, {0:#08o}, {0:08}, {0:#08X}", "15");
In addition to outputting the formatted result to a string, it is also possible:
to output the result to an arbitrary output iterator,
int
main
() {
std
::
format_to(
std
::
ostream_iterator
<
char
>
(std
::
cout,
""
),
"Hello {} in C++{}
\n
"
,
"std::format"
,
20
);
}
to determine the output size,
int
main
() {
std
::
cout
<<
std
::
formatted_size(
"Hello {} in C++{}
\n
"
,
"std::format"
,
20
);
}
27
or limit the size of the output.
int
main
() {
std
::
format_to(
std
::
ostream_iterator
<
char
>
(std
::
cout,
""
),
11
,
"Hello {} in C++{}
\n
"
,
"std::format"
,
20
);
}
Hello std
An example of formatting user defined types is available in the standard
library. It has formatting support for the
chrono
library. (This is not
available in libc++ yet.) These formatters are quite complex. For other types
it is possible quickly create a formatter. For example for the following
enum class
:
enum
class
color
{ red, green, blue };
Adding a formatter based on an existing formatter can be done like:
template
<>
struct
std
::
formatter
<
color
>
:
std
::
formatter
<
const
char
*>
{
static
constexpr
const
char
*
color_names[]
=
{
"red"
,
"green"
,
"blue"
};
auto
format
(color c,
auto
&
ctx)
const
->
decltype
(ctx.out()) {
using
base
=
formatter
<
const
char
*>
;
return
base
::
format(color_names[
static_cast
<
int
>
(c)], ctx);
}
};
Now all features of the
const char*
formatter are available in the color
formatter:
int
main
() {
std
::
cout
<<
std
::
format(
"{:#<10}
\n
{:+^10}
\n
{:->10}
\n
"
,
color
::
red, color
::
green, color
::
blue);
}
red#######
++green+++
------blue
More examples and details of the specification can be found in this
{fmt} cheet sheet
.
The status in LLVM 15
In LLVM 15 most of the basic text formatting is complete. All major papers
have been implemented, but some defect reports are not implemented. The libc++
team also wants to work on performance improvements and improvements to the
compile-time errors. Some of these improvements have already landed in
main
and will be included in LLVM 16, while others are only planned.
Since the library is not entirely complete and the ABI may need to change (due
to planned improvements but also changes voted by the C++ Committee), it is
shipped as an experimental feature in LLVM 15. To use the code in libc++ you
need to compile the code like:
clang -std=c++20 -stdlib=libc++ -fexperimental-library -ofoo foo.cpp
Format support for
chrono
is unavailable. Initial work has landed for
LLVM 16, but none of it is available in LLVM 15. The
chrono
library
itself lacks support for time zones, leap seconds, and some of the less common
clocks. These need to be available before the formatting support for
chrono
can be completed.
Formatting improvements in C++23
In the examples the output is first formatted in a
std::string
before
streaming it to the output. To avoid the temporary
std::string
it is
possible to use
std::format_to
, but that doesn’t have an ergonomic syntax.
In C++23 there will be
std::print
.
int
main
() {
std
::
print(
"Hello {} in C++{}"
,
"std::format"
,
20
);
}
Hello std::format in C++20
There is little support for formatting containers. In C++23 it will become
possible to format ranges and containers.
int
main
() {
std
::
print(
"{::*^5}"
, std
::
vector
<
int
>
{
1
,
2
,
3
});
}
[**1**, **2**, **3**]
Some progress on formatting ranges has been made, but the main focus in the
short term will be to finish C++20’s format implementation.
Closing words
Starting with C++20, formatting text becomes a lot more pleasant and C++23 has
even more improvements lined up. This should provide long awaited functionality
in C++ and allow replacing several uses of
<iostream>
by a more convenient,
faster and safer alternative.
Acknowledgements
Huge thanks to Victor Zverovich, the author of {fmt}. He has been heavily
involved in getting
std::format
in the C++ Standard. He has aided reviewing
libc++’s implementation and his insights and comments have improved the quality
of the implementation.
