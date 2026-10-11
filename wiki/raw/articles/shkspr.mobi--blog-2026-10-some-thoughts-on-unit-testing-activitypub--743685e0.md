---
title: "Some quick thoughts on Unit Testing ActivityPub"
url: "https://shkspr.mobi/blog/2026/10/some-thoughts-on-unit-testing-activitypub/"
fetched_at: 2026-10-11T10:01:12.734549+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Some quick thoughts on Unit Testing ActivityPub

Source: https://shkspr.mobi/blog/2026/10/some-thoughts-on-unit-testing-activitypub/

I'll be radically honest here - I never really got the idea of "Test Driven Development". I'm much more of a "telnet into production and damn the consequences" kind of guy. Look, it's much more fun and my cardiologist recommends severe shocks every now and again.
The essence of unit testing is pretty simple:
Feed a function some data
See how it responds
Send it good data and if it returns "true" the test passes. Send it bad data and make sure it returns false. Easy peasy lemon squeezy.
As part of my
NLnet funded work on ActivityBot
, I'm writing some proper tests for my bot framework. I am hopeful that some of them will be useful to other projects doing similar things.
There are four major classes of tests - here are the problems I've found while writing them.
A basic test might be how to validate that an ActivityPub username is valid. Typically it would be something like
@edent@mastodon.social
- what assumptions do we make with that? It starts with an
@
and has another
@
somewhere in it, dividing into two parts, the user and the server.  The server has to be a valid domain name - but that can include non-ASCII Internationalised Domain Names and Emoji domains.
What about the user part? Is it just A-Z and 0-9? Can it have dots? What about apostrophes like an email address?
Basically, how easy is it find the specifications for all the various component parts of ActivityPub? Not very!
What does a
WebFinger response
look like? Which parts are mandatory and what values can they contain?
With any message that your project generates, how can you be sure that other ActivityPub servers will understand it?
Similarly, when we receive a follow message from an external server, what should it look like?
There are some
JSON Schemas
which can be used to validate some type of messages.
But, again, there are
many
scattered specifications.
As I've written about before,
HTTP Signatures are difficult
. There are two main problems. The first is verifying signatures.
In order to do that, you need to gather a bunch of signatures and then find a way to replay them into the test. So I'm in the process of saving signatures which I can then share with others.
The second problem is
generating
signatures.  Sure, you can run tests on the signatures - but there's only one
real
way to test whether they're acceptable…
Passing tests means nothing if you can't communicate with others and they can't communicate with you.
Some tests are easier than others. Sending a signed request should be easy and repeatable. But receiving messages isn't easily automated. It requires being able to control an external server and asking that to send messages.
With the
Mastodon API
it is possible to make requests which will interact with your server - but only if it is a
public
server.
I'm putting
all my tests online
. I'm also sharing a
collection of messages and signatures
which you can use in your tests.
I'd love to know if you find them useful.
