---
title: "A simple “copy this code” button in JavaScript"
url: "https://shkspr.mobi/blog/2026/08/a-simple-copy-this-code-button-in-javascript/"
fetched_at: 2026-08-30T10:01:00.998611+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# A simple “copy this code” button in JavaScript

Source: https://shkspr.mobi/blog/2026/08/a-simple-copy-this-code-button-in-javascript/

Next to all the code samples on this blog is a little "copy" button. That makes it easier to grab any of the code I've shared.
Copied HTML to 📋
Copied HTML to 📋
Copied HTML to 📋
Copied HTML to 📋
Copied JavaScript to 📋
Copied CSS to 📋
The HTML and JS is delightfully simple:
⧉
HTML
<
button
onclick
="navigator.clipboard.writeText(
        this.parentNode.getElementsByTagName('code')[0].textContent
    );"
title
="Copy code"
>⧉</
button
>
The
navigator.clipboard.writeText
needs a user interaction to work - so it is tied to a click on the button.
It takes some plaintext content. But how to get that content?  My code samples look like this:
⧉
HTML
<
pre
itemscope
itemtype
=https://schema.org/SoftwareSourceCode
translate
=no>
    <
button
onclick
="navigator.clipboard.writeText( this.parentNode.getElementsByTagName('code')[0].textContent );">⧉</
button
>
    <
span
>
        <
img
alt
height
=32
src
=html.svg
width
=32>
        <
span
itemprop
=programmingLanguage> HTML</
span
>
    </
span
>
    <
code
itemprop
=text>[…]</
code
>
</
pre
>
There are various ways I could get that
<code>
element:
Give it a unique ID (but that might clutter the code, or conflict with something else).
Use
this.nextSibling.nextSibling
(but that might not work if the layout changes).
Use
this.lastChild.textContent
(but, again, depends on the layout staying the same).
Select based on
itemprop
(could make the code a bit longer).
Complex filtering on a NodeList (urgh).
None of those are particularly bad
per se
, so I've chosen the method which makes most sense to me.
You can read more about my
Classless Design
, and how I use
metadata to identify programming languages
, including whether
HTML's code blocks be translated
.
To let people know that it has worked, I've added a little
popover
.
Every piece of code has it's own
dialog
element with a unique id:
⧉
HTML
<
dialog
id
=pop
popover
=hint>Copied JS to 📋</
dialog
>
No JavaScript is required to show the popover when the copy button is pressed:
⧉
HTML
<
button
popovertarget
=pop
popovertargetaction
=show>
Closing the the popover hint doesn't require JS; clicking outside it will dismiss it. But a little scrap of JS on the button's
onclick
will make it disappear after a few seconds:
⧉
JavaScript
setTimeout
(
function
() {
        document.
getElementById
(
"pop"
).
hidePopover
();
    }, 
3000);
The browser's default is to place it in the middle of the screen.
Positioning the popup so it is in proximity to the button also requires CSS - no JS.
⧉
CSS
dialog[popover]
{
inset
: unset;
position
: absolute;
padding
: .5em;
}
Although that might not work in Chrome or Safari.
OK, that started out simple but got a bit more complex. Sorry!
