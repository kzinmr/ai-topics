---
title: "Open Source vs the Invisible Hand"
url: "https://nesbitt.io/2026/06/18/open-source-vs-the-invisible-hand.html"
fetched_at: 2026-06-19T07:00:56.690405+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# Open Source vs the Invisible Hand

Source: https://nesbitt.io/2026/06/18/open-source-vs-the-invisible-hand.html

If you handed an economics undergraduate a description of how open source libraries are produced, without saying what it was, and asked them to predict the outcome, they would tell you it doesn’t add up. Non-excludable goods with no price, no contracts, no liability, a median producer headcount of one, and near-total free riding by consumers: there is no model in the textbook under which that arrangement produces anything stable.
Then you run
npm install
and a few hundred of these impossible goods arrive in seconds, and the commercial software industry sits almost entirely on top of them. Open source breaks more or less the full set of market axioms at once.
The free rider problem
.
A public good is non-rival (my use doesn’t reduce yours) and non-excludable (you can’t keep me out), and standard theory holds that such goods will be underproduced because every rational actor waits for someone else to pay. The canonical case is the
lighthouse
, where everyone benefits and nobody volunteers, so government has to build it. An open source library meets the definition exactly, being perfectly non-rival and non-excludable by licence, so the theory predicts a small number of them, grudgingly produced and propped up by grants. npm alone hosts
over five million
, almost none grant-funded, with thousands more turning up every day.
You get what you pay for
.
Price is supposed to
signal
quality and scarcity, giving a market a way to sort good from bad. SQLite, by
its own count
the most widely deployed database engine in the world, costs the same as a week-old typosquat with a crypto miner in the postinstall hook. The most valuable libraries in existence and the most dangerous ones sit at the same number, and consumers route around the missing signal with reputation, download counts, and GitHub stars.
The tragedy of the commons
.
A shared resource gets depleted because each user’s rational move is to take without giving back, so the prediction for a software commons would be a small pool of overused, under-maintained code that decays as consumption outruns contribution. Some corners of the public registries do look like that, but the aggregate has grown every year since registries have existed.
Rational self-interest
.
Economic agents maximise their own utility, and utility can be defined broadly enough to cover enjoyment, status, and ideology as well as money. Even on the broad definition it is a stretch that so many people’s preferences include answering bug reports from strangers at eleven at night, after a full day at an unrelated job, prompted by an issue from a Fortune 500 company titled “URGENT!!”, for a project that pays them nothing. There are enough people whose preferences apparently work that way to keep most of the modern software stack running.
Supply and demand
.
Rising demand is supposed to raise the price and draw in new suppliers until the market clears, but when a library goes from a thousand downloads a week to ten million the price stays at zero and the maintainer count typically stays at one, because demand has no channel through which to act on supply. More users turn up, the issue tracker fills, security researchers start filing CVEs against it, and it stays one person’s job.
Division of labour
.
Critical infrastructure is supposed to be built by specialists, employed full-time, organised into firms that carry liability for failure. Across the public registries ecosyste.ms tracks,
more than half of packages have a single maintainer
, and that one person frequently has a day job in a different field, no employment relationship with any downstream user, and no contractual liability to anyone. The bus factor for long stretches of the dependency graph works out to a single hobbyist.
Firms guard competitive advantage
.
A company is not supposed to pay engineers to build something and then hand it to the people competing for its customers, yet Google, Meta, Microsoft, and Amazon all fund open source libraries the other three run in production. The standard explanation is
commoditising your complement
: give away the layer adjacent to where you make money so nobody can charge you rent there. That accounts for React and gRPC well enough and is the one entry here with a clean market explanation. The explanation does not extend to the much larger tier underneath, the libraries with one maintainer and no adjacent business model, which is most of what
npm install
pulls in.
Economists have noticed all this, and there is a small literature trying to account for it.
Lerner and Tirole
put it down to career signalling, contributing in public to build a reputation you cash in elsewhere. That holds when someone is watching, and not for the maintainer of an obscure dependency no hiring manager will ever look up.
Benkler
argued that the internet made coordination cheap enough to organise production without a firm. That explains how the work gets divided, not why anyone takes on the unglamorous half of it.
Von Hippel
framed it as user innovation, people building what they need and sharing it afterwards for next to nothing. It fits until the maintainer is still answering bug reports years after they stopped using the thing themselves. All three fit some maintainers some of the time, and none on its own accounts for the shape the system has taken or why it has held together this long.
Calling all of the above a list of market failures implies a working market underneath that would behave properly once the failures were corrected, and there isn’t one: open source has run for thirty years on a basis the textbook says cannot hold. It looks more like several arrangements overlaid on each other, part gift economy, part shared infrastructure, part public archive, part reputation system, with no single mechanism carrying it.
The practical fixes that keep being proposed treat it as a market anyway and bolt the missing pieces on, which is where bug bounties, sponsorship marketplaces, dependents-weighted funding formulas, criticality scores, and tokenised reward schemes all come from. Every one of them is an attempt to reconstruct a price for something that has never had one, and to do that they need a number to stand in for value.
The numbers available for that job are
weak proxies
, two or three steps removed from what anyone wants to know: who is keeping this running, how close they are to stopping, and whether a security report filed against it would
reach anyone at all
.
