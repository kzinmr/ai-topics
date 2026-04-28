---
title: "How to use Satori with your Tailwind config"
url: "https://mahadk.com/posts/satori-with-tailwind-config/"
fetched_at: 2026-04-28T07:01:55.599973+00:00
source: "skyfall.dev"
tags: [blog, raw]
---

# How to use Satori with your Tailwind config

Source: https://mahadk.com/posts/satori-with-tailwind-config/

Satori
is an easy to use library that lets you generate an SVG file using React (or Preact)! In my opinion, it’s
the
nicest way to generate images.
Satori also comes with Tailwind support by default, but there’s a catch - it doesn’t work with your Tailwind config out-of-the-box. In this blog post, I’ll be showing you how to get Satori to work with your Tailwind config!
Installing dependencies
We’ll first need to download the dependencies we need. I’ll be using Preact in this tutorial, but React works too (albeit with a few minor changes in the imports and types)
npm
install
preact
# or `npm install react`
We’ll also need the
tw-to-css
library, which’ll convert our Tailwind classes into a
style
prop that Satori can render.
The Code
First, let’s import the things we’ll be using:
import
{
tailwindToCSS
,
type
TailwindConfig
}
from
"tw-to-css"
;
import
{
cloneElement
,
isValidElement
,
type
h
}
from
"preact"
;
import
{
Children
}
from
"preact/compat"
;
We then need to get a
twj
function (Tailwind to JSON); we’ll use it to convert our Tailwind classes into an object of inline styles that the
style
prop will use:
const
{
twj
}
=
tailwindToCSS
(
{
config
:
(
await
import
(
"../tailwind.config.mjs"
))
.
default
as
TailwindConfig
,
Make sure to replace the path above with the path to your Tailwind config!
Now, let’s define an
inlineTailwind
function that’ll convert the Tailwind classes into inline styles:
function
inlineTailwind
(
el
:
h
.
JSX
.
Element
)
:
h
.
JSX
.
Element
{
const
{
tw
,
children
,
style
:
originalStyle
,
...
props
}
=
el
.
props
;
// Generate style from the `tw` prop
const
twStyle
=
tw
?
twj
(tw
.
split
(
" "
))
:
{};
// Merge original and generated styles
const
mergedStyle
=
{
...
originalStyle
,
...
twStyle
};
// Recursively process children
const
processedChildren
=
Children
.
map
(children
,
(
child
)
=>
isValidElement
(child)
?
inlineTailwind
(child
as
h
.
JSX
.
Element
)
:
child
,
// Return cloned element with updated props
return
cloneElement
(el
,
{
...
props
,
style
:
mergedStyle
},
processedChildren)
;
And you’re done! Here’s an example of how you can use this function:
return
<
div
tw
=
"flex bg-base"
>
Hi there! 👋
</
div
>
;
const
element
=
Component
()
;
const
jsx
=
inlineTailwind
(element)
;
const
svg
=
await
satori
(jsx
,
{
// ... any other satori options
Thanks to
this issue on GitHub
for parts of the code!
