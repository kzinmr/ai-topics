---
title: "Why Do React Elements Have a $$typeof Property?"
url: "https://overreacted.io/why-do-react-elements-have-typeof-property/"
fetched_at: 2026-04-28T07:02:40.167624+00:00
source: "overreacted.io"
tags: [blog, raw]
---

# Why Do React Elements Have a $$typeof Property?

Source: https://overreacted.io/why-do-react-elements-have-typeof-property/

You might think you’re writing JSX:
<
marquee
bgcolor=
"
#ffa7c4
"
>
hi
</
marquee
>
But really, you’re calling a function:
React
.
createElement
(
/* type */
'
marquee
'
,
/* props */
{
bgcolor
:
'
#ffa7c4
'
},
/* children */
'
hi
'
)
And that function gives you back an object. We call this object a React
element
. It tells React what to render next. Your components return a tree of them.
{
type:
'
marquee
'
,
props:
{
bgcolor:
'
#ffa7c4
'
,
children:
'
hi
'
,
},
key:
null
,
ref:
null
,
$$typeof:
Symbol
.
for
(
'
react.element
'
),
// 🧐 Who dis
}
If you used React you might be familiar with
type
,
props
,
key
, and
ref
fields.
But what is
$$typeof
? And why does it have a
Symbol()
as a value?
That’s another one of those things that you don’t
need
to know to use React, but that will make you feel good when you do. There’s also some tips about security in this post that you might want to know. Maybe one day you’ll write your own UI library and all of this will come in handy. I certainly hope so.
Before client-side UI libraries became common and added basic protection, it was common for app code to construct HTML and insert it into the DOM:
const
messageEl
=
document
.
getElementById
(
'
message
'
);
messageEl
.
innerHTML
=
'
<p>
'
+
message
.
text
+
'
</p>
'
;
That works fine, except when your
message.text
is something like
'<img src onerror="stealYourPassword()">'
.
You don’t want things written by strangers to appear verbatim in your app’s rendered HTML.
(Fun fact: if you only do client-side rendering, a
<script>
tag here wouldn’t let you run JavaScript. But
don’t let this
lull you into a false sense of security.)
To protect against such attacks, you can use safe APIs like
document.createTextNode()
or
textContent
that only deal with text. You can also preemptively “escape” inputs by replacing potentially dangerous characters like
<
,
>
and others in any user-provided text.
Still, the cost of a mistake is high and it’s a hassle to remember it every time you interpolate a user-written string into your output.
This is why modern libraries like React escape text content for strings by default:
<
p
>
{
message
.
text
}
</
p
>
If
message.text
is a malicious string with an
<img>
or another tag, it won’t turn into a real
<img>
tag. React will escape the content and
then
insert it into the DOM. So instead of seeing the
<img>
tag you’ll just see its markup.
To render arbitrary HTML inside a React element, you have to write
dangerouslySetInnerHTML={{ __html: message.text }}
.
The fact that it’s clumsy to write is a
feature
.
It’s meant to be highly visible so that you can catch it in code reviews and codebase audits.
Does it mean React is entirely safe from injection attacks? No.
HTML and DOM offer
plenty of attack surface
that is too difficult or slow for React or other UI libraries to mitigate against. Most of the remaining attack vectors involve attributes. For example, if you render
<a href={user.website}>
, beware of the user whose website is
'javascript: stealYourPassword()'
. Spreading user input like
<div {...userData}>
is rare but also dangerous.
React
could
provide more protection over time but in many cases these are consequences of server issues that
should
be fixed there anyway.
Still, escaping text content is a reasonable first line of defence that catches a lot of potential attacks. Isn’t it nice to know that code like this is safe?
// Escaped automatically
<
p
>
{
message
.
text
}
</
p
>
Well, that wasn’t always true either.
And that’s where
$$typeof
comes in.
React elements are plain objects by design:
{
type:
'
marquee
'
,
props:
{
bgcolor:
'
#ffa7c4
'
,
children:
'
hi
'
,
},
key:
null
,
ref:
null
,
$$typeof:
Symbol
.
for
(
'
react.element
'
),
}
While normally you create them with
React.createElement()
, it is not required. There are valid use cases for React to support plain element objects written like I just did above. Of course, you probably wouldn’t
want
to write them like this — but this
can be
useful for an optimizing compiler, passing UI elements between workers, or for decoupling JSX from the React package.
However,
if your server has a hole that lets the user store an arbitrary JSON object
while the client code expects a string, this could become a problem:
// Server could have a hole that lets user store JSON
let
expectedTextButGotJSON
=
{
type
:
'
div
'
,
props
:
{
dangerouslySetInnerHTML
:
{
__html
:
'
/* put your exploit here */
'
},
},
// ...
};
let
message
=
{
text
:
expectedTextButGotJSON
};
// Dangerous in React 0.13
<
p
>
{
message
.
text
}
</
p
>
In that case, React 0.13 would be
vulnerable
to an XSS attack. To clarify, again,
this attack depends on an existing server hole
. Still, React could do a better job of protecting people against it. And starting with React 0.14, it does.
The fix in React 0.14 was to
tag every React element with a Symbol
:
{
type:
'
marquee
'
,
props:
{
bgcolor:
'
#ffa7c4
'
,
children:
'
hi
'
,
},
key:
null
,
ref:
null
,
$$typeof:
Symbol
.
for
(
'
react.element
'
),
}
This works because you can’t just put
Symbol
s in JSON.
So even if the server has a security hole and returns JSON instead of text, that JSON can’t include
Symbol.for('react.element')
.
React will check
element.$$typeof
, and will refuse to process the element if it’s missing or invalid.
The nice thing about using
Symbol.for()
specifically is that
Symbols are global between environments like iframes and workers.
So this fix doesn’t prevent passing trusted elements between different parts of the app even in more exotic conditions. Similarly, even if there are multiple copies of React on the page, they can still “agree” on the valid
$$typeof
value.
What about the browsers that
don’t support
Symbols?
Alas, they don’t get this extra protection. React still includes the
$$typeof
field on the element for consistency, but it’s
set to a number
—
0xeac7
.
Why this number specifically?
0xeac7
kinda looks like “React”.
