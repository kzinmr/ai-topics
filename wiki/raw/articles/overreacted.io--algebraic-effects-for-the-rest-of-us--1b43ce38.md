---
title: "Algebraic Effects for the Rest of Us"
url: "https://overreacted.io/algebraic-effects-for-the-rest-of-us/"
fetched_at: 2026-05-01T07:02:02.321598+00:00
source: "overreacted.io"
tags: [blog, raw]
---

# Algebraic Effects for the Rest of Us

Source: https://overreacted.io/algebraic-effects-for-the-rest-of-us/

Have you heard about
algebraic effects
?
My first attempts to figure out what they are or why I should care about them were unsuccessful. I found a
few
pdfs
but they only confused me more. (There’s something about academic pdfs that makes me sleepy.)
But my colleague Sebastian
kept
referring
to
them
as a mental model for some things we do inside of React. (Sebastian works on the React team and came up with quite a few ideas, including Hooks and Suspense.) At some point, it became a running joke on the React team, with many of our conversations ending with:
It turned out that algebraic effects are a cool concept and not as scary as I thought from those pdfs.
If you’re just using React, you don’t need to know anything about them — but if you’re feeling curious, like I was, read on.
(Disclaimer: I’m not a programming language researcher, and might have messed something up in my explanation. I am not an authority on this topic so let me know!)
Algebraic Effects
are a research programming language feature. This means that
unlike
if
, functions, or even
async / await
, you probably can’t really use them in production yet.
They are only supported by a
few
languages
that were created specifically to explore that idea. There is progress on productionizing them in OCaml which is… still
ongoing
. In other words,
Can’t Touch This
.
Edit: a few people mentioned that LISP languages
do offer something similar
, so you can use it in production if you write LISP.
Imagine that you’re writing code with
goto
, and somebody shows you
if
and
for
statements. Or maybe you’re deep in the callback hell, and somebody shows you
async / await
. Pretty cool, huh?
If you’re the kind of person who likes to learn about programming ideas several years before they hit the mainstream, it might be a good time to get curious about algebraic effects. Don’t feel like you
have to
though. It is a bit like thinking about
async / await
in 1999.
The name might be a bit intimidating but the idea is simple. If you’re familiar with
try / catch
blocks, you’ll figure out algebraic effects very fast.
Let’s recap
try / catch
first. Say you have a function that throws. Maybe there’s a bunch of functions between it and the
catch
block:
function
getName
(
user
)
{
let
name
=
user
.
name
;
if
(
name
===
null
)
{
throw
new
Error
(
'
A girl has no name
'
);
}
return
name
;
}
function
makeFriends
(
user1
,
user2
)
{
user1
.
friendNames
.
push
(
getName
(
user2
));
user2
.
friendNames
.
push
(
getName
(
user1
));
}
const
arya
=
{
name
:
null
,
friendNames
:
[]
};
const
gendry
=
{
name
:
'
Gendry
'
,
friendNames
:
[]
};
try
{
makeFriends
(
arya
,
gendry
);
}
catch
(
err
)
{
console
.
log
(
"
Oops, that didn't work out:
"
,
err
);
}
We
throw
inside
getName
, but it “bubbles” up right through
makeFriends
to the closest
catch
block. This is an important property of
try / catch
.
Things in the middle don’t need to concern themselves with error handling.
Unlike error codes in languages like C, with
try / catch
, you don’t have to manually pass errors through every intermediate layer in the fear of losing them. They get propagated automatically.
In the above example, once we hit an error, we can’t continue. When we end up in the
catch
block, there’s no way we can continue executing the original code.
We’re done. It’s too late. The best we can do is to recover from a failure and maybe somehow retry what we were doing, but we can’t magically “go back” to where we were, and do something different.
But with algebraic effects,
we can
.
This is an example written in a hypothetical JavaScript dialect (let’s call it ES2025 just for kicks) that lets us
recover
from a missing
user.name
:
function
getName
(
user
)
{
let
name
=
user
.
name
;
if
(
name
===
null
)
{
name
=
perform
'
ask_name
'
;
}
return
name
;
}
function
makeFriends
(
user1
,
user2
)
{
user1
.
friendNames
.
push
(
getName
(
user2
));
user2
.
friendNames
.
push
(
getName
(
user1
));
}
const
arya
=
{
name
:
null
,
friendNames
:
[]
};
const
gendry
=
{
name
:
'
Gendry
'
,
friendNames
:
[]
};
try
{
makeFriends
(
arya
,
gendry
);
}
handle
(
effect
)
{
if
(
effect
===
'
ask_name
'
)
{
resume
with
'
Arya Stark
'
;
}
}
(I apologize to all readers from 2025 who search the web for “ES2025” and find this article. If algebraic effects are a part of JavaScript by then, I’d be happy to update it!)
Instead of
throw
, we use a hypothetical
perform
keyword. Similarly, instead of
try / catch
, we use a hypothetical
try / handle
.
The exact syntax doesn’t matter here — I just came up with something to illustrate the idea.
So what’s happening? Let’s take a closer look.
Instead of throwing an error, we
perform an effect
. Just like we can
throw
any value, we can pass any value to
perform
. In this example, I’m passing a string, but it could be an object, or any other data type:
function
getName
(
user
)
{
let
name
=
user
.
name
;
if
(
name
===
null
)
{
name
=
perform
'
ask_name
'
;
}
return
name
;
}
When we
throw
an error, the engine looks for the closest
try / catch
error handler up the call stack. Similarly, when we
perform
an effect, the engine would search for the closest
try / handle
effect handler
up the call stack:
try
{
makeFriends
(
arya
,
gendry
);
}
handle
(
effect
)
{
if
(
effect
===
'
ask_name
'
)
{
resume
with
'
Arya Stark
'
;
}
}
This effect lets us decide how to handle the case where a name is missing. The novel part here (compared to exceptions) is the hypothetical
resume with
:
try
{
makeFriends
(
arya
,
gendry
);
}
handle
(
effect
)
{
if
(
effect
===
'
ask_name
'
)
{
resume
with
'
Arya Stark
'
;
}
}
This is the part you can’t do with
try / catch
. It lets us
jump back to where we performed the effect, and pass something back to it from the handler
. 🤯
function
getName
(
user
)
{
let
name
=
user
.
name
;
if
(
name
===
null
)
{
// 1. We perform an effect here
name
=
perform
'
ask_name
'
;
// 4. ...and end up back here (name is now 'Arya Stark')
}
return
name
;
}
// ...
try
{
makeFriends
(
arya
,
gendry
);
}
handle
(
effect
)
{
// 2. We jump to the handler (like try/catch)
if
(
effect
===
'
ask_name
'
)
{
// 3. However, we can resume with a value (unlike try/catch!)
resume
with
'
Arya Stark
'
;
}
}
This takes a bit of time to get comfortable with, but it’s really not much different conceptually from a “resumable
try / catch
”.
Note, however, that
algebraic effects are much more flexible than
try / catch
, and recoverable errors are just one of many possible use cases.
I started with it only because I found it easiest to wrap my mind around it.
Algebraic effects have interesting implications for asynchronous code.
In languages with an
async / await
,
functions usually have a “color”
. For example, in JavaScript we can’t just make
getName
asynchronous without also “infecting”
makeFriends
and its callers with being
async
. This can be a real pain if
a piece of code sometimes needs to be sync, and sometimes needs to be async
.
// If we want to make this async...
async
getName
(
user
)
{
// ...
}
// Then this has to be async too...
async
function
makeFriends
(
user1
,
user2
)
{
user1
.
friendNames
.
push
(
await
getName
(
user2
));
user2
.
friendNames
.
push
(
await
getName
(
user1
));
}
// And so on...
JavaScript generators are
similar
: if you’re working with generators, things in the middle also have to be aware of generators.
So how is that relevant?
For a moment, let’s forget about
async / await
and get back to our example:
function
getName
(
user
)
{
let
name
=
user
.
name
;
if
(
name
===
null
)
{
name
=
perform
'
ask_name
'
;
}
return
name
;
}
function
makeFriends
(
user1
,
user2
)
{
user1
.
friendNames
.
push
(
getName
(
user2
));
user2
.
friendNames
.
push
(
getName
(
user1
));
}
const
arya
=
{
name
:
null
,
friendNames
:
[]
};
const
gendry
=
{
name
:
'
Gendry
'
,
friendNames
:
[]
};
try
{
makeFriends
(
arya
,
gendry
);
}
handle
(
effect
)
{
if
(
effect
===
'
ask_name
'
)
{
resume
with
'
Arya Stark
'
;
}
}
What if our effect handler didn’t know the “fallback name” synchronously? What if we wanted to fetch it from a database?
It turns out, we can call
resume with
asynchronously from our effect handler without making any changes to
getName
or
makeFriends
:
function
getName
(
user
)
{
let
name
=
user
.
name
;
if
(
name
===
null
)
{
name
=
perform
'
ask_name
'
;
}
return
name
;
}
function
makeFriends
(
user1
,
user2
)
{
user1
.
friendNames
.
push
(
getName
(
user2
));
user2
.
friendNames
.
push
(
getName
(
user1
));
}
const
arya
=
{
name
:
null
,
friendNames
:
[]
};
const
gendry
=
{
name
:
'
Gendry
'
,
friendNames
:
[]
};
try
{
makeFriends
(
arya
,
gendry
);
}
handle
(
effect
)
{
if
(
effect
===
'
ask_name
'
)
{
setTimeout
(()
=>
{
resume
with
'
Arya Stark
'
;
},
1000
);
}
}
In this example, we don’t call
resume with
until a second later. You can think of
resume with
as a callback which you may only call once. (You can also impress your friends by calling it a “one-shot delimited continuation.”)
Now the mechanics of algebraic effects should be a bit clearer. When we
throw
an error, the JavaScript engine “unwinds the stack”, destroying local variables in the process. However, when we
perform
an effect, our hypothetical engine would
create a callback
with the rest of our function, and
resume with
calls it.
Again, a reminder: the concrete syntax and specific keywords are made up for this article. They’re not the point, the point is in the mechanics.
It’s worth noting that algebraic effects came out of functional programming research. Some of the problems they solve are unique to pure functional programming. For example, in languages that
don’t
allow arbitrary side effects (like Haskell), you have to use concepts like Monads to wire effects through your program. If you ever read a Monad tutorial, you know they’re a bit tricky to think about. Algebraic effects help do something similar with less ceremony.
This is why so much discussion about algebraic effects is incomprehensible to me. (I
don’t know
Haskell and friends.) However, I do think that even in an impure language like JavaScript,
algebraic effects can be a very powerful instrument to separate the
what
from the
how
in the code.
They let you write code that focuses on
what
you’re doing:
function
enumerateFiles
(
dir
)
{
const
contents
=
perform
OpenDirectory
(
dir
);
perform
Log
(
'
Enumerating files in
'
,
dir
);
for
(
let
file
of
contents
.
files
)
{
perform
HandleFile
(
file
);
}
perform
Log
(
'
Enumerating subdirectories in
'
,
dir
);
for
(
let
directory
of
contents
.
dir
)
{
// We can use recursion or call other functions with effects
enumerateFiles
(
directory
);
}
perform
Log
(
'
Done
'
);
}
And later wrap it with something that specifies
how
:
let
files
=
[];
try
{
enumerateFiles
(
'
C:
\\
'
);
}
handle
(
effect
)
{
if
(
effect
instanceof
Log
)
{
myLoggingLibrary
.
log
(
effect
.
message
);
resume
;
}
else
if
(
effect
instanceof
OpenDirectory
)
{
myFileSystemImpl
.
openDir
(
effect
.
dirName
,
(
contents
)
=>
{
resume
with
contents
;
});
}
else
if
(
effect
instanceof
HandleFile
)
{
files
.
push
(
effect
.
fileName
);
resume
;
}
}
// The `files` array now has all the files
Which means that those pieces can even become librarified:
import
{
withMyLoggingLibrary
}
from
'
my-log
'
;
import
{
withMyFileSystem
}
from
'
my-fs
'
;
function
ourProgram
()
{
enumerateFiles
(
'
C:
\\
'
);
}
withMyLoggingLibrary
(()
=>
{
withMyFileSystem
(()
=>
{
ourProgram
();
});
});
Unlike
async / await
or Generators,
algebraic effects don’t require complicating functions “in the middle”
. Our
enumerateFiles
call could be deep within
ourProgram
, but as long as there’s an effect handler
somewhere above
for each of the effects it may perform, our code would still work.
Effect handlers let us decouple the program logic from its concrete effect implementations without too much ceremony or boilerplate code. For example, we could completely override the behavior in tests to use a fake filesystem and to snapshot logs instead of outputting them to the console:
import
{
withFakeFileSystem
}
from
'
fake-fs
'
;
function
withLogSnapshot
(
fn
)
{
let
logs
=
[];
try
{
fn
();
}
handle
(
effect
)
{
if
(
effect
instanceof
Log
)
{
logs
.
push
(
effect
.
message
);
resume
;
}
}
// Snapshot emitted logs.
expect
(
logs
).
toMatchSnapshot
();
}
test
(
'
my program
'
,
()
=>
{
const
fakeFiles
=
[
/* ... */
];
withFakeFileSystem
(
fakeFiles
,
()
=>
{
withLogSnapshot
(()
=>
{
ourProgram
();
});
});
});
Because there is no
“function color”
(code in the middle doesn’t need to be aware of effects) and effect handlers are
composable
(you can nest them), you can create very expressive abstractions with them.
Because algebraic effects are coming from statically typed languages, much of the debate about them centers on the ways they can be expressed in types. This is no doubt important but can also make it challenging to grasp the concept. That’s why this article doesn’t talk about types at all. However, I should note that usually the fact that a function can perform an effect would be encoded into its type signature. So you shouldn’t end up in a situation where random effects are happening and you can’t trace where they’re coming from.
You might argue that algebraic effects technically do
“give color”
to functions in statically typed languages because effects are a part of the type signature. That’s true. However, fixing a type annotation for an intermediate function to include a new effect is not by itself a semantic change — unlike adding
async
or turning a function into a generator. Inference can also help avoid cascading changes. An important difference is you can “bottle up” an effect by providing a noop or a mock implementation (for example, a sync call for an async effect), which lets you prevent it from reaching the outer code if necessary — or turn it into a different effect.
Honestly, I don’t know. They are very powerful, and you can make an argument that they might be
too
powerful for a language like JavaScript.
I think they could be a great fit for a language where mutation is uncommon, and where the standard library fully embraced effects. If you primarily do
perform Timeout(1000)
,
perform Fetch('http://google.com')
, and
perform ReadFile('file.txt')
, and your language has pattern matching and static typing for effects, it might be a very nice programming environment.
Maybe that language could even compile to JavaScript!
Not that much. You can even say it’s a stretch.
If you watched
my talk about Time Slicing and Suspense
, the second part involves components reading data from a cache:
function
MovieDetails
(
{ id }
)
{
// What if it's still being fetched?
const
movie
=
movieCache
.
read
(
id
);
}
(The talk uses a slightly different API but that’s not the point.)
This builds on a React feature called “Suspense”, which is in active development for the data fetching use case. The interesting part, of course, is that the data might not yet be in the
movieCache
— in which case we need to do
something
because we can’t proceed below. Technically, in that case the
read()
call throws a Promise (yes,
throws
a Promise — let that sink in). This “suspends” the execution. React catches that Promise, and remembers to retry rendering the component tree after the thrown Promise resolves.
This isn’t an algebraic effect per se, even though this trick was
inspired
by them. But it achieves the same goal: some code below in the call stack yields to something above in the call stack (React, in this case) without all the intermediate functions necessarily knowing about it or being “poisoned” by
async
or generators. Of course, we can’t really
resume
execution in JavaScript later, but from React’s point of view, re-rendering a component tree when the Promise resolves is pretty much the same thing. You can cheat when your programming model
assumes idempotence
!
Hooks
are another example that might remind you of algebraic effects. One of the first questions that people ask is: how can a
useState
call possibly know which component it refers to?
function
LikeButton
()
{
// How does useState know which component it's in?
const [
isLiked
,
setIsLiked
]
=
useState
(
false
);
}
I already explained the answer
near the end of this article
: there is a “current dispatcher” mutable state on the React object which points to the implementation you’re using right now (such as the one in
react-dom
). There is similarly a “current component” property that points to our
LikeButton
’s internal data structure. That’s how
useState
knows what to do.
Before people get used to it, they often think it’s a bit “dirty” for an obvious reason. It doesn’t “feel right” to rely on shared mutable state.
(Side note: how do you think
try / catch
is implemented in a JavaScript engine?)
However, conceptually you can think of
useState()
as of being a
perform State()
effect which is handled by React when executing your component. That would “explain” why React (the thing calling your component) can provide state to it (it’s above in the call stack, so it can provide the effect handler). Indeed,
implementing state
is one of the most common examples in the algebraic effect tutorials I’ve encountered.
Again, of course, that’s not how React
actually
works because we don’t have algebraic effects in JavaScript. Instead, there is a hidden field where we keep the current component, as well as a field that points to the current “dispatcher” with the
useState
implementation. As a performance optimization, there are even separate
useState
implementations
for mounts and updates
. But if you squint at this code very hard, you might see them as essentially effect handlers.
To sum up, in JavaScript, throwing can serve as a crude approximation for IO effects (as long as it’s safe to re-execute the code later, and as long as it’s not CPU-bound), and having a mutable “dispatcher” field that’s restored in
try / finally
can serve as a crude approximation for synchronous effect handlers.
You can also get a much higher fidelity effect implementation
with generators
but that means you’ll have to give up on the “transparent” nature of JavaScript functions and you’ll have to make everything a generator. Which is… yeah.
Personally, I was surprised by how much algebraic effects made sense to me. I always struggled understanding abstract concepts like Monads, but Algebraic Effects just “clicked”. I hope this article will help them “click” for you too.
I don’t know if they’re ever going to reach mainstream adoption. I think I’ll be disappointed if they don’t catch on in any mainstream language by 2025. Remind me to check back in five years!
I’m sure there’s so much more you can do with them — but it’s really difficult to get a sense of their power without actually writing code this way. If this post made you curious, here’s a few more resources you might want to check out:
Many people also pointed out that if you omit the typing aspects (as I did in this article), you can find much earlier prior art for this in the
condition system
in Common Lisp. You might also enjoy reading James Long’s
post on continuations
that explains how the
call/cc
primitive can also serve as a foundation for building resumable exceptions in userland.
If you find other useful resources on algebraic effects for people with JavaScript background, please let me know on Twitter!
