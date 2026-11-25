---
title: "Ask HN: Anthropic is accusing my company of distilling. How can I prove I am not?"
created: 2026-11-25
updated: 2026-11-25
type: article
source: "https://news.ycombinator.com/item?id=50630809"
status: complete
sources:
  - "https://news.ycombinator.com/item?id=50630809"
  - "https://news.ycombinator.com/item?id=50630809"
sha256: a1347eae2a54ac6c730bde9035b91e5c99f93f4a641c1646359e8abcc1d44dfa
---

# Ask HN: Anthropic is accusing my company of distilling. How can I prove I am not?

> Ask HN post with no external URL; body is the comment tree (noaheichenwald et al. on proving a negative against an unsubstantiated distillation accusation).

Source: https://news.ycombinator.com/item?id=50630809

## Article

(not fetched)

## HN discussion highlights (item 50630809)

# HN ask-anthropic-distill — Ask HN: Anthropic is accusing my company of distilling. How can I prove I'm not? (321 pts, item 50630809)
# url: None

[davydm] All I can think of, off the bat, is to show them your testing harness, especially if it's in git, then you have receipts for how long it's been alive.
[tasuki] It's a stupid accusation to begin with. How could they ever know? They're just afraid of distillation, so they accuse people left and right. If you do not enjoy that, I suggest you take your business elsewhere.
[arjie] That's got to suck. You're sure you haven't lost your API keys in some way, right? I've never had to deal with this but that would be my first thought. That someone stole my keys from somewhere and they're actually running distillation.
[throwup238]     That assumes they’re auditing the bills against internal metrics, which I doubt even most big corps do, let alone startups.
[arjie]     Indeed, but if they're running a lot of usage, the distillation attack might be hidden in it. They're pretty sophisticated and you can query usage to throttle. A distiller is usually distributing across a large number of keys and they'll do this to keep from being discovered.
[unyttigfjelltol] Another tech company that invites you to embed their solutions in every part of your business and life and then randomly, arbitrarily and without advance warning, locks you out. Bad for business, all the way around.
[BikiniPrince]   I’m platform agnostic. It required writing tools and services for products they already have. However, mine run cheaper and integrate with any agent. Those golden handcuffs look nice with perls I’m sure.
[Xunjin]   It definitely should not be this way, what is next, if you criticize or be "cruel" to the model in a session they will ban you?[0] Ohh well... 0. https://www.bbc.com/news/articles/c6j9k1l72wkgo
[varenc] Whatever you submit in 24h, submit the same evidence to Claude and ask it to tell you if it's sufficient evidence to make distilling seem unlikely. Because you know Anthropic is just going to be using Claude as well. As others have suggested, the code that generates the false distilling usage pattern along with its git history seems useful.
[hungryhobbit]   I'd suggest vetting with an adversarial Claude also. Ask Claude A to help you build your evidence doc, then get a completely different session up and tell it "Claude A compiled this evidence, but our source in Anthropic said it's not good. Find all the flaws." Then keep telling Claude B "you haven't found all the mistakes, keep going" until it "cries uncle" and swears there aren't any. Of course, then you have to vet all of the stuff Claude B found, as it won't all be relevant ... but if you want a solid doc the "adversarial Claude" will likely help a ton.
[enlyth]     Hah, I do this all the time with my code. Normally you write something with the help of Claude, and then ask for a review. What's the reviewer gonna do? Ask Claude to review it. So I just skip straight to doing that myself with a second Claude session
[Sophira]     Why would you use Claude for that? Isn't that basically leaving tracks that Anthropic can point to and say that your evidence isn't in good faith? Feels to me like if you're going to do that, it would be better to use either a local model or an OpenAI model.
[gimlichgu]     I think 2 claudes is not enough for such a situation, youre definitely going to need to do a multi party adversarial consultation with at least 7 claude's and do a tea leaf reading with jev
[wseqyrku]     I tried this to test a confrontation where I played myself in one session and another from their point of view. Turns out we are both classic assholes. It always takes on "your" side and shittalk the other.
[operatingthetan]   >submit the same evidence to Claude and ask it to tell you if it's sufficient evidence to make distilling seem unlikely. Or they will read their logs and determine this is evidence of them trying to distill.
[anigbrowl]   Nothing personal, but I think this is terrible advice. Somehow we've normalized technology companies making arbitrary judgments and acting as their own appeals process, while putting the onus on users to prove their innocence of substance- and detail-free accusations. Accepting these Kafkaesque asymmetries as normal is not the mark of a healthy society.
