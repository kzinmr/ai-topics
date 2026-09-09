---
title: "ActivityPub - Is it worth defending against replay attacks and message/signature time skew?"
url: "https://shkspr.mobi/blog/2026/09/activitypub-is-it-worth-defending-against-replay-attacks-and-message-signature-time-skew/"
fetched_at: 2026-09-09T10:01:00.707811+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# ActivityPub - Is it worth defending against replay attacks and message/signature time skew?

Source: https://shkspr.mobi/blog/2026/09/activitypub-is-it-worth-defending-against-replay-attacks-and-message-signature-time-skew/

Here's a problem that I've found with
ActivityBot
- my little ActivityPub server. Sometimes it receives messages which were originally sent
months
ago. Why does that happen and is it risky to accept and process them?
My tl;dr is that it
probably
isn't worth worrying about. But I'd love someone to tell me why I'm wrong.
Here's my thinking:
Causes
Is that a problem?
What are we trying to protect against?
Putting it all together
No! You're wrong and I can prove it!
All ActivityPub messages should have a "published" timestamp in their body. Some will have an "updated" timestamp. That tells you, unsurprisingly, when the message is alleged to have been originally published or updated. That time might be very different to the time you receive the message.
There are, I think, three different reasons why a server might receive a message which has an out-of-date timestamp.
The first is that sometimes servers are just slow. Processing thousands of messages at the same time means that some of those messages take a while to send.
ActivityPub is one big chain-mail
so it can take several minutes for a message to be sent to all your followers.
Similarly, your server might be slow. If it doesn't acknowledge receipt of a message, the original server will try sending it again. Sometimes that can take a while.
Finally, some servers take a relaxed view of standards. They send an update to an old message but keep the original publication date. Ideally, they'd use an "updated" timestamp but quite often they don't.
For the purposes of checking the legitimacy of the message,
you do not need to check when a message says it was published or updated
. You might want to check it isn't an
obviously
bogus date like far in the future or impossibly far in the past - but that's up to you.
It is normal that your server receives messages which appear to have been published at a totally different time from now.
Probably
not.
As described above, there are various reasons why a message may be delayed in transit - or may appear to come from the distant past.
What we
can
check is when the message was cryptographically signed by the sending server. This is independent of its published or updated timestamp.
HTTP requests to your server will have a
date
header which looks like
Tue, 01 Sep 2026 15:54:21 GMT
- this is in the slightly peculiar and Anglocentric
RFC 5322 format
.
New style RFC 9421 headers will also have a
signature-input
header which will contain something like
created=1788278061
. That uses the slightly obscure
UNIX / POSIX time
which counts seconds since the "Epoch" of 1st January 1970.
If you
convert the UNIX time
to something more modern, you should get an
identical
value to the
date
header.
But that isn't always the case. For example,
the RFC 9421 standard gives this example
:
Copied  to 📋
⧉
Date: Tue, 20 Apr 2021 02:07:55 GMT
"@signature-params": ("@method" "@authority" "@path" \
  "content-digest" "content-length" "content-type")\
  ;created=1618884473;keyid="test-key-rsa-pss"
Converting
1618884473
to normal time gives Tue, 20 Apr 2021 02:07:
53
- a two second difference.
If the
date
and
created
values differ significantly - that may indicate that the message is untrustworthy. Or that there was a delay between the signing and the sending.
The spec says:
The Date header field value represents the timestamp of the HTTP message. However, the creation time of the signature itself is encoded in the created signature parameter. These two values can be different, depending on how the signature and the HTTP message are created and serialized. Applications processing signatures for valid time windows should use the created signature parameter for such calculations. An application could also put limits on how much skew there is between the Date field and the created signature parameter, in order to limit the application of a generated signature to different HTTP messages.
7.2.4. Choosing Signature Parameters and Derived Components over HTTP Fields
But, of course, it doesn't tell you how much skew is problematic. It's up to you how much skew you're prepared to accept.
So that's the difference between the sent time and the signed time. The next time to check is your own. As we've discussed, sometimes servers are slow sending things out. Would you accept a request that was signed five minutes ago? Five days ago? Five months ago? What amount of difference is dangerous?
Here's what various services and sages have to say:
The request contains a Date header. Compare it with current date and time within a reasonable time window to prevent replay attacks.
How to make friends and verify requests
What is "reasonable"? The
source code
suggests one hour.
Time in the Date header must differ from the recipient server’s clock by no more than 30 seconds
A bare-minimum ActivityPub server from scratch
static #maxDateDiff = 5 * 60 * 1000 // 5 minutes
activitypub-bot
The standards don't give a concrete time window to use for this comparison. In practice, an hour plus a few minutes buffer in either direction may be a good value, to account for both clock skew and differences in time zone/daylight savings time configuration across systems.
How To Verify a Signature
Without naming names, it looks like a bunch of popular servers don't check whether there's a significant difference between the date the request was signed and the date it was received.
Various documents and implementations recommend anything between 30 seconds to "a bit more than 60 minutes". Or they just ignore any date difference.
What's the right answer? What happens if the signed date is significantly different from the current date?
Replay Attacks. Suppose someone is listening to the communications between the sending server and your server. They copy the message that is sent to you. Later they send it again!
At this point, you might be thinking "so what?" and… I'm inclined to agree with you!
What's the worst that could happen if you received the same message multiple times? Two things that I can think of.
Firstly, it might
not
be the same message. It is possible to send a new message but with old headers. An attacker could make someone post "I hate Taylor Swift" against their will and watch as legions of fans disembowel the victim.
Except, I don't think this is likely. The signature in the header contains a hash of the message being sent. If you are properly validating the signature, a changed message will have a different hash from the one in the original message. You don't need to check timestamps, you just need to check if the hashes match.
Secondly,
idempotence
. That's a fancy word for "pressing the button multiple times should only result in one action".
What happens if a user appears to send you multiple "like" messages for a single post? You only record one like.
What if they send multiple messages with the same content? Well, each will have a unique ID in the message - so you only post it once.
What if they send multiple
anythings
? I can't think of any ActivityPub action which would not be idempotent.
About the worst thing I can think of is this:
Alice sends a message to you saying "I want to follow Bob".
Mallory intercepts this message.
You record Alice is now following Bob.
Alice sends a message to you saying "I want to
unfollow
Bob".
You record the severed relationship.
Mallory replays the original follow message.
You record Alice is now following Bob.
It's also possible the following could happen:
Alice posts a message saying "I love The Beatles".
You record Alice's message and display it on the timeline.
Alice updates her post to say "I love the Rolling Stones".
Mallory intercepts this message.
You record Alice's updated message and display the new version on the timeline.
Alice updates her post yet again to say "I love the Spice Girls".
You record Alice's updated message and display the new version on the timeline.
Mallory replays the original update message.
You now display that Alice loves the Stones rather than Spice Girls.
Perhaps the same can happen with like/unlike, block/unblock, boost/unboost.
But none of that is significantly prevented by checking the date.
Ultimately, it is up to your sever to check the unique ID of each message and refuse to action any repeated messages. You may not want to trust the unique ID which is sent with the message. If that's the case, you can calculate your own - perhaps using a hash of the contents, the signature, or some other process which will generate an ID based on the message.
Here's what you need to do to prevent replay attacks:
Independently calculate the hash of the message received.
Validate that your calculated hash matches the hash sent in the message's HTTP headers.
If not, this is a potential replay attack and the message must be ignored.
Verify that the signature received in the message's HTTP headers includes the message hash and is cryptographically valid.
If not, the signature is invalid  and the message must be ignored.
Has the received message's unique ID already been processed?
If so, refuse to process it again.
I don't see what checking the timestamp of the HTTP signature has to do with anything. Someone who has access to the original messages and their headers could send them milliseconds after the original delivery.
I think it is probably
pragmatic
to give messages 60ish minutes grace before dropping them. Delays happen, but anything more significant than an hour
might
indicate a attack. But, equally, might just mean that the Internet is having a slow day.
If you are correctly checking signatures and hashes, I don't think you need to worry about skew between signature date and delivery date.
Please tell me where I have erred! Stick a comment in the box or drop me an email. If I've made a massive or subtle mistake, I'd love to know what.
