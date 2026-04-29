---
title: "Unsigned char std::basic_string<> in C++"
url: "https://berthub.eu/articles/posts/unsigned-char-std-string-cpp/"
fetched_at: 2026-04-29T07:02:23.384936+00:00
source: "berthub.eu"
tags: [blog, raw]
---

# Unsigned char std::basic_string<> in C++

Source: https://berthub.eu/articles/posts/unsigned-char-std-string-cpp/

Brief post on a somewhat vexing and irritating C++ problem I ran into some time ago. I hope that this page will help other people deal with this problem more quickly than I did.
I’ve long used
std::basic_string<uint8_t>
, an unsigned char string, for fiddling with bits. You could use a regular
char
string, but especially when doing cryptographic or sub-byte operations, it is more convenient to not have to deal with sign bits.
Now, you could of course also use a
std::vector<uint8_t>
, but
std::vector
lacks some conveniences like
operator+
or
.substr()
. Also, previously, passing around
std::string
could be faster due to some (
now outlawed
) copy on write magic. Meanwhile, in modern C++, returning a
std::vector<>
is also guaranteed to be fast,
since it will be constructed on the caller’s stack
. So there is less of a reason to use
std::basic_string
these days.
Now, my
std::basic_string<uint8_t>
started to break on FreeBSD and later on OpenBSD with confusing errors. At first I blamed the C++ libraries on those systems, but it turns out it is a bit more difficult.
My former co-workers Jeff Sipek and  Otto Moerbeek
helpfully found out what was going on
. Many
std::basic_string<T>
operations are actually powered by
std::char_traits<T>
. Libraries must provide these traits for regular
char
(and several other types), but there is no requirement that they do so for unsigned chars.
Gcc and clang for a long time however did provide a generic
std::char_traits<>
that worked for all types. However, in the libstdc++ source code we read:
/* @note For any given actual character type, this definition is
*  probably wrong.  (Most of the member functions are likely to be
*  right, but the int_type and state_type typedefs, and the eof()
*  member function, are likely to be wrong.)  The reason this class
*  exists is so users can specialize it.
*/
“This definition is probably wrong”, but they note you could use this base class to build your own
std::char_trait
that would then be correct.
In the llvm release notes for 19.1.0,
we read
:
The base template for std::char_traits has been removed in LLVM 19. If you are using std::char_traits with types other than char, wchar_t, char8_t, char16_t, char32_t or a custom character type for which you specialized std::char_traits, your code will stop working. The Standard does not mandate that a base template is provided, and such a base template is bound to be incorrect for some types, which could currently cause unexpected behavior while going undetected.
This is all true, and they warn us that code will stop working, which is nice enough.
So, if you get all kinds of errors compiling code that uses
std::basic_string<uint8_t>
or
std::basic_string<unsigned char>
, know that this previously only worked by accident. And that accident has been fixed now.
Which sadly means spending some quality time replacing string concatenation or uses of
.substr()
or
.c_str()
by their
std::vector<uint8_t>
equivalents. Alternatively, you could provide your own
std::char_traits<uint8_t>
but it appears
this could lead to some surprises
.
Good luck, and thanks are due to Jeff and Otto for telling me what was wrong with my code!
