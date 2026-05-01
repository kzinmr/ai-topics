---
title: "In search for a good Markdown editor for my blogging platform"
url: "https://rakhim.exotext.com/markdown-editor-for-exotext"
fetched_at: 2026-05-01T07:01:23.714063+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# In search for a good Markdown editor for my blogging platform

Source: https://rakhim.exotext.com/markdown-editor-for-exotext

I don't envy beginners trying to get into web development today.
I haven't been doing any frontend web development for more than a decade. Today I was trying to do a simple thing: get a JS markdown editor to work in the browser. Found this beautiful looking library called
Tiptap
. This
example
seems great! Let's try to integrate it.
What I naively expected:
<
script
src
=
"some_cdn_url.js"
>
<
div
id
=
"editor"
>
</
div
>
What happened:
There's a
documentation page
for using TipTap with "vanilla javascript". Sounds good! It starts with:
npm install @tiptap/core @tiptap/pm @tiptap/starter-kit
Wait, what?
npm
is a Node package manager, right? Then it goes to:
import
{
Editor
}
from
'@tiptap/core'
import
StarterKit
from
'@tiptap/starter-kit'
new
Editor
({
element
:
document
.
querySelector
(
'.element'
),
extensions
: [
StarterKit
],
content
:
'<p>Hello World!</p>'
,
})
Hmm... I guess this is Vanilla JS, since
<script type="module">
should be
working
in latest browsers. But... what? Do web developers today mean "Node" when they say "Vanilla JavaScript"?
(I also have seen people saying "without a framework" when using plain React... yeah.)
There's a confusing
github thread
with people seemingly not understanding each other, and a strong "kids nowadays" vibes from one of the participants. Someone did produce a working example of truly Vanilla JS use
here
. It works! But wait again... There's like 50 lines of JS to make the "bold" button work.
Anyway, turns out TipTap does not support Markdown output natively. So, I've looked around more.
SimpleMDE
looks alright, but seems like the development stopped about 8 years ago. Based on Codemirror.
EasyMDE
is a fork of SimpleMDE. Lots of features, and looks pretty good.
Trix
is cool, and I've used it in the past for another project, but it's a rich-text editor without any markdown support. From the creators or Rails.
DHH said
they will soon release their new markdown editor called House, I'm looking forward to trying it.
Prosemirror
is also designed primarily for rich text, but is very flexible. It's more of a framework for building editors.
Remirror
is based on Prosemirror, but can only be used with React.
ByteMD
has some nice features and integrations.
EditorJS
is a block-based editor (similar to Notion), but I for some reason really dislike this concept.
MDXEditor
has some strange design decisions. For example, fenced code blocks don't seem to work by default.
CKEditor
has markdown support, but seems a bit too complicated for my use case.
Toast
is alright.
Milkdown
is not meant to be used outside of frameworks like React or Vue.
There's a bunch more, but most of them have one or more deal-breakers:
Funky WYSIWYG
React or other framework required
Complex structure, difficult to customize without learning all the layers and architecture
For now, I settled on using Codemirror. SimpleMDE and EasyMDE are good wrappers on top of Codemirror, but Codemirror is so straight-forward to work with that I'd rather write my own code to do things like inserting links, bold/italic triggers, image uploads, etc.
I'm writing this post in the new editor. Here's a cat portrait I took in Georgia a few years ago (just to test the image uploading!):
