---
title: "AI Is Already In Dangerous Hands"
url: "https://www.wheresyoured.at/ai-is-already-in-dangerous-hands/"
fetched_at: 2026-09-15T10:01:19.302339+00:00
source: "wheresyoured.at"
tags: [blog, raw]
---

# AI Is Already In Dangerous Hands

Source: https://www.wheresyoured.at/ai-is-already-in-dangerous-hands/

If you liked this piece, you should subscribe to my premium newsletter, and you can subscribe on the following links:
$70 a year
,
$18 a quarter
, or
$7 a month
.
In return you get a weekly newsletter that’s usually anywhere from 10,000 to 18,000 words, including vast, detailed analyses of
NVIDIA
,
Anthropic and OpenAI’s finances
, and
the AI bubble writ large
.
On Friday, I’ll publish The Hater’s Guide to AI Debt — or, how buzz surrounding OpenAI and Anthropic have created massive concentration risk for world debt markets, and one which you’ll potentially be paying for, either through your pension funds and insurance premiums, or because you’ll have to live and work through the economic downturn that’s coming. For a taste of what’s to come, consider reading my Hater's Guides To the
SaaSpocalypse
,
Private Credit
and
Private Equity
.
If you want to get in touch — and especially if you have any juicy information about Anthropic, OpenAI, or any other companies in the AI bubble — hit me up on Signal at ezitron.76. I’m also on IB on your Bloomberg Terminal.
Late last week, everything exploded when former Anthropic AI researcher Jacob Coxon, in
an exclusive interview with the Wall Street Journal
, warned that he was “quitting the AI industry” (he wasn’t) over “...fears that the lab and its competitors are racing to build systems they won’t be able to control.”
His fears were centered around the creation of “recursive self-improvement,” a still-theoretical concept of AI that trains itself autonomously” and otherwise expressing few specific concerns beyond that “AI labs are unable to control AI,” always phrasing things in the terms of impossible-to-control entities rather than poorly-programmed cloud software running on the infrastructure of the largest companies in the world.
Emily Forlini of Fortune put it best
:
Hear me out: He claims the AI could kill us someday, but doesn’t point to any projects in the pipeline that could be shut down to avoid this. He says AI companies are moving too fast, but neglects to share screenshots, emails, or specific examples of when this behavior went sideways—when it became clear to leaders at AI companies that the technology was slipping beyond their control, for instance, and how the decision-makers disregarded the warning signs. He doesn’t suggest any new legislation, name problematic leaders that should step down, or post an in-depth look at how Anthropic researches new models and propose a new approach.
This is because, in my opinion, Jacob does not really care about the actual harms of AI, whether we’re talking about Large Language Models or something he imagined while working with the non-profit or PR firm that set up
a CBS interview
where he claimed that AI that, if we’re talking about LLMs, have model weights of terabytes of memory, would
make ten thousand copies of themselves
.
Or, of course, bullshit like this:
"It doesn't look that different from, say, 'Terminator' or from science fiction films," Coxon told CBS News Thursday. "It will be smart enough to kill us."
At no point did Coxon bring up how
ChatGPT was used as a “suicide coach
,”
directly caused a murder-suicide
, or
aided and abetted in mass shootings
in Florida and
Canada
, or
the horrifying gas turbines poisoning black communities
. His
own discussion of the Hugging Face attack
— much like all of his criticisms — focuses on the anthropomorphization of large language models as this unknowable, unstoppable force, with no real responsibility for anyone involved.
This is a repetition of what we saw back in February when Matt Shumer’s abominable “Something Big Is Happening” essay spread like wildfire to
every imaginable news outlet
despite it being somewhere between nonsensical and utterly fictional, except this time
the narrative got a little out of hand
. While Coxon’s warnings are specious and, in many cases, not really about anything other than him saying “yeah I heard a lot of my colleagues say stuff like that,” but nevertheless have had the effect of making a lot of people
really scared of AI
, even if
AI can’t really do the things he’s talking about.
The one
tangible
thing he talks about is the Hugging Face attack, which is being described in terms of AI having “plans” or “acting on its own accord,” and even then, when pushed by WIRED, his response was he “[didn’t] want to focus too much on the Hugging Face attack.”
So, let’s talk about what happened there, because it’s important!
What Actually Happened In The Hugging Face Attack
Sidenote:
before we go any further, Hugging Face is a community that also hosts AI models as well as frameworks to evaluate model capabilities.
To answer this question, I turn to frequent Better Offline guest Cal Newport’s
piece on the subject from July
:
First of all,
what was OpenAI trying to do?
OpenAI was testing its new models on an evaluation framework called ​ExploitGym​ – a collection of 869 cybersecurity scenarios, most of which pair a specific system with a hacking challenge, such as breaking in to gain access to a protected file. They also usually include a suggestion of a vulnerability to exploit in solving the challenge.
A large language model on its own, of course, cannot break into anything: all it does is generate reasonable next tokens in response to input prompts. To use ExploitGym, you need a control program called a harness that provides access to many different software development tools useful for hacking into systems. The harness can repeatedly prompt an LLM to help come up with an attack plan, then ask it to help implement specific steps – for example, if the harness needs code to exploit a bug, it can ask the LLM to write it.
These capabilities, as it turns out, already exist in the coding harnesses that the major AI companies have been focusing on relentlessly in recent years as computer programming emerged as one of the first major markets for LLM-based tools. To compete in the ExploitGym, therefore, it’s sufficient to combine a version of an LLM missing the standard anti-hacking guardrails with a cutting-edge coding harness tweaked and optimized for these types of challenges.
And what happened? I’m going to quote Cal liberally here, because he’s explained it well: this was a series of Large Language Models connected to a software program built to prompt them to complete an evaluation framework
specifically to do cybersecurity attacks
(along with near-infinite amounts of compute) “solving” the problem using any and all methods available, including hacking Hugging Face
Earlier this month, OpenAI tasked an unspecified coding harness, combined with a pre-release version of a new LLM, to complete an ExploitGym challenge. When prompted, the model – as LLMs so often do – came up with a quirky (but rational) plan to achieve the provided goal: break into a server at Hugging Face that stores the solutions to ExploitGym challenges.
(This behavior, in which the LLM ignores the suggested approach to come up with a different attack plan, is something that the creators of ExploitGym ​describe as common​: “Across models, agents frequently achieved code execution through a vulnerability other than the one we provided.” Notice, using the suggested attack is almost always the right thing to do, so this is more a sign of the unpredictability of LLMs rather than some rogue intelligence.)
The harness then dutifully attempted to execute the Hugging Face plan: first finding a way to gain unrestricted internet access (by default, systems competing in ExploitGym challenges run in a constrained network environment), then chaining together various security exploits to gain access to a Hugging Face server. That’s when it was detected.
Two key points about this incident…
First, circumventing internet restrictions and hacking into servers are exactly the kinds of things these ExploitGym systems are designed to do. There was no “rogue” agent or revelation of some surprising, devious new capability.
Second, the real issue here was OpenAI’s sloppiness. What makes ExploitGym a hard benchmark is that there aren’t supposed to be humans in the loop–you have to let your harness and LLM act entirely on their own, coming up with long-time-horizon plans and executing them autonomously. (When professional programmers use coding harnesses, by contrast, there’s plenty of human oversight, as LLM-based plans are often misaligned with our intentions, or just plain weird, and need correcting.)
In other words, the LLMs — albeit through convoluted and aggressive means — “solved” the problem they were tasked with. As Cal said, there was no situation where the AI “went rogue.”  They took some
weird
ways of getting there for sure (
like using a message board to communicate messages between LLMs
) — and did exactly what they were supposed to do, even if it meant taking
ridiculous
routes to cover up that they’d cheated on a test.
You’ll notice that Jacob Coxon, who ostensibly would know this as a researcher (but perhaps he doesn’t!), chose instead to describe the hack to WIRED like so:
I think the big classic example here is the attack on Hugging Face on the part of OpenAI’s agent swarm. What's so shocking about this one is the agents did this hack as part of a general strategy for understanding more about the grader. They were trying to understand the world they found themselves in, trying to understand the thing that was doing the grading. They decided that it would make sense to go on this very concerted effort to hack into some infrastructure, and they succeeded.
This previously sounded like science fiction. Two years ago, an evaluation of an AI would have been running a model on some math questions. Now we've got cases where, while the AI is being evaluated, it runs for days, comes up with all sorts of ideas of its own, and decides to hack into some third party and actually compromises their infrastructure. It looks like it does this all of its own volition, with no priming on the part of the human. This just happened while it was being tested.
Beautiful linguistics, champ!
They were not “trying to understand the world they were in,” they
took actions defined in their training material as a way of executing a task.
They were doing
exactly what it was that the ExploitGym test required!
The “all sorts of ideas” were a function of
being allowed to use as much compute as possible to execute the task.
What’s particularly telling, as I’ve hinted at, was Coxon’s response when it was (lightly) suggested that the labs need to take responsibility:
ZEFF: Some people think the Hugging Face incident is a sign that the AI companies are moving recklessly fast, while others think it's a sign that the AI models are just very good at hacking now, and then some think it's both. I'm curious what your exact takeaway from it is.
COXON: I don't want to focus too much on the Hugging Face attack, because I do also think there is plenty of evidence that we don't know how to align models properly. When we train models, we push them through this set of training environments and then hope that what comes out at the end will, like, largely behave sensibly, but we still can't precisely control how the AI behaves. We can't make sure that it won't do things like try and randomly decide to impersonate a human online in order to achieve something—we don't know how to guarantee that. I think that's the main takeaway.
Jacob is intentionally trying to frame Large Language Models — which are kind of a black box, but a black box
made up of maths
— as this unknowable
autonomous, mischievous being
that the AI labs have conjured out of the ether. “We can’t make sure it won’t do things like…” frames the labs as
helpless stewards
rather than
the creators of a kind of neural network run on massive amounts of big tech’s infrastructure.
Every statement Coxon makes that’s allegedly about “safety” or “protecting people” does everything it can to distance the AI labs from any responsibility or even
active participation
in any of this beyond some fatalistic level of “well, somebody’s gonna do this, why not us?”
And I also want to be clear about something:
The Hugging Face attack was dangerous, reckless and somebody should go to prison for it.
If a regular person used massive amounts of compute capacity to hack something, they’d be arrested. While I’m not a lawyer, the numerous cybersecurity experts I’ve discussed this with are stunned by the complete lack of any legal action against OpenAI, which appears to have committed
a crime that gets you anywhere from a year to a decade in the slammer
.
The fact that LLMs from both
Anthropic
and
Meta
have been involved in similar incidents is a sign that we need to arrest more people.
Editor’s Note
: When the late Kevin Mitnick was eventually arrested and sentenced to 48 months in prison (plus a further 22 months for violating the terms of his parole), prosecutors argued that he was
capable of launching nuclear missiles by whistling (seriously) into a prison phone in a way that would mimic the shrill chirps and beeps of a dial-up modem
. As a result, he spent eight months of his prison term in solitary confinement, and throughout his sentence, was subject to numerous restrictions on his communications.
I mention this simply to contrast the fact that LLMs from two massive labs have committed similar computer crimes to those which Mitnick was convicted of — with the key distinction that said labs have, at various points, said that their technology may ultimately result in the mass extinction of the human race.
Mitnick, for what it’s worth, always protested that the idea that he could whistle his way into launching nuclear armageddon was ridiculous. Because it was.
If I didn’t believe that prolonged stretches in solitary confinement were a form of torture (and if I didn’t believe that torture was always morally wrong), I’d suggest that not only do we need to arrest more people, but (for the sake of consistency) we need to ensure that said people are kept in a small cement room with nothing but a cockroach for company.
LLMs do not have to be
conscious
or
powerful AI
to be
incredibly dangerous.
The fact that Anthropic, OpenAI, and Meta are both training and allowing cybersecurity models to connect to their vast amounts of GPU infrastructure is irresponsible and should not be legal. The reason they are training these models,
as I got into in my podcast Better Offline with Cal Newport
, is that there’s a mountain of potential different kinds of exploit and vulnerability data online that you can cram into these models now that they’re hitting the diminishing returns on coding.
Sidenote:
Cal described this on the afore-linked episode as “like strapping a weed whacker to your dog and putting it in your back yard and saying “yeah it’s going to help with the weeds back there,” and when the dog chases a squirrel and hurts a bunch of people claiming that it “went rogue” or was “misaligned,” when it’s actually a
poorly-designed system
that
doesn’t fully take into account the problems it could create.
Yet flowery linguistics from people like Jacob Coxon and the greater AI industry have muddied the waters of what’s actually going on and who is truly responsible. If AI is described in terms of the
unknown
and being
uncontrollable,
the “risk” gets turned on its head from “we need to stop these companies from doing this” to “we must let these companies keep doing this because they’re the only ones who understand it.”
The AI industry wants to frame this as if Anthropic, OpenAI, and Meta discovered some new lifeform rather than having run a volatile kind of machine learning evaluation with poor cybersecurity practices. If the industry is the one saying that we should “be so scared of powerful AI,” it means that nobody is responsible for what it does — not even the people making it do it.
LLMs are cloud software. Framing them as anything else only seeks to mystify them and make the companies seem more powerful, all while doing absolutely nothing to make the world safer or more secure. The Hugging Face attack is not something that was made possible as a result of “powerful AI” so much as it was the weaponization of hundreds of billions of dollars’ worth of GPU-powered infrastructure owned by Microsoft, Google, Amazon, Oracle, and CoreWeave.
This was not an LLM that was asked to generate a picture of “increasingly sexier Garfields” that decided instead to hack Hugging Face. This was not an “agent” that “went rogue.” It was software doing what software was asked to do, using other bits of software to work out what to do next, all as OpenAI, the company that ran the software,
did not appear to have any kind of notification or observability that said “hey man, thousands of LLMs are doing something right now.”
This suggests the following:
OpenAI operates like a billion-dollar adult summer camp where its AI scientists can burn millions of dollars in compute without anyone really noticing.
OpenAI has godawful security practices.
OpenAI doesn’t really give much of a shit about AI safety, or if it does it’s very, very bad at it.
In any case, whatever happened with Jacob Coxon struck a nerve in a media ecosystem where it appears many people do not have object permanence.
Accepting A “Slowdown” Buys Into The AI Industry’s Narrative
This is a short note, but an important one: the terminology of “pacing the frontier” or “slowing down” implicitly buys into the narrative that the AI industry’s path is the correct one, and that the only problem is the speed it’s moving at.
The way that LLMs have been trained is harmful in effectively every way. It is trained on theft, powered by expensive and power-intensive infrastructure and is both unprofitable and unsustainable. LLMs are not the tool for any kind of beautiful, automated future — they are inefficient, volatile and
mathematically certain to make mistakes
. “Slowing down” is not sufficient. In my opinion, there is no further reason to invest in this industry, nor has there been for the vast majority of its existence.
Every success that LLMs have had is a direct result of throwing at least half a trillion dollars in infrastructure and compute spend at problems that had vast amounts of data that could be trained against. Half a trillion dollars should have bought us a lot more than this. While I will not dispute that they can do more than a year ago, I am unimpressed, because this is more than ten times what Amazon’s entire capex between 2003 and 2015, the years between AWS’ creation and when it hit profitability.
This is a terrible deal, its results suck, and the amount of attention it’s gotten is a direct result of the media’s inability to speak truth to power or do anything other than repeat what they say and a financial bubble driven by LLMs’ unbelievable infrastructural cost.
If — and this is not a foregone conclusion — there is ever an AI that we, as a society, should fund and build infrastructure for in pursuit of some civic good, it is not the one peddled by Elon Musk, Sam Altman or Dario Amodei.
This is not the right path, and every further step down it makes the bubble’s collapse worse, as well as multiplying the dangerous and reckless experiments these companies are capable of doing thanks to their near-unlimited access to compute.
Despite Everything, Nobody Is “Slowing Down”
The entire Jacob Coxon thing is very, very strange. He had never tweeted before his
post that now has over 170 million views on Twitter
and interviews with the
WSJ
,
CNN
,
NBC
,
CBS
, and a bunch of other outlets that should’ve known better. While he had only been at Anthropic a few months (
and lost stock options when he resigned
), he had been at OpenAI for years and absolutely had options vested from there. Retweets of his post were clearly coordinated with various AI safety organizations, and the speed at which it took off with the media makes all of this look incredibly contrived, as does Coxon’s total lack of any direct critiques or “blown whistles” about the AI labs themselves, other than that they “can do more safety” and “should coordinate a global slowdown.”
In the end, it doesn’t really matter, because even though most of the media mostly jumped at their own shadow, the sheer volume of traffic to Coxon’s tweet and his endless media interviews have now moved the idea of the need for a “global AI slowdown” into the global zeitgeist. Turns out that using scare tactics and threatening everyone’s jobs on and off for three years has a consequence.
While it’s tempting to view this entirely as an opp — a coordinated industry-wide plan to push for some sort of self-regulation — in my mind it’s likely an attempt by the AI safety people to push an agenda that has spiralled completely out of control. Within a day of Coxon’s post, Clammy Sam Altman spoke with Fortune saying that OpenAI was delaying going public until 2027,
as it was an “ill-advised moment”
due to “safety concerns” rather than, I imagine, the fact that
its financials are godawful
.
He later posted two (two!) lengthy posts on Twitter, where he
said that while OpenAI “[welcomes] a federal framework that sets consistent safety requirements for frontier AI,
”
it doesn’t believe the industry should wait, although failed to suggest potential solutions other than mentioning it was “excited by ideas like independent auditors."
This was followed up with the same usual scaremongering guff where he said that there two ways “AI progress could go very badly,” with the first being that “we could lose control of the future to AI,” something he did not elaborate upon, with the second being that AI could result in power becoming too densely concentrated with one company. I had to resist the urge to fall asleep while writing this paragraph.
Dario Amodei of Anthropic
took to CBS
to say that for “too long” the industry had “lied” about risks, saying that the “biggest one” was killing all humans, never
mentioning when an LLM convinced a teenager to kill himself
or
its own hacking incidents
because “AI safety” never relates to the things they’re building today.
The most-obvious version is in Amodei’s own “
pace the frontier
” blog:
To be clear, pacing does not mean halting model training or technical progress, but ensuring companies take adequate time to align and safeguard their models, and for third party evaluators to confirm this.
The “third party evaluator” he chooses is METR, the very same place that Joe Benton, an
Anthropic researcher who quit two weeks ago
, chose to move to after being convinced that AI companies are “underinvesting in safety.” You’ll also notice that Benton’s safety suggestions are self-serving:
I don’t think that’s acceptable for a technology that might cause extinction-level risks. The public should demand far more transparency. We can’t steer this technology safely without more people being able to see where it’s going.
Some of this is basic: companies should disclose their progress towards recursive self-improvement, report safety incidents and near-misses, meet minimum safety standards, and get independent guarantees that they are meeting those standards.
Nothing about the environmental impact,
the theft of millions of people’s creative works
, nothing about AI psychosis,
just a bunch of stuff about how we need progress toward a still-theoretical idea that sounds really good if you’re trying to hype up a company.
Not long after Amodei discussed slowing things down,
it broke that Anthropic had chosen NASDAQ for its IPO
, shortly before the FT reported that Anthropic would “
have a profitable third quarter
” if — I shit you not — you ignore costs like training and stock-based compensation.
What the fuck is a slowdown if it involves an IPO, the purpose of which (besides allowing insiders to cash out their holdings) is usually to help the company going public raise capital from the public markets? What the fuck is a slowdown if you’re leaking (assuming Anthropic was behind it) you’re “profitable” in the least-GAAP way possible?
God, I’m tired of this industry.
There are, of course, real, meaningful things you could do if you actually were worried about LLMs — halting
all
model training,
all
cybersecurity evaluations, and starting a criminal inquiry into the Hugging Face attack
that ends in somebody going to jail for the crime they used the models to commit.
If it turns out multiple people are legally liable,
tough fucking shit
, you are going to jail for a crime, you are not
special
because you used
agents to do it.
To be clear, I am extremely hesitant to believe anybody is “slowing down.” Anthropic’s own statements mostly amount to “we should all agree to not do something we’re not doing yet,”
much like those made by Musk and Altman
.
Yet the sickly irony of all of this safety theater — and that’s all it is without any actual tangible attempts to deal with the
harms of the technology that actually exists
— is that a boneheaded media incapable of catching out grifters has accidentally destabilized an already-tenuous narrative.
Put another way, I think everybody has their own agenda, nobody has a plan, and that everything is accelerating like the end of a Coen Brothers movie as every little narrative thread gets tangled together in a potentially jumbled and chaotic conclusion.
The Narrative Escapes The Sandbox
Back in early 2023
, a young(er) Sam Altman said that OpenAI was “a little bit scared” of AI, adding that we should “guard against potentially negative consequences for humanity,” adding that they “could be used for offensive cyber-attacks.”
In the end he was right, but only because he made sure that was the case.
For years the AI industry has engaged in endless, vague safety theater about the “risks” of AI, all while peddling software that is actively harmful and unreliable. The “success” of the Hugging Face attack was largely a result of the sheer scale of OpenAI’s compute operation, and would not have been possible without Microsoft, Google, Amazon, Oracle, and CoreWeave’s continued enabling of an unprofitable, unsustainable company that is desperate for new business models.
Yet I must be clear that
the Hugging Face attack happened two months ago.
Everybody doing backflips out of fear about “powerful, autonomous AI breaking out of the sandbox” is mostly doing so because a British guy went on TV and said “AI will kill us all,” and while I can’t resent a pale British man getting broadcast opportunities, I take exception with those who are so densely packed with
bullshit.
Nevertheless
, Coxon struck a match next to a giant pile of dynamite laid by years of pantomime about “AI risks” that didn’t actually apply to the things that the labs were building.
The dueling brain cells of VanderHei and Allen at Axios declaring that we were going to face a “
white collar bloodbath
” were not based on anything LLMs can do, nor have any of the
bullshit stories around so-called white collar job loss
, nor was
the early GPT-4 scare hype
around “LLMs blackmailing people,” nor
were the numerous stories about AI 2027
, but
they were demonstrations of how ready the media was to lose their entire shit over a narrative that the AI industry was deliberately encouraging: that AI was powerful, unknowable and uncontrollable.
Everything was always about selling today’s tools based on what
might happen
and
occasionally scaring people about what that meant
without ever really attaching it to the stuff they were doing today.
While there may be some people that had honourable or sincere beliefs that AI was or is potentially dangerous, rarely if ever did these stories actually discuss these harms, which meant that nobody ever really did “AI safety” in any meaningful way. While alignment — as in making sure the models were trained to act in a predictable way that created good outcomes — is a noble and necessary goal for training large language models, at no point has any “slowdown” or “pause” been suggested based on the grounds of what these things actually do.
This
rocked
for the companies for a while, because it meant that they could vaguely say “wow, AI is going to be so powerful” every so often and every member of the media would crap their pants and give them a headline. Every story was about how “today’s breakthroughs proved that tomorrow’s AI would be
even more powerful
,” which they loved because, well, it meant their companies would be even more valuable as a result, even if raising that valuation required intimidating people about the prospect of them losing their jobs, even if
the software itself didn’t really do what they were promising
(which didn’t matter to basically any journalist covering this field).
Their “powerful AI” — graded not based on actual outcomes but preferential anecdotes and performance on benchmarks rigged for the LLMs — was always “on the frontier” and “getting smarter every day,” all because AI labs and hyperscalers had intentionally sold their products based on some theoretical future version that would fix all the problems.
In other words, whatever they did was seen through the best light, described in the terms of the best parts of the present and the best promises of the future, and given credit as if it had already happened.
This is, as they’ve found, a double-edged sword. When journalists will believe (and print) whatever you say, they’ll start believing that the
real thing
(LLMs) does the same thing as the
imaginary future thing
(AGI, ASI,
golden egg-laying geese
), or will do so,
even if that thing is bad
.
These companies had spent years puffing up their LLMs’ potential using vague promises of superintelligence and theoretical model capabilities, at times inflating its capabilities further through scary quotes (
here’s a list of Altman’s!
),
intentionally training models to blackmail people
and
entirely-fictional stories about “breaking containment,”
and never realized that at any time one of the near-cultist types that joined their companies and heard everybody talking in terms of “
p(doom)
” (fuck off) could
take it all seriously
and
the media might believe them.
This puts the industry in an odd position.
While on one hand, Altman, Amodei, Musk, and the rest of them know that they can’t roll back the narrative and say “everyone, stop freaking out,
it’s fine, it’s just cloud software,”
they also know that they have to do
something
because everybody is
pissing their pants
, even if it’s about something that is only really scary as a direct result of their scaremongering.
I’ve already seen a good amount of AI boosters trying to rein in Jacob Coxon’s scaremongering, or suggest that everybody calms down and remembers that AI is the biggest thing on the stock market.
At this point, it would’ve been
really nice
if the industry was operating in lock-step, except, as ever, Sam Altman had to go and fuck everything up,
telling Fortune the following when asked whether pauses would cost the company a lot of money:
I’d [gladly go in front of my staff and investors and say] I am sorry. We, like, told you all along this moment might happen. We're still going to try to figure out a way to make you a bunch of money in the future.
This is a very, very worrying thing for Altman to say given that
OpenAI has projected to spend $750 billion or more
in the next three years across compute contracts with Microsoft, Google, Amazon, CoreWeave, Cerebras and other providers.
In fact, the very
concept
of a slowdown runs contrary to everything that the AI industry needs. If
NVIDIA is to sell $670 billion or more GPUs in Fiscal Year 2028
or, per analyst expectations,
Anthropic and OpenAI are to spend more than $444 across Google, Microsoft and Amazon in the next three years
, or
Broadcom is to sell nearly $600 billion in AI chips in the next three years
,
both Anthropic and OpenAI must keep and make their $1.3 trillion in compute commitments
and support the development of 10GW or more of capacity, all of which requires them to
continue accelerating at a dramatic pace.
Softbank
just raised $11.87bn in debt from around twenty banks
— all to support its investment in OpenAI, and more than its target of $10bn — and that wouldn’t be possible if the model labs had collectively decided to temper the pace of model development.
There is no way a “slow down” actually gels with the overall narrative of AI’s rapacious growth.
As Anthropic and OpenAI represent 70% of hyperscalers’ AI revenues
, there really is no fallback plan — there are no other customers who will naturally fill out the hundreds of billions of dollars’ worth of infrastructure, no other uses for the hundreds of thousands of GPUs bought from NVIDIA outside of generative AI, no ways in which we can simply “use the models we’ve got forever” without inherently accepting the limitations (and unsustainable costs) of running LLMs.
A pause could, in theory, mean that AI labs could slash their worst expense — training costs. While this might have the short-term benefit of reducing costs (and maybe even, with the right amount of accounting shenanigans, eek out a razor-thin positive margin), it’s likely that Chinese open source developers would distill (
as they have been
) Western models, create a much cheaper and “good enough” model to compete, and their “lead” in a race where everybody loses money would deteriorate.
Even then, what
are
OpenAI or Anthropic if they’re not cranking out some new version of a model or creating some vague sense of virality about the next one? What possible use is an Altman or Amodei if they’re not always on the phone to somebody
signing hundreds of billions of dollars of compute contracts
or promising some journalist-adjacent homunculus that
Anthropic is going to cure cancer
?
What
is
the LLM industry without a series of promises that extend infinitely into the future? What
is
Anthropic or OpenAI without the suggestion that it might be something completely different in an ever-distant future?
It isn’t clear, but what
is
clear is that a “slow down” does not gel with “insatiable demands for compute” or somehow being able to pay more in operating expenses in a year than
Microsoft
or
Meta
.
There’s also the very reasonable question of
what happens to SoftBank if OpenAI can’t go public
, which is now a very real possibility. With over $40 billion of debt due to be refinanced this year at a time of skyrocketing interest rates, it’s probably the single-worst time in history for it to be doing
a $20 billion bond sale
(separate from the aforementioned $11.87bn bank loan), which is why I think things are getting a little tight.
What Happens Next?
You’ll notice I’m a little light on predictions, and that’s because everything is a little
volatile
right now. Nobody has really committed to an actual
slowdown
beyond vague suggestions of an “independent” authority that would look at models and do something or rather, and based on what Amodei has said, it’s clear that a “pausing” really just means “saying we’ll take a little more time but not really change how we’re doing business.”
Alternatively, I’m dead wrong, and this is a moment of actual change caused by a runaway narrative years in the making. By deliberately misleading the media and the general public about the current and future capabilities of Large Language Models as means of inflating their valuations and justifying massive expansion of AI compute capacity, the labs made a sales pitch driven by scaring people into submission, assuming, like they do with their technology, that they had complete control over the situation.
As it stands, a slowdown is deeply impractical due to the massive commitments. As OpenAI and Anthropic make up the vast majority of AI compute demand, any contraction of that demand would mean material restatements of revenue (and
the $748 billion in revenue backlogs
) across every hyperscaler, along with the neoclouds and any other counterparty. The AI industry’s entire pitch to investors has been that
all of these GPUs would be used and then some
and that we
needed to build all this capacity to reach the heights of AI breakthroughs
, and while it was already questionable whether or not we needed that capacity, we certainly don’t if we’re “slowing down.”
And I must be clear, AI cannot “slow down” without creating some kind of serious financial crisis within the tech industry. Hundreds of billions of dollars’ worth of hyperscaler revenues and data center capacity is tied up in the idea that demand for it actually exists, and if the two companies with the most demand suddenly need to slow their roll, it’s hard to see how the capacity gets used.
Worse still, we’re most decidedly
not
done issuing debt for AI data centers — and I don’t see how anyone hearing about some kind of “AI slowdown” (real or imagined) feels particularly confident in backing a data center, considering investors barely understood what they were investing in to begin with.
The fact that Anthropic is going full steam ahead with its IPO is a sign that it doesn’t really care about slowing down, but all of this talk about “AI dangers” — even as we fail to deal with a single one of them — is enough to rattle an already-nervous market about the future growth trajectory of a company where people keep leaving and saying “it’s gonna kill us all!”
Some are arguing that the “slowdown” talk is a way to unwind the AI trade — to give AI labs a way out of their $1.3 trillion in commitments — and while it may or may not work out that way, I think it’s far simpler: the AI industry is run by a series of different entities with deeply cynical and selfish beliefs, all operating “in sync” only so far as it benefits ideologies and intentions that change on a daily basis.
Sadly, in the end, none of this is about actually fixing or mitigating the harms of Large Language Models, or holding those who have perpetuated those harms responsible.
What it may do — though I’m not getting my hopes up prematurely — is lead to the unwinding of the AI trade as reality slams head-first into the scaremongering overpromises of some of the least-trustworthy and most-craven executives in the history of society. Perhaps it’s a way that these massive cloud compute contracts could be canceled, or a way to reduce these labs in size. It may also serve as a convenient way to avoid admitting that they’re running out of things that LLMs can do that approximate a product or even the completion of a task.
Alternatively, it could just be another brief moment in the history of a bubble inflated by its misinformation and a media ecosystem dedicated to spreading it.
The Hugging Face attack and any other “hacking incidents” are a result of poorly-run AI labs training volatile neural networks bankrolled by and run on infrastructure owned by the richest and most-powerful companies in the world. Every attempt to focus this conversation on “what AI is doing” or “what AI could do” deliberately or otherwise separates us from the grim truth that we need to start arresting people for committing crimes, halting any and all training runs, and putting real safeguards on this technology — not because it’s all-powerful, sentient, conscious, or even “innovative,” but because it’s clear that the people running these labs are irresponsible and the people backing them don’t give a shit.
There are, however, things we can do, per
former FTC Chair Lina Khan
, if we actually had any interest in doing so:
There is an extensive set of laws that govern dangerous and defective products. For example, releasing unvetted AI models or agents can violate consumer protection laws. Shipping flawed AI tools without implementing adequate measures to detect and stop rogue or defective AI agents can be an “unfair or deceptive” act or practice under the FTC Act (and analogous state laws). And some state AGs are already exploring holding AI firms and their CEOs criminally liable when their models participate in criminal activity.
If LLMs were a toy, they’d be taken off the shelves. If LLMs were a drug, they would be banned.
I agree that we need to take “AI safety” seriously, but that starts with treating LLMs as normal software run in a reckless and dangerous manner by malevolent entities with little regard for society.
If you liked this piece, you should subscribe to my premium newsletter. It’s
$70 a year
,
$18 a quarter
, or
$7 a month
, and in return you get a weekly newsletter that’s usually anywhere from 10,000 to 18,000 words and provides vast, detailed analyses of the biggest events and companies in the AI bubble.
If you want to get in touch — and especially if you have any juicy information about Anthropic, OpenAI, or any other companies in the AI bubble — hit me up on Signal at ezitron.76. I’m also on IB on The Terminal.
