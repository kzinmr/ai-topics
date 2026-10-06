---
title: "Apple Is Going to Further Tighten the Screws on Full Disk Access on MacOS, in Response to Agentic AI Apps Running Amok"
url: "https://daringfireball.net/2026/10/apple_full_disk_access"
fetched_at: 2026-10-03T10:01:01.181280+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Apple Is Going to Further Tighten the Screws on Full Disk Access on MacOS, in Response to Agentic AI Apps Running Amok

Source: https://daringfireball.net/2026/10/apple_full_disk_access

Apple Is Going to Further Tighten the Screws on Full Disk Access on MacOS, in Response to Agentic AI Apps Running Amok
Friday, 2 October 2026
Apple Developer News, in a post titled “
Updates to Full Disk Access in macOS
”:
We give developers powerful APIs to build incredible capabilities
into their apps for Apple products, backed by a set of controls
designed to protect users’ private data. Full Disk Access largely
sidesteps these controls in order to allow backup apps to function
properly on the Mac. Some developers are using Full Disk Access in
ways that could put users at risk, exposing everything on their
systems — including files, mail, messages, and even browsing
history — without users’ full knowledge and understanding. For
communication apps, this can also compromise the privacy of the
people users are communicating with.
Going forward, we will introduce additional controls to ensure
that users who genuinely wish to grant an app this extraordinary
level of access can only do so with very explicit user action.
Addressing this is critical. As AI agents become increasingly
capable and autonomous, the risks associated with this level of
access will grow substantially. We are committed to ensuring users
clearly understand these risks before granting such access, so
they can make informed decisions about their own data and privacy.
They don’t name names, but clearly this is in response to Meta Muse (cf.
Jason Aten’s misadventure
with Muse accessing Aten’s iMessages),
Grok Bot
, Claude, Dots, and the rest. This is why we can’t have nice things.
I really worry about just how much Apple is going to lock Full Disk Access down. I use it with several apps that couldn’t function properly without it, and would be severely hampered if I needed to authorize it manually every time they do something.
But before we Mac power users riot in Cupertino, we should note that we have no idea how many unsophisticated Mac users are calling Apple and queuing up at the retail store Genius Bars to complain about Muse and these other agents having run amok on their Macs, against their desires, after convincing these users to grant them access. It is a legitimate frustration for the highest-functioning users among us that the Mac has, for years, already seemed “too locked down”. But there are now around 150 million Mac users worldwide. Most of them are unsophisticated technically — a majority of them, profoundly so. Many of them have technical needs that cannot be met by the
baby computer
OS that is iPadOS. For a lot of them it might just be the ability to run the real version of Google’s Chrome web browser — or even the desktop version of Safari. So there are tens of millions of people who need to use a Mac to do things that cannot be done on an iPad, but who have zero understanding of what it means, say, to grant Muse permission for Full Disk Access. And then they think it is
Apple’s fault
that Muse is suddenly able to read their private iMessage conversations.
(Anyone out there who, say, works at an Apple retail store and can confirm whether this is an escalating support issue — one way or the other —
I’d love to hear from you
, confidentially.)
On iOS (and its tablet variant, iPadOS), you can say OK to every single thing an app like Muse asks for and Muse still won’t be able to read your email or end-to-end encrypted messages from iMessage or WhatsApp. There is no level of permission that grants third-party apps permission for such things. (The EU wants to force Apple to allow that under the DMA.) MacOS isn’t like that. You still need to grant apps permission for such things, but if you say OK to everything an app like Muse asks for on the Mac, you’re granting that app access to, effectively, almost everything on your startup drive. There are still some things it can’t see, but not many. A lot of non-technical Mac users do not understand this and cannot be expected to understand this. They just think, wrongly, that Apple protects them from allowing anything truly dangerous, because that’s how their iPhone (and/or iPad) works. So they just click OK to every access request from Muse and presume they’re still largely protected.
Hopefully Apple has in mind a solution to this situation that will still enable knowledgeable power users to confirm agreement to a sufficiently scary warning and put their Macs in a state similar to what we have today. I worry. What alleviates my worst fears is the knowledge that every technical user at Apple itself needs to use their Mac as the powerful Unix workstation OS that it is. Some of us need dangerously powerful tools. Most Mac users, however, do not — and don’t realize they’re using a dangerously  powerful Unix workstation with a very friendly (
literal
) face.
