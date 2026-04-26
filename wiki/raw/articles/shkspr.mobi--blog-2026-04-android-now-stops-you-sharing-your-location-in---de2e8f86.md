---
title: "Android now stops you sharing your location in photos"
url: "https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/"
fetched_at: 2026-04-25T12:10:46.478340+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Android now stops you sharing your location in photos

Source: https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/

My wife and I run
OpenBenches
. It's a niche little site which lets people share photos of memorial benches and their locations. Most modern phones embed a geolocation within the photo's metadata, so we use that information to put the photos on a map.
Google's Android has now broken that.
On the web, we used to use:
⧉
HTML
<
input
type
="file"
accept
="image/jpeg">
That opened the phone's photo picker and let the use upload a geotagged photo. But a while ago Google deliberately broke that.
Instead, we were
encourage to use the
file
picker
:
⧉
HTML
<
input
type
="file">
That opened the default file manager. This had the unfortunate side-effect of allowing the user to upload
any
file, rather than just photos. But it did allow the EXIF metadata through unmolested.
Then Google broke that as well
.
Using a "Progressive Web App" doesn't work either.
So, can users transfer their photos via Bluetooth or QuickShare? No.
That's now broken as well
.
You can't even directly share via email without the location being stripped away.
Literally the
only
way to get a photo with geolocation intact is to plug in a USB cable, copy the photo to your computer, and then upload it via a desktop web browser?
Because Google run an anticompetitive monopoly on their dominant mobile operating system.
Privacy.
There's a worry that users don't know they're taking photos with geolocation enabled. If you post a cute picture of your kid / jewellery / pint then there's a risk that a ne’er-do-well could find your exact location.
Most social media services are sensible and strip the location automatically. If you try to send a geotagged photo to Facebook / Mastodon / BlueSky / WhatsApp / etc, they default to
not
showing the location. You can add it in manually if you want, but anyone downloading your photo won't see the geotag.
And, you know, I get it. Google doesn't want the headline "Stalkers found me, kidnapped my baby, and stole my wedding ring - how a little known Android feature puts you in danger!"
But it is just so
tiresome
that Google never consults their community. There was no advance notice of this change that I could find. Just a bunch of frustrated users in my inbox blaming me for breaking something.
I don't know what the answer is. Perhaps a pop up saying "This website wants to see the location of your photos. Yes / No / Always / Never"? People get tired of constant prompts and the wording will never be clear enough for most users.
It looks like the only option available will be to develop a native Android app (and an iOS one?!) with all the cost, effort, and admin that entails. Android apps have
a special permission for accessing geolocation in images
.
If anyone has a
working
way to let Android web-browsers access the full geolocation EXIF metadata of photos uploaded on the web, please drop a comment in the box.
In the meantime, please leave a +1 on
this HTML Spec comment
.
