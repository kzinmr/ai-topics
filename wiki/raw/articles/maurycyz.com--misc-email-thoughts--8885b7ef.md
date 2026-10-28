---
title: "Some thoughts on hosting email"
url: "https://maurycyz.com/misc/email_thoughts/"
fetched_at: 2026-10-28T10:01:26.373584+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Some thoughts on hosting email

Source: https://maurycyz.com/misc/email_thoughts/

Some thoughts on hosting email
2026-10-26
—
2026-10-27
Generally speaking, email isn't as hard as its reputation would suggest.
Yes, big-tech providers will occasionally send my messages to spam...
but paying for commercial email doesn't guarantee delivery:
emails within a single provider are generally safe, but in my experience, big-tech to other big-tech has a ~75% chance.
Because of this, having my own mail server is great for piece of mind:
I can be sure that anyone can send me an email without it mysteriously vanishing.
My reply might go to spam, but at that point we're already in communication and can sort it out.
A softer version of self hosting is to keep a big-tech account, but only use it for initiating conversations.
Point the "reply-to" header at a server you run, and give that address when people ask for contact details.
Since replies to real emails never go to spam, this provides the best of both worlds:
maximizing the chance that someone else will get your message,
while also maximizing the chance that you will get theirs.
Receiving email
requires:
A publicly routable IPv4 address
Any server: good uptime is not required.
A domain [optional]
Despite it being 2026, many mail servers still don't support IPv6:
if you have a good ISP, it should be possible to get a public IPv4 address arranged.
Otherwise, the only real option is to rent space in a datacenter, which will cost some money.
(Note, there's no requirement for the VPS to actually run the mail daemon:
It's possible to have it forwarding traffic to a box in your house)
The server itself doesn't have to be anything special.
A "big" email is only a few megabytes, and people only send a few messages per day.
However, disk space may be a consideration if you plan on having multiple users.
Mailer daemons will retry message delivery, and only give up after days of downtime.
If it does, the sender will get a failure notification:
emails will never be dropped silently.
Regarding domains,
"ihavenoname@[65.109.172.162]" is a perfectly valid email address.
However, doing this ties your identity to your hosting provider or ISP, which is not ideal.
Buying, or rather renting, a domain costs money.
It's not a huge amount of money (around 1 $/month), but it is a significant commitment.
If you let a domain lapse, someone else can buy it and take over your old address.
I prefer to think of the cost as $800 per lifetime:
not a prohibitive amount, but you should think twice before getting yet-another domain for a sideproject.
(Just remember that email needs an MX record)
Sending email
requires:
An IP address with a PTR record
A domain
The domain is unavoidable here, because you'll need to make a few DNS records to prove the moral character of your packets.
Specifically, you'll need SPF and DKIM.
; SPF record
@
TXT
"v=spf1 ip4:65.109.172.162 ip6:2a01:4f9:c011:841a::1 -all"
SPF tells receiving servers to accept mail from particular IP addresses and reject everything else.
Importantly, this means if you have multiple different addresses,
the mailer daemon will have to be configured to use a specific one.
Most servers will handle a missing SPF record as "deny everything", which is sensible:
otherwise, even if someone had SPF at root, bad actors could spoof emails from a non-existent subdomains.
The second authentication mechanism is DKIM, which uses a cryptographic signing key published through DNS.
Here's mine, but you will need to generate your own:
2020._domainkey
TXT
"v=DKIM1;h=sha256;k=rsa;p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBi
QKBgQDcysWHfXhdjsK3jWRnUKa3cdNF7gfl0EP/Xe2r5Ixqp7htPRVx7sntLgF1S5fODBM9o9xWSTwu
TuuFF0DLvkvi2fiddiSFa+0IXMb7sevhYIGha6Ewpk5h4vHkRIEGG7MDTlnXovgQpq5Q6MUymU6Z+Or
H6xXBaiwf8wOfZtRIYwIDAQAB"
Most providers also require reverse DNS on the origin IP address.
This doesn't have to be the same domain as you are sending email from,
but it should be a public hostname associated with your server.
Dealing with spam:
Spam hasn't been as much of a problem as I expected, despite my near-worst case setup:
a catchall email and a contact address listed on a public website.
All I've needed to deal with spam is:
SPF checking, but not enforcement. (default allow)
Light email obfuscation.
A blacklist of 12 domains and IP addresses
I'm not particularly worried
about the spoofing potential of allowing unauthenticated messages since I have infinite addresses;
If I get an email to my blog's comment box purporting to be a bill from my hosting provider,
then I know it's fake regardless of what's in the "From" field or message body.
However, this relaxed SPF does still filter out a lot of the spam:
most of the particularly obnoxious spammers forge emails from well
known-domains which do have an SPF record.
There are lots of wacky solutions
for email obfuscation:
images, javascript initiated network requests, encryption, etc, etc.
In practice, 99% of spam bots don't parse HTML and can be thrown off by something as simple as:
<!-- A random comment -->
blog@maurycyz
<!--.example-->
.com
<!-- Or needless percent encoding -->
<
a
href
=
mailto:blog@
%6d
aurycyz.com
>email</
a
>
This works in every browser, is compatible with screen readers and not too hard to figure out by hand.
More extreme measures would also work, but why bother?
With blacklists
, there is a very long tail needed to get rid of all spam,
but it doesn't take much at all to get it down to tolerable levels.
For me, it was enough to block seven domains and five IP addresses (not address blocks) to get it down to around 3 messages per week:
I think that's a sensible price for being sure nothing important will get caught up.
Security:
Getting your email compromised is bad.
Not only does it have a lot of personal information, most services run password resets and account recovery over email.
Some attacks are technical, but many aren't:
your server password should not be "password123".
If you don't trust yourself to use a good password, set up key-based for authentication.
In terms of defending against exploits, the best thing to do is keep everything up to date and isolated:
Setup automatic updates and check back a moth later to make sure they work.
Services should be run as separate unprivileged users:
if your web server gets popped, the attacker should not be able to read your email.
One thing that is unique to email
is just how aggressive people are be when blacklisting IPs:
if your server gets used to send spam, good luck recovering any reputation.
Because of this, it's a very good idea to lock down outgoing network traffic.
A web server doesn't need to make any outgoing connections.
A minecraft server needs HTTPS and DNS to authenticate users, but should not have access to anything else.
Only the mail daemon needs outgoing port 25 access.
(Also, make sure to lock down locally submitting email)
Reputation aside, this is good security practice.
Remember log4shell, that trivially exploitable RCE against Java applications?
It requires downloading a payload from the attacker's server, so proper firewalling makes it impossible to exploit.
Additionally, almost all malware opens up a communication channel over the internet:
a crypto miner needs to download the blockchain state, a stealer needs to upload the stolen data...
