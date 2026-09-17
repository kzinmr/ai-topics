---
title: "How to get a DOI for your blog posts"
url: "https://shkspr.mobi/blog/2026/09/how-to-get-a-doi-for-your-blog-posts/"
fetched_at: 2026-09-17T10:01:20.829517+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# How to get a DOI for your blog posts

Source: https://shkspr.mobi/blog/2026/09/how-to-get-a-doi-for-your-blog-posts/

Each new post on this blog now has a
Digital Object Identifier
. This post looks at the how and the why of getting one, whether it is useful, and any issues you might experience if you go down this path.
Background
Getting a DOI the easy way
Let's Go Rogue!
Automatic Submission of New Content
Manual Submission of Old Content
Getting the DOI
Generating your own DOI
Making the DOI discoverable in HTML
Downsides
Loss of Control
Tracking Citations
Licencing
Verification
Excluding Content
Deleting Content
Affiliations
More Vanity
Humility
Is it worth it?
A few years ago, I documented
how to to get an International Standard Serial Number for a blog
. An ISSN uniquely identifies a publication, which makes it easier for scholars and researchers to reference it. Getting one depends a little on whether a national institution is willing to accept your application.
Similarly, I also got an
ORCiD
which is used to uniquely identify researchers. That means it is possible to disambiguate "Einstein, A" the eminent physicist from "Einstein, A" a lovely chap called Allen who researches invasive slugs in Paraguay.
My blog posts are
regularly referenced in academic papers, books, conferences, and news articles
. The way most scholars cite a work is using a Digital Object Identifier. The idea is that a DOI is a unique and persistent code which can be used to refer to a specific article. If I ever stop using
shkspr.mobi
as my domain, or re-order my website,  the DOI can be redirected to the article's new home. Future scholars will be able to follow a reference more easily than hoping
https://example.com/article123
still exists.
If you're an academic, your institution will have a paid subscription to a service which will "mint" a new DOI for all your articles.
If not, you can upload your paper to a service like arXiv and they'll mint a DOI for you. That's how
I got a DOI for my MSc
.
What about people who aren't traditional academics or who want to keep their content on their own website? There are a variety of paid-for services, some of which charge an eye-watering amount of money to create a DOI for you.
Or, there's Rogue Scholar.
So what is
Rogue-Scholar.org
?
Rogue Scholar is an open access archive and registry for science blogs. It preserves science blog posts, makes them citable via DOI, and ensures their long-term discoverability alongside formal scholarly literature.
Nifty! My blog
just about
sneaks in to their "Computer Science" category. They require you to have a full-text feed of your posts. You also need to licence your content to them as Creative Commons Attribution.
Applying wasn't too difficult. I filled in their form, then jumped into their Slack. We had a bit of a discussion about what I needed to change in order to be approved.
A few days later, I was live at
https://rogue-scholar.org/communities/shkspr/
Which means, if you visit
https://doi.org/10.59350/395ha-fss97
you'll be redirected to one of my blog posts.
Rogue Scholar automatically polls my feed, ingests my content, and then mints a DOI for every new post they encounter. There's nothing manual I have to do.
That's all very well for new content. But I have posts on here going
way
back to 1986. How can they get discovered and DOI'd?
By default, Rogue Scholar ingested the 40 most recent posts from my blog. Actually, that's not quite accurate. It got the 40 most recently
updated
posts. As I'd recently edited a few older posts, they got themselves a DOI.
I don't know how often Rogue Scholar polls my blog's feed. In my experiments, adding a new post resulted in a DOI being issued a couple of minutes after publication.
At the moment, there doesn't seem to be an easy way to add older content. I'm working on a WordPress plugin to retroactively add DOIs and make them discoverable.
The Rogue Scholar API is based on
InvenioDRM
.
Retrieving the DOI via their API requires you to make an unauthenticated request to:
https://rogue-scholar.org/api/records?q=metadata.identifiers.identifier%3A%22https%3A%2F%2Fexample.com%2Fwhatever%22
That's your URl, wrapped in quotes, and the whole thing URl encoded.
Visit this example
.  You can also use your post's GUID.
That gets back a rather detailed JSON document. The DOI is noted in several locations, but is easiest to find in hits→hits→0→links→doi
It's important to note that
Rogue Scholar generates
two
DOIs for your post
. One for the post, another for the specific version of the post. If you update a post, it should get a new DOI. That way someone can refer to the post where you said your favourite band was the Spice Girls and not the edited one where you changed it to say B*Witched.
Alternatively, you can use the CrossRef search if you want to look at HTML results. See
this CrossRef example
.
As an aside, once you have the DOI, it's possible to create a
short
DOI at
https://shortdoi.org/
- I'll be honest, I've never seen these in the wild and
they are not recommended for use
.  Nevertheless, the API is pretty simple -
https://shortdoi.org/10.59350/395ha-fss97?format=json
will return a shorter URl like
https://doi.org/rnjj
Finally, there's a "vanity" DOI for the entire blog. In my case
10.59350/shkspr
.
Your blog posts can self-attest a DOI - when Rogue Scholar sees that in your Atom feed, it will register it on your behalf.
The code for generating a valid DOI
is relatively straightforward.
Generate a random number between 0 and 1,099,511,627,775.
Convert it to a Base 32 string.
Add a two character checksum to the end.
Prefix it with
10.59350/
Your new DOI can be made discoverable in your Atom feed by adding this to a post:
Copied XML to 📋
⧉
XML
<
id
>https://doi.org/10.59350/12345-67890</
id
>
Shortly after publication, it will be "minted" and be linkable.
How do you semantically add a DOI to your HTML's metadata?  By far the most popular citation manager is
Zotero
. They maintain
a page describing the metadata they look for
. According to them, this needs to be in your page's
<head>
:
Copied HTML to 📋
⧉
HTML
<
meta
name
=citation_doi
content
=10..../...>
They don't say whether it requires the
https://doi.org/
prefix - but looking at
Mendeley
and
AltMetric
, it appears not.
To use
DublinCore
, the
AltMetric recommended syntax
is:
Copied HTML to 📋
⧉
HTML
<
meta
name
=DC.Identifier
content
=doi:10..../...>
Within the HTML, there's no specific Microdata syntax, but
Schema.org recommends the
sameAs
property
. Something like:
Copied HTML to 📋
⧉
HTML
<
a
itemprop
="sameAs"
href
="https://doi.org/10.../...">10.../...</
a
>
OK, it isn't all flowers and kittens. There are a few things you ought to know before proceeding down this path.
For the IndieWeb / ReDeCentralise / Self-Hosing crowd, it's important to realise that DOI is a somewhat centralised services. Yes,
lots of different orgs can mint a DOI
, but as each ID has to be globally unique, doi.org sits in the middle as a benevolent gatekeeper.  If DOI.org went bust or became evil, all the
https://doi.org/10....
links would die. There are many other services like
DataCite
and
CrossRef
which can resolve a DOI - but it might turn out to be a bit fragile.
Similarly, if Rogue Scholar ever goes
properly
rogue then they can redirect my DOI to wherever they like. That level of control is useful if my site disappears; they can redirect to an archive. But if they get hacked, it could redirect somewhere unsavoury.
Having my site's content backed-up somewhere is useful but, again, without control or
verification
I worry that I might not be able to effectively manage it.
I use CSS to control the layout of my work but once it is archived as plain HTML or PDF, that formatting can disappear.
I don't know what will happen if I ever change DOI issuer.
I have a Google Scholar alert set up for my domain
shkspr.mobi
. That picks up people who make reference to this site. Hurrah! But, if they use
https://doi.org/10....
rather than
https://shkspr.mobi/...
I won't get alerted.
Luckily,
Rogue Scholar offer Citation Tracking
which
should
autopopulate their API with any backlinks from other sources. I'm yet to discover how that works in practice. I don't think it will give me an email alert though.
On a vanity issue, the DOI metadata shows the publisher of my posts as Rogue Scholar's parent organisation -
Front Matter
.
If you look at the API response from
https://api.crossref.org/works/10.59350/5ck9b-kjv69
you'll see something like:
Copied JSON to 📋
⧉
JSON
{
"message"
:
{
"institution"
:
[
{
"name"
:
"Front Matter"
}
]
,
"group-title"
:
"Terence Eden's Blog"
,
"publisher"
:
"Front Matter"
,
"DOI"
:
"10.59350/5ck9b-kjv69"
,
"author"
:
[
{
"ORCID"
:
"https://orcid.org/0000-0002-9265-9069"
,
"given"
:
"Terence"
,
"family"
:
"Eden"
}
]
}
}
Some citation managers will show the publication name as "Terence Eden's Blog" - others as "Front Matter".
Rogue Scholar has a hard requirement that all content be Creative Commons Attribution (CC BY). There's no ability (yet) to choose different licences. Personally, I prefer Attribution ShareAlike (CC BY-SA). I've allowed Rogue Scholar to use CC BY for my work which, of course, means if you get my posts through them you are also allowed to use CC BY.
If you get my work through my own website it is the slightly more restrictive CC BY-SA.
Does that make a practical difference? I don't know.
A DOI is persistent. That doesn't mean it is verifiable. If this blog ever goes offline the DOI will redirect to an archive - but there's no real way to tell that the text in that archive is accurate. There's no hashing or cryptographic signing. Yes, those things are rather brittle, but I think it would be helpful for the long-term integrity of citation chains.
Suppose there is content you
don't
want to receive a DOI, what do you do? You'll need to generate an RSS feed which excludes those specific posts.
For WordPress, you can do something like
/feed/atom/?cat=-1234
to exclude posts which have a category with the ID of 1234.
There are some filters on the Rogue Scholar site which you might also be able to use.
I don't think there's a way to delete or retract content from Rogue Scholar's DOI system yet. If you accidentally publish something you didn't mean to, it'll live on in the archives forever.
My ORCiD lists where I worked on certain dates. Initially, Rogue Scholar linked those to blog posts I wrote during my employment. However, all my posts were written in a personal capacity. It is possible to get those affiliations removed if they are inaccurate.
I initially tried generating DOIs like
edent-00f47
- although it's a valid Base 32 string with a checksum, it carries semantic meaning (my name) so shouldn't really be used. Ah well! Back to random strings.
Is this a valid use of the DOI ecosystem? A surprising number of my posts
have been referenced in academic papers
- but surely not
all
of my posts are worthy of getting a DOI? The problem is, I don't know when
a shitpost
will hit the zeitgeist and become quoted in papers, books, and articles.
It feels a bit self-indulgent and a little pretentious to mint a new DOI for every previous and future post on this site. But it isn't like the DOI system is running out of space, is it?
For me? Yes.
I think it is important that
scholarly blogs are properly referenced
. True, not
all
of my posts are cutting-edge research - but I'm always surprised which ones end up in someone's thesis or become part of a set-text.
I'm excited to see if this leads to an increase
or
decrease in my blog's visibility in academia.
If you have strong feelings either way about DOIs and/or blogs, please drop a comment in the box.
You may cite this post using
https://doi.org/10.59350/5ck9b-kjv69
😃
