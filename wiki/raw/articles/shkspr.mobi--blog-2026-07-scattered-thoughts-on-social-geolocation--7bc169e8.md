---
title: "Scattered thoughts on social geolocation"
url: "https://shkspr.mobi/blog/2026/07/scattered-thoughts-on-social-geolocation/"
fetched_at: 2026-07-24T10:13:56.787294+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Scattered thoughts on social geolocation

Source: https://shkspr.mobi/blog/2026/07/scattered-thoughts-on-social-geolocation/

I want to be able to
share my location with my friends
on social media. Twitter (RIP) had a way to attach an optional location to a post. Facebook still lets me check in to venues. But neither ActivityPub (Mastodon) nor AT Protocol (BlueSky) allow me to do that.
I've been
banging on about this for a while
so was delighted to be invited to chat with the
GeoSocial Task Force
on
their monthly call
.
But, before I start, please remember that these proposals are not mandatory. If you don't want to share your location, then please don't share your location. This is an optional feature which shouldn't be used by people with a strong need for privacy.
We were primarily discussing the nascent
Geographical Microsyntax proposals
.
Firstly, I
love
the idea of being able to share my location. I want my friends to know I'm in town for a gig. I want people to think I'm cool because I'm seeing some experimental theatre. I want to virtue signal that I'm giving blood.
Similarly, I want to be able to find social media posts by location. What's happening right now in Paris? Did anyone else hear that sonic boom in London? Which cool people are also at this gig with me?
But, I do think these proposals have some issues which need to be addressed.
The primary thing missing from the proposal is any form of understanding what users want to do with a geotagged post.
You see a post like:
Hanging out with friends. I just checked in to
Leicester Square
.
What do you expect to happen when you click that link?
See who is at the location?
Read more information about the place being discussed?
Find all posts at that specific address?
Discover posts which are
close
to there?
Something else?
What other things do people want to do with geotagged posts?
Find all posts within 5Km of me?
Discover users who have posted near me?
Get emergency alerts for the city I'm in?
See what's trending in a specific country?
Without knowing what people might want to do with this information, it's rather hard to design a service which meets their needs.
Where I disagree with the proposals is the idea of using inline text as a form of microsyntax.
Proposals like "I am in /London/ eating ice-cream" or "Checked in to Leicester Square L:N123456" fail for a couple of reasons.
Things like #hashtags and @mentions developed organically on social networks before they were eventually adopted by the platforms themselves. It is rare that a top-down diktat can be used to tell people how they
should
be formatting their posts.
More importantly, people are
crap
at formatting things consistently! Every event I go to has people using
#Event
alongside
#Event2026
or
#Event26
or a hundred variations.
Even if users could format it consistently, names are ambiguous. Is
🌐:Paris
the one in France or
Texas
?
I'm strongly of the opinion that text is for text, not syntax.
Saying that you're on a specific point on the globe doesn't always provide useful information. Even with altitude, it isn't always possible to work out if your in the Starbucks or the Costa next door. Do you want to say you're in a train station, or a distinct platform, or even a specific train journey?
There are various services which offer unique IDs per loosely-defined place.
Google Maps provides a
Place ID
for every thing that it knows about. There's a similar service from
FourSquare
.  But both of those are closed and proprietary systems - they can only be updated by the company that creates them.
Wikipedia's Wikidata has
IDs for lots of places
, similarly OpenStreetMap has
nodes with names
which can be used to identify locations.
But all of these suffer from the same flaw; they are centralised.
If
Google kills its service
then all those Place IDs die.
This has happened before. Yahoo used to run the
Where On Earth IDentifier
service but discontinued it.
While OSM and Wikipedia are great projects, they're still centralised. If you're banned from OSM, you can't create a new node.
So, to my mind, the
primary
way of identifying a place has to use a fully open, globally agreed, and unrestricted standard.
The obvious choice is latitude and longitude as defined by
WGS 84
. It allows for arbitrary precision anywhere on the planet.
No one can stop you issuing lat/long just because a country is under sanctions. The standards community can't revoke your access to it. The co-ordinates are well understood by almost all software.
There are some alternatives. Google's
Plus.Codes
build on top of lat/long to make something more human readable. But, crucially, human readability is
not
the issue here. This is metadata which should never be shown to a human. If a user interface wants to format a lat/long they can do so as a Plus.Code or any other format.
There are dozens of
competing ways to mark up a location
.
It seems sensible to me that, given most major social media protocols use JSON, adding
GeoJSON
would be the simplest way to add geographic information to a post's metadata.
At its most basic, a single "Point" can be shared like so:
⧉
JSON
{
"type"
:
"Feature"
,
"geometry"
:
{
"type"
:
"Point"
,
"coordinates"
:
[
-0.13005,51.5103
]
}
}
It can have as much or as little precision as needed.
If the place being checked into has a name, it can also be added - this could be used for display purposes within the message
⧉
JSON
{
"type"
:
"Feature"
,
"geometry"
:
{
"type"
:
"Point"
,
"coordinates"
:
[
-0.13005,51.5103
]
}
,
"properties"
:
{
"name"
:
"Leicester Square"
}
}
The
properties
can be as complex as the sender wants. For example it could add Wikidata references, OpenStreetMap IDs, telephone numbers, or some cool new thing which hasn't been invented yet.
Here's a maximalist example of checking in to a park:
⧉
JSON
{
"type"
:
"Feature"
,
"geometry"
:
{
"type"
:
"Polygon"
,
"coordinates"
:
[
[
[
-0.1303791,51.5099976
]
,
[
-0.1295305,51.5100444
]
,
[
-0.1297077,51.510947
]
,
[
-0.1308786,51.5105859
]
,
[
-0.1308893,51.5105793
]
,
[
-0.1303791,51.5099976
]
]
]
}
,
"properties"
:
{
"name"
:
"Leicester Square"
,
"WikiData"
:
"Q848912"
,
"OSM"
:
"4082589"
,
"GooglePlaceID"
:
"ChIJPcTFENIEdkgR94E58rgB69o"
,
"PlusCode"
:
"9C3XGV69+4X"
,
"Quinfrob"
:
"🌐89451_𰻝"
,
"address"
:
{
"road"
:
"Leicester Square"
,
"neighbourhood"
:
"St. James's"
,
"quarter"
:
"East Marylebone"
,
"suburb"
:
"Covent Garden"
,
"city"
:
"City of Westminster"
,
"ISO3166-2-lvl8"
:
"GB-WSM"
,
"state"
:
"England"
,
"ISO3166-2-lvl4"
:
"GB-ENG"
,
"postcode"
:
"WC2H 7NA"
,
"country"
:
"United Kingdom"
,
"country_code"
:
"gb"
}
}
}
My personal opinion is that the following needs to happen:
Talk to some users - find out what they might use this for.
Work with privacy advocates to reduce possible harms (for example, being able to redact a location from a previously shared post).
Discuss with developers about how they'd work with this metadata.
Clients should start adding GeoJSON metadata to their posts, even if it can't be displayed yet.
You can
read the minutes of the meeting
and I'd encourage you to
join the next call
.
