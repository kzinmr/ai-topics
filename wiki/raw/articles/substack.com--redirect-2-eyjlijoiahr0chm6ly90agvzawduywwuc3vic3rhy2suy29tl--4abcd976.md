---
title: "Anthropic's Big Swing, Gemini Everywhere All at Once, and OpenAI's Shape-Shift"
url: "https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly90aGVzaWduYWwuc3Vic3RhY2suY29tL3AvYW50aHJvcGljcy1iaWctc3dpbmctZ2VtaW5pLWV2ZXJ5d2hlcmU_dXRtX2NhbXBhaWduPWVtYWlsLWhhbGYtcG9zdCZyPTJmbHg2JnRva2VuPWV5SjFjMlZ5WDJsa0lqbzBNRGczTkRneUxDSndiM04wWDJsa0lqb3hPVFEyT0RBNU1URXNJbWxoZENJNk1UYzNOall3TkRBeE5Dd2laWGh3SWpveE56YzVNVGsyTURFMExDSnBjM01pT2lKd2RXSXRNamt6TVRVMElpd2ljM1ZpSWpvaWNHOXpkQzF5WldGamRHbHZiaUo5LldSSzZmMVZ1X18xT05rSGF2eGJDbXh0UHE3UE5TOGlqVTFfUjVJcVllVEEiLCJwIjoxOTQ2ODA5MTEsInMiOjI5MzE1NCwiZiI6dHJ1ZSwidSI6NDA4NzQ4MiwiaWF0IjoxNzc2NjA0MDE0LCJleHAiOjIwOTIxODAwMTQsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.QZ9lDJM3nMmK0Ci0TJ0-jZLpaevEkIDvWN4JsgqyYfU?"
fetched_at: 2026-04-19T13:07:04.031655+00:00
source_date: 2026-04-19
tags: [newsletter, auto-ingested]
---

# Anthropic's Big Swing, Gemini Everywhere All at Once, and OpenAI's Shape-Shift

Source: https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly90aGVzaWduYWwuc3Vic3RhY2suY29tL3AvYW50aHJvcGljcy1iaWctc3dpbmctZ2VtaW5pLWV2ZXJ5d2hlcmU_dXRtX2NhbXBhaWduPWVtYWlsLWhhbGYtcG9zdCZyPTJmbHg2JnRva2VuPWV5SjFjMlZ5WDJsa0lqbzBNRGczTkRneUxDSndiM04wWDJsa0lqb3hPVFEyT0RBNU1URXNJbWxoZENJNk1UYzNOall3TkRBeE5Dd2laWGh3SWpveE56YzVNVGsyTURFMExDSnBjM01pT2lKd2RXSXRNamt6TVRVMElpd2ljM1ZpSWpvaWNHOXpkQzF5WldGamRHbHZiaUo5LldSSzZmMVZ1X18xT05rSGF2eGJDbXh0UHE3UE5TOGlqVTFfUjVJcVllVEEiLCJwIjoxOTQ2ODA5MTEsInMiOjI5MzE1NCwiZiI6dHJ1ZSwidSI6NDA4NzQ4MiwiaWF0IjoxNzc2NjA0MDE0LCJleHAiOjIwOTIxODAwMTQsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.QZ9lDJM3nMmK0Ci0TJ0-jZLpaevEkIDvWN4JsgqyYfU?

Hey friends 👋 Happy Sunday.
Here’s your weekly dose of AI and insight.
Every Wednesday, Signal Pro members get a step-by-step AI workflow they can apply immediately. No fluff, just practical guides to upskill you and your team. If you’re only reading the Sunday issue, you’re getting half the picture. Upgrade to paid today.
Upgrade to paid
My top-3 picks of AI news this week.
Dario Amodei, CEO of Anthropic / Reuters/Denis Balibouse / The Signal Newsletter Graphic
Anthropic
Anthropic shipped four launches in four days, across a new frontier model, a design surface, automation in Claude Code, and Word integration for paying subscribers.
New frontier model:
Claude Opus 4.7
is now generally available, with Anthropic claiming stronger performance on long-running coding tasks, tighter instruction-following, and self-verification before reporting back.
Design and Word surfaces:
Claude Design
lets Pro, Max, Team, and Enterprise users build prototypes, slides, and one-pagers by describing what they want, while
Claude for Word
brings tracked-change editing inside Microsoft Word on Pro and Max plans.
Automation in Claude Code:
Routines
let developers package a prompt, a repo, and connectors into a saved configuration that runs on a schedule, via API call, or in response to GitHub events, all on Anthropic’s web infrastructure, so your laptop doesn’t need to stay open.
Alex’s take:
Opus 4.7 feels like the rebirth of Opus 4.6. What I'd love to see are benchmarks comparing 4.6 to 4.7 right before 4.7 was released, because Anthropic clearly
nerfed Opus 4.6 by 67%
as we explored last week. Two things are at play currently that my mind is on. Firstly, it's hard to trust benchmarks anymore because of overfitting to training data, so I generally ignore them and care far more about using the model for real work. Second, the internal model manipulation of reverting to “mid-level” thinking in effort to save on inference costs after the initial release creates a bind for users. Sure, from Anthropic’s position, there’s a clear incentive is to get as many people on the model as early as possible and build workflows around it, but that’s when regression begins. This is immediately noticeable and causes huge frustration, because there are little alternatives available. Anthropic has the best LLM on the market, and moving to OpenAI or Gemini carries enormous switching costs. Consumers are stuck and frustrated at the same time. What I'm more interested in this week is Claude for Word. Extending it to Pro and Max users is a massive unlock for inline edits as previously you had to generate an artifact in the desktop or web app and manually specify highlighted changes in the chat window, which was tedious. Claude is clearly building the ecosystem for work. It’s a bold position, but it’s working—and will continue to work as long as they prioritise building trust with users instead of silent model lobotomies.
Google
Google landed two Gemini launches with a new flagship text-to-speech model topping the leaderboard, and its first native Mac app built in a few days using Google’s own agentic coding tools.
Leaderboard win
:
Gemini 3.1 Flash TTS
ranks first on the Artificial Analysis TTS leaderboard with 200+ audio tags, scene direction, speaker-level controls, and support for 70+ languages, putting real pressure on ElevenLabs.
Scene direction
: You can now prompt tone, pace, accent, and emotion directly inside the text, moving TTS from reading a script to performing one, with
SynthID
watermarking baked into every output.
Catching up on the Mac
: The
native macOS app
brings Gemini to the desktop with Option + Space access, live screen sharing, and file context, arriving roughly two years after OpenAI and Anthropic shipped their own Mac apps.
Alex’s take:
OpenAI and Anthropic have had desktop apps for ages. Google is coming in with theirs almost two years after OpenAI shipped theirs—yet Sundar Pichai, Google CEO, highlighted they went from idea to prototype in a few days using Google’s own Antigravity agentic development platform. Was it because their focus was elsewhere, or because they wanted to prove their own internal tools were capable enough to build more internal tools? Regardless, you need both speed AND quality to compete, and the feedback (including mine) is mixed for the initial V1 of the desktop app.  I’m more interested in bringing Gemini Live to desktop, as this is my favourite feature of the Gemini mobile app and find it incredibly useful. However, perspective is everything. We’re still waiting for Apple Intelligence to turn Siri into something that feels like it belongs in this decade.
OpenAI
OpenAI introduced a major Codex overhaul that turns it into a full computer-use agent, and GPT-Rosalind, a frontier reasoning model built specifically for life sciences research.
Codex goes wide
: The
Codex desktop app
can now see your screen, click and type across Mac apps, run multiple agents in parallel, remember your preferences, generate images, and schedule recurring tasks across days or weeks.
GPT-Rosalind goes deep
: Named after Rosalind Franklin, this is the first release in a new
Life Sciences model
series, built for hypothesis generation, experimental planning, and multi-step research, already being tested by Amgen, Moderna, Thermo Fisher, and the Allen Institute.
Trusted access only
: GPT-Rosalind is locked behind a
vetting programme
for qualified US enterprise customers, with technical safeguards to flag misuse, a nod to the real biosecurity risks of putting a biology-tuned frontier model in more hands.
Alex’s take:
For years the story was one general model to rule them all. This week flips that. OpenAI is going horizontal and vertical at the same time with an agent that sits on your desktop and does the boring stuff, and a specialist that sits inside a pharma lab and reasons about protein structures. Are domain-specific models are the polar opposite of AGI? I think it’s the opposite. You get to AGI by being useful in the messy specifics first, and then zooming out. We’ll be watching this pattern repeat in law, finance, and engineering over the next 18 months.
Dwarkesh Patel and Jensen Huang / Dwarkesh Patel on X
Dwarkesh Patel sat down with Nvidia CEO Jensen Huang this week for an almost
two-hour interview
. What I liked about this conversation specifically was how Dwarkesh was willing to ask the hard questions and kept pressing when Jensen pushed back. This meant things really started to heat up around the 57-minute mark, on whether Nvidia should be selling AI chips to China.
Dwarkesh opened with Anthropic’s Mythos model, which found thousands of zero-days across every major operating system, including one that had sat undetected in OpenBSD for 27 years. Compute is the input to training and deploying models like that at scale. More chips for China means faster Chinese equivalents aimed at American infrastructure. So the question then is, why ship them?
Jensen’s counter leaned on what he called AI’s “five-layer cake”, with energy at the base, applications at the top, with chips, infrastructure, and models in between. China already has abundant energy, 50% of the world’s AI researchers, and a domestic chip industry where Huawei just posted a record year. Withholding Nvidia hardware doesn’t stop the capability from emerging. It
hands the ecosystem
to Huawei and forces Chinese open-source models to be co-designed for a non-American stack. “The day that DeepSeek comes out on Huawei first, that is a horrible outcome for our nation.”
Then Dwarkesh highlighted a quote from Dario Amodei’s
blog post
“The Adolescence of Technology”, published in January this year: “In my view, this is like selling nuclear weapons to North Korea and then bragging that the missile casings are made by Boeing and so the US is ‘winning.’” Jensen called the analogy lunacy. He accused Dwarkesh of arguing from extremes, called the framing childish, and
delivered the line
that’s been capturing the internet all week: “You’re not talking to somebody who woke up a loser.”
Dwarkesh’s whole case rests on a premise Jensen never directly addressed, but that is quietly eroding in the background: AI models stay portable across accelerators. Anthropic runs on GPUs, Trainium, and TPUs, so why wouldn’t Chinese labs do the same? But as the industry shifts from training to inference economics, models are increasingly co-designed for specific hardware topologies. If that trend continues, the question becomes which stack will the global south, the Middle East, and Southeast Asia end up running on?
Allbirds rebrand to NewBird AI / Spencer Platt via Getty Images
Allbirds rebranded as “NewBird AI” last Wednesday. The stock surged 582% in a single session, adding roughly $127 million to its market cap. Three weeks earlier, Allbirds had sold its actual shoe business to American Exchange Group for $39 million. What actually surged was a listing with a
press release
attached.
When you read the press release carefully, it highlights how NewBird AI “seeks to acquire” GPUs, not “will acquire.” Its plans to become a cloud provider are “long-term,” not short-term. The backing is $50 million from an undisclosed institutional investor, which is roughly what Amazon will spend on AI infrastructure every two hours this year. $50 million buys a handful of server racks.
History may not repeat itself, but it sure does rhyme.
In 1999, dozens of old-economy companies added “.com” to their names and watched their stocks jump, weeks before the market topped in March 2000. In 2017, Long Island Iced Tea renamed itself Long Blockchain Corp, and its stock jumped 500%, just before crypto peaked. Kodak tried the same playbook a year later. Each move landed within a month of the top. The day after Allbirds, a penny-stock social media company called Myseum added “AI” to its name. Shares jumped 130%.
Sure, the underlying AI investment cycle is very real. Nvidia booked $68 billion in revenue last quarter. Hyperscaler capex is running above $500 billion annually. But the same mechanism rewarding genuine compute buildouts is now paying out on rebrands with nothing behind them. Long Blockchain was delisted within months. Allbirds has already halved from its peak.
Demis Hassabis calling out the noise:
Demis Hassabis
@demishassabis
Maybe tell your buddy to do some actual work and to stop spreading absolute nonsense. This post is completely false and just pure clickbait.
1:42 AM · Apr 14, 2026
·
830K Views
296 Replies
·
458 Reposts
·
13K Likes
The post in question was from Steve Yegge, a former Googler who now works at Sourcegraph, which happens to sell a rival agentic coding product. His claim was that Google engineers have the same AI adoption curve as a tractor company, Claude Code is banned internally as “the enemy,” and Gemini has never been good enough for real agentic workflows.
Then, Demis stepped in to handle matters. Now he rarely gets into public scraps on X, but when the CEO of DeepMind takes the time to reply, something clearly crossed the line that he felt compelled to correct.
There’s a larger underlying problem here that I think is worth calling out. Hot takes are performing exceptionally well on X right now—this one in particular collected nearly 3M impressions. But people rarely check the narrative behind posts like this. The entire argument of this post rests on an anonymous friend at Google that nobody can verify.
Instead, they get sucked in by the drama and headlines and assume it’s gospel.
I’d argue we need more of this “sense checking” from AI leaders. Most stay quiet and let the narrative set itself. When Demis pushes back publicly on a specific claim, it pulls the conversation closer to the truth. We need more of it.
Source:
Demis Hassabis on X
“Every time I ask AI for business advice, I get recommendations that sound smart but feel generic. What's going on underneath?”
There’s a term worth knowing I want to bring to your attention: “trendslop.”
It describes what happens when AI defaults to buzzy, fashionable ideas over reasoned ones. Ask an LLM a serious strategic question, and you’ll often get back something that sounds smart but reads like an overly sanitised corporate-jargon-filled LinkedIn post.
A
recent HBR article
tested this directly. Researchers ran seven leading LLMs, including Claude, ChatGPT, Gemini, and Grok, across core strategic tensions. Across thousands of simulations, the models clustered tightly around the same trendy answers regardless of context.
ChatGPT kept steering users toward the same fashionable ideas, phrased to sound tailored, such as preferring to augment human work with AI rather than automate it and biasing toward long-term thinking, regardless of immediate urgency.
LLMs are trained on the internet, which produces far more content about “finding your unique value proposition” than case studies on supply chain efficiency. So the models absorb what sounds good in modern business discourse over what actually works in competitive markets. Hiring, positioning, product decisions, anything that requires a real trade-off gets shaped by the same pull.
Therefore, the answer lies in
how
we use these tools—we must use them differently.
As we explored this week in
the illusion of thinking
, LLMs are pattern matchers. They reflect what’s common across their training data rather than what’s right for your specific situation. Trendslop is that same pattern matching showing up in strategic advice.
AI is an incredible thinking partner, so we must treat it like one.
Ask the LLM to make the strongest case for the unfashionable option. Prompt it to surface companies that succeeded doing the opposite of what’s trendy. Steelman the case for and against your idea to make informed decisions.
These are the questions that matter, and they rely on good judgement and critical thought. That’s how you craft great outputs.
Already a subscriber? Get your whole team on board. Signal Pro group subscriptions give everyone access to weekly AI workflows and tutorials, practical upskilling that pays for itself. It’s the kind of thing L&D budgets were made for. Share this with your manager today.
Get a group subscription
💡 If you enjoyed this issue, share it with a friend.
Refer a friend
See you next week,
Alex Banks
P.S. This
Chinese humanoid robot
just shattered the world record for a half marathon. The way they
brought out the stretcher
had me in tears.
