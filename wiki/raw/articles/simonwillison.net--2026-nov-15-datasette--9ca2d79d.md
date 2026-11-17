---
title: "datasette 1.0a43"
url: "https://simonwillison.net/2026/Nov/15/datasette/"
fetched_at: 2026-11-16T10:18:28.392290+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette 1.0a43

Source: https://simonwillison.net/2026/Nov/15/datasette/

I've been leaning hard into Claude Fable 5.2 to help knock things off the
1.0 milestone
, which is now 53% complete.
The biggest 1.0 item in this release is
streaming support for output renderers
- the built-in TSV and CSV export mechanisms now use this as well, and plugins can register themselves as capable of streaming every row in a table in one go via the new
Response.stream()
method.
There are a couple of security fixes, one of which I deemed
deserving of a GitHub advisory
: private stored queries could be exposed, granting access to the title and SQL of the query (but not allowing that query to be executed).
There are dozens of smaller improvements. The row page JSON representation
finally has a design suitable for 1.0
. A new
<datasette-copy-button>
Web Component provides copy-schema in various places. JSON in columns on the row page can be pretty-printed. There's a new
DatasetteModal.confirm()
JavaScript utility method. Plus dozens of bug fixes, including contributions by
Zihan Dai
,
Peter Olkhovets
,
Ilya Khalafi
, and
Ankita Advitot
.
The feature I'm most excited about is a pretty tiny one: I've added CSS multi-page view transitions to Datasette!
Here's the commit
- key CSS is as follows:
/* Enable cross-document view transitions,
for anyone without prefers-reduced-motion */
@media
(
prefers-reduced-motion
:
no-preference
)
{
@view-transition
{
navigation
:
auto
;
}
}
/* .facet-results should morph from old position to new */
html
:
active-view-transition
.
content
>
.
facet-results
{
view-transition-name
:
facet-results
;
}
/* So should a .table-wrapper, provided it contains .rows-and-columns */
html
:
active-view-transition
.
table-wrapper
:
has
(
>
table
.
rows-and-columns
)
{
view-transition-name
:
rows-table
;
}
With that in place, navigations within Datasette - still staunchly a multi-page application - feel more like an SPA. This works on Safari and Chrome at the moment and I believe supports for Firefox is due to land in
Firefox 162
on December 8th 2026 (seeing as they are no longer feature-flagged in Firefox Nightly.)
