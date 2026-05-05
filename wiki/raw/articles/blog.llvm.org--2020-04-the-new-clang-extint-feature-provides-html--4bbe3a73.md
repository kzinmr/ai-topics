---
title: "The New Clang _ExtInt Feature Provides Exact Bitwidth Integer Types"
url: "https://blog.llvm.org/2020/04/the-new-clang-extint-feature-provides.html"
fetched_at: 2026-05-05T07:01:37.683950+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The New Clang _ExtInt Feature Provides Exact Bitwidth Integer Types

Source: https://blog.llvm.org/2020/04/the-new-clang-extint-feature-provides.html

The New Clang _ExtInt Feature Provides Exact Bitwidth Integer Types
By Erich Keane
Apr 21, 2020
#Clang
9 minute read
Author
:
Erich Keane
, Compiler Frontend Engineer, Intel Corporation
Earlier this month I finally committed a patch to implement the extended-integer type class,
_ExtInt
after nearly two and a half years of design and implementation. These types allow developers to use custom width integers, such as a 13-bit signed integer. This patch is currently designed to track
N2472
, a proposal being actively considered by the ISO WG14 C Language Committee. We feel that these types are going to be extremely useful to many downstream users of Clang, and provides a language interface for LLVM's extremely powerful integer type class.
Motivation
LLVM-IR has the ability to represent integers with a bitwidth from 1 all the way to 16,777,215(
(1<<24)-1
), however the C language is limited to just a few power-of-two sizes. Historically, these types have been sufficient for nearly all programming architectures, since power-of-two representation of integers is convenient and practical.
Recently, Field-Programmable Gate Array (FPGA) tooling, called High Level Synthesis Compilers (HLS), has become practical and powerful enough to use a general purpose programming language for their generation. These tools take C or C++ code and produce a transistor layout to be used by the FPGA. However, once programmers gained experience in these tools, it was discovered that the standard C integer types are incredibly wasteful for two main reasons.
First, a vast majority of the time programmers are not using the full width of their integer types. It is rare for someone to use all 16, 32, or 64 bits of their integer representation. On traditional CPUs this isn't much of a problem as the hardware is already in place, so having bits never set comes at zero cost. On the other hand, on FPGAs logic gates are an incredibly valuable resource, and HLS compilers should not be required to waste bits on large power of two integers when they only need a small subset of that! While the optimizer passes are capable of removing some of these widths, a vast majority of this hardware needs to be emitted.
Second, the C language requires that integers smaller than
int
are promoted to operations on the 'int' type. This further complicates hardware generation, as promotions to
int
are expensive and tend to stick with the operation for an entire statement at a time. These promotions typically have semantic meaning, so simply omitting them isn't possible without changing the meaning of the source code. Even worse, the proliferation of
auto
has resulted in user code results in the larger integer size being quite viral throughout a program.
The result is massively larger FPGA/HLS programs than the programmer needed, and likely much larger than they intended. Worse, there was no way for the programmer express their intent in the cases where they do not need the full width of a standard integer type.
Using the
_ExtInt
Language Feature
The patch as accepted and committed into LLVM solves most of the above problems by providing the
_ExtInt
class of types. These types translate directly into the corresponding LLVM-IR integer types. The
_ExtInt
keyword is a type-specifier (like
int
) that accepts a required integral constant expression parameter representing the number of bits to be used. More succinctly:
_ExtInt(7)
is a signed integer type using 7 bits. Because it is a type-specifier, it can also be combined with
signed
and
unsigned
to change the signedness (and overflow behavior!) of the values. So "
unsigned _ExtInt(9) foo;"
declares a variable
foo
that is an unsigned integer type taking up 9 bits and represented as an
i9
in LLVM-IR.
The
_ExtInt
types as implemented do not participate in any implicit conversions or integer promotions, so all math done on them happens at the appropriate bit-width. The WG14 paper proposes integer promotion to the largest of the types (that is, adding an
_ExtInt(5)
and an
_ExtInt(6)
would result in an
_ExtInt(6)
), however the implementation does not permit that and
_ExtInt(5) + _ExtInt(6)
would result in a compiler error. This was done so that in the event that WG14 changes the design of the paper, we will be able to implement it without breaking existing programs. In the meantime, this can be worked around with explicit casts:
(_ExtInt(6))AnExtInt5 + AnExtInt6
or
static_cast<ExtInt(6)>(AnExtInt5) + AnExtInt6.
Additionally, for C++, clang supports making the bitwidth parameter a dependent expression, so that the following is legal:
template<size_t WidthA, size_t WidthB>
_ExtInt(WidthA + WidthB) lossless_mul(_ExtInt(WidthA) a, _ExtInt(WidthB) b) {
return static_cast<
_ExtInt(WidthA + WidthB)>(a)
* static_cast<
_ExtInt(WidthA + WidthB)
>(b);
}
We anticipate that this ability and these types will result in some extremely useful pieces of code, including novel uses of 256 bit, 512 bit, or larger integers, plus uses of 8 and 16 bit integers for those who can't afford promotions. For example, one can now trivially implement an extended integer type struct that does all operations provably losslessly, that is, adding two 6 bit values would result in a 7 bit value.
In order to be consistent with the C Language, expressions that include a standard type will still follow integral promotion and conversion rules. All types smaller than
int
will be promoted, and the operation will then happen at the largest type.  This can be surprising in the case where you add a
short
and an
_ExtInt(15)
, where the result will be
int
. However, this ends up being the most consistent with the C language specification.
Additionally, when it comes to conversions, these types 'lose' to the C standard types of the same size or greater. So, an
int
added to a
_ExtInt(32)
will result in an
int
. However, an
int
and a
_ExtInt(33)
will be the latter. This is necessary to preserve C integer semantics.
History
As mentioned earlier, this feature has been a long time coming! In fact, this is likely the fourth implementation that was done along the way in order to get to this point. Additionally, this is far from over, we very much hope that upon acceptance of this by the WG14 Standards Committee that additional extensions and features will become available.
I was approached to implement this feature in the Fall of 2017 by my company's FPGA group, which had the problems mentioned above. They had attempted a solution that used some clever parsing to make these look like templates, and implemented them extensively throughout the compiler. As I was concerned about the flexibility and usability of these types in the type and template system, we opted to implement these as a type-attribute under the controversially named Arbitrary Precision Int (spelled
__ap_int
). This spelling was heavily influenced by the vector-types implementations in GCC and Clang.
We then were able to wrap a set of typedefs (or dependent
__ap_int
types) in a structure that provided exactly the C and C++ interface we wished to expose. As this was a then proprietary implementation, it was kept in our downstream implementation, where it received extensive testing and usage.
Roughly a year later (and a little more than year ago from today!) I was authorized to contribute our implementation to the open source LLVM community! I decided to significantly refactor the implementation in order to better fit into the Clang type system, and uploaded it for
review
.This (now third!) implementation of this feature was proposed via RFC and code review at the same time.
While the usefulness was immediately acknowledged, it was rejected by the Clang code owner for two reasons: First the spelling was considered unpalatable, and Second it was a pure extension without standardization. This began the nearly year-long effort to come up with a standards proposal that would better define and describe the feature as well as come up with a spelling that was more in line with the standard language.
Thanks to the invaluable feedback and input from Richard Smith, my coworkers Melanie Blower, Tommy Hoffner, and myself were able to propose the spelling _ExtInt for standardization. Additionally, the feature again re-implemented at the beginning of this year and eventually accepted and committed!
The standardization paper (
N2472
) was presented at this Spring's WG14 ISO C Language Committee Meeting where it received near unanimous support. We expect to have an updated version of the paper with wording ready for the next WG14 meeting, where we hope it will receive sufficient support to be accepted into the language.
Future Extensions
While the feautre as committed in Clang is incredibly useful, it can be taken further. There are a handful of future extensions that we wish to implement once guidance from WG14 has been given on their direction and implementation.
First, we believe the special integer promotion/conversion rules, which omit automatic promotion to
int
and instead provide operations at the largest type are both incredibly useful and powerful. While we have received positive encouragement from WG14, we hope that the wording paper we provide will both clarify the mechanism and definition in a way that supports all common uses.
Secondly, we would like to choose a printf/scanf specifier that permits specifying the type for the C language. This was the topic of the WG14 discussion, and also received strong encouragement. We intend to come up with a good representation, then implement this in major implementations.
Finally, numerous people have suggested implementing a way of spelling literals of this type. This is important for two reasons: First, it allows using literals without casts in expressions in a way that doesn't run afoul of promotion rules. Second, it provides a way of spelling integer literals larger than
UINTMAX_MAX
, which can be useful for initializing the larger versions of these types. While the spelling is undecided, we intend something like:
1234X
would result in an integer literal with the value
1234
represented in an
_ExtInt(11)
, which is the smallest type capable of storing this value.
However, without the integer promotion/conversion rules above, this feature isn't nearly as useful. Additionally, we'd like to be consistent with whatever the C language committee chooses. As soon as we receive positive guidance on the spelling and syntax of this type, we look forward to providing an implementation.
Conclusion
In closing, we encourage you to try using this and provide feedback to both myself, my proposal co-authors, and the C committee itself! We feel this is a really useful feature and would love to get as much user experience as possible. Feel free to contact myself and my co-authors with any questions or concerns!
-
Erich Keane
, Intel Corporation
