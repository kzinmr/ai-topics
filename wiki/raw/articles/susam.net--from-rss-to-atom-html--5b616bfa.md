---
title: "From RSS to Atom"
url: "https://susam.net/from-rss-to-atom.html"
fetched_at: 2026-05-04T07:01:09.874458+00:00
source: "susam.net"
tags: [blog, raw]
---

# From RSS to Atom

Source: https://susam.net/from-rss-to-atom.html

From RSS to Atom
By
Susam Pal
on 04 May 2026
Yesterday, I switched my website from RSS feeds to Atom feeds.  In
  case you are wondering whether you have somehow landed on an ancient
  post from 2010, no, you have not.  Yes, this is the year 2026, and I
  have finally switched from RSS feeds to Atom feeds.  Yes, I am
  fifteen, or perhaps twenty, years too late.
Contents
Impulse Coding
I have always wanted to do this but could never make the time for
  it.  Finally, it happened while I was giving my brain some rest from
  my
ongoing
algebraic graph theory studies.
  That's when I felt like spending a little time on my website and
  doing a little Lisp to change the feeds from RSS to Atom.  I suppose
  this was
impulse coding
, a bit like impulse buying, except
  that I ended up with an Atom feed instead of a new book.
I find it quite surprising that when I have plenty of time, it
  usually does not occur to me to do these things, but when I am too
  busy and really short of time, these little ideas possess me during
  the short breaks I take.  My personal website is one of my passion
  projects.  Common Lisp is one of my favourite programming languages.
  So any time spent on this passion project using my favourite
  programming language is a very relaxing experience for me.  It
  serves as an ideal break between intense study sessions.  It took
  about an hour to implement the changes needed to make the switch
  from RSS to Atom.  In the end, I could go back to my studies
  reinvigorated.
In case you are curious, here is the Git commit where I implemented
  the change from RSS to Atom:
596e1dd
.
  As you might notice, a large portion of the change consists of
  replacing the
key
attribute in each post with
  the
uuid
attribute.  The
key
attribute
  value was used as the value of the
<guid>
element
  in the RSS feeds.  While an arbitrary short string could serve as
  the
<guid>
element for the items in an RSS feed,
  the
<id>
element of the entries in an Atom feed
  needs to be a URI.  It turns out UUID URNs are a common choice for
  such a URI.  I ran the following shell command to replace all
  occurrences of the
key
attribute
  with
uuid
:
find . -type f -name '*.html' -exec sh -c '
  for f do
    sed "s/^<!-- key: .* -->/<!-- uuid: $(uuidgen) -->/g" "$f" > tmp &&
    mv tmp "$f"
  done
' sh {} +
The rest of the changes went into the
feed
templates
and the Common Lisp
program
that statically generates the feeds along with the website.
For examples of the resulting feeds, see
feed.xml
and
absurd.xml
.  The first is the main
  website feed and the second is an example of a tag-specific feed.
  Yes, the aforementioned Common Lisp program generates a feed for
  each
tag
.  As of today, the main feed
  at
feed.xml
contains only two entries even
  though this website has over
200 pages
.  I
  explain the reason later in
Temporary Workaround
.
Atom Entries
Here is an example Atom entry from my feeds:
<entry>
  <title>A4 Paper Stories</title>
  <link href="https://susam.net/a4-paper-stories.html"/>
  <id>urn:uuid:06e5304d-c242-481c-bf94-e23b019b0a36</id>
  <updated>2026-01-06T00:00:00Z</updated>
  <content type="html">
    &lt;p&gt;I sometimes resort to a rather common measuring ...
  </content>
</entry>
The ellipsis (
...
) denotes content I have omitted for
  the sake of brevity.
I like how each entry in the feed now has its own UUIDv4.  I also
  like that timestamps in an Atom feed are in the
date-time
format specified in
RFC 3339
,
  which also happens to be a profile of ISO 8601.  Further, I like
  that I can explicitly declare the content type to be HTML.  Commonly
  used values for the content type attribute are
text
,
html
and
xhtml
.  If it is
html
, the content should be escaped HTML.  If it is
xhtml
, the content should be an
  XHTML
<div>
element containing valid XHTML.
  Explicit content type support is likely the biggest advantage of
  Atom over RSS.  In comparison,
RSS 2.0
does not specify any way to declare the content type.  So feed
  readers have to inspect the content and guess what the content type
  might be.
Temporary Workaround
As I mentioned before, as of today, the
main feed
contains only two entries.  That's
  because only new posts published since the migration to Atom are now
  included in the feed.  This was done to avoid spamming subscribers.
  The Atom specification's requirement that each entry's ID must be a
  URI has caused the IDs of every entry to change.  If I were to
  include the older posts from before the change in the feed, then
  those posts would appear as new unread items.  Subscribers can find
  this quite annoying.  In fact, I have received a few
complaints
about this in the past.  So I was careful this time.  I have a little
one-liner
  workaround
in my site generator to exclude posts published before
  this change from the feed.
That was the only workaround I had to implement.  Fortunately, my
  feed file had a neutral name like
feed.xml
, rather than
  a format-specific name like
rss.xml
, so I could avoid a
  URL change and the subsequent overhead of setting up redirects.
Does It Matter?
Does any of this matter today?  I think it does.  Contrary to the
  recurring claim that RSS and Atom are dead, most of the traffic to my
  personal website still comes from web feeds, even in 2026.  Every
  time I publish a new post, I can see a good number of visitors
  arriving from feed readers.  From the referrer data in my web server
  logs (which is not completely reliable but still offers some
  insight), the three largest sources of traffic to my website are
  web feeds, newsletters and search engines, in that order.
On the topic of newsletters, I was surprised to discover just how
  many technology newsletters there are on the Web and how active
  their user bases are.  Once in a while, a newsletter picks up one of
  my silly or quirky posts, which then brings a large number of visits
  from its followers.
Back to the topic of web feeds, there is indeed a decent user base
  around RSS and Atom feeds.  A good number of visitors to my website
  arrive by clicking a feed entry that shows up in their feed
  reader.  I know this with some confidence by looking at
  the
referer
(sic) headers of visits to my HTML pages
  and the subsequent browsing of the website, as opposed to the
  isolated and automated fetches of the XML feeds.  So there must be a
  reasonably active base of users around web feeds.  It is a bit like
  being part of an invisible social network that we know exists and
  that we can measure through indirect evidence.
References
I found these three resources useful while switching to Atom feeds:
