---
title: "Why is Meta destroying its engineering organization?"
url: "https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering"
fetched_at: 2026-07-03T07:00:58.288754+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Why is Meta destroying its engineering organization?

Source: https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering

Hi – this is Gergely with a free issue of the Pragmatic Engineer Newsletter. In every issue, I cover challenges at Big Tech and startups through the lens of senior engineers and engineering leaders. Subscribe to get deepdives like this in your inbox, weekly:
Many subscribers expense this newsletter to their learning and development budget. If you have such a budget, here’s
an email you could send to your manager
.
For two decades, Meta had a unique, high-performance engineering org; right up until around April of this year. For the first 20 years of the company’s existence, it had a “move-fast-and-break-things” culture, and in the early 2020s this shifted to a “move-fast-with-stable-infra” one. Engineers I know at the company were empowered to do good work, focus on impact, and to balance business interests with solid engineering.
But in the past few weeks, all that has changed, as if the leadership has been following detailed blueprints on how to demolish a proven, successful engineering culture in the most ruthlessly efficient way possible.
For the past few weeks, I’ve been
sharing
how bad things are inside the social media company for engineers in one of Silicon Valley’s most prestigious workplaces. In this article, we walk through what’s happened, and ask what’s going through the minds of leadership who are reducing software engineering there from
the profit center
that it was between 2004 until very recently, to the disdained cost center that it has become in just a few weeks.
We cover:
Meta’s pre-AI engineering culture
Investing in AI and pressing engineers to always use it
Core engineering folks feel treated like trash
Most embarrassing-ever outage
Internal mess
Self-inflicted wounds
Is “AI psychosis” just a Meta issue?
I’d split Meta’s engineering culture into two eras: “move fast and break things”, and then “move fast with stable infra.”
In the 2010s, Facebook’s unconventional engineering culture had grown somewhat legendary in the tech industry, as the company went against conventional best practices and succeeded massively.
In 2012, when Facebook hit the billion-users landmark, the company produced a small physical book about its culture which was placed on employees’ desks. Presented with retro propaganda design, it was dubbed the “little red book”, co-opting the name of a famous volume of the thoughts of Chairman Mao, (1964).
At around 70 pages long, Facebook’s version codified its engineering culture: speed, fearlessness, taking ownership, and thinking outside of the box.
Back then, mantras in Facebook’s little red book were also in print across campus, and included:
Move Fast and Break Things
Done is Better Than Perfect
Fail Harder
What Would You Do If You Weren’t Afraid?
Every Day Feels Like a Week
The Wright Brothers Did Not Have Pilot Licenses
The Foolish Wait
Fortune Favors the Bold
There was genuine focus on building good products. Also from the book:
More from Facebook’s Little Red Book
In 2022, I did what is one of the longest deepdives we’ve published on the topic of
Meta’s engineering culture
. By then, things had evolved, and much of any former recklessness was gone, replaced by the principle of moving fast, but with stable infra. Here’s how I described Meta’s engineering culture then:
“
The culture is incredibly engineering-centric: much more than most of Big Tech.
This might come from Mark Zuckerberg being an engineer himself, or because much of the innovation in the early days of Facebook came from engineers.
Focus on individual impact.
Impact has been the bread and butter of the focus at Facebook. This is very true since the early days, and the focus on generating impact remains.
One detail in common with most Big Tech firms is that both the engineering culture and general culture focus so much on individual impact. This results in some people focusing on short-term, measurable wins and assuming that teamwork and split wins between groups might be less rewarded.
The lack of rigid processes.
Facebook seems to have the least amount of processes or standardization across all of Big Tech. Don’t even try to compare it to
Amazon’s engineering culture
and the countless formal processes there. But even compared to companies like Google, Microsoft or Uber, Facebook’s processes are much looser. Most of this comes from the engineering-centric nature of the company and engineers disliking processes.
Surprisingly little emphasis on testing, documentation or code comments.
You’ll find shockingly little automated testing and documentation at Facebook, compared to the rest of Big Tech. Inline code comments are also very rare.
A founder-engineer driven company.
Facebook is one of the few Big Tech firms whose founder is an engineer, and still is the CEO. Netflix is the other one where founder and co-CEO Reed Hastings was also a software engineer before starting the company. Amazon was the other example of this until recently, but it’s not the case at Google or Apple. There are good examples of smaller companies like Cloudflare, but they’re all younger than Facebook.
Bootcamp
. A unique onboarding process, unlike what any other Big Tech firms offer. We cover this more in the
Bootcamp & onboarding section.
”
Also, Facebook, as a product, has one of the
most sophisticated auto rollout systems
in the industry. Instagram has a battle-tested infrastructure where it was almost trivial
to launch a new social network (Threads)
with 100 million users served in its first week.
Engineers whom I knew inside the company are capable, motivated, and product-minded, and their work was appreciated. CEO, Mark Zuckerberg, was influential: he personally coded the first version of Facebook, had stayed close to engineering, and valued software engineers very much. Engineers there felt they were working inside a profit center.
Meta has been the only company among the big five of Apple, Microsoft, Amazon, Google, and itself not to own a hardware platform or operating system. Apple has the iPhone, iPad and Macs, Google has Android, ChromeOS and Pixel phones, Microsoft has Windows, and Amazon has the Kindle.
Stepping back, it looks as though the Mark Zuckerberg of today has resolved not to miss a platform opportunity, after the company failed to build its own mobile OS or mobile phone during the 2010s.
This is one reason for investing so much in virtual reality (VR) with Oculus, and in augmented reality with the Meta Glasses. Facebook changed its name to Meta in 2021, back when it looked like VR – and the metaverse – could be massive. Billions was spent on ensuring Meta would be the market leader in this space. But once again, VR didn’t go mainstream; since the end of the pandemic, popular interest in the segment has died down considerably.
When it became clear that AI would become a mega-trend in 2022, Zuckerberg didn’t miss it: he assembled the internal FAIR group (Fundamental AI Research team) as well as a GenAI product organization and released a series of open-weight AI models:
Llama 1
: released in Feb 2023, three months after ChatGPT, built by FAIR
Llama 2
: in June 2023, built by the GenAI product organization (as well as all subsequent Llama models)
Llama 3
: in April 2024. This model was Meta’s most competitive LLM of all, and gained momentum in adoption across the industry
Llama 4
: in April 2025. This model was
deeply disappointing
In June that year, Meta acquired a 49% stake in Scale AI to reboot its AI efforts
for a whopping $14.8B, and brought in Scale AI’s CEO, Alexandr Wang to take over Meta’s AI strategy. The acquisition of Chinese startup Manus AI for $2B is currently in question after China
blocked
the deal from being completed.
Based on the investment made into Scale AI and Wang, it’s pretty clear that Meta – and Zuckerberg – is determined to build a state-of-the-art LLM that can be competitive with the latest versions of Claude and ChatGPT. But Meta has to start pretty much from scratch, and it’s up to Alexandr Wang to deliver.
Scale AI brings in a very specific kind of expertise to Meta, as one of the best in the industry in:
Training data and labeling:
Scale started, and is still best known, as a provider of high-quality labeled datasets for machine learning and AI training, including code, text, image, video, etc.
RLHF and fine-tuning:
A RLHF (reinforcement learning from human feedback) flow which Scale runs, where people give feedback for foundation models, as a “human in the loop” data engine that many leading AI labs use to create better LLMs.
Wang seems to have a very broad reign to do what he has been an expert in: creating training data, doing data labeling and RLHF. This is being pulled off with the labor of Meta’s engineering workforce, and by surveilling it.
Problem #1: Tracking keystrokes and mouse clicks, with no option to opt out.
In late April, Meta told engineers they were being enrolled into a system that tracks every keystroke and click, to produce training data for Meta’s new AI. There’s no way to opt out.
Needless to say, this is invasive and raises privacy questions: If you log into your personal bank account, does the tool track you? What about when you’re writing a personal email, or responding to a personal call? Meta held no consultation and there are no workarounds; just a top-down decision being pushed through.
This month, Reuters
reported
that people’s concerns there are finally being heard:
“Meta is dialing back elements of its plan to collect employee mouse movements, keystrokes and other actions for use as AI ​training data, it said in an internal memo on Tuesday, following weeks ​of angry pushback from staffers.
New controls will allow employees to pause ⁠the data collection for up to 30 minutes at a time and ​request exemptions from the initiative, according to the memo, authored by Stephane Kasriel, ​a vice president in Meta’s AI model-building Superintelligence Labs unit.”
From talking with current Meta engineers, I understand the logging system has not been rolled out in the UK due to data protection regulation.
Problem #2: 30-50% of engineers on core teams have been forcefully reassigned to data labeling
and RLHF, upsetting folks even more.
Also starting in late April, product engineering teams received a mandate from above, whereby 30-50% of engineers were to leave the team and join the ADO org (Agent Data Optimisation).
“Forceful” reassignment is very relevant here because of Meta’s traditional engineering culture.
Between its founding in 2004 and until last year, Meta gave engineers autonomy to choose where they work and what they work on. This was structural to how the company worked:
Engineers were not hired for a specific team (save for at the Staff+, levels, in some cases). They were hired to the company
During a 6-week bootcamp, new hires got familiar with Meta’s engineering culture and chose a team
Team matching meant talking with multiple teams who had headcount, doing small work with them, and finding a match
Internal transfers were easy, and often initiated by engineers
Team selection via bootcamp started to die down in around 2024, but any Meta engineer with at least two years’ tenure knows that previously they chose what to work on, and of course, could pick the most impactful thing to work on. And then, out of the blue, they’re assigned to a division where the impact is not clear, the work is menial, and doing it too long will surely hurt their career prospects.
“Data labeling” is more involved work, even though a bit repetitive.
There are labeling tasks, where you create a website, then look at it and decide if it looks good or not, and give this feedback: this is the “typical” data labeling. But this is the less frequent type of work. But then there are more involved AI training tasks, which looks like this:
Come up with a task that the AI should do
Then write the tests that confirm the result
Package all of this up into a Docker container, using
Harbor framework
Then read the code that the AI writes - often doing this based on feedback from several models, and give it feedback
This work is not easy to do — and you can see why you need good software engineers to do it! — but it gets repetitive really quickly. Most engineers who I talked to said that they found it hard to do this work motivated day-in, day-out. Then again, I did talk with an engineer inside the org who said that by varying the technologies they use, and challenging themselves, they found this work motivating and interesting! This engineer expects there to be more software engineering work coming up, after the phase of training passes.
There’s a lesson here: when life gives you lemons, you can either complain about it, or you can make lemonade, like this dev has done so.
This training work is secretive across the AI industry, and vendors are offering $100+ per hour for devs to do this type of work. There are rumors across the industry that OpenAI and Anthropic spends more on these training environments (to make the models great at coding) than the model training run itself!
Infrastructure and security teams were hit especially hard by reassignments.
I talked with several engineers in infra orgs, who had 30-50% of their teams drafted into the ADO org. And in some cases, it was the best engineers who left.
One engineer told me that the whole situation feels like the movie, The Hunger Games, when tributes are randomly selected and then removed from their environment, to something completely different. Except, at Meta, many more folks are being affected, with between three and five from a 10-person team going from building products used by hundreds of millions, to giving human feedback on AI-generated GitHub repos, over and over. So, a wider impact than in the Hunger Games, but with less drastic consequences.
Around 6,500 people are in the ADO org, more than at OpenAI and Anthropic.
Roughly four to five thousand of these are software engineers. Meta has around 25,000 engineers, meaning that one in every 5-6 software engineers may now find themselves doing data labeling full time.
As you can imagine, people are actively open to new positions, and nobody is updating their job title on LinkedIn and elsewhere to “data labeling at Meta.”
I’ve spoken with people in this role and they don’t like doing it, and feel upset about the top-down decision making. The silver lining is that they still have a job, have retained their salary, and were not part of layoffs. They still have time to leave Meta for something that pays comparably and is not a data labeling job.
Problem #3: a month-long waiting game, stoking fear across the company.
On 20 April, Reuters
reported
that Meta planned to lay off 10% of staff in a month’s time, and Meta confirmed the news, meaning there was a period of four weeks when everyone knew that they could be unemployed very soon.
Forced reassignments to data labeling started to happen. As I covered
at the time:
“Understandably, there are mixed feelings about this redeployment [to data labeling], with layoffs coming soon. On Wednesday, 20 May, Meta will announce layoffs. Perhaps those moved to do data labeling could actually be “safer” than colleagues on product teams. Of course, this is speculation, but it would be cruel if Meta cut devs reassigned to data labeling.”
Problem #4: Performance review is hyper-aggressive at Meta, so devs optimize all metrics.
The internal performance review process, PSC (Performance Summary Cycle), is very stringent, compared to Google and Apple, I’ve learned. Managers inside Meta “fight” over the pay packets of their employees, which involves “knocking down” the packet of engineers on other teams, so their direct reports are ranked higher. It’s common to weaponize metrics in this process – be that business impact, the number of code reviews, number of lines of code written, pre-AI (see
our Coding Machine archetype podcast
on this.)
Quotas are handed down to managers for the splits of the workforce to be put in each ‘bucket’, and the internal politics gets heated as managers try to get their reports into higher buckets.
After a few years, engineers at Meta learn that the best way to not get a bad PSC rating is to have all metrics – impact, code committed, and other numbers – higher than their peers’ are.
Learn more about
the internal politics of performance calibrations.
Problem #5: tokens are measured as part of perf, so devs aggressively optimize for it.
When layoffs were confirmed, engineers also learned that managers shall inspect token count during perf reviews. This raised worries that those with low token counts might be marked as underperformers and dismissed.
So, what is the natural reaction to this as an engineer at Meta? They started using AI tools for the sake of generating more tokens. This happened while Meta had an internal token leaderboard, encouraging tokenmaxxing. As I wrote
on 16 April:
“As per The Information, Meta employees
used
a total of 60.2 trillion AI tokens (!!) in 30 days. If this was charged at Anthropic’s API prices, it would cost $900M. Of course, Meta is likely purchasing tokens at a discount, but that could still come in at $100M+ – in large part from senseless “tokenmaxxing”.”
The biggest problem: people stop caring about real work and focus on performative work.
Let’s check the four ingredients that Meta’s leadership has decided to introduce to their workplace:
Tracking the keyboards and mouse clicks of all engineers, where legally possible
Reassign a good chunk of engineers to fulltime data labeling
Let staff know that 10% of them will be laid off
Have a culture where devs optimize for any and all metrics measured during PSC
Measure token usage as part of PSC
Shake this mix up well, and what do you get? Two things:
Everyone overuses AI to boost their personal stats.
An engineering workforce that pretends to work with as much AI, and as little human input, as possible. It’s a strange incentive where an outage caused by a failure to review code properly is not grounds for dismissal, but writing code by hand – instead of having an AI agent write it – could cost you your job
Every longer-tenured engineer is seeking a new job, or at least considering it.
Those who have been around at Meta longer term have seen enough. Let me describe this visually:
Why pretty much every engineer at Meta is looking for a way out, visualised
Fresh data seems to confirm that starting in May, a
lot
more engineers at Meta are looking for an “out.” Here’s how signups to leading Big Tech interview preparation service
interviewing.io
from Meta have changed over the last year and a half: we can see a massive jump in May vs the year before, as shared by founder and CEO
Aliner Lerner
with us:
Signups to interviewing.io’s interview prep service from Meta. Source:
interviewing.io
.
(We covered more data from interviewing.io and other interesting data sources in the  deepdive
State of the software engineering job market in 2026
)
To its credit, Meta has given out generous retention equity packages to several engineers considered key on the remaining teams. These packages make it harder to get matching compensation elsewhere. Still, I talked to one engineer who got an equity top-up, and said that this approach helped him decide to leave as soon as possible because he feels bitter about the lack of autonomy and having no control over things.
Meta’s core infra and security teams have suddenly found themselves severely understaffed. Most folks are pushing AI-generated code merged with AI-only reviews, without paying much attention to quality. After all, they’re dealing with the possibility of unemployment, while firefighting to operate a team without its best engineers whose headcount has been cut in half, all with the knowledge that AI usage could affect their own job security.
Two weeks ago, on 30 May, the most embarrassing outage in Meta’s history happened.
Here’s software engineer Siddharth Sundharam’s
summary
(emphasis mine):
“Yesterday, a slew of Instagram accounts, including some high profile ones like the Obama White House account, seemingly got hacked.
Look, I’m no spring chicken. I’ve spent almost a decade and a half identifying vulnerabilities and exploits at unicorn scale, but this is hands down the most unserious, “almost too stupid to be true” of them all.
The Takeover Flow:
Step 01: Faking the Location & Initiating Support. All the attacker needs to kick this off is your account username. Then, they hop on a VPN or proxy close to your city so Instagram’s security algorithms don’t suspect a thing. (You can quite easily get this from your public profile or “About” section or a hundred other ways.) Once it looks like the request is coming from the correct region, they tell the Meta support AI that the account is hacked and ask it to send the verification codes to an arbitrary email address they control.
Step 02: That’s It. Really, that’s it.
The first proper zero auth password reset I’ve seen in production.
There appears to be no additional check as to whether the email being given is actually something the user has used before. Once the AI sends the security code to the attacker’s email, the attacker passes it right back to complete the verification. The platform hands over a fresh password reset link, granting full ownership to the attacker.”
This is a security breach in which Meta left its extra-secure, reinforced front door unlocked, so that anyone could come in, and there was no alarm to notify anybody when it happened! It seemed Meta only noticed when users started reporting it on social media!
From talking with folks inside Meta, I’ve learned that AI was at the heart of this outage.
AI-generated, AI-reviewed code, and security teams being gutted were together the cause of this beyond-embarrassing incident. I poked around, and here’s what I gathered:
Instagram’s Trust and Safety Team lost around 50% of its staff to data labeling and layoffs. Some of the most senior folks were drafted onto AI training tasks.
AI-generated changes that saw no human input, just another AI code review, were very common during the last two months, across the codebase. The change that caused this outage looked like one of these
Normally, the Trust and Safety team would be on top of monitoring and alerting of security breaches,  but it is currently in full disarray due to rapid, internal disorganization.
Meta’s Chief Security Officer resigned the very next day.
The outage was resolved on Monday, 1 June, and an investigation started as part of the SEV process. On Tuesday, Meta’s Chief Information and Security Officer (CISO), Guy Rosen,
announced
his departure.
Coincidence? I suspect not: the CISO might have stepped down if they warned against the Security org being gutted but were then ignored, and so no longer trusts leadership. I also imagine the CISO didn’t have the idea to move a good half of Instagram’s security team over to data labeling.
As a note, the previously worst outage was all Meta services going down for seven hours
in 2021
, due to a DNS / BGP configuration issue. It was a bad outage, but Meta handled the follow up well, in my opinion. After that 2021 outage, Meta
shared a postmortem and apology
. It has not done so for the latest Instagram account takeover outage.
Wired
shares more details
on just how bad the situation is inside Meta, right now:
“Someone interrupted a livestreamed, employee-only presentation at Meta earlier this week with an expletive-filled outburst about “being the company’s bitch,” according to a recording heard by WIRED. The individual then asked the people leading the call to write to a specific Meta AI executive and “tell him that he’s a piece of shit.”
The incident, which took place on a call open to thousands of employees, reflects growing frustration inside the company’s Applied AI team, which was formed in March to support the work of AI researchers at Meta Superintelligence Labs. Three current employees tell WIRED there is widespread dissatisfaction with how Meta assembled the unit of about 6,500 engineers and product managers and the drudgework they allege they have been assigned to improve AI models.
“It’s literally the gulag,” one of the employees claims. “You have zero purpose in life all of a sudden, you barely interact with anyone, you just have these tasks every week.”
There’s more: Meta’s Chief Product Officer, Chris Cox, reportedly admitted to staff that Meta’s upper leadership (the folks above him, meaning the C-level at Meta) created the mess. Also from Wired:
During a meeting this week open to all employees at Instagram, Meta chief product officer Chris Cox addressed the “difficult” and “brutal” environment created by the “insanity of this company” in the past few months, according to a recording heard by WIRED. Cox applauded Instagram employees for launching features and serving around 2 billion users amid what he compared to “running a marathon in the middle of a hailstorm and then, like, your teammate gets replaced and then we’re recording you.”
“It’s like what the fuck,” he said, drawing laughs, before repeating himself. “It is like what the fuck.”
So, is there an ultimate source of the “insanity of this company”, as CPO Chris Cox put it? Engineers whom I talked to point the finger at two individuals: Mark Zuckerberg and Alexandr Wang. Zuckerberg has full control over the business, and has made the decisions to reallocate a good part of engineering folks to data labeling, to roll out tracking software, and to lay off 10% of staff when Meta achieved record revenue and profits. As the CEO, the buck clearly stops with him.
But it’s hard to unsee that – outside of layoffs – everything that Meta is doing is taken from the Scale AI playbook, and that surely comes from Wang:
Mandatory keystroke and mouse tracking to generate training data
Forced data labeling with 4,500+ engineers is to generate high-quality RLHF, surely for Meta’s under-construction coding LLM
Taking away the best engineers from the heart of the business is surely signed off by Mark Zuckerberg, believing that it is more important for Meta to train a coding AI than it is to operate its core business like Instagram, Facebook or Messenger reliably. Oh, did I mention that on Saturday (12 June) Facebook and Instagram
had another SEV0
, that is, a full-on outage?
Before all this happened, Meta
was on track
to overtake Google as the world’s #1 ads business by the end of the year. But for some reason, Mark Zuckerberg decided that building a coding LLM is more important.
Meta’s leadership is now trying to undo all the damage they have done.
Wired reports that Meta CTO, Andrew Bosworth,
admitted
to staff that the AI reorg was atrocious and committed to better communication in the future.
To me, it looks obvious that Zuckerberg doesn’t care how engineers feel about the massive changes, and that Bosworth likely ignored the chaos, all while engineers know for a fact that the next AI model matters more than they do to the business. Bosworth also said that employees will have access to AI coaching tools.
Very considerate, given the situation!
Based on all I’ve learned, Meta’s engineering culture is dead because leadership has made it clear that engineering at the company is
a cost center
.
Needless to say, I hope my assessment is way off, but I’ve seen nothing yet from Mark Zuckerberg and Alexandr Wang – the two executives creating this current mess – to suggest it is.
There may be a short time period where, if major changes like data labeling assignments and staff tracking are undone, then things at Meta could return to normal. The longer the current conditions persist, the more tenured engineers will surely leave.
It’s tragic to see a technical founder at Meta so focused on AI that he neglects the engineers who built the heart of his company. But is Meta a one-off exception?
Mitchell Hashimoto (creator of Ghostty, founder of HashiCorp)
says
he is seeing similar behavior by other founders (emphasis mine:)
“
I strongly believe there are entire companies right now under heavy “AI psychosis” and it’s impossible to have rational conversations about it with them.
I can’t name any specific people because they include personal friends I deeply respect, but I worry about how this plays out.
I lived through the great MTBF vs MTTR (mean-time-between-failure vs. mean-time-to-recovery) reckoning of infrastructure during the transition to cloud and cloud automation. All those arguments are rearing their ugly heads again but now it’s... the whole software development industry (maybe the whole world, really).
It’s frightening, because ‘psychosis folks’ operate under an almost absolute “MTTR is all you need” mentality: “it’s fine to ship bugs because the agents will fix them so quickly and at a scale humans can’t do!” We learned in infrastructure that MTTR is great but you can’t yeet resilient systems entirely.
The main issue is I don’t even know how to bring this up to people I know personally, because bringing this topic up leads to immediate dismissals like “no no, it has full test coverage”, or “bug reports are going down” or something, which just don’t paint the whole picture.
We already learned this lesson once in infrastructure: you can automate yourself into a very resilient catastrophe machine. Systems can appear healthy by local metrics while globally becoming incomprehensible. Bug reports can go down while latent risk explodes. Test coverage can rise while semantic understanding falls. Changes happen so fast that nobody notices the underlying architecture decaying.
I worry.”
The takeover outage at Instagram was exactly like this: the engineering team dropped the quality bar for AI-generated and AI-reviewed code, probably expecting that they could recover quickly from failures. And they did indeed recover… after the damage was done, high-profile Instagram accounts were hacked, and the system was compromised, all very publicly.
Mitchell highlights the specific concern of founders over-estimating the capabilities of AI, and consequently casting aside sensible safeguards when shipping code to production.
Most of us probably have something to learn from the disastrous events at Meta caused by hyper-focus on AI to the exclusion of people who are the lifeblood of that company.
In some good news, I’m hearing that in the UK, some of the 10% layoffs have suddenly been cancelled: at the end of the mandatory consultation period, several infra and security teams are learning that no engineers on their team will be let go, as originally expected.
Meta has a booming business, and is already a beneficiary of AI via increased ads revenue. Meanwhile, my Facebook feed is filled with fake, AI-generated videos, with hundreds of comments from bots and people who seemingly don’t realize it’s AI. It all seems like just more content for Meta to show ads next to.
And yet, despite business booming, Meta’s leadership has gone on a crusade to inflict the most damage possible on its engineering org. Apparently, they’re now learning that most of it was pointless.
If you’re in a leadership position and feeling the temptation to make drastic org changes for AI-related reasons, take a deep breath and see where it left Meta.
Meanwhile, If you’re an engineer at a company whose leadership is over-indexing on AI, consider forwarding this article as additional context.
If you’re hiring standout engineers who are extremely hands-on with AI, then it’s never been easier to get talent from Meta, than right now. Every engineer I know at the company is an extremely early adopter of AI, and knows how to build products and AI infra. These folks have soured on the company and its leadership. Meta’s loss of talent will be the gain of other startups and the rest of Big Tech; it’s one benefit of AI that’s probably a bit unexpected – not least of all by Meta!
It seems like the old mantra of “move fast and break things” has now extended to Meta’s engineering org itself, with the company’s rush to over-invest in AI, so it will avoid missing the latest mega-trend in the tech industry.
