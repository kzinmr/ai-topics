---
title: "Adding a new content type to my blog-to-newsletter tool"
url: "https://simonwillison.net/guides/agentic-engineering-patterns/adding-a-new-content-type/#atom-everything"
fetched_at: 2026-04-30T07:01:13.404940+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Adding a new content type to my blog-to-newsletter tool

Source: https://simonwillison.net/guides/agentic-engineering-patterns/adding-a-new-content-type/#atom-everything

Here's an example of a deceptively short prompt that got a quite a lot of work done in a single shot.
First, some background. I send out a
free Substack newsletter
around once a week containing content copied-and-pasted from my blog. I'm effectively using Substack as a lightweight way to allow people to subscribe to my blog via email.
I generate the newsletter with my
blog-to-newsletter
tool - an HTML and JavaScript app that fetches my latest content from
this Datasette instance
and formats it as rich text HTML, which I can then copy to my clipboard and paste into the Substack editor. Here's a
detailed explanation of how that works
.
I recently
added a new type of content
to my blog to capture content that I post elsewhere, which I called "beats". These include things like releases of my open source projects, new tools that I've built, museums that I've visited (from
niche-museums.com
) and other external content.
I wanted to include these in the generated newsletter. Here's the prompt I ran against the
simonw/tools
repository that hosts my
blog-to-newsletter
tool, using
Claude Code on the web
.
This got me the
exact solution
I needed. Let's break down the prompt.
Clone simonw/simonwillisonblog from github to /tmp for reference
I use this pattern a lot. Coding agents can clone code from GitHub, and the best way to explain a problem is often to have them look at relevant code. By telling them to clone to
/tmp
I ensure they don't accidentally end up including that reference code in their own commit later on.
The
simonw/simonwillisonblog
repository contains the source code for my Django-powered
simonwillison.net
blog. This includes the logic and database schema for my new "beats" feature.
Update blog-to-newsletter.html to include beats that have descriptions - similar to how the Atom everything feed on the blog works
Referencing
blog-to-newsletter.html
is all I need here to tell Claude which of the 200+ HTML apps in that
simonw/tools
repo it should be modifying.
Beats are automatically imported from multiple sources. Often they aren't very interesting - a dot-release bug fix for one of my smaller open source projects, for example.
My blog includes a way for me to add additional descriptions to any beat, which provides extra commentary but also marks that beat as being more interesting than those that I haven't annotated in some way.
I already use this as a distinction to decide which beats end up in my site's
Atom feed
. Telling Claude to imitate that saves me from having to describe the logic in any extra detail.
Run it with python -m http.server and use `uvx rodney --help` to test it - compare what shows up in the newsletter with what's on the homepage of https://simonwillison.net
Coding agents always work best if they have some kind of validation mechanism they can use to test their own work.
In this case I wanted Claude Code to actively check that the changes it made to my tool would correctly fetch and display the latest data.
I reminded it to use
python -m http.server
as a static server because I've had issues in the past with applications that fetch data and break when served as a file from disk instead of a localhost server. In this particular case that may not have been necessary, but my prompting muscle memory has
python -m http.server
baked in at this point!
I described the
uvx rodney --help
trick in
the agentic manual testing chapter
. Rodney is browser automation software that can be installed using
uvx
, and that has
--help
output designed to teach an agent everything it needs to know in order to use the tool.
I figured that telling Claude to compare the results in the newsletter to the content of my blog's homepage would be enough for it to confidently verify that the new changes were working correctly, since I had recently posted content that matched the new requirements.
You can see
the full session here
, or if that doesn't work I have an
alternative transcript
showing all of the individual tool calls.
The
resulting PR
made exactly the right change. It added an additional UNION clause to the SQL query that fetched the blog's content, filtering out draft beats and beats that have nothing in their
note
column:
...
union
all
select
id
,
'beat'
as
type
,
title
,
created
,
slug
,
'No HTML'
as
html
,
json_object
(
'created'
,
date
(
created
),
'beat_type'
,
beat_type
,
'title'
,
title
,
'url'
,
url
,
'commentary'
,
commentary
,
'note'
,
note
)
as
json
,
url
as
external_url
from
blog_beat
where
coalesce
(
note
,
''
)
!=
''
and
is_draft
=
0
union
all
...
And it figured out a mapping of beat types to their formal names, presumably derived from the
Django ORM definition
that it read while it was exploring the reference codebase:
const beatTypeDisplay = {
  release: 'Release',
  til: 'TIL',
  til_update: 'TIL updated',
  research: 'Research',
  tool: 'Tool',
  museum: 'Museum'
};
Telling agents to use another codebase as reference is a powerful shortcut for communicating complex concepts with minimal additional information needed in the prompt.
