---
title: "Some notes on upgrading Hugo"
url: "https://jvns.ca/blog/2024/10/07/some-notes-on-upgrading-hugo/"
fetched_at: 2026-05-05T07:01:47.130867+00:00
source: "Julia Evans (jvns)"
tags: [blog, raw]
---

# Some notes on upgrading Hugo

Source: https://jvns.ca/blog/2024/10/07/some-notes-on-upgrading-hugo/

Warning: this is a post about very boring yakshaving, probably only of interest
to people who are trying to upgrade Hugo from a very old version to a new
version. But what are blogs for if not documenting one’s very boring yakshaves
from time to time?
So yesterday I decided to try to upgrade Hugo. There’s no real reason to do
this – I’ve been using Hugo version 0.40 to generate this blog since 2018, it
works fine, and I don’t have any problems with it. But I thought – maybe it
won’t be as hard as I think, and I kind of like a tedious computer task sometimes!
I thought I’d document what I learned along the way in case it’s useful to
anyone else doing this very specific migration. I upgraded from Hugo v0.40
(from 2018) to v0.135 (from 2024).
Here are most of the changes I had to make:
I had to replace a bunch of instances of
{{ template "theme/partials/header.html" . }}
with
{{ partial "header.html" . }}
.
This happened in
v0.42
:
We have now virtualized the filesystems for project and theme files. This
makes everything simpler, faster and more powerful. But it also means that
template lookups on the form {{ template “theme/partials/pagination.html” .
}} will not work anymore. That syntax has never been documented, so it’s not
expected to be in wide use.
This seems to be discussed in the
release notes for 0.57.2
I just needed to replace
.Data.Pages
with
site.RegularPages
in the template on the homepage as well as in my RSS feed template.
I had this comment in the part of my theme where I link to the next/previous blog post:
“next” and “previous” in hugo apparently mean the opposite of what I’d think
they’d mean intuitively. I’d expect “next” to mean “in the future” and
“previous” to mean “in the past” but it’s the opposite
It looks they changed this in
ad705aac064
so that “next” actually is in the future and “prev” actually is in the past. I
definitely find the new behaviour more intuitive.
Figuring out why/when all of these changes happened was a little difficult. I
ended up hacking together a bash script to
download all of the changelogs from github as text files
, which I
could then grep to try to figure out what happened. It turns out it’s pretty
easy to get all of the changelogs from the GitHub API.
So far everything was not so bad – there was also a change around taxonomies
that’s I can’t quite explain, but it was all pretty manageable, but then we got
to the really tough one: the markdown renderer.
The blackfriday markdown renderer (which was previously the default) was removed in
v0.100.0
. This seems pretty reasonable:
It has been deprecated for a long time, its v1 version is not maintained
anymore, and there are many known issues. Goldmark should be a mature
replacement by now.
Fixing all my Markdown changes was a huge pain – I ended up having to update
80 different Markdown files (out of 700) so that they would render properly, and I’m not totally sure
The obvious question here is – why bother even trying to upgrade Hugo at all
if I have to switch Markdown renderers?
My old site was running totally fine and I think it wasn’t necessarily a
good
use of time, but the one reason I think it might be useful in the future is
that the new renderer (goldmark) uses the
CommonMark markdown standard
, which I’m hoping will be somewhat
more futureproof. So maybe I won’t have to go through this again? We’ll see.
Also it turned out that the new Goldmark renderer does fix some problems I had
(but didn’t know that I had) with smart quotes and how lists/blockquotes
interact.
The hard part of this Markdown change was even figuring out what changed.
Almost all of the problems (including #2 and #3 above) just silently broke the
site, they didn’t cause any errors or anything. So I had to diff the HTML to
hunt them down.
Here’s what I ended up doing:
Generate the site with the old version, put it in
public_old
Generate the new version, put it in
public
Diff every single HTML file in
public/
and
public_old
with
this diff.sh script
and put the results in a
diffs/
folder
Run variations on
find diffs -type f | xargs cat | grep -C 5 '(31m|32m)' | less -r
over and over again to look at every single change until I found something that seemed wrong
Update the Markdown to fix the problem
Repeat until everything seemed okay
(the
grep 31m|32m
thing is searching for red/green text in the diff)
This was very time consuming but it was a little bit fun for some reason so I
kept doing it until it seemed like nothing too horrible was left.
Here’s a list of every type of Markdown change I had to make. It’s very
possible these are all extremely specific to me but it took me a long time to
figure them all out so maybe this will be helpful to one other person who finds
this in the future.
This doesn’t work anymore (it doesn’t expand the link):
<small>
[a link](https://example.com)
</small>
I need to do this instead:
<small>

[a link](https://example.com)

</small>
This works too:
<small> [a link](https://example.com) </small>
I didn’t want this so I needed to configure:
markup:
  goldmark:
    extensions:
      typographer:
        leftAngleQuote: '&lt;&lt;'
        rightAngleQuote: '&gt;&gt;'
This doesn’t render as a nested list anymore if I only indent by 2 spaces, I need to put 4 spaces.
1. a
  * b
  * c
2. b
The problem is that the amount of indent needed depends on the size of the list
markers.
Here’s a reference in CommonMark for this
.
Previously the
> quote
here didn’t render as a blockquote, and with the new renderer it does.
* something
> quote
* something else
I found a bunch of Markdown that had been kind of broken (which I hadn’t
noticed) that works better with the new renderer, and this is an example of
that.
Lists inside blockquotes also seem to work better.
Previously this didn’t render as a heading, but now it does. So I needed to
replace the
#
with
&num;
.
* # passengers: 20
I had something which looked like this:
`1 / (1
+ exp(-1)) = 0.73`
With Blackfriday it rendered like this:
<p><code>1 / (1
+ exp(-1)) = 0.73</code></p>
and with Goldmark it rendered like this:
<p>`1 / (1</p>
<ul>
<li>exp(-1)) = 0.73`</li>
</ul>
Same thing if there was an accidental
1)
at the beginning of a line, like in this Markdown snippet
I set up a small Hadoop cluster (1 master, 2 workers, replication set to 
1) on
To fix this I just had to rewrap the line so that the
+
wasn’t the first character.
The Markdown is formatted this way because I wrap my Markdown to 80 characters
a lot and the wrapping isn’t very context sensitive.
There were a bunch of places where the old renderer (Blackfriday) was doing
unwanted things in code blocks like replacing
...
with
…
or replacing
quotes with smart quotes. I hadn’t realized this was happening and I was very
happy to have it fixed.
The way this gets rendered got better:
"Oh, *interesting*!"
old: “Oh,
interesting
!“
new: “Oh,
interesting
!”
Before there were two left smart quotes, now the quotes match.
Previously if I had an image like this:
<img src="https://jvns.ca/images/rustboot1.png">
it would get wrapped in a
<p>
tag, now it doesn’t anymore. I dealt with this
just by adding a
margin-bottom: 0.75em
to images in the CSS, hopefully
that’ll make them display well enough.
Previously this wouldn’t get wrapped in a
p
tag, but now it seems to:
<br><br>
I just gave up on fixing this though and resigned myself to maybe having some
extra space in some cases. Maybe I’ll try to fix it later if I feel like
another yakshave.
I also needed to
turn off code highlighting (because it wasn’t working properly and I didn’t have it before anyway)
use the old “blackfriday” method to generate heading IDs so they didn’t change
allow raw HTML in my markdown
Here’s what I needed to add to my
config.yaml
to do all that:
markup:
  highlight:
    codeFences: false
  goldmark:
    renderer:
      unsafe: true
    parser:
      autoHeadingIDType: blackfriday
Maybe I’ll try to get syntax highlighting working one day, who knows. I might
prefer having it off though.
I also wrote a little program to compare the Blackfriday and Goldmark output
for various markdown snippets,
here it is in a gist
.
It’s not really configured the exact same way Blackfriday and Goldmark were in
my Hugo versions, but it was still helpful to have to help me understand what
was going on.
My approach to themes in Hugo has been:
pay someone to make a nice design for the site (for example wizardzines.com was designed by
Melody Starling
)
use a totally custom theme
commit that theme to the same Github repo as the site
So I just need to edit the theme files to fix any problems. Also I wrote a lot
of the theme myself so I’m pretty familiar with how it works.
Relying on someone else to keep a theme updated feels kind of scary to me, I
think if I were using a third-party theme I’d just copy the code into my site’s
github repo and then maintain it myself.
I
asked on Mastodon
if
anyone had used a static site generator with good backwards compatibility.
The main answers seemed to be Jekyll and 11ty. Several people said they’d been
using Jekyll for 10 years without any issues, and 11ty says it has
stability as a core goal
.
I think a big factor in how appealing Jekyll/11ty are is how easy it is for you
to maintain a working Ruby / Node environment on your computer: part of the
reason I stopped using Jekyll was that I got tired of having to maintain a
working Ruby installation. But I imagine this wouldn’t be a problem for a Ruby
or Node developer.
Several people said that they don’t build their Jekyll site locally at all –
they just use GitHub Pages to build it.
Overall I’ve been happy with Hugo – I
started using it
because it had fast
build times and it was a static binary, and both of those things are still
extremely useful to me. I might have spent 10 hours on this upgrade, but I’ve
probably spent 1000+ hours writing blog posts without thinking about Hugo at
all so that seems like an extremely reasonable ratio.
I find it hard to be too mad about the backwards incompatible changes, most of
them were quite a long time ago, Hugo does a great job of making their old
releases available so you can use the old release if you want, and the most
difficult one is removing support for the
blackfriday
Markdown renderer in
favour of using something CommonMark-compliant which seems pretty reasonable to
me even if it is a huge pain.
But it did take a long time and I don’t think I’d particularly recommend moving
700 blog posts to a new Markdown renderer unless you’re really in the mood for
a lot of computer suffering for some reason.
The new renderer did fix a bunch of problems so I think overall it might be a
good thing, even if I’ll have to remember to make 2 changes to how I write
Markdown (4.1 and 4.3).
Also I’m still using Hugo 0.54 for
https://wizardzines.com
so maybe these notes
will be useful to Future Me if I ever feel like upgrading Hugo for that site.
Hopefully I didn’t break too many things on the blog by doing this, let me know
if you see anything broken!
