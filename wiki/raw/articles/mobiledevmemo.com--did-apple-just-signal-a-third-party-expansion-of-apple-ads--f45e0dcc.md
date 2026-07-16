---
title: "Did Apple just signal a third-party expansion of Apple Ads?"
url: "https://mobiledevmemo.com/did-apple-just-signal-a-third-party-expansion-of-apple-ads/"
fetched_at: 2026-07-16T07:01:39.913849+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Did Apple just signal a third-party expansion of Apple Ads?

Source: https://mobiledevmemo.com/did-apple-just-signal-a-third-party-expansion-of-apple-ads/

Rumors have swirled for years about a potential extension of Apple’s mobile advertising platform to third-party surfaces. Last April, Apple renamed its advertising platform from Apple Search Ads to Apple Ads. I noted at the time that this could indicate an expansion into Apple Maps, which Apple
ultimately did announce
roughly a year later, in May 2026.
But the rebrand from Apple Search Ads, which characterizes the ad units Apple serves in the App Store, to the more sweeping Apple Ads could be interpreted as a signal of Apple’s broader aspirations and goals for its advertising business, as I articulated in
Apple’s advertising ambitions
, published shortly after the rebrand.
Yesterday, Apple sent a pithy email to advertisers, notifying them that an update to the
Apple Advertising Terms of Service
will go into effect on July 28th. Notably and somewhat curiously, because the terms don’t go into effect for another two weeks, Apple actually publishes the updated terms to a
separate URL
, allowing for a fairly straightforward comparison. Hat tip to independent consultant and former MDM podcast guest
Thomas Petit
for alerting me to this.
The critical change, to my mind, is in term 6(a), related to “Advertising Services.” I’ve compared the two terms below and highlighted the difference:
The most plausible explanation for the change Apple has made to its Advertising Terms of Service is that the company plans to expand Apple Ads to third-party, non-Apple-owned surfaces: the updated language in the terms gives Apple broad latitude to place Apple Ads on apps, websites, and platforms that it doesn’t operate. This would be a dramatic departure from the current Apple Ads operating model, which is limited to Apple-controlled inventory in the App Store, Apple News and Stocks, and MLS programming in the Apple TV app, with Apple Maps inventory coming soon.
The new language could simply accommodate the availability of Apple-owned services on the web and through third-party devices and operating systems; the Apple TV app, for instance, is available on smart TVs, streaming devices, and game consoles. But the addition of “other properties” is conspicuously broad and appears to give Apple the contractual latitude to distribute ads beyond its own services entirely. This would allow for a material expansion of the company’s advertising surface area.
Further, if Apple does indeed plan to expand Apple Ads to third-party surfaces, it would explain why the company
did not reveal an update
to its AdAttributionKit (AAK, formerly SKAdNetwork, or SKAN) attribution framework at this year’s WWDC.
One of my central criticisms of
Apple’s App Tracking Transparency (ATT) privacy policy
was that the company preferenced its own advertising platform by providing a separate measurement API for its exclusive use with ads served in its owned surfaces, whereas all other publishers are forced to use SKAdNetwork (for exhaustive detail on that topic see
ATT advantages Apple’s ad network. Here’s how to fix that
). If Apple Ads are expanded to third-party surfaces — including third-party apps and, apparently, per the updated terms, websites — then AAK and Apple’s own attribution API, the Ads Attribution API, would need to be fused, or something new altogether would need to be introduced.
