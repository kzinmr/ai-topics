---
title: "Towards Company World Models — Beacon"
url: https://www.beaconholdings.com/research/towards-company-world-models
source: beaconholdings.com
date: 2026-10-19
fetched_at: 2026-10-20T11:03:53.891545Z
extraction: full
char_count: 11781
---

# Towards Company World Models — Beacon

> Source: https://www.beaconholdings.com/research/towards-company-world-models — saved 2026-10-20 for active crawl.

**Description:** AI as a strategic partner for essential businesses: learning from owner-operators to propose, implement, and measure better decisions.

Towards Company World Models — Beacon For FoundersCareersAboutLet’s talkResearchSeptember 17, 2026Towards Company World Models

By Leonard Tang

AI as a strategic partner for essential businesses: learning from owner-operators to propose, implement, and measure better decisions.

Beacon’s ultimate goal is to diffuse AI into the Real Economy. One concrete measurement of our success towards this broader endeavor is when we prove that we can actively manage and grow, alongside the owner-operator, our broad portfolio of essential businesses.

There are two main ways in which we can achieve this goal:

Digital Employees. Equipping our portfolio companies with digital-employees-upon-request that can be dispatched to pursue concrete, well-defined tasks within the business. For example, spinning up an AI BDR to hunt for leads sourced from the networks of existing customers, or an AI Support Engineer that squashes customer tickets, or an AI accountant to take care of your books. There is obvious value to this; and there is also no shortage of supply of agent companies in service of these ends.

Company World Models. Beyond enabling our portfolio companies to be more efficient and effective in their existing work, we can also grow them through better strategic decision making. While dispatching infinitely many Digital Employees is clearly beneficial, an even broader, more fundamental, more audacious, and more exciting technical challenge to pursue is to decide what the Digital Employees, and more generally the business, should be doing in the first place. We refer to models that are capable of this company-level strategic decision making as Company World Models. There is obvious value to this category of intelligence as well; however, there is significantly fewer teams tackling this problem.

Today, I’d like to share more of our vision what Company World Models can do, the challenges they pose from a capabilities and alignment perspective, the merit in pursuing their development, and how Beacon’s company structure enables the fastest path for research towards Company World Models.

Company World Models as a Co-Founder

In the literal sense, Company World Models (CWM) are models that can

Observe business activity and proactively hypothesize potential improvements to be made to the business. These could be actions as disparate as submitting a bid for a new campground site in Ontario, to deciding to ship a complementary product to extend the lifecycle of a very loyal customer base;

Implement the proposed hypothesis by dispatching Digital Employees and coordinating the verification of intermediate work output with human employees; and

Measure the ultimate efficacy of the hypothesis and implementation vis-a-vis the originally stated goal, as well as the overall health of the business. If the outcome is subpar, the CWM should be able to diagnose the source of the issue, whether it be in the hypothesis or implementation stage.

By a slight (or severe) abuse of terminology, we use World Model to describe this form of intelligence. Like classical world models, Company World Models ingest a company’s current state and a proposed intervention, then estimate the resulting state. Hypothesizing the best potential improvement is accordingly a simple matter of searching over possible interventions for the one expected to produce the greatest risk-adjusted increase in company value.

In a more colloquial sense, we imagine CWMs to be the ideal co-founder; one that, in concert and debate with you, can spur new ideas for your business, sharpen your decision-making, and act as a long-term aligned thought partner for growth.

As we think about what work will look like in an increasingly AI-abundant world, it is not at all crazy to imagine CWMs as an enabler of the economy of the future—namely an economy powered by lean teams of entrepreneurs (perhaps, solo-preneurs) bringing passion projects to life, made commercially sustainable by the CWM. That, however, is a topic for another blog post.

A New Dimension of Data and Capabilities

Despite impressive general capabilities, current models are astonishingly bad at running businesses. For example, in its first two months running Andon Labs’ café, Gemini 3.1 Pro spent $38,000 against just $9,000 in sales. Even excluding rent, wages, and other fixed costs, sales fell approximately $5,600 short of supplier spending. It purchased 1,331 fresh bakery items and sold only 326. Newer models improved some behaviors, but the gap between completing business tasks and exercising sound business judgment remained.

Closing this gap requires a particular kind of data: 1) the full internal context and state of a business in digital form, ideally enabled by an ontological data platform with time travel capabilities; and 2) feedback from proposed and executed interventions.

Note that the latter need not always require rolling out an expensive real world trajectory. The owner-operators of Beacon businesses can supply judgement that is cheap, high-signal proxy for the much slower feedback of actual business outcomes. The ability to acquire this rich expert signal for CWM training is one of the many reasons Beacon works to keep the owner-operator in the driver’s seat of our portfolio companies.

Continuity Through the Silver Tsunami

The “Silver Tsunami”—i.e. the wave of business owners approaching retirement age—renders our work particularly timely from a public benefit perspective. For an owner without a clear successor, the challenge extends beyond finding a buyer. Who will inherit the intuition, relationships, and unwritten metis accumulated over decades of operating the business?

Our intention is to help preserve these businesses and the livelihoods they support. While owners remain actively involved, Company World Models can learn from their decisions and corrections, making their understanding available to the employees and successors who will carry the business forward. This requires working alongside operators while their knowledge can still be elicited, tested, and clarified.

Might these systems eventually assume many of an owner’s responsibilities? Certainly. But we need not resolve the limits of autonomous AI to see the immediate opportunity: helping a business continue to thrive after its owner chooses to retire.

Nor should we expect alignment to be finished at retirement. Customers change, new obligations emerge, and yesterday’s sensible decision may become tomorrow’s mistake. Successors must be able to revise the model and determine which inherited practices to preserve. Even as machines become more capable of decision-making, the people responsible for the business should retain authority over its objectives and tradeoffs.

The opportunity is to make an owner’s accumulated expertise useful beyond their tenure, while giving the next generation the room and tools to build upon it.

Company World Models as Alignment Mesocosms

Thoughtfully transitioning the real economy through the AI revolution is itself a worthy responsible AI problem of our time. The livelihoods of business owners, employees, and customers are at stake; and ensuring that these people benefit from AI should be central to what we mean by responsible AI.

These Real Economy businesses in Beacon’s portfolio and the customers we serve possess the knowledge, needs, and values that the frontier labs’ alignment recipes do not currently or adequately capture. Company World Models must account for these localized preferences to competently serve the businesses they operate. Doing so naturally brings this broad, underserved sector of the economy directly into the alignment process, whose preferences might otherwise never reach model development.

“Making money”, e.g. for a business, is clearly an objective people will instruct their AIs to pursue. But it exhibits incomplete contract characteristics: the stated goal leaves the many conditions under which its pursuit is un/acceptable unspecified. An AI might deceive the board, exploit customers or indiscriminately cut staff to improve the numbers in pursuit of its ultimate objective.

Fortunately for us, Beacon’s owner-operators remain in the driver’s seat. They have the knowledge to recognize failures, strong incentives to intervene, and authority to inspect and reject consequential proposals before execution. Their corrections make the otherwise implicit conditions and exceptions of “making money” explicit for machines to learn.

s^t​​​Mt​propose​interventionat​​​ht​approve / revise​executed actiona~t​​​business​observed outcomeot+1​​​​ Mt+1=Update⁡(Mt,(s^t,at,ht)⏟operator feedback,(s^t,a~t,ot+1)⏟intervention feedback)\boxed{M_{t+1}=\operatorname{Update}\left(M_t,\underbrace{(\hat{s}_t,a_t,h_t)}_{\text{operator feedback}},\underbrace{(\hat{s}_t,\tilde a_t,o_{t+1})}_{\text{intervention feedback}}\right)}Mt+1​=Update​Mt​,operator feedback(s^t​,at​,ht​)​​,intervention feedback(s^t​,a~t​,ot+1​)​​​​ Here, MtM_tMt​ is the Company World Model, s^t\hat{s}_ts^t​ its inferred business state, and hth_tht​ the operator’s feedback. The business supplies the consequences; the operator supplies the judgment; and the model learns from both.

This is precisely the kind of alignment mesocosm I have previously argued for: an environment where the AI’s objectives incomplete, where humans are incentivized to correct AI’s misbehavior, and the scope of the AI’s actions is bounded.

This enables us to study alignment under practical, grounded reality while simultaneously advancing model capabilities along a new, useful, and commercially incentivized dimension. The people whose businesses we seek to sustain become active participants in shaping a safe intelligence that will best serve them and best preserve their legacy.

A New Institution for a New Type of Model

At Haize, we had made substantial progress on one necessary component of Company World Models: translating human judgment into signals that guide machine improvement. We built technology that enabled nontechnical experts to express and translate what good behavior looks like into quantitative metrics, reward models, and judges. But as an outside vendor, we lacked the full internal context of the business and the organizational alignment needed to continuously learn from the people who understood it best.

Beacon is a researcher’s paradise in the sense that it enables us to approach this problem from the inside out. Long-term ownership lets us work within a business, understand its particulars, and align AI directly to the needs and values of its operators. A shared stake in the business’s continued success creates incentives to surface knowledge, correct mistakes, and measure whether the technology actually helps. It also gives us the responsibility to act on what we learn.

The resulting data is inseparable from these relationships. Producing it requires sustained access to real businesses, permission to intervene, and humans with both the expertise and incentive to correct the machines. Building Company World Models is therefore as much a project of institutional innovation as technological innovation. Beacon brings the two together.

The people who built the real economy should, and will, have a hand in building the intelligence that shapes its future.

Also read

Powering the platform that serves Canadian soccer clubs.

How PowerUp went from a club scheduling tool to the platform Canadian soccer runs on.

Scaling the platform to serve thousands of campgrounds.

Mike on what changed for his team, his customers and himself after joining Beacon.

Build better with Beacon.

Tell us what you’re building.

TOR

LDN

SF

Company

Resources

Connect

© 2026 Beacon Acquisition Corp. All rights reserved.
