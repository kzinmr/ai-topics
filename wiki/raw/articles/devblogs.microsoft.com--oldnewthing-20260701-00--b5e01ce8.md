---
title: "It rather involved being on the other side of this airtight hatchway: Changing administrative settings"
url: "https://devblogs.microsoft.com/oldnewthing/20260701-00/?p=112498"
fetched_at: 2026-07-02T07:01:20.602957+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# It rather involved being on the other side of this airtight hatchway: Changing administrative settings

Source: https://devblogs.microsoft.com/oldnewthing/20260701-00/?p=112498

A security vulnerability report arrived that went roughly like this:
An attacker can bypass security policies by modifying the following registry keys to disable ⟦security feature 1⟧ and ⟦security feature 2⟧.
The statement is true, but what they don’t mention is that administrator privileges are required to modify those keys. This is like saying that a door lock is insecure because you can open the door from the inside. If you are inside, then you have already gotten past the door!
Indeed, the purpose of those keys is to define the security policy in the first place! So it boils down to “It’s a security vulnerability that an administrator can change a security policy.”
What the security researcher found was that if your system has been compromised, the first guy who gets into your inner sanctum can make your system even more vulnerable.¹ If you assume that the attacker has full control, then it’s not surprising that they control everything.
¹ Isn’t this the plot to half of the sci-fi movies ever made? The plucky hero sneaks behind enemy lines in order to disable the bad guys’ shields long enough to let the rest of the team in. This isn’t a security flaw in the shields. It’s a security flaw in whatever was supposed to protect the switch that turns off the shields.
The sci-fi movie analogy would be “If we can get to the switch that turns off the shields, then we can turn them off!”
Well, yeah. The hard part is getting into the room that has the switch.
It rather involved being on the other side of this airtight hatchway.
Bonus chatter
: This is a repeat of
It rather involved being on the other side of the airtight hatchway: Disabling a security feature as an administrator
, but this type of bogus vulnerability report happens so much, I wrote it up again before I realized that it was a duplicate.
