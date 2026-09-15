---
title: "ActivityPub - How to send an updated user profile to Mastodon and the Fediverse"
url: "https://shkspr.mobi/blog/2026/09/activitypub-how-to-send-an-updated-user-profile-to-mastodon-and-the-fediverse/"
fetched_at: 2026-09-13T10:01:14.510581+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# ActivityPub - How to send an updated user profile to Mastodon and the Fediverse

Source: https://shkspr.mobi/blog/2026/09/activitypub-how-to-send-an-updated-user-profile-to-mastodon-and-the-fediverse/

Let's suppose you've updated the description of your ActivityPub account from "World's Number 1 Taylor Swift Fan" to "This account is now a Nickleback Truther". How do you let the rest of the Fediverse know that you've changed your allegiance?
By default, most Mastodon instances won't periodically poll your account information just to see if you've updated it. So how does the information get from your server to your followers' servers?
This wasn't immediately obvious to me, but I got a clue from reading
Evan Prodromou's book on ActivityPub
:
The Update activity type is for updating the properties of an object represented by the object property.
The most common types of objects that can be updated are content objects, like Note or Image. Actor types (like Person) and Question activity types can also be updated.
Aha!
You need to craft an
Update
message which has as its object the
new
user information. That needs to be sent to the inbox of all your followers.
Something like this:
Copied JSON to 📋
⧉
JSON
{
"@context"
:
"https://www.w3.org/ns/activitystreams"
,
"actor"
:
"https://example.com/user"
,
"id"
:
"6a9162a6-a8e5-ca0f-9c08-8e6b814acef8"
,
"published"
:
"2026-08-31T12:34:56+01:00"
,
"to"
:
"https://www.w3.org/ns/activitystreams#Public"
,
"type"
:
"Update"
,
"object"
:
{
"@context"
:
[
"https://www.w3.org/ns/activitystreams"
,
"https://w3id.org/security/v1"
]
,
"id"
:
"https://example.com/user"
,
"name"
:
"My new name"
,
"summary"
:
"A brand new description!"
,
        …
}
,
}
Obviously the
full
user information is a bit more than that - it will include inbox details, public keys, avatars, etc. The
published
property in the Update activity should be when you changed your details - not when the account was created.
Once that was sent, Mastodon immediately reflected the changes.
This blog post was funded in part by the work I'm doing for my NLnet NGI0 grant to develop
ActivityBot
.
