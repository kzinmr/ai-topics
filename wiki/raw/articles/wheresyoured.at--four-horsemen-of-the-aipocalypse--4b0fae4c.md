---
title: "Four Horsemen of the AIpocalypse"
url: "https://www.wheresyoured.at/four-horsemen-of-the-aipocalypse/"
fetched_at: 2026-04-30T07:00:56.534741+00:00
source: "wheresyoured.at"
tags: [blog, raw]
---

# Four Horsemen of the AIpocalypse

Source: https://www.wheresyoured.at/four-horsemen-of-the-aipocalypse/

If you liked this piece, please subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of
NVIDIA
,
Anthropic and OpenAI’s finances
, and
the AI bubble writ large
. I recently put out the timely and important
Hater’s Guide To The SaaSpocalypse
, another on
How AI Isn't Too Big To Fail
, a deep (17,500 word)
Hater’s Guide To OpenAI
, and just last week put out the massive
Hater’s Guide To Private Credit
.
Subscribing to premium is both great value and makes it possible to write these large, deeply-researched free pieces every week.
Soundtrack —
Megadeth — Hangar 18 (Eb Tuning)
For the best part of four years I’ve been wrapped up in writing these massive, sprawling narratives about the AI bubble and the tech industry at large. I still intend to write them, but today I’m going to do what I do best — explaining all the odd shit that’s happening in the tech industry and explaining why it’s concerning to me.
And because I love a good bit, I’m tying these stories to
my pale horses of the AIpocalypse
— signs that things are beginning to unwind in the most annoying bubble in history.
Anyway, considering that the newsletter and the
podcast
are now my main form of income, I’m going to be experimenting with the formats across the free and premium to keep things interesting and varied.
Anthropic’s Products Are Constantly Breaking Because It Doesn’t Have Enough Capacity, And Opus 4.7 Is Both Worse and Burns More Tokens
Pale Horse: Any further price increases or service degradations from Anthropic and OpenAI are a sign that they’re running low on cash.
Let’s start with a fairly direct statement: Anthropic should stop taking on new customers until it works out its capacity issues.
So, generally any service —
Netflix, for example
— you use with any regularity has the “four nines” of availability, meaning that it’s up 99.99% of the time. Once a company grows beyond a certain scale, having four 9s is considered standard business practice…
…
unless you’re Anthropic!
As of writing this sentence,
Anthropic’s availability
for its Claude Chatbot has 98.79% uptime, its platform/console is at 99.14%, its API is at 99.09%, and Claude Code is at 99.25% for the last 90 days.
Let me put this into context. When you have 99.99% uptime, a service is only down for a minute (and 0.48 of a second) each week. If you’re hitting 98.79% uptime, as with the Claude chatbot, your downtime jumps to two hours, one minute, and 58 seconds.
Or, put another way, 98.79% uptime equates to nearly four-and-a-half days in a calendar year where the service is unavailable.
More-astonishingly, Claude for Government sits at 99.91%. Government services are generally expected to be four 9s
minimum,
or 5 (99.999%) for more important systems underlying things like emergency services.
This is a company that recently
raised $30 billion dollars
and gets talked about like somebody’s gifted child, yet Anthropic’s services seem to have constant uptime issues linked to a lack of capacity.
Per the Wall Street Journal
:
Since mid-February, outages for systems across Anthropic have become so common that some of its enterprise clients are switching to other AI model players.
David Hsu, founder and CEO of software development platform Retool, said he prefers to use Anthropic’s Opus 4.6 model to power his company’s AI agent tool because he believes it is the best model for enterprise. He recently changed to OpenAI’s model to power his company’s agent. “Anthropic has just been going down all the time,” he said.
The reliability of core services on the internet is often measured in nines. Four nines means 99.99% of uptime—a typical percentage that a software company commits to customers. As of April 8, Anthropic’s Claude API had a 98.95% uptime rate in the last 90 days.
Yet Anthropic’s problems go far further than simple downtime (
as I discussed last week
), leading to (deliberately or otherwise)
severe performance issues with Opus 4.6
:
One of the most detailed public complaints originated as a
GitHub issue filed by Stella Laurenzo
on April 2, 2026, whose LinkedIn profile identifies her as Senior Director in AMD’s AI group.
In that post, Laurenzo wrote that Claude Code had regressed to the point that it could not be trusted for complex engineering work, then backed that claim with a sprawling analysis of 6,852 Claude Code session files, 17,871 thinking blocks and 234,760 tool calls.
The complaint argued that, starting in February, Claude’s estimated reasoning depth fell sharply while signs of poorer performance rose alongside it, including more premature stopping, more “simplest fix” behavior, more reasoning loops, and a measurable shift from research-first behavior to edit-first behavior.
While Anthropic claims that it doesn’t degrade models to better serve demand
, that doesn’t really square with the many, many users complaining about the problem. Anthropic’s response has, for the most part, been to pretend like nothing is wrong, with a spokesperson waving off Carl Franzen of VentureBeat (
who has a great article on the situation here
) by pointing him to
two
different
Twitter posts, neither of which actually explain what’s going on.
Things only got worse with last week’s launch of Opus 4.7, which appears to have worse performance and burn more tokens.
Per Business Insider
:
One
Reddit post
titled, "Claude Opus 4.7 is a serious regression, not an upgrade," has 2,300 upvotes. An
X user
's suggestion that Opus 4.7 wasn't really an improvement over Opus 4.6 got 14,000 likes. In one informal but popular test of AI intelligence, Opus 4.7 appears to say that there were
two Ps
in "strawberry." Another user screenshot shows it saying that it didn't
cross reference
because it was "being lazy." Some
Redditors
found that Opus 4.7 was rewriting their résumés with new schools and last names.
Multiple
X users
posited that Opus 4.7 had simply gotten dumber.
Some X users have suggested the culprit is the AI model's reasoning times. Anthropic says the new "adaptive reasoning" function lets the model decide when to think for longer or shorter periods.
One user
wrote that they couldn't "get Opus 4.7 to think."
Another wrote
that it "nerfs performance."
"Not accurate," Anthropic's Boris Cherny, the creator of Claude Code,
responded
. "Adaptive thinking lets the model decide when to think, which performs better."
I think it’s deeply bizarre that a huge company allegedly worth hundreds of billions of dollars A) can’t seem to keep its services online with any level of consistency, B) appears to be making its products worse, and C) refuses to actually address or discuss the problem. Users have been complaining about Claude models getting “dumber” going back as
far
as
2024
,
each time faced with a tepid gaslighting from a company with
a CEO that loves to talk about his AI products wiping out half of white collar labor
.
Anthropic Has No Good Solutions To Its Capacity Issues And Shouldn’t Be Accepting New Customers — And More Capacity Will Only Lose It Money
Some might frame this as Anthropic having “insatiable demand for its products,” but what I see is a terrible business with awful infrastructure run in an unethical way.
It is blatantly, alarmingly obvious that Anthropic
cannot afford to provide a stable and reliable service to its customers,
and its plans to expand capacity appear to be
signing deals with Broadcom that will come online “starting in 2027,”
near-theoretical capacity with Hut8, which does not appear to have ever built an AI data center
, and
also with CoreWeave
, a company that is yet to build the full capacity for
its 2025 deals with OpenAI
and only
has around 850MW
of “active power capacity” — so around 653MW of actual compute capacity —
as of the end of 2025, up from 360MW of power at end of 2024
.
Remember: data centers take
forever
to build, and there’s only a limited amount of global capacity, most of which is taken up by Microsoft, Google, Amazon, Meta and OpenAI, with the first three of those already providing capacity to both Anthropic
and
OpenAI.
We’re likely hitting the absolute physical limits of available AI compute capacity, if we haven’t already done so, and even if other data centers are coming online, is the plan to just hand them over to OpenAI or Anthropic in perpetuity?
It’s also unclear what the goal of that additional capacity might be,
as I discussed last week
:
Yet it’s unclear whether “more capacity” means that things will be cheaper, or better, or just a way of Anthropic scaling an increasingly-shittier experience.
To explain, when an AI lab like Anthropic or OpenAI “hits capacity limits,” it doesn’t mean that they start turning away business or stop accepting subscribers, but that current (and new) subscribers will face randomized downtime and model issues, along with increasingly-punishing rate limits.
Neither company is facing a financial shortfall as a result of being unable to provide their services (rather, they’re facing financial shortfalls because they’re providing their services to customers), and the only ones paying that price because of these “capacity limits” are the customers.
What’s the goal, exactly? Providing a better experience to its current customers? Securing enough capacity to keep adding customers? Securing enough capacity to support larger models like Mythos? When, exactly, does Anthropic hit equilibrium, and what does that look like?
There’s also the issue of cost.
Anthropic is
currently
losing billions of dollars a year offering a service with amateurish availability and oscillating quality, and continues to accept new subscribers, meaning that capacity issues are
not
affecting its growth. As a result, adding more capacity simply
makes the product work better for a much higher cost.
Anthropic’s Growth Story Is A Sham Based on Subsidies and Sub-par Service
Anthropic’s growth story is a sham built
on selling subscriptions that let users burn anywhere from $8 to $13.50 for every dollar of subscription revenue
and providing a brittle, inconsistent service, made possible only through a near-infinite stream of venture capital money and infrastructure providers footing the bill for data center construction.
Put another way, Anthropic doesn’t have to play by the rules. Venture capital funding allows it to massively subsidize its services. The endless, breathless support from the media runs cover for the deterioration of its services. A lack of any true regulation of
tech
, let alone
AI
,
means that it can rugpull its customers with varying rate limits whenever it feels like
.
If Anthropic were forced to charge its
actual costs
— and no, I don’t believe its API is profitable
no matter how many people misread Dario Amodei’s interview
— its growth would quickly fall apart as customers faced the real costs of AI (which I’ll get to in a bit). If Anthropic was forced to provide a stable service, it would have to stop accepting new customers or massively increase its inference costs.
Anthropic is a
con
, and said con is only made possible through endless, specious hype. Everybody who blindly applauded everything this company did is a mark.
Claude Mythos Was Held Back Due To Capacity Constraints, Not Fears Around Capabilities
Congratulations to all the current winners of the “Fell For It Again Award.”
Per the Financial Times
:
Anthropic has said it will hold off on a wider release of the model until it is reassured that it is safe and cannot be abused by bad actors. The company also has a finite amount of computing power and has suffered outages in recent weeks.
Multiple people with knowledge of the matter suggested Anthropic was holding back from a wider release until it could reliably serve the model to customers.
So, yeah, anyone in the media who bought the line of shit from Dario Amodei that this was “too dangerous to release” is a mark. Cal Newport
has an excellent piece debunking the hype
, but my general feeling is that if Mythos was so powerful,
how did Claude Code’s source code leak
?
Did… Anthropic not bother to use its super-powerful Mythos model to check? Or did it not find anything? Either way, very embarrassing for all involved.
AI Compute Demand Is Being Inflated By Anthropic and OpenAI, With More Than 50% of AI Data Centers Under Construction Built For Two Companies, and Only 15.2GW of Capacity Under Construction Through The End of 2028
Pale Horse:
data center collapses, misc
.
As I’ve discussed in the past,
only 5GW of AI compute capacity is currently under construction worldwide
(based on research from
Sightline Climate
), with “under construction” meaning everything from a scaffolding yard with a fence (
as is the case with Nscale’s Loughton-based data center
) to a building nearing handoff to the client.
I reached out to Sightline to get some clarity, and they told me that of the 114GW of capacity due to come online by the end of 2028, only 15.2GW is under construction, including the 5GW due in 2026.
That’s…very bad.
It gets worse when you realize that the majority of that construction
is for two companies:
OpenAI’s Stargate data centers account for 4.6GW — with 1.2GW in Abilene, Texas; 1.4GW in Shackelford, Texas; 1GW in Dona Ana, New Mexico; and 1GW in Port Washington, Wisconsin.
It’s safe to assume that with big tech’s hundreds of billions of dollars of capex that its data centers will make up a large amount — as much as 6GW — with most of that likely going to Anthropic or OpenAI.
An indeterminately-large chunk could be Amazon’s Project Rainier in Indiana
, which will “eventually” (per CNBC) draw more than 2.2GW of electricity.
While Amazon says it’s “
fully operational
,” it’s
fucking lying,
as it also claims that it has “nearly half a million Trainium 2 chips,” with each chip being 500 watts, and 500,000 times 500 watts being around 250MW.
Other reports
said it would be up to 1 million Trainium2 chips by the end of 2025, but that would still only amount to 500MW.
Anthropic is apparently the primary tenant.
Anthropic also agreed to take 3.5GW of capacity of TPUs from Google Cloud
, with
the first 1GW coming online in 2027
, and also
agreed to take a gigawatt from Microsoft
made up of “Vera Rubin and Grace Blackwell systems,” meaning that these are likely data centers that are currently under construction.
Anthropic and Google also announced in Q4 2025 that Anthropic would use 1 million TPUs as part of a new deal with Google Cloud, and
that “well over” a gigawatt of capacity would come online in 2026
.
Microsoft is
also taking the 900MW extension to Stargate Abilene
, and considering that most of Microsoft’s GPU infrastructure already goes to OpenAI, I can only imagine that’s where it’s going.
Sidenote:
I’ll also add that Anthropic has agreed to spend $100 billion on Amazon Web Services over the next decade as part of
its $5 billion (with “up to $20 billion” more in the future, and no, there’s no more details than that) investment deal with Amazon
, with Anthropic apparently securing 5GW of capacity and bringing “nearly 1GW of Trainium2 and 3 capacity online by the end of the year,” which I do not believe, but whatever.These deals shouldn’t be legal.
So, to summarize, at least 4.6GW of the 15.2GW of data center capacity under construction is for OpenAI, with at least another 4GW of that reserved for Anthropic through partners like Microsoft, Google and Amazon. In truth, the number could be much higher.
This is a fundamentally insane situation. OpenAI and Anthropic both burn billions of dollars a year,
with The Information reporting that Anthropic expects to burn at least $11 billion
and
OpenAI $25 billion in 2026
. The only way that these companies can continue to exist is by raising endless venture capital funding or, assuming they make it to IPO, endless debt offerings or at-the-market stock sales.
NVIDIA Claims To Have $1 Trillion In Sales Visibility Through 2027, But Only $285 Billion GPUs Worth Of Data Centers Are Under Construction — NVIDIA Is Selling Years’ Worth of GPUs In Advance And Warehousing Them
It’s also
very
concerning that only such a small percentage of announced compute capacity is being built, especially when you run the numbers against NVIDIA’s actual sales.
Last year, Jerome Darling of TD Cowen estimated that it cost around $30 million per megawatt in critical IT (GPUs, servers, storage, and so on) and $12 million to $14 million per megawatt to build a data center, making critical IT around 68% (at the higher end of construction) of the total cost-per-megawatt.
Now, to be clear, those gigawatt and megawatt numbers for data centers refer to the
power
rather than
critical IT
, and if we take an average PUE (power usage efficiency, a measurement of how efficient a data center’s power is) of 1.35, we get 11.2GW of critical IT hardware, with the majority (I’d say 90%) being GPUs, bringing us down to around 10.1GW of GPUs.
If we then cut
that up
into GB200 or GB300 NVL72 racks with a power draw of around 140KW, that’s around 71,429 racks’ worth of hardware at an average of $4 million each, which gives us around $285.7 billion in revenue for NVIDIA.
NVIDIA claims it had a combined $500 billion in orders between 2025 and 2026
, and
$1 trillion of sales through 2027
, and it’s unclear where any of those orders are meant to go other than a warehouse in Taiwan.
At this point, I think it’s fair to ask
why anyone is buying more GPUs, as there’s nowhere to fucking put them.
Every beat-and-raise earnings from NVIDIA is now deeply suspicious.
AI Is Really Expensive, With Companies Spending As Much As 10% Of Headcount Cost On LLM Tokens, And May Reach 100% of Headcount Cost In The Next Few Quarters
New Pale Horse: Any and all signs that companies are facing the economic realities of AI, including any complaints around or adaptations to deal with the increasing costs of AI.
Last week, a report from Goldman Sachs revealed that (
and I quote
) “...companies are overrunning their initial budgets for inference by orders of magnitude (we heard one industry datapoint on inference costs in engineering now approaching about 10% of headcount cost, but could be on track to be on par with headcounts costs in the next several quarters based on current trajectories.”
To simplify, this means that some companies are spending as much as 10% of the cost of their employees on generative AI services, all without appearing to provide any stability, quality or efficiency gains, or (not that I want this) justification to lay people off.
The Information’s Laura Bratton also reported last week
that Uber had managed to blow through its entire AI budget for the year a few months into 2026:
Uber’s surging use of AI coding tools, particularly Anthropic’s Claude Code, has maxed out its full year AI budget just a few months into 2026, according to chief technology officer Praveen Neppalli Naga.
“I'm back to the drawing board because the budget I thought I would need is blown away already,” Neppalli Naga said in an interview.
…
He wouldn’t disclose exact figures of the company’s software budget or what it spends on AI coding tools. Uber’s research and development expenses, which typically reflect companies’ costs of developing new AI products, rose 9% to $3.4 billion in 2025 from the previous year, and the firm said in a recent securities filing it expects that cost will continue rising on an absolute dollar basis.
Uber’s CTO also added that about “...11% of real, live updates to the code in its backend systems are being written by AI agents primarily built with Claude Code, up from just a fraction of a percent three months ago.” Anyone who has ever used Uber’s app in the last year can see how well that’s going, especially if they’ve had to file any kind of support ticket.
Honestly, I find this all
completely fucking insane.
The whole sales pitch for generative AI is that it’s meant to be this magical, efficiency-driving panacea, yet whenever you ask somebody about it the answer is either “yeah, we’re writing all the code with it!” without any described benefits or “it costs so much fucking money, man.”
Let’s get practical about these economics, and use Spotify as an example because its CEO proudly said that its “top engineers”
are barely writing code anymore
, though to be clear, the Goldman Sachs example didn’t specifically name any one company.
For the sake of argument, let’s say that the company has 3000 engineers — one of its sites
claims it has 2700
, but I’ve seen reports as high as 3500. Let’s also assume,
based on the Spotify Blind
(an anonymous social media site for tech workers), that these engineers make a median salary of 192,000 a year.
In the event that Spotify spent 10% of its engineering headcount (around $576 million) on AI inference, it would be spending roughly $57.6 million, or
approximately 4.1% of its $1.393 billion in Research and Development costs from its FY2025 annual report
. Eager math-doers in the audience will note that 100% of headcount would be nearly half of the R&D budget, or around a quarter of its $2.2 billion in net income for the year.
Now, to be clear, these numbers likely already include
some
AI inference spend, but I’m just trying to illustrate the sheer scale of the cost.
While this is
great
for Anthropic (and to a lesser extent OpenAI), I don’t see how it works out for any of its customers. A flat 10% bump on the cost of software engineering is the
direct opposite
of what AI was meant to do, and in the event that costs continue to rise, I’m not sure how anybody justifies the expense much further.
And we’re going to find out fairly quickly, because the world of token subsidies is going away.
The Subprime AI Crisis Continues, With Microsoft Starting Token-Based Billing For GitHub Copilot Later This Year, And Anthropic Already Moving Enterprise Customers To API Rates
Pale Horse: Any further price increases or service degradations from AI startups, and yes, that’s what I’d call GitHub Copilot, in the sense that it loses hundreds of millions of dollars and makes fuck-all revenue.
As I reported yesterday
, internal documents have revealed that Microsoft plans to temporarily suspend individual account signups to its GitHub Copilot coding product, tighten rate limits across the board, remove Opus models from its $10-a-month Pro subscription, and transition from requests (single interactions with GitHub Copilot) towards token-based billing some time later this year, with Microsoft confirming some of these details (but not token-based billing)
in a blog post
.
This is a significant move, driven by (per my own reporting) Microsoft’s week-over-week costs of running GitHub Copilot nearly doubling since January.
An aside/explainer:
if you’re confused as to what “token-based billing” means, know that the vast majority of AI services currently
subsidize their subscriptions
, using another measure (such as “requests” or “rate limits”) to meter out how much a user can use the service. Nevertheless, these services still burn tokens at whatever rate that it costs to pay for them — for example, $5 per million input and $25 per million output for Opus 4.7, as I mentioned previously — meaning that the company almost always loses money unless a person doesn’t use the subscription very much.
Companies did this to grow their subscriber numbers, and I think they assumed things would get cheaper somehow. Great job, everyone!
The move to token-based billing will see GitHub users charged based on their usage of the platform, and how many tokens their prompts consume — and thus, how much compute they use. It’s unclear at this time when this will begin, but it significantly changes the value of the product.
I’ll also say that the fact that Microsoft has
stopped signing up new paid GitHub Copilot subscriptions entirely
is one of the most shocking moves in the history of software. I’ve literally never seen a company do this outside of products it intended to kill entirely, and that’s likely because — per my source — it intends to move paid customers over to token-based-billing, though it’s unclear what these tiers would look like, as the $10-a-month and $39-a-month subscriptions are mostly differentiated based on the amount of requests you can use.
What’s remarkable about this story is that Microsoft is one of the few players capable of bankrolling AI in perpetuity,
with over $20 billion a quarter in profits since the middle of 2023
.
Its decision to start cutting costs around AI suggests that said costs have become unbearable — The Information reported back in January that it was on pace
to spend $500 million a year with Anthropic alone
, and if that amount has
doubled,
it likely means that Microsoft is spending upwards of ten times its GitHub Copilot revenue, as I can report today that at the end of 2025, GitHub Copilot was at around $1.08 billion, with the majority of that revenue coming from its CoPilot Business and Enterprise subscriptions.
The Information also reported a few weeks ago
that GitHub had recently seen a surge of outages attributed to “spiking traffic as well as its effort to move its applications from its own servers to Microsoft’s Azure cloud”:
“Since January, every month, every week almost now has some new peak stat for the highest [usage] rate ever,” [GitHub COO Kyle] Daigle said. He attributed the growth to “both agents and humans,” and also noted that the rise of AI coding tools has led to a rise in humans without deep coding knowledge starting to use GitHub’s platform more.
“Agents” in this case could refer to just about anything — OpenAI’s Codex, Anthropic’s Claude Code, or even people plugging in the
wasteful, questionably-useful OpenClaw
to their GitHub Copilot account, and if
that’s
what happened, it’s very likely behind the move to Token-Based Billing and rate limits.
In any case, if Microsoft’s making this move, it means that CFO Amy Hood —
the woman behind last year’s pullback on data center construction
— has decided that the subsidy party is over. Though Microsoft is yet to formally announce the move to Token-Based Billing, I imagine it’ll be sometime this week that it rips off the bandage.
Two weeks ago,
Anthropic did the same with its enterprise customers
, shifting them to a flat $20-a-seat fee and otherwise charging the per-token rate for whatever models they wanted to use.
I’m making the call that by the end of 2026, a majority of AI services will move some or all of their customers to token-based billing as they reckon with the true costs of running AI models.
This Is The Era of AI Hysteria
I kept things simple today both to give myself a bit of a break and because these were stories I felt needed telling.
Nevertheless, I do have to remark on how
ridiculous
everything has become.
Everywhere you turn, somebody is talking about “agents” in a way that doesn’t remotely match with reality, like Aaron Levie’s epic screeds about how “
AI agents make it so every other company on the planet starts to create software for bringing automation to their workflows in a way that would be either infeasible technically or unaffordable economically
,” a statement that may as well be about fucking unicorns and manticores as far as its connections to reality.
I feel bad picking on Aaron, as he doesn’t seem like a bad guy. He is, however, increasingly-indicative of the hysterical brainrot of executive AI hysteria, where the only way to discuss the industry is in vaguely futuristic-sounding terms about “agents” and “inference” and “tokens as a commodity,” all with the intent of obfuscating the ugly, simple truth: that generative AI is deeply unprofitable, doesn’t seem to provide tangible productivity benefits, and appears to only lose both the
business
and the
customer
money.
Though my arguments might be
verbose,
they’re ultimately pretty simple: AI does not provide even an iota of the benefits — economic or otherwise — to justify its ruinous costs. Every new story that runs about cost-cutting or horrible burnrates increasingly validates my position, and for the most part, boosters respond by saying “
well LOOK at how BIG the REVENUES are
.”
It isn’t! AI revenues are dogshit. They’re awful. They’re pathetic. The entire industry — including OpenAI and Anthropic’s
theoretical
revenues of $13.1 billion and $4.5 billion —
hit around $65 billion last year
, and that includes the revenues from providing compute generated by neoclouds like CoreWeave and hyperscalers like Microsoft.
I’m also just gonna come out and say it: I think the AI startups are misleading their investors and the general public about their revenues.
My reporting from last year
had OpenAI’s revenues at somewhere in the region of $4.3 billion in the first three quarters of 2025, and
Anthropic CFO Krishna Rao said in an an affidavit that the company had made revenue “exceeding” (sigh) $5 billion through March 9, 2026
, which does not make sense when you add up all the annualized revenue figures reported about this company.
Cursor is also reportedly at $6 billion in annualized revenue
(or around $500 million a month) and “gross margin positive” — which I also doubt given that it had to raise over $3 billion last year and is apparently raising another $2 billion this year.
Even if said numbers were real, the majority of OpenAI, Cursor and Anthropic’s revenues come from subsidized software subscriptions. Things have gotten so dire that
even Deidre Bosa of CNBC agrees with me
that AI demand is inflated by token-maxxing and subsidized services.
Otherwise, everybody else is making single or double-digit millions of dollars and losing hundreds of millions of dollars to get there. And
per founder Scott Stevenson
, overstating annualized revenues is extremely common, with AI startups booking “three-year-long” enterprise deals with the first year discounted
and a twelve-month out
:
The reason many AI startups are crushing revenue records is because they are using a dishonest metric
The biggest funds in the world are supporting this and misleading journalists for PR coverage.
The setup: Company signs 3-year enterprise deals. Year 1 is discounted (say $1M), Year 2 steps up ($2M), Year 3 is full price ($3M).
They report $3M as “ARR” — even though they’re only collecting $1M right now.
The worst part: The customer has an opt-out option at 12 months! It’s not actually a 3 year contract.
While it’s hard to say how widespread this
potential act of fraud
might be,
Stevenson estimates that more than 50% of enterprise AI startups
are using “contracted ARR” to pump their values. One (honest) founder responded to Stevenson saying that his company has $350,000 in contracted ARR but only $42,000 of ARR, adding that “next year is gonna be awesome though,” which I don’t think will be the case for what appears to be a chatbot for finding investors.
This industry’s future is predicated entirely on the existence of infinite resources, and most AI companies are effectively front-ends for models owned by Anthropic and OpenAI, two other companies that rely on infinite resources to run their services and fund their infrastructure.
And at the top of the pile sits NVIDIA, the largest company on the stock market, which is selling
more GPUs than can be possibly installed, and very few people seem to notice or care.
I’m talking about hundreds of billions of dollars of GPUs sitting in warehouses that aren’t being installed,
with it taking six months to install a single quarter’s worth of GPU sales
. The assumption, based on every financial publication I’ve read, appears to be “it will keep selling GPUs forever, and it will all be so great.”
Where are you going to put them, Jensen? Where do the fucking GPUs go?
There isn’t enough capacity under construction! If, in fact, NVIDIA is actually selling as many GPUs as it says, it’s likely taking liberties with “
transfers of ownership
” where NVIDIA marks a product as “sold” to somebody that has yet to actually take it on.
Sidenote:
There’re already signs that GPUs are beginning to pile up.
You see, when a hyperscaler buys an AI server, what actually happens is an ODM — original design manufacturer — buys the GPUs from NVIDIA, builds the server, and then ships it to the data center, which, to be clear, is all above board and normal. These ODMs also book
the entire value of the NVIDIA GPU
as revenue, which is why revenues for companies like Foxconn, Wystron and Quanta Computing have all spiked during the AI bubble.
Oh, right, the signs.
Per Quanta Computing’s fourth quarter financial results
, inventory — as in stuff that’s sitting waiting to go somewhere — has spiked from $10.54 billion in Q3 2025 to $16.3 billion 2025, and nearly doubled year-over-year ($8.33 billion) as gross profit dropped from 7.9% in Q4 2024 to 7% Q4 2025. While this isn’t an across-the-board problem (Wistron’s inventories dropped quarter-over-quarter, for example), Taiwanese ODMs are going to be one of the first places to watch for inventory accumulation.
In any case, I keep coming back to the word “hysteria,” because it’s hard to find another word to describe this hype cycle. The way that the media, the markets, analysts, executives, and venture capitalists discuss AI is totally divorced from reality,
discussing “agents” in terms that don’t match with reality
and AI data centers in terms of “gigawatts” that are
entirely fucking theoretical
, all with a terrifying certainty that makes me wonder what it is I’m missing.
But every sign points to me being right, and if I’m right at the scale I think I’m right, I think we’re about to have a legitimacy crisis in investing and mainstream media, because regular people are keenly aware that something isn’t right, in many cases, it’s because they’re able to count.
