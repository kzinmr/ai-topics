---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2013/09/clang-warnings.html"
fetched_at: 2026-05-05T07:01:43.007162+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2013/09/clang-warnings.html

Did you find any bugs? Many common problems are hard to spot from just reading the code. To make a better coding experience, Clang has many diagnostics that will flag these mistakes. The bugs in the code are detailed below.
main.cc does not have any problems.  It merely is a wrapper around the library so that a binary can be produced and run, although running it will not sort the array properly.
sort.h is the header file to the library.
1:#ifndef _EXPERIMENTAL_WARNINGS_SORT_H_
2:#define _EXPERIMNETAL_WARNINGS_SORT_H_
The first warning triggers on the first two lines.  Header guards are used by libraries to prevent multiple
#include
’s of a file from producing redefinition errors.  To work, the
#ifndef
and
#define
must use the same macro name..  The transposition of E and N produces different names and is an easy bug to overlook.  Worse, this sort of bug can hide within headers and never produce a problem when singly included and then much later start producing problems when someone double includes this header. Clang has -Wheader-guard to catch this. GCC does not catch this.
Next, examine the custom ASSERT macro used:
7.#define ASSERT(cond) \
8.    if(!cond) cout << ...
The problem is treating the macro parameter as a function parameter.  Macro arguments are not evaluated.  Instead, they are substituted in as typed.  Thus, code as
ASSERT(x == 5)
becomes
if(!x == 5) cout << ...
The proper fix is to enclose the macro parameter in parentheses, as
if (!(cond)) cout << ...
This is caught by -Wlogical-not-parentheses. Being inside a macro definition, the warning will trigger when the macros are used with a note pointing back here. GCC has no equivalent for -Wlogical-not-parentheses.
13:enum SortType {
14:  unknown = 0,
15:  min_invalid = 3,
16:
17:  bubble = 1,
18:  quick,
19:  insert
20:};
In this enum, a few non-valid values are defined, then the valid enums listed.  Valid enums use the auto increment to get their values.  However,
min_invalid
and
insert
both have value 3.  Luckily, -Wduplicate-enum will identify enums in this situation and point them out. GCC will not warn on this.
On to sort.cc
Class constructor:
4:Sort::Sort(int vec[], int size, bool sorted)
5:    : sorted_(sorted_), vec_(vec), size_(size) {
Members from sort.h:
34:  int* vec_;
35:  bool sorted_;
36:  int &size_;
Checking the only constructor of the class, numerous problems can be seen here.  First notice that the variables are declared
vec_
,
sorted_
, then
size_
, but in the constructor, they are listed as
sorted_
,
vec_
, then
size_
.  The order of initialization is order they were declared, meaning
vec_
is initialized before
sorted_
.  There is no order dependence here, but -Wreorder will warn that the orders don’t match. GCC also has -Wreorder.
Next,
sorted_
is initialized with itself instead of with sorted.  This leads to uninitialized value in
sorted_
, which is caught by the aptly named -Wuninitialized. For this case, GCC has -Wself-assign and -Wself-init.
Finally, notice that
size_
is declared as a reference but size is not passed by reference.  size only lives until the end of the constructor while the reference
size_
will continue to point to it.  -Wdangling-field catches this problem.
7:    ASSERT("!Vector too large.  Number of elements:" + size);
Two problems here.  Adding an integer to a string literal does not concatenate the two together.  Instead, since a string literal is a pointer of type
const char *
, this actually performs pointer math.  With a sufficiently integer, this can even cause the pointer to go past the end of the string into some other memory.  -Wstring-plus-int warns on this case. GCC has no equivalent warning.
7:    ASSERT("!Vector too large.  More than 50 elements.");
When fixed, another problem arises.  A common pattern is to include a string literal describing the assert.  If the assert is always to fire, then expression should evaluate to false.  The string literal evaluates to true, so just negate it to get a false value, right?  Well, a number of common typos can happen.
These values evaluate true:
"true"
"false"
"!true"
"!false"
"any string"
These values evaluate to false:
!"true"
!"false"
!"any string"
!"!any string"
Due to that, -Wstring-conversion will warn when a string literal is converted to a true boolean value.  Use
ASSERT(false && “string”)
or
ASSERT(0 && “string”)
instead. GCC has no equivalent warning.
9:  int sum;
10:  for (unsigned i = 0; !i == size; ++i) {
11:    int sum = sum + vec_[i];
12:    ++i;
13:  }
14:
15:  ASSERT(sum < 100 && "Vector sum is too high");
More bugs here.  The obvious one is the that
sum
is uninitialized on line 9.  When it gets used on line 15, this causes undefined behavior.  This gets caught by -Wuninitialized which suggests setting it to 0 to fix. GCC's -Wuninitialized also catches this.
A poor negation causes a bad condition in the for-loop.
!i == size
is equivalent to
(!i) == size
due to order of operations.  -Wlogical-not-parentheses will suggest
!(i == size)
to correct this. Again, GCC does not have a -Wlogical-not-parantheses equivalent.
On line 10 and 12, for every loop iteration, two
++i
will increment the variable.  A warning in -Wloop-analysis catches this. This warning is Clang-specific.
Two separate problems happen on line 11.  Another -Wuninitialized warning here for using
sum
in its own initialization.  Also, -Wshadow will warn that the variable
sum
inside the loop is different from the variable
sum
outside the loop. Both GCC's and Clang's versions of these warning catches these problems.
18:bool Sort::IsSorted() {
19:  return sort;
20:}
The member variable is called
sorted_
.
sort
is a static function wrapper defined at sort.h line 39.  Here, the function is automatically converted to a function pointer, then to true.  Caught by -Wbool-conversion. GCC has function address to bool conversions placed under -Waddress.
22:static bool CheckSort(int V[]) {
23:  bool ret;
24:  for (int i = 1; i != sizeof(V)/sizeof(V[0]); ++i)
25:    if (V[i] > V[i - 1])
26:      ret = false;
27:  return ret;
28:}
On line 23,
ret
is not initialized.  On line 26, a value may be assigned to it, but it is possible that no path will through the code will set it a value.  The warning -Wsometimes-uninitialized will warn on this and give suggestions on how to fix. GCC will not catch this.
On line 24 inside the for loop conditional, there is
i != sizeof(V)/sizeof(V[0])
, which is trying to keep
i
as a valid array index.  However, the
sizeof
calculation produces the wrong result.  This would be correct if
V
was declared inside the function.  However, as a parameter,
V
has type
int*
, causing the
sizeof
to take the size of a pointer instead of the array.  A separate size argument needs to be passed to the function. Caught by -Wsizeof-array-argument, a Clang specific warning.
30:static const char* TypeToString(SortType Type) {
31:  const char* ret;
32:  switch (Type) {
33:    case bubble:
34:      ret = "bubble";
35:    case quick:
36:      ret = "quick";
37:    case insert:
38:      ret = "insert";
39:  }
40:  return ret;
41:}
A simple enum to string converter function.  Like the previous function,
ret
is again uninitialized, and will be caught by -Wsometimes-uninitialized.  Clang warns here because it can analyze all the paths through the switch and determine that at least one will not assign a value to
ret
. GCC does not have -Wsometimes-uninitialized.
On the switch statement, Clang and GCC notices that
unknown
is not used, caught by the warning -Wswitch.
Clang also has a special attribute,
[[clang::fallthrough]];
, to mark intended fallthroughs in switch cases.  By marking all cases intended uses of fallthrough, Clang can warn on the unintended cases, such as these three cases without break statements.  Otherwise, the fallthrough will cause all three cases to return
“insert”
. This is -Wimplicit-fallthrough, a Clang-specific warning.
43:void Sort::Begin(SortType Type) {
44:  cout << "Sort type: ";
45:  cout << Type == 0 ? "Unknown type, resorting to bubble sort"
46:                    : TypeToString(Type);
47:  cout << endl;
While
cout
uses
operator<<
to stream various types to output, it still is an operator and C++ has a defined order of operations.  Shifts (<< and >>) are evaluated before conditional operators (?:).  To add some parentheses to clear up the order, this becomes:
45:  ((cout << Type) == 0) ? "Unknown type, resorting to bubble sort"
46:                        : TypeToString(Type);
First,
Type
gets pushed to
cout
, via
operator<<
.
operator<<
returns the
cout
stream again.  Streams are convertible to bools to check if they are valid, which is checked against false, converted from 0.  The result of this comparison is used for the conditional operator, whose result is not used anywhere. GCC doesn't catch this, but Clang's -Woverloaded-shift-op-parentheses does.
48:  switch (Type) {
49:    default:
50:    bubble:
51:      BubbleSort(); break;
52:    quick:
53:      QuickSort(); break;
54:    insert:
55:      InsertSort(); break;
56:  }
Another switch statement, also triggers -Wswitch because none of the enum values are represented.  Each of the enum values is missing a case, causing them to become labels instead.  The warning -Wunused-label hints that something is wrong here. -Wunused-label is in both GCC and Clang.
61:  for (int i = 0; i < size_; ++i) {
62:    for (int j = 1; j < size_; ++i) {
...
69:    }
70:  }
This double nested loop gives bubble sort its n
2
running time.  Rather, in this case, an infinite running time.  Note the increment in both of the loops happen on
i
, even in the inner loop.
j
is never touched, either here or inside the loop.  -Wloop-analysis will give a warning when all the variables inside a for loop conditional does not change during the loop iteration. Only in Clang.
63:      int a = vec_[j-1];
64:      int b = vec_[j];
65:      if (a > b); {
66:        vec_[j-1] = b;
67:        vec_[j] = a;
68:      }
Then -Wempty-body warning will trigger on line 65.  The semi-colon here become the entirety of the loop body while the value swap happens on every loop iteration, not only when the conditional is true. Both Clang and GCC has this warning.
This is just a small sample of the warnings that Clang provides. Along with informative diagnostic messages, these warnings help programmers avoid common coding pitfalls. In particular, it saves the programmer time tracking down valid but not intended code later. These warnings make Clang an exceptional productivity and code quality booster for coders.
For reference, a list of warnings discussed above:
-Wbool-conversion
Warns on implicit conversion of a function pointer to a true bool value. GCC has this warning as part of -Waddress.
-Wempty-body
Warns when an if statement, while loop, for loop, or switch statement only has a semi-colon for the body, and is on the same line as the rest of the statement. Clang and GCC warning.
-Wheader-guard
Detects when the #ifndef and #define have different macro names. This causes the header guard to fail to prevent multiple inclusions.
This is a Clang-specific warning available in SVN trunk and slated for the 3.4 release.
-Wimplicit-fallthrough
Enabling this warning will cause a diagnostic to be emitted for all fallthroughs in switch statements that have not been annotated. Requires compilation in C++11 mode. Clang-specific warning, available in the 3.2 release.
-Wlogical-not-parentheses
This warning is part of the -Wparentheses. This group of warnings suggests parentheses in cases where users may read the code differently than the compiler. This warning in particular will trigger when the logical not operator ('!') is applied to the left hand side of a comparison when it was meant to apply to the whole conditional. "!x == y" is different from "!(x == y)" since "!x" will be evaluated before the equality comparison.
This is a Clang-specific warning available in SVN trunk and slated for the 3.4 release.
-Wloop-analysis
Detects questionable code in loops. It catches two interesting loop patterns: a for-loop has an increment/decrement in its header and has the same increment/decrement for the last statement in the loop body, which will execute only half the intended iterations, and when the variables in the for-loop comparison are not modified during the loop, possibly indicating an infinite loop. Clang-specific warning. Unmodified loop variables warning is available in 3.2 and onward. Detection of double increments/decrements is in SVN trunk and slated for the 3.4 release.
-Woverloaded-shift-op-parentheses
The overloaded shift operator is used mainly with streams, such as cin and cout. However, the shift operator has higher precedence than some operators, such as comparison operators, which may cause unexpected problems. This warning suggests parentheses to disambiguate the order of evaluation. Clang-specific warning available since the 3.3 release.
-Wshadow
Variable names in an inner scope may take the same name as a variable in an outer scope, yet refer to different variables.  Then the variable in the outer scope may be difficult or impossible to refer to while inside the inner scope.  -Wshadow points out such variable name reuse.  Both Clang and GCC has this warning.
-Wsizeof-array-argument
Warns when attempting to take the sizeof() of an array that is a parameter. These arrays are treated as a pointer, which will return an unexpected size. Clang-specific warning.
-Wstring-conversion
A literal string has type const char *. As a pointer, it is convertible to a bool, but in most cases, the conversion to bool is not intended. This warning will trigger on such conversions. Clang-specific warning.
-Wswitch
This warning detects when an enum type is used in the switch, and some values of the enum are not represented in the cases. Clang and GCC warning.
-Wuninitialized
When a variable is declared, its value is uninitialized. If its value is used elsewhere before being initialized, undefined behavior may result. Present in both Clang and GCC. Clang performs additional analysis, such as following multiple code paths. Some items caught by Clang's warning falls under different warnings in GCC, such as -Wself-assign and -Wself-init.
-Wunique-enum
Enum elements can either be declared explicitly to a value, or implicitly which gives it the value of the previous element plus one. Clang-specific warning available since the 3.3 release.
-Wunused-label
Warns when a label is present in code, but never called. Clang and GCC warning.
* Edited September 10, 2013. Spelling corrections were made. Warnings which were first available in 3.2 or later are noted. If not marked, the warning has been around since before the 3.2 release.
