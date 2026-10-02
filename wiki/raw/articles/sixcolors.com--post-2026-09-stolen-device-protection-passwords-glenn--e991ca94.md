---
title: "Why Stolen Device Protection makes Passwords safer"
url: "https://sixcolors.com/post/2026/09/stolen-device-protection-passwords-glenn/"
fetched_at: 2026-09-29T10:01:09.076786+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Why Stolen Device Protection makes Passwords safer

Source: https://sixcolors.com/post/2026/09/stolen-device-protection-passwords-glenn/

Why Stolen Device Protection makes Passwords safer
After my massive article on
migrating your passwords, passkeys, and other secrets
from third-party password managers to Apple’s Passwords, Wallet, Safari, and general ecosystem—potentially with help from another app—reader Scott asked whether I was directing people into
weaker
security. He wrote:
If someone manages to steal my device and its passcode, they have access to the contents of my phone, including all of the information stored in Apple Passwords. This is not the case if I use a third-party password manager and have set a separate password for access, as the thief will not have access to my other passwords…I’m surprised this liability is not discussed and considered more frequently.
This is a great follow-up question, and one that I didn’t address within the scope of the migration article, which was already long. Let me pick apart how to answer that by looking at risks and mitigations.
The risks of cracking our eggs at once
I understand the fear of losing everything, whether it is a set of material objects or digital secrets. One of the most heartrending stories I ever heard was from a photographer who lost all his work in an apartment fire shortly after moving to New York City to start his career. He rebuilt. That’s harder to do digitally, where if our privacy is “burned,” we might see bank accounts drained and potentially have to get our Social Security number or other identity number replaced.
Should these eggs crack, whither our password security? (Photo by
Nick Fewings
on
Unsplash
)
But we should consider alongside that how likely it is for the scenario Scott describes: “…someone manages to steal my device and its passcode, they have access to the contents of my phone…” A sequence of actions has to take place for that to be true:
Someone has to steal your device.
Someone has to have obtained your passcode or have forced you to reveal it when or after they steal the device.
That person has to then have the time to put the stolen booty to use, like performing money transfers or cryptocurrency actions, before you erase your device remotely.
It’s most likely an iPhone would be the thing stolen, because we have those with us all the time, and thieves have been known to shoulder surf or record video from a distance to capture you entering your passcode. iPads and Macs can, of course, be taken from us as well, but it’s just much less likely when we’re out and about. A stolen Mac has additional protections if it’s powered down, and we often set longer passwords for a Mac, where an iPhone or iPad might still have a four-digit code.
If you are a privacy advocate, protester, journalist, opposition politician, or promoter of freedom and peace, you are at greater risk, and thus using Passwords as an in-band solution—one in which compromising a device unlock pathway could compromise our secrets—already makes no sense. (I’ve seen some people recommend Bitwarden, not because of a necessarily superior security model, but because it’s open-source and has
an expansive free personal tier
that includes end-to-end encryption for synchronization among your devices.)
So this worry for the rest of us is a kind of prospective and speculative anxiety: that, in the wrong circumstances, all our passwords and other secrets would be exposed. While this happens regularly, the number of instances in which a passcode is obtained
and
malice occurs before we can stop it is fairly low. Most iPhones are stolen to wipe them for resale, which Apple has rendered difficult with the long-ago introduction of Activation Lock. Rather than knowing your passcode, criminals are more likely to try to
threaten you
or
use phishing
to obtain the passcode after they have the device.
Fortunately, Apple came up with a solution after the
Wall Street Journal
in 2023
exposed how a dangerous sequence of events
, which could start with drugging or violence, would allow thieves to reset an Apple Account and take over someone’s digital accounts and life.
We don’t yet have face-stealing technology
Stolen Device Protection uses a combination of delays and biometrics to deter thieves from accessing your data and accounts.
Apple’s
Stolen Device Protection
is a feature that may be one that has irritated you enough that you haven’t cared to understand how it may also keep your secrets safe. Go to Settings: Privacy & Security: Stolen Device Protection, and it’s likely enabled. Based on reports, I believe Apple enabled this by default in iOS 26.4. It’s available only for iPhones.
When enabled, it restricts a number of activities and requires Touch ID or Face ID for many authentication steps—passwords can’t be used instead. For the purposes of protecting your secrets, Stolen Device Protection has two key attributes:
It locks many actions for an hour, such as changing your Apple Account password. Even then, you have to use biometrics to start the countdown and before taking the action. Knowledge of a passcode isn’t helpful. If you have Away from Familiar Locations selected, this occurs only when the device isn’t in a place you routinely spend a lot of time, typically home and work.
You cannot view passwords or fill them into form fields from Apple’s Passwords system without using Touch ID or Face ID with Always enabled, so a thief having your passcode is out of luck. (If you have Away from Familiar Locations selected, a ne’er-do-well would have to be in one of those locations to use a passcode.)
This leaves one rotten scenario, in which you are kept under duress for at least an hour and are forced to use biometrics, then perform other actions. But how likely is that for most people? I don’t want to dismiss the distress of those who have been through that, but the likelihood of most people experiencing it is vanishingly small.
Leaving Stolen Device Protection enabled does mean that you may have to wait an hour in some scenarios to manage aspects of your Apple Account, make changes to Face ID or Touch ID, change your device passcode, and a few other actions. But this minor inconvenience might assuage the kinds of concerns that Scott wrote in about, and make you more comfortable that your big basket of secret eggs won’t scramble.
For further reading
I just updated my book
Take Control of Securing Your Apple Devices
to incorporate changes Apple has made in the last year, including in iOS 27, iPadOS 27, and macOS 27. In the book, I dig into risks and likelihoods further. The book takes the tack that Apple, having secured a lot of our data, now has implemented many protections against physical access to our hardware, including theft, and explains how to enable, configure, and manage a wide set of features.
[
Got a question for the column? You can email glenn@sixcolors.com or use
/glenn
in our
subscriber-only
Discord community.
]
[
Glenn Fleishman
is a printing and comics historian, Jeopardy champion, and serial Kickstarterer. His current books in preparation, which you can pre-order, are
Flong Time, No See
, and
That One Matt Bors Comic
. Other books include
Six Centuries of Type & Printing
and
How Comics Are Made
.
]
If you appreciate articles like this one, support us by
becoming a Six Colors subscriber
. Subscribers get access to an exclusive podcast, members-only stories, and a special community.
