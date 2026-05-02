---
title: "Terence Eden"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Terence Eden

## Overview

**Terence Eden** (pronounced "ed-en") is a technology policy expert, open-source advocate, web standards contributor, and blogger. Based in the UK, he has worked at the intersection of government technology, open data, accessibility, and digital rights for over two decades. He served as a technical advisor to the [[concepts/uk-government-digital-service]] (GDS), where he helped shape the government's approach to open standards and digital accessibility.

Eden blogs at [[concepts/shkspr.mobi]] — a minimalist, self-hosted site he has maintained for years — where he writes about technology policy, open-source sustainability, web accessibility, and the practical consequences of digital design decisions. His work is characterized by **pragmatic idealism**: he believes in open systems and transparent governance, but grounds his advocacy in concrete technical experience and real-world deployment.

He is the creator of several open-source projects including **ActivityBot** (a single-file PHP ActivityPub server under 80KB), **OpenBenches** (a crowdsourced database of 40,000+ memorial benches worldwide), and various bot implementations for decentralized social networks. He is also a prolific speaker on open-source governance, accessibility, and the future of the open web.

---

## Timeline

| Period | Key Events |
|--------|-----------|
| ~2000s | Begins blogging at shkspr.mobi; develops expertise in web standards and accessibility |
| 2010s | Works with [[concepts/uk-government-digital-service]] (GDS); contributes to government digital policy |
| 2014 | Publishes *"Please Stop Inventing New Software Licences"* — widely-cited critique of non-standard open-source licensing |
| 2015 | Publishes plea for *"Easy APIs Without Authentication"* — advocating for open data access |
| 2017 | Follow-up on API accessibility — documenting the decline of open APIs |
| 2020 | Publishes *"The Seven Levels of Open Source"* — influential taxonomy of open-source participation models |
| 2022 | **OpenBenches** reaches 40,000 memorial benches catalogued worldwide |
| 2024 | ActivityBot released — single PHP file implementing full ActivityPub server |
| 2025 | Publishes *"Open Data Man"* essay at Open Data Camp on personal data disclosure ethics |
| 2025 | Writes *"How Can Governments Pay Open Source Maintainers?"* — based on UK Government experience |
| 2026 | Reviews *Diversifying Open Source* by Paloma Oliveira; publishes *"Are there any open APIs left?"* documenting API ecosystem collapse |

---

## Core Ideas

### The Seven Levels of Open Source

In 2024, Eden published an influential taxonomy categorizing open-source projects into **seven levels of openness**:

1. **Look but don't touch** — Source is viewable but not redistributable or modifiable
2. **Do What Thou Wilt** — Unrestricted use, distribution, and modification
3. **Do As You Would Be Done By** — Open with requirements (copyleft, attribution)
4. **I'd rather you didn't** — Open with ethical restrictions (no military, no racist use)
5. **Contributors Welcome** — Open community participation (GitHub-style)
6. **Blessed Contributors** — Open source but closed governance (Google/Android model)
7. **The Future** — New paradigms of openness that don't fit traditional categories

This framework is significant because it moves beyond the binary "open vs. closed" debate and recognizes that **openness exists on a spectrum**. Eden's taxonomy helps developers and organizations articulate what kind of openness they actually want, rather than using "open source" as a meaningless marketing term.

His level 7 is particularly forward-looking:

> "There is something coming that you and I cannot understand. Deep in the darkest trenches of the Internet comes a new breed of hacker... They are building a new form of Open Source. Something that reflects the needs and concerns of their generation, rather than the tired problems of ours."

This demonstrates Eden's humility about his own frameworks — he recognizes that the next generation will redefine openness in ways he cannot predict, and that's okay.

### Government Open-Source Funding

Eden's experience within the [[concepts/uk-government]] gives him unique insight into the structural barriers preventing public-sector support for open-source software. His 2026 post *"How Can Governments Pay Open Source Maintainers?"* is a masterclass in pragmatic policy analysis:

**Problem 1: Ownership ambiguity.** "Lots of OSS doesn't have a well defined owner; so who gets the money?" Governments need to know who they're funding and where the money is going. The risk of accidentally funding sanctioned entities is real.

**Problem 2: Payment mechanisms.** "Many OSS projects get around this by offering support contracts." But donation-based models don't work for government procurement, which requires invoices, purchase orders, and formal vendor relationships.

**Problem 3: Multi-contributor governance.** "How does a moderately sized project decide who receives what share of the funding?" Services like OpenCollective help, but government procurement systems aren't designed for distributed payment.

**Problem 4: Ideological resistance.** "Some OSS projects didn't want to take money from the 'big bad state.'" Anti-government sentiment, while understandable, cuts projects off from a major potential funding source.

Eden's recommendations are concrete:

> "Make it easy for Governments and other large organisations to pay you. Be as obvious as possible that you are able to accept payments from them. Don't be afraid to put a large price on your talents."

This is practical advice from someone who has been inside the system and knows how it works.

### The Death of Open APIs

In his January 2026 post *"Are there any open APIs left?"*, Eden documents a decade-long decline in open web APIs. He revisits APIs he recommended in 2014 and finds:

**Still alive:** Wikipedia, Police.uk, Google Books, Open Notify (space data)

**Dead:** BBC Radio 1, Twitter URL statistics, Star Wars API, British National Bibliography

**Alive but key-required:** Google Location, Spotify, OpenMovieDB

His analysis of **why APIs die** is structural, not conspiratorial:

1. **Cost.** "APIs cost money to run. Yes, even the static ones have a non-zero cost."
2. **Lack of analytics.** "It's hard to build a service if you don't know who is using it."
3. **No communication channel.** "There's no way to communicate with an anonymous consumer."
4. **Abuse prevention.** "Being able to throttle bad actors (figuratively or literally) is a desirable feature."

The "something something … enshittification" quip acknowledges the popular critique while pointing to more nuanced structural causes. Eden's analysis is valuable because it doesn't blame individual bad actors — it identifies **systemic incentives** that drive API closure.

His conclusion is both melancholy and practical: the dream of Web 2.0 — seamless, open integration between services — has largely died. What remains are walled gardens with API keys, rate limits, and terms of service.

### Lightweight Decentralization

Eden's **ActivityBot** project — a full ActivityPub server in a single PHP file under 80KB — embodies his philosophy of **accessible decentralization**. While Mastodon and other Fediverse projects require complex infrastructure, ActivityBot demonstrates that decentralized social networking can be trivially simple:

> "Single PHP file which can run an entire ActivityPub server and it is less than 80KB."

This is not a toy — it powers live instances including the OpenBenches bot and solar monitoring bot. Eden's approach is the inverse of most Fediverse development: instead of building comprehensive platforms, he builds **minimal, composable services** that do one thing well.

His live bot instances are practical examples:
- **@openbenches@bot.openbenches.org** — Memorial bench cataloguing
- **@colours@colours.bots.edent.tel** — Color-based social experiment
- **@solar@solar.bots.edent.tel** — Personal solar generation data

### Personal Open Data Ethics

At the 2025 Open Data Camp, Eden ran a session on **personal data disclosure** — what happens when individuals choose to release their own data as open data. His essay "Open Data Man" is notable for its honesty about the tradeoffs:

He releases his **home's solar generation statistics** as raw open data (cited in several academic papers). He shares his **energy consumption data** at 30-minute granularity with The Living Lab. But he draws a hard line at personal medical data:

> "Some people are very open with their intimate medical data. I'm not. I haven't released a 3D model of my brain scans just in case someone clones my brain."

The humor masks a serious point: **different types of data carry different risks**, and individuals should make informed choices about what they share. Eden's framework is not prescriptive — it's analytical. He wants people to understand the implications before they publish.

### Accessibility as a Technical Requirement

Eden's work consistently treats accessibility not as an afterthought but as a **core technical requirement**. His cross-browser Unicode rendering bug discovery (National Theatre programme misrendering "Ronkẹ Adékọluẹ́jọ" in Firefox/Safari but not Chrome) demonstrates how accessibility failures are often **invisible to the majority** but devastating for affected users.

His review of Paloma Oliveira's *Diversifying Open Source* reinforces this:

> "When projects focus purely on technical excellence without considering accessibility, they create implicit barriers."

For Eden, accessibility is not a checkbox — it's a fundamental design constraint that shapes architecture from the ground up. His minimalist blog design (eInk mode, xterm mode, high-contrast themes) is itself an accessibility statement: **the web should work for everyone, on every device**.

### Open Standards Over Proprietary Lock-In

Eden's 2014 essay *"Please Stop Inventing New Software Licences"* (later cited in Oliveira's book) critiques the proliferation of non-standard open-source licenses. His argument is that **license proliferation fragments the ecosystem**, making it harder for organizations to evaluate and adopt open-source software.

This principle extends to his broader philosophy: **standardization enables participation**. When everyone uses different licenses, different protocols, different authentication schemes, the cost of participation increases. Eden advocates for using existing standards wherever possible and inventing new ones only when absolutely necessary.

His FOAF (Friend of a Friend) analysis reveals the flip side: **standards can become over-engineered**. The oscillation between "complex cryptography/key-signing ceremonies" and "byzantine XML RDF" shows how the pursuit of a perfect trust protocol can produce something nobody actually uses.

### The Corporate AI Deflection Problem

Eden's observation about companies routing customers to AI chatbots during peak call volumes reveals a deeper critique: **automation as deflection rather than solution**.

> "Companies aggressively route customers to AI/WhatsApp chatbots during peak call volumes. This suggests flawed predictive staffing models and over-reliance on automated deflection rather than capacity planning."

This is Eden at his most pragmatic: he's not anti-AI, he's anti-bad-design. If AI chatbots were solving the underlying problem (insufficient human support capacity), they'd be useful. But they're being used to mask the problem, not fix it.

### AI Model Releases & Security Implications (2026)

In April 2026, Eden wrote ["Does Mythos mean you need to shut down your Open Source AI?"](https://shkspr.mobi/blog/2026/04/does-mythos-mean-you-need-to-shut-down-your-ope--021b2763) analyzing the [[concepts/claude-mythos|Claude Mythos]] release and its implications for open-source AI hosting. He concluded that Mythos demonstrated real cyber-capability risks but argued against panic-driven shutdowns of open-source AI infrastructure.

### NHS Goes To War Against Open Source (May 2026)

In May 2026, Eden published a detailed critique of the NHS's decision to effectively ban open-source software from its procurement pipeline. The piece documented how the NHS's new vendor requirements — ostensibly about security — functionally excluded open-source projects that cannot provide formal compliance documentation or indemnification insurance.

Key arguments:
- **Open-source software is not inherently less secure** — in fact, the transparency enables faster vulnerability discovery and patching
- **The real issue is procurement process, not technical capability** — NHS vendors can provide formal SLAs, compliance certifications, and legal indemnification that open-source maintainers cannot
- **This creates a perverse incentive**: vendors wrap open-source software in proprietary packaging to meet procurement requirements, adding cost without adding value
- **The NHS's own open-source contributions** (like the NHS App's frontend framework) become collateral damage

Eden's analysis connects to his broader themes: **standardization enables participation**, and when procurement processes favor closed systems, the ecosystem suffers. He drew parallels to his earlier work on open API decline and government data transparency.

### Regulatory Data Transparency

Eden's experience trying to access historic energy price cap data from Ofgem reveals a structural problem in government data publication:

> "I couldn't find the complete historic data on their site. So I sent a quick email asking for it which they treated as a Freedom of Information request."

The pattern is clear: regulators publish current data (useful for today's decisions) but not historical data (essential for research, analysis, and accountability). Citizens who need historical data must file FOI requests — a process designed for specific, individual inquiries, not systematic data access.

Eden's response is typically pragmatic: file the FOI, get the data, publish the analysis. But the underlying critique is that **proactive data publication** would serve both citizens and regulators better than reactive FOI processes.

---

## Key Quotes

> "There is something coming that you and I cannot understand. Deep in the darkest trenches of the Internet comes a new breed of hacker."

> "Make it easy for Governments and other large organisations to pay you. Be as obvious as possible that you are able to accept payments from them. Don't be afraid to put a large price on your talents."

> "Single PHP file which can run an entire ActivityPub server and it is less than 80KB."

> "When projects focus purely on technical excellence without considering accessibility, they create implicit barriers."

> "I haven't released a 3D model of my brain scans just in case someone clones my brain."

> "Standardization enables participation." (paraphrased from license proliferation critique)

> "APIs cost money to run. Yes, even the static ones have a non-zero cost."

---

## Recent Themes (2024–2026)

**2024:** Published "The Seven Levels of Open Source" taxonomy. Released ActivityBot (single-file PHP ActivityPub server). OpenBenches reached 40,000 memorial benches catalogued. Continued advocacy for open-source sustainability.

**2025:** Published "Open Data Man" essay on personal data disclosure ethics at Open Data Camp. Wrote "How Can Governments Pay Open Source Maintainers?" based on UK Government experience. Continued development of decentralized bot infrastructure.

**2026:** Published "Are there any open APIs left?" documenting a decade of API ecosystem decline. Reviewed *Diversifying Open Source* by Paloma Oliveira, citing his own 2014 license critique. Identified cross-browser Unicode rendering bugs affecting accessibility. Advocated for lightweight, minimal approaches to decentralized infrastructure. Published "Does Mythos mean you need to shut down your Open Source AI?" analyzing Claude Mythos cyber-capability implications. Published "NHS Goes To War Against Open Source" critiquing procurement processes that functionally exclude open-source software.

---

## Related

[[concepts/uk-government-digital-service]] — Eden's former employer; shaped UK government digital policy
[[concepts/activitypub]] — Decentralized social networking protocol; Eden built ActivityBot
[[concepts/openbenches]] — Eden's crowdsourced memorial bench database (40,000+ benches)
[[concepts/open-data]] — Eden's advocacy area; published personal solar and energy consumption data
[[concepts/foaf]] — Friend of a Friend trust model Eden has analyzed
[[concepts/mastodon]] — Fediverse platform; Eden's bots interact with it via ActivityPub
[[concepts/web-accessibility]] — Eden treats as core technical requirement, not afterthought
 — Eden's 2014 critique of license proliferation
 — UK energy regulator; Eden's FOI experience with historic data
Freedom of Information — Process Eden uses to access government data
 — Language Eden uses for minimalist ActivityPub implementation

---

## Sources

- [shkspr.mobi](https://shkspr.mobi) — Primary blog
- *The Seven Levels of Open Source* (2024)
- *How Can Governments Pay Open Source Maintainers?* (March 2026, originally on Hackernoon)
- *Are there any open APIs left?* (January 2026)
- *Open Data Man – how open is too open?* (2025)
- *Please Stop Inventing New Software Licences* (2014, cited in Oliveira's *Diversifying Open Source*)
- *Easy APIs Without Authentication* (2015)
- ActivityBot — Single PHP file ActivityPub server ([GitHub](https://github.com/edent))
- OpenBenches — 40,000+ memorial benches ([openbenches.org](https://openbenches.org))
- GitHub: [@edent](https://github.com/edent) — Open source projects
- Bluesky: [@edent](https://bsky.app/profile/edent) — Social media presence
- UK Government Digital Service — Eden's former employer

## References

- shkspr.mobi--blog-2026-04-android-now-stops-you-sharing-your-location-in---de2e8f86
- shkspr.mobi--blog-2026-04-better-tts-on-linux--f770e312
- shkspr.mobi--blog-2026-04-book-review-how-to-kill-a-witch-a-guide-for-the--a423bf01
- shkspr.mobi--blog-2026-04-book-review-small-comfort-by-ia-genberg--6a80f3d3
- shkspr.mobi--blog-2026-04-book-review-superintelligence-paths-dangers-str--cec9583c
- shkspr.mobi--blog-2026-04-book-review-up-a-scientists-guide-to-the-magic---aabbad6d
- shkspr.mobi--blog-2026-04-cheapest-way-to-keep-a-uk-mobile-number-using-a--64bcfc4c
- shkspr.mobi--blog-2026-04-did-wordpress-vip-leak-my-phone-number--8bd58bd0
- shkspr.mobi--blog-2026-04-does-mythos-mean-you-need-to-shut-down-your-ope--021b2763
- shkspr.mobi--blog-2026-04-lets-get-digging--0b28883d
- shkspr.mobi--blog-2026-04-reprojecting-dual-fisheye-videos-to-equirectang--6550b565
- shkspr.mobi--blog-2026-04-sneaky-spam-in-conversational-replies-to-blog-p--dde8f6c2
- shkspr.mobi--blog-2026-04-someone-at-browserstack-is-leaking-users-email---ca65e456
- shkspr.mobi--blog-2026-04-theatre-review-avenue-q--f4765991
- shkspr.mobi--blog-2026-04-theatre-review-hadestown--44eda2ab
- shkspr.mobi--blog-2026-04-why-is-it-so-hard-to-passively-stalk-my-friends--94b8e163
- shkspr.mobi--blog-2026-04-you-can-parse-an-env-file-as-an-ini-with-php-bu--c596e30b
- shkspr.mobi--blog-2026-05-nhs-goes-to-war-against-open-source--6dd55203
