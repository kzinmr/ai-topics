---
title: "The Email They Shouldn't Have Read"
url: "https://it-notes.dragas.net/2025/10/08/the-email-they-shouldnt-have-read/"
fetched_at: 2026-04-28T07:02:49.637871+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# The Email They Shouldn't Have Read

Source: https://it-notes.dragas.net/2025/10/08/the-email-they-shouldnt-have-read/

Author's Note:
Before we begin, an important clarification. What follows is a horror story based on real events from my career. However, to protect the privacy of the people and companies involved, I have deliberately mixed things up: technologies, contexts, and specific details have been modified or merged with other experiences. I therefore invite you to read this story not as a strict chronicle of a single event, but as an archetype of a widespread problem in the IT world: vendor lock-in and predatory business practices. Any attempt to identify the specific company or software described would lead to an incorrect conclusion. More about it
here
.
When the phone rang, I was in a meeting - so I didn’t answer. But I recognized the number and sent a quick message:
"I’m with a client right now. If it’s not urgent, please send me an email - otherwise I’ll call you ASAP".
The reply, via SMS, left me speechless:
"That’s exactly the problem. I can’t send you an email. Call me as soon as you can".
From that moment on, my perception of a certain kind of world changed forever.
A few years earlier, a major public institution - let’s call it
Agency A
- was still running an ancient Exchange mail server. It hadn’t received security updates for ages, the anti-spam was completely ineffective, and the new regulations were clear: embrace Open Source solutions whenever possible.
They had already received a proposal - expensive but, when compared to similar offers made to other organizations, apparently reasonable - for a managed service hosted by an external provider and based on an open source mail stack. The company offered a managed version with its own proprietary additions and enterprise support.
The catch? While such pricing had become almost "normal" in the market, it was still wildly inflated considering what was actually being delivered.
Agency A
already had solid infrastructure - reputable IP classes, redundant datacenters, everything running smoothly. We had built and maintained that environment for years, and it was still performing perfectly.
The request was simple:
“Evaluate this solution, and if it’s suitable, we’ll migrate.”
. About 500 active mailboxes, roughly the same number of aliases. Manageable, but far from trivial.
So I started experimenting. I had heard of that stack before but never used it directly. I deployed it in some non-critical environments - ours, and a few test clients who agreed to try it at a discounted rate. Everything worked flawlessly for almost a year. I began to appreciate its design and flexibility. Confident, I told
Agency A
we could proceed with a pilot migration.
We built a new server, deployed the stack, and assigned a few secondary domains for early adopters. The feedback was great - so good that users started pushing for a full migration.
The IT team planned carefully: created accounts and aliases, migrated selected mailboxes, and kept the old Exchange server online (hidden, for legacy access).
The morning after the MX switch I was tense, waiting for trouble - but it never came. A couple of small questions, nothing serious. The internal team handled everything perfectly. It was a success.
Word spread quickly.
Agency B
- smaller, but in some ways more influential - contacted me. They were customers of the same managed-service company that had pitched to
Agency A
. Once they saw the potential savings (at less than a tenth of the annual cost), the stability, and the freedom of keeping their data on their own servers, they became very interested. Their contract, however, was a five-year deal with automatic renewal - two years left. The legal office said the notice period was six months, so there was time.
They wanted to prepare silently. Their supplier was known for
aggressive commercial behavior
and often retaliated when customers tried to leave. So we built everything quietly - users, aliases, test setups - and froze the system, waiting for the official termination notice.
That day finally came. The notice was sent, about eight months before expiration. Migration would begin upon confirmation of receipt - or the following month at the latest.
Meanwhile, I learned that
Agency C
- another institution - was also planning to leave the same provider. They wanted to keep the same software stack for consistency, so I told them about our experience. They asked for a quote, which I prepared (without mentioning
Agency B
, of course). My margin would have been small, but the project made sense: it was about
owning your data
, not making money.
Everything seemed to move smoothly - until that SMS.
I called back immediately.
"There’s been a problem with the termination" said the IT manager of
Agency B
.
"Somehow they found out what we were doing. There are hidden clauses we didn’t know about, and now we can’t leave - at least not for another five years. They know everything. Even your quote.".
I was stunned. How could they possibly know?
Minutes later, my phone rang again -
Agency C
this time.
"Forget the proposal", they said. "They called us. Threatened us, actually. They even mentioned your name and said they might take legal action against you for unfair competition - claiming they’re the only
‘authorized’
installers of that software. Which is absurd, of course. It’s open source. But our director doesn’t want trouble.".
Sometimes, when public money is involved, people prefer avoiding troubles over doing what’s right.
Something didn’t add up.
Then someone at
Agency C
noticed a clue: a former interim IT manager still had an email client connected via token authentication - with access to all messages. And that person had signed the original contract with the provider years before. Informally questioned, he admitted contacting them "to warn them" but claimed it was harmless. He never mentioned me - supposedly.
That still didn’t explain how they knew about
Agency B
’s internal steps. To test a theory, we set a trap: I asked a friend abroad to send
Agency B
a fake quote, from a company outside the EU.
The following Monday, the provider called
Agency B
and said, "We advise against working with non-EU companies - compliance can get tricky.".
That strongly suggested it:
it looked as if they might have been reading the emails.
The IT manager exploded and confronted them. The response was chilling:
"I’m not saying we do - but we could. It’s in the contract. You should read the fine print, especially the unilateral amendment from two years ago.".
That amendment, quietly accepted, included horrifying clauses:
- notice period extended from 6 to 12 months
- formerly free services could become paid at the provider’s discretion
- and, "for security reasons", they could disable any access other than the webmail - which they promptly did.
All of this happened before the GDPR era, when certain practices could still slip through.
I tried to contact the company’s owner directly - no reply. Calls, emails, nothing. Their support lines were "not authorized to forward requests". I wanted to confront them about the
“not accredited”
nonsense and the so-called
unfair competition
. But bullies never like a fair conversation.
I urged
Agency B
and
C
to investigate - not only legally, but ethically.
They were horrified, yes - but in the end, nothing changed.
Worse: the provider, invoking that same contract amendment, made previously free features paid ones, increasing their costs by another 30%.
Management wasn’t outraged by the abuse - just by the extra expense, "hard to justify in the budget".
Years later, those directors were gone. The technical staff remained - older, wiser, and determined not to repeat the mistake. They eventually switched providers, though to something "safer", not necessarily better.
I couldn’t solve that problem. The battle had to come from them, and I would have supported them all the way - not for profit, but for principle.
Because when a company that claims to
“support open source”
behaves like that, we all lose.
We all get labeled the same way.
And that’s the real horror of the story - not the software, but what people do with it.
