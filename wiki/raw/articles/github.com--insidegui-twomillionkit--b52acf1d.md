---
title: "insidegui/TwoMillionKit: Use Private Cloud Compute in FoundationModels without an entitlement · GitHub"
url: "https://github.com/insidegui/TwoMillionKit"
fetched_at: 2026-07-13T07:01:31.298494+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# insidegui/TwoMillionKit: Use Private Cloud Compute in FoundationModels without an entitlement · GitHub

Source: https://github.com/insidegui/TwoMillionKit

Apple added the ability for third-party apps to use Private Cloud Compute language models in macOS 27 and aligned releases, but with a significant caveat: only developers who are a part of the Small Business Program can participate, and only those who haven’t had any of their apps surpass 2 million downloads.
According to Apple,
one of my apps has surpassed 2 million downloads
. That’s an iOS app that’s been in the App Store for nearly 10 years, and has had most of its 2 million downloads within the first few years of existence. Because of that, none of my apps can use Private Cloud Compute, putting me in a significant disadvantage because I can’t ship cool AI features like many other small developers will be doing this Fall.
It’s worth noting that even though Apple claims that my app has had more than 2 million downloads,
none of their reports
in App Store connect come close to that number. I asked them to provide me the report that says that my app has had more than 2 million downloads, but my email must have ended up in
/dev/null
because I never got any response.
Apple ships the
fm
command-line tool in macOS 27, which can be used to run inference with the local system model or Private Cloud Compute from Terminal or scripts. You know what else can run command-line tools? Mac apps! 😃
I decided to spend some of my Codex tokens and take GPT 5.6 Sol for a spin. I asked it to create this Swift package. All it does is provide a
LanguageModel
implementation that uses the
fm
command-line tool under the hood, meaning that any Mac app can use the Private Cloud Compute model without requiring a special entitlement from Apple.
The main limitation is that this will not work for sandboxed Mac apps, so any Mac app distributed via the Mac App Store won’t be able to use it.
But for developers of Mac apps distributed outside the Mac App Store, this provides a simple and entitlement-free way to use Private Cloud Compute in their apps.
Use sparingly and at your own risk.
Enjoy!
