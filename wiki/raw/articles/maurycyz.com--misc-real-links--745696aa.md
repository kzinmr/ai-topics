---
title: "Please don't mess with links:"
url: "https://maurycyz.com/misc/real_links/"
fetched_at: 2026-06-01T07:14:10.398320+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Please don't mess with links:

Source: https://maurycyz.com/misc/real_links/

Please don't mess with links:
2026-05-31
(
Rants
) (
Web sites
)
A link is just a button that takes you somewhere when you click it right?
<
style
>
span
{
text-decoration
:
underline
;
color
:
#44EEEE
;
}
</
style
>
<
span
onclick
=
"window.location='https://xkcd.com/'"
>100% legit link</
span
>
100% legit link
Except that's a pale, shallow imitation of a link.
A real link can be:
Opened in a new tab. (ctrl)
... or a fresh window. (shift)
... or saved as a file (alt).
Copied as a URL (right click)
Used with the keyboard (tab + enter)
Seen by tools like search engines and screen readers.
Hovered over to see the URL.
... none of which work with a button.
Another common offense
is to use a real link, but hook the click event to open a popup.
However, with a real <a target="_blank"> link, I can:
See the loading progress...
... or/and cancel it.
... see descriptive error pages and retry if needed.
Open multiple at once.
Read the original page while it loads.
Use my browser's tabs or/and window manager to organize them.
Bookmark the page.
Copy the URL and send it to a friend.
... and above all, they are consistent:
I've long lost count of how many times I've accidentally closed the whole site while trying to close a popup that was a little too convincing.
It's also extremely common to click a link with a slow connection, only to be greeted with perpetual spinner.
I have no idea if anything is actually happening or how long it will take.
Worse, it usually covers up the original page so I can't even read that!
Browsers are good at links and loading pages: It's the whole point.
Don't use javascript buttons as links.
Don't build your own loading animations.
Link previews should open and close on hover, not on click.
Don't open links in javascript popups: Use target="_blank" instead.
Other common problems
:
Infinite scrolling breaks ctrl-f, bookmarks, the home/end keys and often the back button.
You can have a 100k of text on a page:
Browsers will render partially downloaded HTML and the user won't even notice.
Using a 5 MB javascript framework just do a worse job of downloading text is dumb.
To optimize speed, it's best to minimize the total number of round trips.
Just putting everything in a single TCP connection will always be better than breaking it up because of TCP's slow start algorithm.
Don't reimplement <details>
which will break search tools and screen readers.
... but using fancy CSS to make it look nice is fine.
Don't roll your own date picker
(or any other built-in form inputs)
This will always used the user's preferred date format, covert it to the standard yyyy-mm-dd, and works with the keyboard...
also, it's one line of code that works with dark mode by default.
Related
:
Real links!
