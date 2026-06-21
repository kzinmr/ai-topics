---
title: "Which Copyleft Licence is Suitable for an SVG?"
url: "https://shkspr.mobi/blog/2026/06/which-copyleft-licence-is-suitable-for-an-svg/"
fetched_at: 2026-06-21T07:00:49.670917+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Which Copyleft Licence is Suitable for an SVG?

Source: https://shkspr.mobi/blog/2026/06/which-copyleft-licence-is-suitable-for-an-svg/

The Scalable Vector Graphics (SVG) format is amazing. It allows you to precisely define how an image should look. Written in XML, it uses various mathematical operations to display an image which looks crisp and clear at any size.
Here's a trivial example:
⧉
SVG
<
svg
height
="100"
viewBox
="0 0 100 100"
width
="100"
xmlns
="http://www.w3.org/2000/svg">
   <
circle
cx
="50"
cy
="50"
fill
="#fff"
r
="100"/>
</
svg
>
That code produces this circle:
You could print that out with a kilometre radius and it would still be a perfect circle - unlike a traditional raster image which is just a grid of blocky pixels.
But suppose you wanted to freely share your SVG with others - and ensure that they
also
freely share it. What sort of "Copyleft" licence would you give it?
The obvious choice seems to be a Creative Commons Share-Alike licence. SVGs are images. Images are creative works. Creative Commons is suitable for creative works. Job done!
But…
SVGs are
not
images. The are code which
produce
images. If we assume that an SVG is software, this entry in the FAQ becomes relevant:
Can I apply a Creative Commons license to software?
We recommend against using Creative Commons licenses for software.
[…]
Unlike software-specific licenses, CC licenses do not contain specific terms about the distribution of source code, which is often important to ensuring the free reuse and modifiability of software.
[…]
Additionally, our licenses are currently not compatible with the major software licenses, so it would be difficult to integrate CC-licensed work with other free software. Existing software licenses were designed specifically for use with software and offer a similar set of rights to the Creative Commons licenses.
At the end of that FAQ, they also say:
While we recommend against using a CC license on software itself, CC licenses may be used for software documentation, as well as for separate artistic elements such as game art or music.
So, that's a
perhaps?
But let us assume that an SVG is a piece of media rather than software. Would it be suitable to use a software licence for it?
The various Gnu Public Licences have this to say:
Can I use the GPL for something other than software?
You can apply the GPL to any kind of work, as long as it is clear what constitutes the “source code” for the work. The GPL defines this as the preferred form of the work for making changes in it.
A photo JPEG might be derived from the RAW image file. In which case, the RAW is suitable for being GPL'd, not the resultant JPEG.
Similarly, the Photoshop file of a complex and multi-layered illustration would suitable, but not the outputted PNG.
An SVG can straddle both worlds.  It's possible to build an SVG with layers, groups, and transformations, and then simplify it for output. You
could
edit the optimised version, but it's hardly the preferred format.
I read
the GPL
(so you don't have to) and right at the start it says:
The GNU General Public License is a free, copyleft license for software and
other kinds of works
.
(Emphasis added.)
But do they mean that?
Licenses for Other Types of Works
[…]
We don't take the position that artistic or entertainment works must be free, but if you want to make one free, we recommend the
Free Art License
.
But, as delightful as the Free Art License is, the FSF say:
Please don't use it for software or documentation, since it is incompatible with the GNU GPL and with the GNU FDL.
I think so.
It's written in plain text.
It contains definitions, variables, and instructions.
It can contain scripting.
That sure looks like software to me!
But, at the same time, the user
experiences
it as a graphic. An animated GIF, for example, contains a small amount of code-like data to say how long each frame should last for and when to stop running. Is a GIF software? Is the basic circle above software? How much code do you need before something becomes software?
Licences like the
LGPL
and
MPL
allow copyleft libraries to be integrated into non-free software.
A proprietary application could treat an SVG as a library by asking the SVG to render the output and then displaying that. A bit of a reach, perhaps?
Just to complicate things, an SVG can
also
contain raster graphics. That is, it is possible to embed a PNG, JPEG, or any other traditional image within an SVG.
In this case, the embedded image
can
be Creative Commons licenced because
CC BY-SA is compatible with GPLv3
.
When someone creates an adaptation of a BY-SA licensed work and includes it in a GPLv3-licensed project, both licenses apply and downstream users must comply with both licenses. However, Section 2(a)(5)(B) of BY-SA 4.0 allows anyone who receives the adapted material downstream to satisfy the conditions of both BY-SA and GPLv3 (i.e. attribution and ShareAlike)
in the manner dictated by the GPLv3
.
(Emphasis added.)
The barest of SVGs containing only an embedded image probably wouldn't count as software. But what if you started applying programmatic transformations to them? This SVG embeds an image and uses software to rotate it upside down.
⧉
SVG
<
svg
version
="1.1"
xmlns
="http://www.w3.org/2000/svg"
xmlns:xlink
="http://www.w3.org/1999/xlink"
width
="64"
height
="64">
  <
image
x
="0"
y
="0"
width
="64"
height
="64"
transform
="rotate(180)"
href
="data:image/png;base64,iVB…" />
</
svg
>
Is that enough code to count as software?
I conducted a rigorously accurate public survey. Here are the results:
Post by @Edent@mastodon.social
View on Mastodon
Personally, I think SVGs
are
software. I understand the argument that they're suitable for Creative Commons, but I disagree with it. Even the simplest SVG is distributed in a way that its contents are
executed
by the computer.
While SVGs may be minified and stripped of comments, they still retain the essence of source code. I suppose you could
try
to obfuscate them, or package them up in a quasi-binary form, but I maintain the source is still viewable and editable.
If you choose to use a Creative Commons Share-Alike licence, it probably won't cause any harm. But given CC's reluctance to endorse its use on software, it probably makes sense to use a copyleft source-code licence.
