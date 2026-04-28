---
title: "How to generate OpenGraph images with Astro and Satori"
url: "https://mahadk.com/posts/astro-og-with-satori/"
fetched_at: 2026-04-28T07:01:55.645886+00:00
source: "skyfall.dev"
tags: [blog, raw]
---

# How to generate OpenGraph images with Astro and Satori

Source: https://mahadk.com/posts/astro-og-with-satori/

When you share a link on social media, you want it to stand out. That’s where OpenGraph (OG) images come in - they’re
the eye-catching previews that automatically appear when your content is shared on platforms like Twitter/X, Facebook,
or Discord.
OG images aren’t just for show however - they’re
incredibly
powerful for boosting engagement. Research have shown that
content with
custom OpenGraph images attracts 2.3x more clicks
compared to plain links, making them a great way to increase
engagement and drive traffic to your site.
The problem is that making these images manually can be tedious, especially for sites with lots of content.
In this post, I’ll show you how to automatically create beautiful OpenGraph images for your Astro site using Satori,
a library that makes it easy to generate images using React or Preact components. By the end of this tutorial, you’ll have:
Automatic OG image generation for all your blog posts
A reusable template that maintains your brand identity
Better-looking link previews across all social platforms
Installing dependencies
We’ll first need to download the dependencies we need. I’ll be using Preact in this tutorial, but React works too
(albeit with a few minor changes in the imports and types). We’ll also need to install Satori.
npm
install
preact
# or `npm install react`
If you’re going to use Tailwind to make your OG images, and want to use the same Tailwind config,
you’ll also want to use the
tw-to-css
library. I talk more about this in
my blog post on using
Satori with your project’s Tailwind config.
Satori outputs SVGs, which are unfortunately not supported by OpenGraph, so we’ll also need to install
the
sharp
library to convert SVGs to PNGs.
Generating the image
Creating an OG image component
First, let’s create an
OpenGraphImage
component, which will be responsible for rendering the actual content of the OG image. Here’s an example:
// e.g. src/components/og/image.tsx
import
{
type
CollectionEntry
}
from
"astro:content"
;
export
default
function
(
props
:
CollectionEntry
<
"
blog
"
>
)
{
<
div
tw
=
"flex flex-col w-full h-full p-12 items-center text-center justify-center text-white bg-indigo-500"
>
<
h1
tw
=
"flex font-bold text-8xl mb-4"
>
{
props
.
data
.
title
}
</
h1
>
<
p
tw
=
"flex text-5xl mb-12"
>
{
props
.
data
.
description
}
</
p
>
Note that the above code assumes that you have a
blog
collection, with each post having a
title
and
description
field. If you’re using a different collection, you’ll need to adjust the code accordingly.
Setting up the API endpoint
Assuming that your file structure looks something like this:
You’ll want to move the
[id].astro
file to a new
[id]
folder, rename it to
index.astro
, then add a new
og.png.ts
file in that new folder. Here’s how it should look:
This will create a new endpoint at
/blog/[id]/og.png
. Now, let’s set it up:
import
fs
from
"fs/promises"
;
import
satori
from
"satori"
;
import
sharp
from
"sharp"
;
import
{
getCollection
}
from
"astro:content"
;
import
type
{
InferGetStaticParamsType
}
from
"astro"
;
import
OpenGraphImage
from
"path/to/your/og/image/component"
;
const
posts
=
await
getCollection
(
"blog"
)
;
type
Params
=
InferGetStaticParamsType
<
typeof
getStaticPaths
>
;
export
async
function
GET
({
params
}
:
{
params
:
Params
})
{
const
post
=
posts
.
find
(
(
post
)
=>
post
.
id
===
params
.
id)
;
// Find the specific post by ID
return
new
Response
(
"Post not found"
,
{
status
:
404
}
)
;
const
element
=
OpenGraphImage
(post)
;
const
png
=
await
PNG
(element)
;
return
new
Response
(png
,
{
"Content-Type"
:
"image/png"
,
export
async
function
getStaticPaths
()
{
return
posts
.
map
(
(
post
)
=>
(
{
Here, we’re adding a
GET
API endpoint at
/blog/[id]/og.png
, which will return the image for the
post with the ID of
[id]
. We’re also importing the
OpenGraphImage
component from the path you provided,
and the posts from the
blog
collection.
Now, let’s define the
PNG
and
SVG
functions, which will generate the PNG and SVG images respectively:
export
async
function
SVG
(
component
:
h
.
JSX
.
Element
)
{
return
await
satori
(component
as
any
,
{
data
:
await
fs
.
readFile
(
"./src/assets/fonts/og/Outfit-Regular.ttf"
)
,
export
async
function
PNG
(
component
:
h
.
JSX
.
Element
)
{
return
await
sharp
(Buffer
.
from
(
await
SVG
(component)))
NOTE
If your route param isn’t called
id
, you’ll need to change the references to
id
to match your route param.
We’re setting the image size to
1200x630
, which is the recommended size for OG images,
and ensures your images look good on most platforms, like Twitter/X, Facebook, and Discord.
You probably also noticed the
fonts
array we’re passing to
satori
, which, well,
defines the fonts you’re going to be using in your image! I’ve used the
Outfit
font here, but feel free to pick your own from places like
Google Fonts.
Note that the relative paths are relative
to the root directory of your project.
WARNING
You might run into issues with variable font weights. This is due to
a bug
in Satori
, which causes errors
when using variable font weights. To fix this, you’ll need to use a fixed
font weight instead.
Using the OG images
Phew, that’s the hard part done! Finally, let’s add the OG image to our posts.
Here’s an example. First, let’s pass a
ogImage
prop to our
BlogPost
layout, which will use
our new API endpoint to generate the image for the post.
import
{
type
CollectionEntry
,
getCollection
,
render
}
from
"astro:content"
;
import
BlogPost
from
"@layouts/blogpost.astro"
;
export
async
function
getStaticPaths
()
{
const
posts
=
await
getCollection
(
"blog"
)
;
return
posts
.
map
(
(
post
)
=>
(
{
type
Props
=
CollectionEntry
<
"
blog
"
>
;
const
post
=
Astro
.
props
;
const
{
Content
}
=
await
render
(post)
;
<
BlogPost
{
...
post
.
data}
ogImage
=
`
${
Astro
.
site
}
/posts/
${
post
.
id
}
/og.png`
>
Note the usage of
Astro.site
here - the OG image URL needs to be an absolute URL, so we’re using
the
Astro.site
variable to get the base URL of our site.
Now, let’s use the
ogImage
prop in our
BlogPost
layout, which will pass in the image URL to the
root
Layout
.
import
type
{
CollectionEntry
}
from
"astro:content"
;
import
Layout
from
"./layout.astro"
;
type
Props
=
CollectionEntry
<
"
blog
"
>
[
"
data
"
]
&
{
const
{
title
,
description
,
ogImage
}
=
Astro
.
props
;
<
Layout
title
=
{
title
}
description
=
{
description
}
ogImage
=
{
ogImage
}
>
And finally, let’s use the
ogImage
prop in our main layout, by adding a
meta
tag to the
<head>
with the image URL. We’ll also set the
twitter:card
properties to
summary_large_image
, so our image
can be shown in full size.
const
{
title
,
description
,
ogImage
}
=
Astro
.
props
;
<
meta
name
=
"viewport"
content
=
"width=device-width, initial-scale=1.0"
/>
{
ogImage
&&
<
meta
property
=
"og:image"
content
=
{
ogImage
}
/>
}
content
=
{
ogImage
?
"summary_large_image"
:
"summary"
}
And that’s it! You should now have an OG image for your blog posts! Here’s an example of what my
blog’s OG images look like:
