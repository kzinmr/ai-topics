---
title: "Having two security products installed at the same time isn't a great idea, but sometimes you have to do it"
url: "https://devblogs.microsoft.com/oldnewthing/20261123-00/?p=112887/"
fetched_at: 2026-11-25T10:00:48.790874+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Having two security products installed at the same time isn't a great idea, but sometimes you have to do it

Source: https://devblogs.microsoft.com/oldnewthing/20261123-00/?p=112887/

Not too long ago, I noted that
if you install multiple anti-malware products, they might each think the other is malware
.
I used a metaphor of hiring two security services to patrol your building and making sure they know about each other so that they don’t treat the other one as an intruder. And I noted that you can’t introduce software products to each other.
But you can, sort of.
You can add each program to the other program’s exclusion list.
So that at least lets them recognize each other, but that is only part of the problem.
The bigger problem is that both products have made modifications to the system, and if they both try to modify the same thing (say, detouring the same function), things can get ugly. In fact, things can get ugly even if they detour different things, but happen to introduce dependencies that result in a collaborative lock hierarchy violation. For example, program 1 might detour a registry function, and their detour contacts a Web service to do some logging or validation, and program 2 detoured the network call, and in
that
detour, they access the registry to get some configuration information.
Deadlock.
In the building analogy, it’s as if both security companies tried to rewire the elevator. Who knows if one set of wires causes the other to start a fire. Or maybe one security company rewires the elevator so it makes a phone call to validate that the floor request is valid, but the other security company rewired the phone system so that whenever somebody tries to make a phone call, it summons security personnel to check on who is making the call, and the security personnel might need to use the elevator to get there.
Commenter Michael Taylor asserts that best practice is
not to install two anti-malware programs at the same time
because they can collide with each other.
The problem with large enterprises is that they sometimes feel that they are forced into installing multiple security software products because no single product does everything they want.
For example, they may have one security package to prevent users from running malicious programs. And then endpoint detection and response software, for identifying and blocking suspicious network activity. And then they also have data loss protection software, to identify attempts to copy sensitive information to insecure locations, like copying a corporate document to a removable USB drive or uploading it to an unauthorized cloud service. And even if the cloud service is authorized, the data classification software needs to transfer the security classification of the document to the copy in the cloud service. These security classifications may be necessary for regulatory reasons, such as HIPAA or GDPR compliance.
If you can’t find one program that does it all, then you find yourself forced to cobble together a hodgepodge of programs and take the risk that they won’t conflict.
