---
title: "There is absolutely nothing wrong with Web"
url: "https://purplesyringa.moe/blog/./there-is-absolutely-nothing-wrong-with-web/"
fetched_at: 2026-05-05T07:02:08.722256+00:00
source: "Alisa Sireneva (PurpleSyringa)"
tags: [blog, raw]
---

# There is absolutely nothing wrong with Web

Source: https://purplesyringa.moe/blog/./there-is-absolutely-nothing-wrong-with-web/

There is absolutely nothing wrong with Web
March 31, 2026
Lobsters
This is a rant about how broken everything Web is based on is. You know, the usual. No offence intended towards framework developers, I’m glad this technology exists, but I’m sure you know this feeling. It gets too much sometimes.
I’ve been meaning to improve this blog’s technology for a while. It’s held together by two
hacky scripts
as opposed to a typical template engine, and that’s very limiting.
Why not ___?
So, why isn’t this a no-brainer? There are many static site generators, including classics like Hugo and Jekyll.
The answer is in my design decisions. I really value the unique feel of this blog – its bold color choice for the dark theme, a variable-width font for
inline code
, wide code snippets, headings on the left side, and sidenotes.
The last feature is by far the most complicated.
Sidenotes
Let’s start with something simple →
Here’s what this snippet looks like in my Markdown source (almost):
Let's start with something simple &rightarrow;

:::aside
A sidenote with
**formatting**
and math: $2 + 2 = 5$.
:::
Markdown disables all formatting inside HTML tags, so I can’t just use
<aside>
.
markdown-it-container
allows me to create a container that supports nested formatting, but “batteries-included” static site generators often don’t support this.
Moving on, on desktop, sidenotes are shown
to the right
of the commented content. When there’s little horizontal space (e.g. on mobile), they are shown
below
the content instead. This way, you always read the post in the intended order. So Markdown actually specifies both the beginning and the end of the commented part:
<
aside-start-here
/>
Let's start with something simple &rightarrow;

:::aside
A sidenote with
**formatting**
and math: $2 + 2 = 5$.
:::
markdown-it-container
doesn’t support self-closing annotations, so it has to be an HTML tag. Now, how should this be rendered in HTML?
<
div
class
=
"group"
>
main content
<
aside
>
elaboration
</
aside
>
</
div
>
On desktop, I style the
<aside>
as
position: absolute; left: 100%; top: 0;
to align it to the top of the
<div>
.
I used to place
<aside>
first and use
order
on mobile, but it doesn’t account for screen readers, so I had to change it.
Note that
<aside-start-here />
is rendered as a non-closed tag
<div class="group">
, and
:::aside
closes that
</div>
. This breaks renderers that assume Markdown AST nodes directly correspond to HTML AST nodes, which is pretty much every renderer.
So instead, I patch the produced HTML. Needless to say, that’s not a common part of your average SSG pipeline, so you lose all benefits of powerful tools, like hot reload.
Patches
There are other reasons to complicate HTML rendering and/or Markdown parsing:
Tables need to be horizontally scrollable
on mobile devices and narrow screens, which requires wrapping
<table>
in a container.
I need a simple syntax for videos, both
local
and
from YouTube
, i.e.
![]()
should emit
<video>
and
<iframe>
tags. This includes setting
aspect-ratio
for
<iframe>
and configuring autoplay and seizure warnings per-video.
I need to draw
diagrams
with
tikz
without running scripts by hand.
I want
split views
for pictures, custom emojis
, and inlining for small SVGs.
Maybe it’s asking for too much, but to me, that’s basic functionality – most of it is necessary either for accessibility or to get the point across without saying “sorry, my blog software doesn’t support this, so I’ll have to show it differently”.
Frameworks
Point is, I need to take out all the batteries from the battery-included tools, and the best way to do it is to drop the tools altogether.
On the other extreme are feature-complete Web frameworks like React and Dioxus. They are extensive enough to support everything I need.
The devil is in the details. PHP and other old-timey tools don’t support hot reload, which would normally be acceptable, but building
tikz
to SVG is slow as hell and can make page rebuilds take up to 10 seconds. Besides, SSR-based tools can’t run on GitHub Pages, and I value having a reliable hosting when I’m posted on HN.
I
guess
I could start a local server and run
wget -r
during build, but come on.
In contrast, most front-end frameworks import a ton of JavaScript for hydration even with SSR – so even though the site works without JS, the framework doubles the size of the page. This equally applies to modern Wasm-based frameworks. I could strip
<script>
tags, but that would prevent me from adding opt-in interactivity.
If you have JS enabled, press
Ctrl+Enter
to see what I mean.
Silver bullet?
That’s when I learnt about
Astro
. On paper, it has everything I need:
At first, this made me really sad, because it meant I didn’t have an excuse to develop my own framework. But as I started porting the site, cracks began to appear.
Since Astro is based on frontend technology, all code goes through
Vite
, even if it’s server-side-only. Vite is a bundler, and it’s responsible for packaging your project and its dependencies into JS files. More subtly, it makes directives like this work:
import
imageUrl
from
"./images/pic.png"
;
Behind the scenes, Vite intercepts the import, optimizes the picture, and makes it seem like
pic.png
is actually a JS file with the following contents:
export
default
"<url to picture>"
;
It uses a similar mechanism to handle CSS imports and other cool stuff.
Assets
I had naturally assumed that this mechanism would be extensible. My
kitchen sink
page contains tons of icons, so I’d like to write something like:
<
Icon
name
=
"custom-cpp"
/>
I’m using
Nerd Fonts
, which distributes a WOFF font. My plan was to have
<Icon>
extract the glyph from the script, create a virtual file for the resulting SVG, and use the mechanism that Vite uses for on-disk pictures or CSS modules to import it from JS.
Vite isn’t the one that performs the build, though. It’s based on
Rollup
, or alternatively
Rolldown
. (Note: we’re already three levels deep.) Rollup docs denote
a single page
to plugin development. Here’s an example quote from the docs:
If
external
is
true
, then absolute ids will be converted to relative ids based on the user’s choice for the
makeAbsoluteExternalsRelative
option. This choice can be overridden by passing either
external: "relative"
to always convert an absolute id to a relative id or
external: "absolute"
to keep it as an absolute id. When returning an object, relative external ids, i.e. ids starting with
./
or
../
, will not be internally converted to an absolute id and converted back to a relative id in the output, but are instead included in the output unchanged. If you want relative ids to be renormalised and deduplicated instead, return an absolute file system location as
id
and choose
external: "relative"
.
After reading it, I still have no clue what
external
does
, what absolute and relative IDs are and how their behavior differs. But I digress. Amid all this mess, there is
an example
for generating a virtual file using the
emitFile
API. Rollup plugins are valid Vite plugins, so it was easy to make such a plugin:
import
src
from
"virtual:example"
;
...
const
referenceId =
this
.
emitFile
({
type
:
"asset"
,
name
:
"example.txt"
,
source
:
"Hello, world!"
,
});
return
`export default import.meta.ROLLUP_FILE_URL_
${referenceId}
;`
;
...
But when I started a dev server, Vite told me that
actually
, I can’t use
emitFile
:
context method emitFile is not supported in serve mode. This plugin is likely not vite-compatible.
Turns out Vite uses Rollup for release only. How does it bundle files in development?
const
cssContent =
await
getContentWithSourcemap
(css)
const
code = [
`import { updateStyle as __vite__updateStyle, removeStyle as __vite__removeStyle } from
${
JSON
.stringify(
    path.posix.join(config.base, CLIENT_PUBLIC_PATH),
  )}
`
,
`const __vite__id =
${
JSON
.stringify(id)}
`
,
`const __vite__css =
${
JSON
.stringify(cssContent)}
`
,
`__vite__updateStyle(__vite__id, __vite__css)`
,
`
${modulesCode ||
'import.meta.hot.accept()'
}
`
,
`import.meta.hot.prune(() => __vite__removeStyle(__vite__id))`
,
].
join
(
'\n'
)
return
{ code,
map
: {
mappings
:
''
} }
Oh, I see. It inlines the stylesheet into JS. What does it do with pictures?
export
async
function
fileToDevUrl
(
environment: Environment,
  id:
string
,
  asFileUrl =
false
,
):
Promise
<
string
> {
  ...
let
rtn
:
string
if
(publicFile) {
    
    rtn = id
  }
else
if
(id.
startsWith
(
withTrailingSlash
(config.
root
))) {
    
    rtn =
'/'
+ path.
posix
.
relative
(config.
root
, id)
  }
else
{
    
    
    rtn = path.
posix
.
join
(
FS_PREFIX
, id)
  }
const
base =
joinUrlSegments
(config.
server
.
origin
??
''
, config.
decodedBase
)
return
joinUrlSegments
(base,
removeLeadingSlash
(rtn))
}
Right, those are routed to
/@fs/<absolute path>
. Wait, what?
In a nutshell, there are no virtual files in dev mode. If you want a URL with dynamic contents, use
data:
. Oh, and
import.meta.ROLLUP_FILE_URL_${referenceId}
isn’t actually the right thing to do even in release: it only works in JS files and produced complex code, instead you should use the
undocumented
magic string
__VITE_ASSET__${referenceId}__
because
???
. I love this ecosystem.
Say we somehow resolve all that and make
import imageSrc from "virtual:nerd-fonts/custom-cpp.svg"
work. Now we
just
need to tie two things together:
---
interface
Props
{
name
:
string
;
}
const
{ name } =
Astro
.
props
;
const
src =
await
import
(
`virtual:nerd-fonts/
${name}
.svg`
);
---
<
img
src
=
{src}
/>
…wait a second. That’s a
dynamic import
. This wouldn’t be an issue in typical NodeJS, which can resolve imports on-demand. But all code goes through Vite, which tries to build a Web bundle, so it wants to resolve modules before evaluation. Had we used an on-disk relative path, this would be translated roughly like this:
const
src =
await
import
(
`./images/
${name}
.svg`
);
import
file1
from
"./images/file1.svg"
;
import
file2
from
"./images/file2.svg"
;
const
src = {
    file1,
    file2,
    ...
}[name];
…totally negating the entire point of extracting only utilized glyphs from the font. Our only redemption is that this doesn’t even compile, because apparently dynamic imports aren’t supported for virtual files.
Well, okay, screw fast builds, let’s just build everything and rely on tree shaking. What’s the best library for extracting SVGs from fonts, anyway?
ttf2svg
? No,
npm audit
says that one has 15 vulnerabilities. I know,
harfbuzzjs
looks trustworthy:
import
{ decompress }
from
"wawoff2"
;
import
fs
from
"node:fs"
;
import
hbPromise
from
"harfbuzzjs"
;
const
iconNames = ...;
const
renderString = ...;
const
fontData =
await
decompress
(fs.
readFileSync
(
new
URL
(
"font.woff2"
,
import
.
meta
.
url
)));
const
hb =
await
hbPromise;
const
blob = hb.
createBlob
(fontData);
const
face = hb.
createFace
(blob,
0
);
const
font = hb.
createFont
(face);
const
buffer = hb.
createBuffer
();
buffer.
addText
(renderString);
buffer.
guessSegmentProperties
();
hb.
shape
(font, buffer);
const
output = buffer.
json
();
const
svgs = {};
output.
forEach
(
(
glyph, i
) =>
{
const
path = font.
glyphToPath
(glyph.
g
);
    svgs[iconNames[i]] =
`
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048">
            <path fill-rule="evenodd" clip-rule="evenodd" d="
${path}
" fill="#fff" />
        </svg>
    `
;
});
buffer.
destroy
();

font.
destroy
();
face.
destroy
();
blob.
destroy
();
WHY ARE MY ICONS UPSIDE DOWN? Okay, we’ll get to that in a bit, let’s try something easier first, why are they cropped wrong? I guess I should’ve computed the viewbox instead of hard-coding numbers, let’s use the
harfbuzzjs
API to get the bou-
Calling
hExtents
seems to brick the font instance
When running this code, I get:
{ ascender: 0, descender: 0, lineGap: 0 }
(empty line)
It seems like other operations break after
hExtents
as well: for instance, calling
buffer.json
seems to always return glyphs with ID
0
.
Fix memory corruption in hExtents/vExtents
We were allocation 12 bytes but the
hb_font_extents_t
struct is actually 48 bytes (the rest are private fields).
You know what, I don’t want SVGs, let’s try something else.
Fonts
Maybe extracting SVGs from the font wasn’t the brightest idea. It’s going to trigger many HTTP requests, which might be slow. Let’s use the font directly, we just need to drop unused glyphs. Let’s see what
Astro docs
have to say about it:
This API helps you keep your site performant with automatic
web font optimizations
including preload links, optimized fallbacks, and opinionated defaults. See common usage examples.
So, that doesn’t sound like optimizing fonts, that sounds like optimizing everything around fonts. I trust them though
. Let’s check
the config
.
font.subsets
Type:
Array<string>
Default:
["latin"]
Added in: astro@6.0.0
Defines a list of font subsets to preload.
subsets: ["latin"]
That doesn’t look like it supports Unicode codepoints.
font.unicodeRange
That’s encouraging!
Determines when a font must be downloaded and used based on a specific range of unicode characters. If a character on the page matches the configured range, the browser will download the font and all characters will be available for use on the page. To configure a subset of characters preloaded for a single font, see the subsets property instead.
Oh, that only affects preloading. Soooo… there basically isn’t any font optimization.
Don’t get me wrong, I’d gladly write it myself, but it’s not clear how to automatically rebuild the font if new icons are used, and given that virtual files don’t really work, I think it’s fair to say this wouldn’t work reliably anyway.
UnoCSS
You know what, that’s fair, no one cares about build performance and disk space anyway. Let’s just extract SVGs by hand and see what we can do with that.
$
git submodule add https://github.com/ryanoasis/nerd-fonts nerd-fonts
<downloaded 1.3 GB>
$
cd
nerd-fonts/src/svgs
$
ls
-w100 *.svg
ada_nf.svg      elm_nf.svg     karma.svg          rollup.svg
apple.svg       emacs_nf.svg       kotlin_nf.svg      R.svg
argdown.svg     error.svg      less.svg       ruby_nf.svg
asm_nf.svg      eslint.svg     license.svg        rust.svg
...
ejs.svg         java.svg       rails.svg          yml.svg
electron_nf.svg     jenkins.svg    react.svg          zig.svg
elixir_nf.svg       jinja.svg      reasonml.svg       zip.svg
elixir_script.svg   julia.svg      rescript.svg       zsh_nf.svg
A plain
import ... from "<path>.svg"
will either inline
data:
URLs in each
<img>
(bad for page size and caching), or trigger multiple HTTP requests (bad for latency).
Someone told me
UnoCSS
solves this cleanly: add a class with
background-image: url(data:...)
for each icon and let it remove unused definitions. It took me a while to figure out what UnoCSS does, but it’s basically Tailwind on steroids: it
parses HTML with regex
to get a list of used classes and emits only the required CSS rules.
You know, like tree shaking, but for CSS. So it’s basically a CSS bundler implemented from scratch. You know, like Rollup is a bundler and Vite is kinda a bundler. You can
integrate it with Astro
if you want three bundlers in one build. Do you like bundlers?
$
npm run build
$
firefox
The dimensions are wrong, but that’s expected from replacing a font with an SVG. I still have to hard-code the icon list, and I need to add other icon sources from
npm
because
src/svgs
doesn’t contain all glyphs. But maybe it’s not that b-
$
ls
dist/_astro/
...
.rw-r--r--  960 purplesyringa purplesyringa 31 Mar 01:48 -I 󰕙 github-mark-white.S2fJVXLq.svg
.rw-r--r--  960 purplesyringa purplesyringa 31 Mar 01:48 -I 󰕙 github-mark-white.S2fJVXLq_Z2nI3it.svg
...
Why are there two identi–
$
npm
ls
bookshelf@0.0.1 /home/purplesyringa/bookshelf
├── @astrojs/check@0.9.8
├── @astrojs/compiler-rs@0.1.6
├── @astrojs/mdx@5.0.3
├── @astrojs/rss@4.0.18
├── @astrojs/sitemap@3.7.2
├── @emnapi/core@1.9.1 extraneous
├── @emnapi/runtime@1.9.1 extraneous
├── @emnapi/wasi-threads@1.2.0 extraneous
├── @napi-rs/wasm-runtime@1.1.1 extraneous
├── @shikijs/transformers@4.0.2
├── @tybys/wasm-util@0.10.1 extraneous
├── @unocss/astro@66.6.7
├── @unocss/preset-icons@66.6.7
├── astro@6.1.1
├── sharp@0.34.5
├── tslib@2.8.1 extraneous
├── typescript@5.9.3
└── unocss@66.6.7
Why are there extraneous packages right after
npm clean-in
–
$
cat
dist/index.html
...
    <section data-astro-cid-w6ymvdtg="true" data-astro-cid-w56doo5x="true" class="parent">
    <div class="container" data-astro-cid-w56doo5x> 
    
        <p>
Hi! 👋 I'm <b>Alisa Sireneva</b> (she/her), a 21yo dev from Moscow.
</p>
    
 </div>
</section>  
...
Why are there multiple spaces despite
minifyHtml
?
Sigh
There are always going to be bugs and missing features. I’m a developer, I get it.
What I don’t get is why
Astro decided
that actually, React, Vue, and the rest of the frameworks were wrong to consider whitespace in templates insignificant, and so they’re going to make everyone write long lines and use
{/* prettier-ignore */}
. No, I can’t just use React for templating, that turns the component into an island.
Why did we have like three tools post-processing each other’s output to implement different sides of the same functionality, requiring
non-trivial integrations
to keep HMR working, and then someone went, “You know what will fix frontend development once and for all? Making another wrapper around these tools!”
I want to like Astro. I absolutely love the island architecture and easy content discovery. I want to like JavaScript. I love having a terse GC language with an enormous ecosystem, built-in WebAssembly support, and JSX. I want to like Vite, and Rolldown, and
unified
… but why do none of these tools offer a way to implement tree-shaking for fonts despite supporting it for JS and CSS? Why do I have to learn from single-page docs? And why do I have to use software with bangers like:
generatedFiles = [...generatedFiles, { image, width, format }];
It could be
so
simple. Allow components to directly emit virtual files. Might as well let them populate global sets that can then be read out in some centralized manner – that’d handle CSS bundling and font subsetting. It wouldn’t even need any clever hot-reload logic – just pure library functions. But it’s not the way Rollup works, so it’s not the way Vite works, so it’s not the way Astro works. And Rollup is not going away.
Fin.
I’ll probably finish the Astro port. It hurts that features that were trivial in my scripts are becoming complicated, and it won’t resolve issues with slow tikz builds, but it’s probably easier to maintain than whatever I’m using right now. Small steps.
Longer term I’ll probably switch to a custom framework. Cliché, I know. Boo hoo. I drafted a Rust version as an experiment, but I have no clue how well hot reloading code would work, so I’ll probably switch to JS. Having JSX would be great, and the pitfalls should be less… arbitrary. That’s not happening anytime soon, though.
In the meantime, enjoy a slightly improved HTML layout:
links
seems to parse it better, if anyone still uses it, and accessibility should be improved.
