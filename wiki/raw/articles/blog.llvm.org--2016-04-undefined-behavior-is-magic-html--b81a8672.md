---
title: "My Little LLVM: Undefined Behavior is Magic!"
url: "https://blog.llvm.org/2016/04/undefined-behavior-is-magic.html"
fetched_at: 2026-05-05T07:01:39.117834+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# My Little LLVM: Undefined Behavior is Magic!

Source: https://blog.llvm.org/2016/04/undefined-behavior-is-magic.html

My Little LLVM: Undefined Behavior is Magic!
The re-branding puts to rest a long-standing issue with LLVM’s “dragon” logo
actually being a wyvern
with an
upside-down head
, a special form of undefined behavior in its own right. The logo is now
clearly
a pegasus pony.
Another great side-effect of this rebranding is increased security by auto-magically closing all vulnerabilities used by the hacker who goes by the pseudonym “
Pinkie Pie
”.
These new features are enabled with the
-rainbow
clang option, in honor of Rainbow Dash’s unary name.
A Few Examples
C++’s memory model specifies that data races are undefined behavior. It is well established that
no sane compiler would optimize atomics
, LLVM will therefore supplement the Standard’s
happens-before relationship
with an LLVM-specific
happens-to-work relationship
. On most architectures this will be implemented with micro-pause primitives such as x86’s
rep rep rep nop
instruction.
Shifts by bit-width or larger will now return a normally-distributed random number. This also obsoletes
rand()
and
std::random_shuffle
.
bool
now obeys the rules of
truthiness
to avoid that annoying “but what if it’s
not
zero or one?” interview question. Further, incrementing a
bool
with
++
now does the right thing.
Atomic integer arithmetic is already specified to be two’s complement. Regular arithmetic will therefore now also be atomic. Except when
volatile
, but not when
volatile
atomic.
NaNs
will now compare equal, subnormals are free to self-classify as normal / zero / other, negative zero simply won’t be a thing, IEEE-754 has been upgraded to PONY-754, floats will still
round with style
, and generating a signaling NaN is now guaranteed to
not
be quiet by being equivalent to
putchar('\a')
. While we’re at it none of
math.h
will set
errno
anymore. This has nothing to do with undefined behavior but seriously,
errno
?
Type-punning isn’t a thing anymore. We’re renaming it to type-pony-ing, but it doesn’t do anything surprising besides throw parties.
AND WHO DOESN’T LIKE PARTIES‽ EVEN SECURITY PEOPLE DO!
🎉
A Word From Our Sponsors
Cutie Marks
To address the
horse
in the room: we’ve left the new LLVM logo’s cutie mark as
implementation-defined
. Different instances of the logo can use their own cutie mark to illustrate their proclivities, but must clearly document them.
