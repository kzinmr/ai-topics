---
title: "Using FourSquare’s API to post location checkins to social media"
url: "https://shkspr.mobi/blog/2026/06/using-foursquares-api-to-post-location-checkins-to-social-media/"
fetched_at: 2026-06-03T07:01:41.467315+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Using FourSquare’s API to post location checkins to social media

Source: https://shkspr.mobi/blog/2026/06/using-foursquares-api-to-post-location-checkins-to-social-media/

What is this, 2016?
I like sharing my location with my pocket friends sometimes. If I'm in a cool bar that they know, perhaps they can recommend a drink. If they live nearby, maybe they want to come for dinner. Not everyone has FourSquare's SwarmApp, so it is handy to automatically share its updates with other people.
Of course, Swarm doesn't cross-post to social media because walled-gardens are the most profitable. This is my attempt to open it back up again.
Here's what they look like on BlueSky and Mastodon:
Checked in to Hamburger Fischmarkt, Große Elbstr. 9 (Fischmarkt), Germany

Probably a *bit* early for a breakfast beer.
See on Swarm
[image or embed]
— Terence Eden (
@edent.tel
)
24 May 2026 at 07:45
Post by @Edent@mastodon.social
View on Mastodon
You can
get the SwarmToSocial code from my GitLab
.
At the moment, developers get
10,000 API calls for free each month
. That's probably more than enough for most personal uses.
I was pleasantly surprised that
FourSquare's CheckIn documentation
was fairly easy to use and understand.
Once you've
signed up for a developer account
you can create an OAuth app. That will generate a Client ID (
ABC123
), Client Secret (
XYZ789
), and you supply a Project URL.
Once done you can
follow the Authentication documentation
. Or just visit:
⧉
https://foursquare.com/oauth2/authenticate?
   client_id=ABC123
  &response_type=code
  &redirect_uri=https://example.com/
Sign in with your FourSquare account. It will redirect you to:
https://example.com/?code=456QWE
Use that code to construct the final URl:
⧉
https://foursquare.com/oauth2/access_token?
   client_id=ABC123
  &client_secret=XYZ789
  &grant_type=authorization_code
  &redirect_uri=http://example.com/
  &code=456QWE
That will respond with the Access Token:
⧉
JSON
{
"access_token"
:
"asdfghjkl123456"
}
Hurrah! Posting a new checkin is
relatively
simple. POST to this URl with a header of
accept: application/json
⧉
https://api.foursquare.com/v2/checkins/add?
   v=20260223
  &venueId=13600425
  &shout=This%20is%20a%20test
  &oauth_token=asdfghjkl123456
v
is, rather confusingly, a date.
The versioning documentation
has more details but, basically, set it to the date you deployed your app.
venuId
you'll need to find yourself (more on that later).
shout
is up to 140 characters (!) of URl encoded text.
That will send back rather a lot of JSON. Here are the important bits:
⧉
JSON
{
"meta"
:
{
"code"
: 200,
"requestId"
:
"123456789"
}
,
"response"
:
{
"checkin"
:
{
"id"
:
"987654321"
,
"createdAt"
: 1771843820,
"type"
:
"checkin"
,
"visibility"
:
"closeFriends"
,
"shout"
:
"This is a test of the API"
,
"timeZoneOffset"
: -300,
"editableUntil"
: 1771930220000,
"user"
:
{
"id"
:
"56367"
,
"firstName"
:
"Terence"
,
"lastName"
:
"Eden"
,
"relationship"
:
"self"
,
"displayName"
:
"Terence Eden"
}
,
"venue"
:
{
"id"
:
"QWERTYUIOP"
,
"name"
:
"My Birthday Party!"
,
"contact"
:
{
}
,
"location"
:
{
"isFuzzed"
: true,
"lat"
: 39.123456789,
"lng"
: -84.987654321,
"cc"
:
"US"
,
"city"
:
"Cincinnati"
,
"state"
:
"KY"
,
"country"
:
"United States"
,
"formattedAddress"
:
[
"Cincinnati, KY"
,
"United States"
]
}
}
,
"checkinShortUrl"
:
"https://swarmapp.com/user/56367/checkin/987654321?s=wRZ7ByNfCW1DNrOIpsRcytPZelE"
}
}
}
For my purposes, the
shout
and
checkinShortUrl
are the most important. You can view a sample check in:
https://swarmapp.com/user/56367/checkin/699c34b55bad6b7fb1695544?s=LA7jCaAtH-s9CwSpgQrQdHrP5-8
If you're already using
a service like Untappd
you might be able to get the venue ID from that.
If not, FourSquare provides
100 million points of interest
for free - although with
questionable data quality
.
Alternatively, you can
search by location
:
⧉
curl --request GET \
     --url 'https://places-api.foursquare.com/places/search?ll=51.123%2C0.123&radius=1000&sort=POPULARITY' \
     --header 'X-Places-Api-Version: 2025-06-17' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer ABC123'
As far as I can see, the
Bearer Token
only exists
on the documentation page
. I couldn't find it in my developer console. Weird!
That gets you back:
⧉
JSON
{
"results"
:
[
{
"fsq_place_id"
:
"4be584ed2457a593ad8cab15"
,
"latitude"
: 51.11783041264215,
"longitude"
: 0.11219274871133413,
"categories"
:
[
{
"fsq_category_id"
:
"4bf58dd8d48988d1fa941735"
,
"name"
:
"Farmers Market"
,
"short_name"
:
"Farmers Market"
,
"plural_name"
:
"Farmers Markets"
,
"icon"
:
{
"prefix"
:
"https://ss3.4sqi.net/img/categories_v2/shops/food_farmersmarket_"
,
"suffix"
:
".png"
}
}
]
,
"date_created"
:
"2010-05-08"
,
"date_refreshed"
:
"2025-11-01"
,
"distance"
: 970,
"extended_location"
:
{
}
,
"link"
:
"/places/4be584ed2457a593ad8cab15"
,
"location"
:
{
"address"
:
""
,
"locality"
:
"Hartfield"
,
"region"
:
"East Sussex"
,
"postcode"
:
""
,
"admin_region"
:
"England"
,
"country"
:
"GB"
,
"formatted_address"
:
"Hartfield, East Sussex"
}
,
"name"
:
"Perryhill Farm Shop"
,
"placemaker_url"
:
"https://foursquare.com/placemakers/review-place/4be584ed2457a593ad8cab15"
,
"related_places"
:
{
}
,
"social_media"
:
{
"twitter"
:
""
}
,
"tel"
:
""
,
"website"
:
"http://www.perryhillorchards.co.uk/index.php?sec=4"
}
,
{
"fsq_place_id"
:
"8896f77565e54a658585301d"
,
"latitude"
: 51.11649,
"longitude"
: 0.13131,
"categories"
:
[
]
,
"date_created"
:
"2021-12-06"
,
"date_refreshed"
:
"2021-12-06"
,
"distance"
: 909,
"extended_location"
:
{
}
,
"link"
:
"/places/8896f77565e54a658585301d"
,
"location"
:
{
"address"
:
"Priory Park, Beech Green Lane"
,
"locality"
:
"Withyham"
,
"region"
:
"East Sussex"
,
"postcode"
:
"TN7 4DB"
,
"admin_region"
:
"England"
,
"post_town"
:
"Hartfield"
,
"country"
:
"GB"
,
"formatted_address"
:
"Priory Park, Beech Green Lane, Withyham, East Sussex, TN7 4DB"
}
,
"name"
:
"Spectra Studios"
,
"placemaker_url"
:
"https://foursquare.com/placemakers/review-place/8896f77565e54a658585301d"
,
"related_places"
:
{
}
,
"social_media"
:
{
}
,
"tel"
:
"01892 487149"
}
,
]
,
"context"
:
{
"geo_bounds"
:
{
"circle"
:
{
"center"
:
{
"latitude"
: 51.123,
"longitude"
: 0.1234
}
,
"radius"
: 1000
}
}
}
}
You can manually check a place using the Placemaker site:
https://foursquare.com/placemakers/review-place/64eca80f0398c97ab52298ec
What if you've checked in to a place using the official Swarm app? How do you get your own recent checkin data?
Again, there is
documentation on getting user checkins
.
⧉
Bash
curl --request GET \
     --url 'https://api.foursquare.com/v2/users/self/checkins?v=20260223&limit=2&offset=0&oauth_token=asdfghjkl123456' \
     --header 'accept: application/json'
Where it says
oauth_token
it
actually
means the
access_token
.
The JSON that is returned is a bit verbose, so I've simplified it here:
⧉
JSON
{
"meta"
:
{
"code"
: 200,
"requestId"
:
"699c6505b488565a31e315e3"
}
,
"response"
:
{
"checkins"
:
{
"count"
: 2344,
"items"
:
[
{
"id"
:
"699c34b55bad6b7fb1695544"
,
"createdAt"
: 1771844789,
"type"
:
"checkin"
,
"visibility"
:
"closeFriends"
,
"entities"
:
[
]
,
"shout"
:
"Testing the API using an Untappd FourSquare ID."
,
"timeZoneOffset"
: 0,
"editableUntil"
: 1771931189000,
"venue"
:
{
"id"
:
"64eca80f0398c97ab52298ec"
,
"name"
:
"Abbey Wood Fossil Pit"
,
"contact"
:
{
}
,
"location"
:
{
"lat"
: 51.487514,
"lng"
: 0.13048041,
"postalCode"
:
"SE2 0AX"
,
"cc"
:
"GB"
,
"country"
:
"United Kingdom"
,
"formattedAddress"
:
[
"SE2 0AX"
]
}
,
"createdAt"
: 1693231119
}
,
}
,
Annoyingly, there's no
checkinShortUrl
which means it can't easily be shared.
For that, you'll need to
use the
get-checkin-details
API
:
⧉
Bash
curl --request GET \
     --url 'https://api.foursquare.com/v2/checkins/699c34b55bad6b7fb1695544?v=20250202&oauth_token=asdfghjkl123456' \
     --header 'accept: application/json'
Which will return this (truncated for brevity):
⧉
JSON
{
"meta"
:
{
"code"
: 200,
"requestId"
:
"699c67de5f5c0a0e8ab234db"
}
,
"response"
:
{
"checkin"
:
{
"id"
:
"699c34b55bad6b7fb1695544"
,
"createdAt"
: 1771844789,
"type"
:
"checkin"
,
"shout"
:
"Testing the API using an Untappd FourSquare ID."
,
"timeZoneOffset"
: 0,
"checkinShortUrl"
:
"https://swarmapp.com/user/56367/checkin/699c34b55bad6b7fb1695544?s=LA7jCaAtH-s9CwSpgQrQdHrP5-8"
,
If there's a photo with the checkin, it will be return in the JSON like this:
⧉
JSON
{
"response"
:
{
"checkin"
:
{
"photos"
:
{
"count"
: 1,
"items"
:
[
{
"id"
:
"699f3a9f96799c05c0f16c9c"
,
"createdAt"
: 1772042911,
"prefix"
:
"https://fastly.4sqi.net/img/general/"
,
"suffix"
:
"/56367_5VYox4Y-hs66wURVsYc1NLgOokfwBfcWhtKQrOlMdD8.jpg"
,
"width"
: 1008,
"height"
: 1344,
The URl for the image is
prefix width x height suffix
- in this case
https://fastly.4sqi.net/img/general/1008x1344/56367_5VYox4Y-hs66wURVsYc1NLgOokfwBfcWhtKQrOlMdD8.jpg
You can adjust the width and height if you want a thumbnail or some other resolution.
If there's no photo, the count will be 0.
Every 15 minutes,
the SwarmToSocial code
does the following:
Get the most recent checkin.
Read a local file to get the previously seen checkin ID.
If the checkin ID hasn't been seen before:
Get the checkin details.
Get the photo if it exists
Post the checkin (plus photo) to Mastodon & BlueSky.
Save the checkin ID to a file.
Enjoy!
