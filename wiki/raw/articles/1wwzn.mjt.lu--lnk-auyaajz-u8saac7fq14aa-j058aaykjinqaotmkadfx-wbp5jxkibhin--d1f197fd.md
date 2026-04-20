---
title: "Figma's woes compound with Claude Design"
url: "https://1wwzn.mjt.lu/lnk/AUYAAJZ_u8sAAc7fQ14AA-_j058AAYKJInQAoTMkADFx-wBp5jXkibhiNlxtRNuEx5QBNOwcYAAtKWs/0/_I2trtHLn8IlV9aIAfDycQ/aHR0cHM6Ly9tYXJ0aW5hbGRlcnNvbi5jb20vcG9zdHMvZmlnbWFzLXdvZXMtY29tcG91bmQtd2l0aC1jbGF1ZGUtZGVzaWduLz91dG1fc291cmNlPW5ld3NsZXR0ZXImdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249bW9udGhseQ?b=3"
fetched_at: 2026-04-20T14:23:36.598624+00:00
source_date: 2026-04-20
tags: [newsletter, auto-ingested]
---

# Figma's woes compound with Claude Design

Source: https://1wwzn.mjt.lu/lnk/AUYAAJZ_u8sAAc7fQ14AA-_j058AAYKJInQAoTMkADFx-wBp5jXkibhiNlxtRNuEx5QBNOwcYAAtKWs/0/_I2trtHLn8IlV9aIAfDycQ/aHR0cHM6Ly9tYXJ0aW5hbGRlcnNvbi5jb20vcG9zdHMvZmlnbWFzLXdvZXMtY29tcG91bmQtd2l0aC1jbGF1ZGUtZGVzaWduLz91dG1fc291cmNlPW5ld3NsZXR0ZXImdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249bW9udGhseQ?b=3

I think Figma is increasingly becoming a go-to case study in the victims of the so-called "SaaSpocalypse". And Claude Design's recent launch last week just adds a whole new dimension of pain.
What happened to Figma?
Firstly, I should say that I love(d?) the Figma product. It's hard to understand now what a big deal Figma's initial product was when it launched in the mid 2010s.
The initial product ushered in a whole new category of SaaS - using the nascent WebGL and asm.js technologies to allow designers to design entirely in browser. It used to be the running joke that an app like Photoshop would
ever
run in the browser, but Figma proved it wrong.
It quickly overtook Sketch as the defacto design tool in the market. Firstly for UI/UX wireframing and prototyping, but increasingly for everything graphic design. As it was based in the browser, it was a revelation from the developer side to be able to
open
UI/UX files if you weren't on a Mac (Sketch is Mac only). It was also brilliant to be able to leave comments
on
the design and collaborate with the designer(s) to iterate on designs really quickly.
The collaborative features (without requiring anyone to download any software) quickly meant it got adoption outside of pure design roles - PMs and executives could
finally
collaborate in real time on the product they were building, without having to (at best) send back revisions and notes from badly screenshotted files that tended to be out of date by the time they were received.
I'll skip over the rest of the history, including a no doubt distracting takeover attempt by Adobe, that was later blocked on competition grounds. But (of course) LLMs happened and suddenly one of the most forward looking SaaS companies became very vulnerable to disruption itself.
Why did AI hit Figma so hard?
One completely unexpected development me and others noticed (and wrote up a few months ago at
How to make great looking reports with Claude Code
) was that LLMs started to get fairly "good" at design.
By good I do not mean as good as a talented designer, clearly it's nowhere near that - currently. But like many things, not
everything
requires a great designer. Even if you use a great design team to build out your core product experience (and many
do not
), there's an awful lot of design 'resource' required for auxiliary parts of the product, reports, proposals etc. It's not stuff that tends to get designers excited but can sap an awful lot of time going back and forth on a pitch deck.
And this is
exactly
why I think Figma is almost uniquely vulnerable. The way it managed to expand into organisations by getting uptake with non-designers becomes a liability if those non-designers can get an AI agent to
do the design
for them.
Looking at
Figma's S1
(which is somewhat out of date by now, but is the only reported breakdown I can find) corroborates this potential weakness. Only
33%
of Figma's userbase in Q1 2025 was designers, with developers making up 30% and other non-design roles making up 37%.
A lot of Figma's continued expansion
depended
on this part of their userbase. A lot of their recent product development has been to enable further expansion in organisations - "Dev Mode" for developers (which now looks incredibly quaint against LLMs), Slides (to compete against PowerPoint and other presentation tools) and Sites (a WebFlow-esque site builder) all are about expanding their TAM out of "pure" design.
The real surprise for me though was how basic their "flagship" AI design product Figma Make is. It really does feel like something that someone put together in an internal AI hackathon one weekend and it never progressed beyond that. Given how much Figma managed to push the envelope on web technology I found this surprising - perhaps they were caught off guard with how quickly LLMs' design prowess improved, or there were internal disagreements about the role AI should or will play in design. Regardless, it's an incredibly underwhelming product as it stands.
Then Claude Design comes along...
If things weren't bad enough, Anthropic themselves launched Claude Design which is a pretty direct competitor to Figma in many ways. While it's nowhere near functional and polished enough to replace Figma's core design product, I expect it
will
get significant traction outside of that. The ability for it to grab a design system from your existing assets in one click is very powerful - and allows you to then pull together prototypes, presentations or reports in
your
corporate design style that look and feel far better than anything a non-designer could do themselves.
And I thought it was extremely telling that unlike a lot of the other Anthropic product launches that have touched design - Figma did not provide a testimonial on it (understandably).
Canva did
, which I found extremely odd (they are in my eyes
even more
vulnerable to this product than Figma).
I think this really underlines two major weaknesses in many SaaS companies' AI strategies:
Firstly, it's very difficult to compete on AI against the
company
that is providing your AI inference. A quick check on Figma Make suggests that Figma (at least on my account) is indeed using Sonnet 4.5 for its inference - though I have seen it use Gemini in the past:
At this point Figma is effectively funding a competitor - and the more AI usage Figma has - the more money they send over to Anthropic for the tokens they use. Even worse, Sonnet 4.5 is
miles
behind what Anthropic uses on Claude Design (Opus 4.7, which has vastly improved vision capabilities), so the results a user gets on Make vs Claude Design are almost certainly going to underwhelm.
Also, unlike most/all SaaS costs, inference (especially with these frontier models) is
expensive
. As Cursor
found out,
the frontier labs can charge a
lot
less to end users than API customers like Figma. When you are potentially looking at a shrinking userbase, it's far from ideal to have very expensive variable costs that start pulling your profitability down.
Secondly, it really underlines to me how incredibly efficient headcount-wise companies can build products now. Figma has close to 2,000 employees - not all working on product engineering of course. I really doubt Anthropic even needed 10 to build Claude Design. Indeed the entirety of Anthropic is around 2,500 people.
It's also worth noting that a lot of the things that would traditionally lock a company like Figma in stop working as well in an agent-first world. Multiplayer matters less when your collaborator is an agent iterating on a prompt. Plugin ecosystems matter less when you can just ask for the functionality directly. Design system tooling is
the whole point
of Claude Design. Enterprise SSO - Claude already has that. Most of the moats that protect a mature SaaS company are moats against other SaaS companies, not against the thing providing their inference.
I might be wrong about how bad this gets for Figma specifically. Companies with strong brands, great distribution and genuinely talented teams can often adapt faster than outsiders expect, and I'd rather be long Figma than most of
its
competitors.
But the structural point is harder to wriggle out of. Figma has ~2,000 employees. Anthropic has ~2,500 total and I doubt Claude Design took more than a handful to build. Figma now needs to out-execute a competitor whose inference is ~free to them, whose marginal cost to ship is roughly zero, and who employs fewer people on the competing product than Figma has on a single pod. That's a very hard position to pivot out of.
This feels like a preview of where SaaS economics are heading. The companies that built big orgs on the assumption of steady seat expansion are going to find themselves competing with products built by tiny teams inside the frontier labs. Figma just happens to be the first big public name where one of their primary inference suppliers has started competing against them.
