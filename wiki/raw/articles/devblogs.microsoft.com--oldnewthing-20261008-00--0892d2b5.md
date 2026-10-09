---
title: "If one anti-malware software is good, does that make two better?"
url: "https://devblogs.microsoft.com/oldnewthing/20261008-00/?p=112762/"
fetched_at: 2026-10-09T10:01:08.306047+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# If one anti-malware software is good, does that make two better?

Source: https://devblogs.microsoft.com/oldnewthing/20261008-00/?p=112762/

A colleague on the enterprise support team was investigating a complex failure from a customer, and after much analysis, it appeared that the problem was that the system had two different anti-malware programs installed. Let’s call then Contoso and Fabrikam. Fabrikam called a function that Contoso had detoured. Contoso’s detour thought this was suspicious, so it tried to quarantine the Fabrikam process. Unfortunately, Fabrikam had also detoured a function that Contoso was using. The result was mass confusion as the Contoso ended up calling into something that it was trying to quarantine.
Installing two anti-malware programs on the same system is like hiring two different security companies to patrol your building. If they don’t know about each other, each is going to think the other one is an intruder. If you’re lucky, their instructions are merely to report on suspicious activity.
But if you give them weapons and the authority to use them, you may end up with your two security companies pointing their weapons at each other.
In real life, you would introduce the two security companies to each other, or at least make sure they don’t patrol the same floor.
In software, this is harder to do. It’s not like you can invite two programs to lunch and have them get to know each other.
Anti-malware software typically does things that aren’t officially supported, like detouring system functions. And these detours mean that calling a system function no longer does the system thing; instead, it calls into the anti-malware software, and it might decide to do something unrelated to the system function you thought were calling, and that unrelated thing may itself start causing problems, say, by hanging. Not only is there no easy way to identify that this has happened, short of debugging an actual malfunctioning system, but even after you figure out the conflict, there’s usually no way to tell each anti-malware software to “stay on its floor.”
