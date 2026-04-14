---
title: Evan Hahn
created: 2026-04-10
updated: 2026-04-10
tags:
- person
- blogger
- open-source-maintainer
- web-security
- node-js
- javascript
- helmet-js
- ghost
aliases:
- evanhahn.com
- evan-hahn
---

# Evan Hahn

| | |
|---|---|
| **Blog** | [evanhahn.com](https://evanhahn.com) |
| **Email** | me@evanhahn.com |
| **Signal** | EvanHahn.64 |
| **Mastodon** | [@EvanHahn@bigshoulders.city](https://bigshoulders.city/@EvanHahn) |
| **GitHub** | [EvanHahn](https://github.com/EvanHahn) |
| **Role** | Software engineer at Ghost, open-source maintainer, technical writer |
| **Known for** | Helmet.js (226M+ downloads/year), Express in Action (Manning), human.json protocol, pragmatic error-handling philosophy |
| **Bio** | Software engineer at Ghost (nonprofit building software for independent publishers). Creator and maintainer of Helmet.js, a widely-used Node.js security middleware. Author of *Express in Action* (Manning) and *JavaScript Testing with Jasmine* (O'Reilly). Writes thoughtfully about error handling, software craftsmanship, developer ethics, and the human dimensions of programming. |

## Core Ideas

Evan Hahn is a **pragmatic engineer-philosopher** — someone who writes code that protects millions of web applications daily, but whose writing consistently returns to the human, ethical, and craft dimensions of software development. His work spans three interconnected domains: web security, developer practice, and the social responsibilities of programmers.

### Helmet.js: Security as Default

Helmet.js is Evan's most impactful technical contribution — a Node.js middleware that sets various HTTP headers to help protect web applications from common vulnerabilities. With **over 226 million downloads in 2025 alone**, it's one of the most widely deployed security packages in the JavaScript ecosystem.

The philosophy behind Helmet reflects Evan's broader approach to software: **make the secure choice the easy choice.** Helmet doesn't require developers to understand the nuances of Content Security Policy, X-Frame-Options, or Strict-Transport-Security — it applies sensible defaults that protect against the most common web attacks out of the box. This mirrors his writing on error handling: the best systems protect users (and developers) from their own mistakes by building safety in at the infrastructure level.

### The Two Kinds of Error: A Pragmatic Taxonomy

Evan's essay "[The Two Kinds of Error](https://evanhahn.com/the-two-kinds-of-error/)" is a **fundamental re-framing of error handling** that challenges the dominant "catch everything" mentality:

**Expected errors** (user enters invalid data, network fails) are part of normal operation. They're not the developer's fault, should be handled gracefully, and should return error results rather than throwing.

**Unexpected errors** (null pointer exceptions, assertion violations, uninitialized dependencies) are the developer's fault. They likely indicate bugs, should generally NOT be caught, and are allowed to crash the program.

This taxonomy has significant implications:

- **It rejects the false equivalence** of treating all errors the same way
- **It empowers developers to let things fail loudly** when something genuinely unexpected happens
- **It connects error-handling philosophy to language design** — Go forces you to handle expected errors; JavaScript makes everything throwable; Rust classifies most errors as expected at compile time
- **It scales with context** — a space probe's errors are almost all expected; a prototype's errors are almost all unexpected

The essay acknowledges its debt to Rust's error philosophy while making the case that **every language and project needs to consciously decide where the line between expected and unexpected falls.**

### The Lone Developer Problem

In "[The Lone Developer Problem](https://evanhahn.com/the-lone-developer-problem/)," Evan identifies a pattern that affects virtually all software: **code written by a single developer is often hard for others (including the original author, months later) to understand and maintain.**

His diagnosis is notably humble — "I don't know, but I suspect" — and identifies several causes:

- **Implicit knowledge**: When one person understands all the pieces, they connect them in ways that make sense only to themselves
- **Different requirements**: Solo projects often optimize for speed over maintainability
- **No code review**: Bad ideas are easier to implement when no one has to explain them to a colleague
- **Missing cross-pollination**: No one else's good ideas can enter the project

His proposed solutions are practical: bring in another developer, open-source the code (which creates social pressure for quality), or accept that not all code needs to be good code (hackathons, prototypes, scripts).

The essay is notable for its **intellectual honesty**: Evan explicitly acknowledges that this is anecdotal observation, not empirical research, and invites disagreement. This humility runs through all of his writing.

### How to Build Software Quickly: The 8/10 Rule

In "[How I Build Software Quickly](https://evanhahn.com/how-i-build-software-quickly/)," Evan offers a **pragmatic framework for balancing speed and quality**:

- **"Aim for an 8 out of 10, delivered on time"** — The code is good and does its job, with minor issues but nothing major, and it ships when promised
- **"Start with a rough draft/spike"** — Software, like writing, benefits from a first pass that you can refine
- **"Know how good your code needs to be"** — Different contexts demand different quality bars
- **"Reading code is, by far, the most important skill I've acquired"** — More important than writing code

This essay connects to his error-handling philosophy through the theme of **conscious trade-offs**: knowing when to invest in quality and when to ship something that's "good enough."

### Generative AI: Criticism from a User

Evan's "[How I Use Generative AI on This Blog](https://evanhahn.com/how-i-use-gen-ai-on-this-blog/)" is a **nuanced position statement** that refuses easy categorization:

- **He believes generative AI's cons far outweigh its pros** — "The world would be better off without generative AI"
- **He uses it anyway** — Both at work (where he's effectively forced to) and for his blog (where he chooses to)
- **His rule**: "The final product must be word-for-word what I would've written without AI, given enough time"
- **His use cases are narrow**: Like a thesaurus for finding alternative words, or brainstorming for specific examples
- **He prefers local models** running on his phone and laptop

What makes this essay notable is Evan's **strategic positioning**: he wants to change the minds of "AI maxxers," not preach to those who already hate AI. He believes "there's space for critique from a user of a technology they wish didn't exist" and that "these people are more likely to respect criticism from a daily user who's sympathetic to the benefits." He acknowledges the "discomfort and tension" this creates.

### human.json: Identity Through URL Ownership

Evan adopted the **human.json protocol** — a system for humans to assert authorship of their site content and vouch for others' humanity, using URL ownership as identity and trust propagation through a crawlable web of vouches.

This reflects Evan's broader commitment to **decentralized, web-native identity systems** that don't rely on corporate platforms. It's a small but philosophically significant gesture toward a more human-centered web.

### Ethics and Social Responsibility

In his "[Programming Beliefs as of July 2024](https://evanhahn.com/programming-beliefs-as-of-july-2024/)," Evan articulates a clear ethical framework:

- **"The most important problems are non-technical"** — Real-world issues matter more than code quality
- **"It matters who I build for"** — "Humanity is in trouble. An incomplete list of problems: climate change; war; authoritarianism; genocide; poverty; inequality; surveillance. I shouldn't waste my time building software for people who make these problems worse."
- **"Simple opinions tend to be wrong"** — Nuance matters; dogmatism about tools, languages, or processes is usually misplaced
- **"Everything is more complicated than you expect"** — A call for intellectual humility

## Key Quotes

> *"Expected errors should not throw, raise, or panic. Instead, they should return an error result."* — The Two Kinds of Error

> *"If you want to make your stuff more reliable, you'll trend toward expecting more and more errors. Lots can go wrong on a normal day!"* — The Two Kinds of Error

> *"I'm not an amazing programmer but I see this happen to myself all the time. I look at code I wrote a year ago and often find it confusing."* — The Lone Developer Problem

> *"My personal rule of thumb is to aim for an 8 out of 10 score, delivered on time."* — How I Build Software Quickly

> *"The world would be better off without generative AI. Despite this belief, I use it."* — How I Use Generative AI on This Blog

> *"Humanity is in trouble. I shouldn't waste my time building software for people who make these problems worse."* — Programming Beliefs as of July 2024

## Related

- [[concepts/web-security]] — HTTP security headers, middleware, defense-in-depth
- [[concepts/error-handling]] — Expected vs. unexpected errors, language design
- [[concepts/software-craftsmanship]] — Code quality, pragmatism, reading code
- [[concepts/open-source-maintenance]] — Maintaining widely-depended-upon packages
- [[entities/ghost]] — Nonprofit publisher software where Evan works
- [[concepts/decentralized-identity]] — human.json and web-native identity systems

## Sources

- [Evan Hahn's Blog](https://evanhahn.com) (2011–present)
- [The Two Kinds of Error](https://evanhahn.com/the-two-kinds-of-error/) (Mar 2026)
- [The Lone Developer Problem](https://evanhahn.com/the-lone-developer-problem/)
- [How I Build Software Quickly](https://evanhahn.com/how-i-build-software-quickly/)
- [My Programming Beliefs as of July 2024](https://evanhahn.com/programming-beliefs-as-of-july-2024/)
- [How I Use Generative AI on This Blog](https://evanhahn.com/how-i-use-gen-ai-on-this-blog/) (Mar 2026)
- [human.json](https://evanhahn.com/human-dot-json/) (Mar 2026)
- [Helmet.js](https://github.com/helmetjs/helmet) (226M+ downloads/year)
- [Express in Action](https://www.manning.com/books/express-in-action) (Manning)
- [JavaScript Testing with Jasmine](https://www.oreilly.com/library/view/javascript-testing-with/9781491943410/) (O'Reilly)
