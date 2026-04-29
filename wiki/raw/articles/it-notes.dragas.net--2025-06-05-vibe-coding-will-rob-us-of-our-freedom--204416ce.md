---
title: "Vibe Coding Will Rob Us of Our Freedom"
url: "https://it-notes.dragas.net/2025/06/05/vibe-coding-will-rob-us-of-our-freedom/"
fetched_at: 2026-04-29T07:02:10.921490+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Vibe Coding Will Rob Us of Our Freedom

Source: https://it-notes.dragas.net/2025/06/05/vibe-coding-will-rob-us-of-our-freedom/

It was one of those Friday afternoons when everyone just wanted to go home, but their PM had
that look
we all know too well. I manage the infrastructure for this mid-sized e-commerce client, so I get to see their development process from the server side. Their deadline was, as it often is,
completely insane
.
"Alex", a junior developer on their team - I've been watching his commits for about six months now - got stuck with this backend task. I watched him struggle with it for a day, then suddenly,
boom
. Using an AI assistant, he churned out what seemed like working code in
half the expected time
. Their management was thrilled.
Seeing how quickly it came together, I suggested they double-check the code before deployment – I'd rather avoid any potential headaches down the line. But with everything "working" perfectly, they considered it a waste of time.
The vibe was right.
So, into production it went.
That dismissal didn't sit right with me. So, a few days later, I decided to check the code myself. On the surface, it looked clean, even polished. But then I saw
that line
. A single, innocuous-looking database query.
The AI had constructed it in a way that was wide open to a classic SQL Injection attack.
Alex's tests, done with "normal" fake user data, passed perfectly. But a malicious actor could have
wiped their entire user database
with a single, cleverly crafted request. The code worked, but it was a ticking time bomb sitting on my servers. And Alex, who had trusted the tool, had no idea.
Now, before anyone thinks I'm throwing Alex under the bus -
absolutely not
. From what I can see, he's a smart developer dealing with impossible deadlines. I've seen this pattern with other clients too. He's just a symptom of a much larger, more insidious trend I'm calling
"Vibe Coding"
.
It's this methodology (if we can call it that) where developers, pressured by deadlines, are no longer trained on code structure, but on the
"vibe"
– that is, on giving the right prompts to AIs and testing only if the output
seems
to work.
Alex isn't just a case of insecure code.
He's proof of how we're becoming dependent on tools we don't control.
We're shifting from being architects to being interior decorators.
An
architect
understands the foundations, the structural integrity, the load-bearing walls. A
decorator
can make a room look good, but has no idea if the entire building is about to collapse.
And here's what really scares me. I can already see the future: AIs will require ever-increasing computing power, and developers will no longer be trained on code, but on
prompting
. It's not hard to imagine where this leads. To the
complete loss of programming skills
and, in turn, to the
complete loss of the ability to write code not controlled by the big players
.
Indeed, it wouldn't be difficult for them to force the use of specific languages or to produce specific outcomes. In the end, the program works, and the "vibe coder" will no longer be able to understand what it's really doing.
It works → it can go to production. End of story.
Many developers are terrified of losing their jobs for this very reason: AIs sometimes program better than them. And, in my opinion,
they are right to be afraid
. But I'm more afraid of a world (and not just in IT) where code will depend
exclusively
on the companies that sell us AIs.
Today, writing code is something
free
, potentially doable even on a beat-up laptop. But tomorrow? Will we be completely dependent on AIs
(even)
for this?
As
Serena Sensini rightly argued at OSDay 2025
- and her talk really stuck with me -
the point is not to let ourselves be replaced by AIs, but to use them to improve ourselves and our productivity.
We must use these tools to help developers like Alex become
true architects
, not just decorators who are skilled with a new kind of brush. We must always maintain our skills and our irreplaceability.
Because the day we stop writing code, we will stop being free and independent.
