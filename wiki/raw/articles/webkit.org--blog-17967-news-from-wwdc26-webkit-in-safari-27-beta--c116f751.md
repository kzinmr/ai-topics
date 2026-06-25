---
title: "News from WWDC26: WebKit in Safari 27 beta"
url: "https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/"
fetched_at: 2026-06-25T07:01:41.197588+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# News from WWDC26: WebKit in Safari 27 beta

Source: https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/

Contents
Safari 27 beta is here. Don’t miss our
WWDC26 sessions on web technology
, including
What’s new in WebKit for Safari 27
, to go deeper on our work in this release. Now, let’s dig into this beta, packed with 58 new features, 525 fixes and 4 deprecations that will hopefully make your work as a web developer a little easier.
Here’s a sneak peek of the highlights:
After years of anticipation, you can now use customizable
<select>
to style your form elements to match the rest of your site or app without rebuilding it in JavaScript or sacrificing accessibility.
Scroll anchoring prevents those visual jumps when content loads above the viewport.
WebAssembly JavaScript Promise Integration (JSPI) lets Wasm code participate in the async world of JavaScript.
Transform-aware anchor positioning closes out a major gap in the anchor positioning story.
The
:heading
pseudo-class, the
revert-rule
keyword, and the
stretch
keyword for box sizing all land in CSS.
Subpixel inline layout makes text rendering more precise.
And that’s just the start.
If you look through the lists of features and fixes in Safari 27, you’ll notice that, although there are 58 brand-new features and 525 fixes — the largest pile of fixes in any Safari release in recent memory — most of what is released is not about new things.
Most of this work has been about existing features behaving more correctly, handling more edge cases, and fitting together with other features the way you’d expect. We committed our time to increasing quality — that’s the story of this release and the year that led to it.
A lot of this work was also about aligning to web standards. When we found a spec that was unclear or incomplete, we helped update it, and then updated WebKit to match.
For example, Safari 27 contains 30 SVG fixes, including updates based on recent decisions in SVG 2 where we revived the Working Group. SVG is used on 67% of webpages, making this work very impactful. Anchor positioning continues to get refined as the CSS specification settles. And in more subtle places throughout the release — URL parsing details, event listener options, timezone identifier handling,
innerText
edge cases — features that look unchanged on the surface now behave the same way in Safari as they do in Chrome, Firefox, and Edge.
We also spent time making sure features still work across different contexts. A
:has()
selector invalidating properly when siblings change. An
aspect-ratio
resolving correctly against a percentage height.
box-shadow
rendering correctly on table-row elements.
background-clip: text
working on table header elements. Bugs that appear when combining features are among the hardest to find and the most frustrating, but we’ve made significant progress in hunting them down.
If something has been bothering you, test it in Safari 27 beta. You might be pleasantly surprised. And if it hasn’t been fixed yet,
file a bug report
, or add a comment to an existing issue with a concrete scenario, a link to a real site, or a reduced test case. The more concrete the problem, the more helpful it is.
This work goes beyond the Safari browser. When your customers open their news app, their banking app, their shopping app, there’s a good chance the interface they interact with is powered by the HTML, CSS, and JavaScript that’s rendered by WebKit and JavaScriptCore — the same engines inside Safari. Every fix in this release isn’t just for the browser — it benefits everything the web platform touches.
Let’s dive in.
Customizable Select
Safari 27 beta adds support for customizable
<select>
, which transforms the
<select>
element. You can now build a fully custom form element that matches the look and feel of your website or web app, without reaching for a JavaScript library or sacrificing the accessibility, reliability, and native platform integration of a real HTML form control.
Use the new
appearance: base-select
to clear the native styling and start with a clean palette. Then insert any additional CSS you want to create your custom design. Customizable
<select>
comes with new pseudo-elements for more granular control, like
::picker-icon
to target the disclosure indicator and
::checkmark
to target the checkmark that appears next to the selected
<option>
.  Both can be fully customized.
Use the new
<selectedcontent>
element inside the button to display the currently selected option’s content and style
<selectedcontent>
directly to get it to look exactly how you want in the closed state.
And because you’re still working with a real
<select>
, everything that comes with a native form control still works: keyboard navigation, screen reader support, form submission, validation,
change
events. You get the styling freedom of a custom widget with the power of a native HTML element.
Customizable
<select>
is a multi-vendor effort. The same syntax is coming to other browsers. Use progressive enhancement and style your
<select>
with
appearance: base-select
for a great experience in browsers that support it, and let browsers that don’t fall back to their built-in rendering.
Learn more in the WWDC26 session
Rediscover the HTML Select Element
, where Tim walks through the full API and how to build layouts inside options with Grid and Flexbox.
Additional bug fixes:
Fixed an issue where
<select multiple>
did not always fire
onchange
when the mouse button was released far outside the element. (173882861)
Fixed an issue where
<select>
control rendering was broken in vertical writing mode. (174068353)
Fixed a performance issue where parsing
<select>
elements with thousands of
<option>
children via
innerHTML
caused O(n²) overhead due to repeated list recalculation. (174244946)
Fixed
<option>
elements to correctly implement the HTML specification’s dirtiness concept for tracking user-modified
selected
state. (175306111)
Fixed the select picker appearing at an incorrect position when the
<select>
element is anchor positioned. (175454476)
Fixed the default
display
value for
<optgroup>
and
<option>
elements to
block
, matching the behavior of other browsers. (175473184)
Fixed
<option>
and
<optgroup>
elements to match the
:disabled
pseudo-class when inside a disabled
<select>
. (176559708)
Animations
Safari 27 beta adds the
animation
property to the
AnimationEvent
and
TransitionEvent
interfaces, letting event handlers directly access the
Animation
object associated with the event.
Additional bug fixes:
Fixed an issue where
animation-fill-mode
did not correctly apply viewport-based units after the viewport was resized. (80075191)
Fixed an issue where
!important
declarations did not override CSS animation values when CSS transitions were also running on the same property. (174367827)
Fixed an issue where identity matrix decomposition generated invalid quaternions, resulting in incorrect transform animations. (174813328)
CSS
Transform-aware anchor positioning
Safari 27 beta adds support for transform-aware anchor positioning. Now, when an anchor element has a CSS transform applied — scale, rotate, translate, or any combination — elements positioned relative to that anchor follow its transformed position instead of its pre-transform layout position. This works for transforms applied via the
transform
property as well as through the individual
translate
,
rotate
, and
scale
properties.
This closes a long-standing gap in the anchor positioning story. If you use anchor positioning to attach a tooltip, popover, or annotation to a transformed element, it now tracks correctly, even with animated transforms.
:heading pseudo-class
Safari 27 beta adds support for the
:heading
pseudo-class, which matches any heading element —
<h1>
through
<h6>
.
Instead of writing
h1, h2, h3, h4, h5, h6
in your selector list, you can just write
:heading
. And
:heading
can also be combined with functional selectors to target headings at specific levels:
revert-rule keyword
The
revert-rule
keyword is now supported in Safari 27 beta. Like
revert
and
revert-layer
,
revert-rule
rolls back the cascade — but specifically to the state as if the current style rule had not been present.
It gives you a more precise tool for working with overrides, especially in component libraries and design systems where you want to selectively undo declarations within a rule without losing the rest.
stretch keyword for box sizing
Safari 27 beta adds support for the
stretch
keyword in box sizing properties like
width
,
height
,
min-width
, and so on.
stretch
tells an element to fill the available space in the relevant axis, accounting for margins.
.card
{
width
:
stretch
;
}
Previously, the common way to achieve this was
width: 100%
— which doesn’t account for margins and can cause overflow when margins are applied. The
stretch
keyword does the right thing. If you’ve been using
-webkit-fill-available
as a workaround for the same behavior, now is a good time to switch.
Dutch IJ digraph in text-transform: capitalize and ::first-letter
The Dutch IJ digraph is now available in Safari 27 beta. When the content language is Dutch (
lang="nl"
),
text-transform: capitalize
and
::first-letter
now correctly titlecase “ij” to “IJ” at the start of words.
A small but genuine improvement for anyone writing Dutch text on the web.
position-anchor: normal and none
Safari 27 beta adds support for
position-anchor: normal
and
position-anchor: none
. Before,
position-anchor
defaults to
auto
, which makes every element use the implicit anchor element as its default anchor, if one exists. This has a side effect of changing an element’s positioning behavior, whether it uses anchor positioning or not. This may result in compatibility problems.
To fix this, the CSS Working Group has added two values to
position-anchor
to allow opting out of the new behavior:
none
: an element does not have a default anchor, and its positioning behavior is unchanged.
normal
:
auto
if an element uses
position-area
, otherwise
none
.
position-anchor: normal
is the new default value, replacing
auto
. This means elements will only have a default anchor and get anchor positioning behavior if it uses
position-area
, otherwise its behavior remains unchanged.
anchor-valid and anchor-visible
Safari 27 beta adds support for
anchor-valid
and
anchor-visible
. Originally,
position-visibility: anchors-valid
hides an element if any of its required anchor references can’t be resolved. However, it was not clear what constitutes “required anchor references”. The CSS Working Group has since then changed its behavior to only look at the default anchor box. To match the new behavior, some keywords also got renamed to drop the plurality:
anchors-valid
is renamed to
anchor-valid
anchors-visible
is renamed to
anchor-visible
Safari 27 beta aligns with the new behavior but also still supports the old keywords for compatibility.
Style containment for quotes
Safari 27 beta adds support for
contain: style
applying to CSS quotes. This allows you to scope effects of quotes to a certain subtree.
insert keyword for text-autospace
Safari 18.4 added support for text-autospace to control spacing between Chinese/Japanese/Korean (CJK) and non-CJK characters. Safari 27 beta now adds the
insert
keyword, making the following syntaxes equivalent:
text-autospace: ideograph-alpha ideograph-numeric insert
text-autospace: ideograph-alpha ideograph-numeric
Additional Bug Fixes:
Fixed an issue where
-webkit-text-fill-color
incorrectly overrode
text-decoration-color
. (47010945)
Fixed
shape-outside
computing incorrect text wrapping in RTL writing modes. (56890238)
Fixed flex layout to use the used
flex-basis
instead of the specified value for definiteness evaluation. (85707621)
Fixed an issue where the outline offset was too large for
outline: auto
on macOS. (94116168)
Fixed an issue where element positioning was incorrect when the containing block was an anonymous block. (96548847)
Fixed an issue where
box-shadow
did not work on
display: table-row
elements. (96914376)
Fixed
text-indent
with
calc()
containing percentages to correctly treat percentage components as zero for intrinsic size contributions. (97025949)
Fixed an issue where out-of-flow content had an incorrect height when set to
fit-content
. (97492632)
Fixed an issue with percentage size resolution in flex items in quirks mode. (100183902)
Fixed an issue where
clip-path: inset()
border-radius values did not render correctly at certain element and clip-path sizes. (110847266)
Fixed
-webkit-box
flexbox emulation not sizing children correctly inside
<fieldset>
elements. (114094538)
Fixed: Improved performance on pages using
:where
and
:is
selectors. (114904007)
Fixed an issue where elements with
display: table
could have incorrect layout when borders were present. (116110440)
Fixed
font-family
serialization to preserve quotes around family names that match CSS-wide keywords or generic families. (125334960)
Fixed an issue where elements with
border
,
position: absolute
, and
aspect-ratio: 1
were not rendered as squares. (126292577)
Fixed an issue where
perspective-origin
failed to resolve
var()
references when used as the second value, preventing animations from being applied. (131288246)
Fixed
:focus-visible
incorrectly matching after a programmatic
focus()
call triggered by clicking a button with child elements. (134337357)
Fixed an issue where the bottom margin of a last child element collapsed out of a parent with
min-height
. (134356544)
Fixed a performance issue where pages with many DOM manipulations and complex
:has()
selectors could freeze. (138431700)
Fixed an issue where a font was downloaded despite no characters in the document falling within its
unicode-range
. (140674753)
Fixed an issue where
@media (prefers-color-scheme: dark)
inside an iframe did not match when the iframe’s
color-scheme
was set to
dark
. (142072593)
Fixed an issue where
background-clip: text
did not work on table header elements. (142812484)
Fixed an issue where
width: 0
did not collapse a table cell to its minimum size. (142814603)
Fixed an issue where
:has(:empty)
continued to match after the targeted element’s content was dynamically changed to no longer be empty. (143864358)
Fixed an issue where floats and out-of-flow objects could be incorrectly adjacent to anonymous blocks. (144481961)
Fixed an issue where text gradually disappeared when toggling
text-transform
on elements with
::first-letter
styling. (145550507)
Fixed an issue where
height: max-content
resolved to zero on absolutely positioned elements when a child had
max-height: 100%
. (147333178)
Fixed an issue where tables with collapsed borders incorrectly calculated the first row width, causing excess border width to spill into the table’s margin area. (149675907)
Fixed an issue where an
inline-flex
container with
flex-direction: column
did not update its width to match the intrinsic size of a child image when the image was not cached. (150260401)
Fixed CSS
zoom
interacting incorrectly with
font-weight
,
font-style
, and
font-variant
on iPad. (152173269)
Fixed an issue where non-replaced elements with
aspect-ratio
enforced the automatic minimum size even when
min-width
was explicitly set to
0
. (156837730)
Fixed an issue where an element can’t anchor to its previous sibling. (162903640)
Fixed
:has()
style invalidation performance for selectors where
:has()
is in non-subject position. (163512170)
Fixed an issue where RTL grid scrollable areas did not correctly account for grid layout and scrollbars. (167792896)
Fixed pixel snapping to be applied consistently for all
border-width
value types. (168240347)
Fixed rendering of linear gradients when all color stops are at the same position. (169063497)
Fixed an issue where
inset
box-shadow
was incorrectly positioned on table cells with collapsed borders. (169254286)
Fixed
position-try-order
to interpret logical axis values using the containing block’s writing mode instead of the element’s own writing mode. (169501069)
Fixed an issue where children with percentage heights inside absolutely positioned elements using intrinsic height values (
fit-content
,
min-content
,
max-content
) incorrectly resolved against the containing block’s height instead of being treated as
auto
. (171179193)
Fixed an issue where percent-height replaced elements computed stale preferred widths in shrink-to-fit containers. (171184282)
Fixed a regression where
@scope
styles did not apply to slotted elements in web components. (171383788)
Fixed an issue where the table cell
nowrap
minimum width calculation quirk was applied outside of quirks mode. (171410252)
Fixed a performance issue where
contain: layout
caused significantly slower forced layouts when all siblings created their own formatting context. (171545381)
Fixed an issue where dynamically inserting text before existing content did not update
::first-letter
styling. (171649994)
Fixed an issue where underlines were split when a ruby base was expanded due to long ruby text. (171653095)
Fixed an issue where changing
color-scheme
did not repaint iframe background. (171658244)
Fixed an issue where nested children of a popover element failed to render when using
position: absolute
. (171735933)
Fixed an issue where
color: initial
resolved to the wrong color when the system is in dark mode. (172320282)
Fixed an issue where an element with
display: contents
did not establish an anchor scope when using
anchor-scope
. (172355302)
Fixed an issue where ordered list numbers with large starting values were clipped off-screen. (172515216)
Fixed
<general-enclosed>
in media queries to reject content with unmatched close brackets per the
<any-value>
grammar. (172575115)
Fixed an issue where the
rlh
unit was double-zoomed with evaluation-time CSS zoom. (172798163)
Fixed an issue where anchor-positioned elements anchored to children of sticky-positioned boxes did not stick correctly. (172884148)
Fixed an issue where pseudo-elements were not sorted correctly when sorting anchor elements by tree order. (173032203)
Fixed
outline: auto
to correctly respect zoom. (173068660)
Fixed
outline-offset
to work correctly with
outline: auto
on iOS. (173130230)
Fixed
:active
,
:focus-within
, and
:hover
pseudo-classes to correctly account for elements in the top layer. (173145294)
Fixed a regression where the
ic
length unit was incorrectly affected by page scaling. (173198587)
Fixed the
shape()
function to omit default control point anchors in computed value serialization per the CSS Shapes specification. (173233716)
Fixed: Updated SVG and MathML user agent style sheets to use
:focus-visible
instead of
:focus
. (173321368)
Fixed an issue where
lh
and
rlh
units resolved with double-zoom when
line-height
was a number value. (173448638)
Fixed
outline-width
to be ignored when
outline-style
is
auto
, matching the specification. (173567890)
Fixed
:in-range
and
:out-of-range
pseudo-classes for time inputs with reversed ranges. (173589851)
Fixed
:placeholder-shown
to correctly match input elements that have an empty
placeholder
attribute. (173604635)
Fixed an issue where ligatures caused a non-zero layout width for text with
font-size: 0
. (173840866)
Fixed computed value of auto insets or margins as returned by
getComputedStyle()
to be zero, if the element uses
position-area
or
anchor-center
. (173885561)
Fixed
position-area
not being able to anchor to an element positioned using anchor functions. (173964030)
Fixed
:in-range
and
:out-of-range
pseudo-classes to correctly update when the
readonly
attribute changes. (173978657)
Fixed an issue where
view-timeline-inset
serialization failed to coalesce identical values. (174096313)
Fixed CSS variable cycle detection to match the CSS Values Level 5 specification. (174105259)
Fixed
url()
token serialization in CSS custom properties. (174144616)
Fixed
text-autospace
to correctly handle supplementary Unicode characters. (174148315)
Fixed an issue where flex items with different
order
values caused incorrect baseline alignment. (174241817)
Fixed an issue where hovering over
::first-letter
text showed a pointer cursor instead of the expected I-beam cursor. (174258447)
Fixed an issue where
display: grid
on a
<fieldset>
element added extra unnecessary space below its content. (174301311)
Fixed outline radii rendering for elements with a non-auto
outline-style
. (174328839)
Fixed an issue where
aspect-ratio
was not honored when the page was zoomed in. (174361289)
Fixed replaced elements to use the transferred size through intrinsic aspect ratio for min-content and max-content sizing. (174386310)
Fixed an issue where
height: 100%
on a child element altered the layout when the parent’s height was defined via
aspect-ratio
. (174448267)
Fixed margin collapse to be allowed when the preferred block size behaves as auto, per the CSS Sizing specification. (174547610)
Fixed an issue where
document.styleSheets
and
shadowRoot.styleSheets
incorrectly included adopted style sheets, which per the CSSOM specification should only appear in the final CSS style sheets list used for style resolution. (174583340)
Fixed the CSSOM preferred style sheet set name to be established at sheet creation time based on insertion order rather than tree order. (174586058)
Fixed highlight pseudo-elements such as
::selection
and
::highlight
to disallow vendor-prefixed properties, aligning with the CSS Pseudo-Elements specification. (174590593)
Fixed cycle detection and nested function call handling in CSS custom functions. (174609179)
Fixed
FontFace.loaded
to reject when a
local()
font source fails to load. (174631384)
Fixed an issue where
word-break: break-all
incorrectly allowed CJK close punctuation to appear at the start of a line. (174656971)
Fixed an issue where
word-break: keep-all
incorrectly suppressed line break opportunities at CJK punctuation characters. (174658701)
Fixed the
FontFace
constructor to reject with a
SyntaxError
instead of a
NetworkError
when a
BufferSource
fails to parse, per the CSS Font Loading specification. (174669738)
Fixed the
FontFace
family
attribute to return the serialization of the parsed value. (174698351)
Fixed grid layout to correctly handle percentage and
calc()
values for the specified size suggestion. (174863227)
Fixed
:has()
sibling invalidation issues related to relation forwarding. (175006235)
Fixed an issue where
min-width: auto
was not correctly computed for flex items. (175157619)
Fixed an issue where percentage heights inside flex items did not resolve correctly in quirks mode. (175158571)
Fixed an issue where
margin-trim: block-start
did not apply to blocks nested inside inline boxes. (175162899)
Fixed an issue where dynamically changing
display: contents
on a
<fieldset>
legend caused incorrect rendering. (175163337)
Fixed: Improved
:has()
invalidation performance by including the full selector context in invalidation selectors. (175177078)
Fixed the CSS preload scanner to resolve relative
@import
URLs against the
<base>
element URL. (175305190)
Fixed
-webkit-box
flex distribution for children with orthogonal writing modes. (175323734)
Fixed
calc(infinity)
as a
flex-grow
factor not stretching a flex item to 100% width. (175431146)
Fixed
:has()
sibling invalidation failing due to an internal bitfield overflow, causing stale styles when siblings are added or removed. (175433733)
Fixed
:has()
invalidation for sibling combinators when elements are inserted or removed from the DOM. (175441568)
Fixed
transition-property
not preserving the specified case of
<custom-ident>
values during serialization. (175467206)
Fixed the
will-change
property not serializing correctly when used with non-property identifiers or identifiers in a non-standard case. (175482352)
Fixed percentage
top
and
bottom
values on relatively positioned elements not resolving when the containing block has
aspect-ratio
. (175502356)
Fixed: Updated the enhanced
<select>
element to use
self-
keywords for anchor positioning. (175505107)
Fixed
text-indent
computation when tab stop positions are involved. (175529961)
Fixed
calc()
margin computations in flex layout. (175532405)
Fixed
calc()
margin computations for block, fieldset, and table caption layouts. (175548980)
Fixed handling of
<li>
value
attributes in reversed ordered lists. (175558324)
Fixed CSS trigonometric functions to correctly convert degrees to radians. (175575617)
Fixed
sibling-index()
and
sibling-count()
inside calc() functions to be correctly simplified. (175590806)
Fixed
sibling-index()
and
sibling-count()
to correctly return 0 when used in cross-tree
::part()
styling. (175592607)
Fixed the CSS
resize
handle not working on an element when the handle overlaps a child iframe. (175621855)
Fixed flex container baseline alignment being incorrectly computed for scroll containers by clamping to the border edge. (175631095)
Fixed an issue where inline-level boxes with
calc()
margins or padding lost the fixed component during intrinsic width computation. (175669222)
Fixed floats with
margin-start
incorrectly overlapping adjacent floats. (175669464)
Fixed
aspect-ratio
calculations for block-level elements with size constraints. (175669713)
Fixed
aspect-ratio
calculations for flex items with percentage cross-size constraints. (175669774)
Fixed
aspect-ratio
calculations for flex items with definite cross-size values. (175690028)
Fixed
revert-layer
computing incorrectly when there is a leading empty or space substitution value. (175729680)
Fixed
:has()
invalidation incorrectly resetting sibling relation bits, causing style invalidation failures for first-in-sibling-chain elements. (175738008)
Fixed an issue where flex items with explicit
min-height: min-content
were incorrectly treated as scrollable, zeroing out their minimum size. (176173688)
Fixed
:has()
invalidation performance when used inside nested
:is()
selectors. (176354723)
Fixed
sibling-count()
&
sibling-index()
used in
@keyframes
to re-resolve when siblings change. (176531901)
Fixed an issue with a collapsed border color mismatch when the table cell has a different writing-mode. (173655092)
Scroll Anchoring
Scroll anchoring is now supported in Safari 27 beta. When content is inserted or removed above the current viewport position — an image loads, an ad injects, a comment appears — the browser automatically adjusts the scroll position so the content you’re reading stays put instead of jumping.
This is an improvement you’ll feel on many sites, especially ones with lazy-loaded images, infinite-scroll feeds, or dynamically injected content. Most sites get this for free — no opt-in required.
Scroll anchoring is controlled by the
overflow-anchor
CSS property, which defaults to
auto
. If you have a specific element where you need to opt out of scroll anchoring, set
overflow-anchor: none
.
Additional bug fixes:
Fixed an issue on iOS where calling
scrollTo
during a momentum scroll incorrectly interrupted the scroll, ensuring that momentum scrolling continues as expected and smooth scrolling behaves properly. (41949531)
Fixed an issue on iOS where programmatic smooth scrolling with
scroll-snap-type: mandatory
failed after the browser chrome was hidden. (100727098)
Fixed an issue where interrupting scroll momentum caused the scrolling container to stop rendering and hit-testing to be misplaced. (116205365)
Fixed an issue on iOS where restored scroll position was incorrect after relaunching Safari. (127308062)
Fixed an issue where tabbing in a scroll container with
scroll-padding
did not scroll the focused element into view. (147513379)
Fixed an issue on macOS where custom CSS scrollbars could be cut off and the scrollbar corner rect was sized incorrectly. (168566468)
Fixed rubberbanding behaving incorrectly when a site triggers a smooth scroll to the top during a rubberband. (170705188)
Fixed an issue where pages could become blank and jump to the top after dynamically loading new content when scroll anchoring was enabled. (170889205)
Fixed an issue where scroll anchoring could cause pages to scroll to negative offsets. (171221075)
Fixed an issue where pages using the Navigation API could have offset hit test locations, making elements unclickable. (171752650)
Fixed an issue on iOS where composited layers would briefly flash blank when
window.scrollTo()
was called synchronously with a DOM layout change. (173197381)
Fixed an issue where sticky-positioned elements could flicker rapidly after scrolling. (173680821)
Fixed an issue where scroll anchoring could cause a page to scroll to the top or bottom automatically. (173885027)
Fixed an issue where calling
scrollIntoView()
on a scrollable element incorrectly scrolled the element’s own contents. (174173683)
Fixed scroll anchoring interfering with rubberbanding on some websites. (175195943)
Fixed an issue on iOS where scroll position was not preserved correctly when rotating the device on right-to-left pages. (175910769)
HTML
sizes=”auto” on img
The
auto
keyword in the
sizes
attribute on
<img>
elements is now supported in Safari 27 beta.
<
img
src
=
"photo.jpg"
srcset
=
"photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w"
sizes
=
"auto"
loading
=
"lazy"
alt
=
"A mountain landscape"
>
When an image uses
loading="lazy"
and you don’t know its rendered layout width ahead of time,
sizes="auto"
tells the browser to calculate the size automatically based on the actual layout width once it’s known. This makes responsive images work correctly for images inside layout containers with dynamic widths.
shadowrootslotassignment attribute
Safari 27 beta adds support for the
shadowrootslotassignment
attribute on declarative shadow roots. This lets you configure the slot assignment mode (
named
or
manual
) directly in HTML when defining a shadow root declaratively, matching the JavaScript
attachShadow({ slotAssignment: "manual" })
option.
Additional bug fixes:
Fixed an issue where an HTML
map
element without a
name
attribute did not match its associated image using the
id
attribute. (12359382)
Fixed sequential focus navigation to skip elements that do not meet the specification’s focusability requirements. (103370883)
Fixed viewport
<meta>
parsing to correctly treat form feed as ASCII whitespace per the HTML specification. (108440799)
Fixed parsing of
javascript:
URLs to align with the specification. (147612682)
Fixed an issue where a third nested
<iframe>
using the
srcdoc
attribute did not render. (167917471)
Fixed incorrect parsing of pixel-length margin attributes on
<body>
,
<iframe>
, and
<frame>
elements. (171240848)
Fixed an issue where
replaceWith()
stopped processing remaining nodes if a script in the replacement removed a sibling. (172753019)
Fixed an issue where HEIC images were incorrectly converted to JPEG when uploaded via drag-and-drop or file input. (173206598)
Fixed the HTML preload scanner to skip preloading stylesheets that have the
disabled
attribute. (173378582)
Fixed an issue where setting the
rel
attribute on an
<a>
element multiple times did not clear prior link relations. (173567839)
Fixed the HTML parser fast path to correctly process escaped attribute values longer than one character. (173673581)
Fixed the HTML parser fast path to correctly detect nested
<li>
elements. (173983892)
Fixed the HTML parser fast path to use the adjusted current node for MathML and SVG integration point checks. (174096305)
Fixed document named item collection to include all
<object>
elements, aligning with other browser engines. (174537345)
Fixed
window.open()
to correctly consume user activation when creating a new browsing context, aligning with the HTML specification. (174587258)
Fixed remaining issues with
<img sizes="auto">
to fully align with the specification. (174684058)
Fixed an issue where
dir=auto
on
<slot>
elements did not update when slotted content changed. (174871706)
Fixed an issue where
<option>
elements rendered incorrectly when the
label
attribute was empty. (174979446)
Fixed an issue where the preload scanner incorrectly skipped
<source>
elements with an empty
type
attribute inside
<picture>
. (175094037)
Fixed
innerText
to emit a newline for empty
<option>
or
<optgroup>
inside
<select>
. (175245381)
Fixed HTML floating-point number parsing to correctly handle values with a leading
+
sign. (175300431)
Fixed
innerText
to no longer emit newlines for
visibility: hidden
block elements. (175569426)
Fixed
innerText
to correctly emit blank lines around
<p>
elements regardless of their CSS
display
value. (175729427)
Fixed the speculative preload scanner to no longer incorrectly preload scripts inside SVG elements. (175800116)
Fixed
innerText
on tables to no longer emit spurious trailing newlines and to preserve row-exit newlines after empty rows. (176635985)
Fixed an issue where inserting an image with a
srcset
attribute into a dynamically created iframe resulted in an invisible image. (66849050)
Fixed
naturalWidth
and
naturalHeight
returning incorrect values for SVG images without intrinsic dimensions. (141196049)
Fixed an issue where HDR images would flicker and lose their HDR appearance when overlapping layers animate. (163382580)
Fixed an issue where adopting a standalone
img
element did not update its image data. (172856773)
JavaScript
Top-Level Await
Safari 27 beta includes a complete standards-compliant rewrite of the ECMAScript module (ESM) loader. The new loader is implemented in native C++ and conforms directly to the ECMAScript specification’s module loading algorithms, replacing an earlier implementation based on an abandoned 2016 WHATWG Loader proposal that predated top-level await entirely.
The rewrite fixes module execution ordering and initialization issues that could cause imports to access exports before they were fully evaluated. It was validated against test262, the Web Platform Tests, and additional test cases.
Top-level await is a foundational feature of modern JavaScript module authoring, and it’s been a real pain point in Safari for a while — a known source of cross-browser bugs that developers building module-based apps had to work around. This fix closes that gap.
Additional bug fixes:
Fixed multiple top-level await correctness bugs with a rewrite of the ES module loader for standards compliance. (97370038)
Fixed regular expressions in Unicode mode to not count non-capturing groups and modifiers toward the number of available backreferences. (167746769)
Fixed
%TypedArray%.prototype.subarray
to calculate
beginByteOffset
correctly to align with ECMA-262. (168143600)
Fixed the trace behavior of
RegExp.prototype[Symbol.split]
to align with ECMA-262. (168288878)
Fixed
Array.prototype.concat
to correctly handle arrays with indexed accessors, preventing getter reentry from bypassing
Symbol.isConcatSpreadable
checks. (172237596)
Fixed an issue where a greedy or non-greedy non-BMP character class in a regular expression could advance the index past the end of input. (172978772)
Fixed an issue where class instance field initializers did not have the correct evaluation context when used inside arrow functions and nested scopes. (173296563)
Fixed TypedArray
[[Set]]
to check the receiver before writing to the typed array. (173386404)
Fixed
%ArrayIteratorPrototype%.next()
to return
{ done: true }
instead of throwing a
TypeError
when the source TypedArray is detached and the iterator has already completed. (173759106)
Fixed an issue where a fixed-count mixed-width character class in a regular expression did not correctly restore the index on backtrack. (173972458)
Fixed an issue where regular expressions with non-BMP characters could skip valid match positions when alternating between patterns. (174200307)
Fixed an issue where regular expression captures were not properly cleared when backtracking out of fixed-count parenthesized groups and negative lookaheads. (174201284)
Fixed an issue where
import { "*" as x }
was incorrectly treated as a namespace import instead of a named import using the string
“"
as a ModuleExportName. (174314099)
Fixed an issue where
RegExp.prototype.exec
and
RegExp.prototype.test
could match against a stale pattern if
lastIndex
has a
valueOf
that calls
RegExp.prototype.compile
. (174461752)
Fixed an issue where async functions using module-scoped variables could fail when the DFG JIT optimized scope resolution. (174626957)
Fixed an issue where
Intl.Segmenter
with
granularity: "word"
incorrectly reported
isWordLike: false
for numeric segments. (175057894)
Fixed
Object.defineProperties
to call Proxy traps in the correct order. (175068687)
Fixed an issue where
Intl.Locale
did not canonicalize before overriding the language. (175092327)
Fixed time zone identifiers to return primary IANA time zone IDs instead of legacy ICU identifiers. (175098682)
Fixed
Intl.DateTimeFormat
to preserve the original legacy timezone identifier instead of replacing it with the primary IANA ID. (175206605)
Fixed
Promise.prototype.finally
to throw a
TypeError
when
@@species
is not a constructor, matching the behavior of other browsers. (175290627)
Fixed the regular expression engine to reject dangling hyphens in character class syntax when using the
/v
flag. (175559808)
Fixed a performance issue with module resolution by limiting cache population to star-resolution and indirect-resolution cases. (175826413)
Fixed a performance issue with
TypedArray.prototype.lastIndexOf
by adding SIMD-accelerated reverse search for numeric types. (175904377)
Fixed a performance issue where building a module namespace with many
export
statements was significantly slower than necessary. (175949532)
Fixed
DataView
constructor to match specification-defined argument validation order and error throwing behavior. (176110210)
Fixed an issue where
Array.prototype.concat
could produce incorrect results when combining arrays with incompatible indexing types. (176219964)
WebAssembly
JavaScript Promise Integration (JSPI)
Safari 27 beta adds support for WebAssembly JavaScript Promise Integration (JSPI). JSPI lets synchronous-looking WebAssembly code suspend and wait for JavaScript Promises, making it much easier to port existing C, C++, Rust, and other language code to the web where that code expects synchronous I/O.
Before JSPI, porting code that called synchronous APIs to Wasm required rewriting everything on top of a callback or async state machine. With JSPI, the Wasm module can suspend at a call site and resume when the Promise resolves — the rest of the module sees straight-line synchronous code. This is a significant capability for the Wasm ecosystem.
Additional bug fixes:
Fixed
WebAssembly.Suspending
and
WebAssembly.SuspendError
to be data properties instead of getter functions, aligning with other WebAssembly attributes like
WebAssembly.Module
. (170155726)
Fixed incorrect
IntegerOverflow
exceptions thrown by
i32.rem_s
,
i64.rem_s
,
i32.div_u
,
i64.div_u
,
i32.rem_u
, and
i64.rem_u
when both operands are constants. (175122462)
Fixed a regression where
RegisterSet::normalizeWidths()
lost vector-width information, causing v128 argument corruption in WebAssembly SIMD thunks. (176035764)
MathML
Multiple-character operators in MathML
Safari 27 beta now supports multiple-character operators in MathML, improving the rendering of complex mathematical notation that uses operators like
++
,
:=
,
/=
, and similar. We also updated operator dictionary to MathML Core, so that we also support multi-character, combining character, and updated operator dictionary.
tabindex, focus(), blur(), and autofocus on MathML
Safari 27 beta now supports
tabindex
,
focus()
,
blur()
, and
autofocus
on MathML elements, improving MathML feature parity’s with HTML. This makes math content fully participate in keyboard navigation and focus management, which supports interactive educational content and accessibility.
Additional bug fixes:
Fixed an issue where symmetric non-stretchy large operators were not centered around the math axis. (170905663)
Fixed an issue where dynamic changes to
<mo>
element attributes did not trigger a relayout. (170907029)
Fixed an issue where
minsize
and
maxsize
defaults and percentages did not use the unstretched size as specified. (170908253)
Fixed positioning of the
<mprescripts>
element within
<mmultiscripts>
layout. (170909975)
Fixed an issue where the MathML fraction bar was not painted when its thickness was equal to its width. (170934351)
Fixed an issue where
<none>
and
<mprescripts>
elements were not laid out as
<mrow>
elements in MathML. (170940035)
Fixed an issue where MathML token elements ignored
-webkit-text-fill-color
when painting math variant glyphs. (172020318)
Fixed
padding
and
border
rendering on
<msqrt>
and
<mroot>
elements and corrected token sizing for
mathvariant
. (173081436)
Fixed absolute positioning of elements inside MathML by ensuring logical height is updated. (173088146)
Fixed
tabIndex
values not being set correctly for MathML elements. (174734133)
Spatial Web
Immersive website environments in visionOS
Safari 27 beta in visionOS 27 adds support for immersive website environments. Developers can now provide incredible immersive experiences with a simple
<model>
element and one JavaScript API call. The Immersive API on the model element works similarly to how the Fullscreen API does on video elements. Learn more in the WWDC26 session
Explore immersive website environments in visionOS
.
Consider what this makes possible in a browser: a ticketing site where you can see the view from your seat before you buy, or a hotel that lets you walk the room, all built with standard web technology, no app required.
img controls on spatial and panorama photos
Safari 27 beta in visionOS 27 adds support for the
controls
attribute on
<img>
elements displaying spatial and panorama photos. When applied, the image gets native interactive controls appropriate for the content type, allowing the image to be viewed spatially or immersively wrapped around the user.
model on iOS, iPadOS, and macOS
The
<model>
HTML element is now available in Safari on iOS, iPadOS, and macOS, joining its existing availability in visionOS. Web developers can now embed interactive 3D content using standard HTML across Apple platforms.
<
model
src
=
"teapot.usdz"
>
</
model
>
Learn more in the WWDC26 session
Get started with the HTML Model Element
.
dynamic-range-limit on model
Safari 27 beta adds support for
dynamic-range-limit
on the
<model>
element, giving you control over the HDR rendering range for 3D content in iOS and macOS.
Additional bug fixes:
Fixed spatial and panoramic image controls to support RTL language layout and localization of type labels. (161690817)
Fixed
<model>
elements displaying at 100x the expected size for assets authored in tools that use centimeter units. (167805672)
Fixed an issue where WebXR viewports did not get an initial value until
getViewport()
was called. (168125694)
Fixed an issue where the
<model>
element stagemode orbit physics behaved differently between iOS and visionOS. (172189776)
Fixed an issue on visionOS where fullscreen video would sometimes jump when exiting fullscreen if the browser window was narrower than the video. (174454557)
WebGPU
Safari 27 beta now supports the
clip_distances
built-in value in WGSL shaders. Clip distances are a WebGPU feature that allows vertex shaders to define custom clipping planes, enabling you to discard geometry on one side of an arbitrary plane before rasterization occurs.
Additional bug fixes:
Fixed
compressedTexImage
not validating whether the compressed texture format extension has been enabled. (175652171)
Fixed some
texImage
functions reporting errors with incorrect function names. (175652807)
Fixed some WebGL context state properties not being correctly reset on context loss. (176190808)
Fixed
GPUDevice.onuncapturederror
event handler attribute not working. (149577124)
Fixed: Restored
maxStorageBuffersInFragmentStage
and related WebGPU limits. (160800947)
Fixed rendering failing when using direct
GPUTexture
objects instead of
GPUTextureView
with multisampled resolve targets in render passes. (175452924)
Media
TextTrackCue.endTime = Infinity
Safari 27 beta supports setting
TextTrackCue.endTime
to
Infinity
to represent an unbounded cue duration. It’s useful for captions or data cues of live streams.
Additional bug fixes:
Fixed an issue where decoding WebM audio files with more than two channels would fail. (82160691)
Fixed an issue where
preservesPitch
and
playbackRate
were not correctly handled on an
HTMLMediaElement
connected to an
AudioContext
via
createMediaElementSource
. (93275149)
Fixed
MediaCapabilities.decodingInfo()
incorrectly reporting VP8 in WebM as not supported. (127339546)
Fixed an issue on iPad where exiting fullscreen on a media document incorrectly navigated back to the previous page instead of returning to the inline view. (137220651)
Fixed an issue where the WebCodecs
VideoDecoder
API output frames in an incorrect order for videos containing B-frames. (145093697)
Fixed an issue where the darkening overlay on inline video controls made accurate scrubbing difficult and displayed video content incorrectly on macOS. (161271114)
Fixed an issue where WebM with VP9/Vorbis fallback would not play. (164053503)
Fixed video playback failing when the declared MIME type in a
<source>
element does not match the actual content type served by the server. (166181001)
Fixed an issue where text selection was broken after pausing a video when the media player ran in the content process. (167727538)
Fixed
HTMLMediaElement.currentTime
to report smoothly progressing values instead of updating only at fixed intervals. (170115677)
Fixed an issue where MP4 files containing Opus audio tracks could not be decoded with
decodeAudioData
. (170196423)
Fixed an issue where the
VideoFrame
constructor did not handle the video color range correctly for NV12 (I420 BT601) video frames. (170299037)
Fixed an issue where Live Text selection was unavailable on paused fullscreen videos. (170817667)
Fixed an issue where FairPlay-protected VP9 content failed to play via
MediaSource
. (171210968)
Fixed an issue where autoplay would proceed before default text tracks finished loading. (171699293)
Fixed the
currentTime
getter to return
defaultPlaybackStartPosition
when no media player exists. (171722368)
Fixed
HTMLMediaElement
to fire a
timeupdate
event when resetting the playback position during media load as required by the specification. (171785463)
Fixed an issue where the media player
preload
attribute was not properly updated when the
autoplay
attribute was set. (171883159)
Fixed an issue where seeking in a WebM video did not work correctly while content was still loading. (172473039)
Fixed an issue where media playback could not move to the next item in a playlist when the tab was in the background. (172676372)
Fixed an issue where scrubbing a video in full-screen mode could cause it to exit full-screen. (172682230)
Fixed an issue where HDR video content appeared washed out due to colorspace information being lost during processing. (172721079)
Fixed Encrypted Media Extensions to check support for the full content type including codecs, rather than only the MIME type. (173852931)
Fixed an issue where setting
HTMLMediaElement.volume
had no effect when the element was connected to an
AudioContext
. (174278899)
Fixed
ImageCapture
to correctly queue
takePhoto()
and
applyConstraints()
requests to avoid concurrent capture session reconfiguration. (174950018)
Fixed a regression where videos would stop playing and lose audio after a few seconds on some websites. (174966899)
Fixed an issue where U+0000 (NULL) characters were not allowed in
VTTCue
text content. (175084171)
Fixed video content disappearing after switching to another tab and back. (175257980)
Fixed WebVTT cue settings line parsing failures. (175296476)
Fixed
::cue()
selectors to correctly match the WebVTT root object in addition to child nodes. (175550173)
Fixed
currentTime
on iOS to update more frequently during media playback. (175774587)
Fixed Media Source Extensions
readyState
not being updated immediately when playback stalls due to a gap in buffered data. (176330683)
Web API
Service Worker static routing API
Safari 27 beta adds support for the
Service Worker static routing API
. This lets a service worker declare routing rules that the browser can use to bypass the service worker entirely for certain requests, reducing overhead for high-performance PWAs.
Dedicated workers inside shared workers
Safari 27 beta adds support for creating dedicated workers inside shared workers, per the HTML Standard.
ReadableStream  improvements
Safari 27 beta adds three improvements to
ReadableStream
:
async iteration with
for await...of
const
response
=
await
fetch
(
"/data"
);
for
await
(
const
chunk
of
response
.
body
) {
process
(
chunk
);
}
the
ReadableStream.from()
static method for creating a stream from any async iterable or iterable
const
vegetables
=
[
"Carrot"
,
"Broccoli"
,
"Tomato"
,
"Spinach"
];
const
asyncIterator
=
(
async
function
*
() {
yield
1
;
yield
2
;
yield
3
;
})();
const
myReadableStream
=
ReadableStream
.
from
(
vegetables
);
const
asyncReadableStream
=
ReadableStream
.
from
(
asyncIterator
);
the ability to transfer a
ReadableStream
,
WritableStream
and
TransformStream
across contexts via
postMessage()
Additional bug fixes:
Fixed the parent window’s
history.state
being set to
null
when
history.pushState
is called from a child iframe. (50019069)
Fixed clicking on a scrollbar of an overflow container blurring the current
activeElement
. (92367314)
Fixed an issue where the
change
event was not fired on
<input>
and
<textarea>
elements when they lost focus while another application was in the foreground. (98526540)
Fixed Web IDL bindings to correctly reject
SharedArrayBuffer
where
[AllowShared]
is not specified. (107786134)
Fixed Content Security Policy to only recognize ASCII whitespace excluding vertical tabs to align with the specification. (108559413)
Fixed emoji input on Google Docs and similar web applications by supressing keypress events for supplementary characters. (122678873)
Fixed an issue where
MouseEvent.offsetX
and
MouseEvent.offsetY
were not relative to the padding edge as specified. (125763807)
Fixed an issue on visionOS where the
gamepadconnected
event did not fire unless gamepad permission had already been granted. (141623162)
Fixed an issue where
CSPViolationReportBody
did not include the source line number in Content Security Policy violation reports. (152607402)
Fixed an issue where selecting credentials in the Digital Credentials API sometimes required a second click to trigger verification. (163295172)
Fixed window bar visibility properties (
toolbar.visible
,
statusbar.visible
,
menubar.visible
) to return static values per the HTML specification for privacy and interoperability. (166554327)
Fixed handling of unknown
DigitalCredential
protocols by gracefully filtering them out and showing a console warning instead of throwing an error. (166673454)
Fixed: Updated the Digital Credentials API to rename
DigitalCredentialRequest
to
DigitalCredentialGetRequest
per the latest specification. (167115220)
Fixed an issue where Service Worker routes were not matched when no fetch event handler was set. (167753466)
Fixed spec conformance issues in the Streams API piping and abort behavior. (167841090)
Fixed Service Worker static routing rules to enforce limitation checks as required by the specification. (167977145)
Fixed
layerX
and
layerY
to return correct values with CSS transforms. (168968832)
Fixed
location.ancestorOrigins
returning stale origins after an iframe is removed from the document. (169097730)
Fixed
NavigateEvent.canIntercept
to correctly return
false
when navigating to a URL with a different port, aligning with the Navigation API specification. (169845691)
Fixed
NavigateEvent.navigationType
to return
"replace"
when navigating to a URL that matches the active document’s URL. (169999046)
Fixed an issue where the
dragend
event had incorrect coordinates when dragging within a nested
<iframe>
. (170750013)
Fixed an issue where
navigation.currentEntry.key
did not change in private browsing windows after calling history.pushState(). (171147417)
Fixed an issue where touch event properties values were sometimes swapped with neighboring values. (171567543)
Fixed a performance issue where
ResizeObserver
callbacks became increasingly sluggish over time. (172718139)
Fixed a performance issue where
IntersectionObserver
became sluggish over time when observing many elements due to O(n²) iteration. (172727210)
Fixed an issue where
navigation.currentEntry.id
did not change in private browsing windows after calling
history.replaceState()
. (172897962)
Fixed an issue where
document.open()
incorrectly aliased the caller’s security origin. (173369038)
Fixed an issue where
history.replaceState()
on a traversed history entry incorrectly changed
navigation.currentEntry.key
to a new UUID instead of preserving the original key. (173388766)
Fixed an issue where
Object.prototype
could not be serialized by
structuredClone()
. (173728983)
Fixed an issue where backslashes were not handled correctly in non-special URLs. (173757759)
Fixed a URL parsing bug in the special relative or authority state. (173772241)
Fixed an issue where event listener
once
and
passive
flags were not preserved when copying listeners between elements. (173834642)
Fixed: Preserved existing listener options (such as passive defaulting) when overwriting event handler attributes. (173842822)
Fixed the Credential Management API to properly define which credential types are allowed in the same
get()
request. (173918198)
Fixed an issue where
event.target
was not set after dispatching an event in a shadow tree with no listeners. (174136382)
Fixed an issue where
navigator.credentials.create()
and
navigator.credentials.get()
discarded the
AbortSignal
reason and always rejected with a generic
AbortError
. (174220589)
Fixed
Range.extractContents()
to not extract out-of-bounds nodes when the end container is removed during extraction. (174307275)
Fixed
document.createEvent()
to throw an exception for
"MutationEvents"
,
"MutationEvent"
,
"PopStateEvent"
, and
"WheelEvent"
, aligning with other browser engines. (174339775)
Fixed
ParentNode.append()
to correctly de-duplicate nodes when the same node is passed multiple times. (174365465)
Fixed an issue where
MutationObserver
delivered
childList
records in the wrong order when script ran during node insertion. (174368989)
Fixed an issue where setting a
URL
object’s
port
property to whitespace behaved incorrectly. (174484035)
Fixed a missing
return
in the Navigation API’s
performTraversal
that caused incorrect behavior when traversing to an unknown key. (174513305)
Fixed
Blob.slice()
to correctly clamp fractional
start
and
end
parameters using round-half-to-even rounding per the File API specification, which may change how edge-case fractional values like
0.5
are rounded. (174555334)
Fixed
postMessage()
to validate transferable object states after serialization, aligning with the HTML specification. (174558047)
Fixed
structuredClone()
and
window.postMessage()
to correctly throw a
DataCloneError
when serializing a
SharedArrayBuffer
outside of cross-origin isolated contexts. (174562553)
Fixed an issue where calling
Element.blur()
on an
<iframe>
did not reset
document.activeElement
to
<body>
. (174591529)
Fixed
document.styleSheets
to be accessible on documents created by
DOMParser
. (174625774)
Fixed
innerText
getter to correctly handle trailing newlines and blank lines for
<p>
elements and headings. (174642704)
Fixed
innerText
whitespace handling at inline-block boundaries. (174713114)
Fixed
XMLSerializer
namespace handling to correctly serialize elements with namespace prefixes. (174726401)
Fixed the
innerText
getter to preserve newlines for elements with
white-space: pre-line
. (174727341)
Fixed service worker registrations to be unregistered when the main script is missing. (174755909)
Fixed
innerText
handling of replaced elements at block boundaries. (174816319)
Fixed
EventSource
to be closed when
window.stop()
is called. (174830925)
Fixed service worker registrations to be unregistered when failing to retrieve stored imported scripts. (174833692)
Fixed calling
preventDefault()
during a
pointerdown
event to correctly suppress
mousedown
and
mouseup
events on iOS. (174864309)
Fixed innerText
to not fall back to
textContent
for elements with
display: contents`. (174883499)
Fixed
innerText
to preserve the contents of
<option>
elements inside
<select>
. (175006854)
Fixed
Element.innerText
to collect option text when called directly on a
<select>
element. (175156630)
Fixed worker scripts to always be decoded as UTF-8, as per the specification. (175327455)
Fixed an issue where an
Event
object’s
target
property could lose its JavaScript wrapper due to premature garbage collection. (175439759)
Fixed an issue where ancestors of
TreeWalker.currentNode
could be prematurely garbage collected. (175442228)
Fixed
FileSystemDirectoryHandle.resolve()
to return the correct path array for child entries. (175645387)
Fixed
PerformanceNavigationTiming.domInteractive
and
domContentLoadedEventEnd
incorrectly returning 0 instead of the correct timestamps. (175739835)
Fixed
FileSystemDirectoryHandle.removeEntry()
to correctly remove entries. (175745157)
Fixed
CryptoKey
to correctly remain associated with its secure context. (176157712)
Fixed: Improved cross-origin isolation enforcement for workers. (176175488)
Fixed
SharedArrayBuffer
cloning and agent cluster ID assignment. (176465817)
Rendering
srgb-linear and display-p3-linear
Safari 27 beta adds
srgb-linear
and
display-p3-linear
to predefined color spaces, making these linear-light color spaces available in Canvas, WebGL, and other APIs.
Subpixel inline layout
Subpixel inline layout is now available in Safari 27 beta. Text and inline elements can now be positioned with device-pixel precision, improving layout accuracy in block direction.
You don’t need to do anything to benefit. Layout engines have been moving in this direction for years; Safari 27 brings inline layout up to that bar.
Additional bug fixes:
Fixed an issue where a 2D canvas element unnecessarily forced a compositing layer. (172864747)
Fixed an issue where table cells with
rowspan
values exceeding the actual number of rows were incorrectly computing heights. (3209126)
Fixed an issue where
::first-letter
styles caused
Range.getClientRects()
and
Range.getBoundingClientRect()
to return incorrect dimensions. (71546397)
Fixed incorrect distributed height in table rows when a
<td>
element has an explicit height set. (78549188)
Fixed an issue where U+2028 LINE SEPARATOR was not rendered as a forced line break. (88470339)
Fixed an issue where a block formatting context with
margin-start
could overlap an adjacent float. (93187697)
Fixed
position: relative
on table rows (
<tr>
) to correctly establish a containing block for absolutely positioned descendants. (94294819)
Fixed
<marquee>
elements causing incorrect table width calculations. (99826593)
Fixed boxes in the top layer to use the initial containing block as their static-position rectangle. (155495104)
Fixed an issue where a flex item containing a percentage-height image did not shrink correctly around the image. (156902823)
Fixed an issue where form controls with
height: 100%
in auto-height containers incorrectly resolved to zero height. (161699543)
Fixed incorrect box sizing on inline elements when they have no siblings and their
padding-left
plus
margin-left
equals zero. (162376969)
Fixed a regression where an element inside an iframe gaining its own compositing layer could cause an iframe’s semi-transparent background to appear darker.(163509267)
Fixed an issue where space-taking scrollbars did not trigger a proper re-layout when the box size depends on content size. (166836126)
Fixed an issue where View Transition snapshots were incorrectly stored in sRGB, causing rendering issues with non-sRGB colors. (167634138)
Fixed an issue where font subpixel quantization was unnecessarily disabled in some cases, improving text rendering quality. (168088611)
Fixed table layout to properly handle
visibility: collapse
on columns. (168556786)
Fixed intrinsic sizing for absolutely positioned replaced elements. (168815514)
Fixed text being incorrectly truncated in RTL containers when combined with
text-overflow: ellipsis
and an
inline-block
pseudo-element. (168875614)
Fixed percentage padding in table cells to resolve against column widths. (168940907)
Fixed a regression where hovering over elements could leave repaint artifacts on the page. (169112402)
Fixed table height distribution to apply to tbody sections instead of only the first section. (169154677)
Fixed an issue where table sections with explicit heights did not properly constrain and distribute space among contained rows. (169235210)
Fixed an issue where images with
min-width: fit-content
rendered at an incorrect width. (169359566)
Fixed an issue where
height: 100%
was incorrectly calculated for replaced elements like images serving as grid items nested inside a flexbox. (169431440)
Fixed an issue where images were incorrectly stretched in certain page layouts. (170270187)
Fixed an issue where Find in Page scrolled to the wrong location when matching text inside elements with
user-select: none
. (170477571)
Fixed the baseline calculation for
inline-block
elements so that when
overflow
is not
visible
, the baseline is correctly set to the bottom margin edge. (170575015)
Fixed an issue where replaced elements did not correctly apply
min-height
and
min-width
constraints in certain configurations. (170765025)
Fixed an issue where overlay backgrounds would briefly dim incorrectly when de-compositing in a scrollable container. (171024685)
Fixed a regression where sticky-positioned elements inside overflow containers could appear in front of content that should overlap them. (171179878)
Fixed an issue where auto table layout did not honor
max-width
on table cells when distributing width between them. (171459245)
Fixed an issue where
border-spacing
incorrectly included collapsed columns in auto table layout calculations. (171468102)
Fixed an issue where percentage-height children of table cells with unresolvable percentage heights were not sized intrinsically. (171469500)
Fixed an issue where cell backgrounds in collapsed-border tables extended into adjacent cells’ border space at table edges. (172068907)
Fixed an issue where if a document in an iframe uses
@prefers-color-scheme
, it does not follow the
color-scheme
set by grandparents of the iframe. (172229372)
Fixed an issue where list item margins were computed incorrectly when the page was zoomed in or out. (172312498)
Fixed an issue where
about:blank
iframes did not always have a transparent background. (172400258)
Fixed an issue where a right-floated table could overlap another table. (172655655)
Fixed an issue where grid containers failed to avoid float boxes. (172655720)
Fixed an issue where an anonymous block created for list markers was not properly collapsed when block content prevented line-box parenting. (172686060)
Fixed an issue where checkboxes could overlap with adjacent text. (172741572)
Fixed an issue where checkbox outlines appeared misaligned. (172742551)
Fixed an issue where list markers rendered on the wrong line when list items started with empty inline elements. (172762578)
Fixed an issue where U+2029 PARAGRAPH SEPARATOR was not treated as a forced line break. (173106856)
Fixed an issue where tiles were missing after navigating back in history. (173288233)
Fixed an issue where view transition snapshots could capture stale transform values for accelerated CSS transform animations. (173323193)
Fixed an issue with outside list markers when blockification prevents line-box parenting. (173417560)
Fixed a regression where nested empty inline boxes accumulated an incorrect vertical offset, causing inline elements to stack as block-level elements. (173723162)
Fixed an issue where pseudo-elements were incorrectly included in outline rect collection. (174033087)
Fixed an inverted Y-axis comparison that could cause incorrect caret positioning. (174144220)
Fixed an issue where
<br>
elements with
line-height: 0
still created extra vertical space, failing to respect the declared line height. (174400946)
Fixed auto outlines to more closely follow the border radii of elements. (174466854)
Fixed how gradients are renderer to improve performance. (174880197)
Fixed
image-orientation
being ignored for
background-image
,
border-image
, and
list-style-image
. (174894122)
Fixed a
white-space: pre-wrap
layout issue with justified text. (174937310)
Fixed an issue where minimum height was not correctly computed for flex items. (174999995)
Fixed an issue with
flex-wrap
and flex factor computation for wrapping flex items. (175012395)
Fixed vertical
writing-mode
content incorrectly wrapping when the parent has
auto
height. (175123356)
Fixed minimum height calculation for flex items. (175195518)
Fixed incorrect bounding box position for newline characters. (175243361)
Fixed an issue where a child element with
filter: blur()
ignored
border-radius
overflow clipping from its parent. (175519148)
Fixed an issue where absolutely positioned tables with content exceeding their declared width were incorrectly positioned. (175755871)
Fixed height calculations for absolutely positioned tables with percentage-sized children. (175762381)
Fixed an issue where containers with block-in-inline content did not expand when
max-height
was removed. (175799547)
Fixed an issue where absolutely positioned tables with explicit percentage or fixed heights did not resolve correctly against their containing block. (175852400)
Fixed always-on scrollbar thumbs not rendering on the root element of nested documents with
display: flex
. (175866046)
Fixed absolutely positioned tables ignoring
min-height
and shrinking below their content height. (175883577)
Fixed absolutely positioned tables ignoring
max-height
constraints. (175932457)
Fixed
scrollbar-gutter
placement on the root element in RTL layouts. (175939512)
Fixed an issue where a flex item with
aspect-ratio
and
content-box
padding computed the wrong height in a column flex container. (176033726)
Fixed an issue where block-level boxes nested within inline elements were not properly aligned when using
align-content: center
. (176173122)
Fixed intrinsic sizing for non-replaced elements with percentage dimensions. (176493856)
Fixed an issue where panning a zoomed-in PDF on iOS would frequently rubber band back to the starting position. (156854435)
WebRTC
Safari 27 beta adds support for the
targetLatency
attribute in WebRTC, for specifying a target latency on a receiver. It adds support for the
RTCRtpCodec
dictionary and related constructs, improving the ability to inspect and configure codecs. It adds support for
RTCRtpReceiver.jitterBufferTarget
, for tuning the jitter buffer. And it adds video source
width
and
height
to RTC stats.
Additional bug fixes:
Fixed an issue where I420 BT709
VideoFrame
was encoded in an incorrect color space when encoding to VP9. (169425608)
Fixed an issue where
RTCPeerConnection.addIceCandidate()
did not reject when the connection was already closed. (170470988)
Fixed an issue where
RTCDataChannel
did not check the SCTP buffered amount synchronously. (172386678)
Fixed an issue where
MediaStreamTrack
could have incorrect settings if the source settings changed while the track was being transferred. (172657570)
Fixed an issue where a remote WebRTC track was not unmuted when the first packet was received. (172904930)
Fixed validation of RTC send encodings to better align with the specification. (172997814)
Fixed an issue where
RTCRtpSender.setParameters
did not clear parameters that were unset by the web application. (173678165)
Fixed WebRTC VP9 encoders to correctly propagate frame colorspace information. (174008548)
Fixed a regression where
RTCPeerConnection
with
iceTransportPolicy: "relay"
failed to gather ICE candidates. (174794660)
Fixed
RTCInboundRtpStreamStats.trackIdentifier
to match
MediaStreamTrack.id
. (174938984)
Web Extensions
The
runtime.getDocumentId()
Web Extension API now has support in Safari 27 beta. It adds reporting of uncaught JavaScript exceptions and unhandled promise rejections in Web Extension scripts, making extensions easier to debug. And it adds support for propagating user gestures through
sendMessage()
,
connect()
,
postMessage()
, and
executeScript()
— so extensions can reliably perform actions like media playback that require user activation.
Additional bug fixes:
Fixed
browser.i18n.getMessage()
to correctly substitute named placeholders when they appear adjacent to non-space characters. (169146196)
Fixed
browser.i18n.getMessage()
to correctly substitute two adjacent named placeholders. (175315700)
Fixed an issue where web extension service worker registration database files accumulated on each Safari launch, causing performance degradation. (175484888)
Networking
Secure cookies on loopback
Safari 27 beta adds support for
Secure
cookies on loopback hosts. For loopback hosts using plaintext HTTP, cookies marked
Secure
can now be set via JavaScript and
Set-Cookie
headers, matching the behavior of other browsers. This simplifies local development and testing with
Secure
cookies.
Additional bug fixes:
Fixed redirects to
data:
URLs to be blocked for subresources such as images and scripts, aligning with the Fetch specification. (74165956)
Fixed
XMLHttpRequest
incorrectly dropping the request body during redirects. (98459882)
Fixed
X-Frame-Options
to only strip tab or space characters, not vertical tabs. (126915315)
Fixed an issue where Safari’s address bar could display an internationalized domain name (IDN) homograph as a visually identical legitimate Latin domain, enabling potential phishing attacks. (166796168)
Fixed an issue where the preload scanner did not include integrity metadata in requests, causing incorrect Integrity-Policy violation reports. (168280745)
Fixed range request validation to properly handle HTTP 416 (Requested Range Not Satisfiable) responses. (168487440)
Fixed a regression where the referrer could be missing after a process-swap navigation. (169006635)
Fixed incorrect URL query percent-encoding when using non-UTF-8 character encodings such as
iso-8859-2
,
windows-1250
, and
gbk
. (169566553)
Fixed an issue where the multipart form data parser incorrectly required CRLF after the closing delimiter, causing some web applications to fail to render correctly. (174348783)
Fixed an issue where partitioned cookies could not be deleted via
WKHTTPCookieStore
. (174557252)
Storage
maxAge in the Cookie Store API
Safari 27 beta now supports specifying
maxAge
when setting a cookie via the Cookie Store API.
await
cookieStore
.
set
({
name
:
"session"
,
value
:
"abc123"
,
maxAge
:
60
*
60
*
24
*
7
, });
Additional bug fixes:
Fixed an issue where IndexedDB could incorrectly return a version 0 database after an abort during the initial
onupgradeneeded
event. (176195526)
Editing
Safari 27 beta now supports menu items that convert editable text between Simplified and Traditional Chinese characters, now available in the “Transformations” submenu of the context menu for relevant text selections.
Additional bug fixes:
Fixed an issue where characters styled with
::first-letter
were not selectable. (5688237)
Fixed font size 13pt being incorrectly mapped to
<font size="2">
(10pt) when using rich text editing. (15292320)
Fixed an issue where the Font Picker style selection became unusable after changing fonts when editing multiple lines of text. (110651645)
Fixed an issue where adjusting text selection with touch handles was prevented by JavaScript touch event handling on some websites. (151851274)
Fixed an issue where
execCommand('FormatBlock')
did not preserve inline styles of replaced block elements, causing text formatting to be lost when pasting content. (157657531)
Fixed an issue where
text-indent
flickered or was ignored on
contenteditable
elements while typing. (170280101)
Fixed an issue where text selection would jump unexpectedly when selecting absolutely-positioned content inside an element with
user-select: none
. (170475401)
Fixed an issue where text selection was lost when focus transitioned from a
contentEditable
element to a non-editable target. (171221909)
Fixed an issue where CJK encoding state was not reset appropriately during text decoding. (174649963)
SVG
Safari 27 beta adds support for the
lang
and
xml:lang
attribute in SVG. You can now specify the language of text content in SVG, enabling correct language-aware text rendering and accessibility announcements.
Additional bug fixes:
Fixed
offsetX
and
offsetY
for SVG elements to use the outermost SVG as the base for coordinate calculation. (168548585)
Fixed an issue where backslash-escaped dot characters in SVG animation timing attribute ID references were not parsed correctly. (94260935)
Fixed an issue where SMIL animations of
href
or
xlink:href
on SVG
<image>
elements had no visual effect. (96316808)
Fixed an issue where SVG animation did not clear the animated CSS property when
attributeName
was dynamically changed. (97097883)
Fixed
:visited
link color to properly propagate to SVG through
currentColor
. (98776770)
Fixed an issue where a CSS filter referencing an SVG filter via
url(#id)
was not invalidated when the filter content changed. (101870430)
Fixed SVG2 systemLanguage attribute to improve parsing and compliance with the specification. (116427520)
Fixed removing an item from
SVGTransformList
to properly allow attribute removal. (117840533)
Fixed an issue where the XML document parser did not defer inline script execution until pending stylesheets had loaded. (122574381)
Fixed an issue where animated SVG images referenced via an
<img>
tag did not animate correctly due to repaint artifacts with
object-fit
. (141815698)
Fixed an SVG
<tspan>
positioning bug with
xml:space="preserve"
that caused multi-line text to render incorrectly. (143722975)
Fixed an issue where SVG elements referencing non-existent filter IDs were not rendered. (164046592)
Fixed an issue where URL fragments were not percent-decoded before being used for SVG references. (169582378)
Fixed: Updated the default values of
fx
and
fy
attributes on
SVGRadialGradientElement
to
50%
to align with the SVG2 specification. (169645572)
Fixed
SVGAnimatedRect.baseVal
to ignore invalid values set on the
viewBox
attribute, such as negative width or height, aligning with Firefox and Chrome. (170214971)
Fixed SVG length attributes to reset to their default values when removed, rather than retaining previously set values. (170360351)
Fixed an issue where
getScreenCTM()
did not include CSS transforms and zoom contributions in the legacy SVG rendering path. (171525696)
Fixed an issue where an invalid attribute type in one SVG animation group prevented all subsequent animation groups from running. (172593109)
Fixed a regression where wheel events were not dispatched to an empty
<svg>
root element. (172909441)
Fixed an issue where SMIL
parseClockValue
did not reject out-of-range minutes and seconds values per the SMIL timing specification. (173577212)
Fixed the SMIL
values
attribute to preserve empty values and handle trailing semicolons. (173594455)
Fixed SMIL
repeat(n)
event conditions not triggering animations. (173599629)
Fixed SVG2
getStartPositionOfChar
and
getEndPositionOfChar
to be more compliant with the specification. (174145885)
Fixed
glyph-orientation-vertical: auto
to use UTR#50 Vertical Orientation properties for correct character orientation in vertical text. (175064567)
Fixed SVG intrinsic aspect ratio being incorrectly suppressed when
preserveAspectRatio
is set to
none
. (175173375)
Fixed SVG images without complete intrinsic dimensions incorrectly using ratio-based scaling for
background-size
. (175345107)
Fixed the SMIL clock value parser to accept hours greater than 99 and reject malformed seconds values. (175593583)
Fixed
stroke-dasharray
interpolation to use least common multiple for list length matching and corrected composition behavior. (175598175)
Fixed an issue where
@prefers-color-scheme
in an SVG image will sometimes not follow the system color preference. (176413340)
WKWebView
Safari 27 brings a significant expansion of WKWebView public API for native app developers. The additions make it easier to build advanced browser and web-hosting experiences on top of WebKit:
WKSerializedNode
— clone DOM nodes, including shadow roots, between different
WKWebView
instances.
WKJSHandle
— use JavaScript object references from native code.
WKContentWorldConfiguration
— configure content world properties such as autofill scripting, shadow root access, and inspectability when creating a
WKContentWorld
.
alternateRequest
and
overrideReferrerForAllRequests
on
WKWebpagePreferences
— modify the main resource request during navigation and apply custom referrer headers across all resource loads.
willSubmitForm
callback on
WKNavigationDelegate
— receive notification of HTML form submissions via a new
WKFormInfo
object.
mainFrameNavigation
on
WKNavigationAction
and
mainFrameNavigation
on
WKNavigationResponse
— correlate navigation actions and responses with each other and their originating loads.
WKWebView.load(url:)
— load a URL directly without wrapping it in an
NSURLRequest
.
WKHTTPCookieStore.cookies(for:)
— retrieve cookies matching a specific URL without fetching the entire cookie store.
Web Inspector
Several Web Inspector updates in Safari 27 beta make common debugging tasks easier.
The Color Picker now shows
color contrast information
inline as you edit — no more switching tools mid-decision to check whether a color combination is accessible. This works when you’re editing both foreground and background colors at the same time.
The Color Picker’s
format and gamut controls
are also now visible upfront instead of hidden. If you’ve ever gone hunting for those options, this will help.
In the Network tab, when a resource redirects, you can now see
every request in the chain
rather than just the final destination. It’s much easier to figure out what’s actually happening.
The Elements tab adds
Subgrid and Grid-Lanes badges
that make it easy to identify subgrid and grid-lanes layout contexts as you explore a page.
The Timeline tab now includes the
layout root element
in Layout event details, so you can see which element triggered a layout pass.
Additional bug fixes:
Fixed an issue where CSS properties added to new rules were not applied and were marked as invalid. (103548968)
Fixed an issue in the Network panel where the Request / Response menu did not remember the user’s previously selected value. (108231795)
Fixed editing inline
style
attribute values in the Elements panel resulting in truncated or malformed content. (149523483)
Fixed an issue where the input field for recording canvas frames in the Graphics tab was sometimes too small to type in and only allowed typing one character at a time. (157787230)
Fixed the Network tab filtering by resource type not working after clearing a filter that had no matches. (161570940)
Fixed an issue where CSS rules added via the “Add New Rule” button in the Styles panel were intermittently not applied or would vanish after entering a property. (164971557)
Fixed an issue where tree outlines in Web Inspector would intermittently show blank content while scrolling when a filter was active. (169502061)
Fixed an issue where an active recording in the Timelines tab would stop when navigating or reloading the current page even when the setting to stop recording once the page loads was turned off. (169732727)
Fixed an issue in the Timelines tab where rows containing object previews were sometimes not visible in the heap snapshot data grid. (170164522)
Fixed context menu items in the Elements tab to only display relevant options when multiple DOM nodes are selected. (170307979)
Fixed an issue where previewing resources in the Network tab displayed an error upon navigating away and Preserve Log was enabled. (171216835)
Fixed an issue where selected DOM node keys in a Map in the Scope Chain sidebar had unreadable white text on a light background. (171840122)
Fixed an issue where the WebAssembly debugger had no source bytes for modules compiled via
WebAssembly.instantiateStreaming
, preventing source-level debugging in LLDB. (174362152)
Fixed the WebAssembly debugger to generate human-readable module names from the WebAssembly name section and fetch URL, replacing bare address-based fallback names in LLDB’s image list. (174465437)
Fixed the Safari Develop menu and WebDriver to launch Device Hub instead of Simulator when available in Xcode. (174276041)
Fixed the Layers 3D view to correctly map textures to composited bounds and use proper selection highlighting instead of tinting textures. (174355052)
Fixed the Layers 3D view to re-snapshot preserved layers after a repaint instead of displaying stale textures. (174358757)
Fixed an issue where all folder tree elements were expanded after filtering for a resource in the Sources panel. (175009135)
Fixed an erroneous “There are unread messages that have been filtered” banner appearing in the Console when
console.groupCollapsed()
is used. (175279759)
Fixed an issue in the Storage tab where filtering by storage type did not reveal the popup with options. (175444192)
Fixed Timeline recordings showing unrelated events incorrectly nested inside longer events. (176309164)
Fixed Web Inspector toolbar buttons rendering at incorrect sizes. (176508343)
Accessibility
Fixed an issue where calling
speechSynthesis.cancel()
removed utterances queued by subsequent
speechSynthesis.speak()
calls. (46151521)
Fixed an issue where SVG
<use>
elements referencing
<symbol>
elements inside an
<img>
were incorrectly included as unnamed images in VoiceOver’s Images rotor. (98999595)
Fixed an issue where changing the
id
attribute of an element targeted by
aria-owns
did not update the accessibility tree. (107644248)
Fixed slot elements referenced by
aria-labelledby
to correctly use their assigned slotted content for accessible names and ignore hidden slotted nodes. (114500560)
Fixed
<meter>
element to have consistent labels between
aria-label
and
title
attributes. (127460695)
Fixed elements with
display: contents
and content in a shadow root to have their content properly read when referenced by
aria-labelledby
. (129361833)
Fixed
aria-labelledby
to use the checkbox name instead of its value when the checkbox name comes from an associated
<label>
element. (141564913)
Fixed VoiceOver cursor positioning for elements focused via the
drawFocusIfNeeded()
canvas API. (146323788)
Fixed grid elements with child rows in a shadow root to properly work with VoiceOver. (153134654)
Fixed an issue where VoiceOver read text within images that have
role="presentation"
. (159304061)
Fixed an issue where content within dynamically expanded
<details>
elements was not exposed in the accessibility tree. (159865815)
Fixed an issue where the
contextmenu
event was not fired for elements inside iframes when triggered by keyboard or assistive technology actions such as VoiceOver’s VO+Shift+M. (164128676)
Fixed an issue where changes to
<input type="button">
elements inside live regions were not announced by assistive technologies. (168200460)
Fixed
::first-letter
text not being exposed in the accessibility tree when no other text accompanies it. (168458291)
Fixed an issue where VoiceOver was unable to access
aria-owned
rows and their cells in grids and tables. (168770938)
Fixed an issue where VoiceOver could not find focusable splitter elements when navigating to the next or previous form control. (170187464)
Fixed an issue where color picker inputs could not be activated using VoiceOver’s press action. (172218114)
Fixed an issue where interactive elements containing an
<svg>
named by a child
<title>
element did not expose an accessible name. (172559238)
Fixed an issue where incorrect bounding boxes were computed for MathML table rows and cells. (172851295)
Fixed an issue where comboboxes did not forward focus to their
aria-activedescendant
, preventing assistive technologies from interacting with list items. (172931277)
Fixed an issue where
aria-owns
was not respected when computing the accessible name from element content. (173249317)
Fixed VoiceOver line-by-line reading skipping content in read-only documents. (174349841)
Fixed invalidation of aria-hidden=”true” when focus lands inside the aria-hidden subtree. (174449524)
Forms
Fixed an issue where keyboard commands such as paste did not work in form fields that restrict input to numbers. (4360235)
Fixed an issue where keyboard tabbing position was lost when a focused button became disabled, causing focus to jump to the beginning of the page. (120676409)
Fixed an issue where small range input slider thumbs were difficult to interact with on iPadOS and visionOS by expanding their touch hit area. (147428926)
Fixed
<datalist>
suggestions appearing with with white text on a white background in dark mode after typing. (168676757)
Fixed an issue on iOS where typing into an
<input>
element associated with a
<datalist>
was intercepted by type-to-select behavior. (173346270)
Fixed: Made the
<input type="checkbox" switch>
control behave more like other controls with regards to native appearance CSS properties. (173487610)
Fixed an issue where date and time input types without
min
or
max
attributes incorrectly matched the
:in-range
pseudo-class. (174829899)
Fixed an issue where cloned
<input>
and
<textarea>
elements did not preserve their user-modified state. (174892989)
Fixed
field-sizing: content
clipping the placeholder on number inputs that have no value. (175883299)
Printing
Fixed an issue where animations were ignored during print, causing missing content on animated pages. (36901701)
Fixed an issue where printing light text on a dark background with backgrounds disabled could result in invisible text. (170070133)
Fixed a regression where printing a WebView embedded in an enclosing
NSPrintOperation
dropped all text. (174756900)
Updating to Safari 27
Safari 27 beta is available on
Golden Gate (macOS 27)
,
iOS 27
,
iPadOS27
and
visionOS 27
.
To try Safari 27 beta, install the developer beta on your Apple device. You can also install
Safari Technology Preview
for macOS 27 beta and macOS 26.
Feedback
We love hearing from you. To share your thoughts, find our web evangelists online: Jen Simmons on
Bluesky
/
Mastodon
, Saron Yitbarek on
BlueSky
, and Jon Davis on
Bluesky
/
Mastodon
. You can follow WebKit
on LinkedIn
. If you run into any issues, we welcome your
feedback
on Safari UI (learn more about
filing Feedback
), or your
WebKit bug report
about web technologies or Web Inspector. If you run into a website that isn’t working as expected, please file a report at
webcompat.com
. Filing issues really does make a difference.
