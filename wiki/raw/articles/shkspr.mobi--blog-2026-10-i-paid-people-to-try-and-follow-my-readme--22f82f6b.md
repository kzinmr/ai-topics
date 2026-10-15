---
title: "I paid people to try and follow my README"
url: "https://shkspr.mobi/blog/2026/10/i-paid-people-to-try-and-follow-my-readme/"
fetched_at: 2026-10-12T10:11:00.466505+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# I paid people to try and follow my README

Source: https://shkspr.mobi/blog/2026/10/i-paid-people-to-try-and-follow-my-readme/

Developers suck at writing documentation. We like to say RTFM but often there ain't no FM to R. At best we have a half-arsed collection of notes, some obsolete tips, and a link to a desolate forum full of people asking the same questions again and again. That's no way to treat our users.
I naïvely believe there's a better way. As I've written before, you should sit down and
actually
test your readme
. Spin up a fresh Virtual Machine, go through what you've written, and see if it makes sense.
But it is
really
hard to ignore your own biases. Of course you know that certain commands require
sudo
and obviously when you wrote
-foo
you meant
--foo
and everyone knows that you have to reboot afterwards.
How do you get rid of those biases? I paid people!
As part of my
NLnet grant application for ActivityBot
, I said I wanted to test the install experience with real users and I was prepared to pay them €25 for an hour of their time. I stuck out the call on Mastodon, gathered a few people, and had a video call with them.
The format was simple. I explained that I was looking for feedback on the first-run experience. I knew that it wasn't perfect and actively wanted constructive criticism. I asked the volunteer to share their screen and, crucially, to speak aloud. Tell me what they were doing. What they didn't understand, what confused them, what delighted them, what frustrated them, etc.
I took notes by hand (fuck feeding the machine) and spent several hours being told what incorrect assumptions I'd made.
Amongst the highlights I discovered were:
The link to the demo tool was wrong.
Some people read a README in the terminal.
What does it actually mean to rename a file?
How do you rename a hidden file?
Should a demo tool be available on the web or just the user's local machine?
Why does some text explicitly need to be quoted and some not?
My jokes aren't funny and are actively confusing.
Some of the technical terminology needed explaining.
The ordering of the different sections was confusing.
I hadn't actually explained what the software would do.
A whole section which was technically interesting to me was utterly confusing to everyone else.
Not all web servers use permissions in the same way.
And on it went!
After each session I updated the README based on what people found difficult, then I re-tested it with the next person.
In total, I paid out around €150 to have a bunch of people criticise me to my face. Hey, cheaper than therapy, right?
I know someone is going to say "why not just ask an LLM to simulate a range of users?" The answer is very simple - I want to speak to real people. People are brilliant! They can make you laugh, you can see their cat when it wanders on to the call, they bring a unique perspective to the problem, and they're really happy when you give them a €25 voucher. Some will gladly do it for free and make
you
happy!
When I was doing technical writing for GOV.UK, all my beautiful prose was given a second-eye by another human. They eviscerated all my flowery phrases and turned the document into something more readable. They were the ones who caught the mistakes that no spell chequer could. They were able to have a proper conversation with me. More importantly, I could
hear
the frustration in their voice - that's the thing which lets you know a mistake needs to be corrected.
I don't claim that
ActivityBot's README
is now perfect - far from it - but it is now demonstrably easier to follow. Developers need to talk to
real
people. You don't have to pay them if you can't afford it - but find a few people who will talk aloud while they try to follow your instructions. I guarantee you that your README will become much better for it.
